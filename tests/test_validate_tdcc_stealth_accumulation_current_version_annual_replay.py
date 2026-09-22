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


def test_medium_term_real_published_eleven_and_independent_validator_ci_entrypoint(tmp_path):
    """Published artifacts and the entire independent suite are mandatory in CI."""
    import subprocess
    import sys

    tests = subprocess.run(
        [sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider",
         "--basetemp", str(tmp_path / "medium-term-validator"),
         "tests/test_validate_tdcc_stealth_accumulation_medium_term_trend_research.py"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    assert tests.returncode == 0, tests.stdout + tests.stderr


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


@pytest.fixture
def stratification_audit(monkeypatch):
    import sys
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    name = "stratification_independent_audit_test"
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts/validate_tdcc_stealth_accumulation_condition_stratification.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class StratificationSyntheticPrices:
    def __init__(self, audit, stocks=("1111", "2222", "3333")):
        self.audit, self.stocks, self.missing, self.calls = audit, stocks, set(), []

    def daily(self, date):
        self.calls.append(date)
        return {stock: simple_price(self.audit.annual_io, date, stock) for stock in self.stocks if (date, stock) not in self.missing}, {}


def stratification_report(audit, rules, rows, anomalies, contrasts):
    text = ["research_only formal_use=False promotion_evidence_allowed=False 不是strict PIT total-return 不是完全盲測 D20主要、D60僅robustness 切分不重置 精確44個warmup缺口 原65份私有來源 零分母為空 不是corrected/cleaned performance 不使用月營收",
        f"訓練baseline D20/10bps：{rules['training_positions']}部位、{rules['training_stocks']}股、{rules['training_signal_dates']}訊號日期；寬度有效分母{rules['training_width_samples']}；type7 Q75={rules['training_q75']}。",
        "## 固定五個單項條件", "", "| variant | meaning |", "|---|---|"]
    text.extend("| " + variant + " | description |" for variant in audit.VARIANTS[1:])
    text.extend(["", "## 訓練高／低報酬特徵對照（D20／10 bps）", "", "| header |", "|---|"])
    lookup = {(r["population"], r["feature_name"], r["outcome_group"]):r for r in contrasts}
    for population in ("primary", "immutable_prior_candidate_exclusion_sensitivity"):
        for field in ("tdcc_both_net_positive", "tdcc_both_up_count_ge2", "no_new_low_previous20obs", "range_20obs_pct", "return_5d"):
            statistic = "median" if field in {"range_20obs_pct", "return_5d"} else "mean"
            cells = [population, field, statistic] + [lookup[population, field, group][statistic] for group in ("high", "low", "middle")]
            text.append("| " + " | ".join(cells) + " |")
    text.extend(["", "## 訓練／驗證主要與敏感性對照（10 bps）", "", "| header |", "|---|"])
    for row in rows:
        if row["slippage_bps"] == 10 and row["partition"] in {"training", "validation"}:
            cells = [row[k] for k in ("variant", "horizon", "partition", "population", "samples", "stocks", "signal_dates", "entry_dates")] + [f"{row['win_count']}/{row['neutral_count']}/{row['failure_count']}", f"{row['win_rate_pct']}/{row['neutral_rate_pct']}/{row['failure_rate_pct']}"] + [row[k] for k in ("mean_net_return_pct", "median_net_return_pct", "high_return_ge10_rate_pct", "loss_le_minus10_rate_pct")]
            text.append("| " + " | ".join(map(str, cells)) + " |")
    text.extend(["", "## 缺證、未成熟與重疊（10 bps primary）", "", "| header |", "|---|"])
    for row in rows:
        if row["slippage_bps"] == 10 and row["population"] == "primary" and row["partition"] != "all":
            cells = [row[k] for k in ("variant", "horizon", "partition", "unsupported_signals", "filter_rejected_signals", "overlap_blocked_signals", "missing_entry_signals", "immature_positions", "missing_exit_positions", "purged_positions")]
            text.append("| " + " | ".join(map(str, cells)) + " |")
    text.append(f"未解數值候選{len(anomalies)}列")
    return ("\n".join(text) + "\n").encode("utf-8")


@pytest.fixture
def stratification_bundle(stratification_audit, monkeypatch):
    from collections import Counter
    audit = stratification_audit
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_bytes())
    calendar = audit.session_calendar([])
    prices = StratificationSyntheticPrices(audit)
    signals = [base_feature(audit.annual_io, date, stock) for date, stock in (("20250910", "1111"), ("20250911", "1111"), ("20260105", "2222"), ("20260316", "2222"), ("20260402", "2222"), ("20260908", "3333"), ("20260909", "3333"))]
    signals[0]["tdcc_400_change_sum"] = "-1"
    signals = list(audit.annual_io.rows_for("signals", gzip.compress(encode(signals, audit.annual_io.FEATURE_FIELDS), mtime=0)))
    features = [audit.derive_feature(row, prices) for row in signals]
    by_id = {row["feature_id"]: row for row in features}
    original = dict(history_start="20250401", calendar_end="20261030", requested_signal_start="20250910", as_of=audit.AS_OF)
    supplemental = dict(warmup_nonquote_rows=0, supplemental_price_rows=0)
    original_manifest = dict(counts=dict(signals=len(features), supplemental=supplemental))
    context = dict(original=original, original_manifest=original_manifest, signals_payload=gzip.compress(encode(signals, audit.annual_io.FEATURE_FIELDS), mtime=0), retained=[], prices=prices, closures=[], calendar=calendar, inputs=None)
    monkeypatch.setattr(audit, "load_context", lambda *args, **kwargs: context)
    monkeypatch.setattr(audit, "projection_map", lambda *args: {})
    monkeypatch.setattr(audit, "audit_source_bindings", lambda *args: None)
    input_counts = {h: Counter(audit.partition(**{k:v for k,v in audit.holding_dates(calendar, f["signal_date"], h).items() if k in {"entry_date", "exit_date"}}) for f in features) for h in audit.HORIZONS}
    trades, blocked, summary, anomalies, threshold = [], [], [], [], None
    for variant in audit.VARIANTS:
        these, counts = [], Counter()
        for horizon in audit.HORIZONS:
            for kind, row in audit.ledger_rows(features, prices, calendar, variant, threshold, horizon):
                if kind == "trades": these.append(row)
                else:
                    blocked.append(row)
                    counts[row["partition"], horizon, row["record_type"], row["reasons"]] += 1
        compact = [audit.compact_trade(row) for row in these]
        if variant == "baseline": threshold, contrasts, rules = audit.training_material(compact, by_id, contract, [])
        new_anomalies, keys = audit.anomaly_rows(compact, [])
        for row in these: row["anomaly_candidate"] = (row["signal_date"], row["stock_id"], row["horizon"]) in keys
        trades.extend(these)
        anomalies.extend(new_anomalies)
        summary.extend(audit.summaries(compact, counts, input_counts, variant, keys))
    artifacts = {}
    for kind, rows in dict(features=features, trades=trades, blocked=blocked, summary=summary, anomalies=anomalies, training_contrasts=contrasts).items():
        data = encode([{field:row.get(field, "") for field in audit.SCHEMAS[kind]} for row in rows], audit.SCHEMAS[kind])
        artifacts[audit.artifact_name(kind)] = gzip.compress(data, mtime=0) if kind in {"features", "trades", "blocked"} else data
    artifacts[audit.artifact_name("candidate_rules")] = audit.canonical_json(rules)
    artifacts[audit.artifact_name("report")] = stratification_report(audit, rules, summary, anomalies, contrasts)
    manifest = dict(model_id="tdcc_stealth_accumulation", owner_id="tdcc_stealth_accumulation_current_version_annual_replay", artifact_version=audit.PREFIX + "v1", contract_file=audit.CONTRACT_FILE, contract=contract, contract_sha256=audit.APPROVED_CONTRACT_SHA256, base_contract=original,
        calendar=dict(sessions=calendar, closures=[], history_start="20250401", calendar_end="20261030"), candidate_rules=rules,
        warmup_projection_audit=dict(raw_verified_rows=44, raw_verified_missing_pairs=65, projection_used_as_price_fallback=False),
        counts=dict(signals=len(features), trades=len(trades), blocked=len(blocked), summary=len(summary), anomalies=len(anomalies), training_contrasts=len(contrasts), baseline_candidate_source_rows=0, supplemental=supplemental),
        hashes={name:dict(bytes=len(data), sha256=audit.digest(data)) for name,data in artifacts.items()}, **{field:False for field in audit.FALSE_FLAGS})
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest)
    return contract, artifacts


def stratification_rehash(audit, artifacts, kind, payload):
    name = audit.artifact_name(kind)
    artifacts[name] = payload
    manifest = json.loads(artifacts[audit.artifact_name("source_manifest")])
    manifest["hashes"][name] = dict(bytes=len(payload), sha256=audit.digest(payload))
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest)


def test_stratification_synthetic_bundle(stratification_audit, stratification_bundle):
    assert stratification_audit.validate_artifacts(ROOT, *stratification_bundle, published_only=True) == []


@pytest.mark.parametrize("values,p,expected", [([1,2,3,4], ".75", "3.25"), ([9], ".75", "9"), ([1,3], ".5", "2"), (["0.1","0.2"], ".75", "0.175")])
def test_stratification_decimal_type7(stratification_audit, values, p, expected):
    assert stratification_audit.quantile_type7(values, p) == Decimal(expected)


@pytest.mark.parametrize("values", [[], ["NaN"], [1, ""], ["Infinity"]])
def test_stratification_quantile_missing_not_zero(stratification_audit, values):
    with pytest.raises(ValueError): stratification_audit.quantile_type7(values, ".75")


def test_stratification_conditions_are_independent_and_missing_not_false(stratification_audit):
    audit = stratification_audit
    row = dict(tdcc_400_change_sum="-1", tdcc_1000_change_sum="-1", tdcc_400_up_weeks="2", tdcc_1000_up_weeks="2", return_5d="-0.0000", range_20obs_pct="1", current_low="", previous_20obs_low_ex_today="", stratification_feature_supported=False)
    assert audit.condition(row, "tdcc_both_net_positive", None) == (False, True)
    assert audit.condition(row, "tdcc_both_up_count_ge2", None) == (True, True)
    assert audit.condition(row, "price_5obs_nonnegative", None) == (True, True)
    assert audit.condition(row, "range_20obs_le_training_q75", Decimal(1)) == (True, True)
    assert audit.condition(row, "no_new_low_previous20obs", None) == (False, False)
    assert audit.condition(row, "baseline", None) == (True, True)


def test_stratification_observation_window_excludes_today_and_preserves_gap(stratification_audit):
    audit = stratification_audit
    signal = base_feature(audit.annual_io)
    signal["history_gap_count"] = "3"
    prices = StratificationSyntheticPrices(audit)
    row = audit.derive_feature(signal, prices)
    assert row["previous_20obs_low_ex_today"] == "99.0" and row["no_new_low_previous20obs"] is True
    with localcontext() as context:
        context.prec = 50
        assert row["range_20obs_pct"] == str((Decimal("101")/Decimal("99")-1)*100)
    assert row["history_gap_count"] == "3" and row["stratification_feature_supported"] is True
    prices.missing.add((signal["observed_history_dates"].split(";")[0], "1111"))
    missing = audit.derive_feature(signal, prices)
    assert missing["previous_20obs_low_ex_today"] == "" and missing["stratification_feature_supported"] is False
    assert audit.condition(missing, "tdcc_both_net_positive", None) == (True, True)


def test_stratification_chronology_retains_cross_split_lock_and_rebuilds_filtered_entries(stratification_audit, stratification_bundle):
    audit = stratification_audit
    _, artifacts = stratification_bundle
    trades = list(audit.records("trades", artifacts[audit.artifact_name("trades")]))
    baseline = {row["signal_date"] for row in trades if row["variant"] == "baseline" and row["stock_id"] == "1111"}
    filtered = {row["signal_date"] for row in trades if row["variant"] == "tdcc_both_net_positive" and row["stock_id"] == "1111"}
    assert baseline == {"20250910"} and filtered == {"20250911"}
    blocked = list(audit.records("blocked", artifacts[audit.artifact_name("blocked")]))
    cross = [row for row in blocked if row["signal_date"] == "20260402" and row["variant"] == "baseline" and row["horizon"] == "20" and row["record_type"] == "operation_no_entry"]
    assert len(cross) == 1 and cross[0]["partition"] == "validation" and cross[0]["reasons"] == "blocked_active_position"
    rules = json.loads(artifacts[audit.artifact_name("candidate_rules")])
    assert rules["training_positions"] == 2
    assert rules["selection_uses_validation"] is False and rules["selection_uses_anomaly_exclusion"] is False


@pytest.mark.parametrize("kind,field,value", [
    ("features", "observed_history_dates", "20250910"), ("features", "range_20obs_pct", "0"), ("features", "previous_20obs_low_ex_today", "0"),
    ("features", "input_ref", "HEAD"), ("features", "formal_use", "True"), ("features", "price_state", "bottom_confirmed"),
    ("trades", "entry_index", "999"), ("trades", "exit_target_index", "999"), ("trades", "partition", "validation"),
    ("trades", "net_pnl", "999"), ("trades", "strict_missing_evidence", ""), ("trades", "anomaly_candidate", "True"),
    ("blocked", "reasons", "open_immature"), ("blocked", "strict_entry_established", "True"),
    ("summary", "total_input_signals", "0"), ("summary", "samples", "0"), ("summary", "mean_net_return_pct", "999"),
    ("training_contrasts", "samples", "0"), ("training_contrasts", "population", "validation"), ("training_contrasts", "q75", "0"),
])
def test_stratification_rehashed_field_mutations(stratification_audit, stratification_bundle, kind, field, value):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    rows = list(audit.records(kind, artifacts[audit.artifact_name(kind)]))
    rows[0][field] = value
    data = encode(rows, audit.SCHEMAS[kind])
    if kind in {"features", "trades", "blocked"}: data = gzip.compress(data, mtime=0)
    stratification_rehash(audit, artifacts, kind, data)
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("kind", ["source_manifest", "features", "training_contrasts", "candidate_rules", "trades", "blocked", "summary", "anomalies", "report"])
def test_stratification_any_missing_artifact_fails(stratification_audit, stratification_bundle, kind):
    contract, artifacts = stratification_bundle
    artifacts.pop(stratification_audit.artifact_name(kind))
    assert stratification_audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("field", ["training_q75", "training_width_samples", "training_trade_keys_sha256", "selection_uses_validation", "selection_uses_anomaly_exclusion"])
def test_stratification_rehashed_rules_mutations(stratification_audit, stratification_bundle, field):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    rules = json.loads(artifacts[audit.artifact_name("candidate_rules")])
    rules[field] = True if field.startswith("selection") else "999"
    stratification_rehash(audit, artifacts, "candidate_rules", audit.canonical_json(rules))
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("field", ["calendar", "contract_sha256", "formal_use", "counts"])
def test_stratification_manifest_boundary_mutations(stratification_audit, stratification_bundle, field):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    name = audit.artifact_name("source_manifest")
    manifest = json.loads(artifacts[name])
    if field == "calendar": manifest[field]["sessions"].pop(20)
    elif field == "counts": manifest[field]["signals"] = 0
    elif field == "formal_use": manifest[field] = True
    else: manifest[field] = "0" * 64
    artifacts[name] = audit.canonical_json(manifest)
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


def test_stratification_late_h60_is_immature_without_future_lookup(stratification_audit):
    audit = stratification_audit
    calendar = audit.session_calendar([], end="20260915")
    prices = StratificationSyntheticPrices(audit)
    row = base_feature(audit.annual_io, "20260908")
    records = list(audit.ledger_rows([row], prices, calendar, "baseline", None, 60))
    assert records[-1][1]["reasons"] == "open_immature" and records[-1][1]["exit_date"] == ""
    assert all(date <= audit.AS_OF for date in prices.calls)


def test_stratification_missing_private_mode_rejected(stratification_audit, stratification_bundle):
    assert any("requires --input-root" in error for error in stratification_audit.validate_artifacts(ROOT, *stratification_bundle))


def test_stratification_no_new_producer_import_or_eval(stratification_audit):
    tree = ast.parse(Path(stratification_audit.__file__).read_text(encoding="utf-8"))
    imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    imports += [alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names]
    assert not any(name and (name.startswith("build_tdcc") or name == "tdcc_stealth_accumulation_condition_stratification") for name in imports)
    assert not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"exec", "eval", "compile"} for node in ast.walk(tree))


@pytest.mark.parametrize("field", ["base_artifact_ref", "price_source_ref", "protected_artifact_ref", "validation_entry_start", "as_of", "horizons"])
def test_stratification_fixed_contract_pins_cannot_drift(stratification_audit, field):
    audit = stratification_audit
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_bytes())
    contract[field] = "MUTATED"
    with pytest.raises(ValueError, match="contract SHA256"):
        audit.contract_audit(contract)


@pytest.mark.parametrize("mutation", ["missing", "extra", "duplicate", "source_hash", "source_path", "observed_hash", "observed_date", "missing_dates"])
def test_stratification_projection_exact_44_source_scope(stratification_audit, mutation):
    audit = stratification_audit
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_bytes())
    original = json.loads((ROOT / audit.annual_io.CONTRACT_FILE).read_bytes())
    assert len(audit.projection_map(contract, original)) == 44
    rows = contract["published_warmup_low_projection"]["rows"]
    if mutation == "missing": rows.pop()
    elif mutation in {"extra", "duplicate"}: rows.append(copy.deepcopy(rows[0]))
    elif mutation == "source_hash": rows[0]["warmup_sources"][0]["sha256"] = "0"*64
    elif mutation == "source_path": rows[0]["warmup_sources"][0]["path"] = "other.json"
    elif mutation == "observed_hash": rows[0]["observed_dates_sha256"] = "0"*64
    elif mutation == "observed_date": rows[0]["observed_dates"][0] = "20250101"
    else: rows[0]["missing_observation_dates"] = []
    with pytest.raises(ValueError): audit.projection_map(contract, original)


def test_stratification_projection_checks_raw_minimum_and_not_general_fallback(stratification_audit):
    audit = stratification_audit
    signal = base_feature(audit.annual_io)
    dates = signal["observed_history_dates"].split(";")
    projection = dict(feature_id=signal["feature_id"], signal_date=signal["signal_date"], stock_id=signal["stock_id"], observed_dates=dates, observed_dates_sha256=audit.digest(audit.canonical_json(dates)), previous_20obs_low_ex_today="99.0", missing_observation_dates=[dates[0]])
    prices = StratificationSyntheticPrices(audit)
    assert audit.derive_feature(signal, prices, projection)["previous_20obs_low_ex_today"] == "99.0"
    wrong = dict(projection, previous_20obs_low_ex_today="98")
    with pytest.raises(ValueError, match="raw independent minimum"):
        audit.derive_feature(signal, prices, wrong)
    prices.missing.add((dates[0], "1111"))
    assert audit.derive_feature(signal, prices, projection)["previous_20obs_low_ex_today"] == "99.0"
    prices.missing.add((dates[1], "1111"))
    with pytest.raises(ValueError, match="missing-date scope"):
        audit.derive_feature(signal, prices, projection)


def test_stratification_training_q75_includes_candidate_and_excludes_later_labels(stratification_audit):
    audit = stratification_audit
    contract = json.loads((ROOT / audit.CONTRACT_FILE).read_bytes())
    features, trades = {}, []
    for index, (part, width, value) in enumerate((("training", "1", "0"), ("training", "2", "10"), ("training", "3", "-10"), ("training", "100", "100"), ("validation", "100000", "9999"), ("purged_cross_split", "999999", "9999"))):
        feature = base_feature(audit.annual_io, "20250910", str(1111+index))
        feature.update(range_20obs_pct=width, current_low="99", previous_20obs_low_ex_today="99", price_state="nonnegative_short_and_medium")
        features[feature["feature_id"]] = feature
        trades.append(audit.StatTrade("baseline", part, feature["feature_id"], "20250910", feature["stock_id"], 20, 10, "20250911", "20251010", value, f"trade-{index}", None))
    retained = [dict(signal_date="20250910", stock_id="1114", horizon="20")]
    threshold, contrasts, rules = audit.training_material(trades, features, contract, retained)
    assert threshold == Decimal("27.25") and rules["training_width_samples"] == 4
    assert rules["training_outcome_group_counts"] == {"middle":1, "high":2, "low":1}
    assert rules["immutable_training_candidate_group_counts"] == {"high":1}
    sensitivity = next(row for row in contrasts if row["population"] != "primary" and row["feature_name"] == "range_20obs_pct" and row["outcome_group"] == "all_training")
    assert sensitivity["valid_samples"] == 3 and Decimal(sensitivity["q75"]) == Decimal("2.5")
    assert len(contrasts) == 120


def test_stratification_anomaly_iqr_full_ledger_and_cost_flags(stratification_audit):
    audit = stratification_audit
    trades = []
    for horizon in audit.HORIZONS:
        for index, value in enumerate((0,1,2,3,100)):
            for slip in audit.SLIPPAGES:
                trades.append(audit.StatTrade("baseline", "validation" if index == 4 else "training", f"id{index}", "20250910", str(1111+index), horizon, slip, "20250911", "20251212", str(value), f"{index}:{slip}", None))
    retained = [dict(signal_date="20250910", stock_id="1111", horizon="20")]
    rows, keys = audit.anomaly_rows(trades, retained)
    assert ("20250910", "1111", 20) in keys and ("20250910", "1111", 60) not in keys
    assert ("20250910", "1115", 20) in keys and ("20250910", "1115", 60) in keys
    assert len(rows) == 3 and all(row["disposition"] == "unresolved_anomaly_candidate" and row["primary_row_retained"] for row in rows)
    wrong = trades[0]._replace(published_anomaly=False)
    with pytest.raises(ValueError, match="candidate flag"):
        audit.anomaly_rows([wrong, *trades[1:]], retained)


def test_stratification_missing_exit_keeps_unresolved_lock(stratification_audit):
    audit = stratification_audit
    calendar = audit.session_calendar([])
    prices = StratificationSyntheticPrices(audit)
    first = base_feature(audit.annual_io, "20250910")
    target = audit.holding_dates(calendar, first["signal_date"], 20)
    prices.missing.add((target["exit_date"], "1111"))
    later = base_feature(audit.annual_io, "20260105")
    rows = list(audit.ledger_rows([first, later], prices, calendar, "baseline", None, 20))
    assert not any(kind == "trades" for kind, _ in rows)
    assert [row["reasons"] for kind,row in rows if row["record_type"] != "strict_ledger_decision"] == ["open_unresolved_exit_price", "blocked_active_position"]


def test_stratification_costs_minimum_fee_tax_and_empty_denominators(stratification_audit):
    audit = stratification_audit
    trade = audit.cashflows("1", "1", 0)
    assert Decimal(trade["buy_fee"]) == 20 and Decimal(trade["sell_fee"]) == 20
    assert Decimal(trade["sell_tax"]) == 3 and Decimal(trade["net_pnl"]) == -43
    assert Decimal(audit.cashflows("1", "1", 20)["net_return_pct"]) < Decimal(trade["net_return_pct"])
    assert audit.return_statistics([])["mean_net_return_pct"] == ""
    stats = audit.return_statistics([-10,0,10])
    assert stats["win_count"] == stats["neutral_count"] == stats["failure_count"] == 1
    assert stats["high_return_ge10_rate_pct"] == stats["loss_le_minus10_rate_pct"]


@pytest.mark.parametrize("section", ["固定五個單項條件", "訓練高／低報酬特徵對照（D20／10 bps）", "訓練／驗證主要與敏感性對照（10 bps）", "缺證、未成熟與重疊（10 bps primary）"])
def test_stratification_rehashed_report_missing_section(stratification_audit, stratification_bundle, section):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    report = artifacts[audit.artifact_name("report")].decode("utf-8").replace("## " + section, "## MUTATED", 1)
    stratification_rehash(audit, artifacts, "report", report.encode("utf-8"))
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("section,cell", [("訓練高／低報酬特徵對照（D20／10 bps）",3), ("訓練／驗證主要與敏感性對照（10 bps）",9), ("缺證、未成熟與重疊（10 bps primary）",3)])
def test_stratification_rehashed_report_numeric_mutation(stratification_audit, stratification_bundle, section, cell):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    report = artifacts[audit.artifact_name("report")].decode("utf-8")
    start = report.index("## " + section)
    prefix, body = report[:start], report[start:]
    lines = body.splitlines()
    table = [i for i,line in enumerate(lines) if line.startswith("| ")]
    index = table[1]
    fields = lines[index].split("|")
    fields[cell+1] = " 999 "
    lines[index] = "|".join(fields)
    stratification_rehash(audit, artifacts, "report", (prefix + "\n".join(lines) + "\n").encode("utf-8"))
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("mutation", ["bad_hash", "BOM", "CRLF", "truncated_gzip", "duplicate_feature", "extra_trade", "removed_trade"])
def test_stratification_serialization_and_row_cardinality(stratification_audit, stratification_bundle, mutation):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    kind = "features"
    if mutation in {"extra_trade", "removed_trade"}: kind = "trades"
    payload = artifacts[audit.artifact_name(kind)]
    if mutation == "bad_hash":
        artifacts[audit.artifact_name(kind)] = payload + b"x"
    elif mutation == "truncated_gzip":
        stratification_rehash(audit, artifacts, kind, payload[:20])
    elif mutation in {"BOM", "CRLF"}:
        raw = gzip.decompress(payload)
        raw = b"\xef\xbb\xbf" + raw if mutation == "BOM" else raw.replace(b"\n", b"\r\n")
        stratification_rehash(audit, artifacts, kind, gzip.compress(raw, mtime=0))
    else:
        rows = list(audit.records(kind, payload))
        if mutation == "removed_trade": rows.pop()
        else: rows.append(rows[0])
        stratification_rehash(audit, artifacts, kind, gzip.compress(encode(rows, audit.SCHEMAS[kind]), mtime=0))
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("field,value", [("raw_verified_rows",0), ("raw_verified_missing_pairs",0), ("projection_used_as_price_fallback",True)])
def test_stratification_manifest_projection_audit_mutations(stratification_audit, stratification_bundle, field, value):
    audit = stratification_audit
    contract, artifacts = stratification_bundle
    name = audit.artifact_name("source_manifest")
    manifest = json.loads(artifacts[name])
    manifest["warmup_projection_audit"][field] = value
    artifacts[name] = audit.canonical_json(manifest)
    assert audit.validate_artifacts(ROOT, contract, artifacts, published_only=True)


@pytest.mark.parametrize("mutation", ["sha256", "git_blob_oid", "bytes", "ref", "extra_source", "external_sha256", "external_bytes"])
def test_stratification_immutable_and_external_source_bindings(stratification_audit, mutation):
    from types import SimpleNamespace
    audit = stratification_audit
    pairs = [(audit.BASE_REF, audit.annual_io.CONTRACT_FILE)]
    pairs += [(audit.BASE_REF, audit.DIRECTORY + "/" + audit.annual_io.artifact_name(kind)) for kind in ("source_manifest", "signals", "features", "anomalies")]
    pairs += [(audit.PROTECTED_REF, audit.horizon_io.CONTRACT_FILE)]
    pairs += [(audit.PROTECTED_REF, audit.DIRECTORY + "/" + audit.horizon_io.name(kind)) for kind in ("source_manifest", "anomalies")]
    pairs += [(audit.PRICE_REF, path) for path in ("data/daily_price/20250401.csv", "config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv")]
    used = {(ref,path):dict(ref=ref, path=path, git_blob_oid="1"*40, sha256="2"*64, bytes=123) for ref,path in pairs}
    external = [dict(path="private.csv", sha256="3"*64, bytes=456)]
    git = SimpleNamespace(used=used, tree=lambda ref: {"data/daily_price/20250401.csv":"1"*40})
    context = dict(git=git, original=dict(history_start="20250401", as_of="20260909"), original_manifest=dict(external_sources=external), inputs=None)
    manifest = dict(sources=copy.deepcopy(list(used.values())), external_sources=copy.deepcopy(external))
    audit.audit_source_bindings(context, {}, manifest)
    if mutation == "extra_source": manifest["sources"].append(copy.deepcopy(manifest["sources"][0]))
    elif mutation.startswith("external_"): manifest["external_sources"][0][mutation.removeprefix("external_")] = "MUTATED"
    else: manifest["sources"][0][mutation] = "MUTATED"
    with pytest.raises(ValueError): audit.audit_source_bindings(context, {}, manifest)


def test_stratification_missing_entry_never_establishes_proxy_or_strict_lock(stratification_audit):
    audit = stratification_audit
    prices = StratificationSyntheticPrices(audit)
    prices.missing.add(("20250911", "1111"))
    signals = [base_feature(audit.annual_io, date) for date in ("20250910", "20250911")]
    rows = list(audit.ledger_rows(signals, prices, audit.session_calendar([]), "baseline", None, 20))
    assert any(row.get("reasons") == "entry_price_missing_or_invalid" for _,row in rows)
    assert {row["signal_date"] for kind,row in rows if kind == "trades"} == {"20250911"}
    assert all(row["strict_entry_established"] is False for _,row in rows if row.get("record_type") == "strict_ledger_decision")


def test_stratification_real_published_nine_preserve_old_sixteen(stratification_audit):
    """Mandatory published evidence: missing new9 fails; no private-input or skip fallback."""
    audit = stratification_audit
    output = ROOT / audit.DIRECTORY
    paths = [output / audit.artifact_name(kind) for kind in audit.KINDS]
    assert all(path.is_file() and not path.is_symlink() for path in paths), "all nine stratification artifacts required"
    before = {path.name:audit.digest(path.read_bytes()) for path in paths}
    git = audit.annual_io.GitReader(ROOT)
    previous = [audit.annual_io.artifact_name(kind) for kind in audit.annual_io.KINDS] + [audit.horizon_io.name(kind) for kind in audit.horizon_io.KINDS]
    snapshots = {}
    for name in previous:
        relative = audit.DIRECTORY + "/" + name
        data = git.read(audit.PROTECTED_REF, relative)
        path = ROOT / relative
        physical = audit.digest(path.read_bytes()) if path.is_file() else None
        assert not path.is_symlink()
        if physical is not None: assert physical == audit.digest(data)
        snapshots[relative] = git.tree(audit.PROTECTED_REF)[relative], audit.digest(data), physical
    assert audit.validate(ROOT, published_only=True) == []
    assert {path.name:audit.digest(path.read_bytes()) for path in paths} == before
    fresh = audit.annual_io.GitReader(ROOT)
    for relative, (oid, digest_, physical) in snapshots.items():
        path = ROOT / relative
        assert fresh.tree(audit.PROTECTED_REF)[relative] == oid and audit.digest(fresh.read(audit.PROTECTED_REF, relative)) == digest_
        assert (audit.digest(path.read_bytes()) if path.is_file() else None) == physical


@pytest.mark.parametrize("actual,expected", [("",None), (None,""), (None,None), ("","")])
def test_stratification_csv_wire_none_equals_empty_only(stratification_audit, actual, expected):
    stratification_audit.compare_row("blocked", dict(entry_open=actual), dict(entry_open=expected))


@pytest.mark.parametrize("value", [0, False, "0", "False"])
def test_stratification_csv_wire_zero_and_false_are_not_missing(stratification_audit, value):
    with pytest.raises(ValueError, match="entry_open"):
        stratification_audit.compare_row("blocked", dict(entry_open=""), dict(entry_open=value))
    with pytest.raises(ValueError, match="entry_open"):
        stratification_audit.compare_row("blocked", dict(entry_open=value), dict(entry_open=None))


def test_stratification_existing_entry_price_row_with_missing_open_serializes_blocked_empty(stratification_audit):
    audit = stratification_audit
    calendar = audit.session_calendar([])
    signal = base_feature(audit.annual_io, "20250912", "2073")
    entry = audit.holding_dates(calendar, signal["signal_date"], 20)["entry_date"]

    class MissingOpenPrices:
        def daily(self, date):
            row = simple_price(audit.annual_io, date, "2073")
            if date == entry:
                row["open"] = None
            return {"2073":row}, {}

    prices = MissingOpenPrices()
    assert not audit.valid_price(prices.daily(entry)[0]["2073"])
    rows = list(audit.ledger_rows([signal], prices, calendar, "baseline", None, 20))
    assert all(kind == "blocked" for kind, _ in rows)
    expected = [row for _,row in rows]
    strict = next(row for row in expected if row["record_type"] == "strict_ledger_decision")
    assert strict["entry_open"] is None and strict["strict_entry_established"] is False
    assert strict["strict_v3_status"] == "blocked_entry_price"
    assert expected[-1]["reasons"] == "entry_price_missing_or_invalid"
    payload = gzip.compress(encode([{field:row.get(field, "") for field in audit.SCHEMAS["blocked"]} for row in expected], audit.SCHEMAS["blocked"]), mtime=0)
    actual = list(audit.records("blocked", payload))
    assert actual[0]["entry_open"] == ""
    audit.compare_sequence("blocked", actual, expected)
