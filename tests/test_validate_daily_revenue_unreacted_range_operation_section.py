from __future__ import annotations

from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_revenue_unreacted_range_operation_section as validator  # noqa: E402


def test_audit_only_disposition_cannot_replace_active_confirmation_proof() -> None:
    row = {
        "operation_key": "synthetic-operation-1714",
        "lifecycle_state": "unpublished_confirmation_audit_only",
        "confirmed_history_artifact": "",
        "confirmed_history_row_sha256": "",
    }
    with pytest.raises(validator.ValidationError, match="lacks immutable confirmed proof"):
        validator._validate_confirmed_proof(row, current_asof="20261016", row_number=2)


def test_audit_only_label_cannot_hide_published_but_missing_confirmation(tmp_path: Path) -> None:
    missing = tmp_path / (
        "daily_revenue_unreacted_range_operation_section_20261006_" + "a" * 64 + ".csv"
    )
    row = {
        "operation_key": "synthetic-operation-1714",
        "lifecycle_state": "unpublished_confirmation_audit_only",
        "confirmed_history_artifact": missing.as_posix(),
        "confirmed_history_row_sha256": "b" * 64,
    }
    with pytest.raises((validator.ValidationError, FileNotFoundError)):
        validator._validate_confirmed_proof(row, current_asof="20261016", row_number=2)
    assert not missing.exists()
