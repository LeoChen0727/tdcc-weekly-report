from __future__ import annotations

import ast
import csv
import hashlib
import io
import sys
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest


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


def csv_payload(rows: list[dict[str, str]], fields: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def write_bound_artifacts(root: Path) -> dict[Path, bytes]:
    detail = csv_payload(
        [{
            "stock_id": "2330",
            "large_return_observation_codes": "d5_min_observed_return",
            "large_return_spotcheck_status": "unresolved_bounded_source_continuity_check_only",
        }],
        ["stock_id", "large_return_observation_codes", "large_return_spotcheck_status"],
    )
    digest = hashlib.sha256(detail).hexdigest()
    summary = csv_payload(
        [{"horizon": horizon, "detail_artifact_sha256": digest} for horizon in ("D5", "D10", "D20")],
        ["horizon", "detail_artifact_sha256"],
    )
    report = f"# research-only replay\n\n- detail SHA-256: `{digest}`\n".encode("utf-8")
    payloads = {validator.DETAIL: detail, validator.SUMMARY: summary, validator.REPORT: report}
    for relative, payload in payloads.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    return payloads


def test_build_binds_final_observation_markers_not_pre_annotation_digest(tmp_path: Path, monkeypatch) -> None:
    original_fields = list(v1.DETAIL_FIELDS)
    detail_fields = original_fields + producer.DETAIL_EXTRA_FIELDS
    original_detail = []
    for index, sign in enumerate((-1, 1)):
        row = {field: "" for field in detail_fields}
        row.update({
            "stock_id": str(2330 + index),
            "stock_name": "synthetic",
            "candidate_signal_date": "20260102",
            "entry_date": "20260103",
            "entry_open_price": "100.000000",
            "anomaly_candidate": "False",
            "formal_use": "False",
            "trade_eligible": "False",
            "promotion_evidence_allowed": "False",
        })
        for horizon in (5, 10, 20):
            row[f"return_d{horizon}_pct"] = f"{sign * horizon}.000000"
            row[f"exit_d{horizon}_date"] = f"202601{3 + horizon:02d}"
        original_detail.append(row)
    before_digest = hashlib.sha256(csv_payload(original_detail, detail_fields)).hexdigest()
    original_summary = [
        {
            "horizon": f"D{horizon}",
            "source_commit_sha": "a" * 40,
            "snapshot_report_date_min": "20260102",
            "snapshot_report_date_max": "20260102",
            "published_membership_match_count": "0",
            "promotion_blockers": "research_only",
            "unresolved_anomaly_candidate_count": "0",
            "detail_artifact_sha256": before_digest,
        }
        for horizon in (5, 10, 20)
    ]
    original_report = (
        "# historical selector research replay v1\n\n"
        "本報告是固定 synthetic source。\n\n## 研究績效\n\n"
        f"- detail SHA-256: `{before_digest}`\n"
    )

    def fake_base_build(**kwargs):
        assert v1.DETAIL_FIELDS == detail_fields
        return deepcopy(original_detail), deepcopy(original_summary), original_report

    monkeypatch.setattr(v1, "build", fake_base_build)
    monkeypatch.setattr(v1, "GitTree", lambda *args: object())
    prices = [SimpleNamespace(date=f"202601{3 + index:02d}") for index in range(21)]
    monkeypatch.setattr(v1, "_load_prices", lambda *args: {"2330": prices, "2331": prices})
    detail, summary, report = producer.build(root=ROOT, source_ref="fixed-source")
    assert v1.DETAIL_FIELDS == original_fields
    after_payload = csv_payload(detail, detail_fields)
    after_digest = hashlib.sha256(after_payload).hexdigest()
    assert after_digest != before_digest
    assert all(row["large_return_observation_codes"] for row in detail)
    assert all(row["large_return_spotcheck_status"] for row in detail)
    assert {row["detail_artifact_sha256"] for row in summary} == {after_digest}
    assert f"- detail SHA-256: `{after_digest}`" in report
    assert before_digest not in report
    with producer._patched_base(ROOT):
        v1._write_outputs(tmp_path, detail, summary, report)
    assert (tmp_path / validator.DETAIL).read_bytes() == after_payload
    loaded_detail, loaded_summary, _ = validator.load_bound_artifacts(tmp_path)
    assert loaded_detail == detail
    assert {row["detail_artifact_sha256"] for row in loaded_summary} == {after_digest}
    for row in detail:
        for field in ("formal_use", "trade_eligible", "promotion_evidence_allowed"):
            assert row[field] == "False"
    stripped = deepcopy(detail)
    for row in stripped:
        row["large_return_observation_codes"] = ""
        row["large_return_spotcheck_status"] = ""
    assert csv_payload(stripped, detail_fields) == csv_payload(original_detail, detail_fields)


@pytest.mark.parametrize("field", ["large_return_observation_codes", "large_return_spotcheck_status"])
def test_validator_rejects_each_observation_only_mutation(tmp_path: Path, field: str) -> None:
    payloads = write_bound_artifacts(tmp_path)
    rows = list(csv.DictReader(io.StringIO(payloads[validator.DETAIL].decode("utf-8"))))
    rows[0][field] = "changed_observation_only"
    (tmp_path / validator.DETAIL).write_bytes(csv_payload(rows, list(rows[0])))
    with pytest.raises(RuntimeError, match="final detail digest mismatch"):
        validator.load_bound_artifacts(tmp_path)


@pytest.mark.parametrize("horizon", ["D5", "D10", "D20"])
def test_validator_rejects_each_summary_horizon_digest_mismatch(tmp_path: Path, horizon: str) -> None:
    payloads = write_bound_artifacts(tmp_path)
    rows = list(csv.DictReader(io.StringIO(payloads[validator.SUMMARY].decode("utf-8"))))
    next(row for row in rows if row["horizon"] == horizon)["detail_artifact_sha256"] = "0" * 64
    (tmp_path / validator.SUMMARY).write_bytes(csv_payload(rows, list(rows[0])))
    with pytest.raises(RuntimeError, match=f"digest mismatch in summary horizon={horizon}"):
        validator.load_bound_artifacts(tmp_path)


@pytest.mark.parametrize("mutation", ["wrong", "missing", "duplicate", "indented_duplicate", "malformed"])
def test_validator_rejects_invalid_report_digest_marker(tmp_path: Path, mutation: str) -> None:
    payloads = write_bound_artifacts(tmp_path)
    report = payloads[validator.REPORT].decode("utf-8")
    marker = next(line for line in report.splitlines() if line.startswith("- detail SHA-256:"))
    replacements = {
        "wrong": "- detail SHA-256: `" + "0" * 64 + "`",
        "missing": "",
        "duplicate": marker + "\n" + marker,
        "indented_duplicate": marker + "\n  " + marker,
        "malformed": marker.replace("`", ""),
    }
    (tmp_path / validator.REPORT).write_bytes(report.replace(marker, replacements[mutation]).encode("utf-8"))
    with pytest.raises(RuntimeError, match="exactly one matching final detail"):
        validator.load_bound_artifacts(tmp_path)


@pytest.mark.parametrize("detail_crlf", [False, True])
@pytest.mark.parametrize("summary_crlf", [False, True])
@pytest.mark.parametrize("report_crlf", [False, True])
def test_validator_accepts_only_line_ending_representation_changes(
    tmp_path: Path, detail_crlf: bool, summary_crlf: bool, report_crlf: bool,
) -> None:
    payloads = write_bound_artifacts(tmp_path)
    expected = validator.load_bound_artifacts(tmp_path)
    for relative, crlf in zip((validator.DETAIL, validator.SUMMARY, validator.REPORT), (detail_crlf, summary_crlf, report_crlf)):
        if crlf:
            (tmp_path / relative).write_bytes(payloads[relative].replace(b"\n", b"\r\n"))
    assert validator.load_bound_artifacts(tmp_path) == expected


@pytest.mark.parametrize("relative", [validator.DETAIL, validator.SUMMARY, validator.REPORT])
@pytest.mark.parametrize("mutation", ["bom", "bare_cr", "mixed_newlines"])
def test_validator_rejects_non_checkout_byte_changes(tmp_path: Path, relative: Path, mutation: str) -> None:
    payload = write_bound_artifacts(tmp_path)[relative]
    changed = {
        "bom": b"\xef\xbb\xbf" + payload,
        "bare_cr": payload.replace(b"\n", b"\r", 1),
        "mixed_newlines": payload.replace(b"\n", b"\r\n", 1),
    }[mutation]
    (tmp_path / relative).write_bytes(changed)
    with pytest.raises(RuntimeError, match="BOM or bare CR|pure LF or CRLF"):
        validator.load_bound_artifacts(tmp_path)


def test_validate_checks_working_detail_before_source_access(tmp_path: Path, monkeypatch) -> None:
    payloads = write_bound_artifacts(tmp_path)
    (tmp_path / validator.DETAIL).write_bytes(payloads[validator.DETAIL].replace(b"2330", b"9999"))

    def forbidden_git(*args, **kwargs):
        raise AssertionError("digest verification must use working bytes before accessing Git")

    monkeypatch.setattr(validator, "GitTree", forbidden_git)
    monkeypatch.setattr(validator.subprocess, "run", forbidden_git)
    with pytest.raises(RuntimeError, match="final detail digest mismatch"):
        validator.validate(tmp_path, "HEAD")


@pytest.mark.parametrize("mutation", ["lf", "crlf", "bom", "bare_cr", "content"])
def test_field_contract_hash_only_normalizes_checkout_crlf(tmp_path: Path, mutation: str) -> None:
    original = (ROOT / producer.FIELD_CONTRACT_PATH).read_bytes().replace(b"\r\n", b"\n")
    changed = {
        "lf": original,
        "crlf": original.replace(b"\n", b"\r\n"),
        "bom": b"\xef\xbb\xbf" + original,
        "bare_cr": original.replace(b"\n", b"\r", 1),
        "content": original.replace(b"phase is authoritative", b"phase stays authoritative", 1),
    }[mutation]
    path = tmp_path / producer.FIELD_CONTRACT_PATH
    path.parent.mkdir(parents=True)
    path.write_bytes(changed)
    actual = producer._field_contract_sha256(tmp_path)
    expected = hashlib.sha256(original).hexdigest()
    if mutation in {"lf", "crlf"}:
        assert actual == expected
    else:
        assert actual != expected
