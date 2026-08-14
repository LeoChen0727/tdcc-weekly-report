from __future__ import annotations

import argparse
import hashlib
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

import fetch_official_daily_price as official_price_fetch

from scripts import repair_missing_daily_price_files as recovery
import scripts.market_session_calendar as market_session_calendar
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
ContinuityValidateFunc = Callable[..., continuity.ValidationResult]


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_date(value: object) -> str:
    text = re.sub(r"[^0-9]", "", safe_str(value))
    return text if re.fullmatch(r"20\d{6}", text) else ""


def current_taipei_date() -> str:
    return datetime.now(TAIPEI_TZ).strftime("%Y%m%d")


def latest_trading_date_on_or_before(
    as_of_date: str,
    non_trading_days: set[str],
    *,
    include_as_of_date: bool = True,
    max_backtrack_days: int = 30,
) -> str:
    """Return the latest expected trading day on or before as_of_date.

    Production repair includes the current boundary date so an evening repair
    can acquire an absent current-day source. Callers may explicitly retain the
    legacy exclusive boundary for diagnostics only.
    """
    date_text = normalize_date(as_of_date)
    if not date_text:
        raise ValueError(f"invalid as_of_date: {as_of_date!r}")
    current = continuity.parse_yyyymmdd(date_text)
    if not include_as_of_date:
        current -= timedelta(days=1)
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
    *,
    include_as_of_date: bool = True,
) -> tuple[str, list[str]]:
    target_end_date = latest_trading_date_on_or_before(
        as_of_date,
        non_trading_days,
        include_as_of_date=include_as_of_date,
    )
    expected_dates = continuity.expected_trading_dates(target_end_date, lookback_days, non_trading_days)
    return target_end_date, expected_dates


def default_build_history_func(root: Path, args: argparse.Namespace) -> int:
    completed = subprocess.run(
        [sys.executable, "scripts/build_stock_price_history.py"],
        cwd=root,
        check=False,
    )
    return int(completed.returncode)


def _load_current_day_repair_evidence(
    root: Path,
    date_text: str,
    *,
    require_repair_report: bool,
) -> tuple[dict[str, Any], bytes]:
    report_path = root / "output/latest/repair_daily_price_range_latest.json"
    rows: object = []
    if report_path.exists():
        if not report_path.is_file() or report_path.is_symlink():
            raise ValueError(
                "current-day repair range-repair report is unsafe"
            )
        report_payload = json.loads(
            report_path.read_text(encoding="utf-8-sig")
        )
        rows = report_payload.get("rows")
    matches = [
        row
        for row in rows if isinstance(rows, list) and isinstance(row, dict)
        and normalize_date(row.get("date")) == date_text
    ] if isinstance(rows, list) else []
    if require_repair_report and (
        len(matches) != 1 or matches[0].get("status") != "repaired"
    ):
        raise ValueError("current-day repair report lacks one exact repaired row")
    if len(matches) > 1:
        raise ValueError("current-day repair report has duplicate date rows")
    row = matches[0] if matches and matches[0].get("status") == "repaired" else {}
    expected_files = {
        f"data/daily_price/{date_text}.csv",
        f"data/daily_price/daily_price_{date_text}.csv",
    }
    saved_files = {item for item in safe_str(row.get("saved_files")).split(";") if item}
    if row and saved_files != expected_files:
        raise ValueError(
            f"current-day repair saved-file identity mismatch: expected={sorted(expected_files)} "
            f"observed={sorted(saved_files)}"
        )
    payloads: list[bytes] = []
    for relative_path in sorted(expected_files):
        path = root / relative_path
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"current-day repair output is missing or unsafe: {relative_path}")
        payloads.append(path.read_bytes())
    if payloads[0] != payloads[1]:
        raise ValueError("current-day repair canonical and legacy price bytes differ")
    if not row:
        projection = official_price_fetch._price_projection(
            payloads[0], date_text
        )
        row = {
            "date": date_text,
            "status": "verified_existing_canonical",
            "saved_files": ";".join(sorted(expected_files)),
            "twse_rows": projection["twse_rows"],
            "tpex_rows": projection["tpex_rows"],
            "total_rows": projection["total_rows"],
        }
    return row, payloads[0]


def publish_current_day_repair_confirmation(
    root: Path,
    *,
    date_text: str,
    market_session_fetch_bytes: market_session_calendar.FetchBytes | None = None,
    fail_after_evidence_replace: int = 0,
    require_repair_report: bool = True,
    min_full_rows: int = continuity.DEFAULT_MIN_FULL_ROWS,
    deferred_transaction: bool = False,
) -> tuple[dict[str, Any], bool]:
    row, price_payload = _load_current_day_repair_evidence(
        root,
        date_text,
        require_repair_report=require_repair_report,
    )
    transaction_pending = False
    if (
        int(row.get("twse_rows") or 0) < official_price_fetch.MIN_TWSE_ROWS
        or int(row.get("tpex_rows") or 0) < official_price_fetch.MIN_TPEX_ROWS
        or int(row.get("total_rows") or 0)
        < max(min_full_rows, official_price_fetch.MIN_FULL_ROWS)
    ):
        raise ValueError(
            "current-day official price confirmation lacks full-market row coverage"
        )
    canonical_path = root / f"data/daily_price/daily_price_{date_text}.csv"
    previous_paths = sorted(
        (
            path
            for path in (root / "data/daily_price").glob("*.csv")
            if official_price_fetch.daily_file_date(path) < date_text
        ),
        key=official_price_fetch.daily_file_date,
    )
    quality_log: list[str] = []
    if not official_price_fetch.is_daily_file_quality_usable(
        canonical_path,
        previous_paths,
        quality_log,
    ):
        raise ValueError(
            "current-day official price confirmation failed full-market quality: "
            + "; ".join(quality_log)
        )
    existing_ok, existing_confirmation, _ = (
        market_session_calendar.read_official_price_confirmation(root, date_text)
    )
    if (
        existing_ok
        and existing_confirmation.get("price_sha256")
        == hashlib.sha256(price_payload).hexdigest()
        and int(existing_confirmation.get("twse_rows") or 0)
        >= official_price_fetch.MIN_TWSE_ROWS
        and int(existing_confirmation.get("tpex_rows") or 0)
        >= official_price_fetch.MIN_TPEX_ROWS
        and int(existing_confirmation.get("total_rows") or 0)
        >= official_price_fetch.MIN_FULL_ROWS
    ):
        published = json.loads(
            (root / market_session_calendar.OFFICIAL_PRICE_FETCH_STATUS).read_text(
                encoding="utf-8-sig"
            )
        )
    else:
        status = {
            "generated_at": datetime.now(TAIPEI_TZ).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
            "target_date": date_text,
            "saved_price_date": date_text,
            "is_target_date": True,
            "result": "success_current_day_repair_full_market",
            "reason": "current-day range repair produced date-bound TWSE and TPEx evidence",
            "twse_rows": int(row.get("twse_rows") or 0),
            "tpex_rows": int(row.get("tpex_rows") or 0),
            "total_rows": int(row.get("total_rows") or 0),
            "full_market_ok": True,
            "attempts": [dict(row)],
            "paths": {
                "dated_csv": f"data/daily_price/{date_text}.csv",
                "dated_alt_csv": f"data/daily_price/daily_price_{date_text}.csv",
                "latest_csv": "output/latest/official_daily_price_latest.csv",
            },
        }
        published = official_price_fetch.publish_official_price_evidence_transaction(
            root,
            price_payload=price_payload,
            result=status,
            log=[f"current-day repair evidence date={date_text}"],
            fail_after_replace=fail_after_evidence_replace,
            deferred=deferred_transaction,
        )
        transaction_pending = deferred_transaction
    refresh_kwargs: dict[str, Any] = {
        "phase": "confirm",
        "assessment_date": date_text,
        "write_files": False,
    }
    if market_session_fetch_bytes is not None:
        refresh_kwargs["fetch_bytes"] = market_session_fetch_bytes
    try:
        market = market_session_calendar.refresh_market_session_status(root, **refresh_kwargs)
        if market.get("market_status") != market_session_calendar.OPEN_CONFIRMED:
            raise ValueError(
                "current-day repair evidence did not produce open_confirmed: "
                f"status={market.get('market_status')} reason={market.get('reason')}"
            )
    except Exception as exc:
        if transaction_pending:
            try:
                official_price_fetch.recover_official_price_evidence_transaction(root)
            except Exception as rollback_exc:
                raise RuntimeError(
                    "current-day confirmation failed and official latest rollback failed: "
                    f"original={exc}; rollback={rollback_exc}"
                ) from rollback_exc
        raise
    return (
        {
            "official_price_fetch": published,
            "market_session": market,
        },
        transaction_pending,
    )


def repair_recent_gaps(
    root: Path,
    *,
    as_of_date: str = "",
    lookback_days: int = 7,
    min_full_rows: int = continuity.DEFAULT_MIN_FULL_ROWS,
    non_trading_days_path: Path = continuity.NON_TRADING_DAYS,
    max_repair_dates: int = 5,
    include_as_of_date: bool = True,
    rebuild_history_if_repaired: bool = False,
    args: argparse.Namespace | None = None,
    repair_func: recovery.RepairFunc = recovery.default_repair_func,
    build_history_func: BuildHistoryFunc = default_build_history_func,
    continuity_validate_func: ContinuityValidateFunc = continuity.validate,
    market_session_fetch_bytes: market_session_calendar.FetchBytes | None = None,
    fail_after_evidence_replace: int = 0,
    authority_date: str = "",
) -> RecentGapRepairResult:
    args = args or argparse.Namespace(retries=2, sleep_seconds=5.0, check_code="")
    root = root.resolve()
    as_of_date = normalize_date(as_of_date) or current_taipei_date()
    authority_date = normalize_date(authority_date) or current_taipei_date()
    errors: list[str] = []

    try:
        official_price_fetch.recover_official_price_evidence_transaction(root)
    except Exception as exc:
        report = {
            "status": "fail",
            "as_of_date": as_of_date,
            "current_day_confirmation": {},
            "errors": [
                "official price evidence transaction recovery failed: " + str(exc)
            ],
        }
        return RecentGapRepairResult("fail", report, report["errors"])

    try:
        non_trading_days = continuity.load_non_trading_days(root, non_trading_days_path)
        target_end_date, expected_dates = expected_recent_trading_dates(
            as_of_date,
            lookback_days,
            non_trading_days,
            include_as_of_date=include_as_of_date,
        )
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

    current_day_confirmation: dict[str, Any] = {}
    current_day_authority = (
        not errors
        and as_of_date == authority_date
        and target_end_date == authority_date
    )
    if current_day_authority:
        transaction_pending = False
        try:
            prospective_confirmation, transaction_pending = publish_current_day_repair_confirmation(
                root,
                date_text=target_end_date,
                market_session_fetch_bytes=market_session_fetch_bytes,
                fail_after_evidence_replace=fail_after_evidence_replace,
                require_repair_report=target_end_date in missing,
                min_full_rows=min_full_rows,
                deferred_transaction=True,
            )
            initial_continuity = continuity_validate_func(
                root,
                main_price_date_override=target_end_date,
                lookback_days=lookback_days,
                min_full_rows=min_full_rows,
                non_trading_days_path=non_trading_days_path,
            )
            needs_history_rebuild = bool(actions) or bool(initial_continuity.errors)
            final_continuity = initial_continuity
            if rebuild_history_if_repaired and needs_history_rebuild:
                try:
                    return_code = build_history_func(root, args)
                except Exception as exc:
                    rebuild_history_return_code = "exception"
                    rebuild_history_status = "failed"
                    raise RuntimeError(
                        f"stock price history rebuild raised an exception: {exc}"
                    ) from exc
                rebuild_history_return_code = str(return_code)
                rebuild_history_status = "completed" if return_code == 0 else "failed"
                if return_code != 0:
                    raise RuntimeError(
                        f"stock price history rebuild failed with exit code {return_code}"
                    )
                final_continuity = continuity_validate_func(
                    root,
                    main_price_date_override=target_end_date,
                    lookback_days=lookback_days,
                    min_full_rows=min_full_rows,
                    non_trading_days_path=non_trading_days_path,
                )
            elif rebuild_history_if_repaired:
                rebuild_history_status = "skipped_history_current"
            if final_continuity.errors:
                raise ValueError(
                    "target-date stock price history continuity validation failed: "
                    + "; ".join(final_continuity.errors)
                )
            if transaction_pending:
                official_price_fetch.commit_official_price_evidence_transaction(root)
                transaction_pending = False
            current_day_confirmation = prospective_confirmation
        except Exception as exc:
            rollback_error = ""
            transaction_root = root / official_price_fetch.OFFICIAL_PRICE_TRANSACTION_DIR
            if transaction_pending or transaction_root.exists():
                try:
                    official_price_fetch.recover_official_price_evidence_transaction(root)
                except Exception as rollback_exc:
                    rollback_error = (
                        "; official latest rollback failed: " + str(rollback_exc)
                    )
            current_day_confirmation = {}
            errors.append(f"current-day official price confirmation failed: {exc}")
            if rollback_error:
                errors.append(rollback_error.lstrip("; "))

    if rebuild_history_if_repaired and not current_day_authority:
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
        "date_boundary": (
            "include_as_of_date_if_trading" if include_as_of_date else "exclude_as_of_date"
        ),
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
        "current_day_confirmation": current_day_confirmation,
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
            "Production includes the as-of date when it is a trading day so current-day source gaps can be repaired."
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
    parser.add_argument(
        "--exclude-as-of-date",
        action="store_true",
        help="Diagnostics only: retain the legacy exclusive maintenance boundary.",
    )
    parser.add_argument(
        "--skip-market-session-refresh",
        action="store_true",
        help="Diagnostics/tests only. Production repair must refresh official market-session sources.",
    )
    parser.add_argument("--no-write-report", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    if not args.skip_market_session_refresh:
        try:
            market_status = market_session_calendar.refresh_market_session_status(
                root,
                phase="preflight",
                write_files=False,
            )
        except Exception as exc:
            print(f"ERROR: market session refresh failed before recent gap repair: {exc}")
            return 1
        if (
            market_status.get("market_status") == market_session_calendar.UNKNOWN
            and market_status.get("reason_code") != "awaiting_official_price_confirmation"
        ):
            print(
                "ERROR: recent gap repair stopped because market status is unknown: "
                f"reason_code={market_status.get('reason_code')} "
                f"reason={market_status.get('reason')}"
            )
            return 1
    result = repair_recent_gaps(
        root,
        as_of_date=args.as_of_date,
        lookback_days=args.lookback_days,
        min_full_rows=args.min_full_rows,
        non_trading_days_path=Path(args.non_trading_days),
        max_repair_dates=args.max_repair_dates,
        include_as_of_date=not args.exclude_as_of_date,
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
