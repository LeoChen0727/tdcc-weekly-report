from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path

import pytest

from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]


def pr_safe_authorization_payload(
    base_helper: bytes,
    current_helper: bytes,
    current_test: bytes,
    migration_id: str | None = None,
    authorized_paths: frozenset[str] | None = None,
    **overrides: str,
) -> bytes:
    migration_id = migration_id or inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID
    authorized_paths = authorized_paths or inventory.PR_SAFE_AUTHORIZED_STAGE1_PATHS
    row = {
        "migration_id": migration_id,
        "status": "preauthorized",
        "approval_reference": "user_authorized_stage0_test",
        "base_helper_sha256": inventory.canonical_blob_sha256(base_helper),
        "current_helper_sha256": inventory.canonical_blob_sha256(current_helper),
        "current_test_sha256": inventory.canonical_blob_sha256(current_test),
        "changed_paths": ";".join(
            sorted(authorized_paths)
        ),
    }
    row.update(overrides)
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=list(inventory.PR_SAFE_AUTHORIZATION_COLUMNS),
    )
    writer.writeheader()
    retained = [
        retained_row
        for retained_row in inventory.PR_SAFE_RETAINED_AUTHORIZATION_ROWS
        if retained_row["migration_id"] != migration_id
    ]
    if migration_id == inventory.PR_SAFE_SNAPSHOT_MIGRATION_ID:
        retained.extend(inventory.PR_SAFE_CONSUMED_AUTHORIZATION_ROWS)
    writer.writerows([*retained, row])
    return buffer.getvalue().encode("utf-8")


def test_repo_production_inventory_validator_passes() -> None:
    assert inventory.main() == 0


def test_pr_safe_base_audit_workflow_never_executes_pull_request_code() -> None:
    text = (
        ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW
    ).read_text(encoding="utf-8")

    assert "  pull_request_target:" in text
    assert "types: [opened, synchronize, reopened, edited]" in text
    assert f"name: {inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION}" in text
    assert inventory.PR_SAFE_REQUIRED_CHECK_CONTEXT != inventory.PR_SAFE_TARGET_SKIP_CHECK_NAME
    assert "name: pr-safe-base-audit-runner" in text
    assert "if: github.event_name == 'pull_request'" in text
    assert "github.event_name == 'pull_request_target' &&" in text
    assert "github.event.pull_request.base.ref == 'main' &&" in text
    assert (
        "github.event.pull_request.base.repo.full_name == github.repository" in text
    )
    assert (
        "group: individual-stock-pr-validation-${{ github.event_name }}-"
        "${{ github.event.pull_request.number }}" in text
    )
    assert "ref: ${{ github.event.pull_request.base.sha }}" in text
    assert "persist-credentials: false" in text
    assert "checks: write" not in text
    assert "statuses: write" not in text
    assert "actions/github-script" not in text
    assert "15368" not in text
    assert "base-owned-pr-safe-control-plane-migration" not in text
    assert 'refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF' in text
    assert 'test "$(git rev-parse \"$LOCAL_HEAD_REF\")" = "$HEAD_SHA"' in text
    assert "--validate-pr-safe-control-plane-migration" in text
    assert "--audit-manifest \"$AUDIT_MANIFEST\"" in text
    assert "--workflow-ref \"$GITHUB_WORKFLOW_REF\"" in text
    assert "--workflow-sha \"$GITHUB_WORKFLOW_SHA\"" in text


def test_pr_safe_base_audit_trigger_paths_cover_snapshot_stage_b() -> None:
    text = (ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    trigger_paths, errors = inventory.workflow_trigger_paths(
        text,
        "pull_request_target",
    )

    assert errors == []
    assert trigger_paths == tuple(sorted(inventory.PR_SAFE_ALL_AUTHORIZED_MIGRATION_PATHS))
    assert "--event-action \"${{ github.event.action }}\"" in text
    assert "--base-ref \"${{ github.event.pull_request.base.ref }}\"" in text
    assert (
        "--base-repository \"${{ github.event.pull_request.base.repo.full_name }}\""
        in text
    )
    assert (
        "--head-repository \"${{ github.event.pull_request.head.repo.full_name }}\""
        in text
    )
    assert inventory.PR_SAFE_CHECKOUT_ACTION in text
    assert inventory.PR_SAFE_SETUP_PYTHON_ACTION in text
    assert inventory.PR_SAFE_UPLOAD_ARTIFACT_ACTION in text
    assert inventory.workflow_action_uses(text) == (
        inventory.PR_SAFE_EXPECTED_ACTION_USES,
        [],
    )
    assert inventory.workflow_exact_mapping(
        text,
        "permissions",
        section_indent=0,
        entry_indent=2,
    ) == (inventory.PR_SAFE_READ_ONLY_PERMISSIONS, [])
    jobs = inventory.workflow_job_blocks(text)
    assert "    timeout-minutes: 30" in jobs["individual-stock-pr-validation"]
    audit_steps = inventory.workflow_step_blocks(jobs["pr-safe-base-audit-runner"])
    assert tuple(inventory.workflow_step_name(step) for step in audit_steps) == (
        inventory.PR_SAFE_AUDIT_STEP_NAMES
    )
    assert tuple(
        inventory.canonical_workflow_step_sha256(step) for step in audit_steps
    ) == inventory.PR_SAFE_AUDIT_STEP_SHA256
    assert inventory.workflow_exact_mapping(
        jobs["pr-safe-base-audit-runner"],
        "permissions",
        section_indent=4,
        entry_indent=6,
    ) == (inventory.PR_SAFE_READ_ONLY_PERMISSIONS, [])
    assert "actions/checkout@v6" not in text
    assert "actions/upload-artifact@v4" not in text
    assert inventory.workflow_trigger_paths(text, "pull_request_target") == (
        inventory.PR_SAFE_TRIGGER_PATHS,
        [],
    )
    assert "timeout-minutes: 10" in text
    assert 'manifest_name="$(basename "$AUDIT_MANIFEST")"' in text
    assert (
        '(cd "$manifest_dir" && sha256sum "$manifest_name" > '
        '"${manifest_name}.sha256")' in text
    )
    assert 'sha256sum "$AUDIT_MANIFEST"' not in text
    assert "pr-safe-control-plane-audit-${{ github.run_id }}-${{ github.run_attempt }}" in text
    assert "secrets." not in text
    assert "github.event.pull_request.head.ref" not in text
    assert "github.ref" not in text


def test_pr_safe_base_audit_artifact_contract_is_structurally_exact() -> None:
    text = (ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")

    assert inventory.validate_pr_safe_base_guard_workflow_text(text) == []

    mutations = (
        text.replace(
            inventory.PR_SAFE_UPLOAD_ARTIFACT_ACTION,
            "actions/upload-artifact@v4",
            1,
        ),
        text.replace(
            inventory.PR_SAFE_CHECKOUT_ACTION,
            "actions/checkout@v6",
            1,
        ),
        text.replace(
            inventory.PR_SAFE_SETUP_PYTHON_ACTION,
            "actions/setup-python@v6",
            1,
        ),
        text.replace(
            '      - "tests/test_repo_advanced_integrity_pr_safe.py"',
            '      - "tests/test_repo_advanced_integrity_pr_safe.py"\n'
            '      - "scripts/unexpected.py"',
            1,
        ),
        text.replace(
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256",
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256\n"
            "            ${{ runner.temp }}/unexpected-third-path.txt",
            1,
        ),
        text.replace(
            "      - name: Upload audit-only evidence\n        if: always()",
            "      - name: Upload audit-only evidence\n        if: success()",
            1,
        ),
        text.replace("    timeout-minutes: 10\n", "", 1),
        text.replace(
            'manifest_name="$(basename "$AUDIT_MANIFEST")"',
            'manifest_name="$AUDIT_MANIFEST"',
            1,
        ),
        text.replace(
            inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION,
            inventory.PR_SAFE_REQUIRED_CHECK_CONTEXT,
            1,
        ),
        text.replace("    timeout-minutes: 30\n", "", 1),
        text.replace(
            "permissions:\n  contents: read",
            "permissions:\n  contents: write",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: read\n      actions: write",
            1,
        ),
        text.replace(
            "      - name: Upload audit-only evidence",
            "      - name: Unexpected fifth action\n"
            "        uses: actions/cache@0000000000000000000000000000000000000000\n\n"
            "      - name: Upload audit-only evidence",
            1,
        ),
        text.replace(
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            "",
            1,
        ),
        text.replace(
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n"
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            1,
        ),
        text.replace(
            "permissions:\n  contents: read",
            "permissions:\n  contents: read\n  contents: read",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: write",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read\n\n    steps:",
            "    permissions:\n      contents: read\n"
            "    permissions:\n      contents: read\n\n    steps:",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: read\n      contents: read",
            1,
        ),
        text.replace(
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json\n",
            "",
            1,
        ),
        text.replace(
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256\n",
            "",
            1,
        ),
        text.replace(
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json\n",
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json\n"
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json\n",
            1,
        ),
        text.replace(
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256\n",
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256\n"
            "            ${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256\n",
            1,
        ),
    )
    for mutated in mutations:
        assert mutated != text
        assert inventory.validate_pr_safe_base_guard_workflow_text(mutated)


def test_pr_safe_audit_runner_rejects_step_or_head_execution_drift() -> None:
    text = (ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    audit_job = inventory.workflow_job_blocks(text)["pr-safe-base-audit-runner"]
    steps = inventory.workflow_step_blocks(audit_job)
    step_blob = "".join(steps)
    seventh_step = (
        "      - name: Unexpected seventh run step\n"
        "        run: echo unsafe\n\n"
    )

    mutations = (
        text.replace(step_blob, "".join(steps[:-1]) + seventh_step + steps[-1], 1),
        text.replace(step_blob, "".join(steps[:-1]), 1),
        text.replace(step_blob, "".join([steps[0], steps[0], *steps[1:]]), 1),
        text.replace(step_blob, "".join([steps[1], steps[0], *steps[2:]]), 1),
        text.replace(
            "      - name: Record audit manifest SHA-256",
            "      - name: Renamed audit manifest step",
            1,
        ),
        text.replace(
            '          git fetch --no-tags origin "+refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF"',
            '          git fetch --no-tags origin "+refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF"\n'
            '          git checkout "$LOCAL_HEAD_REF"',
            1,
        ),
        text.replace(
            '          git fetch --no-tags origin "+refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF"',
            '          git fetch --no-tags origin "+refs/pull/$PR_NUMBER/head:$LOCAL_HEAD_REF"\n'
            '          git switch --detach "$HEAD_SHA"',
            1,
        ),
        text.replace(
            '          test "$(git rev-parse "$LOCAL_HEAD_REF")" = "$HEAD_SHA"',
            '          test "$(git rev-parse "$LOCAL_HEAD_REF")" = "$HEAD_SHA"\n'
            '          git show "$LOCAL_HEAD_REF:scripts/untrusted.py" | python -',
            1,
        ),
        text.replace(
            "          PR_NUMBER: ${{ github.event.pull_request.number }}",
            "          PR_NUMBER: ${{ github.event.pull_request.number }}\n"
            "          UNTRUSTED: ${{ secrets.UNTRUSTED }}",
            1,
        ),
    )
    for mutated in mutations:
        assert mutated != text
        assert inventory.validate_pr_safe_base_guard_workflow_text(mutated)


def test_pr_safe_audit_runner_rejects_job_header_drift() -> None:
    text = (ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    audit_job = inventory.workflow_job_blocks(text)[inventory.PR_SAFE_AUDIT_JOB_NAME]
    header_sha256, header_errors = inventory.canonical_workflow_job_header_sha256(
        audit_job
    )

    assert header_errors == []
    assert header_sha256 == inventory.PR_SAFE_AUDIT_JOB_HEADER_SHA256
    assert inventory.workflow_job_scalar_values(audit_job, "name") == (
        inventory.PR_SAFE_AUDIT_JOB_NAME,
    )
    assert inventory.workflow_job_scalar_values(audit_job, "runs-on") == (
        inventory.PR_SAFE_AUDIT_JOB_RUNS_ON,
    )
    assert inventory.workflow_job_scalar_values(audit_job, "timeout-minutes") == (
        inventory.PR_SAFE_AUDIT_JOB_TIMEOUT_MINUTES,
    )
    assert inventory.workflow_job_multiline_block(audit_job, "if") == (
        inventory.PR_SAFE_AUDIT_JOB_IF_BLOCK,
        [],
    )

    exact_if = "\n".join(inventory.PR_SAFE_AUDIT_JOB_IF_BLOCK)
    mutations = (
        text.replace(
            "    name: pr-safe-base-audit-runner",
            "    # name: pr-safe-base-audit-runner\n"
            "    name: individual-stock-pr-validation",
            1,
        ),
        text.replace(
            "    name: pr-safe-base-audit-runner",
            "    name: pr-safe-base-audit-runner\n"
            "    name: individual-stock-pr-validation",
            1,
        ),
        text.replace(
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: ubuntu-latest",
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: self-hosted",
            1,
        ),
        text.replace(
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: ubuntu-latest",
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: ubuntu-latest\n    runs-on: self-hosted",
            1,
        ),
        text.replace(exact_if, "    if: always()", 1),
        text.replace(
            exact_if,
            exact_if.replace(
                "      github.event.pull_request.base.ref == 'main' &&\n",
                "",
            ),
            1,
        ),
        text.replace(
            exact_if,
            exact_if.replace(
                "      github.event.pull_request.base.repo.full_name == github.repository",
                "      true",
            ),
            1,
        ),
        text.replace(
            exact_if,
            "    # if: >-\n    if: always()",
            1,
        ),
        text.replace(exact_if, exact_if + "\n    if: always()", 1),
        text.replace(
            "    timeout-minutes: 10",
            "    timeout-minutes: 10\n    timeout-minutes: 999",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read\n\n    steps:",
            "    permissions:\n      contents: read\n    environment: unexpected\n\n    steps:",
            1,
        ),
    )
    for mutated in mutations:
        assert mutated != text
        assert inventory.validate_pr_safe_base_guard_workflow_text(mutated)


def test_pr_safe_base_guard_concurrency_isolated_per_event_and_pull_request() -> None:
    text = (ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    group_line = next(
        line.strip() for line in text.splitlines() if line.strip().startswith("group:")
    )

    assert "${{ github.event_name }}" in group_line
    assert "${{ github.event.pull_request.number }}" in group_line
    assert "github.ref" not in group_line
    rendered_pr_101 = group_line.replace("${{ github.event.pull_request.number }}", "101")
    rendered_pr_202 = group_line.replace("${{ github.event.pull_request.number }}", "202")
    assert rendered_pr_101 != rendered_pr_202


def test_pr_safe_base_guard_accepts_only_exact_preauthorized_helper_bytes() -> None:
    base_helper = b"base helper without consumed migration\n"
    current_helper = (
        f"MIGRATION = '{inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID}'\n"
    ).encode("utf-8")
    current_test = b"def test_fail_closed():\n    assert True\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
    )

    errors = inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_AUTHORIZED_STAGE1_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )

    assert errors == []


def test_pr_safe_base_guard_rejects_tampered_retained_authorization() -> None:
    base_helper = b"base helper without consumed migration\n"
    current_helper = (
        f"MIGRATION = '{inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID}'\n"
    ).encode("utf-8")
    current_test = b"def test_fail_closed():\n    assert True\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
    ).replace(
        b"user_authorized_pr_safe_stage0_control_plane_trust_root_20260803",
        b"tampered_v1_history",
        1,
    )

    errors = inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_AUTHORIZED_STAGE1_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )

    assert (
        "PR-safe authorization history must retain the exact append-only prefix"
        in errors
    )


def test_pr_safe_base_guard_retains_exact_consumed_authorization_prefix() -> None:
    retained = [dict(row) for row in inventory.PR_SAFE_RETAINED_AUTHORIZATION_ROWS]
    assert [row["migration_id"] for row in retained] == [
        "additive-research-validation-registration-pr-safe-v1",
        "additive-research-validation-registration-pr-safe-v2",
    ]
    assert [
        row["migration_id"] for row in inventory.PR_SAFE_CONSUMED_AUTHORIZATION_ROWS
    ] == ["additive-research-validation-registration-pr-safe-v3"]

    tampered_v2 = [dict(row) for row in retained]
    tampered_v2[1]["current_test_sha256"] = "0" * 64
    invalid_histories = (
        retained[:1],
        tampered_v2,
        list(reversed(retained)),
    )
    for rows in invalid_histories:
        assert inventory.validate_pr_safe_authorization_history(rows) == [
            "PR-safe authorization history must retain the exact append-only prefix"
        ]


def test_snapshot_pr_safe_preauthorization_ledger_pins_exact_stage_b_bytes() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)

    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"] == inventory.PR_SAFE_SNAPSHOT_MIGRATION_ID
    ]
    assert matching == [
        {
            "migration_id": inventory.PR_SAFE_SNAPSHOT_MIGRATION_ID,
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_daily_full_checkpoint_replay_snapshot_stage_a_20260808"
            ),
            "base_helper_sha256": inventory.PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256,
            "current_helper_sha256": inventory.PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256,
            "current_test_sha256": inventory.PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256,
            "changed_paths": ";".join(
                sorted(inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS)
            ),
        }
    ]
    assert inventory.PR_SAFE_SNAPSHOT_BASE_CONTENT_REF_SHA == (
        "6a37e30797006397146bdbc6d29c51560c48ef9a"
    )
    assert inventory.PR_SAFE_SNAPSHOT_REQUIRED_MODE == "100644"


def test_snapshot_pr_safe_guard_accepts_only_exact_pinned_blobs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_helper = b"snapshot base helper\n"
    base_test = b"snapshot base tests\n"
    current_helper = b"snapshot helper delegates to base guard\n"
    current_test = b"snapshot helper delegation regression\n"
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256",
        inventory.canonical_blob_sha256(base_helper),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_BASE_TEST_SHA256",
        inventory.canonical_blob_sha256(base_test),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256",
        inventory.canonical_blob_sha256(current_helper),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256",
        inventory.canonical_blob_sha256(current_test),
    )
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_SNAPSHOT_MIGRATION_ID,
        authorized_paths=inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
    )

    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS),
        base_helper=base_helper,
        base_test=base_test,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    ) == []

    mutation_cases = (
        (base_helper + b"drift", base_test, current_helper, current_test),
        (base_helper, base_test + b"drift", current_helper, current_test),
        (base_helper, base_test, current_helper + b"drift", current_test),
        (base_helper, base_test, current_helper, current_test + b"drift"),
    )
    for mutated_base_helper, mutated_base_test, mutated_helper, mutated_test in mutation_cases:
        assert inventory.validate_pr_safe_control_plane_delta(
            set(inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS),
            base_helper=mutated_base_helper,
            base_test=mutated_base_test,
            current_helper=mutated_helper,
            current_test=mutated_test,
            authorization_payload=payload,
        )


def test_snapshot_pr_safe_guard_rejects_extra_path() -> None:
    errors = inventory.validate_pr_safe_control_plane_delta(
        {*inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS, "scripts/unapproved.py"},
        base_helper=b"base\n",
        base_test=b"base test\n",
        current_helper=b"current\n",
        current_test=b"current test\n",
        authorization_payload=(ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes(),
    )

    assert any("must change exactly the preauthorized paths" in error for error in errors)


def test_snapshot_pr_safe_guard_requires_exact_regular_blob_mode(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    unsafe_path = inventory.PR_SAFE_SNAPSHOT_HELPER

    def fake_git_tree_entry_at_ref(ref: str, path: str) -> tuple[str, str, str, str]:
        mode = "100755" if ref == "head-sha" and path == unsafe_path else "100644"
        return mode, "blob", "0" * 40, path

    monkeypatch.setattr(
        inventory,
        "git_tree_entry_at_ref",
        fake_git_tree_entry_at_ref,
    )

    errors = inventory.validate_pr_safe_exact_migration_blob_modes(
        set(inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS),
        "base-sha",
        "head-sha",
    )

    assert any(
        unsafe_path in error and "requires exact regular blob mode" in error
        for error in errors
    )


def test_snapshot_pr_safe_guard_does_not_authorize_mixed_migration_paths() -> None:
    mixed = {
        inventory.PR_SAFE_SNAPSHOT_HELPER,
        inventory.PR_SAFE_ADVANCED_TEST,
    }

    assert inventory.pr_safe_migration_contract_for_paths(mixed) is None


def test_snapshot_helper_self_migration_uses_exact_base_owned_contract(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_ref = "a" * 40
    base_helper = b"snapshot base helper\n"
    base_test = b"snapshot base tests\n"
    base_lifecycle_inventory = b"snapshot base lifecycle inventory\n"
    current_helper = b"snapshot helper delegates to base guard\n"
    current_test = b"snapshot helper delegation regression\n"
    current_lifecycle_inventory = b"snapshot current lifecycle inventory\n"
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_BASE_HELPER_SHA256",
        inventory.canonical_blob_sha256(base_helper),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_BASE_TEST_SHA256",
        inventory.canonical_blob_sha256(base_test),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_CURRENT_HELPER_SHA256",
        inventory.canonical_blob_sha256(current_helper),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_CURRENT_TEST_SHA256",
        inventory.canonical_blob_sha256(current_test),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_BASE_LIFECYCLE_INVENTORY_SHA256",
        inventory.canonical_blob_sha256(base_lifecycle_inventory),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_SNAPSHOT_CURRENT_LIFECYCLE_INVENTORY_SHA256",
        inventory.canonical_blob_sha256(current_lifecycle_inventory),
    )
    authorization_payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_SNAPSHOT_MIGRATION_ID,
        authorized_paths=inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS,
    )
    blobs = {
        (base_ref, inventory.PR_SAFE_AUTHORIZATION_PATH): authorization_payload,
        (base_ref, inventory.PR_SAFE_SNAPSHOT_HELPER): base_helper,
        (base_ref, inventory.PR_SAFE_SNAPSHOT_TEST): base_test,
        (
            base_ref,
            inventory.PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY,
        ): base_lifecycle_inventory,
        ("HEAD", inventory.PR_SAFE_SNAPSHOT_HELPER): current_helper,
        ("HEAD", inventory.PR_SAFE_SNAPSHOT_TEST): current_test,
        (
            "HEAD",
            inventory.PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY,
        ): current_lifecycle_inventory,
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: blobs.get((ref, path)),
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, _ref, path: (
            "100644" if path in inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS else None
        ),
    )
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(inventory.PR_SAFE_SNAPSHOT_AUTHORIZED_PATHS),
        "strict_surface_changes": set(inventory.PR_SAFE_SNAPSHOT_SELF_STRICT_SURFACES),
        "repository_root": tmp_path,
    }

    assert inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)
    blobs[("HEAD", inventory.PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY)] = (
        current_lifecycle_inventory + b"unexpected relation\n"
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)
    blobs[("HEAD", inventory.PR_SAFE_SNAPSHOT_LIFECYCLE_INVENTORY)] = (
        current_lifecycle_inventory
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{**kwargs, "strict_surface_changes": {inventory.PR_SAFE_SNAPSHOT_TEST}}
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{**kwargs, "changed_paths": {*kwargs["changed_paths"], "scripts/extra.py"}}
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{
            **kwargs,
            "changed_paths": {
                inventory.PR_SAFE_SNAPSHOT_HELPER,
                inventory.PR_SAFE_ADVANCED_TEST,
            },
        }
    )


def test_local_validation_replay_advanced_migration_contract_is_exact() -> None:
    paths = set(inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS)
    contract = inventory.pr_safe_migration_contract_for_paths(paths)
    assert contract == (
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID,
        inventory.PR_SAFE_ADVANCED_HELPER,
        inventory.PR_SAFE_ADVANCED_TEST,
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
    )
    assert inventory.pr_safe_migration_contract_for_paths(
        {*paths, "scripts/unapproved.py"}
    ) is None

    base_helper = b"base advanced helper\n"
    current_helper = (
        "current advanced helper\n"
        + inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID
        + "\n"
    ).encode("utf-8")
    current_test = b"current advanced test\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID,
        authorized_paths=inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS,
    )
    assert inventory.validate_pr_safe_control_plane_delta(
        paths,
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    ) == []
    assert inventory.validate_pr_safe_control_plane_delta(
        {*paths, "scripts/unapproved.py"},
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )


def test_daily_full_checkpoint_replay_preauthorization_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    lifecycle_path = "config/repo_file_lifecycle_inventory.csv"
    assert inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH[
        lifecycle_path
    ] == "69831c7ef8b922ddb763af94cbf4df694ee2d981c7a7d475567f67587ed07ce5"
    assert inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH[
        lifecycle_path
    ] == "adf32adc13882d556d2c54595ca49241df36f8c30e2528cb4f4411aad55974b5"
    base_ref = "a" * 40
    base_blobs: dict[str, bytes | None] = {}
    target_blobs: dict[str, bytes] = {}
    base_hashes: dict[str, str | None] = {}
    target_hashes: dict[str, str] = {}
    workflow_path = ".github/workflows/daily_full_pipeline.yml"
    anchor = inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_ANCHOR
    insertion = inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_WORKFLOW_INSERTION

    for path, expected_base_sha in (
        inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH.items()
    ):
        if expected_base_sha is None:
            base_blobs[path] = None
            base_hashes[path] = None
        elif path == workflow_path:
            base_blobs[path] = ("prefix\n" + anchor + "suffix\n").encode("utf-8")
            base_hashes[path] = inventory.canonical_blob_sha256(base_blobs[path] or b"")
        else:
            base_blobs[path] = f"base:{path}\n".encode("utf-8")
            base_hashes[path] = inventory.canonical_blob_sha256(base_blobs[path] or b"")
        if path == workflow_path:
            target_blobs[path] = (base_blobs[path] or b"").replace(
                anchor.encode("utf-8"),
                (insertion + anchor).encode("utf-8"),
                1,
            )
        else:
            target_blobs[path] = f"target:{path}\n".encode("utf-8")
        target_hashes[path] = inventory.canonical_blob_sha256(target_blobs[path])

    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: base_blobs[path] if ref == base_ref else target_blobs[path],
    )
    modes = {
        (ref, path): (
            None if ref == base_ref and base_blobs[path] is None else "100644"
        )
        for ref in (base_ref, "HEAD")
        for path in inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, ref, path: modes[(ref, path)],
    )

    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS),
        "strict_surface_changes": set(
            inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES
        ),
        "repository_root": tmp_path,
    }
    assert inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)

    mutated_path = "scripts/run_daily_full_validation_replay.py"
    original = target_blobs[mutated_path]
    target_blobs[mutated_path] = original + b"semantic drift\n"
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)
    target_blobs[mutated_path] = original

    modes[("HEAD", mutated_path)] = "100755"
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)
    modes[("HEAD", mutated_path)] = "100644"

    wrong_workflow = target_blobs[workflow_path].replace(
        b"retention-days: 30",
        b"retention-days: 31",
    )
    target_blobs[workflow_path] = wrong_workflow
    target_hashes[workflow_path] = inventory.canonical_blob_sha256(wrong_workflow)
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)

    target_blobs[workflow_path] = (base_blobs[workflow_path] or b"").replace(
        anchor.encode("utf-8"),
        (insertion + anchor).encode("utf-8"),
        1,
    )
    target_hashes[workflow_path] = inventory.canonical_blob_sha256(
        target_blobs[workflow_path]
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{**kwargs, "changed_paths": {*kwargs["changed_paths"], "scripts/extra.py"}}
    )


def test_local_validation_replay_routing_preauthorization_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_ref = "a" * 40
    base_blobs: dict[str, bytes | None] = {}
    target_blobs: dict[str, bytes] = {}
    base_hashes: dict[str, str | None] = {}
    target_hashes: dict[str, str] = {}
    for path, expected_base_sha in (
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH.items()
    ):
        if expected_base_sha is None:
            base_blobs[path] = None
            base_hashes[path] = None
        else:
            base_blobs[path] = f"base:{path}\n".encode("utf-8")
            base_hashes[path] = inventory.canonical_blob_sha256(
                base_blobs[path] or b""
            )
        target_blobs[path] = f"target:{path}\n".encode("utf-8")
        target_hashes[path] = inventory.canonical_blob_sha256(target_blobs[path])

    monkeypatch.setattr(
        inventory,
        "PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: (
            base_blobs[path] if ref == base_ref else target_blobs[path]
        ),
    )
    modes = {
        (ref, path): (
            None if ref == base_ref and base_blobs[path] is None else "100644"
        )
        for ref in (base_ref, "HEAD")
        for path in inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, ref, path: modes[(ref, path)],
    )
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(
            inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
        ),
        "strict_surface_changes": set(
            inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
        ),
        "repository_root": tmp_path,
    }

    assert inventory.is_preauthorized_daily_full_checkpoint_replay_migration(**kwargs)
    mutated_path = sorted(
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
    )[0]
    original = target_blobs[mutated_path]
    target_blobs[mutated_path] = original + b"semantic drift\n"
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **kwargs
    )
    target_blobs[mutated_path] = original
    modes[("HEAD", mutated_path)] = "100755"
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **kwargs
    )
    modes[("HEAD", mutated_path)] = "100644"
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{
            **kwargs,
            "strict_surface_changes": {
                *kwargs["strict_surface_changes"],
                "scripts/unapproved.py",
            },
        }
    )
    assert not inventory.is_preauthorized_daily_full_checkpoint_replay_migration(
        **{
            **kwargs,
            "changed_paths": {*kwargs["changed_paths"], "scripts/unapproved.py"},
        }
    )


def test_daily_full_checkpoint_replay_three_layer_lifecycle_reconciliation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fields = (
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
    )
    overlap_path = inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_OVERLAP_ROW

    def payload(rows: list[dict[str, str]]) -> bytes:
        output = io.StringIO(newline="")
        writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        return output.getvalue().encode("utf-8")

    base_overlap = {field: "" for field in fields}
    base_overlap.update(
        path=overlap_path,
        type="python",
        owner="repo_infrastructure",
        status="active",
        called_by_workflow="daily.yml",
        imported_by="snapshot.py",
        removal_risk="high",
    )
    stable_row = {field: "" for field in fields}
    stable_row.update(
        path="scripts/stable.py",
        type="python",
        owner="repo_infrastructure",
        status="active",
        removal_risk="low",
    )
    replay_row = {field: "" for field in fields}
    replay_row.update(
        path="scripts/replay.py",
        type="python",
        owner="repo_infrastructure",
        status="active",
        removal_risk="high",
    )
    stage_f_overlap = {**base_overlap, "imported_by": "snapshot.py;advanced.py"}
    replay_overlap = {**base_overlap, "called_by_workflow": "daily.yml;replay.yml"}
    pre_stage_f = payload([base_overlap, stable_row])
    stage_f = payload([stage_f_overlap, stable_row])
    replay_branch = payload([replay_overlap, stable_row, replay_row])
    expected = payload(
        [
            {
                **replay_overlap,
                "imported_by": "snapshot.py;advanced.py",
            },
            stable_row,
            replay_row,
        ]
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PRE_STAGE_F_LIFECYCLE_SHA256",
        inventory.canonical_blob_sha256(pre_stage_f),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STAGE_F_LIFECYCLE_SHA256",
        inventory.canonical_blob_sha256(stage_f),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_BRANCH_LIFECYCLE_SHA256",
        inventory.canonical_blob_sha256(replay_branch),
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_INTEGRATED_LIFECYCLE_SHA256",
        inventory.canonical_blob_sha256(expected),
    )

    assert (
        inventory.build_daily_full_checkpoint_replay_integrated_lifecycle_inventory(
            pre_stage_f,
            stage_f,
            replay_branch,
        )
        == expected
    )

    invalid_stage_f = payload(
        [
            {
                **stage_f_overlap,
                "called_by_workflow": "daily.yml;unapproved.yml",
            },
            stable_row,
        ]
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STAGE_F_LIFECYCLE_SHA256",
        inventory.canonical_blob_sha256(invalid_stage_f),
    )
    assert (
        inventory.build_daily_full_checkpoint_replay_integrated_lifecycle_inventory(
            pre_stage_f,
            invalid_stage_f,
            replay_branch,
        )
        is None
    )


def test_pr_safe_base_guard_rejects_helper_migration_with_extra_path() -> None:
    base_helper = b"base helper\n"
    current_helper = inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID.encode("utf-8")
    current_test = b"exact tests\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
    )
    changed_paths = {
        *inventory.PR_SAFE_AUTHORIZED_STAGE1_PATHS,
        "scripts/synthetic_daily_production.py",
    }

    errors = inventory.validate_pr_safe_control_plane_delta(
        changed_paths,
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )

    assert any("must change exactly the preauthorized paths" in error for error in errors)


def test_pr_safe_base_guard_rejects_unpinned_helper_semantic_mutation() -> None:
    base_helper = b"base helper\n"
    approved_helper = inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID.encode("utf-8")
    current_helper = approved_helper + b"\nUNAPPROVED = True\n"
    current_test = b"exact tests\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        approved_helper,
        current_test,
    )

    errors = inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_AUTHORIZED_STAGE1_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )

    assert "PR-safe migration authorization current_helper_sha256 mismatch" in errors


def test_pr_safe_advanced_lifecycle_preauthorization_is_exact() -> None:
    base_payload = b"base lifecycle inventory\n"
    current_payload = b"current lifecycle inventory\n"
    original_base = inventory.PR_SAFE_ADVANCED_BASE_LIFECYCLE_INVENTORY_SHA256
    original_current = inventory.PR_SAFE_ADVANCED_CURRENT_LIFECYCLE_INVENTORY_SHA256
    try:
        inventory.PR_SAFE_ADVANCED_BASE_LIFECYCLE_INVENTORY_SHA256 = (
            inventory.canonical_blob_sha256(base_payload)
        )
        inventory.PR_SAFE_ADVANCED_CURRENT_LIFECYCLE_INVENTORY_SHA256 = (
            inventory.canonical_blob_sha256(current_payload)
        )
        assert (
            inventory.validate_pr_safe_advanced_lifecycle_inventory_delta(
                base_payload,
                current_payload,
            )
            == []
        )
        assert inventory.validate_pr_safe_advanced_lifecycle_inventory_delta(
            base_payload,
            current_payload + b"unapproved drift\n",
        ) == ["advanced helper preauthorization current lifecycle SHA mismatch"]
    finally:
        inventory.PR_SAFE_ADVANCED_BASE_LIFECYCLE_INVENTORY_SHA256 = original_base
        inventory.PR_SAFE_ADVANCED_CURRENT_LIFECYCLE_INVENTORY_SHA256 = original_current


def test_input_bound_validator_lifecycle_preauthorization_is_exact() -> None:
    base_payload = b"input-bound base lifecycle inventory\n"
    current_payload = b"input-bound current lifecycle inventory\n"
    original_base = inventory.PR_SAFE_INPUT_BOUND_BASE_LIFECYCLE_INVENTORY_SHA256
    original_current = inventory.PR_SAFE_INPUT_BOUND_CURRENT_LIFECYCLE_INVENTORY_SHA256
    try:
        inventory.PR_SAFE_INPUT_BOUND_BASE_LIFECYCLE_INVENTORY_SHA256 = (
            inventory.canonical_blob_sha256(base_payload)
        )
        inventory.PR_SAFE_INPUT_BOUND_CURRENT_LIFECYCLE_INVENTORY_SHA256 = (
            inventory.canonical_blob_sha256(current_payload)
        )
        assert inventory.validate_pr_safe_input_bound_lifecycle_inventory_delta(
            base_payload,
            current_payload,
        ) == []
        assert inventory.validate_pr_safe_input_bound_lifecycle_inventory_delta(
            base_payload,
            current_payload + b"drift\n",
        ) == ["input-bound preauthorization current lifecycle SHA mismatch"]
    finally:
        inventory.PR_SAFE_INPUT_BOUND_BASE_LIFECYCLE_INVENTORY_SHA256 = original_base
        inventory.PR_SAFE_INPUT_BOUND_CURRENT_LIFECYCLE_INVENTORY_SHA256 = original_current


def test_pr_safe_base_guard_rejects_its_own_trust_root_changes() -> None:
    changed_paths = {inventory.PR_SAFE_BASE_GUARD_WORKFLOW}

    errors = inventory.validate_pr_safe_control_plane_delta(
        changed_paths,
        base_helper=None,
        current_helper=None,
        current_test=None,
        authorization_payload=(
            ",".join(inventory.PR_SAFE_AUTHORIZATION_COLUMNS) + "\n"
        ).encode("utf-8"),
    )

    assert any("may not modify the base-owned PR-safe trust root" in error for error in errors)


def test_pr_safe_base_guard_rejects_changed_workflow_spoof_surfaces() -> None:
    spoof_path = ".github/workflows/spoof.yml"
    payloads = (
        b"permissions:\n  checks: write\n",
        b"permissions: {statuses: write}\n",
        b"permissions: {'checks': 'write'}\n",
        b"permissions: write-all\n",
    )

    for payload in payloads:
        errors = inventory.validate_pr_safe_control_plane_delta(
            {spoof_path},
            base_helper=None,
            current_helper=None,
            current_test=None,
            authorization_payload=(
                ",".join(inventory.PR_SAFE_AUTHORIZATION_COLUMNS) + "\n"
            ).encode("utf-8"),
            changed_workflow_blobs={spoof_path: payload},
        )
        assert errors


def test_pr_safe_base_guard_allows_ordinary_non_control_plane_pr() -> None:
    errors = inventory.validate_pr_safe_control_plane_delta(
        {"docs/research-note.md"},
        base_helper=None,
        current_helper=None,
        current_test=None,
        authorization_payload=(
            ",".join(inventory.PR_SAFE_AUTHORIZATION_COLUMNS) + "\n"
        ).encode("utf-8"),
    )

    assert errors == []


def test_pr_safe_name_status_parser_keeps_type_change_and_both_rename_paths() -> None:
    payload = (
        b"T\0" + inventory.PR_SAFE_ADVANCED_HELPER.encode("utf-8") + b"\0"
        b"R100\0.github/workflows/individual_stock_pr_validation.yml\0"
        b".github/workflows/renamed_guard.yml\0"
    )

    paths, errors = inventory.parse_git_name_status_z(payload)

    assert errors == []
    assert paths == {
        inventory.PR_SAFE_ADVANCED_HELPER,
        ".github/workflows/individual_stock_pr_validation.yml",
        ".github/workflows/renamed_guard.yml",
    }
    guard_errors = inventory.validate_pr_safe_control_plane_delta(
        paths,
        base_helper=None,
        current_helper=None,
        current_test=None,
        authorization_payload=(
            ",".join(inventory.PR_SAFE_AUTHORIZATION_COLUMNS) + "\n"
        ).encode("utf-8"),
    )
    assert any("may not modify the base-owned PR-safe trust root" in error for error in guard_errors)


@pytest.mark.parametrize(
    ("unsafe_mode", "unsafe_type"),
    [
        ("120000", "blob"),
        ("160000", "commit"),
        ("100664", "blob"),
    ],
)
def test_pr_safe_regular_blob_gate_rejects_symlink_submodule_and_other_modes(
    monkeypatch: pytest.MonkeyPatch,
    unsafe_mode: str,
    unsafe_type: str,
) -> None:
    unsafe_path = inventory.PR_SAFE_ADVANCED_HELPER

    def fake_git_output_bytes(*args: str) -> bytes:
        assert args[:2] == ("ls-tree", "-z")
        ref = args[2]
        path = args[-1]
        mode = unsafe_mode if ref == "head-sha" and path == unsafe_path else "100644"
        object_type = (
            unsafe_type if ref == "head-sha" and path == unsafe_path else "blob"
        )
        return (
            f"{mode} {object_type} {'0' * 40}\t{path}\0"
        ).encode("utf-8")

    monkeypatch.setattr(inventory, "git_output_bytes", fake_git_output_bytes)

    errors = inventory.validate_pr_safe_regular_blob_modes("base-sha", "head-sha")

    assert any(
        unsafe_path in error and "must remain a regular blob" in error
        for error in errors
    )


def test_pr_safe_lifecycle_authorization_ledger_is_exact_and_base_owned() -> None:
    payload = (ROOT / inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH).read_bytes()

    rows, errors = inventory.parse_pr_safe_lifecycle_authorizations(payload)

    assert errors == []
    assert {
        (row["row_path"], row["column"])
        for row in rows
    } == inventory.PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS


def test_pr_safe_audit_manifest_pins_exact_evidence_without_trust_identity(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_sha = "a" * 40
    head_sha = "b" * 40
    base_helper = b"base helper without consumed migration\n"
    current_helper = (
        f"MIGRATION = '{inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID}'\n"
    ).encode("utf-8")
    current_test = b"def test_fail_closed():\n    assert True\n"
    authorization_payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
    )
    lifecycle_payload = (
        ROOT / inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH
    ).read_bytes()

    diff_payload = (
        f"M\0{inventory.PR_SAFE_ADVANCED_LIFECYCLE_INVENTORY}\0"
        f"M\0{inventory.PR_SAFE_ADVANCED_HELPER}\0"
        f"M\0{inventory.PR_SAFE_ADVANCED_TEST}\0"
    ).encode("utf-8")

    def fake_git_output_bytes(*args: str) -> bytes:
        if args[0] == "diff":
            return diff_payload
        if args == ("rev-parse", "HEAD"):
            return f"{base_sha}\n".encode("ascii")
        if args[:2] == ("ls-tree", "-z"):
            path = args[-1]
            return f"100644 blob {'0' * 40}\t{path}\0".encode("utf-8")
        raise AssertionError(args)

    def fake_git_blob_at_ref(ref: str, path: str) -> bytes | None:
        if ref == base_sha and path == inventory.PR_SAFE_AUTHORIZATION_PATH:
            return authorization_payload
        if ref == base_sha and path == inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH:
            return lifecycle_payload
        if path == inventory.PR_SAFE_ADVANCED_HELPER:
            return base_helper if ref == base_sha else current_helper
        if path == inventory.PR_SAFE_ADVANCED_TEST:
            return b"base tests\n" if ref == base_sha else current_test
        return b"base-owned audit blob\n"

    monkeypatch.setattr(inventory, "git_output_bytes", fake_git_output_bytes)
    monkeypatch.setattr(inventory, "git_blob_at_ref", fake_git_blob_at_ref)

    manifest = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=(
            f"{inventory.PR_SAFE_REPOSITORY}/"
            f"{inventory.PR_SAFE_BASE_GUARD_WORKFLOW}@refs/heads/main"
        ),
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="462",
    )

    assert manifest["audit_mode"] == inventory.PR_SAFE_AUDIT_MODE
    assert manifest["trust_identity_claimed"] is False
    assert manifest["required_context_used"] is False
    assert manifest["changed_paths_match_allowlist"] is True
    assert manifest["manual_gate_eligible"] is True
    assert manifest["validation"] == {"passed": True, "errors": []}
    assert manifest["preauthorization"]["migration"]["migration_id"] == (
        inventory.PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID
    )
    assert len(manifest["lifecycle_preauthorization"]["migrations"]) == 2
    helper_evidence = manifest["protected_blobs"][inventory.PR_SAFE_ADVANCED_HELPER]
    assert helper_evidence["base"]["object_id"] == "0" * 40
    assert helper_evidence["head"]["raw_sha256"] == hashlib.sha256(
        current_helper
    ).hexdigest()

    destination = tmp_path / inventory.PR_SAFE_AUDIT_MANIFEST_FILENAME
    observed_sha = inventory.write_pr_safe_audit_manifest(manifest, destination)
    assert observed_sha == hashlib.sha256(destination.read_bytes()).hexdigest()

    rejected = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=(
            f"{inventory.PR_SAFE_REPOSITORY}/"
            f"{inventory.PR_SAFE_BASE_GUARD_WORKFLOW}@refs/heads/main"
        ),
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="462",
    )
    assert rejected["validation"]["passed"] is False
    assert any(
        "event_name must be pull_request_target" in error
        for error in rejected["validation"]["errors"]
    )

    for bad_workflow_ref in (
        inventory.PR_SAFE_EXPECTED_WORKFLOW_REF.replace("refs/heads/main", "refs/heads/dev"),
        inventory.PR_SAFE_EXPECTED_WORKFLOW_REF.replace("refs/heads/main", "refs/tags/main"),
        inventory.PR_SAFE_EXPECTED_WORKFLOW_REF.replace("refs/heads/main", "refs/pull/462/merge"),
        inventory.PR_SAFE_EXPECTED_WORKFLOW_REF + "/extra",
    ):
        bad_ref_manifest = inventory.build_pr_safe_audit_manifest(
            base_sha=base_sha,
            head_sha=head_sha,
            validation_errors=[],
            repository=inventory.PR_SAFE_REPOSITORY,
            workflow_ref=bad_workflow_ref,
            workflow_sha=base_sha,
            run_id="12345",
            run_attempt="1",
            event_name="pull_request_target",
            event_action="synchronize",
            base_ref="main",
            base_repository=inventory.PR_SAFE_REPOSITORY,
            head_repository=inventory.PR_SAFE_REPOSITORY,
            pull_request_number="462",
        )
        assert bad_ref_manifest["manual_gate_eligible"] is False
        assert bad_ref_manifest["validation"]["passed"] is False

    rerun_manifest = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=inventory.PR_SAFE_EXPECTED_WORKFLOW_REF,
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="2",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="462",
    )
    assert rerun_manifest["manual_gate_eligible"] is False

    diff_payload = b"M\0docs/unrelated.md\0"
    unrelated_manifest = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=inventory.PR_SAFE_EXPECTED_WORKFLOW_REF,
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="462",
    )
    assert unrelated_manifest["changed_paths_match_allowlist"] is False
    assert unrelated_manifest["manual_gate_eligible"] is False
    assert unrelated_manifest["validation"]["passed"] is False


def test_pr_safe_base_audit_accepts_only_exact_daily_full_replay_target(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_sha = "a" * 40
    head_sha = "b" * 40
    diff_payload = b"".join(
        f"M\0{path}\0".encode("utf-8")
        for path in sorted(inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS)
    )
    authorization_payload = (
        ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH
    ).read_bytes()
    lifecycle_payload = (
        ROOT / inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH
    ).read_bytes()

    def fake_git_output_bytes(*args: str) -> bytes:
        if args[0] == "diff":
            return diff_payload
        if args == ("rev-parse", "HEAD"):
            return f"{base_sha}\n".encode("ascii")
        if args[:2] == ("ls-tree", "-z"):
            path = args[-1]
            return f"100644 blob {'0' * 40}\t{path}\0".encode("utf-8")
        raise AssertionError(args)

    def fake_git_blob_at_ref(ref: str, path: str) -> bytes | None:
        if ref == base_sha and path == inventory.PR_SAFE_AUTHORIZATION_PATH:
            return authorization_payload
        if ref == base_sha and path == inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH:
            return lifecycle_payload
        return f"{ref}:{path}\n".encode("utf-8")

    monkeypatch.setattr(inventory, "git_output_bytes", fake_git_output_bytes)
    monkeypatch.setattr(inventory, "git_blob_at_ref", fake_git_blob_at_ref)
    monkeypatch.setattr(
        inventory,
        "is_preauthorized_daily_full_checkpoint_replay_migration",
        lambda base_ref, changed_paths, strict_surfaces, **kwargs: (
            base_ref == base_sha
            and changed_paths
            == inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
            and strict_surfaces
            == inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES
            and kwargs["head_ref"] == head_sha
        ),
    )

    assert inventory.validate_pr_safe_control_plane_migration(base_sha, head_sha) == []
    manifest = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=inventory.PR_SAFE_EXPECTED_WORKFLOW_REF,
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="482",
    )

    assert manifest["validation"] == {"passed": True, "errors": []}
    assert manifest["manual_gate_eligible"] is True
    assert manifest["changed_paths_match_allowlist"] is True
    assert manifest["changed_path_allowlist"] == sorted(
        inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
    )
    assert manifest["replay_target_preauthorization"]["verified"] is True
    assert set(manifest["protected_blobs"]) >= (
        inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
    )

    monkeypatch.setattr(
        inventory,
        "is_preauthorized_daily_full_checkpoint_replay_migration",
        lambda *args, **kwargs: False,
    )
    rejected = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=inventory.PR_SAFE_EXPECTED_WORKFLOW_REF,
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="482",
    )
    assert rejected["manual_gate_eligible"] is False
    assert rejected["replay_target_preauthorization"]["verified"] is False


def test_local_validation_replay_routing_base_audit_is_exact(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_sha = "a" * 40
    head_sha = "b" * 40
    changed_paths = set(inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS)
    diff_payload = b"".join(
        (
            (b"A\0" if base_sha256 is None else b"M\0")
            + path.encode("utf-8")
            + b"\0"
        )
        for path, base_sha256 in sorted(
            inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_BASE_SHA256_BY_PATH.items()
        )
    )
    authorization_payload = (
        ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH
    ).read_bytes()
    lifecycle_payload = (
        ROOT / inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH
    ).read_bytes()

    def fake_git_output_bytes(*args: str) -> bytes:
        if args[0] == "diff":
            return diff_payload
        if args == ("rev-parse", "HEAD"):
            return f"{base_sha}\n".encode("ascii")
        raise AssertionError(args)

    def fake_git_blob_at_ref(ref: str, path: str) -> bytes | None:
        if ref == base_sha and path == inventory.PR_SAFE_AUTHORIZATION_PATH:
            return authorization_payload
        if ref == base_sha and path == inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH:
            return lifecycle_payload
        return f"{ref}:{path}\n".encode("utf-8")

    monkeypatch.setattr(inventory, "git_output_bytes", fake_git_output_bytes)
    monkeypatch.setattr(inventory, "git_blob_at_ref", fake_git_blob_at_ref)
    monkeypatch.setattr(
        inventory, "validate_pr_safe_regular_blob_modes", lambda *_args: []
    )
    monkeypatch.setattr(
        inventory, "validate_pr_safe_exact_migration_blob_modes", lambda *_args: []
    )
    monkeypatch.setattr(
        inventory,
        "is_preauthorized_daily_full_checkpoint_replay_migration",
        lambda base_ref, observed_paths, strict_surfaces, **kwargs: (
            base_ref == base_sha
            and observed_paths == changed_paths
            and strict_surfaces
            == inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
            and kwargs["head_ref"] == head_sha
        ),
    )
    monkeypatch.setattr(
        inventory,
        "git_tree_entry_at_ref",
        lambda _ref, path: ("100644", "blob", "0" * 40, path),
    )

    assert inventory.validate_pr_safe_control_plane_migration(base_sha, head_sha) == []
    manifest = inventory.build_pr_safe_audit_manifest(
        base_sha=base_sha,
        head_sha=head_sha,
        validation_errors=[],
        repository=inventory.PR_SAFE_REPOSITORY,
        workflow_ref=inventory.PR_SAFE_EXPECTED_WORKFLOW_REF,
        workflow_sha=base_sha,
        run_id="12345",
        run_attempt="1",
        event_name="pull_request_target",
        event_action="synchronize",
        base_ref="main",
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        pull_request_number="506",
    )
    assert manifest["validation"] == {"passed": True, "errors": []}
    assert manifest["changed_paths"] == sorted(changed_paths)
    assert manifest["changed_path_allowlist"] == sorted(changed_paths)
    assert manifest["changed_paths_match_allowlist"] is True
    assert manifest["manual_gate_eligible"] is True
    target = manifest["replay_target_preauthorization"]
    assert target["target_id"] == (
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID
    )
    assert target["strict_surfaces"] == sorted(
        inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
    )
    assert target["verified"] is True


def test_inventory_manifest_exists_and_is_authoritative() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    docs = ROOT / "docs" / "repo_production_inventory.md"

    assert manifest.exists()
    assert docs.exists()
    assert "config/repo_production_inventory.csv" in docs.read_text(encoding="utf-8")
    assert "tests/**/*.py" in docs.read_text(encoding="utf-8")
    assert "executable_script" in docs.read_text(encoding="utf-8")


def test_daily_full_replay_reconciled_target_hashes_are_exact() -> None:
    import hashlib
    import json

    target = inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH
    updated = {
        "scripts/run_daily_full_validation_replay.py": (
            "94707cb4029487f3c119970c7ef2a2476442e7926a70a20f0d8dcede9b602703"
        ),
        "scripts/validate_daily_full_validation_replay.py": (
            "4ec1e81b5781c91d0f0b0a9eec754f29c125c79b4e6c20e04e4474a1fe69ec3b"
        ),
        "tests/test_daily_full_validation_replay.py": (
            "b2e5f48050a7d14b964348511655e1e1e2ef89e11899fe2715945d4fe47a3ee7"
        ),
    }
    assert {path: target[path] for path in updated} == updated
    unchanged = sorted(
        (path, sha256)
        for path, sha256 in target.items()
        if path not in updated
        and path != inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_PATH
    )
    assert len(target) == 9
    assert hashlib.sha256(
        json.dumps(
            unchanged,
            ensure_ascii=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest() == (
        "f9572ab03922e38a239bbadb9347cc1a031f186ae94e952698d1194d1d2e9138"
    )


def test_daily_full_replay_hash_reconciliation_authorization_is_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == "daily-full-checkpoint-replay-target-hash-reconciliation-v2"
    ]
    assert matching == [
        {
            "migration_id": (
                "daily-full-checkpoint-replay-target-hash-reconciliation-v2"
            ),
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_daily_full_replay_hash_reconciliation_20260808"
            ),
            "base_helper_sha256": (
                "5f944d349cac77f6726ac6fcc13d6d8eee2196b6ad9a8bc5756a67ff04abf460"
            ),
            "current_helper_sha256": (
                "6ef1cfa402322114c8b9770f02584af1b208048fff2d550e24c1133e41235eeb"
            ),
            "current_test_sha256": (
                "0c97991722990b3378d5c87ac996ab2270072dc6f56ce0d4f543922da387e64d"
            ),
            "changed_paths": (
                "config/daily_model_pr_safe_self_migration_authorizations.csv;"
                "scripts/validate_repo_production_inventory.py;"
                "tests/test_repo_production_inventory.py"
            ),
        }
    ]


def test_daily_full_replay_lifecycle_target_hash_is_exact() -> None:
    target = inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_TARGET_SHA256_BY_PATH
    assert target[
        inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_LIFECYCLE_PATH
    ] == "adf32adc13882d556d2c54595ca49241df36f8c30e2528cb4f4411aad55974b5"


def test_daily_full_replay_lifecycle_hash_authorization_is_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == "daily-full-checkpoint-replay-lifecycle-target-reconciliation-v3"
    ]
    assert matching == [
        {
            "migration_id": (
                "daily-full-checkpoint-replay-lifecycle-target-reconciliation-v3"
            ),
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_daily_full_replay_lifecycle_reconciliation_20260808"
            ),
            "base_helper_sha256": (
                "6ef1cfa402322114c8b9770f02584af1b208048fff2d550e24c1133e41235eeb"
            ),
            "current_helper_sha256": (
                "64052ce22886dd649554a9567d760da44bf8ab97e2f8ffc413132a4ebc96a92f"
            ),
            "current_test_sha256": (
                "e463927104a978cebdb70986108ed55d76049ea27a119b4f35ffb3daa637649c"
            ),
            "changed_paths": (
                "config/daily_model_pr_safe_self_migration_authorizations.csv;"
                "scripts/validate_repo_production_inventory.py;"
                "tests/test_repo_production_inventory.py"
            ),
        }
    ]


def test_local_validation_replay_routing_authorization_is_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID
    ]
    assert matching == [
        {
            "migration_id": (
                inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_TARGET_ID
            ),
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_local_validation_replay_portable_ci_reconciliation_20260810"
            ),
            "base_helper_sha256": (
                "d415db1eb2433f2bda00d204ca55575a61aa57b326c8db6a938294611dd81ed0"
            ),
            "current_helper_sha256": (
                "20cfc385916432d0a4cf82094270a7bbd41d901aa07a7586bbf88894540bfe90"
            ),
            "current_test_sha256": (
                "7ea9abd8f9c0d6b5907d9dd5109e36d1cddc86bc3ce6e4f270c51e952397890d"
            ),
            "changed_paths": (
                "config/daily_model_pr_safe_self_migration_authorizations.csv;"
                "scripts/validate_repo_production_inventory.py;"
                "tests/test_repo_production_inventory.py"
            ),
        }
    ]


def test_local_validation_replay_advanced_v1_authorization_is_retained() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == "local-validation-replay-advanced-integrity-pr-safe-v1"
    ]
    assert matching == [
        {
            "migration_id": "local-validation-replay-advanced-integrity-pr-safe-v1",
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_local_validation_replay_advanced_pr_safe_20260810"
            ),
            "base_helper_sha256": (
                "4838bf1976c54cd5170d7dc5017127e7c88eee432629ad8703f1e612b2bb48ea"
            ),
            "current_helper_sha256": (
                "985ec761f31a7a4f9e19fd0419f1c9091deaac6afc9ed2863c76b6d700a271cd"
            ),
            "current_test_sha256": (
                "9d510aebede19de7347ca09ea84f9ea28e687ebbe3a381bea7fdb8ad248a89fd"
            ),
            "changed_paths": ";".join(
                sorted(inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS)
            ),
        }
    ]


def test_local_validation_replay_routing_v1_authorization_is_retained() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"] == "local-validation-replay-f-routing-20260810-v1"
    ]
    assert len(matching) == 1
    assert matching[0]["status"] == "preauthorized"
    assert matching[0]["approval_reference"] == (
        "user_authorized_local_validation_replay_f_routing_20260810"
    )


def test_local_validation_replay_advanced_v2_authorization_is_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID
    ]
    assert matching == [
        {
            "migration_id": (
                inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_MIGRATION_ID
            ),
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_local_validation_replay_advanced_pr_safe_v2_20260810"
            ),
            "base_helper_sha256": (
                "4838bf1976c54cd5170d7dc5017127e7c88eee432629ad8703f1e612b2bb48ea"
            ),
            "current_helper_sha256": (
                "02f28d28e7214e1949b2e8fa4aa6ad9df3b39c90bbe11534e0c5c24f350a7b3a"
            ),
            "current_test_sha256": (
                "d26afe8ef1cfb0cc943f4ed82652d0e3784075a86c8329626386677308d03d73"
            ),
            "changed_paths": ";".join(
                sorted(inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ADVANCED_PATHS)
            ),
        }
    ]


def test_local_validation_replay_hash_reconciliation_authorization_is_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    matching = [
        row
        for row in rows
        if row["migration_id"]
        == "local-validation-replay-f-routing-hash-reconciliation-v2"
    ]
    assert matching == [
        {
            "migration_id": (
                "local-validation-replay-f-routing-hash-reconciliation-v2"
            ),
            "status": "preauthorized",
            "approval_reference": (
                "user_authorized_local_validation_replay_hash_reconciliation_20260810"
            ),
            "base_helper_sha256": (
                "395680f68487f0836db8aac9662bf6bd6cd8d79b15e2271ef37ab28d210f544c"
            ),
            "current_helper_sha256": (
                "d415db1eb2433f2bda00d204ca55575a61aa57b326c8db6a938294611dd81ed0"
            ),
            "current_test_sha256": (
                "ff09926d02a76e059e0ca79af9ef6a749207419ef1e0f01b09b6952ee7772c2a"
            ),
            "changed_paths": (
                "config/daily_model_pr_safe_self_migration_authorizations.csv;"
                "scripts/validate_repo_production_inventory.py;"
                "tests/test_repo_production_inventory.py"
            ),
        }
    ]


def test_input_bound_validator_stage_a_preauthorizations_are_exact() -> None:
    payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    rows, errors = inventory.parse_pr_safe_authorizations(payload)
    assert errors == []
    assert [row["migration_id"] for row in rows[-6:]] == [
        inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
        inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_STAGE_A_MIGRATION_ID,
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID,
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID,
        inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID,
        inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID,
    ]
    rows_by_id = {row["migration_id"]: row for row in rows}
    assert rows_by_id[inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID] == {
        "migration_id": inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_input_bound_validator_pr_safe_stage_a_20260811"
        ),
        "base_helper_sha256": (
            "02f28d28e7214e1949b2e8fa4aa6ad9df3b39c90bbe11534e0c5c24f350a7b3a"
        ),
        "current_helper_sha256": (
            "480e53ef1f82bc931e79036521152ee9faa220e2a79ed2646df3016e488b2971"
        ),
        "current_test_sha256": (
            "d2ce9565202835d11116408c8ec6b71e94525aa630b311533cdcb3395303098e"
        ),
        "changed_paths": ";".join(
            sorted(inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS)
        ),
    }
    assert rows_by_id[inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_STAGE_A_MIGRATION_ID] == {
        "migration_id": inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_STAGE_A_MIGRATION_ID,
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_input_bound_validator_control_plane_stage_a_20260811"
        ),
        "base_helper_sha256": (
            "20cfc385916432d0a4cf82094270a7bbd41d901aa07a7586bbf88894540bfe90"
        ),
        "current_helper_sha256": (
            "763d4cdb1a9a7868fddb4eeb656304ca41c07d84a689c344dd2f5b0dc52e0a9d"
        ),
        "current_test_sha256": (
            "c45b96ffbee587d9adf332f123ce0c5b990cca4c8893ceed7fd9e1e8f4238ab5"
        ),
        "changed_paths": (
            "config/daily_model_pr_safe_self_migration_authorizations.csv;"
            "scripts/validate_repo_production_inventory.py;"
            "tests/test_repo_production_inventory.py"
        ),
    }
    assert rows_by_id[inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID] == {
        "migration_id": inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID,
        "status": "preauthorized",
        "approval_reference": "user_authorized_pr521_exact_target_preauthorization_20260811",
        "base_helper_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER
            ]
        ),
        "current_helper_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER
            ]
        ),
        "current_test_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TEST
            ]
        ),
        "changed_paths": ";".join(
            sorted(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS)
        ),
    }
    assert len(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS) == 41
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH[
        "config/repo_file_lifecycle_inventory.csv"
    ] == "6bd6d3c81eccbcfb929112ad713de7130d02829f9e46832055b88c4bd8be1e29"
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH[
        "config/repo_file_lifecycle_inventory.csv"
    ] == "f68002587c18ca4463d80a9ba41859e6ca06b75872566242a2ce64a0fb230431"
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH[
        "config/repo_production_inventory.csv"
    ] == "4f155b6568f60646608ed8c0be596ceb9ba4521afb2e0da82d8b2deea2c9d89b"
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH[
        "config/repo_production_inventory.csv"
    ] == "0273f04dc00d040b5890b3036fc10521b1c295e570aab9b48d7300914d47eac2"
    assert rows_by_id[
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID
    ] == {
        "migration_id": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_ID
        ),
        "status": "preauthorized",
        "approval_reference": "user_authorized_pr524_exact_target_preauthorization_20260812",
        "base_helper_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER
            ]
        ),
        "current_helper_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER
            ]
        ),
        "current_test_sha256": (
            inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TEST
            ]
        ),
        "changed_paths": ";".join(
            sorted(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS)
        ),
    }
    assert len(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS) == 19
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_SHA256_BY_PATH[
        "config/repo_file_lifecycle_inventory.csv"
    ] == "f68002587c18ca4463d80a9ba41859e6ca06b75872566242a2ce64a0fb230431"
    assert inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH[
        "config/repo_file_lifecycle_inventory.csv"
    ] == "fc1fb68e6d4a4910e79386d23aed7837ce41ea9c738ad43a2992eef9c8f9e632"
    assert rows_by_id[inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID] == {
        "migration_id": inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID,
        "status": "preauthorized",
        "approval_reference": "user_authorized_daily_runtime_authority_containment_20260812",
        "base_helper_sha256": (
            inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER
            ]
        ),
        "current_helper_sha256": (
            inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER
            ]
        ),
        "current_test_sha256": (
            inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TEST
            ]
        ),
        "changed_paths": ";".join(
            sorted(inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS)
        ),
    }
    assert len(inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS) == 20
    assert rows_by_id[inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID] == {
        "migration_id": inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_ID,
        "status": "preauthorized",
        "approval_reference": "user_authorized_daily_runtime_recovery_architecture_20260812",
        "base_helper_sha256": (
            inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER
            ]
        ),
        "current_helper_sha256": (
            inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER
            ]
        ),
        "current_test_sha256": (
            inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH[
                inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TEST
            ]
        ),
        "changed_paths": ";".join(
            sorted(inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS)
        ),
    }
    assert len(inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS) == 14


def test_daily_recovery_architecture_target_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_ref = "a" * 40
    head_ref = "b" * 40
    base_blobs = {
        path: None if expected is None else f"base:{path}\n".encode()
        for path, expected in inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH.items()
    }
    target_blobs = {
        path: f"target:{path}\n".encode()
        for path in inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_BASE_SHA256_BY_PATH",
        {
            path: None if payload is None else inventory.canonical_blob_sha256(payload)
            for path, payload in base_blobs.items()
        },
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_TARGET_SHA256_BY_PATH",
        {path: inventory.canonical_blob_sha256(payload) for path, payload in target_blobs.items()},
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: base_blobs[path] if ref == base_ref else target_blobs[path],
    )
    modes = {
        (ref, path): None if ref == base_ref and base_blobs[path] is None else "100644"
        for ref in (base_ref, head_ref)
        for path in inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, ref, path: modes[(ref, path)],
    )
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_PATHS),
        "repository_root": tmp_path,
        "head_ref": head_ref,
    }
    assert inventory.is_preauthorized_daily_authority_containment_target(**kwargs)
    helper = inventory.PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_HELPER
    target_blobs[helper] += b"drift\n"
    assert not inventory.is_preauthorized_daily_authority_containment_target(**kwargs)
    target_blobs[helper] = f"target:{helper}\n".encode()
    assert not inventory.is_preauthorized_daily_authority_containment_target(
        **{**kwargs, "changed_paths": {*kwargs["changed_paths"], "scripts/extra.py"}}
    )


def test_input_bound_validator_stage_a_rejects_mixed_or_drifted_target() -> None:
    base_helper = b"base helper without input-bound registration\n"
    current_helper = (
        inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID.encode("utf-8")
    )
    current_test = b"exact input-bound regressions\n"
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_MIGRATION_ID,
        authorized_paths=inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS,
    )
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    ) == []
    assert inventory.validate_pr_safe_control_plane_delta(
        {
            *inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS,
            "scripts/unregistered.py",
        },
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    )
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_INPUT_BOUND_VALIDATOR_REGISTRATION_PATHS),
        base_helper=base_helper,
        current_helper=current_helper + b"drift",
        current_test=current_test,
        authorization_payload=payload,
    )


def test_revenue_forward_holdout_target_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_ref = "a" * 40
    base_blobs: dict[str, bytes | None] = {}
    target_blobs: dict[str, bytes] = {}
    base_hashes: dict[str, str | None] = {}
    target_hashes: dict[str, str] = {}
    for path, expected_base_sha in (
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH.items()
    ):
        base_blobs[path] = (
            None if expected_base_sha is None else f"base:{path}\n".encode("utf-8")
        )
        target_blobs[path] = f"target:{path}\n".encode("utf-8")
        base_hashes[path] = (
            None
            if base_blobs[path] is None
            else inventory.canonical_blob_sha256(base_blobs[path] or b"")
        )
        target_hashes[path] = inventory.canonical_blob_sha256(target_blobs[path])

    monkeypatch.setattr(
        inventory,
        "PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: base_blobs[path] if ref == base_ref else target_blobs[path],
    )
    modes = {
        (ref, path): (
            None if ref == base_ref and base_blobs[path] is None else "100644"
        )
        for ref in (base_ref, "HEAD")
        for path in inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, ref, path: modes[(ref, path)],
    )
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS),
        "repository_root": tmp_path,
    }
    assert inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)

    mutated_path = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER
    original_target = target_blobs[mutated_path]
    target_blobs[mutated_path] = original_target + b"semantic drift\n"
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    target_blobs[mutated_path] = original_target

    modes[("HEAD", mutated_path)] = "100755"
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    modes[("HEAD", mutated_path)] = "100644"

    existing_path = next(path for path, value in base_blobs.items() if value is not None)
    original_base = base_blobs[existing_path]
    base_blobs[existing_path] = (original_base or b"") + b"base drift\n"
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    base_blobs[existing_path] = original_base
    modes[(base_ref, existing_path)] = "100755"
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    modes[(base_ref, existing_path)] = "100644"

    added_path = next(path for path, value in base_blobs.items() if value is None)
    base_blobs[added_path] = b"unexpected base collision\n"
    modes[(base_ref, added_path)] = "100644"
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    base_blobs[added_path] = None
    modes[(base_ref, added_path)] = None

    assert not inventory.is_preauthorized_revenue_forward_holdout_target(
        **{**kwargs, "changed_paths": {*kwargs["changed_paths"], "scripts/extra.py"}}
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: False,
    )
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)


def test_revenue_forward_holdout_target_uses_base_owned_ledger(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_helper = b"base workflow isolation helper\n"
    current_helper = b"target workflow isolation helper\n"
    current_test = b"target workflow isolation tests\n"
    base_hashes = dict(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH)
    target_hashes = dict(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH)
    base_hashes[inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER] = (
        inventory.canonical_blob_sha256(base_helper)
    )
    target_hashes[inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_HELPER] = (
        inventory.canonical_blob_sha256(current_helper)
    )
    target_hashes[inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TEST] = (
        inventory.canonical_blob_sha256(current_test)
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_REVENUE_FORWARD_HOLDOUT_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_TARGET_ID,
        authorized_paths=inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS,
    )
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    ) == []
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_PATHS),
        base_helper=base_helper,
        current_helper=current_helper + b"drift",
        current_test=current_test,
        authorization_payload=payload,
    )


def test_revenue_forward_holdout_replay_detail_target_matches_frozen_git_objects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_ref = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_CONTENT_REF_SHA
    target_ref = "a005b620328b9806271022539d32224a5ab7886f"
    paths = set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS)
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": paths,
        "repository_root": ROOT,
        "head_ref": target_ref,
    }
    assert inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(
        **{**kwargs, "changed_paths": {*paths, "scripts/unregistered.py"}}
    )
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(
        **{**kwargs, "base_ref": "0" * 40}
    )

    helper = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER
    expected_helper_sha = (
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH[
            helper
        ]
    )
    monkeypatch.setitem(
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH,
        helper,
        "0" * 64,
    )
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)
    monkeypatch.setitem(
        inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TARGET_SHA256_BY_PATH,
        helper,
        expected_helper_sha,
    )

    original_mode = inventory._pr_safe_repo_blob_mode
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda root, ref, path: (
            "100755"
            if ref == target_ref and path == helper
            else original_mode(root, ref, path)
        ),
    )
    assert not inventory.is_preauthorized_revenue_forward_holdout_target(**kwargs)


def test_revenue_forward_holdout_replay_detail_target_uses_base_owned_ledger() -> None:
    base_ref = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_BASE_CONTENT_REF_SHA
    target_ref = "a005b620328b9806271022539d32224a5ab7886f"
    helper = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_HELPER
    direct_test = inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_TEST
    base_helper = inventory.git_blob_at_ref(base_ref, helper)
    current_helper = inventory.git_blob_at_ref(target_ref, helper)
    current_test = inventory.git_blob_at_ref(target_ref, direct_test)
    authorization_payload = (ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    errors = inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=authorization_payload,
    )
    assert errors == []
    assert current_helper is not None
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_REVENUE_FORWARD_HOLDOUT_REPLAY_DETAIL_PATHS),
        base_helper=base_helper,
        current_helper=current_helper + b"drift",
        current_test=current_test,
        authorization_payload=authorization_payload,
    )


def test_daily_authority_containment_target_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    base_ref = "a" * 40
    head_ref = "b" * 40
    base_blobs: dict[str, bytes | None] = {}
    target_blobs: dict[str, bytes] = {}
    base_hashes: dict[str, str | None] = {}
    target_hashes: dict[str, str] = {}
    for path, expected_base_sha in (
        inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH.items()
    ):
        base_blobs[path] = (
            None if expected_base_sha is None else f"base:{path}\n".encode("utf-8")
        )
        target_blobs[path] = f"target:{path}\n".encode("utf-8")
        base_hashes[path] = (
            None
            if base_blobs[path] is None
            else inventory.canonical_blob_sha256(base_blobs[path] or b"")
        )
        target_hashes[path] = inventory.canonical_blob_sha256(target_blobs[path])

    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_ref_is_ancestor",
        lambda _root, _ancestor, _descendant: True,
    )
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob",
        lambda _root, ref, path: (
            base_blobs[path] if ref == base_ref else target_blobs[path]
        ),
    )
    modes = {
        (ref, path): (
            None if ref == base_ref and base_blobs[path] is None else "100644"
        )
        for ref in (base_ref, head_ref)
        for path in inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS
    }
    monkeypatch.setattr(
        inventory,
        "_pr_safe_repo_blob_mode",
        lambda _root, ref, path: modes[(ref, path)],
    )
    kwargs = {
        "base_ref": base_ref,
        "changed_paths": set(inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS),
        "repository_root": tmp_path,
        "head_ref": head_ref,
    }
    assert inventory.is_preauthorized_daily_authority_containment_target(**kwargs)

    helper = inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER
    original_target = target_blobs[helper]
    target_blobs[helper] = original_target + b"drift\n"
    assert not inventory.is_preauthorized_daily_authority_containment_target(**kwargs)
    target_blobs[helper] = original_target

    modes[(head_ref, helper)] = "100755"
    assert not inventory.is_preauthorized_daily_authority_containment_target(**kwargs)
    modes[(head_ref, helper)] = "100644"

    added_path = next(path for path, value in base_blobs.items() if value is None)
    base_blobs[added_path] = b"unexpected collision\n"
    modes[(base_ref, added_path)] = "100644"
    assert not inventory.is_preauthorized_daily_authority_containment_target(**kwargs)
    base_blobs[added_path] = None
    modes[(base_ref, added_path)] = None

    assert not inventory.is_preauthorized_daily_authority_containment_target(
        **{**kwargs, "changed_paths": {*kwargs["changed_paths"], "scripts/extra.py"}}
    )


def test_daily_authority_containment_target_uses_base_owned_ledger(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_helper = b"base daily boundary validator\n"
    current_helper = b"target daily boundary validator\n"
    current_test = b"target daily boundary regressions\n"
    base_hashes = dict(
        inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH
    )
    target_hashes = dict(
        inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH
    )
    base_hashes[inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER] = (
        inventory.canonical_blob_sha256(base_helper)
    )
    target_hashes[inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_HELPER] = (
        inventory.canonical_blob_sha256(current_helper)
    )
    target_hashes[inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TEST] = (
        inventory.canonical_blob_sha256(current_test)
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_BASE_SHA256_BY_PATH",
        base_hashes,
    )
    monkeypatch.setattr(
        inventory,
        "PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_SHA256_BY_PATH",
        target_hashes,
    )
    payload = pr_safe_authorization_payload(
        base_helper,
        current_helper,
        current_test,
        migration_id=inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_TARGET_ID,
        authorized_paths=inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS,
    )
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS),
        base_helper=base_helper,
        current_helper=current_helper,
        current_test=current_test,
        authorization_payload=payload,
    ) == []
    assert inventory.validate_pr_safe_control_plane_delta(
        set(inventory.PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_PATHS),
        base_helper=base_helper,
        current_helper=current_helper + b"drift",
        current_test=current_test,
        authorization_payload=payload,
    )


def test_daily_authority_containment_stage_a_cannot_self_authorize() -> None:
    stage_a_paths = {
        inventory.PR_SAFE_AUTHORIZATION_PATH,
        inventory.PR_SAFE_BASE_GUARD_SCRIPT,
        "tests/test_repo_production_inventory.py",
    }
    assert inventory.pr_safe_migration_contract_for_paths(stage_a_paths) is None
    errors = inventory.validate_pr_safe_control_plane_delta(
        stage_a_paths,
        base_helper=b"base guard\n",
        current_helper=b"branch guard\n",
        current_test=b"branch tests\n",
        authorization_payload=(ROOT / inventory.PR_SAFE_AUTHORIZATION_PATH).read_bytes(),
    )
    assert any("may not modify the base-owned PR-safe trust root" in error for error in errors)


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
