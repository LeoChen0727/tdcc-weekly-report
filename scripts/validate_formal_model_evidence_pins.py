from __future__ import annotations

import csv
from pathlib import Path

from formal_model_evidence import PIN_REGISTRY, ROOT, load_evidence_pins, validate_evidence_pin


CONTRACT_REGISTRY = ROOT / "config/stock_model_contract_registry.csv"
CONDITION_SPEC_REGISTRY = ROOT / "config/daily_model_condition_spec.csv"
SURFACE_REGISTRY = ROOT / "config/model_surface_registry.csv"

REVENUE_MODEL_ID = "revenue_unreacted_range"
LEGACY_REVENUE_PHASE = "legacy_v2_no_pin"
PREPARED_REVENUE_PHASE = "prepared_v3_permissions_false"

ALWAYS_REQUIRED_MODELS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
    "price_pullback_23ema",
}

LEGACY_REVENUE_CONTRACT = {
    "model_name": "Revenue unreacted range",
    "contract_version": "v2",
    "owner_lane": "daily_model_maintenance",
    "production_source_file": "scripts/build_daily_candidate_model_layer.py",
    "condition_function": "cond_revenue_unreacted",
    "score_function": "score_revenue_unreacted",
    "score_profile_id": "revenue_unreacted_range",
    "input_columns": (
        "avg_volume_20d;avg_volume_20d_lots;close;close_1d_ago;close_prev;"
        "cumulative_revenue_yoy;cumulative_yoy_pct;daily_return_calc;downgrade_flags;"
        "event_catalyst_tags;false_breakout_risk;high;high_20;high_20_ex_today;"
        "latest_revenue_yoy;low;low_20;off_60d_low_pct;open;platform_high;platform_low;"
        "prev_close;previous_20d_high;previous_20d_high_ex_today;previous_20d_low;"
        "previous_close;previous_high;prior_20d_high;range_high;return_1d;return_1d_pct;"
        "return_20d;return_20d_pct;return_5d;return_5d_pct;revenue_yoy_pct;"
        "short_platform_high;tdcc_accumulation_signal;tdcc_judge;tdcc_judgement;"
        "tdcc_status;volume_confirmed_breakout;volume_ma20;volume_ma20_lots;volume_ratio;"
        "warrant_flow_signal;warrant_status"
    ),
    "output_columns": (
        "signal_date;stock_id;stock_name;report_bucket;model_id;model_name_zh;model_score;"
        "model_rank;display_rank;score_components;risk_penalty_tags;risk_tags;"
        "next_confirmation;report_line;selection_semantics"
    ),
    "pdf_visibility": "pdf_core_model",
    "approved_for_daily_pdf": "true",
    "approved_for_tdcc_weekly_pdf": "false",
    "approved_for_individual_pdf": "false",
    "research_baseline_required": "true",
    "promotion_required": "true",
    "effective_from": "2026-07-16",
    "deprecated_after": "none",
    "change_reason": (
        "financial_statement_features_fail_closed_until_historical_pit_and_"
        "pre_v2_history_quarantined_2026-07-16"
    ),
}

PREPARED_REVENUE_CONTRACT = {
    "model_name": "Revenue unreacted range",
    "contract_version": "v3",
    "owner_lane": "daily_model_maintenance",
    "production_source_file": "scripts/build_daily_revenue_unreacted_range_operation_section.py",
    "condition_function": "_selected_source_mid_falling",
    "score_function": "build_operation_section",
    "score_profile_id": "revenue_unreacted_range_source_mid_falling_v2_frozen_no_score",
    "input_columns": (
        "stock_id;stock_name;revenue_period;source_table_date;latest_revenue_yoy_pct;"
        "cumulative_revenue_yoy_pct;point_in_time_status;research_join_allowed;"
        "revenue_numerical_anomaly_flag;date;open;high;low;close;theme_mainstream_label;"
        "primary_theme;industry"
    ),
    "output_columns": (
        "model_id;model_variant_id;operation_module_id;adapter_schema_version;"
        "lifecycle_contract_version;approval_status;pdf_view;pdf_section;row_type;"
        "operation_asof_date;report_line;operation_key;stock_id;stock_name;lifecycle_state;"
        "row_action_status;buy_rank_eligible;signal_date;confirmation_date;entry_date;"
        "entry_price;exit_date;exit_price;financial_statement_scope;source_artifacts;"
        "row_canonical_sha256"
    ),
    "pdf_visibility": "pdf_core_model",
    "approved_for_daily_pdf": "false",
    "approved_for_tdcc_weekly_pdf": "false",
    "approved_for_individual_pdf": "false",
    "research_baseline_required": "true",
    "promotion_required": "true",
    "effective_from": "2026-08-31",
    "deprecated_after": "none",
    "change_reason": (
        "source_mid_falling_v2_contract_prepared_permissions_false_"
        "legacy_generic_selector_retired_2026-08-31"
    ),
}

LEGACY_REVENUE_CONDITION = {
    "production_source": "ModelSpec",
    "condition_function": "cond_revenue_unreacted",
    "score_function": "score_revenue_unreacted",
    "score_profile_id": "revenue_unreacted_range",
    "research_baseline_status": "proxy_only",
    "operation_contract": "none",
}

PREPARED_REVENUE_CONDITION = {
    "production_source": "dedicated_operation_adapter_v2",
    "condition_function": "_selected_source_mid_falling",
    "score_function": "build_operation_section",
    "score_profile_id": "revenue_unreacted_range_source_mid_falling_v2_frozen_no_score",
    "research_baseline_status": "proxy_only",
    "operation_contract": "revenue_unreacted_range_source_mid_falling_v2_operation_v2",
}

LEGACY_REVENUE_SURFACE = {
    "surface_name": "Revenue unreacted range",
    "surface_type": "stock_entry_model",
    "selection_level": "individual_stock",
    "owning_lane": "daily_model_maintenance",
    "supporting_lanes": (
        "research_backtest;daily_pdf_production;tdcc_weekly_report;individual_pdf_report"
    ),
    "formal_contract_file": "config/stock_model_contract_registry.csv",
    "primary_source_file": "scripts/build_daily_candidate_model_layer.py",
    "implementation_sources": "scripts/build_daily_candidate_model_layer.py",
    "consumer_surfaces": "daily_pdf;research_backtest",
    "approved_for_daily_pdf": "true",
    "approved_for_tdcc_weekly_pdf": "false",
    "approved_for_individual_pdf": "false",
    "stock_entry_signal": "true",
    "research_parity_status": "warning_research_variant_only",
    "promotion_required": "true",
    "effective_from": "2026-06-22",
    "deprecated_after": "none",
    "change_reason": "initial_model_surface_registry",
    "notes": (
        "Research proxy is broad because historical revenue panel is incomplete; "
        "do not tune production directly from proxy stats."
    ),
}

PREPARED_REVENUE_SURFACE = {
    "surface_name": "Revenue unreacted range",
    "surface_type": "stock_entry_model",
    "selection_level": "individual_stock",
    "owning_lane": "daily_model_maintenance",
    "supporting_lanes": "research_backtest;daily_pdf_production",
    "formal_contract_file": "config/stock_model_contract_registry.csv",
    "primary_source_file": "scripts/build_daily_revenue_unreacted_range_operation_section.py",
    "implementation_sources": (
        "scripts/build_daily_revenue_unreacted_range_operation_section.py;"
        "scripts/validate_daily_revenue_unreacted_range_operation_section.py;"
        "scripts/generate_chatgpt_side_daily_reports.py"
    ),
    "consumer_surfaces": "daily_pdf;research_backtest",
    "approved_for_daily_pdf": "false",
    "approved_for_tdcc_weekly_pdf": "false",
    "approved_for_individual_pdf": "false",
    "stock_entry_signal": "true",
    "research_parity_status": "warning_research_variant_only",
    "promotion_required": "true",
    "effective_from": "2026-08-31",
    "deprecated_after": "none",
    "change_reason": "legacy_generic_runtime_retired_v2_promotion_candidate_preparation_2026-08-31",
    "notes": (
        "Legacy v1 remains immutable audit code and evidence but is unreachable from generic "
        "daily selection warrant sync and PDF. The frozen source_mid_falling v2 operation "
        "contract and evidence pin are promotion-candidate preparation only; all production "
        "Daily PDF presentation and formal-use permissions remain false until exact parity "
        "sync and final activation. Monthly revenue only; EPS gross margin operating margin "
        "operating income non-operating income net income and quarterly or annual statements "
        "are excluded."
    ),
}

PREPARED_REVENUE_PIN = {
    "approval_version": (
        "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
    ),
    "evidence_path": (
        "config/approved_operation_evidence/"
        "revenue_unreacted_range_source_mid_falling_"
        "frozen_rule_launch_evidence_v1_20260830_manifest.csv"
    ),
    "evidence_format": "csv",
    "evidence_version": (
        "revenue_unreacted_range_source_mid_falling_"
        "frozen_rule_launch_evidence_v1_20260830"
    ),
    "evidence_version_column": "evidence_version",
    "canonical_sha256": "4890147988797f8d0e7a27777d400514b423b679f108565675309ec2e83161fb",
    "owner_lane": "daily_model_maintenance",
    "pin_status": "pinned_formal_evidence",
    "notes": (
        "Canonical semantic CSV hash pins the immutable frozen-rule launch manifest; "
        "approval remains provisional and OOS-unconfirmed."
    ),
}


def _read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise RuntimeError(f"missing formal evidence phase registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise RuntimeError(f"formal evidence phase registry has no header: {path}")
        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise RuntimeError(f"formal evidence phase registry has duplicate headers: {path}")
        rows: list[dict[str, str]] = []
        for row_number, row in enumerate(reader, start=2):
            if None in row:
                raise RuntimeError(
                    f"formal evidence phase registry row has values without headers: "
                    f"{path}:{row_number}"
                )
            rows.append({key: (value or "").strip() for key, value in row.items()})
        return rows


def _single_revenue_row(path: Path, id_column: str) -> tuple[dict[str, str] | None, list[str]]:
    try:
        rows = _read_rows(path)
    except RuntimeError as exc:
        return None, [str(exc)]
    if not rows or id_column not in rows[0]:
        return None, [f"formal evidence phase registry missing {id_column}: {path}"]
    matches = [row for row in rows if row.get(id_column) == REVENUE_MODEL_ID]
    if len(matches) != 1:
        display_path = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        return None, [
            f"{display_path} must contain exactly one {REVENUE_MODEL_ID} row; "
            f"actual={len(matches)}"
        ]
    return matches[0], []


def _matches(row: dict[str, str], expected: dict[str, str], id_column: str) -> bool:
    actual = {field: value for field, value in row.items() if field != id_column}
    return actual == expected


def _classify_revenue_evidence_phase(
    contract_row: dict[str, str],
    condition_row: dict[str, str],
    surface_row: dict[str, str],
) -> str | None:
    if (
        _matches(contract_row, LEGACY_REVENUE_CONTRACT, "model_id")
        and _matches(condition_row, LEGACY_REVENUE_CONDITION, "model_id")
        and _matches(surface_row, LEGACY_REVENUE_SURFACE, "surface_id")
    ):
        return LEGACY_REVENUE_PHASE
    if (
        _matches(contract_row, PREPARED_REVENUE_CONTRACT, "model_id")
        and _matches(condition_row, PREPARED_REVENUE_CONDITION, "model_id")
        and _matches(surface_row, PREPARED_REVENUE_SURFACE, "surface_id")
    ):
        return PREPARED_REVENUE_PHASE
    return None


def _validate_prepared_revenue_pin(raw_pin_rows: list[dict[str, str]]) -> list[str]:
    revenue_rows = [row for row in raw_pin_rows if row.get("model_id") == REVENUE_MODEL_ID]
    if len(revenue_rows) != 1:
        return [
            f"{PREPARED_REVENUE_PHASE} requires exactly one {REVENUE_MODEL_ID} evidence pin; "
            f"actual={len(revenue_rows)}"
        ]
    row = revenue_rows[0]
    actual_pin = {field: value for field, value in row.items() if field != "model_id"}
    if actual_pin == PREPARED_REVENUE_PIN:
        return []
    errors: list[str] = []
    for field in sorted(set(actual_pin) | set(PREPARED_REVENUE_PIN)):
        actual = actual_pin.get(field, "<missing>")
        expected = PREPARED_REVENUE_PIN.get(field, "<unexpected>")
        if actual != expected:
            errors.append(
                f"{REVENUE_MODEL_ID} prepared evidence pin {field} mismatch: "
                f"expected={expected}; actual={actual}"
            )
    return errors


def validate(
    *,
    pin_registry: Path = PIN_REGISTRY,
    contract_registry: Path = CONTRACT_REGISTRY,
    condition_spec_registry: Path = CONDITION_SPEC_REGISTRY,
    surface_registry: Path = SURFACE_REGISTRY,
    evidence_root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    try:
        pins = load_evidence_pins(pin_registry)
        raw_pin_rows = _read_rows(pin_registry)
    except RuntimeError as exc:
        return [str(exc)]

    contract_row, contract_errors = _single_revenue_row(contract_registry, "model_id")
    condition_row, condition_errors = _single_revenue_row(condition_spec_registry, "model_id")
    surface_row, surface_errors = _single_revenue_row(surface_registry, "surface_id")
    errors.extend(contract_errors)
    errors.extend(condition_errors)
    errors.extend(surface_errors)

    phase: str | None = None
    if contract_row is not None and condition_row is not None and surface_row is not None:
        phase = _classify_revenue_evidence_phase(contract_row, condition_row, surface_row)
        if phase is None:
            errors.append(
                "unsupported or mixed revenue formal evidence phase: revenue contract, "
                "condition spec, and model surface must exactly match legacy_v2_no_pin "
                "or prepared_v3_permissions_false"
            )

    expected_models = set(ALWAYS_REQUIRED_MODELS)
    if phase == PREPARED_REVENUE_PHASE:
        expected_models.add(REVENUE_MODEL_ID)
        errors.extend(_validate_prepared_revenue_pin(raw_pin_rows))

    model_ids = [pin.model_id for pin in pins]
    duplicates = sorted({model_id for model_id in model_ids if model_ids.count(model_id) > 1})
    if duplicates:
        errors.append(f"duplicate formal model evidence pins: {duplicates}")
    missing = sorted(expected_models - set(model_ids))
    extra = sorted(set(model_ids) - expected_models)
    if missing:
        errors.append(f"missing formal model evidence pins: {missing}")
    if extra:
        errors.append(f"unexpected formal model evidence pins: {extra}")
    for pin in pins:
        errors.extend(validate_evidence_pin(pin, evidence_root))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"formal model evidence pin validation passed: {PIN_REGISTRY.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
