from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import repair_missing_daily_price_files as recovery
from scripts import validate_daily_price_history_continuity as continuity


REPORT_JSON = Path("output/latest/recent_daily_price_gap_repair_latest.json")
REPORT_MD = Path("output/latest/recent_daily_price_gap_repair_latest.md")
TAIPEI_TZ = ZoneInfo("Asia/Taipei")


@dataclass(frozen=True)
class RecentGapRepairResult:
    status: str
    report: dict[str, Any]
    errors: list[str]


BuildHistoryFunc = Callable[[Path, argparse.Namespace], int]


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_date(value: object) -> str:
    text = re.sub(r"[^0-9]", "", safe_str(value))
    return text if re.fullmatch(r"20\d{6}", text) else ""


def current_taipei_date() -> str:
    return datetime.now(TAIPEI_TZ).strftime("%Y%m%d")


def previous_trading_date_before(
    as_of_date: str,
    non_trading_days: set[str],
    *,
    max_backtrack_days: int = 30,
) -> str:
    """Return the latest expected trading day before as_of_date.

    as_of_date is only a maintenance boundary. It must not become the formal
    daily report date.
    """
    date_text = normalize_date(as_of_date)
    if not date_text:
        raise ValueError(f"invalid as_of_date: {as_of_date!r}")
    current = continuity.parse_yyyymmdd(date_text) - timedelta(days=1)
    for _ in range(max_backtrack_days):
        candidate = continuity.yyyymmdd(current)
        if current.weekday() < 5 and candidate not in non_trading_days:
            return candidate
        current -= timedelta(days=1)
    raise ValueError(
        "no prior trading date found before "
        f"{date_text} within max_backtrack_days={max_backtrack_days}"
    )


def expected_recent_trading_dates(
    as_of_date: str,
    lookback_days: int,
    non_trading_days: set[str],
) -> tuple[str, list[str]]:
    target_end_date = previous_trading_date_before(as_of_date, non_trading_days)
    expected_dates = continuity.expected_trading_dates(target_end_date, lookback_days, non_trading_days)
    return target_end_date, expected_dates


def default_build_history_func(root: Path, args: argparse.Namespace) -> int:
    completed = subprocess.run(
        [sys.executable, "scripts/build_stock_price_history.py"],
        cwd=root,
        check=False,
    )
    return int(completed.returncode)


def repair_recent_gaps(
    root: Path,
    *,
    as_of_date: str = "",
    lookback_days: int = 7,
    min_full_rows: int = continuity.DEFAULT_MIN_FULL_ROWS,
    non_trading_days_path: Path = continuity.NON_TRADING_DAYS,
    max_repair_dates: int = 5,
    rebuild_history_if_repaired: bool = False,
    args: argparse.Namespace | None = None,
    repair_func: recovery.RepairFunc = recovery.default_repair_func,
    build_history_func: BuildHistoryFunc = default_build_history_func,
) -> RecentGapRepairResult:
    args = args or argparse.Namespace(retries=2, sleep_seconds=5.0, check_code="")
    root = root.resolve()
    as_of_date = normalize_date(as_of_date) or current_taipei_date()
    errors: list[str] = []

    try:
        non_trading_days = continuity.load_non_trading_days(root, non_trading_days_path)
        target_end_date, expected_dates = expected_recent_trading_dates(as_of_date, lookback_days, non_trading_days)
    except Exception as exc:
        report = {
            "status": "fail",
            "as_of_date": as_of_date,
            "errors": [str(exc)],
        }
        return RecentGapRepairResult("fail", report, report["errors"])

    legacy_only, missing = recovery.classify_missing_files(root, expected_dates)
    actions: list[dict[str, str]] = []
    rebuild_history_status = "not_requested"
    rebuild_history_return_code = ""

    if len(missing) > max_repair_dates:
        errors.append(
            "missing daily price files exceed recent gap repair limit: "
            f"missing={len(missing)} max_repair_dates={max_repair_dates}"
        )
    else:
        actions.extend(recovery.canonicalize_legacy_files(root, legacy_only))
        repair_actions, repair_errors = recovery.repair_missing_dates(root, missing, args, repair_func)
        actions.extend(repair_actions)
        errors.extend(repair_errors)
        errors.extend(recovery.validate_recovered_dates(root, [*legacy_only, *missing], min_full_rows))

    _, missing_after = recovery.classify_missing_files(root, expected_dates)
    if missing_after:
        errors.append(f"canonical daily price files still missing after recent repair: {', '.join(missing_after)}")

    if rebuild_history_if_repaired:
        if actions and not errors:
            return_code = build_history_func(root, args)
            rebuild_history_return_code = str(return_code)
            rebuild_history_status = "completed" if return_code == 0 else "failed"
            if return_code != 0:
                errors.append(f"stock price history rebuild failed with exit code {return_code}")
        elif actions:
            rebuild_history_status = "skipped_due_to_repair_errors"
        else:
            rebuild_history_status = "skipped_no_repair_actions"

    status = "pass"
    if errors:
        status = "fail"
    elif actions:
        status = "repaired"

    report = {
        "status": status,
        "as_of_date": as_of_date,
        "date_boundary": "exclude_as_of_date",
        "target_end_date": target_end_date,
        "lookback_days": lookback_days,
        "expected_trading_dates": expected_dates,
        "non_trading_days_in_window": [
            date
            for date in sorted(non_trading_days)
            if expected_dates and expected_dates[0] <= date <= expected_dates[-1] and continuity.is_weekday(date)
        ],
        "legacy_only_before": legacy_only,
        "missing_before": missing,
        "missing_after": missing_after,
        "actions": actions,
        "rebuild_history_if_repaired": rebuild_history_if_repaired,
        "rebuild_history_status": rebuild_history_status,
        "rebuild_history_return_code": rebuild_history_return_code,
        "errors": errors,
    }
    return RecentGapRepairResult(status, report, errors)


def write_reports(root: Path, report: dict[str, Any]) -> None:
    latest_dir = root / "output" / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    (root / REPORT_JSON).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Recent Daily Price Gap Repair",
        "",
        f"- status: `{report.get('status')}`",
        f"- as_of_date: `{report.get('as_of_date', '')}`",
        f"- date_boundary: `{report.get('date_boundary', '')}`",
        f"- target_end_date: `{report.get('target_end_date', '')}`",
        f"- lookback_days: `{report.get('lookback_days', '')}`",
        f"- expected_trading_dates: `{', '.join(report.get('expected_trading_dates', []))}`",
        f"- non_trading_days_in_window: `{', '.join(report.get('non_trading_days_in_window', []))}`",
        f"- missing_before: `{', '.join(report.get('missing_before', []))}`",
        f"- missing_after: `{', '.join(report.get('missing_after', []))}`",
        f"- rebuild_history_status: `{report.get('rebuild_history_status', '')}`",
        "",
        "## Actions",
        "",
    ]
    actions = report.get("actions", [])
    if actions:
        lines.extend(["| date | action | result | target |", "|---|---|---|---|"])
        for action in actions:
            lines.append(
                "| "
                + " | ".join(
                    [
                        safe_str(action.get("date")),
                        safe_str(action.get("action")),
                        safe_str(action.get("return_code", "ok")),
                        safe_str(action.get("target")),
                    ]
                )
                + " |"
            )
    else:
        lines.append("No recent daily price gap repair action was required.")
    errors = report.get("errors", [])
    if errors:
        lines.extend(["", "## Errors", ""])
        for error in errors:
            lines.append(f"- {error}")
    lines.append("")
    (root / REPORT_MD).write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Proactively repair recent missing official daily price files before report generation. "
            "The as-of date is only used to exclude the current day; it is not a formal report date."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--as-of-date", default="", help="YYYYMMDD maintenance boundary. Default: today Asia/Taipei.")
    parser.add_argument("--lookback-days", type=int, default=7)
    parser.add_argument("--min-full-rows", type=int, default=continuity.DEFAULT_MIN_FULL_ROWS)
    parser.add_argument("--non-trading-days", default=continuity.NON_TRADING_DAYS.as_posix())
    parser.add_argument("--max-repair-dates", type=int, default=5)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--sleep-seconds", type=float, default=5.0)
    parser.add_argument("--check-code", default="")
    parser.add_argument("--rebuild-history-if-repaired", action="store_true")
    parser.add_argument("--no-write-report", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    result = repair_recent_gaps(
        root,
        as_of_date=args.as_of_date,
        lookback_days=args.lookback_days,
        min_full_rows=args.min_full_rows,
        non_trading_days_path=Path(args.non_trading_days),
        max_repair_dates=args.max_repair_dates,
        rebuild_history_if_repaired=args.rebuild_history_if_repaired,
        args=args,
    )
    if not args.no_write_report:
        write_reports(root, result.report)
    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "recent daily price gap repair completed: "
        f"status={result.status}, "
        f"as_of_date={result.report.get('as_of_date')}, "
        f"target_end_date={result.report.get('target_end_date')}, "
        f"missing_before={len(result.report.get('missing_before', []))}, "
        f"missing_after={len(result.report.get('missing_after', []))}, "
        f"rebuild_history_status={result.report.get('rebuild_history_status')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
