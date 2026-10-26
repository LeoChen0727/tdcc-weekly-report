from __future__ import annotations

import ast
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import audit_volume_v2_low_position_d15_reconciliation as audit
import validate_volume_v2_low_position_d15_reconciliation as validator


def encode(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8-sig")


def fixture_rows():
    old = []
    new = []
    for key, signal, confirmation, entry, old_exit, new_exit in [
        ("first", "20260101", "20260102", "20260105", "20260112", "20260120"),
        ("second", "20260113", "20260114", "20260120", "20260127", "20260128"),
    ]:
        base = {"source_event_key": key, "stock_id": "0062", "signal_date": signal,
                "confirmation_date": confirmation, "entry_date": entry, "exit_date": old_exit,
                "artifact_version": audit.D10_VERSION, "model_id": "volume_range_breakout",
                "same_stock_non_overlap_included": "True", "return_pct": "",
                "anomaly_status": "unresolved_anomaly_candidate"}
        old.append(base)
        current = dict(base, artifact_version=audit.D15_VERSION, exit_date=new_exit)
        current["model_id"] = audit.MODEL_ID
        new.append(current)
    return new, old


def inputs(new=None, old=None):
    fixture_new, fixture_old = fixture_rows()
    d15 = encode(fixture_new if new is None else new)
    d10 = encode(fixture_old if old is None else old)
    hashes = {"expected_d15_sha256": hashlib.sha256(d15).hexdigest(),
              "expected_d10_sha256": hashlib.sha256(d10).hexdigest()}
    return d15, d10, hashes


def checked_receipt(new=None, old=None):
    d15, d10, hashes = inputs(new, old)
    receipt = audit.reconcile(d15, d10, **hashes)
    validator.validate_receipt(receipt, d15, d10, **hashes)
    return receipt, d15, d10, hashes


def test_all_original_rows_and_unresolved_flags_retained_with_unpriced_missing():
    receipt, d15, d10, hashes = checked_receipt()
    assert receipt["research_row_count"] == receipt["retained_row_count"] == 2
    assert receipt["overlap_pair_count"] == 1
    for entry in receipt["rows"]:
        assert entry["d15_source_row"]["anomaly_status"] == "unresolved_anomaly_candidate"
        assert entry["original_d10_source_row"]["anomaly_status"] == "unresolved_anomaly_candidate"
        assert entry["d15_source_row"]["return_pct"] == ""
        assert entry["original_d10_source_row"]["return_pct"] == ""
    assert hashlib.sha256(d15).hexdigest() == hashes["expected_d15_sha256"]
    assert hashlib.sha256(d10).hexdigest() == hashes["expected_d10_sha256"]
    for name in ("formal_publication_parity_verified", "formal_position_parity_verified",
                 "promotion_allowed", "return_evidence_allowed", "primary_statistics_modified",
                 "new_returns_calculated", "network_used"):
        assert receipt[name] is False


@pytest.mark.parametrize("which", ["d15", "d10"])
def test_source_hash_drift_fails_audit_and_independent_validator(which):
    receipt, d15, d10, hashes = checked_receipt()
    changed_d15 = d15 + b" " if which == "d15" else d15
    changed_d10 = d10 + b" " if which == "d10" else d10
    with pytest.raises(ValueError):
        audit.reconcile(changed_d15, changed_d10, **hashes)
    with pytest.raises(ValueError):
        validator.validate_receipt(receipt, changed_d15, changed_d10, **hashes)


@pytest.mark.parametrize("which", ["d15", "d10"])
def test_missing_dates_fail_audit_and_validator(which):
    new, old = fixture_rows()
    (new if which == "d15" else old)[0]["exit_date"] = ""
    d15, d10, hashes = inputs(new, old)
    with pytest.raises(ValueError):
        audit.reconcile(d15, d10, **hashes)
    receipt = checked_receipt()[0]
    receipt["sources"]["d15"]["sha256"] = hashes["expected_d15_sha256"]
    receipt["sources"]["d10_admission"]["sha256"] = hashes["expected_d10_sha256"]
    with pytest.raises(ValueError):
        validator.validate_receipt(receipt, d15, d10, **hashes)


@pytest.mark.parametrize("which", ["d15", "d10"])
def test_duplicate_event_keys_fail_audit_and_validator(which):
    new, old = fixture_rows()
    rows = new if which == "d15" else old
    rows.append(dict(rows[0]))
    d15, d10, hashes = inputs(new, old)
    with pytest.raises(ValueError):
        audit.reconcile(d15, d10, **hashes)
    with pytest.raises(ValueError):
        validator.validate_receipt(checked_receipt()[0], d15, d10, **hashes)


def test_same_day_entry_and_prior_exit_is_overlap():
    receipt = checked_receipt()[0]
    assert receipt["overlap_pairs"][0]["same_day_entry_and_prior_exit"] is True
    assert receipt["overlap_pairs"][0]["original_d10_windows_overlap"] is False
    assert receipt["overlap_pairs"][0]["d15_windows_overlap"] is True


def test_entry_after_prior_exit_is_not_overlap():
    new, old = fixture_rows()
    for rows in (new, old):
        rows[1].update(signal_date="20260120", confirmation_date="20260121", entry_date="20260122")
    receipt = checked_receipt(new, old)[0]
    assert receipt["overlap_pair_count"] == 0
    assert receipt["retained_row_count"] == 2


@pytest.mark.parametrize("which", ["d15", "d10"])
def test_wrong_model_fails_audit_and_validator(which):
    new, old = fixture_rows()
    if which == "d10":
        old[0]["model_id"] = "unrelated_model"
    else:
        new[0]["model_id"] = "unrelated_model"
    d15, d10, hashes = inputs(new, old)
    with pytest.raises(ValueError):
        audit.reconcile(d15, d10, **hashes)
    with pytest.raises(ValueError):
        validator.validate_receipt(checked_receipt()[0], d15, d10, **hashes)


def test_d10_admission_cannot_be_assumed():
    new, old = fixture_rows()
    old[0]["same_stock_non_overlap_included"] = "False"
    d15, d10, hashes = inputs(new, old)
    with pytest.raises(ValueError):
        audit.reconcile(d15, d10, **hashes)
    with pytest.raises(ValueError):
        validator.validate_receipt(checked_receipt()[0], d15, d10, **hashes)


@pytest.mark.parametrize("tamper", ["drop", "unresolved", "price", "key", "pair", "promote", "source-hash"])
def test_independent_validator_rejects_receipt_tampering(tamper):
    receipt, d15, d10, hashes = checked_receipt()
    forged = copy.deepcopy(receipt)
    if tamper == "drop":
        forged["rows"].pop()
    elif tamper == "unresolved":
        forged["rows"][0]["d15_source_row"]["anomaly_status"] = "resolved"
    elif tamper == "price":
        forged["rows"][0]["d15_source_row"]["return_pct"] = "0"
    elif tamper == "key":
        forged["rows"][0]["source_event_key"] = "other"
    elif tamper == "pair":
        forged["overlap_pairs"] = []
        forged["overlap_pair_count"] = 0
    elif tamper == "promote":
        forged["return_evidence_allowed"] = True
    else:
        forged["sources"]["d15"]["sha256"] = "0" * 64
    with pytest.raises(ValueError):
        validator.validate_receipt(forged, d15, d10, **hashes)


def test_validator_has_no_business_imports():
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not any(name.startswith(("audit_", "build_", "volume_breakout_operation")) for name in imports)


def test_audit_default_success_is_not_formal_position_parity(tmp_path, monkeypatch):
    receipt = checked_receipt()[0]
    monkeypatch.setattr(audit, "read_git_blob", lambda *args: b"unused")
    monkeypatch.setattr(audit, "reconcile", lambda *args: receipt)
    outside = tmp_path / "evidence"
    repo = tmp_path / "repo"
    assert audit.main(["--repo-root", str(repo), "--output", str(outside / "audit.json")]) == 0
    assert audit.main(["--repo-root", str(repo), "--output", str(outside / "required.json"),
                       "--require-formal-position-parity"]) == 2
    assert json.loads((outside / "required.json").read_text(encoding="utf-8"))["promotion_allowed"] is False


def test_audit_refuses_repo_output_and_existing_receipt(tmp_path, monkeypatch):
    receipt = checked_receipt()[0]
    monkeypatch.setattr(audit, "read_git_blob", lambda *args: b"unused")
    monkeypatch.setattr(audit, "reconcile", lambda *args: receipt)
    repo = tmp_path / "repo"
    assert audit.main(["--repo-root", str(repo), "--output", str(repo / "output" / "bad.json")]) == 1
    assert not repo.exists()
    outside = tmp_path / "receipt.json"
    outside.write_text("existing", encoding="utf-8")
    assert audit.main(["--repo-root", str(repo), "--output", str(outside)]) == 1
    assert outside.read_text(encoding="utf-8") == "existing"


@pytest.mark.parametrize("field", ["formal_publication_parity_verified", "formal_position_parity_verified"])
def test_independent_validator_rejects_parity_claim(field):
    receipt, d15, d10, hashes = checked_receipt()
    receipt[field] = True
    with pytest.raises(ValueError):
        validator.validate_receipt(receipt, d15, d10, **hashes)


def test_independent_validator_requires_boolean_admission_not_number():
    receipt, d15, d10, hashes = checked_receipt()
    receipt["rows"][0]["original_d10_admitted"] = 1
    with pytest.raises(ValueError):
        validator.validate_receipt(receipt, d15, d10, **hashes)


def test_independent_validator_cli_blocks_formal_parity(tmp_path, monkeypatch):
    receipt, d15, d10, hashes = checked_receipt()
    path = tmp_path / "receipt.json"
    path.write_text(json.dumps(receipt), encoding="utf-8")
    monkeypatch.setattr(validator.subprocess, "check_output", lambda *args, **kwargs: b"unused")
    monkeypatch.setattr(validator, "validate_receipt", lambda *args, **kwargs: None)
    assert validator.main(["--receipt", str(path)]) == 0
    assert validator.main(["--receipt", str(path), "--require-formal-position-parity"]) == 2
