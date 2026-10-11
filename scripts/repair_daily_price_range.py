from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import fetch_official_daily_price as fetcher
import scripts.market_session_calendar as market_session_calendar
from scripts import validate_daily_price_history_continuity as continuity


DATA_DIR = Path("data/daily_price")
LATEST_DIR = Path("output/latest")
REPORT_CSV = LATEST_DIR / "repair_daily_price_range_latest.csv"
CHECK_CSV = LATEST_DIR / "repair_daily_price_range_check_code_latest.csv"
REPORT_JSON = LATEST_DIR / "repair_daily_price_range_latest.json"
REPORT_MD = LATEST_DIR / "repair_daily_price_range_latest.md"
SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS = (
    "output/latest/company_industry_snapshot_latest.csv",
    "docs/latest/company_industry_snapshot_latest.csv",
    "output/latest/stock_theme_taxonomy_latest.csv",
    "docs/latest/stock_theme_taxonomy_latest.csv",
)


def parse_yyyymmdd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def yyyymmdd(value: datetime) -> str:
    return value.strftime("%Y%m%d")


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def dataframe_csv_bytes(df: pd.DataFrame, *, encoding: str = "utf-8-sig") -> bytes:
    return df.to_csv(index=False, lineterminator="\n").encode(encoding)


def build_tpex_nine_row_repair_manifest(
    saved_receipts: dict, plan: dict, approval_reference: str
) -> dict:
    """Bind the approved nine-key repair to saved official named-field receipts.

    This does not fetch prices or verify the original publication version. The
    resulting manifest is source-maintenance evidence, not model evidence.
    """
    stocks = ["5498", "6588", "7734"]
    dates = ["20260527", "20260602", "20260605"]
    expected_keys = {(stock, date) for stock in stocks for date in dates}
    primary = plan["primary_diff"]
    if not approval_reference.strip():
        raise ValueError("nine-row repair requires an approval reference")
    if {(row["stock_id"], row["date"]) for row in primary} != expected_keys:
        raise ValueError("nine-row repair plan has unexpected stock/date keys")
    rows = []
    for date in dates:
        comparisons = [
            row for row in saved_receipts["tpex_field_comparisons"]
            if row["official_date"] == date
        ]
        response_hashes = {row["official_response_sha256"] for row in comparisons}
        if len(response_hashes) != 1:
            raise ValueError(f"nine-row repair has no unique official receipt: {date}")
        body_sha = response_hashes.pop()
        responses = [
            row for row in saved_receipts["official_responses"]
            if row["response_sha256"] == body_sha
        ]
        if len(responses) != 1:
            raise ValueError(f"nine-row repair has no unique official body: {date}")
        response = responses[0]
        body = response["body_utf8"].encode("utf-8")
        if sha256_bytes(body) != body_sha:
            raise ValueError(f"nine-row repair official body SHA mismatch: {date}")
        decoded = json.loads(body)
        if decoded.get("date") != date:
            raise ValueError(f"nine-row repair official date mismatch: {date}")
        for stock in stocks:
            matches = []
            for table in decoded["tables"]:
                fields = table["fields"]
                if "代號" not in fields:
                    continue
                index = fields.index("代號")
                matches.extend(
                    (fields, values) for values in table["data"]
                    if str(values[index]).strip() == stock
                )
            if len(matches) != 1:
                raise ValueError(f"nine-row repair official identity mismatch: {stock}/{date}")
            fields, values = matches[0]
            if len(fields) != len(set(fields)) or len(fields) != len(values):
                raise ValueError(f"nine-row repair malformed official fields: {stock}/{date}")
            official = dict(zip(fields, values))
            volume = str(int(str(official["成交股數"]).replace(",", "")))
            trading_value = str(int(str(official["成交金額(元)"]).replace(",", "")))
            row_sha = sha256_bytes(json.dumps(
                official, ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ).encode("utf-8"))
            selected = [
                row for row in primary
                if (row["stock_id"], row["date"]) == (stock, date)
            ]
            sources = {(row["source_before"], row["source_proposed"]) for row in selected}
            if len(sources) != 1:
                raise ValueError(f"nine-row repair source aliases disagree: {stock}/{date}")
            source_before, source_after = sources.pop()
            if source_before not in {"TPEX_OLD_DAILY_JSON", "TPEX_OLD_DAILY_CSV"} or source_after != source_before + "_SHARES_V1":
                raise ValueError(f"nine-row repair has unknown source units: {stock}/{date}")
            if any(
                row["body_sha256"] != body_sha
                or row["official_row_sha256"] != row_sha
                or row["volume_proposed"] != volume
                or row["trading_value_proposed"] != trading_value
                for row in selected
            ):
                raise ValueError(f"nine-row repair plan disagrees with receipt: {stock}/{date}")
            rows.append({
                "stock_id": stock, "date": date,
                "source_before": source_before, "source_after": source_after,
                "official_fields": fields, "official_row": values,
                "official_url": response["url"], "captured_at": response["captured_at_utc"],
                "body_sha256": body_sha, "official_row_sha256": row_sha,
                "volume_shares": volume, "trading_value_ntd": trading_value,
            })
    paths = {
        f"data/daily_price/{prefix}{date}.csv"
        for date in dates for prefix in ("", "daily_price_")
    } | {f"data/stock_price_history/{stock}.csv" for stock in stocks}
    if len(plan["files"]) != 9 or {item["path"] for item in plan["files"]} != paths:
        raise ValueError("nine-row repair plan has unexpected file scope")
    return {
        "schema_version": 1,
        "repair_id": "tpex_official_field_repair_2026_nine_rows",
        "base_ref": plan["source_sha"], "approval_reference": approval_reference,
        "stock_ids": stocks, "dates": dates,
        "original_publication_version_verified": False,
        "writer_function": "scripts/repair_daily_price_range.py:build_tpex_nine_row_repair_manifest",
        "read_functions": [
            "scripts/repair_daily_price_range.py:build_tpex_nine_row_daily_postimages",
            "scripts/repair_daily_price_range.py:stage_tpex_nine_row_repair",
            "scripts/build_stock_price_history.py:build_tpex_nine_row_history_postimages",
            "scripts/validate_tpex_nine_row_history_repair.py:validate_repair_postimages",
        ],
        "permitted_use": "daily_source_integrity_maintenance nine-key source repair only",
        "forbidden_uses": ["model promotion", "backtest evidence", "anomaly disposition", "PDF operation rows"],
        "rows": rows,
        "files": [{
            "path": item["path"], "before_sha256": item["before_sha256"],
            "after_sha256": item["projected_sha256"],
        } for item in plan["files"]],
        "history_windows": [{
            "stock_id": item["stock_id"], "date": item["date"],
        } for item in plan["derived_diff"]],
    }


def build_tpex_nine_row_daily_postimages(
    before: dict[str, bytes], manifest: dict
) -> dict[str, bytes]:
    """Patch only the six approved daily aliases, retaining every other line."""
    contracts = {
        item["path"]: item for item in manifest["files"]
        if item["path"].startswith("data/daily_price/")
    }
    expected_paths = {
        f"data/daily_price/{prefix}{date}.csv"
        for date in ("20260527", "20260602", "20260605")
        for prefix in ("", "daily_price_")
    }
    if set(contracts) != expected_paths:
        raise ValueError("nine-row repair has unexpected daily path scope")
    facts = {(row["stock_id"], row["date"]): row for row in manifest["rows"]}
    expected_keys = {
        (stock, date) for stock in ("5498", "6588", "7734")
        for date in ("20260527", "20260602", "20260605")
    }
    if len(manifest["rows"]) != 9 or set(facts) != expected_keys:
        raise ValueError("nine-row repair has unexpected daily identity scope")
    result = {}
    for path, contract in contracts.items():
        payload = before[path]
        if sha256_bytes(payload) != contract["before_sha256"]:
            raise ValueError(f"nine-row repair before SHA mismatch: {path}")
        lines = payload.splitlines(keepends=True)
        records = list(csv.reader(io.StringIO(payload.decode("utf-8-sig"))))
        if len(lines) != len(records):
            raise ValueError(f"nine-row repair requires single-line CSV records: {path}")
        header = records[0]
        if len(header) != len(set(header)) or any(len(row) != len(header) for row in records[1:]):
            raise ValueError(f"nine-row repair malformed CSV: {path}")
        changed = list(lines)
        found = set()
        for index, cells in enumerate(records[1:], start=1):
            row = dict(zip(header, cells))
            key = row["stock_id"], row["date"]
            if key not in facts:
                continue
            if key in found:
                raise ValueError(f"nine-row repair duplicate identity: {path}/{key}")
            found.add(key)
            fact = facts[key]
            if row["market"] != "TPEx" or row["source"] != fact["source_before"]:
                raise ValueError(f"nine-row repair source mismatch: {path}/{key}")
            if fact["source_after"] != row["source"] + "_SHARES_V1":
                raise ValueError(f"nine-row repair unknown source units: {path}/{key}")
            row.update(volume=fact["volume_shares"], trading_value=fact["trading_value_ntd"], source=fact["source_after"])
            old = lines[index]
            ending = "\r\n" if old.endswith(b"\r\n") else "\n" if old.endswith(b"\n") else ""
            buffer = io.StringIO(newline="")
            csv.writer(buffer, lineterminator=ending).writerow([row[column] for column in header])
            changed[index] = buffer.getvalue().encode("utf-8")
        if len(found) != 3:
            raise ValueError(f"nine-row repair missing daily identity: {path}")
        result[path] = b"".join(changed)
        if sha256_bytes(result[path]) != contract["after_sha256"]:
            raise ValueError(f"nine-row repair postimage SHA mismatch: {path}")
    for date in ("20260527", "20260602", "20260605"):
        paths = [f"data/daily_price/{prefix}{date}.csv" for prefix in ("", "daily_price_")]
        if before[paths[0]] != before[paths[1]] or result[paths[0]] != result[paths[1]]:
            raise ValueError(f"nine-row repair daily aliases disagree: {date}")
    return result


def parse_selected_dates(value: str) -> list[str]:
    dates = [part for part in re.split(r"[,;\s]+", safe_str(value)) if part]
    if not dates:
        return []
    if len(dates) != len(set(dates)):
        raise ValueError("selected dates contain duplicates")
    for date_text in dates:
        parse_yyyymmdd(date_text)
    if dates != sorted(dates):
        raise ValueError("selected dates must be strictly ascending")
    return dates


def stage_tpex_nine_row_repair(
    repo_root: Path, manifest: dict, temporary_root: Path
) -> dict:
    """Atomically stage validated nine-file blobs without materializing data.

    The caller owns the approved sparse task and its recorded temporary root.
    Existing staged entries are preserved; failures leave the index unchanged.
    """
    from scripts.build_stock_price_history import build_tpex_nine_row_history_postimages
    from scripts.validate_tpex_nine_row_history_repair import validate_repair_postimages

    repo_root = repo_root.resolve()

    def git(*arguments: str, payload: bytes | None = None, env: dict | None = None) -> bytes:
        return subprocess.run(
            ["git", *arguments], cwd=repo_root, input=payload,
            capture_output=True, check=True, env=env,
        ).stdout

    paths = sorted(item["path"] for item in manifest["files"])
    if any((repo_root / path).exists() for path in paths):
        raise ValueError("nine-row staging requires absent sparse data files")
    index = Path(git("rev-parse", "--path-format=absolute", "--git-path", "index").decode().strip())
    lock = index.with_name(index.name + ".lock")
    temporary_root.mkdir(parents=True, exist_ok=True)
    # Standard Git index lock prevents a concurrent stage from being overwritten.
    with lock.open("xb") as held_lock:
        published = False
        try:
            before = {path: git("show", f":{path}") for path in paths}
            after = build_tpex_nine_row_daily_postimages(before, manifest)
            after.update(build_tpex_nine_row_history_postimages(before, manifest))
            summary = validate_repair_postimages(before, after, manifest)
            with tempfile.TemporaryDirectory(prefix="nine-row-index-", dir=temporary_root) as scratch:
                scratch_index = Path(scratch) / "index"
                shutil.copyfile(index, scratch_index)
                env = dict(os.environ, GIT_INDEX_FILE=str(scratch_index))
                entries = []
                for path in paths:
                    blob = git("hash-object", "-w", "--stdin", payload=after[path]).decode().strip()
                    entries.append(f"100644 {blob}\t{path}\n")
                git("update-index", "--index-info", payload="".join(entries).encode(), env=env)
                git("update-index", "--skip-worktree", "--stdin", payload=("\n".join(paths) + "\n").encode(), env=env)
                staged = {path: git("show", f":{path}", env=env) for path in paths}
                validate_repair_postimages(before, staged, manifest)
                # update-index touches only these existing regular-file entries.
                original_entries = git("ls-files", "--stage").splitlines()
                new_entries = git("ls-files", "--stage", env=env).splitlines()
                selected = {path.encode() for path in paths}
                keep = lambda rows: [row for row in rows if row.split(b"\t", 1)[1] not in selected]
                if keep(original_entries) != keep(new_entries):
                    raise ValueError("nine-row staging changed another index entry")
                held_lock.write(scratch_index.read_bytes())
                held_lock.flush()
                os.fsync(held_lock.fileno())
            held_lock.close()
            os.replace(lock, index)
            published = True
            return summary
        finally:
            held_lock.close()
            if not published:
                lock.unlink(missing_ok=True)


def parse_expected_date_contracts(values: list[str] | None) -> dict[str, tuple[str, int]]:
    """Parse optional selected-date input bindings without constraining generic range mode."""

    contracts: dict[str, tuple[str, int]] = {}
    for value in values or []:
        parts = safe_str(value).split(":")
        if len(parts) != 3:
            raise ValueError(
                "expected date contract must use YYYYMMDD:sha256:row_count"
            )
        date_text, expected_sha, row_count_text = parts
        parse_yyyymmdd(date_text)
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
            raise ValueError(f"invalid expected SHA-256 for {date_text}")
        try:
            row_count = int(row_count_text)
        except ValueError as exc:
            raise ValueError(f"invalid expected row count for {date_text}") from exc
        if row_count <= 0:
            raise ValueError(f"expected row count must be positive for {date_text}")
        if date_text in contracts:
            raise ValueError(f"duplicate expected date contract: {date_text}")
        contracts[date_text] = (expected_sha, row_count)
    return contracts


def _safe_transaction_target(root: Path, relative_path: Path) -> Path:
    root = root.resolve()
    if relative_path.is_absolute() or any(part in {"", ".", ".."} for part in relative_path.parts):
        raise ValueError(f"selected-date repair path is not canonical: {relative_path}")
    target = (root / relative_path).resolve()
    try:
        target.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"selected-date repair path escapes repository: {relative_path}") from exc
    current = root
    for part in relative_path.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"selected-date repair path contains symlink: {relative_path}")
    if target.exists() and not target.is_file():
        raise ValueError(f"selected-date repair target is not a regular file: {relative_path}")
    return target


def publish_payloads_transaction(
    root: Path,
    payloads: dict[Path, bytes],
    *,
    fail_after_replace: int = 0,
) -> None:
    """Publish a bounded selected-date payload set and restore every target on failure."""

    if not payloads:
        raise ValueError("selected-date repair transaction has no payloads")
    root = root.resolve()
    ordered = sorted(payloads.items(), key=lambda item: item[0].as_posix())
    with tempfile.TemporaryDirectory(
        prefix=".official-price-selected-date-", dir=root
    ) as temp_text:
        temp_root = Path(temp_text)
        prepared: list[tuple[Path, Path, Path | None]] = []
        for index, (relative_path, payload) in enumerate(ordered):
            target = _safe_transaction_target(root, relative_path)
            next_path = temp_root / f"next-{index}.bin"
            next_path.write_bytes(payload)
            if sha256_bytes(next_path.read_bytes()) != sha256_bytes(payload):
                raise ValueError(f"selected-date repair prepared payload mismatch: {relative_path}")
            previous_path: Path | None = None
            if target.exists():
                previous_path = temp_root / f"previous-{index}.bin"
                shutil.copyfile(target, previous_path)
            prepared.append((target, next_path, previous_path))

        replaced: list[tuple[Path, Path | None]] = []
        try:
            for target, next_path, previous_path in prepared:
                target.parent.mkdir(parents=True, exist_ok=True)
                os.replace(next_path, target)
                replaced.append((target, previous_path))
                if fail_after_replace and len(replaced) >= fail_after_replace:
                    raise OSError("injected selected-date repair transaction failure")
        except Exception as exc:
            rollback_errors: list[str] = []
            for target, previous_path in reversed(replaced):
                try:
                    if previous_path is None:
                        target.unlink(missing_ok=True)
                    else:
                        restore_path = previous_path.with_name(previous_path.name + ".restore")
                        shutil.copyfile(previous_path, restore_path)
                        os.replace(restore_path, target)
                except Exception as rollback_exc:  # pragma: no cover - catastrophic filesystem failure
                    rollback_errors.append(f"{target}: {rollback_exc}")
            if rollback_errors:
                raise RuntimeError(
                    "selected-date repair transaction failed and rollback failed: "
                    f"original={exc}; rollback={rollback_errors}"
                ) from exc
            raise


def write_daily_price_files(df: pd.DataFrame, date_text: str) -> list[Path]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    legacy_path = DATA_DIR / f"{date_text}.csv"
    canonical_path = DATA_DIR / f"daily_price_{date_text}.csv"
    df.to_csv(legacy_path, index=False, encoding="utf-8-sig")
    df.to_csv(canonical_path, index=False, encoding="utf-8-sig")
    return [legacy_path, canonical_path]


def fetch_with_retry(date_text: str, retries: int, sleep_seconds: float) -> tuple[pd.DataFrame, dict[str, Any], list[str]]:
    last_df = pd.DataFrame()
    last_status: dict[str, Any] = {"date": date_text, "full_market_ok": False}
    last_log: list[str] = []
    provenance: list[dict[str, Any]] = []
    for attempt in range(1, retries + 1):
        fetcher.reset_fetch_response_provenance()
        log: list[str] = [f"repair attempt {attempt}/{retries} date={date_text}"]
        df, status = fetcher.fetch_price_for_date(date_text, log, deadline=time.monotonic() + 240)
        attempt_provenance = fetcher.fetch_response_provenance()
        for row in attempt_provenance:
            row["attempt"] = attempt
        provenance.extend(attempt_provenance)
        stale_report: dict[str, Any] = {}
        if not df.empty:
            df, stale_report = fetcher.detect_stale_markets_against_previous(df, date_text, log)
            status["total_rows"] = int(len(df))
            status["twse_rows"] = int((df["market"].astype(str) == "TWSE").sum()) if "market" in df.columns else 0
            status["tpex_rows"] = int((df["market"].astype(str) == "TPEx").sum()) if "market" in df.columns else 0
            status["twse_ok"] = status["twse_rows"] >= fetcher.MIN_TWSE_ROWS
            status["tpex_ok"] = status["tpex_rows"] >= fetcher.MIN_TPEX_ROWS
            status["full_market_ok"] = (
                bool(status["twse_ok"])
                and bool(status["tpex_ok"])
                and int(status["total_rows"]) >= fetcher.MIN_FULL_ROWS
                and not stale_report.get("stale_markets")
            )
            status["stale_markets"] = stale_report.get("stale_markets", [])
            status["data_quality_note"] = stale_report.get("data_quality_note", "")
        status["fetch_response_provenance"] = list(provenance)
        last_df = df
        last_status = status
        last_log = log
        if status.get("full_market_ok"):
            return df, status, log
        if attempt < retries:
            time.sleep(sleep_seconds)
    return last_df, last_status, last_log


def check_code_row(df: pd.DataFrame, check_code: str, date_text: str) -> dict[str, Any]:
    stock_col = "stock_id" if "stock_id" in df.columns else "ticker" if "ticker" in df.columns else ""
    if not stock_col or not check_code:
        return {
            "date": date_text,
            "stock_id": check_code,
            "found": False,
            "stock_name": "",
            "market": "",
            "open": "",
            "high": "",
            "low": "",
            "close": "",
            "volume": "",
            "trading_value": "",
        }
    matched = df[df[stock_col].astype(str).str.zfill(4).eq(check_code.zfill(4))]
    if matched.empty:
        return {
            "date": date_text,
            "stock_id": check_code.zfill(4),
            "found": False,
            "stock_name": "",
            "market": "",
            "open": "",
            "high": "",
            "low": "",
            "close": "",
            "volume": "",
            "trading_value": "",
        }
    row = matched.iloc[0]
    name_col = "stock_name" if "stock_name" in matched.columns else "name" if "name" in matched.columns else ""
    return {
        "date": safe_str(row.get("date", date_text)),
        "stock_id": safe_str(row.get(stock_col, check_code.zfill(4))).zfill(4),
        "found": True,
        "stock_name": safe_str(row.get(name_col, "")) if name_col else "",
        "market": safe_str(row.get("market", "")),
        "open": safe_str(row.get("open", "")),
        "high": safe_str(row.get("high", "")),
        "low": safe_str(row.get("low", "")),
        "close": safe_str(row.get("close", "")),
        "volume": safe_str(row.get("volume", "")),
        "trading_value": safe_str(row.get("trading_value", row.get("turnover", ""))),
    }


def build_markdown(rows: list[dict[str, Any]], check_rows: list[dict[str, Any]], args: argparse.Namespace) -> str:
    repaired_count = sum(1 for row in rows if row.get("status") == "repaired")
    failed_count = sum(1 for row in rows if row.get("status") == "failed")
    skipped_count = sum(1 for row in rows if safe_str(row.get("status")).startswith("skipped"))
    lines = [
        "# Repair Daily Price Range Report",
        "",
        f"- mode: `{'selected_dates' if safe_str(getattr(args, 'dates', '')) else 'date_range'}`",
        f"- selected_dates: `{safe_str(getattr(args, 'dates', ''))}`",
        f"- start_date: `{safe_str(getattr(args, 'start_date', ''))}`",
        f"- end_date: `{safe_str(getattr(args, 'end_date', ''))}`",
        f"- source_base_sha: `{safe_str(getattr(args, 'source_base_sha', ''))}`",
        f"- check_code: `{args.check_code}`",
        f"- repaired_count: `{repaired_count}`",
        f"- skipped_count: `{skipped_count}`",
        f"- failed_count: `{failed_count}`",
        "",
        "## Repair Results",
        "",
        "| date | status | twse_rows | tpex_rows | total_rows | price_sha256 | reason | saved_files |",
        "|---|---|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    safe_str(row.get("date")),
                    safe_str(row.get("status")),
                    safe_str(row.get("twse_rows")),
                    safe_str(row.get("tpex_rows")),
                    safe_str(row.get("total_rows")),
                    safe_str(row.get("price_sha256")),
                    safe_str(row.get("reason")),
                    safe_str(row.get("saved_files")),
                ]
            )
            + " |"
        )
    if check_rows:
        lines.extend(
            [
                "",
                f"## Check Code {args.check_code}",
                "",
                "| date | found | stock_id | stock_name | market | open | high | low | close | volume | trading_value |",
                "|---|---|---|---|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in check_rows:
            lines.append(
                "| "
                + " | ".join(
                    [
                        safe_str(row.get("date")),
                        safe_str(row.get("found")),
                        safe_str(row.get("stock_id")),
                        safe_str(row.get("stock_name")),
                        safe_str(row.get("market")),
                        safe_str(row.get("open")),
                        safe_str(row.get("high")),
                        safe_str(row.get("low")),
                        safe_str(row.get("close")),
                        safe_str(row.get("volume")),
                        safe_str(row.get("trading_value")),
                    ]
                )
                + " |"
            )
    return "\n".join(lines) + "\n"


def _repository_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
        timeout=15,
    )
    if result.returncode != 0:
        raise ValueError("cannot resolve repository HEAD for selected-date repair")
    return result.stdout.strip()


def validate_selected_canonical_name_sources(
    root: Path, source_base_sha: str
) -> list[dict[str, str]]:
    """Bind selected-date stock names to four materialized source-base blobs."""

    root = root.resolve()
    configured = tuple(
        Path(path).as_posix() for path in fetcher.CANONICAL_STOCK_NAME_SOURCES
    )
    if configured != SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS:
        raise ValueError(
            "selected-date canonical stock-name source configuration is not exact"
        )
    evidence: list[dict[str, str]] = []
    for path_text in SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS:
        full_path = (root / path_text).resolve()
        try:
            full_path.relative_to(root)
        except ValueError as exc:
            raise ValueError(
                f"selected-date canonical stock-name source escapes repository: {path_text}"
            ) from exc
        current = root
        for part in Path(path_text).parts:
            current = current / part
            if current.is_symlink():
                raise ValueError(
                    f"selected-date canonical stock-name source is symlinked: {path_text}"
                )
        if not full_path.is_file():
            raise ValueError(
                f"selected-date canonical stock-name source is not materialized: {path_text}"
            )

        blob_result = subprocess.run(
            ["git", "rev-parse", f"{source_base_sha}:{path_text}"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        expected_blob_sha = blob_result.stdout.strip()
        if blob_result.returncode != 0 or not re.fullmatch(
            r"[0-9a-f]{40}", expected_blob_sha
        ):
            raise ValueError(
                f"selected-date canonical stock-name source is not tracked at source base: {path_text}"
            )
        observed_blob_result = subprocess.run(
            ["git", "hash-object", "--", path_text],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=15,
        )
        observed_blob_sha = observed_blob_result.stdout.strip()
        git_payload_result = subprocess.run(
            ["git", "show", f"{source_base_sha}:{path_text}"],
            cwd=root,
            capture_output=True,
            check=False,
            timeout=15,
        )
        if (
            observed_blob_result.returncode != 0
            or observed_blob_sha != expected_blob_sha
            or git_payload_result.returncode != 0
        ):
            raise ValueError(
                f"selected-date canonical stock-name source differs from source-base blob: {path_text}"
            )
        evidence.append(
            {
                "path": path_text,
                "git_blob_sha": expected_blob_sha,
                "git_blob_raw_sha256": sha256_bytes(git_payload_result.stdout),
            }
        )
    return evidence


def _report_payloads(
    rows: list[dict[str, Any]],
    check_rows: list[dict[str, Any]],
    args: argparse.Namespace,
    *,
    selected_dates: list[str],
    expected_date_contracts: dict[str, tuple[str, int]] | None = None,
    canonical_name_source_bindings: list[dict[str, str]] | None = None,
) -> dict[Path, bytes]:
    result_df = pd.DataFrame(rows)
    check_df = pd.DataFrame(check_rows)
    report = {
        "schema_version": "repair_daily_price_range_v2",
        "mode": "selected_dates" if selected_dates else "date_range",
        "source_base_sha": safe_str(getattr(args, "source_base_sha", "")),
        "selected_dates": selected_dates,
        "expected_date_contracts": [
            {
                "date": date_text,
                "sha256": contract[0],
                "row_count": contract[1],
            }
            for date_text, contract in sorted((expected_date_contracts or {}).items())
        ],
        "rows": rows,
        "check_rows": check_rows,
    }
    if selected_dates:
        report["canonical_stock_name_source_bindings"] = (
            canonical_name_source_bindings or []
        )
    return {
        REPORT_CSV: dataframe_csv_bytes(result_df),
        CHECK_CSV: dataframe_csv_bytes(check_df),
        REPORT_JSON: (json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"),
        REPORT_MD: build_markdown(rows, check_rows, args).encode("utf-8"),
    }


def run_selected_dates(
    args: argparse.Namespace,
    *,
    fetch_func=fetch_with_retry,
    fail_after_replace: int = 0,
) -> int:
    selected_dates = parse_selected_dates(args.dates)
    if not selected_dates:
        raise ValueError("selected-date mode requires at least one date")
    if len(selected_dates) > args.max_days:
        raise ValueError(
            f"selected-date count too large: {len(selected_dates)} > max_days {args.max_days}"
        )
    if safe_str(args.start_date) or safe_str(args.end_date):
        raise ValueError("--dates is mutually exclusive with --start-date/--end-date")
    expected_contracts = parse_expected_date_contracts(
        getattr(args, "expected_date_contract", None)
    )
    if not expected_contracts:
        raise ValueError(
            "selected-date mode requires expected date contracts for every selected date"
        )
    if set(expected_contracts) != set(selected_dates):
        raise ValueError(
            "expected date contracts must bind every and only selected date: "
            f"missing={sorted(set(selected_dates) - set(expected_contracts))} "
            f"unexpected={sorted(set(expected_contracts) - set(selected_dates))}"
        )
    source_base_sha = safe_str(args.source_base_sha)
    if not source_base_sha:
        raise ValueError("selected-date mode requires source_base_sha")
    if not re.fullmatch(r"[0-9a-f]{40}", source_base_sha):
        raise ValueError("source_base_sha must be a lowercase 40-character git SHA")
    if _repository_head(Path.cwd()) != source_base_sha:
        raise ValueError("selected-date repair source_base_sha does not equal repository HEAD")
    canonical_name_source_bindings = validate_selected_canonical_name_sources(
        Path.cwd(), source_base_sha
    )

    rows: list[dict[str, Any]] = []
    check_rows: list[dict[str, Any]] = []
    payloads: dict[Path, bytes] = {}
    previous_exact_mode = fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = True
    try:
        for date_text in selected_dates:
            print(f"Repairing selected date {date_text}...")
            df, status, log = fetch_func(date_text, args.retries, args.sleep_seconds)
            if not status.get("full_market_ok"):
                reason = status.get("data_quality_note") or "; ".join(log[-5:])
                raise ValueError(f"selected-date official fetch failed {date_text}: {reason}")
            csv_payload = dataframe_csv_bytes(df)
            projection = fetcher._price_projection(csv_payload, date_text)
            if (
                projection["twse_rows"] < fetcher.MIN_TWSE_ROWS
                or projection["tpex_rows"] < fetcher.MIN_TPEX_ROWS
                or projection["total_rows"] < fetcher.MIN_FULL_ROWS
            ):
                raise ValueError(f"selected-date full-market projection is insufficient: {date_text}")
            if expected_contracts:
                expected_sha, expected_rows = expected_contracts[date_text]
                observed_sha = sha256_bytes(csv_payload)
                observed_rows = int(projection["total_rows"])
                if observed_sha != expected_sha or observed_rows != expected_rows:
                    raise ValueError(
                        "selected-date normalized official source drift: "
                        f"date={date_text} expected_sha256={expected_sha} "
                        f"observed_sha256={observed_sha} expected_rows={expected_rows} "
                        f"observed_rows={observed_rows}"
                    )
            canonical = DATA_DIR / f"daily_price_{date_text}.csv"
            legacy = DATA_DIR / f"{date_text}.csv"
            payloads[canonical] = csv_payload
            payloads[legacy] = csv_payload
            row = {
                "date": date_text,
                "status": "repaired",
                "twse_rows": projection["twse_rows"],
                "tpex_rows": projection["tpex_rows"],
                "total_rows": projection["total_rows"],
                "reason": status.get("data_quality_note") or "full_market_ok_exact_historical_date",
                "saved_files": ";".join([legacy.as_posix(), canonical.as_posix()]),
                "canonical_path": canonical.as_posix(),
                "legacy_path": legacy.as_posix(),
                "price_sha256": sha256_bytes(csv_payload),
                "fetch_response_provenance": status.get("fetch_response_provenance", []),
            }
            rows.append(row)
            if args.check_code:
                check_rows.append(check_code_row(df, args.check_code, date_text))
    finally:
        fetcher.REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = previous_exact_mode

    report_payloads = _report_payloads(
        rows,
        check_rows,
        args,
        selected_dates=selected_dates,
        expected_date_contracts=expected_contracts,
        canonical_name_source_bindings=canonical_name_source_bindings,
    )
    payloads.update(report_payloads)
    publish_payloads_transaction(
        Path.cwd(),
        payloads,
        fail_after_replace=fail_after_replace,
    )
    print(
        "Saved exact selected-date repair: "
        f"dates={','.join(selected_dates)} files={len(selected_dates) * 2}"
    )
    return 0


def run(args: argparse.Namespace) -> int:
    if safe_str(getattr(args, "dates", "")):
        return run_selected_dates(args)
    if not safe_str(args.start_date) or not safe_str(args.end_date):
        raise ValueError("range mode requires --start-date and --end-date")
    start_dt = parse_yyyymmdd(args.start_date)
    end_dt = parse_yyyymmdd(args.end_date)
    if end_dt < start_dt:
        raise ValueError("end_date must be >= start_date")
    day_count = (end_dt - start_dt).days + 1
    if day_count > args.max_days:
        raise ValueError(f"date range too large: {day_count} days > max_days {args.max_days}")

    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []
    check_rows: list[dict[str, Any]] = []
    non_trading_days = continuity.load_non_trading_days(ROOT, continuity.NON_TRADING_DAYS)

    current = start_dt
    while current <= end_dt:
        date_text = yyyymmdd(current)
        if current.weekday() >= 5 or date_text in non_trading_days:
            rows.append(
                {
                    "date": date_text,
                    "status": "skipped_non_trading_day",
                    "twse_rows": 0,
                    "tpex_rows": 0,
                    "total_rows": 0,
                    "reason": "weekend" if current.weekday() >= 5 else "shared market calendar",
                    "saved_files": "",
                }
            )
            current += timedelta(days=1)
            continue

        print(f"Repairing {date_text}...")
        df, status, log = fetch_with_retry(date_text, args.retries, args.sleep_seconds)
        if status.get("full_market_ok"):
            saved_files = write_daily_price_files(df, date_text)
            price_payload = saved_files[0].read_bytes()
            rows.append(
                {
                    "date": date_text,
                    "status": "repaired",
                    "twse_rows": status.get("twse_rows", 0),
                    "tpex_rows": status.get("tpex_rows", 0),
                    "total_rows": status.get("total_rows", 0),
                    "reason": status.get("data_quality_note") or "full_market_ok",
                    "saved_files": ";".join(path.as_posix() for path in saved_files),
                    "price_sha256": sha256_bytes(price_payload),
                    "fetch_response_provenance": status.get("fetch_response_provenance", []),
                }
            )
            if args.check_code:
                check_rows.append(check_code_row(df, args.check_code, date_text))
        else:
            rows.append(
                {
                    "date": date_text,
                    "status": "failed",
                    "twse_rows": status.get("twse_rows", 0),
                    "tpex_rows": status.get("tpex_rows", 0),
                    "total_rows": status.get("total_rows", 0),
                    "reason": status.get("data_quality_note") or "; ".join(log[-5:]),
                    "saved_files": "",
                }
            )
        current += timedelta(days=1)

    result_df = pd.DataFrame(rows)
    result_df.to_csv(REPORT_CSV, index=False, encoding="utf-8-sig")
    check_df = pd.DataFrame(check_rows)
    check_df.to_csv(CHECK_CSV, index=False, encoding="utf-8-sig")
    REPORT_JSON.write_text(
        json.dumps({"rows": rows, "check_rows": check_rows}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    REPORT_MD.write_text(build_markdown(rows, check_rows, args), encoding="utf-8")

    failed = [row for row in rows if row.get("status") == "failed"]
    if failed:
        for row in failed:
            print(f"ERROR: repair failed {row['date']}: {row.get('reason')}")
        return 1
    print(f"Saved repair report: {REPORT_MD}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Repair official daily price files for a date range.")
    parser.add_argument("--approved-tpex-nine-row-manifest", type=Path)
    parser.add_argument("--nine-row-index-temp", type=Path)
    parser.add_argument("--start-date", default="")
    parser.add_argument("--end-date", default="")
    parser.add_argument(
        "--dates",
        default="",
        help="Exact ascending comma/space-separated dates. Mutually exclusive with range mode.",
    )
    parser.add_argument(
        "--source-base-sha",
        default="",
        help="Optional exact repository HEAD binding required by controlled selected-date workflows.",
    )
    parser.add_argument(
        "--expected-date-contract",
        action="append",
        default=None,
        help=(
            "Optional selected-date input binding in YYYYMMDD:sha256:row_count form. "
            "May be repeated; when present it must cover every and only --dates values."
        ),
    )
    parser.add_argument("--check-code", default="")
    parser.add_argument("--max-days", type=int, default=120)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--sleep-seconds", type=float, default=5.0)
    parser.add_argument(
        "--market-session-already-refreshed",
        action="store_true",
        help="Internal use by shared repair orchestrators after official source refresh.",
    )
    return parser.parse_args()


def _refresh_range_market_session() -> dict[str, Any]:
    """Refresh the current-session gate for legacy range repair only."""

    return market_session_calendar.refresh_market_session_status(
        ROOT,
        phase="preflight",
    )


def main() -> int:
    args = parse_args()
    manifest_path = getattr(args, "approved_tpex_nine_row_manifest", None)
    if manifest_path:
        if not args.nine_row_index_temp or any((args.start_date, args.end_date, args.dates)):
            raise ValueError("nine-row mode requires an explicit index temp and no date/range mode")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        print(json.dumps(stage_tpex_nine_row_repair(ROOT, manifest, args.nine_row_index_temp), ensure_ascii=False, indent=2))
        return 0
    if safe_str(getattr(args, "dates", "")):
        # Historical selected-date repair must not mutate today's market-session surface.
        return run(args)
    if not args.market_session_already_refreshed:
        try:
            status = _refresh_range_market_session()
        except Exception as exc:
            print(f"ERROR: market session refresh failed before range repair: {exc}")
            return 1
        if (
            status.get("market_status") == market_session_calendar.UNKNOWN
            and status.get("reason_code") != "awaiting_official_price_confirmation"
        ):
            print(
                "ERROR: range repair stopped because market status is unknown: "
                f"reason_code={status.get('reason_code')} reason={status.get('reason')}"
            )
            return 1
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
