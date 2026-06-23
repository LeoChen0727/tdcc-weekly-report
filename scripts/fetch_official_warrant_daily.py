from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import argparse
import io
import json
import os
import re
import time
from typing import Any

import pandas as pd
import requests


OUTPUT_DIR = Path("output/latest")
DEBUG_DIR = Path("output/debug")
HISTORY_DIR = Path("output/history/warrant_daily")

RAW_LATEST = OUTPUT_DIR / "warrant_daily_raw_latest.csv"
FETCH_STATUS_MD = OUTPUT_DIR / "warrant_daily_fetch_latest.md"
DEBUG_MD = DEBUG_DIR / "warrant_fetch_debug_latest.md"
DEBUG_CSV = DEBUG_DIR / "warrant_fetch_debug_latest.csv"

REQUEST_TIMEOUT_SECONDS = float(os.getenv("OFFICIAL_WARRANT_REQUEST_TIMEOUT", "8"))
FETCH_MAX_SECONDS = float(os.getenv("OFFICIAL_WARRANT_FETCH_MAX_SECONDS", "360"))

PRICE_DIR = Path("data/daily_price")


RAW_COLUMNS = [
    "date",
    "market",
    "source_name",
    "source_url",

    "warrant_id",
    "warrant_name",

    "stock_id",
    "stock_name",

    "call_put_raw",
    "call_put",

    "volume",
    "turnover",
    "close",

    "issuer",

    "issued_quantity",
    "cancelled_quantity",
    "latest_warrant_count",
    "float_quantity",
]


def deadline_remaining(deadline: float | None) -> float | None:
    if deadline is None:
        return None
    return max(0.0, deadline - time.monotonic())


def deadline_expired(deadline: float | None) -> bool:
    remaining = deadline_remaining(deadline)
    return remaining is not None and remaining <= 0


def request_timeout(deadline: float | None) -> float:
    remaining = deadline_remaining(deadline)
    if remaining is None:
        return REQUEST_TIMEOUT_SECONDS
    return max(1.0, min(REQUEST_TIMEOUT_SECONDS, remaining))


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def today_taipei_yyyymmdd() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    match = re.search(r"(\d{4})", text)

    if match:
        return match.group(1)

    return ""


def normalize_warrant_id(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip().upper()
    text = text.replace(" ", "")
    text = text.replace("\u3000", "")

    # 權證代號常見：
    # 認購：030001～089999，6 碼數字
    # 認售：03001P / 03001U / 03001T
    # 國外標的 / 牛熊證：F/Q/C/B/X/Y
    match = re.search(r"([0-9]{5,6}[A-Z]?)", text)

    if match:
        return match.group(1)

    return text


def is_warrant_id(value: str) -> bool:
    text = normalize_warrant_id(value)

    if re.fullmatch(r"[0-9]{6}", text):
        try:
            number = int(text)
            return 30001 <= number <= 89999 or 300001 <= number <= 899999
        except Exception:
            return False

    if re.fullmatch(r"[0-9]{5}[PUTFQCBXY]", text):
        return True

    return False


def to_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")

    if text in ["", "-", "nan", "None", "NaN"]:
        return pd.NA

    return pd.to_numeric(text, errors="coerce")


def get_latest_price_date() -> str:
    latest_date = ""

    for path in sorted(PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(path, dtype={"date": str}, usecols=lambda c: c in ["date"])
        except Exception:
            continue

        if "date" not in df.columns or df.empty:
            continue

        dates = (
            df["date"]
            .astype(str)
            .str.replace(r"[^0-9]", "", regex=True)
            .dropna()
        )

        if not dates.empty:
            candidate = dates.max()

            if len(candidate) == 8 and candidate > latest_date:
                latest_date = candidate

    return latest_date or today_taipei_yyyymmdd()


def recent_date_candidates(date_str: str, lookback_days: int = 10) -> list[str]:
    try:
        start = datetime.strptime(date_str, "%Y%m%d")
    except ValueError:
        return [date_str]

    return [
        (start - timedelta(days=offset)).strftime("%Y%m%d")
        for offset in range(0, lookback_days + 1)
    ]


def has_usable_quote_rows(df: pd.DataFrame) -> bool:
    if df.empty:
        return False

    for col in ["turnover", "volume", "close"]:
        if col not in df.columns:
            continue

        values = pd.to_numeric(df[col], errors="coerce").fillna(0)

        if (values > 0).any():
            return True

    return False


def normalize_date_value(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def normalize_raw_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    for col in RAW_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA

    out = out[RAW_COLUMNS].copy()
    out["date"] = out["date"].map(normalize_date_value)
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out["warrant_id"] = out["warrant_id"].map(normalize_warrant_id)

    for col in [
        "volume",
        "turnover",
        "close",
        "issued_quantity",
        "cancelled_quantity",
        "latest_warrant_count",
        "float_quantity",
    ]:
        out[col] = out[col].map(to_number)

    out = out[out["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()
    out = out[out["warrant_id"].astype(str).str.len().gt(0)].copy()
    return out.reset_index(drop=True)


def read_usable_raw_snapshot(path: Path, date_candidates: list[str]) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame(columns=RAW_COLUMNS)

    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        return pd.DataFrame(columns=RAW_COLUMNS)

    if df.empty:
        return pd.DataFrame(columns=RAW_COLUMNS)

    out = normalize_raw_snapshot(df)
    dates = {normalize_date_value(value) for value in date_candidates}
    dates = {date for date in dates if date}

    if dates and "date" in out.columns:
        out = out[out["date"].isin(dates)].copy()

    if out.empty or not has_usable_quote_rows(out):
        return pd.DataFrame(columns=RAW_COLUMNS)

    return out[RAW_COLUMNS].copy()


def raw_fallback_candidates(date_str: str, requested_date: str) -> list[Path]:
    dates = []

    for value in [date_str, requested_date]:
        normalized = normalize_date_value(value)

        if normalized and normalized not in dates:
            dates.append(normalized)

    paths: list[Path] = [RAW_LATEST]

    for date in dates:
        paths.append(HISTORY_DIR / f"warrant_daily_{date}.csv")

    unique_paths: list[Path] = []

    for path in paths:
        if path not in unique_paths:
            unique_paths.append(path)

    return unique_paths


def find_existing_raw_fallback(date_str: str, requested_date: str) -> tuple[Path | None, pd.DataFrame, str]:
    date_candidates = [date_str, requested_date]

    for path in raw_fallback_candidates(date_str, requested_date):
        fallback = read_usable_raw_snapshot(path, date_candidates)

        if fallback.empty:
            continue

        fallback_date = ""

        if "date" in fallback.columns:
            dates = sorted({normalize_date_value(value) for value in fallback["date"] if normalize_date_value(value)})
            fallback_date = dates[-1] if dates else ""

        return path, fallback, fallback_date or normalize_date_value(date_str) or normalize_date_value(requested_date)

    return None, pd.DataFrame(columns=RAW_COLUMNS), ""


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [
        str(c)
        .replace("\ufeff", "")
        .replace("\u3000", "")
        .replace("\n", "")
        .replace("\r", "")
        .strip()
        for c in df.columns
    ]
    return df


def dataframe_from_json_payload(payload: Any) -> list[pd.DataFrame]:
    frames: list[pd.DataFrame] = []

    if isinstance(payload, dict):
        fields = payload.get("fields") or payload.get("headers") or payload.get("columns")
        data = payload.get("data") or payload.get("aaData") or payload.get("rows")

        if isinstance(fields, list) and isinstance(data, list) and len(data) > 0:
            try:
                frames.append(clean_columns(pd.DataFrame(data, columns=fields)))
            except Exception:
                pass

        tables = payload.get("tables")

        if isinstance(tables, list):
            for table in tables:
                frames.extend(dataframe_from_json_payload(table))

        for key, value in payload.items():
            if key in ["tables", "data", "fields", "headers", "columns", "rows", "aaData"]:
                continue

            if isinstance(value, (dict, list)):
                frames.extend(dataframe_from_json_payload(value))

    elif isinstance(payload, list):
        if len(payload) > 0 and isinstance(payload[0], dict):
            try:
                frames.append(clean_columns(pd.DataFrame(payload)))
            except Exception:
                pass
        else:
            for item in payload:
                if isinstance(item, (dict, list)):
                    frames.extend(dataframe_from_json_payload(item))

    return frames


def read_tables_from_text(text: str) -> list[pd.DataFrame]:
    frames: list[pd.DataFrame] = []

    if not text or len(text.strip()) < 10:
        return frames

    cleaned = text.replace("\ufeff", "").strip()

    if cleaned.startswith("{") or cleaned.startswith("["):
        try:
            payload = json.loads(cleaned)
            json_frames = dataframe_from_json_payload(payload)

            if json_frames:
                return json_frames
        except Exception:
            pass

    lines = cleaned.splitlines()

    header_candidates = []

    for idx, line in enumerate(lines[:100]):
        normalized = line.replace(" ", "").replace("\u3000", "")

        if "," in line and any(
            key in normalized
            for key in [
                "權證代號",
                "證券代號",
                "權證名稱",
                "證券名稱",
                "標的",
                "成交股數",
                "成交金額",
                "收盤價",
            ]
        ):
            header_candidates.append(idx)

    if not header_candidates:
        header_candidates = [0]

    for header_index in header_candidates:
        csv_text = "\n".join(lines[header_index:])

        try:
            df = pd.read_csv(io.StringIO(csv_text), dtype=str)
            df = clean_columns(df)

            if not df.empty and len(df.columns) >= 3:
                frames.append(df)
        except Exception:
            continue

    return frames


def fetch_source(
    url: str,
    source_name: str,
    referer: str = "https://www.twse.com.tw/",
    deadline: float | None = None,
) -> tuple[list[pd.DataFrame], str]:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": referer,
    }

    if deadline_expired(deadline):
        return [], f"deadline_exceeded before_request source={source_name}, url={url}"

    try:
        response = requests.get(url, headers=headers, timeout=request_timeout(deadline))
        response.encoding = response.apparent_encoding or response.encoding or "utf-8"

        frames = read_tables_from_text(response.text)

        if not frames and "<table" in response.text.lower():
            try:
                html_frames = pd.read_html(response.text)
                frames.extend([clean_columns(x.astype(str)) for x in html_frames if not x.empty])
            except Exception:
                pass

        if frames:
            return frames, f"ok source={source_name}, status={response.status_code}, tables={len(frames)}, url={url}"

        return [], f"empty_or_unparsed source={source_name}, status={response.status_code}, chars={len(response.text)}, url={url}"

    except Exception as exc:
        return [], f"failed source={source_name}, error={exc}, url={url}"


def pick_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    cols = list(df.columns)

    normalized_map = {
        col: str(col)
        .replace(" ", "")
        .replace("\u3000", "")
        .replace("\n", "")
        .replace("\r", "")
        .replace("(", "")
        .replace(")", "")
        .replace("（", "")
        .replace("）", "")
        .strip()
        for col in cols
    }

    for candidate in candidates:
        candidate_norm = (
            candidate
            .replace(" ", "")
            .replace("\u3000", "")
            .replace("\n", "")
            .replace("\r", "")
            .replace("(", "")
            .replace(")", "")
            .replace("（", "")
            .replace("）", "")
            .strip()
        )

        for col, col_norm in normalized_map.items():
            if col_norm == candidate_norm:
                return col

    for candidate in candidates:
        candidate_norm = (
            candidate
            .replace(" ", "")
            .replace("\u3000", "")
            .replace("\n", "")
            .replace("\r", "")
            .replace("(", "")
            .replace(")", "")
            .replace("（", "")
            .replace("）", "")
            .strip()
        )

        for col, col_norm in normalized_map.items():
            if candidate_norm in col_norm:
                return col

    return None


def classify_call_put_from_type(value: str) -> str:
    text = str(value).lower()

    if any(key in text for key in ["認售", "售", "put"]):
        return "put"

    if any(key in text for key in ["認購", "購", "call"]):
        return "call"

    return "unknown"


def classify_call_put_from_warrant_id(warrant_id: str) -> str:
    wid = normalize_warrant_id(warrant_id)

    if re.fullmatch(r"[0-9]{6}", wid):
        return "call"

    if re.fullmatch(r"[0-9]{5}[PUTQ]", wid):
        return "put"

    if re.fullmatch(r"[0-9]{5}[F]", wid):
        return "call"

    if re.fullmatch(r"[0-9]{5}[CBX]", wid):
        return "call"

    if re.fullmatch(r"[0-9]{5}[BY]", wid):
        return "put"

    return "unknown"


def infer_issuer_from_name(warrant_name: str) -> str:
    text = str(warrant_name)

    issuers = [
        "元大",
        "凱基",
        "群益",
        "富邦",
        "國泰",
        "永豐",
        "元富",
        "統一",
        "兆豐",
        "玉山",
        "台新",
        "中信",
        "第一",
        "華南",
        "康和",
        "國票",
        "宏遠",
        "永全",
        "元展",
        "土銀",
        "合庫",
        "日盛",
        "上海",
        "匯豐",
        "摩根",
        "美林",
        "瑞銀",
        "法興",
    ]

    for issuer in issuers:
        if issuer in text:
            return issuer

    return ""


def standardize_warrant_mapping_table(
    df: pd.DataFrame,
    market: str,
    source_name: str,
    source_url: str,
) -> pd.DataFrame:
    """
    來源：TWSE warrantStock。
    用途：建立 權證代號 -> 標的股票 / 權證類型 / 權證名稱 對照。
    這個來源通常沒有成交股數與成交金額。
    """
    if df.empty:
        return pd.DataFrame()

    df = clean_columns(df)

    warrant_id_col = pick_column(df, [
        "權證代號",
        "證券代號",
        "權證證券代號",
        "權證代碼",
        "代號",
    ])

    warrant_name_col = pick_column(df, [
        "權證簡稱",
        "權證名稱",
        "證券名稱",
        "權證證券名稱",
        "名稱",
    ])

    stock_id_col = pick_column(df, [
        "標的代號",
        "標的證券代號",
        "標的股票代號",
        "連結標的代號",
        "標的金融商品代號",
    ])

    stock_name_col = pick_column(df, [
        "標的名稱",
        "標的證券名稱",
        "標的股票名稱",
        "連結標的名稱",
        "標的金融商品名稱",
    ])

    call_put_col = pick_column(df, [
        "權證類型",
        "認購售",
        "認購/售",
        "認購售別",
        "種類",
        "購售",
    ])

    issued_col = pick_column(df, [
        "發行數量",
        "發行單位總數",
        "發行張數",
        "發行量",
    ])

    cancelled_col = pick_column(df, [
        "累計註銷",
        "註銷量",
        "註銷單位",
        "註銷數量",
    ])

    latest_count_col = pick_column(df, [
        "最新權證數量",
        "最新流通量",
        "流通在外單位",
        "流通量",
        "權證流通在外數量",
    ])

    float_col = pick_column(df, [
        "流通量",
        "最新流通量",
        "流通在外單位",
        "流通在外數量",
        "權證流通在外數量",
    ])

    if not warrant_id_col:
        return pd.DataFrame()

    out = pd.DataFrame()
    out["market"] = market
    out["source_name"] = source_name
    out["source_url"] = source_url

    out["warrant_id"] = df[warrant_id_col].map(normalize_warrant_id)
    out["warrant_name"] = df[warrant_name_col].astype(str).str.strip() if warrant_name_col else ""

    out["stock_id"] = df[stock_id_col].map(normalize_code) if stock_id_col else ""
    out["stock_name"] = df[stock_name_col].astype(str).str.strip() if stock_name_col else ""

    out["call_put_raw"] = df[call_put_col].astype(str).str.strip() if call_put_col else out["warrant_name"]
    out["call_put"] = out["call_put_raw"].apply(classify_call_put_from_type)

    unknown_mask = out["call_put"] == "unknown"

    if unknown_mask.any():
        out.loc[unknown_mask, "call_put"] = out.loc[unknown_mask, "warrant_id"].apply(classify_call_put_from_warrant_id)

    out["issuer"] = out["warrant_name"].apply(infer_issuer_from_name)

    out["issued_quantity"] = df[issued_col].map(to_number) if issued_col else pd.NA
    out["cancelled_quantity"] = df[cancelled_col].map(to_number) if cancelled_col else pd.NA
    out["latest_warrant_count"] = df[latest_count_col].map(to_number) if latest_count_col else pd.NA
    out["float_quantity"] = df[float_col].map(to_number) if float_col else pd.NA

    out = out[out["warrant_id"].apply(is_warrant_id)].copy()
    out = out[out["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    return out


def standardize_twse_mi_index_quotes(
    df: pd.DataFrame,
    source_name: str,
    source_url: str,
) -> pd.DataFrame:
    """
    來源：TWSE MI_INDEX。
    用途：抓權證的成交股數 / 成交金額 / 收盤價。
    """
    if df.empty:
        return pd.DataFrame()

    df = clean_columns(df)

    id_col = pick_column(df, [
        "證券代號",
        "有價證券代號",
        "代號",
    ])

    name_col = pick_column(df, [
        "證券名稱",
        "有價證券名稱",
        "名稱",
    ])

    volume_col = pick_column(df, [
        "成交股數",
        "成交量",
        "成交單位",
    ])

    turnover_col = pick_column(df, [
        "成交金額",
        "成交值",
    ])

    close_col = pick_column(df, [
        "收盤價",
        "收盤",
    ])

    if not id_col:
        return pd.DataFrame()

    out = pd.DataFrame()
    out["market"] = "TWSE"
    out["source_name"] = source_name
    out["source_url"] = source_url
    out["warrant_id"] = df[id_col].map(normalize_warrant_id)
    out["warrant_name"] = df[name_col].astype(str).str.strip() if name_col else ""
    out["volume"] = df[volume_col].map(to_number) if volume_col else pd.NA
    out["turnover"] = df[turnover_col].map(to_number) if turnover_col else pd.NA
    out["close"] = df[close_col].map(to_number) if close_col else pd.NA

    out = out[out["warrant_id"].apply(is_warrant_id)].copy()

    return out


def standardize_twse_mi_index_quotes_v2(
    df: pd.DataFrame,
    source_name: str,
    source_url: str,
) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    df = clean_columns(df)

    id_col = pick_column(df, ["證券代號", "warrant_id", "securities_code"])
    name_col = pick_column(df, ["證券名稱", "warrant_name", "securities_name"])
    volume_col = pick_column(df, ["成交股數", "volume"])
    turnover_col = pick_column(df, ["成交金額", "turnover"])
    close_col = pick_column(df, ["收盤價", "close"])

    if not id_col and len(df.columns) >= 10:
        # Official TWSE MI_INDEX warrant rows are:
        # suspended, id, name, volume, trades, turnover, open, high, low, close, ...
        id_col = df.columns[1]
        name_col = name_col or df.columns[2]
        volume_col = volume_col or df.columns[3]
        turnover_col = turnover_col or df.columns[5]
        close_col = close_col or df.columns[9]

    if not id_col:
        return pd.DataFrame()

    out = pd.DataFrame(index=df.index)
    out["market"] = "TWSE"
    out["source_name"] = source_name
    out["source_url"] = source_url
    out["warrant_id"] = df[id_col].map(normalize_warrant_id)
    out["warrant_name"] = df[name_col].astype(str).str.strip() if name_col else ""
    out["volume"] = df[volume_col].map(to_number) if volume_col else pd.NA
    out["turnover"] = df[turnover_col].map(to_number) if turnover_col else pd.NA
    out["close"] = df[close_col].map(to_number) if close_col else pd.NA

    out = out[out["warrant_id"].apply(is_warrant_id)].copy()

    return out


def fetch_twse_warrant_mapping(
    date_str: str,
    deadline: float | None = None,
) -> tuple[pd.DataFrame, list[str], list[dict]]:
    urls = [
        (
            "TWSE_WARRANT_STOCK_JSON",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=json",
        ),
        (
            "TWSE_WARRANT_STOCK_CSV",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=csv",
        ),
    ]

    logs = []
    debug_rows = []
    frames = []

    for source_name, url in urls:
        if deadline_expired(deadline):
            logs.append(f"deadline_exceeded mapping date={date_str}")
            break

        tables, log = fetch_source(url, source_name, deadline=deadline)
        logs.append(log)

        for idx, table in enumerate(tables):
            debug_rows.append(
                {
                    "source_name": source_name,
                    "market": "TWSE",
                    "table_index": idx,
                    "rows": len(table),
                    "columns": " | ".join(map(str, table.columns.tolist())),
                    "parsed_as": "mapping",
                }
            )

            parsed = standardize_warrant_mapping_table(table, "TWSE", source_name, url)

            if not parsed.empty:
                frames.append(parsed)

    if not frames:
        return pd.DataFrame(), logs, debug_rows

    out = pd.concat(frames, ignore_index=True)
    out = out.drop_duplicates(subset=["warrant_id"], keep="first")

    return out, logs, debug_rows


def fetch_twse_mi_index_quotes(
    date_str: str,
    deadline: float | None = None,
) -> tuple[pd.DataFrame, list[str], list[dict]]:
    """
    重點：
    - ALLBUT0999 會排除權證，不適合權證金流。
    - 這裡改抓 ALL；若官方分類變動，再由 debug 看實際表格。
    - 另外試幾個可能分類，抓得到就合併去重。
    """
    query_types = ["0999", "0999P"]

    logs = []
    debug_rows = []
    frames = []

    for qtype in query_types:
        if deadline_expired(deadline):
            logs.append(f"deadline_exceeded quote date={date_str}, qtype={qtype}")
            break

        urls = [
            (
                f"TWSE_MI_INDEX_{qtype}_JSON",
                f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_str}&type={qtype}&response=json",
            ),
            (
                f"TWSE_MI_INDEX_{qtype}_CSV",
                f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_str}&type={qtype}&response=csv",
            ),
        ]

        for source_name, url in urls:
            if deadline_expired(deadline):
                logs.append(f"deadline_exceeded quote date={date_str}, source={source_name}")
                break

            tables, log = fetch_source(url, source_name, deadline=deadline)
            logs.append(log)

            for idx, table in enumerate(tables):
                debug_rows.append(
                    {
                        "source_name": source_name,
                        "market": "TWSE",
                        "table_index": idx,
                        "rows": len(table),
                        "columns": " | ".join(map(str, table.columns.tolist())),
                        "parsed_as": "quote",
                    }
                )

                parsed = standardize_twse_mi_index_quotes_v2(table, source_name, url)

                if not parsed.empty:
                    frames.append(parsed)

            time.sleep(0.3)

    if not frames:
        return pd.DataFrame(), logs, debug_rows

    out = pd.concat(frames, ignore_index=True)
    out = out.drop_duplicates(subset=["warrant_id"], keep="last")

    return out, logs, debug_rows


def add_fetch_date_to_debug(debug_rows: list[dict], requested_date: str, fetch_date: str) -> list[dict]:
    out = []

    for row in debug_rows:
        copied = dict(row)
        copied["requested_date"] = requested_date
        copied["fetch_date"] = fetch_date
        out.append(copied)

    return out


def fetch_warrant_data_with_quote_fallback(
    requested_date: str,
    lookback_days: int = 10,
    deadline: float | None = None,
) -> tuple[str, pd.DataFrame, pd.DataFrame, pd.DataFrame, list[str], list[dict], str]:
    logs: list[str] = []
    debug_rows: list[dict] = []
    deadline_hit = False

    for candidate_date in recent_date_candidates(requested_date, lookback_days):
        if deadline_expired(deadline):
            logs.append(f"deadline_exceeded before quote fallback date={candidate_date}")
            deadline_hit = True
            break

        quotes, quote_logs, quote_debug = fetch_twse_mi_index_quotes(candidate_date, deadline=deadline)
        logs.extend(quote_logs)
        debug_rows.extend(add_fetch_date_to_debug(quote_debug, requested_date, candidate_date))

        if has_usable_quote_rows(quotes):
            if deadline_expired(deadline):
                logs.append(f"deadline_exceeded before mapping fallback date={candidate_date}")
                deadline_hit = True
                break

            mapping, mapping_logs, mapping_debug = fetch_twse_warrant_mapping(candidate_date, deadline=deadline)
            logs.extend(mapping_logs)
            debug_rows.extend(add_fetch_date_to_debug(mapping_debug, requested_date, candidate_date))

            out = merge_mapping_and_quotes(mapping, quotes, candidate_date)
            warning = ""

            if candidate_date != requested_date:
                warning = (
                    f"requested_date={requested_date} had no usable warrant quote rows; "
                    f"used latest available quote_date={candidate_date}."
                )

            return candidate_date, mapping, quotes, out, logs, debug_rows, warning

        logs.append(
            f"no_usable_quote_rows date={candidate_date}, "
            f"quote_rows={len(quotes)}; trying previous calendar date"
        )
        time.sleep(0.5)

    if deadline_hit or deadline_expired(deadline):
        warning = (
            "official warrant fetch exceeded runtime budget; "
            "created empty raw file so the daily pipeline can continue."
        )
        return (
            requested_date,
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(columns=RAW_COLUMNS),
            logs,
            debug_rows,
            warning,
        )

    mapping, mapping_logs, mapping_debug = fetch_twse_warrant_mapping(requested_date, deadline=deadline)
    logs.extend(mapping_logs)
    debug_rows.extend(add_fetch_date_to_debug(mapping_debug, requested_date, requested_date))

    quotes = pd.DataFrame()
    out = merge_mapping_and_quotes(mapping, quotes, requested_date)
    warning = (
        f"No usable warrant quote rows found in the last {lookback_days} calendar days; "
        "kept mapping/list rows only."
    )

    return requested_date, mapping, quotes, out, logs, debug_rows, warning


def merge_mapping_and_quotes(mapping: pd.DataFrame, quotes: pd.DataFrame, date_str: str) -> pd.DataFrame:
    if mapping.empty and quotes.empty:
        return pd.DataFrame(columns=RAW_COLUMNS)

    if quotes.empty:
        out = mapping.copy()
        out["volume"] = pd.NA
        out["turnover"] = pd.NA
        out["close"] = pd.NA
        out["source_name"] = out["source_name"].astype(str) + "+no_quote"
        out["source_url"] = out["source_url"].astype(str)
    elif mapping.empty:
        out = quotes.copy()
        out["stock_id"] = ""
        out["stock_name"] = ""
        out["call_put_raw"] = out["warrant_id"]
        out["call_put"] = out["warrant_id"].apply(classify_call_put_from_warrant_id)
        out["issuer"] = out["warrant_name"].apply(infer_issuer_from_name)
        out["issued_quantity"] = pd.NA
        out["cancelled_quantity"] = pd.NA
        out["latest_warrant_count"] = pd.NA
        out["float_quantity"] = pd.NA
    else:
        mapping_cols = [
            "warrant_id",
            "stock_id",
            "stock_name",
            "call_put_raw",
            "call_put",
            "issuer",
            "issued_quantity",
            "cancelled_quantity",
            "latest_warrant_count",
            "float_quantity",
        ]

        mapping_small = mapping[[col for col in mapping_cols if col in mapping.columns]].copy()

        out = quotes.merge(mapping_small, on="warrant_id", how="left")

        if "stock_id" not in out.columns:
            out["stock_id"] = ""

        if "stock_name" not in out.columns:
            out["stock_name"] = ""

        if "call_put" not in out.columns:
            out["call_put"] = ""

        missing_type = out["call_put"].isna() | (out["call_put"].astype(str) == "") | (out["call_put"].astype(str) == "unknown")
        out.loc[missing_type, "call_put"] = out.loc[missing_type, "warrant_id"].apply(classify_call_put_from_warrant_id)

        if "call_put_raw" not in out.columns:
            out["call_put_raw"] = out["call_put"]

        if "issuer" not in out.columns:
            out["issuer"] = out["warrant_name"].apply(infer_issuer_from_name)

        for col in ["issued_quantity", "cancelled_quantity", "latest_warrant_count", "float_quantity"]:
            if col not in out.columns:
                out[col] = pd.NA

    out.insert(0, "date", date_str)

    for col in RAW_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA

    out = out[RAW_COLUMNS].copy()

    # 沒標的股票代號就不能彙總到股票層級，先剔除。
    out = out[out["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    out = out.drop_duplicates(subset=["date", "market", "warrant_id"], keep="last")
    out = out.sort_values(["stock_id", "call_put", "warrant_id"]).reset_index(drop=True)

    return out


def write_debug(debug_rows: list[dict], extra_note: str = "") -> None:
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# 權證官方資料抓取 Debug")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append("")

    if extra_note:
        lines.append(f"- note：`{extra_note}`")
        lines.append("")

    if not debug_rows:
        lines.append("沒有解析到任何表格。")
        DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")
        return

    debug_df = pd.DataFrame(debug_rows)
    debug_df.to_csv(DEBUG_CSV, index=False, encoding="utf-8-sig")

    lines.append(f"- debug csv：`{DEBUG_CSV}`")
    lines.append("")
    lines.append("| source_name | market | table_index | rows | parsed_as | columns |")
    lines.append("|---|---|---:|---:|---|---|")

    for row in debug_rows:
        columns_text = str(row.get("columns", "")).replace("|", "/")

        lines.append(
            f"| {row.get('source_name', '')} "
            f"| {row.get('market', '')} "
            f"| {row.get('table_index', '')} "
            f"| {row.get('rows', '')} "
            f"| {row.get('parsed_as', '')} "
            f"| {columns_text} |"
        )

    DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")


def write_status(
    date_str: str,
    rows: int,
    mapping_rows: int,
    quote_rows: int,
    logs: list[str],
    warning: str = "",
    requested_date: str = "",
) -> None:
    lines = []
    lines.append("# 官方權證每日資料抓取狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 資料日期：`{date_str}`")
    lines.append(f"- 輸出檔：`{RAW_LATEST}`")
    lines.append(f"- 權證對照表筆數：`{mapping_rows}`")
    lines.append(f"- 權證成交行情筆數：`{quote_rows}`")
    lines.append(f"- 最終可彙總筆數：`{rows}`")
    lines.append(f"- debug：`{DEBUG_MD}`")
    lines.append("")

    if warning:
        lines.append(f"- warning：`{warning}`")
        lines.append("")

    lines.append("## Fetch logs")
    lines.append("")

    for log in logs:
        lines.append(f"- {log}")

    FETCH_STATUS_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--date",
        default="",
        help="YYYYMMDD. Default: latest date in data/daily_price or Taiwan today.",
    )
    parser.add_argument(
        "--require-current-usable",
        action="store_true",
        help=(
            "Fail when the requested/latest date has no same-date usable "
            "stock-level warrant quote rows."
        ),
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    requested_date = args.date.strip() or get_latest_price_date()
    deadline = time.monotonic() + FETCH_MAX_SECONDS

    fetch_kwargs = {"deadline": deadline}
    if args.require_current_usable:
        fetch_kwargs["lookback_days"] = 0

    (
        date_str,
        mapping,
        quotes,
        out,
        logs,
        debug_rows,
        fallback_warning,
    ) = fetch_warrant_data_with_quote_fallback(requested_date, **fetch_kwargs)

    write_debug(
        debug_rows,
        extra_note=f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}, final_rows={len(out)}",
    )

    if out.empty or not has_usable_quote_rows(out):
        fallback_path, fallback_raw, fallback_date = find_existing_raw_fallback(date_str, requested_date)

        if not fallback_raw.empty:
            fallback_raw.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
            fallback_raw.to_csv(HISTORY_DIR / f"warrant_daily_{fallback_date}.csv", index=False, encoding="utf-8-sig")
            logs.append(
                f"official_fetch_empty_preserved_existing_raw source={fallback_path} "
                f"date={fallback_date} rows={len(fallback_raw)}"
            )

            write_status(
                date_str=fallback_date,
                rows=len(fallback_raw),
                mapping_rows=len(mapping),
                quote_rows=len(quotes),
                logs=logs,
                warning=(
                    "official warrant fetch produced no usable stock-level rows; "
                    f"preserved existing same-date raw snapshot from {fallback_path}."
                ),
                requested_date=requested_date,
            )

            print(
                "Official warrant fetch produced no usable rows; "
                f"preserved existing same-date raw data from {fallback_path}, rows={len(fallback_raw)}"
            )
            return 0

        if not out.empty:
            logs.append("official_fetch_rows_without_usable_quotes_no_same_date_fallback")
            out.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
            out.to_csv(HISTORY_DIR / f"warrant_daily_{date_str}.csv", index=False, encoding="utf-8-sig")
            warning = (
                fallback_warning
                or "official warrant fetch produced rows without usable quote values; "
                "no same-date fallback was available."
            )
            if args.require_current_usable:
                warning = (
                    f"{warning} --require-current-usable requires same-date "
                    "rows with usable quote values."
                )
            write_status(
                date_str=date_str,
                rows=len(out),
                mapping_rows=len(mapping),
                quote_rows=len(quotes),
                logs=logs,
                warning=warning,
                requested_date=requested_date,
            )
            print(f"Saved mapping-only warrant raw data without usable quotes: {RAW_LATEST}, rows={len(out)}")
            if args.require_current_usable:
                print(
                    "Required same-date usable warrant raw data is unavailable; "
                    "failing because --require-current-usable was set."
                )
                return 1
            return 0

        empty = pd.DataFrame(columns=RAW_COLUMNS)
        empty.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")

        write_status(
            date_str=date_str,
            rows=0,
            mapping_rows=len(mapping),
            quote_rows=len(quotes),
            logs=logs,
            warning=(
                "權證資料未能產出股票層級可彙總資料。"
                "若 mapping_rows > 0 但 quote_rows = 0，代表 MI_INDEX 沒抓到權證成交行情；"
                "若 quote_rows > 0 但 final_rows = 0，代表成交行情與權證對照表無法用權證代號合併。"
            ),
        )

        print("No usable stock-level warrant raw data. Empty raw file created.")
        if args.require_current_usable:
            print(
                "Required same-date usable warrant raw data is unavailable; "
                "failing because --require-current-usable was set."
            )
            return 1
        return 0

    out.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
    out.to_csv(HISTORY_DIR / f"warrant_daily_{date_str}.csv", index=False, encoding="utf-8-sig")

    missing_turnover = int(out["turnover"].isna().sum())
    zero_turnover = int((pd.to_numeric(out["turnover"], errors="coerce").fillna(0) == 0).sum())

    warning = fallback_warning

    if missing_turnover == len(out) or zero_turnover == len(out):
        warning = "最終資料有權證對照，但成交金額全部為空或 0，請查看 MI_INDEX quote debug。"

    write_status(
        date_str=date_str,
        rows=len(out),
        mapping_rows=len(mapping),
        quote_rows=len(quotes),
        logs=logs,
        warning=warning,
    )

    print(f"Saved: {RAW_LATEST}, rows={len(out)}")
    print(f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
