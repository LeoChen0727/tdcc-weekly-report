from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_monthly_revenue_history import (  # noqa: E402
    DOCS_LATEST_CSV,
    DOCS_LATEST_MD,
    HISTORY_CSV,
    HISTORY_ID,
    HISTORY_VERSION,
    LATEST_CSV,
    LATEST_MD,
    NUMERIC_COLUMNS,
    OUTPUT_COLUMNS,
    RAW_DIR,
    SOURCE_STATUS_JSON,
    anomaly_flag,
    format_number,
    merge_history,
    normalize_code,
    revenue_flags,
    safe_str,
    write_markdown,
)
from tracking_utils import now_taipei, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
BACKFILL_SOURCE_KIND = "official_mops_static_monthly_revenue_html_conservative_available_date_v1"
SOURCE_TABLE_DATE_POLICY = "conservative_next_month_17th"
DEFAULT_BACKFILL_MONTHS = 25
RAW_HTML_DIR = RAW_DIR / "mops_html"
SOURCE_SCOPES = ("0", "1")

MARKET_DEFS = {
    "listed": {
        "source_market_name": "TWSE",
        "mops_path": "sii",
    },
    "otc": {
        "source_market_name": "TPEX",
        "mops_path": "otc",
    },
}

STATIC_COLUMNS = [
    "stock_id",
    "stock_name",
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


def period_to_parts(period: str) -> tuple[int, int]:
    digits = re.sub(r"\D", "", str(period or ""))
    if not re.fullmatch(r"20\d{4}", digits):
        raise ValueError(f"period must be YYYYMM, got {period!r}")
    month = int(digits[4:6])
    if not 1 <= month <= 12:
        raise ValueError(f"period month must be 01-12, got {period!r}")
    return int(digits[:4]), month


def period_add_months(period: str, months: int) -> str:
    year, month = period_to_parts(period)
    offset = year * 12 + (month - 1) + months
    return f"{offset // 12:04d}{offset % 12 + 1:02d}"


def iter_periods(start_period: str, end_period: str) -> list[str]:
    start_year, start_month = period_to_parts(start_period)
    end_year, end_month = period_to_parts(end_period)
    start_index = start_year * 12 + start_month
    end_index = end_year * 12 + end_month
    if start_index > end_index:
        raise ValueError(f"start_period must be <= end_period, got {start_period}>{end_period}")
    return [period_add_months(start_period, offset) for offset in range(end_index - start_index + 1)]


def conservative_source_table_date(period: str) -> str:
    return period_add_months(period, 1) + "17"


def latest_existing_period() -> str:
    if HISTORY_CSV.exists():
        history = pd.read_csv(HISTORY_CSV, dtype=str, keep_default_na=False)
        if "revenue_period" in history.columns:
            periods = sorted(
                period
                for period in history["revenue_period"].dropna().astype(str).unique().tolist()
                if re.fullmatch(r"20\d{4}", period)
            )
            if periods:
                return periods[-1]
    today = now_taipei()
    return f"{today.year:04d}{max(today.month - 1, 1):02d}"


def source_url(period: str, market: str, source_scope: str = "0") -> str:
    year, month = period_to_parts(period)
    roc_year = year - 1911
    mops_path = MARKET_DEFS[market]["mops_path"]
    return f"https://mopsov.twse.com.tw/nas/t21/{mops_path}/t21sc03_{roc_year}_{month}_{source_scope}.html"


def raw_html_path(period: str, market: str, source_scope: str = "0") -> Path:
    source_date = conservative_source_table_date(period)
    return RAW_HTML_DIR / f"monthly_revenue_html_{market}_{source_scope}_{source_date}_{period}.html"


def decode_mops_html(content: bytes) -> str:
    return content.decode("cp950", errors="replace").replace("\xa0", " ")


def fetch_or_read_html(period: str, market: str, source_scope: str, *, refresh: bool, dry_run: bool) -> tuple[str, str]:
    target = raw_html_path(period, market, source_scope)
    if target.exists() and not refresh:
        return decode_mops_html(target.read_bytes()), target.relative_to(ROOT).as_posix()

    url = source_url(period, market, source_scope)
    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    if len(response.content) < 10_000:
        raise ValueError(f"monthly revenue static html is unexpectedly small: {url}")
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(response.content)
    return decode_mops_html(response.content), target.relative_to(ROOT).as_posix()


def extract_industry(frame: pd.DataFrame) -> str:
    values = [safe_str(value) for value in frame.columns.tolist()]
    values.extend(safe_str(value) for value in frame.astype(str).values.flatten().tolist())
    for value in values:
        if "產業別" in value:
            return value.split("產業別", 1)[-1].replace("：", "").replace(":", "").strip()
    return ""


def parse_static_html(
    html: str,
    *,
    period: str,
    market: str,
    source_file: str,
    source_url_text: str,
    fetch_date: str,
    fetch_timestamp: str,
) -> pd.DataFrame:
    source_date = conservative_source_table_date(period)
    revenue_period_roc = f"{period_to_parts(period)[0] - 1911}{period[4:6]}"
    generated_at = now_text()
    current_industry = ""
    rows: list[dict[str, Any]] = []

    tables = pd.read_html(io.StringIO(html))
    for frame in tables:
        industry = extract_industry(frame)
        if industry:
            current_industry = industry
            continue
        if frame.empty:
            continue
        if frame.shape[1] != len(STATIC_COLUMNS):
            continue
        frame = frame.copy()
        frame.columns = STATIC_COLUMNS
        for _, source_row in frame.iterrows():
            stock_id = normalize_code(source_row.get("stock_id"))
            if not re.fullmatch(r"\d{4,6}", stock_id or ""):
                continue
            values = {
                col: format_number(source_row.get(col, "")) if col in NUMERIC_COLUMNS else ""
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
            rows.append(
                {
                    "generated_at": generated_at,
                    "history_id": HISTORY_ID,
                    "history_version": HISTORY_VERSION,
                    "source_kind": BACKFILL_SOURCE_KIND,
                    "market": market,
                    "source_market_name": MARKET_DEFS[market]["source_market_name"],
                    "stock_id": stock_id,
                    "stock_name": safe_str(source_row.get("stock_name")),
                    "industry": current_industry,
                    "revenue_period": period,
                    "revenue_period_roc": revenue_period_roc,
                    "source_table_date": source_date,
                    "source_table_date_raw": SOURCE_TABLE_DATE_POLICY,
                    "fetch_date": fetch_date,
                    "fetch_timestamp": fetch_timestamp,
                    "source_url": source_url_text,
                    "source_file": source_file,
                    **values,
                    "note": safe_str(source_row.get("note")),
                    "revenue_positive_flag": positive,
                    "revenue_strong_flag": strong,
                    "revenue_numerical_anomaly_flag": anomaly,
                    "revenue_numerical_anomaly_reason": anomaly_reason,
                    "point_in_time_status": "ready_official_source_table_date",
                    "research_join_allowed": "True",
                    "allowed_for_formal_historical_model_use": "False",
                    "formal_use_blocker": "blocked_until_sufficient_history_coverage_and_model_promotion",
                    "coverage_note": (
                        "backfilled_from_official_mops_static_monthly_revenue_html; "
                        "source_table_date uses conservative_next_month_17th to avoid lookahead"
                    ),
                }
            )

    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)


def build_backfill(start_period: str, end_period: str, *, refresh: bool, dry_run: bool) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    fetch_dt = now_taipei()
    fetch_date = fetch_dt.strftime("%Y%m%d")
    fetch_timestamp = fetch_dt.strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")
    frames: list[pd.DataFrame] = []
    statuses: list[dict[str, Any]] = []
    for period in iter_periods(start_period, end_period):
        for market in MARKET_DEFS:
            for source_scope in SOURCE_SCOPES:
                url = source_url(period, market, source_scope)
                source_date = conservative_source_table_date(period)
                try:
                    html, source_file = fetch_or_read_html(period, market, source_scope, refresh=refresh, dry_run=dry_run)
                    frame = parse_static_html(
                        html,
                        period=period,
                        market=market,
                        source_file=source_file,
                        source_url_text=url,
                        fetch_date=fetch_date,
                        fetch_timestamp=fetch_timestamp,
                    )
                    status = "ok" if not frame.empty else "empty_source"
                except Exception as exc:
                    frame = pd.DataFrame(columns=OUTPUT_COLUMNS)
                    source_file = raw_html_path(period, market, source_scope).relative_to(ROOT).as_posix()
                    status = f"fetch_or_parse_failed:{exc}"
                statuses.append(
                    {
                        "market": market,
                        "source_market_name": MARKET_DEFS[market]["source_market_name"],
                        "source_scope": source_scope,
                        "source_url": url,
                        "revenue_period": period,
                        "source_table_date": source_date,
                        "source_table_date_policy": SOURCE_TABLE_DATE_POLICY,
                        "source_file": source_file,
                        "raw_rows": int(len(frame)),
                        "standardized_rows": int(len(frame)),
                        "status": status,
                    }
                )
                if not frame.empty:
                    frames.append(frame)
    if not frames:
        return pd.DataFrame(columns=OUTPUT_COLUMNS), statuses
    backfill = pd.concat(frames, ignore_index=True)
    backfill = backfill.drop_duplicates(["market", "stock_id", "revenue_period"], keep="last")
    return backfill[OUTPUT_COLUMNS].sort_values(["revenue_period", "market", "stock_id"]).reset_index(drop=True), statuses


def write_outputs(backfill: pd.DataFrame, statuses: list[dict[str, Any]]) -> pd.DataFrame:
    history = merge_history(backfill, HISTORY_CSV)
    write_csv(history, HISTORY_CSV)
    write_csv(history, LATEST_CSV)
    write_csv(history, DOCS_LATEST_CSV)
    SOURCE_STATUS_JSON.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_STATUS_JSON.write_text(json.dumps(statuses, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    write_markdown(history, backfill, statuses)
    return history


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill monthly revenue history from official MOPS static HTML pages.")
    parser.add_argument("--start-period", default="", help="Inclusive YYYYMM period. Default: end-period minus months-1.")
    parser.add_argument("--end-period", default="", help="Inclusive YYYYMM period. Default: latest period already present in history.")
    parser.add_argument("--months", type=int, default=DEFAULT_BACKFILL_MONTHS, help="Default number of periods when start-period is omitted.")
    parser.add_argument("--refresh", action="store_true", help="Refetch raw HTML even when the raw cache exists.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and parse without writing artifacts.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    end_period = args.end_period or latest_existing_period()
    start_period = args.start_period or period_add_months(end_period, -(max(args.months, 1) - 1))
    backfill, statuses = build_backfill(start_period, end_period, refresh=bool(args.refresh), dry_run=bool(args.dry_run))
    failed = [status for status in statuses if status.get("status") != "ok"]
    if failed:
        for status in failed[:10]:
            print(f"ERROR: monthly revenue backfill source failed: {status}")
        return 1
    if args.dry_run:
        history_rows = 0
    else:
        history = write_outputs(backfill, statuses)
        history_rows = len(history)
    print(f"backfilled_monthly_revenue_periods={len(iter_periods(start_period, end_period))}")
    print(f"backfilled_monthly_revenue_rows={len(backfill)}")
    print(f"monthly_revenue_history_rows={history_rows}")
    print(f"source_table_date_policy={SOURCE_TABLE_DATE_POLICY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
