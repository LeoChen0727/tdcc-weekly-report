from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from io import StringIO
import time

import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "daily_price"
LATEST_DIR = BASE_DIR / "output" / "latest"
DEBUG_DIR = BASE_DIR / "output" / "debug"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LATEST_DIR.mkdir(parents=True, exist_ok=True)
DEBUG_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json,text/csv,text/plain,*/*",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
    "Connection": "close",
}


def request_with_retries(url, params=None, timeout=60, retries=3):
    last_exc = None

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                url,
                params=params,
                headers=HEADERS,
                timeout=timeout,
            )
            response.raise_for_status()
            return response
        except Exception as exc:
            last_exc = exc
            print(f"Request failed attempt {attempt}/{retries}: {url} params={params} error={exc}")
            time.sleep(2 * attempt)

    print(f"Request finally failed: {url} params={params} error={last_exc}")
    return None


def normalize_date(value):
    if pd.isna(value):
        return None

    text = str(value).strip()
    text = text.replace("年", "/").replace("月", "/").replace("日", "")
    text = text.replace("-", "/").replace(".", "/")

    if "/" in text:
        parts = [p for p in text.split("/") if p != ""]
        if len(parts) >= 3:
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])

                if year < 1911:
                    year += 1911

                return f"{year:04d}{month:02d}{day:02d}"
            except Exception:
                return None

    digits = "".join(ch for ch in text if ch.isdigit())

    if len(digits) == 8:
        year = int(digits[:4])
        if year >= 1911:
            return digits

    if len(digits) == 7:
        try:
            year = int(digits[:3]) + 1911
            month = int(digits[3:5])
            day = int(digits[5:7])
            return f"{year:04d}{month:02d}{day:02d}"
        except Exception:
            return None

    return None


def clean_number(value):
    if pd.isna(value):
        return None

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("--", "")
    text = text.replace("X", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")

    if text == "":
        return None

    return pd.to_numeric(text, errors="coerce")


def clean_price_df(df):
    if df.empty:
        return df

    df = df.copy()

    df["ticker"] = df["ticker"].astype(str).str.strip()
    df["name"] = df["name"].astype(str).str.strip()

    for col in ["volume", "open", "high", "low", "close"]:
        df[col] = df[col].apply(clean_number)

    df = df.dropna(subset=["ticker", "close"])
    df = df[df["ticker"].str.match(r"^\d{4}$", na=False)]
    df = df[df["close"] > 0]

    df = df[
        [
            "date",
            "ticker",
            "name",
            "market",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]
    ]

    return df.reset_index(drop=True)


def parse_twse_table(df, date_str, source_name):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            "".join([str(x) for x in col if str(x) != "nan"]).strip()
            for col in df.columns
        ]
    else:
        df.columns = [str(col).strip() for col in df.columns]

    col_map_candidates = {
        "ticker": ["證券代號", "有價證券代號"],
        "name": ["證券名稱", "有價證券名稱"],
        "volume": ["成交股數"],
        "open": ["開盤價"],
        "high": ["最高價"],
        "low": ["最低價"],
        "close": ["收盤價"],
    }

    selected = {}

    for std_col, possible_cols in col_map_candidates.items():
        for possible_col in possible_cols:
            for actual_col in df.columns:
                if possible_col == actual_col or possible_col in actual_col:
                    selected[std_col] = actual_col
                    break
            if std_col in selected:
                break

    required = ["ticker", "name", "volume", "open", "high", "low", "close"]

    if any(col not in selected for col in required):
        print(
            f"TWSE missing columns for {date_str} source={source_name}: "
            f"columns={list(df.columns)} selected={selected}"
        )
        return pd.DataFrame()

    out = df[
        [
            selected["ticker"],
            selected["name"],
            selected["volume"],
            selected["open"],
            selected["high"],
            selected["low"],
            selected["close"],
        ]
    ].copy()

    out.columns = ["ticker", "name", "volume", "open", "high", "low", "close"]
    out["market"] = "TWSE"
    out["date"] = date_str

    parsed = clean_price_df(out)

    if not parsed.empty:
        print(f"TWSE parsed rows for {date_str} source={source_name}: {len(parsed)}")

    return parsed


def parse_twse_json_response(response, date_str, source_name):
    try:
        data = response.json()
    except Exception as exc:
        print(f"TWSE json parse failed for {date_str} source={source_name}: {exc}")
        return pd.DataFrame()

    tables = data.get("tables", [])

    if not isinstance(tables, list) or not tables:
        print(f"TWSE json no tables for {date_str} source={source_name}")
        return pd.DataFrame()

    for table in tables:
        fields = table.get("fields", [])
        rows = table.get("data", [])

        if not fields or not rows:
            continue

        if "證券代號" in fields and "證券名稱" in fields and "收盤價" in fields:
            df = pd.DataFrame(rows, columns=fields)
            parsed = parse_twse_table(df, date_str, source_name)

            if not parsed.empty:
                return parsed

    print(f"TWSE json no valid price table for {date_str} source={source_name}")
    return pd.DataFrame()


def parse_twse_html_response(response, date_str, source_name):
    try:
        text = response.content.decode("utf-8-sig", errors="replace")
    except Exception:
        text = response.text

    debug_path = DEBUG_DIR / f"twse_response_{date_str}_{source_name}.html"
    debug_path.write_text(text[:10000], encoding="utf-8")

    try:
        tables = pd.read_html(StringIO(text))
    except Exception as exc:
        print(f"TWSE html read failed for {date_str} source={source_name}: {exc}")
        return pd.DataFrame()

    for idx, table in enumerate(tables):
        parsed = parse_twse_table(table, date_str, f"{source_name}_table_{idx}")

        if not parsed.empty:
            return parsed

    print(f"TWSE html no valid price table for {date_str} source={source_name}")
    return pd.DataFrame()


def fetch_twse_daily_price(date_str):
    sources = [
        {
            "name": "rwd_json",
            "url": "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX",
            "params": {
                "response": "json",
                "date": date_str,
                "type": "ALLBUT0999",
            },
            "kind": "json",
            "timeout": 90,
            "retries": 5,
        },
        {
            "name": "legacy_json",
            "url": "https://www.twse.com.tw/exchangeReport/MI_INDEX",
            "params": {
                "response": "json",
                "date": date_str,
                "type": "ALLBUT0999",
            },
            "kind": "json",
            "timeout": 90,
            "retries": 5,
        },
        {
            "name": "rwd_html",
            "url": "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX",
            "params": {
                "response": "html",
                "date": date_str,
                "type": "ALLBUT0999",
            },
            "kind": "html",
            "timeout": 90,
            "retries": 3,
        },
        {
            "name": "legacy_html",
            "url": "https://www.twse.com.tw/exchangeReport/MI_INDEX",
            "params": {
                "response": "html",
                "date": date_str,
                "type": "ALLBUT0999",
            },
            "kind": "html",
            "timeout": 90,
            "retries": 3,
        },
    ]

    for source in sources:
        print(f"Trying TWSE source {source['name']} for {date_str}")

        response = request_with_retries(
            source["url"],
            params=source["params"],
            timeout=source["timeout"],
            retries=source["retries"],
        )

        if response is None:
            continue

        if source["kind"] == "json":
            parsed = parse_twse_json_response(response, date_str, source["name"])
        else:
            parsed = parse_twse_html_response(response, date_str, source["name"])

        if not parsed.empty:
            return parsed

    print(f"TWSE no valid data for {date_str}")
    return pd.DataFrame()


def parse_tpex_table(df, date_str):
    if df.empty:
        return pd.DataFrame()

    df = df.copy()
    df.columns = [str(col).strip().replace('"', "") for col in df.columns]

    date_candidates = ["資料日期", "日期", "Date", "date"]
    date_col = None

    for col in date_candidates:
        if col in df.columns:
            date_col = col
            break

    if date_col is not None:
        df["_normalized_date"] = df[date_col].apply(normalize_date)
        df = df[df["_normalized_date"] == date_str].copy()
    else:
        df["_normalized_date"] = date_str

    if df.empty:
        return pd.DataFrame()

    col_candidates = {
        "ticker": ["代號", "證券代號", "股票代號", "Code", "SecuritiesCompanyCode"],
        "name": ["名稱", "證券名稱", "股票名稱", "Name", "CompanyName"],
        "close": ["收盤", "收盤價", "最後成交價", "Close", "ClosePrice"],
        "open": ["開盤", "開盤價", "Open", "OpenPrice"],
        "high": ["最高", "最高價", "High", "HighPrice"],
        "low": ["最低", "最低價", "Low", "LowPrice"],
        "volume": ["成交股數", "成交股數(股)", "成交仟股", "成交量", "Volume", "TradeVolume"],
    }

    selected = {}

    for std_col, possible_cols in col_candidates.items():
        for col in possible_cols:
            if col in df.columns:
                selected[std_col] = col
                break

    if len(selected) < len(col_candidates):
        print(f"TPEx missing columns for {date_str}: columns={list(df.columns)} selected={selected}")
        return pd.DataFrame()

    out = df[
        [
            selected["ticker"],
            selected["name"],
            selected["volume"],
            selected["open"],
            selected["high"],
            selected["low"],
            selected["close"],
        ]
    ].copy()

    out.columns = ["ticker", "name", "volume", "open", "high", "low", "close"]
    out["market"] = "TPEX"
    out["date"] = date_str

    return clean_price_df(out)


def parse_tpex_json_response(response, date_str, source_name):
    try:
        data = response.json()
    except Exception as exc:
        print(f"TPEx json parse failed for {date_str} source={source_name}: {exc}")
        return pd.DataFrame()

    rows = None
    fields = None

    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict):
        for key in ["data", "Data", "aaData", "tables"]:
            if key in data:
                rows = data.get(key)
                break

        fields = data.get("fields") or data.get("Fields") or data.get("columns") or data.get("Columns")

        if isinstance(rows, list) and rows and isinstance(rows[0], dict) and "data" in rows[0]:
            first_table = rows[0]
            fields = first_table.get("fields") or first_table.get("columns") or fields
            rows = first_table.get("data")

    if rows is None:
        print(f"TPEx json no rows for {date_str} source={source_name}")
        return pd.DataFrame()

    if isinstance(rows, list) and rows and isinstance(rows[0], dict):
        df = pd.DataFrame(rows)
    elif isinstance(rows, list) and fields:
        df = pd.DataFrame(rows, columns=fields)
    else:
        print(f"TPEx json unsupported rows for {date_str} source={source_name}")
        return pd.DataFrame()

    parsed = parse_tpex_table(df, date_str)

    if not parsed.empty:
        print(f"TPEx parsed json rows for {date_str} source={source_name}: {len(parsed)}")

    return parsed


def parse_tpex_csv_response(response, date_str, source_name):
    try:
        text = response.content.decode("utf-8-sig", errors="replace")
    except Exception:
        text = response.text

    debug_path = DEBUG_DIR / f"tpex_response_{date_str}_{source_name}.txt"
    debug_path.write_text(text[:5000], encoding="utf-8")

    lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        if "代號" in line and "名稱" in line:
            lines.append(line)
            continue

        clean_line = line.replace('"', "").replace(",", "")
        if len(clean_line) >= 4 and clean_line[:4].isdigit():
            lines.append(line)

    if len(lines) < 2:
        print(f"TPEx csv no usable lines for {date_str} source={source_name}")
        return pd.DataFrame()

    csv_text = "\n".join(lines)

    try:
        df = pd.read_csv(StringIO(csv_text))
    except Exception as exc:
        print(f"TPEx csv read failed for {date_str} source={source_name}: {exc}")
        return pd.DataFrame()

    parsed = parse_tpex_table(df, date_str)

    if not parsed.empty:
        print(f"TPEx parsed csv rows for {date_str} source={source_name}: {len(parsed)}")

    return parsed


def fetch_tpex_daily_price(date_str):
    roc_year = int(date_str[:4]) - 1911
    roc_date = f"{roc_year}/{date_str[4:6]}/{date_str[6:8]}"

    sources = [
        {
            "name": "open_data_current_json",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {"l": "zh-tw", "o": "data", "se": "EW"},
            "kind": "json",
            "timeout": 90,
            "retries": 5,
        },
        {
            "name": "open_data_current_csv",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php",
            "params": {"l": "zh-tw", "o": "csv", "se": "EW"},
            "kind": "csv",
            "timeout": 90,
            "retries": 5,
        },
        {
            "name": "old_daily_csv",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php",
            "params": {"l": "zh-tw", "d": roc_date, "o": "csv", "se": "EW"},
            "kind": "csv",
            "timeout": 90,
            "retries": 3,
        },
        {
            "name": "old_daily_data",
            "url": "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php",
            "params": {"l": "zh-tw", "d": roc_date, "o": "data", "se": "EW"},
            "kind": "json",
            "timeout": 90,
            "retries": 3,
        },
        {
            "name": "new_aftertrading_json",
            "url": "https://www.tpex.org.tw/www/zh-tw/afterTrading/otc",
            "params": {"date": roc_date, "type": "AL", "response": "json"},
            "kind": "json",
            "timeout": 60,
            "retries": 3,
        },
    ]

    for source in sources:
        print(f"Trying TPEx source {source['name']} for {date_str}")

        response = request_with_retries(
            source["url"],
            params=source["params"],
            timeout=source["timeout"],
            retries=source["retries"],
        )

        if response is None:
            continue

        if source["kind"] == "json":
            parsed = parse_tpex_json_response(response, date_str, source["name"])
        else:
            parsed = parse_tpex_csv_response(response, date_str, source["name"])

        if not parsed.empty:
            return parsed

    print(f"TPEx no valid data for {date_str}")
    return pd.DataFrame()


def is_valid_trading_day_data(twse_df, tpex_df, combined):
    twse_rows = len(twse_df)
    tpex_rows = len(tpex_df)
    total_rows = len(combined)

    if total_rows < 1000:
        return False, f"Total rows too low: {total_rows}"

    if twse_rows < 700:
        return False, f"TWSE rows too low: {twse_rows}"

    if tpex_rows < 500:
        return False, f"TPEx rows too low: {tpex_rows}"

    return True, "valid"


def try_fetch_one_date(date_str):
    print(f"Trying official price date: {date_str}")

    twse_df = fetch_twse_daily_price(date_str)
    tpex_df = fetch_tpex_daily_price(date_str)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if not combined.empty:
        combined = combined.drop_duplicates(subset=["date", "ticker"], keep="last")

    valid, reason = is_valid_trading_day_data(twse_df, tpex_df, combined)

    return {
        "date": date_str,
        "twse_df": twse_df,
        "tpex_df": tpex_df,
        "combined": combined,
        "valid": valid,
        "reason": reason,
        "twse_rows": len(twse_df),
        "tpex_rows": len(tpex_df),
        "total_rows": len(combined),
    }


def write_report(taiwan_now, target_date, selected, log_lines):
    log_text = "\n".join(log_lines)

    if selected is None:
        report = f"""# 官方每日價格抓取報告

執行時間：{taiwan_now.strftime("%Y-%m-%d %H:%M:%S")} Asia/Taipei
台灣目標日期：{target_date}
結果：未存檔
官方價格資料日：無
輸出檔案：無

檢查紀錄：
{log_text}

說明：最近 8 天內沒有找到完整官方收盤資料，程式不會寫入 data/daily_price/，避免污染均線與回測。
"""

        report_path = LATEST_DIR / "official_price_fetch_latest.md"
        report_path.write_text(report, encoding="utf-8")
        return report_path

    date_str = selected["date"]
    output_path = DATA_DIR / f"{date_str}.csv"

    report = f"""# 官方每日價格抓取報告

執行時間：{taiwan_now.strftime("%Y-%m-%d %H:%M:%S")} Asia/Taipei
台灣目標日期：{target_date}
結果：成功
官方價格資料日：{date_str}
上市筆數：{selected["twse_rows"]}
上櫃筆數：{selected["tpex_rows"]}
總筆數：{selected["total_rows"]}
輸出檔案：{output_path}

檢查紀錄：
{log_text}
"""

    report_path = LATEST_DIR / "official_price_fetch_latest.md"
    report_path.write_text(report, encoding="utf-8")
    return report_path


def main():
    taiwan_now = datetime.now(ZoneInfo("Asia/Taipei"))
    target_date = taiwan_now.strftime("%Y%m%d")

    selected = None
    log_lines = []

    for offset in range(0, 8):
        date_str = (taiwan_now - timedelta(days=offset)).strftime("%Y%m%d")
        result = try_fetch_one_date(date_str)

        log_lines.append(
            f"{result['date']}：{result['reason']}，"
            f"上市 {result['twse_rows']}，"
            f"上櫃 {result['tpex_rows']}，"
            f"合計 {result['total_rows']}"
        )

        if result["valid"]:
            selected = result
            break

    if selected is None:
        report_path = write_report(taiwan_now, target_date, None, log_lines)
        print("No valid official daily price data found.")
        print(f"Report saved: {report_path}")
        print("Continue pipeline without updating official daily price data.")
    return 0

    date_str = selected["date"]
    combined = selected["combined"]

    output_path = DATA_DIR / f"{date_str}.csv"
    combined.to_csv(output_path, index=False, encoding="utf-8-sig")

    report_path = write_report(taiwan_now, target_date, selected, log_lines)

    print(f"Taiwan target date: {target_date}")
    print(f"Saved official daily price date: {date_str}")
    print(f"Saved official daily price: {output_path}")
    print(f"Report saved: {report_path}")
    print(f"TWSE rows: {selected['twse_rows']}")
    print(f"TPEx rows: {selected['tpex_rows']}")
    print(f"Total rows: {selected['total_rows']}")


if __name__ == "__main__":
    main()
