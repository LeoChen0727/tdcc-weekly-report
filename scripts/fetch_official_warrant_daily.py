from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse
import io
import re
import time

import pandas as pd
import requests


OUTPUT_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/warrant_daily")

RAW_LATEST = OUTPUT_DIR / "warrant_daily_raw_latest.csv"
FETCH_STATUS_MD = OUTPUT_DIR / "warrant_daily_fetch_latest.md"

PRICE_DIR = Path("data/daily_price")


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def today_taipei_yyyymmdd() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    text = re.sub(r"[^0-9]", "", text)

    if len(text) >= 4:
        return text[:4]

    return text.zfill(4) if text else ""


def to_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")

    if text in ["", "-", "nan", "None"]:
        return pd.NA

    return pd.to_numeric(text, errors="coerce")


def get_latest_price_date() -> str:
    latest_date = ""

    for path in sorted(PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(path, dtype={"date": str}, usecols=lambda c: c in ["date"])
        except Exception:
            continue

        if "date" not in df.columns or df.empty:
            continue

        dates = (
            df["date"]
            .astype(str)
            .str.replace(r"[^0-9]", "", regex=True)
            .dropna()
        )

        if not dates.empty:
            candidate = dates.max()

            if len(candidate) == 8 and candidate > latest_date:
                latest_date = candidate

    return latest_date or today_taipei_yyyymmdd()


def yyyymmdd_to_roc_slash(date_str: str) -> str:
    year = int(date_str[:4]) - 1911
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    return f"{year}/{month:02d}/{day:02d}"


def read_csv_from_response(text: str) -> pd.DataFrame:
    if not text or len(text.strip()) < 10:
        return pd.DataFrame()

    cleaned = text.replace("\ufeff", "").strip()

    if "<html" in cleaned.lower() and "," not in cleaned[:300]:
        return pd.DataFrame()

    lines = cleaned.splitlines()

    header_index = 0

    for idx, line in enumerate(lines[:30]):
        if "," in line and any(key in line for key in ["證券代號", "權證代號", "權證名稱", "標的", "成交"]):
            header_index = idx
            break

    csv_text = "\n".join(lines[header_index:])

    try:
        return pd.read_csv(io.StringIO(csv_text), dtype=str)
    except Exception:
        try:
            return pd.read_csv(io.StringIO(csv_text), dtype=str, encoding="utf-8-sig")
        except Exception:
            return pd.DataFrame()


def fetch_url(url: str) -> tuple[pd.DataFrame, str]:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/csv,text/plain,application/json,*/*",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.encoding = response.apparent_encoding or "utf-8"
        df = read_csv_from_response(response.text)

        if not df.empty:
            return df, f"ok: {url}"

        return pd.DataFrame(), f"empty_or_unparsed: {url}, status={response.status_code}"
    except Exception as exc:
        return pd.DataFrame(), f"failed: {url}, error={exc}"


def standardize_warrant_raw(df: pd.DataFrame, market: str, source_url: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]

    def pick(candidates: list[str]) -> str | None:
        for col in candidates:
            if col in df.columns:
                return col

        for col in df.columns:
            for candidate in candidates:
                if candidate in col:
                    return col

        return None

    warrant_id_col = pick(["權證代號", "證券代號", "代號"])
    warrant_name_col = pick(["權證名稱", "證券名稱", "名稱"])

    underlying_id_col = pick([
        "標的證券代號",
        "標的代號",
        "標的證券",
        "標的股票代號",
        "標的",
        "股票代號",
    ])

    underlying_name_col = pick([
        "標的證券名稱",
        "標的名稱",
        "標的股票名稱",
        "股票名稱",
    ])

    call_put_col = pick([
        "認購售",
        "認購/售",
        "認購售權證種類",
        "權證種類",
        "種類",
        "購售",
    ])

    volume_col = pick(["成交股數", "成交量", "成交單位", "成交數量"])
    turnover_col = pick(["成交金額", "成交值", "成交金額(元)"])

    close_col = pick(["收盤價", "收盤"])
    issuer_col = pick(["發行人", "發行機構", "委託證券商", "券商"])

    issued_col = pick(["發行數量", "發行單位總數", "發行張數", "發行量"])
    cancelled_col = pick(["累計註銷", "註銷量", "註銷單位", "註銷數量"])
    latest_count_col = pick(["最新權證數量", "最新流通量", "流通在外單位", "流通量"])
    float_col = pick(["流通量", "最新流通量", "流通在外單位", "流通在外數量"])

    if not warrant_id_col:
        return pd.DataFrame()

    out = pd.DataFrame()
    out["market"] = market
    out["source_url"] = source_url
    out["warrant_id"] = df[warrant_id_col].astype(str).str.strip()
    out["warrant_name"] = df[warrant_name_col].astype(str).str.strip() if warrant_name_col else ""

    if underlying_id_col:
        out["stock_id"] = df[underlying_id_col].map(normalize_code)
    else:
        out["stock_id"] = out["warrant_name"].astype(str).str.extract(r"(\d{4})")[0].fillna("").map(normalize_code)

    out["stock_name"] = df[underlying_name_col].astype(str).str.strip() if underlying_name_col else ""

    if call_put_col:
        out["call_put_raw"] = df[call_put_col].astype(str).str.strip()
    else:
        out["call_put_raw"] = out["warrant_name"].astype(str)

    out["call_put"] = out["call_put_raw"].apply(classify_call_put)

    out["volume"] = df[volume_col].map(to_number) if volume_col else pd.NA
    out["turnover"] = df[turnover_col].map(to_number) if turnover_col else pd.NA
    out["close"] = df[close_col].map(to_number) if close_col else pd.NA
    out["issuer"] = df[issuer_col].astype(str).str.strip() if issuer_col else ""

    out["issued_quantity"] = df[issued_col].map(to_number) if issued_col else pd.NA
    out["cancelled_quantity"] = df[cancelled_col].map(to_number) if cancelled_col else pd.NA
    out["latest_warrant_count"] = df[latest_count_col].map(to_number) if latest_count_col else pd.NA
    out["float_quantity"] = df[float_col].map(to_number) if float_col else pd.NA

    out = out[out["warrant_id"].astype(str).str.len() > 0].copy()
    out = out[out["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    return out


def classify_call_put(value: str) -> str:
    text = str(value).lower()

    if any(key in text for key in ["認購", "購", "call", "c"]):
        if "認售" not in text and "售" not in text:
            return "call"

    if any(key in text for key in ["認售", "售", "put", "p"]):
        return "put"

    return "unknown"


def fetch_twse_warrants(date_str: str) -> tuple[pd.DataFrame, list[str]]:
    urls = [
        f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=csv",
        f"https://www.twse.com.tw/exchangeReport/warrantStock?date={date_str}&response=csv",
    ]

    logs = []

    for url in urls:
        df, log = fetch_url(url)
        logs.append(log)

        if not df.empty:
            return standardize_warrant_raw(df, "TWSE", url), logs

    return pd.DataFrame(), logs


def fetch_tpex_warrants(date_str: str) -> tuple[pd.DataFrame, list[str]]:
    roc = yyyymmdd_to_roc_slash(date_str)

    urls = [
        f"https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date={roc}&response=csv",
        f"https://www.tpex.org.tw/web/stock/aftertrading/warrant_quotes/warrant_quotes_result.php?l=zh-tw&d={roc}",
        f"https://www.tpex.org.tw/ch/extend/warrant/dailyQ/wntQuts.php?l=zh-tw&d={roc}&s=0,asc,0",
    ]

    logs = []

    for url in urls:
        df, log = fetch_url(url)
        logs.append(log)

        if not df.empty:
            return standardize_warrant_raw(df, "TPEX", url), logs

    return pd.DataFrame(), logs


def write_status(date_str: str, rows: int, logs: list[str], warning: str = "") -> None:
    lines = []
    lines.append("# 官方權證每日資料抓取狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 資料日期：`{date_str}`")
    lines.append(f"- 輸出檔：`{RAW_LATEST}`")
    lines.append(f"- 筆數：`{rows}`")
    lines.append("")

    if warning:
        lines.append(f"- warning：`{warning}`")
        lines.append("")

    lines.append("## Fetch logs")
    lines.append("")

    for log in logs:
        lines.append(f"- {log}")

    FETCH_STATUS_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default="", help="YYYYMMDD. Default: latest date in data/daily_price or Taiwan today.")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    date_str = args.date.strip() or get_latest_price_date()

    logs = []
    frames = []

    twse_df, twse_logs = fetch_twse_warrants(date_str)
    logs.extend(twse_logs)

    if not twse_df.empty:
        frames.append(twse_df)

    time.sleep(1)

    tpex_df, tpex_logs = fetch_tpex_warrants(date_str)
    logs.extend(tpex_logs)

    if not tpex_df.empty:
        frames.append(tpex_df)

    if frames:
        out = pd.concat(frames, ignore_index=True)
        out.insert(0, "date", date_str)

        out.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
        out.to_csv(HISTORY_DIR / f"warrant_daily_{date_str}.csv", index=False, encoding="utf-8-sig")

        write_status(date_str, len(out), logs)

        print(f"Saved: {RAW_LATEST}, rows={len(out)}")
        return 0

    empty_cols = [
        "date",
        "market",
        "source_url",
        "warrant_id",
        "warrant_name",
        "stock_id",
        "stock_name",
        "call_put_raw",
        "call_put",
        "volume",
        "turnover",
        "close",
        "issuer",
        "issued_quantity",
        "cancelled_quantity",
        "latest_warrant_count",
        "float_quantity",
    ]

    pd.DataFrame(columns=empty_cols).to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
    write_status(date_str, 0, logs, warning="官方權證資料抓取失敗或格式無法解析，已輸出空檔避免 workflow 失敗。")

    print("No warrant data fetched. Empty raw file created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
