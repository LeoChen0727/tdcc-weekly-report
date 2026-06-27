from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import validate_daily_price_history_continuity as continuity


REPORT_JSON = Path("output/latest/daily_price_source_recovery_latest.json")
REPORT_MD = Path("output/latest/daily_price_source_recovery_latest.md")
OFFICIAL_FETCH_JSON = Path("output/latest/official_price_fetch_latest.json")


@dataclass(frozen=True)
class RecoveryResult:
    status: str
    report: dict[str, Any]
    errors: list[str]


RepairFunc = Callable[[Path, str, argparse.Namespace], int]


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_date(value: object) -> str:
    text = re.sub(r"[^0-9]", "", safe_str(value))
    return text if re.fullmatch(r"20\d{6}", text) else ""


def daily_price_file(root: Path, date_text: str) -> Path:
    return root / continuity.DAILY_PRICE_DIR / f"daily_price_{date_text}.csv"


def legacy_daily_price_file(root: Path, date_text: str) -> Path:
    return root / continuity.DAILY_PRICE_DIR / f"{date_text}.csv"


def load_official_fetch_saved_date(root: Path, fetch_json_path: Path = OFFICIAL_FETCH_JSON) -> str:
    path = root / fetch_json_path
    if not path.exists():
        return ""
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return ""
    return normalize_date(payload.get("saved_price_date"))


def latest_daily_price_file_date(root: Path) -> str:
    dates: list[str] = []
    price_dir = root / continuity.DAILY_PRICE_DIR
    if not price_dir.exists():
        return ""
    for path in price_dir.glob("daily_price_*.csv"):
        match = re.fullmatch(r"daily_price_(20\d{6})\.csv", path.name)
        if match:
            dates.append(match.group(1))
    return max(dates) if dates else ""


def determine_required_end_date(root: Path, freshness_path: Path) -> tuple[str, dict[str, str]]:
    candidates: dict[str, str] = {}
    try:
        candidates["main_price_date"] = continuity.load_main_price_date(root, freshness_path)
    except Exception:
        candidates["main_price_date"] = ""
    candidates["official_fetch_saved_price_date"] = load_official_fetch_saved_date(root)
    candidates["latest_daily_price_file_date"] = latest_daily_price_file_date(root)
    valid_dates = [date for date in candidates.values() if normalize_date(date)]
    return (max(valid_dates) if valid_dates else "", candidates)


def expected_dates_for_recovery(
    root: Path,
    *,
    required_end_date: str,
    lookback_days: int,
    non_trading_days_path: Path,
) -> list[str]:
    non_trading_days = continuity.load_non_trading_days(root, non_trading_days_path)
    return continuity.expected_trading_dates(required_end_date, lookback_days, non_trading_days)


def classify_missing_files(root: Path, expected_dates: list[str]) -> tuple[list[str], list[str]]:
    legacy_only: list[str] = []
    missing: list[str] = []
    for date_text in expected_dates:
        if daily_price_file(root, date_text).exists():
            continue
        if legacy_daily_price_file(root, date_text).exists():
            legacy_only.append(date_text)
        else:
            missing.append(date_text)
    return legacy_only, missing


def canonicalize_legacy_files(root: Path, dates: list[str]) -> list[dict[str, str]]:
    actions: list[dict[str, str]] = []
    for date_text in dates:
        source = legacy_daily_price_file(root, date_text)
        target = daily_price_file(root, date_text)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        actions.append(
            {
                "date": date_text,
                "action": "copied_legacy_to_canonical",
                "source": source.relative_to(root).as_posix(),
                "target": target.relative_to(root).as_posix(),
            }
        )
    return actions


def default_repair_func(root: Path, date_text: str, args: argparse.Namespace) -> int:
    command = [
        sys.executable,
        "scripts/repair_daily_price_range.py",
        "--start-date",
        date_text,
        "--end-date",
        date_text,
        "--max-days",
        "1",
        "--retries",
        str(args.retries),
        "--sleep-seconds",
        str(args.sleep_seconds),
    ]
    if args.check_code:
        command.extend(["--check-code", args.check_code])
    completed = subprocess.run(command, cwd=root, check=False)
    return int(completed.returncode)


def repair_missing_dates(
    root: Path,
    dates: list[str],
    args: argparse.Namespace,
    repair_func: RepairFunc,
) -> tuple[list[dict[str, str]], list[str]]:
    actions: list[dict[str, str]] = []
    errors: list[str] = []
    for date_text in dates:
        return_code = repair_func(root, date_text, args)
        action = {
            "date": date_text,
            "action": "repair_daily_price_range",
            "return_code": str(return_code),
            "target": daily_price_file(root, date_text).relative_to(root).as_posix(),
        }
        actions.append(action)
        if return_code != 0:
            errors.append(f"{date_text}: repair_daily_price_range failed with exit code {return_code}")
        elif not daily_price_file(root, date_text).exists():
            errors.append(f"{date_text}: repair completed but canonical daily price file is still missing")
    return actions, errors


def validate_recovered_dates(root: Path, dates: list[str], min_full_rows: int) -> list[str]:
    if not dates:
        return []
    errors, _ = continuity.validate_daily_price_files(root, sorted(set(dates)), min_full_rows)
    return errors


def recover(
    root: Path,
    *,
    freshness_path: Path = continuity.DATA_FRESHNESS,
    lookback_days: int = continuity.DEFAULT_LOOKBACK_DAYS,
    min_full_rows: int = continuity.DEFAULT_MIN_FULL_ROWS,
    non_trading_days_path: Path = continuity.NON_TRADING_DAYS,
    max_repair_dates: int = 3,
    args: argparse.Namespace | None = None,
    repair_func: RepairFunc = default_repair_func,
) -> RecoveryResult:
    args = args or argparse.Namespace(retries=2, sleep_seconds=5.0, check_code="")
    root = root.resolve()
    errors: list[str] = []
    required_end_date, date_candidates = determine_required_end_date(root, freshness_path)
    if not required_end_date:
        report = {
            "status": "fail",
            "date_candidates": date_candidates,
            "errors": ["no usable daily price recovery end date found"],
        }
        return RecoveryResult("fail", report, report["errors"])

    expected_dates = expected_dates_for_recovery(
        root,
        required_end_date=required_end_date,
        lookback_days=lookback_days,
        non_trading_days_path=non_trading_days_path,
    )
    legacy_only, missing = classify_missing_files(root, expected_dates)
    actions: list[dict[str, str]] = []

    if len(missing) > max_repair_dates:
        errors.append(
            "missing daily price files exceed automatic recovery limit: "
            f"missing={len(missing)} max_repair_dates={max_repair_dates}"
        )
    else:
        actions.extend(canonicalize_legacy_files(root, legacy_only))
        repair_actions, repair_errors = repair_missing_dates(root, missing, args, repair_func)
        actions.extend(repair_actions)
        errors.extend(repair_errors)
        errors.extend(validate_recovered_dates(root, [*legacy_only, *missing], min_full_rows))

    _, missing_after = classify_missing_files(root, expected_dates)
    if missing_after:
        errors.append(f"canonical daily price files still missing after recovery: {', '.join(missing_after)}")

    status = "pass"
    if errors:
        status = "fail"
    elif actions:
        status = "repaired"

    report = {
        "status": status,
        "required_end_date": required_end_date,
        "date_candidates": date_candidates,
        "lookback_days": lookback_days,
        "expected_trading_dates": expected_dates,
        "legacy_only_before": legacy_only,
        "missing_before": missing,
        "missing_after": missing_after,
        "actions": actions,
        "errors": errors,
    }
    return RecoveryResult(status, report, errors)


def write_reports(root: Path, report: dict[str, Any]) -> None:
    latest_dir = root / "output" / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    (root / REPORT_JSON).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Daily Price Source Recovery",
        "",
        f"- status: `{report.get('status')}`",
        f"- required_end_date: `{report.get('required_end_date', '')}`",
        f"- lookback_days: `{report.get('lookback_days', '')}`",
        f"- expected_trading_date_count: `{len(report.get('expected_trading_dates', []))}`",
        f"- legacy_only_before: `{', '.join(report.get('legacy_only_before', []))}`",
        f"- missing_before: `{', '.join(report.get('missing_before', []))}`",
        f"- missing_after: `{', '.join(report.get('missing_after', []))}`",
        "",
        "## Date Candidates",
        "",
    ]
    for key, value in report.get("date_candidates", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Actions", ""])
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
        lines.append("No recovery action was required.")
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
            "Repair missing canonical daily price files before stock history build. "
            "This only repairs missing source files; the continuity validator remains the hard quality gate."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--freshness-csv", default=continuity.DATA_FRESHNESS.as_posix())
    parser.add_argument("--lookback-days", type=int, default=continuity.DEFAULT_LOOKBACK_DAYS)
    parser.add_argument("--min-full-rows", type=int, default=continuity.DEFAULT_MIN_FULL_ROWS)
    parser.add_argument("--non-trading-days", default=continuity.NON_TRADING_DAYS.as_posix())
    parser.add_argument("--max-repair-dates", type=int, default=3)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--sleep-seconds", type=float, default=5.0)
    parser.add_argument("--check-code", default="")
    parser.add_argument("--no-write-report", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    result = recover(
        root,
        freshness_path=Path(args.freshness_csv),
        lookback_days=args.lookback_days,
        min_full_rows=args.min_full_rows,
        non_trading_days_path=Path(args.non_trading_days),
        max_repair_dates=args.max_repair_dates,
        args=args,
    )
    if not args.no_write_report:
        write_reports(root, result.report)
    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "daily price source recovery completed: "
        f"status={result.status}, "
        f"required_end_date={result.report.get('required_end_date')}, "
        f"missing_before={len(result.report.get('missing_before', []))}, "
        f"missing_after={len(result.report.get('missing_after', []))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
