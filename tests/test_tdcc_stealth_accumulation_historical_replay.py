from __future__ import annotations

import ast
import csv

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_tdcc_stealth_accumulation_historical_replay as producer  # noqa: E402
import validate_tdcc_stealth_accumulation_historical_replay as validator  # noqa: E402


OWNER = "tdcc_stealth_accumulation_historical_selector_replay"
ARTIFACT_GLOB = (
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_historical_selector_replay_*_v1.*"
)


def base_row() -> dict[str, str]:
    return {
        "stock_id": "2330",
        "signal_date": "20260102",
        "tdcc_price_phase": "",
        "tdcc_judgement": "mild_accumulation",
        "tdcc_accumulation_signal": "False",
        "volume_ratio": "1.2",
        "return_5d": "3",
        "return_20d": "7",
        "close": "100",
        "high_20": "110",
        "low_20": "90",
        "open": "99",
        "high": "101",
        "low": "98",
        "previous_20d_high": "110",
        "volume_confirmed_breakout": "False",
    }


def test_replay_has_one_narrow_research_owner_and_one_consumer() -> None:
    def rows(path: str) -> list[dict[str, str]]:
        with (ROOT / path).open(encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    ownership = [
        row
        for row in rows("config/model_research_artifact_ownership.csv")
        if row["artifact_glob"] == ARTIFACT_GLOB
    ]
    assert len(ownership) == 1
    assert ownership[0]["owner_model_id"] == OWNER
    assert ownership[0]["producer"] == producer.PRODUCER
    assert ownership[0]["change_policy"] == "model_owned_write"
    assert ownership[0]["formal_evidence_status"] == "research_only"

    sharing = next(
        row
        for row in rows("config/daily_model_data_sharing_registry.csv")
        if row["data_family_id"]
        == "tdcc_stealth_accumulation_historical_selector_replay_outputs"
    )
    assert sharing["ownership_mode"] == "model_owned_not_shared"
    assert sharing["owner_model_or_family"] == OWNER
    assert sharing["registered_producers"] == producer.PRODUCER
    assert sharing["producer_write_scope"] == ARTIFACT_GLOB
    assert sharing["approved_consumer_models"] == "tdcc_stealth_accumulation"
    assert sharing["consumer_access_mode"] == "owner_model_research_only"

    migration = next(
        row
        for row in rows("config/model_research_artifact_ownership_migrations.csv")
        if row["migration_id"]
        == "tdcc_stealth_accumulation_historical_selector_replay_registration_v1"
    )
    assert migration["previous_owner"] == "unregistered"
    assert migration["new_owner"] == OWNER
    assert migration["record_keys"] == ARTIFACT_GLOB
    assert migration["approval_reference"] == (
        "user_authorized_tdcc_stealth_historical_selector_replay_20260908"
    )


def test_blank_phase_preserves_tdcc_positive_fallback() -> None:
    result = producer.evaluate_selector(base_row())
    assert result["selector_selected"] is True
    assert result["tdcc_price_phase"] == ""
    assert result["tdcc_status"] == "mild_accumulation"


def test_explicit_tdcc_leading_price_is_accepted_without_positive_status() -> None:
    row = base_row()
    row["tdcc_price_phase"] = "tdcc_leading_price"
    row["tdcc_judgement"] = "neutral"
    assert producer.evaluate_selector(row)["selector_selected"] is True


def test_forbidden_phase_and_started_attack_fail_closed() -> None:
    row = base_row()
    row["tdcc_price_phase"] = "price_leading_tdcc"
    assert producer.evaluate_selector(row)["selector_selected"] is False
    row = base_row()
    row["volume_confirmed_breakout"] = "True"
    assert producer.evaluate_selector(row)["selector_selected"] is False


def test_volume_return_and_range_gates_are_independent() -> None:
    for field, value in (("volume_ratio", "2.5"), ("return_5d", "8"), ("return_20d", "20")):
        row = base_row()
        row[field] = value
        assert producer.evaluate_selector(row)["selector_selected"] is False
    row = base_row()
    row["close"] = "130"
    assert producer.evaluate_selector(row)["selector_selected"] is False


def test_alias_order_matches_current_selector_contract() -> None:
    row = base_row()
    row.pop("tdcc_judgement")
    row["tdcc_judgement_x"] = "strong_accumulation"
    row.pop("return_5d")
    row["return_5d_pct_y"] = "2"
    result = producer.evaluate_selector(row)
    assert result["selector_selected"] is True
    assert result["tdcc_status_source"] == "tdcc_judgement_x"


def test_producer_and_validator_are_business_function_independent() -> None:
    producer_source = (SCRIPTS / "build_tdcc_stealth_accumulation_historical_replay.py").read_text(encoding="utf-8")
    validator_source = (SCRIPTS / "validate_tdcc_stealth_accumulation_historical_replay.py").read_text(encoding="utf-8")
    def imports(source: str) -> set[str]:
        tree = ast.parse(source)
        return {
            alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names
        } | {
            node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
        }
    forbidden = {
        "build_daily_candidate_model_layer", "scripts.build_daily_candidate_model_layer",
        "build_tdcc_stealth_accumulation_historical_replay",
        "scripts.build_tdcc_stealth_accumulation_historical_replay",
    }
    assert not (imports(producer_source) & forbidden)
    assert not (imports(validator_source) & forbidden)
    assert validator.independently_selected(base_row()) is True


def test_tracked_replay_artifacts_pass_independent_validation() -> None:
    validator.validate()
