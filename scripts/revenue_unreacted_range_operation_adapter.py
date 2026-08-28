from __future__ import annotations

"""Disabled operation-adapter preparation for revenue_unreacted_range v2.

This module intentionally has no command-line entrypoint and no filesystem
writer.  It defines the model-owned schema and lifecycle invariants that a
future, separately approved production adapter must satisfy.  The only rows it
can currently build are disabled empty-state rows.
"""

from collections.abc import Iterable, Mapping, Sequence
from typing import Any


MODEL_ID = "revenue_unreacted_range"
MODEL_VARIANT_ID = "source_mid_falling"
MODEL_VARIANT_VERSION = "v2"
OPERATION_MODULE_ID = "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
ADAPTER_SCHEMA_VERSION = "revenue_unreacted_range_operation_section_schema_v1"
LIFECYCLE_CONTRACT_VERSION = "revenue_unreacted_range_lifecycle_v1"
ADAPTER_MODE = "disabled_preparation"
RULE_SPEC_ID = "revenue_unreacted_range_source_mid_falling_d30_v1"
RULE_CANONICAL_SHA256 = (
    "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
)
SELECTION_POLICY = "fixed_preselected_no_reselection"
HOLDOUT_USE_POLICY = "natural_maturity_observation_only_no_tuning"

REPORT_LINES = ("mainstream", "non_mainstream")
ADAPTER_SECTIONS = (
    "pending_confirmation",
    "confirmed_operation",
    "confirmed_unranked_operation",
    "active_operation",
)
SECTION_EMPTY_TEXT_ZH = {
    "pending_confirmation": "目前無待確認列",
    "confirmed_operation": "本日無股票推薦",
    "confirmed_unranked_operation": "目前無已確認但未列入買進排序列",
    "active_operation": "目前無操作中追蹤列",
}

CONFIRMATION_RULE_ID = "d1_analysis_close_above_trigger_analysis_close"
ENTRY_RULE_ID = "d2_analysis_open"
EXIT_RULE_ID = "d30_analysis_close_offset29"
STOP_POLICY_ID = "none_no_stop_reference"
CONFIRMATION_OFFSET_TRADING_DAYS = 1
ENTRY_OFFSET_TRADING_DAYS = 2
HOLDING_DAYS = 30
HOLDING_SESSION_INDEX_OFFSET = 29
ENTRY_PRICE_BASIS = "analysis_open"
EXIT_PRICE_BASIS = "fixed_future_close"
PRICE_CONFIRMATION_BASIS = "close_only"

PERMISSION_FIELDS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
)

# This preparation accepts no candidate or fundamental payload.  These names
# are an explicit fail-closed boundary for any future caller that tries to add
# quarterly/annual financial-statement data to the monthly-revenue model.
FORBIDDEN_FINANCIAL_STATEMENT_FIELDS = frozenset(
    {
        "eps",
        "earnings_per_share",
        "gross_margin",
        "operating_margin",
        "operating_income",
        "non_operating_income",
        "net_income",
        "quarterly_financial_statement",
        "annual_financial_statement",
    }
)

ADAPTER_ROW_COLUMNS = (
    "model_id",
    "model_variant_id",
    "model_variant_version",
    "operation_module_id",
    "adapter_schema_version",
    "lifecycle_contract_version",
    "adapter_mode",
    "rule_spec_id",
    "rule_canonical_sha256",
    "selection_policy",
    "holdout_use_policy",
    "report_line",
    "adapter_section",
    "row_type",
    "empty_text_zh",
    "operation_date",
    "operation_key",
    "stock_id",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "lifecycle_state",
    "prior_confirmed_operation_key",
    "buy_rank_eligible",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
    "confirmation_rule_id",
    "entry_rule_id",
    "exit_rule_id",
    "stop_policy_id",
    "confirmation_offset_trading_days",
    "entry_offset_trading_days",
    "holding_days",
    "holding_session_index_offset",
    "entry_price_basis",
    "exit_price_basis",
    "price_confirmation_basis",
)

LIFECYCLE_EVENT_COLUMNS = (
    "model_id",
    "model_variant_id",
    "operation_key",
    "report_line",
    "stock_id",
    "event_date",
    "lifecycle_state",
    "prior_confirmed_operation_key",
    "entry_date",
    "exit_date",
)

LIFECYCLE_STATES = (
    "pending_confirmation",
    "confirmed_operation",
    "confirmed_unranked_operation",
    "active_operation",
    "exited_operation",
)
_STATE_RANK = {
    "pending_confirmation": 0,
    "confirmed_operation": 1,
    "confirmed_unranked_operation": 1,
    "active_operation": 2,
    "exited_operation": 3,
}


class AdapterContractError(ValueError):
    """Raised when disabled adapter or lifecycle invariants are violated."""


def _text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _date(value: Any, label: str) -> str:
    text = _text(value).replace("-", "").replace("/", "")
    if len(text) != 8 or not text.isdigit():
        raise AdapterContractError(f"{label} must be YYYYMMDD, got {value!r}")
    return text


def _require_exact_columns(row: Mapping[str, Any], columns: Sequence[str], label: str) -> None:
    observed = set(row)
    expected = set(columns)
    missing = sorted(expected - observed)
    extra = sorted(observed - expected)
    if missing or extra:
        raise AdapterContractError(
            f"{label} schema mismatch: missing={missing}; extra={extra}"
        )


def _fixed_metadata() -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "model_variant_id": MODEL_VARIANT_ID,
        "model_variant_version": MODEL_VARIANT_VERSION,
        "operation_module_id": OPERATION_MODULE_ID,
        "adapter_schema_version": ADAPTER_SCHEMA_VERSION,
        "lifecycle_contract_version": LIFECYCLE_CONTRACT_VERSION,
        "adapter_mode": ADAPTER_MODE,
        "rule_spec_id": RULE_SPEC_ID,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "selection_policy": SELECTION_POLICY,
        "holdout_use_policy": HOLDOUT_USE_POLICY,
        "buy_rank_eligible": False,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "production_allowed": False,
        "confirmation_rule_id": CONFIRMATION_RULE_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "stop_policy_id": STOP_POLICY_ID,
        "confirmation_offset_trading_days": CONFIRMATION_OFFSET_TRADING_DAYS,
        "entry_offset_trading_days": ENTRY_OFFSET_TRADING_DAYS,
        "holding_days": HOLDING_DAYS,
        "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
        "entry_price_basis": ENTRY_PRICE_BASIS,
        "exit_price_basis": EXIT_PRICE_BASIS,
        "price_confirmation_basis": PRICE_CONFIRMATION_BASIS,
    }


def build_disabled_empty_rows() -> tuple[dict[str, Any], ...]:
    """Return the eight deterministic in-memory rows allowed in this stage."""

    rows: list[dict[str, Any]] = []
    fixed = _fixed_metadata()
    for report_line in REPORT_LINES:
        for section in ADAPTER_SECTIONS:
            rows.append(
                {
                    **fixed,
                    "report_line": report_line,
                    "adapter_section": section,
                    "row_type": "empty_state",
                    "empty_text_zh": SECTION_EMPTY_TEXT_ZH[section],
                    "operation_date": "",
                    "operation_key": "",
                    "stock_id": "",
                    "signal_date": "",
                    "confirmation_date": "",
                    "entry_date": "",
                    "exit_date": "",
                    "lifecycle_state": "",
                    "prior_confirmed_operation_key": "",
                }
            )
    return tuple(rows)


def validate_financial_statement_boundary(field_names: Iterable[str]) -> None:
    """Reject quarterly/annual financial-statement inputs fail closed."""

    normalized = {_text(name).lower() for name in field_names}
    forbidden = sorted(normalized & FORBIDDEN_FINANCIAL_STATEMENT_FIELDS)
    if forbidden:
        raise AdapterContractError(
            "monthly-revenue-only boundary forbids financial-statement fields: "
            f"{forbidden}"
        )


def validate_disabled_adapter_rows(rows: Sequence[Mapping[str, Any]]) -> None:
    """Validate the disabled schema, empty states, uniqueness, and permissions."""

    expected_fixed = _fixed_metadata()
    if len(rows) != len(REPORT_LINES) * len(ADAPTER_SECTIONS):
        raise AdapterContractError(
            "disabled preparation must contain exactly two report lines times four sections"
        )

    identities: set[tuple[str, str]] = set()
    for index, row in enumerate(rows):
        label = f"adapter row {index}"
        _require_exact_columns(row, ADAPTER_ROW_COLUMNS, label)
        report_line = _text(row.get("report_line"))
        section = _text(row.get("adapter_section"))
        identity = (report_line, section)
        if identity in identities:
            raise AdapterContractError(f"duplicate disabled adapter section: {identity}")
        identities.add(identity)
        if report_line not in REPORT_LINES:
            raise AdapterContractError(f"{label} has unsupported report_line={report_line!r}")
        if section not in ADAPTER_SECTIONS:
            raise AdapterContractError(f"{label} has unsupported adapter_section={section!r}")
        if row.get("row_type") != "empty_state":
            raise AdapterContractError(f"{label} must remain empty_state while disabled")
        if row.get("empty_text_zh") != SECTION_EMPTY_TEXT_ZH[section]:
            raise AdapterContractError(f"{label} empty-state text drift")
        for field_name in (
            "operation_date",
            "operation_key",
            "stock_id",
            "signal_date",
            "confirmation_date",
            "entry_date",
            "exit_date",
            "lifecycle_state",
            "prior_confirmed_operation_key",
        ):
            if _text(row.get(field_name)):
                raise AdapterContractError(
                    f"{label} disabled empty row must not populate {field_name}"
                )
        for field_name, expected in expected_fixed.items():
            if row.get(field_name) != expected:
                raise AdapterContractError(
                    f"{label} {field_name} must be {expected!r}, got {row.get(field_name)!r}"
                )

    expected_identities = {
        (report_line, section)
        for report_line in REPORT_LINES
        for section in ADAPTER_SECTIONS
    }
    if identities != expected_identities:
        raise AdapterContractError(
            f"disabled adapter section coverage drift: {sorted(identities)}"
        )


def validate_lifecycle_events(events: Sequence[Mapping[str, Any]]) -> None:
    """Validate future lifecycle rows without producing any operation output.

    The checks keep the selected v2 semantics fixed: an active operation must
    descend from a selected confirmation, an unranked confirmation can never
    become active, the same stock cannot overlap, and an exited operation can
    never be revived.
    """

    if not events:
        return
    normalized: list[dict[str, str]] = []
    unique_events: set[tuple[str, str, str]] = set()
    for index, raw in enumerate(events):
        label = f"lifecycle event {index}"
        _require_exact_columns(raw, LIFECYCLE_EVENT_COLUMNS, label)
        if _text(raw.get("model_id")) != MODEL_ID:
            raise AdapterContractError(f"{label} model_id scope drift")
        if _text(raw.get("model_variant_id")) != MODEL_VARIANT_ID:
            raise AdapterContractError(f"{label} model_variant_id scope drift")
        operation_key = _text(raw.get("operation_key"))
        stock_id = _text(raw.get("stock_id"))
        report_line = _text(raw.get("report_line"))
        state = _text(raw.get("lifecycle_state"))
        if not operation_key or not stock_id:
            raise AdapterContractError(f"{label} requires operation_key and stock_id")
        if report_line not in REPORT_LINES:
            raise AdapterContractError(f"{label} has unsupported report_line={report_line!r}")
        if state not in LIFECYCLE_STATES:
            raise AdapterContractError(f"{label} has unsupported lifecycle_state={state!r}")
        event_date = _date(raw.get("event_date"), f"{label}.event_date")
        identity = (operation_key, event_date, state)
        if identity in unique_events:
            raise AdapterContractError(f"duplicate lifecycle event: {identity}")
        unique_events.add(identity)
        normalized.append(
            {
                key: _text(raw.get(key))
                for key in LIFECYCLE_EVENT_COLUMNS
            }
            | {"event_date": event_date}
        )

    by_operation: dict[str, list[dict[str, str]]] = {}
    for row in normalized:
        by_operation.setdefault(row["operation_key"], []).append(row)
    for operation_key, operation_rows in by_operation.items():
        operation_rows.sort(key=lambda row: (row["event_date"], _STATE_RANK[row["lifecycle_state"]]))
        stock_keys = {(row["report_line"], row["stock_id"]) for row in operation_rows}
        if len(stock_keys) != 1:
            raise AdapterContractError(
                f"operation {operation_key} cannot change report line or stock: {sorted(stock_keys)}"
            )
        states = [row["lifecycle_state"] for row in operation_rows]
        ranks = [_STATE_RANK[state] for state in states]
        if ranks != sorted(ranks):
            raise AdapterContractError(f"operation {operation_key} lifecycle is not monotonic: {states}")
        if "confirmed_operation" in states and "confirmed_unranked_operation" in states:
            raise AdapterContractError(
                f"operation {operation_key} cannot be both selected and unranked"
            )
        if "active_operation" in states:
            if "confirmed_operation" not in states:
                raise AdapterContractError(
                    f"active operation {operation_key} lacks prior selected confirmation"
                )
            if "confirmed_unranked_operation" in states:
                raise AdapterContractError(
                    f"unranked confirmation {operation_key} must never become active"
                )
            first_active = states.index("active_operation")
            selected_index = states.index("confirmed_operation")
            if selected_index >= first_active:
                raise AdapterContractError(
                    f"active operation {operation_key} must follow selected confirmation"
                )
            selected_date = operation_rows[selected_index]["event_date"]
            active_date = operation_rows[first_active]["event_date"]
            if active_date <= selected_date:
                raise AdapterContractError(
                    f"operation {operation_key} cannot be confirmed and active on the same date"
                )
            for row in operation_rows[first_active:]:
                if row["lifecycle_state"] == "active_operation":
                    if row["prior_confirmed_operation_key"] != operation_key:
                        raise AdapterContractError(
                            f"active operation {operation_key} must reference its selected confirmation"
                        )
                    _date(row["entry_date"], f"operation {operation_key}.entry_date")
                    if row["entry_date"] != row["event_date"]:
                        raise AdapterContractError(
                            f"operation {operation_key} active event_date must equal entry_date"
                        )
        if "exited_operation" in states:
            exit_index = states.index("exited_operation")
            if exit_index != len(states) - 1:
                raise AdapterContractError(f"exited operation {operation_key} must not revive")
            if "active_operation" not in states:
                raise AdapterContractError(
                    f"exited operation {operation_key} lacks prior active operation"
                )
            exit_row = operation_rows[exit_index]
            exit_date = _date(exit_row["exit_date"], f"operation {operation_key}.exit_date")
            if exit_date != exit_row["event_date"]:
                raise AdapterContractError(
                    f"operation {operation_key} exit_date must equal exited event_date"
                )

    state_priority = {state: index for index, state in enumerate(LIFECYCLE_STATES)}
    ordered = sorted(
        normalized,
        key=lambda row: (
            row["event_date"],
            state_priority[row["lifecycle_state"]],
            row["operation_key"],
        ),
    )
    exit_identity_dates = {
        (row["report_line"], row["stock_id"], row["operation_key"]): row["event_date"]
        for row in ordered
        if row["lifecycle_state"] == "exited_operation"
    }
    active_by_stock: dict[tuple[str, str], str] = {}
    last_exit_by_stock: dict[tuple[str, str], str] = {}
    for row in ordered:
        stock_key = (row["report_line"], row["stock_id"])
        operation_key = row["operation_key"]
        state = row["lifecycle_state"]
        if state in {"confirmed_operation", "confirmed_unranked_operation"}:
            same_day_prior_exit = any(
                report_line == row["report_line"]
                and stock_id == row["stock_id"]
                and prior_operation_key != operation_key
                and exit_date == row["event_date"]
                for (
                    report_line,
                    stock_id,
                    prior_operation_key,
                ), exit_date in exit_identity_dates.items()
            )
            if same_day_prior_exit:
                raise AdapterContractError(
                    f"same-stock re-entry confirmation must be after prior exit: {stock_key}"
                )
            existing = active_by_stock.get(stock_key)
            if existing and existing != operation_key:
                raise AdapterContractError(
                    f"same stock cannot be confirmed while operation {existing} is active: {stock_key}"
                )
            previous_exit = last_exit_by_stock.get(stock_key)
            if previous_exit and row["event_date"] <= previous_exit:
                raise AdapterContractError(
                    f"same-stock re-entry confirmation must be after prior exit: {stock_key}"
                )
        elif state == "active_operation":
            existing = active_by_stock.get(stock_key)
            if existing and existing != operation_key:
                raise AdapterContractError(
                    f"same stock has overlapping active operations: {stock_key}"
                )
            active_by_stock[stock_key] = operation_key
        elif state == "exited_operation":
            if active_by_stock.get(stock_key) != operation_key:
                raise AdapterContractError(
                    f"exit has no matching active operation: {stock_key}/{operation_key}"
                )
            del active_by_stock[stock_key]
            last_exit_by_stock[stock_key] = row["event_date"]


def validate_disabled_preparation() -> None:
    """Run the complete in-memory validation for this disabled v1 module."""

    validate_disabled_adapter_rows(build_disabled_empty_rows())
    validate_lifecycle_events(())
