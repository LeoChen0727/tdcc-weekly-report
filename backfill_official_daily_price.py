import io
import time
import requests
import pandas as pd

from datetime import datetime, timedelta
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)


LOOKBACK_DAYS = 180


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

    required_cols = ["證券代號", "證券名稱", "開盤價", "最高價", "最低價", "收盤價", "成交股數", "成交金額"]

    for col in required_cols:
        if col not in df.columns:
            print(f"TWSE {date_str}: missing column {col}")
            return pd.DataFrame()

    df = df[df["證券代號"].astype(str).str.match(r"^\d{4}$")].copy()

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

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.encoding = "utf-8"
    except Exception as e:
        print(f"TPEx {date_str}: request failed {e}")
        return pd.DataFrame()

    try:
        data = r.json()
    except Exception:
        print(f"TPEx {date_str}: json parse failed")
        return pd.DataFrame()

    aa_data = data.get("aaData", [])
    fields = data.get("fields", [])

    if not aa_data or not fields:
        print(f"TPEx {date_str}: no data")
        return pd.DataFrame()

    df = pd.DataFrame(aa_data, columns=fields)

    code_col = "代號" if "代號" in df.columns else "證券代號"
    name_col = "名稱" if "名稱" in df.columns else "證券名稱"

    required_cols = [code_col, name_col, "開盤", "最高", "最低", "收盤", "成交股數"]

    for col in required_cols:
        if col not in df.columns:
            print(f"TPEx {date_str}: missing column {col}")
            return pd.DataFrame()

    turnover_col = "成交金額(元)" if "成交金額(元)" in df.columns else None

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
        "turnover": df[turnover_col].apply(normalize_number) if turnover_col else None,
    })

    result = result[result["ticker"].astype(str).str.match(r"^\d{4}$")].copy()
    result = result.dropna(subset=["close", "volume"])

    return result


def fetch_combined_daily_price(date_str):
    twse_df = fetch_twse_daily_price(date_str)
    time.sleep(0.5)

    tpex_df = fetch_tpex_daily_price(date_str)
    time.sleep(0.5)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    return twse_df, tpex_df, combined


def main():
    today = datetime.now()

    success_dates = []
    skipped_existing_dates = []
    no_data_dates = []
    failed_dates = []

    for i in range(LOOKBACK_DAYS):
        target_date = today - timedelta(days=i)
        date_str = target_date.strftime("%Y%m%d")

        output_path = DATA_DIR / f"{date_str}.csv"

        if output_path.exists():
            skipped_existing_dates.append(date_str)
            print(f"Skip existing: {date_str}")
            continue

        print(f"Fetching: {date_str}")

        try:
            twse_df, tpex_df, combined = fetch_combined_daily_price(date_str)

            if combined.empty:
                no_data_dates.append(date_str)
                print(f"No data: {date_str}")
                continue

            combined.to_csv(output_path, index=False, encoding="utf-8-sig")
            success_dates.append(date_str)

            print(
                f"Saved {date_str}: "
                f"TWSE={len(twse_df)}, TPEx={len(tpex_df)}, Total={len(combined)}"
            )

        except Exception as e:
            failed_dates.append(date_str)
            print(f"Failed {date_str}: {e}")

        time.sleep(1.0)

    report = f"""# 官方歷史價格補抓報告

回補天數：{LOOKBACK_DAYS}

成功新增交易日數：{len(success_dates)}
已存在略過：{len(skipped_existing_dates)}
無資料日期：{len(no_data_dates)}
失敗日期：{len(failed_dates)}

## 成功新增日期

{", ".join(success_dates[:50]) if success_dates else "無"}

## 已存在略過日期

{", ".join(skipped_existing_dates[:50]) if skipped_existing_dates else "無"}

## 無資料日期

通常是週末、國定假日，或官方尚未提供資料。

{", ".join(no_data_dates[:80]) if no_data_dates else "無"}

## 失敗日期

{", ".join(failed_dates[:50]) if failed_dates else "無"}
"""

    Path("output/official_price_backfill_latest.md").write_text(report, encoding="utf-8")

    print("Backfill finished.")
    print(f"Success: {len(success_dates)}")
    print(f"Existing: {len(skipped_existing_dates)}")
    print(f"No data: {len(no_data_dates)}")
    print(f"Failed: {len(failed_dates)}")


if __name__ == "__main__":
    main()
