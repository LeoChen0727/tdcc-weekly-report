"""Independent same-model holding-horizon audit; never imports a producer.

The selected input rows are immutable, previously audited annual-v1 evidence.
This audit independently replays new operations; it does not claim to repeat
annual-v1 feature reconstruction or prove original publication availability.
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
import statistics
import subprocess
from array import array
from collections import Counter, defaultdict, namedtuple
from decimal import Decimal, localcontext
from pathlib import Path

import validate_tdcc_stealth_accumulation_current_version_annual_replay as annual

BASE_REF = "d2f3ccfaf95562b5179f433af0b4b41d62bfee17"
PRICE_REF = "07d992bbd9afa283355d8828a294da4524efb56d"
PREFIX = "tdcc_stealth_accumulation_current_version_horizon_extension_"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_current_version_horizon_extension_v1.json"
DEFAULT_DIRECTORY = "output/research/tdcc_stealth_accumulation"
PROFILES = {"full_period": (30, 40, 60), "common_d60": (5, 10, 20, 30, 40, 60)}
ALL_HORIZONS = (5, 10, 20, 30, 40, 60)
SLIPPAGES = (0, 10, 20)
Signal = namedtuple("Signal", "signal_date stock_id stock_name market history_gap_count")
StatTrade = namedtuple("StatTrade", "profile signal_date stock_id horizon slippage_bps net_return_pct history_gap_count entry_date exit_date published_anomaly")
KINDS = ("source_manifest", "trades", "blocked", "summary", "anomalies", "paired_summary", "report")
SCHEMAS = {
    "trades": ["profile"] + annual.SCHEMAS["trades"] + ["entry_index", "exit_target_index"],
    "blocked": ["profile"] + annual.SCHEMAS["blocked"] + ["entry_index", "exit_target_index"],
    "summary": ["profile", "signal_cutoff"] + annual.SCHEMAS["summary"],
    "anomalies": ["profile"] + annual.SCHEMAS["anomalies"],
    "paired_summary": "profile,horizon,slippage_bps,event_count,eventset_sha256,common_signal_count,excluded_missing_entry_or_exit_events,anomaly_candidate_events,possible_TDR_events,win_count,neutral_count,failure_count,mean_net_return_pct,median_net_return_pct,win_rate_pct,neutral_rate_pct,failure_rate_pct,high_return_ge10_rate_pct,loss_le_minus10_rate_pct,min_net_return_pct,max_net_return_pct,reference_horizon,mean_paired_delta_vs_D20_pct,median_paired_delta_vs_D20_pct,paired_delta_positive_count,paired_delta_zero_count,paired_delta_negative_count,primary_row_retained,overlapping_events_allowed,portfolio_performance,formal_use,promotion_evidence_allowed,caveat".split(","),
}
FALSE_FLAGS = ("formal_use", "promotion_evidence_allowed", "input_availability_proven", "full_period_pit_complete", "calendar_complete_coverage_verified", "corporate_action_complete_coverage_verified", "ordinary_stock_universe_certified", "private_raw_publication_allowed")
NUMERIC = annual.NUMERIC_FIELDS | {"entry_index", "exit_target_index", "event_count", "common_signal_count", "excluded_missing_entry_or_exit_events", "anomaly_candidate_events", "possible_TDR_events", "reference_horizon", "mean_paired_delta_vs_D20_pct", "median_paired_delta_vs_D20_pct", "paired_delta_positive_count", "paired_delta_zero_count", "paired_delta_negative_count"}
APPROVED_CONTRACT_SHA256 = "92b3ecd136ac2d70ffcdf575a836f4a5a68767bbbe6fbfb351cf5c158f24abdc"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def name(kind):
    extension = "csv.gz" if kind in {"trades", "blocked"} else "json" if kind == "source_manifest" else "md" if kind == "report" else "csv"
    return f"{PREFIX}{kind}_v1.{extension}"


def holding_dates(calendar, signal_date, horizon, as_of):
    """D0 is next session open; do not invent dates beyond the audit calendar."""
    entry_index = bisect.bisect_right(calendar, signal_date)
    if horizon not in ALL_HORIZONS or entry_index == 0 or calendar[entry_index - 1] != signal_date:
        raise ValueError("unknown holding horizon or non-session signal")
    target = entry_index + horizon
    last_known = bisect.bisect_right(calendar, as_of) - 1
    if entry_index >= len(calendar):
        raise ValueError("audit calendar omits next session entry date")
    if not 0 <= last_known < len(calendar):
        raise ValueError("audit calendar omits as-of history")
    exit_date = calendar[target] if target < len(calendar) else ""
    return dict(entry_date=calendar[entry_index], exit_date=exit_date,
                entry_index=entry_index, exit_target_index=target,
                mature=target <= last_known)


def common_cutoff(calendar, as_of):
    index = bisect.bisect_right(calendar, as_of) - 1 - 61
    if index < 0:
        raise ValueError("audit calendar has no D60-mature signal boundary")
    return calendar[index]


def select_profiles(signals, calendar, as_of):
    cutoff = common_cutoff(calendar, as_of)
    return {"full_period": signals,
            "common_d60": [row for row in signals if row.signal_date <= cutoff]}, cutoff


def compact_signals(payload):
    result, previous, pool = [], None, {}
    for row in annual.rows_for("signals", payload):
        key = row["signal_date"], row["stock_id"]
        if previous is not None and key <= previous:
            raise ValueError("immutable signal identities are not unique/sorted")
        previous = key
        if row["input_ref"] != PRICE_REF or row["selected"] != "True" or row["feature_supported"] != "True":
            raise ValueError("immutable signal selected/source binding drift")
        if any(row[field] != "False" for field in ("input_availability_proven", "formal_use", "promotion_evidence_allowed")):
            raise ValueError("immutable signal research-only boundary drift")
        if any(row[field] for field in ("receipt_id", "available_no_later_than", "entry_cutoff")):
            raise ValueError("immutable current-version signals cannot acquire receipts")
        strings = [pool.setdefault(row[field], row[field]) for field in ("signal_date", "stock_id", "stock_name", "market")]
        result.append(Signal(*strings, annual.integer(row["history_gap_count"])))
    return result


class PublishedPrices:
    """Public Git prices, with exactly one immutable model-output recovery day."""

    def __init__(self, git, base_contract, feature_payload):
        self.git, self.contract = git, base_contract
        self.recovery = {}
        item = next(r for r in base_contract["external_files"] if r["kind"] == "price_recovery")
        if item["date"] != "20250915" or f"data/daily_price/{item['date']}.csv" in git.tree(PRICE_REF):
            raise ValueError("published recovery must remain the exact absent 20250915 source")
        for row in annual.rows_for("features", feature_payload):
            if row["signal_date"] < "20250915":
                continue
            if row["signal_date"] > "20250915":
                break
            stock = row["stock_id"]
            if stock in self.recovery or row["universe_source_path"] != "external:" + item["path"] or row["universe_source_sha256"] != item["sha256"]:
                raise ValueError("immutable recovery feature identity/source mismatch")
            price = dict(stock_id=stock, stock_name=row["stock_name"], market=row["market"], date="20250915",
                         source_path=row["universe_source_path"], source_sha256=row["universe_source_sha256"],
                         **{key: annual.number(row[key]) for key in ("open", "high", "low", "close")})
            price["duplicate_key"] = "signal_ohlc_invalid_or_conflicting" in row["unsupported_reasons"].split(";")
            self.recovery[stock] = price
        if not self.recovery:
            raise ValueError("immutable recovery feature rows missing")

    def daily(self, date):
        if not date or date > self.contract["as_of"]:
            return {}, {}
        if date == "20250915":
            return self.recovery, {}
        return self.git.daily(PRICE_REF, date)


def source_price(prices, date, stock):
    return prices.daily(date)[0].get(stock) if date else None


def records(kind, payload):
    binary = gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") if kind in {"trades", "blocked"} else io.BytesIO(payload)
    with io.TextIOWrapper(binary, encoding="utf-8", newline="") as stream:
        def lines():
            for line in stream:
                if line.startswith("\ufeff") or "\r" in line or not line.endswith("\n"):
                    raise ValueError(f"{kind}: UTF-8/LF serialization drift")
                yield line
        reader = csv.DictReader(lines(), strict=True)
        if reader.fieldnames != SCHEMAS[kind]:
            raise ValueError(f"{kind}: exact schema mismatch")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{kind}: malformed row width")
            yield row


def compare_row(kind, actual, expected, *, ignore=()):
    if actual is None:
        raise ValueError(f"{kind}: missing expected row")
    for field in SCHEMAS[kind]:
        if field in ignore:
            continue
        a, b = actual.get(field, ""), expected.get(field, "")
        a, b = "" if a is None else str(a), "" if b is None else str(b)
        if a == b:
            continue
        x, y = annual.number(a), annual.number(b)
        if field in NUMERIC and a and b and x is not None and y is not None and math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12):
            continue
        raise ValueError(f"{kind}: {field}={a!r} != independent {b!r}; identity={expected.get('profile')}:{expected.get('signal_date')}:{expected.get('stock_id')}:{expected.get('horizon')}")


def compare_sequence(kind, actual, expected):
    actual = iter(actual)
    for row in expected:
        compare_row(kind, next(actual, None), row)
    if next(actual, None) is not None:
        raise ValueError(f"{kind}: unexpected extra row")


def ledger_rows(prices, signals, calendar, *, profile, horizon, as_of):
    """Yield strict/proxy decisions independently, keeping one horizon's locks."""
    held = {}
    for signal in signals:
        date, stock = signal.signal_date, signal.stock_id
        target = holding_dates(calendar, date, horizon, as_of)
        mature = target.pop("mature")
        entry, exit_ = target["entry_date"], target["exit_date"]
        ep = source_price(prices, entry, stock)
        xp = source_price(prices, exit_, stock) if mature else None
        if entry > as_of:
            strict, strict_reason = "blocked_entry_after_as_of", "entry_after_as_of"
        elif not annual.valid_price(ep):
            strict, strict_reason = "blocked_entry_price", "entry_price_missing_or_invalid"
        else:
            strict, strict_reason = "blocked_input_availability_unproven", "current_acquired_historical_versions_not_event_time_receipts"
        common = dict(profile=profile, signal_date=date, stock_id=stock, horizon=horizon, strict_v3_status=strict, **target)
        yield "blocked", dict(common, record_type="strict_ledger_decision", reasons=strict_reason,
                              entry_open=ep["open"] if ep else "", strict_entry_established=False,
                              strict_prior_position_locked=False, proxy_result_must_not_release_strict_lock=True)
        lock = held.get(stock)
        reason = ("blocked_exit_day" if lock == date else "blocked_active_position") if lock and date <= lock else "entry_after_as_of" if entry > as_of else "entry_price_missing_or_invalid" if not annual.valid_price(ep) else ""
        if reason:
            yield "blocked", dict(common, record_type="operation_no_entry", reasons=reason)
            continue
        held[stock] = exit_ if mature and annual.valid_price(xp) else "99999999"
        if not mature or not annual.valid_price(xp):
            yield "blocked", dict(common, record_type="operation_censored", entry_open=ep["open"], reasons="open_immature" if not mature else "open_unresolved_exit_price")
            continue
        for slip in SLIPPAGES:
            yield "trades", dict(common, trade_id=f"{profile}:{date}:{stock}:D{horizon}:S{slip}",
                stock_name=signal.stock_name, market=signal.market, slippage_bps=slip,
                **annual.cashflow(ep["open"], xp["close"], slip), simulation_status="realized_raw_price_proxy",
                strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit",
                ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False,
                input_ref=PRICE_REF, receipt_id="", outcome_ref=PRICE_REF,
                entry_source_path=ep["source_path"], entry_source_sha256=ep["source_sha256"],
                exit_source_path=xp["source_path"], exit_source_sha256=xp["source_sha256"],
                history_gap_count=signal.history_gap_count, anomaly_candidate=False, primary_row_retained=True,
                formal_use=False, promotion_evidence_allowed=False)


def audit_ledgers(prices, groups, calendar, as_of, artifacts):
    readers = {kind: iter(records(kind, artifacts[name(kind)])) for kind in ("trades", "blocked")}
    stats, blocks, counts = defaultdict(list), defaultdict(Counter), Counter()
    for profile, horizons in PROFILES.items():
        for horizon in horizons:
            for kind, expected in ledger_rows(prices, groups[profile], calendar, profile=profile, horizon=horizon, as_of=as_of):
                actual = next(readers[kind], None)
                compare_row(kind, actual, expected, ignore=("anomaly_candidate",) if kind == "trades" else ())
                counts[kind] += 1
                if kind == "blocked":
                    blocks[profile, horizon][expected["record_type"]] += 1
                    blocks[profile, horizon][expected["reasons"]] += 1
                    blocks[profile, horizon][expected["record_type"], expected["reasons"]] += 1
                else:
                    stats[profile, horizon, expected["slippage_bps"]].append(StatTrade(profile,
                        expected["signal_date"], expected["stock_id"], horizon, expected["slippage_bps"],
                        expected["net_return_pct"], expected["history_gap_count"], expected["entry_date"],
                        expected["exit_date"], annual.bool_value(actual["anomaly_candidate"])))
    for kind, reader in readers.items():
        if next(reader, None) is not None:
            raise ValueError(f"{kind}: extra row beyond independent signal/horizon replay")
    return stats, blocks, counts


def anomaly_rows(stats, retained):
    keys, result = set(), []
    for profile, horizons in PROFILES.items():
        current = {(trade.signal_date, trade.stock_id, horizon): trade for horizon in horizons for trade in stats[profile, horizon, 10]}
        for row in retained:
            key = (row["signal_date"], row["stock_id"], annual.integer(row["horizon"]))
            if key not in current or (profile, *key) in keys:
                continue
            keys.add((profile, *key))
            result.append(dict(profile=profile, signal_date=key[0], stock_id=key[1], horizon=key[2],
                net_return_pct=row["net_return_pct"], reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample",
                disposition="unresolved_anomaly_candidate", primary_row_retained=True,
                exclusion_allowed_only_as_sensitivity=True, entry_date=row["entry_date"], exit_date=row["exit_date"], represented_in_current_proxy_trade=True))
        for horizon in horizons:
            sample = stats[profile, horizon, 10]
            if len(sample) < 4:
                continue
            low, _, high = statistics.quantiles(sorted(float(row.net_return_pct) for row in sample), n=4, method="inclusive")
            span = 3 * (high - low)
            for row in sample:
                key = profile, row.signal_date, row.stock_id, horizon
                value = float(row.net_return_pct)
                if low - span <= value <= high + span or key in keys:
                    continue
                keys.add(key)
                result.append(dict(profile=profile, signal_date=row.signal_date, stock_id=row.stock_id, horizon=horizon,
                    net_return_pct=row.net_return_pct, reason="outside_Q1_Q3_plus_3IQR_descriptive_candidate",
                    disposition="unresolved_anomaly_candidate", primary_row_retained=True,
                    exclusion_allowed_only_as_sensitivity=True, entry_date=row.entry_date, exit_date=row.exit_date, represented_in_current_proxy_trade=True))
    for rows in stats.values():
        for row in rows:
            expected = (row.profile, row.signal_date, row.stock_id, row.horizon) in keys
            if row.published_anomaly is not None and row.published_anomaly is not expected:
                raise ValueError("trade anomaly candidate differs from independently retained/IQR keys")
    return result, keys


def return_statistics(values):
    size = len(values)
    wins, neutral, failures = (sum(test(x) for x in values) for test in (lambda x: x > 0, lambda x: x == 0, lambda x: x < 0))
    return dict(win_count=wins, neutral_count=neutral, failure_count=failures,
                mean_net_return_pct=statistics.mean(values) if values else "", median_net_return_pct=statistics.median(values) if values else "",
                win_rate_pct=wins / size * 100 if size else "", neutral_rate_pct=neutral / size * 100 if size else "",
                failure_rate_pct=failures / size * 100 if size else "", high_return_ge10_rate_pct=sum(x >= 10 for x in values) / size * 100 if size else "",
                loss_le_minus10_rate_pct=sum(x <= -10 for x in values) / size * 100 if size else "",
                min_net_return_pct=min(values) if values else "", max_net_return_pct=max(values) if values else "")


def summaries(stats, blocks, groups, cutoff, as_of, anomaly_keys):
    result = []
    for profile, horizons in PROFILES.items():
        for horizon in horizons:
            counters = blocks[profile, horizon]
            for slip in SLIPPAGES:
                for population in ("primary_including_anomaly_candidates", "sensitivity_excluding_anomaly_candidates"):
                    sample = [r for r in stats[profile, horizon, slip] if population.startswith("primary") or (profile, r.signal_date, r.stock_id, horizon) not in anomaly_keys]
                    values = [float(row.net_return_pct) for row in sample]
                    row = dict(profile=profile, signal_cutoff=cutoff if profile == "common_d60" else as_of,
                        horizon=horizon, slippage_bps=slip, population=population, realized_raw_price_proxy_positions=len(sample),
                        total_input_signals=len(groups[profile]), proxy_no_entry_signals=counters["operation_no_entry"],
                        proxy_immature_positions=counters["open_immature"], proxy_unresolved_exit_positions=counters["open_unresolved_exit_price"],
                        strict_verified_total_return_positions=0, denominator="realized_raw_price_proxy_positions",
                        anomaly_candidate_positions=sum((profile, r.signal_date, r.stock_id, horizon) in anomaly_keys for r in sample),
                        caveat="raw_unadjusted_price_proxy_not_verified_total_return;not_performance_promotion_evidence", **return_statistics(values))
                    for label, gap in (("gap_present", True), ("gap_absent", False)):
                        subset = [float(r.net_return_pct) for r in sample if (r.history_gap_count > 0) == gap]
                        row.update({label + "_positions": len(subset), label + "_mean_return_pct": statistics.mean(subset) if subset else "",
                            label + "_median_return_pct": statistics.median(subset) if subset else "", label + "_win_rate_pct": sum(x > 0 for x in subset) / len(subset) * 100 if subset else ""})
                    result.append(row)
    return result


def paired_summary(prices, signals, calendar, as_of, retained=()):
    """Recompute all six returns for the SAME complete-case overlapping events."""
    values, deltas, events = defaultdict(lambda: array("d")), defaultdict(lambda: array("d")), []
    for signal in signals:
        dates = {h: holding_dates(calendar, signal.signal_date, h, as_of) for h in ALL_HORIZONS}
        entry = source_price(prices, dates[20]["entry_date"], signal.stock_id)
        exits = {h: source_price(prices, dates[h]["exit_date"], signal.stock_id) if dates[h]["mature"] else None for h in ALL_HORIZONS}
        if not annual.valid_price(entry) or not all(annual.valid_price(row) for row in exits.values()):
            continue
        events.append([signal.signal_date, signal.stock_id, dates[20]["entry_date"]])
        for slip in SLIPPAGES:
            returns = {h: annual.cashflow(entry["open"], exits[h]["close"], slip)["net_return_pct"] for h in ALL_HORIZONS}
            for horizon in ALL_HORIZONS:
                values[horizon, slip].append(float(returns[horizon]))
                with localcontext() as context:
                    context.prec = 50
                    deltas[horizon, slip].append(float(Decimal(returns[horizon]) - Decimal(returns[20])))
    old_keys = {(r["signal_date"], r["stock_id"], annual.integer(r["horizon"])) for r in retained}
    anomalies, candidate_counts = [], Counter()
    for horizon in ALL_HORIZONS:
        sample = values[horizon, 10]
        lower = upper = None
        if len(sample) >= 4:
            low, _, high = statistics.quantiles(sample, n=4, method="inclusive")
            lower, upper = low - 3 * (high - low), high + 3 * (high - low)
        for event, value in zip(events, sample):
            date, stock, entry = event
            old = (date, stock, horizon) in old_keys
            if not old and (lower is None or lower <= value <= upper):
                continue
            candidate_counts[horizon] += 1
            anomalies.append(dict(profile="paired_common_d60", signal_date=date, stock_id=stock, horizon=horizon,
                net_return_pct=value, reason="previously_observed_candidate_retained_not_reclassified_by_larger_sample" if old else "outside_Q1_Q3_plus_3IQR_descriptive_candidate",
                disposition="unresolved_anomaly_candidate", primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True,
                entry_date=entry, exit_date=holding_dates(calendar, date, horizon, as_of)["exit_date"], represented_in_current_proxy_trade=False))
    event_hash, result = sha(annual.canonical_json(events)), []
    for horizon in ALL_HORIZONS:
        for slip in SLIPPAGES:
            delta = deltas[horizon, slip]
            result.append(dict(profile="paired_common_d60", horizon=horizon, slippage_bps=slip,
                event_count=len(events), eventset_sha256=event_hash, common_signal_count=len(signals),
                excluded_missing_entry_or_exit_events=len(signals) - len(events), anomaly_candidate_events=candidate_counts[horizon],
                possible_TDR_events=sum(stock.startswith("91") for _, stock, _ in events), **return_statistics(values[horizon, slip]),
                reference_horizon=20, mean_paired_delta_vs_D20_pct=statistics.mean(delta) if delta else "",
                median_paired_delta_vs_D20_pct=statistics.median(delta) if delta else "",
                paired_delta_positive_count=sum(x > 0 for x in delta), paired_delta_zero_count=sum(x == 0 for x in delta),
                paired_delta_negative_count=sum(x < 0 for x in delta), primary_row_retained=True, overlapping_events_allowed=True,
                portfolio_performance=False, formal_use=False, promotion_evidence_allowed=False,
                caveat="same_complete_case_eventset;observational_selection;overlapping_events_not_portfolio;raw_price_proxy_not_promotion"))
    return result, anomalies


def load_baseline(repository_root):
    git = annual.GitReader(repository_root)
    original = json.loads(git.read(BASE_REF, annual.CONTRACT_FILE))
    failures = annual._contract_errors(original)
    if failures:
        raise ValueError("immutable annual-v1 contract: " + "; ".join(failures))
    manifest_path = DEFAULT_DIRECTORY + "/" + annual.artifact_name("source_manifest")
    payload = git.read(BASE_REF, manifest_path)
    manifest = json.loads(payload)
    if payload != annual.canonical_json(manifest) or manifest["contract"] != original or manifest["contract_sha256"] != annual.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual-v1 manifest contract drift")
    if any(manifest.get(field) is not False for field in ("formal_use", "promotion_evidence_allowed", "full_period_pit_complete")):
        raise ValueError("immutable annual-v1 research boundary drift")
    blobs = {}
    for kind in ("signals", "anomalies", "features"):
        filename = annual.artifact_name(kind)
        data = git.read(BASE_REF, DEFAULT_DIRECTORY + "/" + filename)
        if manifest["hashes"][filename] != dict(bytes=len(data), sha256=sha(data)):
            raise ValueError("immutable annual-v1 serialized artifact hash mismatch: " + kind)
        blobs[kind] = data
    signals = compact_signals(blobs.pop("signals"))
    retained = list(annual.rows_for("anomalies", blobs.pop("anomalies")))
    if len(signals) != manifest["counts"]["signals"] or len(retained) != manifest["counts"]["anomaly_candidates"]:
        raise ValueError("immutable annual-v1 signal/anomaly count mismatch")
    return git, original, manifest, signals, retained, blobs["features"]


def audit_source_bindings(git, manifest, original):
    base_paths = {annual.CONTRACT_FILE} | {DEFAULT_DIRECTORY + "/" + annual.artifact_name(kind) for kind in ("source_manifest", "signals", "features", "anomalies")}
    expected_keys = {(BASE_REF, path) for path in base_paths}
    expected_keys |= {(PRICE_REF, path) for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv")}
    expected_keys |= {(PRICE_REF, path) for path in git.tree(PRICE_REF) if path.startswith("data/daily_price/") and len(path.rsplit("/", 1)[-1]) == 12 and path[-12:-4].isdigit() and path.endswith(".csv") and original["history_start"] <= path[-12:-4] <= original["as_of"]}
    listed = manifest["sources"]
    if {(row["ref"], row["path"]) for row in listed} != expected_keys or len(listed) != len(expected_keys):
        raise ValueError("extension exact fixed-Git source allowlist mismatch")
    if listed != sorted(listed, key=lambda row: (row["ref"], row["path"])):
        raise ValueError("extension source ordering drift")
    for row in listed:
        key = row["ref"], row["path"]
        if key not in git.used:
            git.read(*key)
        if row != git.used[key]:
            raise ValueError(f"extension immutable source SHA/bytes/OID mismatch: {key}")
    expected_external = original["external_files"]
    if len(manifest["external_sources"]) != len(expected_external):
        raise ValueError("extension external source cardinality mismatch")
    for observed, expected in zip(manifest["external_sources"], expected_external):
        if {key: value for key, value in observed.items() if key != "bytes"} != expected or type(observed.get("bytes")) is not int or observed["bytes"] <= 0:
            raise ValueError("extension exact external source hash/path binding mismatch")


def audit_report(payload, groups, cutoff, original, summary, paired, anomalies, blocks, baseline_candidate_count):
    if payload.startswith(b"\xef\xbb\xbf") or b"\r" in payload or not payload.endswith(b"\n"):
        raise ValueError("extension report UTF-8/LF serialization drift")
    report = payload.decode("utf-8")
    for text in ("research_only", "formal_use=False", "promotion_evidence_allowed=False", "full_period_pit_complete=False",
                 "不是 strict PIT", "已核實 total-return", "出場日訊號仍阻擋", "不是portfolio績效", "不影響主帳本",
                 "全部保留primary", "只作sensitivity", "不是corrected/cleaned performance", "不依異常幅度刪除", "blocked_input_availability_unproven", "沒有配對sensitivity"):
        if text not in report:
            raise ValueError("extension report missing required limitation: " + text)
    for text in (f"原始訊號區間 {original['requested_signal_start']}–{original['requested_signal_end']}；as_of={original['as_of']}；D60共同訊號截止={cutoff or '無'}。",
                 f"全區間原始訊號 {len(groups['full_period'])}；共同區間原始訊號 {len(groups['common_d60'])}。",
                 f"新anomalies共 {len(anomalies)} 列", f"immutable v1 baseline候選 {baseline_candidate_count} 列",
                 f"配對common原始訊號 {paired[0]['common_signal_count']}；六horizon共同有效事件 {paired[0]['event_count']}；缺有效入場／任一出場排除 {paired[0]['excluded_missing_entry_or_exit_events']}；可能91開頭TDR事件 {paired[0]['possible_TDR_events']}。"):
        if text not in report:
            raise ValueError("extension report cutoff/count mismatch: " + text)
    def table(title, paired_rows=False):
        heading = "## " + title + "\n"
        if report.count(heading) != 1:
            raise ValueError("extension report section missing/repeated: " + title)
        section = report.split(heading, 1)[1].split("\n## ", 1)[0]
        prefixes = tuple(f"| {h} |" for h in ALL_HORIZONS) if paired_rows else ("| full_period |", "| common_d60 |")
        return [line for line in section.splitlines() if line.startswith(prefixes)]
    expected = [f"| {r['profile']} | {r['horizon']} | {r['realized_raw_price_proxy_positions']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['win_rate_pct']} | {r['proxy_immature_positions']}／{r['proxy_unresolved_exit_positions']} |" for r in summary if r["slippage_bps"] == 10 and r["population"].startswith("primary")]
    if table("主要結果（10 bps，保留所有未解候選）") != expected:
        raise ValueError("extension report primary values differ from independent summary")
    expected = [f"| {r['profile']} | {r['horizon']} | {r['realized_raw_price_proxy_positions']} | {r['mean_net_return_pct']} | {r['median_net_return_pct']} | {r['win_rate_pct']} |" for r in summary if r["slippage_bps"] == 10 and r["population"].startswith("sensitivity")]
    if table("排除候選敏感性對照（10 bps，不取代primary）") != expected:
        raise ValueError("extension report sensitivity values differ from independent summary")
    reasons = sorted((profile, horizon, key[0], key[1], count) for (profile, horizon), counter in blocks.items() for key, count in counter.items() if isinstance(key, tuple) and key[0] != "strict_ledger_decision")
    expected = [f"| {profile} | {horizon} | {kind} | {reason} | {count} |" for profile, horizon, kind, reason, count in reasons]
    if table("未入場／未成熟／缺出場原因分布") != expected:
        raise ValueError("extension report blocked reasons differ from independent ledger")
    expected = []
    for profile, horizons in PROFILES.items():
        for horizon in horizons:
            candidates = [row for row in anomalies if row["profile"] == profile and row["horizon"] == horizon]
            if not candidates:
                continue
            low = min(candidates, key=lambda row: float(row["net_return_pct"]))
            high = max(candidates, key=lambda row: float(row["net_return_pct"]))
            for row in [low] if low == high else [low, high]:
                expected.append(f"| {profile} | {horizon} | {row['signal_date']} | {row['stock_id']} | {row['net_return_pct']} | unresolved_anomaly_candidate；保留primary |")
    if table("新帳本數值調查候選（10 bps，每組列出最高與最低）") != expected:
        raise ValueError("extension report anomaly candidates differ from independently retained rows")
    expected = [f"| {row['horizon']} | {row['event_count']} | {row['mean_net_return_pct']} | {row['mean_paired_delta_vs_D20_pct']} | {row['median_paired_delta_vs_D20_pct']} |" for row in paired if row["slippage_bps"] == 10]
    actual = table("同事件配對觀察（10 bps）", paired_rows=True)
    if actual != expected:
        raise ValueError("extension report paired values differ from independent event arithmetic")


def validate_artifacts(repository_root, contract, artifacts, *, input_root=None, price_repository_root=None, published_only=False):
    try:
        if sha(annual.canonical_json(contract)) != APPROVED_CONTRACT_SHA256:
            raise ValueError("extension frozen contract digest mismatch")
        if set(artifacts) != {name(kind) for kind in KINDS}:
            raise ValueError("extension requires exactly seven artifacts; missing/extra file")
        manifest_bytes = artifacts[name("source_manifest")]
        manifest = json.loads(manifest_bytes)
        if annual.canonical_json(manifest) != manifest_bytes:
            raise ValueError("extension manifest canonical JSON mismatch")
        expected = dict(model_id=annual.MODEL_ID, owner_id="tdcc_stealth_accumulation_current_version_annual_replay",
            artifact_version=PREFIX + "v1", contract_file=CONTRACT_FILE, contract=contract,
            contract_sha256=APPROVED_CONTRACT_SHA256, base_artifact_ref=BASE_REF,
            base_contract_sha256=annual.APPROVED_CONTRACT_SHA256,
            validation_scope="immutable_v1_signals_and_independent_horizon_source_replay_not_selector_revalidation")
        for field, value in expected.items():
            if manifest.get(field) != value:
                raise ValueError("extension manifest fixed identity drift: " + field)
        if any(manifest.get(field) is not False or contract.get(field) is not False for field in FALSE_FLAGS):
            raise ValueError("extension research-only flags must remain False")
        hashes = {filename: dict(bytes=len(data), sha256=sha(data)) for filename, data in artifacts.items() if filename != name("source_manifest")}
        if manifest["hashes"] != hashes:
            raise ValueError("extension final six serialized artifact hashes/lengths mismatch")
        if not published_only and input_root is None:
            raise ValueError("full horizon source replay requires --input-root; artifact mode must be explicit --published-only")
        git, original, baseline, signals, retained, feature_payload = load_baseline(price_repository_root or repository_root)
        if manifest["base_contract"] != original:
            raise ValueError("extension base contract differs from immutable annual-v1")
        closures = baseline["evidence"]["calendar_closures"]
        calendar = annual.calendar_days(closures, original["history_start"], original["calendar_end"])
        expected_calendar = dict(history_start=original["history_start"], calendar_end=original["calendar_end"], closures=closures,
                                 sessions=calendar, target_index_basis="zero_based_from_history_start")
        if manifest["calendar"] != expected_calendar:
            raise ValueError("extension calendar differs from immutable source sessions/closures")
        if manifest["baseline_anomaly_audit"] != dict(candidate_rows=len(retained), retained_in_immutable_base=True,
            sha256=baseline["hashes"][annual.artifact_name("anomalies")]["sha256"], unrepresented_candidates_not_copied_to_extension_profiles=True):
            raise ValueError("extension retained baseline anomaly audit mismatch")
        groups, cutoff = select_profiles(signals, calendar, original["as_of"])
        if manifest["common_signal_cutoff"] != cutoff:
            raise ValueError("extension common D60 signal cutoff drift")
        supplemental = baseline["counts"]["supplemental"]
        if published_only:
            prices = PublishedPrices(git, original, feature_payload)
        else:
            inputs = annual.PrivateInputs(input_root, original)
            actual_closures = set()
            for item in original["external_files"]:
                data = inputs.read(item)
                if item["kind"] == "calendar":
                    actual_closures.update(row["date"] for row in annual.csv_records(data) if row["scheduled_closed"] == "True")
            for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
                actual_closures.update(row["date"] for row in annual.csv_records(git.read(PRICE_REF, path)))
            if sorted(actual_closures) != closures:
                raise ValueError("full-source official calendar differs from immutable baseline")
            prices = annual.CurrentPrices(git, inputs, original)
            supplemental = prices.supplemental_counts
            if manifest["external_sources"] != [inputs.used[item["path"]] for item in original["external_files"]]:
                raise ValueError("full-source external input SHA/bytes mismatch")
        del feature_payload
        stats, blocks, row_counts = audit_ledgers(prices, groups, calendar, original["as_of"], artifacts)
        anomalies, anomaly_keys = anomaly_rows(stats, retained)
        summary = summaries(stats, blocks, groups, cutoff, original["as_of"], anomaly_keys)
        compare_sequence("summary", records("summary", artifacts[name("summary")]), summary)
        del stats
        paired, paired_anomalies = paired_summary(prices, groups["common_d60"], calendar, original["as_of"], retained)
        anomalies.extend(paired_anomalies)
        compare_sequence("paired_summary", records("paired_summary", artifacts[name("paired_summary")]), paired)
        compare_sequence("anomalies", records("anomalies", artifacts[name("anomalies")]), anomalies)
        expected_counts = dict(base_signals=len(signals), common_signals=len(groups["common_d60"]),
            trade_rows=row_counts["trades"], blocked_rows=row_counts["blocked"], anomaly_rows=len(anomalies), summary_rows=len(summary),
            paired_summary_rows=len(paired), paired_event_count=paired[0]["event_count"], supplemental=supplemental)
        if manifest["counts"] != expected_counts:
            raise ValueError("extension counts differ from independently reconstructed ledgers/events")
        audit_source_bindings(git, manifest, original)
        audit_report(artifacts[name("report")], groups, cutoff, original, summary, paired, anomalies, blocks, len(retained))
        return []
    except (ValueError, KeyError, TypeError, AttributeError, IndexError, OverflowError, UnicodeError, csv.Error, EOFError, OSError, subprocess.CalledProcessError) as error:
        return [f"independent horizon audit failed closed: {type(error).__name__}: {error}"]


def validate(repository_root, output_root=None, *, input_root=None, price_repository_root=None, published_only=False):
    try:
        root = Path(repository_root).resolve()
        output = Path(output_root) if output_root is not None else root / DEFAULT_DIRECTORY
        paths = list(output.glob(PREFIX + "*"))
        if any(not path.is_file() or path.is_symlink() for path in paths):
            raise ValueError("extension artifacts must be regular files")
        artifacts = {path.name: path.read_bytes() for path in paths}
        contract = json.loads((root / CONTRACT_FILE).read_text(encoding="utf-8"))
        return validate_artifacts(root, contract, artifacts, input_root=input_root, price_repository_root=price_repository_root, published_only=published_only)
    except (ValueError, OSError) as error:
        return [f"extension artifact read failed closed: {error}"]


def main(argv=None):
    parser = argparse.ArgumentParser(description="唯讀獨立核對 TDCC D30/D40/D60 目前版本研究延伸")
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--input-root", type=Path)
    parser.add_argument("--price-repository-root", type=Path)
    parser.add_argument("--published-only", action="store_true")
    arguments = parser.parse_args(argv)
    errors = validate(arguments.repository_root, arguments.output_root, input_root=arguments.input_root,
                      price_repository_root=arguments.price_repository_root, published_only=arguments.published_only)
    mode = "immutable_v1_signals_and_published_source_horizon_replay" if arguments.published_only else "immutable_v1_signals_and_independent_horizon_source_replay"
    print(json.dumps(dict(status="fail" if errors else "pass", errors=errors, validation_mode=mode,
        annual_v1_features_recomputed=False, original_publication_availability_verified=False, formal_use=False,
        promotion_evidence_allowed=False), ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
