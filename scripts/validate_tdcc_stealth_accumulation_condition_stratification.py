"""Read-only independent condition-stratification audit for one TDCC model.

Immutable annual-v1 rows are inputs, not the new producer's implementation.
Dates, condition features, fixed split, training quantile, position locks and
summary arithmetic are independently reconstructed here. No producer executes.
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
from collections import Counter, defaultdict, namedtuple
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

import validate_tdcc_stealth_accumulation_current_version_annual_replay as annual_io
import validate_tdcc_stealth_accumulation_current_version_horizon_extension as horizon_io

BASE_REF = "d2f3ccfaf95562b5179f433af0b4b41d62bfee17"
PROTECTED_REF = "129b8669ef17cb1a678dd71b87097cbbff084c82"
PRICE_REF = "07d992bbd9afa283355d8828a294da4524efb56d"
PREFIX = "tdcc_stealth_accumulation_condition_stratification_"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
CONTRACT_FILE = "config/tdcc_stealth_accumulation_condition_stratification_v1.json"
SPLIT = "20260401"
AS_OF = "20260909"
HORIZONS = (20, 60)
SLIPPAGES = (0, 10, 20)
KINDS = ("source_manifest", "features", "training_contrasts", "candidate_rules", "trades", "blocked", "summary", "anomalies", "report")
VARIANTS = ("baseline", "tdcc_both_net_positive", "tdcc_both_up_count_ge2", "price_5obs_nonnegative", "range_20obs_le_training_q75", "no_new_low_previous20obs")
PARTITIONS = ("all", "training", "purged_cross_split", "validation")
FALSE_FLAGS = ("formal_use", "promotion_evidence_allowed", "input_availability_proven", "full_period_pit_complete", "calendar_complete_coverage_verified", "corporate_action_complete_coverage_verified", "ordinary_stock_universe_certified", "private_raw_publication_allowed")
DERIVED = "range_20obs_pct previous_20obs_low_ex_today current_low no_new_low_previous20obs price_state stratification_feature_supported stratification_unsupported_reasons".split()
STATS_FIELDS = "win_count neutral_count failure_count win_rate_pct neutral_rate_pct failure_rate_pct mean_net_return_pct median_net_return_pct high_return_ge10_rate_pct loss_le_minus10_rate_pct min_net_return_pct max_net_return_pct".split()
CONTRAST_FIELDS = "tdcc_400_change_sum tdcc_1000_change_sum tdcc_400_up_weeks tdcc_1000_up_weeks tdcc_both_net_positive tdcc_both_up_count_ge2 return_5d return_20d range_20obs_pct no_new_low_previous20obs history_gap_count".split()
CONTRAST_FIELDS += ["price_state_" + state for state in ("falling", "short_rebound_in_decline", "nonnegative_short_and_medium", "short_pullback")]
SCHEMAS = {
    "features": annual_io.FEATURE_FIELDS + DERIVED,
    "trades": ["variant", "partition", "feature_id"] + annual_io.SCHEMAS["trades"] + ["entry_index", "exit_target_index"],
    "blocked": ["variant", "partition", "feature_id"] + annual_io.SCHEMAS["blocked"] + ["entry_index", "exit_target_index"],
    "training_contrasts": "population feature_name outcome_group samples valid_samples missing_samples mean median q25 q75 minimum maximum".split(),
    "summary": "variant horizon slippage_bps partition population samples stocks signal_dates entry_dates total_input_signals condition_passed_signals unsupported_signals filter_rejected_signals overlap_blocked_signals missing_entry_signals entry_after_as_of_signals immature_positions missing_exit_positions purged_positions anomaly_candidate_positions".split() + STATS_FIELDS + ["formal_use", "promotion_evidence_allowed"],
    "anomalies": ["variant", "partition", "slippage_bps"] + annual_io.SCHEMAS["anomalies"],
}
APPROVED_CONTRACT_SHA256 = "1449b79b9778e7b1ecdf39f874f90e29d970fa1e728ae4427dddfcd0683e191d"
StatTrade = namedtuple("StatTrade", "variant partition feature_id signal_date stock_id horizon slippage_bps entry_date exit_date net_return_pct trade_id published_anomaly")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical_json(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")


def artifact_name(kind):
    extension = "json" if kind in {"source_manifest", "candidate_rules"} else "md" if kind == "report" else "csv.gz" if kind in {"features", "trades", "blocked"} else "csv"
    return f"{PREFIX}{kind}_v1.{extension}"


def decimal_value(value):
    try:
        number = Decimal(str(value).replace(",", "").strip())
        return number if number.is_finite() else None
    except (InvalidOperation, ValueError, TypeError):
        return None


def quantile_type7(values, probability):
    """Linear interpolation at (n-1)*p, never a percentile over validation rows."""
    sample = [decimal_value(value) for value in values]
    if not sample or any(value is None for value in sample):
        raise ValueError("type7 requires nonempty finite observations")
    sample.sort()
    with localcontext() as context:
        context.prec = 50
        probability = Decimal(str(probability))
        if not Decimal(0) <= probability <= Decimal(1):
            raise ValueError("type7 probability outside [0,1]")
        position = (len(sample) - 1) * probability
        left = int(position)
        right = min(left + 1, len(sample) - 1)
        return sample[left] + (position - left) * (sample[right] - sample[left])


def session_calendar(closures, start="20250401", end="20261030"):
    closed = set(closures)
    current, last = (datetime.strptime(value, "%Y%m%d") for value in (start, end))
    result = []
    while current <= last:
        date = current.strftime("%Y%m%d")
        if current.weekday() < 5 and date not in closed:
            result.append(date)
        current += timedelta(days=1)
    return result


def holding_dates(calendar, signal_date, horizon, as_of=AS_OF):
    index = bisect.bisect_right(calendar, signal_date)
    if horizon not in HORIZONS or index == 0 or calendar[index - 1] != signal_date or index >= len(calendar):
        raise ValueError("signal/session/horizon identity invalid")
    target = index + horizon
    return dict(entry_date=calendar[index], exit_date=calendar[target] if target < len(calendar) else "",
                entry_index=index, exit_target_index=target,
                mature=target < bisect.bisect_right(calendar, as_of))


def partition(entry_date, exit_date, split=SPLIT):
    if entry_date >= split:
        return "validation"
    return "training" if exit_date and exit_date < split else "purged_cross_split"


def valid_price(row):
    if not row or any(decimal_value(row.get(key)) is None or decimal_value(row[key]) <= 0 for key in ("open", "high", "low", "close")):
        return False
    numbers = {key: decimal_value(row[key]) for key in ("open", "high", "low", "close")}
    return numbers["low"] <= numbers["open"] <= numbers["high"] and numbers["low"] <= numbers["close"] <= numbers["high"] and not any(row.get(key) for key in ("duplicate_key", "date_mismatch", "alias_payload_conflict"))


def cashflows(entry_open, exit_close, slippage_bps):
    entry, exit_ = decimal_value(entry_open), decimal_value(exit_close)
    if entry is None or exit_ is None or min(entry, exit_) <= 0 or slippage_bps not in SLIPPAGES:
        raise ValueError("invalid operation price or frozen cost scenario")
    with localcontext() as context:
        context.prec = 50
        slip = Decimal(slippage_bps) / 10000
        entry_notional = entry * 1000 * (1 + slip)
        exit_notional = exit_ * 1000 * (1 - slip)
        buy_fee = max(Decimal(20), entry_notional * Decimal("0.001425"))
        sell_fee = max(Decimal(20), exit_notional * Decimal("0.001425"))
        tax = exit_notional * Decimal("0.003")
        cost, proceeds = entry_notional + buy_fee, exit_notional - sell_fee - tax
        pnl = proceeds - cost
        return dict(entry_open=str(entry), exit_close=str(exit_), shares="1000", entry_notional=str(entry_notional),
                    buy_fee=str(buy_fee), entry_cash=str(cost), exit_notional=str(exit_notional), sell_fee=str(sell_fee),
                    sell_tax=str(tax), net_exit_cash=str(proceeds), net_pnl=str(pnl), gross_return_pct=str((exit_ / entry - 1) * 100),
                    net_return_pct=str(pnl / cost * 100), outcome="win" if pnl > 0 else "failure" if pnl < 0 else "neutral")


def derive_warmup_projection(repository_root, input_root):
    """Pre-performance source reference: no trades, outcomes or new output read.

    The only exported private-source information is a derived window minimum,
    immutable observation identity and provenance. Exact rows are later frozen
    in the reviewed contract; this is not a general missing-price fallback.
    """
    git = annual_io.GitReader(repository_root)
    original = json.loads(git.read(BASE_REF, annual_io.CONTRACT_FILE))
    if digest(canonical_json(original)) != annual_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual source contract mismatch")
    inputs = annual_io.PrivateInputs(input_root, original)
    prices = annual_io.CurrentPrices(git, inputs, original)
    warmups = {(date, stock): row for date, stocks in prices.supplements.items()
               if date < original["requested_signal_start"] for stock, row in stocks.items()}
    payload = git.read(BASE_REF, DIRECTORY + "/" + annual_io.artifact_name("signals"))
    result, used_pairs = [], set()
    for signal in annual_io.rows_for("signals", payload):
        dates = signal["observed_history_dates"].split(";")
        gaps = [date for date in dates if (date, signal["stock_id"]) in warmups]
        if not gaps:
            continue
        if len(dates) != 21 or dates != sorted(set(dates)) or dates[-1] != signal["signal_date"]:
            raise ValueError("warmup projection observation identity mismatch")
        observations = [prices.daily(date)[0].get(signal["stock_id"]) for date in dates]
        if not all(valid_price(row) for row in observations):
            raise ValueError("warmup projection required source invalid")
        sources = sorted({(warmups[(date, signal["stock_id"])]["source_path"].removeprefix("external:"),
                           warmups[(date, signal["stock_id"])]["source_sha256"]) for date in gaps})
        used_pairs.update((date, signal["stock_id"]) for date in gaps)
        result.append(dict(feature_id=signal["feature_id"], signal_date=signal["signal_date"], stock_id=signal["stock_id"],
                           observed_dates=dates, observed_dates_sha256=digest(canonical_json(dates)),
                           previous_20obs_low_ex_today=str(min(decimal_value(row["low"]) for row in observations[:-1])),
                           missing_observation_dates=gaps,
                           warmup_sources=[dict(path=path, sha256=sha) for path, sha in sources]))
    if len(result) != 44 or len(used_pairs) != 65 or len({row["feature_id"] for row in result}) != 44:
        raise ValueError(f"exact warmup projection scope mismatch: rows={len(result)} pairs={len(used_pairs)}")
    return dict(rows=result, row_count=44, missing_pair_count=65, rows_sha256=digest(canonical_json(result)),
                scope="pre_performance_derived_previous20obs_minimum_only; not_private_raw_quotes")


def source_price(prices, date, stock):
    return prices.daily(date)[0].get(stock) if date else None


def derive_feature(signal, prices, projection=None):
    """Observe one immutable date window; never consult outcomes or newer prices."""
    errors, extension = [], {}
    high, low = decimal_value(signal.get("high_20")), decimal_value(signal.get("low_20"))
    width = None
    if high is None or low is None or not high >= low > 0:
        errors.append("range_frozen_high_low_missing")
    else:
        with localcontext() as context:
            context.prec = 50
            width = (high / low - 1) * 100
    dates = signal.get("observed_history_dates", "").split(";")
    previous, current = None, None
    if len(dates) != 21 or sorted(set(dates)) != dates or dates[-1] != signal["signal_date"]:
        errors.append("observed_history_dates_invalid")
    else:
        window = [source_price(prices, date, signal["stock_id"]) for date in dates]
        missing = [date for date, row in zip(dates, window) if not valid_price(row)]
        if projection is not None:
            if projection["feature_id"] != signal["feature_id"] or projection["signal_date"] != signal["signal_date"] or projection["stock_id"] != signal["stock_id"] or projection["observed_dates"] != dates or projection["observed_dates_sha256"] != digest(canonical_json(dates)):
                raise ValueError("fixed warmup projection observation binding mismatch")
            if missing and missing != projection["missing_observation_dates"]:
                raise ValueError("fixed warmup projection missing-date scope mismatch")
            if not valid_price(window[-1]):
                raise ValueError("projection cannot substitute today's quote")
            projected = decimal_value(projection["previous_20obs_low_ex_today"])
            if projected is None or projected <= 0:
                raise ValueError("invalid projected window minimum")
            if not missing:
                previous = min(decimal_value(row["low"]) for row in window[:-1])
                if previous != projected:
                    raise ValueError("raw independent minimum differs from frozen projection")
            else:
                previous = projected
            current = decimal_value(window[-1]["low"])
        elif missing:
            errors.append("observed_window_price_missing_or_invalid")
        else:
            previous = min(decimal_value(row["low"]) for row in window[:-1])
            current = decimal_value(window[-1]["low"])
    r5, r20 = decimal_value(signal.get("return_5d")), decimal_value(signal.get("return_20d"))
    states = {(True, True): "falling", (True, False): "short_rebound_in_decline", (False, True): "short_pullback", (False, False): "nonnegative_short_and_medium"}
    extension.update(range_20obs_pct="" if width is None else str(width), previous_20obs_low_ex_today="" if previous is None else str(previous), current_low="" if current is None else str(current), no_new_low_previous20obs="" if previous is None or current is None else current >= previous,
                     price_state="unsupported" if r5 is None or r20 is None else states[r20 < 0, r5 < 0], stratification_feature_supported=not errors, stratification_unsupported_reasons=";".join(errors))
    return dict(signal, **extension)


def condition(feature, variant, threshold):
    """Return (passes, supported); one filter never inherits another's gate."""
    if variant == "baseline":
        return True, True
    operands = {
        "tdcc_both_net_positive": ("tdcc_400_change_sum", "tdcc_1000_change_sum"),
        "tdcc_both_up_count_ge2": ("tdcc_400_up_weeks", "tdcc_1000_up_weeks"),
        "price_5obs_nonnegative": ("return_5d",),
        "range_20obs_le_training_q75": ("range_20obs_pct",),
        "no_new_low_previous20obs": ("current_low", "previous_20obs_low_ex_today"),
    }
    if variant not in operands:
        raise ValueError("unregistered variant")
    values = [decimal_value(feature.get(key)) for key in operands[variant]]
    if any(value is None for value in values) or variant == "range_20obs_le_training_q75" and threshold is None:
        return False, False
    if variant == "tdcc_both_net_positive":
        return all(value > 0 for value in values), True
    if variant == "tdcc_both_up_count_ge2":
        return all(value >= 2 for value in values), True
    if variant == "price_5obs_nonnegative":
        return values[0] >= 0, True
    if variant == "range_20obs_le_training_q75":
        return values[0] <= threshold, True
    return values[0] >= values[1], True


def ledger_rows(features, prices, calendar, variant, threshold, horizon, as_of=AS_OF, split=SPLIT):
    locked_until = {}
    for feature in features:
        date, stock = feature["signal_date"], feature["stock_id"]
        target = holding_dates(calendar, date, horizon, as_of)
        mature = target.pop("mature")
        entry, exit_ = target["entry_date"], target["exit_date"]
        common = dict(variant=variant, partition=partition(entry, exit_, split), feature_id=feature["feature_id"], signal_date=date, stock_id=stock, horizon=horizon, **target)
        passed, supported = condition(feature, variant, threshold)
        if not supported or not passed:
            yield "blocked", dict(common, record_type="condition_rejected" if supported else "condition_unavailable", reasons="single_condition_false" if supported else "required_feature_unsupported", primary_row_retained=True)
            continue
        ep = source_price(prices, entry, stock) if entry <= as_of else None
        xp = source_price(prices, exit_, stock) if mature else None
        strict = "blocked_entry_after_as_of" if entry > as_of else "blocked_entry_price" if not valid_price(ep) else "blocked_input_availability_unproven"
        common["strict_v3_status"] = strict
        yield "blocked", dict(common, record_type="strict_ledger_decision", reasons=strict, entry_open=ep["open"] if ep else "", strict_entry_established=False, strict_prior_position_locked=False, proxy_result_must_not_release_strict_lock=True)
        prior = locked_until.get(stock)
        rejection = ("blocked_exit_day" if date == prior else "blocked_active_position") if prior and date <= prior else "entry_after_as_of" if entry > as_of else "entry_price_missing_or_invalid" if not valid_price(ep) else ""
        if rejection:
            yield "blocked", dict(common, record_type="operation_no_entry", reasons=rejection)
            continue
        locked_until[stock] = exit_ if mature and valid_price(xp) else "99999999"
        if not mature or not valid_price(xp):
            yield "blocked", dict(common, record_type="operation_censored", reasons="open_immature" if not mature else "open_unresolved_exit_price", entry_open=ep["open"])
            continue
        for slip in SLIPPAGES:
            yield "trades", dict(common, trade_id=f"{variant}:{date}:{stock}:D{horizon}:S{slip}", stock_name=feature["stock_name"], market=feature["market"], slippage_bps=slip, **cashflows(ep["open"], xp["close"], slip), simulation_status="realized_raw_price_proxy", strict_missing_evidence="corporate_action_complete_coverage;calendar_event_full_audit", ca_cashflow_assumption="not_applied_not_asserted_absent", total_return_verified=False, input_ref=PRICE_REF, receipt_id="", outcome_ref=PRICE_REF, entry_source_path=ep["source_path"], entry_source_sha256=ep["source_sha256"], exit_source_path=xp["source_path"], exit_source_sha256=xp["source_sha256"], history_gap_count=feature["history_gap_count"], anomaly_candidate=False, primary_row_retained=True, formal_use=False, promotion_evidence_allowed=False)


def records(kind, payload):
    binary = gzip.GzipFile(fileobj=io.BytesIO(payload), mode="rb") if kind in {"features", "trades", "blocked"} else io.BytesIO(payload)
    with io.TextIOWrapper(binary, encoding="utf-8", newline="") as stream:
        def lines():
            for line in stream:
                if "\r" in line or line.startswith("\ufeff") or not line.endswith("\n"):
                    raise ValueError(f"{kind}: noncanonical UTF-8/LF serialization")
                yield line
        reader = csv.DictReader(lines(), strict=True)
        if reader.fieldnames != SCHEMAS[kind]:
            raise ValueError(f"{kind}: exact schema mismatch")
        for row in reader:
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"{kind}: malformed row width")
            yield row


def compare_row(kind, actual, expected, ignore=()):
    if actual is None:
        raise ValueError(f"{kind}: missing expected row")
    for field in SCHEMAS[kind]:
        if field in ignore:
            continue
        a, b = actual.get(field, ""), expected.get(field, "")
        # csv.DictWriter serializes None as an empty cell; zero and False are
        # values, not missing data, and must retain their distinct spellings.
        a, b = "" if a is None else str(a), "" if b is None else str(b)
        if a == b:
            continue
        # Frozen feature spellings and all identity/count/boolean fields are exact.
        numeric = field in STATS_FIELDS or field in {"mean", "median", "q25", "q75", "minimum", "maximum"}
        x, y = decimal_value(a), decimal_value(b)
        if numeric and x is not None and y is not None and math.isclose(float(x), float(y), rel_tol=1e-12, abs_tol=1e-12):
            continue
        if kind == "trades" and field in cashflows(1, 1, 0) and field != "outcome" and x is not None and y is not None and x == y:
            continue
        raise ValueError(f"{kind}: {field}={a!r} differs from independent {b!r}; {expected.get('feature_id', '')}")


def compare_sequence(kind, actual, expected):
    actual = iter(actual)
    for row in expected:
        compare_row(kind, next(actual, None), row)
    if next(actual, None) is not None:
        raise ValueError(f"{kind}: extra row")


def compact_trade(row, published=None):
    return StatTrade(*(row[key] for key in StatTrade._fields[:-1]), published)


def outcome_group(value):
    value = decimal_value(value)
    return "high" if value >= 10 else "low" if value <= -10 else "middle"


def training_material(baseline, by_id, contract, retained):
    selected = [row for row in baseline if row.horizon == 20 and row.slippage_bps == 10 and row.partition == "training"]
    # Primary only: no anomaly marker participates in threshold construction.
    widths = [decimal_value(by_id[row.feature_id]["range_20obs_pct"]) for row in selected]
    widths = [value for value in widths if value is not None]
    threshold = quantile_type7(widths, "0.75") if widths else None
    old = {(row["signal_date"], row["stock_id"], int(row["horizon"])) for row in retained if int(row["horizon"]) == 20}
    contrasts = []
    for population in ("primary", "immutable_prior_candidate_exclusion_sensitivity"):
        available = [row for row in selected if population == "primary" or (row.signal_date, row.stock_id, 20) not in old]
        for group in ("all_training", "high", "low", "middle"):
            sample = [row for row in available if group == "all_training" or outcome_group(row.net_return_pct) == group]
            for field in CONTRAST_FIELDS:
                values = []
                for row in sample:
                    feature = by_id[row.feature_id]
                    if field.startswith("price_state_"):
                        value = None if feature["price_state"] == "unsupported" else Decimal(int(feature["price_state"] == field.removeprefix("price_state_")))
                    elif field in {"tdcc_both_net_positive", "tdcc_both_up_count_ge2", "no_new_low_previous20obs"}:
                        passed, supported = condition(feature, field, None)
                        value = Decimal(int(passed)) if supported else None
                    else:
                        value = decimal_value(feature.get(field))
                    if value is not None:
                        values.append(value)
                with localcontext() as context:
                    context.prec = 50
                    contrasts.append(dict(population=population, feature_name=field, outcome_group=group, samples=len(sample), valid_samples=len(values), missing_samples=len(sample)-len(values),
                        mean=str(sum(values)/len(values)) if values else "", median=str(quantile_type7(values, "0.5")) if values else "", q25=str(quantile_type7(values, "0.25")) if values else "", q75=str(quantile_type7(values, "0.75")) if values else "", minimum=str(min(values)) if values else "", maximum=str(max(values)) if values else ""))
    rules = dict(artifact_version=PREFIX + "v1", training_partition="training", training_horizon=20, training_slippage_bps=10,
                 training_positions=len(selected), training_stocks=len({row.stock_id for row in selected}), training_signal_dates=len({row.signal_date for row in selected}), training_width_samples=len(widths), threshold_feature="range_20obs_pct", quantile_algorithm="Hyndman-Fan type 7", quantile_probability="0.75", training_q75="" if threshold is None else str(threshold), threshold_supported=threshold is not None,
                 training_trade_keys_sha256=digest(canonical_json([row.trade_id for row in selected])), training_widths_sha256=digest(canonical_json([str(value) for value in widths])), training_outcome_group_counts=dict(Counter(outcome_group(row.net_return_pct) for row in selected)), immutable_training_candidate_group_counts=dict(Counter(outcome_group(row.net_return_pct) for row in selected if (row.signal_date, row.stock_id, 20) in old)),
                 variants=contract["variants"], selection_uses_validation=False, selection_uses_anomaly_exclusion=False, formal_use=False, promotion_evidence_allowed=False)
    return threshold, contrasts, rules


def anomaly_rows(trades, retained):
    old = {(row["signal_date"], row["stock_id"], int(row["horizon"])) for row in retained}
    keys, result = set(), []
    for horizon in HORIZONS:
        sample = [row for row in trades if row.horizon == horizon and row.slippage_bps == 10]
        values = sorted(float(row.net_return_pct) for row in sample)
        bounds = None
        if len(values) >= 4:
            # Inclusive type-7 quartiles on the complete ledger, never partitions.
            def percentile(p):
                at = (len(values)-1)*p
                lo = int(at)
                return values[lo] + (values[min(lo+1, len(values)-1)]-values[lo])*(at-lo)
            q1, q3 = percentile(0.25), percentile(0.75)
            bounds = q1-3*(q3-q1), q3+3*(q3-q1)
        for row in sample:
            key = row.signal_date, row.stock_id, horizon
            previous = key in old
            if not previous and (bounds is None or bounds[0] <= float(row.net_return_pct) <= bounds[1]):
                continue
            keys.add(key)
            result.append(dict(variant=row.variant, partition=row.partition, slippage_bps=10, signal_date=row.signal_date, stock_id=row.stock_id, horizon=horizon, net_return_pct=row.net_return_pct,
                reason="immutable_previous_candidate_retained" if previous else "ledger_Q1_Q3_plus_3IQR_descriptive_candidate", disposition="unresolved_anomaly_candidate", primary_row_retained=True, exclusion_allowed_only_as_sensitivity=True, entry_date=row.entry_date, exit_date=row.exit_date, represented_in_current_proxy_trade=True))
    for row in trades:
        if row.published_anomaly is not None and row.published_anomaly is not ((row.signal_date, row.stock_id, row.horizon) in keys):
            raise ValueError("trade candidate flag differs from independent retained/full-ledger IQR membership")
    return result, keys


def return_statistics(values):
    size = len(values)
    counts = {"win": sum(value > 0 for value in values), "neutral": sum(value == 0 for value in values), "failure": sum(value < 0 for value in values)}
    result = {key + "_count": count for key, count in counts.items()}
    result.update({key + "_rate_pct": count / size * 100 if size else "" for key, count in counts.items()})
    result.update(mean_net_return_pct=statistics.mean(values) if size else "", median_net_return_pct=statistics.median(values) if size else "", high_return_ge10_rate_pct=sum(value >= 10 for value in values)/size*100 if size else "", loss_le_minus10_rate_pct=sum(value <= -10 for value in values)/size*100 if size else "", min_net_return_pct=min(values) if size else "", max_net_return_pct=max(values) if size else "")
    return result


def summaries(trades, blocked, input_counts, variant, anomaly_keys):
    result = []
    for horizon in HORIZONS:
        for part in PARTITIONS:
            counter = Counter()
            for (partition_, holding, kind, reason), count in blocked.items():
                if horizon == holding and (part == "all" or partition_ == part):
                    counter[kind, reason] += count
            def count(kind, reason=None):
                return sum(n for (k, r), n in counter.items() if k == kind and (reason is None or reason == r))
            for slip in SLIPPAGES:
                for population in ("primary", "sensitivity_excluding_candidates"):
                    sample = [row for row in trades if row.horizon == horizon and row.slippage_bps == slip and (part == "all" or row.partition == part) and (population == "primary" or (row.signal_date, row.stock_id, horizon) not in anomaly_keys)]
                    result.append(dict(variant=variant, horizon=horizon, slippage_bps=slip, partition=part, population=population, samples=len(sample), stocks=len({row.stock_id for row in sample}), signal_dates=len({row.signal_date for row in sample}), entry_dates=len({row.entry_date for row in sample}),
                        total_input_signals=sum(input_counts[horizon].values()) if part == "all" else input_counts[horizon][part], condition_passed_signals=count("strict_ledger_decision"), unsupported_signals=count("condition_unavailable"), filter_rejected_signals=count("condition_rejected"), overlap_blocked_signals=count("operation_no_entry", "blocked_active_position") + count("operation_no_entry", "blocked_exit_day"), missing_entry_signals=count("operation_no_entry", "entry_price_missing_or_invalid"), entry_after_as_of_signals=count("operation_no_entry", "entry_after_as_of"), immature_positions=count("operation_censored", "open_immature"), missing_exit_positions=count("operation_censored", "open_unresolved_exit_price"), purged_positions=sum(row.partition == "purged_cross_split" for row in sample), anomaly_candidate_positions=sum((row.signal_date, row.stock_id, horizon) in anomaly_keys for row in sample), **return_statistics([float(row.net_return_pct) for row in sample]), formal_use=False, promotion_evidence_allowed=False))
    return result


def contract_audit(contract):
    if digest(canonical_json(contract)) != APPROVED_CONTRACT_SHA256:
        raise ValueError("fixed stratification contract SHA256 mismatch")
    required = dict(base_artifact_ref=BASE_REF, protected_artifact_ref=PROTECTED_REF, code_source_ref=PROTECTED_REF, price_source_ref=PRICE_REF, validation_entry_start=SPLIT, as_of=AS_OF, horizons=list(HORIZONS), slippage_bps=list(SLIPPAGES), artifact_directory=DIRECTORY)
    if any(contract.get(key) != value for key, value in required.items()):
        raise ValueError("fixed source/date/operation contract mismatch")
    if any(contract.get(flag) is not False for flag in FALSE_FLAGS):
        raise ValueError("research-only contract boundary mismatch")
    if tuple(row["variant_id"] for row in contract["variants"]) != VARIANTS or contract["artifact_filenames"] != [artifact_name(kind) for kind in KINDS]:
        raise ValueError("exact variant/artifact allowlist mismatch")
    projection = contract["published_warmup_low_projection"]
    if projection["row_count"] != 44 or projection["missing_pair_count"] != 65 or len(projection["rows"]) != 44 or digest(canonical_json(projection["rows"])) != projection["rows_sha256"]:
        raise ValueError("fixed projection digest/cardinality mismatch")


def load_context(repository_root, contract, *, input_root=None, price_repository_root=None, published_only=False):
    git = annual_io.GitReader(price_repository_root or repository_root)
    original = json.loads(git.read(BASE_REF, annual_io.CONTRACT_FILE))
    if digest(canonical_json(original)) != annual_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual contract digest mismatch")
    original_manifest = json.loads(git.read(BASE_REF, DIRECTORY + "/" + annual_io.artifact_name("source_manifest")))
    if original_manifest["contract"] != original or original_manifest["contract_sha256"] != annual_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable annual manifest contract mismatch")
    payloads = {}
    for kind in ("signals", "features", "anomalies"):
        name = annual_io.artifact_name(kind)
        raw = git.read(BASE_REF, DIRECTORY + "/" + name)
        if original_manifest["hashes"][name] != dict(bytes=len(raw), sha256=digest(raw)):
            raise ValueError("immutable annual evidence content mismatch")
        payloads[kind] = raw
    hcontract = json.loads(git.read(PROTECTED_REF, horizon_io.CONTRACT_FILE))
    if digest(canonical_json(hcontract)) != horizon_io.APPROVED_CONTRACT_SHA256:
        raise ValueError("immutable horizon contract digest mismatch")
    hmanifest = json.loads(git.read(PROTECTED_REF, DIRECTORY + "/" + horizon_io.name("source_manifest")))
    hraw = git.read(PROTECTED_REF, DIRECTORY + "/" + horizon_io.name("anomalies"))
    if hmanifest["hashes"][horizon_io.name("anomalies")] != dict(bytes=len(hraw), sha256=digest(hraw)):
        raise ValueError("immutable horizon candidate source mismatch")
    retained = list(annual_io.rows_for("anomalies", payloads["anomalies"]))
    retained.extend(row for row in horizon_io.records("anomalies", hraw) if row["profile"] == "full_period" and row["horizon"] == "60")
    closures = original_manifest["evidence"]["calendar_closures"]
    inputs = None
    if published_only:
        prices = horizon_io.PublishedPrices(git, original, payloads["features"])
    else:
        if input_root is None:
            raise ValueError("full source validation requires --input-root; public mode requires explicit --published-only")
        inputs = annual_io.PrivateInputs(input_root, original)
        for item in original["external_files"]:
            inputs.read(item)
        prices = annual_io.CurrentPrices(git, inputs, original)
        calendar_item = next(item for item in original["external_files"] if item["kind"] == "calendar")
        raw_closures = {row["date"] for row in annual_io.csv_records(inputs.read(calendar_item)) if row["scheduled_closed"] == "True"}
        for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv"):
            raw_closures.update(row["date"] for row in annual_io.csv_records(git.read(PRICE_REF, path)))
        if sorted(raw_closures) != closures:
            raise ValueError("independent raw calendar differs from immutable reference")
    return dict(git=git, original=original, original_manifest=original_manifest, signals_payload=payloads["signals"], retained=retained,
                prices=prices, closures=closures, calendar=session_calendar(closures, original["history_start"], original["calendar_end"]), inputs=inputs)


def projection_map(contract, original):
    rows = contract["published_warmup_low_projection"]["rows"]
    sources = {item["path"]: item for item in original["external_files"] if item["kind"] == "price_warmup"}
    result, pairs = {}, set()
    for row in rows:
        if row["feature_id"] in result or row["feature_id"] != row["signal_date"] + ":" + row["stock_id"]:
            raise ValueError("fixed projection duplicate/invalid key")
        dates = row["observed_dates"]
        if len(dates) != 21 or sorted(set(dates)) != dates or dates[-1] != row["signal_date"] or digest(canonical_json(dates)) != row["observed_dates_sha256"]:
            raise ValueError("fixed projection observation dates/hash mismatch")
        if not row["missing_observation_dates"] or not set(row["missing_observation_dates"]) <= set(dates[:-1]):
            raise ValueError("fixed projection missing dates mismatch")
        expected_sources = set()
        for date in row["missing_observation_dates"]:
            matches = [item for item in sources.values() if item["stock_id"] == row["stock_id"] and date[:6] in item["path"]]
            if len(matches) != 1:
                raise ValueError("projection raw warmup month source absent/ambiguous")
            expected_sources.add((matches[0]["path"], matches[0]["sha256"]))
            pairs.add((date, row["stock_id"]))
        actual_sources = [(item["path"], item["sha256"]) for item in row["warmup_sources"]]
        if actual_sources != sorted(expected_sources):
            raise ValueError("projection exact source hash binding mismatch")
        result[row["feature_id"]] = row
    if len(result) != 44 or len(pairs) != 65:
        raise ValueError("projection exact row/pair set differs")
    return result


def audit_features(context, contract, payload):
    actual = iter(records("features", payload))
    projections = projection_map(contract, context["original"])
    used, features, previous, pool = set(), [], None, {}
    fields = ("feature_id", "signal_date", "stock_id", "stock_name", "market", "history_gap_count", "tdcc_400_change_sum", "tdcc_1000_change_sum", "tdcc_400_up_weeks", "tdcc_1000_up_weeks", "return_5d", "return_20d", *DERIVED)
    for signal in annual_io.rows_for("signals", context["signals_payload"]):
        key = signal["signal_date"], signal["stock_id"]
        if previous is not None and key <= previous:
            raise ValueError("immutable signals not unique chronological rows")
        previous = key
        if signal["feature_id"] != ":".join(key) or signal["input_ref"] != PRICE_REF or signal["selected"] != "True" or signal["feature_supported"] != "True" or any(signal[field] != "False" for field in ("formal_use", "promotion_evidence_allowed", "input_availability_proven")) or any(signal[field] for field in ("receipt_id", "available_no_later_than", "entry_cutoff")):
            raise ValueError("immutable signal source/research/identity boundary drift")
        projection = projections.get(signal["feature_id"])
        if projection:
            used.add(signal["feature_id"])
        if context["inputs"] is not None:
            private = context["prices"].supplements
            missing = [date for date in signal["observed_history_dates"].split(";") if date < context["original"]["requested_signal_start"] and signal["stock_id"] in private.get(date, {})]
            if missing != (projection["missing_observation_dates"] if projection else []):
                raise ValueError("full raw warmup gap identity differs from frozen exact projection")
        expected = derive_feature(signal, context["prices"], projection)
        compare_row("features", next(actual, None), expected)
        features.append({field: pool.setdefault(expected[field], expected[field]) if field in {"signal_date", "stock_id", "stock_name", "market", "price_state"} else expected[field] for field in fields})
    if next(actual, None) is not None or used != set(projections) or len(features) != context["original_manifest"]["counts"]["signals"]:
        raise ValueError("features row population / exact44 projection use mismatch")
    return features


def audit_source_bindings(context, contract, manifest):
    git, original = context["git"], context["original"]
    expected = {(BASE_REF, annual_io.CONTRACT_FILE)} | {(BASE_REF, DIRECTORY + "/" + annual_io.artifact_name(kind)) for kind in ("source_manifest", "signals", "features", "anomalies")}
    expected |= {(PROTECTED_REF, horizon_io.CONTRACT_FILE)} | {(PROTECTED_REF, DIRECTORY + "/" + horizon_io.name(kind)) for kind in ("source_manifest", "anomalies")}
    expected |= {(PRICE_REF, path) for path in git.tree(PRICE_REF) if re.fullmatch(r"data/daily_price/[0-9]{8}\.csv", path) and original["history_start"] <= path[-12:-4] <= original["as_of"]}
    expected |= {(PRICE_REF, path) for path in ("config/twse_non_trading_days.csv", "data/market_calendar/exceptional_non_trading_days.csv")}
    declared = manifest["sources"]
    if len(declared) != len(expected) or {(row["ref"], row["path"]) for row in declared} != expected:
        raise ValueError("manifest exact immutable source set mismatch")
    for row in declared:
        key = row["ref"], row["path"]
        if key not in git.used:
            git.read(*key)
        if row != git.used[key]:
            raise ValueError("manifest immutable source bytes/blob/hash mismatch")
    external = context["original_manifest"]["external_sources"]
    if manifest["external_sources"] != external:
        raise ValueError("manifest exact65 external source bindings mismatch")
    if context["inputs"] is not None and {row["path"]: row for row in external} != context["inputs"].used:
        raise ValueError("actual private65 input hashes/byte counts mismatch")


def audit_report(payload, rules, summaries_, anomalies, contrasts):
    report = payload.decode("utf-8")
    if report.startswith("\ufeff") or "\r" in report or not report.endswith("\n"):
        raise ValueError("report serialization mismatch")
    required = ("research_only", "formal_use=False", "promotion_evidence_allowed=False", "不是strict PIT", "total-return", "不是完全盲測", "D20主要、D60僅robustness", "切分不重置", "精確44個warmup缺口", "原65份私有來源", "零分母為空", "未解數值候選", "不是corrected/cleaned performance", "不使用月營收")
    if any(text not in report for text in required):
        raise ValueError("report research/source/denominator caveat missing")
    training = f"訓練baseline D20/10bps：{rules['training_positions']}部位、{rules['training_stocks']}股、{rules['training_signal_dates']}訊號日期；寬度有效分母{rules['training_width_samples']}；type7 Q75={rules['training_q75']}。"
    if training not in report or f"未解數值候選{len(anomalies)}列" not in report:
        raise ValueError("report training/anomaly counts mismatch")
    sections = {}
    for fragment in report.split("\n## ")[1:]:
        title, _, body = fragment.partition("\n")
        if title in sections:
            raise ValueError("duplicate report section")
        sections[title] = body
    if "固定五個單項條件" not in sections:
        raise ValueError("report section missing: fixed five conditions")
    legends = [line.split("|")[1].strip() for line in sections["固定五個單項條件"].splitlines() if line.startswith("| ")][1:]
    if legends != list(VARIANTS[1:]):
        raise ValueError("report fixed single-condition legend mismatch")
    lookup = {(row["population"], row["feature_name"], row["outcome_group"]): row for row in contrasts}
    contrast_table = []
    for population in ("primary", "immutable_prior_candidate_exclusion_sensitivity"):
        for field in ("tdcc_both_net_positive", "tdcc_both_up_count_ge2", "no_new_low_previous20obs", "range_20obs_pct", "return_5d"):
            statistic = "median" if field in {"range_20obs_pct", "return_5d"} else "mean"
            contrast_table.append([population, field, statistic] + [lookup[population, field, group][statistic] for group in ("high", "low", "middle")])
    main = []
    reasons = []
    for row in summaries_:
        if row["slippage_bps"] != 10:
            continue
        if row["partition"] in {"training", "validation"}:
            main.append([row[k] for k in ("variant", "horizon", "partition", "population", "samples", "stocks", "signal_dates", "entry_dates")] + [f"{row['win_count']}/{row['neutral_count']}/{row['failure_count']}", f"{row['win_rate_pct']}/{row['neutral_rate_pct']}/{row['failure_rate_pct']}"] + [row[k] for k in ("mean_net_return_pct", "median_net_return_pct", "high_return_ge10_rate_pct", "loss_le_minus10_rate_pct")])
        if row["population"] == "primary" and row["partition"] != "all":
            reasons.append([row[k] for k in ("variant", "horizon", "partition", "unsupported_signals", "filter_rejected_signals", "overlap_blocked_signals", "missing_entry_signals", "immature_positions", "missing_exit_positions", "purged_positions")])
    for title, expected in (("訓練高／低報酬特徵對照（D20／10 bps）", contrast_table), ("訓練／驗證主要與敏感性對照（10 bps）", main), ("缺證、未成熟與重疊（10 bps primary）", reasons)):
        if title not in sections:
            raise ValueError("report section missing: " + title)
        table = [line for line in sections[title].splitlines() if line.startswith("| ")][1:]
        rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in table]
        if len(rows) != len(expected):
            raise ValueError("report table row count mismatch: " + title)
        for actual, wanted in zip(rows, expected):
            if len(actual) != len(wanted):
                raise ValueError("report table column count mismatch")
            for a, b in zip(actual, wanted):
                if a == str(b):
                    continue
                x, y = decimal_value(a), decimal_value(b)
                if x is None or y is None or not math.isclose(float(x), float(y), rel_tol=1e-12, abs_tol=1e-12):
                    raise ValueError("report table numeric/identity mismatch")


def validate_artifacts(repository_root, contract, artifacts, *, input_root=None, price_repository_root=None, published_only=False):
    try:
        contract_audit(contract)
        if set(artifacts) != {artifact_name(kind) for kind in KINDS}:
            raise ValueError("all exact nine published artifacts are required")
        if not published_only and input_root is None:
            raise ValueError("full source validation requires --input-root; use explicit --published-only for public evidence")
        manifest = json.loads(artifacts[artifact_name("source_manifest")])
        expected_header = dict(model_id="tdcc_stealth_accumulation", owner_id="tdcc_stealth_accumulation_current_version_annual_replay", artifact_version=PREFIX + "v1", contract_file=CONTRACT_FILE, contract=contract, contract_sha256=APPROVED_CONTRACT_SHA256)
        if any(canonical_json(manifest.get(key)) != canonical_json(value) for key, value in expected_header.items()) or any(manifest.get(flag) is not False for flag in FALSE_FLAGS):
            raise ValueError("manifest fixed contract/research flags mismatch")
        if canonical_json(manifest.get("warmup_projection_audit")) != canonical_json(dict(raw_verified_rows=44, raw_verified_missing_pairs=65, projection_used_as_price_fallback=False)):
            raise ValueError("manifest fixed warmup projection audit mismatch")
        hashes = {name: dict(bytes=len(data), sha256=digest(data)) for name, data in artifacts.items() if name != artifact_name("source_manifest")}
        if manifest["hashes"] != hashes:
            raise ValueError("manifest actual serialized eight-file hash/byte count mismatch")
        for kind in ("source_manifest", "candidate_rules"):
            if canonical_json(json.loads(artifacts[artifact_name(kind)])) != artifacts[artifact_name(kind)]:
                raise ValueError(kind + ": canonical JSON serialization mismatch")
        context = load_context(repository_root, contract, input_root=input_root, price_repository_root=price_repository_root, published_only=published_only)
        original, calendar = context["original"], context["calendar"]
        if manifest["base_contract"] != original or manifest["calendar"] != dict(sessions=calendar, closures=context["closures"], history_start=original["history_start"], calendar_end=original["calendar_end"]):
            raise ValueError("manifest independent calendar/base contract mismatch")
        features = audit_features(context, contract, artifacts[artifact_name("features")])
        by_id = {row["feature_id"]: row for row in features}
        input_counts = {horizon: Counter(partition(**{key: value for key, value in holding_dates(calendar, feature["signal_date"], horizon).items() if key in {"entry_date", "exit_date"}}) for feature in features) for horizon in HORIZONS}
        actual = {kind: iter(records(kind, artifacts[artifact_name(kind)])) for kind in ("trades", "blocked")}
        counts, all_summaries, all_anomalies = Counter(), [], []
        threshold, contrasts, rules = None, None, None
        for variant in VARIANTS:
            trades, blocked = [], Counter()
            for horizon in HORIZONS:
                for kind, expected in ledger_rows(features, context["prices"], calendar, variant, threshold, horizon):
                    row = next(actual[kind], None)
                    compare_row(kind, row, expected, ("anomaly_candidate",) if kind == "trades" else ())
                    counts[kind] += 1
                    if kind == "trades":
                        trades.append(compact_trade(expected, annual_io.bool_value(row["anomaly_candidate"])))
                    else:
                        blocked[expected["partition"], horizon, expected["record_type"], expected["reasons"]] += 1
            if variant == "baseline":
                threshold, contrasts, rules = training_material(trades, by_id, contract, context["retained"])
                if artifacts[artifact_name("candidate_rules")] != canonical_json(rules) or canonical_json(manifest["candidate_rules"]) != canonical_json(rules):
                    raise ValueError("candidate_rules independent primary training source/threshold/denominator mismatch")
                compare_sequence("training_contrasts", records("training_contrasts", artifacts[artifact_name("training_contrasts")]), contrasts)
            anomalies, keys = anomaly_rows(trades, context["retained"])
            all_anomalies.extend(anomalies)
            all_summaries.extend(summaries(trades, blocked, input_counts, variant, keys))
        if any(next(reader, None) is not None for reader in actual.values()):
            raise ValueError("unexpected extra operations beyond independent full chronology")
        compare_sequence("summary", records("summary", artifacts[artifact_name("summary")]), all_summaries)
        compare_sequence("anomalies", records("anomalies", artifacts[artifact_name("anomalies")]), all_anomalies)
        expected_counts = dict(signals=len(features), trades=counts["trades"], blocked=counts["blocked"], summary=len(all_summaries), anomalies=len(all_anomalies), training_contrasts=len(contrasts), baseline_candidate_source_rows=len(context["retained"]), supplemental=context["original_manifest"]["counts"]["supplemental"])
        if manifest["counts"] != expected_counts:
            raise ValueError("manifest independently recomputed population counts mismatch")
        audit_source_bindings(context, contract, manifest)
        audit_report(artifacts[artifact_name("report")], rules, all_summaries, all_anomalies, contrasts)
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
            return ["all exact nine published regular artifacts are required; no skip/fallback"]
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
    arguments = parser.parse_args(argv)
    errors = validate(arguments.repository_root, arguments.output_root, input_root=arguments.input_root, price_repository_root=arguments.price_repository_root, published_only=arguments.published_only)
    if errors:
        for error in errors:
            print("FAIL: " + error)
        return 1
    mode = "immutable_v1_signals + independent_horizon_source_replay + fixed_44_derived_warmup_projection; private_raw_not_reread" if arguments.published_only else "immutable_v1_signals + independent_condition_and_horizon_source_replay; actual65_private_hashes_and_raw44_minima"
    print("PASS: independent condition stratification; " + mode + "; research_only; input_availability_proven=False; promotion_evidence_allowed=False")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
