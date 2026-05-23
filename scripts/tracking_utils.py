from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import math
import re
from typing import Any

import pandas as pd
import requests


REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
DATA_DIR = Path("data")
HISTORY_DIR = Path("output/history")
DAILY_SIGNALS_DIR = HISTORY_DIR / "daily_signals"
TDCC_SIGNALS_DIR = HISTORY_DIR / "tdcc_signals"
DAILY_PRICE_DIR = DATA_DIR / "daily_price"
STOCK_PRICE_HISTORY_DIR = DATA_DIR / "stock_price_history"
MARKET_INDEX_PATH = DATA_DIR / "market_index_history.csv"

HORIZONS = [1, 2, 5, 10, 20]


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    if len(digits) == 7 and digits.startswith("1"):
        year = int(digits[:3]) + 1911
        return f"{year:04d}{digits[3:]}"
    return ""


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = re.sub(r"[^0-9]", "", text)
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def to_number(value: Any, default: float = math.nan) -> float:
    text = safe_str(value)
    text = text.replace(",", "").replace("%", "").replace("+", "").replace("--", "")
    if text in {"", "-"}:
        return default
    try:
        return float(text)
    except Exception:
        return default


def pct_return(current: Any, base: Any) -> float:
    current_num = to_number(current)
    base_num = to_number(base)
    if math.isnan(current_num) or math.isnan(base_num) or base_num == 0:
        return math.nan
    return (current_num / base_num - 1) * 100


def fmt_pct(value: Any) -> str:
    num = to_number(value)
    if math.isnan(num):
        return "-"
    return f"{num:+.2f}%"


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


def raw_url(path: str | Path) -> str:
    return f"{RAW_PREFIX}/{Path(path).as_posix()}"


def pages_url(path: str | Path) -> str:
    p = Path(path)
    text = p.as_posix()
    if text.startswith("docs/"):
        text = p.relative_to("docs").as_posix()
    elif text.startswith("output/latest/"):
        text = p.relative_to("output").as_posix()
    return f"{PAGES_PREFIX}/{text}"


def read_csv(path: str | Path, **kwargs: Any) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(p, **kwargs)
    except Exception as exc:
        print(f"WARNING: failed to read {p}: {exc}")
        return pd.DataFrame()


def write_csv(df: pd.DataFrame, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False, encoding="utf-8-sig")


def append_update_csv(
    new_df: pd.DataFrame,
    path: str | Path,
    key_cols: list[str],
    sort_cols: list[str] | None = None,
) -> pd.DataFrame:
    old = read_csv(path, dtype=str)
    if old.empty:
        combined = new_df.copy()
    else:
        combined = pd.concat([old, new_df], ignore_index=True, sort=False)
    for col in key_cols:
        if col not in combined.columns:
            combined[col] = ""
    combined = combined.drop_duplicates(subset=key_cols, keep="last")
    if sort_cols:
        existing = [col for col in sort_cols if col in combined.columns]
        if existing:
            combined = combined.sort_values(existing).reset_index(drop=True)
    write_csv(combined, path)
    return combined


def latest_price_date() -> str:
    dates: list[str] = []
    freshness = read_csv(LATEST_DIR / "data_freshness_latest.csv", dtype=str)
    if not freshness.empty and "main_price_date" in freshness.columns:
        date = normalize_date(freshness.iloc[0].get("main_price_date", ""))
        if date:
            return date
    for path in DAILY_PRICE_DIR.glob("*.csv"):
        date = normalize_date(path.stem)
        if date:
            dates.append(date)
    return max(dates) if dates else now_taipei().strftime("%Y%m%d")


def main_price_date_from_freshness() -> str:
    freshness = read_csv(LATEST_DIR / "data_freshness_latest.csv", dtype=str)
    if not freshness.empty:
        for col in ["main_price_date", "all_candidates_date", "official_price_fetch_date"]:
            if col in freshness.columns:
                date = normalize_date(freshness.iloc[0].get(col, ""))
                if date:
                    return date
    return latest_price_date()


def load_price_history(stock_id: Any) -> pd.DataFrame:
    stock_id = normalize_code(stock_id)
    if not stock_id:
        return pd.DataFrame()
    path = STOCK_PRICE_HISTORY_DIR / f"{stock_id}.csv"
    df = read_csv(path, dtype=str)
    if df.empty or "date" not in df.columns:
        return pd.DataFrame()
    if "stock_id" not in df.columns:
        df["stock_id"] = stock_id
    if "market" not in df.columns:
        df["market"] = ""
    df["date"] = df["date"].map(normalize_date)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    for col in [
        "open", "high", "low", "close", "volume", "ma5", "ma10", "ma20",
        "ma60", "ma120", "ema23", "volume_ma20", "volume_ratio",
        "high_20", "high_60", "high_120", "low_20", "low_60", "low_120",
    ]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    df = df.dropna(subset=["date", "close"]).sort_values("date").drop_duplicates("date", keep="last")
    return df.reset_index(drop=True)


def position_on_or_before(df: pd.DataFrame, date: str) -> int | None:
    if df.empty or "date" not in df.columns:
        return None
    date = normalize_date(date)
    subset = df[df["date"] <= date]
    if subset.empty:
        return None
    return int(subset.index[-1])


def stock_return_after(stock_id: Any, signal_date: str, horizon: int) -> tuple[float, float, float, float, int]:
    price = load_price_history(stock_id)
    pos = position_on_or_before(price, signal_date)
    if pos is None:
        return math.nan, math.nan, math.nan, math.nan, 0
    signal_close = to_number(price.loc[pos, "close"])
    available = max(0, len(price) - pos - 1)
    if math.isnan(signal_close) or signal_close <= 0:
        return signal_close, math.nan, math.nan, math.nan, available
    close_h = math.nan
    ret = math.nan
    if pos + horizon < len(price):
        close_h = to_number(price.loc[pos + horizon, "close"])
        ret = pct_return(close_h, signal_close)
    window = price.iloc[pos + 1 : min(len(price), pos + horizon + 1)]
    mfe = pct_return(window["high"].max(), signal_close) if not window.empty and "high" in window.columns else math.nan
    mae = pct_return(window["low"].min(), signal_close) if not window.empty and "low" in window.columns else math.nan
    return close_h, ret, mfe, mae, available


def roc_month_from_yyyymmdd(date_str: str) -> str:
    date_str = normalize_date(date_str) or now_taipei().strftime("%Y%m%d")
    return f"{int(date_str[:4]) - 1911:03d}/{date_str[4:6]}"


def month_starts_back(latest_date: str, months: int = 18) -> list[str]:
    latest_date = normalize_date(latest_date) or now_taipei().strftime("%Y%m%d")
    year = int(latest_date[:4])
    month = int(latest_date[4:6])
    out: list[str] = []
    for _ in range(months):
        out.append(f"{year:04d}{month:02d}01")
        month -= 1
        if month == 0:
            year -= 1
            month = 12
    return sorted(out)


def fetch_twse_index_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date={month_start}&response=json"
    try:
        data = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"}).json()
    except Exception as exc:
        print(f"WARNING: TWSE index fetch failed {month_start}: {exc}")
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for item in data.get("data", []) or []:
        if len(item) < 5:
            continue
        parts = re.findall(r"\d+", safe_str(item[0]))
        if len(parts) >= 3 and len(parts[0]) <= 3:
            date = f"{int(parts[0]) + 1911:04d}{int(parts[1]):02d}{int(parts[2]):02d}"
        else:
            date = normalize_date(item[0])
        rows.append({"date": date, "index_code": "TWSE", "index_name": "TAIEX", "close": to_number(item[4]), "source": url})
    return pd.DataFrame(rows)


def fetch_tpex_index_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.tpex.org.tw/www/zh-tw/indexInfo/inx?date={roc_month_from_yyyymmdd(month_start)}&response=json"
    try:
        data = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"}).json()
    except Exception as exc:
        print(f"WARNING: TPEx index fetch failed {month_start}: {exc}")
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for table in data.get("tables", []) or []:
        for item in table.get("data", []) or []:
            if len(item) < 5:
                continue
            rows.append({"date": normalize_date(item[0]), "index_code": "TPEX", "index_name": "TPEx", "close": to_number(item[4]), "source": url})
    return pd.DataFrame(rows)


def update_market_index_history(months: int = 18) -> pd.DataFrame:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    latest = latest_price_date()
    frames: list[pd.DataFrame] = []
    old = read_csv(MARKET_INDEX_PATH, dtype=str)
    if not old.empty:
        frames.append(old)
    for month_start in month_starts_back(latest, months):
        frames.append(fetch_twse_index_month(month_start))
        frames.append(fetch_tpex_index_month(month_start))
    frames = [df for df in frames if not df.empty]
    if not frames:
        return pd.DataFrame()
    df = pd.concat(frames, ignore_index=True, sort=False)
    df["date"] = df["date"].map(normalize_date)
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df = df.dropna(subset=["date", "index_code", "close"])
    df = df.drop_duplicates(["date", "index_code"], keep="last")
    df = df.sort_values(["index_code", "date"]).reset_index(drop=True)
    for _, part in df.groupby("index_code"):
        part = part.sort_values("date")
        for window in [5, 10, 20, 60]:
            df.loc[part.index, f"return_{window}d"] = part["close"].pct_change(window) * 100
        df.loc[part.index, "ma20"] = part["close"].rolling(20).mean()
        df.loc[part.index, "ma60"] = part["close"].rolling(60).mean()
        df.loc[part.index, "above_ma20"] = part["close"] >= part["close"].rolling(20).mean()
        df.loc[part.index, "above_ma60"] = part["close"] >= part["close"].rolling(60).mean()
    write_csv(df, MARKET_INDEX_PATH)
    latest_rows = df.groupby("index_code", as_index=False).tail(1)
    write_csv(latest_rows, LATEST_DIR / "market_benchmark_latest.csv")
    return df


def load_market_index_history(update_if_missing: bool = True) -> pd.DataFrame:
    df = read_csv(MARKET_INDEX_PATH, dtype=str)
    if df.empty and update_if_missing:
        df = update_market_index_history()
    if df.empty:
        return df
    df["date"] = df["date"].map(normalize_date)
    for col in ["close", "ma20", "ma60", "return_5d", "return_10d", "return_20d", "return_60d"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    for col in ["above_ma20", "above_ma60"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().isin(["true", "1", "yes"])
    return df.sort_values(["index_code", "date"]).reset_index(drop=True)


def market_row_on_or_before(index_df: pd.DataFrame, index_code: str, date: str) -> pd.Series | None:
    if index_df.empty:
        return None
    date = normalize_date(date)
    part = index_df[(index_df["index_code"] == index_code) & (index_df["date"] <= date)].copy()
    if part.empty:
        return None
    return part.sort_values("date").iloc[-1]


def market_return_after(index_df: pd.DataFrame, index_code: str, signal_date: str, horizon: int) -> tuple[float, float]:
    if index_df.empty:
        return math.nan, math.nan
    part = index_df[index_df["index_code"] == index_code].sort_values("date").reset_index(drop=True)
    base_candidates = part[part["date"] <= normalize_date(signal_date)]
    if base_candidates.empty:
        return math.nan, math.nan
    base_idx = int(base_candidates.index[-1])
    if base_idx + horizon >= len(part):
        return math.nan, math.nan
    base_close = to_number(part.loc[base_idx, "close"])
    close_h = to_number(part.loc[base_idx + horizon, "close"])
    return close_h, pct_return(close_h, base_close)


def classify_market_regime(row: pd.Series | None) -> str:
    if row is None:
        return "unknown"
    close = to_number(row.get("close"))
    ma20 = to_number(row.get("ma20"))
    ma60 = to_number(row.get("ma60"))
    ret20 = to_number(row.get("return_20d"))
    above20 = bool(row.get("above_ma20")) if "above_ma20" in row else (not math.isnan(ma20) and close >= ma20)
    above60 = bool(row.get("above_ma60")) if "above_ma60" in row else (not math.isnan(ma60) and close >= ma60)
    if not math.isnan(ma60) and close < ma60 and not math.isnan(ret20) and ret20 < 0:
        return "high_risk"
    if (not above20) or (not math.isnan(ret20) and ret20 <= -3):
        return "correction"
    if above20 and above60 and not math.isnan(ret20) and ret20 >= 5:
        return "strong_bull"
    if above20 and above60:
        return "mild_bull"
    return "range_bound"


def infer_benchmark_index(market: Any) -> str:
    text = safe_str(market).upper()
    if "TPEX" in text or "OTC" in text or "上櫃" in text:
        return "TPEX"
    if "TWSE" in text or "上市" in text:
        return "TWSE"
    return "unknown"


CONSTRUCTION_KEYWORDS = [
    "建材營造", "營建", "不動產", "建設", "工程", "營造", "建案", "待售房地", "合約負債", "在建工程",
]


def is_construction_like(row: pd.Series) -> bool:
    fields = ["industry", "sector", "sub_theme", "細分族群", "theme_group", "concept_tags", "stock_name", "name"]
    text = " ".join(safe_str(row.get(col, "")) for col in fields)
    return any(keyword in text for keyword in CONSTRUCTION_KEYWORDS)


def recognition_type(row: pd.Series) -> str:
    text = " ".join(safe_str(row.get(col, "")) for col in ["industry", "細分族群", "theme_group", "stock_name", "name"])
    if any(key in text for key in ["不動產", "建設", "建案", "待售房地"]):
        return "交屋認列型"
    if any(key in text for key in ["建材營造", "營建", "營造", "工程"]):
        return "營建認列型"
    return "需基本面確認"


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int | None = None) -> str:
    if df.empty:
        return "目前沒有可用資料。"
    show = df.copy()
    if limit is not None:
        show = show.head(limit)
    cols = [col for col in columns if col in show.columns]
    if not cols:
        return "目前沒有可用欄位。"
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in show.iterrows():
        values = [safe_str(row.get(col, "")).replace("|", "/").replace("\n", " ") for col in cols]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)
