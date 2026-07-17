from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_daily_model_background_data_registry import load_registry, validate_registry  # noqa: E402
from model_data_independence import strict_csv_rows  # noqa: E402


def registry_rows() -> list[dict[str, str]]:
    errors: list[str] = []
    rows = load_registry(errors)
    assert errors == []
    return rows


def test_daily_model_background_data_registry_passes() -> None:
    assert validate_registry(registry_rows()) == []


def test_model_specific_family_cannot_be_all_models() -> None:
    rows = deepcopy(registry_rows())
    for row in rows:
        if row["data_family_id"] == "neckline_context_interpretation":
            row["consumer_models"] = "all_models"
            break

    errors = validate_registry(rows)

    assert any("neckline_context_interpretation" in error for error in errors)
    assert any("model-specific family must list specific consumer_models" in error for error in errors)


def test_revenue_panel_must_stay_coverage_limited() -> None:
    rows = deepcopy(registry_rows())
    for row in rows:
        if row["data_family_id"] == "monthly_revenue_point_in_time_panel":
            row["forbidden_use"] = "use as a formal gate"
            row["validator"] = "not_ready_validator.py"
            break

    errors = validate_registry(rows)

    assert any("monthly_revenue_point_in_time_panel" in error for error in errors)
    assert any("validator path missing" in error for error in errors)


def test_financial_statement_data_families_are_registered_and_formal_use_is_blocked() -> None:
    by_id = {row["data_family_id"]: row for row in registry_rows()}
    required = {
        "financial_statement_point_in_time_history",
        "financial_statement_source_manifest",
        "financial_statement_pit_coverage_audit",
    }

    assert required <= set(by_id)
    assert by_id["financial_statement_point_in_time_history"]["scope"] == "shared_objective"
    assert "exact company filing availability" in by_id[
        "financial_statement_point_in_time_history"
    ]["forbidden_use"]
    assert by_id["financial_statement_pit_coverage_audit"]["point_in_time_status"] == (
        "coverage_gate_current_snapshot_only_historical_verifier_and_revision_normalizer_unavailable"
    )
    assert "source-specific official evidence parser" in by_id[
        "financial_statement_source_manifest"
    ]["notes"]
    assert "formal_model_use_allowed=False" in by_id[
        "financial_statement_pit_coverage_audit"
    ]["notes"]


def test_registry_loader_fails_on_unquoted_comma_overflow(tmp_path: Path) -> None:
    path = tmp_path / "background.csv"
    path.write_text("data_family_id,notes\nexample,first,second\n", encoding="utf-8")
    errors: list[str] = []
    rows = strict_csv_rows(path, ("data_family_id", "notes"), errors)
    assert rows == []
    assert any("field count 3 does not match header count 2" in error for error in errors)
