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


# Same-model horizon extension. The annual-v1 regression cases above are unchanged.
@pytest.fixture
def horizon_audit(monkeypatch):
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    path = ROOT / "scripts/validate_tdcc_stealth_accumulation_current_version_horizon_extension.py"
    spec = importlib.util.spec_from_file_location("horizon_independent_audit_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_horizon_extension_has_no_producer_import_or_execution(horizon_audit):
    tree = ast.parse(Path(horizon_audit.__file__).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            modules = [alias.name for alias in node.names] if isinstance(node, ast.Import) else [node.module]
            assert not any("build_" in name or name == "tdcc_stealth_accumulation_current_version_horizon_extension" for name in modules)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "compile", "__import__"}


@pytest.mark.parametrize("horizon", [5, 10, 20, 30, 40, 60])
def test_horizon_extension_entry_index_maturity_and_calendar_tail(horizon_audit, horizon):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    cutoff = calendar[calendar.index("20260909") - 1 - horizon]
    row = horizon_audit.holding_dates(calendar, cutoff, horizon, "20260909")
    assert row["entry_index"] == calendar.index(cutoff) + 1
    assert row["exit_target_index"] == row["entry_index"] + horizon
    assert row["exit_date"] == "20260909" and row["mature"] is True
    following = horizon_audit.holding_dates(calendar, calendar[calendar.index(cutoff) + 1], horizon, "20260909")
    assert following["mature"] is False
    tail = horizon_audit.holding_dates(calendar, "20260908", horizon, "20260909")
    assert tail["mature"] is False
    if tail["exit_target_index"] >= len(calendar):
        assert tail["exit_date"] == ""


def test_horizon_extension_common_cutoff_is_date_not_surviving_trade(horizon_audit):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    cutoff = horizon_audit.common_cutoff(calendar, "20260909")
    i = calendar.index(cutoff)
    signals = [horizon_audit.Signal(calendar[j], "1111", "測試", "TWSE", 0) for j in (i - 1, i, i + 1)]
    profiles, observed = horizon_audit.select_profiles(signals, calendar, "20260909")
    assert observed == cutoff
    assert profiles["full_period"] == signals
    assert profiles["common_d60"] == signals[:2]
    assert horizon_audit.PROFILES == {"full_period": (30, 40, 60), "common_d60": (5, 10, 20, 30, 40, 60)}


class HorizonSyntheticPrices:
    def __init__(self, audit, *, missing=(), as_of="20260909"):
        self.audit, self.missing, self.as_of = audit, set(missing), as_of

    def daily(self, date):
        if not date or date > self.as_of or date in self.missing:
            return {}, {}
        return {"1111": simple_price(self.audit.annual, date, closing=110)}, {}


def test_horizon_extension_rebuilds_locks_not_D20_trade_extension(horizon_audit):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    start = "20250910"
    index = calendar.index(start) + 1
    dates = [start, calendar[index + 20 + 1], calendar[index + 30], calendar[index + 30 + 1]]
    signals = [horizon_audit.Signal(date, "1111", "測試", "TWSE", 0) for date in dates]
    prices = HorizonSyntheticPrices(horizon_audit)
    thirty = list(horizon_audit.ledger_rows(prices, signals, calendar, profile="full_period", horizon=30, as_of="20260909"))
    traded = {row["signal_date"] for kind, row in thirty if kind == "trades"}
    assert traded == {start, dates[-1]}
    assert any(row.get("reasons") == "blocked_exit_day" and row["signal_date"] == dates[2] for _, row in thirty)
    assert any(row.get("reasons") == "blocked_active_position" and row["signal_date"] == dates[1] for _, row in thirty)
    forty = list(horizon_audit.ledger_rows(prices, signals, calendar, profile="full_period", horizon=40, as_of="20260909"))
    assert {row["signal_date"] for kind, row in forty if kind == "trades"} == {start}
    for _, row in thirty + forty:
        if row.get("record_type") == "strict_ledger_decision":
            assert row["strict_entry_established"] is False
            assert row["strict_prior_position_locked"] is False


def test_horizon_extension_missing_exit_and_unknown_future_never_release_lock(horizon_audit):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    start = "20250910"
    index = calendar.index(start) + 1
    exit_date = calendar[index + 30]
    signals = [horizon_audit.Signal(date, "1111", "測試", "TWSE", 0) for date in (start, calendar[index + 31])]
    rows = list(horizon_audit.ledger_rows(HorizonSyntheticPrices(horizon_audit, missing=[exit_date]), signals, calendar, profile="full_period", horizon=30, as_of="20260909"))
    assert not any(kind == "trades" for kind, _ in rows)
    assert any(row.get("reasons") == "open_unresolved_exit_price" for _, row in rows)
    assert any(row.get("reasons") == "blocked_active_position" for _, row in rows)
    late = [horizon_audit.Signal("20260908", "1111", "測試", "TWSE", 0)]
    rows = list(horizon_audit.ledger_rows(HorizonSyntheticPrices(horizon_audit), late, calendar, profile="full_period", horizon=60, as_of="20260909"))
    assert not any(kind == "trades" for kind, _ in rows)
    censored = next(row for _, row in rows if row.get("record_type") == "operation_censored")
    assert censored["reasons"] == "open_immature" and censored["exit_date"] == ""


def test_horizon_extension_paired_all_six_use_same_complete_case_events(horizon_audit):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    signals = [horizon_audit.Signal(date, "1111", "測試", "TWSE", 0) for date in ("20250910", "20250911")]
    target = horizon_audit.holding_dates(calendar, signals[0].signal_date, 60, "20260909")["exit_date"]
    rows, _ = horizon_audit.paired_summary(HorizonSyntheticPrices(horizon_audit, missing=[target]), signals, calendar, "20260909")
    assert len(rows) == 18
    assert {row["event_count"] for row in rows} == {1}
    assert len({row["eventset_sha256"] for row in rows}) == 1
    assert {row["excluded_missing_entry_or_exit_events"] for row in rows} == {1}
    assert all(row["overlapping_events_allowed"] and not row["portfolio_performance"] for row in rows)
    for row in rows:
        if row["horizon"] == 20:
            assert row["mean_paired_delta_vs_D20_pct"] == 0
            assert row["paired_delta_zero_count"] == 1
    complete, _ = horizon_audit.paired_summary(HorizonSyntheticPrices(horizon_audit), signals, calendar, "20260909")
    assert {row["event_count"] for row in complete} == {2}
    portfolio = list(horizon_audit.ledger_rows(HorizonSyntheticPrices(horizon_audit), signals, calendar, profile="common_d60", horizon=60, as_of="20260909"))
    assert len([row for kind, row in portfolio if kind == "trades" and row["slippage_bps"] == 10]) == 1


def horizon_report(audit, original, groups, cutoff, summary, paired, anomalies, blocks):
    lines = ["research_only formal_use=False promotion_evidence_allowed=False full_period_pit_complete=False 不是 strict PIT 已核實 total-return 出場日訊號仍阻擋 不是portfolio績效 不影響主帳本 全部保留primary 只作sensitivity 不是corrected/cleaned performance 不依異常幅度刪除 blocked_input_availability_unproven 沒有配對sensitivity",
        f"原始訊號區間 {original['requested_signal_start']}–{original['requested_signal_end']}；as_of={original['as_of']}；D60共同訊號截止={cutoff}。",
        f"全區間原始訊號 {len(groups['full_period'])}；共同區間原始訊號 {len(groups['common_d60'])}。", f"新anomalies共 {len(anomalies)} 列；immutable v1 baseline候選 0 列",
        f"配對common原始訊號 {paired[0]['common_signal_count']}；六horizon共同有效事件 {paired[0]['event_count']}；缺有效入場／任一出場排除 {paired[0]['excluded_missing_entry_or_exit_events']}；可能91開頭TDR事件 {paired[0]['possible_TDR_events']}。",
        "## 主要結果（10 bps，保留所有未解候選）"]
    for row in summary:
        if row["slippage_bps"] == 10 and row["population"].startswith("primary"):
            lines.append(f"| {row['profile']} | {row['horizon']} | {row['realized_raw_price_proxy_positions']} | {row['mean_net_return_pct']} | {row['median_net_return_pct']} | {row['win_rate_pct']} | {row['proxy_immature_positions']}／{row['proxy_unresolved_exit_positions']} |")
    lines.append("## 排除候選敏感性對照（10 bps，不取代primary）")
    for row in summary:
        if row["slippage_bps"] == 10 and row["population"].startswith("sensitivity"):
            lines.append(f"| {row['profile']} | {row['horizon']} | {row['realized_raw_price_proxy_positions']} | {row['mean_net_return_pct']} | {row['median_net_return_pct']} | {row['win_rate_pct']} |")
    lines.append("## 未入場／未成熟／缺出場原因分布")
    reasons = sorted((p, h, k[0], k[1], n) for (p, h), counter in blocks.items() for k, n in counter.items() if isinstance(k, tuple) and k[0] != "strict_ledger_decision")
    for profile, horizon, kind, reason, count in reasons:
        lines.append(f"| {profile} | {horizon} | {kind} | {reason} | {count} |")
    lines.append("## 新帳本數值調查候選（10 bps，每組列出最高與最低）")
    for profile, horizons in audit.PROFILES.items():
        for horizon in horizons:
            candidates = [r for r in anomalies if r["profile"] == profile and r["horizon"] == horizon]
            if candidates:
                chosen = [min(candidates, key=lambda r:float(r["net_return_pct"])), max(candidates, key=lambda r:float(r["net_return_pct"]))]
                for row in chosen[:1] if chosen[0] == chosen[1] else chosen:
                    lines.append(f"| {profile} | {horizon} | {row['signal_date']} | {row['stock_id']} | {row['net_return_pct']} | unresolved_anomaly_candidate；保留primary |")
    lines.append("## 同事件配對觀察（10 bps）")
    for row in paired:
        if row["slippage_bps"] == 10:
            lines.append(f"| {row['horizon']} | {row['event_count']} | {row['mean_net_return_pct']} | {row['mean_paired_delta_vs_D20_pct']} | {row['median_paired_delta_vs_D20_pct']} |")
    return ("\n".join(lines) + "\n").encode("utf-8")


@pytest.fixture
def horizon_bundle(horizon_audit, monkeypatch):
    audit = horizon_audit
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_text(encoding="utf-8"))
    original = json.loads((ROOT / audit.annual.CONTRACT_FILE).read_text(encoding="utf-8"))
    calendar = audit.annual.calendar_days([], original["history_start"], original["calendar_end"])
    signals = [audit.Signal(date, "1111", "測試", "TWSE", 0) for date in ("20250910", "20250911", "20250918", "20260908", "20260909")]
    groups, cutoff = audit.select_profiles(signals, calendar, original["as_of"])
    prices, trades, blocked = HorizonSyntheticPrices(audit), [], []
    from collections import Counter, defaultdict
    stats, counts = defaultdict(list), defaultdict(Counter)
    for profile, horizons in audit.PROFILES.items():
        for horizon in horizons:
            for kind, row in audit.ledger_rows(prices, groups[profile], calendar, profile=profile, horizon=horizon, as_of=original["as_of"]):
                if kind == "blocked":
                    blocked.append(row)
                    counts[profile, horizon][row["record_type"]] += 1
                    counts[profile, horizon][row["reasons"]] += 1
                    counts[profile, horizon][row["record_type"], row["reasons"]] += 1
                else:
                    trades.append(row)
                    stats[profile, horizon, row["slippage_bps"]].append(audit.StatTrade(profile, row["signal_date"], row["stock_id"], horizon, row["slippage_bps"], row["net_return_pct"], 0, row["entry_date"], row["exit_date"], None))
    anomalies, anomaly_keys = audit.anomaly_rows(stats, [])
    for row in trades:
        row["anomaly_candidate"] = (row["profile"], row["signal_date"], row["stock_id"], row["horizon"]) in anomaly_keys
    summary = audit.summaries(stats, counts, groups, cutoff, original["as_of"], anomaly_keys)
    paired, paired_anomalies = audit.paired_summary(prices, groups["common_d60"], calendar, original["as_of"])
    anomalies.extend(paired_anomalies)
    rows = dict(trades=trades, blocked=blocked, summary=summary, anomalies=anomalies, paired_summary=paired)
    artifacts = {}
    for kind, values in rows.items():
        data = encode(values, audit.SCHEMAS[kind])
        artifacts[audit.name(kind)] = gzip.compress(data, mtime=0) if kind in {"trades", "blocked"} else data
    artifacts[audit.name("report")] = horizon_report(audit, original, groups, cutoff, summary, paired, anomalies, counts)
    supplemental = dict(warmup_nonquote_rows=0, supplemental_price_rows=0)
    baseline = dict(evidence=dict(calendar_closures=[]), counts=dict(supplemental=supplemental), hashes={audit.annual.artifact_name("anomalies"):dict(sha256="a" * 64)})
    manifest = dict(model_id=audit.annual.MODEL_ID, owner_id="tdcc_stealth_accumulation_current_version_annual_replay", artifact_version=audit.PREFIX + "v1", contract_file=audit.CONTRACT_FILE, contract=contract, contract_sha256=audit.APPROVED_CONTRACT_SHA256, base_artifact_ref=audit.BASE_REF, base_contract=original, base_contract_sha256=audit.annual.APPROVED_CONTRACT_SHA256, validation_scope="immutable_v1_signals_and_independent_horizon_source_replay_not_selector_revalidation", calendar=dict(history_start=original["history_start"], calendar_end=original["calendar_end"], closures=[], sessions=calendar, target_index_basis="zero_based_from_history_start"), baseline_anomaly_audit=dict(candidate_rows=0, retained_in_immutable_base=True, sha256="a" * 64, unrepresented_candidates_not_copied_to_extension_profiles=True), common_signal_cutoff=cutoff, counts=dict(base_signals=len(signals), common_signals=len(groups["common_d60"]), trade_rows=len(trades), blocked_rows=len(blocked), anomaly_rows=len(anomalies), summary_rows=54, paired_summary_rows=18, paired_event_count=paired[0]["event_count"], supplemental=supplemental), **{field:False for field in audit.FALSE_FLAGS})
    manifest["hashes"] = {filename:dict(bytes=len(data), sha256=audit.sha(data)) for filename, data in artifacts.items()}
    artifacts[audit.name("source_manifest")] = audit.annual.canonical_json(manifest)
    monkeypatch.setattr(audit, "load_baseline", lambda root: (object(), original, baseline, signals, [], b""))
    monkeypatch.setattr(audit, "PublishedPrices", lambda *args: prices)
    monkeypatch.setattr(audit, "audit_source_bindings", lambda *args: None)
    return contract, artifacts


def horizon_replace(audit, artifacts, kind, mutate):
    filename = audit.name(kind)
    rows = list(audit.records(kind, artifacts[filename]))
    mutate(rows)
    data = encode(rows, audit.SCHEMAS[kind])
    artifacts[filename] = gzip.compress(data, mtime=0) if kind in {"trades", "blocked"} else data
    manifest = json.loads(artifacts[audit.name("source_manifest")])
    manifest["hashes"][filename] = dict(bytes=len(artifacts[filename]), sha256=audit.sha(artifacts[filename]))
    artifacts[audit.name("source_manifest")] = audit.annual.canonical_json(manifest)


def test_horizon_extension_synthetic_bundle(horizon_audit, horizon_bundle):
    contract, artifacts = horizon_bundle
    assert horizon_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True) == []


@pytest.mark.parametrize("kind,field,value", [
    ("trades", "entry_index", "999"), ("trades", "exit_target_index", "999"),
    ("trades", "horizon", "20"), ("trades", "exit_date", "20260909"),
    ("trades", "entry_open", "1"), ("trades", "net_pnl", "0"),
    ("trades", "anomaly_candidate", "True"), ("trades", "primary_row_retained", "False"),
    ("blocked", "strict_entry_established", "True"), ("blocked", "reasons", "open_immature"),
    ("summary", "signal_cutoff", "20260909"), ("summary", "total_input_signals", "0"),
    ("summary", "population", "corrected_performance"), ("summary", "mean_net_return_pct", "999"),
    ("paired_summary", "event_count", "0"), ("paired_summary", "eventset_sha256", "0" * 64),
    ("paired_summary", "mean_paired_delta_vs_D20_pct", "999"), ("paired_summary", "portfolio_performance", "True"),
    ("paired_summary", "possible_TDR_events", "1"), ("paired_summary", "anomaly_candidate_events", "99"),
])
def test_horizon_extension_rehashed_field_mutations(horizon_audit, horizon_bundle, kind, field, value):
    contract, artifacts = horizon_bundle
    def mutate(rows):
        row = next((r for r in rows if r.get("profile") == "common_d60"), rows[0])
        row[field] = value
    horizon_replace(horizon_audit, artifacts, kind, mutate)
    assert horizon_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("field", ["common_signal_cutoff", "calendar", "base_artifact_ref", "input_availability_proven"])
def test_horizon_extension_manifest_boundary_mutations(horizon_audit, horizon_bundle, field):
    contract, artifacts = horizon_bundle
    filename = horizon_audit.name("source_manifest")
    manifest = json.loads(artifacts[filename])
    if field == "calendar": manifest[field]["sessions"].pop(10)
    elif field == "input_availability_proven": manifest[field] = True
    else: manifest[field] = "20990101"
    artifacts[filename] = horizon_audit.annual.canonical_json(manifest)
    assert horizon_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("kind", ["source_manifest", "trades", "blocked", "summary", "anomalies", "paired_summary", "report"])
def test_horizon_extension_missing_any_of_seven_artifacts_fails(horizon_audit, horizon_bundle, kind):
    contract, artifacts = horizon_bundle
    artifacts.pop(horizon_audit.name(kind))
    assert horizon_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


def test_horizon_extension_full_mode_requires_private_inputs(horizon_audit, horizon_bundle):
    contract, artifacts = horizon_bundle
    assert any("requires --input-root" in error for error in horizon_audit.validate_artifacts(ROOT, contract, artifacts))


@pytest.mark.parametrize("section", ["主要結果", "排除候選敏感性對照", "未入場／未成熟／缺出場原因分布", "新帳本數值調查候選", "同事件配對觀察"])
def test_horizon_extension_rehashed_report_section_mutations(horizon_audit, horizon_bundle, section):
    contract, artifacts = horizon_bundle
    filename = horizon_audit.name("report")
    report = artifacts[filename].decode("utf-8")
    report = report.replace("## " + section, "## MUTATED " + section, 1)
    artifacts[filename] = report.encode("utf-8")
    manifest = json.loads(artifacts[horizon_audit.name("source_manifest")])
    manifest["hashes"][filename] = dict(bytes=len(artifacts[filename]), sha256=horizon_audit.sha(artifacts[filename]))
    artifacts[horizon_audit.name("source_manifest")] = horizon_audit.annual.canonical_json(manifest)
    errors = horizon_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)
    assert any("report section" in error for error in errors)


def test_horizon_extension_retains_old_candidates_without_cross_horizon_flags(horizon_audit):
    from collections import defaultdict
    stats = defaultdict(list)
    for horizon in (5, 30):
        for index, value in enumerate((0, 1, 2, 3, 100)):
            stats["common_d60", horizon, 10].append(horizon_audit.StatTrade("common_d60", f"202509{10+index}", str(1111+index), horizon, 10, str(value), 0, "20250911", "20251024", None))
    retained = [dict(signal_date="20250910", stock_id="1111", horizon="5", net_return_pct="0", entry_date="20250911", exit_date="20251024"), dict(signal_date="20260901", stock_id="9999", horizon="20", net_return_pct="999", entry_date="20260902", exit_date="20261001")]
    anomalies, keys = horizon_audit.anomaly_rows(stats, retained)
    assert ("common_d60", "20250910", "1111", 5) in keys
    assert ("common_d60", "20250910", "1111", 30) not in keys
    assert not any(row["stock_id"] == "9999" for row in anomalies)
    assert {row["stock_id"] for row in anomalies if row["reason"].startswith("outside_")} == {"1115"}
    assert all(row["primary_row_retained"] and row["represented_in_current_proxy_trade"] for row in anomalies)


def test_horizon_extension_zero_paired_events_remain_blank_not_zero_return(horizon_audit):
    calendar = horizon_audit.annual.calendar_days([], "20250401", "20261030")
    rows, anomalies = horizon_audit.paired_summary(HorizonSyntheticPrices(horizon_audit), [], calendar, "20260909")
    assert len(rows) == 18 and anomalies == []
    assert all(row["event_count"] == 0 and row["mean_net_return_pct"] == "" and row["mean_paired_delta_vs_D20_pct"] == "" for row in rows)


def test_horizon_extension_real_published_seven_preserve_v1_and_output_bytes(horizon_audit):
    """Required CI consumption test: a missing published artifact must fail, never skip."""
    output = ROOT / horizon_audit.DEFAULT_DIRECTORY
    paths = [output / horizon_audit.name(kind) for kind in horizon_audit.KINDS]
    assert all(path.is_file() and not path.is_symlink() for path in paths), "all seven published horizon artifacts are required"
    before = {path.name:horizon_audit.sha(path.read_bytes()) for path in paths}
    git = horizon_audit.annual.GitReader(ROOT)
    v1 = {}
    for kind in horizon_audit.annual.KINDS:
        filename = horizon_audit.annual.artifact_name(kind)
        relative = horizon_audit.DEFAULT_DIRECTORY + "/" + filename
        data = git.read(horizon_audit.BASE_REF, relative)
        path = ROOT / relative
        v1[relative] = (git.tree(horizon_audit.BASE_REF)[relative], horizon_audit.sha(data), horizon_audit.sha(path.read_bytes()) if path.is_file() else None)
        if path.is_file(): assert horizon_audit.sha(path.read_bytes()) == horizon_audit.sha(data)
    assert horizon_audit.validate(ROOT, published_only=True) == []
    assert {path.name:horizon_audit.sha(path.read_bytes()) for path in paths} == before
    fresh = horizon_audit.annual.GitReader(ROOT)
    for relative, (oid, digest, physical) in v1.items():
        assert fresh.tree(horizon_audit.BASE_REF)[relative] == oid
        assert horizon_audit.sha(fresh.read(horizon_audit.BASE_REF, relative)) == digest
        path = ROOT / relative
        assert (horizon_audit.sha(path.read_bytes()) if path.is_file() else None) == physical
