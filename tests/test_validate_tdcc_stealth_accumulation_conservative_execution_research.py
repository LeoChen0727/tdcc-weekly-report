"""直接契約回歸與必要的實際產物核對；不匯入 producer。"""
from __future__ import annotations

import ast
from collections import Counter
import copy
from decimal import Decimal, localcontext
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_tdcc_stealth_accumulation_conservative_execution_research.py"


@pytest.fixture(scope="module")
def audit():
    spec = importlib.util.spec_from_file_location("conservative_execution_independent_audit", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def policy(audit):
    return json.loads((ROOT / audit.CONTRACT).read_bytes())


def trade(trade_id, stock="1111", strategy="baseline_4", entry="20260402", exit_="20260430", candidate="False"):
    with localcontext() as context:
        context.prec = 50
        buy, sell = Decimal("100100"), Decimal("109890")
        invested = buy + buy * Decimal("0.001425")
        pnl = sell - sell * Decimal("0.001425") - sell * Decimal("0.003") - invested
        value = str(pnl / invested * 100)
    return dict(trade_id=trade_id, stock_id=stock, strategy=strategy, signal_date="20260401", entry_date=entry, exit_date=exit_, entry_open="100", exit_close="110", net_return_pct=value, anomaly_candidate=candidate, primary_row_retained="True", formal_use="False", promotion_evidence_allowed="False")


def materialized(audit, source, policy):
    projected = audit.expected_execution(source, policy)
    return [dict(original, **projected[original["trade_id"]]) for original in source]


def event(state="unknown", quantity=None, covered=False, start="20260402", end="20260430", stock="1111"):
    return dict(event_id="test_event", stock_id=stock, start_date=start, end_date=end, state=state, supported_quantity=quantity, full_validity_covered=covered, reason="test_evidence")


def test_validator_has_no_producer_business_imports():
    tree = ast.parse(VALIDATOR.read_text(encoding="utf-8"))
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name.split(".")[0] for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            modules.add((node.module or "").split(".")[0])
    assert modules <= {"__future__", "argparse", "collections", "csv", "datetime", "decimal", "gzip", "hashlib", "io", "json", "pathlib", "subprocess"}


def test_policy_frozen_canonical_not_raw_format(audit, policy):
    audit.audit_policy(policy)
    assert audit.digest(audit.canonical(policy)) == audit.CONTRACT_SHA256
    policy["cohort_id"] = "changing-signal-date-cohort"
    with pytest.raises(ValueError, match="frozen policy"):
        audit.audit_policy(policy)


def test_fee_tax_slippage_independently_recomputed(audit, policy):
    row = trade("normal")
    assert audit.return_from_prices(row, policy) == Decimal(row["net_return_pct"])
    row.update(entry_open="1", exit_close="1")
    with localcontext() as context:
        context.prec = 50
        expected = (Decimal("999") - 20 - Decimal("2.997") - Decimal("1021")) / Decimal("1021") * 100
    assert audit.return_from_prices(row, policy) == expected


def test_real_dated_exception_not_trade_id_or_return(audit, policy):
    source = [trade("renamed-unseen-id", stock="2492", entry="20260504", exit_="20260601"), trade("another-unseen-id", stock="6806", strategy="trend_8", entry="20260518", exit_="20260615")]
    result = audit.expected_execution(source, policy)
    assert result["renamed-unseen-id"]["execution_entry_state"] == "assumed_regular_price_proxy"
    assert result["renamed-unseen-id"]["execution_position_state"] == "exit_unknown"
    assert result["another-unseen-id"]["execution_position_state"] == "entry_unknown"
    assert result["another-unseen-id"]["execution_entry_quantity"] == ""
    assert all(r["execution_proxy_return_pct"] == "" and r["execution_lock_retained"] == "True" for r in result.values())


def test_fixed_cohort_unknown_retains_lock_strategies_independent(audit, policy):
    policy["exceptions"] = [event(end="20260402")]
    source = [trade("old"), trade("later", entry="20260601", exit_="20260630"), trade("other-strategy", strategy="trend_8", entry="20260601", exit_="20260630")]
    source[1]["signal_date"] = source[2]["signal_date"] = "20260531"
    result = audit.expected_execution(list(reversed(source)), policy)
    assert result["old"]["execution_position_state"] == "entry_unknown"
    assert result["later"]["execution_position_state"] == "lock_blocked"
    assert result["later"]["execution_blocking_trade_id"] == "old"
    assert result["other-strategy"]["execution_position_state"] == "assumed_closed"
    assert {r["execution_cohort_id"] for r in result.values()} == {"common12-validation"}


def test_entry_open_precedes_same_day_exit_close(audit, policy):
    policy["exceptions"] = []
    source = [trade("first"), trade("same-day", entry="20260430", exit_="20260520"), trade("next-day", entry="20260501", exit_="20260521")]
    result = audit.expected_execution(source, policy)
    assert result["same-day"]["execution_position_state"] == "lock_blocked"
    assert result["next-day"]["execution_position_state"] == "assumed_closed"


def test_only_full_validity_no_fill_allows_no_entry_and_no_lock(audit, policy):
    source = [trade("first"), trade("later", entry="20260403", exit_="20260430")]
    policy["exceptions"] = [event("evidenced_no_fill", end="20260402")]
    assert audit.expected_execution(source, policy)["first"]["execution_position_state"] == "entry_unknown"
    policy["exceptions"][0]["full_validity_covered"] = True
    result = audit.expected_execution(source, policy)
    assert result["first"]["execution_position_state"] == "no_entry"
    assert result["first"]["execution_proxy_return_pct"] == ""
    assert result["later"]["execution_position_state"] == "assumed_closed"


def test_partial_entry_and_exit_keep_blank_return_and_lock(audit, policy):
    source = [trade("first"), trade("later", entry="20260501", exit_="20260531")]
    for when, state in (("20260402", "entry_partial"), ("20260430", "exit_partial")):
        policy["exceptions"] = [event("partial_fill_out_of_scope", 300, start=when, end=when)]
        result = audit.expected_execution(source, policy)
        assert result["first"]["execution_position_state"] == state
        assert result["first"]["execution_proxy_return_pct"] == ""
        assert result["later"]["execution_position_state"] == "lock_blocked"
    for quantity in (0, 1000, 300.5, True, "300"):
        policy["exceptions"][0]["supported_quantity"] = quantity
        with pytest.raises(ValueError, match="partial quantity"):
            audit.expected_execution(source, policy)


def test_original_primary_and_unknown_zero_tampering_rejected(audit, policy):
    policy["exceptions"] = [event()]
    source = [trade("first", candidate="True")]
    fields = list(source[0])
    rows = materialized(audit, source, policy)
    audit.audit_positions(fields + audit.EXTRA, rows, fields, source, policy)
    mutations = (("net_return_pct", "0"), ("anomaly_candidate", "False"), ("execution_proxy_return_pct", "0"), ("source_trade_row_sha256", "0" * 64), ("actual_fill_verified", "True"), ("execution_cohort_id", "20260401"))
    for field, value in mutations:
        changed = copy.deepcopy(rows)
        changed[0][field] = value
        with pytest.raises(ValueError):
            audit.audit_positions(fields + audit.EXTRA, changed, fields, source, policy)
    with pytest.raises(ValueError, match="retain every original"):
        audit.audit_positions(fields + audit.EXTRA, [], fields, source, policy)


def summary_fixture(audit, source, projected):
    rows = []
    for population in audit.POPULATIONS:
        selected = source[:1] if population != "original_primary_proxy" else source
        with localcontext() as context:
            context.prec = 50
            values = [Decimal(r["net_return_pct"]) for r in selected]
            count = len(values)
            one = dict(strategy="baseline_4", population=population, primary_samples="2", assumed_completed_samples="1", execution_not_computable_samples="1", execution_not_computable_pct="50", execution_evidence_unknown_samples="2", original_candidate_samples="1", population_candidate_samples=str(sum(r["anomaly_candidate"] == "True" for r in selected)), stocks=str(len({r["stock_id"] for r in selected})), signal_dates="1", samples=str(count), win_count=str(count), neutral_count="0", failure_count="0", win_rate_pct="100", neutral_rate_pct="0", failure_rate_pct="0", mean_net_return_pct=str(sum(values) / count), median_net_return_pct=str(sum(values) / count), high_return_ge10_rate_pct="0", loss_le_minus10_rate_pct="0", min_net_return_pct=str(min(values)), max_net_return_pct=str(max(values)), actual_fill_verified="False", execution_evidence_state="unknown", formal_use="False", promotion_evidence_allowed="False")
        rows.append(one)
    return rows


def test_summary_subset_denominator_and_all_evidence_unknown(audit, policy):
    policy["strategies"] = {"baseline_4": 2}
    policy["exceptions"] = [event(stock="2222")]
    source = [trade("assumed"), trade("unknown", stock="2222", candidate="True")]
    expected = audit.expected_execution(source, policy)
    summaries = summary_fixture(audit, source, expected)
    audit.audit_summary(summaries, source, expected, policy)
    for field, value in (("primary_samples", "1"), ("execution_evidence_unknown_samples", "1"), ("samples", "2"), ("execution_not_computable_pct", "0"), ("mean_net_return_pct", "0")):
        changed = copy.deepcopy(summaries)
        changed[1][field] = value
        with pytest.raises(ValueError, match="summary arithmetic/denominator"):
            audit.audit_summary(changed, source, expected, policy)


def test_manifest_time_and_content_hashes(audit, policy):
    policy["exceptions"] = []
    source = [trade("assumed")]
    expected = audit.expected_execution(source, policy)
    payloads = {kind: kind.encode() for kind in audit.KINDS[:-1]}
    manifest = dict(artifact_version=policy["artifact_version"], owner_id=audit.OWNER, model_id=policy["model_id"], replay_kind="frozen-ledger replay", policy_fixed_at=policy["policy_fixed_at"], replay_started_at="2026-09-30T16:00:00+00:00", policy_canonical_sha256=audit.CONTRACT_SHA256, source_ref=policy["source_ref"], source_ledger=policy["source_ledger"], source_ledger_sha256=policy["source_ledger_sha256"], source_rows=policy["source_rows"], selected_rows=1, source_fields=list(source[0]), appended_fields=audit.EXTRA, cohort_id=policy["cohort_id"], source_row_preservation="all original fields unchanged", state_counts=dict(Counter(r["execution_position_state"] for r in expected.values())), actual_fill_verified=False, execution_evidence_state="unknown", exception_coverage_verified=False, formal_use=False, promotion_evidence_allowed=False, artifacts={audit.name(kind): {"sha256": audit.digest(raw), "bytes": len(raw)} for kind, raw in payloads.items()})
    audit.audit_manifest(manifest, payloads, policy, list(source[0]), source, expected)
    changed = copy.deepcopy(manifest)
    changed["replay_started_at"] = "2026-05-01T00:00:00+00:00"
    with pytest.raises(ValueError, match="before replay"):
        audit.audit_manifest(changed, payloads, policy, list(source[0]), source, expected)
    changed = dict(payloads, **{"report_v1.md": b"changed report"})
    with pytest.raises(ValueError, match="hash/byte"):
        audit.audit_manifest(manifest, changed, policy, list(source[0]), source, expected)


def test_published_artifacts_independent_replay(audit):
    # Mandatory: missing artifacts/source objects are failures, never a skip.
    assert audit.validate(ROOT) == []
