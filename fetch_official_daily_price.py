from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
import io
import json
import math
import re
import shutil
import time
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
DEBUG_MD = OUTPUT_DEBUG / "official_price_fetch_debug_latest.md"

ALL_CANDIDATES_CSV = OUTPUT_LATEST / "all_candidates_latest.csv"
CURRENT_HOLDINGS_JSON = CONFIG_DIR / "current_holdings.json"

REQUEST_TIMEOUT = 25

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


def now_taipei() -> datetime:
    return datetime.now(TAIPEI)


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


def request_text(url: str, log: list[str], referer: str = "https://www.twse.com.tw/") -> str:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": referer,
    }

    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        text = response.text or ""
        log.append(f"GET {url} -> status={response.status_code}, chars={len(text)}")

        if response.status_code != 200:
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
        log.append(f"Trying TWSE batch source={source} date={date_text}")
        text = request_text(url, log, referer="https://www.twse.com.tw/")

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
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
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


def fetch_twse_individual_fallback(date_text: str, universe: pd.DataFrame, log: list[str]) -> pd.DataFrame:
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

    jobs = []
    rows = []

    log.append(f"TWSE individual fallback start: stocks={len(part)} date={date_text}")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        for _, row in part.iterrows():
            sid = safe_str(row.get("stock_id", "")).zfill(4)
            name = safe_str(row.get("stock_name", ""))

            if not is_valid_stock_id(sid):
                continue

            jobs.append(executor.submit(fetch_twse_individual_one, date_text, sid, name))

        for future in as_completed(jobs):
            result = future.result()
            if result:
                rows.append(result)

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
        log.append(f"Trying TPEx batch source={source} date={date_text}")
        text = request_text(url, log, referer="https://www.tpex.org.tw/")

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


def get_latest_existing_daily_file(before_date: str | None = None) -> Path | None:
    candidates = []

    if DATA_DIR.exists():
        candidates.extend(DATA_DIR.glob("*.csv"))

    candidates = [
        p for p in candidates
        if re.search(r"20\d{6}", p.name)
    ]
    if before_date:
        candidates = [p for p in candidates if daily_file_date(p) < before_date]

    if not candidates:
        return None

    return sorted(candidates, key=daily_file_date)[-1]


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

    previous_file = get_latest_existing_daily_file(before_date=target_date)
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


def fetch_price_for_date(date_text: str, log: list[str]) -> tuple[pd.DataFrame, dict[str, Any]]:
    log.append(f"===== Fetch price for date {date_text} =====")

    universe = load_existing_universe()
    log.append(f"Loaded universe rows={len(universe)}")

    twse = fetch_twse_batch(date_text, log)

    if len(twse) < MIN_TWSE_ROWS:
        log.append(f"TWSE batch insufficient rows={len(twse)}; start individual fallback")
        fallback_twse = fetch_twse_individual_fallback(date_text, universe, log)

        if len(fallback_twse) > len(twse):
            twse = fallback_twse
            log.append(f"TWSE replaced by individual fallback rows={len(twse)}")
        else:
            log.append(f"TWSE kept batch rows={len(twse)}; fallback rows={len(fallback_twse)}")

    tpex = fetch_tpex_batch(date_text, log)

    combined = combine_market_data(twse, tpex)

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
    df.to_csv(paths["latest_csv"], index=False, encoding="utf-8-sig")

    return paths


def publish_previous_valid_latest(target_date: str, log: list[str]) -> dict[str, str]:
    previous_file = get_latest_existing_daily_file(before_date=target_date)
    if not previous_file or not previous_file.exists():
        return {}
    OUTPUT_LATEST.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(previous_file, LATEST_PRICE_CSV)
    log.append(f"Published previous valid daily price file as latest: {previous_file}")
    return {
        "previous_valid_csv": str(previous_file),
        "latest_csv": str(LATEST_PRICE_CSV),
    }


def write_report(result: dict[str, Any], log: list[str]) -> None:
    OUTPUT_LATEST.mkdir(parents=True, exist_ok=True)
    OUTPUT_DEBUG.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# 官方每日價格資料抓取狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei().strftime('%Y-%m-%d %H:%M:%S Asia/Taipei')}`")
    lines.append(f"- target_date：`{result.get('target_date', '')}`")
    lines.append(f"- saved_price_date：`{result.get('saved_price_date', '')}`")
    lines.append(f"- is_target_date：`{result.get('is_target_date', False)}`")
    lines.append(f"- result：`{result.get('result', '')}`")
    lines.append(f"- reason：{result.get('reason', '')}")
    lines.append(f"- twse_rows：`{result.get('twse_rows', 0)}`")
    lines.append(f"- tpex_rows：`{result.get('tpex_rows', 0)}`")
    lines.append(f"- total_rows：`{result.get('total_rows', 0)}`")
    lines.append(f"- full_market_ok：`{result.get('full_market_ok', False)}`")
    if result.get("data_quality_note"):
        lines.append(f"- data_quality_note：{result.get('data_quality_note')}")
    if result.get("stale_markets"):
        lines.append(f"- stale_markets：`{', '.join(result.get('stale_markets', []))}`")
        lines.append(f"- stale_market_rows：`{result.get('stale_market_rows', 0)}`")
    lines.append("")

    if result.get("paths"):
        lines.append("## 輸出檔案")
        lines.append("")
        for key, value in result["paths"].items():
            lines.append(f"- {key}: `{value}`")
        lines.append("")

    lines.append("## 嘗試紀錄")
    lines.append("")
    for item in result.get("attempts", []):
        lines.append(
            f"- {item.get('date')}: "
            f"TWSE={item.get('twse_rows')} / "
            f"TPEx={item.get('tpex_rows')} / "
            f"Total={item.get('total_rows')} / "
            f"full_market_ok={item.get('full_market_ok')}"
        )

    lines.append("")
    lines.append("## Fetch logs")
    lines.append("")
    for entry in log[-400:]:
        lines.append(f"- {entry}")

    LATEST_FETCH_MD.write_text("\n".join(lines), encoding="utf-8")

    LATEST_FETCH_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    target_date = detect_target_date()
    log: list[str] = []
    attempts: list[dict[str, Any]] = []

    log.append(f"Start official daily price fetch target_date={target_date}")

    df, status = fetch_price_for_date(target_date, log)
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

    if not df.empty and len(df) >= 1:
        paths = save_price_data(df, target_date)

        full_market_ok = bool(status.get("full_market_ok", False))

        if full_market_ok:
            result_name = "success_target_full_market"
            reason = "成功取得目標日 TWSE + TPEx 官方日線資料。"
        else:
            result_name = "success_target_partial_fallback"
            reason = (
                "已取得目標日部分官方日線資料並寫入今日檔案；"
                "部分市場資料可能由 fallback 補齊不足，請查看 twse_rows / tpex_rows。"
            )

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
            "full_market_ok": full_market_ok,
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
            f"full_market_ok={full_market_ok}"
        )
        print(f"Report saved: {LATEST_FETCH_MD}")
        return 0

    # 真的完全沒有抓到，才不寫今日資料
    previous_paths = publish_previous_valid_latest(target_date, log)
    previous_date = daily_file_date(Path(previous_paths.get("previous_valid_csv", ""))) if previous_paths else ""
    result = {
        "generated_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
        "target_date": target_date,
        "saved_price_date": previous_date,
        "is_target_date": False,
        "result": "failed_no_target_data",
        "reason": "目標日官方來源與 fallback 都沒有取得任何可用日線資料；latest 保留上一個有效交易日。",
        "twse_rows": status.get("twse_rows", 0),
        "tpex_rows": status.get("tpex_rows", 0),
        "total_rows": status.get("total_rows", 0),
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
