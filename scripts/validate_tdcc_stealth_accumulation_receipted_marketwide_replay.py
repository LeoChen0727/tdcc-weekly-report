"""Independent, read-only audit of the receipted TDCC marketwide research replay.

No producer, selector module, or executable AST is imported.  Expected rows are
derived from immutable Git blobs and an independently written decision table.
Passing this audit does not establish complete calendar/CA coverage or promotion.
"""
from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from decimal import Decimal, localcontext
from pathlib import Path

MODEL_ID = "tdcc_stealth_accumulation"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_receipted_marketwide_replay_v1"
PREFIX = "tdcc_stealth_accumulation_receipted_marketwide_replay_"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_receipted_marketwide_replay_v1.json"
AVAILABILITY_FILE = "config/tdcc_stealth_accumulation_receipted_marketwide_availability_v1.json"
DEFAULT_DIRECTORY = "output/research/tdcc_stealth_accumulation"
SELECTOR_REF = "2244a0a36c4542cd62948b50f12ef98ade50e1df"
OPERATION_REF = "b4c289c98f7276f07036c1b8b4d90d9d8de466bd"
OUTCOME_REF = "40cee0405390a9ccaf3a1ad0778aa1e680ab8252"
CLASSIFIER_REF = "af71f09d64aabbbadf9481940590dce21cd8e263"
APPROVED_CONTRACT_SHA256 = "6a6b3a94eae79d6686a9c385d7c4f4bd5b3286dd650ac46d76d0f3ea97e55621"
APPROVED_AVAILABILITY_SHA256 = "8b09a4ccc4887e4081347b5fecda2ddd8442a659cd0b259dbb9876dce89cef40"
FEATURE_FIELDS = "stock_id,stock_name,market,signal_date,tdcc_price_phase,tdcc_status,volume_confirmed_breakout,open,high,low,close,return_5d,return_20d,daily_return_calc,previous_close,high_20,low_20,previous_20d_high_ex_today,volume_ma20,volume_ma20_lots,volume_ratio,tdcc_accumulation_signal,tdcc_accumulation_description,tdcc_400_change_sum,tdcc_1000_change_sum,tdcc_400_up_weeks,tdcc_1000_up_weeks,feature_id,input_ref,receipt_id,available_no_later_than,entry_cutoff,universe_source_path,universe_source_sha256,observed_history_dates,history_observations,history_missing_session_dates,history_gap_count,historical_closed_date_files_excluded,tdcc_window_dates,tdcc_paths,phase_policy,instrument_note,input_availability_proven,feature_supported,unsupported_reasons,raw_selector_selected,selected,positive_resolution,attack_already_started,primary_row_retained,formal_use,promotion_evidence_allowed".split(",")
SCHEMAS = {
    "features": FEATURE_FIELDS,
    "signals": FEATURE_FIELDS,
    "coverage": "signal_date,input_ref,receipt_id,mother_population_basis,path,missing,total_rows,universe_rows,excluded_code_rows,duplicate_keys,alias_payload_conflict,coverage_status,pit_supported_rows,selected_signals,unsupported_reason_counts,historical_closed_date_files_excluded,receipt_available_no_later_than,entry_cutoff,receipt_gap_audit".split(","),
    "trades": "trade_id,signal_date,stock_id,stock_name,market,horizon,slippage_bps,entry_date,exit_date,entry_open,exit_close,shares,entry_notional,buy_fee,entry_cash,exit_notional,sell_fee,sell_tax,net_exit_cash,net_pnl,gross_return_pct,net_return_pct,outcome,simulation_status,strict_v3_status,strict_missing_evidence,ca_cashflow_assumption,total_return_verified,input_ref,receipt_id,outcome_ref,entry_source_path,entry_source_sha256,exit_source_path,exit_source_sha256,history_gap_count,anomaly_candidate,primary_row_retained,formal_use,promotion_evidence_allowed".split(","),
    "summary": "horizon,slippage_bps,population,realized_raw_price_proxy_positions,total_input_signals,proxy_no_entry_signals,proxy_immature_positions,proxy_unresolved_exit_positions,strict_verified_total_return_positions,denominator,win_count,neutral_count,failure_count,mean_net_return_pct,median_net_return_pct,win_rate_pct,neutral_rate_pct,failure_rate_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct,anomaly_candidate_positions,caveat,gap_present_positions,gap_present_mean_return_pct,gap_present_median_return_pct,gap_present_win_rate_pct,gap_absent_positions,gap_absent_mean_return_pct,gap_absent_median_return_pct,gap_absent_win_rate_pct".split(","),
    "blocked": "record_type,signal_date,stock_id,reasons,primary_row_retained,horizon,entry_date,exit_date,entry_open,strict_v3_status,strict_entry_established,strict_prior_position_locked,proxy_result_must_not_release_strict_lock".split(","),
    "anomalies": "signal_date,stock_id,horizon,net_return_pct,reason,disposition,primary_row_retained,exclusion_allowed_only_as_sensitivity,entry_date,exit_date,represented_in_current_proxy_trade".split(","),
}
KINDS = {**{k: "csv" for k in SCHEMAS}, "source_manifest": "json", "report": "md"}
NUMERIC_FIELDS = set("open high low close return_5d return_20d daily_return_calc previous_close high_20 low_20 previous_20d_high_ex_today volume_ma20 volume_ma20_lots volume_ratio tdcc_400_change_sum tdcc_1000_change_sum tdcc_400_up_weeks tdcc_1000_up_weeks history_observations history_gap_count total_rows universe_rows excluded_code_rows duplicate_keys pit_supported_rows selected_signals horizon slippage_bps entry_open exit_close shares entry_notional buy_fee entry_cash exit_notional sell_fee sell_tax net_exit_cash net_pnl gross_return_pct net_return_pct".split())
NUMERIC_FIELDS.update(k for k in SCHEMAS["summary"] if k not in {"population", "denominator", "caveat"})
SERIALIZED_FEATURE_FIELDS = set("return_5d return_20d daily_return_calc previous_close high_20 low_20 previous_20d_high_ex_today volume_ma20 volume_ma20_lots volume_ratio".split())


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


def csv_records(payload):
    return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline="")))


class GitReader:
    """Technical immutable-object reader; no checkout, fetch, imports or writes."""

    def __init__(self, repository_root):
        self.root = Path(repository_root)
        self.trees, self.objects, self.used = {}, {}, {}
        self.prices = {}

    def tree(self, ref):
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            raise ValueError(f"not an immutable commit SHA: {ref}")
        if ref not in self.trees:
            data = subprocess.check_output(["git", "--no-replace-objects", "-C", str(self.root), "ls-tree", "-rz", ref])
            entries = {}
            for entry in data.split(b"\0"):
                if not entry:
                    continue
                meta, path = entry.split(b"\t", 1)
                mode, kind, oid = meta.decode().split()
                if kind == "blob":
                    entries[path.decode("utf-8")] = oid
            self.trees[ref] = entries
        return self.trees[ref]

    def read(self, ref, path):
        oid = self.tree(ref).get(path)
        if oid is None:
            raise ValueError(f"missing immutable input: {ref}:{path}")
        if oid not in self.objects:
            self.objects[oid] = subprocess.check_output(["git", "--no-replace-objects", "-C", str(self.root), "cat-file", "blob", oid])
        data = self.objects[oid]
        self.used[ref, path] = dict(ref=ref, path=path, git_blob_oid=oid, bytes=len(data), sha256=digest(data))
        return data

    def daily(self, ref, date):
        key = ref, date
        if key in self.prices:
            return self.prices[key]
        path = f"data/daily_price/{date}.csv"
        alias = f"data/daily_price/daily_price_{date}.csv"
        if path not in self.tree(ref):
            result = {}, dict(path=path, missing=True, total_rows=0, universe_rows=0)
            self.prices[key] = result
            return result
        data = self.read(ref, path)
        payload_sha = digest(data)
        conflict = alias in self.tree(ref) and self.read(ref, alias) != data
        raw = csv_records(data)
        selected, counts = {}, Counter()
        for item in raw:
            stock = (item.get("stock_id") or item.get("ticker") or "").strip()
            if not re.fullmatch(r"[1-9][0-9]{3}", stock):
                continue
            counts[stock] += 1
            selected[stock] = dict(stock_id=stock, stock_name=item.get("stock_name", item.get("name", "")),
                market=item.get("market", ""), date=item.get("date", "").replace("-", "").strip(),
                source=item.get("source", ""), source_path=path, source_ref=ref, source_sha256=payload_sha,
                **{k: number(item.get(k)) for k in ("open", "high", "low", "close", "volume", "trading_value")})
        for stock, item in selected.items():
            item.update(duplicate_key=counts[stock] > 1, date_mismatch=item["date"] != date,
                        alias_payload_conflict=conflict)
        result = selected, dict(path=path, missing=False, total_rows=len(raw), universe_rows=len(selected),
            excluded_code_rows=len(raw)-sum(counts.values()), duplicate_keys=sum(n > 1 for n in counts.values()),
            alias_payload_conflict=conflict)
        self.prices[key] = result
        return result


def valid_price(row):
    if not row or any(row.get(k) is None or row[k] <= 0 for k in ("open", "high", "low", "close")):
        return False
    return (row["low"] <= row["open"] <= row["high"] and row["low"] <= row["close"] <= row["high"]
            and not any(row.get(k) for k in ("duplicate_key", "date_mismatch", "alias_payload_conflict")))


def selector_truth(row):
    """Independent frozen empty-phase/status enum branch, including attack veto."""
    values = {k: number(row.get(k)) for k in ("open", "high", "low", "close", "previous_close",
        "volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today", "daily_return_calc",
        "return_5d", "return_20d", "high_20", "low_20")}
    o, h, l, c = (values[k] for k in ("open", "high", "low", "close"))
    prev, vol, avg, level, ret = (values[k] for k in ("previous_close", "volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today", "daily_return_calc"))
    bullish = c is not None and o is not None and (c > o or (c == o and prev is not None and c > prev))
    normal = all(v is not None for v in (c, vol, avg, level)) and c >= level * 1.02 and vol >= 2 and avg >= 1000 and bullish
    locked = False
    if all(v is not None for v in (o, h, l, c, level, ret)):
        tight = h == l or (prev is not None and prev > 0 and (h-l)/prev*100 <= 1)
        locked = c >= level*1.02 and ret >= 9 and c >= h*.995 and o >= c*.995 and tight
    attack = bool(normal or locked or str(row.get("volume_confirmed_breakout", "")).lower() in {"true", "1", "yes", "y", "t"})
    enum = str(row.get("tdcc_accumulation_signal", "")).lower()
    positive = enum in {"strong_accumulation", "mild_accumulation"}
    resolution = ("recognized_enum_positive_fallback" if positive else
        "recognized_enum_nonpositive_fail_closed" if enum in {"neutral", "distribution_warning"} else
        "unknown_enum_fail_closed" if enum else "missing_positive_evidence_fail_closed")
    high, low = values["high_20"], values["low_20"]
    in_range = all(v is not None for v in (c, high, low)) and high > low and low*.9 <= c <= high*1.1
    selected = (positive and not attack and (vol is None or vol < 2.5)
        and (values["return_5d"] is None or values["return_5d"] < 8)
        and (values["return_20d"] is None or values["return_20d"] < 20) and in_range)
    return {"selector_selected": bool(selected), "attack_already_started": attack, "tdcc_positive_resolution": resolution}


def classify_four_batches(batches):
    a, b = (batches[-1][k]-batches[0][k] for k in ("p400", "p1000"))
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
    return dict(tdcc_accumulation_signal=enum, tdcc_accumulation_description=description,
        tdcc_400_change_sum=round(a, 4), tdcc_1000_change_sum=round(b, 4),
        tdcc_400_up_weeks=up_a, tdcc_1000_up_weeks=up_b)


def calendar_days(closures, history_start="20260401", calendar_end="20261030"):
    day = datetime.strptime(history_start, "%Y%m%d")
    end = datetime.strptime(calendar_end, "%Y%m%d")
    result = []
    while day <= end:
        date = day.strftime("%Y%m%d")
        if day.weekday() < 5 and date not in closures:
            result.append(date)
        day += timedelta(days=1)
    return result


def reconstruct_features(reader, contract, evidence):
    closures = set()
    for source in evidence["calendar_sources"]:
        ref, path = source.split(":", 1)
        closures.update(r["date"] for r in csv_records(reader.read(ref, path)))
    calendar = calendar_days(closures, contract["history_start"], contract["calendar_end"])
    dates = [d for d in calendar if contract["requested_signal_start"] <= d <= contract["requested_signal_end"]]
    receipts = {}
    for receipt in evidence["receipts"]:
        for date in receipt["signal_dates"]:
            if date in receipts:
                raise ValueError(f"duplicate receipt date: {date}")
            if date not in dates:
                raise ValueError(f"receipt outside requested sessions: {date}")
            receipts[date] = receipt
    features, coverage, blocked = [], [], []
    for date in dates:
        # Price maps have per-ref provenance. Keep only the current day's maps,
        # while immutable byte objects and the full source manifest stay cached.
        reader.prices.clear()
        receipt = receipts.get(date)
        ref = receipt["ref"] if receipt else contract["outcome_ref"]
        universe, meta = reader.daily(ref, date)
        common = dict(signal_date=date, input_ref=ref, receipt_id=receipt["id"] if receipt else "",
            mother_population_basis="same_day_raw_historical_price_codes_not_candidates", **meta)
        if receipt is None:
            audits = [r for r in evidence.get("negative_receipt_audits", []) if r["signal_date"] == date]
            coverage.append(dict(**common, coverage_status="receipt_not_established_from_tested_run" if audits else "exact_version_not_yet_pinned",
                receipt_gap_audit=" | ".join(r["finding"] for r in audits), pit_supported_rows=0, selected_signals=0))
            continue
        entry = calendar[bisect.bisect_right(calendar, date)]
        cutoff = datetime.strptime(entry, "%Y%m%d").strftime("%Y-%m-%d") + "T08:30:00+08:00"
        stamp = datetime.fromisoformat(receipt["available_no_later_than"])
        if stamp.tzinfo is None or stamp >= datetime.fromisoformat(cutoff):
            raise ValueError(f"receipt not strictly before entry cutoff: {date}")
        listing = reader.tree(ref)
        price_dates = sorted(Path(p).stem for p in listing if re.fullmatch(r"data/daily_price/[0-9]{8}\.csv", p)
            and contract["history_start"] <= Path(p).stem <= date and datetime.strptime(Path(p).stem, "%Y%m%d").weekday() < 5)
        excluded = sorted(set(price_dates) & {d for d in closures if d <= date})
        history = defaultdict(list)
        for history_date in price_dates:
            if history_date in excluded:
                continue
            prices, _ = reader.daily(ref, history_date)
            for stock in universe.keys() & prices.keys():
                history[stock].append(prices[stock])
        paths = sorted(p for p in listing if re.fullmatch(r"output/history/tdcc/tdcc_holder_ratio_[0-9]{8}\.csv", p) and p[-12:-4] <= date)[-4:]
        tdcc = defaultdict(list)
        for path in paths:
            seen = set()
            for raw in csv_records(reader.read(ref, path)):
                stock = raw.get("code", raw.get("stock_id", "")).strip()
                if stock in seen:
                    raise ValueError(f"duplicate TDCC stock: {ref}:{path}:{stock}")
                seen.add(stock)
                p400, p1000 = number(raw.get("over_400_pct")), number(raw.get("over_1000_pct"))
                if p400 is not None and p1000 is not None and not 0 <= p1000 <= p400 <= 100:
                    # Structural source evidence, not a new selector or row exclusion.
                    # Missing ratios retain the existing unsupported-row behavior.
                    raise ValueError(f"TDCC structural invariant investigation required: {ref}:{path}:{stock}; "
                                     f"expected 0 <= p1000 <= p400 <= 100, got p1000={p1000}, p400={p400}")
                tdcc[stock].append(dict(date=path[-12:-4], row_date_valid=raw.get("date", "").replace("-", "") == path[-12:-4],
                    p400=p400, p1000=p1000))
        reason_counts, supported, selected_count = Counter(), 0, 0
        for stock, price in sorted(universe.items()):
            observations, batches = history[stock][-21:], tdcc.get(stock, [])
            reasons = []
            if not valid_price(price): reasons.append("signal_ohlc_invalid_or_conflicting")
            if len(observations) < 21: reasons.append("insufficient_21_observations")
            if not all(valid_price(r) for r in observations): reasons.append("history_ohlc_invalid_or_conflicting")
            if any(r["volume"] is None or r["volume"] < 0 for r in observations[-20:]): reasons.append("volume_missing_or_negative")
            if any(r["source"] == "TPEX_OLD_DAILY_JSON" for r in observations[-20:]): reasons.append("raw_volume_lineage_unresolved")
            if len(batches) != 4 or any(r["p400"] is None or r["p1000"] is None for r in batches): reasons.append("tdcc_four_batch_coverage_missing")
            if any(not r["row_date_valid"] for r in batches): reasons.append("tdcc_effective_date_mismatch")
            row = dict(stock_id=stock, stock_name=price["stock_name"], market=price["market"], signal_date=date,
                tdcc_price_phase="", tdcc_status="", volume_confirmed_breakout=False,
                **{k: "" if price[k] is None else str(price[k]) for k in ("open", "high", "low", "close")})
            if len(observations) == 21 and all(valid_price(r) for r in observations):
                last20 = observations[-20:]
                derived = {"return_5d": (price["close"]/observations[-6]["close"]-1)*100,
                    "return_20d": (price["close"]/observations[0]["close"]-1)*100,
                    "daily_return_calc": (price["close"]/observations[-2]["close"]-1)*100,
                    "previous_close": observations[-2]["close"], "high_20": max(r["high"] for r in last20),
                    "low_20": min(r["low"] for r in last20), "previous_20d_high_ex_today": max(r["high"] for r in observations[:-1])}
                if all(r["volume"] is not None and r["volume"] >= 0 for r in last20):
                    average = statistics.mean(r["volume"] for r in last20)
                    if average > 0:
                        derived.update(volume_ma20=average, volume_ma20_lots=average/1000, volume_ratio=price["volume"]/average)
                    else:
                        reasons.append("volume_mean_zero")
                row.update({k: format(round(v, 4), ".4f") for k, v in derived.items()})
            if len(batches) == 4 and all(r["p400"] is not None and r["p1000"] is not None for r in batches):
                row.update(classify_four_batches(batches))
            truth = selector_truth(row)
            usable = not reasons
            selected = usable and truth["selector_selected"]
            missing = [d for d in calendar if observations and observations[0]["date"] <= d <= date and d not in {r["date"] for r in observations}]
            row.update(feature_id=f"{date}:{stock}", input_ref=ref, receipt_id=receipt["id"],
                available_no_later_than=receipt["available_no_later_than"], entry_cutoff=cutoff,
                universe_source_path=price["source_path"], universe_source_sha256=price["source_sha256"],
                observed_history_dates=";".join(r["date"] for r in observations), history_observations=len(observations),
                history_missing_session_dates=";".join(missing), history_gap_count=len(missing),
                historical_closed_date_files_excluded=";".join(excluded), tdcc_window_dates=";".join(r["date"] for r in batches),
                tdcc_paths=";".join(paths), phase_policy="phase_classifier_not_invoked",
                instrument_note="possible_TDR_91_prefix" if stock.startswith("91") else "four_digit_nonzero_equity_code",
                input_availability_proven=True, feature_supported=usable, unsupported_reasons=";".join(reasons),
                raw_selector_selected=truth["selector_selected"], selected=selected,
                positive_resolution=truth["tdcc_positive_resolution"], attack_already_started=truth["attack_already_started"],
                primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False)
            features.append(row)
            supported += usable
            selected_count += selected
            reason_counts.update(reasons)
            if reasons:
                blocked.append(dict(record_type="feature_unavailable", signal_date=date, stock_id=stock,
                    reasons=";".join(reasons), primary_row_retained=True))
        coverage.append(dict(**common, coverage_status="receipted_tree_partial_quality_coverage",
            pit_supported_rows=supported, selected_signals=selected_count,
            unsupported_reason_counts=json.dumps(dict(reason_counts), sort_keys=True),
            historical_closed_date_files_excluded=";".join(excluded),
            receipt_available_no_later_than=receipt["available_no_later_than"], entry_cutoff=cutoff))
    reader.prices.clear()
    return features, coverage, blocked, calendar, dates


def cashflow(entry_open, exit_close, slippage_bps):
    with localcontext() as context:
        context.prec = 50
        entry, exit_ = Decimal(str(entry_open)), Decimal(str(exit_close))
        slip = Decimal(slippage_bps)/10000
        buy, sell = 1000*entry*(1+slip), 1000*exit_*(1-slip)
        buy_fee, sell_fee = max(Decimal(20), buy*Decimal("0.001425")), max(Decimal(20), sell*Decimal("0.001425"))
        tax = sell*Decimal("0.003")
        cost, proceeds = buy+buy_fee, sell-sell_fee-tax
        pnl = proceeds-cost
        return dict(entry_open=str(entry), exit_close=str(exit_), shares="1000", entry_notional=str(buy),
            buy_fee=str(buy_fee), entry_cash=str(cost), exit_notional=str(sell), sell_fee=str(sell_fee),
            sell_tax=str(tax), net_exit_cash=str(proceeds), net_pnl=str(pnl),
            gross_return_pct=str((exit_/entry-1)*100), net_return_pct=str(pnl/cost*100),
            outcome="win" if pnl > 0 else "failure" if pnl < 0 else "neutral")


def reconstruct_operations(reader, contract, evidence, signals, blocked, calendar, dates):
    outcome_dates = [d for d in calendar if contract["requested_signal_start"] <= d <= contract["as_of"]]
    outcomes = {date: reader.daily(contract["outcome_ref"], date)[0] for date in outcome_dates}
    trades, strict_rows = [], []
    as_of = contract["as_of"]
    for horizon in (5, 10, 20):
        proxy_exit, strict_held = {}, set()
        for signal in sorted(signals, key=lambda r: (r["signal_date"], r["stock_id"])):
            stock, date = signal["stock_id"], signal["signal_date"]
            index = bisect.bisect_right(calendar, date)
            entry, exit_ = calendar[index], calendar[index+horizon]
            ep, xp = outcomes.get(entry, {}).get(stock), outcomes.get(exit_, {}).get(stock)
            entered = False
            if stock in strict_held:
                status, why = "blocked_active_position", "prior_strict_position_unresolved"
            elif entry > as_of:
                status, why = "blocked_entry_after_as_of", "entry_after_as_of"
            elif not valid_price(ep):
                status, why = "blocked_entry_price", "entry_price_missing_or_invalid"
            elif not evidence.get("calendar_complete_coverage_verified", False):
                status, why = "blocked_calendar_unverified", "complete_official_calendar_event_coverage_not_yet_verified"
            else:
                strict_held.add(stock)
                entered = True
                status, why = (("open_immature", "future_exit_not_mature") if exit_ > as_of else
                               ("open_unresolved_exit", "corporate_action_complete_coverage_unverified"))
            strict_rows.append(dict(record_type="strict_ledger_decision", signal_date=date, stock_id=stock, horizon=horizon,
                entry_date=entry, exit_date=exit_, strict_v3_status=status, strict_entry_established=entered,
                strict_prior_position_locked=stock in strict_held, reasons=why, entry_open=ep["open"] if ep else "",
                proxy_result_must_not_release_strict_lock=True))
            reason = ""
            if stock in proxy_exit and date <= proxy_exit[stock]:
                reason = "blocked_exit_day" if date == proxy_exit[stock] else "blocked_active_position"
            elif entry > as_of:
                reason = "entry_after_as_of"
            elif not valid_price(ep):
                reason = "entry_price_missing_or_invalid"
            if reason:
                blocked.append(dict(record_type="operation_no_entry", signal_date=date, stock_id=stock, horizon=horizon,
                    entry_date=entry, exit_date=exit_, reasons=reason, strict_v3_status=status))
                continue
            proxy_exit[stock] = exit_ if valid_price(xp) else "99999999"
            if exit_ > as_of or not valid_price(xp):
                blocked.append(dict(record_type="operation_censored", signal_date=date, stock_id=stock, horizon=horizon,
                    entry_date=entry, exit_date=exit_, reasons="open_immature" if exit_ > as_of else "open_unresolved_exit_price",
                    entry_open=ep["open"], strict_v3_status=status))
                continue
            for slip in (0, 10, 20):
                trades.append(dict(trade_id=f"{date}:{stock}:D{horizon}:S{slip}", signal_date=date, stock_id=stock,
                    stock_name=signal["stock_name"], market=signal["market"], horizon=horizon, slippage_bps=slip,
                    entry_date=entry, exit_date=exit_, **cashflow(ep["open"], xp["close"], slip),
                    simulation_status="realized_raw_price_proxy", strict_v3_status=status,
                    strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit",
                    ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False,
                    input_ref=signal["input_ref"], receipt_id=signal["receipt_id"], outcome_ref=contract["outcome_ref"],
                    entry_source_path=ep["source_path"], entry_source_sha256=ep["source_sha256"],
                    exit_source_path=xp["source_path"], exit_source_sha256=xp["source_sha256"],
                    history_gap_count=signal["history_gap_count"], anomaly_candidate=False,
                    primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False))
    return trades, strict_rows


def anomaly_rows(trades, evidence):
    keys, rows = set(), []
    for item in evidence.get("retained_anomaly_candidates", []):
        key = item["signal_date"], item["stock_id"], int(item["horizon"])
        if key in keys:
            raise ValueError(f"duplicate retained anomaly: {key}")
        keys.add(key)
        rows.append(dict(signal_date=key[0], stock_id=key[1], horizon=key[2], net_return_pct=item["net_return_pct"],
            reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample",
            disposition="unresolved_anomaly_candidate", primary_row_retained=True,
            exclusion_allowed_only_as_sensitivity=True, entry_date=item["entry_date"], exit_date=item["exit_date"]))
    for horizon in (5, 10, 20):
        sample = [r for r in trades if r["horizon"] == horizon and r["slippage_bps"] == 10]
        if len(sample) < 4:
            continue
        q1, _, q3 = statistics.quantiles(sorted(float(r["net_return_pct"]) for r in sample), n=4, method="inclusive")
        width = 3*(q3-q1)
        for trade in sample:
            value = float(trade["net_return_pct"])
            key = trade["signal_date"], trade["stock_id"], horizon
            if (value < q1-width or value > q3+width) and key not in keys:
                keys.add(key)
                rows.append(dict(signal_date=key[0], stock_id=key[1], horizon=horizon, net_return_pct=trade["net_return_pct"],
                    reason="outside_Q1_Q3_plus_3IQR_descriptive_candidate", disposition="unresolved_anomaly_candidate",
                    primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True,
                    entry_date=trade["entry_date"], exit_date=trade["exit_date"]))
    represented = {(r["signal_date"], r["stock_id"], r["horizon"]) for r in trades}
    for trade in trades:
        trade["anomaly_candidate"] = (trade["signal_date"], trade["stock_id"], trade["horizon"]) in keys
    for row in rows:
        row["represented_in_current_proxy_trade"] = (row["signal_date"], row["stock_id"], row["horizon"]) in represented
    return rows


def summarize(trades, signals, blocked):
    rows = []
    for horizon in (5, 10, 20):
        for slip in (0, 10, 20):
            for population in ("primary_including_anomaly_candidates", "sensitivity_excluding_anomaly_candidates"):
                group = [r for r in trades if r["horizon"] == horizon and r["slippage_bps"] == slip
                    and (population.startswith("primary") or not r["anomaly_candidate"])]
                values = [float(r["net_return_pct"]) for r in group]
                n = len(values)
                count = lambda predicate: sum(predicate(x) for x in values)
                rate = lambda predicate: count(predicate)/n*100 if n else ""
                row = dict(horizon=horizon, slippage_bps=slip, population=population,
                    realized_raw_price_proxy_positions=n, total_input_signals=len(signals),
                    proxy_no_entry_signals=sum(r.get("horizon") == horizon and r["record_type"] == "operation_no_entry" for r in blocked),
                    proxy_immature_positions=sum(r.get("horizon") == horizon and r.get("reasons") == "open_immature" for r in blocked),
                    proxy_unresolved_exit_positions=sum(r.get("horizon") == horizon and r.get("reasons") == "open_unresolved_exit_price" for r in blocked),
                    strict_verified_total_return_positions=0, denominator="realized_raw_price_proxy_positions",
                    win_count=count(lambda x: x > 0), neutral_count=count(lambda x: x == 0), failure_count=count(lambda x: x < 0),
                    mean_net_return_pct=statistics.mean(values) if n else "", median_net_return_pct=statistics.median(values) if n else "",
                    win_rate_pct=rate(lambda x: x > 0), neutral_rate_pct=rate(lambda x: x == 0), failure_rate_pct=rate(lambda x: x < 0),
                    high_return_ge10_rate_pct=rate(lambda x: x >= 10), loss_le_minus10_rate_pct=rate(lambda x: x <= -10),
                    min_net_return_pct=min(values) if n else "", max_net_return_pct=max(values) if n else "",
                    anomaly_candidate_positions=sum(r["anomaly_candidate"] for r in group),
                    caveat="raw_unadjusted_price_proxy_not_verified_total_return;not_performance_promotion_evidence")
                for label, gap in (("gap_present", True), ("gap_absent", False)):
                    subset = [float(r["net_return_pct"]) for r in group if (r["history_gap_count"] > 0) == gap]
                    row.update({label+"_positions": len(subset), label+"_mean_return_pct": statistics.mean(subset) if subset else "",
                        label+"_median_return_pct": statistics.median(subset) if subset else "",
                        label+"_win_rate_pct": sum(v > 0 for v in subset)/len(subset)*100 if subset else ""})
                rows.append(row)
    return rows


def compare_rows(kind, actual, expected, errors):
    """Exact row membership/order/text; numerical tolerances never fill blanks."""
    if len(actual) != len(expected):
        errors.append(f"{kind}: row count {len(actual)} != independently expected {len(expected)}")
    for index, (got, want) in enumerate(zip(actual, expected), 2):
        for field in SCHEMAS[kind]:
            left, right = got.get(field, ""), want.get(field, "")
            right = "" if right is None else str(right)
            if left == right:
                continue
            a, b = number(left), number(right)
            exact_serialization = kind in {"features", "signals"} and field in SERIALIZED_FEATURE_FIELDS
            if not exact_serialization and field in NUMERIC_FIELDS and left and right and a is not None and b is not None and math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12):
                continue
            errors.append(f"{kind}: row {index} {field}: {left!r} != {right!r}")
            if len(errors) >= 100:
                return


def _contract_errors(contract, evidence):
    errors = []
    if digest(canonical_json(contract)) != APPROVED_CONTRACT_SHA256:
        errors.append("contract canonical SHA256 differs from the approved immutable v1 contract")
    if digest(canonical_json(evidence)) != APPROVED_AVAILABILITY_SHA256:
        errors.append("availability canonical SHA256 differs from the approved immutable v1 evidence")
    required = {"model_id": MODEL_ID, "selector_ref": SELECTOR_REF, "operation_ref": OPERATION_REF,
        "outcome_ref": OUTCOME_REF, "classifier_ref": CLASSIFIER_REF,
        "requested_signal_start": "20260615", "requested_signal_end": "20260909", "as_of": "20260909",
        "history_start": "20260401", "calendar_end": "20261030", "artifact_prefix": PREFIX,
        "research_contract": "receipted_marketwide_raw_derived_v2_enum_plan_a_v1",
        "numeric_feature_serialization": "four decimal places before frozen selector evaluation",
        "formal_use": False, "promotion_evidence_allowed": False}
    for field, value in required.items():
        if contract.get(field) != value or (isinstance(value, bool) and contract.get(field) is not value):
            errors.append(f"contract {field} must remain {value!r}")
    costs = {"shares": 1000, "fee_each_side": "0.001425", "minimum_fee_each_side": "20", "sell_tax": "0.003", "slippage_bps": [0, 10, 20]}
    if contract.get("costs") != costs:
        errors.append("contract costs differ from frozen operation contract")
    kinds = contract.get("artifact_kinds", [])
    if len(kinds) != 9 or {PREFIX+k for k in kinds} != {artifact_name(k) for k in KINDS}:
        errors.append("contract artifact kinds must remain exactly nine approved files")
    for field in ("calendar_complete_coverage_verified", "corporate_action_coverage_verified"):
        if evidence.get(field) is not False:
            errors.append(f"{field} must retain explicit False")
    receipt_dates = [d for r in evidence.get("receipts", []) for d in r.get("signal_dates", [])]
    if len(receipt_dates) != 40 or len(set(receipt_dates)) != 40 or "20260730" not in receipt_dates:
        errors.append("receipt allowlist must contain 40 unique approved dates including 20260730")
    for receipt in evidence.get("receipts", []):
        if not re.fullmatch(r"[0-9a-f]{40}", receipt.get("ref", "")):
            errors.append("receipt lacks immutable SHA")
        if not receipt.get("run_id") or not receipt.get("job_id") or not receipt.get("source_timestamp_verbatim"):
            errors.append("receipt lacks run/job/verbatim timestamp evidence")
        expected_url = f"https://github.com/LeoChen0727/tdcc-weekly-report/actions/runs/{receipt.get('run_id')}/job/{receipt.get('job_id')}"
        if receipt.get("url") != expected_url:
            errors.append("receipt job URL mismatch")
        try:
            bound = datetime.fromisoformat(receipt["available_no_later_than"])
            verbatim = datetime.fromisoformat(receipt["source_timestamp_verbatim"])
            if bound.tzinfo is None or verbatim.tzinfo is None or bound != verbatim:
                errors.append("receipt timestamp/verbatim UTC instant mismatch")
        except (ValueError, TypeError, KeyError):
            errors.append("receipt timestamp is malformed or has no timezone")
    return errors


def validate_report(payload, contract, counts, summaries, errors):
    """Audit published numbers and necessary caveats, not producer prose assembly."""
    if payload.startswith(b"\xef\xbb\xbf") or b"\r" in payload or not payload.endswith(b"\n"):
        errors.append("report: expected UTF-8 without BOM and LF final newline")
    report = payload.decode("utf-8")
    markers = ("TDCC", "raw", "PIT", "formal_use=False", "promotion_evidence_allowed=False",
        "full_period_pit_complete=False", "unknown source lineage 不等於 PIT proof",
        "unresolved_anomaly_candidate 保留 primary", "sensitivity", "不是已核實 total-return")
    for marker in markers:
        if marker not in report:
            errors.append(f"report missing mandatory research limitation marker: {marker}")
    metrics = {"有收據日期": len(counts["receipted_signal_dates"]), "實際特徵列": counts["covered_universe_rows"],
        "支持特徵列": counts["supported_feature_rows"], "訊號": counts["signals"],
        "價格 proxy 交易列": counts["realized_proxy_trade_rows"], "異常候選": counts["anomaly_candidates"]}
    for label, expected in metrics.items():
        values = re.findall(re.escape(label)+r" ([0-9]+)(?=[；。（\s])", report)
        if values != [str(expected)]:
            errors.append(f"report {label} count differs from independent replay")
    if f"訊號範圍：{contract['requested_signal_start']}–{contract['requested_signal_end']}；結果資料 as_of：{contract['as_of']}。" not in report:
        errors.append("report signal/outcome date window mismatch")
    rows = [line for line in report.splitlines() if re.match(r"\| D\+", line)]
    expected_rows = []
    for row in summaries:
        if row["slippage_bps"] != 10 or row["population"] != "primary_including_anomaly_candidates":
            continue
        mean = "" if row["mean_net_return_pct"] == "" else f"{row['mean_net_return_pct']:.6f}"
        median = "" if row["median_net_return_pct"] == "" else f"{row['median_net_return_pct']:.6f}"
        expected_rows.append(f"| D+{row['horizon']} | {row['realized_raw_price_proxy_positions']} | {row['win_count']}/{row['neutral_count']}/{row['failure_count']} | {mean} | {median} |")
    if rows != expected_rows:
        errors.append("report D+5/10/20 primary summary differs from independent replay")


def validate_artifacts(repository_root, contract, availability, artifacts):
    try:
        errors = _contract_errors(contract, availability)
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        return [f"malformed contract/availability: {exc}"]
    names = {artifact_name(k) for k in KINDS}
    if set(artifacts) != names:
        errors.append(f"artifact exact-nine allowlist mismatch: missing={sorted(names-set(artifacts))}, extra={sorted(set(artifacts)-names)}")
        return errors
    parsed = {}
    try:
        for kind in SCHEMAS:
            data = artifacts[artifact_name(kind)]
            if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or not data.endswith(b"\n"):
                raise ValueError(f"{kind}: outputs must use UTF-8 without BOM and LF final newline")
            reader = csv.DictReader(io.StringIO(data.decode("utf-8"), newline=""))
            if reader.fieldnames != SCHEMAS[kind]:
                raise ValueError(f"{kind}: fixed schema mismatch")
            parsed[kind] = list(reader)
            if any(None in r or any(v is None for v in r.values()) for r in parsed[kind]):
                raise ValueError(f"{kind}: malformed CSV row width")
        manifest = json.loads(artifacts[artifact_name("source_manifest")])
        if artifacts[artifact_name("source_manifest")] != canonical_json(manifest):
            errors.append("manifest must use canonical UTF-8 sorted JSON and LF final newline")
        if manifest.get("model_id") != MODEL_ID or manifest.get("artifact_version") != ARTIFACT_VERSION:
            errors.append("manifest model/version mismatch")
        for flag in ("formal_use", "promotion_evidence_allowed", "full_period_pit_complete"):
            if manifest.get(flag) is not False:
                errors.append(f"manifest {flag} must remain False")
        for key, value in (("contract_file", CONTRACT_FILE), ("receipt_evidence_file", AVAILABILITY_FILE),
                           ("contract", contract), ("availability", availability),
                           ("contract_sha256", digest(canonical_json(contract))),
                           ("availability_sha256", digest(canonical_json(availability)))):
            if manifest.get(key) != value:
                errors.append(f"manifest {key} mismatch")
        expected_hashes = {n: dict(bytes=len(v), sha256=digest(v)) for n, v in artifacts.items() if n != artifact_name("source_manifest")}
        if manifest.get("hashes") != expected_hashes:
            errors.append("manifest final output byte/SHA256 bindings mismatch")
        if errors:
            return errors
        git = GitReader(repository_root)
        # Bind reference implementation bytes for provenance only; never execute them.
        reference_inputs = [(SELECTOR_REF, "scripts/build_tdcc_stealth_accumulation_historical_replay.py"),
            (SELECTOR_REF, "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py"),
            (CLASSIFIER_REF, "tdcc_trend_utils.py"),
            (OUTCOME_REF, "scripts/build_stock_price_history.py"),
            (OUTCOME_REF, "config/twse_non_trading_days.csv"),
            (OUTCOME_REF, "data/market_calendar/exceptional_non_trading_days.csv"),
            (OPERATION_REF, "scripts/build_tdcc_stealth_accumulation_operation_replay.py"),
            (OPERATION_REF, "docs/specs/tdcc_stealth_accumulation_operation_replay_v3.md")]
        for reference in reference_inputs:
            git.read(*reference)
        features, coverage, blocked, calendar, dates = reconstruct_features(git, contract, availability)
        signals = [r for r in features if r["selected"]]
        trades, strict = reconstruct_operations(git, contract, availability, signals, blocked, calendar, dates)
        anomalies = anomaly_rows(trades, availability)
        summaries = summarize(trades, signals, blocked)
        expected = dict(features=features, coverage=coverage, signals=signals, trades=trades,
            anomalies=anomalies, summary=summaries, blocked=blocked+strict)
        represented = {(r["signal_date"], r["stock_id"], r["horizon"]) for r in trades if r["anomaly_candidate"]}
        counts = dict(requested_session_dates=len(dates),
            receipted_signal_dates=sorted(d for r in availability["receipts"] for d in r["signal_dates"]),
            covered_universe_rows=len(features), supported_feature_rows=sum(r["feature_supported"] for r in features),
            signals=len(signals), realized_proxy_trade_rows=len(trades), anomaly_candidates=len(anomalies),
            signals_with_history_gaps=sum(r["history_gap_count"] > 0 for r in signals),
            anomaly_candidates_current_proxy_keys=len(represented), anomaly_candidates_removed_from_primary=0,
            strict_verified_total_return_positions=0, strict_ledger_rows=len(strict),
            strict_status_counts=dict(Counter(r["strict_v3_status"] for r in strict)))
        if manifest.get("counts") != counts:
            errors.append("manifest counts differ from independent replay")
        for kind in SCHEMAS:
            compare_rows(kind, parsed[kind], expected[kind], errors)
        listed = {}
        permitted_refs = {r["ref"] for r in availability["receipts"]} | {OUTCOME_REF, SELECTOR_REF, OPERATION_REF, CLASSIFIER_REF}
        permitted_refs.update(p.split(":", 1)[0] for p in availability["calendar_sources"])
        reference_pairs = set(reference_inputs) | {tuple(p.split(":", 1)) for p in availability["calendar_sources"]}
        for entry in manifest.get("sources", []):
            key = entry["ref"], entry["path"]
            raw_path = re.fullmatch(r"data/daily_price/(?:daily_price_)?[0-9]{8}\.csv|output/history/tdcc/tdcc_holder_ratio_[0-9]{8}\.csv", key[1])
            if key not in reference_pairs and (key[0] not in permitted_refs or raw_path is None):
                errors.append(f"manifest unrelated/unapproved source: {key}")
                continue
            if key in listed:
                errors.append(f"duplicate manifest source: {key}")
            listed[key] = entry
            git.read(*key)
            if entry != git.used[key]:
                errors.append(f"source exact-byte binding mismatch: {key}")
        missing = set(git.used)-set(listed)
        if missing:
            errors.append(f"manifest omitted independently consumed inputs: {sorted(missing)[:10]}")
        validate_report(artifacts[artifact_name("report")], contract, counts, summaries, errors)
    except (ValueError, KeyError, TypeError, AttributeError, IndexError, ZeroDivisionError, OverflowError, UnicodeError, csv.Error,
            subprocess.CalledProcessError, OSError) as exc:
        errors.append(f"independent replay audit failed closed: {type(exc).__name__}: {exc}")
    return errors


def validate(repository_root, output_root=None):
    root = Path(repository_root).resolve()
    output = Path(output_root) if output_root is not None else root/DEFAULT_DIRECTORY
    try:
        contract = json.loads((root/CONTRACT_FILE).read_text(encoding="utf-8"))
        availability = json.loads((root/AVAILABILITY_FILE).read_text(encoding="utf-8"))
        paths = list(output.glob(PREFIX+"*"))
        if any(not p.is_file() or p.is_symlink() for p in paths):
            return ["artifact path is not a regular file"]
        artifacts = {p.name: p.read_bytes() for p in paths}
    except (ValueError, OSError) as exc:
        return [f"cannot read immutable contract/artifacts: {exc}"]
    return validate_artifacts(root, contract, availability, artifacts)


def main(argv=None):
    parser = argparse.ArgumentParser(description="唯讀獨立驗證 TDCC 潛伏吸籌 receipted marketwide research")
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-root", type=Path)
    args = parser.parse_args(argv)
    errors = validate(args.repository_root, args.output_root)
    print(json.dumps({"status": "fail" if errors else "pass", "errors": errors,
        "formal_use": False, "promotion_evidence_allowed": False}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
