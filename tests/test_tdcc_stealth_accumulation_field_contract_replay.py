from __future__ import annotations

import ast
import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_tdcc_stealth_accumulation_field_contract_replay as producer  # noqa: E402
import build_tdcc_stealth_accumulation_historical_replay as v1  # noqa: E402
import validate_tdcc_stealth_accumulation_field_contract_replay as validator  # noqa: E402


def base_row() -> dict[str, str]:
    return {
        "stock_id": "2330",
        "signal_date": "20260102",
        "tdcc_price_phase": "",
        "tdcc_judgement": "",
        "tdcc_accumulation_signal": "mild_accumulation",
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


def test_enum_positive_fallback_is_narrow_and_not_boolean() -> None:
    for value in ("mild_accumulation", "strong_accumulation"):
        row = base_row()
        row["tdcc_accumulation_signal"] = value
        result = producer.evaluate_selector(row)
        assert result["selector_selected"] is True
        assert result["tdcc_positive_resolution"] == "recognized_enum_positive_fallback"
        assert result["tdcc_accumulation_signal_raw"] == value


def test_nonpositive_unknown_and_missing_enum_fail_closed() -> None:
    expected = {
        "distribution_warning": "recognized_enum_nonpositive_fail_closed",
        "neutral": "recognized_enum_nonpositive_fail_closed",
        "future_enum": "unknown_enum_fail_closed",
        "": "missing_positive_evidence_fail_closed",
    }
    for value, resolution in expected.items():
        row = base_row()
        row["tdcc_accumulation_signal"] = value
        result = producer.evaluate_selector(row)
        assert result["selector_selected"] is False
        assert result["tdcc_positive_resolution"] == resolution


def test_phase_and_status_priority_are_preserved() -> None:
    row = base_row()
    row["tdcc_price_phase"] = "tdcc_leading_price"
    row["tdcc_accumulation_signal"] = ""
    result = producer.evaluate_selector(row)
    assert result["selector_selected"] is True
    assert result["tdcc_positive_source"] == "tdcc_price_phase"

    row = base_row()
    row["tdcc_judgement"] = "strong_accumulation"
    row["tdcc_accumulation_signal"] = ""
    result = producer.evaluate_selector(row)
    assert result["selector_selected"] is True
    assert result["tdcc_positive_source"] == "status_alias"


def test_recognized_status_enum_conflict_is_reported_without_new_veto() -> None:
    row = base_row()
    row["tdcc_judgement"] = "strong_accumulation"
    row["tdcc_accumulation_signal"] = "distribution_warning"
    result = producer.evaluate_selector(row)
    assert result["selector_selected"] is True
    assert result["tdcc_field_conflict"] is True
    assert result["tdcc_positive_resolution"] == "recognized_status_positive"


def test_current_boolean_positive_behavior_is_preserved() -> None:
    row = base_row()
    row["tdcc_accumulation_signal"] = "True"
    result = producer.evaluate_selector(row)
    assert result["selector_selected"] is True
    assert result["tdcc_positive_resolution"] == "current_boolean_positive_preserved"


def test_all_other_selector_gates_are_unchanged() -> None:
    for field, value in (
        ("volume_confirmed_breakout", "True"),
        ("volume_ratio", "2.5"),
        ("return_5d", "8"),
        ("return_20d", "20"),
        ("close", "130"),
    ):
        row = base_row()
        row[field] = value
        assert producer.evaluate_selector(row)["selector_selected"] is False


def test_v1_v2_difference_is_only_blank_phase_status_positive_enum() -> None:
    for phase in ("", "tdcc_leading_price", "price_leading_tdcc", "future_phase"):
        for status in ("", "mild_accumulation", "distribution_warning", "future_status"):
            for enum_value in ("", "False", "True", "mild_accumulation", "strong_accumulation", "neutral", "future_enum"):
                row = base_row()
                row["tdcc_price_phase"] = phase
                row["tdcc_judgement"] = status
                row["tdcc_accumulation_signal"] = enum_value
                old = v1.evaluate_selector(row)["selector_selected"]
                new = producer.evaluate_selector(row)["selector_selected"]
                expected_change = not phase and not status and enum_value in producer.POSITIVE
                assert new != old if expected_change else new == old


def test_independent_validator_matches_synthetic_selector() -> None:
    for enum_value, selected in (
        ("mild_accumulation", True),
        ("strong_accumulation", True),
        ("distribution_warning", False),
        ("neutral", False),
        ("future_enum", False),
    ):
        row = base_row()
        row["tdcc_accumulation_signal"] = enum_value
        assert validator.independently_selected(row) is selected


def test_field_contract_has_only_three_prioritized_roles() -> None:
    with (ROOT / producer.FIELD_CONTRACT_PATH).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert [row["field_role"] for row in rows] == ["phase", "status", "enum_fallback"]
    assert [row["priority"] for row in rows] == ["1", "2", "3"]
    enum_row = next(row for row in rows if row["field_role"] == "enum_fallback")
    assert enum_row["unknown_behavior"] == "fail_closed"
    assert all(row["conflict_behavior"] != "fail_closed" for row in rows)
    assert all(row["formal_use"] == "False" for row in rows)


def test_v2_owner_and_data_contract_are_registered() -> None:
    def rows(path: str) -> list[dict[str, str]]:
        with (ROOT / path).open(encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    ownership = next(
        row for row in rows("config/model_research_artifact_ownership.csv")
        if row["owner_model_id"] == producer.OWNER_ID
    )
    assert ownership["producer"] == producer.PRODUCER
    assert ownership["formal_evidence_status"] == "research_only"

    family = "tdcc_stealth_accumulation_field_contract_replay_outputs"
    background = next(
        row for row in rows("config/daily_model_background_data_registry.csv")
        if row["data_family_id"] == family
    )
    sharing = next(
        row for row in rows("config/daily_model_data_sharing_registry.csv")
        if row["data_family_id"] == family
    )
    contract_fields = (
        "data_family_id", "scope", "owner_lane", "producer", "artifact_path",
        "source_artifacts", "consumer_surfaces", "consumer_models",
        "point_in_time_status", "allowed_use", "forbidden_use", "validator",
        "retention_policy", "cleanup_status", "notes",
    )
    payload = "\n".join(f"{field}={background[field]}" for field in contract_fields)
    assert sharing["data_contract_sha256"] == hashlib.sha256(payload.encode("utf-8")).hexdigest()
    assert sharing["approved_consumer_models"] == producer.MODEL_ID
    assert sharing["formal_evidence_policy"].startswith("research_only")

    independence = next(
        row for row in rows("config/daily_model_validator_independence.csv")
        if row["validator_path"] == "scripts/validate_tdcc_stealth_accumulation_field_contract_replay.py"
    )
    assert independence["independence_claim"] == "True"
    assert independence["allowed_evidence_use"].endswith("not_promotion_proof")


def test_v2_producer_does_not_import_production_business_module() -> None:
    source = (SCRIPTS / "build_tdcc_stealth_accumulation_field_contract_replay.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names
    } | {
        node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)
    }
    assert "build_daily_candidate_model_layer" not in imported
    assert "scripts.build_daily_candidate_model_layer" not in imported

    validator_source = (SCRIPTS / "validate_tdcc_stealth_accumulation_field_contract_replay.py").read_text(encoding="utf-8")
    validator_tree = ast.parse(validator_source)
    validator_imported = {
        alias.name for node in ast.walk(validator_tree) if isinstance(node, ast.Import) for alias in node.names
    } | {
        node.module or "" for node in ast.walk(validator_tree) if isinstance(node, ast.ImportFrom)
    }
    assert "build_tdcc_stealth_accumulation_field_contract_replay" not in validator_imported
    assert "build_tdcc_stealth_accumulation_historical_replay" not in validator_imported
