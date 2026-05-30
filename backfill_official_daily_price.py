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


# Keep enough price history for 180D chart windows plus D+20 model validation.
# This is intentionally larger than the daily report window; it is used by the
# manual backfill workflow, not the daily pipeline.
LOOKBACK_DAYS = 420

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


def extract_tpex_table_from_json(data):
    """
    TPEx DAILY_CLOSE_quotes 回傳格式是 dict，真正資料在 tables 裡。
    這裡從 tables 中找出包含股票代號、名稱、收盤等欄位的表格。
    """
    tables = data.get("tables", [])

    if not isinstance(tables, list) or not tables:
        return pd.DataFrame()

    for table in tables:
        fields = table.get("fields") or table.get("field") or []
        rows = table.get("data") or table.get("aaData") or []

        if not fields or not rows:
            continue

        df = pd.DataFrame(rows, columns=fields)

        columns = set(df.columns)

        possible_code_cols = ["代號", "證券代號"]
        possible_name_cols = ["名稱", "證券名稱"]

        code_col = next((c for c in possible_code_cols if c in columns), None)
        name_col = next((c for c in possible_name_cols if c in columns), None)

        required = [code_col, name_col, "開盤", "最高", "最低", "收盤", "成交股數"]

        if code_col and name_col and all(c in columns for c in required if c):
            return df

    return pd.DataFrame()


def fetch_tpex_daily_price(date_str):
    """
    抓 TPEx 上櫃每日收盤行情。
    使用 DAILY_CLOSE_quotes + o=json + 指定日期。
    """
    roc_date = f"{int(date_str[:4]) - 1911}/{date_str[4:6]}/{date_str[6:8]}"

    url = "https://www.tpex.org.tw/web/stock/aftertrading/DAILY_CLOSE_quotes/stk_quote_result.php"
    params = {
        "l": "zh-tw",
        "d": roc_date,
        "o": "json",
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.encoding = "utf-8"
        data = r.json()
    except Exception as e:
        print(f"TPEx {date_str}: request/json failed {e}")
        return pd.DataFrame()

    if not isinstance(data, dict):
        print(f"TPEx {date_str}: json is not dict")
        return pd.DataFrame()

    df = extract_tpex_table_from_json(data)

    if df.empty:
        print(f"TPEx {date_str}: no usable table")
        return pd.DataFrame()

    code_col = "代號" if "代號" in df.columns else "證券代號"
    name_col = "名稱" if "名稱" in df.columns else "證券名稱"

    turnover_col = "成交金額(元)" if "成交金額(元)" in df.columns else None

    if turnover_col is None:
        turnover_col = "成交金額" if "成交金額" in df.columns else None

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


def fetch_combined_daily_price(date_str):
    twse_df = fetch_twse_daily_price(date_str)
    time.sleep(0.5)

    tpex_df = fetch_tpex_daily_price(date_str)
    time.sleep(0.5)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if not combined.empty:
        combined = combined.drop_duplicates(subset=["date", "ticker"], keep="last")

    return twse_df, tpex_df, combined


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
    today = datetime.now()

    success_dates = []
    invalid_dates = []
    failed_dates = []
    skipped_existing_dates = []
    row_stats = []

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

            valid, reason = is_valid_trading_day_data(twse_df, tpex_df, combined)

            row_stats.append({
                "date": date_str,
                "twse_rows": len(twse_df),
                "tpex_rows": len(tpex_df),
                "total_rows": len(combined),
                "valid": valid,
                "reason": reason,
            })

            if not valid:
                invalid_dates.append(f"{date_str} ({reason})")
                print(f"Invalid data: {date_str} - {reason}")
                continue

            combined.to_csv(output_path, index=False, encoding="utf-8-sig")
            success_dates.append(date_str)

            print(
                f"Saved {date_str}: "
                f"TWSE={len(twse_df)}, TPEx={len(tpex_df)}, Total={len(combined)}"
            )

        except Exception as e:
            failed_dates.append(f"{date_str} ({e})")
            print(f"Failed {date_str}: {e}")

        time.sleep(1.0)

    stats_df = pd.DataFrame(row_stats)

    if not stats_df.empty:
        stats_df.to_csv(
            OUTPUT_DIR / "official_price_backfill_row_stats.csv",
            index=False,
            encoding="utf-8-sig"
        )

    report = f"""# 官方歷史價格補抓報告

回補天數：{LOOKBACK_DAYS}

成功新增交易日數：{len(success_dates)}
已存在略過日期數：{len(skipped_existing_dates)}
無效 / 非交易日 / 資料不完整日期數：{len(invalid_dates)}
失敗日期數：{len(failed_dates)}

## 成功新增日期

{", ".join(success_dates[:100]) if success_dates else "無"}

## 已存在略過日期

{", ".join(skipped_existing_dates[:100]) if skipped_existing_dates else "無"}

## 無效 / 非交易日 / 資料不完整日期

{chr(10).join(invalid_dates[:120]) if invalid_dates else "無"}

## 失敗日期

{chr(10).join(failed_dates[:120]) if failed_dates else "無"}

## 每日筆數統計

{stats_df.head(80).to_markdown(index=False) if not stats_df.empty else "無"}
"""

    Path("output/official_price_backfill_latest.md").write_text(report, encoding="utf-8")

    print("Backfill finished.")
    print(f"Success: {len(success_dates)}")
    print(f"Existing skipped: {len(skipped_existing_dates)}")
    print(f"Invalid: {len(invalid_dates)}")
    print(f"Failed: {len(failed_dates)}")


if __name__ == "__main__":
    main()
