from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_daily_model_background_data_registry import load_registry, validate_registry  # noqa: E402


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


def test_missing_revenue_panel_must_stay_blocked() -> None:
    rows = deepcopy(registry_rows())
    for row in rows:
        if row["data_family_id"] == "monthly_revenue_point_in_time_panel":
            row["artifact_path"] = "output/latest/fake_revenue.csv"
            row["allowed_use"] = "use now"
            row["validator"] = "not_ready_validator.py"
            row["cleanup_status"] = "active"
            break

    errors = validate_registry(rows)

    assert any("missing data family must use cleanup_status" in error for error in errors)
    assert any("missing data family must not point to a real artifact_path" in error for error in errors)
    assert any("missing data family must use validator=not_implemented" in error for error in errors)
