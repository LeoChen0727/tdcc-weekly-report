from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path
import subprocess

import pytest

from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]
VOLUME_V2_ADVISORY_LINEAGE_REFRESH_WORKFLOW = (
    ".github/workflows/volume_v2_advisory_lineage_refresh.yml"
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










def test_pr_safe_lifecycle_authorization_ledger_is_exact_and_base_owned() -> None:
    payload = (ROOT / inventory.PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH).read_bytes()

    rows, errors = inventory.parse_pr_safe_lifecycle_authorizations(payload)

    assert errors == []
    assert {
        (row["row_path"], row["column"])
        for row in rows
    } == inventory.PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS








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


def test_daily_required_commands_keep_pdf_runtime_gates_not_repo_static_self_hooks() -> None:
    commands = inventory.REQUIRED_WORKFLOW_COMMANDS[inventory.DAILY_WORKFLOW]

    assert "python scripts/validate_pdf_production_inventory.py" in commands
    assert "python scripts/validate_daily_pdf_contract_consumers.py" in commands
    assert "python scripts/validate_daily_pdf_shared_path_isolation.py" in commands
    assert "python scripts/validate_daily_pdf_completion_hard_gate.py" in commands
    assert "python scripts/validate_repo_production_inventory.py" not in commands
    assert "python scripts/validate_repo_code_isolation_policy.py" not in commands
    assert "python scripts/validate_model_research_workflow_isolation.py" not in commands


























































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


def test_pr_safe_trust_root_set_is_exact_and_routine_profiles_are_retired() -> None:
    assert inventory.PR_SAFE_TRUST_ROOT_PATHS == {
        ".github/workflows/individual_stock_pr_validation.yml",
        "scripts/validate_repo_production_inventory.py",
        inventory.PR_SAFE_ADVANCED_HELPER,
        inventory.PR_SAFE_SNAPSHOT_HELPER,
        "config/daily_model_pr_safe_self_migration_authorizations.csv",
        "config/repo_file_lifecycle_semantic_migrations.csv",
    }
    retired_prefixes = (
        "PR_SAFE_REVENUE_FORWARD_HOLDOUT_",
        "PR_SAFE_REVENUE_PROMOTION_PREPARATION",
        "PR_SAFE_DAILY_AUTHORITY_CONTAINMENT_",
        "PR_SAFE_DAILY_RECOVERY_ARCHITECTURE_",
        "PR_SAFE_DAILY_RUNTIME_INTEGRATION_REGRESSIONS_",
        "PR_SAFE_DAILY_AUTHORITY_SNAPSHOT_REPLAY_",
        "PR_SAFE_VOLUME_V2_",
    )
    assert not [
        name for name in vars(inventory) if name.startswith(retired_prefixes)
    ]
    assert not hasattr(inventory, "validate_pr_safe_control_plane_migration")
    assert not hasattr(inventory, "build_pr_safe_audit_manifest")
    validator_source = (
        ROOT / "scripts" / "validate_repo_production_inventory.py"
    ).read_text(encoding="utf-8")
    assert (
        '"scripts/validate_revenue_unreacted_range_promotion_preparation.py"'
        not in validator_source
    )
    assert inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_PATHS
    assert inventory.PR_SAFE_DAILY_FULL_CHECKPOINT_REPLAY_STRICT_SURFACES
    assert inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_PATHS
    assert inventory.PR_SAFE_LOCAL_VALIDATION_REPLAY_ROUTING_STRICT_SURFACES
    assert callable(inventory.is_preauthorized_daily_full_checkpoint_replay_migration)


def test_pr_trust_root_guard_fast_passes_routine_diff(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=b"M\0docs/routine-note.md\0",
    )
    assert inventory.validate_pr_trust_root_change(base_sha, head_sha) == []


def test_pr_trust_root_guard_requires_same_repo_and_label_but_allows_new_bytes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target_path = inventory.PR_SAFE_ADVANCED_HELPER
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
    ).read_bytes()
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
