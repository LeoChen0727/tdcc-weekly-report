from __future__ import annotations

import ast
import csv
import hashlib
import io
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
VERSION = "tdcc_stealth_accumulation_historical_selector_replay_v1"
REPLAY_KIND = "fixed_current_selector_historical_reconstruction_not_as_published"
OUTPUT_DIR = ROOT / "output/research/tdcc_stealth_accumulation"
DETAIL = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_replay_detail_v1.csv"
SUMMARY = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_replay_summary_v1.csv"
REPORT = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_replay_report_v1.md"
MANIFEST_PATH = "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv"
PRODUCTION_SOURCE = "scripts/build_daily_candidate_model_layer.py"
HORIZONS = (5, 10, 20)
POSITIVE_TDCC = {"strong_accumulation", "mild_accumulation"}


def text(value: Any) -> str:
    if value is None:
        return ""
    result = str(value).replace("\ufeff", "").strip()
    return "" if result.lower() in {"nan", "none", "nat", "<na>"} else result


def number(value: Any) -> float:
    raw = text(value).replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    if raw in {"", "-"}:
        return math.nan
    try:
        return float(raw)
    except ValueError:
        return math.nan


def row_text(row: dict[str, str], *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            value = text(row.get(candidate, ""))
            if value:
                return value
    return ""


def row_num(row: dict[str, str], *names: str) -> float:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            value = number(row.get(candidate, ""))
            if not math.isnan(value):
                return value
    return math.nan


def flag(row: dict[str, str], name: str) -> bool:
    return text(row.get(name, "")).lower() in {"true", "1", "yes", "y", "t"}


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def row_sha(row: dict[str, str]) -> str:
    payload = json.dumps(
        {str(key): text(value) for key, value in row.items()},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"),
    ).encode("utf-8")
    return sha256(payload)


def csv_rows(payload: bytes) -> tuple[list[str], list[dict[str, str]]]:
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    fields = list(reader.fieldnames or [])
    if not fields:
        raise RuntimeError("CSV has no header")
    return fields, [{str(k): text(v) for k, v in row.items()} for row in reader]


class Tree:
    def __init__(self, commit: str) -> None:
        if re.fullmatch(r"[0-9a-f]{40}", commit) is None:
            raise RuntimeError(f"invalid source commit: {commit}")
        self.commit = commit
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--full-tree", commit], cwd=ROOT,
            check=True, capture_output=True, text=True, encoding="utf-8",
        )
        self.entries: dict[str, str] = {}
        for line in result.stdout.splitlines():
            if "\t" not in line:
                continue
            meta, path = line.split("\t", 1)
            parts = meta.split()
            if len(parts) == 3 and parts[1] == "blob":
                self.entries[path] = parts[2]

    def read(self, path: str) -> bytes:
        oid = self.entries.get(path)
        if not oid:
            raise RuntimeError(f"missing source path at {self.commit}: {path}")
        return subprocess.run(
            ["git", "cat-file", "blob", oid], cwd=ROOT, check=True, capture_output=True,
        ).stdout


def previous_close(row: dict[str, str]) -> float:
    return row_num(row, "previous_close", "prev_close", "close_prev", "close_1d_ago")


def breakout_level(row: dict[str, str]) -> float:
    value = row_num(row, "previous_20d_high_ex_today", "prior_20d_high", "previous_20d_high", "high_20_ex_today")
    high = row_num(row, "high")
    close = row_num(row, "close")
    platform = row_num(row, "platform_high", "short_platform_high", "range_high")
    if not any(math.isnan(v) for v in (value, high, close, platform)) and value >= high * 0.999 and platform < value:
        return platform
    return value


def volume_ma20_lots(row: dict[str, str]) -> float:
    value = row_num(row, "volume_ma20_lots", "avg_volume_20d_lots")
    if not math.isnan(value):
        return value
    value = row_num(row, "volume_ma20", "avg_volume_20d")
    return value / 1000 if not math.isnan(value) and value >= 100000 else value


def attack_started(row: dict[str, str]) -> bool:
    close = row_num(row, "close")
    open_ = row_num(row, "open")
    high = row_num(row, "high")
    low = row_num(row, "low")
    previous = previous_close(row)
    level = breakout_level(row)
    volume_ratio = row_num(row, "volume_ratio")
    ma20 = volume_ma20_lots(row)
    bullish = not math.isnan(close) and not math.isnan(open_) and (
        close > open_ or (close == open_ and not math.isnan(previous) and close > previous)
    )
    normal = not any(math.isnan(v) for v in (close, level, volume_ratio, ma20)) and close >= level * 1.02 and volume_ratio >= 2 and ma20 >= 1000 and bullish
    day_return = row_num(row, "daily_return_calc", "return_1d", "return_1d_pct")
    if math.isnan(day_return) and not math.isnan(close) and not math.isnan(previous) and previous > 0:
        day_return = (close / previous - 1) * 100
    locked = False
    if not any(math.isnan(v) for v in (close, open_, high, low, level, day_return)):
        one_price = high == low
        range_pct = math.nan if one_price or math.isnan(previous) or previous <= 0 else (high - low) / previous * 100
        locked = close >= level * 1.02 and day_return >= 9 and close >= high * 0.995 and open_ >= close * 0.995 and (one_price or (not math.isnan(range_pct) and range_pct <= 1))
    return normal or locked or flag(row, "volume_confirmed_breakout")


def independently_selected(row: dict[str, str]) -> bool:
    phase = row_text(row, "tdcc_price_phase").lower()
    status = row_text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge").lower()
    volume_ratio = row_num(row, "volume_ratio")
    return5 = row_num(row, "return_5d", "return_5d_pct")
    return20 = row_num(row, "return_20d", "return_20d_pct")
    close = row_num(row, "close")
    high = row_num(row, "high_20", "previous_20d_high", "platform_high")
    low = row_num(row, "low_20", "previous_20d_low", "platform_low")
    phase_ok = phase == "tdcc_leading_price" or (not phase and (status in POSITIVE_TDCC or flag(row, "tdcc_accumulation_signal")))
    in_range = not any(math.isnan(v) for v in (close, high, low)) and high > low and low * 0.9 <= close <= high * 1.1
    return (
        phase not in {"price_leading_tdcc", "overheated_after_tdcc"}
        and not attack_started(row)
        and (math.isnan(volume_ratio) or volume_ratio < 2.5)
        and phase_ok
        and (math.isnan(return5) or return5 < 8)
        and (math.isnan(return20) or return20 < 20)
        and in_range
    )


def revision_number(value: str) -> int:
    match = re.fullmatch(r"r([0-9]+)", value.lower())
    if not match:
        raise RuntimeError(f"invalid revision: {value}")
    return int(match.group(1))


def validate() -> None:
    for path in (DETAIL, SUMMARY, REPORT):
        if not path.is_file():
            raise RuntimeError(f"missing replay artifact: {path}")
    detail_payload = DETAIL.read_bytes()
    detail_fields, detail = csv_rows(detail_payload)
    _, summary = csv_rows(SUMMARY.read_bytes())
    if len(summary) != 3 or {row["horizon"] for row in summary} != {"D5", "D10", "D20"}:
        raise RuntimeError("summary must contain exactly D5/D10/D20 rows")
    if any(row.get("artifact_version") != VERSION or row.get("replay_kind") != REPLAY_KIND for row in detail + summary):
        raise RuntimeError("artifact version or replay kind drift")
    commit_values = {row["source_commit_sha"] for row in summary}
    if len(commit_values) != 1:
        raise RuntimeError("summary source commit must be singular")
    tree = Tree(next(iter(commit_values)))
    commit_time = subprocess.run(
        ["git", "show", "-s", "--format=%cI", tree.commit],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout.strip()
    if {row["source_commit_time"] for row in summary} != {commit_time}:
        raise RuntimeError("source commit time mismatch")
    production_sha = sha256(tree.read(PRODUCTION_SOURCE))
    if {row["production_source_sha256"] for row in summary} != {production_sha}:
        raise RuntimeError("production source SHA mismatch")

    _, manifest = csv_rows(tree.read(MANIFEST_PATH))
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in manifest:
        if row.get("artifact_id") == "all_candidates_source_rows":
            grouped[row["snapshot_report_date"]].append(row)
    selected_manifest = [max(rows, key=lambda row: revision_number(row["snapshot_revision"])) for _, rows in sorted(grouped.items())]
    expected: dict[tuple[str, str, str], tuple[dict[str, str], dict[str, str]]] = {}
    candidate_count = 0
    diagnostic_population = 0
    phase_presence: Counter[str] = Counter()
    status_presence: Counter[str] = Counter()
    accumulation_values: Counter[str] = Counter()
    for manifest_row in selected_manifest:
        payload = tree.read(manifest_row["snapshot_path"])
        hashes = {
            sha256(payload),
            sha256(payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")),
        }
        if manifest_row["snapshot_sha256"].lower() not in hashes:
            crlf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n").replace(b"\n", b"\r\n")
            if manifest_row["snapshot_sha256"].lower() != sha256(crlf):
                raise RuntimeError(f"snapshot hash mismatch: {manifest_row['snapshot_path']}")
        _, rows = csv_rows(payload)
        candidate_count += len(rows)
        for row_number, row in enumerate(rows, start=2):
            phase = row_text(row, "tdcc_price_phase").lower()
            volume_ratio = row_num(row, "volume_ratio")
            if (
                phase not in {"price_leading_tdcc", "overheated_after_tdcc"}
                and not attack_started(row)
                and (math.isnan(volume_ratio) or volume_ratio < 2.5)
            ):
                diagnostic_population += 1
                phase_keys = [
                    key for key in ("tdcc_price_phase", "tdcc_price_phase_x", "tdcc_price_phase_y")
                    if key in row
                ]
                phase_presence[
                    "missing" if not phase_keys else ("blank" if not phase else "nonblank")
                ] += 1
                status = row_text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge").lower()
                status_keys = [
                    f"{base}{suffix}"
                    for base in ("tdcc_status", "tdcc_judgement", "tdcc_judge")
                    for suffix in ("", "_x", "_y")
                    if f"{base}{suffix}" in row
                ]
                status_presence[
                    "missing" if not status_keys else ("blank" if not status else "nonblank")
                ] += 1
                accumulation_values[text(row.get("tdcc_accumulation_signal")) or "<blank>"] += 1
            if independently_selected(row):
                identity = (manifest_row["snapshot_report_date"], text(row.get("stock_id") or row.get("ticker")), str(row_number))
                expected[identity] = (manifest_row, row)
    actual = {(row["snapshot_report_date"], row["stock_id"], row["snapshot_row_number"]): row for row in detail}
    if set(actual) != set(expected):
        missing = sorted(set(expected) - set(actual))[:5]
        extra = sorted(set(actual) - set(expected))[:5]
        raise RuntimeError(f"independent selector replay mismatch: missing={missing}; extra={extra}")
    for identity, output_row in actual.items():
        manifest_row, source_row = expected[identity]
        if output_row["snapshot_row_sha256"] != row_sha(source_row):
            raise RuntimeError(f"snapshot row hash mismatch: {identity}")
        if output_row["snapshot_path"] != manifest_row["snapshot_path"]:
            raise RuntimeError(f"snapshot path mismatch: {identity}")
        if output_row["selector_selected"] != "True":
            raise RuntimeError(f"detail contains non-selected row: {identity}")
        if output_row["formal_use"] != "False" or output_row["promotion_evidence_allowed"] != "False":
            raise RuntimeError(f"formal-use boundary drift: {identity}")

    detail_sha = sha256(detail_payload)
    for row in summary:
        horizon = int(row["horizon"][1:])
        values = [Decimal(item[f"return_d{horizon}_pct"]) for item in detail if item[f"return_d{horizon}_pct"]]
        wins = sum(value > 0 for value in values)
        neutral = sum(value == 0 for value in values)
        failures = sum(value < 0 for value in values)
        expected_map = {
            "selected_snapshot_count": str(len(selected_manifest)),
            "candidate_row_count": str(candidate_count),
            "selector_selected_count": str(len(expected)),
            "evaluated_count": str(len(values)),
            "right_censored_count": str(len(expected) - len(values)),
            "win_count": str(wins), "neutral_count": str(neutral), "failure_count": str(failures),
            "detail_artifact_sha256": detail_sha, "formal_use": "False",
            "trade_eligible": "False", "promotion_evidence_allowed": "False",
            "sensitivity_is_corrected_primary": "False",
        }
        if values:
            expected_map.update({
                "win_rate_pct": fmt_decimal(Decimal(wins) * 100 / Decimal(len(values))),
                "average_return_pct": fmt_decimal(sum(values) / Decimal(len(values))),
                "median_return_pct": fmt_decimal(Decimal(str(statistics.median(values)))),
            })
        else:
            expected_map.update({"win_rate_pct": "", "average_return_pct": "", "median_return_pct": ""})
        for key, expected_value in expected_map.items():
            if row.get(key, "") != expected_value:
                raise RuntimeError(f"summary mismatch {row['horizon']} {key}: {row.get(key)!r} != {expected_value!r}")
    report = REPORT.read_text(encoding="utf-8")
    required_report_tokens = (
        tree.commit, commit_time, f"{candidate_count} 列候選", f"重建選出 {len(expected)} 列",
        "不是當時實際發布推薦", "formal_use=False", "D5", "D10", "D20",
        f"通過 attack 與量比後的 {diagnostic_population} 列",
        f"missing / blank / nonblank = {phase_presence['missing']} / {phase_presence['blank']} / {phase_presence['nonblank']}",
        f"missing / blank / nonblank = {status_presence['missing']} / {status_presence['blank']} / {status_presence['nonblank']}",
        f"`mild_accumulation` + `strong_accumulation` 共 {accumulation_values['mild_accumulation'] + accumulation_values['strong_accumulation']} 列",
        "欄位語意不相容",
    )
    for token in required_report_tokens:
        if token not in report:
            raise RuntimeError(f"report missing evidence token: {token}")
    source_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported_modules = {
        alias.name
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(source_tree)
        if isinstance(node, ast.ImportFrom)
    }
    forbidden_imports = {
        "build_daily_candidate_model_layer",
        "scripts.build_daily_candidate_model_layer",
        "build_tdcc_stealth_accumulation_historical_replay",
        "scripts.build_tdcc_stealth_accumulation_historical_replay",
    }
    if imported_modules & forbidden_imports:
        raise RuntimeError("validator independence violation: production or producer import found")
    print(f"validated_tdcc_stealth_historical_replay_source_commit={tree.commit}")
    print(f"validated_tdcc_stealth_historical_replay_snapshot_count={len(selected_manifest)}")
    print(f"validated_tdcc_stealth_historical_replay_candidate_rows={candidate_count}")
    print(f"validated_tdcc_stealth_historical_replay_selected_rows={len(expected)}")


def fmt_decimal(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP), "f")


if __name__ == "__main__":
    validate()
