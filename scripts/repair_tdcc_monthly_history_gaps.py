from __future__ import annotations

import argparse
import json
import math
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

import backfill_tdcc_history as backfill
from tracking_utils import normalize_code, normalize_date, now_text, read_csv, write_csv


TDCC_HISTORY_DIR = backfill.TDCC_HISTORY_DIR
LATEST_DIR = backfill.LATEST_DIR
REPORT_JSON = LATEST_DIR / "tdcc_monthly_history_gap_repair_latest.json"
REPORT_MD = LATEST_DIR / "tdcc_monthly_history_gap_repair_latest.md"

SUMMARY_COLUMNS = backfill.SUMMARY_COLUMNS


@dataclass(frozen=True)
class MissingTdccRows:
    date: str
    missing_stock_ids: list[str]
    existing_rows: int


def parse_yyyymmdd(value: str) -> datetime:
    normalized = normalize_date(value)
    if len(normalized) != 8:
        raise ValueError(f"date must be YYYYMMDD, got: {value!r}")
    return datetime.strptime(normalized, "%Y%m%d")


def default_as_of_date() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")


def current_week_start(as_of_date: str) -> datetime:
    day = parse_yyyymmdd(as_of_date)
    return day - timedelta(days=day.weekday())


def current_month_tdcc_dates_excluding_current_week(
    available_dates: list[str],
    as_of_date: str,
) -> list[str]:
    as_of = parse_yyyymmdd(as_of_date)
    week_start = current_week_start(as_of_date)
    month_prefix = as_of.strftime("%Y%m")
    targets: list[str] = []
    for value in available_dates:
        normalized = normalize_date(value)
        if len(normalized) != 8 or not normalized.startswith(month_prefix):
            continue
        day = parse_yyyymmdd(normalized)
        if day < week_start:
            targets.append(normalized)
    return sorted(set(targets))


def read_summary_snapshot(date: str) -> pd.DataFrame:
    path = TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{normalize_date(date)}.csv"
    df = read_csv(path, dtype=str)
    if df.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    for col in SUMMARY_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["date"] = df["date"].map(normalize_date)
    df["code"] = df["code"].map(normalize_code)
    return df[SUMMARY_COLUMNS]


def find_missing_rows(target_dates: list[str], stock_ids: list[str]) -> list[MissingTdccRows]:
    wanted = [normalize_code(stock_id) for stock_id in stock_ids if normalize_code(stock_id)]
    missing: list[MissingTdccRows] = []
    for date in target_dates:
        snapshot = read_summary_snapshot(date)
        existing = set(snapshot.get("code", pd.Series(dtype=str)).map(normalize_code))
        missing_ids = [stock_id for stock_id in wanted if stock_id not in existing]
        if missing_ids:
            missing.append(
                MissingTdccRows(
                    date=normalize_date(date),
                    missing_stock_ids=missing_ids,
                    existing_rows=int(len(snapshot)),
                )
            )
    return missing


def fetch_missing_tdcc_rows(
    session: requests.Session,
    missing_rows: list[MissingTdccRows],
    name_map: dict[str, str],
    max_requests: int,
    sleep_seconds: float,
) -> list[dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    request_count = 0
    for item in missing_rows:
        for stock_id in item.missing_stock_ids:
            if max_requests and request_count >= max_requests:
                actions.append(
                    {
                        "date": item.date,
                        "stock_id": stock_id,
                        "status": "skipped_request_cap",
                        "message": f"reached max_requests={max_requests}",
                    }
                )
                continue
            if backfill.stock_date_already_present(stock_id, item.date):
                actions.append(
                    {
                        "date": item.date,
                        "stock_id": stock_id,
                        "status": "skipped_existing",
                        "message": "",
                    }
                )
                continue
            request_count += 1
            try:
                table = backfill.fetch_stock_distribution(session, stock_id, item.date)
                if table.empty:
                    raise RuntimeError("empty distribution table")
                summary = backfill.summarize_distribution(
                    table,
                    item.date,
                    stock_id,
                    name_map.get(stock_id, ""),
                )
                if any(math.isnan(backfill.to_number(summary.get(f"over_{threshold}_pct"))) for threshold in backfill.THRESHOLD_LEVEL_START):
                    raise RuntimeError("invalid threshold summary")
                backfill.write_summary_row(summary)
                backfill.write_raw_stock_rows(stock_id, item.date, table)
                actions.append(
                    {
                        "date": item.date,
                        "stock_id": stock_id,
                        "stock_name": name_map.get(stock_id, ""),
                        "status": "repaired",
                        "message": "",
                    }
                )
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
            except Exception as exc:
                actions.append(
                    {
                        "date": item.date,
                        "stock_id": stock_id,
                        "stock_name": name_map.get(stock_id, ""),
                        "status": "failed",
                        "message": str(exc),
                    }
                )
    return actions


def missing_rows_to_dicts(missing_rows: list[MissingTdccRows]) -> list[dict[str, Any]]:
    return [
        {
            "date": item.date,
            "missing_stock_count": len(item.missing_stock_ids),
            "existing_rows": item.existing_rows,
            "missing_stock_ids": item.missing_stock_ids,
        }
        for item in missing_rows
    ]


def write_report(report: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# TDCC Monthly History Gap Repair",
        "",
        f"- status: `{report['status']}`",
        f"- generated_at: `{report['generated_at']}`",
        f"- as_of_date: `{report['as_of_date']}`",
        f"- current_week_start: `{report['current_week_start']}`",
        f"- universe: `{report['universe']}`",
        f"- stocks_selected: {report['stocks_selected']}",
        f"- target_dates: {', '.join(report['target_dates']) if report['target_dates'] else 'none'}",
        f"- missing_date_count_before: {report['missing_date_count_before']}",
        f"- missing_stock_rows_before: {report['missing_stock_rows_before']}",
        f"- repair_action_count: {report['repair_action_count']}",
        f"- repaired_count: {report['repaired_count']}",
        f"- failed_count: {report['failed_count']}",
        f"- missing_date_count_after: {report['missing_date_count_after']}",
        f"- missing_stock_rows_after: {report['missing_stock_rows_after']}",
        "",
        "## Notes",
        "",
        "- Target dates come from the official TDCC query form and are limited to the current calendar month before the current ISO week.",
        "- The current week is excluded so this maintenance workflow does not assume the newest weekly TDCC date is already available.",
        "- This repair only fills missing TDCC history rows for the selected TDCC report universe.",
        "",
    ]
    if report.get("missing_before"):
        lines.extend(["## Missing Before", ""])
        for item in report["missing_before"]:
            lines.append(
                f"- `{item['date']}`: missing_stock_count={item['missing_stock_count']} "
                f"existing_rows={item['existing_rows']}"
            )
        lines.append("")
    if report.get("actions"):
        lines.extend(["## Actions", ""])
        for item in report["actions"][:80]:
            lines.append(
                f"- `{item.get('date', '')}` `{item.get('stock_id', '')}` "
                f"{item.get('status', '')}: {item.get('message', '')}"
            )
        if len(report["actions"]) > 80:
            lines.append(f"- ... {len(report['actions']) - 80} more actions")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def repair_tdcc_monthly_gaps(
    *,
    as_of_date: str,
    universe: str,
    max_stocks: int,
    max_requests: int,
    sleep_seconds: float,
    dry_run: bool,
    write_report_file: bool,
    available_dates_func: Callable[[requests.Session], list[str]] | None = None,
    repair_func: Callable[[requests.Session, list[MissingTdccRows], dict[str, str], int, float], list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    as_of = normalize_date(as_of_date) or default_as_of_date()
    session = requests.Session()
    if available_dates_func is None:
        def available_dates_func(session: requests.Session) -> list[str]:
            _token, _uri, _fir_date, dates = backfill.fetch_query_form(session)
            return dates
    dates = available_dates_func(session)
    target_dates = current_month_tdcc_dates_excluding_current_week(dates, as_of)
    name_map = backfill.load_name_map()
    limit = None if max_stocks == 0 else max_stocks
    stock_ids = backfill.load_universe(name_map, universe, limit, [])
    missing_before = find_missing_rows(target_dates, stock_ids)
    missing_stock_rows_before = sum(len(item.missing_stock_ids) for item in missing_before)

    actions: list[dict[str, Any]] = []
    if missing_before and not dry_run:
        fetcher = repair_func or fetch_missing_tdcc_rows
        actions = fetcher(session, missing_before, name_map, max_requests, sleep_seconds)

    missing_after = missing_before if dry_run else find_missing_rows(target_dates, stock_ids)
    missing_stock_rows_after = sum(len(item.missing_stock_ids) for item in missing_after)
    failed_count = sum(1 for item in actions if item.get("status") in {"failed", "skipped_request_cap"})
    repaired_count = sum(1 for item in actions if item.get("status") == "repaired")
    status = "pass"
    if dry_run:
        status = "dry_run"
    elif failed_count or missing_stock_rows_after:
        status = "fail"
    elif repaired_count:
        status = "repaired"

    report = {
        "status": status,
        "generated_at": now_text(),
        "as_of_date": as_of,
        "current_week_start": current_week_start(as_of).strftime("%Y%m%d"),
        "universe": universe,
        "max_stocks": max_stocks,
        "max_requests": max_requests,
        "dry_run": dry_run,
        "stocks_selected": len(stock_ids),
        "target_dates": target_dates,
        "available_dates_in_month_excluding_current_week": target_dates,
        "missing_date_count_before": len(missing_before),
        "missing_stock_rows_before": missing_stock_rows_before,
        "missing_before": missing_rows_to_dicts(missing_before),
        "repair_action_count": len(actions),
        "repaired_count": repaired_count,
        "failed_count": failed_count,
        "actions": actions,
        "missing_date_count_after": len(missing_after),
        "missing_stock_rows_after": missing_stock_rows_after,
        "missing_after": missing_rows_to_dicts(missing_after),
    }
    if write_report_file:
        write_report(report)
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repair missing current-month TDCC weekly history rows, excluding the current week."
    )
    parser.add_argument("--as-of-date", default="", help="YYYYMMDD boundary date. Default: Asia/Taipei today.")
    parser.add_argument(
        "--universe",
        default="chatgpt-top",
        choices=["chatgpt-top", "top", "candidates", "signals", "all-known", "explicit"],
        help="TDCC stock universe to check and repair. Default: chatgpt-top.",
    )
    parser.add_argument("--max-stocks", type=int, default=80, help="Maximum stocks to check. Use 0 for no limit.")
    parser.add_argument("--max-requests", type=int, default=500, help="Maximum TDCC HTTP requests. Use 0 for no cap.")
    parser.add_argument("--sleep", type=float, default=0.15, help="Seconds to sleep between successful TDCC requests.")
    parser.add_argument("--dry-run", action="store_true", help="Detect gaps without repairing or rebuilding TDCC history.")
    parser.add_argument("--no-write-report", action="store_true", help="Do not write latest JSON/MD evidence artifacts.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = repair_tdcc_monthly_gaps(
        as_of_date=args.as_of_date or default_as_of_date(),
        universe=args.universe,
        max_stocks=args.max_stocks,
        max_requests=args.max_requests,
        sleep_seconds=args.sleep,
        dry_run=args.dry_run,
        write_report_file=not args.no_write_report,
    )
    print(
        "TDCC monthly history gap repair completed: "
        f"status={report['status']}, "
        f"as_of_date={report['as_of_date']}, "
        f"target_dates={len(report['target_dates'])}, "
        f"missing_before={report['missing_stock_rows_before']}, "
        f"missing_after={report['missing_stock_rows_after']}, "
        f"repair_action_count={report['repair_action_count']}"
    )
    return 1 if report["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
