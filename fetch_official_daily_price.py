import io
import requests
import pandas as pd

from datetime import datetime
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


def normalize_number(value):
    if pd.isna(value):
        return None

    text = str(value).replace(",", "").replace("--", "").strip()

    if text in ["", "X", "除權息"]:
        return None

    try:
        return float(text)
    except ValueError:
        return None


def fetch_twse_daily_price(date_str):
    """
    抓 TWSE 上市每日收盤行情。
    date_str format: YYYYMMDD
    """
    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX"
    params = {
        "response": "csv",
        "date": date_str,
        "type": "ALLBUT0999",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, params=params, headers=headers, timeout=30)
    r.encoding = "big5"

    lines = r.text.splitlines()

    header_index = None
    for i, line in enumerate(lines):
        if "證券代號" in line and "證券名稱" in line:
            header_index = i
            break

    if header_index is None:
        print("TWSE: no table found")
        return pd.DataFrame()

    csv_text = "\n".join(lines[header_index:])
    df = pd.read_csv(io.StringIO(csv_text))

    df.columns = [str(c).replace('"', "").strip() for c in df.columns]

    if "證券代號" not in df.columns:
        print("TWSE: missing 證券代號 column")
        return pd.DataFrame()

    df = df[df["證券代號"].astype(str).str.match(r"^\d{4}$")].copy()

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

    result = result.dropna(subset=["close", "volume"])

    return result


def fetch_tpex_daily_price(date_str):
    """
    抓 TPEx 上櫃每日收盤行情。
    date_str format: YYYYMMDD
    """
    roc_date = f"{int(date_str[:4]) - 1911}/{date_str[4:6]}/{date_str[6:8]}"

    url = "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php"
    params = {
        "l": "zh-tw",
        "d": roc_date,
        "s": "0,asc,0",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, params=params, headers=headers, timeout=30)
    r.encoding = "utf-8"

    try:
        data = r.json()
    except Exception:
        print("TPEx: json parse failed")
        return pd.DataFrame()

    aa_data = data.get("aaData", [])
    fields = data.get("fields", [])

    if not aa_data or not fields:
        print("TPEx: no data")
        return pd.DataFrame()

    df = pd.DataFrame(aa_data, columns=fields)

    code_col = "代號" if "代號" in df.columns else "證券代號"
    name_col = "名稱" if "名稱" in df.columns else "證券名稱"

    result = pd.DataFrame({
        "date": date_str,
        "ticker": df[code_col].astype(str),
        "name": df[name_col].astype(str),
        "market": "otc",
        "open": df["開盤"].apply(normalize_number),
        "high": df["最高"].apply(normalize_number),
        "low": df["最低"].apply(normalize_number),
        "close": df["收盤"].apply(normalize_number),
        "volume": df["成交股數"].apply(normalize_number),
        "turnover": df["成交金額(元)"].apply(normalize_number),
    })

    result = result[result["ticker"].astype(str).str.match(r"^\d{4}$")].copy()
    result = result.dropna(subset=["close", "volume"])

    return result


def main():
    date_str = datetime.now().strftime("%Y%m%d")

    twse_df = fetch_twse_daily_price(date_str)
    tpex_df = fetch_tpex_daily_price(date_str)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if combined.empty:
        report = f"""# 官方每日價格抓取報告

日期：{date_str}

結果：沒有抓到資料。

可能原因：
- 今天不是交易日
- 官方資料尚未更新
- 官方 API 格式變動
"""
        Path("output/official_price_fetch_latest.md").write_text(report, encoding="utf-8")
        print("No official price data fetched.")
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
