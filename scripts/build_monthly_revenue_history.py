from __future__ import annotations

import io
import json
import math
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_taipei, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "monthly_revenue_history"
RAW_DIR = DATA_DIR / "raw"
HISTORY_CSV = DATA_DIR / "monthly_revenue_history.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_history_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "monthly_revenue_history_latest.md"
SOURCE_STATUS_JSON = RESEARCH_LATEST_DIR / "monthly_revenue_history_source_status_latest.json"
DOCS_LATEST_CSV = DOCS_LATEST_DIR / LATEST_CSV.name
DOCS_LATEST_MD = DOCS_LATEST_DIR / LATEST_MD.name

HISTORY_ID = "monthly_revenue_history"
HISTORY_VERSION = "official_mops_monthly_revenue_v1"
SOURCE_KIND = "official_mops_current_monthly_revenue_openapi"
FALLBACK_SOURCE_STATUS = "fallback_reused_validated_history"
FALLBACK_SOURCE_KIND = "official_mops_current_monthly_revenue_openapi_unavailable_reused_validated_history"
DEFAULT_FALLBACK_MAX_AGE_DAYS = 25
REQUIRED_MARKETS = {"listed", "otc"}

SOURCE_DEFS = [
    ("listed", "TWSE", "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv"),
    ("otc", "TPEX", "https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv"),
]

SOURCE_FIELD_ORDER = [
    "source_table_date",
    "revenue_period",
    "stock_id",
    "stock_name",
    "industry",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
]

SOURCE_STANDARD_ALIASES = {
    "source_table_date": ["source_table_date", "table_date"],
    "revenue_period": ["revenue_period"],
    "stock_id": ["stock_id", "ticker", "code"],
    "stock_name": ["stock_name", "name", "company_name"],
    "industry": ["industry"],
    "monthly_revenue": ["monthly_revenue"],
    "previous_month_revenue": ["previous_month_revenue"],
    "last_year_month_revenue": ["last_year_month_revenue"],
    "month_over_month_pct": ["month_over_month_pct"],
    "latest_revenue_yoy_pct": ["latest_revenue_yoy_pct", "revenue_yoy_pct"],
    "cumulative_revenue": ["cumulative_revenue"],
    "last_year_cumulative_revenue": ["last_year_cumulative_revenue"],
    "cumulative_revenue_yoy_pct": ["cumulative_revenue_yoy_pct", "cumulative_yoy_pct"],
    "note": ["note"],
}

OUTPUT_COLUMNS = [
    "generated_at",
    "history_id",
    "history_version",
    "source_kind",
    "market",
    "source_market_name",
    "stock_id",
    "stock_name",
    "industry",
    "revenue_period",
    "revenue_period_roc",
    "source_table_date",
    "source_table_date_raw",
    "fetch_date",
    "fetch_timestamp",
    "source_url",
    "source_file",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "formal_use_blocker",
    "coverage_note",
]

NUMERIC_COLUMNS = [
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
]


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>", "null"}:
        return ""
    return text


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = re.sub(r"\D", "", text)
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def clean_numeric_text(value: Any) -> str:
    text = safe_str(value).replace(",", "").replace("%", "").replace("+", "")
    if text in {"", "-", "--"}:
        return ""
    if re.fullmatch(r"-?\d+\.0", text):
        text = text[:-2]
    return text


def to_float(value: Any) -> float:
    text = clean_numeric_text(value)
    if not text:
        return math.nan
    try:
        num = float(text)
    except ValueError:
        return math.nan
    return num if math.isfinite(num) else math.nan


def format_number(value: Any) -> str:
    num = to_float(value)
    if math.isnan(num):
        return ""
    if num.is_integer():
        return str(int(num))
    return f"{num:.6f}".rstrip("0").rstrip(".")


def parse_roc_or_yyyymm(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", ""
    if len(digits) in {5, 6}:
        padded = digits.zfill(6)
        year = int(padded[:-2])
        month = int(padded[-2:])
        if year < 1911:
            year += 1911
        if 1 <= month <= 12:
            return f"{year:04d}{month:02d}", digits
    if len(digits) >= 6:
        year = int(digits[:4])
        month = int(digits[4:6])
        if year >= 1911 and 1 <= month <= 12:
            return digits[:6], digits
    return "", digits


def parse_roc_or_yyyymmdd(value: Any) -> tuple[str, str]:
    raw = clean_numeric_text(value)
    digits = re.sub(r"\D", "", raw)
    if not digits:
        return "", ""
    if len(digits) == 7:
        year = int(digits[:3]) + 1911
        month = int(digits[3:5])
        day = int(digits[5:7])
    elif len(digits) == 8:
        year = int(digits[:4])
        month = int(digits[4:6])
        day = int(digits[6:8])
    else:
        return "", digits
    try:
        return f"{year:04d}{month:02d}{day:02d}", digits
    except ValueError:
        return "", digits


def pick_column(df: pd.DataFrame, candidates: list[str]) -> str:
    for col in candidates:
        if col in df.columns:
            return col
    return ""


def select_source_columns(df: pd.DataFrame) -> tuple[dict[str, str], str]:
    selected: dict[str, str] = {}
    for key, aliases in SOURCE_STANDARD_ALIASES.items():
        selected[key] = pick_column(df, aliases)
    missing = [key for key, column in selected.items() if not column]
    if missing and len(df.columns) >= len(SOURCE_FIELD_ORDER):
        for index, key in enumerate(SOURCE_FIELD_ORDER):
            selected.setdefault(key, "")
            if not selected[key]:
                selected[key] = str(df.columns[index])
        return selected, "official_position_fallback"
    return selected, "standard_alias"


def revenue_flags(latest_yoy: Any, cumulative_yoy: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    positive = (
        (not math.isnan(latest) and latest > 0)
        or (not math.isnan(cumulative) and cumulative > 0)
    )
    strong = (
        (not math.isnan(latest) and latest >= 20)
        or (not math.isnan(cumulative) and cumulative >= 10)
    )
    return ("True" if positive else "False", "True" if strong else "False")


def anomaly_flag(latest_yoy: Any, cumulative_yoy: Any, monthly_revenue: Any) -> tuple[str, str]:
    latest = to_float(latest_yoy)
    cumulative = to_float(cumulative_yoy)
    monthly = to_float(monthly_revenue)
    reasons: list[str] = []
    if not math.isnan(latest) and abs(latest) >= 300:
        reasons.append("latest_revenue_yoy_abs_ge_300pct")
    if not math.isnan(cumulative) and abs(cumulative) >= 500:
        reasons.append("cumulative_revenue_yoy_abs_ge_500pct")
    if not math.isnan(monthly) and monthly < 0:
        reasons.append("monthly_revenue_negative")
    return ("True" if reasons else "False", ";".join(reasons))


def raw_file_name(market: str, source_table_date: str, revenue_period: str) -> str:
    date_part = source_table_date or "unknown_date"
    period_part = revenue_period or "unknown_period"
    return f"monthly_revenue_raw_{market}_{date_part}_{period_part}.csv"


def fetch_source(url: str, timeout: int = 30) -> pd.DataFrame:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    response.encoding = "utf-8-sig"
    return pd.read_csv(io.StringIO(response.text), dtype=str, keep_default_na=False)


def env_int(name: str, default: int, *, min_value: int = 1) -> int:
    raw = os.environ.get(name, "")
    if not raw:
        return default
    try:
        value = int(raw)
    except ValueError:
        return default
    return max(min_value, value)


def parse_yyyymmdd_date(value: Any) -> datetime | None:
    text = safe_str(value)
    if not re.fullmatch(r"20\d{6}", text):
        return None
    try:
        return datetime.strptime(text, "%Y%m%d")
    except ValueError:
        return None


def latest_period_rows(history: pd.DataFrame) -> pd.DataFrame:
    if history.empty or "revenue_period" not in history.columns:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)
    latest_period = history["revenue_period"].astype(str).max()
    return (
        history[history["revenue_period"].astype(str).eq(latest_period)][OUTPUT_COLUMNS]
        .sort_values(["revenue_period", "market", "stock_id"])
        .reset_index(drop=True)
    )


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def official_current_sources_ready(current: pd.DataFrame, statuses: list[dict[str, Any]]) -> bool:
    if current.empty:
        return False
    by_market = {safe_str(item.get("market")): item for item in statuses}
    if not REQUIRED_MARKETS <= set(by_market):
        return False
    for market in REQUIRED_MARKETS:
        item = by_market[market]
        if safe_str(item.get("status")) != "ok":
            return False
        if int(item.get("standardized_rows") or 0) <= 0:
            return False
    return True


def load_recent_history_fallback(
    statuses: list[dict[str, Any]],
    *,
    history_path: Path = HISTORY_CSV,
    fetch_date: str | None = None,
    max_age_days: int | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, list[dict[str, Any]]]:
    max_age_days = DEFAULT_FALLBACK_MAX_AGE_DAYS if max_age_days is None else max_age_days
    fetch_date = fetch_date or now_taipei().strftime("%Y%m%d")
    fetch_dt = parse_yyyymmdd_date(fetch_date)
    if fetch_dt is None:
        raise RuntimeError(f"Cannot evaluate monthly revenue fallback freshness for fetch_date={fetch_date}")
    if not history_path.exists():
        raise RuntimeError("No monthly revenue rows fetched from official sources and no cached history exists")

    history = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    missing = set(OUTPUT_COLUMNS) - set(history.columns)
    if missing:
        raise RuntimeError(f"cached monthly revenue history missing columns: {sorted(missing)}")
    if history.empty:
        raise RuntimeError("No monthly revenue rows fetched from official sources and cached history is empty")
    markets = set(history["market"].astype(str))
    if not REQUIRED_MARKETS <= markets:
        raise RuntimeError(f"cached monthly revenue history missing required markets: {sorted(REQUIRED_MARKETS - markets)}")

    source_dates = [parse_yyyymmdd_date(value) for value in history["source_table_date"].astype(str)]
    source_dates = [value for value in source_dates if value is not None]
    if not source_dates:
        raise RuntimeError("cached monthly revenue history has no valid source_table_date")
    max_source_dt = max(source_dates)
    age_days = max(0, (fetch_dt - max_source_dt).days)
    if age_days > max_age_days:
        raise RuntimeError(
            "No monthly revenue rows fetched from official sources and cached history is stale: "
            f"max_source_table_date={max_source_dt.strftime('%Y%m%d')}, "
            f"age_days={age_days}, max_age_days={max_age_days}"
        )

    history = history[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True)
    fallback_status = {
        "market": "all",
        "source_market_name": "validated_history_cache",
        "source_url": display_path(history_path),
        "raw_rows": int(len(history)),
        "standardized_rows": int(len(history)),
        "status": FALLBACK_SOURCE_STATUS,
        "source_kind": FALLBACK_SOURCE_KIND,
        "fallback_reason": "official_sources_unavailable_or_incomplete",
        "fallback_fetch_date": fetch_date,
        "fallback_max_source_table_date": max_source_dt.strftime("%Y%m%d"),
        "fallback_age_days": age_days,
        "fallback_max_age_days": max_age_days,
    }
    return history, latest_period_rows(history), [*statuses, fallback_status]


def standardize_source(
    df: pd.DataFrame,
    *,
    market: str,
    source_market_name: str,
    source_url: str,
    fetch_date: str,
    fetch_timestamp: str,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    status: dict[str, Any] = {
        "market": market,
        "source_market_name": source_market_name,
        "source_url": source_url,
        "raw_rows": int(len(df)),
        "standardized_rows": 0,
        "status": "ok",
    }
    if df.empty:
        status["status"] = "empty_source"
        return pd.DataFrame(columns=OUTPUT_COLUMNS), status

    selected, selected_column_mode = select_source_columns(df)
    status["selected_columns"] = selected
    status["selected_column_indexes"] = {
        key: int(df.columns.get_loc(column))
        for key, column in selected.items()
        if column in df.columns
    }
    status["selected_column_mode"] = selected_column_mode
    required = ["stock_id", "revenue_period", "source_table_date", "latest_revenue_yoy_pct"]
    missing = [key for key in required if not selected.get(key)]
    if missing:
        status["status"] = f"missing_required_columns:{';'.join(missing)}"
        return pd.DataFrame(columns=OUTPUT_COLUMNS), status

    rows: list[dict[str, Any]] = []
    generated_at = now_text()
    for _, row in df.iterrows():
        stock_id = normalize_code(row.get(selected["stock_id"], ""))
        revenue_period, revenue_period_roc = parse_roc_or_yyyymm(row.get(selected["revenue_period"], ""))
        source_table_date, source_table_date_raw = parse_roc_or_yyyymmdd(row.get(selected["source_table_date"], ""))
        if not stock_id or not revenue_period or not source_table_date:
            continue
        values = {
            col: format_number(row.get(selected[col], "")) if selected.get(col) else ""
            for col in NUMERIC_COLUMNS
        }
        positive, strong = revenue_flags(
            values["latest_revenue_yoy_pct"],
            values["cumulative_revenue_yoy_pct"],
        )
        anomaly, anomaly_reason = anomaly_flag(
            values["latest_revenue_yoy_pct"],
            values["cumulative_revenue_yoy_pct"],
            values["monthly_revenue"],
        )
        source_file = RAW_DIR / raw_file_name(market, source_table_date, revenue_period)
        rows.append(
            {
                "generated_at": generated_at,
                "history_id": HISTORY_ID,
                "history_version": HISTORY_VERSION,
                "source_kind": SOURCE_KIND,
                "market": market,
                "source_market_name": source_market_name,
                "stock_id": stock_id,
                "stock_name": safe_str(row.get(selected.get("stock_name", ""), "")),
                "industry": safe_str(row.get(selected.get("industry", ""), "")),
                "revenue_period": revenue_period,
                "revenue_period_roc": revenue_period_roc,
                "source_table_date": source_table_date,
                "source_table_date_raw": source_table_date_raw,
                "fetch_date": fetch_date,
                "fetch_timestamp": fetch_timestamp,
                "source_url": source_url,
                "source_file": source_file.relative_to(ROOT).as_posix(),
                **values,
                "note": safe_str(row.get(selected.get("note", ""), "")),
                "revenue_positive_flag": positive,
                "revenue_strong_flag": strong,
                "revenue_numerical_anomaly_flag": anomaly,
                "revenue_numerical_anomaly_reason": anomaly_reason,
                "point_in_time_status": "ready_official_source_table_date",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
                "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
                "coverage_note": (
                    "full_market_current_monthly_revenue_saved_from_official_openapi; "
                    "historical coverage starts at the first saved source table date unless separately backfilled"
                ),
            }
        )

    out = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    status["standardized_rows"] = int(len(out))
    status["revenue_periods"] = sorted(out["revenue_period"].dropna().astype(str).unique().tolist()) if not out.empty else []
    status["source_table_dates"] = sorted(out["source_table_date"].dropna().astype(str).unique().tolist()) if not out.empty else []
    return out, status


def fetch_current_sources() -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    fetch_dt = now_taipei()
    fetch_date = fetch_dt.strftime("%Y%m%d")
    fetch_timestamp = fetch_dt.strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")
    attempts = env_int("MONTHLY_REVENUE_SOURCE_FETCH_ATTEMPTS", 3)
    sleep_seconds = env_int("MONTHLY_REVENUE_SOURCE_FETCH_SLEEP_SECONDS", 5, min_value=0)
    frames: list[pd.DataFrame] = []
    statuses: list[dict[str, Any]] = []
    for market, source_market_name, url in SOURCE_DEFS:
        raw = pd.DataFrame()
        fetch_error = ""
        try:
            for attempt in range(1, attempts + 1):
                try:
                    raw = fetch_source(url)
                    if not raw.empty or attempt == attempts:
                        break
                    fetch_error = "empty_raw_response"
                except Exception as exc:
                    fetch_error = str(exc)
                    if attempt == attempts:
                        raise
                if sleep_seconds:
                    time.sleep(sleep_seconds)
        except Exception as exc:
            statuses.append(
                {
                    "market": market,
                    "source_market_name": source_market_name,
                    "source_url": url,
                    "raw_rows": 0,
                    "standardized_rows": 0,
                    "status": f"fetch_failed:{exc}",
                    "fetch_attempts": attempts,
                }
            )
            continue
        standardized, status = standardize_source(
            raw,
            market=market,
            source_market_name=source_market_name,
            source_url=url,
            fetch_date=fetch_date,
            fetch_timestamp=fetch_timestamp,
        )
        status["fetch_attempts"] = attempts
        if fetch_error and status.get("status") == "ok":
            status["fetch_recovered_after"] = fetch_error
        statuses.append(status)
        if not standardized.empty:
            frames.append(standardized)
            for source_file in sorted(standardized["source_file"].unique()):
                target = ROOT / source_file
                target.parent.mkdir(parents=True, exist_ok=True)
                subset = raw.copy()
                subset.to_csv(target, index=False, encoding="utf-8-sig", lineterminator="\n")
    if not frames:
        return pd.DataFrame(columns=OUTPUT_COLUMNS), statuses
    current = pd.concat(frames, ignore_index=True)
    current = current.drop_duplicates(["market", "stock_id", "revenue_period"], keep="last")
    return current[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True), statuses


def merge_history(current: pd.DataFrame, history_path: Path = HISTORY_CSV) -> pd.DataFrame:
    if history_path.exists():
        existing = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    else:
        existing = pd.DataFrame(columns=OUTPUT_COLUMNS)
    for col in OUTPUT_COLUMNS:
        if col not in existing.columns:
            existing[col] = ""
        if col not in current.columns:
            current[col] = ""
    combined = pd.concat([existing[OUTPUT_COLUMNS], current[OUTPUT_COLUMNS]], ignore_index=True, sort=False)
    combined = combined.drop_duplicates(["market", "stock_id", "revenue_period"], keep="last")
    return combined[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True)


def write_markdown(
    history: pd.DataFrame,
    current: pd.DataFrame,
    statuses: list[dict[str, Any]],
    *,
    source_fetch_mode: str = "official_current_sources",
) -> None:
    source_kinds = (
        ";".join(sorted(set(history["source_kind"].dropna().astype(str))))
        if not history.empty and "source_kind" in history.columns
        else SOURCE_KIND
    )
    period_coverage = (
        history.groupby("revenue_period", dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"), source_table_date=("source_table_date", "max"))
        .reset_index()
        .sort_values("revenue_period")
        if not history.empty
        else pd.DataFrame(columns=["revenue_period", "rows", "unique_stocks", "source_table_date"])
    )
    market_coverage = (
        history.groupby(["revenue_period", "market"], dropna=False)
        .agg(rows=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
        .sort_values(["revenue_period", "market"])
        if not history.empty
        else pd.DataFrame(columns=["revenue_period", "market", "rows", "unique_stocks"])
    )
    anomalies = (
        history[history["revenue_numerical_anomaly_flag"].astype(str).eq("True")]
        .groupby("revenue_numerical_anomaly_reason", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values("rows", ascending=False)
        if not history.empty
        else pd.DataFrame(columns=["revenue_numerical_anomaly_reason", "rows"])
    )
    status_df = pd.DataFrame(statuses)
    lines = [
        "# Monthly Revenue History Data Layer",
        "",
        f"- generated_at: `{now_text()}`",
        f"- history_id: `{HISTORY_ID}`",
        f"- history_version: `{HISTORY_VERSION}`",
        f"- source_kind: `{source_kinds}`",
        f"- source_fetch_mode: `{source_fetch_mode}`",
        f"- latest_build_rows: `{len(current)}`",
        f"- total_history_rows: `{len(history)}`",
        f"- unique_stocks: `{history['stock_id'].nunique() if not history.empty else 0}`",
        f"- revenue_period_min: `{history['revenue_period'].min() if not history.empty else ''}`",
        f"- revenue_period_max: `{history['revenue_period'].max() if not history.empty else ''}`",
        "- allowed_use: save full-market official monthly revenue rows and join research rows where `source_table_date <= signal_date`.",
        "- forbidden_use: do not label older historical signals with the latest saved revenue period; formal model gates require sufficient coverage audit and promotion.",
        "- current_limitation: the current official OpenAPI returns the latest available revenue period only; older periods require validated historical backfill or accumulation over future runs.",
        "- historical_backfill_policy: static MOPS monthly revenue HTML backfill uses a conservative next-month-17 source date so historical research joins do not look ahead.",
        f"- official_source_fallback_policy: if any official OpenAPI source is empty or unavailable, reuse validated cached history for at most `{DEFAULT_FALLBACK_MAX_AGE_DAYS}` days from its latest `source_table_date`; stale cache fails closed.",
        "",
        "## Source Fetch Status",
        "",
        markdown_table(status_df, ["market", "source_market_name", "raw_rows", "standardized_rows", "status"], limit=10)
        if not status_df.empty
        else "No source status rows.",
        "",
        "## Period Coverage",
        "",
        markdown_table(period_coverage, ["revenue_period", "rows", "unique_stocks", "source_table_date"], limit=60)
        if not period_coverage.empty
        else "No period coverage rows.",
        "",
        "## Market Coverage",
        "",
        markdown_table(market_coverage, ["revenue_period", "market", "rows", "unique_stocks"], limit=80)
        if not market_coverage.empty
        else "No market coverage rows.",
        "",
        "## Numerical Anomaly Labels",
        "",
        markdown_table(anomalies, ["revenue_numerical_anomaly_reason", "rows"], limit=30)
        if not anomalies.empty
        else "No numerical anomaly labels.",
        "",
        "## Current Sample",
        "",
        markdown_table(
            current,
            [
                "market",
                "stock_id",
                "stock_name",
                "revenue_period",
                "source_table_date",
                "latest_revenue_yoy_pct",
                "cumulative_revenue_yoy_pct",
                "revenue_strong_flag",
                "allowed_for_formal_historical_model_use",
            ],
            limit=30,
        )
        if not current.empty
        else "No current rows.",
    ]
    LATEST_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_LATEST_MD.write_text(LATEST_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    current, statuses = fetch_current_sources()
    source_fetch_mode = "official_current_sources"
    if official_current_sources_ready(current, statuses):
        history = merge_history(current)
    else:
        try:
            history, current, statuses = load_recent_history_fallback(statuses)
        except RuntimeError as exc:
            statuses.append(
                {
                    "market": "all",
                    "source_market_name": "validated_history_cache",
                    "source_url": display_path(HISTORY_CSV),
                    "raw_rows": 0,
                    "standardized_rows": 0,
                    "status": f"fallback_unavailable:{exc}",
                }
            )
            SOURCE_STATUS_JSON.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            raise
        source_fetch_mode = "validated_history_cache_fallback"
    write_csv(history, HISTORY_CSV)
    write_csv(history, LATEST_CSV)
    write_csv(history, DOCS_LATEST_CSV)
    SOURCE_STATUS_JSON.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(history, current, statuses, source_fetch_mode=source_fetch_mode)
    print(f"Saved {HISTORY_CSV} rows={len(history)}")
    print(f"Saved {LATEST_CSV} rows={len(history)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
