from __future__ import annotations

import ast
import copy
import json
import subprocess
from decimal import Decimal, localcontext
from pathlib import Path

import pytest

from scripts import validate_tdcc_stealth_accumulation_operation_replay as validator


def test_d0_plus_five_counts_exchange_dates_not_price_rows():
    assert validator._scheduled_dates("20260709", 5, {"20260710"}) == ("20260713", "20260720")
    assert validator._scheduled_dates("20260616", 10, {"20260619"}) == ("20260617", "20260702")


@pytest.mark.parametrize("horizon", [0, 1, 4, 6, 15, 30])
def test_unregistered_horizons_rejected(horizon):
    with pytest.raises(ValueError, match="unregistered"):
        validator._scheduled_dates("20260709", horizon, {"20260710"})


def verified_feature(**changes):
    row = {
        "feature": "close", "effective_date": "20260709",
        "available_at": "2026-07-13T08:29:59+08:00",
        "evidence_status": "verified_historical_availability",
        "evidence_type": "original_archived_release",
        "source_ref": "immutable-acquisition-record", "source_sha256": "a" * 64,
    }
    row.update(changes)
    return row


def test_pit_strict_before_cutoff_and_effective_day():
    check = lambda r: validator._pit_errors([r], "20260709", "20260713", {"close"})
    assert check(verified_feature()) == []
    assert check(verified_feature(available_at="2026-07-13T00:29:59Z")) == []
    assert any("strictly before" in e for e in check(verified_feature(available_at="2026-07-13T08:30:00+08:00")))
    assert any("strictly before" in e for e in check(verified_feature(available_at="2026-07-13T08:30:01+08:00")))
    assert any("effective date" in e for e in check(verified_feature(effective_date="20260710")))


@pytest.mark.parametrize("kind", ["git_commit", "snapshot_generated_at", "current_download", "backfill"])
def test_metadata_not_accepted_as_feature_availability(kind):
    errors = validator._pit_errors([verified_feature(evidence_type=kind)], "20260709", "20260713", {"close"})
    assert any("metadata" in error for error in errors)


@pytest.mark.parametrize("change", [
    {"source_sha256": ""}, {"source_ref": ""}, {"effective_date": ""},
    {"available_at": "2026-07-13T08:29:59"}, {"evidence_status": "unverified"},
])
def test_missing_pit_evidence_fails_closed(change):
    assert validator._pit_errors([verified_feature(**change)], "20260709", "20260713", {"close"})


def test_pit_cannot_omit_duplicate_or_invent_feature_coverage():
    for evidence, required in [([], {"close"}), ([verified_feature()] * 2, {"close"}),
                               ([verified_feature()], {"close", "volume_ratio"})]:
        assert validator._pit_errors(evidence, "20260709", "20260713", required)


def test_cost_minimum_fee_tax_cash_and_slippage_independent_numbers():
    result = validator._cost_oracle("1", "1.1", "0")
    assert result["buy_fee"] == result["sell_fee"] == Decimal(20)
    assert result["sell_tax"] == Decimal("3.3")
    assert result["entry_cash"] == Decimal(1020)
    assert result["net_exit_cash"] == Decimal("1076.7")
    assert result["net_profit"] == Decimal("56.7")
    assert result["gross_return_pct"] == Decimal(10)
    with_cash = validator._cost_oracle("1", "1.1", "0", cash_flows="50")
    assert with_cash["net_exit_cash"] - result["net_exit_cash"] == 50
    results = [validator._cost_oracle("100", "110", s) for s in ["0", "0.001", "0.002"]]
    assert results[0]["net_return_pct"] > results[1]["net_return_pct"] > results[2]["net_return_pct"]
    assert results[1]["buy_notional"] == Decimal(100100)
    assert results[1]["sell_notional"] == Decimal(109890)
    assert results[1]["buy_fee"] == Decimal("142.6425")
    assert results[1]["sell_fee"] == Decimal("156.59325")
    assert results[1]["sell_tax"] == Decimal("329.670")


def test_cost_share_action_not_double_counted_and_precision_local():
    expected = validator._cost_oracle("100", "50", "0", exit_shares="2000", cash_flows="2000")
    assert expected["gross_return_pct"] == Decimal(2)
    with localcontext() as context:
        context.prec = 7
        assert validator._cost_oracle("100", "50", "0", exit_shares="2000", cash_flows="2000") == expected
        assert context.prec == 7


@pytest.mark.parametrize("value", ["NaN", "Infinity", "-Infinity", "", "0", "-1"])
def test_invalid_prices_never_generate_return(value):
    with pytest.raises(ValueError):
        validator._cost_oracle(value, "10", "0.001")


@pytest.mark.parametrize("payload", [b"\xef\xbb\xbfa,b\n1,2\n", b"a,b\r1,2\r", b"a,b\r\n1,2\n", b"\xff"])
def test_output_bytes_reject_transport_ambiguity(payload):
    with pytest.raises((ValueError, UnicodeError)):
        validator._csv(payload, output=True)


def test_actual_changed_bytes_are_never_replaced_by_git_head():
    assert validator._lf_payload(b"a,b\r\n1,2\r\n") == b"a,b\n1,2\n"
    assert validator._sha(validator._lf_payload(b"a,b\n1,3\n")) != validator._sha(b"a,b\n1,2\n")


@pytest.mark.parametrize("payload", [b"a,a\n1,2\n", b"a,b\n1\n", b"a,b\n1,2,3\n"])
def test_csv_duplicate_and_width_corruption_rejected(payload):
    with pytest.raises(ValueError):
        validator._csv(payload, output=True)


def test_manifest_duplicate_keys_rejected():
    with pytest.raises(ValueError, match="duplicate JSON"):
        validator._unique_json('{"source_ref":"a","source_ref":"b"}')


def test_validator_is_independent_of_business_producers():
    source = Path(validator.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            forbidden.extend(alias.name for alias in node.names if "build_" in alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module and ("build_" in node.module or "production" in node.module):
            forbidden.append(node.module)
    assert forbidden == []
    assert "exec(" not in source and "eval(" not in source


def signature_row(**changes):
    row = {
        "tdcc_accumulation_signal": "mild_accumulation", "volume_ratio": "1.5",
        "return_5d_pct": "2", "return_20d_pct": "3", "close": "10", "open": "9.5",
        "high": "10.5", "low": "9", "previous_20d_high": "12", "previous_20d_low": "8",
        "previous_close": "9.5", "volume_ma20": "1000000", "daily_return_calc": "5",
    }
    row.update(changes)
    return row


def test_signature_compares_actual_values_not_only_gate_booleans():
    baseline, _ = validator._serialized_signature(signature_row())
    changed, _ = validator._serialized_signature(signature_row(volume_ratio="1.6"))
    assert baseline != changed
    assert baseline["volume_ratio"] == "1.5" and changed["volume_ratio"] == "1.6"


def test_unused_fallback_metadata_and_alias_name_do_not_create_conflict():
    baseline, source = validator._serialized_signature(signature_row())
    unused, _ = validator._serialized_signature(signature_row(platform_low="0", source_path="other", category="other", volume_ratio_x="999"))
    assert baseline == unused
    alias_row = signature_row(volume_ratio="", volume_ratio_x="1.500")
    alias, alias_source = validator._serialized_signature(alias_row)
    assert baseline == alias
    assert source["volume_ratio"] != alias_source["volume_ratio"]


def test_explicit_phase_does_not_use_status_or_enum_fallback():
    a, _ = validator._serialized_signature(signature_row(tdcc_price_phase="TDCC_LEADING_PRICE", tdcc_status="unknown", tdcc_accumulation_signal="distribution"))
    b, _ = validator._serialized_signature(signature_row(tdcc_price_phase="tdcc_leading_price", tdcc_status="mild_accumulation", tdcc_accumulation_signal="mild_accumulation"))
    assert a == b
    assert a["tdcc_positive_branch"] == "explicit_phase"
    assert "tdcc_status" not in a and "tdcc_accumulation_enum" not in a


def test_original_boolean_does_not_consume_suffixed_true_as_boolean():
    a, _ = validator._serialized_signature(signature_row(tdcc_accumulation_signal="", tdcc_accumulation_signal_x="True"))
    b, _ = validator._serialized_signature(signature_row(tdcc_accumulation_signal="True"))
    assert a["tdcc_positive_branch"] == "enum_fallback"
    assert b["tdcc_positive_branch"] == "original_boolean"
    assert a != b


def test_signature_attack_helpers_units_level_and_daily_return():
    row = signature_row(previous_20d_high="11", high="10", platform_high="10.5", daily_return_calc="", previous_close="8")
    values, sources = validator._serialized_signature(row)
    assert values["volume_ma20_lots"] == "1000"
    assert values["breakout_level"] == "10.5"
    assert sources["breakout_level"] == "platform_high"
    assert values["daily_return_pct"] == "25"
    assert sources["daily_return_pct"] == "derived_close_previous_close"
    alternate, _ = validator._serialized_signature({**row, "previous_close": "9"})
    assert values != alternate


@pytest.mark.parametrize("mutation", [
    {"verified": True}, {"available_at": "2026-07-13T08:00:00+08:00"},
    {"effective_date": "20260709"}, {"evidence_ref": "git:abc"},
])
def test_fixed_historical_source_cannot_gain_fabricated_feature_evidence(mutation):
    field = {"name": "close", "effective_date": "", "available_at": "", "verified": False, "evidence_ref": ""}
    assert validator._check_feature_placeholders([field], {"close"})
    assert not validator._check_feature_placeholders([{**field, **mutation}], {"close"})
    assert not validator._check_feature_placeholders([], {"close"})


def position_fixture(event_id="A:20260701", signal_date="20260701", entry_date="20260702", exit_date="20260709", status="realized", horizon="5"):
    base = {
        "event_id": event_id, "position_id": f"{event_id}:D{horizon}", "stock_id": "A", "signal_date": signal_date,
        "horizon": horizon, "entry_date": entry_date, "exit_date": exit_date, "entry_open": "1", "exit_close": "1.1",
        "status": status, "actions": "[]", "quantity": "1000", "anomaly_candidate": "False", "observation_ids": "[]",
        "net_return_pct": "", "gross_return_pct": "", "net_pnl": "", "outcome": "", "high_return_hit": "", "major_loss": "",
    }
    rows = []
    for s in validator.SLIPPAGES:
        row = {**base, "slippage": str(s)}
        if status == "realized":
            with localcontext() as context:
                context.prec = 50
                buy = Decimal(1000) * (1 + s)
                sell = Decimal(1100) * (1 - s)
                entry_cash = buy + 20
                tax = sell * Decimal("0.003")
                net_exit = sell - 20 - tax
                pnl = net_exit - entry_cash
                metrics = {"buy_amount": buy, "sell_amount": sell, "buy_fee": Decimal(20), "sell_fee": Decimal(20),
                           "sell_tax": tax, "entry_cash": entry_cash, "net_exit_cash": net_exit, "net_pnl": pnl,
                           "net_return_pct": pnl / entry_cash * 100, "gross_pnl": Decimal(100), "gross_return_pct": Decimal(10), "final_shares": Decimal(1000), "cash_flows": Decimal(0)}
                row.update({name: str(value) for name, value in metrics.items()})
                row.update(outcome="win", high_return_hit="False", major_loss="False")
        rows.append(row)
    event = {"event_id": event_id, "horizon": horizon, "status": "position_opened"}
    return rows, [event]


def test_independent_nonempty_cost_position_fixture_passes():
    positions, events = position_fixture()
    assert validator._validate_positions(positions, events) == []


@pytest.mark.parametrize("field", ["buy_amount", "sell_amount", "buy_fee", "sell_fee", "sell_tax", "entry_cash", "net_exit_cash", "net_pnl", "gross_pnl", "net_return_pct", "gross_return_pct", "final_shares", "cash_flows"])
def test_actual_position_cost_mutation_is_detected(field):
    positions, events = position_fixture()
    positions[0][field] = str(Decimal(positions[0][field]) + 1)
    assert validator._validate_positions(positions, events)


def test_three_slippages_are_same_position_set_not_three_positions():
    positions, events = position_fixture()
    assert validator._validate_positions(positions[:-1], events)
    positions[2]["entry_date"] = "20260703"
    assert any("sensitivity changed" in e for e in validator._validate_positions(positions, events))


def test_no_entry_without_accepted_event_and_quantity_fixed():
    positions, events = position_fixture()
    events[0]["status"] = "feature_evidence_missing"
    assert any("accepted entry" in e for e in validator._validate_positions(positions, events))
    positions[0]["quantity"] = "2000"
    assert any("quantity" in e for e in validator._validate_positions(positions, events))


@pytest.mark.parametrize("prior_status", ["open_immature", "open_unresolved_exit"])
def test_unresolved_and_immature_lock_never_released(prior_status):
    old_positions, old_events = position_fixture(status=prior_status)
    new_positions, new_events = position_fixture("A:20260710", "20260710", "20260713", "20260720")
    assert any("lock" in e for e in validator._validate_positions(old_positions + new_positions, old_events + new_events))


def test_exit_day_cannot_reenter_and_later_new_signal_can():
    old_positions, old_events = position_fixture()
    same_positions, same_events = position_fixture("A:20260709", "20260709", "20260710", "20260717")
    assert any("lock" in e for e in validator._validate_positions(old_positions + same_positions, old_events + same_events))
    new_positions, new_events = position_fixture("A:20260710", "20260710", "20260713", "20260720")
    assert validator._validate_positions(old_positions + new_positions, old_events + new_events) == []


def test_horizon_position_locks_are_independent():
    old_positions, old_events = position_fixture(status="open_unresolved_exit")
    new_positions, new_events = position_fixture("A:20260703", "20260703", "20260706", "20260720", horizon="10")
    assert validator._validate_positions(old_positions + new_positions, old_events + new_events) == []


def test_unrealized_cannot_sneak_zero_return_into_denominator():
    positions, events = position_fixture(status="open_unresolved_exit")
    positions[0]["net_return_pct"] = "0"
    assert any("denominators" in e for e in validator._validate_positions(positions, events))


def test_source_refs_are_not_interchangeable_and_actual_files_required(tmp_path):
    assert validator.validate(tmp_path, validator.ARTIFACT_SOURCE_REF, validator.SOURCE_REF)
    assert any("actual artifact" in e for e in validator.validate(tmp_path))
    assert validator.main(["--repository-root", str(tmp_path)]) == 1


def test_price_oracle_never_skips_missing_scheduled_stock_or_future_day():
    class Source:
        def rows(self, ref, path):
            return [{"date": "20260713", "stock_id": "B", "open": "10", "close": "11"}]
    baseline = {"as_of": "20260713", "price_paths": {"20260713": "price"}}
    assert validator._price_observation(Source(), baseline, "20260713", "A", "open", {})[0] == "missing_stock_price"
    assert validator._price_observation(Source(), baseline, "20260710", "A", "open", {})[0] == "missing_date_file"
    assert validator._price_observation(Source(), baseline, "20260714", "B", "open", {})[0] == "after_source_asof"


def summary_fixture():
    positions, _ = position_fixture()
    events = []
    for horizon in ("5", "10", "20"):
        for stock in ("A", "B"):
            events.append({"event_id": f"{stock}:20260701", "stock_id": stock, "horizon": horizon,
                           "window_status": "immature" if horizon == "20" else "mature_calendar_window",
                           "evidence_missing": "" if stock == "A" and horizon == "5" else "feature_missing",
                           "signature_conflict": "False", "status": "position_opened" if stock == "A" and horizon == "5" else "feature_evidence_missing"})
    summaries = []
    for horizon in ("5", "10", "20"):
        for slip in ("0", "0.001", "0.002"):
            for population in ("primary", "excluding_anomaly_candidates_sensitivity"):
                n = 1 if horizon == "5" else 0
                returned = next(row["net_return_pct"] for row in positions if row["slippage"] == slip) if n else ""
                summaries.append({
                    "horizon": horizon, "slippage": slip, "analysis_population": population,
                    "artifact_version": "tdcc_stealth_accumulation_operation_replay_v3", "signal_count": "3", "event_count": "2",
                    "stock_count": "2", "position_count": str(n), "realized_count": str(n), "immature_count": "0", "unresolved_count": "0",
                    "immature_event_count": "2" if horizon == "20" else "0", "evidence_missing_event_count": "1" if n else "2",
                    "conflict_event_count": "0", "win_count": str(n), "neutral_count": "0", "loss_count": "0",
                    "high_return_hit_count": "0", "major_loss_count": "0",
                    "denominator": "all_realized_positions_in_this_horizon_slippage_population",
                    "performance_status": "research_only_verified_position_sample" if n else "unavailable_no_realized_verified_positions",
                    "status_counts": json.dumps({"feature_evidence_missing": 1, "position_opened": 1} if n else {"feature_evidence_missing": 2}, sort_keys=True, separators=(",", ":")),
                    "win_rate_pct": "100" if n else "", "neutral_rate_pct": "0" if n else "", "loss_rate_pct": "0" if n else "",
                    "high_return_hit_rate_pct": "0" if n else "", "major_loss_rate_pct": "0" if n else "",
                    "average_net_return_pct": returned, "median_net_return_pct": returned, "tail_loss_pct": returned,
                })
    return summaries, events, positions


def test_summary_denominator_uses_realized_positions_not_signal_or_event_counts():
    summary, events, positions = summary_fixture()
    assert validator._validate_summary(summary, events, positions, 3) == []
    summary[0]["win_rate_pct"] = "50"
    assert any("win_rate_pct" in error for error in validator._validate_summary(summary, events, positions, 3))


@pytest.mark.parametrize("field", ["event_count", "signal_count", "position_count", "realized_count", "immature_event_count", "evidence_missing_event_count", "win_count", "loss_count", "high_return_hit_count", "major_loss_count", "average_net_return_pct", "median_net_return_pct", "tail_loss_pct"])
def test_summary_cannot_self_report_changed_counts_or_metrics(field):
    summary, events, positions = summary_fixture()
    summary[0][field] = "999"
    assert any(field in error for error in validator._validate_summary(summary, events, positions, 3))


def test_empty_realized_denominator_requires_blank_not_zero_return():
    summary, events, positions = summary_fixture()
    empty = next(row for row in summary if row["horizon"] == "10")
    assert empty["average_net_return_pct"] == ""
    empty["average_net_return_pct"] = "0"
    assert any("average_net_return_pct" in error for error in validator._validate_summary(summary, events, positions, 3))


def test_sensitivity_must_not_remove_or_rename_primary_summary_cells():
    summary, events, positions = summary_fixture()
    assert validator._validate_summary(summary[1:], events, positions, 3)
    summary[0]["analysis_population"] = "corrected_primary"
    assert validator._validate_summary(summary, events, positions, 3)


@pytest.mark.parametrize("flag", validator.FALSE_FLAGS)
def test_no_formal_promotion_or_trade_eligibility_allowed(flag):
    row = {field: "False" for field in validator.FALSE_FLAGS}
    assert validator._flag_errors([row], "test") == []
    row[flag] = "True"
    assert validator._flag_errors([row], "test")
    del row[flag]
    assert validator._flag_errors([row], "test")


def test_every_immutable_git_read_ignores_replace_objects(tmp_path, monkeypatch):
    calls = []
    class Result:
        stdout = b"verified"
    def capture(argv, **kwargs):
        calls.append(argv)
        return Result()
    monkeypatch.setattr(validator.subprocess, "run", capture)
    reader = validator._Sources(tmp_path)
    for command in [("show", "ref:path"), ("rev-parse", "ref"), ("ls-tree", "-r", "ref")]:
        assert reader.git(*command) == b"verified"
    assert all(call[:4] == ["git", "--no-replace-objects", "-C", str(tmp_path)] for call in calls)


def test_real_git_replace_cannot_substitute_validator_blob(tmp_path):
    subprocess.run(["git", "init", "--quiet", str(tmp_path)], check=True, capture_output=True)
    def git(*args, data=None):
        return subprocess.run(["git", "-C", str(tmp_path), *args], input=data, check=True, capture_output=True).stdout
    original = git("hash-object", "-w", "--stdin", data=b"immutable original\n").decode().strip()
    substitute = git("hash-object", "-w", "--stdin", data=b"replacement poisoned\n").decode().strip()
    git("replace", original, substitute)
    assert git("cat-file", "blob", original) == b"replacement poisoned\n"
    assert validator._Sources(tmp_path).git("cat-file", "blob", original) == b"immutable original\n"


def action(kind, event_date="20260706", **fields):
    return {"kind": kind, "event_date": event_date, "evidence_verified": True, "evidence_ref": f"source:{kind}", **fields}


def test_verified_cash_and_share_factors_use_temporal_shares_once():
    actions = [action("share_factor", "20260703", share_factor="2"), action("cash", "20260706", cash_per_share="3")]
    assert validator._action_cash_oracle(actions, "20260702", "20260709") == (Decimal(2000), Decimal(6000))
    reversed_dates = [action("cash", "20260703", cash_per_share="3"), action("share_factor", "20260706", share_factor="2")]
    assert validator._action_cash_oracle(reversed_dates, "20260702", "20260709") == (Decimal(2000), Decimal(3000))


def test_same_day_mixed_actions_require_evidenced_order_not_list_order():
    actions = [action("cash", cash_per_share="3"), action("share_factor", share_factor="2")]
    with pytest.raises(ValueError, match="ordering"):
        validator._action_cash_oracle(actions, "20260702", "20260709")
    actions[0].update(sequence=2, sequence_evidence_ref="filing:order")
    actions[1].update(sequence=1, sequence_evidence_ref="filing:order")
    assert validator._action_cash_oracle(actions, "20260702", "20260709") == (Decimal(2000), Decimal(6000))
    actions[0]["sequence"] = 1
    with pytest.raises(ValueError, match="ordering"):
        validator._action_cash_oracle(actions, "20260702", "20260709")


@pytest.mark.parametrize("mutation", [{"evidence_verified": False}, {"evidence_ref": ""}, {"event_date": "20260710"}, {"event_date": "20260701"}, {"event_date": "20260230"}])
def test_action_missing_evidence_or_outside_window_is_not_applied(mutation):
    row = action("cash", cash_per_share="3")
    row.update(mutation)
    with pytest.raises(ValueError):
        validator._action_cash_oracle([row], "20260702", "20260709")


def test_identical_cash_event_cannot_be_counted_twice():
    row = action("cash", cash_per_share="3")
    with pytest.raises(ValueError, match="double-count"):
        validator._action_cash_oracle([row, row.copy()], "20260702", "20260709")


@pytest.mark.parametrize("manifest", [b"[]\n", b"null\n", b'"text"\n', b"1\n"])
def test_malformed_manifest_shape_returns_errors_not_attribute_error(manifest):
    payloads = {name: b"id\n" for name in validator.ARTIFACT_SUFFIXES}
    payloads["manifest_v3.json"] = manifest
    assert validator._validate_payloads(payloads, None) == ["manifest JSON must be an object"]
