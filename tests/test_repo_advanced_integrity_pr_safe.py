from __future__ import annotations

import csv
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
