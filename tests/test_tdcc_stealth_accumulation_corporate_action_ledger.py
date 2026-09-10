"""Synthetic timing/accounting probes; never evidence of realized performance.

Exercises scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py and
scripts/validate_tdcc_stealth_accumulation_corporate_action_ledger.py.
"""
from __future__ import annotations

import ast
import base64
import copy
import csv
from contextlib import contextmanager
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
STEM = "tdcc_stealth_accumulation_corporate_action_ledger"
CONFIG_REL = f"config/{STEM}_v1.json"
OUT_REL = Path("output/research/tdcc_stealth_accumulation")
OUTPUT_NAMES = {
    f"{STEM}_{kind}" for kind in (
        "source_manifest_v1.json", "events_v1.csv", "positions_v1.csv",
        "blocked_v1.csv", "report_v1.md",
    )
}


def module(prefix):
    paths = {
        "build": "scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py",
        "validate": "scripts/validate_tdcc_stealth_accumulation_corporate_action_ledger.py",
    }
    previous_path = list(sys.path)
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        if prefix == "build":
            import build_tdcc_stealth_accumulation_corporate_action_ledger as loaded

            loaded = importlib.reload(loaded)
        else:
            path = ROOT / paths[prefix]
            spec = importlib.util.spec_from_file_location(f"{prefix}_ca_ledger_test", path)
            loaded = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(loaded)
    finally:
        sys.path[:] = previous_path
    return loaded


@pytest.fixture
def producer():
    return module("build")


@pytest.fixture
def validator():
    return module("validate")


def configuration():
    return json.loads((ROOT / CONFIG_REL).read_text(encoding="utf-8"))


def signal(**overrides):
    return dict(stock_id="5386", signal_date="20260101", raw_label="合成訊號", **overrides)


def trade(**overrides):
    row = dict(
        trade_id="synthetic-position-1", stock_id="5386", stock_name="合成測試",
        signal_date="20260101", horizon="10", slippage_bps="10",
        entry_date="20260102", exit_date="20260120", entry_open="100",
        exit_close="50", shares="1000", strict_v3_status="blocked_calendar_unverified",
        net_return_pct="-50.2345", anomaly_candidate="True", formal_use="False",
        promotion_evidence_allowed="False",
    )
    row.update(overrides)
    return row


def event(kind="stock_dividend", **overrides):
    row = copy.deepcopy(next(e for e in configuration()["events"] if e["kind"] == kind))
    row.update(
        event_id=f"synthetic-{kind}", stock_id="5386", stock_name="合成測試",
        entitlement_date="20260105", effective_date="20260105",
        tradable_date="20260110" if kind != "cash_dividend" else "",
        scheduled_payment_date="20260112" if kind == "cash_dividend" else "",
        actual_payment_date="", payment_confirmed=False, payment_confirmation_ref="",
        record_date="20260107", suspension_start="", suspension_end="",
        share_factor="2" if kind == "share_exchange" else "1",
        new_shares_per_old_share="0.5" if kind == "stock_dividend" else "0",
        cash_per_old_share="1.5" if kind == "cash_dividend" else "0",
    )
    row.update(overrides)
    return row


def reconcile(producer, events, **changes):
    return producer.reconcile_position(trade(**changes), events, signal())


def assert_research_lock(row):
    for key in ("formal_use", "promotion_evidence_allowed", "total_return_verified",
                "coverage_complete", "strict_lock_released"):
        assert row[key] == "False", key
    assert row["verified_total_return_pct"] == ""
    assert row["primary_row_retained"] == "True"
    assert row["original_proxy_net_return_pct"] == "-50.2345"


def test_no_known_event_is_not_verified_absence_or_zero_return(producer):
    row = reconcile(producer, [])
    assert row["matched_event_ids"] == ""
    assert row["known_event_share_balance"] == "1000"
    assert row["confirmed_cash_receipt"] == ""
    assert row["announced_gross_cash_entitlement"] == ""
    assert row["anomaly_disposition"] == "unresolved_anomaly_candidate"
    assert_research_lock(row)


@pytest.mark.parametrize("entry_date", ["20260105", "20260106"])
def test_entry_on_or_after_ex_date_does_not_acquire_old_share_rights(producer, entry_date):
    row = reconcile(producer, [event()], entry_date=entry_date)
    assert row["matched_event_ids"] == ""
    assert row["known_event_share_balance"] == "1000"
    assert row["pending_share_rights"] == "0"
    assert_research_lock(row)


@pytest.mark.parametrize("exit_date,balance,pending", [
    ("20260109", "1000", "500"), ("20260110", "1500", "0"),
    ("20260113", "1500", "0"),
])
def test_stock_dividend_tradability_boundary(producer, exit_date, balance, pending):
    row = reconcile(producer, [event()], exit_date=exit_date)
    assert row["known_event_share_balance"] == balance
    assert row["pending_share_rights"] == pending
    assert row["matched_event_ids"] == "synthetic-stock_dividend"
    assert_research_lock(row)


@pytest.mark.parametrize("exit_date,balance,pending", [
    ("20260109", "0", "2000"), ("20260110", "2000", "0"),
    ("20260113", "2000", "0"),
])
def test_exchange_does_not_sell_old_or_undelivered_new_shares(producer, exit_date, balance, pending):
    row = reconcile(producer, [event("share_exchange")], exit_date=exit_date)
    assert row["known_event_share_balance"] == balance
    assert row["pending_share_rights"] == pending
    assert_research_lock(row)


@pytest.mark.parametrize("reverse", [False, True])
def test_same_day_stock_and_cash_dividend_use_pre_event_shares(producer, reverse):
    events = [event(), event("cash_dividend")]
    if reverse:
        events.reverse()
    row = reconcile(producer, events)
    assert row["known_event_share_balance"] == "1500"
    assert row["announced_gross_cash_entitlement"] == "1500"
    assert row["unsettled_gross_cash_entitlement"] == "1500"
    assert row["confirmed_cash_receipt"] == ""
    assert_research_lock(row)


@pytest.mark.parametrize("factor,shares,balance,whole,fraction", [
    ("2", "0.25", "0.5", "0", "0.5"),
    ("0.618578", "1000", "618.578", "618", "0.578"),
    ("0.618578", "1", "0.618578", "0", "0.618578"),
])
def test_split_reduction_preserve_exact_theoretical_fractional_shares(
    producer, factor, shares, balance, whole, fraction,
):
    row = reconcile(producer, [event("share_exchange", share_factor=factor)], shares=shares)
    assert row["known_event_share_balance"] == balance
    assert row["eligible_whole_share_component"] == whole
    assert row["unresolved_fractional_share_component"] == fraction
    assert_research_lock(row)


def test_official_precise_stock_dividend_rate_is_not_rounded(producer):
    row = reconcile(producer, [event(new_shares_per_old_share="0.50000001386")])
    assert row["known_event_share_balance"] == "1500.00001386"
    assert row["unresolved_fractional_share_component"] == "0.00001386"
    assert_research_lock(row)


@pytest.mark.parametrize("scheduled", ["20260107", "20260120", "20260121", ""])
def test_scheduled_payment_never_proves_cash_received(producer, scheduled):
    row = reconcile(producer, [event("cash_dividend", scheduled_payment_date=scheduled)])
    assert row["announced_gross_cash_entitlement"] == "1500"
    assert row["unsettled_gross_cash_entitlement"] == "1500"
    assert row["confirmed_cash_receipt"] == ""
    assert_research_lock(row)


def test_confirmed_cash_requires_actual_date_and_receipt_reference(producer):
    paid = event("cash_dividend", payment_confirmed=True,
                 actual_payment_date="20260112", payment_confirmation_ref="synthetic-receipt")
    row = reconcile(producer, [paid])
    assert row["confirmed_cash_receipt"] == "1500"
    assert row["unsettled_gross_cash_entitlement"] == "0"
    assert_research_lock(row)
    for missing in ("actual_payment_date", "payment_confirmation_ref"):
        incomplete = copy.deepcopy(paid)
        incomplete[missing] = ""
        with pytest.raises(ValueError):
            reconcile(producer, [incomplete])


def test_actual_payment_after_exit_is_not_received_at_exit(producer):
    row = reconcile(producer, [event("cash_dividend", payment_confirmed=True,
        actual_payment_date="20260121", payment_confirmation_ref="synthetic-later-receipt")])
    assert row["confirmed_cash_receipt"] == ""
    assert row["unsettled_gross_cash_entitlement"] == "1500"
    assert_research_lock(row)


def test_unknown_cash_stays_blank_not_zero(producer):
    row = reconcile(producer, [event("cash_dividend", cash_per_old_share="")])
    for key in ("announced_gross_cash_entitlement", "unsettled_gross_cash_entitlement",
                "confirmed_cash_receipt", "verified_total_return_pct"):
        assert row[key] == ""
    assert_research_lock(row)


def test_6669_undelivered_shares_cannot_be_sold_at_original_exit(producer):
    e = event(stock_id="6669", event_id="6669-unknown-delivery",
              new_shares_per_old_share="1.98279460", tradable_date="")
    t = trade(stock_id="6669")
    s = dict(stock_id="6669", signal_date=t["signal_date"])
    row = producer.reconcile_position(t, [e], s)
    assert row["known_event_share_balance"] == "1000"
    assert row["pending_share_rights"] == "1982.7946"
    assert row["confirmed_cash_receipt"] == ""
    assert_research_lock(row)


def test_future_event_does_not_change_exit_proxy_or_balances(producer):
    baseline = reconcile(producer, [])
    row = reconcile(producer, [event(entitlement_date="20260121", effective_date="20260121",
        tradable_date="20260122", record_date="20260122")])
    for field in ("known_event_share_balance", "pending_share_rights", "matched_event_ids",
                  "original_proxy_net_return_pct", "verified_total_return_pct"):
        assert row[field] == baseline[field]
    assert_research_lock(row)


def test_pending_rights_then_later_entitlement_is_not_guessed(producer):
    first = event(tradable_date="20260121")
    second = event("cash_dividend", entitlement_date="20260108", effective_date="20260108",
                   record_date="20260109")
    with pytest.raises(ValueError):
        reconcile(producer, [first, second])


@pytest.mark.parametrize("delivery_date", ["20260115", "20260110"])
def test_delivery_before_exit_does_not_backdate_shares_to_intervening_entitlement(producer, delivery_date):
    first = event(tradable_date=delivery_date)
    intervening = event("cash_dividend", entitlement_date="20260110",
        effective_date="20260110", record_date="20260111")
    with pytest.raises(ValueError):
        reconcile(producer, [first, intervening])


def test_shares_tradable_before_later_entitlement_change_the_later_basis(producer):
    first = event(tradable_date="20260109")
    subsequent = event("cash_dividend", entitlement_date="20260110",
        effective_date="20260110", record_date="20260111")
    row = reconcile(producer, [first, subsequent])
    assert row["known_event_share_balance"] == "1500"
    assert row["announced_gross_cash_entitlement"] == "2250"
    assert row["unsettled_gross_cash_entitlement"] == "2250"
    assert row["confirmed_cash_receipt"] == ""
    assert_research_lock(row)


def test_duplicate_event_rejected(producer):
    e = event()
    with pytest.raises(ValueError):
        reconcile(producer, [e, copy.deepcopy(e)])


@pytest.mark.parametrize("updates", [
    {"kind": "unregistered_event"}, {"documents": []},
    {"entitlement_date": "20260230"}, {"effective_date": "2026-01-05"},
    {"tradable_date": "20260199"}, {"scheduled_payment_date": "tomorrow"},
    {"actual_payment_date": "NaN"}, {"record_date": "20260100"},
    {"suspension_start": "20260109", "suspension_end": "20260108"},
    {"tradable_date": "20260104"}, {"new_shares_per_old_share": "-1"},
    {"new_shares_per_old_share": "NaN"}, {"new_shares_per_old_share": "Infinity"},
    {"cash_per_old_share": "-1"}, {"share_factor": "-1"},
])
def test_invalid_event_fails_closed(producer, updates):
    invalid = event()
    invalid.update(updates)
    with pytest.raises(ValueError):
        reconcile(producer, [invalid])


@pytest.mark.parametrize("updates", [
    {"shares": "-1"}, {"shares": "NaN"}, {"shares": "Infinity"},
    {"entry_open": "-1"}, {"exit_close": "NaN"},
    {"entry_date": "20260230"}, {"exit_date": "20260100"},
    {"entry_date": "20260121"},
])
def test_invalid_position_fails_closed(producer, updates):
    with pytest.raises(ValueError):
        reconcile(producer, [event()], **updates)


def test_signal_identity_must_match_position(producer):
    with pytest.raises(ValueError):
        producer.reconcile_position(trade(), [event()], dict(stock_id="4747", signal_date="20260101"))
    with pytest.raises(ValueError):
        producer.reconcile_position(trade(), [event()], dict(stock_id="5386", signal_date="20260102"))


def test_input_rows_immutable_and_full_raw_source_lineage(producer):
    t, s, events = trade(unused_original_field="must-remain"), signal(), [event()]
    before = copy.deepcopy((t, s, events))
    row = producer.reconcile_position(t, events, s)
    assert (t, s, events) == before
    assert json.loads(row["source_row_json"]) == t
    encoded = json.dumps(s, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert row["source_signal_sha256"] == hashlib.sha256(encoded).hexdigest()
    encoded_trade = json.dumps(t, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert row["source_trade_sha256"] == hashlib.sha256(encoded_trade).hexdigest()
    assert_research_lock(row)


def test_frozen_contract_scope_and_all_embedded_source_hashes():
    c = configuration()
    assert c["stock_ids"] == ["4747", "5386", "6461", "6669"]
    assert c["expected_source_counts"] == {"signals": 59, "trades": 90, "blocked": 381}
    assert set(f"{STEM}_{suffix}" for suffix in c["output_kinds"]) == OUTPUT_NAMES
    for flag in ("coverage_complete", "individual_cash_receipts_verified", "formal_use",
                 "promotion_evidence_allowed", "total_return_verified"):
        assert c[flag] is False
    for doc in c["documents"].values():
        raw = base64.b64decode(doc["payload_base64"], validate=True)
        assert len(raw) == doc["bytes"]
        assert hashlib.sha256(raw).hexdigest() == doc["sha256"]
        assert doc["first_publication_verified"] is False
        assert doc["original_revision_chain_verified"] is False


def test_validator_independent_of_producer_and_business_logic():
    path = ROOT / "scripts" / f"validate_{STEM}.py"
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not any(name.startswith(("build_", "scripts.build_")) for name in imports)
    assert "importlib" not in imports
    assert not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                   and node.func.id in ("__import__", "exec", "eval") for node in ast.walk(tree))


def test_economic_duplicate_with_different_id_is_rejected(producer):
    with pytest.raises(ValueError):
        reconcile(producer, [event(), event(event_id="different-id-same-economic-event")])


def test_unverified_actual_payment_date_is_not_a_cash_receipt(producer):
    row = reconcile(producer, [event("cash_dividend", actual_payment_date="20260112")])
    assert row["confirmed_cash_receipt"] == ""
    assert row["unsettled_gross_cash_entitlement"] == "1500"
    assert_research_lock(row)


@pytest.fixture
def writer_root(tmp_path):
    target = tmp_path / "writer-repository"
    (target / "config").mkdir(parents=True)
    name = "model_research_artifact_ownership.csv"
    (target / "config" / name).write_bytes((ROOT / "config" / name).read_bytes())
    return target


def test_writer_only_exact_five_owned_artifacts(producer, writer_root):
    payloads = {name: b"synthetic-writer-probe\n" for name in OUTPUT_NAMES}
    ownership = writer_root / "config/model_research_artifact_ownership.csv"
    before = ownership.read_bytes()
    producer.write_outputs(writer_root, payloads)
    written = {path.relative_to(writer_root).as_posix() for path in writer_root.rglob("*") if path.is_file()}
    expected = {(OUT_REL / name).as_posix() for name in OUTPUT_NAMES}
    assert written == expected | {"config/model_research_artifact_ownership.csv"}
    assert ownership.read_bytes() == before
    for name in OUTPUT_NAMES:
        assert (writer_root / OUT_REL / name).read_bytes() == payloads[name]


@pytest.mark.parametrize("bad_name", [
    "extra.csv", "../escape.csv", "../../outside.csv", "/absolute.csv",
    "F:/unapproved.csv", "..\\escape.csv",
    "tdcc_stealth_accumulation_operation_replay_trades_v3.csv",
])
def test_writer_rejects_extra_or_escaping_names_before_any_write(producer, writer_root, bad_name):
    payloads = {name: b"synthetic\n" for name in OUTPUT_NAMES}
    payloads[bad_name] = b"forbidden\n"
    with pytest.raises(ValueError):
        producer.write_outputs(writer_root, payloads)
    assert not (writer_root / OUT_REL).exists()


def test_writer_rejects_missing_or_non_bytes_payloads(producer, writer_root):
    payloads = {name: b"synthetic\n" for name in OUTPUT_NAMES}
    first = sorted(payloads)[0]
    del payloads[first]
    with pytest.raises(ValueError):
        producer.write_outputs(writer_root, payloads)
    payloads[first] = "not bytes"
    with pytest.raises(ValueError):
        producer.write_outputs(writer_root, payloads)
    assert not (writer_root / OUT_REL).exists()


@pytest.mark.parametrize("symlink_part", ["output", "artifact"])
def test_writer_rejects_symlink_parent_or_artifact_without_following_it(
    producer, writer_root, monkeypatch, symlink_part,
):
    destination = writer_root / OUT_REL
    destination.mkdir(parents=True)
    blocked = writer_root / "output" if symlink_part == "output" else destination / sorted(OUTPUT_NAMES)[0]
    if symlink_part == "artifact":
        blocked.write_bytes(b"original")
    original = Path.is_symlink
    monkeypatch.setattr(Path, "is_symlink", lambda path: path == blocked or original(path))
    with pytest.raises(ValueError, match="symlink|reparse"):
        producer.write_outputs(writer_root, {name: b"synthetic\n" for name in OUTPUT_NAMES})
    assert not any(path.read_bytes() == b"synthetic\n" for path in destination.iterdir() if path.is_file())


@pytest.mark.parametrize("change", ["payload", "hash", "size", "origin", "pit", "retrieval"])
def test_validator_rejects_unproven_or_mutated_official_sources(validator, change):
    c = configuration()
    doc = c["documents"]["tpex_5386_capital_detail.json"]
    if change == "payload":
        doc["payload_base64"] = base64.b64encode(b"altered official bytes").decode()
    elif change == "hash":
        doc["sha256"] = "0" * 64
    elif change == "size":
        doc["bytes"] += 1
    elif change == "origin":
        doc["url"] = "https://unproven.invalid/fake-official-source"
    elif change == "pit":
        doc["first_publication_verified"] = True
    else:
        doc["retrieved_at"] = "2026-01-01"
    with pytest.raises(ValueError):
        validator.verify_official_sources(c)


def test_pinned_contract_and_official_sources_independently_validate(validator):
    assert len(validator.verify_contract(configuration())) == 5


@pytest.mark.parametrize("change", ["source_hash", "source_ref", "coverage", "rate", "orphan", "duplicate"])
def test_producer_and_validator_reject_changed_contract(producer, validator, tmp_path, change):
    c = configuration()
    if change == "source_hash":
        c["source_files"]["trades"]["sha256"] = "0" * 64
    elif change == "source_ref":
        c["source_ref"] = "0" * 40
    elif change == "coverage":
        c["coverage_complete"] = True
    elif change == "rate":
        c["events"][0]["share_factor"] = "3"
    elif change == "orphan":
        c["events"][0]["documents"] = ["unregistered-source"]
    else:
        c["events"].append(copy.deepcopy(c["events"][0]))
    root = tmp_path / "bad-contract"
    path = root / CONFIG_REL
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(c, ensure_ascii=False), encoding="utf-8")
    with pytest.raises(ValueError):
        producer.load_contract(root)
    with pytest.raises(ValueError):
        validator.verify_contract(c)


@pytest.mark.parametrize("payload", [b'{"x":1,"x":2}', b'{"x":NaN}', b'\xef\xbb\xbf{}'])
def test_validator_rejects_ambiguous_json_transport(validator, payload):
    with pytest.raises(ValueError):
        validator.json_value(payload)


@pytest.mark.parametrize("payload", [b"a,a\n1,2\n", b"a,b\n1\n", b"a,b\n1,2,3\n",
                                      b"a,b\r\n1,2\r\n", b"\xef\xbb\xbfa,b\n1,2\n"])
def test_validator_rejects_malformed_or_unbound_csv_transport(validator, payload):
    with pytest.raises(ValueError):
        validator.csv_records(payload, strict_transport=True)


@pytest.fixture(scope="module")
def frozen_artifacts():
    """Read fixed Git once; build byte payloads in memory, never write outputs."""
    build_module = module("build")
    check_module = module("validate")
    c = configuration()
    sources = check_module.fixed_sources(ROOT, c)
    artifacts = build_module.build(ROOT)
    return check_module, c, sources, artifacts


def test_real_frozen_source_hashes_and_in_memory_artifacts(frozen_artifacts, monkeypatch):
    check, c, sources, artifacts = frozen_artifacts
    assert {key: len(sources[key]) for key in ("signals", "trades", "blocked")} == c["expected_source_counts"]
    assert set(artifacts) == OUTPUT_NAMES
    # fixed_sources above already verified the immutable real Git bytes and SHA-256.
    monkeypatch.setattr(check, "fixed_sources", lambda root, contract: copy.deepcopy(sources))
    assert check.validate_artifacts(ROOT, c, artifacts) == []


def rebind_artifact(manifest_payload, name, payload):
    manifest = json.loads(manifest_payload)
    manifest["artifacts"][name] = {"sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload)}
    return (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


@pytest.mark.parametrize("suffix", ["events_v1.csv", "positions_v1.csv", "blocked_v1.csv", "report_v1.md"])
def test_artifact_byte_mutation_breaks_manifest_binding(frozen_artifacts, monkeypatch, suffix):
    check, c, sources, original = frozen_artifacts
    monkeypatch.setattr(check, "fixed_sources", lambda root, contract: copy.deepcopy(sources))
    artifacts = dict(original)
    name = f"{STEM}_{suffix}"
    artifacts[name] += b"\n"
    assert check.validate_artifacts(ROOT, c, artifacts)


@pytest.mark.parametrize("field,value", [
    ("known_event_share_balance", "999999"), ("pending_share_rights", "999999"),
    ("announced_gross_cash_entitlement", "999999"), ("confirmed_cash_receipt", "0"),
    ("verified_total_return_pct", "12.5"), ("formal_use", "True"),
    ("promotion_evidence_allowed", "True"), ("total_return_verified", "True"),
    ("coverage_complete", "True"), ("strict_lock_released", "True"),
    ("primary_row_retained", "False"), ("source_trade_sha256", "0" * 64),
    ("source_signal_sha256", "0" * 64), ("source_row_json", "{}"),
    ("original_proxy_net_return_pct", "0"), ("exit_date", "20261231"),
])
def test_independent_replay_rejects_semantic_tamper_even_if_manifest_rehashed(
    frozen_artifacts, monkeypatch, field, value,
):
    check, c, sources, original = frozen_artifacts
    monkeypatch.setattr(check, "fixed_sources", lambda root, contract: copy.deepcopy(sources))
    artifacts = dict(original)
    name = f"{STEM}_positions_v1.csv"
    parsed = list(csv.DictReader(io.StringIO(artifacts[name].decode("utf-8"))))
    assert parsed[0][field] != value
    parsed[0][field] = value
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(parsed[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(parsed)
    artifacts[name] = stream.getvalue().encode("utf-8")
    manifest_name = f"{STEM}_source_manifest_v1.json"
    artifacts[manifest_name] = rebind_artifact(artifacts[manifest_name], name, artifacts[name])
    assert check.validate_artifacts(ROOT, c, artifacts)


@pytest.mark.parametrize("mutation", ["missing", "extra", "foreign", "manifest_count", "manifest_formal"])
def test_validator_exact_artifact_set_and_manifest_contract(frozen_artifacts, monkeypatch, mutation):
    check, c, sources, original = frozen_artifacts
    monkeypatch.setattr(check, "fixed_sources", lambda root, contract: copy.deepcopy(sources))
    artifacts = dict(original)
    if mutation == "missing":
        del artifacts[f"{STEM}_events_v1.csv"]
    elif mutation == "extra":
        artifacts["extra.csv"] = b"x\n"
    elif mutation == "foreign":
        artifacts["daily_tdcc_stealth_accumulation_operation_section_latest.csv"] = b"x\n"
    else:
        name = f"{STEM}_source_manifest_v1.json"
        manifest = json.loads(artifacts[name])
        if mutation == "manifest_count":
            manifest["counts"]["positions"] = 89
        else:
            manifest["formal_use"] = True
        artifacts[name] = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    assert check.validate_artifacts(ROOT, c, artifacts)


def test_mutated_git_source_bytes_are_rejected_before_parsing(validator, monkeypatch):
    monkeypatch.setattr(validator, "_git_blob", lambda root, path: b"mutated fixed source")
    with pytest.raises(ValueError, match="SHA-256"):
        validator.fixed_sources(ROOT, configuration())


def require_exact_ledger_lf_attributes(text):
    prefix = (OUT_REL / (STEM + "_")).as_posix()
    actual = [line.split() for line in text.splitlines()
              if line.strip() and not line.lstrip().startswith("#")
              and line.split()[0].startswith(prefix)]
    expected = [[(OUT_REL / name).as_posix(), "text", "eol=lf"] for name in sorted(OUTPUT_NAMES)]
    assert len(actual) == 5
    assert sorted(actual) == expected


def test_gitattributes_exact_five_versioned_ledger_outputs_are_lf():
    require_exact_ledger_lf_attributes((ROOT / ".gitattributes").read_text(encoding="utf-8"))


@pytest.mark.parametrize("mutation", ["missing", "crlf", "duplicate", "family_wildcard"])
def test_gitattributes_missing_or_broadened_ledger_rules_fail_closed(mutation):
    lines = [f"{(OUT_REL / name).as_posix()} text eol=lf" for name in sorted(OUTPUT_NAMES)]
    if mutation == "missing":
        lines.pop()
    elif mutation == "crlf":
        lines[-1] = lines[-1].replace("eol=lf", "eol=crlf")
    elif mutation == "duplicate":
        lines.append(lines[-1])
    else:
        lines.append(f"{OUT_REL.as_posix()}/{STEM}_* text eol=lf")
    with pytest.raises(AssertionError):
        require_exact_ledger_lf_attributes("\n".join(lines))


@pytest.fixture
def checkout_filter_git(tmp_path):
    """A local object-only Git fixture; no commits, remote, or repository staging."""
    root = tmp_path / "lf-git"
    root.mkdir()
    # Python may need an extended Windows path; Git's -C must use its native path.
    git_root = str(root)
    if os.name == "nt" and git_root.startswith("\\\\?\\"):
        git_root = git_root[4:]
    environment = {key: value for key, value in os.environ.items() if not key.upper().startswith("GIT_")}
    environment.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")

    def run(*arguments, input_bytes=None):
        return subprocess.check_output([
            "git", "-c", "core.autocrlf=true", "-c", "core.eol=crlf",
            "-c", "core.safecrlf=false", "-c", "core.longpaths=true",
            "-C", git_root, *arguments,
        ], input=input_bytes, env=environment, stderr=subprocess.PIPE)

    run("init", "--quiet")
    return root, run


def require_effective_checkout_lf(run):
    paths = sorted((OUT_REL / name).as_posix() for name in OUTPUT_NAMES)
    fields = run("check-attr", "-z", "text", "eol", "--", *paths).decode("utf-8").split("\0")
    assert fields[-1] == ""
    triples = list(zip(fields[0:-1:3], fields[1:-1:3], fields[2:-1:3]))
    assert triples == [entry for path in paths for entry in ((path, "text", "set"), (path, "eol", "lf"))]


def checkout_filter_bytes(run, path, payload):
    oid = run("hash-object", "-w", "--stdin", f"--path={path}", input_bytes=payload).decode().strip()
    return run("cat-file", "--filters", f"--path={path}", oid)


def test_git_checkout_filters_preserve_all_five_serialized_bytes_and_hashes(
    checkout_filter_git, frozen_artifacts,
):
    root, run = checkout_filter_git
    attributes = (ROOT / ".gitattributes").read_bytes()
    require_exact_ledger_lf_attributes(attributes.decode("utf-8"))
    (root / ".gitattributes").write_bytes(attributes)
    require_effective_checkout_lf(run)
    _, _, _, artifacts = frozen_artifacts
    assert set(artifacts) == OUTPUT_NAMES
    for name, payload in artifacts.items():
        assert b"\r" not in payload and payload.endswith(b"\n")
        filtered = checkout_filter_bytes(run, (OUT_REL / name).as_posix(), payload)
        assert filtered == payload, name
        assert hashlib.sha256(filtered).hexdigest() == hashlib.sha256(payload).hexdigest(), name
    assert run("ls-files", "--stage") == b""


@pytest.mark.parametrize("mutation", ["missing", "crlf_override", "broad_override"])
def test_git_checkout_filter_probe_detects_missing_or_overridden_lf_rules(checkout_filter_git, mutation):
    root, run = checkout_filter_git
    name = f"{STEM}_report_v1.md"
    target = (OUT_REL / name).as_posix()
    lines = [f"{(OUT_REL / item).as_posix()} text eol=lf" for item in sorted(OUTPUT_NAMES)]
    if mutation == "missing":
        lines.remove(f"{target} text eol=lf")
    elif mutation == "crlf_override":
        lines.append(f"{target} text eol=crlf")
    else:
        lines.append("output/research/** text eol=crlf")
    (root / ".gitattributes").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    with pytest.raises(AssertionError):
        require_effective_checkout_lf(run)
    original = "# 合成 checkout 轉換探針\n\n只測試 byte 綁定。\n".encode("utf-8")
    filtered = checkout_filter_bytes(run, target, original)
    assert filtered != original
    assert b"\r\n" in filtered
    assert hashlib.sha256(filtered).hexdigest() != hashlib.sha256(original).hexdigest()
    assert run("ls-files", "--stage") == b""


@pytest.fixture
def guarded_main_root(producer, writer_root, monkeypatch):
    """Only Git plumbing is replaced; both real guards inspect physical files."""
    sentinel = writer_root / "protected/mature.csv"
    sentinel.parent.mkdir()
    sentinel.write_bytes(b"stock_id,unchanged\n9999,True\n")
    registry = writer_root / "config/model_research_protected_sentinels.csv"
    registry.write_text(
        "sentinel_id,artifact_glob,owner,sentinel_class,required\n"
        "synthetic_mature,protected/mature.csv,another_model,mature_model,True\n",
        encoding="utf-8", newline="\n",
    )
    guard_module = sys.modules[producer.model_owned_artifact_guard.__module__]

    def status_paths(root):
        return {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}

    def immutable_empty_git_mapping(root, *arguments):
        assert arguments in (("ls-tree", "-r", "-z", "HEAD"), ("ls-files", "--stage", "-z"))
        return b""

    monkeypatch.setattr(guard_module, "_git_status_paths", status_paths)
    monkeypatch.setattr(producer, "git", immutable_empty_git_mapping)
    payloads = {name: b"synthetic guarded writer\n" for name in OUTPUT_NAMES}
    return writer_root, sentinel, payloads


def test_main_build_and_write_are_nested_inside_both_actual_guards(producer, guarded_main_root, monkeypatch):
    root, sentinel, payloads = guarded_main_root
    original = sentinel.read_bytes()
    local_guard = producer.artifact_guard
    model_guard = producer.model_owned_artifact_guard
    write = producer.write_outputs
    entered, sequence = set(), []

    @contextmanager
    def observed_local_guard(actual_root):
        assert actual_root == root.resolve()
        with local_guard(actual_root):
            entered.add("local")
            sequence.append("local_enter")
            yield
            sequence.append("local_exit")
            entered.remove("local")

    @contextmanager
    def observed_model_guard(owner, producer_path, **kwargs):
        assert entered == {"local"}
        assert owner == STEM
        assert producer_path == "scripts/build_tdcc_stealth_accumulation_corporate_action_ledger.py"
        assert kwargs == {
            "root": root.resolve(),
            "registry_path": root.resolve() / "config/model_research_artifact_ownership.csv",
            "sentinel_registry_path": root.resolve() / "config/model_research_protected_sentinels.csv",
        }
        with model_guard(owner, producer_path, **kwargs):
            entered.add("model")
            sequence.append("model_enter")
            yield
            sequence.append("model_exit")
            entered.remove("model")

    def guarded_build(actual_root):
        assert actual_root == root.resolve()
        assert entered == {"local", "model"}
        sequence.append("build")
        return payloads

    def guarded_write(actual_root, actual_payloads):
        assert entered == {"local", "model"}
        assert actual_payloads == payloads
        sequence.append("write")
        write(actual_root, actual_payloads)

    monkeypatch.setattr(producer, "artifact_guard", observed_local_guard)
    monkeypatch.setattr(producer, "model_owned_artifact_guard", observed_model_guard)
    monkeypatch.setattr(producer, "build", guarded_build)
    monkeypatch.setattr(producer, "write_outputs", guarded_write)
    assert producer.main(["--repository-root", str(root)]) == 0
    assert sequence == ["local_enter", "model_enter", "build", "write", "model_exit", "local_exit"]
    assert entered == set()
    assert sentinel.read_bytes() == original
    for name in OUTPUT_NAMES:
        assert (root / OUT_REL / name).read_bytes() == payloads[name]


def test_missing_required_sentinel_blocks_main_before_build_or_write(producer, guarded_main_root, monkeypatch):
    root, sentinel, _ = guarded_main_root
    sentinel.unlink()
    calls = []
    monkeypatch.setattr(producer, "build", lambda *args: calls.append("build"))
    monkeypatch.setattr(producer, "write_outputs", lambda *args: calls.append("write"))
    with pytest.raises(RuntimeError, match="required protected sentinel has no files"):
        producer.main(["--repository-root", str(root)])
    assert calls == []
    assert not (root / OUT_REL).exists()


def exception_chain_text(error):
    messages, seen = [], set()
    while error is not None and id(error) not in seen:
        seen.add(id(error))
        messages.append(str(error))
        error = error.__cause__ or error.__context__
    return "\n".join(messages)


@pytest.mark.parametrize("mutate_during", ["build", "write"])
def test_main_sentinel_hash_drift_is_rejected_by_both_guards(
    producer, guarded_main_root, monkeypatch, mutate_during,
):
    root, sentinel, payloads = guarded_main_root
    write = producer.write_outputs

    def drift_build(actual_root):
        if mutate_during == "build":
            sentinel.write_bytes(b"unapproved sentinel drift\n")
        return payloads

    def drift_write(actual_root, actual_payloads):
        if mutate_during == "write":
            sentinel.write_bytes(b"unapproved sentinel drift\n")
        write(actual_root, actual_payloads)

    monkeypatch.setattr(producer, "build", drift_build)
    monkeypatch.setattr(producer, "write_outputs", drift_write)
    with pytest.raises(ValueError, match="Git mapping") as failed:
        producer.main(["--repository-root", str(root)])
    details = exception_chain_text(failed.value)
    assert "protected sentinel hash drift" in details
    assert "unregistered artifact change: protected/mature.csv" in details


@pytest.mark.parametrize("existing", [False, True])
def test_main_forbids_non_allowlisted_physical_writes_without_touching_sentinel(
    producer, guarded_main_root, monkeypatch, existing,
):
    root, sentinel, payloads = guarded_main_root
    original = sentinel.read_bytes()
    outside = root / "outside-ledger-allowlist.txt"
    if existing:
        outside.write_bytes(b"preexisting user data\n")

    def outside_write_build(actual_root):
        outside.write_bytes(b"unapproved addition or overwrite\n")
        return payloads

    monkeypatch.setattr(producer, "build", outside_write_build)
    with pytest.raises(ValueError, match="Git mapping") as failed:
        producer.main(["--repository-root", str(root)])
    assert "unregistered artifact change: outside-ledger-allowlist.txt" in exception_chain_text(failed.value)
    assert sentinel.read_bytes() == original
