from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import argparse
import io
import json
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

    # 有些欄位會是 "2330 台積電" 或 "2330"
    match = re.search(r"(\d{4})", text)
    if match:
        return match.group(1)

    return ""


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


def yyyymmdd_to_roc_slash(date_str: str) -> str:
    year = int(date_str[:4]) - 1911
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    return f"{year}/{month:02d}/{day:02d}"


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
    """
    TWSE / TPEx 官方 API 有時回傳：
    1. {"fields": [...], "data": [[...], ...]}
    2. {"tables": [{"fields": [...], "data": [[...]]}, ...]}
    3. 巢狀 dict/list
    這裡盡量把所有可轉成表格的資料抓出來。
    """
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

        for value in payload.values():
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


def read_csv_from_text(text: str) -> list[pd.DataFrame]:
    frames: list[pd.DataFrame] = []

    if not text or len(text.strip()) < 10:
        return frames

    cleaned = text.replace("\ufeff", "").strip()

    # JSON fallback
    if cleaned.startswith("{") or cleaned.startswith("["):
        try:
            payload = json.loads(cleaned)
            return dataframe_from_json_payload(payload)
        except Exception:
            pass

    lines = cleaned.splitlines()

    # 找可能的 header，不要只依賴第一行
    header_candidates = []

    for idx, line in enumerate(lines[:80]):
        normalized = line.replace(" ", "")

        if "," in line and any(
            key in normalized
            for key in [
                "權證代號",
                "證券代號",
                "權證名稱",
                "標的",
                "成交",
                "發行",
                "流通",
            ]
        ):
            header_candidates.append(idx)

    if not header_candidates:
        header_candidates = [0]

    for header_index in header_candidates:
        csv_text = "\n".join(lines[header_index:])

        for encoding_name in ["utf-8", "big5", "cp950"]:
            try:
                df = pd.read_csv(io.StringIO(csv_text), dtype=str)
                df = clean_columns(df)

                if not df.empty and len(df.columns) >= 3:
                    frames.append(df)
                    break
            except Exception:
                continue

    return frames


def fetch_source(url: str, source_name: str) -> tuple[list[pd.DataFrame], str]:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": "https://www.twse.com.tw/",
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        raw_text = response.text or ""

        # requests 有時自動判錯編碼，先讓它猜，再保留原文處理
        if response.encoding:
            response.encoding = response.apparent_encoding or response.encoding

        frames = read_csv_from_text(response.text)

        # pandas read_html 當備援；如果環境沒 lxml/html5lib，會自動跳過
        if not frames and "<table" in raw_text.lower():
            try:
                html_frames = pd.read_html(raw_text)
                frames.extend([clean_columns(x.astype(str)) for x in html_frames if not x.empty])
            except Exception:
                pass

        if frames:
            return frames, f"ok source={source_name}, status={response.status_code}, tables={len(frames)}, url={url}"

        return [], f"empty_or_unparsed source={source_name}, status={response.status_code}, chars={len(raw_text)}, url={url}"

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


def classify_call_put(value: str) -> str:
    text = str(value).lower()

    if any(key in text for key in ["認售", "售", "put", " p", "-p", " p "]):
        return "put"

    if any(key in text for key in ["認購", "購", "call", " c", "-c", " c "]):
        return "call"

    return "unknown"


def infer_call_put_from_name(warrant_name: str) -> str:
    text = str(warrant_name)

    if "售" in text:
        return "put"

    if "購" in text:
        return "call"

    return "unknown"


def infer_issuer_from_name(warrant_name: str) -> str:
    """
    權證名稱常見格式：
    台積電元大52購01
    欄位沒有 issuer 時，先用常見券商名做粗略推估。
    """
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
        "合作金庫",
        "日盛",
        "上海",
        "香港上海匯豐",
        "摩根",
        "美林",
        "瑞銀",
        "法興",
    ]

    for issuer in issuers:
        if issuer in text:
            return issuer

    return ""


def standardize_warrant_table(
    df: pd.DataFrame,
    market: str,
    source_name: str,
    source_url: str,
) -> pd.DataFrame:
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
        "權證名稱",
        "證券名稱",
        "權證證券名稱",
        "名稱",
    ])

    underlying_id_col = pick_column(df, [
        "標的證券代號",
        "標的代號",
        "標的股票代號",
        "標的證券",
        "標的股票",
        "標的",
        "連結標的代號",
        "標的金融商品代號",
    ])

    underlying_name_col = pick_column(df, [
        "標的證券名稱",
        "標的名稱",
        "標的股票名稱",
        "連結標的名稱",
        "標的金融商品名稱",
    ])

    call_put_col = pick_column(df, [
        "認購售",
        "認購/售",
        "認購售別",
        "權證種類",
        "種類",
        "購售",
        "權證類型",
    ])

    volume_col = pick_column(df, [
        "成交股數",
        "成交張數",
        "成交量",
        "成交單位",
        "成交數量",
    ])

    turnover_col = pick_column(df, [
        "成交金額",
        "成交值",
        "成交金額元",
    ])

    close_col = pick_column(df, [
        "收盤價",
        "收盤",
        "最後成交價",
    ])

    issuer_col = pick_column(df, [
        "發行人",
        "發行機構",
        "委託證券商",
        "券商",
        "發行券商",
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

    # 如果沒有權證代號或權證名稱，這張表就不是權證明細表
    if not warrant_id_col and not warrant_name_col:
        return pd.DataFrame()

    out = pd.DataFrame()
    out["market"] = market
    out["source_name"] = source_name
    out["source_url"] = source_url

    out["warrant_id"] = df[warrant_id_col].astype(str).str.strip() if warrant_id_col else ""
    out["warrant_name"] = df[warrant_name_col].astype(str).str.strip() if warrant_name_col else ""

    if underlying_id_col:
        out["stock_id"] = df[underlying_id_col].map(normalize_code)
    else:
        out["stock_id"] = ""

    # 有些表格標的欄位只有名稱，或代號藏在權證名稱裡；抓不到就先留空，debug 會顯示
    out["stock_name"] = df[underlying_name_col].astype(str).str.strip() if underlying_name_col else ""

    if call_put_col:
        out["call_put_raw"] = df[call_put_col].astype(str).str.strip()
        out["call_put"] = out["call_put_raw"].apply(classify_call_put)
    else:
        out["call_put_raw"] = out["warrant_name"]
        out["call_put"] = out["warrant_name"].apply(infer_call_put_from_name)

    out["volume"] = df[volume_col].map(to_number) if volume_col else pd.NA
    out["turnover"] = df[turnover_col].map(to_number) if turnover_col else pd.NA
    out["close"] = df[close_col].map(to_number) if close_col else pd.NA

    if issuer_col:
        out["issuer"] = df[issuer_col].astype(str).str.strip()
    else:
        out["issuer"] = out["warrant_name"].apply(infer_issuer_from_name)

    out["issued_quantity"] = df[issued_col].map(to_number) if issued_col else pd.NA
    out["cancelled_quantity"] = df[cancelled_col].map(to_number) if cancelled_col else pd.NA
    out["latest_warrant_count"] = df[latest_count_col].map(to_number) if latest_count_col else pd.NA
    out["float_quantity"] = df[float_col].map(to_number) if float_col else pd.NA

    out = out[out["warrant_id"].astype(str).str.strip().str.len() > 0].copy()

    # 權證代號通常是 5～6 碼，避免把說明列誤判成資料
    out = out[out["warrant_id"].astype(str).str.contains(r"\d", na=False)].copy()

    # 標的股票代號抓不到時先剔除，否則無法彙總到股票層級
    out = out[out["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    return out


def fetch_twse_warrants(date_str: str) -> tuple[list[pd.DataFrame], list[str], list[dict]]:
    urls = [
        (
            "TWSE_JSON_RWD",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=json",
        ),
        (
            "TWSE_CSV_RWD",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=csv",
        ),
        (
            "TWSE_JSON_OLD",
            f"https://www.twse.com.tw/exchangeReport/warrantStock?date={date_str}&response=json",
        ),
        (
            "TWSE_CSV_OLD",
            f"https://www.twse.com.tw/exchangeReport/warrantStock?date={date_str}&response=csv",
        ),
    ]

    logs = []
    debug_rows = []
    standardized_frames = []

    for source_name, url in urls:
        frames, log = fetch_source(url, source_name)
        logs.append(log)

        for idx, frame in enumerate(frames):
            debug_rows.append(
                {
                    "source_name": source_name,
                    "market": "TWSE",
                    "table_index": idx,
                    "rows": len(frame),
                    "columns": " | ".join(map(str, frame.columns.tolist())),
                }
            )

            standardized = standardize_warrant_table(frame, "TWSE", source_name, url)

            if not standardized.empty:
                standardized_frames.append(standardized)

    return standardized_frames, logs, debug_rows


def fetch_tpex_warrants(date_str: str) -> tuple[list[pd.DataFrame], list[str], list[dict]]:
    roc = yyyymmdd_to_roc_slash(date_str)

    urls = [
        (
            "TPEX_DAILYQ_JSON",
            f"https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date={roc}&response=json",
        ),
        (
            "TPEX_DAILYQ_CSV",
            f"https://www.tpex.org.tw/www/zh-tw/warrant/dailyQ?date={roc}&response=csv",
        ),
        (
            "TPEX_LEGACY_HTML",
            f"https://www.tpex.org.tw/web/stock/aftertrading/warrant_quotes/warrant_quotes_result.php?l=zh-tw&d={roc}",
        ),
        (
            "TPEX_EXTEND",
            f"https://www.tpex.org.tw/ch/extend/warrant/dailyQ/wntQuts.php?l=zh-tw&d={roc}&s=0,asc,0",
        ),
    ]

    logs = []
    debug_rows = []
    standardized_frames = []

    for source_name, url in urls:
        frames, log = fetch_source(url, source_name)
        logs.append(log)

        for idx, frame in enumerate(frames):
            debug_rows.append(
                {
                    "source_name": source_name,
                    "market": "TPEX",
                    "table_index": idx,
                    "rows": len(frame),
                    "columns": " | ".join(map(str, frame.columns.tolist())),
                }
            )

            standardized = standardize_warrant_table(frame, "TPEX", source_name, url)

            if not standardized.empty:
                standardized_frames.append(standardized)

    return standardized_frames, logs, debug_rows


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
    debug_csv = DEBUG_DIR / "warrant_fetch_debug_latest.csv"
    debug_df.to_csv(debug_csv, index=False, encoding="utf-8-sig")

    lines.append(f"- debug csv：`{debug_csv}`")
    lines.append("")
    lines.append("| source_name | market | table_index | rows | columns |")
    lines.append("|---|---|---:|---:|---|")

    for row in debug_rows:
        lines.append(
            f"| {row.get('source_name', '')} "
            f"| {row.get('market', '')} "
            f"| {row.get('table_index', '')} "
            f"| {row.get('rows', '')} "
            f"| {str(row.get('columns', '')).replace('|', '/')} |"
        )

    DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")


def write_status(date_str: str, rows: int, logs: list[str], warning: str = "") -> None:
    lines = []
    lines.append("# 官方權證每日資料抓取狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 資料日期：`{date_str}`")
    lines.append(f"- 輸出檔：`{RAW_LATEST}`")
    lines.append(f"- 筆數：`{rows}`")
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
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    date_str = args.date.strip() or get_latest_price_date()

    logs = []
    debug_rows = []
    frames = []

    twse_frames, twse_logs, twse_debug = fetch_twse_warrants(date_str)
    logs.extend(twse_logs)
    debug_rows.extend(twse_debug)
    frames.extend(twse_frames)

    time.sleep(1)

    tpex_frames, tpex_logs, tpex_debug = fetch_tpex_warrants(date_str)
    logs.extend(tpex_logs)
    debug_rows.extend(tpex_debug)
    frames.extend(tpex_frames)

    write_debug(debug_rows)

    if frames:
        out = pd.concat(frames, ignore_index=True)
        out.insert(0, "date", date_str)

        for col in RAW_COLUMNS:
            if col not in out.columns:
                out[col] = pd.NA

        out = out[RAW_COLUMNS].copy()
        out = out.drop_duplicates(subset=["date", "market", "warrant_id"], keep="last")
        out = out.sort_values(["stock_id", "call_put", "warrant_id"]).reset_index(drop=True)

        out.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")
        out.to_csv(HISTORY_DIR / f"warrant_daily_{date_str}.csv", index=False, encoding="utf-8-sig")

        write_status(date_str, len(out), logs)

        print(f"Saved: {RAW_LATEST}, rows={len(out)}")
        return 0

    empty = pd.DataFrame(columns=RAW_COLUMNS)
    empty.to_csv(RAW_LATEST, index=False, encoding="utf-8-sig")

    write_status(
        date_str,
        0,
        logs,
        warning="官方權證資料抓取失敗、格式無法解析，或官方資料沒有提供標的股票代號；已輸出空檔避免 workflow 失敗。",
    )

    print("No standardized warrant data fetched. Empty raw file created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
