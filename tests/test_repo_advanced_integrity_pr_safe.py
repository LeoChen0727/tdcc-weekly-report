from __future__ import annotations

import csv
import hashlib
import io
from pathlib import Path

import pytest

from scripts import validate_repo_advanced_integrity as strict_validator
from scripts import validate_repo_advanced_integrity_pr_safe as pr_safe


FRESHNESS_ROW = {
    "main_price_date": "20260730",
    "main_price_date_source": "historical_replay_override",
    "historical_replay_main_price_date": "20260730",
    "expected_price_history_high_water_date": "20260730",
    "actual_stock_price_history_date": "20260730",
    "official_price_fetch_date": "20260730",
    "stock_monitor_price_date": "20260717",
    "all_candidates_date": "20260717",
    "report_ready": "False",
    "report_ready_note": (
        "historical structured-source replay updates objective-source freshness only; "
        "publish artifacts remain stale"
    ),
    "daily_pdf_ready": "False",
    "daily_pdf_ready_note": (
        "historical structured-source replay must not mark stale daily PDFs ready"
    ),
}

CONTRACT_ROWS = [
    {
        "source_id": "official_daily_price",
        "status_artifact": pr_safe.FRESHNESS_RELATIVE_PATH,
        "freshness_date_column": "official_price_fetch_date",
        "readiness_column": "report_ready",
        "require_matches_main_price_date": "True",
    },
    {
        "source_id": "daily_stock_monitor",
        "status_artifact": pr_safe.FRESHNESS_RELATIVE_PATH,
        "freshness_date_column": "stock_monitor_price_date",
        "readiness_column": "report_ready",
        "require_matches_main_price_date": "True",
    },
    {
        "source_id": "all_candidates",
        "status_artifact": pr_safe.FRESHNESS_RELATIVE_PATH,
        "freshness_date_column": "all_candidates_date",
        "readiness_column": "report_ready",
        "require_matches_main_price_date": "True",
    },
    {
        "source_id": "daily_pdf_source",
        "status_artifact": pr_safe.FRESHNESS_RELATIVE_PATH,
        "freshness_date_column": "main_price_date",
        "readiness_column": "daily_pdf_ready",
        "require_matches_main_price_date": "True",
    },
]

EXPECTED_STRICT_ERRORS = {
    "external source official_daily_price readiness report_ready is not True",
    (
        "external source daily_stock_monitor date stock_monitor_price_date=20260717 "
        "does not match main_price_date=20260730"
    ),
    "external source daily_stock_monitor readiness report_ready is not True",
    (
        "external source all_candidates date all_candidates_date=20260717 "
        "does not match main_price_date=20260730"
    ),
    "external source all_candidates readiness report_ready is not True",
    "external source daily_pdf_source readiness daily_pdf_ready is not True",
}


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def csv_payload(rows: list[dict[str, str]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def install_registered_source_identity_migration(
    repository_root: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    producer: str = "build_all_candidates_latest.py",
) -> set[str]:
    contract_rows = []
    for row in CONTRACT_ROWS:
        contract_rows.append(
            {
                **row,
                "producer": producer if row["source_id"] == "all_candidates" else "",
                "validator": "",
                "json_status_path": "",
                "allowed_statuses": "",
            }
        )
    write_csv(repository_root / pr_safe.EXTERNAL_SOURCE_CONTRACT_PATH, contract_rows)
    producer_file = repository_root / producer
    producer_file.parent.mkdir(parents=True, exist_ok=True)
    producer_file.write_text("# registered external producer\n", encoding="utf-8")

    test_path = "tests/test_all_candidates_source_identity.py"
    test_file = repository_root / test_path
    test_file.parent.mkdir(parents=True, exist_ok=True)
    test_file.write_text("def test_source_identity():\n    pass\n", encoding="utf-8")

    base_inventory = [
        {"path": "placeholder.py", "type": "python", "owner": "repo"},
        {"path": producer, "type": "python", "owner": "daily_production"},
    ]
    added_test_inventory = {
        "path": test_path,
        "type": "test_python",
        "owner": "daily_production",
    }
    write_csv(
        repository_root / pr_safe.PRODUCTION_INVENTORY_PATH,
        [*base_inventory, added_test_inventory],
    )

    base_migration = {
        "migration_id": "existing_migration",
        "changed_lineage_ids": "existing_lineage",
        "previous_contract_sha256s": "NEW",
        "new_contract_sha256s": "b" * 64,
        "affected_models": "existing_model",
        "affected_consumers": "existing.py",
        "validation_commands": "python existing.py",
        "user_approval_reference": "existing_approval",
        "migration_status": pr_safe.SOURCE_IDENTITY_MIGRATION_STATUS,
        "notes": "existing",
    }
    migration_id = "all_candidates_source_identity_20260731"
    contract_sha = "a" * 64
    added_migration = {
        **base_migration,
        "migration_id": migration_id,
        "changed_lineage_ids": "candidate_source_row_id__all_candidates_current",
        "new_contract_sha256s": contract_sha,
        "affected_consumers": producer,
        "validation_commands": (
            f"python {pr_safe.CANONICAL_LINEAGE_VALIDATOR_PATH};"
            f"python -m pytest {test_path}"
        ),
        "user_approval_reference": "approved_source_identity_migration",
        "notes": "immutable source identity",
    }
    write_csv(
        repository_root / pr_safe.CANONICAL_LINEAGE_MIGRATIONS_PATH,
        [base_migration, added_migration],
    )

    base_registry = {
        "lineage_id": "existing_lineage",
        "field_name": "existing_field",
        "model_family": "existing_family",
        "artifact_path": "output/latest/existing.csv",
        "artifact_role": "existing_role",
        "producer": "existing.py",
        "identity_columns": "stock_id",
        "as_of_columns": "date",
        "canonical_source_artifact": "output/latest/existing.csv",
        "allowed_consumer_modules": "existing.py",
        "allowed_use": "existing_use",
        "forbidden_use": "existing_forbidden_use",
        "collision_policy": "existing_collision",
        "parity_policy": "existing_parity",
        "contract_sha256": "b" * 64,
        "last_migration_id": "existing_migration",
        "approval_reference": "existing_approval",
        "required_validation_commands": "python existing.py",
        "notes": "existing",
    }
    added_registry = {
        **base_registry,
        "lineage_id": "candidate_source_row_id__all_candidates_current",
        "field_name": "candidate_source_row_id",
        "model_family": "volume_v2_candidate_source_identity_current",
        "artifact_path": "output/latest/all_candidates_latest.csv",
        "artifact_role": pr_safe.SOURCE_IDENTITY_ARTIFACT_ROLE,
        "producer": producer,
        "identity_columns": "candidate_source_artifact;candidate_source_record_number",
        "canonical_source_artifact": "output/latest/all_candidates_latest.csv",
        "allowed_consumer_modules": "scripts/build_daily_candidate_model_layer.py",
        "allowed_use": "immutable_source_identity_trace",
        "forbidden_use": "model_gate_score_or_rank",
        "collision_policy": "source_row_id_unique",
        "parity_policy": "raw_to_normalized_identity_parity",
        "contract_sha256": contract_sha,
        "last_migration_id": migration_id,
        "approval_reference": "approved_source_identity_migration",
        "required_validation_commands": f"python -m pytest {test_path}",
        "notes": "immutable source identity",
    }
    write_csv(
        repository_root / pr_safe.CANONICAL_LINEAGE_REGISTRY_PATH,
        [base_registry, added_registry],
    )

    workflow = repository_root / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(
        f"{pr_safe.PR_SAFE_COMMAND}\n{pr_safe.CANONICAL_LINEAGE_PR_COMMAND}\n",
        encoding="utf-8",
    )

    base_payloads = {
        pr_safe.PRODUCTION_INVENTORY_PATH: csv_payload(base_inventory),
        pr_safe.CANONICAL_LINEAGE_MIGRATIONS_PATH: csv_payload([base_migration]),
        pr_safe.CANONICAL_LINEAGE_REGISTRY_PATH: csv_payload([base_registry]),
    }
    monkeypatch.setattr(
        pr_safe,
        "git_blob_at_ref",
        lambda _ref, path, **_kwargs: base_payloads.get(path),
    )
    monkeypatch.setattr(
        pr_safe,
        "git_path_exists_at_ref",
        lambda _ref, path, **_kwargs: False if path == test_path else True,
    )
    changed_paths = {
        producer,
        pr_safe.PRODUCTION_INVENTORY_PATH,
        pr_safe.CANONICAL_LINEAGE_MIGRATIONS_PATH,
        pr_safe.CANONICAL_LINEAGE_REGISTRY_PATH,
        test_path,
    }
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (set(changed_paths), []),
    )
    return changed_paths


@pytest.fixture
def historical_replay_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    freshness = tmp_path / pr_safe.FRESHNESS_RELATIVE_PATH
    contract = tmp_path / pr_safe.EXTERNAL_SOURCE_CONTRACT_PATH
    inventory = tmp_path / pr_safe.PRODUCTION_INVENTORY_PATH
    write_csv(freshness, [FRESHNESS_ROW])
    write_csv(
        contract,
        [
            {
                **row,
                "producer": "",
                "validator": "",
                "json_status_path": "",
                "allowed_statuses": "",
            }
            for row in CONTRACT_ROWS
        ],
    )
    write_csv(inventory, [{"path": "placeholder.py"}])

    monkeypatch.setattr(strict_validator, "ROOT", tmp_path)
    monkeypatch.setattr(strict_validator, "FRESHNESS_CSV", freshness)
    monkeypatch.setattr(strict_validator, "EXTERNAL_SOURCE_CONTRACT", contract)
    monkeypatch.setattr(strict_validator, "INVENTORY_CSV", inventory)
    for name in (
        "validate_required_configs",
        "validate_runtime_file_lineage_contract",
        "validate_pdf_golden_contract",
        "validate_historical_replay_semantics",
        "validate_model_condition_spec",
    ):
        monkeypatch.setattr(strict_validator, name, lambda: [])

    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: ({"scripts/unrelated_change.py"}, []),
    )
    monkeypatch.setattr(
        pr_safe,
        "validate_freshness_is_inherited_from_base",
        lambda *_args, **_kwargs: [],
    )
    return tmp_path


def test_unrelated_pr_inherits_exact_historical_replay_not_ready_state(
    historical_replay_repo: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    strict_errors = strict_validator.validate()
    assert set(strict_errors) == EXPECTED_STRICT_ERRORS
    assert strict_validator.main() == 1
    strict_stdout = capsys.readouterr().out
    assert "official_daily_price readiness report_ready is not True" in strict_stdout
    assert "daily_stock_monitor date stock_monitor_price_date=20260717" in strict_stdout
    assert "all_candidates date all_candidates_date=20260717" in strict_stdout
    assert "daily_pdf_source readiness daily_pdf_ready is not True" in strict_stdout

    assert (
        pr_safe.validate_pr_safe_advanced_integrity_contract(
            "base-sha",
            repository_root=historical_replay_repo,
        )
        == []
    )


@pytest.mark.parametrize(
    "changed_path",
    [
        pr_safe.STRICT_VALIDATOR_PATH,
        pr_safe.EXTERNAL_SOURCE_CONTRACT_PATH,
        pr_safe.FRESHNESS_RELATIVE_PATH,
    ],
)
def test_related_strict_surface_cannot_inherit_not_ready_state(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    changed_path: str,
) -> None:
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: ({changed_path}, []),
    )

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert errors
    assert "full runtime repo advanced-integrity validation is required" in errors[0]
    assert changed_path in errors[0]


def test_changed_freshness_bytes_fail_closed(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        pr_safe,
        "validate_freshness_is_inherited_from_base",
        lambda *_args, **_kwargs: ["freshness differs from base"],
    )

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert errors == ["freshness differs from base"]


def test_unexpected_external_source_failure_is_not_inheritable(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    original = strict_validator.validate_external_source_contract
    monkeypatch.setattr(
        strict_validator,
        "validate_external_source_contract",
        lambda: [*original(), "external source calendar_sources unexpected failure"],
    )

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert "may inherit only the exact external source errors" in errors[0]
    assert errors[-1] == "external source calendar_sources unexpected failure"


def test_initial_control_plane_bootstrap_is_exact_and_one_time(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    workflow = historical_replay_repo / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    boundary = historical_replay_repo / pr_safe.PR_BOUNDARY_VALIDATOR_PATH
    inventory = historical_replay_repo / pr_safe.PRODUCTION_INVENTORY_PATH
    helper = historical_replay_repo / pr_safe.PR_SAFE_HELPER_PATH
    workflow.parent.mkdir(parents=True, exist_ok=True)
    boundary.parent.mkdir(parents=True, exist_ok=True)
    helper.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(
        f"{pr_safe.PR_SAFE_COMMAND}\n{pr_safe.STRICT_RUNTIME_TEST_DESELECT}\n",
        encoding="utf-8",
    )
    boundary.write_text(pr_safe.PR_SAFE_COMMAND + "\n", encoding="utf-8")
    helper.write_text("bootstrap helper\n", encoding="utf-8")
    inventory.write_text(
        f"path\n{pr_safe.PR_SAFE_HELPER_PATH}\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (set(pr_safe.PR_SAFE_BOOTSTRAP_SURFACES), []),
    )
    monkeypatch.setattr(pr_safe, "git_path_exists_at_ref", lambda *_a, **_k: False)

    base_payloads = {
        pr_safe.PR_VALIDATION_WORKFLOW_PATH: b"tests/test_repo_advanced_integrity.py\n",
        pr_safe.PR_BOUNDARY_VALIDATOR_PATH: b"old boundary\n",
        pr_safe.PRODUCTION_INVENTORY_PATH: b"path\n",
    }
    monkeypatch.setattr(
        pr_safe,
        "git_blob_at_ref",
        lambda _ref, path, **_kwargs: base_payloads.get(path),
    )

    assert (
        pr_safe.validate_pr_safe_advanced_integrity_contract(
            "base-sha",
            repository_root=historical_replay_repo,
        )
        == []
    )

    monkeypatch.setattr(pr_safe, "git_path_exists_at_ref", lambda *_a, **_k: True)
    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )
    assert errors
    assert "full runtime repo advanced-integrity validation is required" in errors[0]


def test_registered_source_identity_migration_inherits_stale_runtime_but_strict_fails(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    install_registered_source_identity_migration(
        historical_replay_repo,
        monkeypatch,
    )

    assert strict_validator.main() == 1
    strict_stdout = capsys.readouterr().out
    assert "all_candidates date all_candidates_date=20260717" in strict_stdout
    assert "daily_pdf_source readiness daily_pdf_ready is not True" in strict_stdout
    assert (
        pr_safe.validate_pr_safe_advanced_integrity_contract(
            "base-sha",
            repository_root=historical_replay_repo,
        )
        == []
    )


@pytest.mark.parametrize(
    "forbidden_path",
    [
        pr_safe.EXTERNAL_SOURCE_CONTRACT_PATH,
        pr_safe.FRESHNESS_RELATIVE_PATH,
        ".github/workflows/daily_full_pipeline.yml",
        "output/latest/published_reports/daily_market/report.pdf",
    ],
)
def test_registered_source_identity_migration_cannot_cover_strict_contract_or_runtime_paths(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    forbidden_path: str,
) -> None:
    changed_paths = install_registered_source_identity_migration(
        historical_replay_repo,
        monkeypatch,
    )
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: ({*changed_paths, forbidden_path}, []),
    )

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert errors
    assert "full runtime repo advanced-integrity validation is required" in errors[0]
    assert forbidden_path in errors[0]


def test_unregistered_external_producer_cannot_use_registered_migration_evidence(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_registered_source_identity_migration(
        historical_replay_repo,
        monkeypatch,
        producer="scripts/unregistered_external_producer.py",
    )
    migration_path = historical_replay_repo / pr_safe.CANONICAL_LINEAGE_MIGRATIONS_PATH
    rows = list(csv.DictReader(migration_path.read_text(encoding="utf-8").splitlines()))
    rows[-1]["affected_consumers"] = "build_all_candidates_latest.py"
    write_csv(migration_path, rows)
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (set(changed_paths), []),
    )

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert errors
    assert "migration consumer evidence" in "\n".join(errors)


def test_incomplete_source_identity_contract_sha_evidence_fails_closed(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    install_registered_source_identity_migration(
        historical_replay_repo,
        monkeypatch,
    )
    registry_path = historical_replay_repo / pr_safe.CANONICAL_LINEAGE_REGISTRY_PATH
    rows = list(csv.DictReader(registry_path.read_text(encoding="utf-8").splitlines()))
    rows[-1]["contract_sha256"] = "c" * 64
    write_csv(registry_path, rows)

    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )

    assert errors
    assert "contract SHA mismatch" in "\n".join(errors)


def test_registered_source_identity_gate_self_update_is_exact_and_one_time(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    helper_path = historical_replay_repo / pr_safe.PR_SAFE_HELPER_PATH
    test_path = historical_replay_repo / pr_safe.SOURCE_IDENTITY_GATE_TEST_PATH
    helper_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.parent.mkdir(parents=True, exist_ok=True)
    helper_path.write_text(
        pr_safe.SOURCE_IDENTITY_GATE_SELF_UPDATE_ID,
        encoding="utf-8",
    )
    test_path.write_text(
        pr_safe.SOURCE_IDENTITY_GATE_SELF_UPDATE_TEST_MARKER,
        encoding="utf-8",
    )
    base_helper = b"exact base helper"
    monkeypatch.setattr(
        pr_safe,
        "SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256",
        hashlib.sha256(base_helper).hexdigest(),
    )
    monkeypatch.setattr(
        pr_safe,
        "git_blob_at_ref",
        lambda _ref, path, **_kwargs: (
            base_helper if path == pr_safe.PR_SAFE_HELPER_PATH else None
        ),
    )
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (
            set(pr_safe.SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS),
            [],
        ),
    )

    assert (
        pr_safe.validate_pr_safe_advanced_integrity_contract(
            "base-sha",
            repository_root=historical_replay_repo,
        )
        == []
    )

    monkeypatch.setattr(
        pr_safe,
        "SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256",
        "0" * 64,
    )
    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )
    assert errors
    assert "full runtime repo advanced-integrity validation is required" in errors[0]

    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (
            {
                *pr_safe.SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS,
                pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            },
            [],
        ),
    )
    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )
    assert errors
    assert pr_safe.PR_VALIDATION_WORKFLOW_PATH in errors[0]
