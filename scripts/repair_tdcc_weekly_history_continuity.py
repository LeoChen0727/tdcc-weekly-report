from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import math
import sys
import threading
import time
from pathlib import Path
from typing import Any, Callable

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

import backfill_tdcc_history as backfill
import repair_tdcc_monthly_history_gaps as monthly_repair
from tdcc_weekly_data_readiness import load_readiness


normalize_code = backfill.normalize_code
normalize_date = backfill.normalize_date
now_text = backfill.now_text


def read_csv(path: Path, dtype: type | str = str) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=dtype)


REPORT_JSON = Path("output/latest/tdcc_weekly_history_continuity_latest.json")
REPORT_MD = Path("output/latest/tdcc_weekly_history_continuity_latest.md")
FULL_MARKET_CONTINUITY_BASELINE = "20260430"
DEFAULT_REQUIRED_PERIODS = 0
DEFAULT_RETRY_ATTEMPTS = 3
DEFAULT_WORKERS = 6


def current_snapshot_path(signal_date: str) -> Path:
    return backfill.TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{normalize_date(signal_date)}.csv"


def load_current_snapshot(signal_date: str) -> pd.DataFrame:
    path = current_snapshot_path(signal_date)
    snapshot = read_csv(path, dtype=str)
    if snapshot.empty or "code" not in snapshot.columns or "date" not in snapshot.columns:
        raise RuntimeError(f"current TDCC snapshot is missing or malformed: {path}")
    snapshot["code"] = snapshot["code"].map(normalize_code)
    snapshot["date"] = snapshot["date"].map(normalize_date)
    snapshot = snapshot[snapshot["code"].ne("") & snapshot["date"].eq(normalize_date(signal_date))]
    if snapshot.empty:
        raise RuntimeError(f"current TDCC snapshot does not contain signal_date={signal_date}: {path}")
    return snapshot.drop_duplicates("code", keep="last").reset_index(drop=True)


def required_official_dates(
    official_dates: list[str],
    signal_date: str,
    required_periods: int,
) -> list[str]:
    normalized = sorted({normalize_date(value) for value in official_dates if len(normalize_date(value)) == 8})
    signal_date = normalize_date(signal_date)
    if signal_date not in normalized:
        raise RuntimeError(f"signal_date={signal_date} is absent from official TDCC dates")
    eligible = [
        date
        for date in normalized
        if FULL_MARKET_CONTINUITY_BASELINE <= date <= signal_date
    ]
    if signal_date not in eligible:
        raise RuntimeError(
            f"signal_date={signal_date} predates full-market continuity baseline={FULL_MARKET_CONTINUITY_BASELINE}"
        )
    if required_periods > 0:
        return eligible[-max(2, required_periods) :]
    return eligible


def is_invalid_single_holder_table(table: pd.DataFrame) -> bool:
    if table.empty or table.shape[0] < 16 or table.shape[1] < 5:
        return False
    distribution_pct = pd.to_numeric(table.iloc[:15, -1], errors="coerce").fillna(0)
    non_zero = distribution_pct[distribution_pct > 0]
    if len(non_zero) != 1 or float(non_zero.iloc[0]) < 99.9:
        return False
    holder_counts = pd.to_numeric(table.iloc[:, 2], errors="coerce")
    active_index = int(non_zero.index[0])
    active_holders = holder_counts.loc[active_index] if active_index in holder_counts.index else math.nan
    total_holders = holder_counts.iloc[15]
    return bool(
        (pd.notna(active_holders) and float(active_holders) <= 1)
        or (pd.notna(total_holders) and float(total_holders) <= 1)
    )


def stock_name_map_from_snapshot(snapshot: pd.DataFrame) -> dict[str, str]:
    names = backfill.load_name_map()
    if "name" in snapshot.columns:
        for _, row in snapshot.iterrows():
            stock_id = normalize_code(row.get("code", ""))
            stock_name = str(row.get("name", "") or "").strip()
            if stock_id and stock_name:
                names[stock_id] = stock_name
    return names


def fetch_missing_with_retries(
    missing_rows: list[monthly_repair.MissingTdccRows],
    name_map: dict[str, str],
    *,
    retry_attempts: int,
    sleep_seconds: float,
    workers: int,
    fetch_func: Callable[[requests.Session, str, str], pd.DataFrame] | None = None,
) -> list[dict[str, Any]]:
    fetcher = fetch_func or backfill.fetch_stock_distribution
    write_lock = threading.Lock()
    tasks = [
        (missing.date, stock_id)
        for missing in missing_rows
        for stock_id in missing.missing_stock_ids
        if not backfill.stock_date_already_present(stock_id, missing.date)
    ]

    def fetch_one(date: str, stock_id: str) -> dict[str, Any]:
        session = requests.Session()
        last_error = ""
        empty_response_count = 0
        for attempt in range(1, max(1, retry_attempts) + 1):
            try:
                table = fetcher(session, stock_id, date)
                if table.empty:
                    empty_response_count += 1
                    raise RuntimeError("official query returned no distribution row")
                if is_invalid_single_holder_table(table):
                    return {
                        "date": date,
                        "stock_id": stock_id,
                        "stock_name": name_map.get(stock_id, ""),
                        "status": "invalid_holder_distribution",
                        "attempts": attempt,
                        "message": "single-holder or placeholder distribution",
                    }
                summary = backfill.summarize_distribution(
                    table,
                    date,
                    stock_id,
                    name_map.get(stock_id, ""),
                )
                if any(
                    math.isnan(backfill.to_number(summary.get(f"over_{threshold}_pct")))
                    for threshold in backfill.THRESHOLD_LEVEL_START
                ):
                    raise RuntimeError("invalid threshold summary")
                with write_lock:
                    backfill.write_summary_row(summary)
                    backfill.write_raw_stock_rows(stock_id, date, table)
                if sleep_seconds > 0:
                    time.sleep(sleep_seconds)
                return {
                    "date": date,
                    "stock_id": stock_id,
                    "stock_name": name_map.get(stock_id, ""),
                    "status": "repaired",
                    "attempts": attempt,
                    "message": "",
                }
            except Exception as exc:
                last_error = str(exc)
                if attempt < max(1, retry_attempts):
                    time.sleep(min(2.0, 0.25 * (2 ** (attempt - 1))))
        return {
            "date": date,
            "stock_id": stock_id,
            "stock_name": name_map.get(stock_id, ""),
            "status": (
                "official_no_data"
                if empty_response_count == max(1, retry_attempts)
                else "failed"
            ),
            "attempts": max(1, retry_attempts),
            "message": last_error,
        }

    actions: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        futures = {
            executor.submit(fetch_one, date, stock_id): (date, stock_id)
            for date, stock_id in tasks
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            actions.append(future.result())
            if completed % 50 == 0 or completed == len(futures):
                print(f"TDCC continuity backfill progress: {completed}/{len(futures)}")
    return sorted(actions, key=lambda item: (item["date"], item["stock_id"]))


def continuity_keys(items: list[monthly_repair.MissingTdccRows]) -> set[tuple[str, str]]:
    return {
        (item.date, stock_id)
        for item in items
        for stock_id in item.missing_stock_ids
    }


def write_report(report: dict[str, Any]) -> None:
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# TDCC Weekly History Continuity",
        "",
        f"- status: `{report['status']}`",
        f"- generated_at: `{report['generated_at']}`",
        f"- signal_date: `{report['signal_date']}`",
        f"- required_dates: `{', '.join(report['required_dates'])}`",
        f"- current_stock_count: {report['current_stock_count']}",
        f"- missing_rows_before: {report['missing_rows_before']}",
        f"- repaired_count: {report['repaired_count']}",
        f"- accepted_exception_count: {report['accepted_exception_count']}",
        f"- official_no_data_count: {report['official_no_data_count']}",
        f"- invalid_holder_distribution_count: {report['invalid_holder_distribution_count']}",
        f"- unresolved_missing_rows: {report['unresolved_missing_rows']}",
        "",
        "## Contract",
        "",
        "- Required dates come from the official TDCC query form, not filename spacing or computer date.",
        "- Missing historical rows are fetched before any 1w/2w/3w or consecutive calculation.",
        "- A systemic or unresolved history gap blocks report production; a confirmed per-stock history exception is recorded explicitly.",
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
        for item in report["actions"][:100]:
            lines.append(
                f"- `{item['date']}` `{item['stock_id']}` {item['status']} "
                f"attempts={item['attempts']}: {item['message']}"
            )
        if len(report["actions"]) > 100:
            lines.append(f"- ... {len(report['actions']) - 100} more actions")
        lines.append("")
    REPORT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def repair_weekly_history_continuity(
    *,
    required_periods: int = DEFAULT_REQUIRED_PERIODS,
    retry_attempts: int = DEFAULT_RETRY_ATTEMPTS,
    sleep_seconds: float = 0.15,
    workers: int = DEFAULT_WORKERS,
    write_report_file: bool = True,
    fetch_func: Callable[[requests.Session, str, str], pd.DataFrame] | None = None,
) -> dict[str, Any]:
    readiness = load_readiness()
    signal_date = readiness["selected_official_date"]
    required_dates = required_official_dates(
        readiness["official_dates"],
        signal_date,
        required_periods,
    )
    snapshot = load_current_snapshot(signal_date)
    stock_ids = sorted(set(snapshot["code"].map(normalize_code)) - {""})
    name_map = stock_name_map_from_snapshot(snapshot)
    missing_before = monthly_repair.find_missing_rows(required_dates, stock_ids)

    actions = fetch_missing_with_retries(
        missing_before,
        name_map,
        retry_attempts=retry_attempts,
        sleep_seconds=sleep_seconds,
        workers=workers,
        fetch_func=fetch_func,
    )
    missing_after = monthly_repair.find_missing_rows(required_dates, stock_ids)
    missing_after_keys = continuity_keys(missing_after)
    accepted_exceptions = {
        (item["date"], item["stock_id"])
        for item in actions
        if item.get("status") in {"official_no_data", "invalid_holder_distribution"}
    }
    unresolved = sorted(missing_after_keys - accepted_exceptions)
    history_exception_limit = max(5, math.ceil(len(stock_ids) * 0.01))
    official_no_data_count = sum(item.get("status") == "official_no_data" for item in actions)
    invalid_distribution_count = sum(
        item.get("status") == "invalid_holder_distribution" for item in actions
    )
    systemic_history_exception = len(accepted_exceptions) > history_exception_limit
    status = "pass"
    if unresolved or systemic_history_exception:
        status = "fail"
    elif any(item.get("status") == "repaired" for item in actions):
        status = "repaired"

    report = {
        "status": status,
        "generated_at": now_text(),
        "signal_date": signal_date,
        "readiness_path": str(Path("output/latest/tdcc_weekly_data_readiness_latest.json")),
        "required_periods": required_periods,
        "required_dates": required_dates,
        "current_stock_count": len(stock_ids),
        "missing_rows_before": sum(len(item.missing_stock_ids) for item in missing_before),
        "missing_before": monthly_repair.missing_rows_to_dicts(missing_before),
        "actions": actions,
        "repaired_count": sum(item.get("status") == "repaired" for item in actions),
        "failed_count": sum(item.get("status") == "failed" for item in actions),
        "accepted_exception_count": len(accepted_exceptions),
        "official_no_data_count": official_no_data_count,
        "invalid_holder_distribution_count": invalid_distribution_count,
        "confirmed_history_exceptions": [
            {"date": date, "stock_id": stock_id}
            for date, stock_id in sorted(accepted_exceptions)
        ],
        "history_exception_limit": history_exception_limit,
        "systemic_history_exception": systemic_history_exception,
        "missing_rows_after": sum(len(item.missing_stock_ids) for item in missing_after),
        "unresolved_missing_rows": len(unresolved),
        "unresolved": [
            {"date": date, "stock_id": stock_id}
            for date, stock_id in unresolved
        ],
    }
    if write_report_file:
        write_report(report)
    return report


def load_continuity_report(path: Path = REPORT_JSON) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"TDCC weekly continuity artifact is missing: {path}")
    report = json.loads(path.read_text(encoding="utf-8"))
    if report.get("status") not in {"pass", "repaired"}:
        raise RuntimeError(f"TDCC weekly continuity status is not pass: {report.get('status', '')}")
    if report.get("unresolved_missing_rows") != 0:
        raise RuntimeError("TDCC weekly continuity has unresolved missing rows")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repair official TDCC weekly history gaps before derived holder-flow calculations."
    )
    parser.add_argument("--required-periods", type=int, default=DEFAULT_REQUIRED_PERIODS)
    parser.add_argument("--retry-attempts", type=int, default=DEFAULT_RETRY_ATTEMPTS)
    parser.add_argument("--sleep", type=float, default=0.15)
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = repair_weekly_history_continuity(
            required_periods=args.required_periods,
            retry_attempts=args.retry_attempts,
            sleep_seconds=args.sleep,
            workers=args.workers,
        )
    except Exception as exc:
        print(f"TDCC_HISTORY_CONTINUITY_ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "TDCC weekly history continuity completed: "
        f"status={report['status']} signal_date={report['signal_date']} "
        f"missing_before={report['missing_rows_before']} repaired={report['repaired_count']} "
        f"unresolved={report['unresolved_missing_rows']}"
    )
    return 0 if report["status"] in {"pass", "repaired"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
