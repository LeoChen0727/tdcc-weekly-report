"""方案 A 的直接語意 oracle；合成證據不得被引用為真實交易證明。"""

from __future__ import annotations

import hashlib
import os
import subprocess
import sys
from copy import deepcopy
from decimal import Decimal, localcontext
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_tdcc_stealth_accumulation_operation_replay as producer  # noqa: E402


# 測試明確注入的交易所日期 fixture，不宣稱是這段期間的真實官方日曆。
CALENDAR = [
    "20260911", "20260914", "20260915", "20260916", "20260917",
    "20260918", "20260921", "20260922", "20260923", "20260924",
    "20260925", "20260928", "20260929", "20260930", "20261001",
    "20261002", "20261005", "20261006", "20261007", "20261008",
    "20261009", "20261012", "20261013", "20261014", "20261015",
    "20261016",
]
FORMAL_FLAGS = ("formal_use", "trade_eligible", "promotion_evidence_allowed")


def raw_signal() -> dict[str, str]:
    return {
        "stock_id": "2330",
        "signal_date": "20260911",
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
        "volume": "1200000",
        "volume_ma20": "1000000",
        "previous_close": "99",
        "previous_20d_high": "110",
        "daily_return": "1",
        "volume_confirmed_breakout": "False",
    }


def signal(
    signal_id: str = "signal-1", stock_id: str = "2330", date: str = "20260911"
) -> dict:
    raw = raw_signal()
    raw.update(stock_id=stock_id, signal_date=date)
    signature = producer.signal_signature(raw)["values"]
    entry = CALENDAR[CALENDAR.index(date) + 1]
    timestamp = f"{entry[:4]}-{entry[4:6]}-{entry[6:]}T08:29:59+08:00"
    return {
        "signal_id": signal_id,
        "stock_id": stock_id,
        "signal_date": date,
        "signature": signature,
        "source_lineage": {"source_path": f"fixture/{signal_id}.csv", "row": "1"},
        "feature_evidence": [
            {
                "name": name,
                "effective_date": date,
                "available_at": timestamp,
                "verified": True,
                "evidence_ref": f"synthetic-proof/{signal_id}/{name}",
            }
            for name in signature
        ],
        "calendar_verified": True,
        "corporate_actions_verified": True,
        "actions": [],
        "anomaly_candidate": False,
        "anomaly_disposition": "",
        "observation_ids": [],
    }


def prices(stocks: tuple[str, ...] = ("2330",)) -> dict:
    return {
        (stock, date): {
            "open": "100",
            "close": "110",
            "open_verified": True,
            "close_verified": True,
            "executable": True,
            "source_path": f"synthetic-price/{stock}/{date}.csv",
            "source_sha256": "a" * 64,
            "row_sha256": "b" * 64,
        }
        for stock in stocks
        for date in CALENDAR
    }


def replay(signals: list[dict], *, quote_rows=None, as_of="20261016", horizons=(5,)):
    events = producer.merge_signals(signals)
    return producer.replay_events(
        events, CALENDAR, prices() if quote_rows is None else quote_rows, as_of, horizons=horizons
    )


def base_positions(rows: list[dict], horizon: int = 5) -> list[dict]:
    return [
        row for row in rows
        if int(row["horizon"]) == horizon and Decimal(str(row["slippage"])) == Decimal("0.001")
    ]


def test_entry_is_next_exchange_day_and_entry_is_d0() -> None:
    assert producer.plan_dates("20260911", CALENDAR[:8], 5) == ("20260914", "20260921")
    assert producer.plan_dates("20260911", CALENDAR, 10) == ("20260914", "20260928")
    assert producer.plan_dates("20260911", CALENDAR, 20) == ("20260914", "20261012")


def test_calendar_exhaustion_does_not_invent_exit_or_entry() -> None:
    entry, exit_date = producer.plan_dates("20260911", CALENDAR[:6], 5)
    assert entry == "20260914"
    assert not exit_date
    entry, exit_date = producer.plan_dates("20261016", CALENDAR, 5)
    assert not entry
    assert not exit_date


def test_plan_is_driven_by_calendar_not_next_observed_price() -> None:
    quote_rows = prices()
    del quote_rows[("2330", "20260921")]
    evaluations, positions = replay([signal()], quote_rows=quote_rows)
    assert len(evaluations) == 1
    assert len(positions) == 3
    assert {row["exit_date"] for row in positions} == {"20260921"}
    assert {row["status"] for row in positions} == {"open_unresolved_exit"}
    assert all(not row.get("net_return_pct") for row in positions)


@pytest.mark.parametrize("defect", ["absent", "empty", "zero", "negative", "unverified", "unexecutable"])
def test_unavailable_entry_never_jumps_to_later_price(defect: str) -> None:
    quote_rows = prices()
    entry = quote_rows[("2330", "20260914")]
    if defect == "absent":
        del quote_rows[("2330", "20260914")]
    elif defect == "empty":
        entry["open"] = ""
    elif defect == "zero":
        entry["open"] = "0"
    elif defect == "negative":
        entry["open"] = "-1"
    elif defect == "unverified":
        entry["open_verified"] = False
    else:
        entry["executable"] = False
    evaluations, positions = replay([signal()], quote_rows=quote_rows)
    assert len(evaluations) == 1
    assert not positions


def test_exit_date_signal_cannot_reenter_but_later_signal_can() -> None:
    evaluations, positions = replay([
        signal("initial"),
        signal("held", date="20260918"),
        signal("same-exit", date="20260921"),
        signal("strictly-after", date="20260922"),
    ])
    assert len(evaluations) == 4
    assert [row["signal_date"] for row in base_positions(positions)] == ["20260911", "20260922"]
    assert [row["entry_date"] for row in base_positions(positions)] == ["20260914", "20260923"]
    assert [row["exit_date"] for row in base_positions(positions)] == ["20260921", "20260930"]


def test_held_signals_are_retained_but_never_queued_for_later_entry() -> None:
    evaluations, positions = replay([signal("initial"), signal("held", date="20260918")])
    assert len(evaluations) == 2
    assert len({row["event_id"] for row in evaluations}) == 2
    assert [row["signal_date"] for row in base_positions(positions)] == ["20260911"]


def test_each_horizon_has_an_independent_stock_lock() -> None:
    evaluations, positions = replay(
        [signal("initial"), signal("d5-reentry", date="20260922")], horizons=(5, 10)
    )
    assert len(evaluations) == 4
    assert [row["signal_date"] for row in base_positions(positions, 5)] == ["20260911", "20260922"]
    assert [row["signal_date"] for row in base_positions(positions, 10)] == ["20260911"]


@pytest.mark.parametrize("defect", ["absent", "empty", "unverified", "unexecutable"])
def test_unresolved_exit_keeps_lock_after_nominal_exit_date(defect: str) -> None:
    quote_rows = prices()
    exit_quote = quote_rows[("2330", "20260921")]
    if defect == "absent":
        del quote_rows[("2330", "20260921")]
    elif defect == "empty":
        exit_quote["close"] = ""
    elif defect == "unverified":
        exit_quote["close_verified"] = False
    else:
        exit_quote["executable"] = False
    evaluations, positions = replay(
        [signal("initial"), signal("later", date="20260922"), signal("much-later", date="20260928")],
        quote_rows=quote_rows,
    )
    assert len(evaluations) == 3
    assert len(positions) == 3
    assert {row["status"] for row in positions} == {"open_unresolved_exit"}
    assert {row["signal_date"] for row in positions} == {"20260911"}


def test_no_cross_stock_capital_or_ranking_constraint() -> None:
    evaluations, positions = replay(
        [signal("one", "2330"), signal("two", "2317")], quote_rows=prices(("2330", "2317"))
    )
    assert len(evaluations) == 2
    assert {row["stock_id"] for row in base_positions(positions)} == {"2330", "2317"}


@pytest.mark.parametrize(
    ("timestamp", "expected_positions"),
    [
        ("2026-09-14T08:29:59+08:00", 3),
        ("2026-09-14T08:30:00+08:00", 0),
        ("2026-09-14T08:30:01+08:00", 0),
        ("2026-09-14T00:29:59+00:00", 3),
        ("2026-09-14T00:30:00+00:00", 0),
    ],
)
def test_feature_availability_is_strict_before_taipei_cutoff(timestamp, expected_positions) -> None:
    row = signal()
    for evidence in row["feature_evidence"]:
        evidence["available_at"] = timestamp
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert len(positions) == expected_positions


@pytest.mark.parametrize(
    "defect", ["future-effective", "invalid-effective", "unverified", "missing-ref", "missing-date", "missing-available", "empty"]
)
def test_any_missing_or_invalid_feature_proof_fails_closed(defect: str) -> None:
    row = signal()
    evidence = row["feature_evidence"][0]
    if defect == "future-effective":
        evidence["effective_date"] = "20260914"
    elif defect == "invalid-effective":
        evidence["effective_date"] = "20260231"
    elif defect == "unverified":
        evidence["verified"] = False
    elif defect == "missing-ref":
        evidence["evidence_ref"] = ""
    elif defect == "missing-date":
        evidence["effective_date"] = ""
    elif defect == "missing-available":
        evidence["available_at"] = ""
    else:
        row["feature_evidence"] = []
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert not positions


def test_future_download_timestamp_is_not_historical_availability() -> None:
    row = signal()
    for evidence in row["feature_evidence"]:
        evidence["available_at"] = "2026-10-01T00:00:00+08:00"
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert not positions


def test_omitting_one_required_feature_proof_is_not_vacuously_verified() -> None:
    row = signal()
    assert len(row["feature_evidence"]) > 1
    row["feature_evidence"].pop()
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert not positions


@pytest.mark.parametrize("evidence_field", ["calendar_verified", "corporate_actions_verified"])
def test_missing_calendar_or_corporate_action_coverage_cannot_realize(evidence_field: str) -> None:
    row = signal()
    row[evidence_field] = False
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert not [position for position in positions if position["status"] == "realized"]


def test_missing_corporate_action_coverage_keeps_unresolved_position_lock() -> None:
    initial = signal("initial")
    initial["corporate_actions_verified"] = False
    evaluations, positions = replay([initial, signal("later", date="20260922")])
    assert len(evaluations) == 2
    assert len(positions) == 3
    assert {row["signal_date"] for row in positions} == {"20260911"}
    assert {row["status"] for row in positions} == {"open_unresolved_exit"}


def test_same_day_lineage_difference_merges_and_keeps_all_source_ids() -> None:
    first, second = signal("source-a"), signal("source-b")
    second["source_lineage"] = {"source_path": "another/category.csv", "sha256": "c" * 64, "row": "42"}
    events = producer.merge_signals([first, second])
    assert len(events) == 1
    assert events[0]["signature_conflict"] is False
    assert set(events[0]["source_ids"]) == {"source-a", "source-b"}
    evaluations, positions = replay([first, second])
    assert len(evaluations) == 1
    assert len(base_positions(positions)) == 1


@pytest.mark.parametrize("field,alternative", [("volume_ratio", "1.3"), ("return_5d", "4"), ("close", "101")])
def test_actual_signal_value_conflict_is_not_erased_by_both_rows_passing(field, alternative) -> None:
    first, second = signal("source-a"), signal("source-b")
    modified = raw_signal()
    modified[field] = alternative
    second["signature"] = producer.signal_signature(modified)["values"]
    events = producer.merge_signals([first, second])
    assert len(events) == 1
    assert events[0]["signature_conflict"] is True
    assert set(events[0]["source_ids"]) == {"source-a", "source-b"}
    evaluations, positions = replay([first, second])
    assert len(evaluations) == 1
    assert not positions


def test_signature_ignores_unused_fallback_and_path_hash_category() -> None:
    first = raw_signal()
    second = dict(first, close_x="999", volume_ratio_y="999", source_path="other.csv", source_sha256="d" * 64, category="other")
    assert producer.signal_signature(first)["values"] == producer.signal_signature(second)["values"]


def test_signature_resolves_value_priority_and_keeps_chosen_source_separately() -> None:
    direct = raw_signal()
    suffixed = raw_signal()
    suffixed.pop("close")
    suffixed["close_x"] = "100"
    suffixed["close_y"] = "999"
    direct_signature = producer.signal_signature(direct)
    suffix_signature = producer.signal_signature(suffixed)
    assert direct_signature["values"] == suffix_signature["values"]
    assert direct_signature["sources"]["close"] == "close"
    assert suffix_signature["sources"]["close"] == "close_x"


def test_decimal_cost_oracle_and_gross_hit_is_not_net_hit() -> None:
    result = producer.calculate_costs("100", "110")
    expected = {
        "buy_amount": "100100", "sell_amount": "109890",
        "buy_fee": "142.6425", "sell_fee": "156.59325", "sell_tax": "329.67",
        "entry_cash": "100242.6425", "net_exit_cash": "109403.73675",
        "net_pnl": "9161.09425", "gross_pnl": "10000", "gross_return_pct": "10",
    }
    for field, value in expected.items():
        assert isinstance(result[field], Decimal), field
        assert result[field] == Decimal(value), field
    with localcontext() as context:
        context.prec = 50
        assert result["net_return_pct"] == Decimal("9161.09425") / Decimal("100242.6425") * Decimal("100")
    assert abs(result["net_return_pct"] - Decimal("9.1389193476")) < Decimal("0.0000000001")
    assert result["net_return_pct"] < Decimal("10")


def test_minimum_commission_oracle() -> None:
    result = producer.calculate_costs("10", "11")
    assert result["buy_fee"] == result["sell_fee"] == Decimal("20")
    assert result["net_pnl"] == Decimal("906.033")


def test_flat_gross_price_is_net_loss() -> None:
    result = producer.calculate_costs("100", "100")
    assert result["gross_return_pct"] == Decimal("0")
    assert result["net_pnl"] == Decimal("-784.7")
    assert result["net_return_pct"] < 0


def test_costs_use_decimal_input_without_intermediate_rounding() -> None:
    result = producer.calculate_costs("100.123456789", "110.987654321", slippage="0.002")
    buy = Decimal("1000") * Decimal("100.123456789") * Decimal("1.002")
    sell = Decimal("1000") * Decimal("110.987654321") * Decimal("0.998")
    buy_fee = buy * Decimal("0.001425")
    sell_fee = sell * Decimal("0.001425")
    assert result["buy_amount"] == buy
    assert result["buy_fee"] == buy_fee
    assert result["sell_fee"] == sell_fee
    assert result["net_pnl"] == sell - sell_fee - sell * Decimal("0.003") - buy - buy_fee


def action(kind: str, date: str, value: str) -> dict:
    return {
        "event_date": date,
        "kind": kind,
        "cash_per_share" if kind == "cash" else "share_factor": value,
        "evidence_verified": True,
        "evidence_ref": f"synthetic-corporate-action/{date}/{kind}",
    }


def test_verified_split_then_cash_uses_event_time_shares_once() -> None:
    # 輸入刻意逆序，計算必須依 event_date；55 為未還原出場價格。
    result = producer.calculate_costs(
        "100", "55", actions=[action("cash", "20260916", "1"), action("share_factor", "20260915", "2")]
    )
    assert result["final_shares"] == Decimal("2000")
    assert result["cash_flows"] == Decimal("2000")
    assert result["sell_amount"] == Decimal("109890")
    assert result["net_pnl"] == Decimal("11161.09425")
    assert result["gross_pnl"] == Decimal("12000")
    assert result["gross_return_pct"] == Decimal("12")


def test_cash_before_split_uses_only_pre_split_shares() -> None:
    result = producer.calculate_costs(
        "100", "55", actions=[action("share_factor", "20260916", "2"), action("cash", "20260915", "1")]
    )
    assert result["final_shares"] == Decimal("2000")
    assert result["cash_flows"] == Decimal("1000")
    assert result["net_pnl"] == Decimal("10161.09425")
    assert result["gross_pnl"] == Decimal("11000")
    assert result["gross_return_pct"] == Decimal("11")


@pytest.mark.parametrize("defect", ["unverified", "missing-ref"])
def test_unproven_corporate_action_cannot_be_silently_applied(defect: str) -> None:
    event = action("cash", "20260916", "1")
    event["evidence_verified" if defect == "unverified" else "evidence_ref"] = False if defect == "unverified" else ""
    with pytest.raises(ValueError):
        producer.calculate_costs("100", "110", actions=[event])


def test_corporate_action_window_is_independent_for_each_horizon() -> None:
    row = signal()
    row["actions"] = [action("cash", "20260925", "1")]
    evaluations, positions = replay([row], horizons=(5, 10))
    assert len(evaluations) == 2
    assert len(positions) == 6
    assert {position["status"] for position in positions} == {"realized"}
    d5, d10 = base_positions(positions, 5)[0], base_positions(positions, 10)[0]
    assert d5["entry_date"] == d10["entry_date"] == "20260914"
    assert d5["exit_date"] == "20260921"
    assert d10["exit_date"] == "20260928"
    assert Decimal(d5["cash_flows"]) == 0
    assert Decimal(d5["net_pnl"]) == Decimal("9161.09425")
    assert Decimal(d10["cash_flows"]) == 1000
    assert Decimal(d10["net_pnl"]) == Decimal("10161.09425")


@pytest.mark.parametrize("reverse_input", [False, True])
def test_same_day_cash_and_split_without_sequence_proof_fail_closed(reverse_input: bool) -> None:
    actions = [action("cash", "20260916", "1"), action("share_factor", "20260916", "2")]
    if reverse_input:
        actions.reverse()
    with pytest.raises(ValueError):
        producer.calculate_costs("100", "55", actions=actions)
    row = signal()
    row["actions"] = actions
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert len(positions) == 3
    assert {position["status"] for position in positions} == {"open_unresolved_exit"}
    assert all(not position.get("net_return_pct") for position in positions)


@pytest.mark.parametrize("cash_first", [False, True])
@pytest.mark.parametrize("reverse_input", [False, True])
def test_same_day_corporate_actions_follow_verified_sequence_not_input_order(cash_first, reverse_input) -> None:
    cash = action("cash", "20260916", "1")
    split = action("share_factor", "20260916", "2")
    cash.update(sequence=1 if cash_first else 2, sequence_evidence_ref="synthetic-sequence/cash")
    split.update(sequence=2 if cash_first else 1, sequence_evidence_ref="synthetic-sequence/split")
    actions = [cash, split]
    if reverse_input:
        actions.reverse()
    expected_cash = Decimal("1000" if cash_first else "2000")
    expected_pnl = Decimal("10161.09425" if cash_first else "11161.09425")
    result = producer.calculate_costs("100", "55", actions=actions)
    assert result["final_shares"] == 2000
    assert result["cash_flows"] == expected_cash
    assert result["net_pnl"] == expected_pnl
    row, quote_rows = signal(), prices()
    row["actions"] = actions
    quote_rows[("2330", "20260921")]["close"] = "55"
    _, positions = replay([row], quote_rows=quote_rows)
    assert {position["status"] for position in positions} == {"realized"}
    base = base_positions(positions)[0]
    assert Decimal(base["final_shares"]) == 2000
    assert Decimal(base["cash_flows"]) == expected_cash
    assert Decimal(base["net_pnl"]) == expected_pnl


@pytest.mark.parametrize("defect", ["duplicate", "string", "boolean", "missing-ref"])
def test_same_day_sequence_requires_unique_integers_and_each_evidence_ref(defect: str) -> None:
    cash = action("cash", "20260916", "1")
    split = action("share_factor", "20260916", "2")
    cash.update(sequence=1, sequence_evidence_ref="synthetic-sequence/cash")
    split.update(sequence=2, sequence_evidence_ref="synthetic-sequence/split")
    if defect == "duplicate":
        split["sequence"] = 1
    elif defect == "string":
        cash["sequence"] = "1"
    elif defect == "boolean":
        cash["sequence"] = True
    else:
        split["sequence_evidence_ref"] = ""
    with pytest.raises(ValueError):
        producer.calculate_costs("100", "55", actions=[cash, split])
    row = signal()
    row["actions"] = [cash, split]
    _, positions = replay([row])
    assert len(positions) == 3
    assert {position["status"] for position in positions} == {"open_unresolved_exit"}


def test_immature_position_has_no_realized_return() -> None:
    evaluations, positions = replay([signal()], as_of="20260918")
    assert len(evaluations) == 1
    assert len(positions) == 3
    assert {row["status"] for row in positions} == {"open_immature"}
    assert all(not row.get("net_return_pct") for row in positions)


def test_slippage_sensitivity_preserves_exact_position_set() -> None:
    _, positions = replay([signal("initial"), signal("after", date="20260922")], horizons=(5, 10, 20))
    by_slippage = {
        Decimal(s): {
            (row["event_id"], int(row["horizon"]), row["stock_id"], row["entry_date"], row["exit_date"], row["status"])
            for row in positions if Decimal(str(row["slippage"])) == Decimal(s)
        }
        for s in ("0", "0.001", "0.002")
    }
    assert by_slippage[Decimal("0")]
    assert by_slippage[Decimal("0")] == by_slippage[Decimal("0.001")] == by_slippage[Decimal("0.002")]


def test_unresolved_anomaly_candidate_is_retained_in_primary_positions() -> None:
    row = signal()
    row["anomaly_candidate"] = True
    row["anomaly_disposition"] = "unresolved_anomaly_candidate"
    row["observation_ids"] = ["synthetic-unresolved-observation"]
    evaluations, positions = replay([row])
    assert len(evaluations) == 1
    assert len(positions) == 3
    assert {position["status"] for position in positions} == {"realized"}
    assert all(position["anomaly_candidate"] == "True" for position in positions)
    assert all(position["retained_in_primary"] == "True" for position in positions)
    assert all("synthetic-unresolved-observation" in position["observation_ids"] for position in positions)


def test_summary_uses_realized_positions_and_keeps_anomaly_candidates_in_primary() -> None:
    stocks = ("2330", "2317", "2454", "2303", "2603")
    signals = [signal(f"signal-{stock}", stock) for stock in stocks]
    signals[0]["anomaly_candidate"] = True
    signals[0]["anomaly_disposition"] = "unresolved_anomaly_candidate"
    evaluations, positions = replay(signals, quote_rows=prices(stocks))
    # 這是摘要函式的獨立輸入 fixture，不將人造回報冒充成本回放的產出。
    returns = {"2330": "20", "2317": "-10", "2454": "0", "2303": "5"}
    for position in positions:
        stock = position["stock_id"]
        if stock == "2603":
            position.update(status="open_immature", net_return_pct="", net_pnl="", outcome="")
        else:
            outcome = {"2330": "win", "2317": "loss", "2454": "neutral", "2303": "win"}[stock]
            position.update(net_return_pct=Decimal(returns[stock]), net_pnl=Decimal(returns[stock]), outcome=outcome)
    summaries = producer.summarize(evaluations, positions, signal_count=len(signals))
    base = {
        row["analysis_population"]: row for row in summaries
        if int(row["horizon"]) == 5 and Decimal(str(row["slippage"])) == Decimal("0.001")
    }
    assert set(base) == {"primary", "excluding_anomaly_candidates_sensitivity"}
    primary = base["primary"]
    expected = {
        "position_count": 5, "realized_count": 4, "immature_count": 1, "unresolved_count": 0,
        "win_count": 2, "neutral_count": 1, "loss_count": 1,
        "win_rate_pct": 50, "neutral_rate_pct": 25, "loss_rate_pct": 25,
        "average_net_return_pct": "3.75", "median_net_return_pct": "2.5", "tail_loss_pct": -10,
        "high_return_hit_count": 1, "high_return_hit_rate_pct": 25,
        "major_loss_count": 1, "major_loss_rate_pct": 25,
    }
    for field, value in expected.items():
        assert Decimal(str(primary[field])) == Decimal(str(value)), field
    sensitivity = base["excluding_anomaly_candidates_sensitivity"]
    assert sensitivity["position_count"] == 4
    assert sensitivity["realized_count"] == 3
    assert sensitivity["immature_count"] == 1
    assert sensitivity["win_count"] == sensitivity["neutral_count"] == sensitivity["loss_count"] == 1
    assert sensitivity["high_return_hit_count"] == 0
    assert Decimal(str(sensitivity["median_net_return_pct"])) == 0


def test_summary_does_not_report_zero_performance_when_no_positions_are_realized() -> None:
    evaluations, positions = replay([signal()], as_of="20260918")
    summaries = producer.summarize(evaluations, positions, signal_count=1)
    assert summaries
    for row in summaries:
        assert row["realized_count"] == 0
        for field in (
            "win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "average_net_return_pct",
            "median_net_return_pct", "tail_loss_pct", "high_return_hit_rate_pct", "major_loss_rate_pct",
        ):
            assert row[field] == "", field


def test_summary_counts_open_unresolved_separately_from_realized_and_immature() -> None:
    quote_rows = prices()
    del quote_rows[("2330", "20260921")]
    evaluations, positions = replay([signal()], quote_rows=quote_rows)
    summaries = producer.summarize(evaluations, positions, signal_count=1)
    for row in summaries:
        if int(row["horizon"]) == 5:
            assert row["position_count"] == 1
            assert row["realized_count"] == 0
            assert row["immature_count"] == 0
            assert row["unresolved_count"] == 1


def test_all_formal_use_flags_remain_false_even_with_verified_synthetic_trade() -> None:
    events = producer.merge_signals([signal()])
    evaluations, positions = producer.replay_events(events, CALENDAR, prices(), "20261016", horizons=(5,))
    assert len(positions) == 3
    summaries = producer.summarize(evaluations, positions, signal_count=1)
    for row in [*evaluations, *positions, *summaries]:
        for flag in FORMAL_FLAGS:
            assert row[flag] == "False", (flag, row)


@pytest.mark.parametrize(
    ("closing", "outcome", "high_hit", "major_loss"),
    [("110", "win", "False", "False"), ("100", "loss", "False", "False"),
     ("120", "win", "True", "False"), ("80", "loss", "False", "True")],
)
def test_realized_outcomes_and_return_groups_follow_net_not_gross(closing, outcome, high_hit, major_loss) -> None:
    quote_rows = prices()
    quote_rows[("2330", "20260921")]["close"] = closing
    _, positions = replay([signal()], quote_rows=quote_rows)
    position = base_positions(positions)[0]
    assert position["status"] == "realized"
    assert position["outcome"] == outcome
    assert position["high_return_hit"] == high_hit
    assert position["major_loss"] == major_loss


def test_replay_does_not_mutate_signal_or_price_input() -> None:
    signals, quote_rows = [signal()], prices()
    before_signals, before_prices = deepcopy(signals), deepcopy(quote_rows)
    replay(signals, quote_rows=quote_rows)
    assert signals == before_signals
    assert quote_rows == before_prices


PROTECTED_FIXTURE = "protected/family/base.csv"


def fixture_git(root: Path, *arguments: str, input_text: str | None = None) -> str:
    return subprocess.run(
        ["git", *arguments], cwd=root, input=input_text, check=True,
        capture_output=True, text=True, encoding="utf-8",
    ).stdout.strip()


def fixture_commit(root: Path, message="synthetic fixture") -> None:
    fixture_git(
        root, "-c", "user.name=Synthetic Fixture", "-c", "user.email=fixture@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", message,
    )


def seven_payloads() -> dict[str, bytes]:
    prefix = "output/research/tdcc_stealth_accumulation/tdcc_stealth_accumulation_operation_replay_"
    names = (
        "signals_v3.csv", "events_v3.csv", "positions_v3.csv", "summary_v3.csv",
        "evidence_v3.csv", "manifest_v3.json", "report_v3.md",
    )
    return {prefix + name: ("synthetic:" + name + "\n").encode("utf-8") for name in names}


@pytest.fixture
def sparse_guard_repo(tmp_path, monkeypatch):
    """全部 Git／刪檔操作只作用於 pytest 自動管理的全新暫存 repo。"""
    root = tmp_path / "operation-replay-guard"
    root.mkdir()
    extra_config = {
        "core.autocrlf": "false", "core.safecrlf": "false", "core.longpaths": "true",
        "core.hooksPath": str(root / "disabled-fixture-hooks"), "safe.directory": root.as_posix(),
    }
    count = int(os.environ.get("GIT_CONFIG_COUNT", "0"))
    for offset, (key, value) in enumerate(extra_config.items(), count):
        monkeypatch.setenv(f"GIT_CONFIG_KEY_{offset}", key)
        monkeypatch.setenv(f"GIT_CONFIG_VALUE_{offset}", value)
    monkeypatch.setenv("GIT_CONFIG_COUNT", str(count + len(extra_config)))
    fixture_git(root, "init", "--quiet")
    protected = root / PROTECTED_FIXTURE
    protected.parent.mkdir(parents=True)
    protected.write_bytes(b"original-protected-bytes\n")
    (root / "ordinary.txt").write_bytes(b"original ordinary bytes\n")
    (root / ".gitignore").write_bytes(b"protected/family/ignored*.csv\n")
    fixture_git(root, "add", "--", ".gitignore", "ordinary.txt", PROTECTED_FIXTURE)
    fixture_commit(root)
    fixture_git(root, "config", "core.sparseCheckout", "true")
    sentinels = [SimpleNamespace(sentinel_id="synthetic-family", artifact_glob="protected/family/*.csv", required=True)]
    ownership = [
        SimpleNamespace(
            owner_model_id=producer.OWNER_ID, producer=producer.PRODUCER,
            artifact_glob=path, change_policy="model_owned_write",
        )
        for path in seven_payloads()
    ]
    monkeypatch.setattr(producer, "load_protected_sentinels", lambda _path: sentinels)
    monkeypatch.setattr(producer, "load_ownership_rules", lambda _path: ownership)
    return root, sentinels


def test_sparse_snapshot_binds_tree_index_and_physical_bytes_independently(sparse_guard_repo) -> None:
    root, sentinels = sparse_guard_repo
    snapshot = producer.protected_snapshot(root, sentinels)
    assert set(snapshot) == {"git_tree_blob_mapping", "git_index_blob_mapping", "physical_sha256"}
    assert set(snapshot["git_tree_blob_mapping"]) == {PROTECTED_FIXTURE}
    assert set(snapshot["git_index_blob_mapping"]) == {PROTECTED_FIXTURE}
    assert snapshot["physical_sha256"] == {PROTECTED_FIXTURE: hashlib.sha256(b"original-protected-bytes\n").hexdigest()}
    # 合法 sparse 未 materialize 只保留 Git 證據，不虛報已檢查實體檔案。
    fixture_git(root, "update-index", "--skip-worktree", "--", PROTECTED_FIXTURE)
    (root / PROTECTED_FIXTURE).unlink()
    sparse = producer.protected_snapshot(root, sentinels)
    assert sparse["git_tree_blob_mapping"] == snapshot["git_tree_blob_mapping"]
    assert sparse["git_index_blob_mapping"] == snapshot["git_index_blob_mapping"]
    assert sparse["physical_sha256"] == {}


def test_sparse_guard_detects_skip_worktree_physical_mutation(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    fixture_git(root, "update-index", "--skip-worktree", "--", PROTECTED_FIXTURE)
    assert fixture_git(root, "status", "--porcelain") == ""
    with pytest.raises(RuntimeError, match="protected sentinel.*drift"):
        with producer.artifact_guard(root):
            (root / PROTECTED_FIXTURE).write_bytes(b"hidden mutation\n")
            assert fixture_git(root, "status", "--porcelain") == ""


def test_sparse_guard_detects_new_ignored_file_in_protected_family(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    ignored = root / "protected/family/ignored_new.csv"
    with pytest.raises(RuntimeError, match="protected sentinel.*drift"):
        with producer.artifact_guard(root):
            ignored.write_bytes(b"ignored but protected\n")
            assert fixture_git(root, "status", "--porcelain") == ""


def test_sparse_guard_detects_physical_deletion_hidden_by_skip_worktree(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    fixture_git(root, "update-index", "--skip-worktree", "--", PROTECTED_FIXTURE)
    with pytest.raises(RuntimeError, match="protected sentinel.*drift"):
        with producer.artifact_guard(root):
            (root / PROTECTED_FIXTURE).unlink()
            assert fixture_git(root, "status", "--porcelain") == ""


def test_sparse_guard_detects_index_only_blob_replacement(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    blob = fixture_git(root, "hash-object", "-w", "--stdin", input_text="changed index bytes\n")
    before = (root / PROTECTED_FIXTURE).read_bytes()
    with pytest.raises(RuntimeError, match="protected sentinel.*drift"):
        with producer.artifact_guard(root):
            fixture_git(root, "update-index", "--cacheinfo", f"100644,{blob},{PROTECTED_FIXTURE}")
    assert (root / PROTECTED_FIXTURE).read_bytes() == before


def test_sparse_guard_detects_protected_index_addition_without_physical_file(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    blob = fixture_git(root, "hash-object", "-w", "--stdin", input_text="new protected index bytes\n")
    new_path = "protected/family/index_only.csv"
    with pytest.raises(RuntimeError, match="protected sentinel.*drift"):
        with producer.artifact_guard(root):
            fixture_git(root, "update-index", "--add", "--cacheinfo", f"100644,{blob},{new_path}")
    assert not (root / new_path).exists()


def test_required_protected_family_absent_from_git_and_disk_fails_closed(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    missing = [SimpleNamespace(sentinel_id="synthetic-missing", artifact_glob="missing/*.csv", required=True)]
    with pytest.raises(RuntimeError, match="required protected sentinel family missing from Git and disk"):
        producer.protected_snapshot(root, missing)


def test_sparse_guard_rejects_family_removed_from_head_index_and_disk(sparse_guard_repo) -> None:
    root, _ = sparse_guard_repo
    with pytest.raises(RuntimeError, match="required protected sentinel family missing from Git and disk"):
        with producer.artifact_guard(root):
            fixture_git(root, "rm", "--quiet", "--", PROTECTED_FIXTURE)
            fixture_commit(root, "remove only synthetic protected fixture")
    assert not (root / PROTECTED_FIXTURE).exists()


@pytest.mark.parametrize("build_raises", [False, True])
def test_main_guard_encloses_build_stage_and_rejects_out_of_scope_write(sparse_guard_repo, monkeypatch, build_raises) -> None:
    root, _ = sparse_guard_repo

    def fake_build(*_args):
        (root / "ordinary.txt").write_bytes(b"out-of-scope build-stage write\n")
        if build_raises:
            raise ValueError("synthetic build error after forbidden write")
        return seven_payloads()

    monkeypatch.setattr(producer, "build", fake_build)
    with pytest.raises(RuntimeError, match="unregistered artifact change: ordinary.txt"):
        producer.main(["--repository-root", str(root)])


@pytest.mark.parametrize("defect", ["missing", "extra"])
def test_main_rejects_any_payload_set_other_than_exact_seven(sparse_guard_repo, monkeypatch, defect) -> None:
    root, _ = sparse_guard_repo
    payloads = seven_payloads()
    if defect == "missing":
        payloads.pop(next(iter(payloads)))
    else:
        payloads["output/research/tdcc_stealth_accumulation/tdcc_stealth_accumulation_operation_replay_extra_v3.csv"] = b"not approved\n"
    monkeypatch.setattr(producer, "build", lambda *_args: payloads)
    with pytest.raises(RuntimeError, match="exactly the seven v3 artifacts"):
        producer.main(["--repository-root", str(root)])
    assert not (root / "output").exists()


def test_main_accepts_exact_seven_with_actual_sparse_guard(sparse_guard_repo, monkeypatch) -> None:
    root, sentinels = sparse_guard_repo
    payloads = seven_payloads()
    before = producer.protected_snapshot(root, sentinels)
    monkeypatch.setattr(producer, "build", lambda *_args: payloads)
    assert producer.main(["--repository-root", str(root)]) == 0
    assert {path.relative_to(root).as_posix() for path in (root / "output").rglob("*") if path.is_file()} == set(payloads)
    for path, expected in payloads.items():
        assert (root / path).read_bytes() == expected
    assert producer.protected_snapshot(root, sentinels) == before


def test_identical_verified_cash_action_must_not_be_counted_twice() -> None:
    action = {"event_date": "20260916", "kind": "cash", "cash_per_share": "1",
              "evidence_verified": True, "evidence_ref": "synthetic:cash-entitlement"}
    with pytest.raises(ValueError, match="duplicate corporate action"):
        producer.calculate_costs("100", "110", actions=[action, deepcopy(action)])
    row = signal()
    row["actions"] = [action, deepcopy(action)]
    _, positions = replay([row])
    assert {position["status"] for position in positions} == {"open_unresolved_exit"}


def test_immutable_git_reader_disables_replace_objects(tmp_path, monkeypatch) -> None:
    calls = []

    def capture(argv, **kwargs):
        calls.append(argv)
        return producer.SOURCE_REF + "\n" if "rev-parse" in argv else b"immutable bytes"

    monkeypatch.setattr(producer.subprocess, "check_output", capture)
    source = producer.GitSource(tmp_path, producer.SOURCE_REF, producer.SOURCE_REF)
    assert source.read("fixture.csv") == b"immutable bytes"
    assert len(calls) == 2
    assert all(argv[:2] == ["git", "--no-replace-objects"] for argv in calls)
