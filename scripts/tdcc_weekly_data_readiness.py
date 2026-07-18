from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

import backfill_tdcc_history as backfill


normalize_date = backfill.normalize_date
now_text = backfill.now_text


READINESS_JSON = Path("output/latest/tdcc_weekly_data_readiness_latest.json")
READINESS_MD = Path("output/latest/tdcc_weekly_data_readiness_latest.md")
TAIPEI = ZoneInfo("Asia/Taipei")


class TdccWeeklyDataNotReadyError(RuntimeError):
    pass


@dataclass(frozen=True)
class ReportWeek:
    start: str
    end: str


def parse_date(value: str) -> datetime:
    normalized = normalize_date(value)
    if len(normalized) != 8:
        raise ValueError(f"date must be YYYYMMDD, got {value!r}")
    return datetime.strptime(normalized, "%Y%m%d")


def taipei_today() -> str:
    return datetime.now(TAIPEI).strftime("%Y%m%d")


def expected_report_week(as_of_date: str) -> ReportWeek:
    """Return the latest report week whose Friday has passed or is imminent.

    Saturday/Sunday runs target the current Monday-Friday week. Monday-Friday
    retries target the previous completed Monday-Friday week.
    """

    as_of = parse_date(as_of_date)
    current_monday = as_of - timedelta(days=as_of.weekday())
    target_monday = current_monday if as_of.weekday() >= 5 else current_monday - timedelta(days=7)
    return ReportWeek(
        start=target_monday.strftime("%Y%m%d"),
        end=(target_monday + timedelta(days=4)).strftime("%Y%m%d"),
    )


def normalize_official_dates(values: list[str]) -> list[str]:
    return sorted(
        {
            normalized
            for value in values
            if len(normalized := normalize_date(value)) == 8
        }
    )


def select_official_date_for_week(official_dates: list[str], report_week: ReportWeek) -> str:
    candidates = [
        date
        for date in normalize_official_dates(official_dates)
        if report_week.start <= date <= report_week.end
    ]
    return candidates[-1] if candidates else ""


def build_readiness_report(
    *,
    as_of_date: str,
    official_dates: list[str],
    source_url: str = backfill.TDCC_QUERY_URL,
) -> dict[str, Any]:
    report_week = expected_report_week(as_of_date)
    normalized_dates = normalize_official_dates(official_dates)
    selected_date = select_official_date_for_week(normalized_dates, report_week)
    status = "pass" if selected_date else "waiting_for_official_period"
    return {
        "status": status,
        "generated_at": now_text(),
        "as_of_date": normalize_date(as_of_date),
        "timezone": "Asia/Taipei",
        "target_week_start": report_week.start,
        "target_week_end": report_week.end,
        "selected_official_date": selected_date,
        "latest_official_date": normalized_dates[-1] if normalized_dates else "",
        "previous_official_date": (
            normalized_dates[normalized_dates.index(selected_date) - 1]
            if selected_date and normalized_dates.index(selected_date) > 0
            else ""
        ),
        "official_dates": normalized_dates,
        "official_date_source": source_url,
        "date_contract": "official_tdcc_query_form_date_within_target_report_week",
    }


def write_readiness_report(report: dict[str, Any]) -> None:
    READINESS_JSON.parent.mkdir(parents=True, exist_ok=True)
    READINESS_JSON.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# TDCC Weekly Data Readiness",
        "",
        f"- status: `{report['status']}`",
        f"- generated_at: `{report['generated_at']}`",
        f"- as_of_date: `{report['as_of_date']}`",
        f"- target_week: `{report['target_week_start']} ~ {report['target_week_end']}`",
        f"- selected_official_date: `{report['selected_official_date'] or 'none'}`",
        f"- latest_official_date: `{report['latest_official_date'] or 'none'}`",
        f"- previous_official_date: `{report['previous_official_date'] or 'none'}`",
        f"- official_date_source: `{report['official_date_source']}`",
        "",
        "正式週報只能使用 target week 內由 TDCC 官方查詢頁列出的資料日期。",
        "若該期尚未出現，workflow 必須停止且由外部 orchestrator 稍後重試，不得沿用舊 snapshot。",
        "",
    ]
    READINESS_MD.write_text("\n".join(lines), encoding="utf-8")


def fetch_official_dates(session: requests.Session | None = None) -> list[str]:
    active_session = session or requests.Session()
    _token, _uri, _fir_date, dates = backfill.fetch_query_form(active_session)
    return dates


def ensure_weekly_data_ready(
    *,
    as_of_date: str,
    available_dates_func: Callable[[], list[str]] | None = None,
    write_report: bool = True,
) -> dict[str, Any]:
    dates = available_dates_func() if available_dates_func else fetch_official_dates()
    report = build_readiness_report(as_of_date=as_of_date, official_dates=dates)
    if write_report:
        write_readiness_report(report)
    if report["status"] != "pass":
        raise TdccWeeklyDataNotReadyError(
            "TDCC official period is not ready for target week "
            f"{report['target_week_start']}~{report['target_week_end']}; "
            f"latest_official_date={report['latest_official_date'] or 'none'}"
        )
    return report


def load_readiness(path: Path = READINESS_JSON) -> dict[str, Any]:
    if not path.exists():
        raise RuntimeError(f"TDCC weekly readiness artifact is missing: {path}")
    report = json.loads(path.read_text(encoding="utf-8"))
    if report.get("status") != "pass":
        raise RuntimeError(f"TDCC weekly readiness status is not pass: {report.get('status', '')}")
    selected_date = normalize_date(report.get("selected_official_date", ""))
    official_dates = normalize_official_dates(report.get("official_dates", []))
    if len(selected_date) != 8 or selected_date not in official_dates:
        raise RuntimeError("TDCC weekly readiness selected_official_date is invalid")
    report["selected_official_date"] = selected_date
    report["official_dates"] = official_dates
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Require an official TDCC data date in the expected report week before weekly production."
    )
    parser.add_argument("--as-of-date", default="", help="YYYYMMDD in Asia/Taipei; defaults to today.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = ensure_weekly_data_ready(as_of_date=args.as_of_date or taipei_today())
    except TdccWeeklyDataNotReadyError as exc:
        print(f"TDCC_DATA_NOT_READY: {exc}", file=sys.stderr)
        return 75
    except Exception as exc:
        print(f"TDCC_DATA_SOURCE_ERROR: {exc}", file=sys.stderr)
        return 1
    print(
        "TDCC weekly data readiness passed: "
        f"target_week={report['target_week_start']}~{report['target_week_end']} "
        f"selected_official_date={report['selected_official_date']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
