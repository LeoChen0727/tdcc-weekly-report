"""Model-owned Scheme A replay. Historical evidence gaps are not executable trades."""
from __future__ import annotations

import argparse
import bisect
import csv
import fnmatch
import hashlib
import io
import json
import re
import subprocess
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

from model_research_artifact_guard import (
    load_ownership_rules, load_protected_sentinels, model_owned_artifact_guard, validate_changed_paths,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_REF = "7ef37a966280201a5ee236856306fdb513de7092"
ARTIFACT_SOURCE_REF = "2244a0a36c4542cd62948b50f12ef98ade50e1df"
OWNER_ID = "tdcc_stealth_accumulation_operation_replay"
MODEL_ID = "tdcc_stealth_accumulation"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_operation_replay.py"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_operation_replay_v3"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
PREFIX = "tdcc_stealth_accumulation_operation_replay_"
V2_DETAIL = f"{DIRECTORY}/tdcc_stealth_accumulation_historical_selector_field_contract_replay_detail_v2.csv"
V2_SUMMARY = f"{DIRECTORY}/tdcc_stealth_accumulation_historical_selector_field_contract_replay_summary_v2.csv"
AUDIT = f"{DIRECTORY}/tdcc_stealth_accumulation_price_pit_audit_v1.csv"
V2_SHA256 = "4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3"
AUDIT_SHA256 = "fc3fe80afcca8018aaa1af08181eb9170a2b9cf56baaec02386cb9316a6bc32e"
HORIZONS = (5, 10, 20)
SLIPPAGES = ("0", "0.001", "0.002")
FLAGS = {"formal_use": "False", "trade_eligible": "False", "promotion_evidence_allowed": "False"}
TAIPEI = timezone(timedelta(hours=8))


def canonical(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def text(value) -> str:
    value = ("" if value is None else str(value)).replace("\ufeff", "").strip()
    return "" if value.lower() in {"nan", "none", "nat", "<na>"} else value


def number(value) -> Decimal | None:
    value = text(value).replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    try:
        result = Decimal(value)
        return result if result.is_finite() else None
    except InvalidOperation:
        return None


def decimal_text(value) -> str:
    if value is None:
        return ""
    value = Decimal(value)
    rendered = format(value, "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def signal_signature(row: dict) -> dict:
    """Compare resolved business values, separately retain alias/path provenance.

    This does not select stocks: membership is the immutable accepted v2 detail.
    All attack-helper resolved inputs are retained, not merely selected=True.
    """
    values, sources = {}, {}

    def take(key, *names, numeric=False):
        for name in names:
            for candidate in (name, name + "_x", name + "_y"):
                value = number(row.get(candidate)) if numeric else text(row.get(candidate))
                if value is not None and (numeric or value):
                    values[key] = decimal_text(value) if numeric else value.lower()
                    sources[key] = candidate
                    return value
        values[key], sources[key] = "", ""
        return None if numeric else ""

    phase = take("tdcc_price_phase", "tdcc_price_phase")
    phase = str(phase).lower()
    if phase:
        values["tdcc_positive_branch"] = "explicit_phase"
    else:
        status = take("tdcc_status", "tdcc_status", "tdcc_judgement", "tdcc_judge")
        boolean = text(row.get("tdcc_accumulation_signal")).lower() in {"true", "1", "yes", "y", "t"}
        if status:
            values["tdcc_positive_branch"] = "status_alias"
            if str(status).lower() not in {"mild_accumulation", "strong_accumulation"}:
                values["tdcc_accumulation_boolean"] = str(boolean)
                sources["tdcc_accumulation_boolean"] = "tdcc_accumulation_signal"
        elif boolean:
            values["tdcc_positive_branch"] = "original_boolean"
            values["tdcc_accumulation_boolean"] = "True"
            sources["tdcc_accumulation_boolean"] = "tdcc_accumulation_signal"
        else:
            values["tdcc_positive_branch"] = "enum_fallback"
            take("tdcc_accumulation_enum", "tdcc_accumulation_signal")
    for key, names in (
        ("volume_ratio", ("volume_ratio",)),
        ("return_5d_pct", ("return_5d", "return_5d_pct")),
        ("return_20d_pct", ("return_20d", "return_20d_pct")),
        ("recent_range_high", ("high_20", "previous_20d_high", "platform_high")),
        ("recent_range_low", ("low_20", "previous_20d_low", "platform_low")),
        ("open", ("open",)), ("high", ("high",)), ("low", ("low",)), ("close", ("close",)),
        ("previous_close", ("previous_close", "prev_close", "close_prev", "close_1d_ago")),
    ):
        take(key, *names, numeric=True)
    ma20 = take("volume_ma20_lots", "volume_ma20_lots", "avg_volume_20d_lots", numeric=True)
    if ma20 is None:
        ma20 = take("volume_ma20_lots", "volume_ma20", "avg_volume_20d", numeric=True)
        if ma20 is not None and ma20 >= 100000:
            values["volume_ma20_lots"] = decimal_text(ma20 / 1000)
    level = take("breakout_level", "previous_20d_high_ex_today", "prior_20d_high", "previous_20d_high", "high_20_ex_today", numeric=True)
    high, close = number(values["high"]), number(values["close"])
    if level is not None and high is not None and close is not None and level >= high * Decimal("0.999"):
        platform = take("_platform", "platform_high", "short_platform_high", "range_high", numeric=True)
        if platform is not None and platform < level:
            values["breakout_level"], sources["breakout_level"] = values["_platform"], sources["_platform"]
        values.pop("_platform")
        sources.pop("_platform")
    daily_return = take("daily_return_pct", "daily_return_calc", "return_1d", "return_1d_pct", numeric=True)
    previous = number(values["previous_close"])
    if daily_return is None and close is not None and previous is not None and previous > 0:
        with localcontext() as ctx:
            ctx.prec = 50
            values["daily_return_pct"] = decimal_text((close / previous - 1) * 100)
        sources["daily_return_pct"] = "derived_close_previous_close"
    values["volume_confirmed_breakout"] = str(text(row.get("volume_confirmed_breakout")).lower() in {"true", "1", "yes", "y", "t"})
    sources["volume_confirmed_breakout"] = "volume_confirmed_breakout"
    return {"values": values, "sources": sources}


def merge_signals(signals: list[dict]) -> list[dict]:
    grouped = defaultdict(list)
    for row in signals:
        grouped[(row["stock_id"], row["signal_date"])].append(row)
    events = []
    for (stock, date), rows in sorted(grouped.items(), key=lambda pair: (pair[0][1], pair[0][0])):
        signatures = {canonical(row["signature"]) for row in rows}
        features = [feature for row in rows for feature in row.get("feature_evidence", [])]
        events.append({
            "event_id": f"{stock}:{date}", "stock_id": stock, "signal_date": date,
            "source_ids": [row["signal_id"] for row in rows],
            "signature_conflict": len(signatures) != 1,
            "signature": rows[0]["signature"] if len(signatures) == 1 else {},
            "signature_count": len(signatures), "feature_evidence": features,
            "calendar_verified": all(row.get("calendar_verified") is True for row in rows),
            "corporate_actions_verified": all(row.get("corporate_actions_verified") is True for row in rows) and len({canonical(row.get("actions", [])) for row in rows}) == 1,
            "actions": rows[0].get("actions", []),
            "anomaly_candidate": any(row.get("anomaly_candidate") in (True, "True") for row in rows),
            "observation_ids": sorted({code for row in rows for code in row.get("observation_ids", [])}),
        })
    return events


def plan_dates(signal_date: str, calendar: list[str], horizon: int) -> tuple[str, str]:
    if calendar != sorted(set(calendar)):
        raise ValueError("calendar must contain unique ascending exchange trading dates")
    if horizon not in HORIZONS:
        raise ValueError("only preregistered D5/D10/D20 horizons are allowed")
    index = bisect.bisect_right(calendar, signal_date)
    entry = calendar[index] if index < len(calendar) else ""
    exit_date = calendar[index + horizon] if index + horizon < len(calendar) else ""
    return entry, exit_date


def feature_evidence_status(event: dict, entry: str) -> list[str]:
    if not entry:
        return ["decision_cutoff_unavailable"]
    cutoff = datetime.strptime(entry, "%Y%m%d").replace(hour=8, minute=30, tzinfo=TAIPEI)
    features = event.get("feature_evidence", [])
    errors = []
    if not features:
        return ["feature_evidence_missing"]
    expected = set(event.get("signature", {}))
    if expected and not expected.issubset({f.get("name") for f in features}):
        errors.append("feature_evidence_incomplete")
    for feature in features:
        if feature.get("verified") is not True or not feature.get("evidence_ref"):
            errors.append("historical_availability_unproven")
        effective = str(feature.get("effective_date", ""))
        try:
            if not re.fullmatch(r"\d{8}", effective):
                raise ValueError("effective date format")
            datetime.strptime(effective, "%Y%m%d")
            if effective > event["signal_date"]:
                errors.append("feature_effective_after_signal")
        except ValueError:
            errors.append("feature_effective_date_unproven")
        try:
            available = datetime.fromisoformat(str(feature.get("available_at", "")).replace("Z", "+00:00"))
            if available.tzinfo is None or available >= cutoff:
                errors.append("feature_not_strictly_before_cutoff")
        except (ValueError, TypeError):
            errors.append("historical_availability_unproven")
    return sorted(set(errors))


def calculate_costs(open_price, close_price, slippage="0.001", quantity=1000, actions=None) -> dict:
    with localcontext() as ctx:
        ctx.prec = 50
        opening, closing, slip, shares = map(lambda item: Decimal(str(item)), (open_price, close_price, slippage, quantity))
        if not all(value.is_finite() for value in (opening, closing, slip, shares)) or min(opening, closing, shares) <= 0 or slip < 0 or slip >= 1:
            raise ValueError("invalid execution price, quantity, or slippage")
        original_shares, cash = shares, Decimal(0)
        action_fingerprints = [canonical(action) for action in actions or []]
        if len(action_fingerprints) != len(set(action_fingerprints)):
            raise ValueError("duplicate corporate action would double-count shares or cash flow")
        grouped_actions = defaultdict(list)
        for action in actions or []:
            date = str(action.get("event_date", ""))
            if not re.fullmatch(r"\d{8}", date):
                raise ValueError("corporate action effective date is invalid")
            datetime.strptime(date, "%Y%m%d")
            grouped_actions[date].append(action)
        ordered = []
        for date, same_day in sorted(grouped_actions.items()):
            if {action.get("kind") for action in same_day} >= {"cash", "share_factor"}:
                sequences = [action.get("sequence") for action in same_day]
                if not all(type(sequence) is int for sequence in sequences) or len(set(sequences)) != len(same_day) or not all(action.get("sequence_evidence_ref") for action in same_day):
                    raise ValueError("same-day cash/share changes require verified event ordering")
                same_day = sorted(same_day, key=lambda action: action["sequence"])
            ordered.extend(same_day)
        for action in ordered:
            if action.get("evidence_verified") is not True or not action.get("evidence_ref"):
                raise ValueError("corporate action requires verified shares/cash-flow evidence")
            if action["kind"] == "share_factor":
                factor = Decimal(str(action["share_factor"]))
                if not factor.is_finite() or factor <= 0:
                    raise ValueError("invalid share factor")
                shares *= factor
            elif action["kind"] == "cash":
                cash_per_share = Decimal(str(action["cash_per_share"]))
                if not cash_per_share.is_finite():
                    raise ValueError("invalid verified cash flow")
                cash += shares * cash_per_share
            else:
                raise ValueError("unsupported corporate action")
        buy, sell = original_shares * opening * (1 + slip), shares * closing * (1 - slip)
        buy_fee, sell_fee, tax = max(Decimal(20), buy * Decimal("0.001425")), max(Decimal(20), sell * Decimal("0.001425")), sell * Decimal("0.003")
        entry_cash, net_exit = buy + buy_fee, sell - sell_fee - tax + cash
        return {
            "buy_amount": buy, "sell_amount": sell, "buy_fee": buy_fee, "sell_fee": sell_fee,
            "sell_tax": tax, "entry_cash": entry_cash, "net_exit_cash": net_exit,
            "net_pnl": net_exit - entry_cash, "gross_pnl": shares * closing + cash - original_shares * opening,
            "gross_return_pct": (shares * closing + cash - original_shares * opening) / (original_shares * opening) * 100,
            "net_return_pct": (net_exit - entry_cash) / entry_cash * 100,
            "final_shares": shares, "cash_flows": cash,
        }


def replay_events(events, calendar, prices, as_of, horizons=HORIZONS):
    evaluations, positions = [], []
    for horizon in horizons:
        held = {}
        for event in sorted(events, key=lambda row: (row["signal_date"], row["stock_id"], row["event_id"])):
            stock, signal_date = event["stock_id"], event["signal_date"]
            entry, exit_date = plan_dates(signal_date, calendar, horizon)
            entry_price, exit_price = prices.get((stock, entry), {}), prices.get((stock, exit_date), {})
            opening, closing = number(entry_price.get("open")), number(exit_price.get("close"))
            missing = feature_evidence_status(event, entry)
            if event.get("calendar_verified") is not True:
                missing.append("official_calendar_evidence_unproven")
            if event.get("corporate_actions_verified") is not True:
                missing.append("corporate_action_coverage_unproven")
            if entry_price.get("open_verified") is not True or entry_price.get("executable") is not True:
                missing.append("entry_execution_unproven")
            if exit_price.get("close_verified") is not True or exit_price.get("executable") is not True:
                missing.append("exit_execution_unproven")
            row = {
                "event_id": event["event_id"], "stock_id": stock, "signal_date": signal_date,
                "horizon": horizon, "entry_date": entry, "exit_date": exit_date,
                "decision_cutoff": f"{entry}T08:30:00+08:00" if entry else "",
                "source_ids": canonical(event.get("source_ids", [])),
                "source_row_count": len(event.get("source_ids", [])),
                "signature_conflict": str(event.get("signature_conflict") is True),
                "signature_count": event.get("signature_count", 1),
                "entry_open": decimal_text(opening), "exit_close": decimal_text(closing),
                "entry_price_status": "missing" if opening is None or opening <= 0 else "observed_raw_unverified" if entry_price.get("open_verified") is not True else "verified",
                "exit_price_status": "missing" if closing is None or closing <= 0 else "observed_raw_unverified" if exit_price.get("close_verified") is not True else "verified",
                "window_status": "calendar_date_unavailable" if not exit_date else "immature" if exit_date > as_of else "mature_calendar_window",
                "evidence_missing": ";".join(sorted(set(missing))),
                "feature_evidence": canonical(event.get("feature_evidence", [])),
                "calendar_verified": str(event.get("calendar_verified") is True),
                "corporate_actions_verified": str(event.get("corporate_actions_verified") is True),
                "entry_source_path": entry_price.get("source_path", ""), "entry_source_sha256": entry_price.get("source_sha256", ""),
                "entry_row_sha256": entry_price.get("row_sha256", ""),
                "exit_source_path": exit_price.get("source_path", ""), "exit_source_sha256": exit_price.get("source_sha256", ""),
                "exit_row_sha256": exit_price.get("row_sha256", ""),
                "anomaly_candidate": str(event.get("anomaly_candidate") is True),
                "observation_ids": canonical(event.get("observation_ids", [])),
                "retained_in_primary": "True", **FLAGS,
            }
            prior = held.get(stock)
            status = ""
            if prior and prior["status"] == "realized" and signal_date > prior["exit_date"]:
                del held[stock]
                prior = None
            if prior:
                status = "blocked_exit_day" if prior["status"] == "realized" and signal_date == prior["exit_date"] else "blocked_active_position"
            elif event.get("signature_conflict") is True:
                status = "signature_conflict"
            elif signal_date not in calendar:
                status = "signal_not_exchange_day"
            elif not entry:
                status = "entry_date_unavailable"
            elif entry > as_of:
                status = "entry_after_as_of"
            elif opening is None or opening <= 0:
                status = "entry_price_missing"
            elif feature_evidence_status(event, entry):
                status = "feature_evidence_missing"
            elif event.get("calendar_verified") is not True:
                status = "calendar_evidence_missing"
            elif entry_price.get("open_verified") is not True or entry_price.get("executable") is not True:
                status = "entry_execution_unverified"
            if status:
                row["status"] = status
                evaluations.append(row)
                continue
            row["status"] = "position_opened"
            evaluations.append(row)
            position_status = "open_immature" if not exit_date or exit_date > as_of else "realized"
            actions, valid_actions = [], True
            for action in event.get("actions", []):
                action_date = str(action.get("event_date", ""))
                try:
                    if not re.fullmatch(r"\d{8}", action_date):
                        raise ValueError("invalid action date")
                    datetime.strptime(action_date, "%Y%m%d")
                except ValueError:
                    valid_actions = False
                    continue
                # Each horizon has its own holding interval. Future actions do not
                # contaminate an earlier exit, and are not assumed paid early.
                if entry <= action_date <= exit_date:
                    actions.append(action)
                    valid_actions = valid_actions and action.get("evidence_verified") is True and bool(action.get("evidence_ref"))
            if position_status == "realized" and (closing is None or closing <= 0 or exit_price.get("close_verified") is not True or exit_price.get("executable") is not True or event.get("corporate_actions_verified") is not True or not valid_actions):
                position_status = "open_unresolved_exit"
            if position_status == "realized":
                try:
                    calculate_costs(opening, closing, "0", actions=actions)
                except (ValueError, KeyError, InvalidOperation):
                    position_status = "open_unresolved_exit"
            held[stock] = {"exit_date": exit_date, "status": position_status}
            for slip in SLIPPAGES:
                position = {**row, "position_id": f"{event['event_id']}:D{horizon}", "slippage": slip, "quantity": 1000, "status": position_status, "actions": canonical(actions), "outcome": "", "high_return_hit": "", "major_loss": ""}
                if position_status == "realized":
                    costs = calculate_costs(opening, closing, slip, actions=actions)
                    position.update({key: decimal_text(value) for key, value in costs.items()})
                    position["outcome"] = "win" if costs["net_pnl"] > 0 else "loss" if costs["net_pnl"] < 0 else "neutral"
                    position["high_return_hit"] = str(costs["net_return_pct"] >= 10)
                    position["major_loss"] = str(costs["net_return_pct"] <= -10)
                positions.append(position)
    return evaluations, positions


def summarize(evaluations, positions, signal_count: int):
    summaries = []
    for horizon in HORIZONS:
        evaluated = [row for row in evaluations if int(row["horizon"]) == horizon]
        for slip in SLIPPAGES:
            for population in ("primary", "excluding_anomaly_candidates_sensitivity"):
                rows = [row for row in positions if int(row["horizon"]) == horizon and str(row["slippage"]) == slip and (population == "primary" or row["anomaly_candidate"] not in (True, "True"))]
                realized = [row for row in rows if row["status"] == "realized"]
                returns = sorted(Decimal(row["net_return_pct"]) for row in realized)
                n = len(returns)
                counts = Counter(row["outcome"] for row in realized)
                high, major = sum(value >= 10 for value in returns), sum(value <= -10 for value in returns)
                with localcontext() as ctx:
                    ctx.prec = 50
                    rate = lambda count: decimal_text(Decimal(count) / n * 100) if n else ""
                    mean = decimal_text(sum(returns) / n) if n else ""
                    median = decimal_text(returns[n // 2] if n % 2 else (returns[n // 2 - 1] + returns[n // 2]) / 2) if n else ""
                    summaries.append({
                        "artifact_version": ARTIFACT_VERSION, "horizon": horizon, "slippage": slip,
                        "analysis_population": population, "signal_count": signal_count, "event_count": len(evaluated),
                        "stock_count": len({row["stock_id"] for row in evaluated}),
                        "position_count": len(rows), "realized_count": n,
                        "immature_count": sum(row["status"] == "open_immature" for row in rows),
                        "unresolved_count": sum(row["status"] == "open_unresolved_exit" for row in rows),
                        "immature_event_count": sum(row["window_status"] == "immature" for row in evaluated),
                        "evidence_missing_event_count": sum(bool(row["evidence_missing"]) for row in evaluated),
                        "conflict_event_count": sum(row["signature_conflict"] == "True" for row in evaluated),
                        "win_count": counts["win"], "neutral_count": counts["neutral"], "loss_count": counts["loss"],
                        "win_rate_pct": rate(counts["win"]), "neutral_rate_pct": rate(counts["neutral"]), "loss_rate_pct": rate(counts["loss"]),
                        "average_net_return_pct": mean, "median_net_return_pct": median,
                        "tail_loss_pct": decimal_text(min(returns)) if n else "",
                        "high_return_hit_count": high, "high_return_hit_rate_pct": rate(high),
                        "major_loss_count": major, "major_loss_rate_pct": rate(major),
                        "denominator": "all_realized_positions_in_this_horizon_slippage_population",
                        "performance_status": "research_only_verified_position_sample" if n else "unavailable_no_realized_verified_positions",
                        "status_counts": canonical(dict(sorted(Counter(row["status"] for row in evaluated).items()))),
                        **FLAGS,
                    })
    return summaries


class GitSource:
    def __init__(self, root: Path, source_ref: str, expected: str):
        self.root = root
        self.commit = subprocess.check_output(["git", "--no-replace-objects", "rev-parse", source_ref + "^{commit}"], cwd=root, text=True).strip()
        if self.commit != expected:
            raise ValueError(f"immutable source role mismatch: expected={expected}; observed={self.commit}")
        self.sources = {}

    def read(self, path: str) -> bytes:
        payload = subprocess.check_output(["git", "--no-replace-objects", "show", f"{self.commit}:{path}"], cwd=self.root)
        self.sources[path] = {"source_commit_sha": self.commit, "path": path, "sha256": sha(payload), "size_bytes": len(payload)}
        return payload

    def rows(self, path: str):
        payload = self.read(path)
        return list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline="")))


def load_inputs(root: Path, source_ref=SOURCE_REF, artifact_source_ref=ARTIFACT_SOURCE_REF):
    raw, accepted = GitSource(root, source_ref, SOURCE_REF), GitSource(root, artifact_source_ref, ARTIFACT_SOURCE_REF)
    detail_bytes, audit_bytes = accepted.read(V2_DETAIL), accepted.read(AUDIT)
    if sha(detail_bytes) != V2_SHA256 or sha(audit_bytes) != AUDIT_SHA256:
        raise ValueError("accepted v2 detail or anomaly audit byte digest mismatch")
    detail = list(csv.DictReader(io.StringIO(detail_bytes.decode("utf-8-sig"))))
    audit = list(csv.DictReader(io.StringIO(audit_bytes.decode("utf-8-sig"))))
    baseline = accepted.rows(V2_SUMMARY)
    manifest_rows = raw.rows("output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv")
    if not manifest_rows:
        raise ValueError("candidate snapshot manifest missing")
    snapshots = {path: raw.rows(path) for path in sorted({row["snapshot_path"] for row in detail})}
    # Validate each immutable snapshot once, never run a git process per signal row.
    for path in snapshots:
        expected_hashes = {row["snapshot_sha256"] for row in detail if row["snapshot_path"] == path}
        payload = subprocess.check_output(["git", "--no-replace-objects", "show", f"{SOURCE_REF}:{path}"], cwd=root)
        accepted_hashes = {sha(payload), sha(payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n"))}
        if len(expected_hashes) != 1 or not expected_hashes.issubset(accepted_hashes):
            raise ValueError("candidate snapshot digest mismatch")
    if len(detail) != 6821 or len(snapshots) != 36 or sum(map(len, snapshots.values())) != 19361:
        raise ValueError("frozen candidate/detail population drift")
    signals, signal_records = [], []
    observations = defaultdict(list)
    for row in audit:
        observations[(row["stock_id"], row.get("signal_date", row.get("candidate_signal_date", "")))].append(row["observation_id"])
    for index, row in enumerate(detail, 2):
        candidate = snapshots[row["snapshot_path"]][int(row["snapshot_row_number"]) - 2]
        canonical_row = {str(key): text(value) for key, value in candidate.items()}
        if sha(canonical(canonical_row).encode("utf-8")) != row["snapshot_row_sha256"] or text(candidate.get("stock_id")) != row["stock_id"]:
            raise ValueError("immutable candidate row identity/hash mismatch")
        signature = signal_signature(candidate)
        signal_id = f"v2:{index}"
        codes = observations[(row["stock_id"], row["candidate_signal_date"])]
        features = [{"name": name, "effective_date": "", "available_at": "", "verified": False, "evidence_ref": ""} for name in signature["values"]]
        visible_dates = {name: text(value) for name, value in candidate.items() if name in {"date", "signal_date", "main_price_date", "source_date", "raw_source_date", "tdcc_date"} and text(value)}
        source_lineage = {key: row[key] for key in ("snapshot_path", "snapshot_sha256", "snapshot_row_number", "snapshot_row_sha256", "snapshot_generated_at", "snapshot_pipeline_commit_sha")}
        signal = {"signal_id": signal_id, "stock_id": row["stock_id"], "signal_date": row["candidate_signal_date"], "signature": signature["values"], "source_lineage": source_lineage, "feature_evidence": features, "calendar_verified": False, "corporate_actions_verified": False, "actions": [], "anomaly_candidate": bool(codes) or row["anomaly_candidate"] == "True", "observation_ids": codes}
        signals.append(signal)
        signal_records.append({
            "signal_id": signal_id, "event_id": f"{row['stock_id']}:{row['candidate_signal_date']}",
            "stock_id": row["stock_id"], "stock_name": row["stock_name"], "signal_date": row["candidate_signal_date"],
            "v2_detail_row_number": index, "v2_detail_sha256": V2_SHA256,
            "source_commit_sha": SOURCE_REF, "artifact_source_commit_sha": ARTIFACT_SOURCE_REF,
            **source_lineage, "signature": canonical(signature["values"]), "signature_sources": canonical(signature["sources"]),
            "signature_sha256": sha(canonical(signature["values"]).encode("utf-8")),
            "feature_evidence": canonical(features), "visible_source_dates": canonical(visible_dates),
            "pit_status": "not_complete_event_time_PIT_proof", "calendar_verified": "False", "corporate_actions_verified": "False",
            "anomaly_candidate": str(signal["anomaly_candidate"]), "anomaly_disposition": "unresolved_anomaly_candidate" if signal["anomaly_candidate"] else "not_triggered",
            "observation_ids": canonical(codes), "retained_in_primary": "True", **FLAGS,
        })
    events = merge_signals(signals)
    if len(events) != 5108 or len({row["stock_id"] for row in signals}) != 520:
        raise ValueError("frozen event/stock population drift")
    holidays = raw.rows("config/twse_non_trading_days.csv")
    exceptional = raw.rows("data/market_calendar/exceptional_non_trading_days.csv")
    company_events = raw.rows("data/company_calendar/company_event_calendar.csv")
    closed = {re.sub(r"[^0-9]", "", row["date"]) for row in holidays}
    for row in exceptional:
        date = row.get("date") or row.get("market_date") or row.get("session_date")
        if not date:
            raise ValueError("exceptional calendar requires explicit date")
        closed.add(re.sub(r"[^0-9]", "", date))
    start, as_of = min(row["signal_date"] for row in signals), "20260907"
    cursor = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(as_of, "%Y%m%d") + timedelta(days=70)
    calendar = []
    while cursor <= end:
        date = cursor.strftime("%Y%m%d")
        if cursor.weekday() < 5 and date not in closed:
            calendar.append(date)
        cursor += timedelta(days=1)
    paths = subprocess.check_output(["git", "--no-replace-objects", "ls-tree", "-r", "--name-only", SOURCE_REF, "data/daily_price"], cwd=root, text=True).splitlines()
    prices = {}
    stocks = {row["stock_id"] for row in signals}
    for path in paths:
        match = re.fullmatch(r"data/daily_price/(\d{8})\.csv", path)
        if not match or not start <= match[1] <= as_of:
            continue
        for price in raw.rows(path):
            stock, date = text(price.get("stock_id")), re.sub(r"[^0-9]", "", text(price.get("date")))
            if stock not in stocks:
                continue
            key = stock, date
            if key in prices:
                raise ValueError("duplicate canonical stock/date price")
            prices[key] = {"open": price["open"], "close": price["close"], "open_verified": False, "close_verified": False, "executable": False, "source_path": path, "source_sha256": raw.sources[path]["sha256"], "row_sha256": sha(canonical({str(k): text(v) for k, v in price.items()}).encode("utf-8"))}
    evidence = []
    for item in audit:
        signal_date = item.get("signal_date", item.get("candidate_signal_date", ""))
        matched = [row for row in signals if row["stock_id"] == item["stock_id"] and row["signal_date"] == signal_date]
        if not matched:
            raise ValueError("anomaly observation lost from primary population")
        evidence.append({"observation_id": item["observation_id"], "stock_id": item["stock_id"], "signal_date": signal_date, "event_id": f"{item['stock_id']}:{signal_date}", "source_signal_ids": canonical([row["signal_id"] for row in matched]), "audit_source_path": AUDIT, "audit_source_sha256": AUDIT_SHA256, "audit_row": canonical(item), "anomaly_disposition": "unresolved_anomaly_candidate", "retained_in_primary": "True", "historical_availability_status": "unproven", "corporate_action_coverage_status": "unproven", "execution_status": "unproven", **FLAGS})
    if len(evidence) != 6 or len({row["observation_id"] for row in evidence}) != 6:
        raise ValueError("all six immutable anomaly observations must be retained")
    return {"signals": signal_records, "events": events, "prices": prices, "calendar": calendar, "as_of": as_of, "evidence": evidence, "baseline": baseline, "sources": sorted(list(raw.sources.values()) + list(accepted.sources.values()), key=lambda row: (row["source_commit_sha"], row["path"])), "company_event_rows": len(company_events)}


POSITION_EXTRA = ["position_id", "slippage", "quantity", "actions", "outcome", "high_return_hit", "major_loss", "buy_amount", "sell_amount", "buy_fee", "sell_fee", "sell_tax", "entry_cash", "net_exit_cash", "net_pnl", "gross_pnl", "gross_return_pct", "net_return_pct", "final_shares", "cash_flows"]


def csv_bytes(rows, fields=None):
    fields = fields or list(rows[0])
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def build(root: Path, source_ref=SOURCE_REF, artifact_source_ref=ARTIFACT_SOURCE_REF):
    inputs = load_inputs(root, source_ref, artifact_source_ref)
    events, positions = replay_events(inputs["events"], inputs["calendar"], inputs["prices"], inputs["as_of"])
    summary = summarize(events, positions, len(inputs["signals"]))
    payloads = {
        "signals_v3.csv": csv_bytes(inputs["signals"]), "events_v3.csv": csv_bytes(events),
        "positions_v3.csv": csv_bytes(positions, list(events[0]) + POSITION_EXTRA),
        "summary_v3.csv": csv_bytes(summary), "evidence_v3.csv": csv_bytes(inputs["evidence"]),
    }
    primary = [row for row in summary if row["analysis_population"] == "primary" and row["slippage"] == "0.001"]
    lines = ["# TDCC 潛伏吸籌：方案 A 操作回放 v3", "", "本版已逐事件執行研究規則；歷史資訊、官方日曆、成交與公司行動證據不足，未建立可證明的實現持倉。這不是零報酬結論，也不是正式可交易回測。", "", f"- 原始來源：`{SOURCE_REF}`；accepted v2：`{ARTIFACT_SOURCE_REF}`。", f"- 固定 v2：6,821 訊號列、520 股、5,108 個股票＋訊號日；本版 {len(events):,} 個事件／horizon 評估。", "- entry=D0，D+5/D+10/D+20 以交易所日曆預定，不跳到下一筆有效價格；三個帳本獨立。", "- repo 日曆可重現預定日，但未升格為完整官方事件核驗。缺證逐列列於 events.evidence_missing。", "- 基準各邊滑價0.1%；0與0.2%僅敏感度；Decimal成本無中間四捨五入。", "- 月營收只保留既有lineage；不加入EPS、毛利率、營益率、營業利益、業外損益、淨利與季度／年度財報。", "", "| 帳本 | 事件 | 欄位衝突 | 未成熟事件 | 缺證事件 | 持倉 | 已實現 | 淨勝率／平均／中位 |", "|---|---:|---:|---:|---:|---:|---:|---|" ]
    for row in primary:
        lines.append(f"| D+{row['horizon']} | {row['event_count']} | {row['conflict_event_count']} | {row['immature_event_count']} | {row['evidence_missing_event_count']} | {row['position_count']} | {row['realized_count']} | 不可評估（非0） |")
    missing_entries = sorted({(row["stock_id"], row["signal_date"], row["entry_date"]) for row in events if row["status"] == "entry_price_missing"})
    lines.extend(["", "## 缺預定入場價格：保留身分，不挪動日期", ""])
    for stock, signal_date, entry_date in missing_entries:
        lines.append(f"- `{stock}`：訊號日 `{signal_date}`，預定入場 `{entry_date}`；固定來源缺該股票開盤價格，不改用後一筆價格。")
    lines.extend(["", "## 既有訊號列基準：保持原樣，不與新持倉績效混稱", "", "以下是 accepted v2 summary 的原始欄位快照，未重算或覆寫；它是訊號列加權、原價格序列口徑的歷史觀察，不是方案 A 可交易持倉績效。", "", "```json", json.dumps(inputs["baseline"], ensure_ascii=False, indent=2), "```", "", "## 六筆異常候選全部保留", "", "六筆仍為 unresolved_anomaly_candidate；未刪除原主結果。排除候選的 summary 列只屬 sensitivity，不是修正／清理績效。數值大小不自行判定資料錯誤或非可比。", ""])
    for row in inputs["evidence"]:
        lines.append(f"- {row['stock_id']}／{row['signal_date']}／{row['observation_id']}：保留；歷史可用、成交及公司行動證據仍缺。")
    lines.extend(["", "## 使用界線", "", "獨立 validator 與合成測試驗證規則實作；它們不能補造缺失的歷史證據。後續高低報酬特徵比較須同買點、出場窗、持倉及異常口徑，不能用本版缺證樣本新增條件或升級模型。", "", "`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。無正式推薦、PDF、operation adapter 或 production 修改。", ""])
    payloads["report_v3.md"] = "\n".join(lines).encode("utf-8")
    manifest = {
        "artifact_version": ARTIFACT_VERSION, "owner_id": OWNER_ID, "model_id": MODEL_ID,
        "source_commit_sha": SOURCE_REF, "artifact_source_commit_sha": ARTIFACT_SOURCE_REF,
        "accepted_v2_detail_sha256": V2_SHA256, "as_of": inputs["as_of"],
        "hash_basis": "actual_serialized_utf8_bytes_no_bom_lf", "decimal_precision": 50,
        "source_artifacts": inputs["sources"], "exchange_calendar": inputs["calendar"],
        "calendar_evidence_status": "repo_version_reproducible_official_event_payload_not_fully_verified",
        "corporate_action_evidence_status": "company_calendar_is_advisory_not_complete_cash_flow_ledger",
        "artifacts": {PREFIX + name: {"sha256": sha(payload), "size_bytes": len(payload)} for name, payload in payloads.items()},
        "signal_rows": len(inputs["signals"]), "unique_events": len(inputs["events"]),
        "event_horizon_rows": len(events), "position_sensitivity_rows": len(positions),
        "anomaly_observations": len(inputs["evidence"]), **FLAGS,
    }
    payloads["manifest_v3.json"] = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    return {f"{DIRECTORY}/{PREFIX}{name}": payload for name, payload in payloads.items()}


def dirty_hashes(root):
    data = subprocess.check_output(["git", "--no-replace-objects", "status", "--porcelain", "-z", "--untracked-files=all"], cwd=root)
    result = {}
    for entry in data.decode("utf-8").split("\0"):
        if entry:
            path = entry[3:]
            file = root / path
            result[path] = sha(file.read_bytes()) if file.is_file() else "missing"
    return result


def protected_snapshot(root: Path, sentinels):
    """Sparse equivalent: immutable Git-object identities plus physical bytes.

    Absent sparse files are NOT claimed physically inspected. Their complete
    tree/index membership is bound, while ignored/skip-worktree physical files
    are inspected independently of git status. No protected materialization.
    """
    patterns = [sentinel.artifact_glob for sentinel in sentinels]
    matches = lambda path: any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    tree_data = subprocess.check_output(["git", "--no-replace-objects", "ls-tree", "-r", "-z", "HEAD"], cwd=root)
    index_data = subprocess.check_output(["git", "--no-replace-objects", "ls-files", "--stage", "-z"], cwd=root)
    tree, index, physical = {}, {}, {}
    for entry in tree_data.decode("utf-8").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            if matches(path):
                tree[path] = meta
    for entry in index_data.decode("utf-8").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            if matches(path):
                index[path] = meta
    candidates = set(tree) | set(index)
    for pattern in patterns:
        wildcard = min((pattern.find(char) for char in "*?[" if char in pattern), default=-1)
        if wildcard == -1:
            candidates.add(pattern)
            continue
        prefix = pattern[:wildcard].rsplit("/", 1)[0]
        directory = root / prefix
        if directory.exists():
            candidates.update(path.relative_to(root).as_posix() for path in directory.rglob("*") if path.is_file() and matches(path.relative_to(root).as_posix()))
    for relative in sorted(candidates):
        path = root / relative
        if path.is_symlink():
            raise RuntimeError(f"protected sentinel cannot be a symlink: {relative}")
        if path.is_file():
            physical[relative] = sha(path.read_bytes())
    for sentinel in sentinels:
        if sentinel.required and not any(fnmatch.fnmatchcase(path, sentinel.artifact_glob) for path in set(tree) | set(index) | set(physical)):
            raise RuntimeError(f"required protected sentinel family missing from Git and disk: {sentinel.sentinel_id}")
    return {"git_tree_blob_mapping": tree, "git_index_blob_mapping": index, "physical_sha256": physical}


@contextmanager
def artifact_guard(root):
    sparse = subprocess.run(["git", "--no-replace-objects", "config", "--bool", "core.sparseCheckout"], cwd=root, check=False, capture_output=True, text=True).stdout.strip() == "true"
    if not sparse:
        with model_owned_artifact_guard(OWNER_ID, PRODUCER, root=root, registry_path=root / "config/model_research_artifact_ownership.csv", sentinel_registry_path=root / "config/model_research_protected_sentinels.csv"):
            yield
        return
    sentinels = load_protected_sentinels(root / "config/model_research_protected_sentinels.csv")
    protected_before = protected_snapshot(root, sentinels)
    before = dirty_hashes(root)
    try:
        yield
    finally:
        after = dirty_hashes(root)
        protected_after = protected_snapshot(root, sentinels)
        if protected_before != protected_after:
            raise RuntimeError("protected sentinel Git mapping or physical SHA256 drift during model build/write")
        changed = [path for path in set(before) | set(after) if before.get(path, "clean") != after.get(path, "clean")]
        errors = validate_changed_paths(OWNER_ID, PRODUCER, changed, load_ownership_rules(root / "config/model_research_artifact_ownership.csv"))
        if errors:
            raise RuntimeError("model-owned sparse artifact guard failed: " + "; ".join(errors))
        print(f"model-owned sparse artifact guard passed owner={OWNER_ID} changed_paths={len(changed)}")
        print(f"protected_git_mapping_paths={len(protected_after['git_tree_blob_mapping'])}; protected_physical_files={len(protected_after['physical_sha256'])}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build only the immutable TDCC Scheme A research operation replay v3.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ref", default=SOURCE_REF)
    parser.add_argument("--artifact-source-ref", default=ARTIFACT_SOURCE_REF)
    args = parser.parse_args(argv)
    with artifact_guard(args.repository_root.resolve()):
        payloads = build(args.repository_root.resolve(), args.source_ref, args.artifact_source_ref)
        expected = {f"{DIRECTORY}/{PREFIX}{name}_v3.csv" for name in ("signals", "events", "positions", "summary", "evidence")} | {f"{DIRECTORY}/{PREFIX}manifest_v3.json", f"{DIRECTORY}/{PREFIX}report_v3.md"}
        if set(payloads) != expected:
            raise RuntimeError("producer output allowlist must be exactly the seven v3 artifacts")
        for path, payload in payloads.items():
            destination = args.repository_root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
    print(f"operation_replay_v3_artifacts={len(payloads)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
