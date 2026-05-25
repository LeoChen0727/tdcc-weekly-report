from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DAILY_SIGNALS_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    main_price_date_from_freshness,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
SIGNAL_LOG = DAILY_SIGNALS_DIR / "daily_candidate_signal_log.csv"
SIGNAL_LOG_ALIAS = HISTORY_DIR / "daily_candidates" / "daily_candidate_signal_log.csv"
REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
REPEAT_MD = LATEST_DIR / "candidate_repeat_appearance_latest.md"
VALIDATION_JSON = LATEST_DIR / "candidate_repeat_appearance_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "candidate_repeat_appearance_validation_latest.md"

REQUIRED_REPEAT_COLUMNS = {
    "signal_date",
    "stock_id",
    "stock_name",
    "consecutive_appear_days_any_category",
    "consecutive_appear_days_same_category",
    "appear_count_5d",
    "appear_count_10d",
    "appear_count_20d",
    "first_seen_date",
    "last_seen_date",
    "multi_category_flags",
    "repeat_appear_label",
    "repeat_appear_note",
}

REQUIRED_ALL_CANDIDATE_COLUMNS = REQUIRED_REPEAT_COLUMNS - {"stock_name"}


def inspect_csv(path: Path) -> pd.DataFrame:
    df = read_csv(path, dtype=str, keep_default_na=False)
    if not df.empty and "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_code)
    if not df.empty and "signal_date" in df.columns:
        df["signal_date"] = df["signal_date"].map(normalize_date)
    return df


def validate() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    main_date = main_price_date_from_freshness()

    log = inspect_csv(SIGNAL_LOG)
    alias = inspect_csv(SIGNAL_LOG_ALIAS)
    repeat = inspect_csv(REPEAT_CSV)
    all_candidates = inspect_csv(ALL_CANDIDATES)

    if log.empty:
        errors.append(f"missing or empty {SIGNAL_LOG}")
    if alias.empty:
        errors.append(f"missing or empty alias {SIGNAL_LOG_ALIAS}")
    if repeat.empty:
        errors.append(f"missing or empty {REPEAT_CSV}")
    if not REPEAT_MD.exists() or REPEAT_MD.stat().st_size < 200:
        errors.append(f"missing or too small {REPEAT_MD}")
    if all_candidates.empty:
        errors.append(f"missing or empty {ALL_CANDIDATES}")

    if not log.empty and main_date not in set(log.get("signal_date", pd.Series(dtype=str)).astype(str)):
        errors.append(f"{SIGNAL_LOG} does not contain main_price_date={main_date}")
    if not alias.empty and main_date not in set(alias.get("signal_date", pd.Series(dtype=str)).astype(str)):
        errors.append(f"{SIGNAL_LOG_ALIAS} does not contain main_price_date={main_date}")
    if not repeat.empty and main_date not in set(repeat.get("signal_date", pd.Series(dtype=str)).astype(str)):
        errors.append(f"{REPEAT_CSV} does not contain main_price_date={main_date}")

    if not repeat.empty:
        missing = REQUIRED_REPEAT_COLUMNS - set(repeat.columns)
        if missing:
            errors.append(f"{REPEAT_CSV} missing columns: {sorted(missing)}")
        duplicated = repeat.duplicated(subset=["signal_date", "stock_id"]).sum() if {"signal_date", "stock_id"} <= set(repeat.columns) else 0
        if duplicated:
            errors.append(f"{REPEAT_CSV} has duplicated signal_date + stock_id rows: {duplicated}")
        allowed = {
            "first_seen",
            "continued_2_3d",
            "continued_many_days",
            "repeated_but_no_breakout",
            "continued_overheated",
            "stale_signal",
        }
        if "repeat_appear_label" in repeat.columns:
            labels = set(safe_str(x) for x in repeat["repeat_appear_label"].tolist() if safe_str(x))
            unknown = labels - allowed
            if unknown:
                errors.append(f"{REPEAT_CSV} has unknown repeat_appear_label values: {sorted(unknown)}")

    if not all_candidates.empty:
        missing = REQUIRED_ALL_CANDIDATE_COLUMNS - set(all_candidates.columns)
        if missing:
            errors.append(f"{ALL_CANDIDATES} missing repeat appearance columns: {sorted(missing)}")
        if "date" in all_candidates.columns:
            dates = {normalize_date(x) for x in all_candidates["date"].tolist()}
            dates.discard("")
            if dates and main_date not in dates:
                errors.append(f"{ALL_CANDIDATES} date mismatch: main_price_date={main_date}, dates={sorted(dates)}")

    history_days = 0
    if not log.empty and "signal_date" in log.columns:
        history_days = len({safe_str(x) for x in log["signal_date"].tolist() if safe_str(x)})
        if history_days < 2:
            warnings.append("history_available_days < 2; repeat appearance labels are mostly first_seen")

    result = {
        "generated_at": now_text(),
        "status": "pass" if not errors else "fail",
        "main_price_date": main_date,
        "history_available_days": history_days,
        "files": {
            "signal_log": SIGNAL_LOG.as_posix(),
            "signal_log_alias": SIGNAL_LOG_ALIAS.as_posix(),
            "repeat_csv": REPEAT_CSV.as_posix(),
            "repeat_md": REPEAT_MD.as_posix(),
            "all_candidates": ALL_CANDIDATES.as_posix(),
        },
        "row_counts": {
            "signal_log": len(log),
            "signal_log_alias": len(alias),
            "repeat_csv": len(repeat),
            "all_candidates": len(all_candidates),
        },
        "checks": {
            "signal_log_exists": not log.empty,
            "signal_log_alias_exists": not alias.empty,
            "main_price_date_appended": not log.empty and main_date in set(log["signal_date"].astype(str)),
            "repeat_csv_exists": not repeat.empty,
            "repeat_columns_present": not repeat.empty and REQUIRED_REPEAT_COLUMNS <= set(repeat.columns),
            "all_candidates_repeat_columns_present": not all_candidates.empty and REQUIRED_ALL_CANDIDATE_COLUMNS <= set(all_candidates.columns),
            "no_duplicate_stock_day_in_repeat": not repeat.empty and not repeat.duplicated(subset=["signal_date", "stock_id"]).any(),
        },
        "errors": errors,
        "warnings": warnings,
    }
    return result


def write_outputs(result: dict[str, Any]) -> None:
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Candidate Repeat Appearance Validation",
        "",
        f"- generated_at: `{result.get('generated_at', '')}`",
        f"- status: `{result.get('status', '')}`",
        f"- main_price_date: `{result.get('main_price_date', '')}`",
        f"- history_available_days: `{result.get('history_available_days', '')}`",
        "",
        "## Files",
    ]
    for key, value in result.get("files", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Row Counts")
    for key, value in result.get("row_counts", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Checks")
    for key, value in result.get("checks", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.append("")
    lines.append("## Errors")
    if result.get("errors"):
        for error in result["errors"]:
            lines.append(f"- {error}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Warnings")
    if result.get("warnings"):
        for warning in result["warnings"]:
            lines.append(f"- {warning}")
    else:
        lines.append("- none")
    lines.append("")
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    result = validate()
    write_outputs(result)
    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    if result["status"] != "pass":
        for error in result["errors"]:
            print(f"ERROR: {error}")
        return 1
    print("Candidate repeat appearance validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
