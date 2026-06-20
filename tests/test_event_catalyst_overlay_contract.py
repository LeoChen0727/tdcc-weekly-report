from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_event_catalyst_overlay_contract as validator


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"


def contract_rows() -> list[dict[str, str]]:
    with CONTRACT.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def test_event_catalyst_overlay_contract_validator_passes() -> None:
    assert validator.main() == 0


def test_event_catalyst_overlay_contract_has_required_schema() -> None:
    rows = contract_rows()

    assert rows
    assert list(rows[0]) == validator.REQUIRED_COLUMNS


def test_phase_one_overlay_contract_is_disclosure_only() -> None:
    for row in contract_rows():
        assert row["allowed_effect"] == "disclosure_only"
        assert row["score_allowed"] == "false"
        assert row["ranking_allowed"] == "false"
        assert row["reason_text_allowed"] == "false"
        assert row["disclosure_only"] == "true"


def test_phase_one_degraded_behavior_blocks_score_rank_and_reason() -> None:
    for row in contract_rows():
        degraded_behavior = row["degraded_behavior"].lower()
        assert "no_score" in degraded_behavior
        assert "no_rank" in degraded_behavior
        assert "no_reason" in degraded_behavior


def test_tdcc_weekly_pdf_approved_fields_are_disclosure_only() -> None:
    approved = [row for row in contract_rows() if row["approved_for_tdcc_weekly_pdf"] == "true"]

    assert approved
    for row in approved:
        assert row["allowed_effect"] == "disclosure_only"
        assert row["score_allowed"] == "false"
        assert row["ranking_allowed"] == "false"
        assert row["reason_text_allowed"] == "false"
        assert "tdcc_weekly_pdf" in row["allowed_consumers"].split(";")


def test_allowed_effect_enum_matches_contract_rule() -> None:
    assert validator.ALLOWED_EFFECTS == {
        "disclosure_only",
        "reason_text_only",
        "risk_flag",
        "score_overlay",
        "ranking_modifier",
    }
