"""Independent medium-term audit fixtures; never import the research producer."""
from __future__ import annotations

import ast
import copy
import csv
import gzip
import importlib.util
import io
import json
import sys
from collections import Counter
from datetime import datetime, timedelta
from decimal import Decimal, localcontext
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_tdcc_stealth_accumulation_medium_term_trend_research.py"
sys.path.insert(0, str(ROOT / "scripts"))


@pytest.fixture(scope="module")
def audit():
    spec = importlib.util.spec_from_file_location("medium_term_independent_audit_test", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def contract(audit):
    return json.loads((ROOT / audit.CONTRACT_FILE).read_bytes())


def csv_bytes(fields, rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in fields})
    return stream.getvalue().encode("utf-8")


def packed(audit, kind, rows):
    payload = csv_bytes(audit.SCHEMAS[kind], rows)
    return gzip.compress(payload, mtime=0) if kind in audit.GZIP_KINDS else payload


def dates_from(offsets, start="20250815"):
    origin = datetime.strptime(start, "%Y%m%d")
    return [(origin + timedelta(days=offset)).strftime("%Y%m%d") for offset in offsets]


def weekly_fixture(dates, values=None, stock="1111"):
    values = values or list(range(len(dates)))
    return {day: {stock: {"p400": Decimal(40) + Decimal(str(value)), "p1000": Decimal(20) + Decimal(str(value)),
                          "path": "private/" + day + ".csv", "sha256": "a" * 64}}
            for day, value in zip(dates, values)}


def quote(date, stock="1111", close=100.0):
    return dict(stock_id=stock, stock_name="合成測試", market="TWSE", date=date,
                open=100.0, high=max(101.0, close), low=min(99.0, close), close=close,
                volume=1000000.0, trading_value=100000000.0, source="OFFICIAL",
                source_path="data/daily_price/" + date + ".csv", source_sha256="b" * 64,
                duplicate_key=False, date_mismatch=False, alias_payload_conflict=False)


def feature(date, *, supported8=True, supported12=True, selected4=True, selected8=True, selected12=True, stock="1111"):
    return dict(feature_id=date + ":" + stock, signal_date=date, stock_id=stock, stock_name="合成測試", market="TWSE",
                history_gap_count=0, price_qualified=True, baseline_4_supported=True, baseline_4_selected=selected4,
                w8_supported=supported8, w8_selected=selected8, w12_supported=supported12, w12_selected=selected12)


class Quotes:
    def __init__(self, rows=None):
        self.rows = rows or {}

    def daily(self, date):
        return self.rows.get(date, {}), {}


def trade(date, value, *, horizon=20, slip=10, profile="full_available", strategy="trend_8", stock="1111", partition="training"):
    return dict(profile=profile, strategy=strategy, partition=partition, feature_id=date + ":" + stock,
                signal_date=date, stock_id=stock, horizon=horizon, slippage_bps=slip,
                entry_date=date, exit_date=date, net_return_pct=str(value), anomaly_candidate=False)


def test_validator_imports_only_technical_prior_validator_io():
    tree = ast.parse(VALIDATOR.read_text(encoding="utf-8"))
    permitted_prior = {"annual_io": {"FEATURE_FIELDS", "SCHEMAS", "GitReader", "CONTRACT_FILE", "APPROVED_CONTRACT_SHA256", "artifact_name", "PrivateInputs", "CurrentPrices", "csv_records", "rows_for"},
                       "horizon_io": {"PublishedPrices"}}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert not any("build_tdcc" in alias.name for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            assert "build_tdcc" not in (node.module or "")
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in permitted_prior:
            assert node.attr in permitted_prior[node.value.id]
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "compile", "__import__"}


def test_frozen_contract_bytes_and_exact_eleven(audit, contract):
    payload = (ROOT / audit.CONTRACT_FILE).read_bytes()
    assert audit.digest(payload) == audit.APPROVED_CONTRACT_SHA256
    assert payload == audit.canonical_json(contract)
    assert len(audit.KINDS) == 11
    assert audit.contract_audit(contract) is None


@pytest.mark.parametrize("field,value", [("split_date", "20260402"), ("formal_use", True), ("price_source_ref", "0" * 40),
                                         ("genuine_unseen_oos", True), ("feature_contrast_policy", "low<0"),
                                         ("anomaly_policy", "remove IQR outliers from primary")])
def test_contract_mutation_fails_closed(audit, contract, field, value):
    contract[field] = value
    with pytest.raises(ValueError, match="frozen medium-term contract"):
        audit.contract_audit(contract)


def test_actual_date_ols_linear_one_pp_week(audit):
    offsets = [0, 7, 14, 20, 28, 35, 48, 55]
    with localcontext() as ctx:
        ctx.prec = 50
        values = [Decimal(30) + Decimal(day) / 7 for day in offsets]
        result = audit.exact_ols(dates_from(offsets), values)
        assert abs(result["slope"] - 1) < Decimal("1e-45")


@pytest.mark.parametrize("values", [[3] * 8, [1, 2, 3, 4, 4, 3, 2, 1]])
def test_equal_date_zero_is_exact_and_not_selected(audit, values):
    dates = dates_from(range(0, 56, 7))
    result = audit.exact_ols(dates, values)
    assert result["numerator"] == result["slope"] == 0
    window = audit.window_metrics(weekly_fixture(dates, values), dates[-1], "1111", 8, audit.session_calendar([]))
    assert window["supported"] is True and window["selected"] is False


def test_irregular_symmetric_values_are_positive_not_forced_zero(audit):
    dates = dates_from([0, 7, 14, 21, 28, 35, 42, 48])
    result = audit.exact_ols(dates, [1, 2, 3, 4, 4, 3, 2, 1])
    with localcontext() as ctx:
        ctx.prec = 50
        assert result["slope"] == Decimal(84) / Decimal(16079)
    assert result["numerator"] > 0


def test_decimal_small_positive_has_no_epsilon(audit):
    dates = dates_from(range(0, 56, 7))
    result = audit.exact_ols(dates, ["0"] * 7 + ["0.000000000000000000000000000001"])
    assert result["slope"] > 0 and result["numerator"] > 0


@pytest.mark.parametrize("dates,values", [(["20251003"], [1]), (["20251003", "20251003"], [1, 2]),
                                         (["20251009", "20251003"], [1, 2]),
                                         (["20251003", "20251009"], [1]), (["20251003", "20251009"], [1, "NaN"])])
def test_ols_rejects_invalid_or_missing_values(audit, dates, values):
    with pytest.raises(ValueError):
        audit.exact_ols(dates, values)


def test_old_rejects_new_accepts_despite_final_large_decline(audit):
    dates = dates_from(range(0, 56, 7))
    weeks = weekly_fixture(dates, [1, 2, 3, 4, 5, 6, 7, 0])
    old = audit.baseline_four(weeks, dates[-1], "1111")
    new = audit.window_metrics(weeks, dates[-1], "1111", 8, audit.session_calendar([]))
    assert old["supported"] and not old["selected"]
    assert old["delta400"] < 0 and old["delta1000"] < 0
    assert new["supported"] and new["selected"]
    with localcontext() as ctx:
        ctx.prec = 50
        assert Decimal(new["slope400_pp_per_week"]) == Decimal(1) / 3
        assert Decimal(new["slope1000_pp_per_week"]) == Decimal(1) / 3
    assert Decimal(new["last400_pp"]) == -7
    assert Decimal(new["max_positive_share400"]) == Decimal(new["max_positive_share1000"])


def test_no_positive_jump_is_missing_description_not_eligibility(audit):
    dates = dates_from(range(0, 56, 7))
    result = audit.window_metrics(weekly_fixture(dates, [2] * 8), dates[-1], "1111", 8, audit.session_calendar([]))
    assert result["supported"] and not result["selected"]
    assert result["max_positive_share400"] == ""
    assert result["descriptive_missing_reasons"] == "no_positive_change_400;no_positive_change_1000"


@pytest.mark.parametrize("missing_ratio", [False, True])
def test_current_window_missing_stock_or_ratio_cannot_backfill(audit, missing_ratio):
    dates = dates_from(range(0, 63, 7))
    weeks = weekly_fixture(dates)
    if missing_ratio:
        weeks[dates[-3]]["1111"]["p400"] = None
    else:
        del weeks[dates[-3]]["1111"]
    result = audit.window_metrics(weeks, dates[-1], "1111", 8, audit.session_calendar([]))
    assert not result["supported"] and not result["selected"]
    assert result["dates"].split(";") == dates[-8:]
    assert result["missing_batch_dates"] == dates[-3]


def test_six_eight_day_intervals_and_future_mutation_do_not_change_past(audit):
    dates = ["20250822", "20250829", "20250905", "20250912", "20250919", "20250926", "20251003", "20251009", "20251017"]
    weeks = weekly_fixture(dates)
    calendar = audit.session_calendar([])
    past = audit.window_metrics(weeks, "20251016", "1111", 8, calendar)
    assert past["supported"] and past["span_days"] == 48
    weeks["20251017"]["1111"]["p400"] = Decimal(-999)
    assert audit.window_metrics(weeks, "20251016", "1111", 8, calendar) == past
    del weeks["20251017"]
    assert audit.window_metrics(weeks, "20251016", "1111", 8, calendar) == past
    ended = audit.window_metrics(weeks, "20251020", "1111", 8, calendar)
    assert not ended["supported"] and ended["missing_open_weeks"] == "20251013"


def test_full_closed_week_allowed_but_open_week_missing_rejected(audit):
    dates = dates_from([0, 7, 14, 21, 28, 35, 49, 56])
    missing_monday = audit.monday(dates_from([42])[0])
    closures = dates_from(range(5), missing_monday)
    weeks = weekly_fixture(dates)
    assert audit.window_metrics(weeks, dates[-1], "1111", 8, audit.session_calendar(closures))["supported"]
    result = audit.window_metrics(weeks, dates[-1], "1111", 8, audit.session_calendar([]))
    assert not result["supported"] and result["missing_open_weeks"] == missing_monday


def test_outside_calendar_evidence_is_unsupported(audit):
    dates = dates_from(range(0, 56, 7))
    result = audit.window_metrics(weekly_fixture(dates), dates[-1], "1111", 8, audit.session_calendar([]), calendar_start=dates[1])
    assert not result["supported"] and "calendar_evidence_insufficient" in result["reasons"]


def test_signal_after_calendar_end_is_unsupported_even_when_last_batch_inside(audit):
    dates = dates_from(range(0, 56, 7), "20251010")
    assert dates[-1] == "20251128"
    weeks = weekly_fixture(dates)
    calendar = audit.session_calendar([], end="20251128")
    assert audit.window_metrics(weeks, "20251128", "1111", 8, calendar, calendar_end="20251128")["supported"]
    after = audit.window_metrics(weeks, "20251129", "1111", 8, calendar, calendar_end="20251128")
    assert not after["supported"] and "calendar_evidence_insufficient" in after["reasons"]


@pytest.mark.parametrize("mutation,expected", [(dict(volume_ratio="2.5"), "volume_below_2_5"),
                                               (dict(return_5d="8"), "short_not_attacked"),
                                               (dict(return_20d="20"), "not_rallied"),
                                               (dict(close="120"), "in_recent_range_10pct")])
def test_original_price_thresholds_remain_independent_of_tdcc(audit, mutation, expected):
    row = dict(close="100", open="100", high="101", low="99", previous_close="100", volume_ratio="1",
               volume_ma20_lots="1000", previous_20d_high_ex_today="101", daily_return_calc="0",
               return_5d="0", return_20d="0", high_20="101", low_20="99")
    assert audit.price_qualifier(row) == (True, [], False)
    row.update(mutation)
    passed, reasons, _ = audit.price_qualifier(row)
    assert not passed and expected in reasons


def test_price_support_does_not_hide_missing_four_batch_tdcc(audit):
    calendar = audit.session_calendar([])
    date = "20250910"
    position = calendar.index(date)
    history = [quote(day) for day in calendar[position - 20:position + 1]]
    row = audit.derive_price_row(date, "1111", history[-1], history, calendar, {"20250905"}, {"external_files": []}, dict(supported=False, dates=[]))
    assert row["price_supported"] and row["price_qualified"]
    assert not row["feature_supported"] and not row["selected"]
    assert row["unsupported_reasons"] == "tdcc_four_batch_coverage_missing"
    assert row["historical_closed_date_files_excluded"] == "20250905"


def full_universe_fixture(audit, *, published_only=False):
    """Two price-qualified names: the second fails old TDCC but passes slope."""
    date = "20251003"
    dates = dates_from(range(0, 56, 7))
    weeks = weekly_fixture(dates)
    other = weekly_fixture(dates, [1, 2, 3, 4, 5, 6, 7, 0], stock="2222")
    for day in weeks:
        weeks[day].update(other[day])
    calendar = audit.session_calendar(["20250901", "20250902"])
    index = calendar.index(date)
    observed = calendar[index - 20:index + 1]
    quotes = {day: {stock: quote(day, stock) for stock in ("1111", "2222")} for day in observed}
    quotes["20250901"] = {"1111": quote("20250901")}
    original = dict(history_start="20250401", calendar_end="20261030", external_files=[
        dict(kind="tdcc", date=day, path=weeks[day]["1111"]["path"], sha256="a" * 64) for day in dates])
    features = []
    for stock in ("1111", "2222"):
        baseline = audit.baseline_four(weeks, date, stock)
        history = [quotes[day][stock] for day in observed]
        row = audit.derive_price_row(date, stock, quotes[date][stock], history, calendar, {"20250901"}, original, baseline)
        for count in (8, 12):
            row.update({f"w{count}_{key}": value for key, value in audit.window_metrics(weeks, date, stock, count, calendar).items()})
        features.append(row)
    assert features[0]["selected"] is True and features[1]["selected"] is False
    assert all(row["price_qualified"] and row["w8_selected"] for row in features)
    counts = dict(signal_date=date, raw_universe_rows=2, price_supported_rows=2, price_qualified_rows=2,
                  baseline_4_supported_rows=2, baseline_4_signals=1, trend_8_supported_rows=2, trend_8_signals=2,
                  trend_12_supported_rows=0, trend_12_signals=0, common_8_eligible_rows=2, common_12_eligible_rows=0,
                  price_unsupported_reason_counts="{}", trend_8_unsupported_reason_counts="{}",
                  trend_12_unsupported_reason_counts='{"insufficient_market_batches": 2}', possible_tdr_rows=0,
                  formal_use=False, promotion_evidence_allowed=False)
    controls = {kind: gzip.compress(csv_bytes(audit.annual_io.FEATURE_FIELDS, rows), mtime=0)
                for kind, rows in (("features", features), ("signals", features[:1]))}
    context = dict(original=original, calendar=calendar, prices=Quotes(quotes), weeks=weeks, published_only=published_only,
                   controls=controls, price_dates=set(quotes), closures=["20250901", "20250902"],
                   original_manifest={"counts": {"covered_universe_rows": 2, "signals": 1}})
    artifacts = {audit.artifact_name("features"): packed(audit, "features", features),
                 audit.artifact_name("weekly_features"): packed(audit, "weekly_features", list(audit.normalized_weekly(weeks))),
                 audit.artifact_name("coverage"): packed(audit, "coverage", [counts])}
    return context, {"requested_signal_start": date, "requested_signal_end": date}, artifacts, features


@pytest.mark.parametrize("published_only", [False, True])
def test_complete_daily_universe_is_not_old_selected_signal_intersection(audit, published_only):
    context, contract, artifacts, expected = full_universe_fixture(audit, published_only=published_only)
    actual, coverage, counts = audit.audit_features(context, contract, artifacts)
    assert [row["stock_id"] for row in actual] == ["1111", "2222"]
    assert counts["universe_rows"] == counts["price_qualified_rows"] == 2
    assert counts["baseline_4_control_signals"] == 1
    assert coverage[0]["trend_8_signals"] == 2
    # Only an actual closed-date price file is an exclusion; no phantom holiday file.
    assert all(row["historical_closed_date_files_excluded"] == "20250901" for row in expected)


@pytest.mark.parametrize("mutation", ["drop_old_rejected_stock", "reject_old_rejected_stock", "omit_control_stock", "forge_price", "invent_excluded_holiday"])
def test_full_universe_and_raw_price_mutations_fail(audit, mutation):
    context, contract, artifacts, features = full_universe_fixture(audit)
    if mutation == "drop_old_rejected_stock":
        artifacts[audit.artifact_name("features")] = packed(audit, "features", features[:1])
    elif mutation == "reject_old_rejected_stock":
        features[1]["w8_selected"] = False
        artifacts[audit.artifact_name("features")] = packed(audit, "features", features)
    elif mutation == "omit_control_stock":
        context["controls"]["features"] = gzip.compress(csv_bytes(audit.annual_io.FEATURE_FIELDS, features[:1]), mtime=0)
    elif mutation == "forge_price":
        context["prices"].rows["20251003"]["2222"]["close"] = 100.5
    else:
        features[1]["historical_closed_date_files_excluded"] = "20250901;20250902"
        artifacts[audit.artifact_name("features")] = packed(audit, "features", features)
    with pytest.raises(ValueError):
        audit.audit_features(context, contract, artifacts)


@pytest.mark.parametrize("bad_field,bad_value", [("duplicate_key", True), ("date_mismatch", True), ("alias_payload_conflict", True), ("close", -1), ("high", 90)])
def test_invalid_raw_prices_fail_closed(audit, bad_field, bad_value):
    row = quote("20251003")
    row[bad_field] = bad_value
    assert not audit.valid_price(row)


def test_common_profile_has_same_eligible_universe_not_selected_intersection(audit):
    row = feature("20251003", selected4=False, selected8=True, selected12=False)
    assert audit.cohort_decision(row, "common_8", "baseline_4") == (True, True, False)
    assert audit.cohort_decision(row, "common_8", "trend_8") == (True, True, True)
    for strategy in audit.STRATEGIES:
        assert audit.cohort_decision(row, "common_12", strategy)[0]
    row["w12_supported"] = False
    for strategy in audit.STRATEGIES:
        assert not audit.cohort_decision(row, "common_12", strategy)[0]


def test_common_ledger_starts_empty_without_baseline_prestart_lock(audit):
    calendar = audit.session_calendar([])
    days = ["20250910", "20250917"]
    rows = [feature(days[0], supported8=False), feature(days[1])]
    needed = {audit.holding_dates(calendar, day, 20)[field] for day in days for field in ("entry_date", "exit_date")}
    prices = Quotes({day: {"1111": quote(day)} for day in needed})
    full = list(audit.ledger_rows(rows, prices, calendar, "full_available", "baseline_4", 20))
    common4 = list(audit.ledger_rows(rows, prices, calendar, "common_8", "baseline_4", 20))
    common8 = list(audit.ledger_rows(rows, prices, calendar, "common_8", "trend_8", 20))
    assert {row["signal_date"] for kind, row in full if kind == "trades"} == {days[0]}
    assert {row["signal_date"] for kind, row in common4 if kind == "trades"} == {days[1]}
    assert {row["signal_date"] for kind, row in common8 if kind == "trades"} == {days[1]}


@pytest.mark.parametrize("entry,exit_,expected", [("20260331", "20260331", "training"), ("20260331", "20260401", "purged_cross_split"),
                                                ("20260401", "20260428", "validation"), ("20260331", "", "purged_cross_split")])
def test_partition_is_by_entry_date(audit, entry, exit_, expected):
    assert audit.partition(entry, exit_) == expected


def test_signal_before_split_entry_at_split_is_validation(audit):
    calendar = audit.session_calendar([])
    target = audit.holding_dates(calendar, "20260331", 20)
    assert target["entry_date"] == "20260401"
    assert audit.partition(target["entry_date"], target["exit_date"]) == "validation"


def test_purged_position_preserves_chronology_lock_through_exit_day(audit):
    calendar = audit.session_calendar([])
    first = "20260320"
    target = audit.holding_dates(calendar, first, 20)
    next_signal = calendar[calendar.index(target["exit_date"]) + 1]
    signals = [first, "20260401", target["exit_date"], next_signal]
    prices = Quotes({day: {"1111": quote(day)} for day in calendar})
    rows = list(audit.ledger_rows([feature(day) for day in signals], prices, calendar, "common_12", "trend_8", 20))
    realized = [row for kind, row in rows if kind == "trades" and row["slippage_bps"] == 10]
    assert [row["signal_date"] for row in realized] == [first, next_signal]
    assert realized[0]["partition"] == "purged_cross_split" and realized[1]["partition"] == "validation"
    reasons = {row["signal_date"]: row["reasons"] for kind, row in rows if kind == "blocked" and row["record_type"] == "operation_no_entry"}
    assert reasons["20260401"] == "blocked_active_position"
    assert reasons[target["exit_date"]] == "blocked_exit_day"


@pytest.mark.parametrize("missing", ["entry", "exit"])
def test_missing_entry_does_not_lock_but_missing_exit_does(audit, missing):
    calendar = audit.session_calendar([])
    dates = ["20250910", "20250911"]
    targets = [audit.holding_dates(calendar, day, 20) for day in dates]
    values = {day: {"1111": quote(day)} for day in calendar}
    values.pop(targets[0][missing + "_date"])
    rows = list(audit.ledger_rows([feature(day) for day in dates], Quotes(values), calendar, "full_available", "trend_8", 20))
    realized = [row for kind, row in rows if kind == "trades"]
    if missing == "entry":
        assert {row["signal_date"] for row in realized} == {dates[1]}
    else:
        assert not realized
        assert any(row.get("reasons") == "blocked_active_position" for _, row in rows)


def test_horizon_is_exchange_session_offset_and_maturity_checked(audit):
    calendar = audit.session_calendar(["20260406"])
    result = audit.holding_dates(calendar, "20260331", 20)
    assert result["exit_target_index"] == result["entry_index"] + 20
    assert result["exit_date"] == calendar[result["entry_index"] + 20]
    late = audit.holding_dates(calendar, "20260909", 60)
    assert not late["mature"] and late["exit_date"] == ""


@pytest.mark.parametrize("slip", [0, 10, 20])
def test_cashflow_arithmetic_costs_and_slippage(audit, slip):
    result = audit.cashflows("100", "110", slip)
    buy = Decimal(100000) * (1 + Decimal(slip) / 10000)
    sell = Decimal(110000) * (1 - Decimal(slip) / 10000)
    cost = buy + buy * Decimal(".001425")
    proceeds = sell - sell * Decimal(".001425") - sell * Decimal(".003")
    assert Decimal(result["entry_cash"]) == cost
    assert Decimal(result["net_exit_cash"]) == proceeds
    assert Decimal(result["net_pnl"]) == proceeds - cost
    assert Decimal(result["gross_return_pct"]) == 10
    assert result["outcome"] == "win"


def test_minimum_fees_and_zero_price_rejected(audit):
    result = audit.cashflows("1", "1", 0)
    assert Decimal(result["buy_fee"]) == Decimal(result["sell_fee"]) == 20
    assert Decimal(result["net_pnl"]) == -43
    for price in ("0", "-1", "NaN", ""):
        with pytest.raises(ValueError):
            audit.cashflows(price, "100", 10)


@pytest.mark.parametrize("value,expected", [("10", "high"), ("-10", "low"), ("-9.9999", "middle"), ("-0.1", "middle"), ("0", "middle"), ("9.9999", "middle")])
def test_high_low_outcome_groups_keep_frozen_denominator(audit, value, expected):
    assert audit.outcome_group(value) == expected


def test_win_failure_and_payoff_metrics_use_separate_thresholds(audit):
    result = audit.statistics_row([-10, -1, 0, 1, 10])
    assert (result["win_count"], result["neutral_count"], result["failure_count"]) == (2, 1, 2)
    assert result["high_return_ge10_rate_pct"] == result["loss_le_minus10_rate_pct"] == 20
    assert result["mean_net_return_pct"] == result["median_net_return_pct"] == 0
    assert audit.statistics_row([])["mean_net_return_pct"] == ""


def test_iqr_requires_four_inclusive_full_chronology_and_strict_fences(audit):
    assert audit.anomaly_detections([trade("20260101", 0), trade("20260102", 0), trade("20260103", 999)]) == []
    rows = [trade(f"202601{index + 1:02d}", value, partition="purged_cross_split" if index == 4 else "training")
            for index, value in enumerate([0, 0, 0, 0, 100])]
    found = audit.anomaly_detections(rows)
    assert len(found) == 1 and found[0]["signal_date"] == "20260105"
    assert found[0]["q1"] == found[0]["q3"] == found[0]["lower_fence"] == found[0]["upper_fence"] == 0
    assert not audit.anomaly_detections([dict(row, slippage_bps=0) for row in rows])
    at_fence = [trade(f"202601{index + 1:02d}", value) for index, value in enumerate([0, 0, 1, 1, 4])]
    assert not audit.anomaly_detections(at_fence)
    at_fence[-1]["net_return_pct"] = "4.00000001"
    assert len(audit.anomaly_detections(at_fence)) == 1


def test_prior_union_is_exact_horizon_and_all_slippages_remain_primary(audit):
    rows = [trade("20260101", 30, slip=slip) for slip in audit.SLIPPAGES]
    rows += [trade("20260101", 30, horizon=60)]
    prior = {("20260101", "1111", 20), ("20250101", "2222", 20)}
    anomalies = audit.anomaly_rows(rows, prior, {})
    assert [row["anomaly_candidate"] for row in rows] == [True, True, True, False]
    assert len(anomalies) == 1 and anomalies[0]["primary_row_retained"] is True
    assert anomalies[0]["disposition"] == "unresolved_anomaly_candidate"
    assert anomalies[0]["reason"] == "immutable_previous_candidate_retained"


def test_new_candidate_union_crosses_profile_strategy_not_horizon(audit):
    cause = dict(signal_date="20260101", stock_id="1111", horizon=20, detector_profile="full_available",
                 detector_strategy="trend_8", q1=0, q3=1, lower_fence=-3, upper_fence=4)
    rows = [trade("20260101", 100, profile="common_12", strategy="baseline_4", slip=slip) for slip in audit.SLIPPAGES]
    rows.append(trade("20260101", 100, profile="common_12", strategy="baseline_4", horizon=60))
    anomalies = audit.anomaly_rows(rows, set(), {("20260101", "1111", 20): [cause]})
    assert [row["anomaly_candidate"] for row in rows] == [True, True, True, False]
    assert len(anomalies) == 1 and anomalies[0]["profile"] == "common_12"
    assert anomalies[0]["detector_profile"] == "full_available"
    assert anomalies[0]["detector_strategy"] == "trend_8"


def test_summary_retains_unresolved_primary_and_labels_exclusion_only_sensitivity(audit):
    rows = [trade("20260101", -100), trade("20260102", 10)]
    rows[0]["anomaly_candidate"] = True
    summary = audit.summaries(rows, Counter(), [], audit.session_calendar([]), "common_12", "trend_8")
    selected = {row["population"]: row for row in summary if row["horizon"] == 20 and row["slippage_bps"] == 10 and row["partition"] == "all"}
    assert selected["primary"]["samples"] == 2
    assert selected["primary"]["mean_net_return_pct"] == -45
    assert selected["primary"]["anomaly_candidate_positions"] == 1
    assert selected["sensitivity_excluding_candidates"]["samples"] == 1
    assert selected["sensitivity_excluding_candidates"]["mean_net_return_pct"] == 10


def test_empty_profile_ledgers_and_summaries_stay_explicit(audit):
    calendar = audit.session_calendar([])
    assert list(audit.ledger_rows([], Quotes(), calendar, "common_12", "trend_12", 20)) == []
    summary = audit.summaries([], Counter(), [], calendar, "common_12", "trend_12")
    assert len(summary) == 2 * 3 * 4 * 2
    assert all(row["samples"] == 0 and row["mean_net_return_pct"] == "" for row in summary)
    assert all(row["formal_use"] is False and row["promotion_evidence_allowed"] is False for row in summary)


def test_feature_contrast_sensitivity_excludes_only_immutable_prior(audit, monkeypatch):
    monkeypatch.setattr(audit, "CONTRAST_FIELDS", ("w8_slope400_pp_per_week",))
    rows = [trade("20260101", -10), trade("20260102", -1), trade("20260103", 10)]
    for row in rows:
        row["anomaly_candidate"] = True
    by_id = {row["feature_id"]: {"w8_slope400_pp_per_week": str(index)} for index, row in enumerate(rows)}
    contrasts = list(audit.feature_contrasts(rows, by_id, {audit.anomaly_key(rows[0])}, "full_available", "trend_8"))
    subset = {(row["population"], row["outcome_group"]): row for row in contrasts if row["horizon"] == 20 and row["slippage_bps"] == 10 and row["partition"] == "all"}
    assert subset["primary", "all_realized"]["samples"] == 3
    assert subset["primary", "low"]["samples"] == 1
    assert subset["primary", "middle"]["samples"] == 1
    assert subset["immutable_prior_candidate_exclusion_sensitivity", "all_realized"]["samples"] == 2


def test_exact_schema_bom_crlf_missing_newline_and_width_rejected(audit):
    fields = audit.SCHEMAS["coverage"]
    good = csv_bytes(fields, [dict.fromkeys(fields, "0")])
    assert len(list(audit.records("coverage", good))) == 1
    variants = [b"\xef\xbb\xbf" + good, good.replace(b"\n", b"\r\n"), good.rstrip(b"\n"), good.replace(b"signal_date,", b"date,"), good + b"extra,wide,row\n"]
    for payload in variants:
        with pytest.raises((ValueError, csv.Error)):
            list(audit.records("coverage", payload))


def test_row_counts_and_numerators_are_exact_not_tolerated_statistics(audit):
    expected = dict.fromkeys(audit.SCHEMAS["features"], "")
    expected["w8_numerator400"] = "0.000000000000000000001"
    actual = dict(expected, w8_numerator400="0")
    with pytest.raises(ValueError, match="numerator400"):
        audit.compare_row("features", actual, expected)
    with pytest.raises(ValueError, match="missing expected"):
        audit.compare_sequence("features", [], [expected])
    with pytest.raises(ValueError, match="unexpected extra"):
        audit.compare_sequence("features", [expected], [])


def test_normalized_offsets_accept_only_exact_decimal_equivalence(audit):
    dates = dates_from(range(0, 63, 7), "20251003")
    weeks = weekly_fixture(dates)
    weeks[dates[0]]["1111"].update(p400=Decimal("40.0000"), p1000=Decimal("20.0000"))
    normalized = {day: {"1111": dict(values["1111"], p400=values["1111"]["p400"] - Decimal("40.0000"),
                                    p1000=values["1111"]["p1000"] - Decimal("20.0000"))} for day, values in weeks.items()}
    raw = audit.window_metrics(weeks, dates[-1], "1111", 8, audit.session_calendar([]))
    derived = audit.window_metrics(normalized, dates[-1], "1111", 8, audit.session_calendar([]))
    assert raw["net400_pp"] == "7" and derived["net400_pp"] == "7.0000"
    assert raw["numerator400"] == "2352" and derived["numerator400"] == "2352.0000"
    expected = {f"w8_{field}": value for field, value in raw.items()}
    actual = {f"w8_{field}": value for field, value in derived.items()}
    audit.compare_row("features", actual, expected)
    for field in audit.WINDOW_DECIMAL_FIELDS:
        expected, actual = {field: "0.1000"}, {field: "0.1"}
        audit.compare_row("features", actual, expected)
        actual[field] = "0.10000000000000000001"
        with pytest.raises(ValueError, match=field):
            audit.compare_row("features", actual, expected)
        actual[field] = ""
        with pytest.raises(ValueError, match=field):
            audit.compare_row("features", actual, expected)


def test_weekly_normalized_offsets_bind_sources_and_no_private_absolutes(audit):
    weeks = weekly_fixture(["20251003", "20251009"], [0, 1])
    source = {"external_files": [dict(kind="tdcc", date=date, path=values["1111"]["path"], sha256="a" * 64) for date, values in weeks.items()]}
    rows = list(audit.normalized_weekly(weeks))
    assert rows[0]["offset400_pp"] == rows[0]["offset1000_pp"] == "0"
    assert rows[1]["offset400_pp"] == "1"
    published = audit.published_weeks(packed(audit, "weekly_features", rows), source)
    assert published["20251003"]["1111"]["p400"] == 0
    for field, value, error in (("source_sha256", "f" * 64, "SHA/path"), ("anchor_date", "20251009", "anchor"),
                                ("offset400_pp", "1", "zero offsets"), ("formal_use", True, "research-only")):
        bad = copy.deepcopy(rows)
        bad[0][field] = value
        with pytest.raises(ValueError, match=error):
            audit.published_weeks(packed(audit, "weekly_features", bad), source)
    with pytest.raises(ValueError, match="omit an entire"):
        audit.published_weeks(packed(audit, "weekly_features", rows[:1]), source)


def test_complete_and_incomplete_weekly_rows_cannot_fill_gaps(audit):
    weeks = weekly_fixture(["20251003", "20251009"], [0, 1])
    weeks["20251003"]["1111"]["p400"] = None
    original = {"external_files": [dict(kind="tdcc", date=date, path=values["1111"]["path"], sha256="a" * 64) for date, values in weeks.items()]}
    rows = list(audit.normalized_weekly(weeks))
    assert rows[0]["anchor_date"] == rows[0]["offset400_pp"] == ""
    assert rows[1]["anchor_date"] == "20251009" and rows[1]["offset400_pp"] == "0"
    audit.published_weeks(packed(audit, "weekly_features", rows), original)
    rows[0]["offset400_pp"] = "0"
    with pytest.raises(ValueError, match="cannot fill"):
        audit.published_weeks(packed(audit, "weekly_features", rows), original)


def raw_fixture(audit, *, mutation=""):
    rows = [{"日期": "2025-10-03", "股票代碼": "1111", "持股分級": level, "比例": value}
            for level, value in zip(audit.LEVELS, ["5.0001", "6.0002", "7.0003", "20.0004"])]
    if mutation == "missing_bin":
        rows.pop(0)
    elif mutation == "duplicate_bin":
        rows.append(dict(rows[0]))
    elif mutation == "wrong_date":
        rows[0]["日期"] = "2025-10-09"
    elif mutation == "invalid_ratio":
        rows[0]["比例"] = "999"
    payload = csv_bytes(["日期", "股票代碼", "持股分級", "比例"], rows)
    item = dict(kind="tdcc", date="20251003", path="private/20251003.csv", sha256=audit.digest(payload), rows=len(rows))
    original = dict(external_files=[item], expected_tdcc_weeks=1, expected_tdcc_rows=len(rows))
    class Inputs:
        def read(self, request):
            assert request == item
            return payload
    return Inputs(), original


def test_raw_tdcc_sums_decimal_bands_without_filling_missing(audit):
    inputs, original = raw_fixture(audit)
    result = audit.raw_tdcc(inputs, original)["20251003"]["1111"]
    assert result["p400"] == Decimal("38.0010") and result["p1000"] == Decimal("20.0004")
    inputs, original = raw_fixture(audit, mutation="missing_bin")
    assert audit.raw_tdcc(inputs, original)["20251003"]["1111"]["p400"] is None


@pytest.mark.parametrize("mutation,expected", [("duplicate_bin", "duplicate"), ("wrong_date", "effective date"), ("invalid_ratio", "structural invariant")])
def test_raw_tdcc_schema_identity_and_ratio_invariants(audit, mutation, expected):
    inputs, original = raw_fixture(audit, mutation=mutation)
    with pytest.raises(ValueError, match=expected):
        audit.raw_tdcc(inputs, original)


def test_raw_tdcc_expected_counts_are_not_advisory(audit):
    inputs, original = raw_fixture(audit)
    original["expected_tdcc_rows"] += 1
    with pytest.raises(ValueError, match="total week/row"):
        audit.raw_tdcc(inputs, original)


def test_manifest_serialized_hash_and_owner_mutations_fail_before_source_io(audit, contract, monkeypatch):
    def no_source(*args, **kwargs):
        raise AssertionError("source IO must not run before envelope checks")
    monkeypatch.setattr(audit, "load_context", no_source)
    artifacts = {audit.artifact_name(kind): b"synthetic\n" for kind in audit.KINDS}
    manifest = dict(model_id="tdcc_stealth_accumulation", owner_id=audit.OWNER, artifact_version=audit.PREFIX + "v1", contract=contract,
                    contract_file=audit.CONTRACT_FILE, contract_sha256=audit.APPROVED_CONTRACT_SHA256,
                    hashes={name: dict(bytes=len(payload), sha256=audit.digest(payload)) for name, payload in artifacts.items() if name != audit.artifact_name("source_manifest")},
                    **dict.fromkeys(audit.FALSE_FLAGS, False))
    for field, value, expected in (("owner_id", "rogue", "owner/contract"), ("formal_use", True, "owner/contract"),
                                   ("hashes", {}, "serialized ten-file hashes")):
        changed = dict(manifest, **{field: value})
        artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(changed)
        assert expected in " ".join(audit.validate_artifacts(ROOT, contract, artifacts, published_only=True))
    artifacts[audit.artifact_name("source_manifest")] = audit.canonical_json(manifest).replace(b"\n", b"\r\n")
    assert "canonical JSON" in " ".join(audit.validate_artifacts(ROOT, contract, artifacts, published_only=True))


def test_source_mode_never_falls_back_to_public_without_explicit_flag(audit, contract):
    artifacts = {audit.artifact_name(kind): b"" for kind in audit.KINDS}
    assert "requires --input-root" in " ".join(audit.validate_artifacts(ROOT, contract, artifacts))
    artifacts.pop(audit.artifact_name("features"))
    assert "exact eleven" in " ".join(audit.validate_artifacts(ROOT, contract, artifacts, published_only=True))


@pytest.mark.parametrize("missing_kind", ["source_manifest", "weekly_features", "features", "signals", "trades", "blocked", "coverage", "summary", "feature_contrasts", "anomalies", "report"])
def test_each_published_artifact_missing_is_failure_not_skip(audit, tmp_path, missing_kind):
    for kind in audit.KINDS:
        if kind != missing_kind:
            (tmp_path / audit.artifact_name(kind)).write_bytes(b"synthetic\n")
    assert audit.validate(ROOT, tmp_path, published_only=True) == ["all exact eleven published regular artifacts are required; no skip/fallback"]


def test_real_published_eleven_independently_validate_without_skip(audit):
    """Required published replay: sparse/missing deliverables are a hard failure."""
    paths = [ROOT / audit.DIRECTORY / audit.artifact_name(kind) for kind in audit.KINDS]
    missing = [str(path) for path in paths if not path.is_file()]
    assert not missing, "Mandatory eleven-artifact replay cannot skip: " + "; ".join(missing)
    before = {str(path): audit.digest(path.read_bytes()) for path in paths}
    assert audit.validate(ROOT, published_only=True) == []
    assert {str(path): audit.digest(path.read_bytes()) for path in paths} == before
