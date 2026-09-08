from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable

try:
    from model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )
except ModuleNotFoundError:
    from scripts.model_research_artifact_guard import (
        load_ownership_rules,
        model_owned_artifact_guard,
        validate_changed_paths,
    )


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
OWNER_ID = "tdcc_stealth_accumulation_historical_selector_replay"
MODEL_NAME_ZH = "TDCC潛伏吸籌模型"
PRODUCER = "scripts/build_tdcc_stealth_accumulation_historical_replay.py"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_historical_selector_replay_v1"
REPLAY_KIND = "fixed_current_selector_historical_reconstruction_not_as_published"
SELECTOR_CONTRACT_VERSION = "current_selector_at_source_commit_v1"
HORIZONS = (5, 10, 20)
HIGH_RETURN_THRESHOLD_PCT = Decimal("10")
ANOMALY_ABS_RETURN_THRESHOLD_PCT = Decimal("80")

ARTIFACT_DIR = Path("output/research/tdcc_stealth_accumulation")
DETAIL_NAME = "tdcc_stealth_accumulation_historical_selector_replay_detail_v1.csv"
SUMMARY_NAME = "tdcc_stealth_accumulation_historical_selector_replay_summary_v1.csv"
REPORT_NAME = "tdcc_stealth_accumulation_historical_selector_replay_report_v1.md"
MANIFEST_PATH = "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv"
PRODUCTION_SOURCE_PATH = "scripts/build_daily_candidate_model_layer.py"
ALL_CANDIDATES_ARTIFACT_ID = "all_candidates_source_rows"
MODEL_SIGNALS_ARTIFACT_ID = "model_signals_for_report"

POSITIVE_TDCC = {"strong_accumulation", "mild_accumulation"}

DETAIL_FIELDS = [
    "artifact_version", "replay_kind", "model_id", "model_name_zh",
    "source_ref", "source_commit_sha", "source_commit_time", "production_source_path",
    "production_source_sha256", "selector_contract_version",
    "selector_contract_sha256", "snapshot_report_date", "snapshot_revision",
    "snapshot_path", "snapshot_sha256", "snapshot_row_number",
    "snapshot_row_sha256", "snapshot_generated_at", "snapshot_pipeline_commit_sha",
    "candidate_signal_date", "stock_id", "stock_name",
    "published_membership_status", "published_snapshot_path",
    "published_snapshot_sha256", "selector_input_present_count",
    "selector_input_missing_count", "selector_missing_inputs",
    "tdcc_price_phase", "tdcc_price_phase_source", "tdcc_status",
    "tdcc_status_source", "tdcc_accumulation_signal", "volume_ratio",
    "return_5d_pct", "return_20d_pct", "recent_range_high",
    "recent_range_low", "close", "phase_ok", "attack_already_started",
    "volume_below_2_5", "short_not_attacked", "not_rallied",
    "in_recent_range_10pct", "selector_selected", "overlap_with_prior_signal",
    "prior_same_stock_signal_date", "research_entry_basis", "entry_date",
    "entry_open_price", "entry_price_source_path", "entry_price_source_sha256",
    "entry_price_row_sha256", "exit_d5_date", "exit_d5_close_price",
    "exit_d5_price_source_path", "exit_d5_price_source_sha256",
    "exit_d5_price_row_sha256", "return_d5_pct", "exit_d10_date",
    "exit_d10_close_price", "exit_d10_price_source_path",
    "exit_d10_price_source_sha256", "exit_d10_price_row_sha256",
    "return_d10_pct", "exit_d20_date", "exit_d20_close_price",
    "exit_d20_price_source_path", "exit_d20_price_source_sha256",
    "exit_d20_price_row_sha256", "return_d20_pct", "forward_window_status",
    "right_censor_reason", "cost_basis", "price_adjustment_basis",
    "candidate_snapshot_pit_status", "outcome_price_lineage_status",
    "anomaly_candidate", "anomaly_trigger_codes", "anomaly_disposition",
    "retained_in_primary", "formal_use", "trade_eligible",
    "promotion_evidence_allowed", "promotion_status",
]

SUMMARY_FIELDS = [
    "artifact_version", "replay_kind", "model_id", "model_name_zh",
    "source_ref", "source_commit_sha", "source_commit_time", "production_source_sha256",
    "selector_contract_version", "selector_contract_sha256", "horizon",
    "entry_basis", "exit_basis", "cost_basis", "selected_snapshot_count",
    "snapshot_report_date_min", "snapshot_report_date_max", "candidate_row_count",
    "selector_selected_count", "published_membership_match_count",
    "overlap_signal_count", "evaluated_count", "right_censored_count",
    "invalid_price_count", "win_count", "neutral_count", "failure_count",
    "win_rate_pct", "neutral_rate_pct", "failure_rate_pct",
    "average_return_pct", "median_return_pct", "high_return_hit_count",
    "high_return_hit_rate_pct", "loss_count", "loss_rate_pct",
    "unresolved_anomaly_candidate_count", "primary_metric_basis",
    "sensitivity_analysis_basis", "sensitivity_is_corrected_primary",
    "sensitivity_evaluated_count", "sensitivity_excluded_anomaly_candidate_count",
    "sensitivity_win_rate_pct", "sensitivity_average_return_pct",
    "sensitivity_median_return_pct", "candidate_snapshot_pit_status",
    "outcome_price_lineage_status", "phase_classifier_status",
    "formal_use", "trade_eligible", "promotion_evidence_allowed",
    "promotion_status", "promotion_blockers", "detail_artifact_sha256",
]


def _text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\ufeff", "").strip()
    return "" if text.lower() in {"nan", "none", "nat", "<na>"} else text


def _number(value: Any) -> float:
    text = _text(value).replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    if text in {"", "-"}:
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


def _truthy(value: Any) -> bool:
    return _text(value).lower() in {"true", "1", "yes", "y", "t"}


def _row_text(row: dict[str, str], *names: str) -> tuple[str, str]:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            if candidate in row:
                value = _text(row.get(candidate))
                if value:
                    return value, candidate
    return "", ""


def _row_num(row: dict[str, str], *names: str) -> tuple[float, str]:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            if candidate in row:
                value = _number(row.get(candidate))
                if not math.isnan(value):
                    return value, candidate
    return math.nan, ""


def _flag(row: dict[str, str], name: str) -> bool:
    return _truthy(row.get(name, ""))


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_row_sha256(row: dict[str, Any]) -> str:
    payload = json.dumps(
        {str(key): _text(value) for key, value in row.items()},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return _sha256(payload)


def _hash_candidates(payload: bytes) -> set[str]:
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return {_sha256(payload), _sha256(lf), _sha256(lf.replace(b"\n", b"\r\n"))}


def _csv_rows(payload: bytes, source: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
        fields = list(reader.fieldnames or [])
        rows = [{str(k): _text(v) for k, v in row.items()} for row in reader]
    except (UnicodeDecodeError, csv.Error) as exc:
        raise RuntimeError(f"failed to read CSV {source}: {exc}") from exc
    if not fields:
        raise RuntimeError(f"CSV has no header: {source}")
    return fields, rows


class GitTree:
    def __init__(self, root: Path, source_ref: str) -> None:
        self.root = root.resolve()
        self.source_ref = source_ref
        self.commit_sha = self._run("rev-parse", "--verify", f"{source_ref}^{{commit}}").strip().lower()
        if re.fullmatch(r"[0-9a-f]{40}", self.commit_sha) is None:
            raise RuntimeError(f"invalid source commit: {self.commit_sha}")
        self.commit_time = self._run("show", "-s", "--format=%cI", self.commit_sha).strip()
        self._entries: dict[str, str] | None = None

    def _run(self, *args: str, binary: bool = False) -> Any:
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True,
            text=not binary, encoding=None if binary else "utf-8",
        ).stdout

    def entries(self) -> dict[str, str]:
        if self._entries is None:
            listing = self._run("ls-tree", "-r", "--full-tree", self.commit_sha)
            entries: dict[str, str] = {}
            for line in listing.splitlines():
                if "\t" not in line:
                    continue
                meta, path = line.split("\t", 1)
                parts = meta.split()
                if len(parts) == 3 and parts[1] == "blob":
                    entries[path.replace("\\", "/")] = parts[2]
            self._entries = entries
        return self._entries

    def read(self, path: str) -> bytes:
        normalized = path.replace("\\", "/").lstrip("./")
        if normalized not in self.entries():
            raise RuntimeError(f"source path missing from {self.commit_sha}: {normalized}")
        return self._run("cat-file", "blob", self.entries()[normalized], binary=True)

    def list_paths(self, prefix: str, name_pattern: re.Pattern[str]) -> list[str]:
        prefix = prefix.rstrip("/") + "/"
        return sorted(path for path in self.entries() if path.startswith(prefix) and name_pattern.fullmatch(Path(path).name))


def _revision_number(value: str) -> int:
    match = re.fullmatch(r"r([0-9]+)", _text(value).lower())
    if not match:
        raise RuntimeError(f"invalid snapshot revision: {value!r}")
    return int(match.group(1))


def _selected_manifest_rows(rows: list[dict[str, str]], artifact_id: str) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("artifact_id") == artifact_id:
            date = row.get("snapshot_report_date", "")
            if re.fullmatch(r"20[0-9]{6}", date) is None:
                raise RuntimeError(f"invalid snapshot report date: {date!r}")
            grouped[date].append(row)
    selected: list[dict[str, str]] = []
    for date, candidates in sorted(grouped.items()):
        selected.append(max(candidates, key=lambda row: _revision_number(row.get("snapshot_revision", ""))))
    if not selected:
        raise RuntimeError(f"no selected manifest rows for artifact_id={artifact_id}")
    return selected


def _volume_ma20_lots(row: dict[str, str]) -> float:
    value, _ = _row_num(row, "volume_ma20_lots", "avg_volume_20d_lots")
    if not math.isnan(value):
        return value
    value, _ = _row_num(row, "volume_ma20", "avg_volume_20d")
    if math.isnan(value):
        return math.nan
    return value / 1000.0 if value >= 100000 else value


def _previous_close(row: dict[str, str]) -> float:
    return _row_num(row, "previous_close", "prev_close", "close_prev", "close_1d_ago")[0]


def _breakout_level(row: dict[str, str]) -> float:
    value, _ = _row_num(row, "previous_20d_high_ex_today", "prior_20d_high", "previous_20d_high", "high_20_ex_today")
    today_high, _ = _row_num(row, "high")
    close, _ = _row_num(row, "close")
    if not any(math.isnan(v) for v in (value, today_high, close)):
        platform_high, _ = _row_num(row, "platform_high", "short_platform_high", "range_high")
        if value >= today_high * 0.999 and not math.isnan(platform_high) and platform_high < value:
            return platform_high
    return value


def _bottom_volume_attack_like(row: dict[str, str]) -> bool:
    close, _ = _row_num(row, "close")
    open_, _ = _row_num(row, "open")
    high, _ = _row_num(row, "high")
    low, _ = _row_num(row, "low")
    vol, _ = _row_num(row, "volume_ratio")
    ma20 = _volume_ma20_lots(row)
    level = _breakout_level(row)
    prev_close = _previous_close(row)
    bullish = (
        not math.isnan(close) and not math.isnan(open_)
        and (close > open_ or (close == open_ and not math.isnan(prev_close) and close > prev_close))
    )
    normal = (
        not any(math.isnan(v) for v in (vol, ma20, level, close))
        and close >= level * 1.02 and vol >= 2.0 and ma20 >= 1000 and bullish
    )
    ret, _ = _row_num(row, "daily_return_calc", "return_1d", "return_1d_pct")
    if math.isnan(ret) and not math.isnan(close) and not math.isnan(prev_close) and prev_close > 0:
        ret = (close / prev_close - 1) * 100
    locked = False
    if not any(math.isnan(v) for v in (close, open_, high, low, level, ret)):
        one_price = high == low
        range_pct = math.nan if one_price or math.isnan(prev_close) or prev_close <= 0 else (high - low) / prev_close * 100
        tight = one_price or (not math.isnan(range_pct) and range_pct <= 1.0)
        locked = close >= level * 1.02 and ret >= 9.0 and close >= high * 0.995 and open_ >= close * 0.995 and tight
    return normal or locked


def evaluate_selector(row: dict[str, str]) -> dict[str, Any]:
    phase, phase_source = _row_text(row, "tdcc_price_phase")
    phase = phase.lower()
    tdcc_status, tdcc_status_source = _row_text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge")
    tdcc_status = tdcc_status.lower()
    vol, _ = _row_num(row, "volume_ratio")
    ret5, _ = _row_num(row, "return_5d", "return_5d_pct")
    ret20, _ = _row_num(row, "return_20d", "return_20d_pct")
    close, _ = _row_num(row, "close")
    recent_high, _ = _row_num(row, "high_20", "previous_20d_high", "platform_high")
    recent_low, _ = _row_num(row, "low_20", "previous_20d_low", "platform_low")
    attack = _bottom_volume_attack_like(row) or _flag(row, "volume_confirmed_breakout")
    phase_ok = phase == "tdcc_leading_price" or (
        not phase and (tdcc_status in POSITIVE_TDCC or _flag(row, "tdcc_accumulation_signal"))
    )
    phase_forbidden = phase in {"price_leading_tdcc", "overheated_after_tdcc"}
    volume_ok = math.isnan(vol) or vol < 2.5
    short_ok = math.isnan(ret5) or ret5 < 8
    not_rallied = math.isnan(ret20) or ret20 < 20
    in_range = (
        not any(math.isnan(v) for v in (close, recent_high, recent_low))
        and recent_high > recent_low
        and recent_low * 0.9 <= close <= recent_high * 1.1
    )
    selected = not phase_forbidden and not attack and volume_ok and phase_ok and short_ok and not_rallied and in_range
    return {
        "tdcc_price_phase": phase, "tdcc_price_phase_source": phase_source,
        "tdcc_status": tdcc_status, "tdcc_status_source": tdcc_status_source,
        "tdcc_accumulation_signal": str(_flag(row, "tdcc_accumulation_signal")),
        "volume_ratio": vol, "return_5d_pct": ret5, "return_20d_pct": ret20,
        "recent_range_high": recent_high, "recent_range_low": recent_low, "close": close,
        "phase_ok": phase_ok and not phase_forbidden, "attack_already_started": attack,
        "volume_below_2_5": volume_ok, "short_not_attacked": short_ok,
        "not_rallied": not_rallied, "in_recent_range_10pct": in_range,
        "selector_selected": selected,
    }


SELECTOR_INPUT_NAMES = (
    "tdcc_price_phase", "tdcc_status", "tdcc_judgement", "tdcc_judge",
    "tdcc_accumulation_signal", "volume_ratio", "return_5d", "return_5d_pct",
    "return_20d", "return_20d_pct", "close", "high_20", "previous_20d_high",
    "platform_high", "low_20", "previous_20d_low", "platform_low",
    "volume_confirmed_breakout", "volume_ma20_lots", "avg_volume_20d_lots",
    "volume_ma20", "avg_volume_20d", "previous_20d_high_ex_today",
    "prior_20d_high", "high_20_ex_today", "short_platform_high", "range_high",
    "open", "high", "low", "previous_close", "prev_close", "close_prev",
    "close_1d_ago", "daily_return_calc", "return_1d", "return_1d_pct",
)


def _selector_contract_sha256() -> str:
    contract = {
        "version": SELECTOR_CONTRACT_VERSION,
        "positive_tdcc": sorted(POSITIVE_TDCC),
        "input_names": SELECTOR_INPUT_NAMES,
        "rule": "production_cond_tdcc_stealth_and_transitive_helpers_exact_at_source_commit",
    }
    return _sha256(json.dumps(contract, sort_keys=True, separators=(",", ":")).encode("utf-8"))


@dataclass(frozen=True)
class PriceRow:
    date: str
    stock_id: str
    open_price: Decimal
    close_price: Decimal
    path: str
    source_sha256: str
    row_sha256: str


def _decimal(value: str) -> Decimal | None:
    try:
        result = Decimal(_text(value).replace(",", ""))
    except InvalidOperation:
        return None
    return result if result.is_finite() and result > 0 else None


def _load_prices(tree: GitTree, min_date: str) -> dict[str, list[PriceRow]]:
    paths = tree.list_paths("data/daily_price", re.compile(r"20[0-9]{6}\.csv"))
    by_stock: dict[str, list[PriceRow]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for path in paths:
        date_from_path = Path(path).stem
        if date_from_path < min_date:
            continue
        payload = tree.read(path)
        source_sha = _sha256(payload)
        _, rows = _csv_rows(payload, path)
        for row in rows:
            date = _text(row.get("date")) or date_from_path
            stock_id = _text(row.get("stock_id") or row.get("ticker") or row.get("code"))
            if not re.fullmatch(r"[0-9]{4,6}", stock_id) or date != date_from_path:
                continue
            open_price = _decimal(row.get("open", ""))
            close_price = _decimal(row.get("close", ""))
            if open_price is None or close_price is None:
                continue
            identity = (date, stock_id)
            if identity in seen:
                raise RuntimeError(f"duplicate daily price identity: {date}|{stock_id}")
            seen.add(identity)
            by_stock[stock_id].append(PriceRow(date, stock_id, open_price, close_price, path, source_sha, _canonical_row_sha256(row)))
    for rows in by_stock.values():
        rows.sort(key=lambda row: row.date)
    return by_stock


def _fmt_number(value: Any) -> str:
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, float):
        return "" if math.isnan(value) else format(value, ".10g")
    if isinstance(value, Decimal):
        return format(value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP), "f")
    return _text(value)


def _return_pct(exit_price: Decimal, entry_price: Decimal) -> Decimal:
    return ((exit_price / entry_price) - Decimal("1")) * Decimal("100")


def _csv_bytes(rows: Iterable[dict[str, str]], fields: list[str]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def _rates(values: list[Decimal]) -> dict[str, str]:
    n = len(values)
    wins = sum(value > 0 for value in values)
    neutral = sum(value == 0 for value in values)
    failures = sum(value < 0 for value in values)
    high = sum(value >= HIGH_RETURN_THRESHOLD_PCT for value in values)
    def rate(count: int) -> str:
        return "" if not n else _fmt_number(Decimal(count) * Decimal("100") / Decimal(n))
    return {
        "win_count": str(wins), "neutral_count": str(neutral), "failure_count": str(failures),
        "win_rate_pct": rate(wins), "neutral_rate_pct": rate(neutral), "failure_rate_pct": rate(failures),
        "average_return_pct": "" if not n else _fmt_number(sum(values) / Decimal(n)),
        "median_return_pct": "" if not n else _fmt_number(Decimal(str(statistics.median(values)))),
        "high_return_hit_count": str(high), "high_return_hit_rate_pct": rate(high),
        "loss_count": str(failures), "loss_rate_pct": rate(failures),
    }


def build(*, root: Path, source_ref: str) -> tuple[list[dict[str, str]], list[dict[str, str]], str]:
    tree = GitTree(root, source_ref)
    production_payload = tree.read(PRODUCTION_SOURCE_PATH)
    manifest_payload = tree.read(MANIFEST_PATH)
    _, manifest_rows = _csv_rows(manifest_payload, MANIFEST_PATH)
    candidate_manifest = _selected_manifest_rows(manifest_rows, ALL_CANDIDATES_ARTIFACT_ID)
    published_manifest = {row["snapshot_report_date"]: row for row in _selected_manifest_rows(manifest_rows, MODEL_SIGNALS_ARTIFACT_ID)}
    price_by_stock = _load_prices(tree, candidate_manifest[0]["snapshot_report_date"])
    selector_sha = _selector_contract_sha256()

    published_membership: dict[str, tuple[str, str, set[str]]] = {}
    for date, row in published_manifest.items():
        payload = tree.read(row["snapshot_path"])
        if row["snapshot_sha256"].lower() not in _hash_candidates(payload):
            raise RuntimeError(f"published snapshot hash mismatch: {row['snapshot_path']}")
        _, signal_rows = _csv_rows(payload, row["snapshot_path"])
        ids = {
            _text(signal.get("stock_id")) for signal in signal_rows
            if _text(signal.get("model_id")) == MODEL_ID
        }
        published_membership[date] = (row["snapshot_path"], row["snapshot_sha256"].lower(), ids)

    detail: list[dict[str, str]] = []
    total_candidate_rows = 0
    funnel_order = (
        "phase_not_forbidden",
        "attack_not_started",
        "volume_below_2_5",
        "phase_or_blank_positive_fallback",
        "return_5d_below_8",
        "return_20d_below_20",
        "inside_recent_range_10pct",
    )
    funnel_counts = {name: 0 for name in funnel_order}
    diagnostic_population = 0
    phase_presence: Counter[str] = Counter()
    phase_values: Counter[str] = Counter()
    status_presence: Counter[str] = Counter()
    status_values: Counter[str] = Counter()
    accumulation_presence: Counter[str] = Counter()
    accumulation_values: Counter[str] = Counter()
    last_signal_by_stock: dict[str, str] = {}
    for manifest_row in candidate_manifest:
        path = manifest_row["snapshot_path"]
        payload = tree.read(path)
        if manifest_row["snapshot_sha256"].lower() not in _hash_candidates(payload):
            raise RuntimeError(f"candidate snapshot hash mismatch: {path}")
        fields, candidates = _csv_rows(payload, path)
        total_candidate_rows += len(candidates)
        field_set = set(fields)
        present = sorted(name for name in SELECTOR_INPUT_NAMES if any(candidate in field_set for candidate in (name, f"{name}_x", f"{name}_y")))
        missing = sorted(set(SELECTOR_INPUT_NAMES) - set(present))
        report_date = manifest_row["snapshot_report_date"]
        published_path, published_sha, published_ids = published_membership.get(report_date, ("", "", set()))
        for row_number, candidate in enumerate(candidates, start=2):
            evaluation = evaluate_selector(candidate)
            cumulative_checks = (
                evaluation["tdcc_price_phase"] not in {"price_leading_tdcc", "overheated_after_tdcc"},
                not evaluation["attack_already_started"],
                evaluation["volume_below_2_5"],
                evaluation["phase_ok"],
                evaluation["short_not_attacked"],
                evaluation["not_rallied"],
                evaluation["in_recent_range_10pct"],
            )
            still_eligible = True
            for name, passed in zip(funnel_order, cumulative_checks, strict=True):
                still_eligible = still_eligible and passed
                if still_eligible:
                    funnel_counts[name] += 1
            if all(cumulative_checks[:3]):
                diagnostic_population += 1
                phase_keys = tuple(
                    key for key in ("tdcc_price_phase", "tdcc_price_phase_x", "tdcc_price_phase_y")
                    if key in candidate
                )
                phase_presence[
                    "missing" if not phase_keys else ("blank" if not evaluation["tdcc_price_phase"] else "nonblank")
                ] += 1
                phase_values[evaluation["tdcc_price_phase"] or "<blank>"] += 1
                status_keys = tuple(
                    f"{base}{suffix}"
                    for base in ("tdcc_status", "tdcc_judgement", "tdcc_judge")
                    for suffix in ("", "_x", "_y")
                    if f"{base}{suffix}" in candidate
                )
                status_presence[
                    "missing" if not status_keys else ("blank" if not evaluation["tdcc_status"] else "nonblank")
                ] += 1
                status_values[evaluation["tdcc_status"] or "<blank>"] += 1
                raw_accumulation = _text(candidate.get("tdcc_accumulation_signal"))
                accumulation_presence[
                    "missing" if "tdcc_accumulation_signal" not in candidate else ("blank" if not raw_accumulation else "nonblank")
                ] += 1
                accumulation_values[raw_accumulation or "<blank>"] += 1
            if not evaluation["selector_selected"]:
                continue
            stock_id = _text(candidate.get("stock_id") or candidate.get("ticker"))
            signal_date = _text(candidate.get("signal_date") or candidate.get("date") or report_date)
            if not re.fullmatch(r"[0-9]{4,6}", stock_id):
                raise RuntimeError(f"selected candidate has invalid stock_id: {stock_id!r}")
            if signal_date != report_date:
                raise RuntimeError(f"selected candidate date mismatch: {path} row {row_number}")
            prior_signal = last_signal_by_stock.get(stock_id, "")
            prices = [row for row in price_by_stock.get(stock_id, []) if row.date > signal_date]
            entry = prices[0] if prices else None
            result: dict[str, str] = {
                "artifact_version": ARTIFACT_VERSION, "replay_kind": REPLAY_KIND,
                "model_id": MODEL_ID, "model_name_zh": MODEL_NAME_ZH,
                "source_ref": source_ref, "source_commit_sha": tree.commit_sha,
                "source_commit_time": tree.commit_time,
                "production_source_path": PRODUCTION_SOURCE_PATH,
                "production_source_sha256": _sha256(production_payload),
                "selector_contract_version": SELECTOR_CONTRACT_VERSION,
                "selector_contract_sha256": selector_sha,
                "snapshot_report_date": report_date,
                "snapshot_revision": manifest_row["snapshot_revision"],
                "snapshot_path": path, "snapshot_sha256": manifest_row["snapshot_sha256"].lower(),
                "snapshot_row_number": str(row_number), "snapshot_row_sha256": _canonical_row_sha256(candidate),
                "snapshot_generated_at": manifest_row.get("generated_at", ""),
                "snapshot_pipeline_commit_sha": manifest_row.get("pipeline_commit_sha", ""),
                "candidate_signal_date": signal_date, "stock_id": stock_id,
                "stock_name": _text(candidate.get("stock_name") or candidate.get("name")),
                "published_membership_status": "matched_actual_published_recommendation" if stock_id in published_ids else "not_found_in_actual_published_recommendations",
                "published_snapshot_path": published_path, "published_snapshot_sha256": published_sha,
                "selector_input_present_count": str(len(present)), "selector_input_missing_count": str(len(missing)),
                "selector_missing_inputs": ";".join(missing),
                "overlap_with_prior_signal": str(bool(prior_signal)),
                "prior_same_stock_signal_date": prior_signal,
                "research_entry_basis": "signal_close_confirmed_next_available_trading_day_open",
                "cost_basis": "gross_before_fees_taxes_and_slippage",
                "price_adjustment_basis": "date_snapshot_source_basis_unverified_for_corporate_actions",
                "candidate_snapshot_pit_status": "immutable_commit_bound_snapshot_generated_at_recorded_not_complete_event_time_PIT_proof",
                "outcome_price_lineage_status": "immutable_source_commit_bound_date_files_adjustment_basis_unverified",
                "formal_use": "False", "trade_eligible": "False",
                "promotion_evidence_allowed": "False", "promotion_status": "research_only_blocked",
                "anomaly_candidate": "False", "anomaly_trigger_codes": "",
                "anomaly_disposition": "not_triggered", "retained_in_primary": "True",
            }
            for key, value in evaluation.items():
                result[key] = _fmt_number(value)
            if entry is None:
                result["forward_window_status"] = "right_censored_no_next_trading_day_open"
                result["right_censor_reason"] = "source_commit_has_no_later_valid_price_row"
            else:
                result.update({
                    "entry_date": entry.date, "entry_open_price": _fmt_number(entry.open_price),
                    "entry_price_source_path": entry.path, "entry_price_source_sha256": entry.source_sha256,
                    "entry_price_row_sha256": entry.row_sha256,
                })
                complete = True
                anomaly_codes: list[str] = []
                for horizon in HORIZONS:
                    key = f"d{horizon}"
                    if len(prices) <= horizon:
                        complete = False
                        continue
                    exit_row = prices[horizon]
                    return_value = _return_pct(exit_row.close_price, entry.open_price)
                    result.update({
                        f"exit_{key}_date": exit_row.date,
                        f"exit_{key}_close_price": _fmt_number(exit_row.close_price),
                        f"exit_{key}_price_source_path": exit_row.path,
                        f"exit_{key}_price_source_sha256": exit_row.source_sha256,
                        f"exit_{key}_price_row_sha256": exit_row.row_sha256,
                        f"return_{key}_pct": _fmt_number(return_value),
                    })
                    if abs(return_value) >= ANOMALY_ABS_RETURN_THRESHOLD_PCT:
                        anomaly_codes.append(f"abs_return_{key}_ge_80pct")
                result["forward_window_status"] = "complete_d5_d10_d20" if complete else "partial_right_censored"
                result["right_censor_reason"] = "" if complete else "source_commit_has_insufficient_later_trading_rows"
                if anomaly_codes:
                    result["anomaly_candidate"] = "True"
                    result["anomaly_trigger_codes"] = ";".join(anomaly_codes)
                    result["anomaly_disposition"] = "unresolved_anomaly_candidate"
            detail.append({field: _text(result.get(field, "")) for field in DETAIL_FIELDS})
            last_signal_by_stock[stock_id] = signal_date

    detail_payload = _csv_bytes(detail, DETAIL_FIELDS)
    detail_sha = _sha256(detail_payload)
    dates = [row["snapshot_report_date"] for row in candidate_manifest]
    summary: list[dict[str, str]] = []
    blockers = (
        "not_as_published_reconstruction;incomplete_event_time_PIT_proof;"
        "price_adjustment_basis_unverified;formal_operation_rules_undecided"
    )
    for horizon in HORIZONS:
        return_key = f"return_d{horizon}_pct"
        values = [Decimal(row[return_key]) for row in detail if row[return_key]]
        anomalies = [row for row in detail if row[return_key] and row["anomaly_candidate"] == "True"]
        sensitivity = [Decimal(row[return_key]) for row in detail if row[return_key] and row["anomaly_candidate"] != "True"]
        metrics = _rates(values)
        sensitivity_metrics = _rates(sensitivity)
        row = {
            "artifact_version": ARTIFACT_VERSION, "replay_kind": REPLAY_KIND,
            "model_id": MODEL_ID, "model_name_zh": MODEL_NAME_ZH,
            "source_ref": source_ref, "source_commit_sha": tree.commit_sha,
            "source_commit_time": tree.commit_time,
            "production_source_sha256": _sha256(production_payload),
            "selector_contract_version": SELECTOR_CONTRACT_VERSION,
            "selector_contract_sha256": selector_sha, "horizon": f"D{horizon}",
            "entry_basis": "signal_close_confirmed_next_available_trading_day_open",
            "exit_basis": f"fixed_future_D{horizon}_close_research_only",
            "cost_basis": "gross_before_fees_taxes_and_slippage",
            "selected_snapshot_count": str(len(candidate_manifest)),
            "snapshot_report_date_min": min(dates), "snapshot_report_date_max": max(dates),
            "candidate_row_count": str(total_candidate_rows), "selector_selected_count": str(len(detail)),
            "published_membership_match_count": str(sum(row["published_membership_status"] == "matched_actual_published_recommendation" for row in detail)),
            "overlap_signal_count": str(sum(row["overlap_with_prior_signal"] == "True" for row in detail)),
            "evaluated_count": str(len(values)), "right_censored_count": str(len(detail) - len(values)),
            "invalid_price_count": "0", **metrics,
            "unresolved_anomaly_candidate_count": str(len(anomalies)),
            "primary_metric_basis": "all_selected_rows_including_overlaps_and_unresolved_anomaly_candidates",
            "sensitivity_analysis_basis": "excluding_unresolved_anomaly_candidates_only",
            "sensitivity_is_corrected_primary": "False",
            "sensitivity_evaluated_count": str(len(sensitivity)),
            "sensitivity_excluded_anomaly_candidate_count": str(len(values) - len(sensitivity)),
            "sensitivity_win_rate_pct": sensitivity_metrics["win_rate_pct"],
            "sensitivity_average_return_pct": sensitivity_metrics["average_return_pct"],
            "sensitivity_median_return_pct": sensitivity_metrics["median_return_pct"],
            "candidate_snapshot_pit_status": "immutable_commit_bound_snapshot_generated_at_recorded_not_complete_event_time_PIT_proof",
            "outcome_price_lineage_status": "immutable_source_commit_bound_date_files_adjustment_basis_unverified",
            "phase_classifier_status": "not_invoked_current_blank_phase_fallback_preserved",
            "formal_use": "False", "trade_eligible": "False", "promotion_evidence_allowed": "False",
            "promotion_status": "research_only_blocked", "promotion_blockers": blockers,
            "detail_artifact_sha256": detail_sha,
        }
        summary.append({field: _text(row.get(field, "")) for field in SUMMARY_FIELDS})
    report_lines = [
        "# TDCC潛伏吸籌模型 historical selector research replay v1",
        "",
        "## 結論",
        "",
        f"本報告是固定 `{tree.commit_sha}` 現行 selector 套用歷史候選快照的研究重建，不是當時實際發布推薦。共讀取 {len(candidate_manifest)} 個 immutable commit-bound 候選快照、{total_candidate_rows} 列候選，重建選出 {len(detail)} 列；其中與實際發布的 `{MODEL_ID}` 推薦相符 {sum(row['published_membership_status'] == 'matched_actual_published_recommendation' for row in detail)} 列。",
        "",
        "## 研究績效（未扣交易成本）",
        "",
        "| 持有窗 | 可評估 | 右設限 | 勝 / 平 / 敗 | 勝率 | 平均報酬 | 中位報酬 | 高報酬命中 | 未解異常候選 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summary:
        report_lines.append(
            f"| {row['horizon']} | {row['evaluated_count']} | {row['right_censored_count']} | {row['win_count']} / {row['neutral_count']} / {row['failure_count']} | {row['win_rate_pct'] or '—'}% | {row['average_return_pct'] or '—'}% | {row['median_return_pct'] or '—'}% | {row['high_return_hit_count']} | {row['unresolved_anomaly_candidate_count']} |"
        )
    report_lines += [
        "", "## 既有條件逐步診斷", "",
        "以下依 `cond_tdcc_stealth()` 的實際短路順序統計；首次拒絕數是上一關剩餘數減本關剩餘數，未新增任何條件。",
        "", "| 既有判斷步驟 | 通過後剩餘 | 本步首次拒絕 |",
        "|---|---:|---:|",
    ]
    previous = total_candidate_rows
    funnel_labels = {
        "phase_not_forbidden": "排除 `price_leading_tdcc` / `overheated_after_tdcc` phase",
        "attack_not_started": "排除既有 attack-already-started（含 `volume_confirmed_breakout`）",
        "volume_below_2_5": "量比空白或 `<2.5`",
        "phase_or_blank_positive_fallback": "`tdcc_leading_price` 或空白 phase + `tdcc_positive` fallback",
        "return_5d_below_8": "5日報酬空白或 `<8%`",
        "return_20d_below_20": "20日報酬空白或 `<20%`",
        "inside_recent_range_10pct": "收盤位於近20日區間上下 10% 容許帶",
    }
    for name in funnel_order:
        remaining = funnel_counts[name]
        report_lines.append(f"| {funnel_labels[name]} | {remaining} | {previous - remaining} |")
        previous = remaining
    report_lines += [
        "", "## 零樣本資料契約診斷", "",
        f"在通過 attack 與量比後的 {diagnostic_population} 列中，`tdcc_price_phase` 欄位 missing / blank / nonblank = {phase_presence['missing']} / {phase_presence['blank']} / {phase_presence['nonblank']}；實際選值分布為 "
        + "、".join(f"`{key}` {value}" for key, value in sorted(phase_values.items())) + "。",
        f"`tdcc_status` / `tdcc_judgement` / `tdcc_judge` alias 組合 missing / blank / nonblank = {status_presence['missing']} / {status_presence['blank']} / {status_presence['nonblank']}；實際選值分布為 "
        + "、".join(f"`{key}` {value}" for key, value in sorted(status_values.items())) + "。",
        f"`tdcc_accumulation_signal` missing / blank / nonblank = {accumulation_presence['missing']} / {accumulation_presence['blank']} / {accumulation_presence['nonblank']}；原始值分布為 "
        + "、".join(f"`{key}` {value}" for key, value in sorted(accumulation_values.items())) + "。",
        f"其中 `mild_accumulation` + `strong_accumulation` 共 {accumulation_values['mild_accumulation'] + accumulation_values['strong_accumulation']} 列，但 source commit 的 `tdcc_positive()` 對此欄位套用 boolean `flag()`，只接受 `true/1/yes/y/t`。因此 current-rule replay 必須維持 0 命中；這是歷史 snapshot 與 current selector 的欄位語意不相容，不能解讀為真實沒有正向 TDCC 狀態，也不能在本研究中擅自 reinterpret enum。",
        "", "## 口徑與限制", "",
        "- 入場：訊號日收盤確認後，下一個有該股票有效價格列的交易日開盤。",
        "- 出場：D5、D10、D20 固定未來收盤，只是研究比較窗，不是正式操作契約。",
        "- 成本：報酬為未扣手續費、交易稅與滑價的 gross return。",
        "- 同股重疊：全部保留於 primary metrics，並在 detail 標記。",
        "- 異常：數值觸發只標記 `unresolved_anomaly_candidate`，仍保留於 primary；排除後僅為 sensitivity，不能稱為修正績效。",
        "- PIT：候選與價格檔均綁定 source commit 與 SHA-256，但 snapshot `generated_at` 不是完整 event-time filed-at 證明；價格調整／公司行動基礎尚未權威核實。",
        "- phase：不呼叫任何共用 `classify_tdcc_price_phase()`；完整保留現行空白 `tdcc_price_phase` 加 `tdcc_positive` fallback。",
        "- 正式界線：`formal_use=False`、`trade_eligible=False`、`promotion_evidence_allowed=False`。",
        "", "## 來源綁定", "",
        f"- source ref: `{source_ref}`",
        f"- source commit: `{tree.commit_sha}`",
        f"- source commit time: `{tree.commit_time}`",
        f"- production source SHA-256: `{_sha256(production_payload)}`",
        f"- selector contract SHA-256: `{selector_sha}`",
        f"- detail SHA-256: `{detail_sha}`",
        "",
    ]
    return detail, summary, "\n".join(report_lines)


def _write_outputs(root: Path, detail: list[dict[str, str]], summary: list[dict[str, str]], report: str) -> None:
    output_dir = root / ARTIFACT_DIR
    paths = {DETAIL_NAME: DETAIL_FIELDS, SUMMARY_NAME: SUMMARY_FIELDS}
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, fields in paths.items():
        rows = detail if name == DETAIL_NAME else summary
        (output_dir / name).write_bytes(_csv_bytes(rows, fields))
    (output_dir / REPORT_NAME).write_text(report, encoding="utf-8", newline="\n")


def _status_snapshot(root: Path) -> dict[str, str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"], cwd=root,
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    snapshot: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        relative = line[3:].strip().strip('"').replace("\\", "/")
        if " -> " in relative:
            relative = relative.split(" -> ", 1)[1]
        path = root / relative
        snapshot[relative] = _sha256(path.read_bytes()) if path.is_file() else "__missing__"
    return snapshot


@contextmanager
def _sparse_model_owned_artifact_guard(root: Path):
    sparse = subprocess.run(
        ["git", "config", "--bool", "core.sparseCheckout"], cwd=root,
        check=False, capture_output=True, text=True, encoding="utf-8",
    ).stdout.strip().lower() == "true"
    if not sparse:
        raise RuntimeError("sparse guard is forbidden outside a Git sparse checkout")
    before = _status_snapshot(root)
    yield
    after = _status_snapshot(root)
    changed = sorted(path for path in set(before) | set(after) if before.get(path, "__clean__") != after.get(path, "__clean__"))
    rules = load_ownership_rules(root / "config/model_research_artifact_ownership.csv")
    errors = validate_changed_paths(OWNER_ID, PRODUCER, changed, rules)
    if errors:
        raise RuntimeError("sparse model-owned artifact guard failed:\n" + "\n".join(f"- {error}" for error in errors))
    print(f"sparse model-owned artifact guard passed owner={OWNER_ID} changed_paths={len(changed)}")


def _artifact_guard(root: Path):
    sparse = subprocess.run(
        ["git", "config", "--bool", "core.sparseCheckout"], cwd=root,
        check=False, capture_output=True, text=True, encoding="utf-8",
    ).stdout.strip().lower() == "true"
    if sparse:
        return _sparse_model_owned_artifact_guard(root)
    return model_owned_artifact_guard(
        OWNER_ID,
        PRODUCER,
        root=root,
        registry_path=root / "config/model_research_artifact_ownership.csv",
        sentinel_registry_path=root / "config/model_research_protected_sentinels.csv",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build research-only current-selector historical replay for tdcc_stealth_accumulation.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ref", default="HEAD")
    args = parser.parse_args(argv)
    root = args.repository_root.resolve()
    detail, summary, report = build(root=root, source_ref=args.source_ref)
    with _artifact_guard(root):
        _write_outputs(root, detail, summary, report)
    print(f"tdcc_stealth_historical_replay_detail_rows={len(detail)}")
    print(f"tdcc_stealth_historical_replay_summary_rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
