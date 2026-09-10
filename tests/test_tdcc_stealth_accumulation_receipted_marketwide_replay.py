"""Synthetic replay regressions plus immutable-Git and transport contract probes.

The small fixture replaces only configuration cardinality and technical IO.
The validator independently reconstructs features, selection and cashflows.
Live immutable-source parity is also checked by the model-owned CLI validator.
"""
from __future__ import annotations

import ast
import copy
import csv
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
STEM = "tdcc_stealth_accumulation_receipted_marketwide_replay"


def load_module(prefix):
    paths = {
        "build": "scripts/build_tdcc_stealth_accumulation_receipted_marketwide_replay.py",
        "validate": "scripts/validate_tdcc_stealth_accumulation_receipted_marketwide_replay.py",
    }
    path = ROOT / paths[prefix]
    spec = importlib.util.spec_from_file_location(prefix + "_receipted_replay_test", path)
    module = importlib.util.module_from_spec(spec)
    previous_path = list(sys.path)
    try:
        sys.path.insert(0, str(ROOT / "scripts"))
        spec.loader.exec_module(module)
    finally:
        sys.path[:] = previous_path
    return module


@pytest.fixture
def producer():
    return load_module("build")


@pytest.fixture
def validator():
    return load_module("validate")


def encode_csv(rows, fields=None):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields or list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def decode_csv(payload):
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8"))))


def real_configuration():
    contract = json.loads((ROOT / "config" / f"{STEM}_v1.json").read_text(encoding="utf-8"))
    availability = json.loads((ROOT / "config/tdcc_stealth_accumulation_receipted_marketwide_availability_v1.json").read_text(encoding="utf-8"))
    return contract, availability


@pytest.fixture
def synthetic(monkeypatch, producer, validator):
    contract, _ = real_configuration()
    contract.update(requested_signal_end="20260703", as_of="20260703")
    dates = ["20260615", "20260617", "20260624", "20260625"]
    refs = {hashlib.sha1(d.encode()).hexdigest(): d for d in dates}
    calendar_ref = "7ef37a966280201a5ee236856306fdb513de7092"
    evidence = dict(receipts=[dict(id="fixture_" + d, ref=ref, signal_dates=[d],
        available_no_later_than=f"2026-06-{d[-2:]}T12:00:00Z",
        source_timestamp_verbatim=f"2026-06-{d[-2:]}T12:00:00Z") for ref, d in refs.items()],
        calendar_sources=[calendar_ref + ":config/twse_non_trading_days.csv",
                          calendar_ref + ":data/market_calendar/exceptional_non_trading_days.csv"],
        calendar_complete_coverage_verified=False, corporate_action_coverage_verified=False,
        retained_anomaly_candidates=[dict(signal_date="20260615", stock_id="1111", horizon=5,
            net_return_pct="9", entry_date="20260616", exit_date="20260624")])
    input_files, outcome_files = {}, {}
    day = datetime(2026, 5, 1)
    while day <= datetime(2026, 7, 3):
        date = day.strftime("%Y%m%d")
        if day.weekday() < 5 and date != "20260619":
            rows = []
            for stock in ("1111", "2222", "3333", "4444", "0050"):
                if stock == "4444" and date < "20260610":
                    continue
                rows.append(dict(date=date, stock_id=stock, stock_name="合成測試", market="TWSE",
                    open="100", high="101", low="99", close="100", volume="1000000",
                    trading_value="100000000", source="TWSE_RWD_JSON_MI_INDEX"))
            outcome = copy.deepcopy(rows)
            if date == "20260616":
                outcome = [r for r in outcome if r["stock_id"] != "2222"]
            if date == "20260624":
                outcome = [r for r in outcome if r["stock_id"] != "3333"]
                for row in outcome:
                    if row["stock_id"] == "1111":
                        row.update(open="110", high="111", low="109", close="110")
            for path in (f"data/daily_price/{date}.csv", f"data/daily_price/daily_price_{date}.csv"):
                input_files[path] = encode_csv(rows)
                outcome_files[path] = encode_csv(outcome)
        day += timedelta(days=1)
    for n, date in enumerate(("20260522", "20260529", "20260605", "20260612")):
        rows = [dict(date=date, code=s, name="合成測試", over_400_pct=str(40+n),
                     over_600_pct=str(35+n), over_800_pct=str(30+n), over_1000_pct=str(25+n))
                for s in ("1111", "2222", "3333", "4444")]
        input_files[f"output/history/tdcc/tdcc_holder_ratio_{date}.csv"] = encode_csv(rows)
    references = ["scripts/build_tdcc_stealth_accumulation_historical_replay.py",
        "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py", "tdcc_trend_utils.py",
        "scripts/build_stock_price_history.py", "scripts/build_tdcc_stealth_accumulation_operation_replay.py",
        "docs/specs/tdcc_stealth_accumulation_operation_replay_v3.md"]
    for path in references:
        input_files[path] = outcome_files[path] = b"# Synthetic provenance fixture; never executed.\n"
    for path, data in {"config/twse_non_trading_days.csv": b"date\n20260619\n",
                       "data/market_calendar/exceptional_non_trading_days.csv": b"date\n"}.items():
        input_files[path] = outcome_files[path] = data

    def contents(ref):
        files = outcome_files if ref == contract["outcome_ref"] else input_files
        cutoff = refs.get(ref, "99999999")
        return {p: b for p, b in files.items() if not (p.startswith("data/daily_price/")
            and p[-12:-4] > cutoff)}

    class MemorySource:
        def __init__(self, root):
            self.sources, self._prices = {}, {}

        def tree(self, ref):
            return {p: hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
                    for p, b in contents(ref).items()}

        def blob(self, ref, path):
            data = contents(ref)[path]
            self.sources[ref, path] = dict(ref=ref, path=path, git_blob_oid=self.tree(ref)[path],
                bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            return data

    class MemoryReader(validator.GitReader):
        def tree(self, ref):
            return MemorySource(self.root).tree(ref)

        def read(self, ref, path):
            data = contents(ref)[path]
            self.used[ref, path] = dict(ref=ref, path=path, git_blob_oid=self.tree(ref)[path],
                bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
            return data

    def fixture_selector(source, config):
        for path in references[:3]:
            source.blob(config["classifier_ref"] if path == "tdcc_trend_utils.py" else config["selector_ref"], path)
        def choose(row):
            # Fixture prices are flat, positive accumulation, volume ratio=1, no attack.
            warmed = all(row.get(k) not in (None, "") for k in ("high_20", "low_20", "previous_close"))
            return dict(selector_selected=warmed, attack_already_started=False,
                        tdcc_positive_resolution="recognized_enum_positive_fallback")
        def classify(*args):
            return "strong_accumulation", "近幾週400張與1000張同步累積"
        return choose, classify

    monkeypatch.setattr(producer, "GitSource", MemorySource)
    monkeypatch.setattr(producer, "load_selector", fixture_selector)
    monkeypatch.setattr(validator, "GitReader", MemoryReader)
    # Configuration cardinality is tested separately against the genuine 40-date contract.
    monkeypatch.setattr(validator, "_contract_errors", lambda c, a: [])
    return contract, evidence, input_files, outcome_files


def test_real_configuration_pins_and_false_promotion_flags(producer, validator):
    contract, evidence = real_configuration()
    producer.validate_contract(contract)
    assert validator._contract_errors(contract, evidence) == []
    assert len(evidence["receipts"]) == 40
    assert sum("20260730" in r["signal_dates"] for r in evidence["receipts"]) == 1
    assert len(evidence["retained_anomaly_candidates"]) == 200
    assert evidence["prior_candidate_ledger_binding"]["sha256"] == "e832c3eefcdd1339cc67ab4692c2b7b0166022bf6ac460a631769e38ca6c49a2"
    assert ("20260626", "1709", 5) in {
        (r["signal_date"], r["stock_id"], r["horizon"]) for r in evidence["retained_anomaly_candidates"]
    }
    bad = copy.deepcopy(contract)
    bad["selector_ref"] = "0" * 40
    with pytest.raises(ValueError):
        producer.validate_contract(bad)
    assert validator._contract_errors(bad, evidence)
    bad = copy.deepcopy(contract)
    bad["formal_use"] = True
    assert validator._contract_errors(bad, evidence)


@pytest.mark.parametrize("mutation", ["anomalies", "calendar", "receipt_ref", "receipt_job", "contract_text"])
def test_approved_configuration_cannot_be_rebound(validator, mutation):
    contract, evidence = real_configuration()
    if mutation == "anomalies":
        evidence["retained_anomaly_candidates"] = []
    elif mutation == "calendar":
        evidence["calendar_sources"] = []
    elif mutation == "receipt_ref":
        evidence["receipts"][0]["ref"] = contract["outcome_ref"]
    elif mutation == "receipt_job":
        evidence["receipts"][0].update(run_id="1", job_id="1",
            url="https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/1/job/1")
    else:
        contract["phase_policy"] = "unapproved replacement"
    assert validator._contract_errors(contract, evidence)


@pytest.mark.parametrize("opening,closing,slip", [(1, 1, 0), (12.3, 24.25, 10), (100, 110, 20), (100, 1, 10)])
def test_cashflow_independent_decimal_parity(producer, validator, opening, closing, slip):
    actual = producer.cost_cashflows(opening, closing, slip)
    expected = validator.cashflow(opening, closing, slip)
    assert actual == expected
    assert Decimal(actual["entry_cash"]) > Decimal(actual["entry_notional"])
    assert Decimal(actual["buy_fee"]) >= 20 and Decimal(actual["sell_fee"]) >= 20


def test_independent_selector_matches_pinned_reference_boundaries(producer, validator):
    contract, _ = real_configuration()
    choose, classify = producer.load_selector(producer.GitSource(ROOT), contract)
    base = dict(open="100", high="101", low="99", close="100", previous_close="100",
                volume_ratio="1", volume_ma20_lots="1000", previous_20d_high_ex_today="101",
                daily_return_calc="0", return_5d="0", return_20d="0", high_20="101", low_20="99",
                tdcc_accumulation_signal="strong_accumulation", tdcc_price_phase="", tdcc_status="",
                volume_confirmed_breakout=False)
    assert choose(base)["selector_selected"]
    cases = [base]
    for key, values in {
        "volume_ratio": ["", "2.4999", "2.5", "2.5001"],
        "return_5d": ["", "7.9999", "8", "8.0001"],
        "return_20d": ["", "19.9999", "20", "20.0001"],
        "tdcc_accumulation_signal": ["mild_accumulation", "neutral", "distribution_warning", "", "unknown"],
        "volume_confirmed_breakout": [True, "true", "false"],
        "high_20": ["", "99", "100"],
    }.items():
        cases.extend(dict(base, **{key: value}) for value in values)
    cases.extend([
        dict(base, close="103", open="101", high="104", low="100", volume_ratio="2", daily_return_calc="3"),
        dict(base, close="110", open="110", high="110", low="110", volume_ratio="1", daily_return_calc="10"),
    ])
    for row in cases:
        actual, expected = choose(row), validator.selector_truth(row)
        assert all(actual[key] == value for key, value in expected.items()), row
    for p400 in ([40, 41, 42, 43], [40, 39, 38, 37], [40, 40, 40, 40], [40, 39, 40, 41]):
        for p1000 in ([20, 21, 22, 23], [20, 19, 18, 17], [20, 20, 20, 20]):
            batches = [dict(p400=a, p1000=b) for a, b in zip(p400, p1000)]
            expected = validator.classify_four_batches(batches)
            enum, description = classify(4, p400[-1]-p400[0], p1000[-1]-p1000[0],
                sum(b>a for a,b in zip(p400,p400[1:])), sum(b>a for a,b in zip(p1000,p1000[1:])))
            assert (enum, description) == (expected["tdcc_accumulation_signal"], expected["tdcc_accumulation_description"])


def test_complete_synthetic_roundtrip_and_determinism(producer, validator, synthetic):
    contract, evidence, _, _ = synthetic
    first = producer.build(ROOT, contract, evidence)
    assert len(first) == 9
    assert first == producer.build(ROOT, contract, evidence)
    assert validator.validate_artifacts(ROOT, contract, evidence, first) == []
    features = decode_csv(first[validator.artifact_name("features")])
    assert {r["signal_date"] for r in features} == {"20260615", "20260617", "20260624", "20260625"}
    assert all(r["stock_id"] != "0050" for r in features)
    assert all(r["feature_supported"] == "False" for r in features if r["stock_id"] == "4444")
    coverage = decode_csv(first[validator.artifact_name("coverage")])
    assert any(not r["receipt_id"] and r["selected_signals"] == "0" for r in coverage)
    trades = decode_csv(first[validator.artifact_name("trades")])
    assert all(r["formal_use"] == "False" and r["total_return_verified"] == "False" for r in trades)
    assert any(r["stock_id"] == "1111" and r["anomaly_candidate"] == "True" for r in trades)
    blocked = decode_csv(first[validator.artifact_name("blocked")])
    reasons = {r["reasons"] for r in blocked}
    assert {"blocked_exit_day", "blocked_active_position", "entry_price_missing_or_invalid",
            "open_unresolved_exit_price", "open_immature"} <= reasons
    assert any(r["stock_id"] == "3333" and r["signal_date"] == "20260625"
               and r["reasons"] == "blocked_active_position" for r in blocked)


def test_late_or_duplicate_receipt_fails_closed(producer, synthetic):
    contract, evidence, _, _ = synthetic
    bad = copy.deepcopy(evidence)
    bad["receipts"][0]["available_no_later_than"] = "2026-06-16T08:30:00+08:00"
    with pytest.raises(ValueError):
        producer.build(ROOT, contract, bad)
    duplicate = copy.deepcopy(evidence)
    duplicate["receipts"].append(copy.deepcopy(duplicate["receipts"][0]))
    with pytest.raises(ValueError):
        producer.build(ROOT, contract, duplicate)


def test_volume_lineage_only_last_twenty_observations(producer, validator, synthetic):
    contract, evidence, inputs, _ = synthetic
    initial = producer.build(ROOT, contract, evidence)
    row = next(r for r in decode_csv(initial[validator.artifact_name("features")])
               if r["signal_date"] == "20260615" and r["stock_id"] == "1111")
    dates = row["observed_history_dates"].split(";")
    def legacy(date):
        path = f"data/daily_price/{date}.csv"
        rows = decode_csv(inputs[path])
        for r in rows:
            if r["stock_id"] == "1111":
                r["source"] = "TPEX_OLD_DAILY_JSON"
        inputs[path] = inputs[f"data/daily_price/daily_price_{date}.csv"] = encode_csv(rows)
    legacy(dates[0])
    result = producer.build(ROOT, contract, evidence)
    row = next(r for r in decode_csv(result[validator.artifact_name("features")])
               if r["signal_date"] == "20260615" and r["stock_id"] == "1111")
    assert row["feature_supported"] == "True"
    legacy(dates[1])
    result = producer.build(ROOT, contract, evidence)
    row = next(r for r in decode_csv(result[validator.artifact_name("features")])
               if r["signal_date"] == "20260615" and r["stock_id"] == "1111")
    assert row["feature_supported"] == "False"
    assert "raw_volume_lineage_unresolved" in row["unsupported_reasons"]


@pytest.mark.parametrize("kind", ["features", "signals", "trades", "summary", "blocked", "anomalies", "coverage"])
def test_mutated_output_is_rejected_even_with_rehashed_manifest(producer, validator, synthetic, kind):
    contract, evidence, _, _ = synthetic
    payloads = producer.build(ROOT, contract, evidence)
    name = validator.artifact_name(kind)
    rows = decode_csv(payloads[name])
    assert rows
    rows[0][next(iter(rows[0]))] = "tampered"
    payloads[name] = encode_csv(rows)
    manifest_name = validator.artifact_name("source_manifest")
    manifest = json.loads(payloads[manifest_name])
    manifest["hashes"][name] = dict(bytes=len(payloads[name]), sha256=hashlib.sha256(payloads[name]).hexdigest())
    payloads[manifest_name] = producer.json_bytes(manifest)
    assert validator.validate_artifacts(ROOT, contract, evidence, payloads)


@pytest.mark.parametrize("prefix,replacement", [(b"\xef\xbb\xbf", False), (b"", True)])
def test_csv_bom_crlf_transport_is_rejected(producer, validator, synthetic, prefix, replacement):
    contract, evidence, _, _ = synthetic
    payloads = producer.build(ROOT, contract, evidence)
    name = validator.artifact_name("summary")
    payloads[name] = prefix + (payloads[name].replace(b"\n", b"\r\n") if replacement else payloads[name])
    assert validator.validate_artifacts(ROOT, contract, evidence, payloads)


def test_validator_does_not_import_or_execute_model_business_functions():
    path = ROOT / "scripts" / f"validate_{STEM}.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    imports = [n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)]
    imports += [a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names]
    assert all("build_tdcc" not in item and "tdcc_trend" not in item for item in imports)
    calls = [n.func.id for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]
    assert not {"exec", "eval", "compile"}.intersection(calls)


def test_new_artifacts_keep_lf_under_windows_checkout(producer):
    paths = sorted(producer.DIRECTORY + "/" + name for name in producer.GENERATED)
    result = subprocess.check_output(
        ["git", "-c", "core.autocrlf=true", "check-attr", "-z", "eol", "--", *paths], cwd=ROOT
    ).decode("utf-8").split("\0")[:-1]
    assert len(result) == 27
    assert {result[i]: result[i+2] for i in range(0, len(result), 3)} == {p: "lf" for p in paths}
    local_lines = [line.split() for line in (ROOT / ".gitattributes").read_text(encoding="utf-8").splitlines()
                   if "tdcc_stealth_accumulation_receipted_marketwide_replay_" in line]
    assert {row[0] for row in local_lines} == set(paths)
    assert all(row[1:] == ["text", "eol=lf"] for row in local_lines)


def test_raw_source_mutation_is_rejected(producer, validator, synthetic):
    contract, evidence, _, outcomes = synthetic
    payloads = producer.build(ROOT, contract, evidence)
    path = "data/daily_price/20260624.csv"
    rows = decode_csv(outcomes[path])
    for row in rows:
        if row["stock_id"] == "1111":
            row["close"] = "109"
    outcomes[path] = outcomes["data/daily_price/daily_price_20260624.csv"] = encode_csv(rows)
    errors = validator.validate_artifacts(ROOT, contract, evidence, payloads)
    assert errors
    assert any("source exact-byte binding mismatch" in item for item in errors)


def test_manifest_cannot_omit_consumed_source(producer, validator, synthetic):
    contract, evidence, _, _ = synthetic
    payloads = producer.build(ROOT, contract, evidence)
    name = validator.artifact_name("source_manifest")
    manifest = json.loads(payloads[name])
    manifest["sources"].pop()
    payloads[name] = producer.json_bytes(manifest)
    assert any("omitted independently consumed" in item
               for item in validator.validate_artifacts(ROOT, contract, evidence, payloads))


def test_tdcc_percentage_invariant_blocks_validation_without_dropping_rows(producer, validator, synthetic):
    contract, evidence, inputs, _ = synthetic
    for path in [p for p in inputs if p.startswith("output/history/tdcc/")]:
        rows = decode_csv(inputs[path])
        for row in rows:
            if row["code"] == "1111":
                row["over_1000_pct"] = str(Decimal(row["over_1000_pct"]) + 100)
        inputs[path] = encode_csv(rows)
    payloads = producer.build(ROOT, contract, evidence)
    features = decode_csv(payloads[validator.artifact_name("features")])
    assert any(r["stock_id"] == "1111" for r in features)
    errors = validator.validate_artifacts(ROOT, contract, evidence, payloads)
    assert any("invariant" in item.lower() for item in errors)


def test_writer_only_allows_registered_nine_files(producer, monkeypatch):
    root = Path("F:/CodexStorage/task-worktrees/tdcc-replay-memory-only-fixture")
    output = root / producer.DIRECTORY
    payloads = {name: b"fixture\n" for name in producer.GENERATED}
    writes = []
    monkeypatch.setattr(Path, "mkdir", lambda *a, **k: None)
    monkeypatch.setattr(Path, "write_bytes", lambda path, data: writes.append((path, data)))
    producer.write_outputs(root, output, payloads)
    assert {path.name for path, _ in writes} == producer.GENERATED
    assert all(path.parent == output.resolve() for path, _ in writes)
    writes.clear()
    for destination in (root, root / "output/latest", root.parent / "outside",
                        Path("C:/tdcc-replay-forbidden"), producer.SEALED_ROOT / "forbidden"):
        with pytest.raises(ValueError):
            producer.write_outputs(root, destination, payloads)
        assert not writes
    for bad in (dict(payloads, **{"unregistered.csv": b"x"}),
                {name: b"x" for name in list(producer.GENERATED)[1:]}):
        with pytest.raises(ValueError):
            producer.write_outputs(root, output, bad)
        assert not writes
    monkeypatch.setattr(Path, "is_symlink", lambda path: path.name in producer.GENERATED)
    with pytest.raises(ValueError):
        producer.write_outputs(root, output, payloads)
    assert not writes
