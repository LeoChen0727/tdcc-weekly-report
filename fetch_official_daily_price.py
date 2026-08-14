from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError, as_completed
import csv
import hashlib
import io
import json
import math
import os
import re
import shutil
import stat
import time
import uuid
from typing import Any

import pandas as pd
import requests


TAIPEI = ZoneInfo("Asia/Taipei")

DATA_DIR = Path("data/daily_price")
OUTPUT_LATEST = Path("output/latest")
OUTPUT_DEBUG = Path("output/debug")
CONFIG_DIR = Path("config")

LATEST_PRICE_CSV = OUTPUT_LATEST / "official_daily_price_latest.csv"
LATEST_FETCH_MD = OUTPUT_LATEST / "official_price_fetch_latest.md"
LATEST_FETCH_JSON = OUTPUT_LATEST / "official_price_fetch_latest.json"
OFFICIAL_PRICE_TRANSACTION_DIR = (
    OUTPUT_LATEST / ".official_price_evidence_transaction"
)
DEBUG_MD = OUTPUT_DEBUG / "official_price_fetch_debug_latest.md"

ALL_CANDIDATES_CSV = OUTPUT_LATEST / "all_candidates_latest.csv"
CURRENT_HOLDINGS_JSON = CONFIG_DIR / "current_holdings.json"
CANONICAL_STOCK_NAME_SOURCES = [
    OUTPUT_LATEST / "company_industry_snapshot_latest.csv",
    Path("docs/latest/company_industry_snapshot_latest.csv"),
    OUTPUT_LATEST / "stock_theme_taxonomy_latest.csv",
    Path("docs/latest/stock_theme_taxonomy_latest.csv"),
]

REQUEST_TIMEOUT = int(os.environ.get("OFFICIAL_PRICE_REQUEST_TIMEOUT", "25"))
INDIVIDUAL_REQUEST_TIMEOUT = int(os.environ.get("OFFICIAL_PRICE_INDIVIDUAL_REQUEST_TIMEOUT", "8"))
INDIVIDUAL_FALLBACK_MAX_SECONDS = int(
    os.environ.get("OFFICIAL_PRICE_INDIVIDUAL_FALLBACK_MAX_SECONDS", "180")
)
SCRIPT_MAX_SECONDS = int(os.environ.get("OFFICIAL_PRICE_FETCH_MAX_SECONDS", "480"))

MIN_TWSE_ROWS = 700
MIN_TPEX_ROWS = 500
MIN_FULL_ROWS = 1300

# 個股 fallback 最多同時請求數，太高容易被官方擋
MAX_WORKERS = 12
REQUEST_SLEEP_SECONDS = 0.02

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0 Safari/537.36"
)

FINAL_COLUMNS = [
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
]
FETCH_RESPONSE_PROVENANCE: list[dict[str, Any]] = []
REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES = False


def reset_fetch_response_provenance() -> None:
    FETCH_RESPONSE_PROVENANCE.clear()


def fetch_response_provenance() -> list[dict[str, Any]]:
    return [dict(row) for row in FETCH_RESPONSE_PROVENANCE]


def collect_official_response_dates_from_text(text: str) -> list[str]:
    payload = parse_json(text)
    values: list[str] = []
    if isinstance(payload, dict):
        for key in ("title", "date", "queryDate", "reportDate", "tradeDate"):
            if key in payload and not isinstance(payload[key], (dict, list)):
                values.append(str(payload[key]))
        tables = payload.get("tables")
        if isinstance(tables, list):
            for table in tables:
                if not isinstance(table, dict):
                    continue
                for key in ("title", "date", "queryDate", "reportDate", "tradeDate"):
                    if key in table and not isinstance(table[key], (dict, list)):
                        values.append(str(table[key]))
    elif payload is None:
        # Official CSV puts the report title on its first non-empty line.
        # Do not scan securities rows, where unrelated dates may appear.
        first_line = next((line.strip() for line in str(text or "").splitlines() if line.strip()), "")
        if first_line:
            values.append(first_line)
    dates: set[str] = set()
    for value in values:
        for roc_year, month, day in re.findall(r"(?<!\d)(\d{2,3})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日", value):
            try:
                dates.add(datetime(int(roc_year) + 1911, int(month), int(day)).strftime("%Y%m%d"))
            except ValueError:
                continue
        for year, month, day in re.findall(r"(?<!\d)(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})(?!\d)", value):
            try:
                dates.add(datetime(int(year), int(month), int(day)).strftime("%Y%m%d"))
            except ValueError:
                continue
        for compact in re.findall(r"(?<!\d)(20\d{6})(?!\d)", value):
            try:
                dates.add(datetime.strptime(compact, "%Y%m%d").strftime("%Y%m%d"))
            except ValueError:
                continue
    return sorted(dates)


def record_response_provenance(
    url: str,
    response: Any,
    *,
    source_name: str = "",
    expected_response_date: str = "",
) -> dict[str, Any]:
    text = str(getattr(response, "text", "") or "")
    raw = getattr(response, "content", None)
    if not isinstance(raw, bytes):
        raw = text.encode("utf-8")
    observed_dates = collect_official_response_dates_from_text(text)
    row = {
            "endpoint": url,
            "source_name": source_name,
            "params": {},
            "status_code": int(getattr(response, "status_code", 0) or 0),
            "fetched_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "normalized_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "observed_response_dates": observed_dates,
            "expected_response_date": expected_response_date,
            "exact_date_match": (
                observed_dates == [expected_response_date] if expected_response_date else "not_required"
            ),
        }
    FETCH_RESPONSE_PROVENANCE.append(row)
    return dict(row)


def now_taipei() -> datetime:
    return datetime.now(TAIPEI)


def remaining_seconds(deadline: float | None) -> float:
    if deadline is None:
        return float("inf")
    return max(0.0, deadline - time.monotonic())


def ymd(dt: datetime) -> str:
    return dt.strftime("%Y%m%d")


def normalize_date_text(value: Any) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    # ROC date: 115/05/22, 1150522
    if len(digits) >= 7:
        try:
            roc_year = int(digits[:3])
            year = roc_year + 1911
            month = int(digits[3:5])
            day = int(digits[5:7])
            return f"{year:04d}{month:02d}{day:02d}"
        except Exception:
            pass

    return ""


def roc_date_from_yyyymmdd(date_text: str) -> str:
    year = int(date_text[:4]) - 1911
    return f"{year}/{date_text[4:6]}/{date_text[6:8]}"


def slash_date_from_yyyymmdd(date_text: str) -> str:
    return f"{date_text[:4]}/{date_text[4:6]}/{date_text[6:8]}"


def extract_response_date(text: str) -> str:
    for pattern in [
        r'"date"\s*:\s*"([^"]+)"',
        r"(?:資料日期|Date)\s*[:：]\s*([0-9]{3,4}/[0-9]{1,2}/[0-9]{1,2}|[0-9]{8})",
    ]:
        match = re.search(pattern, text)
        if match:
            return normalize_date_text(match.group(1))
    return ""


def collect_json_response_dates(node: Any) -> set[str]:
    dates: set[str] = set()
    if isinstance(node, dict):
        for key, value in node.items():
            if str(key).lower() == "date":
                parsed = normalize_date_text(value)
                if parsed:
                    dates.add(parsed)
            if isinstance(value, (list, dict)):
                dates.update(collect_json_response_dates(value))
    elif isinstance(node, list):
        for value in node:
            if isinstance(value, (list, dict)):
                dates.update(collect_json_response_dates(value))
    return dates


def response_date_matches_target(response_date: str, target_date: str) -> bool:
    return bool(response_date) and response_date == target_date


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "<na>", "null"}:
        return ""
    return text


def clean_number(value: Any) -> float:
    text = safe_str(value)

    if text in {"", "--", "-", "X", "x", "除權", "除息", "除權息"}:
        return math.nan

    text = text.replace(",", "")
    text = text.replace("+", "")
    text = text.replace("％", "")
    text = text.replace("%", "")
    text = re.sub(r"[^\d.\-]", "", text)

    if text in {"", "-", ".", "-."}:
        return math.nan

    try:
        return float(text)
    except Exception:
        return math.nan


def clean_int(value: Any) -> int:
    number = clean_number(value)
    if math.isnan(number):
        return 0
    return int(round(number))


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Za-z]", "", text)

    if text.isdigit():
        return text.zfill(4)

    return text


def is_valid_stock_id(stock_id: str) -> bool:
    return bool(re.fullmatch(r"\d{4,6}", safe_str(stock_id)))


def request_text(
    url: str,
    log: list[str],
    referer: str = "https://www.twse.com.tw/",
    *,
    source_name: str = "",
    expected_response_date: str = "",
) -> str:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": referer,
    }

    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        provenance = record_response_provenance(
            url,
            response,
            source_name=source_name,
            expected_response_date=expected_response_date,
        )
        text = response.text or ""
        log.append(f"GET {url} -> status={response.status_code}, chars={len(text)}")

        if response.status_code != 200:
            return ""
        if expected_response_date and provenance["exact_date_match"] is not True:
            log.append(
                f"{source_name}: rejected response date evidence "
                f"{provenance['observed_response_dates']}; target date is {expected_response_date}"
            )
            return ""

        return text
    except Exception as exc:
        log.append(f"GET {url} failed: {type(exc).__name__}: {exc}")
        return ""


def parse_json(text: str) -> Any:
    if not text:
        return None

    text = text.lstrip("\ufeff").strip()

    try:
        return json.loads(text)
    except Exception:
        return None


def normalize_row(
    *,
    date_text: str,
    stock_id: Any,
    stock_name: Any,
    market: str,
    open_price: Any,
    high_price: Any,
    low_price: Any,
    close_price: Any,
    volume: Any,
    trading_value: Any,
    source: str,
) -> dict[str, Any] | None:
    sid = normalize_stock_id(stock_id)
    name = safe_str(stock_name)

    if not is_valid_stock_id(sid):
        return None

    o = clean_number(open_price)
    h = clean_number(high_price)
    l = clean_number(low_price)
    c = clean_number(close_price)

    if math.isnan(c):
        return None

    if math.isnan(o):
        o = c
    if math.isnan(h):
        h = max(o, c)
    if math.isnan(l):
        l = min(o, c)

    vol = clean_int(volume)
    val = clean_int(trading_value)

    if vol <= 0 and val <= 0:
        return None

    return {
        "date": date_text,
        "stock_id": sid,
        "stock_name": name,
        "market": market,
        "open": o,
        "high": h,
        "low": l,
        "close": c,
        "volume": vol,
        "trading_value": val,
        "source": source,
    }


def dataframe_from_rows(rows: list[dict[str, Any]]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=FINAL_COLUMNS)

    df = pd.DataFrame(rows)

    for col in FINAL_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df = df[FINAL_COLUMNS].copy()
    df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)
    df = df.drop_duplicates(["date", "stock_id"], keep="first")
    df = df.sort_values(["market", "stock_id"]).reset_index(drop=True)

    return df


def load_canonical_stock_names() -> dict[str, str]:
    names: dict[str, str] = {}
    for path in CANONICAL_STOCK_NAME_SOURCES:
        if not path.exists():
            continue
        try:
            df = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
        except Exception:
            continue
        if not {"stock_id", "stock_name"}.issubset(df.columns):
            continue
        for _, row in df.iterrows():
            stock_id = normalize_stock_id(row.get("stock_id", ""))
            stock_name = safe_str(row.get("stock_name", ""))
            if stock_id and stock_name and stock_id not in names:
                names[stock_id] = stock_name
    return names


def apply_canonical_stock_names(df: pd.DataFrame, log: list[str] | None = None) -> pd.DataFrame:
    if df.empty or not {"stock_id", "stock_name"}.issubset(df.columns):
        return df
    names = load_canonical_stock_names()
    if not names:
        return df

    out = df.copy()
    canonical = out["stock_id"].map(lambda value: names.get(normalize_stock_id(value), ""))
    current = out["stock_name"].map(safe_str)
    mask = canonical.map(bool)
    changed = int((mask & current.ne(canonical)).sum())
    out.loc[mask, "stock_name"] = canonical[mask]
    if log is not None and changed:
        log.append(f"Applied canonical stock names from metadata snapshot changed_rows={changed}")
    return out


def parse_twse_mi_index_list_row(item: list[Any], date_text: str, source: str) -> dict[str, Any] | None:
    if len(item) < 9:
        return None

    # TWSE MI_INDEX 常見欄位：
    # 0 證券代號
    # 1 證券名稱
    # 2 成交股數
    # 3 成交筆數
    # 4 成交金額
    # 5 開盤價
    # 6 最高價
    # 7 最低價
    # 8 收盤價
    return normalize_row(
        date_text=date_text,
        stock_id=item[0],
        stock_name=item[1],
        market="TWSE",
        volume=item[2],
        trading_value=item[4],
        open_price=item[5],
        high_price=item[6],
        low_price=item[7],
        close_price=item[8],
        source=source,
    )


def parse_twse_mi_index_json(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json(text)

    if not isinstance(obj, dict):
        log.append(f"{source}: JSON parse failed")
        return pd.DataFrame(columns=FINAL_COLUMNS)
    if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES:
        response_dates = collect_official_response_dates_from_text(text)
        if response_dates != [date_text]:
            log.append(
                f"{source}: rejected TWSE response dates {response_dates}; target date is {date_text}"
            )
            return pd.DataFrame(columns=FINAL_COLUMNS)

    rows: list[dict[str, Any]] = []

    possible_data = []

    for key in ["data9", "data", "aaData"]:
        if isinstance(obj.get(key), list):
            possible_data.append(obj[key])

    if isinstance(obj.get("tables"), list):
        for table in obj["tables"]:
            if isinstance(table, dict):
                for key in ["data", "aaData"]:
                    if isinstance(table.get(key), list):
                        possible_data.append(table[key])

    for data in possible_data:
        for item in data:
            if isinstance(item, list):
                parsed = parse_twse_mi_index_list_row(item, date_text, source)
                if parsed:
                    rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TWSE rows={len(df)}")
    return df


def parse_twse_mi_index_csv(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES:
        response_dates = collect_official_response_dates_from_text(text)
        if response_dates != [date_text]:
            log.append(
                f"{source}: rejected TWSE CSV response dates {response_dates}; target date is {date_text}"
            )
            return pd.DataFrame(columns=FINAL_COLUMNS)
    rows = []

    reader = csv.reader(io.StringIO(text.lstrip("\ufeff")))

    for item in reader:
        if len(item) < 9:
            continue

        if not re.fullmatch(r"\s*\d{4,6}\s*", safe_str(item[0])):
            continue

        parsed = parse_twse_mi_index_list_row(item, date_text, source)
        if parsed:
            rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TWSE CSV rows={len(df)}")
    return df


def parse_twse_openapi_stock_day_all(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json(text)

    if not isinstance(obj, list):
        log.append(f"{source}: JSON parse failed or not list")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    for item in obj:
        if not isinstance(item, dict):
            continue

        parsed = normalize_row(
            date_text=date_text,
            stock_id=item.get("Code") or item.get("證券代號") or item.get("stock_id"),
            stock_name=item.get("Name") or item.get("證券名稱") or item.get("stock_name"),
            market="TWSE",
            volume=item.get("TradeVolume") or item.get("成交股數") or item.get("Volume"),
            trading_value=item.get("TradeValue") or item.get("成交金額") or item.get("TradingValue"),
            open_price=item.get("OpeningPrice") or item.get("開盤價") or item.get("Open"),
            high_price=item.get("HighestPrice") or item.get("最高價") or item.get("High"),
            low_price=item.get("LowestPrice") or item.get("最低價") or item.get("Low"),
            close_price=item.get("ClosingPrice") or item.get("收盤價") or item.get("Close"),
            source=source,
        )

        if parsed:
            rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TWSE OpenAPI rows={len(df)}")
    return df


def fetch_twse_batch(date_text: str, log: list[str]) -> pd.DataFrame:
    urls = [
        (
            "TWSE_RWD_JSON_MI_INDEX",
            f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_text}&type=ALLBUT0999&response=json",
            "json_mi",
        ),
        (
            "TWSE_RWD_CSV_MI_INDEX",
            f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_text}&type=ALLBUT0999&response=csv",
            "csv_mi",
        ),
        (
            "TWSE_LEGACY_JSON_MI_INDEX",
            f"https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&date={date_text}&type=ALLBUT0999",
            "json_mi",
        ),
        (
            "TWSE_OPENAPI_STOCK_DAY_ALL",
            "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL",
            "openapi",
        ),
    ]

    best = pd.DataFrame(columns=FINAL_COLUMNS)

    for source, url, kind in urls:
        if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES and kind == "openapi":
            log.append(f"Skip TWSE latest-only source={source} for historical target date {date_text}")
            continue
        log.append(f"Trying TWSE batch source={source} date={date_text}")
        text = request_text(
            url,
            log,
            referer="https://www.twse.com.tw/",
            source_name=source,
            expected_response_date=(date_text if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES else ""),
        )

        if not text:
            continue

        if kind == "json_mi":
            df = parse_twse_mi_index_json(text, date_text, source, log)
        elif kind == "csv_mi":
            df = parse_twse_mi_index_csv(text, date_text, source, log)
        elif kind == "openapi":
            df = parse_twse_openapi_stock_day_all(text, date_text, source, log)
        else:
            df = pd.DataFrame(columns=FINAL_COLUMNS)

        if len(df) > len(best):
            best = df

        if len(df) >= MIN_TWSE_ROWS:
            log.append(f"TWSE batch selected source={source}, rows={len(df)}")
            return df

    log.append(f"TWSE batch best rows={len(best)}")
    return best


def parse_twse_stock_day_individual(
    text: str,
    date_text: str,
    stock_id: str,
    stock_name: str,
    log: list[str] | None = None,
) -> dict[str, Any] | None:
    obj = parse_json(text)

    if not isinstance(obj, dict):
        return None

    data = obj.get("data")

    if not isinstance(data, list):
        return None

    for row in data:
        if not isinstance(row, list) or len(row) < 9:
            continue

        row_date = normalize_date_text(row[0])

        if row_date != date_text:
            continue

        # STOCK_DAY 欄位：
        # 0 日期
        # 1 成交股數
        # 2 成交金額
        # 3 開盤價
        # 4 最高價
        # 5 最低價
        # 6 收盤價
        return normalize_row(
            date_text=date_text,
            stock_id=stock_id,
            stock_name=stock_name,
            market="TWSE",
            volume=row[1],
            trading_value=row[2],
            open_price=row[3],
            high_price=row[4],
            low_price=row[5],
            close_price=row[6],
            source="TWSE_INDIVIDUAL_STOCK_DAY",
        )

    return None


def fetch_twse_individual_one(
    date_text: str,
    stock_id: str,
    stock_name: str,
) -> dict[str, Any] | None:
    url = (
        "https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY"
        f"?date={date_text}&stockNo={stock_id}&response=json"
    )

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/plain,*/*",
        "Referer": "https://www.twse.com.tw/",
    }

    try:
        time.sleep(REQUEST_SLEEP_SECONDS)
        resp = requests.get(url, headers=headers, timeout=INDIVIDUAL_REQUEST_TIMEOUT)
        record_response_provenance(url, resp)
        if resp.status_code != 200:
            return None

        return parse_twse_stock_day_individual(
            resp.text,
            date_text=date_text,
            stock_id=stock_id,
            stock_name=stock_name,
        )
    except Exception:
        return None


def fetch_twse_individual_fallback(
    date_text: str,
    universe: pd.DataFrame,
    log: list[str],
    *,
    deadline: float | None = None,
) -> pd.DataFrame:
    if universe.empty:
        log.append("TWSE individual fallback skipped: empty universe")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    part = universe.copy()

    if "market" in part.columns:
        part = part[part["market"].astype(str).str.upper().eq("TWSE")].copy()

    if part.empty:
        log.append("TWSE individual fallback skipped: no TWSE universe rows")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    part["stock_id"] = part["stock_id"].astype(str).str.zfill(4)
    part = part.drop_duplicates("stock_id")

    fallback_deadline = time.monotonic() + INDIVIDUAL_FALLBACK_MAX_SECONDS
    if deadline is not None:
        fallback_deadline = min(fallback_deadline, deadline)

    jobs = []
    rows = []

    log.append(
        f"TWSE individual fallback start: stocks={len(part)} date={date_text} "
        f"budget_seconds={remaining_seconds(fallback_deadline):.0f}"
    )

    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    try:
        for _, row in part.iterrows():
            if remaining_seconds(fallback_deadline) <= 1:
                log.append("TWSE individual fallback submit stopped: time budget exhausted")
                break

            sid = safe_str(row.get("stock_id", "")).zfill(4)
            name = safe_str(row.get("stock_name", ""))

            if not is_valid_stock_id(sid):
                continue

            jobs.append(executor.submit(fetch_twse_individual_one, date_text, sid, name))

        try:
            for future in as_completed(jobs, timeout=max(1.0, remaining_seconds(fallback_deadline))):
                result = future.result()
                if result:
                    rows.append(result)
                if remaining_seconds(fallback_deadline) <= 1:
                    log.append("TWSE individual fallback collection stopped: time budget exhausted")
                    break
        except FutureTimeoutError:
            log.append(
                f"TWSE individual fallback timed out after collecting rows={len(rows)} "
                f"submitted={len(jobs)}"
            )
    finally:
        for future in jobs:
            future.cancel()
        executor.shutdown(wait=False, cancel_futures=True)

    df = dataframe_from_rows(rows)
    log.append(f"TWSE individual fallback parsed rows={len(df)}")
    return df


def parse_tpex_list_row(item: list[Any], date_text: str, source: str) -> dict[str, Any] | None:
    if len(item) < 8:
        return None

    if not re.fullmatch(r"\s*\d{4,6}\s*", safe_str(item[0])):
        return None

    # TPEx 常見欄位：
    # 0 代號
    # 1 名稱
    # 2 收盤
    # 3 漲跌
    # 4 開盤
    # 5 最高
    # 6 最低
    # 7 成交股數 / 成交張數
    # 8 成交金額
    return normalize_row(
        date_text=date_text,
        stock_id=item[0],
        stock_name=item[1] if len(item) > 1 else "",
        market="TPEx",
        close_price=item[2] if len(item) > 2 else "",
        open_price=item[4] if len(item) > 4 else "",
        high_price=item[5] if len(item) > 5 else "",
        low_price=item[6] if len(item) > 6 else "",
        volume=item[7] if len(item) > 7 else "",
        trading_value=item[8] if len(item) > 8 else "",
        source=source,
    )


def parse_tpex_dict_row(item: dict[str, Any], date_text: str, source: str) -> dict[str, Any] | None:
    stock_id = (
        item.get("SecuritiesCompanyCode")
        or item.get("SecuritiesCode")
        or item.get("Code")
        or item.get("代號")
        or item.get("有價證券代號")
        or item.get("stock_id")
    )

    stock_name = (
        item.get("CompanyName")
        or item.get("Name")
        or item.get("名稱")
        or item.get("有價證券名稱")
        or item.get("stock_name")
    )

    return normalize_row(
        date_text=date_text,
        stock_id=stock_id,
        stock_name=stock_name,
        market="TPEx",
        open_price=item.get("Open") or item.get("OpenPrice") or item.get("開盤") or item.get("開盤價"),
        high_price=item.get("High") or item.get("HighPrice") or item.get("最高") or item.get("最高價"),
        low_price=item.get("Low") or item.get("LowPrice") or item.get("最低") or item.get("最低價"),
        close_price=item.get("Close") or item.get("ClosePrice") or item.get("收盤") or item.get("收盤價"),
        volume=item.get("TradingShares") or item.get("成交股數") or item.get("Volume") or item.get("成交量"),
        trading_value=item.get("TransactionAmount") or item.get("成交金額") or item.get("TradingValue") or item.get("成交值"),
        source=source,
    )


def parse_tpex_json(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json(text)

    if obj is None:
        log.append(f"{source}: JSON parse failed")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    response_dates = collect_json_response_dates(obj)
    official_response_dates = set(collect_official_response_dates_from_text(text))
    if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES and official_response_dates != {date_text}:
        log.append(
            f"{source}: rejected response dates {sorted(official_response_dates)}; target date is {date_text}"
        )
        return pd.DataFrame(columns=FINAL_COLUMNS)
    if response_dates and date_text not in response_dates:
        log.append(
            f"{source}: rejected response dates {sorted(response_dates)}; target date is {date_text}"
        )
        return pd.DataFrame(columns=FINAL_COLUMNS)
    if response_dates and date_text in response_dates and len(response_dates) > 1:
        unexpected = sorted(date for date in response_dates if date != date_text)
        if unexpected:
            log.append(
                f"{source}: rejected mixed response dates {sorted(response_dates)}; target date is {date_text}"
            )
            return pd.DataFrame(columns=FINAL_COLUMNS)

    rows: list[dict[str, Any]] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            parsed = parse_tpex_dict_row(node, date_text, source)
            if parsed:
                rows.append(parsed)

            for key in ["aaData", "data", "tables", "items", "list"]:
                if key in node:
                    walk(node[key])

            for value in node.values():
                if isinstance(value, (list, dict)):
                    walk(value)

        elif isinstance(node, list):
            if node and all(not isinstance(x, (list, dict)) for x in node):
                parsed = parse_tpex_list_row(node, date_text, source)
                if parsed:
                    rows.append(parsed)
            else:
                for value in node:
                    walk(value)

    walk(obj)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TPEx JSON rows={len(df)}")
    return df


def parse_tpex_csv(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    response_date = extract_response_date(text)
    official_response_dates = collect_official_response_dates_from_text(text)
    if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES and official_response_dates != [date_text]:
        log.append(
            f"{source}: rejected response dates {official_response_dates}; target date is {date_text}"
        )
        return pd.DataFrame(columns=FINAL_COLUMNS)
    if response_date and not response_date_matches_target(response_date, date_text):
        log.append(f"{source}: rejected response date {response_date}; target date is {date_text}")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    reader = csv.reader(io.StringIO(text.lstrip("\ufeff")))

    for item in reader:
        if len(item) < 8:
            continue

        if not re.fullmatch(r"\s*\d{4,6}\s*", safe_str(item[0])):
            continue

        parsed = parse_tpex_list_row(item, date_text, source)
        if parsed:
            rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TPEx CSV rows={len(df)}")
    return df


def fetch_tpex_batch(date_text: str, log: list[str]) -> pd.DataFrame:
    roc_date = roc_date_from_yyyymmdd(date_text)
    slash_date = slash_date_from_yyyymmdd(date_text)
    current_date = ymd(now_taipei())

    urls = [
        (
            "TPEX_NEW_AFTERTRADING_JSON",
            f"https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date={slash_date}&type=EW&response=json",
            "json",
        ),
        (
            "TPEX_NEW_AFTERTRADING_CSV",
            f"https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyCloseQuotes?date={slash_date}&type=EW&response=csv",
            "csv",
        ),
        (
            "TPEX_OTC_QUOTES_NO1430_JSON",
            f"https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=json&d={roc_date}&se=EW",
            "json",
        ),
        (
            "TPEX_OTC_QUOTES_NO1430_CSV",
            f"https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=csv&d={roc_date}&se=EW",
            "csv",
        ),
        (
            "TPEX_OLD_DAILY_JSON",
            f"https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=json&d={roc_date}&s=0,asc,0",
            "json",
        ),
        (
            "TPEX_OLD_DAILY_CSV",
            f"https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw&o=csv&d={roc_date}&s=0,asc,0",
            "csv",
        ),
        (
            "TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES",
            "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes",
            "json",
        ),
    ]

    best = pd.DataFrame(columns=FINAL_COLUMNS)

    for source, url, kind in urls:
        if source.startswith("TPEX_OPENAPI_") and date_text != current_date:
            log.append(
                f"Skip TPEx latest-only source={source} for historical target date {date_text}"
            )
            continue
        log.append(f"Trying TPEx batch source={source} date={date_text}")
        text = request_text(
            url,
            log,
            referer="https://www.tpex.org.tw/",
            source_name=source,
            expected_response_date=(date_text if REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES else ""),
        )

        if not text:
            continue

        if kind == "json":
            df = parse_tpex_json(text, date_text, source, log)
        elif kind == "csv":
            df = parse_tpex_csv(text, date_text, source, log)
        else:
            df = pd.DataFrame(columns=FINAL_COLUMNS)

        if len(df) > len(best):
            best = df

        if len(df) >= MIN_TPEX_ROWS:
            log.append(f"TPEx batch selected source={source}, rows={len(df)}")
            return df

    log.append(f"TPEx batch best rows={len(best)}")
    return best


def daily_file_date(path: Path) -> str:
    match = re.search(r"20\d{6}", path.name)
    return match.group(0) if match else ""


DAILY_PRICE_COMPARE_COLS = ["open", "high", "low", "close", "volume"]


def list_existing_daily_files(before_date: str | None = None) -> list[Path]:
    candidates: list[Path] = []

    if DATA_DIR.exists():
        candidates.extend(DATA_DIR.glob("*.csv"))

    candidates = [p for p in candidates if re.search(r"20\d{6}", p.name)]
    if before_date:
        candidates = [p for p in candidates if daily_file_date(p) < before_date]

    by_date: dict[str, list[Path]] = {}
    for path in candidates:
        date_text = daily_file_date(path)
        if not date_text:
            continue
        by_date.setdefault(date_text, []).append(path)

    selected: list[Path] = []
    for paths in by_date.values():
        # Prefer the canonical daily_price_YYYYMMDD.csv when both naming styles exist.
        selected.append(
            sorted(
                paths,
                key=lambda p: (p.name.startswith("daily_price_"), p.name),
            )[-1]
        )
    return sorted(selected, key=daily_file_date)


def read_daily_file_for_quality(path: Path) -> pd.DataFrame:
    try:
        payload = path.read_bytes()
        date_text = daily_file_date(path)
        if not date_text:
            return pd.DataFrame()
        _price_projection(payload, date_text)
        df = pd.read_csv(io.BytesIO(payload), dtype=str).fillna("")
    except Exception:
        return pd.DataFrame()
    required = {"stock_id", "market", *DAILY_PRICE_COMPARE_COLS}
    if not required.issubset(set(df.columns)):
        return pd.DataFrame()
    result = df[["stock_id", "market", *DAILY_PRICE_COMPARE_COLS]].copy()
    result["stock_id"] = result["stock_id"].astype(str).str.strip()
    result["market"] = result["market"].astype(str).str.strip()
    for col in DAILY_PRICE_COMPARE_COLS:
        result[col] = pd.to_numeric(result[col], errors="coerce")
    return result[result["stock_id"].ne("") & result["market"].ne("")]


def stale_duplicate_markets_between(
    current: pd.DataFrame,
    previous: pd.DataFrame,
    same_threshold: float = 0.98,
    min_common_rows: int = 300,
) -> tuple[list[str], dict[str, float]]:
    stale_markets: list[str] = []
    ratios: dict[str, float] = {}
    if current.empty or previous.empty:
        return stale_markets, ratios

    for market, current_part in current.groupby(current["market"].astype(str), sort=True):
        if not market:
            continue
        previous_part = previous[previous["market"].astype(str).eq(market)]
        merged = previous_part[["stock_id"] + DAILY_PRICE_COMPARE_COLS].merge(
            current_part[["stock_id"] + DAILY_PRICE_COMPARE_COLS],
            on="stock_id",
            suffixes=("_prev", "_cur"),
        )
        if len(merged) < min_common_rows:
            continue
        same = pd.Series(True, index=merged.index)
        for col in DAILY_PRICE_COMPARE_COLS:
            same &= (
                merged[f"{col}_prev"].sub(merged[f"{col}_cur"]).abs().fillna(math.inf)
                <= 1e-9
            )
        ratio = float(same.mean()) if len(same) else 0.0
        ratios[market] = ratio
        if ratio >= same_threshold:
            stale_markets.append(market)
    return stale_markets, ratios


def is_daily_file_quality_usable(
    path: Path,
    previous_paths: list[Path],
    log: list[str] | None = None,
) -> bool:
    current = read_daily_file_for_quality(path)
    if current.empty:
        if log is not None:
            log.append(f"Daily file quality check rejected unreadable file: {path}")
        return False

    for previous_path in reversed(previous_paths[-5:]):
        previous = read_daily_file_for_quality(previous_path)
        stale_markets, ratios = stale_duplicate_markets_between(current, previous)
        if stale_markets:
            if log is not None:
                ratio_text = ", ".join(f"{k}={v:.1%}" for k, v in sorted(ratios.items()))
                log.append(
                    "Daily file quality check rejected "
                    f"{path.name}: stale markets {','.join(stale_markets)} "
                    f"duplicate {previous_path.name} ({ratio_text})"
                )
            return False
    return True


def get_latest_existing_daily_file(
    before_date: str | None = None,
    *,
    require_quality: bool = True,
    log: list[str] | None = None,
) -> Path | None:
    candidates = list_existing_daily_files(before_date=before_date)
    if not candidates:
        return None

    for index in range(len(candidates) - 1, -1, -1):
        candidate = candidates[index]
        if require_quality and not is_daily_file_quality_usable(candidate, candidates[:index], log):
            continue
        return candidate
    return None


def detect_stale_markets_against_previous(
    df: pd.DataFrame,
    target_date: str,
    log: list[str],
    same_threshold: float = 0.98,
    min_common_rows: int = 300,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Remove market segments that exactly duplicate the previous trading day.

    Exchange fallback endpoints can return the latest available TPEx data while
    the target-date TWSE data is already available. Keeping those rows under the
    target date pollutes per-stock history with fake candles, so the fetch layer
    rejects stale market segments before writing the daily file.
    """
    report: dict[str, Any] = {
        "previous_file": "",
        "stale_markets": [],
        "stale_market_rows": 0,
        "market_same_ratios": {},
        "data_quality_note": "",
    }
    if df.empty:
        return df, report

    previous_file = get_latest_existing_daily_file(before_date=target_date, log=log)
    if not previous_file:
        return df, report

    report["previous_file"] = previous_file.as_posix()
    try:
        previous = pd.read_csv(previous_file, dtype=str).fillna("")
    except Exception as exc:
        log.append(f"Stale market check skipped: cannot read previous file {previous_file}: {exc}")
        return df, report

    required = {"stock_id", "market", "open", "high", "low", "close", "volume"}
    if not required.issubset(set(previous.columns)) or not required.issubset(set(df.columns)):
        log.append("Stale market check skipped: missing required columns")
        return df, report

    compare_cols = ["open", "high", "low", "close", "volume"]
    keep_mask = pd.Series(True, index=df.index)
    stale_markets: list[str] = []
    stale_rows = 0
    for market, current_part in df.groupby(df["market"].astype(str), sort=True):
        if not market:
            continue
        previous_part = previous[previous["market"].astype(str).eq(market)]
        merged = previous_part[["stock_id"] + compare_cols].merge(
            current_part[["stock_id"] + compare_cols],
            on="stock_id",
            suffixes=("_prev", "_cur"),
        )
        if len(merged) < min_common_rows:
            continue
        same = pd.Series(True, index=merged.index)
        for col in compare_cols:
            prev = pd.to_numeric(merged[f"{col}_prev"], errors="coerce")
            cur = pd.to_numeric(merged[f"{col}_cur"], errors="coerce")
            same &= (prev - cur).abs().fillna(math.inf) <= 1e-9
        ratio = float(same.mean()) if len(same) else 0.0
        report["market_same_ratios"][market] = ratio
        if ratio >= same_threshold:
            stale_markets.append(market)
            stale_rows += int(len(current_part))
            keep_mask.loc[current_part.index] = False
            log.append(
                f"Reject stale {market} target-date rows: {ratio:.1%} match previous file {previous_file.name}"
            )

    if stale_markets:
        report["stale_markets"] = stale_markets
        report["stale_market_rows"] = stale_rows
        report["data_quality_note"] = (
            "partial_market_stale_rejected: "
            + ",".join(stale_markets)
            + f" matched previous trading day file {previous_file.name}"
        )
        df = df[keep_mask].copy().reset_index(drop=True)

    return df, report


def load_existing_universe() -> pd.DataFrame:
    frames = []

    latest_file = get_latest_existing_daily_file()
    if latest_file and latest_file.exists():
        try:
            df = pd.read_csv(latest_file, dtype=str)
            if "stock_id" in df.columns:
                frames.append(df[["stock_id", "stock_name", "market"]].copy())
        except Exception:
            pass

    if LATEST_PRICE_CSV.exists():
        try:
            df = pd.read_csv(LATEST_PRICE_CSV, dtype=str)
            if "stock_id" in df.columns:
                cols = [c for c in ["stock_id", "stock_name", "market"] if c in df.columns]
                frames.append(df[cols].copy())
        except Exception:
            pass

    if ALL_CANDIDATES_CSV.exists():
        try:
            df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str)
            if "stock_id" in df.columns:
                if "stock_name" not in df.columns:
                    df["stock_name"] = ""
                if "market" not in df.columns:
                    df["market"] = ""
                frames.append(df[["stock_id", "stock_name", "market"]].copy())
        except Exception:
            pass

    if CURRENT_HOLDINGS_JSON.exists():
        try:
            items = json.loads(CURRENT_HOLDINGS_JSON.read_text(encoding="utf-8"))
            if isinstance(items, list):
                rows = []
                for item in items:
                    if isinstance(item, dict):
                        rows.append(
                            {
                                "stock_id": item.get("stock_id", ""),
                                "stock_name": item.get("stock_name", ""),
                                "market": "",
                            }
                        )
                if rows:
                    frames.append(pd.DataFrame(rows))
        except Exception:
            pass

    if not frames:
        return pd.DataFrame(columns=["stock_id", "stock_name", "market"])

    universe = pd.concat(frames, ignore_index=True)

    for col in ["stock_id", "stock_name", "market"]:
        if col not in universe.columns:
            universe[col] = ""

    universe["stock_id"] = universe["stock_id"].map(normalize_stock_id)
    universe = universe[universe["stock_id"].map(is_valid_stock_id)].copy()
    universe = universe.drop_duplicates("stock_id", keep="first").reset_index(drop=True)

    return universe


def combine_market_data(twse: pd.DataFrame, tpex: pd.DataFrame) -> pd.DataFrame:
    frames = []

    if not twse.empty:
        frames.append(twse)

    if not tpex.empty:
        frames.append(tpex)

    if not frames:
        return pd.DataFrame(columns=FINAL_COLUMNS)

    df = pd.concat(frames, ignore_index=True)

    for col in FINAL_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    df = df[FINAL_COLUMNS].copy()
    df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)
    df = df.drop_duplicates(["date", "stock_id"], keep="first")
    df = df.sort_values(["market", "stock_id"]).reset_index(drop=True)

    return df


def fetch_price_for_date(
    date_text: str,
    log: list[str],
    *,
    deadline: float | None = None,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    log.append(f"===== Fetch price for date {date_text} =====")

    universe = load_existing_universe()
    log.append(f"Loaded universe rows={len(universe)}")

    twse = fetch_twse_batch(date_text, log)

    if (
        len(twse) < MIN_TWSE_ROWS
        and remaining_seconds(deadline) > 5
        and not REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES
    ):
        log.append(f"TWSE batch insufficient rows={len(twse)}; start individual fallback")
        fallback_twse = fetch_twse_individual_fallback(date_text, universe, log, deadline=deadline)

        if len(fallback_twse) > len(twse):
            twse = fallback_twse
            log.append(f"TWSE replaced by individual fallback rows={len(twse)}")
        else:
            log.append(f"TWSE kept batch rows={len(twse)}; fallback rows={len(fallback_twse)}")

    if remaining_seconds(deadline) <= 5:
        log.append("TPEx batch skipped: fetch time budget nearly exhausted")
        tpex = pd.DataFrame(columns=FINAL_COLUMNS)
    else:
        tpex = fetch_tpex_batch(date_text, log)

    combined = apply_canonical_stock_names(combine_market_data(twse, tpex), log)

    status = {
        "date": date_text,
        "twse_rows": len(twse),
        "tpex_rows": len(tpex),
        "total_rows": len(combined),
        "twse_ok": len(twse) >= MIN_TWSE_ROWS,
        "tpex_ok": len(tpex) >= MIN_TPEX_ROWS,
        "full_market_ok": (
            len(twse) >= MIN_TWSE_ROWS
            and len(tpex) >= MIN_TPEX_ROWS
            and len(combined) >= MIN_FULL_ROWS
        ),
        "universe_rows": len(universe),
    }

    log.append(
        f"date={date_text} twse_rows={status['twse_rows']} "
        f"tpex_rows={status['tpex_rows']} total_rows={status['total_rows']} "
        f"full_market_ok={status['full_market_ok']}"
    )

    return combined, status


def detect_target_date() -> str:
    # 自動化晚上跑，目標就是台北今天
    override = str(os.environ.get("OFFICIAL_PRICE_TARGET_DATE") or "").strip()
    if override:
        if not re.fullmatch(r"20\d{6}", override):
            raise ValueError(
                "OFFICIAL_PRICE_TARGET_DATE must be YYYYMMDD, "
                f"got {override!r}"
            )
        datetime.strptime(override, "%Y%m%d")
        return override
    return ymd(now_taipei())


def save_price_data(df: pd.DataFrame, saved_date: str) -> dict[str, str]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_LATEST.mkdir(parents=True, exist_ok=True)

    paths = {
        "dated_csv": str(DATA_DIR / f"{saved_date}.csv"),
        "dated_alt_csv": str(DATA_DIR / f"daily_price_{saved_date}.csv"),
        "latest_csv": str(LATEST_PRICE_CSV),
    }

    df.to_csv(paths["dated_csv"], index=False, encoding="utf-8-sig")
    df.to_csv(paths["dated_alt_csv"], index=False, encoding="utf-8-sig")

    return paths


def publish_previous_valid_latest(target_date: str, log: list[str]) -> dict[str, str]:
    previous_file = get_latest_existing_daily_file(before_date=target_date, log=log)
    if not previous_file or not previous_file.exists():
        return {}
    log.append(f"Selected previous valid daily price file for atomic latest publication: {previous_file}")
    return {
        "previous_valid_csv": str(previous_file),
        "latest_csv": str(LATEST_PRICE_CSV),
    }


def _report_markdown_bytes(result: dict[str, Any], log: list[str]) -> bytes:
    lines = [
        "# Official Daily Price Fetch Report",
        "",
        f"- generated_at: `{now_taipei().strftime('%Y-%m-%d %H:%M:%S Asia/Taipei')}`",
        f"- target_date: `{result.get('target_date', '')}`",
        f"- saved_price_date: `{result.get('saved_price_date', '')}`",
        f"- is_target_date: `{result.get('is_target_date', False)}`",
        f"- result: `{result.get('result', '')}`",
        f"- reason: {result.get('reason', '')}",
        f"- twse_rows: `{result.get('twse_rows', 0)}`",
        f"- tpex_rows: `{result.get('tpex_rows', 0)}`",
        f"- total_rows: `{result.get('total_rows', 0)}`",
        f"- full_market_ok: `{result.get('full_market_ok', False)}`",
    ]
    if result.get("data_quality_note"):
        lines.append(f"- data_quality_note: {result.get('data_quality_note')}")
    if result.get("stale_markets"):
        lines.append(f"- stale_markets: `{', '.join(result.get('stale_markets', []))}`")
        lines.append(f"- stale_market_rows: `{result.get('stale_market_rows', 0)}`")
    lines.append("")

    if result.get("paths"):
        lines.extend(["## Output Paths", ""])
        for key, value in result["paths"].items():
            lines.append(f"- {key}: `{value}`")
        lines.append("")

    lines.extend(["## Fetch Attempts", ""])
    for item in result.get("attempts", []):
        lines.append(
            f"- {item.get('date')}: "
            f"TWSE={item.get('twse_rows')} / "
            f"TPEx={item.get('tpex_rows')} / "
            f"Total={item.get('total_rows')} / "
            f"full_market_ok={item.get('full_market_ok')}"
        )

    lines.extend(["", "## Fetch Logs", ""])
    for entry in log[-400:]:
        lines.append(f"- {entry}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _write_durable_file(path: Path, payload: bytes) -> None:
    with path.open("wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())


def _is_reparse_path(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except FileNotFoundError:
        return False
    return path.is_symlink() or bool(
        getattr(metadata, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    )


def _safe_repo_path(root: Path, relative_path: Path) -> Path:
    root = Path(os.path.abspath(root))
    if not root.is_dir() or _is_reparse_path(root):
        raise ValueError("official price evidence repository root is unsafe")
    if relative_path.is_absolute() or any(
        part in {"", ".", ".."} for part in relative_path.parts
    ):
        raise ValueError(
            f"official price evidence path is not canonical: {relative_path}"
        )
    target = root / relative_path
    current = root
    for part in relative_path.parts:
        current = current / part
        if _is_reparse_path(current):
            raise ValueError(
                f"official price evidence path contains reparse point: {relative_path}"
            )
    return target


def _remove_official_price_transaction(transaction_root: Path) -> None:
    if transaction_root.exists():
        if not transaction_root.is_dir() or transaction_root.is_symlink():
            raise ValueError(
                "official price evidence transaction root is not a safe directory"
            )
        shutil.rmtree(transaction_root)


def _derive_official_price_transaction_id(journal: dict[str, Any]) -> str:
    identity = {
        key: journal.get(key)
        for key in (
            "schema_version",
            "transaction_kind",
            "required_paths",
            "entries",
        )
    }
    payload = (
        json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:32]


def _write_official_price_transaction_journal(
    transaction_root: Path,
    journal: dict[str, Any],
) -> None:
    normalized = dict(journal)
    normalized.pop("journal_sha256", None)
    identity_payload = (
        json.dumps(normalized, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        + "\n"
    ).encode("utf-8")
    normalized["journal_sha256"] = hashlib.sha256(identity_payload).hexdigest()
    payload = (
        json.dumps(normalized, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    prepare = transaction_root / "journal.prepare"
    prepare.unlink(missing_ok=True)
    _write_durable_file(prepare, payload)
    os.replace(prepare, transaction_root / "journal.json")


def _load_official_price_transaction(
    root: Path,
) -> tuple[Path, dict[str, Any], list[tuple[dict[str, Any], Path, bytes | None]]]:
    root = Path(os.path.abspath(root))
    transaction_root = _safe_repo_path(root, OFFICIAL_PRICE_TRANSACTION_DIR)
    if not transaction_root.is_dir() or transaction_root.is_symlink():
        raise ValueError(
            "official price evidence transaction root is not a safe directory"
        )
    journal_path = transaction_root / "journal.json"
    if not journal_path.is_file() or journal_path.is_symlink():
        raise ValueError("official price evidence transaction journal is unsafe")
    try:
        journal = json.loads(journal_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(
            f"official price evidence transaction journal is unreadable: {exc}"
        ) from exc
    if not isinstance(journal, dict):
        raise ValueError("official price evidence transaction journal is invalid")
    schema = journal.get("schema_version")
    state = safe_str(journal.get("state"))
    if (
        schema != "official_price_evidence_transaction_v3"
        or state not in {"pending", "committed"}
    ):
        raise ValueError("official price evidence transaction journal is invalid")
    allowed_paths = {
        LATEST_PRICE_CSV.as_posix(),
        LATEST_FETCH_JSON.as_posix(),
        LATEST_FETCH_MD.as_posix(),
    }
    expected_journal_sha = safe_str(journal.get("journal_sha256"))
    identity = dict(journal)
    identity.pop("journal_sha256", None)
    identity_payload = (
        json.dumps(
            identity,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    if (
        not re.fullmatch(r"[0-9a-f]{64}", expected_journal_sha)
        or hashlib.sha256(identity_payload).hexdigest() != expected_journal_sha
    ):
        raise ValueError(
            "official price evidence transaction journal identity mismatch"
        )
    transaction_id = safe_str(journal.get("transaction_id"))
    if (
        not re.fullmatch(r"[0-9a-f]{32}", transaction_id)
        or transaction_id != _derive_official_price_transaction_id(journal)
    ):
        raise ValueError(
            "official price evidence transaction identity mismatch"
        )
    transaction_kind = safe_str(journal.get("transaction_kind"))
    required_path_values = journal.get("required_paths")
    if (
        transaction_kind
        not in {
            "atomic_official_price_evidence",
            "deferred_official_latest_triplet",
        }
        or not isinstance(required_path_values, list)
        or not required_path_values
        or any(not isinstance(path, str) for path in required_path_values)
        or len(required_path_values) != len(set(required_path_values))
    ):
        raise ValueError(
            "official price evidence transaction required path identity is invalid"
        )
    required_paths = set(required_path_values)
    if not required_paths.issubset(allowed_paths):
        raise ValueError(
            "official price evidence transaction required path identity is invalid"
        )
    if (
        transaction_kind == "deferred_official_latest_triplet"
        and required_paths != allowed_paths
    ):
        raise ValueError(
            "deferred official price evidence transaction journal requires the exact triplet"
        )
    entries = journal.get("entries")
    if not isinstance(entries, list) or not entries:
        raise ValueError("official price evidence transaction journal is invalid")
    observed_paths: set[str] = set()
    validated: list[tuple[dict[str, Any], Path, bytes | None]] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            raise ValueError("official price evidence transaction entry is invalid")
        relative_text = safe_str(entry.get("path"))
        if relative_text not in allowed_paths or relative_text in observed_paths:
            raise ValueError("official price evidence transaction path set is invalid")
        observed_paths.add(relative_text)
        target = _safe_repo_path(root, Path(relative_text))
        if target.exists() and (not target.is_file() or target.is_symlink()):
            raise ValueError(
                f"official price evidence recovery target is unsafe: {relative_text}"
            )
        if not isinstance(entry.get("previous_existed"), bool):
            raise ValueError(
                "official price evidence previous-target identity is invalid"
            )
        try:
            previous_bytes = int(entry.get("previous_bytes"))
            next_bytes = int(entry.get("next_bytes"))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                "official price evidence transaction byte identity is invalid"
            ) from exc
        if previous_bytes < 0 or next_bytes < 0:
            raise ValueError(
                "official price evidence transaction byte identity is invalid"
            )
        previous_payload: bytes | None = None
        if entry.get("previous_existed") is True:
            backup_name = safe_str(entry.get("previous_file"))
            if backup_name != f"previous-{index}.bin":
                raise ValueError(
                    "official price evidence recovery backup identity is invalid"
                )
            if not re.fullmatch(
                r"[0-9a-f]{64}", safe_str(entry.get("previous_sha256"))
            ):
                raise ValueError(
                    "official price evidence recovery backup SHA identity is invalid"
                )
            if state == "pending":
                backup_path = transaction_root / backup_name
                if not backup_path.is_file() or backup_path.is_symlink():
                    raise ValueError(
                        "official price evidence recovery backup is missing or unsafe"
                    )
                previous_payload = backup_path.read_bytes()
                if (
                    len(previous_payload) != previous_bytes
                    or hashlib.sha256(previous_payload).hexdigest()
                    != entry.get("previous_sha256")
                ):
                    raise ValueError(
                        "official price evidence recovery backup identity mismatch"
                    )
        elif (
            safe_str(entry.get("previous_file"))
            or previous_bytes != 0
            or safe_str(entry.get("previous_sha256"))
            != hashlib.sha256(b"").hexdigest()
        ):
            raise ValueError(
                "official price evidence absent-target identity is invalid"
            )
        if safe_str(entry.get("next_file")) != f"next-{index}.bin":
            raise ValueError(
                "official price evidence prepared payload identity is invalid"
            )
        if not re.fullmatch(r"[0-9a-f]{64}", safe_str(entry.get("next_sha256"))):
            raise ValueError(
                "official price evidence prepared payload SHA identity is invalid"
            )
        validated.append((entry, target, previous_payload))
    if observed_paths != required_paths:
        raise ValueError(
            "official price evidence transaction journal path set is incomplete"
        )
    journal["state"] = state
    return transaction_root, journal, validated


def recover_official_price_evidence_transaction(root: Path) -> bool:
    root = Path(os.path.abspath(root))
    transaction_root = _safe_repo_path(
        root, OFFICIAL_PRICE_TRANSACTION_DIR
    )
    if not transaction_root.exists():
        return False
    if not transaction_root.is_dir() or transaction_root.is_symlink():
        raise ValueError(
            "official price evidence transaction root is not a safe directory"
        )
    journal_path = transaction_root / "journal.json"
    if not journal_path.exists():
        raise ValueError(
            "official price evidence transaction journal is missing; "
            "preserving transaction evidence and refusing recovery"
        )
    transaction_root, journal, validated = _load_official_price_transaction(root)
    if journal["state"] == "committed":
        for entry, target, _ in validated:
            if not target.is_file() or target.is_symlink():
                raise ValueError(
                    "committed official price evidence target is missing or unsafe: "
                    f"{entry['path']}"
                )
            payload = target.read_bytes()
            if (
                len(payload) != int(entry["next_bytes"])
                or hashlib.sha256(payload).hexdigest() != entry["next_sha256"]
            ):
                raise ValueError(
                    "committed official price evidence target identity mismatch: "
                    f"{entry['path']}"
                )
        _remove_official_price_transaction(transaction_root)
        return True

    for index, (entry, target, previous_payload) in enumerate(validated):
        if previous_payload is not None:
            target.parent.mkdir(parents=True, exist_ok=True)
            restore = transaction_root / f"restore-{index}.bin"
            _write_durable_file(restore, previous_payload)
            os.replace(restore, target)
        else:
            target.unlink(missing_ok=True)
    _remove_official_price_transaction(transaction_root)
    return True


def _begin_official_price_evidence_transaction(
    root: Path,
    payloads: dict[Path, bytes],
    *,
    fail_after_replace: int = 0,
    crash_after_replace: int = 0,
    require_exact_triplet: bool = False,
) -> str:
    root = Path(os.path.abspath(root))
    recover_official_price_evidence_transaction(root)
    allowed_paths = {
        LATEST_PRICE_CSV,
        LATEST_FETCH_JSON,
        LATEST_FETCH_MD,
    }
    if not payloads or not set(payloads).issubset(allowed_paths):
        raise ValueError("official price evidence transaction path set is invalid")
    if require_exact_triplet and set(payloads) != allowed_paths:
        raise ValueError(
            "deferred official price evidence transaction requires the exact triplet"
        )
    transaction_root = _safe_repo_path(
        root, OFFICIAL_PRICE_TRANSACTION_DIR
    )
    if transaction_root.exists() or transaction_root.is_symlink():
        raise ValueError("official price evidence transaction root collision")
    transaction_root.mkdir(parents=True, exist_ok=False)
    try:
        entries: list[dict[str, Any]] = []
        targets: list[tuple[Path, Path]] = []
        for index, (relative_path, payload) in enumerate(
            sorted(payloads.items(), key=lambda item: item[0].as_posix())
        ):
            target = _safe_repo_path(root, relative_path)
            if target.exists() and (not target.is_file() or target.is_symlink()):
                raise ValueError(
                    "official price evidence path is not a safe regular file: "
                    f"{relative_path}"
                )
            target.parent.mkdir(parents=True, exist_ok=True)
            previous_existed = target.exists()
            previous_payload = target.read_bytes() if previous_existed else b""
            previous_name = f"previous-{index}.bin" if previous_existed else ""
            if previous_existed:
                _write_durable_file(
                    transaction_root / previous_name,
                    previous_payload,
                )
            next_name = f"next-{index}.bin"
            next_path = transaction_root / next_name
            _write_durable_file(next_path, payload)
            entries.append(
                {
                    "path": relative_path.as_posix(),
                    "previous_existed": previous_existed,
                    "previous_file": previous_name,
                    "previous_bytes": len(previous_payload),
                    "previous_sha256": hashlib.sha256(previous_payload).hexdigest(),
                    "next_file": next_name,
                    "next_bytes": len(payload),
                    "next_sha256": hashlib.sha256(payload).hexdigest(),
                }
            )
            targets.append((target, next_path))
        journal = {
            "schema_version": "official_price_evidence_transaction_v3",
            "transaction_kind": (
                "deferred_official_latest_triplet"
                if require_exact_triplet
                else "atomic_official_price_evidence"
            ),
            "required_paths": sorted(
                relative_path.as_posix() for relative_path in payloads
            ),
            "state": "pending",
            "entries": entries,
        }
        transaction_id = _derive_official_price_transaction_id(journal)
        journal["transaction_id"] = transaction_id
        _write_official_price_transaction_journal(transaction_root, journal)

        replaced = 0
        for index, (target, next_path) in enumerate(targets):
            entry = entries[index]
            next_payload = next_path.read_bytes()
            if (
                len(next_payload) != entry["next_bytes"]
                or hashlib.sha256(next_payload).hexdigest()
                != entry["next_sha256"]
            ):
                raise ValueError(
                    "official price evidence prepared payload identity mismatch"
                )
            os.replace(next_path, target)
            replaced += 1
            if crash_after_replace and replaced >= crash_after_replace:
                os._exit(91)
            if fail_after_replace and replaced >= fail_after_replace:
                raise OSError("injected official price evidence transaction failure")
    except Exception as exc:
        try:
            if (transaction_root / "journal.json").exists():
                recover_official_price_evidence_transaction(root)
            else:
                _remove_official_price_transaction(transaction_root)
        except Exception as rollback_exc:
            raise RuntimeError(
                "official price evidence transaction failed and rollback failed: "
                f"original={exc}; rollback={rollback_exc}"
            ) from rollback_exc
        raise
    return transaction_id


def commit_official_price_evidence_transaction(
    root: Path,
    *,
    crash_after_commit_marker: bool = False,
) -> str:
    root = Path(os.path.abspath(root))
    transaction_root, journal, validated = _load_official_price_transaction(root)
    if journal["state"] == "committed":
        recover_official_price_evidence_transaction(root)
        return safe_str(journal.get("transaction_id"))
    try:
        for entry, target, _ in validated:
            if not target.is_file() or target.is_symlink():
                raise ValueError(
                    "official price evidence commit target is missing or unsafe: "
                    f"{entry['path']}"
                )
            payload = target.read_bytes()
            if (
                len(payload) != int(entry["next_bytes"])
                or hashlib.sha256(payload).hexdigest() != entry["next_sha256"]
            ):
                raise ValueError(
                    "official price evidence commit target identity mismatch: "
                    f"{entry['path']}"
                )
    except Exception as exc:
        try:
            recover_official_price_evidence_transaction(root)
        except Exception as rollback_exc:
            raise RuntimeError(
                "official price evidence commit validation failed and rollback failed: "
                f"original={exc}; rollback={rollback_exc}"
            ) from rollback_exc
        raise
    committed = dict(journal)
    committed["schema_version"] = "official_price_evidence_transaction_v3"
    committed["state"] = "committed"
    _write_official_price_transaction_journal(transaction_root, committed)
    if crash_after_commit_marker:
        os._exit(92)
    _remove_official_price_transaction(transaction_root)
    return safe_str(committed.get("transaction_id"))


def _atomic_publish_payloads(
    root: Path,
    payloads: dict[Path, bytes],
    *,
    fail_after_replace: int = 0,
    crash_after_replace: int = 0,
) -> None:
    _begin_official_price_evidence_transaction(
        root,
        payloads,
        fail_after_replace=fail_after_replace,
        crash_after_replace=crash_after_replace,
    )
    commit_official_price_evidence_transaction(root)


def _price_projection(price_payload: bytes, saved_date: str) -> dict[str, int]:
    try:
        rows = list(csv.DictReader(io.StringIO(price_payload.decode("utf-8-sig"))))
    except Exception as exc:
        raise ValueError(f"official daily price payload is not valid UTF-8 CSV: {exc}") from exc
    if not rows:
        raise ValueError("official daily price payload has no rows")
    required = {
        "date",
        "stock_id",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
    }
    missing = sorted(required - set(rows[0]))
    if missing:
        raise ValueError(
            "official daily price payload is missing quality columns: "
            + ", ".join(missing)
        )
    counts = {"TWSE": 0, "TPEx": 0}
    wrong_date_rows = 0
    invalid_rows = 0
    seen_stock_ids: set[str] = set()
    duplicate_stock_ids: set[str] = set()
    for row in rows:
        if normalize_date_text(row.get("date")) != saved_date:
            wrong_date_rows += 1
            continue
        stock_id = normalize_stock_id(row.get("stock_id"))
        if not is_valid_stock_id(stock_id):
            invalid_rows += 1
        elif stock_id in seen_stock_ids:
            duplicate_stock_ids.add(stock_id)
        else:
            seen_stock_ids.add(stock_id)
        market = safe_str(row.get("market")).lower()
        if market in {"twse", "listed"}:
            counts["TWSE"] += 1
        elif market in {"tpex", "otc", "emerging"}:
            counts["TPEx"] += 1
        else:
            invalid_rows += 1
        numeric: dict[str, float] = {}
        for field in DAILY_PRICE_COMPARE_COLS:
            try:
                number = float(safe_str(row.get(field)))
            except (TypeError, ValueError):
                number = math.nan
            if not math.isfinite(number):
                invalid_rows += 1
            numeric[field] = number
        if all(math.isfinite(numeric[field]) for field in DAILY_PRICE_COMPARE_COLS):
            if (
                min(
                    numeric["open"],
                    numeric["high"],
                    numeric["low"],
                    numeric["close"],
                )
                <= 0
                or numeric["volume"] < 0
                or numeric["high"]
                < max(numeric["open"], numeric["low"], numeric["close"])
                or numeric["low"]
                > min(numeric["open"], numeric["high"], numeric["close"])
            ):
                invalid_rows += 1
    if (
        wrong_date_rows
        or invalid_rows
        or duplicate_stock_ids
        or counts["TWSE"] <= 0
        or counts["TPEx"] <= 0
        or counts["TWSE"] + counts["TPEx"] != len(rows)
    ):
        raise ValueError(
            "official daily price payload does not contain clean unique target-date "
            "TWSE/TPEx OHLCV rows: "
            f"TWSE={counts['TWSE']} TPEx={counts['TPEx']} "
            f"wrong_date_rows={wrong_date_rows} invalid_rows={invalid_rows} "
            f"duplicate_stock_ids={sorted(duplicate_stock_ids)}"
        )
    return {
        "twse_rows": counts["TWSE"],
        "tpex_rows": counts["TPEx"],
        "total_rows": len(rows),
        "wrong_date_rows": wrong_date_rows,
    }


def publish_official_price_evidence_transaction(
    root: Path,
    *,
    price_payload: bytes,
    result: dict[str, Any],
    log: list[str] | None = None,
    fail_after_replace: int = 0,
    crash_after_replace: int = 0,
    deferred: bool = False,
) -> dict[str, Any]:
    root = root.resolve()
    target_date = normalize_date_text(result.get("target_date"))
    saved_date = normalize_date_text(result.get("saved_price_date"))
    if not target_date or not saved_date:
        raise ValueError("official price evidence requires exact target_date and saved_price_date")
    if result.get("is_target_date") is True and saved_date != target_date:
        raise ValueError("target-date official price evidence cannot publish a different saved date")
    projection = _price_projection(price_payload, saved_date)
    for field in ("twse_rows", "tpex_rows", "total_rows"):
        if int(result.get(field) or -1) != projection[field]:
            raise ValueError(
                f"official price evidence {field} mismatch: "
                f"reported={result.get(field)!r} observed={projection[field]}"
            )
    if result.get("full_market_ok") is True and (
        projection["twse_rows"] <= 0 or projection["tpex_rows"] <= 0
    ):
        raise ValueError("full-market official price evidence requires both TWSE and TPEx rows")

    canonical_price_path = f"data/daily_price/daily_price_{saved_date}.csv"
    enriched = dict(result)
    enriched.update(
        {
            "price_path": canonical_price_path,
            "price_bytes": len(price_payload),
            "price_sha256": hashlib.sha256(price_payload).hexdigest(),
            "latest_price_path": LATEST_PRICE_CSV.as_posix(),
            "latest_price_bytes": len(price_payload),
            "latest_price_sha256": hashlib.sha256(price_payload).hexdigest(),
        }
    )
    markdown_payload = _report_markdown_bytes(enriched, list(log or []))
    enriched.update(
        {
            "fetch_markdown_path": LATEST_FETCH_MD.as_posix(),
            "fetch_markdown_bytes": len(markdown_payload),
            "fetch_markdown_sha256": hashlib.sha256(markdown_payload).hexdigest(),
        }
    )
    json_payload = (
        json.dumps(enriched, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    payloads = {
        LATEST_PRICE_CSV: price_payload,
        LATEST_FETCH_JSON: json_payload,
        LATEST_FETCH_MD: markdown_payload,
    }
    if deferred:
        _begin_official_price_evidence_transaction(
            root,
            payloads,
            fail_after_replace=fail_after_replace,
            crash_after_replace=crash_after_replace,
            require_exact_triplet=True,
        )
    else:
        _atomic_publish_payloads(
            root,
            payloads,
            fail_after_replace=fail_after_replace,
            crash_after_replace=crash_after_replace,
        )
    return enriched


def write_report(result: dict[str, Any], log: list[str]) -> None:
    OUTPUT_LATEST.mkdir(parents=True, exist_ok=True)
    OUTPUT_DEBUG.mkdir(parents=True, exist_ok=True)
    paths = result.get("paths") if isinstance(result.get("paths"), dict) else {}
    source_text = str(paths.get("dated_csv") or paths.get("previous_valid_csv") or "")
    source_path = Path(source_text) if source_text else None
    if source_path is not None and source_path.is_file():
        published = publish_official_price_evidence_transaction(
            Path.cwd(),
            price_payload=source_path.read_bytes(),
            result=result,
            log=log,
        )
        result.clear()
        result.update(published)
    else:
        _atomic_publish_payloads(
            Path.cwd(),
            {
                LATEST_FETCH_JSON: (
                    json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
                ).encode("utf-8"),
                LATEST_FETCH_MD: _report_markdown_bytes(result, log),
            },
        )

    DEBUG_MD.write_bytes(_report_markdown_bytes(result, log))

def main() -> int:
    target_date = detect_target_date()
    deadline = time.monotonic() + SCRIPT_MAX_SECONDS
    log: list[str] = []
    attempts: list[dict[str, Any]] = []

    log.append(
        f"Start official daily price fetch target_date={target_date} "
        f"max_seconds={SCRIPT_MAX_SECONDS}"
    )

    df, status = fetch_price_for_date(target_date, log, deadline=deadline)
    attempts.append(status)

    # 這版的精神：今天跑，就盡最大努力寫今天資料。
    # 如果批次 + fallback 有抓到足夠資料，就寫 target_date。
    # 不再偷偷沿用昨天。
    stale_report: dict[str, Any] = {}
    if not df.empty:
        df, stale_report = detect_stale_markets_against_previous(df, target_date, log)
        status["total_rows"] = int(len(df))
        status["twse_rows"] = int((df["market"].astype(str) == "TWSE").sum()) if "market" in df.columns else 0
        status["tpex_rows"] = int((df["market"].astype(str) == "TPEx").sum()) if "market" in df.columns else 0
        status["twse_ok"] = status["twse_rows"] >= MIN_TWSE_ROWS
        status["tpex_ok"] = status["tpex_rows"] >= MIN_TPEX_ROWS
        status["full_market_ok"] = (
            status["twse_ok"]
            and status["tpex_ok"]
            and status["total_rows"] >= MIN_FULL_ROWS
            and not stale_report.get("stale_markets")
        )
        if stale_report.get("stale_markets"):
            attempts[-1] = status | {
                "stale_markets": stale_report.get("stale_markets", []),
                "stale_market_rows": stale_report.get("stale_market_rows", 0),
                "data_quality_note": stale_report.get("data_quality_note", ""),
            }

    if not df.empty and bool(status.get("full_market_ok", False)):
        paths = save_price_data(df, target_date)

        result_name = "success_target_full_market"
        reason = "成功取得目標日 TWSE + TPEx 官方日線資料。"

        result = {
            "generated_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
            "target_date": target_date,
            "saved_price_date": target_date,
            "is_target_date": True,
            "result": result_name,
            "reason": reason,
            "twse_rows": status.get("twse_rows", 0),
            "tpex_rows": status.get("tpex_rows", 0),
            "total_rows": status.get("total_rows", 0),
            "full_market_ok": True,
            "stale_markets": stale_report.get("stale_markets", []),
            "stale_market_rows": stale_report.get("stale_market_rows", 0),
            "data_quality_note": stale_report.get("data_quality_note", ""),
            "market_same_ratios": stale_report.get("market_same_ratios", {}),
            "attempts": attempts,
            "paths": paths,
        }

        write_report(result, log)

        print(f"Saved official daily price data date={target_date}")
        print(
            f"Rows={len(df)} "
            f"TWSE={status.get('twse_rows', 0)} "
            f"TPEx={status.get('tpex_rows', 0)} "
            "full_market_ok=True"
        )
        print(f"Report saved: {LATEST_FETCH_MD}")
        return 0

    # 真的完全沒有抓到，才不寫今日資料
    previous_paths = publish_previous_valid_latest(target_date, log)
    previous_date = daily_file_date(Path(previous_paths.get("previous_valid_csv", ""))) if previous_paths else ""
    previous_projection = (
        _price_projection(
            Path(previous_paths["previous_valid_csv"]).read_bytes(),
            previous_date,
        )
        if previous_date
        else {"twse_rows": 0, "tpex_rows": 0, "total_rows": 0}
    )
    result = {
        "generated_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
        "target_date": target_date,
        "saved_price_date": previous_date,
        "is_target_date": False,
        "result": "failed_no_target_data",
        "reason": "目標日官方來源與 fallback 都沒有取得任何可用日線資料；latest 保留上一個有效交易日。",
        "twse_rows": previous_projection["twse_rows"],
        "tpex_rows": previous_projection["tpex_rows"],
        "total_rows": previous_projection["total_rows"],
        "full_market_ok": False,
        "stale_markets": stale_report.get("stale_markets", []),
        "stale_market_rows": stale_report.get("stale_market_rows", 0),
        "data_quality_note": stale_report.get("data_quality_note", ""),
        "market_same_ratios": stale_report.get("market_same_ratios", {}),
        "attempts": attempts,
        "paths": previous_paths,
    }

    write_report(result, log)

    print("No target-date official price data found.")
    print(f"Report saved: {LATEST_FETCH_MD}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
