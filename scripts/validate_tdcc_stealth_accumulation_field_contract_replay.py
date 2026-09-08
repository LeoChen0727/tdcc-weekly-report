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
from collections import defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
VERSION = "tdcc_stealth_accumulation_historical_selector_field_contract_replay_v2"
OUTPUT_DIR = Path("output/research/tdcc_stealth_accumulation")
DETAIL = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_field_contract_replay_detail_v2.csv"
SUMMARY = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_field_contract_replay_summary_v2.csv"
REPORT = OUTPUT_DIR / "tdcc_stealth_accumulation_historical_selector_field_contract_replay_report_v2.md"
MANIFEST = "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv"
POSITIVE = {"strong_accumulation", "mild_accumulation"}


def text(value: Any) -> str:
    if value is None:
        return ""
    value = str(value).replace("\ufeff", "").strip()
    return "" if value.lower() in {"nan", "none", "nat", "<na>"} else value


def number(value: Any) -> float:
    value = text(value).replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    if value in {"", "-"}:
        return math.nan
    try:
        return float(value)
    except ValueError:
        return math.nan


def truthy(value: Any) -> bool:
    return text(value).lower() in {"true", "1", "yes", "y", "t"}


def row_text(row: dict[str, str], *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            value = text(row.get(candidate))
            if candidate in row and value:
                return value.lower()
    return ""


def row_num(row: dict[str, str], *names: str) -> float:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            value = number(row.get(candidate))
            if not math.isnan(value):
                return value
    return math.nan


def flag(row: dict[str, str], name: str) -> bool:
    return truthy(row.get(name, ""))


def volume_ma20_lots(row: dict[str, str]) -> float:
    value = row_num(row, "volume_ma20_lots", "avg_volume_20d_lots")
    if not math.isnan(value):
        return value
    value = row_num(row, "volume_ma20", "avg_volume_20d")
    if math.isnan(value):
        return math.nan
    return value / 1000.0 if value >= 100000 else value


def breakout_level(row: dict[str, str]) -> float:
    return row_num(
        row,
        "previous_20d_high_ex_today", "previous_20d_high", "prior_20d_high",
        "high_20_ex_today", "high_20", "short_platform_high", "platform_high", "range_high",
    )


def previous_close(row: dict[str, str]) -> float:
    return row_num(row, "previous_close", "prev_close", "close_prev", "close_1d_ago")


def bottom_volume_attack_like(row: dict[str, str]) -> bool:
    close = row_num(row, "close")
    open_ = row_num(row, "open")
    high = row_num(row, "high")
    low = row_num(row, "low")
    vol = row_num(row, "volume_ratio")
    ma20 = volume_ma20_lots(row)
    level = breakout_level(row)
    prev_close = previous_close(row)
    bullish = not math.isnan(close) and not math.isnan(open_) and (
        close > open_ or (close == open_ and not math.isnan(prev_close) and close > prev_close)
    )
    normal = (
        not any(math.isnan(value) for value in (vol, ma20, level, close))
        and close >= level * 1.02 and vol >= 2.0 and ma20 >= 1000 and bullish
    )
    ret = row_num(row, "daily_return_calc", "return_1d", "return_1d_pct")
    if math.isnan(ret) and not math.isnan(close) and not math.isnan(prev_close) and prev_close > 0:
        ret = (close / prev_close - 1) * 100
    locked = False
    if not any(math.isnan(value) for value in (close, open_, high, low, level, ret)):
        one_price = high == low
        range_pct = math.nan if one_price or math.isnan(prev_close) or prev_close <= 0 else (high - low) / prev_close * 100
        tight = one_price or (not math.isnan(range_pct) and range_pct <= 1.0)
        locked = close >= level * 1.02 and ret >= 9.0 and close >= high * 0.995 and open_ >= close * 0.995 and tight
    return normal or locked


def independently_selected(row: dict[str, str]) -> bool:
    phase = row_text(row, "tdcc_price_phase")
    status = row_text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge")
    enum_value = row_text(row, "tdcc_accumulation_signal")
    if phase:
        tdcc_positive = phase == "tdcc_leading_price"
    elif status:
        tdcc_positive = status in POSITIVE or flag(row, "tdcc_accumulation_signal")
    else:
        tdcc_positive = flag(row, "tdcc_accumulation_signal") or enum_value in POSITIVE
    vol = row_num(row, "volume_ratio")
    ret5 = row_num(row, "return_5d", "return_5d_pct")
    ret20 = row_num(row, "return_20d", "return_20d_pct")
    close = row_num(row, "close")
    recent_high = row_num(row, "high_20", "previous_20d_high", "platform_high")
    recent_low = row_num(row, "low_20", "previous_20d_low", "platform_low")
    in_range = (
        not any(math.isnan(value) for value in (close, recent_high, recent_low))
        and recent_high > recent_low
        and recent_low * 0.9 <= close <= recent_high * 1.1
    )
    return (
        phase not in {"price_leading_tdcc", "overheated_after_tdcc"}
        and not (bottom_volume_attack_like(row) or flag(row, "volume_confirmed_breakout"))
        and (math.isnan(vol) or vol < 2.5)
        and tdcc_positive
        and (math.isnan(ret5) or ret5 < 8)
        and (math.isnan(ret20) or ret20 < 20)
        and in_range
    )


class GitTree:
    def __init__(self, root: Path, source_ref: str) -> None:
        self.root = root
        self.commit = self.run("rev-parse", "--verify", f"{source_ref}^{{commit}}").strip().lower()
        self.entries: dict[str, str] = {}
        for line in self.run("ls-tree", "-r", "--full-tree", self.commit).splitlines():
            meta, path = line.split("\t", 1)
            parts = meta.split()
            if len(parts) == 3 and parts[1] == "blob":
                self.entries[path] = parts[2]

    def run(self, *args: str, binary: bool = False):
        return subprocess.run(
            ["git", *args], cwd=self.root, check=True, capture_output=True,
            text=not binary, encoding=None if binary else "utf-8",
        ).stdout

    def read(self, path: str) -> bytes:
        if path not in self.entries:
            raise RuntimeError(f"missing source path: {path}")
        return self.run("cat-file", "blob", self.entries[path], binary=True)


def csv_rows(payload: bytes) -> list[dict[str, str]]:
    return [{str(key): text(value) for key, value in row.items()} for row in csv.DictReader(io.StringIO(payload.decode("utf-8-sig")))]


def decimal_price(value: Any) -> Decimal | None:
    try:
        result = Decimal(text(value).replace(",", ""))
    except InvalidOperation:
        return None
    return result if result.is_finite() and result > 0 else None


def formatted(value: Decimal) -> str:
    return format(value.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP), "f")


def canonical_row_sha256(row: dict[str, str]) -> str:
    payload = json.dumps(
        {str(key): text(value) for key, value in row.items()},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_prices(tree: GitTree, min_date: str) -> dict[str, list[dict[str, Any]]]:
    by_stock: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for path in sorted(tree.entries):
        match = re.fullmatch(r"data/daily_price/(20[0-9]{6})\.csv", path)
        if not match or match.group(1) < min_date:
            continue
        payload = tree.read(path)
        source_sha = hashlib.sha256(payload).hexdigest()
        for row in csv_rows(payload):
            date = text(row.get("date")) or match.group(1)
            stock_id = text(row.get("stock_id") or row.get("ticker") or row.get("code"))
            open_price = decimal_price(row.get("open"))
            close_price = decimal_price(row.get("close"))
            if not re.fullmatch(r"[0-9]{4,6}", stock_id) or date != match.group(1) or open_price is None or close_price is None:
                continue
            identity = (date, stock_id)
            if identity in seen:
                raise RuntimeError(f"duplicate price identity: {date}|{stock_id}")
            seen.add(identity)
            by_stock[stock_id].append(
                {
                    "date": date,
                    "open": open_price,
                    "close": close_price,
                    "path": path,
                    "source_sha256": source_sha,
                    "row_sha256": canonical_row_sha256(row),
                }
            )
    for rows in by_stock.values():
        rows.sort(key=lambda row: row["date"])
    return by_stock


def selected_manifest_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("artifact_id") == "all_candidates_source_rows":
            grouped[row["snapshot_report_date"]].append(row)
    return [max(candidates, key=lambda row: int(re.fullmatch(r"r([0-9]+)", row["snapshot_revision"]).group(1))) for _, candidates in sorted(grouped.items())]


def validate(root: Path, source_ref: str) -> None:
    detail_path = root / DETAIL
    summary_path = root / SUMMARY
    report_path = root / REPORT
    detail = list(csv.DictReader(detail_path.open(encoding="utf-8-sig", newline="")))
    summary = list(csv.DictReader(summary_path.open(encoding="utf-8-sig", newline="")))
    if len(summary) != 3 or {row["horizon"] for row in summary} != {"D5", "D10", "D20"}:
        raise RuntimeError("summary must contain exactly D5, D10, and D20")
    tree = GitTree(root, source_ref)
    manifest = selected_manifest_rows(csv_rows(tree.read(MANIFEST)))
    expected: set[tuple[str, str, str, str]] = set()
    for manifest_row in manifest:
        path = manifest_row["snapshot_path"]
        for row_number, row in enumerate(csv_rows(tree.read(path)), start=2):
            if independently_selected(row):
                expected.add((path, str(row_number), text(row.get("stock_id") or row.get("ticker")), text(row.get("signal_date") or row.get("date") or manifest_row["snapshot_report_date"])))
    actual = {
        (row["snapshot_path"], row["snapshot_row_number"], row["stock_id"], row["candidate_signal_date"])
        for row in detail
    }
    if actual != expected:
        raise RuntimeError(f"independent selector mismatch expected={len(expected)} actual={len(actual)}")
    if any(row["artifact_version"] != VERSION for row in detail + summary):
        raise RuntimeError("artifact version mismatch")
    if any(row["formal_use"] != "False" or row["trade_eligible"] != "False" or row["promotion_evidence_allowed"] != "False" for row in detail + summary):
        raise RuntimeError("research-only flags violated")
    if any(int(row["selector_selected_count"]) != len(detail) for row in summary):
        raise RuntimeError("summary selected count mismatch")
    if any(row["source_commit_sha"] != tree.commit for row in detail + summary):
        raise RuntimeError("source commit mismatch")
    if any(row["tdcc_positive_resolution"] != "recognized_enum_positive_fallback" for row in detail):
        raise RuntimeError("unexpected selected resolution")
    prices = load_prices(tree, min(row["snapshot_report_date"] for row in manifest))
    returns_by_horizon: dict[int, list[Decimal]] = {5: [], 10: [], 20: []}
    anomaly_rows_by_horizon = {5: 0, 10: 0, 20: 0}
    for row in detail:
        later = [price for price in prices.get(row["stock_id"], []) if price["date"] > row["candidate_signal_date"]]
        if not later:
            if row["forward_window_status"] != "right_censored_no_next_trading_day_open":
                raise RuntimeError("missing-entry right censor mismatch")
            continue
        entry = later[0]
        for key, expected_value in (
            ("entry_date", entry["date"]),
            ("entry_open_price", formatted(entry["open"])),
            ("entry_price_source_path", entry["path"]),
            ("entry_price_source_sha256", entry["source_sha256"]),
            ("entry_price_row_sha256", entry["row_sha256"]),
        ):
            if row[key] != expected_value:
                raise RuntimeError(f"entry mismatch {row['stock_id']} {row['candidate_signal_date']} field={key}")
        anomaly = False
        for horizon in (5, 10, 20):
            if len(later) <= horizon:
                if row[f"return_d{horizon}_pct"]:
                    raise RuntimeError("right-censored horizon unexpectedly has return")
                continue
            exit_row = later[horizon]
            return_value = ((exit_row["close"] / entry["open"]) - Decimal("1")) * Decimal("100")
            returns_by_horizon[horizon].append(Decimal(formatted(return_value)))
            for key, expected_value in (
                (f"exit_d{horizon}_date", exit_row["date"]),
                (f"exit_d{horizon}_close_price", formatted(exit_row["close"])),
                (f"exit_d{horizon}_price_source_path", exit_row["path"]),
                (f"exit_d{horizon}_price_source_sha256", exit_row["source_sha256"]),
                (f"exit_d{horizon}_price_row_sha256", exit_row["row_sha256"]),
                (f"return_d{horizon}_pct", formatted(return_value)),
            ):
                if row[key] != expected_value:
                    raise RuntimeError(f"outcome mismatch {row['stock_id']} {row['candidate_signal_date']} field={key}")
            anomaly = anomaly or abs(return_value) >= Decimal("80")
        if (row["anomaly_candidate"] == "True") != anomaly:
            raise RuntimeError("anomaly flag mismatch")
        if anomaly:
            for horizon in (5, 10, 20):
                if row[f"return_d{horizon}_pct"]:
                    anomaly_rows_by_horizon[horizon] += 1
    for row in summary:
        horizon = int(row["horizon"][1:])
        values = returns_by_horizon[horizon]
        expected_average = formatted(sum(values) / Decimal(len(values))) if values else ""
        expected_median = formatted(Decimal(str(statistics.median(values)))) if values else ""
        checks = {
            "evaluated_count": str(len(values)),
            "right_censored_count": str(len(detail) - len(values)),
            "invalid_price_count": "0",
            "average_return_pct": expected_average,
            "median_return_pct": expected_median,
            "unresolved_anomaly_candidate_count": str(anomaly_rows_by_horizon[horizon]),
        }
        for key, expected_value in checks.items():
            if row[key] != expected_value:
                raise RuntimeError(
                    f"summary mismatch horizon={horizon} field={key} "
                    f"expected={expected_value} actual={row[key]}"
                )
    report = report_path.read_text(encoding="utf-8")
    for required in ("v1 / v2 比較界線", "advisory-only", "不是 `8434`", tree.commit):
        if required not in report:
            raise RuntimeError(f"report missing required text: {required}")
    print(f"validated_source_commit={tree.commit}")
    print(f"validated_snapshot_count={len(manifest)}")
    print(f"validated_selected_count={len(actual)}")
    print(f"validated_unique_stock_count={len({row['stock_id'] for row in detail})}")
    print(f"validated_overlap_count={sum(row['overlap_with_prior_signal'] == 'True' for row in detail)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Independently validate TDCC field-contract replay v2.")
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--source-ref", required=True)
    args = parser.parse_args(argv)
    validate(args.repository_root.resolve(), args.source_ref)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
