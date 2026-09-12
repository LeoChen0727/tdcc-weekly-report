"""Read-only, independently calculated annual current-version TDCC audit.

This module never imports a producer, evaluates its AST, executes frozen source,
downloads inputs, or writes artifacts. Published-only checks are explicitly not
an independent audit of the private raw sources or historical availability.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import gzip
import hashlib
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

MODEL_ID = "tdcc_stealth_accumulation"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_current_version_annual_replay_v1"
PREFIX = "tdcc_stealth_accumulation_current_version_annual_replay_"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_current_version_annual_replay_v1.json"
DEFAULT_DIRECTORY = "output/research/tdcc_stealth_accumulation"
PRICE_REF = "07d992bbd9afa283355d8828a294da4524efb56d"
SELECTOR_REF = "2244a0a36c4542cd62948b50f12ef98ade50e1df"
OPERATION_REF = "b4c289c98f7276f07036c1b8b4d90d9d8de466bd"
CLASSIFIER_REF = "af71f09d64aabbbadf9481940590dce21cd8e263"
# Set from the final reviewed contract, not from an artifact-supplied digest.
APPROVED_CONTRACT_SHA256 = "fbccfcd32079dd1bf81eba942c91b57bc7942da0dffc3a5cd01df4872461de91"
FEATURE_FIELDS = "stock_id,stock_name,market,signal_date,tdcc_price_phase,tdcc_status,volume_confirmed_breakout,open,high,low,close,return_5d,return_20d,daily_return_calc,previous_close,high_20,low_20,previous_20d_high_ex_today,volume_ma20,volume_ma20_lots,volume_ratio,tdcc_accumulation_signal,tdcc_accumulation_description,tdcc_400_change_sum,tdcc_1000_change_sum,tdcc_400_up_weeks,tdcc_1000_up_weeks,feature_id,input_ref,receipt_id,available_no_later_than,entry_cutoff,universe_source_path,universe_source_sha256,observed_history_dates,history_observations,history_missing_session_dates,history_gap_count,historical_closed_date_files_excluded,tdcc_window_dates,tdcc_paths,phase_policy,instrument_note,input_availability_proven,feature_supported,unsupported_reasons,raw_selector_selected,selected,positive_resolution,attack_already_started,primary_row_retained,formal_use,promotion_evidence_allowed".split(",")
SCHEMAS = {
    "features": FEATURE_FIELDS,
    "signals": FEATURE_FIELDS,
    "coverage": "signal_date,input_ref,receipt_id,mother_population_basis,path,missing,total_rows,universe_rows,excluded_code_rows,duplicate_keys,alias_payload_conflict,coverage_status,pit_supported_rows,current_version_supported_rows,selected_signals,unsupported_reason_counts,historical_closed_date_files_excluded,receipt_available_no_later_than,entry_cutoff,receipt_gap_audit".split(","),
    "trades": "trade_id,signal_date,stock_id,stock_name,market,horizon,slippage_bps,entry_date,exit_date,entry_open,exit_close,shares,entry_notional,buy_fee,entry_cash,exit_notional,sell_fee,sell_tax,net_exit_cash,net_pnl,gross_return_pct,net_return_pct,outcome,simulation_status,strict_v3_status,strict_missing_evidence,ca_cashflow_assumption,total_return_verified,input_ref,receipt_id,outcome_ref,entry_source_path,entry_source_sha256,exit_source_path,exit_source_sha256,history_gap_count,anomaly_candidate,primary_row_retained,formal_use,promotion_evidence_allowed".split(","),
    "summary": "horizon,slippage_bps,population,realized_raw_price_proxy_positions,total_input_signals,proxy_no_entry_signals,proxy_immature_positions,proxy_unresolved_exit_positions,strict_verified_total_return_positions,denominator,win_count,neutral_count,failure_count,mean_net_return_pct,median_net_return_pct,win_rate_pct,neutral_rate_pct,failure_rate_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct,anomaly_candidate_positions,caveat,gap_present_positions,gap_present_mean_return_pct,gap_present_median_return_pct,gap_present_win_rate_pct,gap_absent_positions,gap_absent_mean_return_pct,gap_absent_median_return_pct,gap_absent_win_rate_pct".split(","),
    "blocked": "record_type,signal_date,stock_id,reasons,primary_row_retained,horizon,entry_date,exit_date,entry_open,strict_v3_status,strict_entry_established,strict_prior_position_locked,proxy_result_must_not_release_strict_lock".split(","),
    "anomalies": "signal_date,stock_id,horizon,net_return_pct,reason,disposition,primary_row_retained,exclusion_allowed_only_as_sensitivity,entry_date,exit_date,represented_in_current_proxy_trade".split(","),
}
KINDS = {**{k: "csv" for k in SCHEMAS}, "features": "csv.gz", "signals": "csv.gz", "trades": "csv.gz", "blocked": "csv.gz", "source_manifest": "json", "report": "md"}
SERIALIZED_FEATURE_FIELDS = set("return_5d return_20d daily_return_calc previous_close high_20 low_20 previous_20d_high_ex_today volume_ma20 volume_ma20_lots volume_ratio".split())
NUMERIC_FIELDS = set("open high low close return_5d return_20d daily_return_calc previous_close high_20 low_20 previous_20d_high_ex_today volume_ma20 volume_ma20_lots volume_ratio tdcc_400_change_sum tdcc_1000_change_sum tdcc_400_up_weeks tdcc_1000_up_weeks history_observations history_gap_count total_rows universe_rows excluded_code_rows duplicate_keys pit_supported_rows current_version_supported_rows selected_signals horizon slippage_bps entry_open exit_close shares entry_notional buy_fee entry_cash exit_notional sell_fee sell_tax net_exit_cash net_pnl gross_return_pct net_return_pct".split())
NUMERIC_FIELDS.update(k for k in SCHEMAS["summary"] if k not in {"population", "denominator", "caveat"})


def artifact_name(kind):
    return f"{PREFIX}{kind}_v1.{KINDS[kind]}"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical_json(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def number(value):
    try:
        result = float(str(value).replace(",", "").strip())
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def integer(value):
    parsed = number(value)
    if parsed is None or not parsed.is_integer():
        raise ValueError(f"expected finite integer: {value!r}")
    return int(parsed)


def bool_value(value):
    if value is True or value == "True":
        return True
    if value is False or value == "False":
        return False
    raise ValueError(f"noncanonical boolean: {value!r}")


def date_value(value):
    if not re.fullmatch(r"[0-9]{8}", str(value)):
        raise ValueError(f"noncanonical date: {value!r}")
    datetime.strptime(value, "%Y%m%d")
    return value


def csv_records(payload):
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline="")))


def rows_for(kind, payload):
    binary = gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") if KINDS[kind].endswith(".gz") else io.BytesIO(payload)
    with io.TextIOWrapper(binary, encoding="utf-8", newline="") as stream:
        def lines():
            for line in stream:
                if "\r" in line or line.startswith("\ufeff") or not line.endswith("\n"):
                    raise ValueError(f"{kind}: expected UTF-8 without BOM and LF final newline")
                yield line
        reader = csv.DictReader(lines(), strict=True)
        if reader.fieldnames != SCHEMAS[kind]:
            raise ValueError(f"{kind}: fixed schema mismatch: {reader.fieldnames!r}")
        for row in reader:
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f"{kind}: malformed CSV row width")
            yield row


def compare_rows(kind, actual, expected, errors):
    """Ordered exact membership; tolerances never turn missing values into zero."""
    sentinel = object()
    left, right = iter(actual), iter(expected)
    index = 1
    while True:
        got, want = next(left, sentinel), next(right, sentinel)
        index += 1
        if got is sentinel or want is sentinel:
            if got is not sentinel or want is not sentinel:
                errors.append(f"{kind}: row count mismatch at row {index}")
            return
        for field in SCHEMAS[kind]:
            a = "" if got.get(field) is None else str(got.get(field, ""))
            b = "" if want.get(field) is None else str(want.get(field, ""))
            if a == b:
                continue
            x, y = number(a), number(b)
            exact = kind in {"features", "signals"} and field in SERIALIZED_FEATURE_FIELDS
            if not exact and field in NUMERIC_FIELDS and a and b and x is not None and y is not None and math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12):
                continue
            errors.append(f"{kind}: row {index} {field}: {a!r} != independently expected {b!r}")
            if len(errors) >= 100:
                return


def selector_truth(row):
    """Independent frozen v2 enum-fallback decision table, not production import."""
    n = {k: number(row.get(k)) for k in ("open", "high", "low", "close", "previous_close", "volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today", "daily_return_calc", "return_5d", "return_20d", "high_20", "low_20")}
    o, h, l, c = (n[k] for k in ("open", "high", "low", "close"))
    prev, volume, average, level, change = (n[k] for k in ("previous_close", "volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today", "daily_return_calc"))
    bullish = c is not None and o is not None and (c > o or (c == o and prev is not None and c > prev))
    breakout = all(v is not None for v in (c, volume, average, level)) and c >= level * 1.02 and volume >= 2 and average >= 1000 and bullish
    locked = False
    if all(v is not None for v in (o, h, l, c, level, change)):
        tight = h == l or (prev is not None and prev > 0 and (h - l) / prev * 100 <= 1)
        locked = c >= level * 1.02 and change >= 9 and c >= h * .995 and o >= c * .995 and tight
    attack = bool(breakout or locked or str(row.get("volume_confirmed_breakout", "")).lower() in {"true", "1", "yes", "y", "t"})
    enum = str(row.get("tdcc_accumulation_signal", "")).lower()
    positive = enum in {"strong_accumulation", "mild_accumulation"}
    resolution = ("recognized_enum_positive_fallback" if positive else "recognized_enum_nonpositive_fail_closed" if enum in {"neutral", "distribution_warning"} else "unknown_enum_fail_closed" if enum else "missing_positive_evidence_fail_closed")
    high, low = n["high_20"], n["low_20"]
    ranged = all(v is not None for v in (c, high, low)) and high > low and low * .9 <= c <= high * 1.1
    selected = positive and not attack and (volume is None or volume < 2.5) and (n["return_5d"] is None or n["return_5d"] < 8) and (n["return_20d"] is None or n["return_20d"] < 20) and ranged
    return dict(selector_selected=bool(selected), attack_already_started=attack, tdcc_positive_resolution=resolution)


def classify_four_batches(batches):
    if len(batches) != 4:
        raise ValueError("TDCC classification needs exactly four batches")
    a, b = (batches[-1][k] - batches[0][k] for k in ("p400", "p1000"))
    up_a = sum(y["p400"] > x["p400"] for x, y in zip(batches, batches[1:]))
    up_b = sum(y["p1000"] > x["p1000"] for x, y in zip(batches, batches[1:]))
    if a > 0 and b > 0 and min(up_a, up_b) >= 2:
        enum, description = "strong_accumulation", "近幾週400張與1000張同步累積"
    elif a > 0 and b > 0:
        enum, description = "mild_accumulation", "近幾週400張與1000張合計增加"
    elif a > 0 or b > 0:
        enum, description = "mild_accumulation", "近幾週其中一項大戶級距增加"
    elif a < 0 and b < 0:
        enum, description = "distribution_warning", "近幾週400張與1000張同步減少"
    elif a < 0 or b < 0:
        enum, description = "distribution_warning", "近幾週其中一項大戶級距減少"
    else:
        enum, description = "neutral", "近幾週TDCC無明顯累積"
    return dict(tdcc_accumulation_signal=enum, tdcc_accumulation_description=description, tdcc_400_change_sum=round(a, 4), tdcc_1000_change_sum=round(b, 4), tdcc_400_up_weeks=up_a, tdcc_1000_up_weeks=up_b)


def calendar_days(closures, history_start="20250401", calendar_end="20261030"):
    day, end = (datetime.strptime(x, "%Y%m%d") for x in (history_start, calendar_end))
    closed = {date_value(d) for d in closures}
    days = []
    while day <= end:
        value = day.strftime("%Y%m%d")
        if day.weekday() < 5 and value not in closed:
            days.append(value)
        day += timedelta(days=1)
    return days


def cashflow(entry_open, exit_close, slippage_bps):
    with localcontext() as context:
        context.prec = 50
        entry, exit_ = Decimal(str(entry_open)), Decimal(str(exit_close))
        if not entry.is_finite() or not exit_.is_finite() or min(entry, exit_) <= 0 or slippage_bps not in (0, 10, 20):
            raise ValueError("cashflow inputs are not valid positive prices/frozen slippage")
        slip = Decimal(slippage_bps) / 10000
        buy, sell = 1000 * entry * (1 + slip), 1000 * exit_ * (1 - slip)
        buy_fee, sell_fee = max(Decimal(20), buy * Decimal("0.001425")), max(Decimal(20), sell * Decimal("0.001425"))
        tax = sell * Decimal("0.003")
        cost, proceeds = buy + buy_fee, sell - sell_fee - tax
        pnl = proceeds - cost
        return dict(entry_open=str(entry), exit_close=str(exit_), shares="1000", entry_notional=str(buy), buy_fee=str(buy_fee), entry_cash=str(cost), exit_notional=str(sell), sell_fee=str(sell_fee), sell_tax=str(tax), net_exit_cash=str(proceeds), net_pnl=str(pnl), gross_return_pct=str((exit_ / entry - 1) * 100), net_return_pct=str(pnl / cost * 100), outcome="win" if pnl > 0 else "failure" if pnl < 0 else "neutral")


def anomaly_rows(trades, evidence):
    keys, rows = set(), []
    for item in evidence.get("retained_anomaly_candidates", []):
        key = item["signal_date"], item["stock_id"], integer(item["horizon"])
        if key in keys:
            raise ValueError(f"duplicate retained anomaly: {key}")
        keys.add(key)
        rows.append(dict(signal_date=key[0], stock_id=key[1], horizon=key[2], net_return_pct=item["net_return_pct"], reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample", disposition="unresolved_anomaly_candidate", primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True, entry_date=item["entry_date"], exit_date=item["exit_date"]))
    for horizon in (5, 10, 20):
        sample = [r for r in trades if integer(r["horizon"]) == horizon and integer(r["slippage_bps"]) == 10]
        if len(sample) < 4:
            continue
        q1, _, q3 = statistics.quantiles(sorted(float(r["net_return_pct"]) for r in sample), n=4, method="inclusive")
        width = 3 * (q3 - q1)
        for trade in sample:
            value = float(trade["net_return_pct"])
            key = trade["signal_date"], trade["stock_id"], horizon
            if (value < q1 - width or value > q3 + width) and key not in keys:
                keys.add(key)
                rows.append(dict(signal_date=key[0], stock_id=key[1], horizon=horizon, net_return_pct=trade["net_return_pct"], reason="outside_Q1_Q3_plus_3IQR_descriptive_candidate", disposition="unresolved_anomaly_candidate", primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True, entry_date=trade["entry_date"], exit_date=trade["exit_date"]))
    represented = {(r["signal_date"], r["stock_id"], integer(r["horizon"])) for r in trades}
    for trade in trades:
        trade["anomaly_candidate"] = (trade["signal_date"], trade["stock_id"], integer(trade["horizon"])) in keys
    for row in rows:
        row["represented_in_current_proxy_trade"] = (row["signal_date"], row["stock_id"], row["horizon"]) in represented
    return rows


def summarize(trades, signals, blocked):
    rows = []
    for horizon in (5, 10, 20):
        for slip in (0, 10, 20):
            for population in ("primary_including_anomaly_candidates", "sensitivity_excluding_anomaly_candidates"):
                group = [r for r in trades if integer(r["horizon"]) == horizon and integer(r["slippage_bps"]) == slip and (population.startswith("primary") or not bool_value(r["anomaly_candidate"]))]
                values = [float(r["net_return_pct"]) for r in group]
                n = len(values)
                count = lambda predicate: sum(predicate(x) for x in values)
                rate = lambda predicate: count(predicate) / n * 100 if n else ""
                row = dict(horizon=horizon, slippage_bps=slip, population=population, realized_raw_price_proxy_positions=n, total_input_signals=len(signals), proxy_no_entry_signals=sum(integer(r.get("horizon") or 0) == horizon and r["record_type"] == "operation_no_entry" for r in blocked), proxy_immature_positions=sum(integer(r.get("horizon") or 0) == horizon and r.get("reasons") == "open_immature" for r in blocked), proxy_unresolved_exit_positions=sum(integer(r.get("horizon") or 0) == horizon and r.get("reasons") == "open_unresolved_exit_price" for r in blocked), strict_verified_total_return_positions=0, denominator="realized_raw_price_proxy_positions", win_count=count(lambda x: x > 0), neutral_count=count(lambda x: x == 0), failure_count=count(lambda x: x < 0), mean_net_return_pct=statistics.mean(values) if n else "", median_net_return_pct=statistics.median(values) if n else "", win_rate_pct=rate(lambda x: x > 0), neutral_rate_pct=rate(lambda x: x == 0), failure_rate_pct=rate(lambda x: x < 0), high_return_ge10_rate_pct=rate(lambda x: x >= 10), loss_le_minus10_rate_pct=rate(lambda x: x <= -10), min_net_return_pct=min(values) if n else "", max_net_return_pct=max(values) if n else "", anomaly_candidate_positions=sum(bool_value(r["anomaly_candidate"]) for r in group), caveat="raw_unadjusted_price_proxy_not_verified_total_return;not_performance_promotion_evidence")
                for label, gap in (("gap_present", True), ("gap_absent", False)):
                    subset = [float(r["net_return_pct"]) for r in group if (integer(r["history_gap_count"]) > 0) == gap]
                    row.update({label + "_positions": len(subset), label + "_mean_return_pct": statistics.mean(subset) if subset else "", label + "_median_return_pct": statistics.median(subset) if subset else "", label + "_win_rate_pct": sum(v > 0 for v in subset) / len(subset) * 100 if subset else ""})
                rows.append(row)
    return rows


class GitReader:
    """Immutable-object IO only. Alias prices and checked-out market files are forbidden."""

    def __init__(self, repository_root):
        self.root = Path(repository_root)
        self.trees, self.used, self.prices = {}, {}, {}

    def tree(self, ref):
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            raise ValueError(f"not an immutable commit SHA: {ref!r}")
        if ref not in self.trees:
            data = subprocess.check_output(["git", "--no-replace-objects", "-C", str(self.root), "ls-tree", "-rz", ref])
            entries = {}
            for entry in data.split(b"\0"):
                if entry:
                    meta, path = entry.split(b"\t", 1)
                    mode, kind, oid = meta.decode().split()
                    if kind == "blob" and mode == "100644":
                        entries[path.decode("utf-8")] = oid
            self.trees[ref] = entries
        return self.trees[ref]

    def read(self, ref, path):
        oid = self.tree(ref).get(path)
        if oid is None:
            raise ValueError(f"missing immutable regular source: {ref}:{path}")
        data = subprocess.check_output(["git", "--no-replace-objects", "-C", str(self.root), "cat-file", "blob", oid])
        self.used[ref, path] = dict(ref=ref, path=path, git_blob_oid=oid, bytes=len(data), sha256=digest(data))
        return data

    def daily(self, ref, date):
        key = ref, date
        if key not in self.prices:
            path = f"data/daily_price/{date_value(date)}.csv"
            if path not in self.tree(ref):
                result = {}, dict(path=path, missing=True, total_rows=0, universe_rows=0)
            else:
                data = self.read(ref, path)
                result = price_records(csv_records(data), date, path, ref, digest(data))
            # The independent audit is bounded in RAM even for annual features.
            if len(self.prices) >= 64:
                self.prices.pop(next(iter(self.prices)))
            self.prices[key] = result
        return self.prices[key]


def price_records(raw, date, path, ref, sha):
    selected, counts = {}, Counter()
    for row in raw:
        stock = (row.get("stock_id") or row.get("ticker") or "").strip()
        if not re.fullmatch(r"[1-9][0-9]{3}", stock):
            continue
        counts[stock] += 1
        selected[stock] = dict(stock_id=stock, stock_name=row.get("stock_name", row.get("name", "")), market=row.get("market", ""), date=row.get("date", "").replace("-", "").strip(), source=row.get("source", ""), source_path=path, source_ref=ref, source_sha256=sha, **{k: number(row.get(k)) for k in ("open", "high", "low", "close", "volume", "trading_value")})
    for stock, row in selected.items():
        row.update(duplicate_key=counts[stock] > 1, date_mismatch=row["date"] != date, alias_payload_conflict=False)
    return selected, dict(path=path, missing=False, total_rows=len(raw), universe_rows=len(selected), excluded_code_rows=len(raw) - sum(counts.values()), duplicate_keys=sum(n > 1 for n in counts.values()), alias_payload_conflict=False)


def valid_price(row):
    if not row or any(row.get(k) is None or row[k] <= 0 for k in ("open", "high", "low", "close")):
        return False
    return row["low"] <= row["open"] <= row["high"] and row["low"] <= row["close"] <= row["high"] and not any(row.get(k) for k in ("duplicate_key", "date_mismatch", "alias_payload_conflict"))


def _contract_errors(contract):
    errors = []
    if digest(canonical_json(contract)) != APPROVED_CONTRACT_SHA256:
        errors.append("contract canonical SHA256 differs from the approved annual contract")
    required = dict(model_id=MODEL_ID, research_contract="current_acquired_historical_versions_annual_v1", selector_ref=SELECTOR_REF, operation_ref=OPERATION_REF, classifier_ref=CLASSIFIER_REF, outcome_ref=PRICE_REF, price_source_ref=PRICE_REF, requested_signal_start="20250910", requested_signal_end="20260909", as_of="20260909", history_start="20250401", calendar_end="20261030", artifact_prefix=PREFIX, numeric_feature_serialization="four decimal places before frozen selector evaluation", expected_tdcc_weeks=55, expected_tdcc_rows=3667325)
    for field in ("formal_use", "promotion_evidence_allowed", "ordinary_stock_universe_certified", "input_availability_proven", "full_period_pit_complete", "calendar_complete_coverage_verified", "corporate_action_complete_coverage_verified", "private_raw_publication_allowed"):
        required[field] = False
    for field, value in required.items():
        if contract.get(field) != value or (isinstance(value, bool) and contract.get(field) is not value):
            errors.append(f"contract {field} must remain {value!r}")
    if contract.get("costs") != dict(shares=1000, fee_each_side="0.001425", minimum_fee_each_side="20", sell_tax="0.003", slippage_bps=[0, 10, 20]):
        errors.append("contract costs differ from frozen operation contract")
    if contract.get("artifact_kinds") != [artifact_name(k)[len(PREFIX):] for k in ("source_manifest", "coverage", "features", "signals", "trades", "summary", "blocked", "anomalies", "report")]:
        errors.append("contract must name exactly the nine ordered annual artifacts")
    external = contract.get("external_files", [])
    if Counter(r.get("kind") for r in external) != Counter(tdcc=55, price_warmup=8, price_recovery=1, calendar=1):
        errors.append("external source cardinality must be 55 TDCC/8 warmup/1 recovery/1 calendar")
    if len({r.get("path") for r in external}) != len(external):
        errors.append("duplicate external source path")
    tdcc = [r for r in external if r.get("kind") == "tdcc"]
    if len({r.get("date") for r in tdcc}) != len(tdcc):
        errors.append("duplicate TDCC effective date")
    for row in external:
        if not re.fullmatch(r"[0-9a-f]{64}", row.get("sha256", "")) or not row.get("path") or Path(row["path"]).is_absolute():
            errors.append("external source needs exact relative path and SHA256")
    return errors


def published_features(rows, contract, calendar, errors):
    signals, counters, unavailable = [], {}, []
    previous = None
    all_stocks = set()
    for row in rows:
        date, stock = row["signal_date"], row["stock_id"]
        key = date, stock
        if previous is not None and key <= previous:
            raise ValueError(f"features repeated or unsorted identity: {key}")
        previous = key
        if date not in calendar or not contract["requested_signal_start"] <= date <= contract["requested_signal_end"] or not re.fullmatch(r"[1-9][0-9]{3}", stock):
            raise ValueError(f"features identity outside annual universe: {key}")
        if row["feature_id"] != f"{date}:{stock}":
            raise ValueError(f"features feature_id mismatch: {key}")
        for field in ("receipt_id", "available_no_later_than", "entry_cutoff", "tdcc_price_phase", "tdcc_status"):
            if row[field] != "":
                raise ValueError(f"current-version feature must leave {field} blank: {key}")
        for field in ("input_availability_proven", "formal_use", "promotion_evidence_allowed", "volume_confirmed_breakout"):
            if bool_value(row[field]):
                raise ValueError(f"current-version feature {field} must remain False: {key}")
        if not bool_value(row["primary_row_retained"]) or row["input_ref"] != contract["price_source_ref"]:
            raise ValueError(f"feature retention/source version drift: {key}")
        if row["phase_policy"] != "phase_classifier_not_invoked":
            raise ValueError("feature phase policy drift")
        for field in SERIALIZED_FEATURE_FIELDS:
            if row[field] and not re.fullmatch(r"-?[0-9]+\.[0-9]{4}", row[field]):
                raise ValueError(f"feature {field} not serialized to four decimals: {key}")
        supported = bool_value(row["feature_supported"])
        reasons = row["unsupported_reasons"].split(";") if row["unsupported_reasons"] else []
        if supported != (not reasons):
            raise ValueError(f"feature support/reason contradiction: {key}")
        truth = selector_truth(row)
        expected = dict(raw_selector_selected=truth["selector_selected"], selected=supported and truth["selector_selected"], positive_resolution=truth["tdcc_positive_resolution"], attack_already_started=truth["attack_already_started"])
        for field, value in expected.items():
            if str(row[field]) != str(value):
                raise ValueError(f"feature frozen selector mismatch: {key}:{field}")
        observed = row["observed_history_dates"].split(";") if row["observed_history_dates"] else []
        if observed != sorted(set(observed)) or len(observed) != integer(row["history_observations"]) or len(observed) > 21 or any(d > date or d < contract["history_start"] or d not in calendar for d in observed):
            raise ValueError(f"feature historical observation lineage invalid: {key}")
        missing = [d for d in calendar if observed and observed[0] <= d <= date and d not in observed]
        if row["history_missing_session_dates"] != ";".join(missing) or integer(row["history_gap_count"]) != len(missing):
            raise ValueError(f"feature history gaps mismatch: {key}")
        batches = row["tdcc_window_dates"].split(";") if row["tdcc_window_dates"] else []
        if batches != sorted(set(batches)) or any(d > date for d in batches) or (supported and len(batches) != 4):
            raise ValueError(f"feature TDCC effective dates invalid: {key}")
        bucket = counters.setdefault(date, dict(rows=0, supported=0, selected=0, tdr=0, reasons=Counter()))
        bucket["rows"] += 1
        bucket["supported"] += supported
        bucket["selected"] += expected["selected"]
        bucket["tdr"] += stock.startswith("91")
        bucket["reasons"].update(reasons)
        all_stocks.add(stock)
        if expected["selected"]:
            signals.append(row)
        if reasons:
            unavailable.append(dict(record_type="feature_unavailable", signal_date=date, stock_id=stock, reasons=";".join(reasons), primary_row_retained=True))
    return signals, counters, unavailable, all_stocks


def published_operations(contract, signals, trades, blocked, calendar, errors):
    """Audit all published decisions, cashflows and separate horizon locks.

    This validates the published decision evidence; full raw price validation is
    reserved for the input-root path and is never claimed by this function.
    """
    strict = [r for r in blocked if r["record_type"] == "strict_ledger_decision"]
    noentry = [r for r in blocked if r["record_type"] == "operation_no_entry"]
    censored = [r for r in blocked if r["record_type"] == "operation_censored"]
    allowed_types = {"strict_ledger_decision", "operation_no_entry", "operation_censored", "feature_unavailable"}
    if any(r["record_type"] not in allowed_types for r in blocked):
        raise ValueError("unknown blocked record_type")
    by_strict, decisions, by_trade = {}, {}, defaultdict(list)
    for row in strict:
        key = row["signal_date"], row["stock_id"], integer(row["horizon"])
        if key in by_strict:
            raise ValueError(f"duplicate strict decision: {key}")
        by_strict[key] = row
    for row in noentry + censored:
        key = row["signal_date"], row["stock_id"], integer(row["horizon"])
        if key in decisions:
            raise ValueError(f"duplicate proxy decision: {key}")
        decisions[key] = row
    for row in trades:
        key = row["signal_date"], row["stock_id"], integer(row["horizon"])
        by_trade[key].append(row)
    expected_keys = {(r["signal_date"], r["stock_id"], horizon) for horizon in (5, 10, 20) for r in signals}
    if set(by_strict) != expected_keys or set(decisions) | set(by_trade) != expected_keys or set(decisions) & set(by_trade):
        raise ValueError("operation membership does not partition every signal/horizon exactly once")
    for horizon in (5, 10, 20):
        prior_exit = {}
        for signal in signals:
            date, stock = signal["signal_date"], signal["stock_id"]
            key = date, stock, horizon
            position = bisect.bisect_right(calendar, date)
            entry, exit_ = calendar[position], calendar[position + horizon]
            state = by_strict[key]
            if state["entry_date"] != entry or state["exit_date"] != exit_:
                raise ValueError(f"strict horizon indexing drift: {key}")
            if bool_value(state["strict_entry_established"]) or bool_value(state["strict_prior_position_locked"]) or not bool_value(state["proxy_result_must_not_release_strict_lock"]):
                raise ValueError(f"strict availability-unproven position must never establish entry: {key}")
            if entry > contract["as_of"]:
                strict_status, strict_reason = "blocked_entry_after_as_of", "entry_after_as_of"
            elif state["strict_v3_status"] == "blocked_entry_price":
                strict_status, strict_reason = "blocked_entry_price", "entry_price_missing_or_invalid"
            else:
                strict_status, strict_reason = "blocked_input_availability_unproven", "current_acquired_historical_versions_not_event_time_receipts"
                if number(state["entry_open"]) is None or number(state["entry_open"]) <= 0:
                    raise ValueError(f"strict unproven-input state lacks valid entry price: {key}")
            if (state["strict_v3_status"], state["reasons"]) != (strict_status, strict_reason):
                raise ValueError(f"strict blocked state drift: {key}")
            lock = prior_exit.get(stock)
            reason = ("blocked_exit_day" if date == lock else "blocked_active_position") if lock and date <= lock else "entry_after_as_of" if entry > contract["as_of"] else "entry_price_missing_or_invalid" if strict_status == "blocked_entry_price" else ""
            decision = decisions.get(key)
            if reason:
                if not decision or decision["record_type"] != "operation_no_entry" or decision["reasons"] != reason:
                    raise ValueError(f"proxy same-stock lock/no-entry drift: {key}")
            elif decision:
                if decision["record_type"] != "operation_censored" or decision["reasons"] != ("open_immature" if exit_ > contract["as_of"] else "open_unresolved_exit_price"):
                    raise ValueError(f"proxy unresolved/immature state drift: {key}")
                prior_exit[stock] = "99999999"
            else:
                if exit_ > contract["as_of"]:
                    raise ValueError(f"future exit cannot be realized: {key}")
                rows = by_trade[key]
                if [integer(r["slippage_bps"]) for r in rows] != [0, 10, 20]:
                    raise ValueError(f"trade slippage coverage/order drift: {key}")
                for row in rows:
                    slip = integer(row["slippage_bps"])
                    expected = dict(row, **cashflow(row["entry_open"], row["exit_close"], slip))
                    expected.update(trade_id=f"{date}:{stock}:D{horizon}:S{slip}", entry_date=entry, exit_date=exit_, stock_name=signal["stock_name"], market=signal["market"], input_ref=contract["price_source_ref"], outcome_ref=contract["outcome_ref"], receipt_id="", simulation_status="realized_raw_price_proxy", strict_v3_status=strict_status, strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit", ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False, primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False, history_gap_count=signal["history_gap_count"])
                    compare_rows("trades", [row], [expected], errors)
                    if number(row["entry_open"]) != number(state["entry_open"]):
                        raise ValueError(f"trade entry price differs from strict decision evidence: {key}")
                if len({(r["entry_open"], r["exit_close"], r["entry_source_path"], r["entry_source_sha256"], r["exit_source_path"], r["exit_source_sha256"]) for r in rows}) != 1:
                    raise ValueError(f"slippage scenarios disagree on source prices: {key}")
                prior_exit[stock] = exit_
            if decision and (decision["entry_date"] != entry or decision["exit_date"] != exit_ or decision["strict_v3_status"] != strict_status):
                raise ValueError(f"proxy decision dates/strict status drift: {key}")
    return strict


class PrivateInputs:
    """Consume exact approved source bytes without publishing or modifying them."""

    def __init__(self, input_root, contract):
        self.root, self.contract, self.used = Path(input_root), contract, {}

    def read(self, item):
        lexical = self.root / item["path"]
        for component in (lexical, *lexical.parents):
            if component.is_symlink():
                raise ValueError(f"linked private source: {item['path']}")
            if component.exists():
                metadata = component.lstat()
                if getattr(metadata, "st_file_attributes", 0) & 0x400:
                    raise ValueError(f"reparse private source: {item['path']}")
        path = lexical.resolve(strict=True)
        if not path.is_file():
            raise ValueError(f"not a private regular file: {item['path']}")
        data = path.read_bytes()
        if digest(data) != item["sha256"]:
            raise ValueError(f"private input SHA256 mismatch: {item['path']}")
        self.used[item["path"]] = dict(item, bytes=len(data))
        return data


def private_tdcc(inputs, contract):
    weeks, total = {}, 0
    bins_needed = ("400,001-600,000", "600,001-800,000", "800,001-1,000,000", "more than 1,000,001")
    for item in contract["external_files"]:
        if item["kind"] != "tdcc":
            continue
        data = inputs.read(item)
        by_stock = defaultdict(dict)
        count = 0
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline=""), strict=True)
        for row in reader:
            count += 1
            if row["日期"].replace("-", "") != item["date"]:
                raise ValueError(f"TDCC row effective date mismatch: {item['path']}")
            stock, level = row["股票代碼"].strip(), row["持股分級"].strip()
            if level in by_stock[stock]:
                raise ValueError(f"duplicate TDCC stock/week/bin: {item['date']}:{stock}:{level}")
            try:
                ratio = Decimal(str(row["比例"]).replace(",", "").strip())
                by_stock[stock][level] = ratio if ratio.is_finite() else None
            except InvalidOperation:
                by_stock[stock][level] = None
        if count != item["rows"]:
            raise ValueError(f"TDCC source row count mismatch: {item['path']}")
        total += count
        values = {}
        for stock, bins in by_stock.items():
            with localcontext() as context:
                context.prec = 50
                p400 = float(sum((bins[k] for k in bins_needed), Decimal(0))) if all(bins.get(k) is not None for k in bins_needed) else None
            p1000 = float(bins[bins_needed[-1]]) if bins.get(bins_needed[-1]) is not None else None
            if p400 is not None and p1000 is not None and not 0 <= p1000 <= p400 <= 100:
                raise ValueError(f"TDCC structural invariant requires source investigation: {item['date']}:{stock}")
            values[stock] = dict(date=item["date"], row_date_valid=True, p400=p400, p1000=p1000, path=item["path"])
        if item["date"] in weeks:
            raise ValueError("duplicate TDCC effective week")
        weeks[item["date"]] = values
    if len(weeks) != contract["expected_tdcc_weeks"] or total != contract["expected_tdcc_rows"]:
        raise ValueError("TDCC exact total week/row count mismatch")
    return weeks


class CurrentPrices:
    """Independent canonical-Git prices plus exact authorized private supplements."""

    def __init__(self, git, inputs, contract):
        self.git, self.contract, self.ref = git, contract, contract["price_source_ref"]
        self.supplements, self.recovery_meta = defaultdict(dict), {}
        self.supplemental_counts = dict(warmup_nonquote_rows=0, supplemental_price_rows=0)
        self.dates = {p[-12:-4] for p in git.tree(self.ref) if re.fullmatch(r"data/daily_price/[0-9]{8}\.csv", p) and contract["history_start"] <= p[-12:-4] <= contract["as_of"]}
        for item in contract["external_files"]:
            if item["kind"] not in {"price_warmup", "price_recovery"}:
                continue
            data = inputs.read(item)
            if item["kind"] == "price_warmup":
                table = json.loads(data)["tables"][0]
                if table["fields"][:7] != ["日 期", "成交張數", "成交仟元", "開盤", "最高", "最低", "收盤"]:
                    raise ValueError("official warmup field schema mismatch")
                raw = []
                for values in table["data"]:
                    row = dict(zip(table["fields"], values))
                    year, month, day = (int(x) for x in str(row["日 期"]).split("/"))
                    date = date_value(f"{year + 1911:04d}{month:02d}{day:02d}")
                    if date >= contract["requested_signal_start"]:
                        raise ValueError("warmup source cannot provide an annual signal date")
                    volume = number(row["成交張數"])
                    raw.append(dict(date=date, stock_id=item["stock_id"], market="TPEX", name="", open=row["開盤"], high=row["最高"], low=row["最低"], close=row["收盤"], volume_shares=volume * 1000 if volume is not None else None))
            else:
                raw = csv_records(data)
                if len(raw) != item["rows"] or item["date"] in self.dates:
                    raise ValueError("recovery must contain exact rows for an absent canonical main date")
            identities = set()
            for original in raw:
                stock, date = original["stock_id"], original["date"].replace("-", "")
                if not re.fullmatch(r"[1-9][0-9]{3}", stock):
                    continue
                if (date, stock) in identities:
                    raise ValueError("duplicate supplemental price identity")
                identities.add((date, stock))
                if item["kind"] == "price_recovery" and date != item["date"]:
                    raise ValueError("recovered quote date mismatch")
                row = dict(stock_id=stock, stock_name=original.get("name", ""), market=original["market"], date=date, source="TPEx_OFFICIAL_MONTHLY_CURRENT_VERSION" if item["kind"] == "price_warmup" else "OFFICIAL_RECOVERED_CURRENT_VERSION", source_path="external:" + item["path"], source_ref=self.ref, source_sha256=item["sha256"], duplicate_key=False, date_mismatch=False, alias_payload_conflict=False, **{k: number(original[k]) for k in ("open", "high", "low", "close")}, volume=number(original.get("volume_shares")), trading_value=None)
                if item["kind"] == "price_warmup" and not valid_price(row):
                    self.supplemental_counts["warmup_nonquote_rows"] += 1
                    continue
                prior = self.git.daily(self.ref, date)[0].get(stock)
                if valid_price(prior):
                    if any(prior[k] != row[k] for k in ("open", "high", "low", "close", "volume")):
                        raise ValueError("official warmup and valid canonical main row conflict")
                    continue
                if stock in self.supplements[date]:
                    raise ValueError("overlapping supplemental price identity")
                self.supplements[date][stock] = row
                self.supplemental_counts["supplemental_price_rows"] += 1
                self.dates.add(date)
            if item["kind"] == "price_recovery":
                self.recovery_meta[item["date"]] = dict(path="external:" + item["path"], missing=False, total_rows=len(raw), universe_rows=len(self.supplements[item["date"]]), excluded_code_rows=len(raw) - len(self.supplements[item["date"]]), duplicate_keys=0, alias_payload_conflict=False)

    def daily(self, date):
        if date > self.contract["as_of"]:
            return {}, dict(path=f"data/daily_price/{date}.csv", missing=True, total_rows=0, universe_rows=0)
        prices, meta = self.git.daily(self.ref, date)
        if date in self.supplements:
            prices = dict(prices, **self.supplements[date])
        return prices, self.recovery_meta.get(date, meta)


def reconstruct_features(prices, weeks, contract, closures, actual, errors):
    calendar = calendar_days(closures, contract["history_start"], contract["calendar_end"])
    dates = [d for d in calendar if contract["requested_signal_start"] <= d <= contract["requested_signal_end"]]
    histories = defaultdict(lambda: deque(maxlen=21))
    history_dates = iter(sorted(prices.dates & set(calendar)))
    pending = next(history_dates, None)
    actual_iter = iter(actual)
    signals, coverage, blocked, stocks, tdr_rows, row_count, supported_count = [], [], [], set(), 0, 0, 0
    for date in dates:
        excluded = ";".join(sorted(d for d in prices.dates & set(closures) if d <= date))
        while pending is not None and pending <= date:
            for stock, row in prices.daily(pending)[0].items():
                histories[stock].append(row)
            pending = next(history_dates, None)
        universe, meta = prices.daily(date)
        week_dates = sorted(d for d in weeks if d <= date)[-4:]
        week_paths = [next(r["path"] for r in contract["external_files"] if r["kind"] == "tdcc" and r["date"] == d) for d in week_dates]
        reasons_count, count_supported, count_selected = Counter(), 0, 0
        for stock, price in sorted(universe.items()):
            observations = list(histories[stock])
            batches = [weeks[d][stock] for d in week_dates if stock in weeks[d]]
            reasons = []
            if not valid_price(price): reasons.append("signal_ohlc_invalid_or_conflicting")
            if len(observations) < 21: reasons.append("insufficient_21_observations")
            if not all(valid_price(r) for r in observations): reasons.append("history_ohlc_invalid_or_conflicting")
            if any(r["volume"] is None or r["volume"] < 0 for r in observations[-20:]): reasons.append("volume_missing_or_negative")
            if any(r["source"] == "TPEX_OLD_DAILY_JSON" for r in observations[-20:]): reasons.append("raw_volume_lineage_unresolved")
            if len(batches) != 4 or any(r["p400"] is None or r["p1000"] is None for r in batches): reasons.append("tdcc_four_batch_coverage_missing")
            if any(not r["row_date_valid"] for r in batches): reasons.append("tdcc_effective_date_mismatch")
            row = dict(stock_id=stock, stock_name=price["stock_name"], market=price["market"], signal_date=date, tdcc_price_phase="", tdcc_status="", volume_confirmed_breakout=False, **{k: "" if price[k] is None else str(price[k]) for k in ("open", "high", "low", "close")})
            if len(observations) == 21 and all(valid_price(r) for r in observations):
                last20 = observations[-20:]
                derived = dict(return_5d=(price["close"] / observations[-6]["close"] - 1) * 100, return_20d=(price["close"] / observations[0]["close"] - 1) * 100, daily_return_calc=(price["close"] / observations[-2]["close"] - 1) * 100, previous_close=observations[-2]["close"], high_20=max(r["high"] for r in last20), low_20=min(r["low"] for r in last20), previous_20d_high_ex_today=max(r["high"] for r in observations[:-1]))
                if all(r["volume"] is not None and r["volume"] >= 0 for r in last20):
                    average = statistics.mean(r["volume"] for r in last20)
                    if average > 0:
                        derived.update(volume_ma20=average, volume_ma20_lots=average / 1000, volume_ratio=price["volume"] / average)
                    else:
                        reasons.append("volume_mean_zero")
                row.update({k: format(round(v, 4), ".4f") for k, v in derived.items()})
            if len(batches) == 4 and all(r["p400"] is not None and r["p1000"] is not None for r in batches):
                row.update(classify_four_batches(batches))
            truth = selector_truth(row)
            supported = not reasons
            selected = supported and truth["selector_selected"]
            observed = [r["date"] for r in observations]
            missing = [d for d in calendar if observed and observed[0] <= d <= date and d not in observed]
            row.update(feature_id=f"{date}:{stock}", input_ref=contract["price_source_ref"], receipt_id="", available_no_later_than="", entry_cutoff="", universe_source_path=price["source_path"], universe_source_sha256=price["source_sha256"], observed_history_dates=";".join(observed), history_observations=len(observations), history_missing_session_dates=";".join(missing), history_gap_count=len(missing), historical_closed_date_files_excluded=excluded, tdcc_window_dates=";".join(r["date"] for r in batches), tdcc_paths=";".join(week_paths), phase_policy="phase_classifier_not_invoked", instrument_note="possible_TDR_91_prefix" if stock.startswith("91") else "four_digit_nonzero_equity_code", input_availability_proven=False, feature_supported=supported, unsupported_reasons=";".join(reasons), raw_selector_selected=truth["selector_selected"], selected=selected, positive_resolution=truth["tdcc_positive_resolution"], attack_already_started=truth["attack_already_started"], primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False)
            observed_row = next(actual_iter, None)
            if observed_row is None:
                raise ValueError(f"missing feature from raw reconstruction: {date}:{stock}")
            compare_rows("features", [observed_row], [row], errors)
            if len(errors) >= 100:
                raise ValueError("raw feature audit reached error limit")
            row_count += 1
            supported_count += supported
            tdr_rows += stock.startswith("91")
            stocks.add(stock)
            count_supported += supported
            count_selected += selected
            reasons_count.update(reasons)
            if selected:
                signals.append(row)
            if reasons:
                blocked.append(dict(record_type="feature_unavailable", signal_date=date, stock_id=stock, reasons=";".join(reasons), primary_row_retained=True))
        coverage.append(dict(signal_date=date, input_ref=contract["price_source_ref"], receipt_id="", mother_population_basis="same_day_raw_historical_price_codes_not_candidates", **meta, coverage_status="current_version_research_partial_quality_coverage", pit_supported_rows=0, current_version_supported_rows=count_supported, selected_signals=count_selected, unsupported_reason_counts=json.dumps(dict(reasons_count), sort_keys=True), historical_closed_date_files_excluded=excluded, receipt_available_no_later_than="", entry_cutoff=""))
    if next(actual_iter, None) is not None:
        raise ValueError("unexpected extra features beyond independent source replay")
    return signals, coverage, blocked, calendar, dates, dict(covered_universe_rows=row_count, supported_feature_rows=supported_count, unique_universe_stocks=len(stocks), possible_TDR_universe_rows=tdr_rows)


def reconstruct_operations(prices, contract, signals, blocked, calendar):
    trades, strict = [], []
    for horizon in (5, 10, 20):
        proxy_exit = {}
        for signal in signals:
            stock, date = signal["stock_id"], signal["signal_date"]
            index = bisect.bisect_right(calendar, date)
            entry, exit_ = calendar[index], calendar[index + horizon]
            ep, xp = prices.daily(entry)[0].get(stock), prices.daily(exit_)[0].get(stock)
            if entry > contract["as_of"]:
                status, why = "blocked_entry_after_as_of", "entry_after_as_of"
            elif not valid_price(ep):
                status, why = "blocked_entry_price", "entry_price_missing_or_invalid"
            else:
                status, why = "blocked_input_availability_unproven", "current_acquired_historical_versions_not_event_time_receipts"
            strict.append(dict(record_type="strict_ledger_decision", signal_date=date, stock_id=stock, horizon=horizon, entry_date=entry, exit_date=exit_, strict_v3_status=status, strict_entry_established=False, strict_prior_position_locked=False, reasons=why, entry_open=ep["open"] if ep else "", proxy_result_must_not_release_strict_lock=True))
            reason = ""
            if stock in proxy_exit and date <= proxy_exit[stock]:
                reason = "blocked_exit_day" if date == proxy_exit[stock] else "blocked_active_position"
            elif entry > contract["as_of"]:
                reason = "entry_after_as_of"
            elif not valid_price(ep):
                reason = "entry_price_missing_or_invalid"
            if reason:
                blocked.append(dict(record_type="operation_no_entry", signal_date=date, stock_id=stock, horizon=horizon, entry_date=entry, exit_date=exit_, reasons=reason, strict_v3_status=status))
                continue
            proxy_exit[stock] = exit_ if valid_price(xp) else "99999999"
            if exit_ > contract["as_of"] or not valid_price(xp):
                blocked.append(dict(record_type="operation_censored", signal_date=date, stock_id=stock, horizon=horizon, entry_date=entry, exit_date=exit_, reasons="open_immature" if exit_ > contract["as_of"] else "open_unresolved_exit_price", entry_open=ep["open"], strict_v3_status=status))
                continue
            for slip in (0, 10, 20):
                trades.append(dict(trade_id=f"{date}:{stock}:D{horizon}:S{slip}", signal_date=date, stock_id=stock, stock_name=signal["stock_name"], market=signal["market"], horizon=horizon, slippage_bps=slip, entry_date=entry, exit_date=exit_, **cashflow(ep["open"], xp["close"], slip), simulation_status="realized_raw_price_proxy", strict_v3_status=status, strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit", ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False, input_ref=signal["input_ref"], receipt_id="", outcome_ref=contract["outcome_ref"], entry_source_path=ep["source_path"], entry_source_sha256=ep["source_sha256"], exit_source_path=xp["source_path"], exit_source_sha256=xp["source_sha256"], history_gap_count=signal["history_gap_count"], anomaly_candidate=False, primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False))
    return trades, strict


def reference_pairs(contract):
    return {
        (contract["selector_ref"], "scripts/build_tdcc_stealth_accumulation_historical_replay.py"),
        (contract["selector_ref"], "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py"),
        (contract["classifier_ref"], "tdcc_trend_utils.py"),
        (contract["operation_ref"], "scripts/build_tdcc_stealth_accumulation_operation_replay.py"),
        (contract["operation_ref"], "docs/specs/tdcc_stealth_accumulation_operation_replay_v3.md"),
        (contract["price_source_ref"], "scripts/build_stock_price_history.py"),
        (contract["price_source_ref"], "config/twse_non_trading_days.csv"),
        (contract["price_source_ref"], "data/market_calendar/exceptional_non_trading_days.csv"),
        (contract["anomaly_retention_reference"]["ref"], contract["anomaly_retention_reference"]["path"]),
    }


def source_bindings(manifest, contract):
    listed = {}
    references = reference_pairs(contract)
    for row in manifest["sources"]:
        key = row["ref"], row["path"]
        price_path = re.fullmatch(r"data/daily_price/([0-9]{8})\.csv", row["path"])
        permitted = key in references or (row["ref"] == contract["price_source_ref"] and price_path and contract["history_start"] <= price_path[1] <= contract["as_of"])
        if not permitted or key in listed:
            raise ValueError(f"duplicate or unapproved manifest Git source: {key}")
        if set(row) != {"ref", "path", "git_blob_oid", "bytes", "sha256"} or not re.fullmatch(r"[0-9a-f]{40}", row["git_blob_oid"]) or not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) or not isinstance(row["bytes"], int) or isinstance(row["bytes"], bool) or row["bytes"] <= 0:
            raise ValueError(f"malformed Git source binding: {key}")
        listed[key] = row
    if not references <= set(listed):
        raise ValueError("manifest omits a fixed selector/operation/calendar/anomaly provenance source")
    if manifest["sources"] != sorted(manifest["sources"], key=lambda r: (r["ref"], r["path"])):
        raise ValueError("manifest Git source order mismatch")
    external = manifest["external_sources"]
    if len(external) != len(contract["external_files"]):
        raise ValueError("manifest external source exact allowlist count mismatch")
    for actual, expected in zip(external, contract["external_files"]):
        if {k: v for k, v in actual.items() if k != "bytes"} != expected or not isinstance(actual.get("bytes"), int) or isinstance(actual["bytes"], bool) or actual["bytes"] <= 0:
            raise ValueError("manifest external source binding differs from exact contract")
    return listed, {"external:" + r["path"]: r["sha256"] for r in external}


def fixed_evidence_audit(repository_root, contract, evidence, listed):
    """Cheap public-Git pins remain auditable without private raw inputs in CI."""
    git = GitReader(repository_root)
    for key in sorted(reference_pairs(contract)):
        git.read(*key)
        if git.used[key] != listed[key]:
            raise ValueError(f"fixed public provenance SHA/bytes mismatch: {key}")
    retention = contract["anomaly_retention_reference"]
    expected = json.loads(git.read(retention["ref"], retention["path"]))[retention["field"]]
    if evidence.get("retained_anomaly_candidates") != expected:
        raise ValueError("retained anomaly evidence differs from immutable public reference")
    closures = set(evidence["calendar_closures"])
    for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
        if not {r["date"] for r in csv_records(git.read(contract["price_source_ref"], path))} <= closures:
            raise ValueError("published calendar omits immutable official closure evidence")
    return git


def validate_coverage(coverage, counters, contract, dates):
    if [r["signal_date"] for r in coverage] != dates:
        raise ValueError("coverage does not enumerate every annual exchange session exactly once")
    for row in coverage:
        date = row["signal_date"]
        count = counters.get(date, dict(rows=0, supported=0, selected=0, reasons=Counter()))
        if integer(row["universe_rows"]) != count["rows"] or integer(row["pit_supported_rows"]) != 0 or integer(row["current_version_supported_rows"]) != count["supported"] or integer(row["selected_signals"]) != count["selected"]:
            raise ValueError(f"coverage feature/support/selection count mismatch: {date}")
        if row["input_ref"] != contract["price_source_ref"] or row["coverage_status"] != "current_version_research_partial_quality_coverage" or row["mother_population_basis"] != "same_day_raw_historical_price_codes_not_candidates":
            raise ValueError(f"coverage current-version provenance drift: {date}")
        for field in ("receipt_id", "receipt_available_no_later_than", "entry_cutoff", "receipt_gap_audit"):
            if row[field] != "":
                raise ValueError(f"coverage receipt/time field must be blank: {date}:{field}")
        if json.loads(row["unsupported_reason_counts"]) != dict(count["reasons"]):
            raise ValueError(f"coverage unsupported-reason counts mismatch: {date}")
        if integer(row["total_rows"]) < integer(row["universe_rows"]) or integer(row["excluded_code_rows"] or 0) < 0 or integer(row["duplicate_keys"] or 0) < 0:
            raise ValueError(f"coverage raw row accounting invalid: {date}")
        if bool_value(row["missing"]) and count["rows"]:
            raise ValueError(f"missing price date cannot contain features: {date}")
        if row["alias_payload_conflict"] not in ("", "False"):
            raise ValueError("canonical current-version source must not consume aliases")


def validate_report(payload, contract, counts, summaries, errors):
    if payload.startswith(b"\xef\xbb\xbf") or b"\r" in payload or not payload.endswith(b"\n"):
        raise ValueError("report must be UTF-8 without BOM and LF final newline")
    report = payload.decode("utf-8")
    for marker in ("TDCC", "目前取得歷史版本", "不是 strict PIT", "formal_use=False", "promotion_evidence_allowed=False", "full_period_pit_complete=False", "input_availability_proven=False", "unresolved_anomaly_candidate 保留 primary", "sensitivity", "不是已核實 total-return"):
        if marker not in report:
            errors.append(f"report missing mandatory limitation: {marker}")
    metrics = {"研究訊號日期": len(counts["current_version_signal_dates"]), "實際特徵列": counts["covered_universe_rows"], "支持特徵列": counts["supported_feature_rows"], "訊號": counts["signals"], "價格 proxy 交易列": counts["realized_proxy_trade_rows"], "異常候選": counts["anomaly_candidates"]}
    for label, expected in metrics.items():
        observed = re.findall(re.escape(label) + r" ([0-9]+)(?=[；。（\s])", report)
        if observed != [str(expected)]:
            errors.append(f"report {label} count mismatch")
    if f"訊號範圍：{contract['requested_signal_start']}–{contract['requested_signal_end']}；結果資料 as_of：{contract['as_of']}。" not in report:
        errors.append("report annual/as-of date window mismatch")
    expected = []
    for row in summaries:
        if integer(row["slippage_bps"]) == 10 and row["population"] == "primary_including_anomaly_candidates":
            mean = "" if row["mean_net_return_pct"] == "" else f"{row['mean_net_return_pct']:.6f}"
            median = "" if row["median_net_return_pct"] == "" else f"{row['median_net_return_pct']:.6f}"
            expected.append(f"| D+{row['horizon']} | {row['realized_raw_price_proxy_positions']} | {row['win_count']}/{row['neutral_count']}/{row['failure_count']} | {mean} | {median} |")
    for row in summaries:
        if integer(row["slippage_bps"]) == 10 and row["population"] == "primary_including_anomaly_candidates":
            values = ["" if row[name] == "" else f"{row[name]:.6f}" for name in ("win_rate_pct", "high_return_ge10_rate_pct", "loss_le_minus10_rate_pct", "min_net_return_pct", "max_net_return_pct")]
            expected.append(f"| D+{row['horizon']} | {values[0]} | {values[1]} | {values[2]} | {values[3]} / {values[4]} | {row['proxy_immature_positions']} / {row['proxy_unresolved_exit_positions']} |")
    for row in summaries:
        if integer(row["slippage_bps"]) == 10 and row["population"] == "sensitivity_excluding_anomaly_candidates":
            values = ["" if row[name] == "" else f"{row[name]:.6f}" for name in ("mean_net_return_pct", "median_net_return_pct", "win_rate_pct")]
            expected.append(f"| D+{row['horizon']} | {row['realized_raw_price_proxy_positions']} | {values[0]} | {values[1]} | {values[2]} |")
    actual = [r for r in report.splitlines() if r.startswith("| D+")]
    if actual != expected:
        errors.append("report primary/distribution/maturity/sensitivity D+5/10/20 values differ from independent arithmetic")


def validate_artifacts(repository_root, contract, artifacts, *, input_root=None, price_repository_root=None, published_only=False):
    errors = []
    try:
        errors.extend(_contract_errors(contract))
        names = {artifact_name(k) for k in KINDS}
        if set(artifacts) != names:
            errors.append(f"artifact exact-nine allowlist mismatch: missing={sorted(names - set(artifacts))}; extra={sorted(set(artifacts) - names)}")
        if errors:
            return errors
        manifest = json.loads(artifacts[artifact_name("source_manifest")])
        if artifacts[artifact_name("source_manifest")] != canonical_json(manifest):
            raise ValueError("source manifest must use canonical sorted JSON with final LF")
        required = dict(model_id=MODEL_ID, artifact_version=ARTIFACT_VERSION, contract_file=CONTRACT_FILE, contract=contract, contract_sha256=digest(canonical_json(contract)))
        for key, expected in required.items():
            if manifest.get(key) != expected:
                raise ValueError(f"manifest {key} differs from approved annual contract")
        for key in ("formal_use", "promotion_evidence_allowed", "full_period_pit_complete"):
            if manifest.get(key) is not False:
                raise ValueError(f"manifest {key} must remain False")
        hashes = {name: dict(bytes=len(data), sha256=digest(data)) for name, data in artifacts.items() if name != artifact_name("source_manifest")}
        if manifest.get("hashes") != hashes:
            raise ValueError("manifest final eight serialized artifact hashes/lengths mismatch")
        listed, external_hashes = source_bindings(manifest, contract)
        evidence = manifest["evidence"]
        if evidence.get("calendar_complete_coverage_verified") is not False:
            raise ValueError("evidence calendar complete coverage must remain False")
        closures = evidence["calendar_closures"]
        if closures != sorted(set(closures)):
            raise ValueError("calendar closure identity/order mismatch")
        calendar = calendar_days(closures, contract["history_start"], contract["calendar_end"])
        git = fixed_evidence_audit(price_repository_root or repository_root, contract, evidence, listed)
        dates = [d for d in calendar if contract["requested_signal_start"] <= d <= contract["requested_signal_end"]]
        parsed = {kind: list(rows_for(kind, artifacts[artifact_name(kind)])) for kind in SCHEMAS if kind != "features"}
        signals, counters, unavailable, all_stocks = published_features(rows_for("features", artifacts[artifact_name("features")]), contract, calendar, errors)
        compare_rows("signals", parsed["signals"], signals, errors)
        validate_coverage(parsed["coverage"], counters, contract, dates)
        for signal in signals:
            expected_sha = listed.get((contract["price_source_ref"], signal["universe_source_path"]), {}).get("sha256", external_hashes.get(signal["universe_source_path"]))
            if signal["universe_source_sha256"] != expected_sha:
                raise ValueError("selected feature source SHA absent from exact provenance bindings")
        strict = published_operations(contract, signals, parsed["trades"], parsed["blocked"], calendar, errors)
        for row in parsed["trades"]:
            for phase in ("entry", "exit"):
                path = row[phase + "_source_path"]
                expected_sha = listed.get((contract["price_source_ref"], path), {}).get("sha256", external_hashes.get(path))
                if expected_sha != row[phase + "_source_sha256"]:
                    raise ValueError("trade source SHA absent from exact provenance bindings")
                if path.startswith("data/") and path != f"data/daily_price/{row[phase + '_date']}.csv":
                    raise ValueError("trade source date/path identity mismatch")
        compare_rows("blocked", [r for r in parsed["blocked"] if r["record_type"] == "feature_unavailable"], unavailable, errors)
        computed_trades = [dict(r) for r in parsed["trades"]]
        anomalies = anomaly_rows(computed_trades, evidence)
        compare_rows("anomalies", parsed["anomalies"], anomalies, errors)
        compare_rows("trades", parsed["trades"], computed_trades, errors)
        summaries = summarize(computed_trades, signals, parsed["blocked"])
        compare_rows("summary", parsed["summary"], summaries, errors)
        counts = dict(requested_session_dates=len(dates), current_version_signal_dates=dates, tdcc_weeks=contract["expected_tdcc_weeks"], tdcc_rows=contract["expected_tdcc_rows"], unique_universe_stocks=len(all_stocks), missing_price_dates=[d for d in dates if not counters.get(d, {}).get("rows")], possible_TDR_universe_rows=sum(r["tdr"] for r in counters.values()), covered_universe_rows=sum(r["rows"] for r in counters.values()), supported_feature_rows=sum(r["supported"] for r in counters.values()), signals=len(signals), realized_proxy_trade_rows=len(computed_trades), anomaly_candidates=len(anomalies), signals_with_history_gaps=sum(integer(r["history_gap_count"]) > 0 for r in signals), anomaly_candidates_current_proxy_keys=sum(r["represented_in_current_proxy_trade"] for r in anomalies), anomaly_candidates_removed_from_primary=0, strict_verified_total_return_positions=0, strict_ledger_rows=len(strict), strict_status_counts=dict(Counter(r["strict_v3_status"] for r in strict)))
        if set(manifest["counts"]) != set(counts) | {"supplemental"}:
            raise ValueError("manifest count field coverage mismatch")
        for key, value in counts.items():
            if manifest["counts"].get(key) != value:
                errors.append(f"manifest {key} differs from independent artifact arithmetic")
        supplemental = manifest["counts"]["supplemental"]
        if set(supplemental) != {"warmup_nonquote_rows", "supplemental_price_rows"} or any(not isinstance(v, int) or isinstance(v, bool) or v < 0 for v in supplemental.values()):
            raise ValueError("manifest supplemental counts malformed")
        if not published_only and not errors:
            if input_root is None:
                raise ValueError("full independent source audit requires --input-root; use --published-only explicitly for artifact-only audit")
            lineage = contract["anomaly_retention_reference"]
            retained = json.loads(git.read(lineage["ref"], lineage["path"]))[lineage["field"]]
            if evidence["retained_anomaly_candidates"] != retained:
                raise ValueError("retained anomaly evidence differs from immutable source")
            inputs = PrivateInputs(input_root, contract)
            independent_closures = set()
            for item in contract["external_files"]:
                if item["kind"] == "calendar":
                    independent_closures.update(r["date"] for r in csv_records(inputs.read(item)) if r["scheduled_closed"] == "True")
            for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
                independent_closures.update(r["date"] for r in csv_records(git.read(contract["price_source_ref"], path)))
            if closures != sorted(independent_closures):
                raise ValueError("published closures differ from independently read official calendar sources")
            weeks = private_tdcc(inputs, contract)
            prices = CurrentPrices(git, inputs, contract)
            expected_signals, coverage, blocked, calendar, dates, raw_counts = reconstruct_features(prices, weeks, contract, closures, rows_for("features", artifacts[artifact_name("features")]), errors)
            compare_rows("signals", signals, expected_signals, errors)
            compare_rows("coverage", parsed["coverage"], coverage, errors)
            trades, expected_strict = reconstruct_operations(prices, contract, expected_signals, blocked, calendar)
            expected_anomalies = anomaly_rows(trades, evidence)
            compare_rows("trades", parsed["trades"], trades, errors)
            compare_rows("blocked", parsed["blocked"], blocked + expected_strict, errors)
            compare_rows("anomalies", parsed["anomalies"], expected_anomalies, errors)
            compare_rows("summary", parsed["summary"], summarize(trades, expected_signals, blocked), errors)
            if supplemental != prices.supplemental_counts:
                errors.append("supplemental price counts differ from independently read sources")
            for key, value in raw_counts.items():
                if counts[key] != value:
                    errors.append(f"raw-source count mismatch: {key}")
            # Source manifests must include every canonical price blob in the
            # fixed range, including excluded closed-date copies for disclosure.
            for path in sorted(git.tree(contract["price_source_ref"])):
                match = re.fullmatch(r"data/daily_price/([0-9]{8})\.csv", path)
                if match and contract["history_start"] <= match[1] <= contract["as_of"]:
                    pair = contract["price_source_ref"], path
                    if pair not in git.used:
                        git.read(*pair)
            if listed != git.used:
                errors.append("manifest Git sources differ from exact independently consumed bytes")
            if manifest["external_sources"] != [inputs.used[r["path"]] for r in contract["external_files"]]:
                errors.append("manifest private source bytes differ from independently consumed inputs")
        validate_report(artifacts[artifact_name("report")], contract, counts, summaries, errors)
    except (ValueError, KeyError, TypeError, AttributeError, IndexError, ZeroDivisionError, OverflowError, UnicodeError, csv.Error, EOFError, subprocess.CalledProcessError, OSError) as exc:
        errors.append(f"annual independent audit failed closed: {type(exc).__name__}: {exc}")
    return errors


def validate(repository_root, output_root=None, *, input_root=None, price_repository_root=None, published_only=False):
    root = Path(repository_root).resolve()
    output = Path(output_root) if output_root is not None else root / DEFAULT_DIRECTORY
    try:
        contract = json.loads((root / CONTRACT_FILE).read_text(encoding="utf-8"))
        paths = list(output.glob(PREFIX + "*"))
        if any(not p.is_file() or p.is_symlink() for p in paths):
            return ["annual artifact path must be a regular file"]
        artifacts = {p.name: p.read_bytes() for p in paths}
    except (ValueError, OSError) as exc:
        return [f"cannot read annual contract/artifacts: {exc}"]
    return validate_artifacts(root, contract, artifacts, input_root=input_root, price_repository_root=price_repository_root, published_only=published_only)


def main(argv=None):
    parser = argparse.ArgumentParser(description="唯讀獨立核對 TDCC 一年目前取得歷史版本研究回放")
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--input-root", type=Path)
    parser.add_argument("--price-repository-root", type=Path)
    parser.add_argument("--published-only", action="store_true")
    args = parser.parse_args(argv)
    errors = validate(args.repository_root, args.output_root, input_root=args.input_root, price_repository_root=args.price_repository_root, published_only=args.published_only)
    print(json.dumps(dict(status="fail" if errors else "pass", errors=errors, validation_mode="published_artifact_integrity_only" if args.published_only else "independent_source_replay", original_publication_availability_verified=False, formal_use=False, promotion_evidence_allowed=False), ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
