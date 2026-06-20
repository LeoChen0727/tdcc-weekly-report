from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_stock_model_contract_registry as validator


ROOT = Path(__file__).resolve().parents[1]


def contract_rows() -> list[dict[str, str]]:
    path = ROOT / "config" / "stock_model_contract_registry.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def condition_spec_rows() -> list[dict[str, str]]:
    path = ROOT / "config" / "daily_model_condition_spec.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def test_stock_model_contract_registry_validator_passes() -> None:
    assert validator.main() == 0


def test_stock_model_contract_registry_has_required_schema() -> None:
    rows = contract_rows()

    assert rows
    assert set(validator.REQUIRED_COLUMNS) <= set(rows[0])


def test_stock_model_contract_registry_covers_condition_spec_models() -> None:
    contract_by_model = {row["model_id"]: row for row in contract_rows()}

    for spec in condition_spec_rows():
        model_id = spec["model_id"]
        assert model_id in contract_by_model
        assert contract_by_model[model_id]["condition_function"] == spec["condition_function"]
        assert contract_by_model[model_id]["score_function"] == spec["score_function"]
        assert contract_by_model[model_id]["score_profile_id"] == spec["score_profile_id"]


def test_stock_model_contract_registry_approval_columns_are_booleans() -> None:
    for row in contract_rows():
        for col in validator.APPROVAL_COLUMNS:
            assert row[col] in {"true", "false"}


def test_tdcc_weekly_pdf_approval_is_explicit_allowlist() -> None:
    approved = sorted(
        row["model_id"]
        for row in contract_rows()
        if row["approved_for_tdcc_weekly_pdf"] == "true"
    )

    assert approved == ["tdcc_short_term_continuation_d5_d10"]
