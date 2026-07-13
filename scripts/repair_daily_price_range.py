from __future__ import annotations

import argparse
import json
import sys
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


def parse_yyyymmdd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def yyyymmdd(value: datetime) -> str:
    return value.strftime("%Y%m%d")


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


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
    for attempt in range(1, retries + 1):
        log: list[str] = [f"repair attempt {attempt}/{retries} date={date_text}"]
        df, status = fetcher.fetch_price_for_date(date_text, log, deadline=time.monotonic() + 240)
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
        f"- start_date: `{args.start_date}`",
        f"- end_date: `{args.end_date}`",
        f"- check_code: `{args.check_code}`",
        f"- repaired_count: `{repaired_count}`",
        f"- skipped_count: `{skipped_count}`",
        f"- failed_count: `{failed_count}`",
        "",
        "## Repair Results",
        "",
        "| date | status | twse_rows | tpex_rows | total_rows | reason | saved_files |",
        "|---|---|---:|---:|---:|---|---|",
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


def run(args: argparse.Namespace) -> int:
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
            rows.append(
                {
                    "date": date_text,
                    "status": "repaired",
                    "twse_rows": status.get("twse_rows", 0),
                    "tpex_rows": status.get("tpex_rows", 0),
                    "total_rows": status.get("total_rows", 0),
                    "reason": status.get("data_quality_note") or "full_market_ok",
                    "saved_files": ";".join(path.as_posix() for path in saved_files),
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
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
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


def main() -> int:
    args = parse_args()
    if not args.market_session_already_refreshed:
        try:
            status = market_session_calendar.refresh_market_session_status(
                ROOT,
                phase="preflight",
            )
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
