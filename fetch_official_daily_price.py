import io
import requests
import pandas as pd

from datetime import datetime
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


MIN_TWSE_ROWS = 700
MIN_TPEX_ROWS = 500
MIN_TOTAL_ROWS = 1500


def normalize_number(value):
    if pd.isna(value):
        return None

    text = str(value).replace(",", "").replace("--", "").strip()

    if text in ["", "X", "除權息", "----"]:
        return None

    try:
        return float(text)
    except ValueError:
        return None


def is_common_stock_ticker(value):
    text = str(value).strip()

    if not text.isdigit():
        return False

    if len(text) != 4:
        return False

    if text.startswith("00"):
        return False

    return True


def fetch_twse_daily_price(date_str):
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX"
    params = {
        "response": "csv",
        "date": date_str,
        "type": "ALLBUT0999",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.encoding = "big5"
    except Exception as e:
        print(f"TWSE {date_str}: request failed {e}")
        return pd.DataFrame()

    lines = r.text.splitlines()

    header_index = None
    for i, line in enumerate(lines):
        if "證券代號" in line and "證券名稱" in line:
            header_index = i
            break

    if header_index is None:
        print(f"TWSE {date_str}: no table found")
        return pd.DataFrame()

    csv_text = "\n".join(lines[header_index:])

    try:
        df = pd.read_csv(io.StringIO(csv_text))
    except Exception as e:
        print(f"TWSE {date_str}: csv parse failed {e}")
        return pd.DataFrame()

    df.columns = [str(c).replace('"', "").strip() for c in df.columns]

    required_cols = [
        "證券代號",
        "證券名稱",
        "開盤價",
        "最高價",
        "最低價",
        "收盤價",
        "成交股數",
        "成交金額",
    ]

    for col in required_cols:
        if col not in df.columns:
            print(f"TWSE {date_str}: missing column {col}")
            return pd.DataFrame()

    df = df[df["證券代號"].apply(is_common_stock_ticker)].copy()

    if df.empty:
        return pd.DataFrame()

    result = pd.DataFrame({
        "date": date_str,
        "ticker": df["證券代號"].astype(str),
        "name": df["證券名稱"].astype(str),
        "market": "listed",
        "open": df["開盤價"].apply(normalize_number),
        "high": df["最高價"].apply(normalize_number),
        "low": df["最低價"].apply(normalize_number),
        "close": df["收盤價"].apply(normalize_number),
        "volume": df["成交股數"].apply(normalize_number),
        "turnover": df["成交金額"].apply(normalize_number),
    })

    result = result.dropna(subset=["ticker", "close", "volume"])
    result = result[result["ticker"].apply(is_common_stock_ticker)].copy()

    return result.reset_index(drop=True)


def fetch_tpex_daily_price(date_str):
    roc_date = f"{int(date_str[:4]) - 1911}/{date_str[4:6]}/{date_str[6:8]}"

    url = "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php"
    params = {
        "l": "zh-tw",
        "d": roc_date,
        "s": "0,asc,0",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.encoding = "utf-8"
        data = r.json()
    except Exception as e:
        print(f"TPEx {date_str}: request/json failed {e}")
        return pd.DataFrame()

    aa_data = data.get("aaData", [])
    fields = data.get("fields", [])

    if not aa_data or not fields:
        print(f"TPEx {date_str}: no data")
        return pd.DataFrame()

    df = pd.DataFrame(aa_data, columns=fields)

    code_col = "代號" if "代號" in df.columns else "證券代號"
    name_col = "名稱" if "名稱" in df.columns else "證券名稱"

    required_cols = [
        code_col,
        name_col,
        "開盤",
        "最高",
        "最低",
        "收盤",
        "成交股數",
    ]

    for col in required_cols:
        if col not in df.columns:
            print(f"TPEx {date_str}: missing column {col}; columns={list(df.columns)}")
            return pd.DataFrame()

    turnover_col = "成交金額(元)" if "成交金額(元)" in df.columns else None

    result = pd.DataFrame({
        "date": date_str,
        "ticker": df[code_col].astype(str).str.extract(r"(\d{4})")[0],
        "name": df[name_col].astype(str),
        "market": "otc",
        "open": df["開盤"].apply(normalize_number),
        "high": df["最高"].apply(normalize_number),
        "low": df["最低"].apply(normalize_number),
        "close": df["收盤"].apply(normalize_number),
        "volume": df["成交股數"].apply(normalize_number),
        "turnover": df[turnover_col].apply(normalize_number) if turnover_col else None,
    })

    result = result.dropna(subset=["ticker", "close", "volume"])
    result = result[result["ticker"].apply(is_common_stock_ticker)].copy()

    return result.reset_index(drop=True)


def is_valid_trading_day_data(twse_df, tpex_df, combined):
    if combined.empty:
        return False, "combined empty"

    if len(twse_df) < MIN_TWSE_ROWS:
        return False, f"TWSE rows too low: {len(twse_df)}"

    if len(tpex_df) < MIN_TPEX_ROWS:
        return False, f"TPEx rows too low: {len(tpex_df)}"

    if len(combined) < MIN_TOTAL_ROWS:
        return False, f"total rows too low: {len(combined)}"

    markets = set(combined["market"].dropna().unique())

    if "listed" not in markets:
        return False, "missing listed market"

    if "otc" not in markets:
        return False, "missing otc market"

    if combined["ticker"].astype(str).str.startswith("00").any():
        return False, "contains 00xx products"

    return True, "valid"


def main():
    date_str = datetime.now().strftime("%Y%m%d")

    twse_df = fetch_twse_daily_price(date_str)
    tpex_df = fetch_tpex_daily_price(date_str)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if not combined.empty:
        combined = combined.drop_duplicates(subset=["date", "ticker"], keep="last")

    valid, reason = is_valid_trading_day_data(twse_df, tpex_df, combined)

    if not valid:
        report = f"""# 官方每日價格抓取報告

日期：{date_str}

結果：未存檔

原因：{reason}

上市筆數：{len(twse_df)}
上櫃筆數：{len(tpex_df)}
總筆數：{len(combined)}

說明：
- 這通常代表今天不是交易日、官方資料尚未更新，或資料不完整。
- 程式不會把不完整資料寫入 data/daily_price/，避免污染均線與回測。
"""
        Path("output/official_price_fetch_latest.md").write_text(report, encoding="utf-8")
        print(f"Invalid official price data: {reason}")
        return

    output_path = DATA_DIR / f"{date_str}.csv"
    combined.to_csv(output_path, index=False, encoding="utf-8-sig")

    report = f"""# 官方每日價格抓取報告

日期：{date_str}

結果：成功

上市筆數：{len(twse_df)}
上櫃筆數：{len(tpex_df)}
總筆數：{len(combined)}

輸出檔案：

{output_path}
"""

    Path("output/official_price_fetch_latest.md").write_text(report, encoding="utf-8")

    print(f"Saved official daily price: {output_path}")
    print(f"TWSE rows: {len(twse_df)}")
    print(f"TPEx rows: {len(tpex_df)}")
    print(f"Total rows: {len(combined)}")


if __name__ == "__main__":
    main()
