"""Read-only independent medium-term TDCC source, cohort and cashflow audit.

No producer is imported or executed. Full mode rereads the 65 private sources;
published mode audits derived offsets, not the unpublished absolute holdings.
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
import zlib
from collections import Counter, defaultdict, deque
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from itertools import groupby

import validate_tdcc_stealth_accumulation_current_version_annual_replay as annual_io
import validate_tdcc_stealth_accumulation_current_version_horizon_extension as horizon_io

OWNER = "tdcc_stealth_accumulation_medium_term_trend_research"
PREFIX = OWNER + "_"
CONTRACT_FILE = "config/" + PREFIX + "v1.json"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
APPROVED_CONTRACT_SHA256 = "fa38bab5d57e4b8a21984e568ce94eff8bcbdc4d69cbb45ed4fa24da29b63be6"
SOURCE_REF = "847d774ca80f354253e4680e32bc1a46584e35c0"
BASE_REF = "d2f3ccfaf95562b5179f433af0b4b41d62bfee17"
PRICE_REF = "07d992bbd9afa283355d8828a294da4524efb56d"
AS_OF, SPLIT = "20260909", "20260401"
STRATEGIES = ("baseline_4", "trend_8", "trend_12")
PROFILES = {"full_available": STRATEGIES, "common_8": STRATEGIES[:2], "common_12": STRATEGIES}
PARTITIONS = ("all", "training", "purged_cross_split", "validation")
HORIZONS, SLIPPAGES = (20, 60), (0, 10, 20)
FALSE_FLAGS = "formal_use promotion_evidence_allowed input_availability_proven full_period_pit_complete calendar_complete_coverage_verified corporate_action_complete_coverage_verified ordinary_stock_universe_certified private_raw_publication_allowed".split()
KINDS = ("source_manifest", "coverage", "weekly_features", "features", "signals", "trades", "blocked", "summary", "feature_contrasts", "anomalies", "report")
GZIP_KINDS = {"weekly_features", "features", "signals", "trades", "blocked"}
WINDOW_FIELDS = "supported,reasons,dates,span_days,missing_open_weeks,missing_batch_dates,net400_pp,net1000_pp,slope400_pp_per_week,slope1000_pp_per_week,numerator400,numerator1000,last400_pp,last1000_pp,max_positive_share400,max_positive_share1000,descriptive_missing_reasons,selected".split(",")
WINDOW_DECIMAL_FIELDS = {f"w{n}_{key}" for n in (8, 12) for key in (
    "span_days", "net400_pp", "net1000_pp", "slope400_pp_per_week", "slope1000_pp_per_week",
    "numerator400", "numerator1000", "last400_pp", "last1000_pp", "max_positive_share400", "max_positive_share1000")}
EXTRA_FIELDS = "price_supported,price_unsupported_reasons,price_qualified,price_rejection_reasons,baseline_4_supported,baseline_4_selected".split(",") + [f"w{n}_{key}" for n in (8, 12) for key in WINDOW_FIELDS]
METRICS = "win_count,neutral_count,failure_count,win_rate_pct,neutral_rate_pct,failure_rate_pct,mean_net_return_pct,median_net_return_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct".split(",")
SCHEMAS = {
    "weekly_features": "stock_id,batch_date,source_path,source_sha256,complete,unsupported_reasons,anchor_date,offset400_pp,offset1000_pp,formal_use,promotion_evidence_allowed".split(","),
    "features": list(annual_io.FEATURE_FIELDS) + EXTRA_FIELDS,
    "signals": "profile,strategy,feature_id,signal_date,stock_id,stock_name,market,history_gap_count,formal_use,promotion_evidence_allowed".split(","),
    "coverage": "signal_date,raw_universe_rows,price_supported_rows,price_qualified_rows,baseline_4_supported_rows,baseline_4_signals,trend_8_supported_rows,trend_8_signals,trend_12_supported_rows,trend_12_signals,common_8_eligible_rows,common_12_eligible_rows,price_unsupported_reason_counts,trend_8_unsupported_reason_counts,trend_12_unsupported_reason_counts,possible_tdr_rows,formal_use,promotion_evidence_allowed".split(","),
    "trades": ["profile", "strategy", "partition", "feature_id"] + list(annual_io.SCHEMAS["trades"]) + ["entry_index", "exit_target_index"],
    "blocked": ["profile", "strategy", "partition", "feature_id"] + list(annual_io.SCHEMAS["blocked"]) + ["entry_index", "exit_target_index"],
    "summary": "profile,strategy,horizon,slippage_bps,partition,population,samples,stocks,signal_dates,entry_dates,price_qualified_rows,cohort_eligible_rows,strategy_supported_rows,selected_signals,unsupported_rows,cohort_ineligible_rows,rejected_rows,overlap_blocked_signals,missing_entry_signals,entry_after_as_of_signals,immature_positions,missing_exit_positions,purged_positions,anomaly_candidate_positions".split(",") + METRICS + ["formal_use", "promotion_evidence_allowed"],
    "feature_contrasts": "profile,strategy,horizon,slippage_bps,partition,population,feature_name,outcome_group,samples,valid_samples,missing_samples,mean,median,q25,q75,minimum,maximum".split(","),
    "anomalies": ["profile", "strategy", "partition", "slippage_bps"] + list(annual_io.SCHEMAS["anomalies"]) + ["detector_profile", "detector_strategy", "q1", "q3", "lower_fence", "upper_fence"],
}
CONTRAST_FIELDS = tuple("tdcc_400_change_sum tdcc_1000_change_sum tdcc_400_up_weeks tdcc_1000_up_weeks return_5d return_20d volume_ratio history_gap_count".split()) + tuple(f"w{n}_{key}" for n in (8, 12) for key in ("slope400_pp_per_week", "slope1000_pp_per_week", "net400_pp", "net1000_pp", "last400_pp", "last1000_pp", "max_positive_share400", "max_positive_share1000", "span_days"))
LEVELS = ("400,001-600,000", "600,001-800,000", "800,001-1,000,000", "more than 1,000,001")


def artifact_name(kind):
    suffix = "json" if kind == "source_manifest" else "md" if kind == "report" else "csv.gz" if kind in GZIP_KINDS else "csv"
    return PREFIX + kind + "_v1." + suffix


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def canonical_json(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def wire(value):
    return "" if value is None else str(value)


def decimal(value):
    try:
        result = Decimal(str(value).replace(",", "").strip())
        return result if result.is_finite() else None
    except (InvalidOperation, ValueError, TypeError):
        return None


def true(value):
    if value is True or value == "True":
        return True
    if value is False or value == "False":
        return False
    raise ValueError("noncanonical boolean: " + repr(value))


def records(kind, payload):
    source = gzip.GzipFile(fileobj=io.BytesIO(payload)) if kind in GZIP_KINDS else io.BytesIO(payload)
    with io.TextIOWrapper(source, encoding="utf-8", newline="") as stream:
        def lines():
            for line in stream:
                if "\r" in line or line.startswith("\ufeff") or not line.endswith("\n"):
                    raise ValueError(kind + ": UTF-8/LF serialization mismatch")
                yield line
        reader = csv.DictReader(lines(), strict=True)
        if reader.fieldnames != SCHEMAS[kind]:
            raise ValueError(kind + ": exact schema mismatch")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(kind + ": malformed CSV width")
            yield row


def compare_row(kind, actual, expected, ignore=()):
    if actual is None:
        raise ValueError(kind + ": missing expected row")
    for field in SCHEMAS[kind]:
        if field in ignore:
            continue
        left, right = wire(actual.get(field, "")), wire(expected.get(field, ""))
        if left == right:
            continue
        a, b = decimal(left), decimal(right)
        # Offset normalization can preserve additional trailing zeros. Compare
        # these exact Decimal quantities numerically, never with an epsilon.
        if kind == "features" and field in WINDOW_DECIMAL_FIELDS and a is not None and b is not None and a == b:
            continue
        # Counts, identities, booleans, missing cells and gate numerators are exact.
        statistic = field in METRICS[3:] or field in {"mean", "median", "q25", "q75", "minimum", "maximum", "q1", "q3", "lower_fence", "upper_fence"}
        if a is not None and b is not None and statistic and math.isclose(float(a), float(b), rel_tol=1e-12, abs_tol=1e-12):
            continue
        cash = kind == "trades" and field in {"entry_open", "exit_close", "shares", "entry_notional", "buy_fee", "entry_cash", "exit_notional", "sell_fee", "sell_tax", "net_exit_cash", "net_pnl", "gross_return_pct", "net_return_pct"}
        if cash and a is not None and b is not None and a == b:
            continue
        raise ValueError(f"{kind}: {field}={left!r} differs from independent {right!r}; {expected.get('feature_id', '')}")


def compare_sequence(kind, actual, expected, ignore=()):
    iterator = iter(actual)
    for row in expected:
        compare_row(kind, next(iterator, None), row, ignore)
    if next(iterator, None) is not None:
        raise ValueError(kind + ": unexpected extra row")


def contract_audit(contract):
    if digest(canonical_json(contract)) != APPROVED_CONTRACT_SHA256:
        raise ValueError("frozen medium-term contract SHA256 mismatch")
    if any(contract.get(flag) is not False for flag in FALSE_FLAGS):
        raise ValueError("research-only contract flags changed")
    if contract["source_commit_sha"] != SOURCE_REF or contract["base_artifact_ref"] != BASE_REF or contract["price_source_ref"] != PRICE_REF:
        raise ValueError("immutable source pins changed")
    if {PREFIX + suffix for suffix in contract["artifact_kinds"]} != {artifact_name(kind) for kind in KINDS}:
        raise ValueError("fixed eleven-artifact scope changed")


def session_calendar(closures, start="20250401", end="20261030"):
    result, closed = [], set(closures)
    current, last = (datetime.strptime(value, "%Y%m%d") for value in (start, end))
    while current <= last:
        day = current.strftime("%Y%m%d")
        if current.weekday() < 5 and day not in closed:
            result.append(day)
        current += timedelta(days=1)
    return result


def monday(value):
    date = datetime.strptime(value, "%Y%m%d")
    return (date - timedelta(days=date.weekday())).strftime("%Y%m%d")


def missing_open_weeks(dates, calendar, signal_date):
    if not dates:
        return []
    effective_weeks = {monday(day) for day in dates}
    open_weeks = set()
    for day in calendar:
        if dates[0] <= day < signal_date:
            week = monday(day)
            sunday = datetime.strptime(week, "%Y%m%d") + timedelta(days=6)
            if sunday.strftime("%Y%m%d") < signal_date:
                open_weeks.add(week)
    return sorted(open_weeks - effective_weeks)


def exact_ols(dates, values):
    if len(dates) != len(values) or len(dates) < 2 or dates != sorted(set(dates)):
        raise ValueError("OLS requires equal-length, strictly increasing dates")
    values = [decimal(value) for value in values]
    if any(value is None for value in values):
        raise ValueError("OLS cannot fill missing ratios")
    with localcontext() as ctx:
        ctx.prec = 50
        origin = datetime.strptime(dates[0], "%Y%m%d")
        days = [(datetime.strptime(value, "%Y%m%d") - origin).days for value in dates]
        n, sum_day = len(days), sum(days)
        denominator = n * sum(day * day for day in days) - sum_day ** 2
        numerator = sum((Decimal(n * day - sum_day) * value for day, value in zip(days, values)), Decimal(0))
        positive = [b - a for a, b in zip(values, values[1:]) if b > a]
        return dict(numerator=numerator, slope=Decimal(7) * numerator / denominator,
                    net=values[-1] - values[0], last=values[-1] - values[-2],
                    max_positive_share=max(positive) / sum(positive) if positive else None)


def window_metrics(weeks, date, stock, batches, calendar, calendar_start="20250401", calendar_end="20261030"):
    dates = sorted(day for day in weeks if day <= date)[-batches:]
    missing = [day for day in dates if stock not in weeks[day] or any(weeks[day][stock][key] is None for key in ("p400", "p1000"))]
    open_gaps = missing_open_weeks(dates, calendar, date)
    reasons = []
    if len(dates) != batches:
        reasons.append("insufficient_market_batches")
    if missing:
        reasons.append("stock_batch_or_ratio_missing")
    if open_gaps:
        reasons.append("missing_open_week_batch")
    if not dates or dates[0] < calendar_start or dates[-1] > calendar_end or date > calendar_end:
        reasons.append("calendar_evidence_insufficient")
    result = {field: "" for field in WINDOW_FIELDS}
    span = (datetime.strptime(dates[-1], "%Y%m%d") - datetime.strptime(dates[0], "%Y%m%d")).days if dates else ""
    result.update(supported=not reasons, reasons=";".join(reasons), dates=";".join(dates), span_days=span,
                  missing_open_weeks=";".join(open_gaps), missing_batch_dates=";".join(missing), selected=False)
    if reasons:
        return result
    metrics = {bucket: exact_ols(dates, [weeks[day][stock]["p" + str(bucket)] for day in dates]) for bucket in (400, 1000)}
    for bucket, values in metrics.items():
        for key, metric in (("net", "net"), ("last", "last")):
            result[f"{key}{bucket}_pp"] = wire(values[metric])
        result[f"slope{bucket}_pp_per_week"] = wire(values["slope"])
        result[f"numerator{bucket}"] = wire(values["numerator"])
        result[f"max_positive_share{bucket}"] = wire(values["max_positive_share"])
    result["descriptive_missing_reasons"] = ";".join(f"no_positive_change_{bucket}" for bucket in (400, 1000) if metrics[bucket]["max_positive_share"] is None)
    result["selected"] = all(metric["numerator"] > 0 for metric in metrics.values())
    return result


def raw_tdcc(inputs, original):
    weeks, total = {}, 0
    for item in original["external_files"]:
        if item["kind"] != "tdcc":
            continue
        stock_bins, count = defaultdict(dict), 0
        for row in csv.DictReader(io.StringIO(inputs.read(item).decode("utf-8-sig"), newline=""), strict=True):
            count += 1
            if row["日期"].replace("-", "") != item["date"]:
                raise ValueError("TDCC effective date mismatch")
            stock, level = row["股票代碼"].strip(), row["持股分級"].strip()
            if level in stock_bins[stock]:
                raise ValueError("duplicate TDCC stock/week/bin")
            stock_bins[stock][level] = decimal(row["比例"])
        if count != item["rows"] or item["date"] in weeks:
            raise ValueError("TDCC source count or batch identity mismatch")
        total += count
        batch = {}
        for stock, values in stock_bins.items():
            if not re.fullmatch(r"[1-9][0-9]{3}", stock):
                continue
            with localcontext() as ctx:
                ctx.prec = 50
                p400 = sum((values[key] for key in LEVELS), Decimal(0)) if all(values.get(key) is not None for key in LEVELS) else None
            p1000 = values.get(LEVELS[-1])
            if p400 is not None and p1000 is not None and not 0 <= p1000 <= p400 <= 100:
                raise ValueError("TDCC absolute ratio structural invariant failed")
            batch[stock] = dict(p400=p400, p1000=p1000, path=item["path"], sha256=item["sha256"])
        weeks[item["date"]] = batch
    if len(weeks) != original["expected_tdcc_weeks"] or total != original["expected_tdcc_rows"]:
        raise ValueError("TDCC total week/row count mismatch")
    return weeks


def normalized_weekly(weeks):
    anchors = {}
    for date in sorted(weeks):
        for stock, values in sorted(weeks[date].items()):
            complete = all(values[key] is not None for key in ("p400", "p1000"))
            if complete and stock not in anchors:
                anchors[stock] = (date, values["p400"], values["p1000"])
            anchor = anchors.get(stock)
            with localcontext() as ctx:
                ctx.prec = 50
                yield dict(stock_id=stock, batch_date=date, source_path=values["path"], source_sha256=values["sha256"],
                           complete=complete, unsupported_reasons="" if complete else "required_holding_bin_missing",
                           anchor_date=anchor[0] if anchor else "", offset400_pp=wire(values["p400"] - anchor[1]) if complete else "",
                           offset1000_pp=wire(values["p1000"] - anchor[2]) if complete else "", formal_use=False, promotion_evidence_allowed=False)


def published_weeks(payload, original):
    sources = {item["date"]: item for item in original["external_files"] if item["kind"] == "tdcc"}
    weeks, anchors, previous = {date: {} for date in sources}, {}, None
    for row in records("weekly_features", payload):
        day, stock = row["batch_date"], row["stock_id"]
        key = day, stock
        if previous is not None and key <= previous:
            raise ValueError("weekly identities duplicate or not sorted")
        previous = key
        if day not in sources or not re.fullmatch(r"[1-9][0-9]{3}", stock):
            raise ValueError("weekly source date/stock outside frozen scope")
        source = sources[day]
        if row["source_path"] != source["path"] or row["source_sha256"] != source["sha256"]:
            raise ValueError("weekly source SHA/path binding mismatch")
        if any(row[flag] != "False" for flag in ("formal_use", "promotion_evidence_allowed")):
            raise ValueError("weekly research-only flags changed")
        complete = true(row["complete"])
        a, b = decimal(row["offset400_pp"]), decimal(row["offset1000_pp"])
        if complete:
            if a is None or b is None or row["unsupported_reasons"]:
                raise ValueError("complete weekly row requires finite offsets")
            if stock not in anchors:
                anchors[stock] = day
                if a != 0 or b != 0:
                    raise ValueError("first complete batch must have zero offsets")
        elif a is not None or b is not None or row["offset400_pp"] or row["offset1000_pp"] or row["unsupported_reasons"] != "required_holding_bin_missing":
            raise ValueError("incomplete weekly row cannot fill missing offsets")
        if row["anchor_date"] != anchors.get(stock, ""):
            raise ValueError("weekly anchor changed or uses future batch")
        weeks[day][stock] = dict(p400=a, p1000=b, path=source["path"], sha256=source["sha256"])
    if any(not batch for batch in weeks.values()):
        raise ValueError("weekly features omit an entire frozen batch")
    return weeks


def baseline_four(weeks, date, stock):
    dates = sorted(day for day in weeks if day <= date)[-4:]
    existing = [day for day in dates if stock in weeks[day]]
    rows = [weeks[day][stock] for day in existing]
    complete = len(rows) == 4 and all(row[key] is not None for row in rows for key in ("p400", "p1000"))
    result = dict(supported=complete, dates=existing)
    if not complete:
        return result
    a, b = ([float(row[key]) for row in rows] for key in ("p400", "p1000"))
    da, db = a[-1] - a[0], b[-1] - b[0]
    ua, ub = (sum(y > x for x, y in zip(values, values[1:])) for values in (a, b))
    if da > 0 and db > 0 and min(ua, ub) >= 2:
        enum, desc = "strong_accumulation", "近幾週400張與1000張同步累積"
    elif da > 0 and db > 0:
        enum, desc = "mild_accumulation", "近幾週400張與1000張合計增加"
    elif da > 0 or db > 0:
        enum, desc = "mild_accumulation", "近幾週其中一項大戶級距增加"
    elif da < 0 and db < 0:
        enum, desc = "distribution_warning", "近幾週400張與1000張同步減少"
    elif da < 0 or db < 0:
        enum, desc = "distribution_warning", "近幾週其中一項大戶級距減少"
    else:
        enum, desc = "neutral", "近幾週TDCC無明顯累積"
    result.update(enum=enum, description=desc, delta400=round(da, 4), delta1000=round(db, 4), up400=ua, up1000=ub,
                  selected=enum in {"strong_accumulation", "mild_accumulation"})
    return result


def valid_price(row):
    if not row:
        return False
    numbers = {key: decimal(row.get(key)) for key in ("open", "high", "low", "close")}
    if any(value is None or value <= 0 for value in numbers.values()):
        return False
    return (numbers["low"] <= numbers["open"] <= numbers["high"] and numbers["low"] <= numbers["close"] <= numbers["high"]
            and not any(row.get(key) for key in ("duplicate_key", "date_mismatch", "alias_payload_conflict")))


def price_qualifier(row):
    n = {key: float(value) if (value := decimal(row.get(key))) is not None else None for key in ("close", "open", "high", "low", "previous_close", "volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today", "daily_return_calc", "return_5d", "return_20d", "high_20", "low_20")}
    c, o, h, low, prev = (n[key] for key in ("close", "open", "high", "low", "previous_close"))
    v, lots, level = (n[key] for key in ("volume_ratio", "volume_ma20_lots", "previous_20d_high_ex_today"))
    bullish = c is not None and o is not None and (c > o or (c == o and prev is not None and c > prev))
    breakout = all(value is not None for value in (c, v, lots, level)) and c >= level * 1.02 and v >= 2 and lots >= 1000 and bullish
    locked = False
    if all(value is not None for value in (c, o, h, low, level, n["daily_return_calc"])):
        narrow = h == low or (prev is not None and prev > 0 and (h - low) / prev * 100 <= 1)
        locked = c >= level * 1.02 and n["daily_return_calc"] >= 9 and c >= h * .995 and o >= c * .995 and narrow
    attack = bool(breakout or locked)
    failed = ["attack_already_started"] if attack else []
    for key, passed in (("volume_below_2_5", v is None or v < 2.5), ("short_not_attacked", n["return_5d"] is None or n["return_5d"] < 8), ("not_rallied", n["return_20d"] is None or n["return_20d"] < 20), ("in_recent_range_10pct", all(n[key] is not None for key in ("close", "high_20", "low_20")) and n["high_20"] > n["low_20"] and n["low_20"] * .9 <= c <= n["high_20"] * 1.1)):
        if not passed:
            failed.append(key)
    return not failed, failed, attack


def holding_dates(calendar, signal_date, horizon, as_of=AS_OF):
    entry = bisect.bisect_right(calendar, signal_date)
    if horizon not in HORIZONS or entry == 0 or calendar[entry - 1] != signal_date or entry >= len(calendar):
        raise ValueError("holding horizon or signal calendar identity invalid")
    target = entry + horizon
    return dict(entry_date=calendar[entry], exit_date=calendar[target] if target < len(calendar) else "", entry_index=entry,
                exit_target_index=target, mature=target < bisect.bisect_right(calendar, as_of))


def partition(entry_date, exit_date, split=SPLIT):
    return "validation" if entry_date >= split else "training" if exit_date and exit_date < split else "purged_cross_split"


def cashflows(entry_open, exit_close, slippage_bps):
    entry, exit_ = decimal(entry_open), decimal(exit_close)
    if entry is None or exit_ is None or min(entry, exit_) <= 0 or slippage_bps not in SLIPPAGES:
        raise ValueError("invalid positive prices or fixed slippage")
    with localcontext() as ctx:
        ctx.prec = 50
        slip = Decimal(slippage_bps) / 10000
        buy, sell = entry * 1000 * (1 + slip), exit_ * 1000 * (1 - slip)
        bf, sf, tax = max(Decimal(20), buy * Decimal("0.001425")), max(Decimal(20), sell * Decimal("0.001425")), sell * Decimal("0.003")
        cost, proceeds = buy + bf, sell - sf - tax
        pnl = proceeds - cost
        return dict(entry_open=str(entry), exit_close=str(exit_), shares="1000", entry_notional=str(buy), buy_fee=str(bf), entry_cash=str(cost),
                    exit_notional=str(sell), sell_fee=str(sf), sell_tax=str(tax), net_exit_cash=str(proceeds), net_pnl=str(pnl),
                    gross_return_pct=str((exit_ / entry - 1) * 100), net_return_pct=str(pnl / cost * 100), outcome="win" if pnl > 0 else "failure" if pnl < 0 else "neutral")


def derive_price_row(date, stock, price, history, calendar, excluded_closed, original, baseline):
    observations = list(history)[-21:]
    reasons = []
    if not valid_price(price):
        reasons.append("signal_ohlc_invalid_or_conflicting")
    if len(observations) < 21:
        reasons.append("insufficient_21_observations")
    if not all(valid_price(item) for item in observations):
        reasons.append("history_ohlc_invalid_or_conflicting")
    if any(item["volume"] is None or item["volume"] < 0 for item in observations[-20:]):
        reasons.append("volume_missing_or_negative")
    if any(item["source"] == "TPEX_OLD_DAILY_JSON" for item in observations[-20:]):
        reasons.append("raw_volume_lineage_unresolved")
    row = {key: "" for key in annual_io.FEATURE_FIELDS}
    row.update(stock_id=stock, stock_name=price["stock_name"], market=price["market"], signal_date=date,
               tdcc_price_phase="", tdcc_status="", volume_confirmed_breakout=False,
               **{key: wire(price[key]) for key in ("open", "high", "low", "close")})
    derived = {}
    if len(observations) == 21 and all(valid_price(item) for item in observations):
        current, previous, first = price["close"], observations[-2]["close"], observations[0]["close"]
        derived.update(return_5d=(current / observations[-6]["close"] - 1) * 100, return_20d=(current / first - 1) * 100,
                       daily_return_calc=(current / previous - 1) * 100, previous_close=previous,
                       high_20=max(item["high"] for item in observations[-20:]), low_20=min(item["low"] for item in observations[-20:]),
                       previous_20d_high_ex_today=max(item["high"] for item in observations[:-1]))
        if all(item["volume"] is not None and item["volume"] >= 0 for item in observations[-20:]):
            average = statistics.mean(item["volume"] for item in observations[-20:])
            if average > 0:
                derived.update(volume_ma20=average, volume_ma20_lots=average / 1000, volume_ratio=price["volume"] / average)
            else:
                reasons.append("volume_mean_zero")
    row.update({key: format(round(value, 4), ".4f") for key, value in derived.items()})
    qualified, rejected, attack = price_qualifier(row)
    old_reasons = reasons + ([] if baseline["supported"] else ["tdcc_four_batch_coverage_missing"])
    if baseline["supported"]:
        row.update(tdcc_accumulation_signal=baseline["enum"], tdcc_accumulation_description=baseline["description"],
                   tdcc_400_change_sum=baseline["delta400"], tdcc_1000_change_sum=baseline["delta1000"],
                   tdcc_400_up_weeks=baseline["up400"], tdcc_1000_up_weeks=baseline["up1000"])
    observed = [item["date"] for item in observations]
    missing = [day for day in calendar if observed and observed[0] <= day <= date and day not in observed]
    batches = sorted(item["date"] for item in original["external_files"] if item["kind"] == "tdcc" and item["date"] <= date)[-4:]
    batch_paths = {item["date"]: item["path"] for item in original["external_files"] if item["kind"] == "tdcc"}
    row.update(feature_id=date + ":" + stock, input_ref=PRICE_REF, receipt_id="", available_no_later_than="", entry_cutoff="",
               universe_source_path=price["source_path"], universe_source_sha256=price["source_sha256"], observed_history_dates=";".join(observed),
               history_observations=len(observed), history_missing_session_dates=";".join(missing), history_gap_count=len(missing),
               historical_closed_date_files_excluded=";".join(day for day in sorted(excluded_closed) if day <= date),
               tdcc_window_dates=";".join(baseline["dates"]), tdcc_paths=";".join(batch_paths[day] for day in batches),
               phase_policy="phase_classifier_not_invoked", instrument_note="possible_TDR_91_prefix" if stock.startswith("91") else "four_digit_nonzero_equity_code",
               input_availability_proven=False, feature_supported=not old_reasons, unsupported_reasons=";".join(old_reasons),
               raw_selector_selected=qualified and baseline.get("selected", False), selected=not old_reasons and qualified and baseline.get("selected", False),
               positive_resolution="recognized_enum_positive_fallback" if baseline.get("selected") else "recognized_enum_nonpositive_fail_closed" if baseline["supported"] else "missing_positive_evidence_fail_closed",
               attack_already_started=attack, primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False,
               price_supported=not reasons, price_unsupported_reasons=";".join(reasons), price_qualified=not reasons and qualified,
               price_rejection_reasons=";".join(rejected), baseline_4_supported=baseline["supported"], baseline_4_selected=baseline.get("selected", False))
    return row


def cohort_decision(feature, profile, strategy):
    if profile not in PROFILES or strategy not in PROFILES[profile]:
        raise ValueError("unknown profile/strategy pair")
    common = 0 if profile == "full_available" else 8 if profile == "common_8" else 12
    eligible = not common or true(feature[f"w{common}_supported"])
    prefix = "baseline_4" if strategy == "baseline_4" else "w" + strategy.split("_")[1]
    supported, selected = true(feature[prefix + "_supported"]), true(feature[prefix + "_selected"])
    return eligible, supported, eligible and supported and selected


def ledger_rows(features, prices, calendar, profile, strategy, horizon, as_of=AS_OF, split=SPLIT):
    held = {}
    for feature in features:
        date, stock = feature["signal_date"], feature["stock_id"]
        target = holding_dates(calendar, date, horizon, as_of)
        mature = target.pop("mature")
        entry, exit_ = target["entry_date"], target["exit_date"]
        common = dict(profile=profile, strategy=strategy, partition=partition(entry, exit_, split), feature_id=feature["feature_id"],
                      signal_date=date, stock_id=stock, horizon=horizon, **target)
        eligible, supported, selected = cohort_decision(feature, profile, strategy)
        if not selected:
            reason = "cohort_data_ineligible" if not eligible else "strategy_feature_unsupported" if not supported else "strategy_rule_false"
            yield "blocked", dict(common, record_type="qualification_decision", reasons=reason, primary_row_retained=True)
            continue
        ep = prices.daily(entry)[0].get(stock) if entry <= as_of else None
        strict = "blocked_entry_after_as_of" if entry > as_of else "blocked_entry_price" if not valid_price(ep) else "blocked_input_availability_unproven"
        common["strict_v3_status"] = strict
        yield "blocked", dict(common, record_type="strict_ledger_decision", reasons=strict, entry_open=ep["open"] if ep else "",
                              strict_entry_established=False, strict_prior_position_locked=False, proxy_result_must_not_release_strict_lock=True)
        prior = held.get(stock)
        reason = ("blocked_exit_day" if date == prior else "blocked_active_position") if prior and date <= prior else "entry_after_as_of" if entry > as_of else "entry_price_missing_or_invalid" if not valid_price(ep) else ""
        if reason:
            yield "blocked", dict(common, record_type="operation_no_entry", reasons=reason)
            continue
        xp = prices.daily(exit_)[0].get(stock) if mature else None
        held[stock] = exit_ if mature and valid_price(xp) else "99999999"
        if not mature or not valid_price(xp):
            yield "blocked", dict(common, record_type="operation_censored", reasons="open_immature" if not mature else "open_unresolved_exit_price", entry_open=ep["open"])
            continue
        for slip in SLIPPAGES:
            yield "trades", dict(common, trade_id=f"{profile}:{strategy}:{date}:{stock}:D{horizon}:S{slip}", stock_name=feature["stock_name"], market=feature["market"],
                                 slippage_bps=slip, **cashflows(ep["open"], xp["close"], slip), simulation_status="realized_raw_price_proxy",
                                 strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit", ca_cashflow_assumption="not_applied_not_asserted_absent",
                                 total_return_verified=False, input_ref=PRICE_REF, receipt_id="", outcome_ref=PRICE_REF,
                                 entry_source_path=ep["source_path"], entry_source_sha256=ep["source_sha256"], exit_source_path=xp["source_path"], exit_source_sha256=xp["source_sha256"],
                                 history_gap_count=feature["history_gap_count"], anomaly_candidate=False, primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False)


def anomaly_key(row):
    return row["signal_date"], row["stock_id"], int(row["horizon"])


def anomaly_detections(trades):
    result = []
    for horizon in HORIZONS:
        sample = [row for row in trades if int(row["horizon"]) == horizon and int(row["slippage_bps"]) == 10]
        if len(sample) < 4:
            continue
        first, _, third = statistics.quantiles([float(row["net_return_pct"]) for row in sample], n=4, method="inclusive")
        low, high = first - 3 * (third - first), third + 3 * (third - first)
        for row in sample:
            if not low <= float(row["net_return_pct"]) <= high:
                result.append(dict(signal_date=row["signal_date"], stock_id=row["stock_id"], horizon=horizon,
                                   detector_profile=row["profile"], detector_strategy=row["strategy"], q1=first, q3=third, lower_fence=low, upper_fence=high))
    return result


def anomaly_rows(trades, prior_keys, detections):
    keys = set(prior_keys) | set(detections)
    result = []
    for trade in trades:
        key = anomaly_key(trade)
        trade["anomaly_candidate"] = key in keys
        if key not in keys or int(trade["slippage_bps"]) != 10:
            continue
        causes = list(detections.get(key, []))
        if key in prior_keys:
            causes.insert(0, dict(detector_profile="immutable_prior", detector_strategy="", q1="", q3="", lower_fence="", upper_fence=""))
        for cause in causes:
            result.append(dict(profile=trade["profile"], strategy=trade["strategy"], partition=trade["partition"], slippage_bps=10,
                               signal_date=trade["signal_date"], stock_id=trade["stock_id"], horizon=trade["horizon"], net_return_pct=trade["net_return_pct"],
                               reason="immutable_previous_candidate_retained" if cause["detector_profile"] == "immutable_prior" else "full_ledger_Q1_Q3_plus_3IQR_candidate_union",
                               disposition="unresolved_anomaly_candidate", primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True,
                               entry_date=trade["entry_date"], exit_date=trade["exit_date"], represented_in_current_proxy_trade=True,
                               **{field: cause[field] for field in ("detector_profile", "detector_strategy", "q1", "q3", "lower_fence", "upper_fence")}))
    return result


def statistics_row(values):
    n = len(values)
    wins, neutrals, failures = (sum(test(value) for value in values) for test in (lambda x: x > 0, lambda x: x == 0, lambda x: x < 0))
    return dict(win_count=wins, neutral_count=neutrals, failure_count=failures,
                win_rate_pct=100 * wins / n if n else "", neutral_rate_pct=100 * neutrals / n if n else "", failure_rate_pct=100 * failures / n if n else "",
                mean_net_return_pct=statistics.mean(values) if n else "", median_net_return_pct=statistics.median(values) if n else "",
                high_return_ge10_rate_pct=100 * sum(value >= 10 for value in values) / n if n else "", loss_le_minus10_rate_pct=100 * sum(value <= -10 for value in values) / n if n else "",
                min_net_return_pct=min(values) if n else "", max_net_return_pct=max(values) if n else "")


def summaries(trades, blocked, features, calendar, profile, strategy):
    result = []
    for horizon in HORIZONS:
        counts = Counter()
        for feature in features:
            target = holding_dates(calendar, feature["signal_date"], horizon)
            part = partition(target["entry_date"], target["exit_date"])
            eligible, supported, _ = cohort_decision(feature, profile, strategy)
            for p in ("all", part):
                counts[p, "price"] += 1
                counts[p, "eligible"] += eligible
                counts[p, "supported"] += eligible and supported
        for part in PARTITIONS:
            reasons = Counter()
            for (p, h, kind, reason), n in blocked.items():
                if h == horizon and (part == "all" or p == part):
                    reasons[kind, reason] += n
            def count(kind, reason=None):
                return sum(n for (k, r), n in reasons.items() if k == kind and (reason is None or r == reason))
            for slip in SLIPPAGES:
                sample = [row for row in trades if row["horizon"] == horizon and row["slippage_bps"] == slip and (part == "all" or row["partition"] == part)]
                for population in ("primary", "sensitivity_excluding_candidates"):
                    members = [row for row in sample if population == "primary" or not row["anomaly_candidate"]]
                    result.append(dict(profile=profile, strategy=strategy, horizon=horizon, slippage_bps=slip, partition=part, population=population,
                                       samples=len(members), stocks=len({row["stock_id"] for row in members}), signal_dates=len({row["signal_date"] for row in members}), entry_dates=len({row["entry_date"] for row in members}),
                                       price_qualified_rows=counts[part, "price"], cohort_eligible_rows=counts[part, "eligible"], strategy_supported_rows=counts[part, "supported"],
                                       selected_signals=count("strict_ledger_decision"), unsupported_rows=count("qualification_decision", "strategy_feature_unsupported"),
                                       cohort_ineligible_rows=count("qualification_decision", "cohort_data_ineligible"), rejected_rows=count("qualification_decision", "strategy_rule_false"),
                                       overlap_blocked_signals=count("operation_no_entry", "blocked_active_position") + count("operation_no_entry", "blocked_exit_day"),
                                       missing_entry_signals=count("operation_no_entry", "entry_price_missing_or_invalid"), entry_after_as_of_signals=count("operation_no_entry", "entry_after_as_of"),
                                       immature_positions=count("operation_censored", "open_immature"), missing_exit_positions=count("operation_censored", "open_unresolved_exit_price"),
                                       purged_positions=sum(row["partition"] == "purged_cross_split" for row in members), anomaly_candidate_positions=sum(row["anomaly_candidate"] for row in members),
                                       **statistics_row([float(row["net_return_pct"]) for row in members]), formal_use=False, promotion_evidence_allowed=False))
    return result


def type7(values, probability):
    if not values:
        return None
    ordered = sorted(values)
    with localcontext() as ctx:
        ctx.prec = 50
        index = Decimal(len(values) - 1) * Decimal(probability)
        left = int(index)
        return ordered[left] + (ordered[min(left + 1, len(values) - 1)] - ordered[left]) * (index - left)


def outcome_group(value):
    value = decimal(value)
    if value is None:
        raise ValueError("outcome comparison requires finite realized return")
    return "high" if value >= 10 else "low" if value <= -10 else "middle"


def feature_contrasts(trades, by_id, prior_keys, profile, strategy):
    for horizon in HORIZONS:
        for slip in SLIPPAGES:
            for part in PARTITIONS:
                sample = [row for row in trades if row["horizon"] == horizon and row["slippage_bps"] == slip and (part == "all" or row["partition"] == part)]
                for population in ("primary", "immutable_prior_candidate_exclusion_sensitivity"):
                    subset = [row for row in sample if population == "primary" or anomaly_key(row) not in prior_keys]
                    for group in ("all_realized", "high", "low", "middle"):
                        members = [row for row in subset if group == "all_realized" or outcome_group(row["net_return_pct"]) == group]
                        for field in CONTRAST_FIELDS:
                            values = [decimal(by_id[row["feature_id"]].get(field)) for row in members]
                            valid = [value for value in values if value is not None]
                            with localcontext() as ctx:
                                ctx.prec = 50
                                yield dict(profile=profile, strategy=strategy, horizon=horizon, slippage_bps=slip, partition=part, population=population,
                                           feature_name=field, outcome_group=group, samples=len(members), valid_samples=len(valid), missing_samples=len(members) - len(valid),
                                           mean=str(sum(valid) / len(valid)) if valid else "", median=wire(type7(valid, ".5")), q25=wire(type7(valid, ".25")),
                                           q75=wire(type7(valid, ".75")), minimum=str(min(valid)) if valid else "", maximum=str(max(valid)) if valid else "")


def load_context(repository_root, contract, *, input_root=None, price_repository_root=None, published_only=False):
    git = annual_io.GitReader(price_repository_root or repository_root)
    original = json.loads(git.read(BASE_REF, annual_io.CONTRACT_FILE))
    if digest(canonical_json(original)) != annual_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual contract SHA mismatch")
    base_manifest = json.loads(git.read(BASE_REF, DIRECTORY + "/" + annual_io.artifact_name("source_manifest")))
    if base_manifest["contract"] != original or base_manifest["contract_sha256"] != annual_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual manifest contract mismatch")
    controls = {}
    for kind in ("features", "signals"):
        name = annual_io.artifact_name(kind)
        data = git.read(BASE_REF, DIRECTORY + "/" + name)
        if base_manifest["hashes"][name] != dict(bytes=len(data), sha256=digest(data)):
            raise ValueError("immutable all-features/signal control serialized binding mismatch")
        controls[kind] = data
    prior, prior_evidence = set(), []
    for source in contract["anomaly_retention_sources"]:
        payload = git.read(source["ref"], source["path"])
        rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline="")))
        prior.update(anomaly_key(row) for row in rows)
        prior_evidence.append(dict(source, sha256=digest(payload), rows=len(rows)))
    git.read(original["classifier_ref"], "tdcc_trend_utils.py")
    if git.used[original["classifier_ref"], "tdcc_trend_utils.py"]["git_blob_oid"] != original["classifier_blob_oid"]:
        raise ValueError("immutable classifier provenance blob mismatch")
    closures = set()
    for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
        closures.update(row["date"] for row in annual_io.csv_records(git.read(PRICE_REF, path)))
    inputs, weeks = None, None
    if published_only:
        # The calendar's private-only dates are frozen control, not raw rereads.
        closures.update(base_manifest["evidence"]["calendar_closures"])
        prices = horizon_io.PublishedPrices(git, original, controls["features"])
        price_dates = {path[-12:-4] for path in git.tree(PRICE_REF) if re.fullmatch(r"data/daily_price/[0-9]{8}\.csv", path)
                       and original["history_start"] <= path[-12:-4] <= AS_OF} | {"20250915"}
    else:
        if input_root is None:
            raise ValueError("full source validation requires --input-root")
        inputs = annual_io.PrivateInputs(input_root, original)
        weeks = raw_tdcc(inputs, original)
        prices = annual_io.CurrentPrices(git, inputs, original)
        price_dates = prices.dates
        for item in original["external_files"]:
            if item["kind"] == "calendar":
                closures.update(row["date"] for row in annual_io.csv_records(inputs.read(item)) if row["scheduled_closed"] == "True")
        if len(inputs.used) != 65:
            raise ValueError("full source verification did not read all 65 exact private files")
    closures = sorted(closures)
    if closures != base_manifest["evidence"]["calendar_closures"]:
        raise ValueError("independent official-calendar closure union mismatch")
    calendar = session_calendar(closures, original["history_start"], original["calendar_end"])
    return dict(git=git, original=original, original_manifest=base_manifest, controls=controls, prices=prices, price_dates=price_dates,
                closures=closures, calendar=calendar, inputs=inputs, weeks=weeks, prior=prior, prior_evidence=prior_evidence, published_only=published_only)


def public_price_control(control, price, baseline):
    """Immutable price/warmup and original-float control, never a universe source."""
    row = dict(control)
    for key in ("stock_id", "stock_name", "market", "universe_source_path", "universe_source_sha256"):
        source_key = {"universe_source_path": "source_path", "universe_source_sha256": "source_sha256"}.get(key, key)
        if wire(row[key]) != wire(price[source_key]):
            raise ValueError("published Git universe/control row provenance mismatch: " + key)
    for key in ("open", "high", "low", "close"):
        if decimal(row[key]) != decimal(price[key]):
            raise ValueError("published Git current OHLC/control mismatch: " + key)
    if row["tdcc_window_dates"] != ";".join(baseline["dates"]):
        raise ValueError("baseline control batch dates differ from normalized weekly membership")
    complete = baseline["supported"]
    enum = row["tdcc_accumulation_signal"]
    if complete != bool(enum):
        raise ValueError("baseline control completeness differs from normalized weekly membership")
    if enum not in {"", "strong_accumulation", "mild_accumulation", "distribution_warning", "neutral"}:
        raise ValueError("baseline immutable classification enum invalid")
    positive = enum in {"strong_accumulation", "mild_accumulation"}
    price_reasons = [reason for reason in row["unsupported_reasons"].split(";") if reason and reason not in {"tdcc_four_batch_coverage_missing", "tdcc_effective_date_mismatch"}]
    qualified, rejected, attack = price_qualifier(row)
    row.update(price_supported=not price_reasons, price_unsupported_reasons=";".join(price_reasons),
               price_qualified=not price_reasons and qualified, price_rejection_reasons=";".join(rejected),
               baseline_4_supported=complete, baseline_4_selected=positive)
    if true(row["selected"]) != (not price_reasons and complete and qualified and positive) or true(row["attack_already_started"]) != attack:
        raise ValueError("immutable baseline control/frozen price decision mismatch")
    return row


def audit_features(context, contract, artifacts):
    original, calendar, prices = context["original"], context["calendar"], context["prices"]
    weeks = context["weeks"]
    if context["published_only"]:
        weeks = published_weeks(artifacts[artifact_name("weekly_features")], original)
    else:
        compare_sequence("weekly_features", records("weekly_features", artifacts[artifact_name("weekly_features")]), normalized_weekly(weeks))
    weekly_count = sum(len(batch) for batch in weeks.values())
    controls = iter(annual_io.rows_for("features", context["controls"]["features"]))
    old_signals = iter(annual_io.rows_for("signals", context["controls"]["signals"]))
    actual = iter(records("features", artifacts[artifact_name("features")]))
    history, qualified_features, coverage = defaultdict(lambda: deque(maxlen=21)), [], []
    dates = iter(sorted(context["price_dates"] & set(calendar)))
    pending = next(dates, None)
    excluded = set(context["price_dates"]) & set(context["closures"])
    version, window_cache, four_cache = None, {}, {}
    count_rows = baseline_count = 0
    pool = {}
    keep = tuple(dict.fromkeys(("feature_id", "signal_date", "stock_id", "stock_name", "market", "price_qualified", "baseline_4_supported", "baseline_4_selected",
                               "w8_supported", "w8_selected", "w12_supported", "w12_selected", *CONTRAST_FIELDS)))
    for date in (day for day in calendar if contract["requested_signal_start"] <= day <= contract["requested_signal_end"]):
        if not context["published_only"]:
            while pending is not None and pending <= date:
                for stock, item in prices.daily(pending)[0].items():
                    history[stock].append(item)
                pending = next(dates, None)
        current = (max((day for day in weeks if day <= date), default=""), monday(date))
        if current != version:
            version, window_cache, four_cache = current, {}, {}
        counts, reasons = Counter(), {"price": Counter(), 8: Counter(), 12: Counter()}
        # Membership comes from daily source quotes, not from old features/signals.
        for stock, price in sorted(prices.daily(date)[0].items()):
            frozen = next(controls, None)
            if frozen is None or (frozen["signal_date"], frozen["stock_id"]) != (date, stock):
                raise ValueError("Git daily full-universe differs from immutable all-feature control")
            if stock not in four_cache:
                four_cache[stock] = baseline_four(weeks, date, stock)
            baseline = four_cache[stock]
            if context["published_only"]:
                row = public_price_control(frozen, price, baseline)
            else:
                row = derive_price_row(date, stock, price, history[stock], calendar, excluded, original, baseline)
                for key in annual_io.FEATURE_FIELDS:
                    if wire(row[key]) != frozen[key]:
                        raise ValueError(f"raw independent annual full-universe control mismatch: {date}:{stock}:{key}")
            if row["historical_closed_date_files_excluded"] != ";".join(day for day in sorted(excluded) if day <= date):
                raise ValueError("excluded closed dates must bind actual existing price files")
            if true(row["selected"]):
                if next(old_signals, None) != frozen:
                    raise ValueError("independent baseline4 selected set differs from frozen control")
                baseline_count += 1
            for n in (8, 12):
                if (stock, n) not in window_cache:
                    window_cache[stock, n] = window_metrics(weeks, date, stock, n, calendar, original["history_start"], original["calendar_end"])
                row.update({f"w{n}_{key}": value for key, value in window_cache[stock, n].items()})
            compare_row("features", next(actual, None), row)
            count_rows += 1
            counts["raw"] += 1
            counts["price_supported"] += true(row["price_supported"])
            counts["price_qualified"] += true(row["price_qualified"])
            counts["tdr"] += stock.startswith("91")
            reasons["price"].update(filter(None, row["price_unsupported_reasons"].split(";")))
            if true(row["price_qualified"]):
                small = {key: row[key] for key in keep}
                for key in ("signal_date", "stock_id", "stock_name", "market"):
                    small[key] = pool.setdefault(small[key], small[key])
                qualified_features.append(small)
                counts["baseline_supported"] += true(row["baseline_4_supported"])
                counts["baseline_selected"] += true(row["baseline_4_supported"]) and true(row["baseline_4_selected"])
                for n in (8, 12):
                    counts[f"supported{n}"] += true(row[f"w{n}_supported"])
                    counts[f"selected{n}"] += true(row[f"w{n}_selected"])
                    reasons[n].update(filter(None, row[f"w{n}_reasons"].split(";")))
        coverage.append(dict(signal_date=date, raw_universe_rows=counts["raw"], price_supported_rows=counts["price_supported"], price_qualified_rows=counts["price_qualified"],
                             baseline_4_supported_rows=counts["baseline_supported"], baseline_4_signals=counts["baseline_selected"],
                             trend_8_supported_rows=counts["supported8"], trend_8_signals=counts["selected8"], trend_12_supported_rows=counts["supported12"], trend_12_signals=counts["selected12"],
                             common_8_eligible_rows=counts["supported8"], common_12_eligible_rows=counts["supported12"], price_unsupported_reason_counts=json.dumps(dict(reasons["price"]), sort_keys=True),
                             trend_8_unsupported_reason_counts=json.dumps(dict(reasons[8]), sort_keys=True), trend_12_unsupported_reason_counts=json.dumps(dict(reasons[12]), sort_keys=True),
                             possible_tdr_rows=counts["tdr"], formal_use=False, promotion_evidence_allowed=False))
    if any(next(iterator, None) is not None for iterator in (actual, controls, old_signals)):
        raise ValueError("unmatched extra features or immutable baseline controls")
    if count_rows != context["original_manifest"]["counts"]["covered_universe_rows"] or baseline_count != context["original_manifest"]["counts"]["signals"]:
        raise ValueError("independent full-universe/baseline population control count mismatch")
    compare_sequence("coverage", records("coverage", artifacts[artifact_name("coverage")]), coverage)
    counts = dict(universe_rows=count_rows, price_supported_rows=sum(row["price_supported_rows"] for row in coverage), price_qualified_rows=len(qualified_features),
                  baseline_4_control_signals=baseline_count, possible_tdr_rows=sum(row["possible_tdr_rows"] for row in coverage), weekly_features=weekly_count, features=count_rows, coverage=len(coverage))
    return qualified_features, coverage, counts


class OperationPrices:
    """One cached quote panel for repeated independent ledgers; no business rules."""
    def __init__(self, source, dates):
        self.values = {}
        fields = ("open", "high", "low", "close", "source_path", "source_sha256", "duplicate_key", "date_mismatch", "alias_payload_conflict")
        for date in dates:
            self.values[date] = {stock: {key: row.get(key) for key in fields} for stock, row in source.daily(date)[0].items()}

    def daily(self, date):
        return self.values.get(date, {}), {}


def audit_source_bindings(context, contract, manifest):
    git, original = context["git"], context["original"]
    fixed = {(BASE_REF, annual_io.CONTRACT_FILE), (original["classifier_ref"], "tdcc_trend_utils.py"),
             (PRICE_REF, "config/twse_non_trading_days.csv"), (PRICE_REF, "data/market_calendar/exceptional_non_trading_days.csv")}
    fixed.update((BASE_REF, DIRECTORY + "/" + annual_io.artifact_name(kind)) for kind in ("source_manifest", "features", "signals"))
    fixed.update((row["ref"], row["path"]) for row in contract["anomaly_retention_sources"])
    seen = set()
    if manifest["sources"] != sorted(manifest["sources"], key=lambda row: (row["ref"], row["path"])):
        raise ValueError("manifest Git source order mismatch")
    for source in manifest["sources"]:
        key = source["ref"], source["path"]
        match = re.fullmatch(r"data/daily_price/([0-9]{8})\.csv", source["path"])
        permitted = key in fixed or (source["ref"] == PRICE_REF and match and original["history_start"] <= match[1] <= AS_OF)
        if key in seen or not permitted:
            raise ValueError("manifest duplicate/unapproved Git source")
        seen.add(key)
        if key not in git.used:
            git.read(*key)
        if source != git.used[key]:
            raise ValueError("manifest Git source bytes/blob/SHA mismatch: " + source["path"])
    if not fixed <= seen:
        raise ValueError("manifest missing required immutable controls/calendar/classifier/prior source")
    # All daily quotes actually consumed must be bound, not merely a subset.
    if not {key for key in git.used if re.fullmatch(r"data/daily_price/[0-9]{8}\.csv", key[1])} <= seen:
        raise ValueError("manifest omits consumed immutable daily source")
    expected_external = original["external_files"]
    if len(manifest["external_sources"]) != 65:
        raise ValueError("manifest must bind exact 65 private sources")
    base_external = context["original_manifest"]["external_sources"]
    for actual, expected, prior in zip(manifest["external_sources"], expected_external, base_external):
        if {key: value for key, value in actual.items() if key != "bytes"} != expected or actual != prior:
            raise ValueError("external source exact path/hash/size control mismatch")
        if context["inputs"] is not None and actual != context["inputs"].used[expected["path"]]:
            raise ValueError("raw private source actual byte count mismatch")
    if manifest["prior_candidate_sources"] != context["prior_evidence"]:
        raise ValueError("prior anomaly source/count/hash provenance mismatch")


def preliminary_detections(payload):
    """Read a proposed detector union, later checked against every raw replay.

    This saves a second expensive price replay. The proposal is never accepted
    until independent cashflows reproduce each ledger's exact detector rows.
    """
    result, by_ledger, order = defaultdict(list), {}, []
    for key, group in groupby(records("trades", payload), key=lambda row: (row["profile"], row["strategy"])):
        if key in by_ledger or key[0] not in PROFILES or key[1] not in PROFILES[key[0]]:
            raise ValueError("trade ledger ordering or identity mismatch")
        order.append(key)
        sample = [{field: row[field] for field in ("profile", "strategy", "signal_date", "stock_id", "horizon", "slippage_bps", "net_return_pct")}
                  for row in group if row["slippage_bps"] == "10"]
        found = anomaly_detections(sample)
        by_ledger[key] = found
        for row in found:
            result[anomaly_key(row)].append(row)
    expected_order = [key for key in ((profile, strategy) for profile in PROFILES for strategy in PROFILES[profile]) if key in by_ledger]
    if order != expected_order:
        raise ValueError("trade ledgers not in frozen profile/strategy order")
    return result, by_ledger


def report_tables(payload):
    if payload.startswith(b"\xef\xbb\xbf") or b"\r" in payload or not payload.endswith(b"\n"):
        raise ValueError("report UTF-8/LF serialization mismatch")
    text = payload.decode("utf-8")
    result = {}
    for section in re.split(r"(?m)^## ", text)[1:]:
        title, _, body = section.partition("\n")
        if title in result:
            raise ValueError("duplicate report section")
        result[title] = [[cell.strip() for cell in line.strip().strip("|").split("|")]
                         for line in body.splitlines() if line.startswith("| ")][1:]
    return text, result


def compare_table(actual, expected, title):
    if actual is None or len(actual) != len(expected):
        raise ValueError("report table row count mismatch: " + title)
    for row, wanted in zip(actual, expected):
        if len(row) != len(wanted):
            raise ValueError("report table column count mismatch: " + title)
        for a, b in zip(row, wanted):
            if a == wire(b):
                continue
            # Compound win/neutral/failure cells contain three independent values.
            xs, ys = a.split("/"), wire(b).split("/")
            if len(xs) == len(ys) and all(x == y or (decimal(x) is not None and decimal(y) is not None and math.isclose(float(decimal(x)), float(decimal(y)), rel_tol=1e-12, abs_tol=1e-12)) for x, y in zip(xs, ys)):
                continue
            raise ValueError("report table numeric/identity mismatch: " + title)


def audit_report(payload, coverage, summary, contrasts, counts):
    text, tables = report_tables(payload)
    for marker in ("advisory-only", "formal_use=False", "promotion_evidence_allowed=False", "不是strict PIT", "total-return", "不是genuine unseen OOS",
                   "selected signals", "exact", "split不重置", "purged", "high>=10%", "low<=-10%", "negative<0", "候選全留primary", "不是corrected/cleaned performance",
                   "published-only不能聲稱重讀私有原文", "兩級距重疊", "月營收", "EPS", "季／年財報全排除"):
        if marker == "exact":
            marker = "精確分子皆>0"
        if marker not in text:
            raise ValueError("report missing required limitation: " + marker)
    main_count = f"原始母體{counts['universe_rows']}列；price-supported {counts['price_supported_rows']}列；price-qualified {counts['price_qualified_rows']}列；可能TDR {counts['possible_tdr_rows']}列。"
    candidate_count = f"既有候選鍵{counts['prior_candidate_keys']}；新增偵測ledger列{counts['new_candidate_detections']}；本次聯集候選鍵{counts['candidate_union_keys']}。"
    if main_count not in text or candidate_count not in text:
        raise ValueError("report universe/candidate counts mismatch")
    cover = [["baseline_4可支持", sum(row["baseline_4_supported_rows"] for row in coverage)],
             ["trend_8可支持／common_8資格", sum(row["trend_8_supported_rows"] for row in coverage)],
             ["trend_12可支持／common_12資格", sum(row["trend_12_supported_rows"] for row in coverage)]]
    compare_table(tables.get("覆蓋與共同資格"), cover, "coverage")
    for window in (8, 12):
        reasons = Counter()
        for row in coverage:
            reasons.update(json.loads(row[f"trend_{window}_unsupported_reason_counts"]))
        if f"`{json.dumps(dict(reasons), ensure_ascii=False, sort_keys=True)}`" not in text:
            raise ValueError("report missing-week/unsupported reason counts mismatch")
    contrast_lookup = {(row["profile"], row["strategy"], row["horizon"], row["slippage_bps"], row["partition"], row["population"], row["feature_name"], row["outcome_group"]): row for row in contrasts}
    contrast_table = []
    for profile, strategies in PROFILES.items():
        for strategy in strategies:
            for horizon in HORIZONS:
                for field in ("w8_slope400_pp_per_week", "w8_slope1000_pp_per_week", "w12_slope400_pp_per_week", "w12_slope1000_pp_per_week", "w8_net400_pp", "w8_last400_pp", "w8_max_positive_share400"):
                    contrast_table.append([profile, strategy, horizon, field] + [contrast_lookup[profile, strategy, horizon, 10, "all", "primary", field, group]["median"] for group in ("high", "low", "middle")])
    compare_table(tables.get("固定高／低報酬特徵對照（10 bps primary）"), contrast_table, "feature contrasts")
    primary, reasons = [], []
    for row in summary:
        if row["slippage_bps"] != 10:
            continue
        if row["partition"] in {"all", "training", "validation"}:
            primary.append([row[key] for key in ("profile", "strategy", "horizon", "partition", "population", "samples", "stocks", "signal_dates", "entry_dates")]
                           + [f"{row['win_count']}/{row['neutral_count']}/{row['failure_count']}", f"{row['win_rate_pct']}/{row['neutral_rate_pct']}/{row['failure_rate_pct']}"]
                           + [row[key] for key in ("mean_net_return_pct", "median_net_return_pct", "high_return_ge10_rate_pct", "loss_le_minus10_rate_pct")])
        if row["population"] == "primary":
            reasons.append([row[key] for key in ("profile", "strategy", "horizon", "partition", "unsupported_rows", "cohort_ineligible_rows", "rejected_rows", "overlap_blocked_signals", "missing_entry_signals", "entry_after_as_of_signals", "immature_positions", "missing_exit_positions", "purged_positions")])
    compare_table(tables.get("原始價格proxy主要與敏感性（10 bps）"), primary, "primary/sensitivity")
    compare_table(tables.get("未入場、未成熟及purged（10 bps primary）"), reasons, "censoring/locks")


def validate_artifacts(repository_root, contract, artifacts, *, input_root=None, price_repository_root=None, published_only=False):
    try:
        contract_audit(contract)
        if set(artifacts) != {artifact_name(kind) for kind in KINDS}:
            raise ValueError("all exact eleven published artifacts are required")
        if not published_only and input_root is None:
            raise ValueError("full source validation requires --input-root; public evidence requires explicit --published-only")
        manifest_payload = artifacts[artifact_name("source_manifest")]
        manifest = json.loads(manifest_payload)
        if canonical_json(manifest) != manifest_payload:
            raise ValueError("manifest must have canonical JSON bytes")
        header = dict(model_id="tdcc_stealth_accumulation", owner_id=OWNER, artifact_version=PREFIX + "v1", contract=contract, contract_file=CONTRACT_FILE, contract_sha256=APPROVED_CONTRACT_SHA256)
        if any(canonical_json(manifest.get(key)) != canonical_json(value) for key, value in header.items()) or any(manifest.get(flag) is not False for flag in FALSE_FLAGS):
            raise ValueError("manifest owner/contract/research-only flags mismatch")
        hashes = {name: dict(bytes=len(payload), sha256=digest(payload)) for name, payload in artifacts.items() if name != artifact_name("source_manifest")}
        if manifest["hashes"] != hashes:
            raise ValueError("manifest actual serialized ten-file hashes mismatch")
        context = load_context(repository_root, contract, input_root=input_root, price_repository_root=price_repository_root, published_only=published_only)
        calendar, original = context["calendar"], context["original"]
        if manifest["base_contract"] != original or manifest["calendar"] != dict(sessions=calendar, closures=context["closures"], history_start=original["history_start"], calendar_end=original["calendar_end"]):
            raise ValueError("manifest frozen base-contract or independent calendar mismatch")
        features, coverage, counts = audit_features(context, contract, artifacts)
        by_id = {row["feature_id"]: row for row in features}
        if len(by_id) != len(features):
            raise ValueError("duplicate price-qualified feature identity")
        prices = OperationPrices(context["prices"], [day for day in calendar if contract["requested_signal_start"] <= day <= AS_OF])
        # Proposed detector union is fully verified against each independent replay.
        detections, proposed = preliminary_detections(artifacts[artifact_name("trades")])
        candidate_keys = context["prior"] | set(detections)
        actual = {kind: iter(records(kind, artifacts[artifact_name(kind)])) for kind in ("signals", "trades", "blocked", "anomalies", "summary", "feature_contrasts")}
        cohorts, represented, totals, all_summary, report_contrasts = {}, set(), Counter(), [], []
        for profile, strategies in PROFILES.items():
            for strategy in strategies:
                eligible_ids, selected_count = [], 0
                for feature in features:
                    eligible, supported, selected = cohort_decision(feature, profile, strategy)
                    if eligible:
                        eligible_ids.append(feature["feature_id"])
                    if selected:
                        expected = dict(profile=profile, strategy=strategy, **{key: feature[key] for key in ("feature_id", "signal_date", "stock_id", "stock_name", "market", "history_gap_count")}, formal_use=False, promotion_evidence_allowed=False)
                        compare_row("signals", next(actual["signals"], None), expected)
                        selected_count += 1
                        totals["signals"] += 1
                cohorts[profile + ":" + strategy] = dict(eligible_rows=len(eligible_ids), eligible_keys_sha256=digest(canonical_json(eligible_ids)),
                                                        first_eligible_date=eligible_ids[0].split(":")[0] if eligible_ids else "", selected_signals=selected_count)
                trades, blocked = [], Counter()
                for horizon in HORIZONS:
                    for kind, expected in ledger_rows(features, prices, calendar, profile, strategy, horizon):
                        row = next(actual[kind], None)
                        if kind == "trades":
                            expected["anomaly_candidate"] = anomaly_key(expected) in candidate_keys
                        compare_row(kind, row, expected)
                        totals[kind] += 1
                        if kind == "blocked":
                            blocked[expected["partition"], horizon, expected["record_type"], expected["reasons"]] += 1
                        else:
                            kept = ("profile", "strategy", "partition", "feature_id", "signal_date", "stock_id", "horizon", "slippage_bps", "entry_date", "exit_date", "net_return_pct", "anomaly_candidate")
                            trades.append({key: expected[key] for key in kept})
                found = anomaly_detections(trades)
                if canonical_json(found) != canonical_json(proposed.get((profile, strategy), [])):
                    raise ValueError("proposed anomaly union differs from independent full-ledger cashflow detections")
                represented.update(anomaly_key(row) for row in trades)
                anomalies = anomaly_rows(trades, context["prior"], detections)
                for row in anomalies:
                    compare_row("anomalies", next(actual["anomalies"], None), row)
                totals["anomalies"] += len(anomalies)
                summary = summaries(trades, blocked, features, calendar, profile, strategy)
                for row in summary:
                    compare_row("summary", next(actual["summary"], None), row)
                all_summary.extend(summary)
                totals["summary"] += len(summary)
                for row in feature_contrasts(trades, by_id, context["prior"], profile, strategy):
                    compare_row("feature_contrasts", next(actual["feature_contrasts"], None), row)
                    totals["feature_contrasts"] += 1
                    if row["slippage_bps"] == 10 and row["partition"] == "all" and row["population"] == "primary":
                        report_contrasts.append(row)
        if any(next(iterator, None) is not None for iterator in actual.values()):
            raise ValueError("unexpected extra signal/operation/summary/anomaly/contrast rows")
        counts.update(totals)
        for kind in ("signals", "trades", "blocked", "summary", "anomalies", "feature_contrasts"):
            counts.setdefault(kind, 0)
        supplemental = context["prices"].supplemental_counts if context["inputs"] is not None else context["original_manifest"]["counts"]["supplemental"]
        counts.update(prior_candidate_keys=len(context["prior"]), prior_candidate_keys_represented=len(context["prior"] & represented),
                      prior_candidate_keys_unrepresented=len(context["prior"] - represented), new_candidate_detections=sum(map(len, detections.values())),
                      candidate_union_keys=len(candidate_keys), supplemental=supplemental)
        if manifest["counts"] != counts or manifest["cohorts"] != cohorts:
            raise ValueError("manifest independent count/cohort membership hashes mismatch")
        control = dict(ref=BASE_REF, full_universe_rows=counts["universe_rows"], selected_signals=counts["baseline_4_control_signals"], used_as_universe=False)
        if manifest["baseline_control"] != control:
            raise ValueError("baseline control cannot become selected-signal universe")
        audit_source_bindings(context, contract, manifest)
        audit_report(artifacts[artifact_name("report")], coverage, all_summary, report_contrasts, counts)
    except (AssertionError, KeyError, ValueError, TypeError, OSError, EOFError, zlib.error, csv.Error, ArithmeticError, UnicodeError, subprocess.CalledProcessError) as error:
        return [str(error)]
    return []


def validate(repository_root, output_root=None, *, input_root=None, price_repository_root=None, published_only=False):
    root = Path(repository_root)
    output = Path(output_root) if output_root else root / DIRECTORY
    try:
        contract = json.loads((root / CONTRACT_FILE).read_bytes())
        paths = {artifact_name(kind): output / artifact_name(kind) for kind in KINDS}
        if any(not path.is_file() or path.is_symlink() for path in paths.values()):
            return ["all exact eleven published regular artifacts are required; no skip/fallback"]
        artifacts = {name: path.read_bytes() for name, path in paths.items()}
        return validate_artifacts(root, contract, artifacts, input_root=input_root, price_repository_root=price_repository_root, published_only=published_only)
    except (OSError, ValueError) as error:
        return [str(error)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--input-root", type=Path)
    parser.add_argument("--price-repository-root", type=Path)
    parser.add_argument("--published-only", action="store_true")
    args = parser.parse_args(argv)
    errors = validate(args.repository_root, args.output_root, input_root=args.input_root, price_repository_root=args.price_repository_root, published_only=args.published_only)
    if errors:
        for error in errors:
            print("FAIL: " + error, flush=True)
        return 1
    mode = "normalized_weekly_offsets + immutable_all_features_price_warmup_control; private_raw_not_reread" if args.published_only else "independent_raw65_full_price_universe_Decimal_OLS_and_cashflow_replay"
    print("PASS: independent medium-term TDCC; " + mode + "; research_only; input_availability_proven=False; promotion_evidence_allowed=False", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
