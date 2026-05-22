from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import csv
import io
import json
import math
import re
import sys
from typing import Any

import pandas as pd
import requests


TAIPEI = ZoneInfo("Asia/Taipei")

DATA_DIR = Path("data/daily_price")
OUTPUT_LATEST = Path("output/latest")
OUTPUT_DEBUG = Path("output/debug")

LATEST_PRICE_CSV = OUTPUT_LATEST / "official_daily_price_latest.csv"
LATEST_FETCH_MD = OUTPUT_LATEST / "official_price_fetch_latest.md"
LATEST_FETCH_JSON = OUTPUT_LATEST / "official_price_fetch_latest.json"
DEBUG_MD = OUTPUT_DEBUG / "official_price_fetch_debug_latest.md"

REQUEST_TIMEOUT = 25

MIN_TWSE_ROWS = 700
MIN_TPEX_ROWS = 500
MIN_TOTAL_ROWS = 1400

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
    text = text.strip()

    # 有些官方欄位會混入空白或不可見字元
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
    if not stock_id:
        return False
    if not re.fullmatch(r"\d{4,6}", stock_id):
        return False
    return True


def request_text(url: str, log: list[str]) -> str:
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": "https://www.twse.com.tw/",
    }

    try:
        resp = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        log.append(f"GET {url} -> status={resp.status_code}, chars={len(resp.text)}")
        if resp.status_code != 200:
            return ""
        return resp.text
    except Exception as exc:
        log.append(f"GET {url} failed: {type(exc).__name__}: {exc}")
        return ""


def parse_json_text(text: str) -> Any:
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

    # 開高低有時缺值，但收盤有值；先用收盤補，避免整列被丟掉
    if math.isnan(o):
        o = c
    if math.isnan(h):
        h = max(o, c)
    if math.isnan(l):
        l = min(o, c)

    vol = clean_int(volume)
    val = clean_int(trading_value)

    if vol <= 0 and val <= 0:
        # ETF、特殊商品或停牌會有 0，但股票日線監測不需要
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
    df = df.drop_duplicates(["date", "stock_id"], keep="first")

    return df


def parse_twse_mi_index_json(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json_text(text)

    if not isinstance(obj, dict):
        log.append(f"{source}: json parse failed")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    possible_pairs = []

    for data_key, fields_key in [
        ("data9", "fields9"),
        ("data", "fields"),
        ("tables", "fields"),
    ]:
        if data_key in obj:
            possible_pairs.append((obj.get(data_key), obj.get(fields_key)))

    if "tables" in obj and isinstance(obj["tables"], list):
        for table in obj["tables"]:
            if isinstance(table, dict):
                possible_pairs.append((table.get("data"), table.get("fields")))

    rows = []

    for data, fields in possible_pairs:
        if not isinstance(data, list):
            continue

        field_map = {}
        if isinstance(fields, list):
            for i, field in enumerate(fields):
                field_map[safe_str(field)] = i

        for item in data:
            if not isinstance(item, list):
                continue

            parsed = parse_twse_list_row(item, date_text, source)
            if parsed:
                rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TWSE rows={len(df)}")
    return df


def parse_twse_list_row(item: list[Any], date_text: str, source: str) -> dict[str, Any] | None:
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

    if len(item) < 9:
        return None

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


def parse_twse_csv(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    if not text:
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    # TWSE CSV 有時前面會有說明列，所以逐行找像股票資料的列
    reader = csv.reader(io.StringIO(text.lstrip("\ufeff")))

    for item in reader:
        if len(item) < 9:
            continue

        # 股票代號通常在第 0 欄
        if not re.fullmatch(r"\s*\d{4,6}\s*", safe_str(item[0])):
            continue

        parsed = parse_twse_list_row(item, date_text, source)
        if parsed:
            rows.append(parsed)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TWSE CSV rows={len(df)}")
    return df


def parse_twse_openapi(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json_text(text)

    if not isinstance(obj, list):
        log.append(f"{source}: openapi json parse failed or not list")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    for item in obj:
        if not isinstance(item, dict):
            continue

        stock_id = (
            item.get("Code")
            or item.get("證券代號")
            or item.get("STOCK_ID")
            or item.get("stock_id")
        )

        stock_name = (
            item.get("Name")
            or item.get("證券名稱")
            or item.get("STOCK_NAME")
            or item.get("stock_name")
        )

        parsed = normalize_row(
            date_text=date_text,
            stock_id=stock_id,
            stock_name=stock_name,
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


def fetch_twse(date_text: str, log: list[str]) -> pd.DataFrame:
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

    frames = []

    for source, url, kind in urls:
        log.append(f"Trying TWSE source={source} date={date_text}")
        text = request_text(url, log)

        if not text:
            continue

        if kind == "json_mi":
            df = parse_twse_mi_index_json(text, date_text, source, log)
        elif kind == "csv_mi":
            df = parse_twse_csv(text, date_text, source, log)
        elif kind == "openapi":
            df = parse_twse_openapi(text, date_text, source, log)
        else:
            df = pd.DataFrame(columns=FINAL_COLUMNS)

        if len(df) >= MIN_TWSE_ROWS:
            log.append(f"TWSE selected source={source}, rows={len(df)}")
            return df

        if not df.empty:
            frames.append(df)

    if frames:
        combined = pd.concat(frames, ignore_index=True)
        combined = combined.drop_duplicates(["date", "stock_id"], keep="first")
        log.append(f"TWSE combined partial rows={len(combined)}")
        return combined

    log.append("TWSE no rows")
    return pd.DataFrame(columns=FINAL_COLUMNS)


def parse_tpex_json_tables(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    obj = parse_json_text(text)

    if obj is None:
        log.append(f"{source}: json parse failed")
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key in ["aaData", "data", "tables", "items", "list"]:
                if key in node:
                    walk(node[key])

            # dict row 形式
            maybe = parse_tpex_dict_row(node, date_text, source)
            if maybe:
                rows.append(maybe)

            for value in node.values():
                if isinstance(value, (dict, list)):
                    walk(value)

        elif isinstance(node, list):
            if node and all(not isinstance(x, (dict, list)) for x in node):
                maybe = parse_tpex_list_row(node, date_text, source)
                if maybe:
                    rows.append(maybe)
            else:
                for value in node:
                    walk(value)

    walk(obj)

    df = dataframe_from_rows(rows)
    log.append(f"{source}: parsed TPEx json rows={len(df)}")
    return df


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

    close_price = (
        item.get("Close")
        or item.get("ClosePrice")
        or item.get("收盤")
        or item.get("收盤價")
    )

    open_price = (
        item.get("Open")
        or item.get("OpenPrice")
        or item.get("開盤")
        or item.get("開盤價")
    )

    high_price = (
        item.get("High")
        or item.get("HighPrice")
        or item.get("最高")
        or item.get("最高價")
    )

    low_price = (
        item.get("Low")
        or item.get("LowPrice")
        or item.get("最低")
        or item.get("最低價")
    )

    volume = (
        item.get("TradingShares")
        or item.get("成交股數")
        or item.get("成交股數合計")
        or item.get("Volume")
        or item.get("成交量")
    )

    trading_value = (
        item.get("TransactionAmount")
        or item.get("成交金額")
        or item.get("TradingValue")
        or item.get("成交值")
    )

    return normalize_row(
        date_text=date_text,
        stock_id=stock_id,
        stock_name=stock_name,
        market="TPEx",
        open_price=open_price,
        high_price=high_price,
        low_price=low_price,
        close_price=close_price,
        volume=volume,
        trading_value=trading_value,
        source=source,
    )


def parse_tpex_list_row(item: list[Any], date_text: str, source: str) -> dict[str, Any] | None:
    if len(item) < 8:
        return None

    # TPEx 舊版常見：
    # 0 代號
    # 1 名稱
    # 2 收盤
    # 3 漲跌
    # 4 開盤
    # 5 最高
    # 6 最低
    # 7 成交股數
    # 8 成交金額
    #
    # 有些新版欄位會多幾欄，仍以這組位置優先解析。

    if not re.fullmatch(r"\s*\d{4,6}\s*", safe_str(item[0])):
        return None

    close_price = item[2] if len(item) > 2 else ""
    open_price = item[4] if len(item) > 4 else close_price
    high_price = item[5] if len(item) > 5 else close_price
    low_price = item[6] if len(item) > 6 else close_price
    volume = item[7] if len(item) > 7 else ""
    trading_value = item[8] if len(item) > 8 else ""

    return normalize_row(
        date_text=date_text,
        stock_id=item[0],
        stock_name=item[1] if len(item) > 1 else "",
        market="TPEx",
        open_price=open_price,
        high_price=high_price,
        low_price=low_price,
        close_price=close_price,
        volume=volume,
        trading_value=trading_value,
        source=source,
    )


def parse_tpex_csv(text: str, date_text: str, source: str, log: list[str]) -> pd.DataFrame:
    if not text:
        return pd.DataFrame(columns=FINAL_COLUMNS)

    rows = []

    for encoding_try in [text]:
        reader = csv.reader(io.StringIO(encoding_try.lstrip("\ufeff")))

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


def fetch_tpex(date_text: str, log: list[str]) -> pd.DataFrame:
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
    ]

    frames = []

    for source, url, kind in urls:
        log.append(f"Trying TPEx source={source} date={date_text}")
        text = request_text(url, log)

        if not text:
            continue

        if kind == "json":
            df = parse_tpex_json_tables(text, date_text, source, log)
        elif kind == "csv":
            df = parse_tpex_csv(text, date_text, source, log)
        else:
            df = pd.DataFrame(columns=FINAL_COLUMNS)

        if len(df) >= MIN_TPEX_ROWS:
            log.append(f"TPEx selected source={source}, rows={len(df)}")
            return df

        if not df.empty:
            frames.append(df)

    if frames:
        combined = pd.concat(frames, ignore_index=True)
        combined = combined.drop_duplicates(["date", "stock_id"], keep="first")
        log.append(f"TPEx combined partial rows={len(combined)}")
        return combined

    log.append("TPEx no rows")
    return pd.DataFrame(columns=FINAL_COLUMNS)


def build_price_for_date(date_text: str, log: list[str]) -> tuple[pd.DataFrame, dict[str, Any]]:
    twse = fetch_twse(date_text, log)
    tpex = fetch_tpex(date_text, log)

    twse_rows = len(twse)
    tpex_rows = len(tpex)

    frames = []
    if not twse.empty:
        frames.append(twse)
    if not tpex.empty:
        frames.append(tpex)

    if frames:
        combined = pd.concat(frames, ignore_index=True)
        combined = combined.drop_duplicates(["date", "stock_id"], keep="first")
        combined = combined.sort_values(["market", "stock_id"]).reset_index(drop=True)
    else:
        combined = pd.DataFrame(columns=FINAL_COLUMNS)

    status = {
        "date": date_text,
        "twse_rows": twse_rows,
        "tpex_rows": tpex_rows,
        "total_rows": len(combined),
        "twse_ok": twse_rows >= MIN_TWSE_ROWS,
        "tpex_ok": tpex_rows >= MIN_TPEX_ROWS,
        "full_market_ok": (
            twse_rows >= MIN_TWSE_ROWS
            and tpex_rows >= MIN_TPEX_ROWS
            and len(combined) >= MIN_TOTAL_ROWS
        ),
    }

    log.append(
        f"date={date_text} twse_rows={twse_rows} "
        f"tpex_rows={tpex_rows} total_rows={len(combined)} "
        f"full_market_ok={status['full_market_ok']}"
    )

    return combined, status


def detect_target_date() -> str:
    now = now_taipei()

    # 台股夜間跑報告時，目標日期就是今天。
    # 週末手動跑時，會先試今天，再往前回查。
    return ymd(now)


def candidate_dates(target_date: str, lookback_days: int = 8) -> list[str]:
    start = datetime.strptime(target_date, "%Y%m%d").replace(tzinfo=TAIPEI)
    return [ymd(start - timedelta(days=i)) for i in range(lookback_days)]


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


def write_fetch_report(result: dict[str, Any], log: list[str]) -> None:
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
    lines.append("")

    if result.get("paths"):
        lines.append("## 輸出檔案")
        lines.append("")
        for key, value in result["paths"].items():
            lines.append(f"- {key}: `{value}`")
        lines.append("")

    lines.append("## 最近嘗試日期")
    lines.append("")

    for item in result.get("attempts", []):
        lines.append(
            f"- {item.get('date')}: "
            f"twse={item.get('twse_rows')} / "
            f"tpex={item.get('tpex_rows')} / "
            f"total={item.get('total_rows')} / "
            f"full_market_ok={item.get('full_market_ok')}"
        )

    lines.append("")
    lines.append("## Fetch logs")
    lines.append("")
    for entry in log[-300:]:
        lines.append(f"- {entry}")

    LATEST_FETCH_MD.write_text("\n".join(lines), encoding="utf-8")

    LATEST_FETCH_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    target_date = detect_target_date()
    dates = candidate_dates(target_date, lookback_days=8)

    log: list[str] = []
    attempts: list[dict[str, Any]] = []

    selected_df = pd.DataFrame(columns=FINAL_COLUMNS)
    selected_status: dict[str, Any] | None = None

    log.append(f"Start official daily price fetch target_date={target_date}")

    for date_text in dates:
        log.append(f"===== Try date {date_text} =====")
        df, status = build_price_for_date(date_text, log)
        attempts.append(status)

        if status["full_market_ok"]:
            selected_df = df
            selected_status = status
            break

    if selected_status is None or selected_df.empty:
        result = {
            "generated_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
            "target_date": target_date,
            "saved_price_date": "",
            "is_target_date": False,
            "result": "failed",
            "reason": "最近回查日期都沒有取得完整 TWSE + TPEx 官方日線資料；未更新 data/daily_price。",
            "twse_rows": 0,
            "tpex_rows": 0,
            "total_rows": 0,
            "attempts": attempts,
            "paths": {},
        }

        write_fetch_report(result, log)

        print("No valid full-market official daily price data found.")
        print(f"Report saved: {LATEST_FETCH_MD}")
        print("Do not update data/daily_price.")
        print("Continue workflow, but downstream freshness should mark report_ready=False if target date is missing.")
        return 0

    saved_date = selected_status["date"]
    paths = save_price_data(selected_df, saved_date)

    is_target = saved_date == target_date

    result = {
        "generated_at": now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei"),
        "target_date": target_date,
        "saved_price_date": saved_date,
        "is_target_date": is_target,
        "result": "success_target" if is_target else "success_fallback_previous_date",
        "reason": (
            "成功取得目標日完整官方日線資料。"
            if is_target
            else "未取得目標日完整資料，改用最近一個完整官方日線資料日。"
        ),
        "twse_rows": selected_status["twse_rows"],
        "tpex_rows": selected_status["tpex_rows"],
        "total_rows": selected_status["total_rows"],
        "attempts": attempts,
        "paths": paths,
    }

    write_fetch_report(result, log)

    print(f"Saved official daily price data date={saved_date}")
    print(f"Rows={len(selected_df)} TWSE={selected_status['twse_rows']} TPEx={selected_status['tpex_rows']}")
    print(f"is_target_date={is_target}")
    print(f"Report saved: {LATEST_FETCH_MD}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
