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
MIN_EXPECTED_TOTAL_ROWS = 1500


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


def fetch_tpex_daily_price_from_openapi(date_str):
    """
    從 TPEx OpenAPI 抓上櫃每日收盤行情。
    OpenAPI 通常提供最新交易日資料，不一定支援指定歷史日期。
    所以這個函數只在 date_str 等於最新資料日時有效。
    """
    url = "https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes"

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.encoding = "utf-8"
        data = r.json()
    except Exception as e:
        print(f"TPEx OpenAPI {date_str}: request/json failed {e}")
        return pd.DataFrame()

    if not isinstance(data, list) or not data:
        print(f"TPEx OpenAPI {date_str}: no data")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    rename_candidates = {
        "Date": "api_date",
        "SecuritiesCompanyCode": "ticker",
        "CompanyName": "name",
        "Close": "close",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "TradingShares": "volume",
        "TransactionAmount": "turnover",
    }

    df = df.rename(columns={k: v for k, v in rename_candidates.items() if k in df.columns})

    required_cols = ["ticker", "name", "open", "high", "low", "close", "volume"]

    for col in required_cols:
        if col not in df.columns:
            print(f"TPEx OpenAPI {date_str}: missing column {col}; columns={list(df.columns)}")
            return pd.DataFrame()

    result = pd.DataFrame({
        "date": date_str,
        "ticker": df["ticker"].astype(str).str.extract(r"(\d{4})")[0],
        "name": df["name"].astype(str),
        "market": "otc",
        "open": df["open"].apply(normalize_number),
        "high": df["high"].apply(normalize_number),
        "low": df["low"].apply(normalize_number),
        "close": df["close"].apply(normalize_number),
        "volume": df["volume"].apply(normalize_number),
        "turnover": df["turnover"].apply(normalize_number) if "turnover" in df.columns else None,
    })

    result = result.dropna(subset=["ticker", "close", "volume"])
    result = result[result["ticker"].astype(str).str.match(r"^\d{4}$")].copy()

    return result


def fetch_tpex_daily_price_legacy(date_str):
    """
    從 TPEx 舊版查詢端點抓指定日期上櫃每日收盤行情。
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
        data = r.json()
    except Exception as e:
        print(f"TPEx legacy {date_str}: request/json failed {e}")
        return pd.DataFrame()

    aa_data = data.get("aaData", [])
    fields = data.get("fields", [])

    if not aa_data or not fields:
        print(f"TPEx legacy {date_str}: no data")
        return pd.DataFrame()

    df = pd.DataFrame(aa_data, columns=fields)

    code_col = "代號" if "代號" in df.columns else "證券代號"
    name_col = "名稱" if "名稱" in df.columns else "證券名稱"

    required_cols = [code_col, name_col, "開盤", "最高", "最低", "收盤", "成交股數"]

    for col in required_cols:
        if col not in df.columns:
            print(f"TPEx legacy {date_str}: missing column {col}; columns={list(df.columns)}")
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
    result = result[result["ticker"].astype(str).str.match(r"^\d{4}$")].copy()

    return result


def fetch_tpex_daily_price(date_str):
    legacy_df = fetch_tpex_daily_price_legacy(date_str)

    if not legacy_df.empty:
        return legacy_df

    openapi_df = fetch_tpex_daily_price_from_openapi(date_str)

    return openapi_df


def fetch_combined_daily_price(date_str):
    twse_df = fetch_twse_daily_price(date_str)
    time.sleep(0.5)

    tpex_df = fetch_tpex_daily_price(date_str)
    time.sleep(0.5)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if not combined.empty:
        combined = combined.drop_duplicates(subset=["date", "ticker"], keep="last")

    return twse_df, tpex_df, combined


def existing_file_is_complete(output_path):
    if not output_path.exists():
        return False

    try:
        old_df = pd.read_csv(output_path, dtype={"ticker": str})
    except Exception:
        return False

    if old_df.empty:
        return False

    markets = set(old_df.get("market", []))
    total_rows = len(old_df)

    if "listed" not in markets:
        return False

    if "otc" not in markets:
        return False

    if total_rows < MIN_EXPECTED_TOTAL_ROWS:
        return False

    return True


def main():
    today = datetime.now()

    success_dates = []
    skipped_complete_dates = []
    replaced_incomplete_dates = []
    no_data_dates = []
    failed_dates = []
    row_stats = []

    for i in range(LOOKBACK_DAYS):
        target_date = today - timedelta(days=i)
        date_str = target_date.strftime("%Y%m%d")

        output_path = DATA_DIR / f"{date_str}.csv"

        if existing_file_is_complete(output_path):
            skipped_complete_dates.append(date_str)
            print(f"Skip complete existing: {date_str}")
            continue

        if output_path.exists():
            replaced_incomplete_dates.append(date_str)
            print(f"Replace incomplete existing: {date_str}")

        print(f"Fetching: {date_str}")

        try:
            twse_df, tpex_df, combined = fetch_combined_daily_price(date_str)

            if combined.empty:
                no_data_dates.append(date_str)
                print(f"No data: {date_str}")
                continue

            combined.to_csv(output_path, index=False, encoding="utf-8-sig")
            success_dates.append(date_str)

            row_stats.append({
                "date": date_str,
                "twse_rows": len(twse_df),
                "tpex_rows": len(tpex_df),
                "total_rows": len(combined),
            })

            print(
                f"Saved {date_str}: "
                f"TWSE={len(twse_df)}, TPEx={len(tpex_df)}, Total={len(combined)}"
            )

        except Exception as e:
            failed_dates.append(date_str)
            print(f"Failed {date_str}: {e}")

        time.sleep(1.0)

    stats_df = pd.DataFrame(row_stats)

    if not stats_df.empty:
        stats_df.to_csv(OUTPUT_DIR / "official_price_backfill_row_stats.csv", index=False, encoding="utf-8-sig")

    report = f"""# 官方歷史價格補抓報告

回補天數：{LOOKBACK_DAYS}

成功新增 / 覆蓋交易日數：{len(success_dates)}
完整已存在略過：{len(skipped_complete_dates)}
不完整檔案被覆蓋：{len(replaced_incomplete_dates)}
無資料日期：{len(no_data_dates)}
失敗日期：{len(failed_dates)}

## 成功新增 / 覆蓋日期

{", ".join(success_dates[:80]) if success_dates else "無"}

## 不完整檔案被覆蓋日期

{", ".join(replaced_incomplete_dates[:80]) if replaced_incomplete_dates else "無"}

## 完整已存在略過日期

{", ".join(skipped_complete_dates[:80]) if skipped_complete_dates else "無"}

## 無資料日期

通常是週末、國定假日，或官方尚未提供資料。

{", ".join(no_data_dates[:100]) if no_data_dates else "無"}

## 失敗日期

{", ".join(failed_dates[:80]) if failed_dates else "無"}

## 每日筆數統計

{stats_df.head(30).to_markdown(index=False) if not stats_df.empty else "無"}
"""

    Path("output/official_price_backfill_latest.md").write_text(report, encoding="utf-8")

    print("Backfill finished.")
    print(f"Success/replaced: {len(success_dates)}")
    print(f"Complete existing: {len(skipped_complete_dates)}")
    print(f"Incomplete replaced: {len(replaced_incomplete_dates)}")
    print(f"No data: {len(no_data_dates)}")
    print(f"Failed: {len(failed_dates)}")


if __name__ == "__main__":
    main()
