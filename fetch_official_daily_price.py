from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from io import StringIO

import pandas as pd
import requests


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "daily_price"
LATEST_DIR = BASE_DIR / "output" / "latest"

DATA_DIR.mkdir(parents=True, exist_ok=True)
LATEST_DIR.mkdir(parents=True, exist_ok=True)


def clean_number(value):
    if pd.isna(value):
        return None
    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("--", "")
    text = text.replace("X", "")
    text = text.replace("+", "")
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


def fetch_twse_daily_price(date_str):
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX"
    params = {
        "response": "json",
        "date": date_str,
        "type": "ALLBUT0999",
    }

    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        print(f"TWSE fetch failed for {date_str}: {exc}")
        return pd.DataFrame()

    tables = data.get("tables", [])
    target_table = None

    for table in tables:
        fields = table.get("fields", [])
        if "證券代號" in fields and "證券名稱" in fields and "收盤價" in fields:
            target_table = table
            break

    if target_table is None:
        print(f"TWSE no valid table for {date_str}")
        return pd.DataFrame()

    fields = target_table.get("fields", [])
    rows = target_table.get("data", [])

    df = pd.DataFrame(rows, columns=fields)

    col_map = {
        "證券代號": "ticker",
        "證券名稱": "name",
        "成交股數": "volume",
        "開盤價": "open",
        "最高價": "high",
        "最低價": "low",
        "收盤價": "close",
    }

    missing_cols = [col for col in col_map if col not in df.columns]
    if missing_cols:
        print(f"TWSE missing columns for {date_str}: {missing_cols}")
        return pd.DataFrame()

    df = df[list(col_map.keys())].rename(columns=col_map)
    df["market"] = "TWSE"
    df["date"] = date_str

    return clean_price_df(df)


def fetch_tpex_daily_price(date_str):
    roc_year = int(date_str[:4]) - 1911
    roc_date = f"{roc_year}/{date_str[4:6]}/{date_str[6:8]}"

    urls = [
        "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php",
        "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=zh-tw",
    ]

    param_sets = [
        {"l": "zh-tw", "d": roc_date, "o": "csv"},
        {"l": "zh-tw", "d": roc_date, "se": "EW", "o": "csv"},
        {"l": "zh-tw", "d": roc_date, "s": "0,asc,0", "o": "csv"},
    ]

    for url in urls:
        for params in param_sets:
            try:
                response = requests.get(url, params=params, timeout=30)
                response.raise_for_status()
                text = response.text
            except Exception as exc:
                print(f"TPEx fetch failed for {date_str}: {exc}")
                continue

            parsed = parse_tpex_csv_text(text, date_str)
            if not parsed.empty:
                print(f"TPEx parsed rows for {date_str}: {len(parsed)}")
                return parsed

    print(f"TPEx no valid data for {date_str}")
    return pd.DataFrame()


def parse_tpex_csv_text(text, date_str):
    if not text:
        return pd.DataFrame()

    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if "代號" in line and "名稱" in line and "收盤" in line:
            lines.append(line)
            continue
        if line[:4].isdigit() or line.startswith('"0') or line.startswith("0"):
            lines.append(line)

    if len(lines) < 2:
        return pd.DataFrame()

    csv_text = "\n".join(lines)

    try:
        df = pd.read_csv(StringIO(csv_text))
    except Exception:
        try:
            df = pd.read_csv(StringIO(csv_text), header=None)
        except Exception:
            return pd.DataFrame()

    df.columns = [str(col).strip().replace('"', "") for col in df.columns]

    col_candidates = {
        "ticker": ["代號", "證券代號"],
        "name": ["名稱", "證券名稱"],
        "close": ["收盤", "收盤價"],
        "open": ["開盤", "開盤價"],
        "high": ["最高", "最高價"],
        "low": ["最低", "最低價"],
        "volume": ["成交股數", "成交股數(股)", "成交仟股"],
    }

    selected = {}

    for std_col, possible_cols in col_candidates.items():
        for col in possible_cols:
            if col in df.columns:
                selected[std_col] = col
                break

    if len(selected) < len(col_candidates):
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

        print("No valid official daily price data found.")
        print(f"Report saved: {report_path}")
        return

    date_str = selected["date"]
    combined = selected["combined"]

    output_path = DATA_DIR / f"{date_str}.csv"
    combined.to_csv(output_path, index=False, encoding="utf-8-sig")

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

    print(f"Taiwan target date: {target_date}")
    print(f"Saved official daily price date: {date_str}")
    print(f"Saved official daily price: {output_path}")
    print(f"Report saved: {report_path}")
    print(f"TWSE rows: {selected['twse_rows']}")
    print(f"TPEx rows: {selected['tpex_rows']}")
    print(f"Total rows: {selected['total_rows']}")


if __name__ == "__main__":
    main()
