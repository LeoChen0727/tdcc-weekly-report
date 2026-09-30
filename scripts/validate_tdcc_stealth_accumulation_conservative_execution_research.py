"""獨立核對 TDCC frozen-ledger 保守成交假設；不匯入 producer 業務函式。"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime
from decimal import Decimal, localcontext
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OWNER = "tdcc_stealth_accumulation_conservative_execution_research"
CONTRACT = f"config/{OWNER}_v1.json"
CONTRACT_SHA256 = "3c3c0e12a575ae98a6db3eb0a9a9f71b65d7c7a6b17a5b94b690f1ddbdde2b7a"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
KINDS = ("positions_v1.csv.gz", "summary_v1.csv", "report_v1.md", "source_manifest_v1.json")
EXTRA = "source_trade_row_sha256 execution_model_id execution_cohort_id execution_entry_state execution_exit_state execution_entry_quantity execution_exit_quantity execution_entry_event_ids execution_exit_event_ids execution_entry_reason execution_exit_reason execution_position_state execution_blocking_trade_id execution_lock_retained original_primary_proxy_return_pct execution_proxy_return_pct execution_assumed_completed actual_fill_verified execution_evidence_state exception_coverage_verified".split()
POPULATIONS = ("original_primary_proxy", "assumed_completed_subset", "original_candidate_exclusion_sensitivity", "assumed_completed_candidate_exclusion_sensitivity")


def check(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def name(kind):
    return OWNER + "_" + kind


def records(raw, compressed=False):
    stream = gzip.GzipFile(fileobj=io.BytesIO(raw)) if compressed else io.BytesIO(raw)
    with io.TextIOWrapper(stream, encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        check(fields and len(fields) == len(set(fields)), "missing or duplicate CSV fields")
        rows = list(reader)
    check(all(None not in row and all(v is not None for v in row.values()) for row in rows), "malformed CSV row")
    return fields, rows


def audit_policy(policy):
    check(digest(canonical(policy)) == CONTRACT_SHA256, "frozen policy canonical SHA mismatch")


def read_source(root, policy, source_ledger=None):
    if source_ledger is not None:
        raw = Path(source_ledger).read_bytes()
    else:
        raw = subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), "show", policy["source_ref"] + ":" + policy["source_ledger"]])
    check(digest(raw) == policy["source_ledger_sha256"], "source ledger SHA mismatch")
    selected, total = [], 0
    with gzip.open(io.BytesIO(raw), "rt", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        check(fields and not set(fields).intersection(EXTRA), "source field collision")
        for row in reader:
            total += 1
            if row["strategy"] in policy["strategies"] and all(row[k] == policy[k] for k in ("profile", "partition", "horizon", "slippage_bps")):
                check(row["shares"] == "1000", "source shares changed")
                check(int(row["exit_target_index"]) - int(row["entry_index"]) == 20, "source D20 changed")
                check(row["signal_date"] < row["entry_date"] <= row["exit_date"], "source date sequence changed")
                check(row["primary_row_retained"] == "True", "source primary not retained")
                check(row["formal_use"] == row["promotion_evidence_allowed"] == "False", "source formal boundary changed")
                check(Decimal(row["net_return_pct"]) == return_from_prices(row, policy), "source primary cost formula mismatch")
                selected.append(row)
    check(total == policy["source_rows"], "source row count mismatch")
    check(Counter(r["strategy"] for r in selected) == policy["strategies"], "selected strategy counts mismatch")
    check(Counter(r["strategy"] for r in selected if r["anomaly_candidate"] == "True") == policy["original_candidate_counts"], "original candidate counts mismatch")
    check(len({r["trade_id"] for r in selected}) == len(selected), "source duplicate trade_id")
    return fields, selected, total


def return_from_prices(row, policy):
    """Independent original net-PnL/entry-cash formula, including minimum fees."""
    with localcontext() as context:
        context.prec = 50
        costs = policy["costs"]
        shares, slip = Decimal(costs["shares"]), Decimal(policy["slippage_bps"]) / 10000
        entry = Decimal(row["entry_open"]) * shares * (1 + slip)
        exit_ = Decimal(row["exit_close"]) * shares * (1 - slip)
        floor, fee = Decimal(costs["minimum_fee_each_side"]), Decimal(costs["fee_each_side"])
        invested = entry + max(floor, entry * fee)
        proceeds = exit_ - max(floor, exit_ * fee) - exit_ * Decimal(costs["sell_tax"])
        return (proceeds - invested) / invested * 100


def expected_leg(policy, stock, day):
    found = sorted((event for event in policy["exceptions"] if event["stock_id"] == stock and event["start_date"] <= day and (event["end_date"] is None or day <= event["end_date"])), key=lambda e: e["event_id"])
    if not found:
        return ("assumed_regular_price_proxy", "1000", "", "bounded_normal_regime_assumption_not_verified")
    ids = ";".join(e["event_id"] for e in found)
    reasons = ";".join(sorted({e["reason"] for e in found}))
    if any(e["state"] == "evidenced_no_fill" and e.get("full_validity_covered") is True for e in found):
        return "evidenced_no_fill", "0", ids, reasons
    partials = [e for e in found if e["state"] == "partial_fill_out_of_scope"]
    if partials:
        quantities = [e.get("supported_quantity") for e in partials]
        check(all(type(q) is int and 0 < q < 1000 for q in quantities) and len(set(quantities)) == 1, "partial quantity must be one supported integer strictly between 0 and 1000")
        return "partial_fill_out_of_scope", str(quantities[0]), ids, reasons
    return "unknown", "", ids, reasons


def expected_execution(source, policy):
    """Project each stock/strategy's chronology independently of published states.

    A closed position only releases before a strictly later entry date: an entry
    on its exit day is the open, before the close. An unresolved owner has no
    release date. The fixed policy cohort is never derived from signal_date.
    """
    groups, expected = defaultdict(list), {}
    for original in source:
        groups[(policy["model_id"], original["strategy"], policy["cohort_id"], original["stock_id"])].append(original)
    for members in groups.values():
        owner, release = "", None
        for original in sorted(members, key=lambda r: (r["entry_date"], r["trade_id"])):
            row = dict.fromkeys(EXTRA, "")
            row.update(source_trade_row_sha256=digest(canonical(original)), execution_model_id=policy["model_id"], execution_cohort_id=policy["cohort_id"], original_primary_proxy_return_pct=original["net_return_pct"], execution_assumed_completed="False", actual_fill_verified="False", execution_evidence_state="unknown", exception_coverage_verified="False", execution_lock_retained="False")
            expected[original["trade_id"]] = row
            if owner and (release is None or original["entry_date"] <= release):
                row.update(execution_entry_state="blocked_existing_lock", execution_exit_state="not_evaluated_entry_unresolved", execution_position_state="lock_blocked", execution_blocking_trade_id=owner, execution_entry_reason="prior_position_lock_not_released", execution_lock_retained="True")
                continue
            owner, release = "", None
            entry_state, quantity, ids, reason = expected_leg(policy, original["stock_id"], original["entry_date"])
            row.update(execution_entry_state=entry_state, execution_entry_quantity=quantity, execution_entry_event_ids=ids, execution_entry_reason=reason)
            if entry_state == "evidenced_no_fill":
                row.update(execution_position_state="no_entry", execution_exit_state="not_applicable_no_entry")
                continue
            owner = original["trade_id"]
            row["execution_lock_retained"] = "True"
            if entry_state != "assumed_regular_price_proxy":
                row.update(execution_position_state="entry_partial" if entry_state == "partial_fill_out_of_scope" else "entry_unknown", execution_exit_state="not_evaluated_entry_unresolved")
                continue
            exit_state, quantity, ids, reason = expected_leg(policy, original["stock_id"], original["exit_date"])
            row.update(execution_exit_state=exit_state, execution_exit_quantity=quantity, execution_exit_event_ids=ids, execution_exit_reason=reason)
            if exit_state == "assumed_regular_price_proxy":
                release = original["exit_date"]
                row.update(execution_position_state="assumed_closed", execution_proxy_return_pct=str(return_from_prices(original, policy)), execution_assumed_completed="True", execution_lock_retained="False")
            else:
                row["execution_position_state"] = {"unknown": "exit_unknown", "partial_fill_out_of_scope": "exit_partial", "evidenced_no_fill": "exit_no_fill"}[exit_state]
    return expected


def audit_positions(fields, rows, source_fields, source, policy):
    check(fields == source_fields + EXTRA, "positions source/appended schema mismatch")
    actual = {r["trade_id"]: r for r in rows}
    originals = {r["trade_id"]: r for r in source}
    check(len(actual) == len(rows) == len(source) and set(actual) == set(originals), "positions must retain every original primary trade exactly once")
    expected = expected_execution(source, policy)
    for trade_id, original in originals.items():
        row = actual[trade_id]
        check(all(row[k] == original[k] for k in source_fields), f"original primary field changed: {trade_id}")
        for field, value in expected[trade_id].items():
            check(row[field] == value, f"execution field mismatch: {trade_id}: {field}")
    return expected


def summary_metrics(values):
    with localcontext() as context:
        context.prec = 50
        n, ordered = len(values), sorted(values)
        counts = {"win_count": sum(v > 0 for v in values), "neutral_count": sum(v == 0 for v in values), "failure_count": sum(v < 0 for v in values)}
        result = dict(samples=n, **counts)
        result.update({k.replace("count", "rate_pct"): Decimal(count) * 100 / n if n else "" for k, count in counts.items()})
        median = (ordered[(n - 1) // 2] + ordered[n // 2]) / 2 if n else ""
        result.update(mean_net_return_pct=sum(values) / n if n else "", median_net_return_pct=median, high_return_ge10_rate_pct=Decimal(sum(v >= 10 for v in values)) * 100 / n if n else "", loss_le_minus10_rate_pct=Decimal(sum(v <= -10 for v in values)) * 100 / n if n else "", min_net_return_pct=min(values) if n else "", max_net_return_pct=max(values) if n else "")
        return result


def audit_summary(rows, source, expected, policy):
    actual = {(r["strategy"], r["population"]): r for r in rows}
    keys = {(strategy, population) for strategy in policy["strategies"] for population in POPULATIONS}
    check(len(rows) == len(actual) and set(actual) == keys, "summary populations mismatch")
    for strategy, population in sorted(keys):
        base = [r for r in source if r["strategy"] == strategy]
        completed = [r for r in base if expected[r["trade_id"]]["execution_assumed_completed"] == "True"]
        selected = completed if population.startswith("assumed_completed") else base
        if "candidate_exclusion_sensitivity" in population:
            selected = [r for r in selected if r["anomaly_candidate"] != "True"]
        n, done = len(base), len(completed)
        with localcontext() as context:
            context.prec = 50
            wanted = dict(primary_samples=n, assumed_completed_samples=done, execution_not_computable_samples=n-done, execution_not_computable_pct=Decimal(n-done)*100/n if n else "", execution_evidence_unknown_samples=n, original_candidate_samples=sum(r["anomaly_candidate"] == "True" for r in base), population_candidate_samples=sum(r["anomaly_candidate"] == "True" for r in selected), stocks=len({r["stock_id"] for r in selected}), signal_dates=len({r["signal_date"] for r in selected}), **summary_metrics([return_from_prices(r, policy) if population.startswith("assumed_completed") else Decimal(r["net_return_pct"]) for r in selected]))
        actual_row = actual[strategy, population]
        for field, value in wanted.items():
            got = actual_row[field]
            if value == "":
                check(got == "", f"summary empty metric mismatch: {strategy}/{population}/{field}")
            else:
                # Producers serialize the ratio outside a local precision-50 context.
                check(got != "" and Decimal(got).is_finite() and abs(Decimal(got) - Decimal(value)) <= Decimal("1e-24"), f"summary arithmetic/denominator mismatch: {strategy}/{population}/{field}")
        check(all(actual_row[k] == "False" for k in ("actual_fill_verified", "formal_use", "promotion_evidence_allowed")) and actual_row["execution_evidence_state"] == "unknown", "summary research boundary mismatch")


def audit_manifest(manifest, payloads, policy, source_fields, source, expected):
    values = dict(artifact_version=policy["artifact_version"], owner_id=OWNER, model_id=policy["model_id"], replay_kind="frozen-ledger replay", policy_fixed_at=policy["policy_fixed_at"], policy_canonical_sha256=CONTRACT_SHA256, source_ref=policy["source_ref"], source_ledger=policy["source_ledger"], source_ledger_sha256=policy["source_ledger_sha256"], source_rows=policy["source_rows"], selected_rows=len(source), source_fields=source_fields, appended_fields=EXTRA, cohort_id=policy["cohort_id"], source_row_preservation="all original fields unchanged", state_counts=dict(Counter(r["execution_position_state"] for r in expected.values())), actual_fill_verified=False, execution_evidence_state="unknown", exception_coverage_verified=False, formal_use=False, promotion_evidence_allowed=False)
    for field, value in values.items():
        check(manifest.get(field) == value, f"manifest contract mismatch: {field}")
    fixed, started = (datetime.fromisoformat(manifest[k]) for k in ("policy_fixed_at", "replay_started_at"))
    check(fixed.tzinfo is not None and started.tzinfo is not None and fixed < started, "policy must be fixed before replay")
    wanted = {name(kind): {"sha256": digest(payloads[kind]), "bytes": len(payloads[kind])} for kind in KINDS[:-1]}
    check(manifest.get("artifacts") == wanted, "manifest content artifact hash/byte mismatch")


def validate(root=ROOT, source_ledger=None) -> list[str]:
    root = Path(root)
    try:
        policy = json.loads((root / CONTRACT).read_bytes())
        audit_policy(policy)
        payloads = {kind: (root / DIRECTORY / name(kind)).read_bytes() for kind in KINDS}
        source_fields, source, _ = read_source(root, policy, source_ledger)
        fields, positions = records(payloads["positions_v1.csv.gz"], compressed=True)
        expected = audit_positions(fields, positions, source_fields, source, policy)
        _, summaries = records(payloads["summary_v1.csv"])
        audit_summary(summaries, source, expected, policy)
        manifest = json.loads(payloads["source_manifest_v1.json"])
        audit_manifest(manifest, payloads, policy, source_fields, source, expected)
        report = payloads["report_v1.md"].decode("utf-8")
        for text in ("frozen-ledger replay", "原 primary 全保留", "全市場例外清單未核實", "假設完成子集", "formal_use=False", "promotion_evidence_allowed=False", manifest["replay_started_at"]):
            check(text in report, "report missing research limitation: " + text)
        if source_ledger is not None:
            check(digest(Path(source_ledger).read_bytes()) == policy["source_ledger_sha256"], "source ledger bytes changed during validation")
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        return [str(exc)]
    return []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ledger", type=Path)
    args = parser.parse_args(argv)
    errors = validate(args.repository_root.resolve(), args.source_ledger)
    print(json.dumps({"validator": OWNER, "status": "fail" if errors else "pass", "errors": errors}, ensure_ascii=False))
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
