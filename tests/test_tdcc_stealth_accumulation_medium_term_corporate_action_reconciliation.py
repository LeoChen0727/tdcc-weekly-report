"""TDCC 潛伏吸籌：新帳本 synthetic；不重播舊 selector。"""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_tdcc_stealth_accumulation_medium_term_corporate_action_reconciliation as p


def event(**updates):
    row = dict(event_id="8422_share_exchange_20251117", stock_id="8422", kind="share_exchange", holding_cutoff_date="20251106", effective_date="20251117", tradable_date="20251117", record_date="20251114", suspension_end="20251114", share_factor="10", cash_per_old_share="", documents=["official"])
    row.update(updates)
    return row


def trade(**updates):
    row = dict(profile="common_12", strategy="trend_8", partition="training", trade_id="test:8422:D20:S0", signal_date="20251102", stock_id="8422", horizon="20", slippage_bps="0", entry_date="20251103", exit_date="20251201", shares="1000", entry_open="241.5", exit_close="23.9", entry_cash="241844.1375", net_return_pct="-90.181", primary_row_retained="True", anomaly_candidate="True", formal_use="False", promotion_evidence_allowed="False")
    row.update(updates)
    return row


def test_real_contract_sealed_official_documents_and_exact_three_events():
    cfg = p.load_contract(ROOT)
    assert len(cfg["events"]) == 3
    assert cfg["source_trade_count"] == 305673
    assert all(e["cash_per_old_share"] == "" for e in cfg["events"])


def test_one_to_ten_changes_only_new_fields_and_unknown_cash_is_not_zero():
    old = trade(); preserved = deepcopy(old)
    result = p.reconcile(old, [event()])
    assert old == preserved
    assert result["theoretical_exit_shares"] == "10000"
    assert abs(Decimal(result["known_action_gross_price_proxy_pct"]) - (Decimal("239000") / Decimal("241500") - 1) * 100) < Decimal("1e-25")
    assert result["known_action_costed_proxy_pct"] == ""
    assert "action_cash_amount_unknown" in result["reconciliation_block_reasons"]
    assert result["verified_total_return_pct"] == ""
    assert result["reconciliation_total_return_verified"] == "False"


def test_explicit_zero_action_cash_is_only_conditional_cost_proxy_not_realized():
    result = p.reconcile(trade(), [event(cash_per_old_share="0")])
    assert result["known_action_costed_proxy_pct"] != ""
    assert result["verified_total_return_pct"] == ""
    assert result["corporate_action_coverage_complete"] == "False"
    assert "dividend_coverage_unverified" in result["reconciliation_block_reasons"]


def test_precise_capital_reduction_preserves_fraction_without_rounded_cash_disposal():
    result = p.reconcile(trade(), [event(share_factor="0.27658171", cash_per_old_share="0")])
    assert result["theoretical_exit_shares"] == "276.58171"
    assert result["theoretical_whole_shares"] == "276"
    assert result["unresolved_fractional_shares"] == "0.58171"
    assert result["known_action_gross_price_proxy_pct"] != ""
    assert result["known_action_costed_proxy_pct"] == ""
    assert "fractional_disposition_unverified" in result["reconciliation_block_reasons"]


@pytest.mark.parametrize("exit_date,tradable,shares,pending", [("20251114", "20251117", "0", "10000"), ("20251117", "20251117", "10000", "0"), ("20251201", "", "0", "10000")])
def test_original_exit_and_unknown_tradability_are_not_backfilled(exit_date, tradable, shares, pending):
    old = trade(exit_date=exit_date)
    result = p.reconcile(old, [event(tradable_date=tradable)])
    assert old["exit_date"] == exit_date
    assert result["theoretical_exit_shares"] == shares
    assert result["pending_share_rights"] == pending
    if pending != "0": assert result["known_action_gross_price_proxy_pct"] == ""


def test_no_event_and_future_event_do_not_certify_absence():
    for events in ([], [event(holding_cutoff_date="20261201", effective_date="20261210", tradable_date="20261210", record_date="20261209", suspension_end="20261209")]):
        row = p.reconcile(trade(), events)
        assert row["matched_event_ids"] == ""
        assert row["known_action_gross_price_proxy_pct"] == ""
        assert "no_event_is_not_absence_proof" in row["reconciliation_block_reasons"]


@pytest.mark.parametrize("entry", ["20251106", "20251114"])
def test_entry_during_known_suspension_fails_closed(entry):
    with pytest.raises(ValueError, match="停牌"):
        p.reconcile(trade(entry_date=entry), [event()])


def test_entry_on_new_tradable_date_receives_no_old_share_conversion():
    result = p.reconcile(trade(entry_date="20251117"), [event()])
    assert result["matched_event_ids"] == ""
    assert result["theoretical_exit_shares"] == "1000"


@pytest.mark.parametrize("changes", [dict(share_factor="0"), dict(share_factor="NaN"), dict(share_factor="-1"), dict(holding_cutoff_date="20250230"), dict(tradable_date="20251101"), dict(kind="cash_dividend"), dict(documents=[])])
def test_invalid_events_rejected(changes):
    with pytest.raises((ValueError, ArithmeticError)):
        p.reconcile(trade(), [event(**changes)])


def test_duplicate_economic_event_and_unsettled_followup_rejected():
    with pytest.raises(ValueError, match="重複"):
        p.reconcile(trade(), [event(), event(event_id="duplicate")])
    with pytest.raises(ValueError, match="前次權利"):
        p.reconcile(trade(), [event(tradable_date=""), event(event_id="next", holding_cutoff_date="20251120", effective_date="20251130", tradable_date="20251130", record_date="20251129", suspension_end="20251129")])


def test_writer_exact_allowlist_and_registration_precede_write(tmp_path, monkeypatch):
    if sys.platform == "win32": tmp_path = Path("\\\\?\\" + str(tmp_path))
    monkeypatch.setattr(p, "load_ownership_rules", lambda path: [])
    monkeypatch.setattr(p, "validate_changed_paths", lambda *args: [])
    payloads = {name: b"synthetic\n" for name in p.GENERATED}
    p.write_outputs(tmp_path, payloads)
    assert {x.name for x in (tmp_path / p.DIRECTORY).iterdir()} == p.GENERATED
    with pytest.raises(ValueError, match="六個"):
        p.write_outputs(tmp_path, {**payloads, "outside.txt": b"x"})
    monkeypatch.setattr(p, "validate_changed_paths", lambda *args: ["wrong owner"])
    with pytest.raises(ValueError, match="登錄"):
        p.write_outputs(tmp_path, payloads)


def test_contract_mutation_is_not_a_baseline_update(tmp_path):
    cfg = json.loads((ROOT / p.CONTRACT).read_text(encoding="utf-8"))
    cfg["events"][2]["share_factor"] = "0.2766"
    path = tmp_path / p.CONTRACT
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(cfg), encoding="utf-8")
    with pytest.raises(ValueError, match="雜湊"):
        p.load_contract(tmp_path)


def test_main_binds_outside_bytes_even_after_exception(monkeypatch, tmp_path):
    snapshots = iter(["before", "after"])
    monkeypatch.setattr(p, "snapshot", lambda root: next(snapshots))
    monkeypatch.setattr(p, "build", lambda root: {})
    monkeypatch.setattr(p, "write_outputs", lambda *args: None)
    with pytest.raises(ValueError, match="漂移"):
        p.main(["--repository-root", str(tmp_path)])
