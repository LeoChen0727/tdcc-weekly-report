from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import subprocess
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
EXCEPTIONAL_NON_TRADING_DAYS = Path("data/market_calendar/exceptional_non_trading_days.csv")
MARKET_SESSION_STATUS = Path("output/latest/market_session_status_latest.json")
LATEST_DIR = Path("output/latest")
REPORT_JSON = LATEST_DIR / "daily_price_history_continuity_latest.json"
REPORT_MD = LATEST_DIR / "daily_price_history_continuity_latest.md"

TARGET_STOCK_SOURCE_FILES = [
    Path("output/latest/daily_candidate_model_signals_latest.csv"),
    Path("output/latest/daily_candidate_model_signals_for_report_latest.csv"),
    Path("output/latest/daily_volume_breakout_operation_section_latest.csv"),
    Path("output/latest/daily_w_bottom_right_side_operation_section_latest.csv"),
    Path("output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"),
]

SELECTED_BASE_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "market",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "trading_value",
    "source",
    "source_file",
]
SELECTED_NUMERIC_COLUMNS = {
    "open",
    "high",
    "low",
    "close",
    "volume",
    "trading_value",
}
SELECTED_INDICATOR_COLUMNS = [
    "ma5",
    "ma20",
    "ma60",
    "ma120",
    "ema23",
    "return_1d",
    "return_5d",
    "return_20d",
    "return_60d",
    "return_120d",
    "volume_ma20",
    "volume_ratio",
    "high_20",
    "high_60",
    "high_120",
    "low_20",
    "low_60",
    "low_120",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "distance_to_ma120_pct",
    "distance_to_ema23_pct",
    "distance_to_high_20_pct",
    "distance_to_high_60_pct",
    "distance_to_high_120_pct",
    "distance_to_low_60_pct",
    "distance_to_low_120_pct",
]
SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS = (
    "output/latest/company_industry_snapshot_latest.csv",
    "docs/latest/company_industry_snapshot_latest.csv",
    "output/latest/stock_theme_taxonomy_latest.csv",
    "docs/latest/stock_theme_taxonomy_latest.csv",
)


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
    text = re.sub(r"\.0$", "", safe_str(value))
    text = re.sub(r"[^0-9]", "", text)
    if not text:
        return ""
    if len(text) < 4:
        return text.zfill(4)
    return text


def is_supported_security_id(value: object) -> bool:
    text = normalize_stock_id(value)
    if not text.isdigit():
        return False
    if len(text) == 4:
        return True
    return text.startswith("00") and 5 <= len(text) <= 6


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


def load_non_trading_days_csv(full_path: Path) -> set[str]:
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


def load_market_session_non_trading_days(root: Path) -> tuple[set[str], set[int]]:
    status_path = root / MARKET_SESSION_STATUS
    if not status_path.exists():
        return set(), set()
    payload = json.loads(status_path.read_text(encoding="utf-8-sig"))
    dates: set[str] = set()
    for field in ("scheduled_non_trading_days", "exceptional_non_trading_days"):
        values = payload.get(field, [])
        if not isinstance(values, list):
            raise ValueError(f"{status_path.as_posix()} {field} must be a list")
        for value in values:
            date_text = safe_str(value)
            if not re.fullmatch(r"\d{8}", date_text):
                raise ValueError(f"{status_path.as_posix()} {field} has invalid date: {date_text!r}")
            dates.add(date_text)
    sources = payload.get("official_sources", {})
    annual = sources.get("twse_annual_calendar", {}) if isinstance(sources, dict) else {}
    covered_values = annual.get("covered_years", []) if isinstance(annual, dict) else []
    if not isinstance(covered_values, list):
        raise ValueError(f"{status_path.as_posix()} covered_years must be a list")
    covered_years: set[int] = set()
    for value in covered_values:
        try:
            covered_years.add(int(value))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{status_path.as_posix()} has invalid covered year: {value!r}") from exc
    return dates, covered_years


def load_non_trading_days(root: Path, path: Path) -> set[str]:
    static_dates = load_non_trading_days_csv(root / path)
    status_dates, covered_years = load_market_session_non_trading_days(root)
    if covered_years:
        dates = {
            date_text for date_text in static_dates if int(date_text[:4]) not in covered_years
        }
        dates.update(status_dates)
    else:
        dates = set(static_dates)
    exceptional_path = root / EXCEPTIONAL_NON_TRADING_DAYS
    if exceptional_path.resolve() != (root / path).resolve():
        dates.update(load_non_trading_days_csv(exceptional_path))
    return dates


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
    df["_is_supported_security"] = df["_stock_id"].map(is_supported_security_id)
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
        stock_count = (
            int(date_rows["_is_supported_security"].sum())
            if "_is_supported_security" in date_rows.columns
            else 0
        )
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
        result.update(normalize_stock_id(value) for value in df[stock_col] if is_supported_security_id(value))
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
        supported_daily = daily[daily["_is_supported_security"]].copy()
        present = {stock_id for stock_id in supported_daily["_stock_id"].astype(str) if stock_id in target_stock_ids}
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
    main_price_date_override: str = "",
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    min_full_rows: int = DEFAULT_MIN_FULL_ROWS,
    non_trading_days_path: Path = NON_TRADING_DAYS,
) -> ValidationResult:
    errors: list[str] = []
    try:
        if main_price_date_override:
            main_date = safe_str(main_price_date_override)
            if not re.fullmatch(r"\d{8}", main_date):
                raise ValueError(f"invalid --main-price-date: {main_date!r}")
            parse_yyyymmdd(main_date)
        else:
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


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_source_file(value: object) -> str:
    text = safe_str(value).replace("\\", "/")
    marker = "/data/daily_price/"
    if marker in text:
        return "data/daily_price/" + text.split(marker, 1)[1]
    return text


def _normalize_selected_stock_id(value: object) -> str:
    text = re.sub(r"\.0$", "", safe_str(value).upper())
    text = re.sub(r"[^0-9A-Z]", "", text)
    if text.isdigit() and len(text) < 4:
        text = text.zfill(4)
    return text


def _normalize_selected_base(frame: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(index=frame.index)
    for column in SELECTED_BASE_COLUMNS:
        if column in frame.columns:
            result[column] = frame[column]
        elif column in SELECTED_NUMERIC_COLUMNS:
            result[column] = math.nan
        else:
            result[column] = ""
    result["date"] = result["date"].map(safe_str)
    result["stock_id"] = result["stock_id"].map(_normalize_selected_stock_id)
    for column in ("stock_name", "market", "source", "source_file"):
        result[column] = result[column].map(safe_str)
    result["source_file"] = result["source_file"].map(_canonical_source_file)
    for column in SELECTED_NUMERIC_COLUMNS:
        result[column] = pd.to_numeric(result[column], errors="coerce")
    return result[SELECTED_BASE_COLUMNS]


def _is_selected_repair_eligible_stock_id(value: object) -> bool:
    stock_id = _normalize_selected_stock_id(value)
    if not stock_id.isdigit():
        return False
    if len(stock_id) == 4:
        return True
    return stock_id.startswith("00") and 5 <= len(stock_id) <= 6


def _canonical_number(value: object) -> str:
    number = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return "" if pd.isna(number) else format(float(number), ".15g")


def _selected_base_records(
    frame: pd.DataFrame,
    *,
    excluded_dates: set[str] | None = None,
) -> list[dict[str, str]]:
    excluded_dates = excluded_dates or set()
    normalized = _normalize_selected_base(frame)
    normalized = normalized[~normalized["date"].isin(excluded_dates)]
    records: list[dict[str, str]] = []
    for _, row in normalized.sort_values(["stock_id", "date"]).iterrows():
        records.append(
            {
                column: (
                    _canonical_number(row[column])
                    if column in SELECTED_NUMERIC_COLUMNS
                    else safe_str(row[column])
                )
                for column in SELECTED_BASE_COLUMNS
            }
        )
    return records


def _selected_indicator_records(
    frame: pd.DataFrame,
    *,
    before_date: str = "",
) -> list[dict[str, str]]:
    if "date" not in frame.columns:
        return []
    filtered = frame.copy()
    filtered["date"] = filtered["date"].map(safe_str)
    if before_date:
        filtered = filtered[filtered["date"].lt(before_date)]
    records: list[dict[str, str]] = []
    for _, row in filtered.sort_values("date").iterrows():
        record = {
            "date": safe_str(row.get("date")),
            "stock_id": _normalize_selected_stock_id(row.get("stock_id")),
        }
        for column in SELECTED_INDICATOR_COLUMNS:
            record[column] = _canonical_number(row.get(column, ""))
        records.append(record)
    return records


def _replay_selected_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    base = _normalize_selected_base(frame).sort_values("date").copy()
    close = base["close"]
    for window in (5, 20, 60, 120):
        base[f"ma{window}"] = close.rolling(window, min_periods=min(5, window)).mean()
    base["ema23"] = close.ewm(span=23, adjust=False, min_periods=5).mean()
    for days in (1, 5, 20, 60, 120):
        base[f"return_{days}d"] = close.pct_change(periods=days) * 100
    base["volume_ma20"] = base["volume"].rolling(20, min_periods=5).mean()
    base["volume_ratio"] = base["volume"] / base["volume_ma20"]
    for days in (20, 60, 120):
        base[f"high_{days}"] = base["high"].rolling(days, min_periods=5).max()
        base[f"low_{days}"] = base["low"].rolling(days, min_periods=5).min()
    for target in ("ma20", "ma60", "ma120", "ema23", "high_20", "high_60", "high_120"):
        base[f"distance_to_{target}_pct"] = (close / base[target] - 1) * 100
    for target in ("low_60", "low_120"):
        base[f"distance_to_{target}_pct"] = (close / base[target] - 1) * 100
    for column in SELECTED_INDICATOR_COLUMNS:
        base[column] = pd.to_numeric(base[column], errors="coerce").round(4)
    return base[SELECTED_BASE_COLUMNS + SELECTED_INDICATOR_COLUMNS]


def parse_selected_date_contracts(values: list[str] | None) -> dict[str, tuple[str, int]]:
    contracts: dict[str, tuple[str, int]] = {}
    for value in values or []:
        parts = safe_str(value).split(":")
        if len(parts) != 3:
            raise ValueError("selected date contract must use YYYYMMDD:sha256:row_count")
        date_text, expected_sha, row_count_text = parts
        parse_yyyymmdd(date_text)
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha):
            raise ValueError(f"selected date contract SHA-256 is invalid: {date_text}")
        row_count = int(row_count_text)
        if row_count <= 0 or date_text in contracts:
            raise ValueError(f"selected date contract identity is invalid: {date_text}")
        contracts[date_text] = (expected_sha, row_count)
    if not contracts:
        raise ValueError("selected repair validation requires date contracts")
    return contracts


def _git_file_bytes(root: Path, base_sha: str, path_text: str) -> bytes | None:
    result = subprocess.run(
        ["git", "show", f"{base_sha}:{path_text}"],
        cwd=root,
        capture_output=True,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def _validate_selected_canonical_name_source_bindings(
    root: Path, source_base_sha: str, report: dict[str, Any]
) -> None:
    bindings = report.get("canonical_stock_name_source_bindings")
    if not isinstance(bindings, list) or len(bindings) != len(
        SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS
    ):
        raise ValueError("selected repair canonical stock-name bindings are missing")
    by_path: dict[str, dict[str, Any]] = {}
    for item in bindings:
        if not isinstance(item, dict):
            raise ValueError("selected repair canonical stock-name binding is malformed")
        path_text = safe_str(item.get("path")).replace("\\", "/")
        if path_text in by_path:
            raise ValueError("selected repair canonical stock-name bindings are duplicated")
        by_path[path_text] = item
    if set(by_path) != set(SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS):
        raise ValueError("selected repair canonical stock-name path set is not exact")

    for path_text in SELECTED_CANONICAL_STOCK_NAME_SOURCE_PATHS:
        full_path = (root / path_text).resolve()
        try:
            full_path.relative_to(root)
        except ValueError as exc:
            raise ValueError(
                f"selected repair canonical stock-name source escapes repository: {path_text}"
            ) from exc
        current = root
        for part in Path(path_text).parts:
            current = current / part
            if current.is_symlink():
                raise ValueError(
                    f"selected repair canonical stock-name source is symlinked: {path_text}"
                )
        if not full_path.is_file():
            raise ValueError(
                f"selected repair canonical stock-name source is not materialized: {path_text}"
            )
        expected_blob_result = subprocess.run(
            ["git", "rev-parse", f"{source_base_sha}:{path_text}"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        expected_blob_sha = expected_blob_result.stdout.strip()
        observed_blob_result = subprocess.run(
            ["git", "hash-object", "--", path_text],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        git_payload = _git_file_bytes(root, source_base_sha, path_text)
        if (
            expected_blob_result.returncode != 0
            or not re.fullmatch(r"[0-9a-f]{40}", expected_blob_sha)
            or observed_blob_result.returncode != 0
            or observed_blob_result.stdout.strip() != expected_blob_sha
            or git_payload is None
        ):
            raise ValueError(
                f"selected repair canonical stock-name source differs from source base: {path_text}"
            )
        binding = by_path[path_text]
        if (
            safe_str(binding.get("git_blob_sha")) != expected_blob_sha
            or safe_str(binding.get("git_blob_raw_sha256"))
            != _sha256_bytes(git_payload)
        ):
            raise ValueError(
                f"selected repair canonical stock-name evidence mismatch: {path_text}"
            )


def validate_selected_repair(
    root: Path,
    *,
    report_path: Path,
    source_base_sha: str,
    date_contracts: dict[str, tuple[str, int]],
    expected_stock_union_count: int,
    expected_selected_row_count: int,
    expected_existing_history_count: int,
    expected_created_history_count: int,
    expected_untouched_history_count: int,
    expected_created_stock_ids: set[str],
    require_all_eligible_changed: bool = False,
    pathspec_nul_output: Path | None = None,
    pathspec_json_output: Path | None = None,
    history_stock_id_output: Path | None = None,
) -> dict[str, Any]:
    """Independently replay and validate a controlled selected-date repair."""

    root = root.resolve()
    if not re.fullmatch(r"[0-9a-f]{40}", source_base_sha):
        raise ValueError("selected repair source base SHA is invalid")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    if head != source_base_sha:
        raise ValueError("selected repair validator HEAD/source-base mismatch")
    full_report_path = report_path if report_path.is_absolute() else root / report_path
    report = json.loads(full_report_path.read_text(encoding="utf-8-sig"))
    dates = sorted(date_contracts)
    date_set = set(dates)
    if (
        report.get("schema_version") != "repair_daily_price_range_v2"
        or report.get("mode") != "selected_dates"
        or report.get("source_base_sha") != source_base_sha
        or report.get("selected_dates") != dates
    ):
        raise ValueError("selected repair report schema/base/date identity mismatch")
    _validate_selected_canonical_name_source_bindings(root, source_base_sha, report)
    reported_contracts = report.get("expected_date_contracts")
    if not isinstance(reported_contracts, list):
        raise ValueError("selected repair report expected date contracts are missing")
    reported_contract_map: dict[str, tuple[str, int]] = {}
    for item in reported_contracts:
        if not isinstance(item, dict):
            raise ValueError("selected repair report expected date contract is malformed")
        date_text = safe_str(item.get("date"))
        if date_text in reported_contract_map:
            raise ValueError("selected repair report expected date contracts are duplicated")
        reported_contract_map[date_text] = (
            safe_str(item.get("sha256")),
            int(item.get("row_count", -1)),
        )
    if reported_contract_map != date_contracts:
        raise ValueError("selected repair report expected date contracts differ from input")

    rows = report.get("rows")
    if not isinstance(rows, list) or len(rows) != len(dates):
        raise ValueError("selected repair report row count mismatch")
    rows_by_date = {safe_str(row.get("date")): row for row in rows if isinstance(row, dict)}
    if set(rows_by_date) != date_set or len(rows_by_date) != len(rows):
        raise ValueError("selected repair report date set is not exact")

    daily_frames: list[pd.DataFrame] = []
    expected_daily_paths: set[str] = set()
    for date_text in dates:
        row = rows_by_date[date_text]
        expected_sha, expected_rows = date_contracts[date_text]
        canonical_text = f"data/daily_price/daily_price_{date_text}.csv"
        legacy_text = f"data/daily_price/{date_text}.csv"
        observed_paths = {
            item.replace("\\", "/")
            for item in safe_str(row.get("saved_files")).split(";")
            if item
        }
        if (
            row.get("status") != "repaired"
            or safe_str(row.get("canonical_path")).replace("\\", "/") != canonical_text
            or safe_str(row.get("legacy_path")).replace("\\", "/") != legacy_text
            or observed_paths != {canonical_text, legacy_text}
        ):
            raise ValueError(f"selected repair source path/status mismatch: {date_text}")
        canonical_payload = (root / canonical_text).read_bytes()
        legacy_payload = (root / legacy_text).read_bytes()
        if canonical_payload != legacy_payload:
            raise ValueError(f"selected repair canonical/legacy mismatch: {date_text}")
        if (
            not canonical_payload.startswith(b"\xef\xbb\xbf")
            or b"\r\n" in canonical_payload
        ):
            raise ValueError(
                f"selected repair source encoding/line-ending mismatch: {date_text}"
            )
        if (
            _sha256_bytes(canonical_payload) != expected_sha
            or safe_str(row.get("price_sha256")) != expected_sha
            or int(row.get("total_rows", -1)) != expected_rows
        ):
            raise ValueError(f"selected repair expected source contract drift: {date_text}")
        frame = pd.read_csv(io.BytesIO(canonical_payload), dtype=str).fillna("")
        if len(frame) != expected_rows or set(frame["date"].astype(str)) != {date_text}:
            raise ValueError(f"selected repair source row/date mismatch: {date_text}")
        provenance = row.get("fetch_response_provenance")
        if not isinstance(provenance, list) or not provenance:
            raise ValueError(f"selected repair source provenance is missing: {date_text}")
        canonical_provenance_rows: set[str] = set()
        attempts: list[int] = []
        for item in provenance:
            if not isinstance(item, dict):
                raise ValueError(f"selected repair source provenance is malformed: {date_text}")
            canonical_item = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            if canonical_item in canonical_provenance_rows:
                raise ValueError(f"selected repair source provenance contains duplicates: {date_text}")
            canonical_provenance_rows.add(canonical_item)
            try:
                attempt = int(item.get("attempt", 0))
                int(item.get("status_code", 0))
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"selected repair source provenance attempt/status is invalid: {date_text}"
                ) from exc
            if attempt <= 0:
                raise ValueError(f"selected repair source provenance attempt is invalid: {date_text}")
            attempts.append(attempt)
            if (
                item.get("expected_response_date") != date_text
                or not safe_str(item.get("source_name"))
                or not safe_str(item.get("endpoint")).startswith("https://")
                or any(
                    not re.fullmatch(r"[0-9a-f]{64}", safe_str(item.get(field)))
                    for field in ("raw_sha256", "normalized_sha256")
                )
            ):
                raise ValueError(f"selected repair source provenance binding is invalid: {date_text}")
        final_attempt = max(attempts)
        final_success = [
            item
            for item in provenance
            if int(item["attempt"]) == final_attempt
            and int(item["status_code"]) == 200
            and item.get("exact_date_match") is True
        ]
        final_success_names = [safe_str(item.get("source_name")) for item in final_success]
        if len(final_success_names) != len(set(final_success_names)):
            raise ValueError(f"selected repair final source roles are duplicated: {date_text}")
        if not any(name.startswith("TWSE_") for name in final_success_names) or not any(
            name.startswith("TPEX_") for name in final_success_names
        ):
            raise ValueError(f"selected repair exact TWSE/TPEx provenance is incomplete: {date_text}")
        observed_sources = {
            safe_str(value) for value in frame.get("source", pd.Series(dtype=str)) if safe_str(value)
        }
        if not observed_sources or not observed_sources.issubset(set(final_success_names)):
            raise ValueError(f"selected repair source/provenance roles differ: {date_text}")
        frame["source_file"] = canonical_text
        daily_frames.append(_normalize_selected_base(frame))
        expected_daily_paths.update({canonical_text, legacy_text})

    raw_selected = pd.concat(daily_frames, ignore_index=True)
    selected = raw_selected[
        raw_selected["stock_id"].map(_is_selected_repair_eligible_stock_id)
    ].copy()
    if selected.duplicated(["stock_id", "date"]).any():
        raise ValueError("selected repair source contains duplicate stock/date keys")
    selected_stock_ids = set(selected["stock_id"])
    if len(selected) != expected_selected_row_count:
        raise ValueError("selected repair independently derived row count mismatch")
    if len(selected_stock_ids) != expected_stock_union_count:
        raise ValueError("selected repair independently derived stock union mismatch")

    history = report.get("history_repair")
    if not isinstance(history, dict):
        raise ValueError("selected repair history report is missing")
    expected_scalars = {
        "eligible_stock_union_count": expected_stock_union_count,
        "eligible_stock_date_row_count": expected_selected_row_count,
        "existing_history_count": expected_existing_history_count,
        "created_history_count": expected_created_history_count,
        "untouched_history_count": expected_untouched_history_count,
    }
    for field, expected in expected_scalars.items():
        if int(history.get(field, -1)) != expected:
            raise ValueError(f"selected repair history scalar mismatch: {field}")
    created_ids = {
        _normalize_selected_stock_id(value)
        for value in history.get("created_history_stock_ids", [])
    }
    if created_ids != expected_created_stock_ids:
        raise ValueError("selected repair created stock-id set mismatch")
    raw_created_source_rows: list[tuple[str, str, str]] = []
    for source_path in sorted((root / DAILY_PRICE_DIR).glob("*.csv")):
        if not source_path.is_file() or source_path.is_symlink():
            raise ValueError(f"selected repair raw source path is unsafe: {source_path}")
        try:
            raw_frame = pd.read_csv(
                source_path, dtype=str, keep_default_na=False
            ).fillna("")
        except Exception as exc:
            raise ValueError(f"selected repair cannot scan raw source: {source_path}") from exc
        code_column = next(
            (name for name in ("stock_id", "ticker", "code") if name in raw_frame.columns),
            "",
        )
        if not code_column or "date" not in raw_frame.columns:
            raise ValueError(f"selected repair raw source lacks identity/date: {source_path}")
        normalized_stock_ids = raw_frame[code_column].map(_normalize_selected_stock_id)
        matched = raw_frame.loc[normalized_stock_ids.isin(created_ids), ["date"]].copy()
        matched["stock_id"] = normalized_stock_ids.loc[matched.index]
        for raw_row in matched.itertuples(index=False):
            stock_id = safe_str(raw_row.stock_id)
            date_text = re.sub(r"[^0-9]", "", safe_str(raw_row.date))
            if not re.fullmatch(r"20\d{6}", date_text):
                raise ValueError(
                    f"selected repair raw created-stock date is invalid: {source_path}/{stock_id}"
                )
            raw_created_source_rows.append(
                (stock_id, date_text, source_path.relative_to(root).as_posix())
            )
    outside_created_rows = [
        row for row in raw_created_source_rows if row[1] not in date_set
    ]
    if outside_created_rows:
        raise ValueError(
            "selected repair created stock has raw source rows outside selected dates: "
            + ",".join(f"{stock_id}/{date}" for stock_id, date, _ in outside_created_rows[:20])
        )
    independently_created_rows = int(selected["stock_id"].isin(created_ids).sum())
    independently_existing_rows = len(selected) - independently_created_rows
    if int(history.get("selected_rows_created_histories", -1)) != independently_created_rows:
        raise ValueError("selected repair created-history row count mismatch")
    if int(history.get("selected_rows_injected_existing_histories", -1)) != independently_existing_rows:
        raise ValueError("selected repair existing-history injected row count mismatch")
    eligible_paths = {
        safe_str(value).replace("\\", "/") for value in history.get("eligible_history_paths", [])
    }
    derived_paths = {
        f"data/stock_price_history/{stock_id}.csv" for stock_id in selected_stock_ids
    }
    if eligible_paths != derived_paths:
        raise ValueError("selected repair eligible history paths differ from source-derived union")
    changed_paths = {
        safe_str(value).replace("\\", "/") for value in history.get("changed_history_paths", [])
    }
    if not changed_paths.issubset(eligible_paths) or (
        require_all_eligible_changed and changed_paths != eligible_paths
    ):
        raise ValueError("selected repair changed history path set mismatch")
    history_hashes = history.get("changed_history_sha256s")
    if not isinstance(history_hashes, dict) or set(history_hashes) != changed_paths:
        raise ValueError("selected repair changed history SHA path set mismatch")
    if history.get("non_selected_base_before_sha256") != history.get(
        "non_selected_base_after_sha256"
    ):
        raise ValueError("selected repair report shows non-selected base drift")
    if history.get("pre_repair_indicator_before_sha256") != history.get(
        "pre_repair_indicator_after_sha256"
    ):
        raise ValueError("selected repair report shows pre-repair indicator drift")
    if history.get("untouched_history_before_sha256") != history.get(
        "untouched_history_after_sha256"
    ):
        raise ValueError("selected repair report shows outside-union history drift")

    earliest_date = dates[0]
    for path_text in sorted(eligible_paths):
        path = root / path_text
        payload = path.read_bytes()
        if path_text in history_hashes and _sha256_bytes(payload) != history_hashes[path_text]:
            raise ValueError(f"selected repair history SHA mismatch: {path_text}")
        current = pd.read_csv(io.BytesIO(payload), dtype=str).fillna("")
        stock_id = path.stem
        expected_selected = selected[selected["stock_id"].eq(stock_id)]
        actual_selected = current[current["date"].astype(str).isin(date_set)]
        if _selected_base_records(actual_selected) != _selected_base_records(expected_selected):
            raise ValueError(f"selected repair history/source mismatch: {stock_id}")
        independently_replayed = _replay_selected_indicators(current)
        if _selected_indicator_records(current) != _selected_indicator_records(
            independently_replayed
        ):
            raise ValueError(f"selected repair independent indicator replay mismatch: {stock_id}")

        previous_payload = _git_file_bytes(root, source_base_sha, path_text)
        if stock_id in created_ids:
            if previous_payload is not None or set(current["date"].astype(str)) - date_set:
                raise ValueError(f"selected repair created history coverage mismatch: {stock_id}")
        else:
            if previous_payload is None:
                raise ValueError(f"selected repair existing history missing from base: {stock_id}")
            previous = pd.read_csv(io.BytesIO(previous_payload), dtype=str).fillna("")
            if _selected_base_records(
                previous, excluded_dates=date_set
            ) != _selected_base_records(current, excluded_dates=date_set):
                raise ValueError(f"selected repair changed non-selected base rows: {stock_id}")
            if _selected_indicator_records(
                previous, before_date=earliest_date
            ) != _selected_indicator_records(current, before_date=earliest_date):
                raise ValueError(f"selected repair changed pre-repair indicators: {stock_id}")

    coverage = history.get("new_history_source_coverage")
    if not isinstance(coverage, list) or {
        _normalize_selected_stock_id(item.get("stock_id"))
        for item in coverage
        if isinstance(item, dict)
    } != created_ids:
        raise ValueError("selected repair new-history coverage identity mismatch")
    if any(
        not isinstance(item, dict)
        or item.get("new_history_source_coverage") != "target_dates_only"
        or int(item.get("outside_selected_date_source_rows", -1)) != 0
        for item in coverage
    ):
        raise ValueError("selected repair new-history coverage is not target-date-only")

    current_history_paths = {
        path.relative_to(root).as_posix()
        for path in (root / STOCK_HISTORY_DIR).glob("*.csv")
        if path.is_file() and not path.is_symlink()
    }
    untouched_paths = current_history_paths - eligible_paths
    if len(untouched_paths) != expected_untouched_history_count:
        raise ValueError("selected repair independently derived untouched count mismatch")
    for path_text in sorted(untouched_paths):
        previous_payload = _git_file_bytes(root, source_base_sha, path_text)
        if previous_payload is None or (root / path_text).read_bytes() != previous_payload:
            raise ValueError(f"selected repair changed outside-union history: {path_text}")

    manifest_hashes = history.get("manifest_sha256s")
    expected_manifest_paths = {
        f"{prefix}/stock_price_history_manifest.{suffix}"
        for prefix in ("output/latest", "docs/latest")
        for suffix in ("csv", "json", "md")
    }
    if set(history.get("manifest_paths") or []) != expected_manifest_paths:
        raise ValueError("selected repair history report manifest path set is not exact")
    if not isinstance(manifest_hashes, dict) or set(manifest_hashes) != expected_manifest_paths:
        raise ValueError("selected repair manifest path contract is not the exact six mirrors")
    for path_text, expected_hash in manifest_hashes.items():
        full_path = (root / path_text).resolve()
        try:
            full_path.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"selected repair manifest path escapes repository: {path_text}") from exc
        if not full_path.is_file() or full_path.is_symlink():
            raise ValueError(f"selected repair manifest path is missing or unsafe: {path_text}")
        if _sha256_bytes(full_path.read_bytes()) != expected_hash:
            raise ValueError(f"selected repair manifest SHA mismatch: {path_text}")
    for suffix in ("csv", "json", "md"):
        output_payload = (
            root / f"output/latest/stock_price_history_manifest.{suffix}"
        ).read_bytes()
        docs_payload = (root / f"docs/latest/stock_price_history_manifest.{suffix}").read_bytes()
        if output_payload != docs_payload:
            raise ValueError(f"selected repair manifest mirror payload mismatch: {suffix}")
    manifest_csv = pd.read_csv(
        root / "output/latest/stock_price_history_manifest.csv", dtype=str
    ).fillna("")
    required_manifest_columns = [
        "stock_id",
        "stock_name",
        "market",
        "rows",
        "start_date",
        "end_date",
        "latest_close",
        "latest_volume",
        "file_path",
        "raw_url",
    ]
    if list(manifest_csv.columns) != required_manifest_columns or manifest_csv["stock_id"].map(
        _normalize_selected_stock_id
    ).duplicated().any():
        raise ValueError("selected repair manifest stock identity is invalid")
    manifest_ids = set(manifest_csv["stock_id"].map(_normalize_selected_stock_id))
    current_history_ids = {Path(path_text).stem for path_text in current_history_paths}
    if len(manifest_csv) != len(current_history_paths) or manifest_ids != current_history_ids:
        raise ValueError("selected repair manifest/history identity or count mismatch")
    manifest_csv["_stock_id"] = manifest_csv["stock_id"].map(_normalize_selected_stock_id)
    manifest_by_id = manifest_csv.set_index("_stock_id", drop=False)
    for stock_id in sorted(current_history_ids):
        path_text = f"data/stock_price_history/{stock_id}.csv"
        frame = pd.read_csv(root / path_text, dtype=str).fillna("")
        latest = frame.sort_values("date").iloc[-1]
        nonempty_names = frame["stock_name"].map(safe_str)
        nonempty_names = nonempty_names[nonempty_names.ne("")]
        nonempty_markets = frame["market"].map(safe_str)
        nonempty_markets = nonempty_markets[nonempty_markets.ne("")]
        manifest_row = manifest_by_id.loc[stock_id]
        expected_text = {
            "stock_name": safe_str(nonempty_names.iloc[-1]) if not nonempty_names.empty else "",
            "market": safe_str(nonempty_markets.iloc[-1]) if not nonempty_markets.empty else "",
            "rows": str(len(frame)),
            "start_date": safe_str(frame["date"].min()),
            "end_date": safe_str(frame["date"].max()),
            "file_path": path_text,
            "raw_url": (
                "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"
                + path_text
            ),
        }
        for field, expected_value in expected_text.items():
            if safe_str(manifest_row.get(field)) != expected_value:
                raise ValueError(
                    f"selected repair manifest metadata mismatch: {stock_id}/{field}"
                )
        for field, source_field in (("latest_close", "close"), ("latest_volume", "volume")):
            if _canonical_number(manifest_row.get(field)) != _canonical_number(
                latest.get(source_field)
            ):
                raise ValueError(
                    f"selected repair manifest numeric metadata mismatch: {stock_id}/{field}"
                )

    base_manifest_payload = _git_file_bytes(
        root, source_base_sha, "output/latest/stock_price_history_manifest.csv"
    )
    if base_manifest_payload is None:
        raise ValueError("selected repair base stock-history manifest is missing")
    base_manifest = pd.read_csv(io.BytesIO(base_manifest_payload), dtype=str).fillna("")
    if any(column not in base_manifest.columns for column in required_manifest_columns):
        raise ValueError("selected repair base stock-history manifest schema mismatch")
    base_manifest["_stock_id"] = base_manifest["stock_id"].map(_normalize_selected_stock_id)
    if base_manifest["_stock_id"].duplicated().any():
        raise ValueError("selected repair base stock-history manifest has duplicate IDs")
    base_by_id = base_manifest.set_index("_stock_id", drop=False)
    for stock_id in sorted(current_history_ids - selected_stock_ids):
        if stock_id not in base_by_id.index:
            raise ValueError(f"selected repair untouched manifest row missing from base: {stock_id}")
        current_record = {
            column: safe_str(manifest_by_id.loc[stock_id].get(column))
            for column in required_manifest_columns
        }
        base_record = {
            column: safe_str(base_by_id.loc[stock_id].get(column))
            for column in required_manifest_columns
        }
        if current_record != base_record:
            raise ValueError(f"selected repair changed untouched manifest row: {stock_id}")

    manifest_json_payload = json.loads(
        (root / "output/latest/stock_price_history_manifest.json").read_text(
            encoding="utf-8-sig"
        )
    )
    base_manifest_json_bytes = _git_file_bytes(
        root, source_base_sha, "output/latest/stock_price_history_manifest.json"
    )
    if base_manifest_json_bytes is None:
        raise ValueError("selected repair base stock-history manifest JSON is missing")
    try:
        base_manifest_json = json.loads(base_manifest_json_bytes.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            "selected repair base stock-history manifest JSON is invalid"
        ) from exc
    if not isinstance(manifest_json_payload, dict) or not isinstance(
        base_manifest_json, dict
    ):
        raise ValueError("selected repair manifest JSON must be an object")
    required_json_fields = {
        "generated_at",
        "status",
        "stock_count",
        "daily_price_file_count",
        "manifest_csv",
        "manifest_raw_url",
        "manifest_pages_url",
        "history_dir",
    }
    expected_json_locations = {
        "manifest_csv": "output/latest/stock_price_history_manifest.csv",
        "manifest_raw_url": (
            "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"
            "output/latest/stock_price_history_manifest.csv"
        ),
        "manifest_pages_url": (
            "https://LeoChen0727.github.io/tdcc-weekly-report/latest/"
            "stock_price_history_manifest.csv"
        ),
        "history_dir": "data/stock_price_history",
    }
    mutable_json_fields = {
        "generated_at",
        "status",
        "stock_count",
        "daily_price_file_count",
    }
    preserved_manifest_json = {
        key: value
        for key, value in manifest_json_payload.items()
        if key not in mutable_json_fields
    }
    preserved_base_manifest_json = {
        key: value
        for key, value in base_manifest_json.items()
        if key not in mutable_json_fields
    }
    if (
        not required_json_fields.issubset(manifest_json_payload)
        or int(manifest_json_payload.get("stock_count", -1)) != len(current_history_paths)
        or manifest_json_payload.get("status") != "selected_date_repair"
        or safe_str(manifest_json_payload.get("generated_at")) == ""
        or safe_str(manifest_json_payload.get("generated_at"))
        != safe_str(history.get("generated_at"))
        or int(manifest_json_payload.get("daily_price_file_count", -1))
        != len(list((root / DAILY_PRICE_DIR).glob("*.csv")))
        or any(
            safe_str(manifest_json_payload.get(field)) != expected_value
            for field, expected_value in expected_json_locations.items()
        )
        or preserved_manifest_json != preserved_base_manifest_json
    ):
        raise ValueError("selected repair manifest JSON semantic contract mismatch")

    fixed_paths = {
        "output/latest/repair_daily_price_range_latest.csv",
        "output/latest/repair_daily_price_range_check_code_latest.csv",
        "output/latest/repair_daily_price_range_latest.json",
        "output/latest/repair_daily_price_range_latest.md",
    }
    exact_paths = expected_daily_paths | changed_paths | set(manifest_hashes) | fixed_paths
    if pathspec_nul_output:
        pathspec_nul_output.parent.mkdir(parents=True, exist_ok=True)
        pathspec_nul_output.write_bytes(
            b"\0".join(path.encode("utf-8") for path in sorted(exact_paths)) + b"\0"
        )
    if pathspec_json_output:
        pathspec_json_output.parent.mkdir(parents=True, exist_ok=True)
        pathspec_json_output.write_text(json.dumps(sorted(exact_paths)), encoding="utf-8")
    if history_stock_id_output:
        history_stock_id_output.parent.mkdir(parents=True, exist_ok=True)
        history_stock_id_output.write_text(
            "".join(f"{stock_id}\n" for stock_id in sorted(selected_stock_ids)),
            encoding="ascii",
        )
    return {
        "dates": dates,
        "selected_row_count": len(selected),
        "stock_union_count": len(selected_stock_ids),
        "changed_history_count": len(changed_paths),
        "exact_path_count": len(exact_paths),
    }


def verify_selected_repair_staged_paths(root: Path, expected_json_path: Path) -> int:
    """Verify exact staged paths and reject every unstaged or untracked residue."""

    root = root.resolve()
    full_json_path = (
        expected_json_path
        if expected_json_path.is_absolute()
        else (root / expected_json_path).resolve()
    )
    expected_values = json.loads(full_json_path.read_text(encoding="utf-8"))
    if not isinstance(expected_values, list) or not expected_values:
        raise ValueError("selected repair staged-path plan must be a non-empty list")
    expected: set[str] = set()
    for value in expected_values:
        path_text = safe_str(value).replace("\\", "/")
        path = Path(path_text)
        if (
            not path_text
            or path.is_absolute()
            or any(part in {"", ".", ".."} for part in path.parts)
            or path_text in expected
        ):
            raise ValueError(f"selected repair staged-path plan is not canonical: {value!r}")
        full_path = (root / path).resolve()
        try:
            full_path.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"selected repair staged path escapes repository: {path_text}") from exc
        if not full_path.is_file() or full_path.is_symlink():
            raise ValueError(f"selected repair staged path is missing or unsafe: {path_text}")
        expected.add(path_text)

    staged_output = subprocess.check_output(
        ["git", "diff", "--cached", "--name-only", "-z"], cwd=root
    )
    staged = {
        item.decode("utf-8").replace("\\", "/")
        for item in staged_output.split(b"\0")
        if item
    }
    if staged != expected:
        raise ValueError(
            "selected repair staged path set mismatch: "
            f"missing={sorted(expected - staged)[:20]} "
            f"unexpected={sorted(staged - expected)[:20]}"
        )
    unstaged = subprocess.check_output(
        ["git", "diff", "--name-only", "-z"], cwd=root
    )
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=root
    )
    if unstaged or untracked:
        raise ValueError("selected repair left unstaged or untracked repository paths")
    return len(staged)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate recent official daily price files and per-stock history continuity. "
            "This is a data-source gate; it does not fetch or infer missing prices."
        )
    )
    parser.add_argument("--repo-root", default=".", help="Repository root. Default: current directory.")
    parser.add_argument("--freshness-csv", default=DATA_FRESHNESS.as_posix())
    parser.add_argument(
        "--main-price-date",
        default="",
        help=(
            "Optional explicit YYYYMMDD validation end date. This is used by historical "
            "source replay before data_freshness_latest.csv is regenerated."
        ),
    )
    parser.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS)
    parser.add_argument("--min-full-rows", type=int, default=DEFAULT_MIN_FULL_ROWS)
    parser.add_argument("--non-trading-days", default=NON_TRADING_DAYS.as_posix())
    parser.add_argument("--no-write-report", action="store_true")
    parser.add_argument(
        "--selected-repair-report",
        default="",
        help="Validate a controlled selected-date repair report instead of the rolling continuity surface.",
    )
    parser.add_argument("--selected-source-base-sha", default="")
    parser.add_argument("--selected-date-contract", action="append", default=None)
    parser.add_argument("--expected-stock-union-count", type=int, default=None)
    parser.add_argument("--expected-selected-row-count", type=int, default=None)
    parser.add_argument("--expected-existing-history-count", type=int, default=None)
    parser.add_argument("--expected-created-history-count", type=int, default=None)
    parser.add_argument("--expected-untouched-history-count", type=int, default=None)
    parser.add_argument("--expected-created-stock-id", action="append", default=None)
    parser.add_argument("--require-all-eligible-changed", action="store_true")
    parser.add_argument("--pathspec-nul-output", default="")
    parser.add_argument("--pathspec-json-output", default="")
    parser.add_argument("--history-stock-id-output", default="")
    parser.add_argument("--verify-staged-paths-json", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo_root).resolve()
    if args.verify_staged_paths_json:
        if not args.no_write_report:
            print("ERROR: staged-path validation requires --no-write-report")
            return 1
        try:
            staged_count = verify_selected_repair_staged_paths(
                root, Path(args.verify_staged_paths_json)
            )
        except Exception as exc:
            print(f"ERROR: selected repair staged-path validation failed: {exc}")
            return 1
        print(f"selected repair staged-path validation passed: paths={staged_count}")
        return 0
    if args.selected_repair_report:
        if not args.no_write_report:
            print("ERROR: selected repair validation requires --no-write-report")
            return 1
        try:
            expected_counts = (
                args.expected_stock_union_count,
                args.expected_selected_row_count,
                args.expected_existing_history_count,
                args.expected_created_history_count,
                args.expected_untouched_history_count,
            )
            if any(value is None for value in expected_counts):
                raise ValueError("selected repair validation requires every expected count")
            summary = validate_selected_repair(
                root,
                report_path=Path(args.selected_repair_report),
                source_base_sha=args.selected_source_base_sha,
                date_contracts=parse_selected_date_contracts(args.selected_date_contract),
                expected_stock_union_count=args.expected_stock_union_count,
                expected_selected_row_count=args.expected_selected_row_count,
                expected_existing_history_count=args.expected_existing_history_count,
                expected_created_history_count=args.expected_created_history_count,
                expected_untouched_history_count=args.expected_untouched_history_count,
                expected_created_stock_ids={
                    normalize_stock_id(value)
                    for value in (args.expected_created_stock_id or [])
                },
                require_all_eligible_changed=args.require_all_eligible_changed,
                pathspec_nul_output=(
                    Path(args.pathspec_nul_output) if args.pathspec_nul_output else None
                ),
                pathspec_json_output=(
                    Path(args.pathspec_json_output) if args.pathspec_json_output else None
                ),
                history_stock_id_output=(
                    Path(args.history_stock_id_output)
                    if args.history_stock_id_output
                    else None
                ),
            )
        except Exception as exc:
            print(f"ERROR: selected repair validation failed: {exc}")
            return 1
        print(
            "selected repair validation passed: "
            f"dates={len(summary['dates'])} rows={summary['selected_row_count']} "
            f"stocks={summary['stock_union_count']} paths={summary['exact_path_count']}"
        )
        return 0
    result = validate(
        root,
        freshness_path=Path(args.freshness_csv),
        main_price_date_override=args.main_price_date,
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
