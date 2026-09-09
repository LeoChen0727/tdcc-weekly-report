"""Independent evidence and arithmetic oracle for TDCC stealth research v3.

This module deliberately imports neither a research producer nor production
business code. Immutable inputs and actual output bytes are checked separately.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
SOURCE_REF = "7ef37a966280201a5ee236856306fdb513de7092"
ARTIFACT_SOURCE_REF = "2244a0a36c4542cd62948b50f12ef98ade50e1df"
DETAIL_SHA256 = "4e404bd8f73ed888b56384a1447461644ed6d5afa06ac420774983ddb595ddc3"
DIRECTORY = "output/research/tdcc_stealth_accumulation"
PREFIX = "tdcc_stealth_accumulation_operation_replay_"
DETAIL_PATH = f"{DIRECTORY}/tdcc_stealth_accumulation_historical_selector_field_contract_replay_detail_v2.csv"
AUDIT_PATH = f"{DIRECTORY}/tdcc_stealth_accumulation_price_pit_audit_v1.csv"
HORIZONS = (5, 10, 20)
SLIPPAGES = (Decimal("0"), Decimal("0.001"), Decimal("0.002"))
TAIPEI = timezone(timedelta(hours=8))
FALSE_FLAGS = ("formal_use", "trade_eligible", "promotion_evidence_allowed")
ARTIFACT_SUFFIXES = (
    "signals_v3.csv", "events_v3.csv", "positions_v3.csv", "summary_v3.csv",
    "evidence_v3.csv", "manifest_v3.json", "report_v3.md",
)


def _sha(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _text(value: Any) -> str:
    text = str(value if value is not None else "").replace("\ufeff", "").strip()
    return "" if text.lower() in {"nan", "none", "nat", "<na>"} else text


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _canonical_row_hash(row: dict[str, Any]) -> str:
    return _sha(_canonical({str(k): _text(v) for k, v in row.items()}).encode("utf-8"))


def _lf_payload(payload: bytes) -> bytes:
    if payload.startswith(b"\xef\xbb\xbf"):
        raise ValueError("output UTF-8 BOM is forbidden")
    without_pairs = payload.replace(b"\r\n", b"")
    if b"\r" in without_pairs:
        raise ValueError("bare CR is forbidden")
    if b"\r\n" in payload and b"\n" in without_pairs:
        raise ValueError("mixed LF/CRLF is forbidden")
    payload.decode("utf-8", errors="strict")
    return payload.replace(b"\r\n", b"\n")


def _csv(payload: bytes, *, output: bool = False) -> tuple[list[str], list[dict[str, str]]]:
    text = (_lf_payload(payload) if output else payload).decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text, newline=""), strict=True)
    fields = reader.fieldnames or []
    if not fields or len(fields) != len(set(fields)) or any(not field for field in fields):
        raise ValueError("CSV missing or duplicate column names")
    rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError("CSV row width differs from header")
    return fields, rows


def _unique_json(payload: bytes | str) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(payload, object_pairs_hook=pairs)


def _decimal(value: Any, *, positive: bool = False) -> Decimal:
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"invalid decimal: {value!r}") from exc
    if not result.is_finite() or (positive and result <= 0):
        raise ValueError(f"invalid finite positive decimal: {value!r}")
    return result


def _ymd(value: str) -> date:
    if not re.fullmatch(r"20\d{6}", value):
        raise ValueError(f"invalid trading date: {value!r}")
    return datetime.strptime(value, "%Y%m%d").date()


def _next_session(value: str, closed: set[str]) -> str:
    current = _ymd(value)
    for _ in range(370):
        current += timedelta(days=1)
        result = current.strftime("%Y%m%d")
        if current.weekday() < 5 and result not in closed:
            return result
    raise ValueError("calendar does not provide a next session")


def _scheduled_dates(signal_date: str, horizon: int, closed: set[str]) -> tuple[str, str]:
    if horizon not in HORIZONS:
        raise ValueError("unregistered research horizon")
    entry = _next_session(signal_date, closed)
    exit_date = entry
    for _ in range(horizon):
        exit_date = _next_session(exit_date, closed)
    return entry, exit_date


def _cutoff(entry_date: str) -> datetime:
    return datetime.combine(_ymd(entry_date), time(8, 30), TAIPEI)


def _timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("available_at must have an explicit timezone")
    return parsed.astimezone(TAIPEI)


def _pit_errors(evidence: list[dict[str, Any]], signal_date: str, entry_date: str,
                required_features: set[str]) -> list[str]:
    errors: list[str] = []
    by_feature: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in evidence:
        by_feature[str(item.get("feature", ""))].append(item)
    if set(by_feature) != required_features:
        errors.append("feature evidence coverage differs from effective signature")
    for feature in sorted(required_features):
        items = by_feature.get(feature, [])
        if len(items) != 1:
            errors.append(f"{feature}: evidence must be unique")
            continue
        item = items[0]
        if item.get("evidence_status") != "verified_historical_availability":
            errors.append(f"{feature}: historical availability unverified")
        if item.get("evidence_type") in {"git_commit", "snapshot_generated_at", "current_download", "backfill"}:
            errors.append(f"{feature}: metadata is not historical feature availability")
        if not item.get("source_ref") or not re.fullmatch(r"[0-9a-f]{64}", str(item.get("source_sha256", ""))):
            errors.append(f"{feature}: evidence lineage missing")
        try:
            if _ymd(str(item.get("effective_date", ""))) > _ymd(signal_date):
                errors.append(f"{feature}: effective date is later than signal")
            if _timestamp(str(item.get("available_at", ""))) >= _cutoff(entry_date):
                errors.append(f"{feature}: availability must be strictly before 08:30")
        except (TypeError, ValueError):
            errors.append(f"{feature}: missing or malformed point-in-time date")
    return errors


def _cost_oracle(entry_open: Any, exit_close: Any, slippage: Any, *,
                 exit_shares: Any = "1000", cash_flows: Any = "0") -> dict[str, Decimal]:
    """Calculate from unadjusted prices and independently verified cash flows."""
    with localcontext() as context:
        context.prec = 50
        opening = _decimal(entry_open, positive=True)
        closing = _decimal(exit_close, positive=True)
        shares = _decimal(exit_shares, positive=True)
        cash = _decimal(cash_flows)
        slip = _decimal(slippage)
        if slip not in SLIPPAGES:
            raise ValueError("unregistered slippage assumption")
        buy = Decimal(1000) * opening * (1 + slip)
        sell = shares * closing * (1 - slip)
        buy_fee = max(Decimal(20), buy * Decimal("0.001425"))
        sell_fee = max(Decimal(20), sell * Decimal("0.001425"))
        tax = sell * Decimal("0.003")
        entry_cash = buy + buy_fee
        net_exit_cash = sell - sell_fee - tax + cash
        profit = net_exit_cash - entry_cash
        gross = (shares * closing + cash - Decimal(1000) * opening) / (Decimal(1000) * opening) * 100
        return {
            "buy_notional": buy, "sell_notional": sell, "buy_fee": buy_fee,
            "sell_fee": sell_fee, "sell_tax": tax, "entry_cash": entry_cash,
            "net_exit_cash": net_exit_cash, "net_profit": profit,
            "net_return_pct": profit / entry_cash * 100, "gross_return_pct": gross,
            "gross_pnl": shares * closing + cash - Decimal(1000) * opening,
        }


class _Sources:
    """Only immutable Git-object reads; no checkout or generated source writes."""

    def __init__(self, root: Path):
        self.root = root
        self.payloads: dict[tuple[str, str], bytes] = {}

    def git(self, *args: str) -> bytes:
        return subprocess.run(["git", "--no-replace-objects", "-C", str(self.root), *args], check=True,
                              capture_output=True).stdout

    def read(self, ref: str, path: str) -> bytes:
        if ref not in {SOURCE_REF, ARTIFACT_SOURCE_REF}:
            raise ValueError("source ref is outside the two immutable source roles")
        if path.startswith(("/", "\\")) or ".." in Path(path).parts or ":" in path:
            raise ValueError("source path is not repository relative")
        key = (ref, path)
        if key not in self.payloads:
            self.payloads[key] = self.git("show", f"{ref}:{path}")
        return self.payloads[key]

    def rows(self, ref: str, path: str) -> list[dict[str, str]]:
        return _csv(self.read(ref, path))[1]

    def paths(self, ref: str, prefix: str) -> list[str]:
        return self.git("ls-tree", "-r", "--name-only", ref, "--", prefix).decode("utf-8").splitlines()


def _flag_errors(rows: list[dict[str, str]], label: str) -> list[str]:
    return [f"{label} row {index}: {flag} must be False"
            for index, row in enumerate(rows, 2) for flag in FALSE_FLAGS
            if row.get(flag) != "False"]


def _load_baseline(sources: _Sources) -> dict[str, Any]:
    detail_bytes = sources.read(ARTIFACT_SOURCE_REF, DETAIL_PATH)
    if _sha(detail_bytes) != DETAIL_SHA256:
        raise ValueError("accepted v2 raw Git bytes differ from immutable detail digest")
    detail = _csv(detail_bytes)[1]
    if len(detail) != 6821 or len({row["stock_id"] for row in detail}) != 520:
        raise ValueError("accepted v2 population differs from 6821 signals / 520 stocks")
    if any(row["source_commit_sha"] != SOURCE_REF for row in detail):
        raise ValueError("v2 raw research source role differs from the fixed source")
    by_identity: dict[tuple[str, str], dict[str, str]] = {}
    originals: dict[tuple[str, str], dict[str, str]] = {}
    grouped: dict[tuple[str, str], list[tuple[str, str]]] = defaultdict(list)
    snapshots: dict[str, list[dict[str, str]]] = {}
    for row in detail:
        identity = row["snapshot_path"], row["snapshot_row_number"]
        if identity in by_identity:
            raise ValueError("v2 snapshot-row identity is duplicated")
        path, number = identity
        if path not in snapshots:
            snapshots[path] = sources.rows(SOURCE_REF, path)
        index = int(number) - 2
        if index < 0 or index >= len(snapshots[path]):
            raise ValueError("v2 snapshot source row is outside its source file")
        original = snapshots[path][index]
        if original["stock_id"] != row["stock_id"] or _canonical_row_hash(original) != row["snapshot_row_sha256"]:
            raise ValueError("v2 snapshot row identity or immutable source hash differs")
        by_identity[identity] = row
        originals[identity] = original
        grouped[(row["stock_id"], row["candidate_signal_date"])].append(identity)
    if len(grouped) != 5108 or len(snapshots) != 36 or sum(map(len, snapshots.values())) != 19361:
        raise ValueError("fixed snapshot / raw candidate / research event population mismatch")
    observations = sources.rows(ARTIFACT_SOURCE_REF, AUDIT_PATH)
    expected_observations = {
        "d10_max_observed_return": "8261", "d5_min_observed_return": "2492",
        "d5_max_observed_return": "1447", "d10_min_observed_return": "3624",
        "d20_min_observed_return": "8358", "d20_max_observed_return": "3653",
    }
    if len(observations) != 6 or {row["observation_id"]: row["stock_id"] for row in observations} != expected_observations:
        raise ValueError("all six original audit observations must be present")
    observation_ids: dict[tuple[str, str], list[str]] = defaultdict(list)
    for row in observations:
        if row["disposition"] != "unresolved_anomaly_candidate" or row["retained_in_primary"] != "True":
            raise ValueError("original unresolved audit candidate was removed or resolved")
        identity = (f"output/history/daily_model_snapshots/all_candidates_{row['snapshot_date']}.csv",
                    row["snapshot_row_number"])
        if identity not in by_identity or by_identity[identity]["stock_id"] != row["stock_id"]:
            raise ValueError("audit observation cannot be traced to the fixed signal row")
        observation_ids[identity].append(row["observation_id"])
    static = sources.rows(SOURCE_REF, "config/twse_non_trading_days.csv")
    emergency = sources.rows(SOURCE_REF, "data/market_calendar/exceptional_non_trading_days.csv")
    closed = {row["date"] for row in static}
    closed.update(row["date"] for row in emergency if row["market_status"] == "closed_emergency")
    for value in closed:
        _ymd(value)
    price_paths = {
        Path(path).stem: path for path in sources.paths(SOURCE_REF, "data/daily_price")
        if re.fullmatch(r"20\d{6}\.csv", Path(path).name)
    }
    as_of = max(price_paths)
    if as_of != "20260907":
        raise ValueError("fixed source price-as-of differs from 20260907")
    return {
        "signals": by_identity, "originals": originals, "groups": grouped,
        "observation_ids": observation_ids, "observations": observations,
        "closed": closed, "price_paths": price_paths, "as_of": as_of,
    }


def _price_observation(sources: _Sources, baseline: dict[str, Any], date_value: str,
                       stock: str, field: str,
                       cache: dict[str, dict[str, list[dict[str, str]]]]) -> tuple[str, str, str, str]:
    """Status, raw value, source file, immutable row hash; never advance a date."""
    if date_value > baseline["as_of"]:
        return "after_source_asof", "", "", ""
    path = baseline["price_paths"].get(date_value)
    if not path:
        return "missing_date_file", "", "", ""
    if path not in cache:
        indexed: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in sources.rows(SOURCE_REF, path):
            if row["date"] != date_value:
                raise ValueError("price file contains a mismatching row date")
            indexed[row["stock_id"]].append(row)
        cache[path] = indexed
    matches = cache[path].get(stock, [])
    if not matches:
        return "missing_stock_price", "", path, ""
    if len(matches) != 1:
        return "ambiguous_stock_price", "", path, ""
    row = matches[0]
    try:
        _decimal(row[field], positive=True)
    except (KeyError, ValueError):
        return "invalid_price", "", path, _canonical_row_hash(row)
    return "raw_price_present_unverified_execution", row[field], path, _canonical_row_hash(row)


def _number_cell(value: Any) -> Decimal | None:
    text = _text(value).replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    try:
        return _decimal(text)
    except ValueError:
        return None


def _chosen(row: dict[str, str], names: tuple[str, ...], *, numeric: bool = False) -> tuple[Any, str]:
    for name in names:
        for column in (name, name + "_x", name + "_y"):
            value = _number_cell(row.get(column, "")) if numeric else _text(row.get(column, ""))
            if value is not None and value != "":
                return value, column
    return (None if numeric else ""), ""


def _bool_cell(value: Any) -> bool:
    return _text(value).lower() in {"true", "1", "yes", "y", "t"}


def _signature_oracle(row: dict[str, str]) -> tuple[dict[str, Any], dict[str, str]]:
    """Resolve values independently; unused alias values and paths are excluded.

    Source aliases are returned as lineage, not conflated with value conflicts.
    The legacy boolean paths intentionally read only the unsuffixed column.
    """
    values: dict[str, Any] = {}
    lineage: dict[str, str] = {}

    def read(key: str, *names: str, numeric: bool = True) -> Any:
        value, source = _chosen(row, tuple(names), numeric=numeric)
        values[key], lineage[key] = value, source
        return value

    phase = read("phase", "tdcc_price_phase", numeric=False).lower()
    status = read("status", "tdcc_status", "tdcc_judgement", "tdcc_judge", numeric=False).lower()
    values["phase"], values["status"] = phase, status
    enum, enum_source = _chosen(row, ("tdcc_accumulation_signal",))
    enum = enum.lower()
    current_bool = _bool_cell(row.get("tdcc_accumulation_signal", ""))
    positive = {"strong_accumulation", "mild_accumulation"}
    if phase:
        values["tdcc_branch"] = "phase"
        values["tdcc_value"] = phase
        values["tdcc_positive"] = phase == "tdcc_leading_price"
        values.pop("status")
        lineage.pop("status")
    elif status:
        values["tdcc_branch"] = "status"
        values["tdcc_value"] = status
        values["tdcc_positive"] = status in positive or current_bool
        if status not in positive:
            values["tdcc_boolean"] = current_bool
            lineage["tdcc_boolean"] = "tdcc_accumulation_signal"
    elif current_bool:
        values["tdcc_branch"] = "boolean"
        values["tdcc_value"] = True
        values["tdcc_positive"] = True
        lineage["tdcc_value"] = "tdcc_accumulation_signal"
    else:
        values["tdcc_branch"] = "enum_fallback"
        values["tdcc_value"] = enum
        values["tdcc_positive"] = enum in positive
        lineage["tdcc_value"] = enum_source

    read("volume_ratio", "volume_ratio")
    read("return_5d_pct", "return_5d", "return_5d_pct")
    read("return_20d_pct", "return_20d", "return_20d_pct")
    close = read("close", "close")
    read("recent_range_high", "high_20", "previous_20d_high", "platform_high")
    read("recent_range_low", "low_20", "previous_20d_low", "platform_low")
    read("open", "open")
    high = read("high", "high")
    read("low", "low")
    ma, ma_source = _chosen(row, ("volume_ma20_lots", "avg_volume_20d_lots"), numeric=True)
    if ma is None:
        ma, ma_source = _chosen(row, ("volume_ma20", "avg_volume_20d"), numeric=True)
        if ma is not None and ma >= 100000:
            ma /= 1000
    values["volume_ma20_lots"], lineage["volume_ma20_lots"] = ma, ma_source
    previous = read("previous_close", "previous_close", "prev_close", "close_prev", "close_1d_ago")
    level, level_source = _chosen(row, ("previous_20d_high_ex_today", "prior_20d_high", "previous_20d_high", "high_20_ex_today"), numeric=True)
    values["breakout_branch"] = "prior_high"
    if level is not None and high is not None and close is not None:
        platform, platform_source = _chosen(row, ("platform_high", "short_platform_high", "range_high"), numeric=True)
        if level >= high * Decimal("0.999") and platform is not None and platform < level:
            level, level_source = platform, platform_source
            values["breakout_branch"] = "lower_platform_replacement"
    values["breakout_level"], lineage["breakout_level"] = level, level_source
    daily, daily_source = _chosen(row, ("daily_return_calc", "return_1d", "return_1d_pct"), numeric=True)
    values["daily_return_branch"] = "provided"
    if daily is None and close is not None and previous is not None and previous > 0:
        with localcontext() as context:
            context.prec = 50
            daily = (close / previous - 1) * 100
        values["daily_return_branch"] = "close_previous_close_fallback"
        daily_source = "close/previous_close"
    values["daily_return_pct"], lineage["daily_return_pct"] = daily, daily_source
    values["volume_confirmed_breakout"] = _bool_cell(row.get("volume_confirmed_breakout", ""))
    lineage["volume_confirmed_breakout"] = "volume_confirmed_breakout"
    return values, lineage


def _fixed(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, Decimal):
        rendered = format(value, "f")
        return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered
    return str(value)


def _serialized_signature(raw: dict[str, str]) -> tuple[dict[str, str], dict[str, str]]:
    facts, provenance = _signature_oracle(raw)
    branch = facts["tdcc_branch"]
    values = {"tdcc_price_phase": facts["phase"]}
    sources = {"tdcc_price_phase": provenance["phase"]}
    if branch != "phase":
        values["tdcc_status"] = facts["status"]
        sources["tdcc_status"] = provenance["status"]
    values["tdcc_positive_branch"] = {
        "phase": "explicit_phase", "status": "status_alias",
        "boolean": "original_boolean", "enum_fallback": "enum_fallback",
    }[branch]
    if branch == "boolean" or "tdcc_boolean" in facts:
        values["tdcc_accumulation_boolean"] = str(facts.get("tdcc_boolean", True))
        sources["tdcc_accumulation_boolean"] = "tdcc_accumulation_signal"
    elif branch == "enum_fallback":
        values["tdcc_accumulation_enum"] = facts["tdcc_value"]
        sources["tdcc_accumulation_enum"] = provenance["tdcc_value"]
    names = (
        "volume_ratio", "return_5d_pct", "return_20d_pct", "recent_range_high",
        "recent_range_low", "open", "high", "low", "close", "previous_close",
        "volume_ma20_lots", "breakout_level", "daily_return_pct", "volume_confirmed_breakout",
    )
    for name in names:
        values[name] = _fixed(facts[name])
        sources[name] = provenance[name]
    if facts["daily_return_branch"] == "close_previous_close_fallback":
        sources["daily_return_pct"] = "derived_close_previous_close"
    return values, sources


def _check_feature_placeholders(features: Any, names: set[str]) -> bool:
    """Pinned snapshots have no acceptable per-feature availability records."""
    if not isinstance(features, list) or len(features) != len(names):
        return False
    if {feature.get("name") for feature in features if isinstance(feature, dict)} != names:
        return False
    return all(feature == {"name": feature["name"], "effective_date": "", "available_at": "",
                           "verified": False, "evidence_ref": ""} for feature in features)


def _action_cash_oracle(actions: list[dict[str, Any]], entry: str, exit_date: str) -> tuple[Decimal, Decimal]:
    if len({_canonical(action) for action in actions}) != len(actions):
        raise ValueError("duplicate corporate action would double-count shares/cash")
    daily: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for action in actions:
        event_date = action["event_date"]
        _ymd(event_date)
        if not entry <= event_date <= exit_date:
            raise ValueError("company action is outside the holding window")
        if action.get("evidence_verified") is not True or not action.get("evidence_ref"):
            raise ValueError("company action is unverified")
        daily[event_date].append(action)
    ordered: list[dict[str, Any]] = []
    for _, same_day in sorted(daily.items()):
        if {item.get("kind") for item in same_day} >= {"cash", "share_factor"}:
            sequence = [item.get("sequence") for item in same_day]
            if not all(type(value) is int for value in sequence) or len(set(sequence)) != len(sequence) or not all(item.get("sequence_evidence_ref") for item in same_day):
                raise ValueError("same-day cash/share actions require unique verified ordering")
            same_day = sorted(same_day, key=lambda item: item["sequence"])
        ordered.extend(same_day)
    with localcontext() as context:
        context.prec = 50
        shares, cash = Decimal(1000), Decimal(0)
        for item in ordered:
            if item["kind"] == "share_factor":
                shares *= _decimal(item["share_factor"], positive=True)
            elif item["kind"] == "cash":
                cash += shares * _decimal(item["cash_per_share"])
            else:
                raise ValueError("unknown company action")
    return shares, cash


def _validate_positions(positions: list[dict[str, str]], events: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    by_event = {(row["event_id"], row["horizon"]): row for row in events}
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in positions:
        groups[row.get("position_id", "")].append(row)
    ledgers: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for position_id, variants in groups.items():
        base = variants[0]
        prefix = f"position {position_id}"
        try:
            if len(variants) != 3 or {_decimal(row["slippage"]) for row in variants} != set(SLIPPAGES):
                errors.append(f"{prefix}: sensitivity must contain the same position at all three slippages")
            key = (base["event_id"], base["horizon"])
            event = by_event.get(key)
            if not event or event["status"] != "position_opened":
                errors.append(f"{prefix}: no accepted entry event")
            if position_id != f"{base['event_id']}:D{base['horizon']}":
                errors.append(f"{prefix}: position identity mismatch")
            invariant = ("stock_id", "signal_date", "horizon", "entry_date", "exit_date", "entry_open",
                         "exit_close", "status", "actions", "quantity", "anomaly_candidate", "observation_ids")
            for row in variants:
                if any(row.get(field) != base.get(field) for field in invariant):
                    errors.append(f"{prefix}: sensitivity changed position identity or lifecycle")
                if row.get("quantity") != "1000":
                    errors.append(f"{prefix}: fixed quantity must be 1000")
            if base["status"] not in {"realized", "open_immature", "open_unresolved_exit"}:
                errors.append(f"{prefix}: invalid lifecycle status")
            ledgers[(base["stock_id"], base["horizon"])].append(base)
            if base["status"] != "realized":
                for row in variants:
                    if any(row.get(field, "") for field in ("net_return_pct", "gross_return_pct", "net_pnl", "gross_pnl", "outcome", "high_return_hit", "major_loss")):
                        errors.append(f"{prefix}: unrealized positions must not enter return denominators")
                continue
            actions = _unique_json(base.get("actions", "[]"))
            shares, cash = _action_cash_oracle(actions, base["entry_date"], base["exit_date"])
            for row in variants:
                costs = _cost_oracle(row["entry_open"], row["exit_close"], row["slippage"], exit_shares=shares, cash_flows=cash)
                mapping = {"buy_notional": "buy_amount", "sell_notional": "sell_amount", "net_profit": "net_pnl"}
                for field, expected in costs.items():
                    actual_name = mapping.get(field, field)
                    if _decimal(row.get(actual_name, "")) != expected:
                        errors.append(f"{prefix}: Decimal {actual_name} mismatch")
                if _decimal(row.get("final_shares", "")) != shares or _decimal(row.get("cash_flows", "")) != cash:
                    errors.append(f"{prefix}: verified shares or cash flow double-counted/missing")
                outcome = "win" if costs["net_profit"] > 0 else "loss" if costs["net_profit"] < 0 else "neutral"
                if row["outcome"] != outcome or row["high_return_hit"] != str(costs["net_return_pct"] >= 10) or row["major_loss"] != str(costs["net_return_pct"] <= -10):
                    errors.append(f"{prefix}: fixed descriptive return group mismatch")
        except (KeyError, TypeError, ValueError, InvalidOperation) as exc:
            errors.append(f"{prefix}: malformed lifecycle/cost evidence: {exc}")
    for key, ledger in ledgers.items():
        ordered = sorted(ledger, key=lambda row: (row["signal_date"], row["entry_date"]))
        for prior, later in zip(ordered, ordered[1:]):
            if prior["status"] != "realized" or later["signal_date"] <= prior["exit_date"]:
                errors.append(f"ledger {key}: active/unresolved/exit-day lock was released or queued signal entered")
    if {(r["event_id"], r["horizon"]) for r in positions} != {key for key, row in by_event.items() if row["status"] == "position_opened"}:
        errors.append("positions do not exactly cover accepted entry events")
    return errors


def _validate_summary(summary: list[dict[str, str]], events: list[dict[str, str]],
                      positions: list[dict[str, str]], signal_count: int) -> list[str]:
    errors: list[str] = []
    expected_keys = {(str(h), str(s), population) for h in HORIZONS for s in SLIPPAGES
                     for population in ("primary", "excluding_anomaly_candidates_sensitivity")}
    observed = [(r.get("horizon"), r.get("slippage"), r.get("analysis_population")) for r in summary]
    if len(observed) != 18 or set(observed) != expected_keys:
        return ["summary must contain all 18 preregistered horizon/slippage/population cells"]
    for row in summary:
        horizon, slip, population = row["horizon"], row["slippage"], row["analysis_population"]
        selected_events = [e for e in events if e["horizon"] == horizon]
        selected = [p for p in positions if p["horizon"] == horizon and p["slippage"] == slip
                    and (population == "primary" or p["anomaly_candidate"] != "True")]
        realized = [p for p in selected if p["status"] == "realized"]
        returns = sorted(_decimal(p["net_return_pct"]) for p in realized)
        n = len(returns)
        win = sum(_decimal(p["net_pnl"]) > 0 for p in realized)
        neutral = sum(_decimal(p["net_pnl"]) == 0 for p in realized)
        loss = n - win - neutral
        high, major = sum(v >= 10 for v in returns), sum(v <= -10 for v in returns)
        expected: dict[str, Any] = {
            "artifact_version": "tdcc_stealth_accumulation_operation_replay_v3",
            "signal_count": signal_count, "event_count": len(selected_events),
            "stock_count": len({e["stock_id"] for e in selected_events}),
            "position_count": len(selected), "realized_count": n,
            "immature_count": sum(p["status"] == "open_immature" for p in selected),
            "unresolved_count": sum(p["status"] == "open_unresolved_exit" for p in selected),
            "immature_event_count": sum(e["window_status"] == "immature" for e in selected_events),
            "evidence_missing_event_count": sum(bool(e["evidence_missing"]) for e in selected_events),
            "conflict_event_count": sum(e["signature_conflict"] == "True" for e in selected_events),
            "win_count": win, "neutral_count": neutral, "loss_count": loss,
            "high_return_hit_count": high, "major_loss_count": major,
            "denominator": "all_realized_positions_in_this_horizon_slippage_population",
            "performance_status": "research_only_verified_position_sample" if n else "unavailable_no_realized_verified_positions",
            "status_counts": _canonical(dict(Counter(e["status"] for e in selected_events))),
        }
        with localcontext() as context:
            context.prec = 50
            for name, count in (("win_rate_pct", win), ("neutral_rate_pct", neutral), ("loss_rate_pct", loss),
                                ("high_return_hit_rate_pct", high), ("major_loss_rate_pct", major)):
                expected[name] = _fixed(Decimal(count) / n * 100) if n else ""
            expected["average_net_return_pct"] = _fixed(sum(returns) / n) if n else ""
            expected["median_net_return_pct"] = _fixed(returns[n // 2] if n % 2 else (returns[n // 2 - 1] + returns[n // 2]) / 2) if n else ""
            expected["tail_loss_pct"] = _fixed(min(returns)) if n else ""
        for field, value in expected.items():
            if row.get(field) != str(value):
                errors.append(f"summary D{horizon}/{slip}/{population}: {field} differs from independently counted rows")
    return errors


def _validate_payloads(payloads: dict[str, bytes], sources: _Sources,
                       baseline: dict[str, Any] | None = None) -> list[str]:
    """Validate real serialized outputs against an independent immutable oracle."""
    errors: list[str] = []

    def check(label: str, actual: Any, expected: Any) -> None:
        if actual != expected:
            errors.append(f"{label}: expected {str(expected)[:140]!r}, observed {str(actual)[:140]!r}")

    if set(payloads) != set(ARTIFACT_SUFFIXES):
        return ["all seven exact model-owned v3 artifacts are required"]
    try:
        for name, payload in payloads.items():
            if _lf_payload(payload) != payload:
                errors.append(f"{name}: actual serialized LF bytes required by manifest hash_basis")
        manifest = _unique_json(payloads["manifest_v3.json"])
        if not isinstance(manifest, dict):
            return errors + ["manifest JSON must be an object"]
        tables = {name: _csv(payloads[name], output=True) for name in ARTIFACT_SUFFIXES if name.endswith(".csv")}
        report = payloads["report_v3.md"].decode("utf-8")
    except (ValueError, UnicodeError, csv.Error) as exc:
        return errors + [f"unreadable or ambiguous artifact: {exc}"]
    try:
        for field, expected in {
            "artifact_version": "tdcc_stealth_accumulation_operation_replay_v3",
            "owner_id": "tdcc_stealth_accumulation_operation_replay", "model_id": MODEL_ID,
            "source_commit_sha": SOURCE_REF, "artifact_source_commit_sha": ARTIFACT_SOURCE_REF,
            "accepted_v2_detail_sha256": DETAIL_SHA256, "as_of": "20260907",
            "hash_basis": "actual_serialized_utf8_bytes_no_bom_lf", "decimal_precision": 50,
            "signal_rows": 6821, "unique_events": 5108, "event_horizon_rows": 15324,
            "position_sensitivity_rows": 0, "anomaly_observations": 6,
            "calendar_evidence_status": "repo_version_reproducible_official_event_payload_not_fully_verified",
            "corporate_action_evidence_status": "company_calendar_is_advisory_not_complete_cash_flow_ledger",
            **{flag: "False" for flag in FALSE_FLAGS},
        }.items():
            check(f"manifest {field}", manifest.get(field), expected)
        entries = manifest.get("artifacts", {})
        expected_names = {PREFIX + name for name in ARTIFACT_SUFFIXES if name != "manifest_v3.json"}
        check("manifest six payload inventory", set(entries), expected_names)
        for name in ARTIFACT_SUFFIXES:
            if name == "manifest_v3.json":
                continue
            entry = entries.get(PREFIX + name, {})
            check(f"{name} actual-byte digest", entry.get("sha256"), _sha(payloads[name]))
            check(f"{name} actual-byte size", entry.get("size_bytes"), len(payloads[name]))
        if baseline is None:
            baseline = _load_baseline(sources)
        accepted_summary_path = f"{DIRECTORY}/tdcc_stealth_accumulation_historical_selector_field_contract_replay_summary_v2.csv"
        old_summary = sources.rows(ARTIFACT_SOURCE_REF, accepted_summary_path)
        sources.read(SOURCE_REF, "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv")
        sources.read(SOURCE_REF, "data/company_calendar/company_event_calendar.csv")
        start = min(signal for stock, signal in baseline["groups"])
        end = _ymd(baseline["as_of"]) + timedelta(days=70)
        current = _ymd(start)
        calendar: list[str] = []
        while current <= end:
            value = current.strftime("%Y%m%d")
            if current.weekday() < 5 and value not in baseline["closed"]:
                calendar.append(value)
            current += timedelta(days=1)
        check("manifest exchange-calendar dates", manifest.get("exchange_calendar"), calendar)
        # The producer reads the complete fixed-date files, not only endpoints.
        for day, path in baseline["price_paths"].items():
            if start <= day <= baseline["as_of"]:
                sources.read(SOURCE_REF, path)
        source_entries = manifest.get("source_artifacts", [])
        observed_sources = {(item["source_commit_sha"], item["path"]): item for item in source_entries}
        check("manifest unique source entries", len(observed_sources), len(source_entries))
        check("manifest complete source inventory", set(observed_sources), set(sources.payloads))
        for key, payload in sources.payloads.items():
            item = observed_sources.get(key, {})
            check(f"source {key} digest", item.get("sha256"), _sha(payload))
            check(f"source {key} size", item.get("size_bytes"), len(payload))

        signals = tables["signals_v3.csv"][1]
        events = tables["events_v3.csv"][1]
        positions = tables["positions_v3.csv"][1]
        summary = tables["summary_v3.csv"][1]
        evidence = tables["evidence_v3.csv"][1]
        for label, (_, rows) in tables.items():
            errors.extend(_flag_errors(rows, label))
        for label, rows, expected_count in (("signals", signals, 6821), ("events", events, 15324), ("positions", positions, 0), ("evidence", evidence, 6)):
            check(f"{label} actual row count", len(rows), expected_count)
        required_signal = {
            "signal_id", "event_id", "stock_id", "stock_name", "signal_date", "v2_detail_row_number",
            "v2_detail_sha256", "source_commit_sha", "artifact_source_commit_sha", "snapshot_path",
            "snapshot_sha256", "snapshot_row_number", "snapshot_row_sha256", "snapshot_generated_at",
            "snapshot_pipeline_commit_sha", "signature", "signature_sources", "signature_sha256",
            "feature_evidence", "visible_source_dates", "pit_status", "calendar_verified",
            "corporate_actions_verified", "anomaly_candidate", "anomaly_disposition", "observation_ids",
            "retained_in_primary", *FALSE_FLAGS,
        }
        check("signal schema", set(tables["signals_v3.csv"][0]), required_signal)
        event_fields = {
            "event_id", "stock_id", "signal_date", "horizon", "entry_date", "exit_date", "decision_cutoff",
            "source_ids", "source_row_count", "signature_conflict", "signature_count", "entry_open", "exit_close",
            "entry_price_status", "exit_price_status", "window_status", "evidence_missing", "feature_evidence",
            "calendar_verified", "corporate_actions_verified", "entry_source_path", "entry_source_sha256",
            "entry_row_sha256", "exit_source_path", "exit_source_sha256", "exit_row_sha256", "anomaly_candidate",
            "observation_ids", "retained_in_primary", "status", *FALSE_FLAGS,
        }
        check("event schema", set(tables["events_v3.csv"][0]), event_fields)
        position_extra = {
            "position_id", "slippage", "quantity", "actions", "outcome", "high_return_hit", "major_loss",
            "buy_amount", "sell_amount", "buy_fee", "sell_fee", "sell_tax", "entry_cash", "net_exit_cash",
            "net_pnl", "gross_pnl", "gross_return_pct", "net_return_pct", "final_shares", "cash_flows",
        }
        check("positions empty or nonempty schema", set(tables["positions_v3.csv"][0]), event_fields | position_extra)
        signal_by_id = {row["signal_id"]: row for row in signals}
        expected_signal_ids = {f"v2:{index}" for index in range(2, len(baseline["signals"]) + 2)}
        check("signal identities", set(signal_by_id), expected_signal_ids)
        check("signal identity uniqueness", len(signal_by_id), len(signals))
        observation_groups: dict[tuple[str, str], list[str]] = defaultdict(list)
        for item in baseline["observations"]:
            observation_groups[(item["stock_id"], item["signal_date"])].append(item["observation_id"])
        expected_signatures: dict[str, dict[str, str]] = {}
        event_signals: dict[tuple[str, str], list[str]] = defaultdict(list)
        expected_features: dict[str, list[dict[str, Any]]] = {}
        event_anomaly: dict[tuple[str, str], bool] = defaultdict(bool)
        lineage_fields = ("snapshot_path", "snapshot_sha256", "snapshot_row_number", "snapshot_row_sha256",
                          "snapshot_generated_at", "snapshot_pipeline_commit_sha")
        for index, (identity, old) in enumerate(baseline["signals"].items(), 2):
            signal_id = f"v2:{index}"
            actual = signal_by_id.get(signal_id, {})
            raw = baseline["originals"][identity]
            values, source_fields = _serialized_signature(raw)
            expected_signatures[signal_id] = values
            group = (old["stock_id"], old["candidate_signal_date"])
            event_signals[group].append(signal_id)
            codes = observation_groups.get(group, [])
            anomaly = bool(codes) or old["anomaly_candidate"] == "True"
            event_anomaly[group] |= anomaly
            expected = {
                "event_id": f"{group[0]}:{group[1]}", "stock_id": group[0], "stock_name": old["stock_name"],
                "signal_date": group[1], "v2_detail_row_number": str(index), "v2_detail_sha256": DETAIL_SHA256,
                "source_commit_sha": SOURCE_REF, "artifact_source_commit_sha": ARTIFACT_SOURCE_REF,
                "signature_sha256": _sha(_canonical(values).encode("utf-8")),
                "pit_status": "not_complete_event_time_PIT_proof", "calendar_verified": "False",
                "corporate_actions_verified": "False", "anomaly_candidate": str(anomaly),
                "anomaly_disposition": "unresolved_anomaly_candidate" if anomaly else "not_triggered",
                "retained_in_primary": "True", **{field: old[field] for field in lineage_fields},
            }
            for field, expected_value in expected.items():
                check(f"signal {signal_id} {field}", actual.get(field), expected_value)
            check(f"signal {signal_id} parsed signature", _unique_json(actual.get("signature", "{}")), values)
            check(f"signal {signal_id} effective alias lineage", _unique_json(actual.get("signature_sources", "{}")), source_fields)
            check(f"signal {signal_id} observations", _unique_json(actual.get("observation_ids", "[]")), codes)
            visible = {field: _text(raw.get(field)) for field in ("date", "signal_date", "main_price_date", "source_date", "raw_source_date", "tdcc_date") if _text(raw.get(field))}
            check(f"signal {signal_id} visible dates", _unique_json(actual.get("visible_source_dates", "{}")), visible)
            features = _unique_json(actual.get("feature_evidence", "[]"))
            if not _check_feature_placeholders(features, set(values)):
                errors.append(f"signal {signal_id}: fabricated, omitted, or malformed historical feature evidence")
            expected_features[signal_id] = features

        event_by_key = {(row["event_id"], row["horizon"]): row for row in events}
        expected_event_keys = {(f"{stock}:{signal}", str(h)) for stock, signal in event_signals for h in HORIZONS}
        check("all 5108 events in three independent horizons", set(event_by_key), expected_event_keys)
        check("event identity uniqueness", len(event_by_key), len(events))
        price_cache: dict[str, dict[str, list[dict[str, str]]]] = {}
        for group, ids in event_signals.items():
            stock, signal_date = group
            event_id = f"{stock}:{signal_date}"
            signature_count = len({_canonical(expected_signatures[signal_id]) for signal_id in ids})
            features = [feature for signal_id in ids for feature in expected_features[signal_id]]
            for horizon in HORIZONS:
                actual = event_by_key.get((event_id, str(horizon)), {})
                entry_date, exit_date = _scheduled_dates(signal_date, horizon, baseline["closed"])
                entry_obs = _price_observation(sources, baseline, entry_date, stock, "open", price_cache)
                exit_obs = _price_observation(sources, baseline, exit_date, stock, "close", price_cache)
                opening = _number_cell(entry_obs[1])
                closing = _number_cell(exit_obs[1])
                if signature_count != 1:
                    status = "signature_conflict"
                elif signal_date not in calendar:
                    status = "signal_not_exchange_day"
                elif entry_date > baseline["as_of"]:
                    status = "entry_after_as_of"
                elif opening is None or opening <= 0:
                    status = "entry_price_missing"
                else:
                    status = "feature_evidence_missing"
                expected = {
                    "event_id": event_id, "stock_id": stock, "signal_date": signal_date, "horizon": str(horizon),
                    "entry_date": entry_date, "exit_date": exit_date, "decision_cutoff": f"{entry_date}T08:30:00+08:00",
                    "source_row_count": str(len(ids)), "signature_count": str(signature_count),
                    "signature_conflict": str(signature_count != 1), "entry_open": _fixed(opening), "exit_close": _fixed(closing),
                    "entry_price_status": "missing" if opening is None or opening <= 0 else "observed_raw_unverified",
                    "exit_price_status": "missing" if closing is None or closing <= 0 else "observed_raw_unverified",
                    "window_status": "immature" if exit_date > baseline["as_of"] else "mature_calendar_window",
                    "evidence_missing": ";".join(sorted({"historical_availability_unproven", "feature_effective_date_unproven",
                        "official_calendar_evidence_unproven", "corporate_action_coverage_unproven", "entry_execution_unproven", "exit_execution_unproven"})),
                    "calendar_verified": "False", "corporate_actions_verified": "False",
                    "anomaly_candidate": str(event_anomaly[group]), "retained_in_primary": "True", "status": status,
                }
                for endpoint, observation in (("entry", entry_obs), ("exit", exit_obs)):
                    has_row = bool(observation[3])
                    expected[endpoint + "_source_path"] = observation[2] if has_row else ""
                    expected[endpoint + "_source_sha256"] = _sha(sources.read(SOURCE_REF, observation[2])) if has_row else ""
                    expected[endpoint + "_row_sha256"] = observation[3]
                for field, expected_value in expected.items():
                    check(f"event {event_id}/D{horizon} {field}", actual.get(field), expected_value)
                check(f"event {event_id}/D{horizon} all source IDs", _unique_json(actual.get("source_ids", "[]")), ids)
                check(f"event {event_id}/D{horizon} feature evidence", _unique_json(actual.get("feature_evidence", "[]")), features)
                check(f"event {event_id}/D{horizon} observations", _unique_json(actual.get("observation_ids", "[]")), sorted(observation_groups.get(group, [])))
        errors.extend(_validate_positions(positions, events))
        errors.extend(_validate_summary(summary, events, positions, len(signals)))
        evidence_by_id = {row["observation_id"]: row for row in evidence}
        check("six unique evidence identities", len(evidence_by_id), 6)
        check("all original observation IDs retained", set(evidence_by_id), {row["observation_id"] for row in baseline["observations"]})
        for old in baseline["observations"]:
            actual = evidence_by_id.get(old["observation_id"], {})
            group = old["stock_id"], old["signal_date"]
            for field, value in {
                "stock_id": group[0], "signal_date": group[1], "event_id": f"{group[0]}:{group[1]}",
                "audit_source_path": AUDIT_PATH, "audit_source_sha256": _sha(sources.read(ARTIFACT_SOURCE_REF, AUDIT_PATH)),
                "anomaly_disposition": "unresolved_anomaly_candidate", "retained_in_primary": "True",
                "historical_availability_status": "unproven", "corporate_action_coverage_status": "unproven", "execution_status": "unproven",
            }.items():
                check(f"evidence {old['observation_id']} {field}", actual.get(field), value)
            check(f"evidence {old['observation_id']} immutable original audit row", _unique_json(actual.get("audit_row", "{}")), old)
            check(f"evidence {old['observation_id']} complete event lineage", _unique_json(actual.get("source_signal_ids", "[]")), event_signals[group])
        for token in ("TDCC 潛伏吸籌", SOURCE_REF, ARTIFACT_SOURCE_REF, "6,821", "5,108", "15,324",
                      "不可評估（非0）", "unresolved_anomaly_candidate", "sensitivity", "formal_use=False",
                      "trade_eligible=False", "promotion_evidence_allowed=False"):
            if token not in report:
                errors.append(f"report missing required factual boundary: {token}")
        blocks = re.findall(r"```json\s*([\s\S]*?)```", report)
        if len(blocks) != 1 or _unique_json(blocks[0]) != old_summary:
            errors.append("report changed or omitted accepted v2 primary summary baseline")
        for row in summary:
            if row["analysis_population"] == "primary" and row["slippage"] == "0.001":
                expected_line = "| D+{} | {} | {} | {} | {} | {} | {} | 不可評估（非0） |".format(
                    row["horizon"], row["event_count"], row["conflict_event_count"], row["immature_event_count"],
                    row["evidence_missing_event_count"], row["position_count"], row["realized_count"])
                if report.count(expected_line) != 1:
                    errors.append(f"report D{row['horizon']} table differs from verified summary")
        for old in baseline["observations"]:
            if old["observation_id"] not in report:
                errors.append(f"report omitted original anomaly observation {old['observation_id']}")
    except (KeyError, TypeError, ValueError, IndexError, csv.Error, InvalidOperation, subprocess.CalledProcessError) as exc:
        errors.append(f"malformed source or model artifact prevents independent validation: {type(exc).__name__}: {exc}")
    return errors


def validate(root: Path, source_ref: str = SOURCE_REF,
             artifact_source_ref: str = ARTIFACT_SOURCE_REF) -> list[str]:
    root = root.resolve()
    if source_ref != SOURCE_REF or artifact_source_ref != ARTIFACT_SOURCE_REF:
        return ["two immutable source roles must be supplied separately and exactly"]
    payloads: dict[str, bytes] = {}
    for name in ARTIFACT_SUFFIXES:
        path = root / DIRECTORY / (PREFIX + name)
        try:
            payloads[name] = path.read_bytes()
        except OSError as exc:
            return [f"required actual artifact missing/unreadable: {path}: {exc}"]
    return _validate_payloads(payloads, _Sources(root))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Independently validate TDCC stealth Scheme A operation replay v3.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ref", default=SOURCE_REF)
    parser.add_argument("--artifact-source-ref", default=ARTIFACT_SOURCE_REF)
    args = parser.parse_args(argv)
    errors = validate(args.repository_root, args.source_ref, args.artifact_source_ref)
    if errors:
        for error in errors[:100]:
            print("ERROR: " + error)
        if len(errors) > 100:
            print(f"additional_errors={len(errors) - 100}")
        return 1
    print("TDCC 潛伏吸籌 operation_replay_v3 independent validation passed: signals=6821 events=15324 observations=6")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
