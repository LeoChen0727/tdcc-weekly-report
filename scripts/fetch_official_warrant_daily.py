from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import argparse
import hashlib
import io
import json
import os
import re
import shutil
import tempfile
import time
from typing import Any

import pandas as pd
import requests


OUTPUT_DIR = Path("output/latest")
DEBUG_DIR = Path("output/debug")
HISTORY_DIR = Path("output/history/warrant_daily")

RAW_LATEST = OUTPUT_DIR / "warrant_daily_raw_latest.csv"
FETCH_STATUS_MD = OUTPUT_DIR / "warrant_daily_fetch_latest.md"
SOURCE_STATUS_JSON = OUTPUT_DIR / "warrant_source_status_latest.json"
SOURCE_STATUS_MD = OUTPUT_DIR / "warrant_source_status_latest.md"
DEBUG_MD = DEBUG_DIR / "warrant_fetch_debug_latest.md"
DEBUG_CSV = DEBUG_DIR / "warrant_fetch_debug_latest.csv"
FETCH_RESPONSE_PROVENANCE: list[dict[str, Any]] = []

REQUEST_TIMEOUT_SECONDS = float(os.getenv("OFFICIAL_WARRANT_REQUEST_TIMEOUT", "8"))
HISTORICAL_REPLAY_REQUEST_TIMEOUT_SECONDS = float(
    os.getenv("OFFICIAL_WARRANT_HISTORICAL_REQUEST_TIMEOUT", "30")
)
FETCH_MAX_SECONDS = float(os.getenv("OFFICIAL_WARRANT_FETCH_MAX_SECONDS", "360"))
HISTORICAL_REPLAY_MAX_ATTEMPTS = int(
    os.getenv("OFFICIAL_WARRANT_HISTORICAL_MAX_ATTEMPTS", "3")
)
HISTORICAL_REPLAY_RETRY_BACKOFF_SECONDS = float(
    os.getenv("OFFICIAL_WARRANT_HISTORICAL_RETRY_BACKOFF_SECONDS", "1")
)
MAX_CONSECUTIVE_UNAVAILABLE_DAYS = int(os.getenv("OFFICIAL_WARRANT_MAX_CONSECUTIVE_UNAVAILABLE_DAYS", "2"))

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


def request_timeout(deadline: float | None, timeout_seconds: float | None = None) -> float:
    configured_timeout = REQUEST_TIMEOUT_SECONDS if timeout_seconds is None else timeout_seconds
    if configured_timeout <= 0:
        raise RuntimeError("official warrant request timeout must be positive")
    remaining = deadline_remaining(deadline)
    if remaining is None:
        return configured_timeout
    if remaining <= 0:
        raise RuntimeError("official warrant request deadline exhausted before request")
    return min(configured_timeout, remaining)


def sleep_with_deadline(seconds: float, deadline: float | None) -> float:
    delay = max(0.0, float(seconds))
    remaining = deadline_remaining(deadline)
    if remaining is not None:
        delay = min(delay, remaining)
    if delay > 0:
        time.sleep(delay)
    return delay


def reset_fetch_response_provenance() -> None:
    FETCH_RESPONSE_PROVENANCE.clear()


def fetch_response_provenance() -> list[dict[str, Any]]:
    return [dict(row) for row in FETCH_RESPONSE_PROVENANCE]


def extract_official_response_dates(text: str) -> list[str]:
    payload_text = str(text or "")
    try:
        payload = json.loads(payload_text)
    except Exception:
        payload = None

    values: list[str] = []
    if isinstance(payload, dict):
        for key in ("title", "date", "queryDate", "reportDate", "tradeDate"):
            if key in payload and not isinstance(payload[key], (dict, list)):
                values.append(str(payload[key]))
        tables = payload.get("tables")
        if isinstance(tables, list):
            for table in tables:
                if not isinstance(table, dict):
                    continue
                for key in ("title", "date", "queryDate", "reportDate", "tradeDate"):
                    if key in table and not isinstance(table[key], (dict, list)):
                        values.append(str(table[key]))
    elif payload is None:
        # Official CSV puts the report title on the first non-empty line.
        # Never scan body rows, which contain exercise/listing dates.
        first_line = next((line.strip() for line in payload_text.splitlines() if line.strip()), "")
        if first_line:
            values.append(first_line)
    dates: set[str] = set()
    for value in values:
        for roc_year, month, day in re.findall(r"(?<!\d)(\d{2,3})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日", value):
            try:
                dates.add(datetime(int(roc_year) + 1911, int(month), int(day)).strftime("%Y%m%d"))
            except ValueError:
                continue
        for year, month, day in re.findall(r"(?<!\d)(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})(?!\d)", value):
            try:
                dates.add(datetime(int(year), int(month), int(day)).strftime("%Y%m%d"))
            except ValueError:
                continue
        for compact in re.findall(r"(?<!\d)(20\d{6})(?!\d)", value):
            try:
                dates.add(datetime.strptime(compact, "%Y%m%d").strftime("%Y%m%d"))
            except ValueError:
                continue
    return sorted(dates)


def record_response_provenance(
    url: str,
    response: Any,
    *,
    source_name: str = "",
    expected_response_date: str = "",
    family: str = "",
    logical_group: str = "",
    attempt_number: int = 1,
    params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    text = str(getattr(response, "text", "") or "")
    raw = getattr(response, "content", None)
    if not isinstance(raw, bytes):
        raw = text.encode("utf-8")
    observed_dates = extract_official_response_dates(text)
    row = {
            "endpoint": url,
            "source_name": source_name,
            "family": family,
            "logical_group": logical_group or family,
            "attempt": attempt_number,
            "params": dict(params or {}),
            "status_code": int(getattr(response, "status_code", 0) or 0),
            "fetched_at": f"{now_taipei()} Asia/Taipei",
            "elapsed_seconds": 0.0,
            "raw_bytes": len(raw),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "normalized_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "encoding": str(getattr(response, "encoding", "") or ""),
            "observed_response_dates": observed_dates,
            "expected_response_date": expected_response_date,
            "exact_date_match": (
                observed_dates == [expected_response_date] if expected_response_date else "not_required"
            ),
            "parsed_table_count": 0,
            "parsed_table_rows": 0,
            "accepted_rows": 0,
            "accepted": False,
            "status": "received",
            "error": "",
        }
    FETCH_RESPONSE_PROVENANCE.append(row)
    return row


def failed_request_provenance(
    url: str,
    *,
    source_name: str,
    expected_response_date: str,
    family: str,
    logical_group: str,
    attempt_number: int,
    params: dict[str, Any] | None,
    error: str,
) -> dict[str, Any]:
    row = {
        "endpoint": url,
        "source_name": source_name,
        "family": family,
        "logical_group": logical_group or family,
        "attempt": attempt_number,
        "params": dict(params or {}),
        "status_code": 0,
        "fetched_at": f"{now_taipei()} Asia/Taipei",
        "elapsed_seconds": 0.0,
        "raw_bytes": 0,
        "raw_sha256": "",
        "normalized_sha256": "",
        "encoding": "",
        "observed_response_dates": [],
        "expected_response_date": expected_response_date,
        "exact_date_match": False if expected_response_date else "not_required",
        "parsed_table_count": 0,
        "parsed_table_rows": 0,
        "accepted_rows": 0,
        "accepted": False,
        "status": "failed",
        "error": error,
    }
    FETCH_RESPONSE_PROVENANCE.append(row)
    return row


def historical_family_attempts(family: str, requested_date: str) -> list[dict[str, Any]]:
    return [
        dict(row)
        for row in FETCH_RESPONSE_PROVENANCE
        if row.get("family") == family
        and row.get("expected_response_date") == requested_date
    ]


def raise_historical_family_exhaustion(
    family: str,
    requested_date: str,
    *,
    subfamily: str = "",
) -> None:
    attempts = historical_family_attempts(family, requested_date)
    evidence = json.dumps(attempts, ensure_ascii=False, sort_keys=True)
    suffix = f" subfamily={subfamily}" if subfamily else ""
    raise RuntimeError(
        "historical warrant fetch exhausted bounded retries "
        f"family={family}{suffix} requested_date={requested_date} attempts={evidence}"
    )


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


def require_calendar_date(value: str, label: str = "date") -> str:
    text = normalize_date_value(value)
    if text != str(value or "").strip():
        raise RuntimeError(f"{label} must be calendar-valid YYYYMMDD")
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError(f"{label} must be calendar-valid YYYYMMDD") from exc
    return text


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
    expected_response_date: str = "",
    *,
    family: str = "",
    logical_group: str = "",
    attempt_number: int = 1,
    params: dict[str, Any] | None = None,
) -> tuple[list[pd.DataFrame], str, dict[str, Any]]:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json,text/csv,text/plain,text/html,*/*",
        "Referer": referer,
    }

    if deadline_expired(deadline):
        error = f"deadline_exceeded before_request source={source_name}, url={url}"
        attempt = failed_request_provenance(
            url,
            source_name=source_name,
            expected_response_date=expected_response_date,
            family=family,
            logical_group=logical_group,
            attempt_number=attempt_number,
            params=params,
            error=error,
        )
        return [], error, attempt

    provenance: dict[str, Any] | None = None
    started_at = time.monotonic()
    try:
        timeout_seconds = (
            HISTORICAL_REPLAY_REQUEST_TIMEOUT_SECONDS
            if expected_response_date
            else REQUEST_TIMEOUT_SECONDS
        )
        response = requests.get(
            url,
            headers=headers,
            timeout=request_timeout(deadline, timeout_seconds),
        )
        response.encoding = response.apparent_encoding or response.encoding or "utf-8"
        provenance = record_response_provenance(
            url,
            response,
            source_name=source_name,
            expected_response_date=expected_response_date,
            family=family,
            logical_group=logical_group,
            attempt_number=attempt_number,
            params=params,
        )
        if provenance["status_code"] < 200 or provenance["status_code"] >= 300:
            raise RuntimeError(f"HTTP status {provenance['status_code']}")
        if expected_response_date and provenance["exact_date_match"] is not True:
            raise RuntimeError(
                "response_date_mismatch "
                f"source={source_name}, expected={expected_response_date}, "
                f"observed={provenance['observed_response_dates']}, url={url}"
            )

        frames = read_tables_from_text(response.text)

        if not frames and "<table" in response.text.lower():
            try:
                html_frames = pd.read_html(response.text)
                frames.extend([clean_columns(x.astype(str)) for x in html_frames if not x.empty])
            except Exception:
                pass

        if frames:
            provenance["parsed_table_count"] = len(frames)
            provenance["parsed_table_rows"] = sum(len(frame) for frame in frames)
            provenance["elapsed_seconds"] = round(time.monotonic() - started_at, 6)
            provenance["status"] = "parsed"
            return (
                frames,
                f"ok source={source_name}, status={response.status_code}, tables={len(frames)}, url={url}",
                provenance,
            )

        raise RuntimeError(
            f"empty_or_unparsed source={source_name}, status={response.status_code}, "
            f"chars={len(response.text)}, url={url}"
        )

    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        if provenance is None:
            provenance = failed_request_provenance(
                url,
                source_name=source_name,
                expected_response_date=expected_response_date,
                family=family,
                logical_group=logical_group,
                attempt_number=attempt_number,
                params=params,
                error=error,
            )
        else:
            provenance["status"] = "failed"
            provenance["error"] = error
        provenance["elapsed_seconds"] = round(time.monotonic() - started_at, 6)
        return [], f"failed source={source_name}, error={error}, url={url}", provenance


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
    require_exact_response_date: bool = False,
) -> tuple[pd.DataFrame, list[str], list[dict]]:
    urls = [
        (
            "TWSE_WARRANT_STOCK_JSON",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=json",
            {"date": date_str, "response": "json"},
        ),
        (
            "TWSE_WARRANT_STOCK_CSV",
            f"https://www.twse.com.tw/rwd/zh/stock/warrantStock?date={date_str}&response=csv",
            {"date": date_str, "response": "csv"},
        ),
    ]

    logs = []
    debug_rows = []
    frames = []
    max_attempts = HISTORICAL_REPLAY_MAX_ATTEMPTS if require_exact_response_date else 1
    if max_attempts < 1:
        raise RuntimeError("historical warrant replay max attempts must be at least 1")
    if HISTORICAL_REPLAY_RETRY_BACKOFF_SECONDS < 0:
        raise RuntimeError("historical warrant replay retry backoff must be non-negative")

    for source_name, url, params in urls:
        for attempt_number in range(1, max_attempts + 1):
            tables, log, attempt = fetch_source(
                url,
                source_name,
                deadline=deadline,
                expected_response_date=date_str if require_exact_response_date else "",
                family="mapping",
                logical_group="mapping",
                attempt_number=attempt_number,
                params=params,
            )
            logs.append(log)
            parsed_frames: list[pd.DataFrame] = []

            for idx, table in enumerate(tables):
                debug_rows.append(
                    {
                        "source_name": source_name,
                        "market": "TWSE",
                        "attempt": attempt_number,
                        "table_index": idx,
                        "rows": len(table),
                        "columns": " | ".join(map(str, table.columns.tolist())),
                        "parsed_as": "mapping",
                    }
                )

                parsed = standardize_warrant_mapping_table(table, "TWSE", source_name, url)
                if not parsed.empty:
                    parsed_frames.append(parsed)

            parsed_attempt = (
                pd.concat(parsed_frames, ignore_index=True)
                if parsed_frames
                else pd.DataFrame()
            )
            attempt["accepted_rows"] = len(parsed_attempt)
            if not parsed_attempt.empty:
                attempt["accepted"] = True
                attempt["status"] = "accepted"
                attempt["error"] = ""
                frames.append(parsed_attempt)
                if require_exact_response_date:
                    out = pd.concat(frames, ignore_index=True)
                    return out.drop_duplicates(subset=["warrant_id"], keep="first"), logs, debug_rows
                break

            attempt["accepted"] = False
            attempt["status"] = "failed"
            if not attempt.get("error"):
                attempt["error"] = "mapping parser produced no accepted warrant rows"
            if require_exact_response_date and attempt_number < max_attempts:
                proposed_delay = HISTORICAL_REPLAY_RETRY_BACKOFF_SECONDS * attempt_number
                remaining = deadline_remaining(deadline)
                delay = proposed_delay if remaining is None else min(proposed_delay, remaining)
                retry_log = (
                    "retry historical warrant family=mapping "
                    f"source={source_name} attempt={attempt_number}/{max_attempts} "
                    f"delay_seconds={delay:g} error={attempt['error']}"
                )
                logs.append(retry_log)
                print(retry_log)
                sleep_with_deadline(delay, deadline)

        if not require_exact_response_date:
            continue

    if require_exact_response_date:
        raise_historical_family_exhaustion("mapping", date_str)

    if not frames:
        return pd.DataFrame(), logs, debug_rows

    out = pd.concat(frames, ignore_index=True)
    out = out.drop_duplicates(subset=["warrant_id"], keep="first")

    return out, logs, debug_rows


def fetch_twse_mi_index_quotes(
    date_str: str,
    deadline: float | None = None,
    require_exact_response_date: bool = False,
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
    max_attempts = HISTORICAL_REPLAY_MAX_ATTEMPTS if require_exact_response_date else 1
    if max_attempts < 1:
        raise RuntimeError("historical warrant replay max attempts must be at least 1")
    if HISTORICAL_REPLAY_RETRY_BACKOFF_SECONDS < 0:
        raise RuntimeError("historical warrant replay retry backoff must be non-negative")

    for qtype in query_types:
        urls = [
            (
                f"TWSE_MI_INDEX_{qtype}_JSON",
                f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_str}&type={qtype}&response=json",
                {"date": date_str, "type": qtype, "response": "json"},
            ),
            (
                f"TWSE_MI_INDEX_{qtype}_CSV",
                f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date_str}&type={qtype}&response=csv",
                {"date": date_str, "type": qtype, "response": "csv"},
            ),
        ]
        qtype_accepted = False

        for source_name, url, params in urls:
            for attempt_number in range(1, max_attempts + 1):
                tables, log, attempt = fetch_source(
                    url,
                    source_name,
                    deadline=deadline,
                    expected_response_date=date_str if require_exact_response_date else "",
                    family="quote",
                    logical_group=f"quote-{qtype}",
                    attempt_number=attempt_number,
                    params=params,
                )
                logs.append(log)
                parsed_frames: list[pd.DataFrame] = []

                for idx, table in enumerate(tables):
                    debug_rows.append(
                        {
                            "source_name": source_name,
                            "market": "TWSE",
                            "attempt": attempt_number,
                            "table_index": idx,
                            "rows": len(table),
                            "columns": " | ".join(map(str, table.columns.tolist())),
                            "parsed_as": "quote",
                        }
                    )

                    parsed = standardize_twse_mi_index_quotes_v2(table, source_name, url)
                    if not parsed.empty:
                        parsed_frames.append(parsed)

                parsed_attempt = (
                    pd.concat(parsed_frames, ignore_index=True)
                    if parsed_frames
                    else pd.DataFrame()
                )
                attempt["accepted_rows"] = len(parsed_attempt)
                if has_usable_quote_rows(parsed_attempt):
                    attempt["accepted"] = True
                    attempt["status"] = "accepted"
                    attempt["error"] = ""
                    frames.append(parsed_attempt)
                    qtype_accepted = True
                    break

                attempt["accepted"] = False
                attempt["status"] = "failed"
                if not attempt.get("error"):
                    attempt["error"] = (
                        f"quote parser produced no usable warrant rows for type={qtype}"
                    )
                if require_exact_response_date and attempt_number < max_attempts:
                    proposed_delay = HISTORICAL_REPLAY_RETRY_BACKOFF_SECONDS * attempt_number
                    remaining = deadline_remaining(deadline)
                    delay = proposed_delay if remaining is None else min(proposed_delay, remaining)
                    retry_log = (
                        "retry historical warrant family=quote "
                        f"type={qtype} source={source_name} "
                        f"attempt={attempt_number}/{max_attempts} delay_seconds={delay:g} "
                        f"error={attempt['error']}"
                    )
                    logs.append(retry_log)
                    print(retry_log)
                    sleep_with_deadline(delay, deadline)

            if require_exact_response_date and qtype_accepted:
                break
            if not require_exact_response_date:
                sleep_with_deadline(0.3, deadline)

        if require_exact_response_date and not qtype_accepted:
            raise_historical_family_exhaustion("quote", date_str, subfamily=qtype)
        if require_exact_response_date:
            sleep_with_deadline(0.3, deadline)

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
    require_exact_response_date: bool = False,
) -> tuple[str, pd.DataFrame, pd.DataFrame, pd.DataFrame, list[str], list[dict], str]:
    logs: list[str] = []
    debug_rows: list[dict] = []
    deadline_hit = False

    for candidate_date in recent_date_candidates(requested_date, lookback_days):
        if deadline_expired(deadline) and not require_exact_response_date:
            logs.append(f"deadline_exceeded before quote fallback date={candidate_date}")
            deadline_hit = True
            break

        quotes, quote_logs, quote_debug = fetch_twse_mi_index_quotes(
            candidate_date,
            deadline=deadline,
            require_exact_response_date=require_exact_response_date,
        )
        logs.extend(quote_logs)
        debug_rows.extend(add_fetch_date_to_debug(quote_debug, requested_date, candidate_date))

        if has_usable_quote_rows(quotes):
            if deadline_expired(deadline) and not require_exact_response_date:
                logs.append(f"deadline_exceeded before mapping fallback date={candidate_date}")
                deadline_hit = True
                break

            mapping, mapping_logs, mapping_debug = fetch_twse_warrant_mapping(
                candidate_date,
                deadline=deadline,
                require_exact_response_date=require_exact_response_date,
            )
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
        sleep_with_deadline(0.5, deadline)

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

    mapping, mapping_logs, mapping_debug = fetch_twse_warrant_mapping(
        requested_date,
        deadline=deadline,
        require_exact_response_date=require_exact_response_date,
    )
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


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def commit_staged_paths(staged_paths: list[tuple[Path, Path]], rollback_root: Path) -> None:
    if not staged_paths:
        raise RuntimeError("historical warrant replay staged publish set is empty")
    targets = [target.resolve() for _, target in staged_paths]
    if len(targets) != len(set(targets)):
        raise RuntimeError("historical warrant replay staged publish has duplicate targets")
    target_volumes = {target.anchor.lower() for target in targets}
    staged_volumes = {staged.resolve().anchor.lower() for staged, _ in staged_paths}
    if len(target_volumes) != 1 or staged_volumes != target_volumes:
        raise RuntimeError(
            "historical warrant replay atomic publish requires one shared filesystem volume"
        )

    rollback_root.mkdir(parents=True, exist_ok=False)
    manifest: list[dict[str, Any]] = []
    for index, (staged_path, target_path) in enumerate(staged_paths):
        if not staged_path.is_file():
            raise RuntimeError(f"historical warrant replay staged file missing: {staged_path}")
        backup_path = rollback_root / f"{index:04d}.bak"
        existed = target_path.is_file()
        if existed:
            shutil.copy2(target_path, backup_path)
        manifest.append(
            {
                "staged": staged_path,
                "target": target_path,
                "backup": backup_path,
                "existed": existed,
                "sha256": file_sha256(staged_path),
            }
        )

    touched: list[dict[str, Any]] = []
    try:
        for item in manifest:
            target_path = item["target"]
            target_path.parent.mkdir(parents=True, exist_ok=True)
            item["staged"].replace(target_path)
            touched.append(item)
            if file_sha256(target_path) != item["sha256"]:
                raise RuntimeError(
                    f"historical warrant replay post-publish SHA-256 mismatch: {target_path}"
                )
    except Exception:
        rollback_errors: list[str] = []
        for item in reversed(touched):
            target_path = item["target"]
            try:
                if item["existed"]:
                    shutil.copy2(item["backup"], target_path)
                    if file_sha256(target_path) != file_sha256(item["backup"]):
                        raise RuntimeError("restored bytes failed SHA-256 verification")
                elif target_path.exists():
                    target_path.unlink()
            except Exception as rollback_exc:  # pragma: no cover - catastrophic IO path
                rollback_errors.append(f"{target_path}: {rollback_exc}")
        if rollback_errors:
            raise RuntimeError(
                "historical warrant replay publish failed and rollback was incomplete: "
                + "; ".join(rollback_errors)
            )
        raise


def write_debug(
    debug_rows: list[dict],
    extra_note: str = "",
    *,
    debug_md_path: Path | None = None,
    debug_csv_path: Path | None = None,
) -> None:
    debug_md_path = debug_md_path or DEBUG_MD
    debug_csv_path = debug_csv_path or DEBUG_CSV
    debug_md_path.parent.mkdir(parents=True, exist_ok=True)
    debug_csv_path.parent.mkdir(parents=True, exist_ok=True)

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
        debug_md_path.write_text("\n".join(lines), encoding="utf-8")
        return

    debug_df = pd.DataFrame(debug_rows)
    debug_df.to_csv(debug_csv_path, index=False, encoding="utf-8-sig")

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

    debug_md_path.write_text("\n".join(lines), encoding="utf-8")


def write_status(
    date_str: str,
    rows: int,
    mapping_rows: int,
    quote_rows: int,
    logs: list[str],
    warning: str = "",
    requested_date: str = "",
    *,
    fetch_status_path: Path | None = None,
) -> None:
    fetch_status_path = fetch_status_path or FETCH_STATUS_MD
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

    fetch_status_path.parent.mkdir(parents=True, exist_ok=True)
    fetch_status_path.write_text("\n".join(lines), encoding="utf-8")


def read_source_status() -> dict[str, Any]:
    if not SOURCE_STATUS_JSON.exists():
        return {}
    try:
        data = json.loads(SOURCE_STATUS_JSON.read_text(encoding="utf-8-sig"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def unavailable_count_for_date(requested_date: str) -> int:
    requested_date = normalize_date_value(requested_date)
    previous = read_source_status()
    previous_status = str(previous.get("status", "")).strip()
    previous_date = normalize_date_value(
        previous.get("last_unavailable_date")
        or previous.get("target_date")
        or previous.get("requested_date")
        or ""
    )
    try:
        previous_count = int(previous.get("consecutive_unavailable_trading_days", 0))
    except Exception:
        previous_count = 0

    if previous_status not in {"warning_grace", "failed"} or previous_count <= 0:
        return 1
    if requested_date and previous_date == requested_date:
        return max(previous_count, 1)
    if requested_date and previous_date and previous_date < requested_date:
        return previous_count + 1
    return 1


def build_source_status(
    *,
    requested_date: str,
    data_date: str,
    usable: bool,
    final_rows: int,
    mapping_rows: int,
    quote_rows: int,
    note: str,
) -> dict[str, Any]:
    requested_date = normalize_date_value(requested_date)
    data_date = normalize_date_value(data_date)
    generated_at = f"{now_taipei()} Asia/Taipei"

    if usable:
        return {
            "status": "ok",
            "generated_at": generated_at,
            "requested_date": requested_date,
            "target_date": requested_date,
            "data_date": data_date or requested_date,
            "last_unavailable_date": "",
            "consecutive_unavailable_trading_days": 0,
            "max_warning_days": MAX_CONSECUTIVE_UNAVAILABLE_DAYS,
            "hard_fail_after_days": MAX_CONSECUTIVE_UNAVAILABLE_DAYS + 1,
            "daily_publish_allowed": True,
            "warrant_pdf_visibility": "visible",
            "model_effect_allowed": True,
            "pdf_effect_allowed": True,
            "final_rows": int(final_rows),
            "mapping_rows": int(mapping_rows),
            "quote_rows": int(quote_rows),
            "note": note or "current-date stock-level warrant data is usable",
        }

    unavailable_count = unavailable_count_for_date(requested_date)
    in_grace = unavailable_count <= MAX_CONSECUTIVE_UNAVAILABLE_DAYS
    status = "warning_grace" if in_grace else "failed"
    return {
        "status": status,
        "generated_at": generated_at,
        "requested_date": requested_date,
        "target_date": requested_date,
        "data_date": data_date,
        "last_unavailable_date": requested_date,
        "consecutive_unavailable_trading_days": unavailable_count,
        "max_warning_days": MAX_CONSECUTIVE_UNAVAILABLE_DAYS,
        "hard_fail_after_days": MAX_CONSECUTIVE_UNAVAILABLE_DAYS + 1,
        "daily_publish_allowed": bool(in_grace),
        "warrant_pdf_visibility": "hidden_unavailable" if in_grace else "blocked_unavailable",
        "model_effect_allowed": False,
        "pdf_effect_allowed": False,
        "final_rows": int(final_rows),
        "mapping_rows": int(mapping_rows),
        "quote_rows": int(quote_rows),
        "note": note or "current-date stock-level warrant data is unavailable",
    }


def attach_replay_provenance(
    status: dict[str, Any],
    *,
    historical_replay: bool,
    requested_date: str,
    data_date: str,
    fallback_used: bool,
) -> dict[str, Any]:
    result = dict(status)
    result.update(
        {
            "mode": "reconstructed_source_tail_gap" if historical_replay else "latest_refresh",
            "publication_status": (
                "reconstructed_not_as_published" if historical_replay else "as_published"
            ),
            "as_published": False if historical_replay else True,
            "requested_date": normalize_date_value(requested_date),
            "observed_date": normalize_date_value(data_date),
            "fallback_used": bool(fallback_used),
            "future_rows_used": False,
            "source_responses": fetch_response_provenance(),
        }
    )
    if historical_replay:
        if result["requested_date"] != result["observed_date"]:
            raise RuntimeError(
                "historical warrant replay response date mismatch: "
                f"{result['observed_date']} != {result['requested_date']}"
            )
        if fallback_used:
            raise RuntimeError("historical warrant replay forbids existing-artifact fallback")
        if not result["source_responses"]:
            raise RuntimeError("historical warrant replay requires live source response provenance")
        accepted_exact_families: set[str] = set()
        accepted_quote_types: set[str] = set()
        accepted_logical_groups: set[str] = set()
        for index, response in enumerate(result["source_responses"]):
            if not isinstance(response, dict):
                raise RuntimeError(
                    f"historical warrant replay source response {index} must be an object"
                )
            if not str(response.get("endpoint", "")).strip():
                raise RuntimeError(
                    f"historical warrant replay source response {index} lacks endpoint"
                )
            if not str(response.get("source_name", "")).strip():
                raise RuntimeError(
                    f"historical warrant replay source response {index} lacks source_name"
                )
            if not isinstance(response.get("attempt"), int) or response["attempt"] < 1:
                raise RuntimeError(
                    f"historical warrant replay source response {index} lacks valid attempt"
                )
            logical_group = str(response.get("logical_group", "")).strip()
            if logical_group not in {"mapping", "quote-0999", "quote-0999P"}:
                raise RuntimeError(
                    f"historical warrant replay source response {index} has invalid logical_group"
                )
            status_code = int(response.get("status_code", 0) or 0)
            if status_code:
                for field in ("raw_sha256", "normalized_sha256"):
                    if re.fullmatch(r"[0-9a-f]{64}", str(response.get(field, ""))):
                        continue
                    raise RuntimeError(
                        f"historical warrant replay source response {index} lacks valid {field}"
                    )
            accepted = response.get("accepted") is True
            if accepted:
                if response.get("status") != "accepted":
                    raise RuntimeError(
                        f"historical warrant replay accepted response {index} lacks accepted status"
                    )
                if not 200 <= status_code < 300:
                    raise RuntimeError(
                        f"historical warrant replay accepted response {index} lacks successful HTTP status"
                    )
                if int(response.get("accepted_rows", 0) or 0) < 1:
                    raise RuntimeError(
                        f"historical warrant replay accepted response {index} lacks parsed rows"
                    )
                if response.get("exact_date_match") is not True:
                    raise RuntimeError(
                        f"historical warrant replay accepted response {index} lacks exact date match"
                    )
                if response.get("observed_response_dates") != [result["requested_date"]]:
                    raise RuntimeError(
                        "historical warrant replay accepted response date evidence mismatch"
                    )
                source_name = str(response.get("source_name", ""))
                accepted_logical_groups.add(logical_group)
                if source_name.startswith("TWSE_WARRANT_STOCK_"):
                    accepted_exact_families.add("mapping")
                if source_name.startswith("TWSE_MI_INDEX_"):
                    accepted_exact_families.add("quote")
                    if source_name.startswith("TWSE_MI_INDEX_0999P_"):
                        accepted_quote_types.add("0999P")
                    elif source_name.startswith("TWSE_MI_INDEX_0999_"):
                        accepted_quote_types.add("0999")
            elif not str(response.get("error", "")).strip():
                raise RuntimeError(
                    f"historical warrant replay rejected response {index} lacks error evidence"
                )
        if accepted_exact_families != {"mapping", "quote"}:
            raise RuntimeError(
                "historical warrant replay requires accepted exact-date mapping and quote responses"
            )
        if accepted_quote_types != {"0999", "0999P"}:
            raise RuntimeError(
                "historical warrant replay requires accepted exact-date quote types 0999 and 0999P"
            )
        if accepted_logical_groups != {"mapping", "quote-0999", "quote-0999P"}:
            raise RuntimeError(
                "historical warrant replay requires complete accepted logical source groups"
            )
    return result


def write_source_status(
    status: dict[str, Any],
    *,
    source_status_json_path: Path | None = None,
    source_status_md_path: Path | None = None,
) -> None:
    source_status_json_path = source_status_json_path or SOURCE_STATUS_JSON
    source_status_md_path = source_status_md_path or SOURCE_STATUS_MD
    source_status_json_path.parent.mkdir(parents=True, exist_ok=True)
    source_status_md_path.parent.mkdir(parents=True, exist_ok=True)
    source_status_json_path.write_text(
        json.dumps(status, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Warrant Source Status",
        "",
        f"- generated_at: `{status.get('generated_at', '')}`",
        f"- status: `{status.get('status', '')}`",
        f"- requested_date: `{status.get('requested_date', '')}`",
        f"- data_date: `{status.get('data_date', '')}`",
        f"- consecutive_unavailable_trading_days: `{status.get('consecutive_unavailable_trading_days', '')}`",
        f"- max_warning_days: `{status.get('max_warning_days', '')}`",
        f"- hard_fail_after_days: `{status.get('hard_fail_after_days', '')}`",
        f"- daily_publish_allowed: `{status.get('daily_publish_allowed', '')}`",
        f"- warrant_pdf_visibility: `{status.get('warrant_pdf_visibility', '')}`",
        f"- model_effect_allowed: `{status.get('model_effect_allowed', '')}`",
        f"- pdf_effect_allowed: `{status.get('pdf_effect_allowed', '')}`",
        f"- final_rows: `{status.get('final_rows', '')}`",
        f"- mapping_rows: `{status.get('mapping_rows', '')}`",
        f"- quote_rows: `{status.get('quote_rows', '')}`",
        f"- note: {status.get('note', '')}",
    ]
    source_status_md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_historical_replay_output(
    *,
    requested_date: str,
    data_date: str,
    mapping: pd.DataFrame,
    quotes: pd.DataFrame,
    out: pd.DataFrame,
) -> None:
    if normalize_date_value(data_date) != requested_date:
        raise RuntimeError(
            f"historical warrant replay response date mismatch: {data_date} != {requested_date}"
        )
    if mapping.empty:
        raise RuntimeError("historical warrant replay mapping output is empty")
    if quotes.empty or not has_usable_quote_rows(quotes):
        raise RuntimeError("historical warrant replay quote output has no usable rows")
    if out.empty or not has_usable_quote_rows(out):
        raise RuntimeError("historical warrant replay merged output has no usable rows")

    if "warrant_id" not in mapping.columns:
        raise RuntimeError("historical warrant replay mapping output lacks warrant_id")
    if mapping["warrant_id"].astype(str).duplicated().any():
        raise RuntimeError("historical warrant replay mapping warrant_id is not unique")
    required_quote_columns = {"market", "warrant_id"}
    missing_quote_columns = sorted(required_quote_columns - set(quotes.columns))
    if missing_quote_columns:
        raise RuntimeError(
            "historical warrant replay quote output lacks columns: "
            + ",".join(missing_quote_columns)
        )
    quote_keys = list(
        zip(
            quotes["market"].astype(str).str.strip(),
            quotes["warrant_id"].astype(str).str.strip(),
        )
    )
    if any(not market or not warrant_id for market, warrant_id in quote_keys):
        raise RuntimeError("historical warrant replay quote output has blank primary-key values")
    if len(quote_keys) != len(set(quote_keys)):
        raise RuntimeError("historical warrant replay quote primary key is not unique")

    required_output_columns = {"date", "market", "warrant_id"}
    missing_output_columns = sorted(required_output_columns - set(out.columns))
    if missing_output_columns:
        raise RuntimeError(
            "historical warrant replay merged output lacks columns: "
            + ",".join(missing_output_columns)
        )
    normalized_out_dates = out["date"].map(normalize_date_value)
    invalid_date_rows = normalized_out_dates != requested_date
    if invalid_date_rows.any():
        invalid_examples = out.loc[invalid_date_rows, "date"].astype(str).head(10).tolist()
        raise RuntimeError(
            "historical warrant replay merged output has non-exact date rows: "
            f"count={int(invalid_date_rows.sum())} examples={invalid_examples}"
        )
    if out.duplicated(subset=["date", "market", "warrant_id"]).any():
        raise RuntimeError("historical warrant replay merged output primary key is not unique")

    output_keys = list(
        zip(
            out["market"].astype(str).str.strip(),
            out["warrant_id"].astype(str).str.strip(),
        )
    )
    if any(not market or not warrant_id for market, warrant_id in output_keys):
        raise RuntimeError("historical warrant replay merged output has blank primary-key values")
    quote_key_set = set(quote_keys)
    output_key_set = set(output_keys)
    if len(output_keys) != len(quote_keys) or output_key_set != quote_key_set:
        missing_keys = sorted(quote_key_set - output_key_set)
        unexpected_keys = sorted(output_key_set - quote_key_set)
        raise RuntimeError(
            "historical warrant replay merge lost or added quote rows: "
            f"quote_rows={len(quote_keys)} output_rows={len(output_keys)} "
            f"missing_count={len(missing_keys)} unexpected_count={len(unexpected_keys)} "
            f"missing_examples={missing_keys[:10]} unexpected_examples={unexpected_keys[:10]}"
        )


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
    parser.add_argument("--historical-replay", action="store_true")
    parser.add_argument("--require-live-fetch", action="store_true")
    args = parser.parse_args()

    if args.historical_replay and not (args.require_live_fetch and args.require_current_usable):
        raise RuntimeError(
            "--historical-replay requires --require-live-fetch and --require-current-usable"
        )
    if args.require_live_fetch and not args.historical_replay:
        raise RuntimeError("--require-live-fetch is valid only with --historical-replay")

    requested_date = args.date.strip() or get_latest_price_date()
    if args.historical_replay:
        requested_date = require_calendar_date(requested_date, "historical warrant replay --date")
    deadline = time.monotonic() + FETCH_MAX_SECONDS
    reset_fetch_response_provenance()

    fetch_kwargs = {"deadline": deadline}
    if args.require_current_usable or args.historical_replay:
        fetch_kwargs["lookback_days"] = 0
    if args.historical_replay:
        fetch_kwargs["require_exact_response_date"] = True

    (
        date_str,
        mapping,
        quotes,
        out,
        logs,
        debug_rows,
        fallback_warning,
    ) = fetch_warrant_data_with_quote_fallback(requested_date, **fetch_kwargs)
    if args.historical_replay:
        validate_historical_replay_output(
            requested_date=requested_date,
            data_date=date_str,
            mapping=mapping,
            quotes=quotes,
            out=out,
        )
        warning = fallback_warning
        source_status = attach_replay_provenance(
            build_source_status(
                requested_date=requested_date,
                data_date=date_str,
                usable=True,
                final_rows=len(out),
                mapping_rows=len(mapping),
                quote_rows=len(quotes),
                note=warning or "current-date stock-level warrant data is usable",
            ),
            historical_replay=True,
            requested_date=requested_date,
            data_date=date_str,
            fallback_used=False,
        )

        # Historical replay is deliberately compute -> validate -> publish.  No
        # latest/history/status/debug file is touched before every exact-date,
        # logical-source-group, usable-row, merge, and PK gate above passes.
        history_target = HISTORY_DIR / f"warrant_daily_{date_str}.csv"
        for parent in {
            RAW_LATEST.parent,
            history_target.parent,
            FETCH_STATUS_MD.parent,
            SOURCE_STATUS_JSON.parent,
            SOURCE_STATUS_MD.parent,
            DEBUG_MD.parent,
            DEBUG_CSV.parent,
        }:
            parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix=".historical-warrant-replay-",
            dir=str(RAW_LATEST.parent.resolve()),
        ) as temporary_dir:
            stage_root = Path(temporary_dir)
            stage_raw = stage_root / "warrant_daily_raw_latest.csv"
            stage_history = stage_root / f"warrant_daily_{date_str}.csv"
            stage_fetch_status = stage_root / "warrant_daily_fetch_latest.md"
            stage_source_json = stage_root / "warrant_source_status_latest.json"
            stage_source_md = stage_root / "warrant_source_status_latest.md"
            stage_debug_md = stage_root / "warrant_fetch_debug_latest.md"
            stage_debug_csv = stage_root / "warrant_fetch_debug_latest.csv"

            out.to_csv(stage_raw, index=False, encoding="utf-8-sig")
            out.to_csv(stage_history, index=False, encoding="utf-8-sig")
            write_debug(
                debug_rows,
                extra_note=(
                    f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}, "
                    f"final_rows={len(out)}"
                ),
                debug_md_path=stage_debug_md,
                debug_csv_path=stage_debug_csv,
            )
            write_status(
                date_str=date_str,
                rows=len(out),
                mapping_rows=len(mapping),
                quote_rows=len(quotes),
                logs=logs,
                warning=warning,
                requested_date=requested_date,
                fetch_status_path=stage_fetch_status,
            )
            write_source_status(
                source_status,
                source_status_json_path=stage_source_json,
                source_status_md_path=stage_source_md,
            )

            staged_paths = [
                (stage_raw, RAW_LATEST),
                (stage_history, history_target),
                (stage_fetch_status, FETCH_STATUS_MD),
                (stage_source_json, SOURCE_STATUS_JSON),
                (stage_source_md, SOURCE_STATUS_MD),
                (stage_debug_md, DEBUG_MD),
            ]
            if stage_debug_csv.is_file():
                staged_paths.append((stage_debug_csv, DEBUG_CSV))
            commit_staged_paths(staged_paths, stage_root / "rollback")
        print(f"Saved: {RAW_LATEST}, rows={len(out)}")
        print(f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}")
        return 0

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    write_debug(
        debug_rows,
        extra_note=f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}, final_rows={len(out)}",
    )

    if out.empty or not has_usable_quote_rows(out):
        if args.require_live_fetch:
            fallback_path, fallback_raw, fallback_date = None, pd.DataFrame(), ""
        else:
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
            write_source_status(
                attach_replay_provenance(
                    build_source_status(
                        requested_date=requested_date,
                        data_date=fallback_date,
                        usable=True,
                        final_rows=len(fallback_raw),
                        mapping_rows=len(mapping),
                        quote_rows=len(quotes),
                        note=f"preserved existing same-date usable raw snapshot from {fallback_path}",
                    ),
                    historical_replay=args.historical_replay,
                    requested_date=requested_date,
                    data_date=fallback_date,
                    fallback_used=True,
                )
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
            write_source_status(
                attach_replay_provenance(
                    build_source_status(
                        requested_date=requested_date,
                        data_date=date_str,
                        usable=False,
                        final_rows=len(out),
                        mapping_rows=len(mapping),
                        quote_rows=len(quotes),
                        note=warning,
                    ),
                    historical_replay=args.historical_replay,
                    requested_date=requested_date,
                    data_date=date_str,
                    fallback_used=False,
                )
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
        write_source_status(
            attach_replay_provenance(
                build_source_status(
                    requested_date=requested_date,
                    data_date=date_str,
                    usable=False,
                    final_rows=0,
                    mapping_rows=len(mapping),
                    quote_rows=len(quotes),
                    note="current-date stock-level warrant raw data is unavailable",
                ),
                historical_replay=args.historical_replay,
                requested_date=requested_date,
                data_date=date_str,
                fallback_used=False,
            )
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
    write_source_status(
        attach_replay_provenance(
            build_source_status(
                requested_date=requested_date,
                data_date=date_str,
                usable=True,
                final_rows=len(out),
                mapping_rows=len(mapping),
                quote_rows=len(quotes),
                note=warning or "current-date stock-level warrant data is usable",
            ),
            historical_replay=args.historical_replay,
            requested_date=requested_date,
            data_date=date_str,
            fallback_used=False,
        )
    )

    print(f"Saved: {RAW_LATEST}, rows={len(out)}")
    print(f"mapping_rows={len(mapping)}, quote_rows={len(quotes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
