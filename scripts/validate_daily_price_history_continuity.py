from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd


DEFAULT_LOOKBACK_DAYS = 20
DEFAULT_MIN_FULL_ROWS = 1300

DATA_FRESHNESS = Path("output/latest/data_freshness_latest.csv")
DAILY_PRICE_DIR = Path("data/daily_price")
STOCK_HISTORY_DIR = Path("data/stock_price_history")
NON_TRADING_DAYS = Path("config/twse_non_trading_days.csv")
LATEST_DIR = Path("output/latest")
REPORT_JSON = LATEST_DIR / "daily_price_history_continuity_latest.json"
REPORT_MD = LATEST_DIR / "daily_price_history_continuity_latest.md"

TARGET_STOCK_SOURCE_FILES = [
    Path("output/latest/daily_candidate_model_signals_latest.csv"),
    Path("output/latest/daily_candidate_model_signals_for_report_latest.csv"),
    Path("output/latest/daily_volume_breakout_operation_section_latest.csv"),
]


@dataclass
class ValidationResult:
    status: str
    report: dict[str, Any]
    errors: list[str]


def safe_str(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_stock_id(value: object) -> str:
    text = re.sub(r"[^0-9]", "", safe_str(value))
    if not text:
        return ""
    return text.zfill(4) if len(text) < 4 else text


def parse_yyyymmdd(value: str) -> datetime:
    return datetime.strptime(value, "%Y%m%d")


def yyyymmdd(value: datetime) -> str:
    return value.strftime("%Y%m%d")


def is_weekday(date_text: str) -> bool:
    return parse_yyyymmdd(date_text).weekday() < 5


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")


def load_main_price_date(root: Path, freshness_path: Path) -> str:
    path = root / freshness_path
    if not path.exists():
        raise FileNotFoundError(f"missing {path.as_posix()}")
    df = read_csv(path)
    if len(df) != 1:
        raise ValueError(f"{path.as_posix()} must contain exactly one row")
    main_date = safe_str(df.iloc[0].get("main_price_date"))
    if not re.fullmatch(r"\d{8}", main_date):
        raise ValueError(f"invalid main_price_date: {main_date!r}")
    return main_date


def load_non_trading_days(root: Path, path: Path) -> set[str]:
    full_path = root / path
    if not full_path.exists():
        return set()
    df = read_csv(full_path)
    if "date" not in df.columns:
        raise ValueError(f"{full_path.as_posix()} missing date column")
    dates = {safe_str(value) for value in df["date"]}
    invalid = sorted(date for date in dates if date and not re.fullmatch(r"\d{8}", date))
    if invalid:
        raise ValueError(f"{full_path.as_posix()} has invalid dates: {invalid[:10]}")
    return {date for date in dates if date}


def expected_trading_dates(main_price_date: str, lookback_days: int, non_trading_days: set[str]) -> list[str]:
    end = parse_yyyymmdd(main_price_date)
    start = end - timedelta(days=lookback_days)
    dates: list[str] = []
    current = start
    while current <= end:
        date_text = yyyymmdd(current)
        if current.weekday() < 5 and date_text not in non_trading_days:
            dates.append(date_text)
        current += timedelta(days=1)
    return dates


def daily_price_file(root: Path, date_text: str) -> Path:
    return root / DAILY_PRICE_DIR / f"daily_price_{date_text}.csv"


def normalize_market(value: object) -> str:
    text = safe_str(value)
    lowered = text.lower()
    if lowered in {"twse", "listed"}:
        return "TWSE"
    if lowered in {"tpex", "otc", "emerging"}:
        return "TPEx"
    return text


def read_daily_price_for_date(root: Path, date_text: str) -> pd.DataFrame:
    path = daily_price_file(root, date_text)
    if not path.exists():
        return pd.DataFrame()
    df = read_csv(path)
    if "date" in df.columns:
        df["_date_digits"] = df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
    else:
        df["_date_digits"] = ""
    stock_col = "stock_id" if "stock_id" in df.columns else "ticker" if "ticker" in df.columns else ""
    if stock_col:
        df["_stock_id"] = df[stock_col].map(normalize_stock_id)
    else:
        df["_stock_id"] = ""
    if "market" in df.columns:
        df["_market_norm"] = df["market"].map(normalize_market)
    else:
        df["_market_norm"] = ""
    return df


def validate_daily_price_files(
    root: Path,
    expected_dates: list[str],
    min_full_rows: int,
) -> tuple[list[str], dict[str, dict[str, Any]]]:
    errors: list[str] = []
    file_reports: dict[str, dict[str, Any]] = {}
    for date_text in expected_dates:
        path = daily_price_file(root, date_text)
        legacy_path = root / DAILY_PRICE_DIR / f"{date_text}.csv"
        if not path.exists():
            if legacy_path.exists():
                errors.append(
                    f"{date_text}: missing canonical daily_price_{date_text}.csv; legacy {date_text}.csv exists"
                )
            else:
                errors.append(f"{date_text}: missing daily price file")
            file_reports[date_text] = {
                "path": path.as_posix(),
                "exists": False,
                "legacy_exists": legacy_path.exists(),
            }
            continue
        df = read_daily_price_for_date(root, date_text)
        date_rows = df[df["_date_digits"].eq(date_text)].copy() if "_date_digits" in df.columns else pd.DataFrame()
        markets = sorted({normalize_market(value) for value in date_rows.get("_market_norm", pd.Series(dtype=str)) if safe_str(value)})
        stock_count = int(date_rows["_stock_id"].astype(str).str.len().gt(0).sum()) if "_stock_id" in date_rows.columns else 0
        file_reports[date_text] = {
            "path": path.as_posix(),
            "exists": True,
            "legacy_exists": legacy_path.exists(),
            "rows": int(len(df)),
            "date_rows": int(len(date_rows)),
            "stock_rows": stock_count,
            "markets": markets,
        }
        if len(date_rows) < min_full_rows:
            errors.append(f"{date_text}: daily price rows too low: {len(date_rows)} < {min_full_rows}")
        if not {"TWSE", "TPEx"}.issubset(set(markets)):
            errors.append(f"{date_text}: daily price file missing TWSE/TPEx markets: {markets}")
        if stock_count < min_full_rows:
            errors.append(f"{date_text}: daily price stock id rows too low: {stock_count} < {min_full_rows}")
    return errors, file_reports


def load_target_stock_ids(root: Path) -> set[str]:
    result: set[str] = set()
    for rel_path in TARGET_STOCK_SOURCE_FILES:
        path = root / rel_path
        if not path.exists():
            continue
        try:
            df = read_csv(path)
        except Exception:
            continue
        stock_col = "stock_id" if "stock_id" in df.columns else "ticker" if "ticker" in df.columns else ""
        if not stock_col:
            continue
        result.update(normalize_stock_id(value) for value in df[stock_col])
    return {stock_id for stock_id in result if stock_id}


def load_history_dates(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        df = pd.read_csv(path, dtype=str, usecols=["date"], keep_default_na=False).fillna("")
    except Exception:
        return set()
    return {safe_str(value) for value in df["date"] if safe_str(value)}


def validate_stock_history_coverage(
    root: Path,
    expected_dates: list[str],
    target_stock_ids: set[str],
) -> tuple[list[str], list[dict[str, str]]]:
    errors: list[str] = []
    missing_rows: list[dict[str, str]] = []
    if not target_stock_ids:
        return errors, missing_rows

    history_cache: dict[str, set[str]] = {}
    for date_text in expected_dates:
        daily = read_daily_price_for_date(root, date_text)
        if daily.empty or "_stock_id" not in daily.columns:
            continue
        present = {stock_id for stock_id in daily["_stock_id"].astype(str) if stock_id in target_stock_ids}
        for stock_id in sorted(present):
            if stock_id not in history_cache:
                history_cache[stock_id] = load_history_dates(root / STOCK_HISTORY_DIR / f"{stock_id}.csv")
            if date_text not in history_cache[stock_id]:
                missing_rows.append({"date": date_text, "stock_id": stock_id})
                if len(missing_rows) <= 30:
                    errors.append(f"{date_text}: stock history missing row for {stock_id}")
    if len(missing_rows) > 30:
        errors.append(f"stock history missing rows exceed sample limit: total={len(missing_rows)}")
    return errors, missing_rows


def validate(
    root: Path,
    *,
    freshness_path: Path = DATA_FRESHNESS,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    min_full_rows: int = DEFAULT_MIN_FULL_ROWS,
    non_trading_days_path: Path = NON_TRADING_DAYS,
) -> ValidationResult:
    errors: list[str] = []
    try:
        main_date = load_main_price_date(root, freshness_path)
        non_trading_days = load_non_trading_days(root, non_trading_days_path)
    except Exception as exc:
        report = {"status": "fail", "error": str(exc)}
        return ValidationResult("fail", report, [str(exc)])

    expected_dates = expected_trading_dates(main_date, lookback_days, non_trading_days)
    file_errors, file_reports = validate_daily_price_files(root, expected_dates, min_full_rows)
    errors.extend(file_errors)

    target_stock_ids = load_target_stock_ids(root)
    coverage_errors, missing_history_rows = validate_stock_history_coverage(root, expected_dates, target_stock_ids)
    errors.extend(coverage_errors)

    report = {
        "status": "pass" if not errors else "fail",
        "main_price_date": main_date,
        "lookback_days": lookback_days,
        "expected_trading_dates": expected_dates,
        "non_trading_days_in_window": [
            date
            for date in sorted(non_trading_days)
            if expected_dates and expected_dates[0] <= date <= expected_dates[-1] and is_weekday(date)
        ],
        "daily_price_files": file_reports,
        "target_stock_count": len(target_stock_ids),
        "stock_history_missing_rows": missing_history_rows[:200],
        "stock_history_missing_row_count": len(missing_history_rows),
        "errors": errors,
    }
    return ValidationResult(report["status"], report, errors)


def write_reports(root: Path, report: dict[str, Any]) -> None:
    latest = root / LATEST_DIR
    latest.mkdir(parents=True, exist_ok=True)
    (root / REPORT_JSON).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Daily Price History Continuity Validation",
        "",
        f"- status: `{report.get('status')}`",
        f"- main_price_date: `{report.get('main_price_date', '')}`",
        f"- lookback_days: `{report.get('lookback_days', '')}`",
        f"- expected_trading_dates: `{', '.join(report.get('expected_trading_dates', []))}`",
        f"- target_stock_count: `{report.get('target_stock_count', 0)}`",
        f"- stock_history_missing_row_count: `{report.get('stock_history_missing_row_count', 0)}`",
        "",
    ]
    errors = report.get("errors", [])
    if errors:
        lines.extend(["## Errors", ""])
        for error in errors:
            lines.append(f"- {error}")
    else:
        lines.append("No continuity errors found.")
    lines.append("")
    (root / REPORT_MD).write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate recent official daily price files and per-stock history continuity. "
            "This is a data-source gate; it does not fetch or infer missing prices."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--freshness-csv", default=DATA_FRESHNESS.as_posix())
    parser.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS)
    parser.add_argument("--min-full-rows", type=int, default=DEFAULT_MIN_FULL_ROWS)
    parser.add_argument("--non-trading-days", default=NON_TRADING_DAYS.as_posix())
    parser.add_argument("--no-write-report", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    result = validate(
        root,
        freshness_path=Path(args.freshness_csv),
        lookback_days=args.lookback_days,
        min_full_rows=args.min_full_rows,
        non_trading_days_path=Path(args.non_trading_days),
    )
    if not args.no_write_report:
        write_reports(root, result.report)

    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "daily price history continuity validation passed: "
        f"main_price_date={result.report.get('main_price_date')}, "
        f"expected_trading_dates={len(result.report.get('expected_trading_dates', []))}, "
        f"target_stock_count={result.report.get('target_stock_count')}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
