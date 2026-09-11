import hashlib
import io
import re
import time
import requests
import pandas as pd

from datetime import datetime, timedelta
from pathlib import Path


DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")

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


def _tpex_response_date(value):
    if isinstance(value, str) and re.fullmatch(r"[0-9]{8}", value):
        return datetime.strptime(value, "%Y%m%d").strftime("%Y%m%d")
    if isinstance(value, str) and re.fullmatch(r"[0-9]{3,4}/[0-9]{2}/[0-9]{2}", value):
        year, month, day = value.split("/")
        year = int(year) + (1911 if len(year) == 3 else 0)
        return datetime(year, int(month), int(day)).strftime("%Y%m%d")
    raise ValueError(f"TPEx missing or invalid response date: {value!r}")


def parse_tpex_daily_price(payload: dict, date_str: str) -> pd.DataFrame:
    """Parse the official OTC table; reject ambiguous dates and identities."""
    if not re.fullmatch(r"[0-9]{8}", date_str):
        raise ValueError(f"TPEx invalid requested date: {date_str!r}")
    requested_date = datetime.strptime(date_str, "%Y%m%d").strftime("%Y%m%d")
    if not isinstance(payload, dict) or payload.get("stat") != "ok":
        raise ValueError("TPEx response is not an ok payload")
    if _tpex_response_date(payload.get("date")) != requested_date:
        raise ValueError(f"TPEx response date mismatch for {date_str}")

    tables = payload.get("tables")
    if not isinstance(tables, list):
        raise ValueError("TPEx missing tables")
    matches = [
        table for table in tables
        if isinstance(table, dict)
        and table.get("title") == "上櫃股票每日收盤行情(不含定價)"
    ]
    if len(matches) != 1:
        raise ValueError("TPEx expected exactly one official OTC table")
    table = matches[0]
    if _tpex_response_date(table.get("date")) != requested_date:
        raise ValueError(f"TPEx table date mismatch for {date_str}")

    fields = [str(field).strip() for field in table.get("fields", [])]
    required = {"代號", "名稱", "開盤", "最高", "最低", "收盤", "成交股數", "成交金額(元)"}
    if len(fields) != len(set(fields)) or not required.issubset(fields):
        raise ValueError("TPEx missing or duplicate price fields")
    df = pd.DataFrame(table["data"], columns=fields)
    codes = df["代號"].astype(str).str.strip()
    duplicates = codes[codes.duplicated(keep=False)]
    if not duplicates.empty:
        raise ValueError(f"TPEx duplicate raw security code: {duplicates.tolist()}")
    # Filter the complete source code before numeric cleanup; never truncate it.
    df = df.loc[codes.apply(is_common_stock_ticker).astype(bool)].copy()

    result = pd.DataFrame({
        "date": date_str,
        "ticker": codes.loc[df.index],
        "name": df["名稱"].astype(str),
        "market": "otc",
        "open": df["開盤"].apply(normalize_number),
        "high": df["最高"].apply(normalize_number),
        "low": df["最低"].apply(normalize_number),
        "close": df["收盤"].apply(normalize_number),
        "volume": df["成交股數"].apply(normalize_number),
        "turnover": df["成交金額(元)"].apply(normalize_number),
    })

    # Keep the existing close/volume eligibility; missing OHLC is never filled.
    result = result.dropna(subset=["ticker", "close", "volume"])
    return result.reset_index(drop=True)


def fetch_tpex_daily_price(date_str):
    url = "https://www.tpex.org.tw/www/zh-tw/afterTrading/otc"
    params = {
        "date": datetime.strptime(date_str, "%Y%m%d").strftime("%Y/%m/%d"),
        "type": "EW",
        "response": "json",
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        data = r.json()
    except Exception as e:
        print(f"TPEx {date_str}: request/json failed {e}")
        return pd.DataFrame()

    return parse_tpex_daily_price(data, date_str)


def fetch_combined_daily_price(date_str):
    twse_df = fetch_twse_daily_price(date_str)
    time.sleep(0.5)

    tpex_df = fetch_tpex_daily_price(date_str)
    time.sleep(0.5)

    combined = pd.concat([twse_df, tpex_df], ignore_index=True)

    if not combined.empty:
        duplicates = combined.duplicated(subset=["date", "ticker"], keep=False)
        if duplicates.any():
            identities = combined.loc[duplicates, ["date", "ticker", "market"]]
            raise ValueError(f"Duplicate or cross-market daily identity: {identities.to_dict('records')}")

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


def _tpex_batch_signature(frame):
    columns = ["ticker", "name", "market", "open", "high", "low", "close", "volume", "turnover"]
    otc = frame.loc[frame["market"] == "otc", columns].copy()
    if otc.empty:
        return None
    otc["ticker"] = otc["ticker"].astype(str)
    for column in columns[3:]:
        otc[column] = pd.to_numeric(otc[column], errors="raise").astype(float)
    # Canonicalize only row order and numeric dtypes for existing CSV comparisons.
    batch = otc.sort_values("ticker").to_csv(index=False, float_format="%.17g")
    return hashlib.sha256(batch.encode("utf-8")).hexdigest()


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)
    today = datetime.now()
    existing_dates = sorted(path.stem for path in DATA_DIR.glob("????????.csv") if path.stem.isdigit())
    seen_tpex_batches = {}

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

            if valid:
                signature = _tpex_batch_signature(tpex_df)
                if signature in seen_tpex_batches:
                    valid = False
                    reason = f"TPEx exact batch repeats {seen_tpex_batches[signature]} on {date_str}"
                else:
                    previous_date = next((day for day in reversed(existing_dates) if day < date_str), None)
                    if previous_date:
                        previous = pd.read_csv(
                            DATA_DIR / f"{previous_date}.csv",
                            dtype={"date": str, "ticker": str},
                            float_precision="round_trip",
                        )
                        if signature == _tpex_batch_signature(previous):
                            valid = False
                            reason = f"TPEx exact batch repeats existing {previous_date} on {date_str}"

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
            seen_tpex_batches[signature] = date_str
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

    (OUTPUT_DIR / "official_price_backfill_latest.md").write_text(report, encoding="utf-8")

    print("Backfill finished.")
    print(f"Success: {len(success_dates)}")
    print(f"Existing skipped: {len(skipped_existing_dates)}")
    print(f"Invalid: {len(invalid_dates)}")
    print(f"Failed: {len(failed_dates)}")


if __name__ == "__main__":
    main()
