from __future__ import annotations

import copy
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_operation_adapter as adapter  # noqa: E402
import validate_revenue_unreacted_range_operation_adapter as validator  # noqa: E402


def _event(
    operation_key: str,
    state: str,
    event_date: str,
    *,
    stock_id: str = "2408",
    report_line: str = "mainstream",
    prior_confirmed_operation_key: str = "",
    entry_date: str = "",
    exit_date: str = "",
) -> dict[str, str]:
    return {
        "model_id": adapter.MODEL_ID,
        "model_variant_id": adapter.MODEL_VARIANT_ID,
        "operation_key": operation_key,
        "report_line": report_line,
        "stock_id": stock_id,
        "event_date": event_date,
        "lifecycle_state": state,
        "prior_confirmed_operation_key": prior_confirmed_operation_key,
        "entry_date": entry_date,
        "exit_date": exit_date,
    }


def _valid_completed_events(operation_key: str = "op-1") -> list[dict[str, str]]:
    return [
        _event(operation_key, "pending_confirmation", "20260803"),
        _event(operation_key, "confirmed_operation", "20260804"),
        _event(
            operation_key,
            "active_operation",
            "20260805",
            prior_confirmed_operation_key=operation_key,
            entry_date="20260805",
        ),
        _event(
            operation_key,
            "exited_operation",
            "20260915",
            exit_date="20260915",
        ),
    ]


def test_disabled_adapter_builds_two_report_lines_times_four_exact_empty_sections() -> None:
    rows = adapter.build_disabled_empty_rows()

    assert len(rows) == 8
    assert [
        (row["report_line"], row["adapter_section"])
        for row in rows
    ] == [
        (report_line, section)
        for report_line in adapter.REPORT_LINES
        for section in adapter.ADAPTER_SECTIONS
    ]
    assert {
        row["adapter_section"]: row["empty_text_zh"]
        for row in rows[:4]
    } == adapter.SECTION_EMPTY_TEXT_ZH
    adapter.validate_disabled_adapter_rows(rows)


def test_disabled_adapter_has_fixed_close_only_no_stop_d30_contract() -> None:
    row = adapter.build_disabled_empty_rows()[0]

    assert row["rule_spec_id"] == "revenue_unreacted_range_source_mid_falling_d30_v1"
    assert row["rule_canonical_sha256"] == (
        "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
    )
    assert row["selection_policy"] == "fixed_preselected_no_reselection"
    assert row["holdout_use_policy"] == "natural_maturity_observation_only_no_tuning"
    assert row["confirmation_offset_trading_days"] == 1
    assert row["entry_offset_trading_days"] == 2
    assert row["holding_days"] == 30
    assert row["holding_session_index_offset"] == 29
    assert row["entry_price_basis"] == "analysis_open"
    assert row["exit_price_basis"] == "fixed_future_close"
    assert row["price_confirmation_basis"] == "close_only"
    assert row["stop_policy_id"] == "none_no_stop_reference"


def test_disabled_adapter_permissions_are_all_false_and_no_data_rows() -> None:
    rows = adapter.build_disabled_empty_rows()

    assert {row["row_type"] for row in rows} == {"empty_state"}
    for field_name in adapter.PERMISSION_FIELDS:
        assert {row[field_name] for row in rows} == {False}
    assert all(not row["stock_id"] for row in rows)
    assert all(not row["operation_key"] for row in rows)


def test_disabled_adapter_rejects_duplicate_and_mixed_empty_data_rows() -> None:
    rows = [dict(row) for row in adapter.build_disabled_empty_rows()]
    rows[-1] = dict(rows[0])
    with pytest.raises(adapter.AdapterContractError, match="duplicate"):
        adapter.validate_disabled_adapter_rows(rows)

    rows = [dict(row) for row in adapter.build_disabled_empty_rows()]
    rows[0]["row_type"] = "data"
    with pytest.raises(adapter.AdapterContractError, match="must remain empty_state"):
        adapter.validate_disabled_adapter_rows(rows)


def test_disabled_adapter_rejects_schema_and_permission_drift() -> None:
    rows = [dict(row) for row in adapter.build_disabled_empty_rows()]
    rows[0]["eps"] = "1.00"
    with pytest.raises(adapter.AdapterContractError, match="schema mismatch"):
        adapter.validate_disabled_adapter_rows(rows)

    rows = [dict(row) for row in adapter.build_disabled_empty_rows()]
    rows[0]["production_allowed"] = True
    with pytest.raises(adapter.AdapterContractError, match="production_allowed"):
        adapter.validate_disabled_adapter_rows(rows)


@pytest.mark.parametrize(
    "field_name",
    [
        "eps",
        "gross_margin",
        "operating_margin",
        "operating_income",
        "non_operating_income",
        "net_income",
        "quarterly_financial_statement",
        "annual_financial_statement",
    ],
)
def test_monthly_revenue_boundary_rejects_financial_statement_fields(
    field_name: str,
) -> None:
    with pytest.raises(adapter.AdapterContractError, match="monthly-revenue-only"):
        adapter.validate_financial_statement_boundary([field_name])


def test_lifecycle_accepts_selected_confirmed_active_exit_chain() -> None:
    adapter.validate_lifecycle_events(_valid_completed_events())


def test_lifecycle_rejects_active_without_selected_confirmation() -> None:
    events = [
        _event(
            "op-1",
            "active_operation",
            "20260805",
            prior_confirmed_operation_key="op-1",
            entry_date="20260805",
        )
    ]
    with pytest.raises(adapter.AdapterContractError, match="lacks prior selected confirmation"):
        adapter.validate_lifecycle_events(events)


def test_lifecycle_rejects_unranked_confirmation_becoming_active() -> None:
    events = [
        _event("op-1", "pending_confirmation", "20260803"),
        _event("op-1", "confirmed_unranked_operation", "20260804"),
        _event(
            "op-1",
            "active_operation",
            "20260805",
            prior_confirmed_operation_key="op-1",
            entry_date="20260805",
        ),
    ]
    with pytest.raises(adapter.AdapterContractError, match="lacks prior selected confirmation"):
        adapter.validate_lifecycle_events(events)


def test_lifecycle_rejects_same_stock_overlap() -> None:
    events = _valid_completed_events("op-1")[:-1]
    events.extend(
        [
            _event("op-2", "pending_confirmation", "20260806"),
            _event("op-2", "confirmed_operation", "20260807"),
        ]
    )
    with pytest.raises(adapter.AdapterContractError, match="while operation op-1 is active"):
        adapter.validate_lifecycle_events(events)


def test_lifecycle_rejects_confirmed_and_active_on_same_date() -> None:
    events = [
        _event("op-1", "pending_confirmation", "20260803"),
        _event("op-1", "confirmed_operation", "20260804"),
        _event(
            "op-1",
            "active_operation",
            "20260804",
            prior_confirmed_operation_key="op-1",
            entry_date="20260804",
        ),
    ]
    with pytest.raises(adapter.AdapterContractError, match="same date"):
        adapter.validate_lifecycle_events(events)


def test_lifecycle_rejects_same_day_reentry_after_exit() -> None:
    events = _valid_completed_events("op-1")
    events.extend(
        [
            _event("op-2", "pending_confirmation", "20260914"),
            _event("op-2", "confirmed_operation", "20260915"),
        ]
    )
    with pytest.raises(adapter.AdapterContractError, match="after prior exit"):
        adapter.validate_lifecycle_events(events)


def test_lifecycle_allows_reentry_only_after_prior_exit() -> None:
    events = _valid_completed_events("op-1")
    events.extend(
        [
            _event("op-2", "pending_confirmation", "20260916"),
            _event("op-2", "confirmed_operation", "20260917"),
            _event(
                "op-2",
                "active_operation",
                "20260918",
                prior_confirmed_operation_key="op-2",
                entry_date="20260918",
            ),
        ]
    )
    adapter.validate_lifecycle_events(events)


def test_lifecycle_rejects_non_monotonic_revival() -> None:
    events = _valid_completed_events("op-1")
    events.append(
        _event(
            "op-1",
            "active_operation",
            "20260916",
            prior_confirmed_operation_key="op-1",
            entry_date="20260805",
        )
    )
    with pytest.raises(adapter.AdapterContractError, match="not monotonic"):
        adapter.validate_lifecycle_events(events)


def test_validator_accepts_disabled_preparation_and_detects_runtime_writer(
    tmp_path: Path,
) -> None:
    assert validator.validate_disabled_preparation(validator.DEFAULT_MODULE) == []

    unsafe = tmp_path / "unsafe_adapter.py"
    unsafe.write_text(
        validator.DEFAULT_MODULE.read_text(encoding="utf-8")
        + "\nopen('artifact.csv', 'w')\n",
        encoding="utf-8",
    )
    errors = validator.validate_disabled_preparation(unsafe)
    assert any("forbidden writer call open" in error for error in errors)


def test_validator_cli_passes_disabled_and_fails_production_approval() -> None:
    script = ROOT / "scripts/validate_revenue_unreacted_range_operation_adapter.py"
    disabled = subprocess.run(
        [sys.executable, str(script), "--phase", "disabled-preparation"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    production = subprocess.run(
        [sys.executable, str(script), "--phase", "production-approval"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert disabled.returncode == 0, disabled.stdout + disabled.stderr
    assert "no runtime artifact" in disabled.stdout
    assert production.returncode == 1
    assert "production approval" in production.stdout


def test_module_has_no_artifact_writer_or_runtime_output_path() -> None:
    source = validator.DEFAULT_MODULE.read_text(encoding="utf-8")
    assert "output/latest" not in source
    assert "docs/latest" not in source
    assert "daily_revenue_unreacted_range_operation_section_latest.csv" not in source
    assert not hasattr(adapter, "main")
    assert not any(name.startswith("write_") for name in dir(adapter))
