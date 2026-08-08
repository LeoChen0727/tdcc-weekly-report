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
        ("HEAD", inventory.PR_SAFE_SNAPSHOT_HELPER): current_helper,
        ("HEAD", inventory.PR_SAFE_SNAPSHOT_TEST): current_test,
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


def test_daily_full_checkpoint_replay_preauthorization_is_exact_and_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
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
