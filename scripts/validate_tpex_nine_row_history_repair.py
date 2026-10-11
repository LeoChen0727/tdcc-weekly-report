"""Independently inspect the approved nine-key TPEx repair from immutable bytes.

This is source-repair evidence, not PIT, backtest, or anomaly-disposition evidence.
It does not import production parsers, writers, or model business functions.
"""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse


REPAIR_ID = "tpex_official_field_repair_2026_nine_rows"
BASE_REF = "7a96be629c4f9938f39d4b2274c8e5c7d6593283"
MANIFEST_PATH = "config/tpex_official_field_repair_2026_nine_rows.json"
STOCK_IDS = ("5498", "6588", "7734")
DATES = ("20260527", "20260602", "20260605")
WINDOW_ENDS = dict(zip(DATES, ("20260624", "20260630", "20260703")))
EXPECTED_KEYS = {(stock_id, date) for stock_id in STOCK_IDS for date in DATES}
EXPECTED_PATHS = {
    f"data/daily_price/{prefix}{date}.csv"
    for date in DATES
    for prefix in ("", "daily_price_")
} | {f"data/stock_price_history/{stock_id}.csv" for stock_id in STOCK_IDS}
PRIMARY_COLUMNS = {"volume", "trading_value", "source"}
DERIVED_COLUMNS = {"volume_ma20", "volume_ratio"}
ROUND_4 = Decimal("0.0001")


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _decimal(value: object, label: str) -> Decimal:
    try:
        number = Decimal(str(value).replace(",", "").strip())
    except InvalidOperation as exc:
        raise ValueError(f"invalid numeric value: {label}") from exc
    _require(number.is_finite(), f"non-finite numeric value: {label}")
    return number


def _valid_sha(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def _official_rows(manifest: dict) -> dict[tuple[str, str], dict]:
    _require(manifest.get("schema_version") == 1, "unsupported repair schema_version")
    _require(manifest.get("repair_id") == REPAIR_ID, "unexpected repair_id")
    _require(manifest.get("base_ref") == BASE_REF, "unexpected immutable base_ref")
    _require(bool(manifest.get("approval_reference")), "missing approval_reference")
    _require(manifest.get("original_publication_version_verified") is False,
             "repair must not claim verified original publication/PIT")
    _require(manifest.get("stock_ids") == list(STOCK_IDS), "unexpected stock_ids")
    _require(manifest.get("dates") == list(DATES), "unexpected repair dates")
    records = manifest.get("rows")
    _require(isinstance(records, list) and len(records) == 9, "expected nine official rows")
    result = {}
    date_receipts = {}
    for record in records:
        _require(isinstance(record, dict), "invalid official row record")
        key = (record.get("stock_id"), record.get("date"))
        _require(key in EXPECTED_KEYS and key not in result, f"duplicate/unapproved official identity: {key}")
        fields, values = record.get("official_fields"), record.get("official_row")
        _require(isinstance(fields, list) and isinstance(values, list) and len(fields) == len(values),
                 f"official fields/row width mismatch: {key}")
        _require(all(isinstance(field, str) for field in fields) and len(fields) == len(set(fields)),
                 f"duplicate/invalid official fields: {key}")
        _require({"代號", "成交股數", "成交金額(元)"}.issubset(fields),
                 f"missing explicit official share/NTD fields: {key}")
        named = dict(zip(fields, values))
        canonical = json.dumps(named, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        _require(_sha256(canonical) == record.get("official_row_sha256"), f"official row SHA mismatch: {key}")
        _require(str(named["代號"]).strip() == key[0], f"official stock identity mismatch: {key}")
        for name, field in (("volume_shares", "成交股數"), ("trading_value_ntd", "成交金額(元)")):
            official = _decimal(named[field], f"{key}/{field}")
            _require(official >= 0 and official == official.to_integral_value(), f"invalid official integer unit: {key}/{field}")
            _require(official == _decimal(record.get(name), f"{key}/{name}"), f"official value mismatch: {key}/{name}")
        source = record.get("source_before")
        _require(source in {"TPEX_OLD_DAILY_JSON", "TPEX_OLD_DAILY_CSV"}, f"unsupported old provider: {key}")
        _require(record.get("source_after") == source + "_SHARES_V1", f"unknown repaired share-unit version: {key}")
        _require(_valid_sha(record.get("body_sha256")), f"invalid official body SHA: {key}")
        url = record.get("official_url")
        _require(isinstance(url, str) and urlparse(url).scheme == "https" and
                 (urlparse(url).hostname or "").endswith(".tpex.org.tw"), f"missing official TPEx URL: {key}")
        _require(bool(record.get("captured_at")), f"missing official capture timestamp: {key}")
        receipt = (url, record["body_sha256"], record["captured_at"])
        _require(key[1] not in date_receipts or date_receipts[key[1]] == receipt,
                 f"inconsistent saved official response for date: {key[1]}")
        date_receipts[key[1]] = receipt
        result[key] = record
    _require(set(result) == EXPECTED_KEYS, "missing approved official identities")
    return result


def _csv_rows(content: bytes, path: str) -> tuple[list[bytes], list[str], list[dict[str, str]]]:
    lines = content.splitlines(keepends=True)
    _require(bool(lines), f"empty CSV: {path}")
    try:
        parsed = [next(csv.reader([line.decode("utf-8-sig")], strict=True)) for line in lines]
    except (UnicodeDecodeError, csv.Error, StopIteration) as exc:
        raise ValueError(f"invalid CSV: {path}") from exc
    header = parsed[0]
    _require(len(header) == len(set(header)), f"duplicate CSV header: {path}")
    required = {"stock_id", "date"} | PRIMARY_COLUMNS
    if path.startswith("data/stock_price_history/"):
        required |= DERIVED_COLUMNS
    _require(required.issubset(header), f"missing CSV columns: {path}")
    _require(all(len(row) == len(header) for row in parsed[1:]), f"CSV row width mismatch: {path}")
    rows = [dict(zip(header, row)) for row in parsed[1:]]
    keys = [(row["stock_id"], row["date"]) for row in rows]
    _require(len(keys) == len(set(keys)), f"duplicate CSV identity: {path}")
    return lines, header, rows


def _line_ending(line: bytes) -> bytes:
    return b"\r\n" if line.endswith(b"\r\n") else b"\n" if line.endswith(b"\n") else b""


def validate_repair_postimages(before: dict[str, bytes], after: dict[str, bytes], manifest: dict) -> dict:
    """Return bounded repair evidence or raise ValueError on a semantic mismatch."""
    _require(isinstance(manifest, dict), "invalid repair manifest")
    official = _official_rows(manifest)
    _require(set(before) == EXPECTED_PATHS and set(after) == EXPECTED_PATHS, "expected exact nine repair paths")
    files = manifest.get("files")
    _require(isinstance(files, list) and len(files) == 9, "expected nine immutable file records")
    file_records = {record.get("path"): record for record in files if isinstance(record, dict)}
    _require(set(file_records) == EXPECTED_PATHS and len(file_records) == len(files), "duplicate/unapproved file record")
    parsed = {}
    for path in sorted(EXPECTED_PATHS):
        record = file_records[path]
        _require(_sha256(before[path]) == record.get("before_sha256"), f"before SHA mismatch: {path}")
        _require(_sha256(after[path]) == record.get("after_sha256"), f"after SHA mismatch: {path}")
        old_lines, old_header, old_rows = _csv_rows(before[path], path)
        new_lines, new_header, new_rows = _csv_rows(after[path], path)
        _require(old_header == new_header and old_lines[0] == new_lines[0], f"CSV header changed: {path}")
        _require(len(old_rows) == len(new_rows), f"CSV row count changed: {path}")
        parsed[path] = (old_lines, new_lines, old_rows, new_rows)

    for date in DATES:
        paths = (f"data/daily_price/{date}.csv", f"data/daily_price/daily_price_{date}.csv")
        _require(before[paths[0]] == before[paths[1]] and after[paths[0]] == after[paths[1]],
                 f"daily aliases differ: {date}")

    windows = set()
    means = {}
    for stock_id in STOCK_IDS:
        path = f"data/stock_price_history/{stock_id}.csv"
        new_rows = parsed[path][3]
        dates = [row["date"] for row in new_rows]
        _require(all(row["stock_id"] == stock_id for row in new_rows) and dates == sorted(dates),
                 f"history identity/order mismatch: {path}")
        _require("20260706" in dates, f"missing next unchanged history row: {path}")
        volumes = [_decimal(row["volume"], f"{path}/{row['date']}/volume") for row in new_rows]
        for date in DATES:
            _require(date in dates, f"missing primary history date: {stock_id}/{date}")
            start = dates.index(date)
            affected = dates[start:start + 20]
            _require(len(affected) == 20 and affected[-1] == WINDOW_ENDS[date],
                     f"unexpected include-current rolling20 window: {stock_id}/{date}")
            windows.update((stock_id, affected_date) for affected_date in affected)
        for index, row in enumerate(new_rows):
            key = (stock_id, row["date"])
            if key in windows:
                sample = volumes[max(0, index - 19):index + 1]
                _require(len(sample) >= 5, f"rolling20 min_periods=5 not met: {key}")
                mean = sum(sample, Decimal(0)) / len(sample)
                ratio = volumes[index] / mean if mean else None
                means[key] = (mean.quantize(ROUND_4, rounding=ROUND_HALF_EVEN),
                              ratio.quantize(ROUND_4, rounding=ROUND_HALF_EVEN) if ratio is not None else None)
    manifest_windows = manifest.get("history_windows")
    _require(isinstance(manifest_windows, list) and len(manifest_windows) == 81, "expected 81 history window records")
    declared = {(row.get("stock_id"), row.get("date")) for row in manifest_windows if isinstance(row, dict)}
    _require(len(declared) == 81 and declared == windows, "history window boundary mismatch")
    _require(len(windows) == 81 and max(date for _, date in windows) == "20260703", "unexpected history window extent")

    changed_rows = daily_rows = history_primary_rows = history_derived_rows = 0
    seen_primary = set()
    for path, (old_lines, new_lines, old_rows, new_rows) in parsed.items():
        history = path.startswith("data/stock_price_history/")
        for index, (old, new) in enumerate(zip(old_rows, new_rows), start=1):
            key = (old["stock_id"], old["date"])
            _require(key == (new["stock_id"], new["date"]), f"CSV identity changed: {path}/{key}")
            primary = key in official
            derived = history and key in windows
            allowed = (PRIMARY_COLUMNS if primary else set()) | (DERIVED_COLUMNS if derived else set())
            if not allowed:
                _require(old_lines[index] == new_lines[index], f"unselected CSV row changed: {path}/{key}")
                continue
            _require(_line_ending(old_lines[index]) == _line_ending(new_lines[index]), f"line ending changed: {path}/{key}")
            _require(all(old[column] == new[column] for column in old if column not in allowed),
                     f"unapproved column/price changed: {path}/{key}")
            if primary:
                record = official[key]
                _require(old["source"] == record["source_before"] and new["source"] == record["source_after"],
                         f"source share-unit version mismatch: {path}/{key}")
                for column, field in (("volume", "volume_shares"), ("trading_value", "trading_value_ntd")):
                    _require(_decimal(new[column], f"{path}/{key}/{column}") == _decimal(record[field], field),
                             f"repaired official value mismatch: {path}/{key}/{column}")
                seen_primary.add((path, key))
                if history:
                    history_primary_rows += 1
                else:
                    daily_rows += 1
            if derived:
                mean, ratio = means[key]
                _require(_decimal(new["volume_ma20"], f"{path}/{key}/volume_ma20") == mean,
                         f"independent volume_ma20 mismatch: {path}/{key}")
                _require((ratio is None and not new["volume_ratio"]) or
                         (ratio is not None and _decimal(new["volume_ratio"], f"{path}/{key}/volume_ratio") == ratio),
                         f"independent volume_ratio mismatch: {path}/{key}")
                history_derived_rows += 1
            _require(old_lines[index] != new_lines[index], f"approved selected row was not repaired: {path}/{key}")
            changed_rows += 1
    _require((daily_rows, history_primary_rows, history_derived_rows, changed_rows) == (18, 9, 81, 99),
             "expected 18 daily + 81 history physical row changes, including nine history primary rows")
    _require(len(seen_primary) == 27, "missing primary repair rows")
    return {
        "result": "PASS", "repair_id": REPAIR_ID, "files": 9,
        "logical_stock_date_keys": 9, "raw_daily_copy_rows": daily_rows,
        "history_primary_rows": history_primary_rows, "history_derived_rows": history_derived_rows,
        "changed_physical_rows": changed_rows, "derived_first_date": "20260527",
        "derived_last_date": "20260703", "next_history_date_unchanged": "20260706",
        "original_publication_version_verified": False,
        "formal_model_backtest_parity_or_anomaly_disposition_proven": False,
    }


def _git(repo_root: Path, *arguments: str) -> bytes:
    result = subprocess.run(["git", *arguments], cwd=repo_root, capture_output=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="獨立驗證已批准的 TPEx 九列歷史修復；不抓取來源、不寫入資料。")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--manifest-path", type=Path, help="本機 manifest；省略時讀取 --ref 中的不可變 manifest。")
    args = parser.parse_args(argv)
    try:
        base_sha = _git(args.repo_root, "rev-parse", "--verify", f"{args.base_ref}^{{commit}}").decode().strip()
        ref_sha = _git(args.repo_root, "rev-parse", "--verify", f"{args.ref}^{{commit}}").decode().strip()
        _require(base_sha == BASE_REF, "--base-ref differs from approved immutable base")
        if args.manifest_path:
            manifest_path = args.manifest_path if args.manifest_path.is_absolute() else args.repo_root / args.manifest_path
            manifest_bytes = manifest_path.read_bytes()
        else:
            manifest_bytes = _git(args.repo_root, "show", f"{ref_sha}:{MANIFEST_PATH}")
        manifest = json.loads(manifest_bytes.decode("utf-8-sig"))
        before = {path: _git(args.repo_root, "show", f"{base_sha}:{path}") for path in EXPECTED_PATHS}
        after = {path: _git(args.repo_root, "show", f"{ref_sha}:{path}") for path in EXPECTED_PATHS}
        summary = validate_repair_postimages(before, after, manifest)
        summary.update(base_ref=base_sha, ref=ref_sha, manifest_sha256=_sha256(manifest_bytes))
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError) as exc:
        print(f"TPEx 九列歷史修復驗證失敗：{exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
