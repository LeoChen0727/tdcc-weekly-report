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


PR462_RESEARCH_PRODUCERS = (
    "scripts/revenue_unreacted_range_synthetic_pr_safe_fixture_source_snapshot_projection.py",
    "scripts/revenue_unreacted_range_synthetic_pr_safe_fixture_low_mid_falling_candidate_audit.py",
    "scripts/revenue_unreacted_range_synthetic_pr_safe_fixture_monthly_revenue_cross_market_resolution.py",
    "scripts/revenue_unreacted_range_synthetic_pr_safe_fixture_research_frame.py",
)
PR462_RESEARCH_VALIDATORS = (
    "scripts/validate_revenue_unreacted_range_synthetic_pr_safe_fixture_source_snapshot_projection.py",
    "scripts/validate_revenue_unreacted_range_synthetic_pr_safe_fixture_low_mid_falling_candidate_audit.py",
    "scripts/validate_revenue_unreacted_range_synthetic_pr_safe_fixture_monthly_revenue_cross_market_resolution.py",
)
PR462_RESEARCH_TESTS = (
    "tests/test_revenue_unreacted_range_synthetic_pr_safe_fixture_source_snapshot_projection.py",
    "tests/test_revenue_unreacted_range_synthetic_pr_safe_fixture_monthly_revenue_cross_market_resolution.py",
    "tests/test_validate_revenue_unreacted_range_synthetic_pr_safe_fixture_monthly_revenue_cross_market_resolution.py",
    "tests/test_revenue_unreacted_range_synthetic_pr_safe_fixture_low_mid_falling_candidate_audit.py",
    "tests/test_validate_revenue_unreacted_range_synthetic_pr_safe_fixture_low_mid_falling_candidate_audit.py",
)
PR462_SYNTHETIC_FIXTURE_PATHS = (
    *PR462_RESEARCH_PRODUCERS,
    *PR462_RESEARCH_VALIDATORS,
    *PR462_RESEARCH_TESTS,
)
PR462_EXISTING_RESEARCH_ROWS = (
    "scripts/synthetic_pr_safe_fixture_existing_research_audit.py",
    "scripts/synthetic_pr_safe_fixture_existing_research_validator.py",
)
PR462_LIFECYCLE_TARGETS = (
    "scripts/synthetic_pr_safe_fixture_data_independence_audit.py",
    "scripts/synthetic_pr_safe_fixture_revenue_research_producer.py",
)
PR462_CONTROL_PATHS = tuple(pr_safe.RESEARCH_CONTROL_PYTHON_ALLOWLIST)
PR462_PRODUCTION_SENTINEL = "scripts/build_daily_candidate_model_layer.py"
PR462_LEGACY_RESEARCH_ARTIFACT = (
    "output/latest/research_backtest/monthly_revenue_history_latest.csv"
)
PR462_REPLACEMENT_RESEARCH_CONFIG = (
    "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG = (
    "config/revenue_unreacted_range_price_comparability_resolution.csv"
)


def test_pr462_fixture_python_paths_are_synthetic_and_repo_absent() -> None:
    repository_root = Path(__file__).resolve().parents[1]

    for path in PR462_SYNTHETIC_FIXTURE_PATHS:
        assert "synthetic_pr_safe_fixture" in path
        assert not (repository_root / path).exists()


def production_inventory_row(
    path: str,
    *,
    kind: str = "python",
    purpose: str = "research-only path",
    allowed_workflows: str = pr_safe.RESEARCH_WORKFLOW_PATH,
    owner: str = pr_safe.RESEARCH_OWNER,
) -> dict[str, str]:
    return {
        "path": path,
        "kind": kind,
        "owner": owner,
        "status": "active",
        "purpose": purpose,
        "allowed_workflows": allowed_workflows,
        "allowed_stage_patterns": "",
    }


def lifecycle_inventory_row(
    path: str,
    *,
    kind: str,
    tested_by: str = "",
    owner: str = pr_safe.RESEARCH_OWNER,
) -> dict[str, str]:
    return {
        "path": path,
        "type": kind,
        "owner": owner,
        "status": "active",
        "called_by_workflow": (
            f"{pr_safe.PR_VALIDATION_WORKFLOW_PATH};{pr_safe.RESEARCH_WORKFLOW_PATH}"
            if path in PR462_RESEARCH_VALIDATORS
            else ""
        ),
        "imported_by": "",
        "tested_by": tested_by,
        "documented_by": "",
        "writes_artifact": "",
        "reads_artifact": "",
        "keep_reason": "registered research-only path",
        "delete_reason": "",
        "removal_risk": "high",
    }


def lifecycle_authorization_row(
    migration_id: str,
    row_path: str,
    base_value: str,
    current_value: str,
    **overrides: str,
) -> dict[str, str]:
    base_values = set(pr_safe.split_list(base_value))
    current_values = set(pr_safe.split_list(current_value))
    row = {
        "migration_id": migration_id,
        "status": pr_safe.LIFECYCLE_SEMANTIC_MIGRATION_STATUS,
        "approval_reference": "user_delegated_pr462_research_registration_20260803",
        "row_path": row_path,
        "column": "reads_artifact",
        "base_value_sha256": pr_safe.canonical_sha256(base_value.encode("utf-8")),
        "current_value_sha256": pr_safe.canonical_sha256(
            current_value.encode("utf-8")
        ),
        "added_values": ";".join(sorted(current_values - base_values)),
        "removed_values": ";".join(sorted(base_values - current_values)),
        "scope": pr_safe.LIFECYCLE_SEMANTIC_MIGRATION_SCOPE,
    }
    row.update(overrides)
    return row


def install_pr462_additive_research_registration(
    repository_root: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    lifecycle_authorization_overrides: dict[str, str] | None = None,
    include_config_filter_assertion: bool = True,
) -> set[str]:
    monkeypatch.setattr(
        pr_safe,
        "RESEARCH_LIFECYCLE_CONTROL_ALLOWLIST",
        frozenset(
            {
                *pr_safe.RESEARCH_LIFECYCLE_CONTROL_ALLOWLIST,
                PR462_LIFECYCLE_TARGETS[0],
            }
        ),
    )
    base_workflow = """name: Daily Model Maintenance PR Validation
on:
  pull_request:
    paths:
      - "config/daily_model_*.csv"
      - "tests/test_revenue_unreacted_range_*.py"
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Validate contracts
        run: |
          python scripts/validate_revenue_unreacted_range_existing.py
      - name: Focused tests
        run: |
          python -m pytest -q \\
            tests/test_revenue_unreacted_range_existing.py
"""
    current_workflow = base_workflow.replace(
        '      - "config/daily_model_*.csv"\n',
        '      - "config/daily_model_*.csv"\n'
        '      - "config/revenue_unreacted_range_*.csv"\n',
        1,
    ).replace(
        '      - "tests/test_revenue_unreacted_range_*.py"\n',
        '      - "tests/test_revenue_unreacted_range_*.py"\n'
        '      - "tests/test_validate_revenue_unreacted_range_*.py"\n',
        1,
    ).replace(
        "          python scripts/validate_revenue_unreacted_range_existing.py\n",
        "          python scripts/validate_revenue_unreacted_range_existing.py\n"
        + "".join(f"          python {path}\n" for path in PR462_RESEARCH_VALIDATORS),
        1,
    ).replace(
        "            tests/test_revenue_unreacted_range_existing.py\n",
        "".join(f"            {path} \\\n" for path in PR462_RESEARCH_TESTS)
        + "            tests/test_revenue_unreacted_range_existing.py\n",
        1,
    )
    workflow_path = repository_root / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    workflow_path.parent.mkdir(parents=True, exist_ok=True)
    workflow_path.write_text(current_workflow, encoding="utf-8")

    base_rows = [
        production_inventory_row(
            PR462_EXISTING_RESEARCH_ROWS[0],
            purpose="revenue forward confirmation audit module",
        ),
        production_inventory_row(
            PR462_EXISTING_RESEARCH_ROWS[1],
            purpose="revenue forward confirmation validator",
            allowed_workflows=(
                f"{pr_safe.PR_VALIDATION_WORKFLOW_PATH};"
                f"{pr_safe.RESEARCH_WORKFLOW_PATH}"
            ),
        ),
    ]
    base_rows.extend(
        (
            production_inventory_row(
                PR462_LIFECYCLE_TARGETS[0],
                owner="repo_infrastructure",
                allowed_workflows="",
                purpose="formal model data independence audit builder",
            ),
            production_inventory_row(
                PR462_LIFECYCLE_TARGETS[1],
                purpose="model-owned revenue research producer",
            ),
        )
    )
    for path in PR462_CONTROL_PATHS:
        owner, kind = pr_safe.RESEARCH_CONTROL_PYTHON_ALLOWLIST[path]
        base_rows.append(
            production_inventory_row(
                path,
                kind=kind,
                owner=owner,
                allowed_workflows="",
                purpose="registered research control-plane regression",
            )
        )
    base_rows.append(
        production_inventory_row(
            PR462_PRODUCTION_SENTINEL,
            owner="daily_production",
            allowed_workflows=".github/workflows/daily_full_pipeline.yml",
            purpose="formal daily production sentinel",
        )
    )
    current_rows = [dict(row) for row in base_rows]
    current_rows[0]["purpose"] = "projection-bound forward audit module"
    current_rows[1]["purpose"] = "projection-bound forward validator"
    for path in PR462_RESEARCH_PRODUCERS:
        current_rows.append(production_inventory_row(path))
    for path in PR462_RESEARCH_VALIDATORS:
        current_rows.append(
            production_inventory_row(
                path,
                allowed_workflows=(
                    f"{pr_safe.PR_VALIDATION_WORKFLOW_PATH};"
                    f"{pr_safe.RESEARCH_WORKFLOW_PATH}"
                ),
            )
        )
    for path in PR462_RESEARCH_TESTS:
        current_rows.append(
            production_inventory_row(
                path,
                kind="test_python",
                allowed_workflows="",
            )
        )
    write_csv(repository_root / pr_safe.PRODUCTION_INVENTORY_PATH, current_rows)

    validator_tests = {
        PR462_RESEARCH_VALIDATORS[0]: PR462_RESEARCH_TESTS[0],
        PR462_RESEARCH_VALIDATORS[1]: PR462_RESEARCH_TESTS[4],
        PR462_RESEARCH_VALIDATORS[2]: PR462_RESEARCH_TESTS[2],
    }
    base_lifecycle_rows = [
        lifecycle_inventory_row(path, kind="python")
        for path in PR462_EXISTING_RESEARCH_ROWS
    ]
    base_lifecycle_rows.extend(
        (
            lifecycle_inventory_row(
                PR462_LIFECYCLE_TARGETS[0],
                kind="python",
                owner="repo_infrastructure",
            ),
            lifecycle_inventory_row(
                PR462_LIFECYCLE_TARGETS[1],
                kind="python",
            ),
        )
    )
    base_lifecycle_rows[2]["reads_artifact"] = PR462_LEGACY_RESEARCH_ARTIFACT
    base_lifecycle_rows[3]["reads_artifact"] = PR462_LEGACY_RESEARCH_ARTIFACT
    base_lifecycle_rows.extend(
        lifecycle_inventory_row(
            path,
            kind=pr_safe.RESEARCH_CONTROL_PYTHON_ALLOWLIST[path][1],
            owner=pr_safe.RESEARCH_CONTROL_PYTHON_ALLOWLIST[path][0],
        )
        for path in PR462_CONTROL_PATHS
    )
    base_lifecycle_rows.append(
        lifecycle_inventory_row(
            PR462_PRODUCTION_SENTINEL,
            kind="python",
            owner="daily_production",
        )
    )
    lifecycle_rows = [dict(row) for row in base_lifecycle_rows]
    lifecycle_rows[2]["reads_artifact"] = (
        f"{PR462_LEGACY_RESEARCH_ARTIFACT};{PR462_REPLACEMENT_RESEARCH_CONFIG}"
    )
    lifecycle_rows[3]["reads_artifact"] = (
        f"{PR462_REPLACEMENT_RESEARCH_CONFIG};"
        f"{PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG}"
    )
    lifecycle_rows.extend(
        lifecycle_inventory_row(path, kind="python")
        for path in PR462_RESEARCH_PRODUCERS
    )
    lifecycle_rows.extend(
        lifecycle_inventory_row(
            path,
            kind="python",
            tested_by=validator_tests[path],
        )
        for path in PR462_RESEARCH_VALIDATORS
    )
    lifecycle_rows.extend(
        lifecycle_inventory_row(path, kind="test_python")
        for path in PR462_RESEARCH_TESTS
    )
    write_csv(
        repository_root / pr_safe.LIFECYCLE_INVENTORY_PATH,
        lifecycle_rows,
    )

    workflow_test_path = (
        repository_root
        / "tests/test_daily_model_maintenance_pr_validation_workflow.py"
    )
    workflow_test_path.parent.mkdir(parents=True, exist_ok=True)
    asserted_path_patterns = (
        ("        'config/revenue_unreacted_range_*.csv',\n")
        if include_config_filter_assertion
        else ""
    ) + "        'tests/test_validate_revenue_unreacted_range_*.py',\n"
    workflow_test_path.write_text(
        "from pathlib import Path\n\n"
        "WORKFLOW = Path('.github/workflows/daily_model_maintenance_pr_validation.yml')\n\n"
        "def test_revenue_research_paths_are_asserted() -> None:\n"
        "    text = WORKFLOW.read_text(encoding='utf-8')\n"
        "    required_patterns = (\n"
        + asserted_path_patterns
        + "    )\n"
        "    for pattern in required_patterns:\n"
        "        assert pattern in text\n"
        "    required_commands = (\n"
        + "".join(f"        'python {path}',\n" for path in PR462_RESEARCH_VALIDATORS)
        + "    )\n"
        "    for command in required_commands:\n"
        "        assert command in text\n"
        "    required_tests = (\n"
        + "".join(f"        '{path}',\n" for path in PR462_RESEARCH_TESTS)
        + "    )\n"
        "    for path in required_tests:\n"
        "        assert path in text\n",
        encoding="utf-8",
    )
    new_python_paths = {
        *PR462_RESEARCH_PRODUCERS,
        *PR462_RESEARCH_VALIDATORS,
        *PR462_RESEARCH_TESTS,
    }
    for path in (
        *new_python_paths,
        *PR462_EXISTING_RESEARCH_ROWS,
        *PR462_LIFECYCLE_TARGETS,
        *PR462_CONTROL_PATHS,
        PR462_PRODUCTION_SENTINEL,
    ):
        if path == pr_safe.RESEARCH_WORKFLOW_REGRESSION_TEST_PATH:
            continue
        target = repository_root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("RESEARCH_ONLY = True\n", encoding="utf-8")
    new_config_path = PR462_REPLACEMENT_RESEARCH_CONFIG
    config_path = repository_root / new_config_path
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text("stock_id,canonical_market\n5236,TWSE\n", encoding="utf-8")
    second_config_path = PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG
    second_config = repository_root / second_config_path
    second_config_payload = b"stock_id,comparable\n5236,true\n"
    second_config.write_bytes(second_config_payload)
    lifecycle_authorizations = [
        lifecycle_authorization_row(
            "pr462-additive-lifecycle-test",
            PR462_LIFECYCLE_TARGETS[0],
            base_lifecycle_rows[2]["reads_artifact"],
            lifecycle_rows[2]["reads_artifact"],
            **(lifecycle_authorization_overrides or {}),
        ),
        lifecycle_authorization_row(
            "pr462-rewrite-lifecycle-test",
            PR462_LIFECYCLE_TARGETS[1],
            base_lifecycle_rows[3]["reads_artifact"],
            lifecycle_rows[3]["reads_artifact"],
        ),
    ]
    migration_path = repository_root / pr_safe.LIFECYCLE_SEMANTIC_MIGRATIONS_PATH
    migration_path.parent.mkdir(parents=True, exist_ok=True)
    write_csv(migration_path, lifecycle_authorizations)

    changed_paths = {
        pr_safe.PR_VALIDATION_WORKFLOW_PATH,
        pr_safe.PRODUCTION_INVENTORY_PATH,
        pr_safe.LIFECYCLE_INVENTORY_PATH,
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        new_config_path,
        *new_python_paths,
        *PR462_EXISTING_RESEARCH_ROWS,
        PR462_LIFECYCLE_TARGETS[1],
        *PR462_CONTROL_PATHS,
    }
    base_payloads = {
        pr_safe.PR_VALIDATION_WORKFLOW_PATH: base_workflow.encode("utf-8"),
        pr_safe.PRODUCTION_INVENTORY_PATH: csv_payload(base_rows),
        pr_safe.LIFECYCLE_INVENTORY_PATH: csv_payload(base_lifecycle_rows),
        pr_safe.LIFECYCLE_SEMANTIC_MIGRATIONS_PATH: csv_payload(
            lifecycle_authorizations
        ),
        pr_safe.BACKGROUND_DATA_REGISTRY_PATH: csv_payload(
            [
                {
                    "data_family_id": "revenue_unreacted_range_fixture",
                    "scope": "model_research_output",
                    "owner_lane": "daily_model_maintenance",
                    "producer": PR462_LIFECYCLE_TARGETS[1],
                    "artifact_path": "output/latest/research_backtest/fixture.csv",
                    "source_artifacts": second_config_path,
                    "consumer_surfaces": "research_backtest",
                    "consumer_models": "revenue_unreacted_range",
                    "point_in_time_status": "research_only",
                    "allowed_use": "research fixture",
                    "forbidden_use": "do not use in production",
                    "validator": PR462_RESEARCH_VALIDATORS[0],
                    "retention_policy": "keep",
                    "cleanup_status": "active",
                    "notes": "base-owned fixture governance",
                }
            ]
        ),
        second_config_path: second_config_payload,
    }
    monkeypatch.setattr(
        pr_safe,
        "git_blob_at_ref",
        lambda _ref, path, **_kwargs: base_payloads.get(path),
    )
    monkeypatch.setattr(
        pr_safe,
        "git_path_exists_at_ref",
        lambda _ref, path, **_kwargs: False
        if path in {*new_python_paths, new_config_path}
        else True,
    )
    monkeypatch.setattr(
        pr_safe,
        "git_tree_entry_at_ref",
        lambda _ref, path, **_kwargs: (
            ("100644", "blob", "1" * 40, path)
            if path == second_config_path
            else None
        ),
    )
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (set(changed_paths), []),
    )
    return changed_paths


def test_pr462_exact_additive_research_workflow_and_inventory_shape_is_pr_safe(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors == []
    assert (
        pr_safe.validate_pr_safe_advanced_integrity_contract(
            "base-sha",
            repository_root=historical_replay_repo,
        )
        == []
    )


def test_pr462_current_projection_is_rejected_until_config_filter_is_asserted(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
        include_config_filter_assertion=False,
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors == [
        "PR workflow regression does not assert additive path filter: "
        "config/revenue_unreacted_range_*.csv"
    ]

    workflow_test = (
        historical_replay_repo / pr_safe.RESEARCH_WORKFLOW_REGRESSION_TEST_PATH
    )
    current_source = workflow_test.read_text(encoding="utf-8")
    workflow_test.write_text(
        current_source.replace(
            "        'tests/test_validate_revenue_unreacted_range_*.py',\n",
            "        'config/revenue_unreacted_range_*.csv',\n"
            "        'tests/test_validate_revenue_unreacted_range_*.py',\n",
            1,
        ),
        encoding="utf-8",
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors == []


def test_additive_research_registration_rejects_existing_production_python_change(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    changed_paths.add(PR462_PRODUCTION_SENTINEL)

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any(
        PR462_PRODUCTION_SENTINEL in error
        and "outside the additive research ownership boundary" in error
        for error in errors
    )


def test_additive_research_registration_rejects_existing_lifecycle_governance_drift(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    lifecycle_path = historical_replay_repo / pr_safe.LIFECYCLE_INVENTORY_PATH
    rows = list(csv.DictReader(lifecycle_path.read_text(encoding="utf-8").splitlines()))
    next(
        row for row in rows if row["path"] == PR462_EXISTING_RESEARCH_ROWS[0]
    )["status"] = "legacy_deprecated"
    write_csv(lifecycle_path, rows)

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any(
        "existing lifecycle governance semantics may not change" in error
        and PR462_EXISTING_RESEARCH_ROWS[0] in error
        for error in errors
    )


def test_additive_research_registration_rejects_lifecycle_rewrite_without_migration(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    migration_path = (
        historical_replay_repo / pr_safe.LIFECYCLE_SEMANTIC_MIGRATIONS_PATH
    )
    rows = list(csv.DictReader(migration_path.read_text(encoding="utf-8").splitlines()))
    write_csv(migration_path, rows[1:])
    changed_paths.add(pr_safe.LIFECYCLE_SEMANTIC_MIGRATIONS_PATH)

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any(
        "base-owned lifecycle semantic authorization ledger" in error
        for error in errors
    )


def test_additive_research_registration_accepts_exact_lifecycle_semantic_migration(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors == []
    assert pr_safe.LIFECYCLE_SEMANTIC_MIGRATIONS_PATH not in changed_paths


def test_unchanged_dependency_allows_only_canonical_line_ending_difference(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    dependency = historical_replay_repo / PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG
    dependency.write_bytes(dependency.read_bytes().replace(b"\n", b"\r\n"))

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors == []


@pytest.mark.parametrize("failure_mode", ["content", "mode", "governance"])
def test_additive_research_registration_rejects_unverified_unchanged_dependency(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_mode: str,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    dependency = historical_replay_repo / PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG
    if failure_mode == "content":
        dependency.write_text("stock_id,comparable\n5236,false\n", encoding="utf-8")
    elif failure_mode == "mode":
        monkeypatch.setattr(
            pr_safe,
            "git_tree_entry_at_ref",
            lambda _ref, path, **_kwargs: (
                ("120000", "blob", "1" * 40, path)
                if path == PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG
                else None
            ),
        )
    else:
        original_git_blob = pr_safe.git_blob_at_ref
        ungoverned_registry = csv_payload(
            [
                {
                    "scope": "model_research_output",
                    "producer": PR462_LIFECYCLE_TARGETS[1],
                    "source_artifacts": "",
                    "consumer_surfaces": "research_backtest",
                    "consumer_models": "revenue_unreacted_range",
                    "forbidden_use": "do not use in production",
                    "cleanup_status": "active",
                }
            ]
        )
        monkeypatch.setattr(
            pr_safe,
            "git_blob_at_ref",
            lambda ref, path, **kwargs: (
                ungoverned_registry
                if path == pr_safe.BACKGROUND_DATA_REGISTRY_PATH
                else original_git_blob(ref, path, **kwargs)
            ),
        )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any(
        "research lifecycle addition is not bound to a changed path" in error
        and PR462_SECOND_REPLACEMENT_RESEARCH_CONFIG in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("base_value_sha256", "0" * 64),
        ("current_value_sha256", "1" * 64),
        ("removed_values", "output/latest/research_backtest/not-the-base.csv"),
        ("scope", "production_lifecycle"),
    ],
)
def test_additive_research_registration_rejects_inexact_lifecycle_migration(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    value: str,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
        lifecycle_authorization_overrides={field: value},
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any(
        "base-owned lifecycle authorization does not match exact base/current evidence"
        in error
        for error in errors
    )


def test_additive_research_registration_rejects_dummy_workflow_test_substrings(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    workflow_test = (
        historical_replay_repo / pr_safe.RESEARCH_WORKFLOW_REGRESSION_TEST_PATH
    )
    workflow_test.write_text(
        "\n".join(
            (
                "config/revenue_unreacted_range_*.csv",
                "tests/test_validate_revenue_unreacted_range_*.py",
                *PR462_RESEARCH_VALIDATORS,
                *PR462_RESEARCH_TESTS,
            )
        )
        + "\n",
        encoding="utf-8",
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any("does not assert additive research path" in error for error in errors)
    assert any("does not assert additive path filter" in error for error in errors)


@pytest.mark.parametrize(
    "source",
    [
        (
            "from pathlib import Path\n"
            "WORKFLOW = Path('.github/workflows/daily_model_maintenance_pr_validation.yml')\n"
            "def test_dummy():\n"
            "    text = WORKFLOW.read_text(encoding='utf-8')\n"
            "    required = ('needle',)\n"
            "    for item in required:\n"
            "        assert item in item\n"
        ),
        (
            "from pathlib import Path\n"
            "WORKFLOW = Path('.github/workflows/daily_model_maintenance_pr_validation.yml')\n"
            "def test_dummy():\n"
            "    text = WORKFLOW.read_text(encoding='utf-8')\n"
            "    required = ('needle',)\n"
            "    for item in required:\n"
            "        assert item in 'constant needle'\n"
        ),
        (
            "from pathlib import Path\n"
            "WORKFLOW = Path('.github/workflows/not-the-pr-workflow.yml')\n"
            "def test_dummy():\n"
            "    text = WORKFLOW.read_text(encoding='utf-8')\n"
            "    required = ('needle',)\n"
            "    for item in required:\n"
            "        assert item in text\n"
        ),
        (
            "from pathlib import Path\n"
            "WORKFLOW = Path('.github/workflows/daily_model_maintenance_pr_validation.yml')\n"
            "def test_dummy():\n"
            "    text = 'needle'\n"
            "    assert 'needle' in text\n"
            "    text = WORKFLOW.read_text(encoding='utf-8')\n"
        ),
    ],
)
def test_workflow_regression_ast_rejects_untrusted_membership_rhs(source: str) -> None:
    asserted, errors = pr_safe.asserted_workflow_regression_literals(source)

    assert errors == []
    assert asserted == set()


@pytest.mark.parametrize(
    ("old", "new"),
    [
        (
            "          python scripts/validate_revenue_unreacted_range_existing.py\n",
            "",
        ),
        ("  contents: read\n", "  contents: write\n"),
        (
            "  pull_request:\n    paths:\n",
            "  pull_request:\n    branches: [main]\n    paths:\n",
        ),
        (
            "    runs-on: ubuntu-latest\n",
            "    runs-on: ubuntu-latest\n    timeout-minutes: 10\n",
        ),
        (
            "          python scripts/validate_revenue_unreacted_range_existing.py\n",
            "          python scripts/validate_revenue_unreacted_range_existing.py\n"
            "          python scripts/synthetic_pr_safe_fixture_forbidden_entrypoint.py\n",
        ),
    ],
)
def test_additive_research_registration_rejects_workflow_semantic_mutation(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    old: str,
    new: str,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    workflow_path = historical_replay_repo / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    workflow_path.write_text(
        workflow_path.read_text(encoding="utf-8").replace(old, new, 1),
        encoding="utf-8",
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors


@pytest.mark.parametrize(
    ("path", "column", "value"),
    [
        (PR462_RESEARCH_VALIDATORS[0], "owner", "daily_production"),
        (
            PR462_EXISTING_RESEARCH_ROWS[1],
            "allowed_workflows",
            ".github/workflows/daily_full_pipeline.yml",
        ),
    ],
)
def test_additive_research_registration_rejects_inventory_semantic_mutation(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    path: str,
    column: str,
    value: str,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    inventory_path = historical_replay_repo / pr_safe.PRODUCTION_INVENTORY_PATH
    rows = list(csv.DictReader(inventory_path.read_text(encoding="utf-8").splitlines()))
    next(row for row in rows if row["path"] == path)[column] = value
    write_csv(inventory_path, rows)

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert errors


def test_additive_research_registration_rejects_unregistered_new_producer(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    unregistered = "scripts/revenue_unreacted_range_unregistered_producer.py"
    target = historical_replay_repo / unregistered
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("RESEARCH_ONLY = True\n", encoding="utf-8")
    changed_paths.add(unregistered)
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (set(changed_paths), []),
    )
    original_exists = pr_safe.git_path_exists_at_ref
    monkeypatch.setattr(
        pr_safe,
        "git_path_exists_at_ref",
        lambda ref, path, **kwargs: (
            False if path == unregistered else original_exists(ref, path, **kwargs)
        ),
    )

    recognized, errors = pr_safe.validate_additive_research_validation_registration(
        "base-sha",
        changed_paths,
        {
            pr_safe.PR_VALIDATION_WORKFLOW_PATH,
            pr_safe.PRODUCTION_INVENTORY_PATH,
        },
        repository_root=historical_replay_repo,
    )

    assert recognized
    assert any("lacks production inventory" in error for error in errors)


def test_additive_research_registration_cannot_cover_readiness_change(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    changed_paths = install_pr462_additive_research_registration(
        historical_replay_repo,
        monkeypatch,
    )
    changed_paths.add(pr_safe.FRESHNESS_RELATIVE_PATH)
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
    assert "full runtime repo advanced-integrity validation is required" in errors[0]
    assert pr_safe.FRESHNESS_RELATIVE_PATH in errors[0]


def test_additive_research_gate_self_update_is_exact_and_one_time(
    historical_replay_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    helper_path = historical_replay_repo / pr_safe.PR_SAFE_HELPER_PATH
    test_path = historical_replay_repo / pr_safe.SOURCE_IDENTITY_GATE_TEST_PATH
    authorization_path = (
        historical_replay_repo
        / pr_safe.ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH
    )
    helper_path.parent.mkdir(parents=True, exist_ok=True)
    test_path.parent.mkdir(parents=True, exist_ok=True)
    authorization_path.parent.mkdir(parents=True, exist_ok=True)
    current_helper = (
        f"GATE_ID = '{pr_safe.ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID}'\n"
        "def enforce_additive_research_contract() -> bool:\n"
        "    return True\n"
    ).encode("utf-8")
    current_tests = (
        "def test_additive_research_contract_is_fail_closed() -> None:\n"
        "    assert True\n"
    ).encode("utf-8")
    helper_path.write_bytes(current_helper)
    test_path.write_bytes(current_tests)
    base_helper = b"exact additive research gate base helper\n"
    authorization_row = {
        "migration_id": pr_safe.ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID,
        "status": "preauthorized",
        "approval_reference": "user-approved-stage0",
        "base_helper_sha256": pr_safe.canonical_sha256(base_helper),
        "current_helper_sha256": pr_safe.canonical_sha256(current_helper),
        "current_test_sha256": pr_safe.canonical_sha256(current_tests),
        "changed_paths": ";".join(
            sorted(pr_safe.ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS)
        ),
    }
    write_csv(authorization_path, [authorization_row])
    base_authorizations = csv_payload([authorization_row])
    base_payloads = {
        pr_safe.PR_SAFE_HELPER_PATH: base_helper,
        pr_safe.ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH: base_authorizations,
    }
    monkeypatch.setattr(
        pr_safe,
        "git_blob_at_ref",
        lambda _ref, path, **_kwargs: base_payloads.get(path),
    )
    monkeypatch.setattr(
        pr_safe,
        "changed_paths_from_base",
        lambda *_args, **_kwargs: (
            set(pr_safe.ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS),
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

    helper_path.write_bytes(
        current_helper
        + b"\n# marker remains, but this unapproved semantic mutation must fail\n"
    )
    errors = pr_safe.validate_pr_safe_advanced_integrity_contract(
        "base-sha",
        repository_root=historical_replay_repo,
    )
    assert errors
    assert "full runtime repo advanced-integrity validation is required" in errors[0]

    helper_path.write_bytes(current_helper)
    test_path.write_bytes(current_tests + b"\n# unapproved test mutation\n")
    assert not pr_safe.is_additive_research_gate_self_update(
        "base-sha",
        set(pr_safe.ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS),
        {pr_safe.PR_SAFE_HELPER_PATH},
        repository_root=historical_replay_repo,
    )
