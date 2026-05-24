from __future__ import annotations

from pathlib import Path
from typing import Any
import argparse
import json

import pandas as pd

from tracking_utils import LATEST_DIR, now_text, read_csv, safe_str


COMPANY_EVENT_CALENDAR = Path("data/company_calendar/company_event_calendar.csv")
MACRO_EVENT_CALENDAR = Path("data/macro_events/macro_event_calendar.csv")
UPCOMING_COMPANY_CALENDAR = LATEST_DIR / "upcoming_catalyst_calendar_latest.csv"
UPCOMING_MACRO_CALENDAR = LATEST_DIR / "upcoming_macro_event_calendar_latest.csv"
UPCOMING_COMPANY_MD = LATEST_DIR / "upcoming_catalyst_calendar_latest.md"
UPCOMING_MACRO_MD = LATEST_DIR / "upcoming_macro_event_calendar_latest.md"
STATUS_JSON = LATEST_DIR / "calendar_data_source_status_latest.json"
STATUS_MD = LATEST_DIR / "calendar_data_source_status_latest.md"
README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
PACKET_TXT = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
VALIDATION_JSON = LATEST_DIR / "event_calendar_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "event_calendar_validation_latest.md"

COMPANY_REQUIRED = [
    "event_date",
    "event_end_date",
    "stock_id",
    "stock_name",
    "event_type",
    "event_status",
    "event_confidence",
    "catalyst_tags",
    "source",
    "source_url",
    "days_to_event",
    "proximity_bucket",
]

MACRO_REQUIRED = [
    "event_date",
    "event_name",
    "event_type",
    "region",
    "importance",
    "source",
    "source_url",
    "days_to_event",
    "proximity_bucket",
    "related_themes",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def missing_columns(df: pd.DataFrame, columns: list[str]) -> list[str]:
    return [col for col in columns if col not in df.columns]


def file_info(path: Path) -> dict[str, Any]:
    df = pd.DataFrame()
    if path.suffix.lower() == ".csv":
        df = read_csv(path, dtype=str)
    return {
        "path": path.as_posix(),
        "exists": path.exists(),
        "rows": int(len(df)),
        "size_bytes": path.stat().st_size if path.exists() else 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema-only", action="store_true")
    args = parser.parse_args()

    issues: list[str] = []
    company = read_csv(COMPANY_EVENT_CALENDAR, dtype=str)
    macro = read_csv(MACRO_EVENT_CALENDAR, dtype=str)
    upcoming_company = read_csv(UPCOMING_COMPANY_CALENDAR, dtype=str)
    upcoming_macro = read_csv(UPCOMING_MACRO_CALENDAR, dtype=str)

    for path in [COMPANY_EVENT_CALENDAR, MACRO_EVENT_CALENDAR, UPCOMING_COMPANY_CALENDAR, UPCOMING_MACRO_CALENDAR, STATUS_JSON, STATUS_MD]:
        if not path.exists():
            issues.append(f"missing_file:{path.as_posix()}")

    for col in missing_columns(company, COMPANY_REQUIRED):
        issues.append(f"company_calendar_missing_column:{col}")
    for col in missing_columns(macro, MACRO_REQUIRED):
        issues.append(f"macro_calendar_missing_column:{col}")
    for col in missing_columns(upcoming_company, COMPANY_REQUIRED):
        issues.append(f"upcoming_company_missing_column:{col}")
    for col in missing_columns(upcoming_macro, MACRO_REQUIRED):
        issues.append(f"upcoming_macro_missing_column:{col}")

    if not args.schema_only:
        if company.empty:
            issues.append("company_calendar_empty")
        if macro.empty:
            issues.append("macro_calendar_empty")
        if upcoming_company.empty:
            issues.append("upcoming_company_calendar_empty")
        if upcoming_macro.empty:
            issues.append("upcoming_macro_calendar_empty")

        readme = read_text(README_TXT)
        packet = read_text(PACKET_TXT)
        for field in [
            "company_event_calendar_raw_url",
            "macro_event_calendar_raw_url",
            "upcoming_catalyst_calendar_raw_url",
            "upcoming_macro_event_calendar_raw_url",
            "calendar_data_source_status_raw_url",
        ]:
            if readme and field not in readme:
                issues.append(f"readme_missing_field:{field}")
            if packet and field not in packet:
                issues.append(f"packet_missing_field:{field}")

    status = {
        "generated_at": now_text(),
        "status": "pass" if not issues else "fail",
        "schema_only": bool(args.schema_only),
        "issues": issues,
        "files": {
            "company_event_calendar": file_info(COMPANY_EVENT_CALENDAR),
            "macro_event_calendar": file_info(MACRO_EVENT_CALENDAR),
            "upcoming_company_calendar": file_info(UPCOMING_COMPANY_CALENDAR),
            "upcoming_macro_calendar": file_info(UPCOMING_MACRO_CALENDAR),
            "status_json": file_info(STATUS_JSON),
            "status_md": file_info(STATUS_MD),
        },
    }
    VALIDATION_JSON.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Event Calendar Validation",
        "",
        f"- generated_at: `{status['generated_at']}`",
        f"- status: `{status['status']}`",
        f"- schema_only: `{status['schema_only']}`",
        "",
        "| file | exists | rows | size_bytes |",
        "|---|---:|---:|---:|",
    ]
    for name, info in status["files"].items():
        lines.append(f"| {name} | {info['exists']} | {info['rows']} | {info['size_bytes']} |")
    lines.extend(["", "## Issues", ""])
    if issues:
        lines.extend(f"- {safe_str(issue)}" for issue in issues)
    else:
        lines.append("- none")
    VALIDATION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    print(f"status={status['status']}")
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
