"""Independent synthetic and tamper tests; no producer execution or private IO."""
from __future__ import annotations

import ast
import copy
import csv
import gzip
import importlib.util
import io
import json
from decimal import Decimal, localcontext
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_tdcc_stealth_accumulation_current_version_annual_replay.py"


@pytest.fixture
def audit():
    spec = importlib.util.spec_from_file_location("annual_independent_audit_test", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode(rows, fields):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def base_feature(audit, date="20250910", stock="1111"):
    calendar = audit.calendar_days([], "20250401", "20261030")
    i = calendar.index(date)
    observed = calendar[i - 20:i + 1]
    row = dict.fromkeys(audit.FEATURE_FIELDS, "")
    row.update(stock_id=stock, stock_name="合成測試", market="TWSE", signal_date=date,
        volume_confirmed_breakout=False, open="100.0", high="101.0", low="99.0", close="100.0",
        return_5d="0.0000", return_20d="0.0000", daily_return_calc="0.0000",
        previous_close="100.0000", high_20="101.0000", low_20="99.0000",
        previous_20d_high_ex_today="101.0000", volume_ma20="1000000.0000",
        volume_ma20_lots="1000.0000", volume_ratio="1.0000",
        tdcc_accumulation_signal="strong_accumulation", tdcc_accumulation_description="近幾週400張與1000張同步累積",
        tdcc_400_change_sum=3.0, tdcc_1000_change_sum=3.0, tdcc_400_up_weeks=3,
        tdcc_1000_up_weeks=3, feature_id=f"{date}:{stock}", input_ref=audit.PRICE_REF,
        universe_source_path=f"data/daily_price/{date}.csv", universe_source_sha256=audit.digest(b"price\n"),
        observed_history_dates=";".join(observed), history_observations=21, history_gap_count=0,
        tdcc_window_dates="20250815;20250822;20250829;20250905", tdcc_paths="a;b;c;d",
        phase_policy="phase_classifier_not_invoked", instrument_note="four_digit_nonzero_equity_code",
        input_availability_proven=False, feature_supported=True, raw_selector_selected=True,
        selected=True, positive_resolution="recognized_enum_positive_fallback", attack_already_started=False,
        primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False)
    return row


def simple_price(audit, date, stock="1111", closing=100):
    return dict(stock_id=stock, stock_name="合成測試", market="TWSE", date=date,
        open=100.0, high=max(101.0, closing), low=99.0, close=float(closing), volume=1000000.0,
        trading_value=100000000.0, source="OFFICIAL", source_path=f"data/daily_price/{date}.csv",
        source_ref=audit.PRICE_REF, source_sha256=audit.digest(b"price\n"),
        duplicate_key=False, date_mismatch=False, alias_payload_conflict=False)


def test_source_module_has_no_producer_import_or_executable_frozen_ast():
    tree = ast.parse(VALIDATOR.read_text(encoding="utf-8"))
    allowed_modules = {"__future__", "argparse", "bisect", "csv", "gzip", "hashlib", "io", "json", "math", "re", "statistics", "subprocess", "collections", "datetime", "decimal", "pathlib"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert all(alias.name in allowed_modules for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            assert node.module in allowed_modules
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "compile", "__import__"}


def test_real_annual_contract_exact_pin(audit):
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_text(encoding="utf-8"))
    assert audit._contract_errors(contract) == []
    for field, value in (("input_availability_proven", True), ("price_source_ref", "0" * 40),
                         ("requested_signal_start", "20260910"), ("history_start", "20250701")):
        changed = copy.deepcopy(contract)
        changed[field] = value
        assert audit._contract_errors(changed)


@pytest.mark.parametrize("field,value,selected", [
    ("volume_ratio", "2.4999", True), ("volume_ratio", "2.5000", False),
    ("return_5d", "7.9999", True), ("return_5d", "8.0000", False),
    ("return_20d", "19.9999", True), ("return_20d", "20.0000", False),
    ("tdcc_accumulation_signal", "mild_accumulation", True),
    ("tdcc_accumulation_signal", "neutral", False),
    ("tdcc_accumulation_signal", "unknown", False),
    ("tdcc_accumulation_signal", "", False),
    ("high_20", "99.0000", False), ("volume_confirmed_breakout", True, False),
])
def test_frozen_selector_boundaries(audit, field, value, selected):
    assert audit.selector_truth(dict(base_feature(audit), **{field: value}))["selector_selected"] is selected


def test_attack_veto_includes_normal_and_locked_breakout(audit):
    base = base_feature(audit)
    normal = dict(base, close="104", high="105", open="100", volume_ratio="2.0000")
    locked = dict(base, open="110", high="110", low="110", close="110", daily_return_calc="10.0000")
    for row in (normal, locked):
        result = audit.selector_truth(row)
        assert result["attack_already_started"] is True
        assert result["selector_selected"] is False


@pytest.mark.parametrize("bins,expected", [
    ([dict(p400=40 + i, p1000=20 + i) for i in range(4)], "strong_accumulation"),
    ([dict(p400=40, p1000=20), dict(p400=39, p1000=19), dict(p400=38, p1000=18), dict(p400=41, p1000=21)], "mild_accumulation"),
    ([dict(p400=40 + i, p1000=20) for i in range(4)], "mild_accumulation"),
    ([dict(p400=40 - i, p1000=20 - i) for i in range(4)], "distribution_warning"),
])
def test_independent_four_batch_classification(audit, bins, expected):
    assert audit.classify_four_batches(bins)["tdcc_accumulation_signal"] == expected


def test_raw_decimal_bin_sum_does_not_create_phantom_positive(audit):
    levels = ("400,001-600,000", "600,001-800,000", "800,001-1,000,000", "more than 1,000,001")
    data, specs = {}, []
    for i, date in enumerate(("20250815", "20250822", "20250829", "20250905")):
        ratios = ("0.15", "0.15", "0", "0") if i < 2 else ("0.1", "0.2", "0", "0")
        rows = [dict(日期=date, 股票代碼="1111", 持股分級=level, 比例=value) for level, value in zip(levels, ratios)]
        data[date] = encode(rows, ["日期", "股票代碼", "持股分級", "比例"])
        specs.append(dict(kind="tdcc", path=date, date=date, rows=4))
    class Inputs:
        def read(self, item): return data[item["path"]]
    weeks = audit.private_tdcc(Inputs(), dict(external_files=specs, expected_tdcc_weeks=4, expected_tdcc_rows=16))
    batches = [weeks[d]["1111"] for d in sorted(weeks)]
    assert {row["p400"] for row in batches} == {0.3}
    assert audit.classify_four_batches(batches)["tdcc_accumulation_signal"] == "neutral"
    assert audit.classify_four_batches(batches)["tdcc_400_change_sum"] == 0


def test_minimum_fee_cashflows_are_exact_and_context_independent(audit):
    with localcontext() as context:
        context.prec = 6
        result = audit.cashflow(1, 1, 0)
    assert Decimal(result["entry_notional"]) == 1000
    assert Decimal(result["buy_fee"]) == 20
    assert Decimal(result["sell_fee"]) == 20
    assert Decimal(result["sell_tax"]) == 3
    assert Decimal(result["net_pnl"]) == -43
    assert result["outcome"] == "failure"
    expected = audit.cashflow(100, 110, 0)
    assert Decimal(expected["buy_fee"]) == Decimal("142.500000")
    assert Decimal(expected["net_pnl"]) == Decimal("9370.750000")
    with pytest.raises(ValueError): audit.cashflow(100, 110, 5)
    with pytest.raises(ValueError): audit.cashflow("nan", 110, 10)


def test_horizon_independent_lock_exit_day_and_strict_unproven(audit):
    calendar = audit.calendar_days([], "20250901", "20261231")
    contract = dict(as_of="20261130", outcome_ref=audit.PRICE_REF)
    class Prices:
        def daily(self, date): return {"1111": simple_price(audit, date)}, {}
    signals = [base_feature(audit, date) for date in ("20250910", "20250918", "20250919")]
    blocked = []
    trades, strict = audit.reconstruct_operations(Prices(), contract, signals, blocked, calendar)
    assert {(r["signal_date"], r["horizon"]) for r in trades} == {
        ("20250910", 5), ("20250910", 10), ("20250910", 20), ("20250919", 5)}
    assert any(r["signal_date"] == "20250918" and r["horizon"] == 5 and r["reasons"] == "blocked_exit_day" for r in blocked)
    assert all(r["strict_v3_status"] == "blocked_input_availability_unproven" for r in strict)
    assert all(r["strict_entry_established"] is False and r["strict_prior_position_locked"] is False for r in strict)


def test_missing_exit_never_releases_proxy_lock(audit):
    calendar = audit.calendar_days([], "20250901", "20261231")
    class Prices:
        def daily(self, date): return ({}, {}) if date == "20250918" else ({"1111": simple_price(audit, date)}, {})
    blocked = []
    trades, _ = audit.reconstruct_operations(Prices(), dict(as_of="20261130", outcome_ref=audit.PRICE_REF), [base_feature(audit, d) for d in ("20250910", "20250919")], blocked, calendar)
    assert not any(r["horizon"] == 5 for r in trades)
    assert any(r["horizon"] == 5 and r["reasons"] == "open_unresolved_exit_price" for r in blocked)
    assert any(r["signal_date"] == "20250919" and r["horizon"] == 5 and r["reasons"] == "blocked_active_position" for r in blocked)


def test_anomaly_magnitude_only_flags_and_primary_retains(audit):
    trades = [dict(signal_date=f"202509{10 + i}", stock_id=str(1111 + i), horizon=5, slippage_bps=10,
        net_return_pct=str(value), entry_date="20250911", exit_date="20250918", history_gap_count=0)
        for i, value in enumerate((0, 1, 2, 3, 100))]
    anomalies = audit.anomaly_rows(trades, dict(retained_anomaly_candidates=[]))
    assert len(anomalies) == 1
    assert anomalies[0]["disposition"] == "unresolved_anomaly_candidate"
    assert anomalies[0]["primary_row_retained"] is True
    summaries = audit.summarize(trades, [{}] * 5, [])
    primary = next(r for r in summaries if r["horizon"] == 5 and r["slippage_bps"] == 10 and r["population"].startswith("primary"))
    sensitivity = next(r for r in summaries if r["horizon"] == 5 and r["slippage_bps"] == 10 and r["population"].startswith("sensitivity"))
    assert len(summaries) == 18
    assert primary["realized_raw_price_proxy_positions"] == 5
    assert primary["mean_net_return_pct"] == 21.2
    assert sensitivity["realized_raw_price_proxy_positions"] == 4


@pytest.mark.parametrize("value", ["true", "false", "1", "0", "", "yes", None])
def test_boolean_drift_fails_closed(audit, value):
    with pytest.raises(ValueError): audit.bool_value(value)


@pytest.mark.parametrize("mutation", ["bom", "crlf", "missing_lf", "wrong_schema", "extra_column", "gzip_crc"])
def test_streaming_serialization_contract(audit, mutation):
    data = encode([base_feature(audit)], audit.FEATURE_FIELDS)
    if mutation == "bom": data = b"\xef\xbb\xbf" + data
    elif mutation == "crlf": data = data.replace(b"\n", b"\r\n")
    elif mutation == "missing_lf": data = data[:-1]
    elif mutation == "wrong_schema": data = data.replace(b"stock_id", b"stockid", 1)
    elif mutation == "extra_column": data = data[:-1] + b",extra\n"
    payload = gzip.compress(data, mtime=0)
    if mutation == "gzip_crc": payload = payload[:-4] + b"0000"
    with pytest.raises((ValueError, OSError, EOFError)):
        list(audit.rows_for("features", payload))


@pytest.fixture
def bundle(audit, monkeypatch):
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_text(encoding="utf-8"))
    signal = base_feature(audit)
    calendar = audit.calendar_days([], contract["history_start"], contract["calendar_end"])
    dates = [d for d in calendar if contract["requested_signal_start"] <= d <= contract["requested_signal_end"]]
    coverage = []
    for date in dates:
        present = date == signal["signal_date"]
        coverage.append(dict(signal_date=date, input_ref=audit.PRICE_REF, receipt_id="", mother_population_basis="same_day_raw_historical_price_codes_not_candidates", path=f"data/daily_price/{date}.csv", missing=not present, total_rows=int(present), universe_rows=int(present), excluded_code_rows=0, duplicate_keys=0, alias_payload_conflict=False, coverage_status="current_version_research_partial_quality_coverage", pit_supported_rows=0, current_version_supported_rows=int(present), selected_signals=int(present), unsupported_reason_counts="{}", historical_closed_date_files_excluded="", receipt_available_no_later_than="", entry_cutoff="", receipt_gap_audit=""))
    class Prices:
        def daily(self, date): return {"1111": simple_price(audit, date, closing=110)}, {}
    blocked = []
    trades, strict = audit.reconstruct_operations(Prices(), contract, [signal], blocked, calendar)
    evidence = dict(calendar_complete_coverage_verified=False, retained_anomaly_candidates=[], calendar_closures=[])
    anomalies = audit.anomaly_rows(trades, evidence)
    summaries = audit.summarize(trades, [signal], blocked)
    rows = dict(features=[signal], signals=[signal], coverage=coverage, trades=trades, summary=summaries, blocked=blocked + strict, anomalies=anomalies)
    counts = dict(requested_session_dates=len(dates), current_version_signal_dates=dates, tdcc_weeks=55, tdcc_rows=3667325, unique_universe_stocks=1, missing_price_dates=[d for d in dates if d != signal["signal_date"]], possible_TDR_universe_rows=0, supplemental=dict(warmup_nonquote_rows=0, supplemental_price_rows=0), covered_universe_rows=1, supported_feature_rows=1, signals=1, realized_proxy_trade_rows=9, anomaly_candidates=0, signals_with_history_gaps=0, anomaly_candidates_current_proxy_keys=0, anomaly_candidates_removed_from_primary=0, strict_verified_total_return_positions=0, strict_ledger_rows=3, strict_status_counts={"blocked_input_availability_unproven": 3})
    sources = {}
    for ref, path in audit.reference_pairs(contract):
        data = b"date\n" if path.endswith(".csv") else b'{"retained_anomaly_candidates":[]}' if path == contract["anomaly_retention_reference"]["path"] else b"# never executed\n"
        sources[ref, path] = data
    sources[audit.PRICE_REF, signal["universe_source_path"]] = b"price\n"
    for row in trades:
        for side in ("entry", "exit"):
            sources[audit.PRICE_REF, row[side + "_source_path"]] = b"price\n"
    class MemoryGit:
        def __init__(self, root): self.used = {}
        def read(self, ref, path):
            data = sources[ref, path]
            self.used[ref, path] = dict(ref=ref, path=path, git_blob_oid="1" * 40, bytes=len(data), sha256=audit.digest(data))
            return data
    monkeypatch.setattr(audit, "GitReader", MemoryGit)
    report = ["TDCC 目前取得歷史版本 不是 strict PIT formal_use=False promotion_evidence_allowed=False full_period_pit_complete=False input_availability_proven=False unresolved_anomaly_candidate 保留 primary sensitivity 不是已核實 total-return",
        "訊號範圍：20250910–20260909；結果資料 as_of：20260909。",
        f"研究訊號日期 {len(dates)}；實際特徵列 1；支持特徵列 1；訊號 1。",
        "價格 proxy 交易列 9（每部位三種情境）；異常候選 0。"]
    for row in summaries:
        if row["slippage_bps"] == 10 and row["population"].startswith("primary"):
            report.append(f"| D+{row['horizon']} | 1 | 1/0/0 | {row['mean_net_return_pct']:.6f} | {row['median_net_return_pct']:.6f} |")
    for row in summaries:
        if row["slippage_bps"] == 10 and row["population"].startswith("primary"):
            report.append(f"| D+{row['horizon']} | 100.000000 | {row['high_return_ge10_rate_pct']:.6f} | 0.000000 | {row['min_net_return_pct']:.6f} / {row['max_net_return_pct']:.6f} | 0 / 0 |")
    for row in summaries:
        if row["slippage_bps"] == 10 and row["population"].startswith("sensitivity"):
            report.append(f"| D+{row['horizon']} | 1 | {row['mean_net_return_pct']:.6f} | {row['median_net_return_pct']:.6f} | 100.000000 |")
    artifacts = {}
    for kind, values in rows.items():
        data = encode(values, audit.SCHEMAS[kind])
        artifacts[audit.artifact_name(kind)] = gzip.compress(data, mtime=0) if audit.KINDS[kind].endswith(".gz") else data
    artifacts[audit.artifact_name("report")] = ("\n".join(report) + "\n").encode("utf-8")
    manifest = dict(model_id=audit.MODEL_ID, artifact_version=audit.ARTIFACT_VERSION, contract_file=audit.CONTRACT_FILE, contract=contract, contract_sha256=audit.digest(audit.canonical_json(contract)), formal_use=False, promotion_evidence_allowed=False, full_period_pit_complete=False, evidence=evidence, counts=counts, external_sources=[dict(r, bytes=1) for r in contract["external_files"]], sources=[dict(ref=ref, path=path, git_blob_oid="1" * 40, bytes=len(data), sha256=audit.digest(data)) for (ref, path), data in sorted(sources.items())])
    manifest["hashes"] = {name: dict(bytes=len(data), sha256=audit.digest(data)) for name, data in artifacts.items()}
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest)
    return contract, artifacts


def replace_rows(audit, artifacts, kind, mutate):
    name = audit.artifact_name(kind)
    rows = list(audit.rows_for(kind, artifacts[name]))
    mutate(rows)
    data = encode(rows, audit.SCHEMAS[kind])
    artifacts[name] = gzip.compress(data, mtime=0) if audit.KINDS[kind].endswith(".gz") else data
    manifest = json.loads(artifacts[audit.artifact_name("source_manifest")])
    manifest["hashes"][name] = dict(bytes=len(artifacts[name]), sha256=audit.digest(artifacts[name]))
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest)


def test_synthetic_published_bundle_passes_without_private_inputs(audit, bundle):
    contract, artifacts = bundle
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True) == []


@pytest.mark.parametrize("kind,field,value", [
    ("features", "selected", "False"), ("features", "input_availability_proven", "True"),
    ("features", "return_5d", "8.0000"), ("features", "receipt_id", "invented"),
    ("features", "history_gap_count", "1"), ("features", "tdcc_price_phase", "quiet"),
    ("signals", "stock_id", "2222"), ("coverage", "pit_supported_rows", "1"),
    ("coverage", "current_version_supported_rows", "0"), ("trades", "net_pnl", "999"),
    ("trades", "exit_date", "20250917"), ("trades", "formal_use", "True"),
    ("trades", "slippage_bps", "5"), ("summary", "win_count", "0"),
    ("trades", "strict_missing_evidence", ""),
    ("blocked", "strict_entry_established", "True"),
    ("blocked", "strict_v3_status", "open_unresolved_exit"),
])
def test_rehashed_tampering_is_not_a_validation_bypass(audit, bundle, kind, field, value):
    contract, artifacts = bundle
    replace_rows(audit, artifacts, kind, lambda rows: rows[0].update({field: value}))
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("kind", ["features", "signals", "trades", "blocked", "summary", "coverage"])
def test_rehashed_row_omission_fails(audit, bundle, kind):
    contract, artifacts = bundle
    replace_rows(audit, artifacts, kind, lambda rows: rows.pop())
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("row_index", range(9))
@pytest.mark.parametrize("mutation", ["value", "omit", "duplicate"])
def test_rehashed_report_statistics_cannot_drift(audit, bundle, row_index, mutation):
    contract, artifacts = bundle
    name = audit.artifact_name("report")
    lines = artifacts[name].decode("utf-8").splitlines()
    index = [i for i, line in enumerate(lines) if line.startswith("| D+")][row_index]
    if mutation == "omit":
        lines.pop(index)
    elif mutation == "duplicate":
        lines.insert(index, lines[index])
    else:
        cells = lines[index].split(" | ")
        cells[1] = "999999"
        lines[index] = " | ".join(cells)
    artifacts[name] = ("\n".join(lines) + "\n").encode("utf-8")
    manifest = json.loads(artifacts[audit.artifact_name("source_manifest")])
    manifest["hashes"][name] = dict(bytes=len(artifacts[name]), sha256=audit.digest(artifacts[name]))
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest)
    errors = audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)
    assert any("report primary/distribution/maturity/sensitivity" in error for error in errors)


def test_private_raw_source_omission_never_silently_downgrades(audit, bundle):
    contract, artifacts = bundle
    errors = audit.validate_artifacts(ROOT, contract, artifacts)
    assert any("requires --input-root" in e for e in errors)


def test_manifest_rebinding_retained_anomalies_fails(audit, bundle):
    contract, artifacts = bundle
    name = audit.artifact_name("source_manifest")
    manifest = json.loads(artifacts[name])
    manifest["evidence"]["retained_anomaly_candidates"] = [dict(signal_date="20250910", stock_id="1111", horizon=5)]
    artifacts[name] = audit.canonical_json(manifest)
    assert any("retained anomaly" in e for e in audit.validate_artifacts(ROOT, contract, artifacts, published_only=True))
