from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import io
import json
import math
import re
from typing import Any

import pandas as pd
import requests


# ============================================================
# Paths
# ============================================================

TAIPEI = ZoneInfo("Asia/Taipei")

DATA_DIR = Path("data/daily_price")
OUTPUT_DIR = Path("output")
LATEST_DIR = OUTPUT_DIR / "latest"
HISTORY_DIR = OUTPUT_DIR / "history"

REPORT_PATH = LATEST_DIR / "stock_monitor_latest.md"
BREAKOUT_CSV_PATH = LATEST_DIR / "breakout_latest.csv"
RANGE_REBOUND_CSV_PATH = LATEST_DIR / "range_rebound_watch_latest.csv"
REVENUE_PULLBACK_CSV_PATH = LATEST_DIR / "revenue_pullback_latest.csv"
PULLBACK_REBOUND_CSV_PATH = LATEST_DIR / "pullback_rebound_latest.csv"

TDCC_LATEST_PATH = LATEST_DIR / "tdcc_holder_ratio_latest.csv"

OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_LATEST_CSV = LATEST_DIR / "official_daily_price_latest.csv"

LATEST_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Settings
# ============================================================

MIN_VOLUME_LOTS = 1000
MIN_HISTORY_DAYS_BREAKOUT = 90
MIN_HISTORY_DAYS_REVENUE = 61

MAINSTREAM_INDUSTRY_KEYWORDS = [
    "半導體",
    "電子零組件",
    "電腦及週邊",
    "通信網路",
    "光電",
    "其他電子",
    "資訊服務",
    "電子通路",
    "電機機械",
    "綠能環保",
    "生技醫療",
    "數位雲端",
]

NUMERIC_PRICE_COLS = [
    "open",
    "high",
    "low",
    "close",
    "volume",
    "turnover",
    "trading_value",
]


# ============================================================
# Basic helpers
# ============================================================

def now_taipei() -> str:
    return datetime.now(TAIPEI).strftime("%Y-%m-%d %H:%M:%S")


def normalize_text(value: Any) -> str:
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


def normalize_code(value: Any) -> str:
    text = normalize_text(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9]", "", text)
    if not text:
        return ""
    return text.zfill(4)


def normalize_date(value: Any) -> str:
    text = normalize_text(value)
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    # ROC date，例如 1150522
    if len(digits) >= 7:
        try:
            y = int(digits[:3]) + 1911
            m = int(digits[3:5])
            d = int(digits[5:7])
            return f"{y:04d}{m:02d}{d:02d}"
        except Exception:
            pass

    return ""


def to_number(value: Any) -> float:
    text = normalize_text(value)
    if text in {"", "--", "-", "X", "x"}:
        return math.nan

    text = (
        text.replace(",", "")
        .replace("%", "")
        .replace("％", "")
        .replace("+", "")
        .strip()
    )
    text = re.sub(r"[^\d.\-]", "", text)

    if text in {"", "-", ".", "-."}:
        return math.nan

    try:
        return float(text)
    except Exception:
        return math.nan


def safe_round(value: Any, digits: int = 2):
    try:
        if pd.isna(value):
            return pd.NA
    except Exception:
        pass

    try:
        return round(float(value), digits)
    except Exception:
        return pd.NA


def pct_change(new: float, old: float) -> float:
    if old is None or old == 0 or pd.isna(old):
        return 0.0
    if new is None or pd.isna(new):
        return 0.0
    return (new / old - 1) * 100


def is_mainstream_industry(industry: Any) -> bool:
    text = normalize_text(industry)
    return any(keyword in text for keyword in MAINSTREAM_INDUSTRY_KEYWORDS)


def split_mainstream(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if df.empty or "industry" not in df.columns:
        return pd.DataFrame(), pd.DataFrame()

    mainstream = df[df["industry"].apply(is_mainstream_industry)].copy()
    non_mainstream = df[~df["industry"].apply(is_mainstream_industry)].copy()
    return mainstream, non_mainstream


def get_official_fetch_saved_date() -> str:
    if OFFICIAL_PRICE_FETCH_JSON.exists():
        try:
            data = json.loads(OFFICIAL_PRICE_FETCH_JSON.read_text(encoding="utf-8"))
            return normalize_date(data.get("saved_price_date", ""))
        except Exception:
            pass

    if OFFICIAL_PRICE_FETCH_MD.exists():
        text = OFFICIAL_PRICE_FETCH_MD.read_text(encoding="utf-8", errors="ignore")
        for pattern in [
            r"saved_price_date[：:\s`]*([0-9/\-]{8,10})",
            r"官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
            r"最新官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
        ]:
            match = re.search(pattern, text)
            if match:
                date = normalize_date(match.group(1))
                if date:
                    return date

    return ""


# ============================================================
# Price data loading
# ============================================================

def normalize_price_columns(df: pd.DataFrame, file: Path | None = None) -> pd.DataFrame:
    df = df.copy()

    rename_map = {}

    # 新版 fetch_official_daily_price.py
    if "stock_id" in df.columns and "ticker" not in df.columns:
        rename_map["stock_id"] = "ticker"

    if "stock_name" in df.columns and "name" not in df.columns:
        rename_map["stock_name"] = "name"

    if "trading_value" in df.columns and "turnover" not in df.columns:
        rename_map["trading_value"] = "turnover"

    # 舊版或其他中文欄位
    if "證券代號" in df.columns and "ticker" not in df.columns:
        rename_map["證券代號"] = "ticker"

    if "證券名稱" in df.columns and "name" not in df.columns:
        rename_map["證券名稱"] = "name"

    if "收盤價" in df.columns and "close" not in df.columns:
        rename_map["收盤價"] = "close"

    if "開盤價" in df.columns and "open" not in df.columns:
        rename_map["開盤價"] = "open"

    if "最高價" in df.columns and "high" not in df.columns:
        rename_map["最高價"] = "high"

    if "最低價" in df.columns and "low" not in df.columns:
        rename_map["最低價"] = "low"

    if "成交股數" in df.columns and "volume" not in df.columns:
        rename_map["成交股數"] = "volume"

    if "成交金額" in df.columns and "turnover" not in df.columns:
        rename_map["成交金額"] = "turnover"

    df = df.rename(columns=rename_map)

    if "date" not in df.columns:
        # 從檔名補日期
        file_date = ""
        if file is not None:
            match = re.search(r"20\d{6}", file.name)
            if match:
                file_date = match.group(0)
        df["date"] = file_date

    if "ticker" not in df.columns:
        return pd.DataFrame()

    if "name" not in df.columns:
        df["name"] = ""

    if "market" not in df.columns:
        df["market"] = ""

    if "close" not in df.columns:
        return pd.DataFrame()

    if "open" not in df.columns:
        df["open"] = df["close"]

    if "high" not in df.columns:
        df["high"] = df["close"]

    if "low" not in df.columns:
        df["low"] = df["close"]

    if "volume" not in df.columns:
        df["volume"] = 0

    if "turnover" not in df.columns:
        df["turnover"] = 0

    keep_cols = [
        "date",
        "ticker",
        "name",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "turnover",
    ]

    df = df[keep_cols].copy()

    df["ticker"] = df["ticker"].map(normalize_code)
    df["date"] = df["date"].map(normalize_date)
    df["name"] = df["name"].map(normalize_text)
    df["market"] = df["market"].map(normalize_text)

    for col in ["open", "high", "low", "close", "volume", "turnover"]:
        df[col] = df[col].map(to_number)

    df = df.dropna(subset=["ticker", "date", "close"])
    df = df[df["ticker"].astype(str).str.match(r"^\d{4}$", na=False)].copy()
    df = df[df["date"].astype(str).str.match(r"^20\d{6}$", na=False)].copy()

    df["volume"] = df["volume"].fillna(0)
    df["turnover"] = df["turnover"].fillna(0)

    df = df[df["close"] > 0].copy()

    return df


def load_official_price_history() -> pd.DataFrame:
    frames = []

    # 先讀 data/daily_price 全部歷史
    if DATA_DIR.exists():
        files = sorted(DATA_DIR.glob("*.csv"))
    else:
        files = []

    for file in files:
        try:
            df = pd.read_csv(file, dtype=str)
            df = normalize_price_columns(df, file=file)
            if not df.empty:
                frames.append(df)
        except Exception as exc:
            print(f"Skip price file {file}: {exc}")

    # 再讀 output/latest/official_daily_price_latest.csv，確保最新日一定被吃到
    if OFFICIAL_PRICE_LATEST_CSV.exists():
        try:
            latest = pd.read_csv(OFFICIAL_PRICE_LATEST_CSV, dtype=str)
            latest = normalize_price_columns(latest, file=OFFICIAL_PRICE_LATEST_CSV)
            if not latest.empty:
                frames.append(latest)
        except Exception as exc:
            print(f"Skip latest official price file: {exc}")

    if not frames:
        print("No official daily price files found.")
        return pd.DataFrame()

    data = pd.concat(frames, ignore_index=True)

    data = data.drop_duplicates(["ticker", "date"], keep="last")
    data = data.sort_values(["ticker", "date"]).reset_index(drop=True)

    latest_date = data["date"].max() if not data.empty else ""
    official_fetch_date = get_official_fetch_saved_date()

    print(f"Loaded official price history rows={len(data)}, latest_date={latest_date}")
    print(f"Official fetch saved_price_date={official_fetch_date}")

    return data


# ============================================================
# Revenue
# ============================================================

def fetch_monthly_revenue() -> pd.DataFrame:
    urls = [
        ("listed", "https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv"),
        ("otc", "https://mopsfin.twse.com.tw/opendata/t187ap05_O.csv"),
    ]

    frames = []

    for market, url in urls:
        try:
            response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            response.encoding = "utf-8-sig"
            df = pd.read_csv(io.StringIO(response.text))
            df["market"] = market
            frames.append(df)
        except Exception as exc:
            print(f"Revenue fetch failed: {market} {exc}")

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)

    rename_map = {
        "公司代號": "ticker",
        "公司名稱": "name",
        "產業別": "industry",
        "資料年月": "revenue_period",
        "營業收入-當月營收": "monthly_revenue",
        "營業收入-去年同月增減(%)": "revenue_yoy_pct",
        "累計營業收入-前期比較增減(%)": "cumulative_yoy_pct",
    }

    keep = [col for col in rename_map if col in df.columns]
    if not keep:
        return pd.DataFrame()

    df = df[keep + ["market"]].rename(columns=rename_map).copy()
    df["ticker"] = df["ticker"].map(normalize_code)

    for col in ["monthly_revenue", "revenue_yoy_pct", "cumulative_yoy_pct"]:
        if col in df.columns:
            df[col] = df[col].map(to_number)

    df = df.dropna(subset=["ticker", "revenue_yoy_pct", "cumulative_yoy_pct"])
    df = df[df["ticker"].astype(str).str.match(r"^\d{4}$", na=False)].copy()

    return df.reset_index(drop=True)


def build_industry_map(revenue_df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if revenue_df.empty:
        return {}

    temp = revenue_df.copy()
    temp["ticker"] = temp["ticker"].map(normalize_code)

    result = {}

    for _, row in temp.iterrows():
        ticker = row["ticker"]
        result[ticker] = {
            "industry": row.get("industry", ""),
            "revenue_period": row.get("revenue_period", ""),
            "revenue_yoy_pct": row.get("revenue_yoy_pct", pd.NA),
            "cumulative_yoy_pct": row.get("cumulative_yoy_pct", pd.NA),
        }

    return result


# ============================================================
# TDCC
# ============================================================

def load_tdcc_latest() -> pd.DataFrame:
    if not TDCC_LATEST_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(TDCC_LATEST_PATH, dtype=str)
    except Exception as exc:
        print(f"TDCC read failed: {exc}")
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    rename_map = {}

    if "stock_id" in df.columns and "ticker" not in df.columns:
        rename_map["stock_id"] = "ticker"

    if "code" in df.columns and "ticker" not in df.columns:
        rename_map["code"] = "ticker"

    if "股票代號" in df.columns and "ticker" not in df.columns:
        rename_map["股票代號"] = "ticker"

    if "date" in df.columns and "tdcc_date" not in df.columns:
        rename_map["date"] = "tdcc_date"

    if "資料日期" in df.columns and "tdcc_date" not in df.columns:
        rename_map["資料日期"] = "tdcc_date"

    if "400張以上%" in df.columns and "holder_400_pct" not in df.columns:
        rename_map["400張以上%"] = "holder_400_pct"

    if "400張變化" in df.columns and "holder_400_change" not in df.columns:
        rename_map["400張變化"] = "holder_400_change"

    if "1000張以上%" in df.columns and "holder_1000_pct" not in df.columns:
        rename_map["1000張以上%"] = "holder_1000_pct"

    if "1000張變化" in df.columns and "holder_1000_change" not in df.columns:
        rename_map["1000張變化"] = "holder_1000_change"

    if "TDCC判斷" in df.columns and "tdcc_judgement" not in df.columns:
        rename_map["TDCC判斷"] = "tdcc_judgement"

    df = df.rename(columns=rename_map).copy()

    if "ticker" not in df.columns:
        return pd.DataFrame()

    df["ticker"] = df["ticker"].map(normalize_code)

    for col in [
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
        "tdcc_400_change_sum",
        "tdcc_1000_change_sum",
        "tdcc_400_up_weeks",
        "tdcc_1000_up_weeks",
        "tdcc_weeks_used",
    ]:
        if col in df.columns:
            df[col] = df[col].map(to_number)
        else:
            df[col] = pd.NA

    if "tdcc_date" not in df.columns:
        df["tdcc_date"] = ""

    if "tdcc_judgement" not in df.columns:
        df["tdcc_judgement"] = ""

    if "tdcc_accumulation_signal" not in df.columns:
        df["tdcc_accumulation_signal"] = ""

    if "tdcc_accumulation_note" not in df.columns:
        df["tdcc_accumulation_note"] = ""

    return df.drop_duplicates("ticker", keep="last").reset_index(drop=True)


def tdcc_signal_from_row(row: pd.Series) -> tuple[str, str]:
    explicit_signal = normalize_text(row.get("tdcc_accumulation_signal", ""))
    explicit_note = normalize_text(row.get("tdcc_accumulation_note", ""))

    if explicit_signal:
        return explicit_signal, explicit_note

    c400 = row.get("holder_400_change", pd.NA)
    c1000 = row.get("holder_1000_change", pd.NA)

    try:
        c400 = 0 if pd.isna(c400) else float(c400)
    except Exception:
        c400 = 0

    try:
        c1000 = 0 if pd.isna(c1000) else float(c1000)
    except Exception:
        c1000 = 0

    if c400 > 0 and c1000 > 0:
        return "strong_accumulation", "400張與1000張同步增加"

    if c400 > 0 or c1000 > 0:
        return "mild_accumulation", "400張或1000張其中一項增加"

    if c400 < 0 and c1000 < 0:
        return "distribution_warning", "400張與1000張同步減少"

    return "", ""


def merge_tdcc(df: pd.DataFrame, tdcc_df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    result = df.copy()

    tdcc_cols = [
        "ticker",
        "tdcc_date",
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
        "tdcc_judgement",
        "tdcc_weeks_used",
        "tdcc_400_change_sum",
        "tdcc_1000_change_sum",
        "tdcc_400_up_weeks",
        "tdcc_1000_up_weeks",
        "tdcc_accumulation_signal",
        "tdcc_accumulation_note",
    ]

    for col in tdcc_cols:
        if col not in result.columns and col != "ticker":
            result[col] = pd.NA

    if tdcc_df.empty:
        return result

    tdcc = tdcc_df.copy()

    for col in tdcc_cols:
        if col not in tdcc.columns:
            tdcc[col] = pd.NA

    tdcc = tdcc[tdcc_cols].copy()

    merged = result.merge(tdcc, on="ticker", how="left", suffixes=("", "_tdcc"))

    for col in tdcc_cols:
        if col == "ticker":
            continue

        tdcc_col = f"{col}_tdcc"

        if tdcc_col in merged.columns:
            merged[col] = merged[tdcc_col].combine_first(merged[col])
            merged = merged.drop(columns=[tdcc_col])

    signals = merged.apply(tdcc_signal_from_row, axis=1)
    merged["tdcc_accumulation_signal"] = [item[0] for item in signals]
    merged["tdcc_accumulation_note"] = [item[1] for item in signals]

    return merged


# ============================================================
# Stock history and metrics
# ============================================================

def build_stock_history_map(price_data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    stock_map = {}

    if price_data.empty:
        return stock_map

    for ticker, group in price_data.groupby("ticker"):
        group = group.sort_values("date").copy()
        if len(group) < 60:
            continue
        stock_map[ticker] = group.reset_index(drop=True)

    return stock_map


def add_technical_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["ema23"] = df["close"].ewm(span=23, adjust=False).mean()
    df["vol20"] = df["volume"].rolling(20).mean()
    return df


def build_common_price_metrics(df: pd.DataFrame) -> dict[str, Any] | None:
    df = add_technical_metrics(df)

    if len(df) < 61:
        return None

    latest = df.iloc[-1]
    prev = df.iloc[-2]

    close = latest["close"]
    open_price = latest["open"]
    high = latest["high"]
    low = latest["low"]
    prev_close = prev["close"]
    volume = latest["volume"]
    vol20 = latest["vol20"]

    if pd.isna(close) or pd.isna(prev_close) or pd.isna(volume) or pd.isna(vol20):
        return None

    if prev_close <= 0 or vol20 <= 0:
        return None

    ma20 = latest["ma20"]
    ma60 = latest["ma60"]
    ema23 = latest["ema23"]

    if pd.isna(ma20) or pd.isna(ma60) or pd.isna(ema23):
        return None

    previous_60 = df.iloc[-61:-1].copy()
    previous_40 = df.iloc[-41:-1].copy()
    previous_20 = df.iloc[-21:-1].copy()

    high_60 = previous_60["high"].max()
    low_60 = previous_60["low"].min()
    high_40 = previous_40["high"].max()
    low_40 = previous_40["low"].min()
    high_20 = previous_20["high"].max()
    low_20 = previous_20["low"].min()

    if low_60 <= 0 or high_60 <= 0:
        return None

    return_5d = pct_change(close, df.iloc[-6]["close"]) if len(df) >= 6 else 0
    return_10d = pct_change(close, df.iloc[-11]["close"]) if len(df) >= 11 else 0
    return_20d = pct_change(close, df.iloc[-21]["close"]) if len(df) >= 21 else 0
    return_60d = pct_change(close, df.iloc[-61]["close"]) if len(df) >= 61 else 0
    return_120d = pct_change(close, df.iloc[-121]["close"]) if len(df) >= 121 else 0

    volume_ratio = volume / vol20 if vol20 > 0 else 0
    daily_return = pct_change(close, prev_close)

    return {
        "date": latest["date"],
        "available_days": len(df),
        "open": open_price,
        "high": high,
        "low": low,
        "close": close,
        "volume": volume,
        "volume_lots": volume / 1000,
        "turnover": latest.get("turnover", 0),
        "ma20": ma20,
        "ma60": ma60,
        "ema23": ema23,
        "vol20": vol20,
        "volume_ratio": volume_ratio,
        "daily_return_pct": daily_return,
        "return_5d_pct": return_5d,
        "return_10d_pct": return_10d,
        "return_20d_pct": return_20d,
        "return_60d_pct": return_60d,
        "return_120d_pct": return_120d,
        "previous_20d_high": high_20,
        "previous_20d_low": low_20,
        "previous_40d_high": high_40,
        "previous_40d_low": low_40,
        "previous_60d_high": high_60,
        "previous_60d_low": low_60,
        "distance_to_previous_40d_high_pct": pct_change(close, high_40),
        "distance_to_previous_60d_high_pct": pct_change(close, high_60),
        "gap_ma20_pct": pct_change(close, ma20),
        "gap_ma60_pct": pct_change(close, ma60),
        "gap_ema23_pct": pct_change(close, ema23),
        "off_60d_low_pct": pct_change(close, low_60),
        "off_120d_low_pct": pct_change(close, df.tail(120)["low"].min()) if len(df) >= 120 else pd.NA,
    }


# ============================================================
# Breakout / range rebound
# ============================================================

def calculate_breakout_score(df: pd.DataFrame) -> dict[str, Any] | None:
    if len(df) < MIN_HISTORY_DAYS_BREAKOUT:
        return None

    metrics = build_common_price_metrics(df)

    if metrics is None:
        return None

    close = metrics["close"]
    open_price = metrics["open"]
    high_today = metrics["high"]
    volume_lots = metrics["volume_lots"]
    volume_ratio = metrics["volume_ratio"]
    daily_return = metrics["daily_return_pct"]
    return_5d = metrics["return_5d_pct"]

    if volume_lots < MIN_VOLUME_LOTS:
        return None

    previous_60d_high = metrics["previous_60d_high"]
    previous_60d_low = metrics["previous_60d_low"]
    previous_40d_high = metrics["previous_40d_high"]
    previous_40d_low = metrics["previous_40d_low"]

    consolidation_range_pct = pct_change(previous_40d_high, previous_40d_low)
    breakout_pct = pct_change(close, previous_60d_high)
    distance_to_previous_60d_high_pct = metrics["distance_to_previous_60d_high_pct"]

    close_above_ma20 = close > metrics["ma20"]
    close_above_ma60 = close > metrics["ma60"]
    close_above_ema23 = close > metrics["ema23"]
    close_near_high = close >= high_today * 0.995 if high_today > 0 else False

    limit_up_breakout = (
        close > previous_60d_high
        and daily_return >= 9.5
        and close_near_high
    )

    true_breakout = (
        close > previous_60d_high
        and (volume_ratio >= 1.5 or limit_up_breakout)
    )

    abnormal_volume_up = (
        not true_breakout
        and close < previous_60d_high
        and volume_ratio >= 3.0
        and daily_return >= 5
        and (close_above_ma20 or close_above_ema23)
        and close > open_price
    )

    range_rebound = (
        not true_breakout
        and close < previous_60d_high
        and volume_ratio >= 1.5
        and (close_above_ma20 or close_above_ema23)
        and distance_to_previous_60d_high_pct >= -10
        and close >= open_price
    )

    near_resistance = (
        not true_breakout
        and close < previous_60d_high
        and distance_to_previous_60d_high_pct >= -5
        and volume_ratio >= 1.5
        and (close_above_ma20 or close_above_ema23)
    )

    if true_breakout:
        breakout_type = "true_breakout"
    elif abnormal_volume_up:
        breakout_type = "abnormal_volume_up"
    elif range_rebound:
        breakout_type = "range_rebound"
    elif near_resistance:
        breakout_type = "near_resistance"
    else:
        return None

    score = 0

    if consolidation_range_pct <= 18:
        score += 25
    elif consolidation_range_pct <= 25:
        score += 15

    if breakout_type == "true_breakout":
        if breakout_pct >= 5:
            score += 35
        elif breakout_pct >= 2:
            score += 32
        else:
            score += 30
    elif breakout_type == "abnormal_volume_up":
        score += 22
    else:
        score += 12

    if volume_ratio >= 3:
        score += 30
    elif volume_ratio >= 2:
        score += 25
    elif volume_ratio >= 1.5:
        score += 18

    if close_above_ma20:
        score += 10
    if close_above_ema23:
        score += 8
    if close_above_ma60:
        score += 10
    if close > open_price:
        score += 5
    if daily_return > 0:
        score += 5
    if limit_up_breakout:
        score += 8

    if breakout_type == "true_breakout":
        if return_5d > 20:
            score -= 20
        elif return_5d > 12:
            score -= 10
    else:
        if distance_to_previous_60d_high_pct >= -3:
            score += 8
        elif distance_to_previous_60d_high_pct >= -10:
            score += 5
        score = min(score, 69)

    result = {
        **metrics,
        "breakout_type": breakout_type,
        "consolidation_range_pct": consolidation_range_pct,
        "breakout_pct": breakout_pct,
        "limit_up_breakout": bool(limit_up_breakout),
        "abnormal_volume_up": bool(abnormal_volume_up),
        "score": score,
    }

    return clean_metric_output(result)


def judge_breakout(row: pd.Series) -> str:
    score = row.get("score", 0)
    if score >= 85:
        return "強突破候選"
    if score >= 70:
        return "可觀察"
    if score >= 55:
        return "初步觀察"
    return "不列入"


def clean_metric_output(metrics: dict[str, Any]) -> dict[str, Any]:
    clean = {}

    for key, value in metrics.items():
        if isinstance(value, (float, int)):
            if pd.isna(value):
                clean[key] = pd.NA
            else:
                clean[key] = round(float(value), 2)
        else:
            clean[key] = value

    return clean


def find_breakout_candidates(
    stock_map: dict[str, pd.DataFrame],
    industry_map: dict[str, dict[str, Any]],
) -> pd.DataFrame:
    rows = []

    for ticker, df in stock_map.items():
        try:
            metrics = calculate_breakout_score(df)

            if metrics is None:
                continue

            if metrics["score"] < 55:
                continue

            latest = df.iloc[-1]
            industry_info = industry_map.get(ticker, {})

            rows.append(
                {
                    "ticker": ticker,
                    "name": latest.get("name", ""),
                    "market": latest.get("market", ""),
                    "industry": industry_info.get("industry", ""),
                    "revenue_period": industry_info.get("revenue_period", ""),
                    "revenue_yoy_pct": industry_info.get("revenue_yoy_pct", pd.NA),
                    "cumulative_yoy_pct": industry_info.get("cumulative_yoy_pct", pd.NA),
                    **metrics,
                }
            )
        except Exception as exc:
            print(f"Breakout skip {ticker}: {exc}")

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_breakout, axis=1)
    result = result.sort_values(
        ["score", "volume_lots", "volume_ratio"],
        ascending=False,
    ).reset_index(drop=True)

    return result


# ============================================================
# Revenue pullback / rebound
# ============================================================

def calculate_revenue_pullback_score(df: pd.DataFrame, revenue_row: pd.Series) -> dict[str, Any] | None:
    if len(df) < MIN_HISTORY_DAYS_REVENUE:
        return None

    metrics = build_common_price_metrics(df)

    if metrics is None:
        return None

    if metrics["volume_lots"] < MIN_VOLUME_LOTS:
        return None

    revenue_yoy = revenue_row.get("revenue_yoy_pct", pd.NA)
    cumulative_yoy = revenue_row.get("cumulative_yoy_pct", pd.NA)

    if pd.isna(revenue_yoy) or pd.isna(cumulative_yoy):
        return None

    close = metrics["close"]
    open_price = metrics["open"]
    prev_close = df.iloc[-2]["close"]

    gap_ma20 = metrics["gap_ma20_pct"]
    gap_ma60 = metrics["gap_ma60_pct"]
    return_10d = metrics["return_10d_pct"]
    return_20d = metrics["return_20d_pct"]

    score = 0

    if revenue_yoy >= 50:
        score += 30
    elif revenue_yoy >= 20:
        score += 22
    elif revenue_yoy >= 10:
        score += 12

    if cumulative_yoy >= 30:
        score += 25
    elif cumulative_yoy >= 10:
        score += 18
    elif cumulative_yoy >= 5:
        score += 8

    if return_10d <= -8:
        score += 20
    elif return_10d <= -5:
        score += 14
    elif return_20d <= -8:
        score += 12

    if abs(gap_ma20) <= 5:
        score += 15
    elif abs(gap_ma60) <= 7:
        score += 15
    elif abs(gap_ma20) <= 8:
        score += 8

    if gap_ma60 < -10:
        score -= 20
    if gap_ma20 > 12:
        score -= 15

    result = {
        **metrics,
        "revenue_period": revenue_row.get("revenue_period", ""),
        "industry": revenue_row.get("industry", ""),
        "revenue_yoy_pct": revenue_yoy,
        "cumulative_yoy_pct": cumulative_yoy,
        "close_vs_prev_pct": pct_change(close, prev_close),
        "intraday_pct": pct_change(close, open_price),
        "score": score,
    }

    return clean_metric_output(result)


def judge_revenue_pullback(row: pd.Series) -> str:
    score = row.get("score", 0)
    if score >= 80:
        return "高優先觀察"
    if score >= 65:
        return "可觀察"
    if score >= 50:
        return "初步觀察"
    return "不列入"


def judge_rebound(row: pd.Series) -> str:
    volume_ratio = row.get("volume_ratio", 0)
    close_vs_prev = row.get("close_vs_prev_pct", 0)

    if volume_ratio >= 1.8 and close_vs_prev >= 3:
        return "強轉強"
    if volume_ratio >= 1.2 and close_vs_prev > 0:
        return "初步轉強"
    return "觀察"


def find_revenue_pullback_candidates(
    stock_map: dict[str, pd.DataFrame],
    revenue_df: pd.DataFrame,
) -> pd.DataFrame:
    if revenue_df.empty:
        return pd.DataFrame()

    base = revenue_df[
        (revenue_df["revenue_yoy_pct"] >= 20)
        & (revenue_df["cumulative_yoy_pct"] >= 10)
    ].copy()

    rows = []

    for _, item in base.iterrows():
        ticker = normalize_code(item.get("ticker", ""))

        if ticker not in stock_map:
            continue

        try:
            metrics = calculate_revenue_pullback_score(stock_map[ticker], item)

            if metrics is None:
                continue

            if metrics["score"] < 50:
                continue

            latest = stock_map[ticker].iloc[-1]

            rows.append(
                {
                    "ticker": ticker,
                    "name": item.get("name", latest.get("name", "")),
                    "market": item.get("market", latest.get("market", "")),
                    **metrics,
                }
            )
        except Exception as exc:
            print(f"Revenue pullback skip {ticker}: {exc}")

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    result["judge"] = result.apply(judge_revenue_pullback, axis=1)
    result = result.sort_values(
        ["score", "volume_lots", "revenue_yoy_pct"],
        ascending=False,
    ).reset_index(drop=True)

    return result


def find_pullback_rebound_candidates(revenue_pullback_df: pd.DataFrame) -> pd.DataFrame:
    if revenue_pullback_df.empty:
        return pd.DataFrame()

    df = revenue_pullback_df.copy()

    cond = (
        (pd.to_numeric(df["close_vs_prev_pct"], errors="coerce") > 0)
        & (pd.to_numeric(df["intraday_pct"], errors="coerce") >= 0)
        & (pd.to_numeric(df["volume_ratio"], errors="coerce") >= 1.2)
    )

    df = df[cond].copy()

    if df.empty:
        return df

    df["rebound_judge"] = df.apply(judge_rebound, axis=1)

    df = df.sort_values(
        ["score", "volume_ratio", "close_vs_prev_pct"],
        ascending=False,
    ).reset_index(drop=True)

    return df


# ============================================================
# Output normalization
# ============================================================

def add_standard_columns(df: pd.DataFrame, category: str, category_cn: str, breakout_type: str) -> pd.DataFrame:
    if df.empty:
        return df

    result = df.copy()

    result["category"] = category
    result["category_cn"] = category_cn

    if "breakout_type" not in result.columns:
        result["breakout_type"] = breakout_type
    else:
        result["breakout_type"] = result["breakout_type"].fillna("").replace("", breakout_type)

    result["stock_id"] = result["ticker"].map(normalize_code)
    result["stock_name"] = result["name"].map(normalize_text)

    result["price_data_warning"] = ""
    result.loc[pd.to_numeric(result.get("available_days", 999), errors="coerce") < 90, "price_data_warning"] = "available_days_below_90"

    result["note"] = result.apply(build_note, axis=1)

    return result


def build_note(row: pd.Series) -> str:
    parts = []

    breakout_type = normalize_text(row.get("breakout_type", ""))

    if breakout_type == "true_breakout":
        parts.append("嚴格突破")
    elif breakout_type == "range_rebound":
        parts.append("區間內轉強")
    elif breakout_type == "near_resistance":
        parts.append("挑戰前高")
    elif breakout_type == "abnormal_volume_up":
        parts.append("異常放量上漲")

    if not pd.isna(row.get("volume_ratio", pd.NA)):
        parts.append(f"量比{row.get('volume_ratio')}x")

    tdcc_signal = normalize_text(row.get("tdcc_accumulation_signal", ""))
    if tdcc_signal:
        parts.append(tdcc_signal)

    revenue_yoy = row.get("revenue_yoy_pct", pd.NA)
    cumulative_yoy = row.get("cumulative_yoy_pct", pd.NA)

    if not pd.isna(revenue_yoy):
        parts.append(f"月營收YoY {safe_round(revenue_yoy, 1)}%")

    if not pd.isna(cumulative_yoy):
        parts.append(f"累計YoY {safe_round(cumulative_yoy, 1)}%")

    return "；".join(parts)


def choose_output_columns(df: pd.DataFrame) -> pd.DataFrame:
    columns = [
        "date",
        "category",
        "category_cn",
        "breakout_type",
        "ticker",
        "stock_id",
        "name",
        "stock_name",
        "market",
        "industry",
        "score",
        "judge",
        "rebound_judge",
        "revenue_period",
        "revenue_yoy_pct",
        "cumulative_yoy_pct",
        "close",
        "open",
        "high",
        "low",
        "volume",
        "volume_lots",
        "volume_ratio",
        "ma20",
        "ma60",
        "ema23",
        "gap_ma20_pct",
        "gap_ma60_pct",
        "gap_ema23_pct",
        "return_5d_pct",
        "return_10d_pct",
        "return_20d_pct",
        "return_60d_pct",
        "return_120d_pct",
        "previous_20d_high",
        "previous_20d_low",
        "previous_40d_high",
        "previous_40d_low",
        "previous_60d_high",
        "previous_60d_low",
        "distance_to_previous_40d_high_pct",
        "distance_to_previous_60d_high_pct",
        "consolidation_range_pct",
        "breakout_pct",
        "limit_up_breakout",
        "abnormal_volume_up",
        "available_days",
        "price_data_warning",
        "tdcc_date",
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
        "tdcc_judgement",
        "tdcc_weeks_used",
        "tdcc_400_change_sum",
        "tdcc_1000_change_sum",
        "tdcc_400_up_weeks",
        "tdcc_1000_up_weeks",
        "tdcc_accumulation_signal",
        "tdcc_accumulation_note",
        "note",
    ]

    result = df.copy()

    for col in columns:
        if col not in result.columns:
            result[col] = pd.NA

    return result[columns].copy()


# ============================================================
# Markdown report
# ============================================================

def render_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    lines = []

    if df.empty:
        lines.append("無符合條件資料。")
        return lines

    part = df.head(limit).copy()

    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")

    for _, row in part.iterrows():
        values = []
        for col in columns:
            value = row.get(col, "")
            if pd.isna(value):
                value = ""
            values.append(str(value))
        lines.append("| " + " | ".join(values) + " |")

    return lines


def write_stock_monitor_report(
    *,
    price_data: pd.DataFrame,
    breakout_df: pd.DataFrame,
    range_df: pd.DataFrame,
    revenue_df: pd.DataFrame,
    rebound_df: pd.DataFrame,
) -> None:
    latest_price_date = price_data["date"].max() if not price_data.empty else ""
    official_fetch_date = get_official_fetch_saved_date()

    lines = []

    lines.append("# 每日全市場股價監測報告")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 主資料日期：`{latest_price_date}`")
    lines.append(f"- 最新官方價格資料日：`{official_fetch_date}`")
    lines.append(f"- 價格資料筆數：`{len(price_data)}`")
    lines.append("")
    lines.append("## 今日分類摘要")
    lines.append("")
    lines.append("| 分類 | 檔數 |")
    lines.append("|---|---:|")
    lines.append(f"| 嚴格突破 | {len(breakout_df)} |")
    lines.append(f"| 區間內轉強 / 挑戰前高觀察 | {len(range_df)} |")
    lines.append(f"| 營收成長股價回檔 | {len(revenue_df)} |")
    lines.append(f"| 回檔後短線轉強 | {len(rebound_df)} |")
    lines.append("")
    lines.append("## 嚴格突破")
    lines.append("")
    lines.extend(
        render_table(
            breakout_df,
            ["ticker", "name", "industry", "score", "breakout_type", "close", "volume_ratio", "tdcc_accumulation_signal", "note"],
            limit=30,
        )
    )
    lines.append("")
    lines.append("## 區間內轉強 / 挑戰前高觀察")
    lines.append("")
    lines.extend(
        render_table(
            range_df,
            ["ticker", "name", "industry", "score", "breakout_type", "close", "volume_ratio", "distance_to_previous_60d_high_pct", "tdcc_accumulation_signal", "note"],
            limit=30,
        )
    )
    lines.append("")
    lines.append("## 營收成長股價回檔")
    lines.append("")
    lines.extend(
        render_table(
            revenue_df,
            ["ticker", "name", "industry", "score", "revenue_yoy_pct", "cumulative_yoy_pct", "close", "gap_ma20_pct", "gap_ma60_pct", "tdcc_accumulation_signal", "note"],
            limit=30,
        )
    )
    lines.append("")
    lines.append("## 回檔後短線轉強")
    lines.append("")
    lines.extend(
        render_table(
            rebound_df,
            ["ticker", "name", "industry", "score", "rebound_judge", "close_vs_prev_pct", "volume_ratio", "tdcc_accumulation_signal", "note"],
            limit=30,
        )
    )
    lines.append("")
    lines.append("## 資料說明")
    lines.append("")
    lines.append("- 本報告使用 `output/latest/official_daily_price_latest.csv` 與 `data/daily_price/` 歷史資料。")
    lines.append("- `stock_monitor_latest.md` 的主資料日期應與最新官方價格資料日一致。")
    lines.append("- `range_rebound` / `near_resistance` / `abnormal_volume_up` 不混入嚴格突破。")
    lines.append("- TDCC 僅作背景確認，不作硬篩選。")
    lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


# ============================================================
# Main
# ============================================================

def main() -> int:
    price_data = load_official_price_history()

    if price_data.empty:
        REPORT_PATH.write_text(
            "# 每日全市場股價監測報告\n\n無官方價格資料，無法產出監測報告。\n",
            encoding="utf-8",
        )
        for path in [BREAKOUT_CSV_PATH, RANGE_REBOUND_CSV_PATH, REVENUE_PULLBACK_CSV_PATH, PULLBACK_REBOUND_CSV_PATH]:
            pd.DataFrame().to_csv(path, index=False, encoding="utf-8-sig")
        return 0

    latest_price_date = price_data["date"].max()
    official_fetch_date = get_official_fetch_saved_date()

    print(f"Stock monitor latest_price_date={latest_price_date}")
    print(f"Official fetch saved date={official_fetch_date}")

    revenue_raw = fetch_monthly_revenue()
    industry_map = build_industry_map(revenue_raw)

    stock_map = build_stock_history_map(price_data)
    tdcc_df = load_tdcc_latest()

    breakout_all = find_breakout_candidates(stock_map, industry_map)

    if breakout_all.empty:
        breakout_df = pd.DataFrame()
        range_df = pd.DataFrame()
    else:
        breakout_df = breakout_all[breakout_all["breakout_type"] == "true_breakout"].copy()
        range_df = breakout_all[
            breakout_all["breakout_type"].isin(["range_rebound", "near_resistance", "abnormal_volume_up"])
        ].copy()

    revenue_df = find_revenue_pullback_candidates(stock_map, revenue_raw)
    rebound_df = find_pullback_rebound_candidates(revenue_df)

    breakout_df = add_standard_columns(
        merge_tdcc(breakout_df, tdcc_df),
        category="true_breakout",
        category_cn="嚴格突破",
        breakout_type="true_breakout",
    )

    range_df = add_standard_columns(
        merge_tdcc(range_df, tdcc_df),
        category="range_rebound",
        category_cn="區間內轉強 / 挑戰前高觀察",
        breakout_type="range_rebound",
    )

    revenue_df = add_standard_columns(
        merge_tdcc(revenue_df, tdcc_df),
        category="revenue_pullback",
        category_cn="營收成長股價回檔",
        breakout_type="revenue_pullback",
    )

    rebound_df = add_standard_columns(
        merge_tdcc(rebound_df, tdcc_df),
        category="pullback_rebound",
        category_cn="回檔後短線轉強",
        breakout_type="pullback_rebound",
    )

    breakout_out = choose_output_columns(breakout_df)
    range_out = choose_output_columns(range_df)
    revenue_out = choose_output_columns(revenue_df)
    rebound_out = choose_output_columns(rebound_df)

    breakout_out.to_csv(BREAKOUT_CSV_PATH, index=False, encoding="utf-8-sig")
    range_out.to_csv(RANGE_REBOUND_CSV_PATH, index=False, encoding="utf-8-sig")
    revenue_out.to_csv(REVENUE_PULLBACK_CSV_PATH, index=False, encoding="utf-8-sig")
    rebound_out.to_csv(PULLBACK_REBOUND_CSV_PATH, index=False, encoding="utf-8-sig")

    write_stock_monitor_report(
        price_data=price_data,
        breakout_df=breakout_out,
        range_df=range_out,
        revenue_df=revenue_out,
        rebound_df=rebound_out,
    )

    print(f"Saved: {REPORT_PATH}")
    print(f"Saved: {BREAKOUT_CSV_PATH}, rows={len(breakout_out)}")
    print(f"Saved: {RANGE_REBOUND_CSV_PATH}, rows={len(range_out)}")
    print(f"Saved: {REVENUE_PULLBACK_CSV_PATH}, rows={len(revenue_out)}")
    print(f"Saved: {PULLBACK_REBOUND_CSV_PATH}, rows={len(rebound_out)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
