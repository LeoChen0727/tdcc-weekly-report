from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_volume_breakout_operation_section as validator  # noqa: E402


MODEL_IDS = sorted(validator.FORMAL_MODEL_IDS)
CALENDAR = {
    "official_sources": {
        "twse_annual_calendar": {
            "status": "ok",
            "sha256": "a" * 64,
            "covered_years": [2026],
        }
    },
    "scheduled_non_trading_days": ["20261026"],
    "exceptional_non_trading_days": ["20261023"],
}


def management_row(**changes: object) -> dict[str, object]:
    row: dict[str, object] = {field: "" for field in validator.V2_MANAGEMENT_COLUMNS}
    row.update({
        "model_id": MODEL_IDS[0],
        "stock_id": "1234",
        "pdf_section": "active_operation",
        "row_type": "data",
        "operation_asof_date": "20261030",
        "selected_confirmation_date": "20261020",
        "entry_date": "20261021",
        "operation_age_days": "6",
        "row_action_status": "active_operation",
        "stop_reference_price": "9.6",
        "stop_reference_date": "20261030",
        "stop_confirmed_days": "2",
        "holding_days": "6",
        "planned_exit_date": "20261112",
        "planned_exit_date_status": "scheduled_official_calendar",
        "next_action_zh": "每日收盤核對四日停損；未提前停損則第15日收盤出場。",
    })
    row.update(changes)
    return row


def check(row: dict[str, object], calendar: dict | None = None) -> None:
    validator.validate_management_fields(
        pd.DataFrame([row]), calendar_status=CALENDAR if calendar is None else calendar
    )


@pytest.mark.parametrize("model_id", MODEL_IDS)
def test_all_three_models_accept_actual_entry_day_counts_and_calendar(model_id: str) -> None:
    check(management_row(model_id=model_id))


@pytest.mark.parametrize("model_id", MODEL_IDS)
def test_all_three_models_accept_pending_stop_without_inventing_exit(model_id: str) -> None:
    check(management_row(
        model_id=model_id,
        entry_date="20261027",
        holding_days="4",
        operation_age_days="4",
        stop_confirmed_days="4",
        row_action_status="stop_exit_pending_next_open",
        planned_exit_date="20261116",
        stop_confirmation_date="20261030",
        next_action_date="20261102",
        next_action_date_status="scheduled_official_calendar",
        next_action_zh="已連續4日收盤確認；下一交易日開盤停損，實際開盤價待確認。",
    ))


@pytest.mark.parametrize("count", ["", "0"])
def test_confirmed_empty_counts_are_not_missing_actual_fills(count: str) -> None:
    check(management_row(
        pdf_section="confirmed_operation",
        row_action_status="confirmed_buy_candidate",
        selected_confirmation_date="20261030",
        entry_date="",
        operation_age_days="1",
        holding_days=count,
        stop_confirmed_days=count,
        planned_entry_date="20261102",
        planned_exit_date="20261120",
    ))


@pytest.mark.parametrize(("field", "bad"), [
    ("holding_days", "0"),
    ("holding_days", "15"),
    ("holding_days", "6.5"),
    ("stop_confirmed_days", "-1"),
    ("stop_confirmed_days", "7"),
    ("stop_confirmed_days", "4"),
    ("operation_age_days", "7"),
    ("stop_reference_price", "0"),
    ("stop_reference_price", "nan"),
    ("stop_reference_date", "20261029"),
    ("planned_exit_date", "20261113"),
    ("planned_exit_date_status", "unavailable_calendar"),
    ("next_action_date", "20261102"),
    ("stop_confirmation_date", "20261030"),
])
def test_management_contract_rejects_inconsistent_values(field: str, bad: str) -> None:
    with pytest.raises(SystemExit):
        check(management_row(**{field: bad}))


def test_pending_stop_requires_fourth_close_and_visible_next_open_instruction() -> None:
    with pytest.raises(SystemExit):
        check(management_row(row_action_status="stop_exit_pending_next_open"))


def test_missing_calendar_requires_blank_dates_and_unavailable_status() -> None:
    check(management_row(planned_exit_date="", planned_exit_date_status="unavailable_calendar"), {})
    with pytest.raises(SystemExit):
        check(management_row(), {})


@pytest.mark.parametrize("annual_change", [
    {"status": "unavailable"},
    {"sha256": "not-a-source-sha"},
    {"covered_years": [2025]},
])
def test_invalid_or_uncovered_annual_source_cannot_authorize_planned_dates(annual_change: dict) -> None:
    calendar = deepcopy(CALENDAR)
    calendar["official_sources"]["twse_annual_calendar"].update(annual_change)
    with pytest.raises(SystemExit):
        check(management_row(), calendar)
    check(management_row(planned_exit_date="", planned_exit_date_status="unavailable_calendar"), calendar)


def test_pending_and_empty_rows_cannot_acquire_operation_prices() -> None:
    row = management_row(pdf_section="pending_confirmation", holding_days="", stop_confirmed_days="")
    with pytest.raises(SystemExit):
        check(row)
    for field in validator.V2_MANAGEMENT_COLUMNS:
        row[field] = ""
    check(row)
    row["row_type"] = "empty_state"
    row["stop_reference_price"] = "9.6"
    with pytest.raises(SystemExit):
        check(row)


def test_missing_management_column_fails_closed() -> None:
    row = management_row()
    del row["stop_reference_date"]
    with pytest.raises(SystemExit):
        check(row)


def test_unavailable_averages_keep_the_existing_empty_reference_and_reset_policy() -> None:
    check(management_row(stop_reference_price="", stop_confirmed_days="0"))
    with pytest.raises(SystemExit):
        check(management_row(stop_reference_price="", stop_confirmed_days="2"))


def test_calendar_cross_year_without_coverage_does_not_guess_weekdays() -> None:
    assert validator._management_calendar_date(
        CALENDAR, "20261231", 15, include_anchor=True
    ) == ""


def audit_exit_row(**changes: object) -> dict[str, object]:
    row: dict[str, object] = {field: "" for field in validator.V2_MANAGEMENT_AUDIT_COLUMNS}
    row.update({
        "model_id": MODEL_IDS[0],
        "operation_asof_date": "20261030",
        "operation_lifecycle_state": "expired",
        "included_in_daily_adapter": "False",
        "entry_date": "20261001",
        "entry_price": "10",
        "holding_days": "15",
        "exit_date": "20261022",
        "exit_price": "11",
        "exit_reason": "fixed_15d_close",
        "exit_price_basis": "fixed_future_close",
    })
    row.update(changes)
    return row


def test_current_audit_accepts_actual_fixed_close_and_next_open_exits() -> None:
    validator.validate_management_audit_fields(pd.DataFrame([audit_exit_row()]))
    validator.validate_management_audit_fields(pd.DataFrame([audit_exit_row(
        holding_days="5",
        exit_date="20261030",
        exit_reason="sustained_close_below_lower_ma20_ema23_4pct_4d",
        exit_price_basis="next_trading_day_open",
        stop_confirmation_date="20261029",
        stop_confirmed_days="4",
    )]))


@pytest.mark.parametrize("changes", [
    {"exit_date": "20261102"},
    {"exit_date": ""},
    {"exit_price": "0"},
    {"exit_price_basis": "intraday_low"},
    {"holding_days": "16"},
    {"operation_lifecycle_state": "active_operation"},
    {"included_in_daily_adapter": "True"},
])
def test_current_audit_rejects_future_or_inconsistent_actual_exits(changes: dict) -> None:
    with pytest.raises(SystemExit):
        validator.validate_management_audit_fields(pd.DataFrame([audit_exit_row(**changes)]))


def test_pending_stop_audit_keeps_actual_exit_columns_blank() -> None:
    row = audit_exit_row(
        operation_lifecycle_state="active_operation",
        included_in_daily_adapter="True",
        holding_days="4",
        stop_confirmed_days="4",
        stop_confirmation_date="20261030",
        exit_date="", exit_price="", exit_reason="", exit_price_basis="",
    )
    validator.validate_management_audit_fields(pd.DataFrame([row]))
