from __future__ import annotations

import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import time
from typing import Any, Sequence
from zoneinfo import ZoneInfo

import pandas as pd
import requests


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_DIR = Path("output/history/market_abnormal_status")
DATA_DIR = Path("data/market_abnormal_status")
BUNDLE_ROOT = DATA_DIR / "bundles"

OUT_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"
OUT_MD = LATEST_DIR / "market_abnormal_status_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
HISTORY_CSV = HISTORY_DIR / "market_abnormal_status_history.csv"

BUNDLE_SCHEMA_VERSION = "market_abnormal_status_raw_bundle/v1"
HISTORICAL_UNAVAILABLE_REASON = "exact_target_raw_bundle_unavailable"
FETCH_ATTEMPTS = 3
TRANSPORT_BACKOFF_SECONDS = (1.0, 2.0)
CONTENT_BACKOFF_SECONDS = (0.25, 0.5)
MAX_RETRY_AFTER_SECONDS = 30.0
SOURCE_URLS = {
    "twse_disposition": "https://openapi.twse.com.tw/v1/announcement/punish",
    "twse_attention": "https://openapi.twse.com.tw/v1/announcement/notice",
    "twse_attention_note": "https://openapi.twse.com.tw/v1/announcement/notetrans",
    "tpex_disposition": "https://www.tpex.org.tw/openapi/v1/tpex_disposal_information",
    "tpex_attention": "https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_information",
    "tpex_attention_note": "https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_note",
    "tpex_trading_mode": "https://www.tpex.org.tw/openapi/v1/tpex_cmode",
}
SOURCE_REQUIRED_COLUMNS = {
    "twse_disposition": (
        "Date",
        "Code",
        "Name",
        "NumberOfAnnouncement",
        "ReasonsOfDisposition",
        "DispositionPeriod",
        "DispositionMeasures",
        "Detail",
    ),
    "twse_attention": (
        "Date",
        "Code",
        "Name",
        "NumberOfAnnouncement",
        "TradingInfoForAttention",
    ),
    "twse_attention_note": (
        "Code",
        "Name",
        "RecentlyMetAttentionSecuritiesCriteria",
    ),
    "tpex_disposition": (
        "Date",
        "SecuritiesCompanyCode",
        "CompanyName",
        "DispositionPeriod",
        "DispositionReasons",
        "DisposalCondition",
    ),
    "tpex_attention": (
        "Date",
        "SecuritiesCompanyCode",
        "CompanyName",
        "TradingInformation",
    ),
    "tpex_attention_note": (
        "Date",
        "SecuritiesCompanyCode",
        "CompanyName",
        "AccumulationSituation",
    ),
    "tpex_trading_mode": (
        "Date",
        "SecuritiesCompanyCode",
        "CompanyName",
        "AlteredTrading",
        "PeriodicTrading",
        "ManagedStock",
        "MatchingFrequency",
        "SuspensionOfTrading",
    ),
}
SOURCE_STOCK_ID_COLUMN = {
    "twse_disposition": "Code",
    "twse_attention": "Code",
    "twse_attention_note": "Code",
    "tpex_disposition": "SecuritiesCompanyCode",
    "tpex_attention": "SecuritiesCompanyCode",
    "tpex_attention_note": "SecuritiesCompanyCode",
    "tpex_trading_mode": "SecuritiesCompanyCode",
}

BOOL_COLUMNS = [
    "is_disposition",
    "is_attention",
    "is_attention_accumulation",
    "is_altered_trading",
    "is_periodic_trading",
    "is_managed_stock",
    "is_suspension",
]
LEGACY_LATEST_COLUMNS = [
    "fetch_date",
    "fetched_at",
    "stock_id",
    "stock_name",
    "source_market",
    "market_abnormal_status",
    "market_abnormal_risk_level",
    *BOOL_COLUMNS,
    "announcement_date",
    "source_date_raw",
    "number_of_announcement",
    "disposition_period",
    "disposition_measures",
    "disposition_reason",
    "attention_reason",
    "attention_accumulation_note",
    "trading_mode_note",
    "execution_risk_note",
    "source_name",
    "source_url",
    "data_quality_status",
]
LATEST_COLUMNS = [
    "target_date",
    *LEGACY_LATEST_COLUMNS,
]

DIRECT_SOURCE_SPECS = {
    "twse_disposition": {
        "market": "TWSE",
        "stock_id": "Code",
        "stock_name": "Name",
        "flag": "is_disposition",
        "fields": {
            "announcement_date": "Date",
            "number_of_announcement": "NumberOfAnnouncement",
            "disposition_period": "DispositionPeriod",
            "disposition_measures": "DispositionMeasures",
            "disposition_reason": "ReasonsOfDisposition",
        },
    },
    "twse_attention": {
        "market": "TWSE",
        "stock_id": "Code",
        "stock_name": "Name",
        "flag": "is_attention",
        "fields": {
            "announcement_date": "Date",
            "number_of_announcement": "NumberOfAnnouncement",
            "attention_reason": "TradingInfoForAttention",
        },
    },
    "twse_attention_note": {
        "market": "TWSE",
        "stock_id": "Code",
        "stock_name": "Name",
        "flag": "is_attention_accumulation",
        "fields": {
            "attention_accumulation_note": "RecentlyMetAttentionSecuritiesCriteria",
        },
    },
    "tpex_disposition": {
        "market": "TPEx",
        "stock_id": "SecuritiesCompanyCode",
        "stock_name": "CompanyName",
        "flag": "is_disposition",
        "fields": {
            "announcement_date": "Date",
            "disposition_period": "DispositionPeriod",
            "disposition_reason": "DispositionReasons",
            "disposition_measures": "DisposalCondition",
        },
    },
    "tpex_attention": {
        "market": "TPEx",
        "stock_id": "SecuritiesCompanyCode",
        "stock_name": "CompanyName",
        "flag": "is_attention",
        "fields": {
            "announcement_date": "Date",
            "attention_reason": "TradingInformation",
        },
    },
    "tpex_attention_note": {
        "market": "TPEx",
        "stock_id": "SecuritiesCompanyCode",
        "stock_name": "CompanyName",
        "flag": "is_attention_accumulation",
        "fields": {
            "announcement_date": "Date",
            "attention_accumulation_note": "AccumulationSituation",
        },
    },
}


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def format_taipei(value: datetime) -> str:
    return value.astimezone(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def parse_target_date(value: str) -> str:
    text = str(value or "").strip()
    if re.fullmatch(r"20\d{6}", text) is None:
        raise ValueError(f"target_date must be exact YYYYMMDD: {text!r}")
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise ValueError(f"target_date is not a calendar date: {text!r}") from exc
    return text


def normalize_stock_id(value: Any) -> str:
    text = str(value or "").strip()
    return text if re.fullmatch(r"\d{4}", text) else ""


def normalize_source_date(value: Any) -> str:
    text = str(value or "").strip()
    digits = re.sub(r"\D", "", text)
    normalized = ""
    if len(digits) == 8 and digits.startswith("20"):
        normalized = digits
    elif len(digits) == 7:
        try:
            normalized = f"{int(digits[:3]) + 1911:04d}{digits[3:]}"
        except ValueError:
            return ""
    if not normalized:
        return ""
    try:
        datetime.strptime(normalized, "%Y%m%d")
    except ValueError:
        return ""
    return normalized


def extract_roc_text_dates(value: Any) -> list[str]:
    text = str(value or "").strip()
    normalized: list[str] = []
    patterns = (
        re.compile(r"(?<!\d)(\d{3})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日"),
        re.compile(r"(?<!\d)(20\d{2})[/-](\d{1,2})[/-](\d{1,2})(?!\d)"),
        re.compile(r"(?<!\d)(20\d{6}|\d{7})(?!\d)"),
    )
    for pattern in patterns:
        for match in pattern.finditer(text):
            if len(match.groups()) == 3:
                year_text, month_text, day_text = match.groups()
                year = int(year_text)
                if len(year_text) == 3:
                    year += 1911
                candidate = f"{year:04d}{int(month_text):02d}{int(day_text):02d}"
            else:
                candidate = normalize_source_date(match.group(1))
            candidate = normalize_source_date(candidate)
            if candidate:
                normalized.append(candidate)
    return sorted(set(normalized))


def source_row_date(source_name: str, row: pd.Series) -> str:
    if source_name == "twse_attention_note":
        dates = extract_roc_text_dates(
            row.get("RecentlyMetAttentionSecuritiesCriteria", "")
        )
        return max(dates) if dates else ""
    return normalize_source_date(row.get("Date", ""))


def is_empty_sentinel(row: pd.Series) -> bool:
    return all(
        pd.isna(value) or str(value).strip() in {"", "0", "0.0"}
        for value in row.values
    )


def validate_source_frame(
    source_name: str,
    frame: pd.DataFrame,
    *,
    target_date: str,
) -> None:
    if source_name not in SOURCE_URLS:
        raise ValueError(f"unknown market-abnormal source: {source_name!r}")
    if frame.empty:
        raise ValueError(f"market-abnormal source is empty: {source_name}")
    if frame.columns.has_duplicates:
        raise ValueError(f"market-abnormal source has duplicate columns: {source_name}")
    columns = [str(column) for column in frame.columns]
    if any(not column.strip() for column in columns):
        raise ValueError(f"market-abnormal source has a blank column: {source_name}")
    required = set(SOURCE_REQUIRED_COLUMNS[source_name])
    missing = sorted(required - set(columns))
    if missing:
        raise ValueError(
            f"market-abnormal source schema mismatch: source={source_name} missing={missing}"
        )
    for column in frame.columns:
        for value in frame[column]:
            if isinstance(value, (dict, list, tuple, set)):
                raise ValueError(
                    "market-abnormal source contains nested JSON cells: "
                    f"source={source_name} column={column!r}"
                )
    stock_column = SOURCE_STOCK_ID_COLUMN[source_name]
    for row_index, row in frame.iterrows():
        source_code = str(row.get(stock_column, "") or "").strip().upper()
        if not source_code:
            if is_empty_sentinel(row):
                continue
            raise ValueError(
                "market-abnormal source row has no valid stock_id and is not an empty sentinel: "
                f"source={source_name} row={row_index}"
            )
        if re.fullmatch(r"(?=.*\d)[0-9A-Z]{4,6}", source_code) is None:
            raise ValueError(
                "market-abnormal source row has an invalid security code: "
                f"source={source_name} row={row_index} source_code={source_code!r}"
            )
        row_date = source_row_date(source_name, row)
        if not row_date:
            raise ValueError(
                "market-abnormal target-sensitive row has no verifiable date: "
                f"source={source_name} row={row_index} source_code={source_code}"
            )
        if row_date > target_date:
            raise ValueError(
                "market-abnormal target-sensitive row is newer than target_date: "
                f"source={source_name} row={row_index} source_code={source_code} "
                f"row_date={row_date} target_date={target_date}"
            )


def parse_json_source_bytes(source_name: str, payload: bytes) -> pd.DataFrame:
    try:
        decoded = payload.decode("utf-8-sig")
        data = json.loads(decoded)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"market-abnormal source is not valid UTF-8 JSON: {source_name}"
        ) from exc
    if not isinstance(data, list) or not data:
        raise ValueError(
            f"market-abnormal source JSON must be a non-empty list: {source_name}"
        )
    if any(not isinstance(row, dict) for row in data):
        raise ValueError(
            f"market-abnormal source JSON rows must be objects: {source_name}"
        )
    return pd.DataFrame(data)


def manifest_path_for(target_date: str) -> Path:
    return BUNDLE_ROOT / target_date / "manifest.json"


def source_path_for(target_date: str, source_name: str) -> Path:
    return BUNDLE_ROOT / target_date / "sources" / f"{source_name}.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def retry_after_seconds(response: requests.Response | None) -> float | None:
    if response is None:
        return None
    raw_value = str(response.headers.get("Retry-After", "")).strip()
    if not raw_value:
        return None
    try:
        seconds = float(raw_value)
    except ValueError:
        try:
            retry_at = parsedate_to_datetime(raw_value)
        except (TypeError, ValueError, OverflowError):
            return None
        if retry_at.tzinfo is None:
            retry_at = retry_at.replace(tzinfo=timezone.utc)
        seconds = (retry_at - datetime.now(timezone.utc)).total_seconds()
    return min(max(seconds, 0.0), MAX_RETRY_AFTER_SECONDS)


def retryable_http_status(status_code: int) -> bool:
    return status_code in {408, 425, 429} or 500 <= status_code <= 599


def fetch_live_source(
    source_name: str,
    source_url: str,
    *,
    target_date: str,
) -> bytes:
    last_error: Exception | None = None
    for attempt in range(1, FETCH_ATTEMPTS + 1):
        response: requests.Response | None = None
        try:
            response = requests.get(source_url, timeout=30)
            response.raise_for_status()
            content_type = str(response.headers.get("Content-Type", "")).lower()
            if "json" not in content_type:
                raise ValueError(
                    "market-abnormal source did not return JSON content type: "
                    f"source={source_name} content_type={content_type!r}"
                )
            payload = bytes(response.content)
            frame = parse_json_source_bytes(source_name, payload)
            validate_source_frame(source_name, frame, target_date=target_date)
            return payload
        except requests.RequestException as exc:
            last_error = exc
            status_code = int(response.status_code) if response is not None else 0
            if status_code and not retryable_http_status(status_code):
                raise RuntimeError(
                    "market-abnormal source request failed without retry: "
                    f"source={source_name} status={status_code} error={exc}"
                ) from exc
            if attempt == FETCH_ATTEMPTS:
                break
            delay = retry_after_seconds(response)
            if delay is None:
                delay = TRANSPORT_BACKOFF_SECONDS[attempt - 1]
        except ValueError as exc:
            last_error = exc
            if attempt == FETCH_ATTEMPTS:
                break
            delay = CONTENT_BACKOFF_SECONDS[attempt - 1]
        time.sleep(delay)
    raise RuntimeError(
        "market-abnormal source fetch/validation failed after bounded retries: "
        f"source={source_name} attempts={FETCH_ATTEMPTS} error={last_error}"
    ) from last_error


def fetch_all_live_sources(target_date: str) -> tuple[dict[str, bytes], str, str]:
    payloads: dict[str, bytes] = {}
    for source_name, source_url in SOURCE_URLS.items():
        payloads[source_name] = fetch_live_source(
            source_name,
            source_url,
            target_date=target_date,
        )

    fetched = now_taipei()
    fetch_date = fetched.strftime("%Y%m%d")
    if target_date != fetch_date:
        raise ValueError(
            "live current endpoints are allowed only for the Taipei collection date: "
            f"target_date={target_date} fetch_date={fetch_date}"
        )
    return payloads, fetch_date, format_taipei(fetched)


def publish_bundle_atomically(
    *,
    target_date: str,
    payloads: dict[str, bytes],
    fetch_date: str,
    fetched_at: str,
) -> Path:
    source_names = set(payloads)
    require(
        source_names in (set(), set(SOURCE_URLS)),
        f"market-abnormal source set is incomplete: {sorted(payloads)}",
    )
    BUNDLE_ROOT.mkdir(parents=True, exist_ok=True)
    final_dir = BUNDLE_ROOT / target_date
    if final_dir.exists():
        raise FileExistsError(
            f"immutable market-abnormal bundle already exists: {final_dir.as_posix()}"
        )
    staging_dir = Path(
        tempfile.mkdtemp(prefix=f".{target_date}-", dir=str(BUNDLE_ROOT))
    )
    try:
        source_entries: dict[str, dict[str, Any]] = {}
        for source_name, source_url in SOURCE_URLS.items():
            if source_name not in payloads:
                continue
            payload = payloads[source_name]
            frame = parse_json_source_bytes(source_name, payload)
            validate_source_frame(source_name, frame, target_date=target_date)
            staged_source = staging_dir / "sources" / f"{source_name}.json"
            staged_source.parent.mkdir(parents=True, exist_ok=True)
            staged_source.write_bytes(payload)
            source_entries[source_name] = {
                "source_url": source_url,
                "path": source_path_for(target_date, source_name).as_posix(),
                "raw_sha256": hashlib.sha256(payload).hexdigest(),
                "row_count": int(len(frame)),
                "columns": [str(column) for column in frame.columns],
            }
        manifest = {
            "schema_version": BUNDLE_SCHEMA_VERSION,
            "target_date": target_date,
            "fetch_date": fetch_date,
            "fetched_at": fetched_at,
            "collection_mode": (
                "live_current_endpoints"
                if payloads
                else "historical_unavailable"
            ),
            "source_count": len(payloads),
            "sources": source_entries,
        }
        if not payloads:
            manifest["reason"] = HISTORICAL_UNAVAILABLE_REASON
        (staging_dir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        os.rename(staging_dir, final_dir)
    except Exception:
        if staging_dir.exists():
            shutil.rmtree(staging_dir)
        raise
    return final_dir / "manifest.json"


def load_verified_bundle(
    target_date: str,
) -> tuple[dict[str, pd.DataFrame], dict[str, str]]:
    manifest_path = manifest_path_for(target_date)
    if not manifest_path.is_file():
        raise FileNotFoundError(
            "exact-target market-abnormal raw bundle manifest is missing: "
            f"{manifest_path.as_posix()}"
        )
    manifest_bytes = manifest_path.read_bytes()
    try:
        manifest = json.loads(manifest_bytes.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(
            f"market-abnormal raw bundle manifest is invalid JSON: {manifest_path}"
        ) from exc
    require(isinstance(manifest, dict), "market-abnormal manifest must be an object")
    collection_mode = str(manifest.get("collection_mode", ""))
    require(
        collection_mode in {"live_current_endpoints", "historical_unavailable"},
        f"market-abnormal manifest collection_mode is invalid: {collection_mode!r}",
    )
    fetch_date = parse_target_date(str(manifest.get("fetch_date", "")))
    expected_header = {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "target_date": target_date,
        "fetch_date": fetch_date,
        "collection_mode": collection_mode,
        "source_count": len(SOURCE_URLS) if collection_mode == "live_current_endpoints" else 0,
    }
    for field, expected in expected_header.items():
        require(
            manifest.get(field) == expected,
            f"market-abnormal manifest {field} mismatch: {manifest.get(field)!r}",
        )
    fetched_at = str(manifest.get("fetched_at", ""))
    try:
        parsed_fetched_at = datetime.strptime(
            fetched_at, "%Y-%m-%d %H:%M:%S Asia/Taipei"
        )
    except ValueError as exc:
        raise ValueError(
            f"market-abnormal manifest fetched_at is invalid: {fetched_at!r}"
        ) from exc
    require(
        parsed_fetched_at.strftime("%Y%m%d") == fetch_date,
        f"market-abnormal fetched_at is not on fetch_date: {fetched_at}",
    )

    entries = manifest.get("sources")
    require(isinstance(entries, dict), "market-abnormal manifest sources must be an object")
    if collection_mode == "historical_unavailable":
        require(fetch_date > target_date, "historical-unavailable fetch_date must follow target_date")
        require(entries == {}, "historical-unavailable manifest must not contain sources")
        require(
            manifest.get("reason") == HISTORICAL_UNAVAILABLE_REASON,
            "historical-unavailable manifest reason mismatch",
        )
        require(
            {path.name for path in manifest_path.parent.iterdir()} == {"manifest.json"},
            "historical-unavailable bundle must contain only its manifest",
        )
        return {}, {
            "target_date": target_date,
            "fetch_date": fetch_date,
            "fetched_at": fetched_at,
            "manifest_path": manifest_path.as_posix(),
            "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
            "access_mode": "historical_unavailable",
            "unavailable_reason": HISTORICAL_UNAVAILABLE_REASON,
        }
    require(fetch_date == target_date, "live bundle fetch_date must equal target_date")
    require(
        set(entries) == set(SOURCE_URLS),
        f"market-abnormal manifest source set mismatch: {sorted(entries)}",
    )

    bundle_dir = manifest_path.parent
    require(
        {path.name for path in bundle_dir.iterdir()} == {"manifest.json", "sources"},
        "market-abnormal bundle contains unexpected entries",
    )
    source_dir = bundle_dir / "sources"
    require(source_dir.is_dir(), "market-abnormal bundle sources path is not a directory")
    expected_raw_names = {f"{name}.json" for name in SOURCE_URLS}
    actual_source_entries = list(source_dir.iterdir())
    actual_raw_names = {path.name for path in actual_source_entries if path.is_file()}
    require(
        actual_raw_names == expected_raw_names
        and all(path.is_file() for path in actual_source_entries),
        f"market-abnormal raw source file set mismatch: {sorted(actual_raw_names)}",
    )

    sources: dict[str, pd.DataFrame] = {}
    for source_name, source_url in SOURCE_URLS.items():
        entry = entries[source_name]
        require(isinstance(entry, dict), f"invalid manifest entry: {source_name}")
        expected_path = source_path_for(target_date, source_name)
        require(entry.get("source_url") == source_url, f"source URL mismatch: {source_name}")
        require(entry.get("path") == expected_path.as_posix(), f"source path mismatch: {source_name}")
        payload = expected_path.read_bytes()
        actual_sha = hashlib.sha256(payload).hexdigest()
        require(entry.get("raw_sha256") == actual_sha, f"raw SHA-256 mismatch: {source_name}")
        frame = parse_json_source_bytes(source_name, payload)
        columns = [str(column) for column in frame.columns]
        require(entry.get("columns") == columns, f"columns mismatch: {source_name}")
        require(entry.get("row_count") == len(frame), f"row_count mismatch: {source_name}")
        validate_source_frame(source_name, frame, target_date=target_date)
        sources[source_name] = frame

    return sources, {
        "target_date": target_date,
        "fetch_date": fetch_date,
        "fetched_at": fetched_at,
        "manifest_path": manifest_path.as_posix(),
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
    }


def materialize_sources(
    target_date: str,
) -> tuple[dict[str, pd.DataFrame], dict[str, str]]:
    target_date = parse_target_date(target_date)
    collection_time = now_taipei()
    collection_date = collection_time.strftime("%Y%m%d")
    if target_date > collection_date:
        raise ValueError(
            "market-abnormal target_date cannot be in the future: "
            f"target_date={target_date} collection_date={collection_date}"
        )
    manifest_path = manifest_path_for(target_date)
    if manifest_path.parent.exists():
        sources, metadata = load_verified_bundle(target_date)
        if metadata.get("access_mode") != "historical_unavailable":
            metadata["access_mode"] = "exact_target_bundle_replay"
        return sources, metadata
    if target_date != collection_date:
        publish_bundle_atomically(
            target_date=target_date,
            payloads={},
            fetch_date=collection_date,
            fetched_at=format_taipei(collection_time),
        )
        return load_verified_bundle(target_date)
    payloads, fetch_date, fetched_at = fetch_all_live_sources(target_date)
    publish_bundle_atomically(
        target_date=target_date,
        payloads=payloads,
        fetch_date=fetch_date,
        fetched_at=fetched_at,
    )
    sources, metadata = load_verified_bundle(target_date)
    metadata["access_mode"] = "live_current_endpoints"
    return sources, metadata


def add_record(
    records: list[dict[str, Any]],
    *,
    metadata: dict[str, str],
    **kwargs: Any,
) -> None:
    stock_id = normalize_stock_id(kwargs.get("stock_id", ""))
    if not stock_id:
        return
    record = {
        "target_date": metadata["target_date"],
        "fetch_date": metadata["fetch_date"],
        "fetched_at": metadata["fetched_at"],
        "source_market": kwargs.get("source_market", ""),
        "stock_id": stock_id,
        "stock_name": str(kwargs.get("stock_name", "") or "").strip(),
        "is_disposition": bool(kwargs.get("is_disposition", False)),
        "is_attention": bool(kwargs.get("is_attention", False)),
        "is_attention_accumulation": bool(
            kwargs.get("is_attention_accumulation", False)
        ),
        "is_altered_trading": bool(kwargs.get("is_altered_trading", False)),
        "is_periodic_trading": bool(kwargs.get("is_periodic_trading", False)),
        "is_managed_stock": bool(kwargs.get("is_managed_stock", False)),
        "is_suspension": bool(kwargs.get("is_suspension", False)),
        "announcement_date": normalize_source_date(
            kwargs.get("announcement_date", "")
        ),
        "source_date_raw": str(kwargs.get("announcement_date", "") or "").strip(),
        "number_of_announcement": str(
            kwargs.get("number_of_announcement", "") or ""
        ).strip(),
        "disposition_period": str(kwargs.get("disposition_period", "") or "").strip(),
        "disposition_measures": str(
            kwargs.get("disposition_measures", "") or ""
        ).strip(),
        "disposition_reason": str(kwargs.get("disposition_reason", "") or "").strip(),
        "attention_reason": str(kwargs.get("attention_reason", "") or "").strip(),
        "attention_accumulation_note": str(
            kwargs.get("attention_accumulation_note", "") or ""
        ).strip(),
        "trading_mode_note": str(kwargs.get("trading_mode_note", "") or "").strip(),
        "source_name": kwargs.get("source_name", ""),
        "source_url": kwargs.get("source_url", ""),
        "data_quality_status": (
            "ok_exact_target_bundle_replay"
            if metadata["access_mode"] == "exact_target_bundle_replay"
            else "ok_live_current"
        ),
    }
    records.append(record)


def normalize_records(
    sources: dict[str, pd.DataFrame],
    metadata: dict[str, str],
) -> pd.DataFrame:
    if not sources:
        return pd.DataFrame(columns=LATEST_COLUMNS)
    records: list[dict[str, Any]] = []
    for source_name, spec in DIRECT_SOURCE_SPECS.items():
        for _, row in sources[source_name].iterrows():
            fields = {
                output_field: row.get(source_field, "")
                for output_field, source_field in spec["fields"].items()
            }
            if source_name == "twse_attention_note":
                fields["announcement_date"] = source_row_date(source_name, row)
            if source_name == "twse_disposition" and not fields["disposition_reason"]:
                fields["disposition_reason"] = row.get("Detail", "")
            if source_name == "tpex_disposition" and not fields["disposition_reason"]:
                fields["disposition_reason"] = row.get("DisposalCondition", "")
            add_record(
                records,
                metadata=metadata,
                source_market=spec["market"],
                stock_id=row.get(spec["stock_id"], ""),
                stock_name=row.get(spec["stock_name"], ""),
                source_name=source_name,
                source_url=SOURCE_URLS[source_name],
                **{spec["flag"]: True},
                **fields,
            )

    for _, row in sources["tpex_trading_mode"].iterrows():
        altered = str(row.get("AlteredTrading", "")).strip().upper() == "Ｙ"
        periodic = str(row.get("PeriodicTrading", "")).strip().upper() == "Ｙ"
        managed = str(row.get("ManagedStock", "")).strip().upper() == "Ｙ"
        suspended = str(row.get("SuspensionOfTrading", "")).strip().upper() == "Ｙ"
        if not any([altered, periodic, managed, suspended]):
            continue
        add_record(
            records,
            metadata=metadata,
            source_market="TPEx",
            stock_id=row.get("SecuritiesCompanyCode"),
            stock_name=row.get("CompanyName"),
            is_altered_trading=altered,
            is_periodic_trading=periodic,
            is_managed_stock=managed,
            is_suspension=suspended,
            announcement_date=row.get("Date"),
            trading_mode_note=(
                f"altered={altered}; periodic={periodic}; managed={managed}; "
                f"suspension={suspended}; matching_frequency={row.get('MatchingFrequency', '')}"
            ),
            source_name="tpex_trading_mode",
            source_url=SOURCE_URLS["tpex_trading_mode"],
        )

    if not records:
        return pd.DataFrame(columns=LATEST_COLUMNS)

    raw = pd.DataFrame(records)
    for column in BOOL_COLUMNS:
        raw[column] = raw[column].astype(bool)

    def join_unique(values: pd.Series) -> str:
        return "; ".join(
            sorted(set(str(value) for value in values if str(value).strip()))
        )

    aggregate: dict[str, Any] = {
        "target_date": "first",
        "fetch_date": "first",
        "fetched_at": "first",
        "source_market": lambda values: "/".join(join_unique(values).split("; ")),
        "stock_name": lambda values: next(
            (str(value) for value in values if str(value).strip()), ""
        ),
        "announcement_date": "max",
        "data_quality_status": "first",
    }
    for column in (
        "source_date_raw",
        "number_of_announcement",
        "disposition_period",
        "disposition_measures",
        "disposition_reason",
        "attention_reason",
        "attention_accumulation_note",
        "trading_mode_note",
        "source_name",
        "source_url",
    ):
        aggregate[column] = join_unique
    for column in BOOL_COLUMNS:
        aggregate[column] = "max"

    latest = raw.groupby("stock_id", as_index=False).agg(aggregate)

    def status(row: pd.Series) -> str:
        tags: list[str] = []
        if bool(row.get("is_disposition")):
            tags.append("disposition")
        if bool(row.get("is_attention")):
            tags.append("attention")
        if bool(row.get("is_attention_accumulation")):
            tags.append("attention_accumulation")
        if bool(row.get("is_periodic_trading")):
            tags.append("periodic_trading")
        if bool(row.get("is_altered_trading")):
            tags.append("altered_trading")
        if bool(row.get("is_managed_stock")):
            tags.append("managed_stock")
        if bool(row.get("is_suspension")):
            tags.append("suspension")
        return ";".join(tags) if tags else "normal"

    def severity(row: pd.Series) -> str:
        if bool(row.get("is_suspension")):
            return "E_suspension"
        if bool(row.get("is_disposition")) or bool(row.get("is_periodic_trading")):
            return "D_disposition_or_periodic"
        if bool(row.get("is_attention")) or bool(
            row.get("is_attention_accumulation")
        ):
            return "C_attention"
        if bool(row.get("is_altered_trading")) or bool(row.get("is_managed_stock")):
            return "B_trading_mode_watch"
        return "A_normal"

    latest["market_abnormal_status"] = latest.apply(status, axis=1)
    latest["market_abnormal_risk_level"] = latest.apply(severity, axis=1)
    latest["execution_risk_note"] = latest.apply(
        lambda row: (
            "處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。"
            if row["market_abnormal_status"] != "normal"
            else ""
        ),
        axis=1,
    )
    return (
        latest[LATEST_COLUMNS]
        .sort_values(
            ["market_abnormal_risk_level", "stock_id"],
            ascending=[False, True],
        )
        .reset_index(drop=True)
    )


def build_history(latest: pd.DataFrame) -> pd.DataFrame:
    if HISTORY_CSV.exists():
        history = pd.read_csv(HISTORY_CSV, dtype=str, keep_default_na=False)
        actual_columns = list(history.columns)
        if actual_columns == LEGACY_LATEST_COLUMNS:
            history.insert(0, "target_date", "")
        elif actual_columns != LATEST_COLUMNS:
            raise ValueError(
                "market-abnormal history schema mismatch: "
                f"expected legacy/current schema, actual={actual_columns}"
            )
    else:
        history = pd.DataFrame(columns=LATEST_COLUMNS)
    combined = pd.concat([history, latest.astype(str)], ignore_index=True)
    legacy = combined.loc[combined["target_date"].eq("")].copy()
    verified = combined.loc[combined["target_date"].ne("")].copy()
    verified = verified.drop_duplicates(
        subset=["target_date", "stock_id"], keep="last"
    )
    return pd.concat([legacy, verified], ignore_index=True)[LATEST_COLUMNS]


def dataframe_csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8-sig")


def atomic_write_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except Exception:
        if temp_path.exists():
            temp_path.unlink()
        raise


def build_markdown(
    latest: pd.DataFrame,
    sources: dict[str, pd.DataFrame],
    metadata: dict[str, str],
) -> str:
    lines: list[str] = []
    lines.append("# Market Abnormal Status Latest")
    lines.append("")
    lines.append(f"- target_date: `{metadata['target_date']}`")
    lines.append(f"- fetch_date: `{metadata['fetch_date']}`")
    lines.append(f"- fetched_at: `{metadata['fetched_at']}`")
    lines.append(f"- access_mode: `{metadata['access_mode']}`")
    lines.append(f"- raw_bundle_manifest: `{metadata['manifest_path']}`")
    lines.append(
        f"- raw_bundle_manifest_sha256: `{metadata['manifest_sha256']}`"
    )
    lines.append(
        "- source: TWSE / TPEx official OpenAPI"
        if metadata["access_mode"] != "historical_unavailable"
        else "- intended_source: TWSE / TPEx official OpenAPI (not available for this target date)"
    )
    lines.append(
        "- usage: execution-risk flag for daily candidate, short-term research, and backtest segmentation."
    )
    lines.append(
        "- limitation: legacy history rows with blank target_date predate exact-target bundle lineage and must not be used as point-in-time evidence."
    )
    lines.append("")
    if metadata["access_mode"] == "historical_unavailable":
        lines.append("## Availability")
        lines.append("")
        lines.append(f"- status: `historical_unavailable`")
        lines.append(f"- reason: `{metadata['unavailable_reason']}`")
        lines.append("- interpretation: advisory execution-risk status was not checked; no stock may be inferred normal from this empty snapshot.")
        lines.append("")
        return "\n".join(lines) + "\n"
    source_rows = [
        [name, "verified", len(sources[name]), url]
        for name, url in SOURCE_URLS.items()
    ]
    lines.append("## Source Status")
    lines.append(
        pd.DataFrame(
            source_rows, columns=["source", "status", "rows", "url"]
        ).to_markdown(index=False)
    )
    lines.append("")
    if latest.empty:
        lines.append("_No abnormal status rows._")
        return "\n".join(lines) + "\n"
    lines.append("## Counts")
    counts = latest["market_abnormal_status"].value_counts().reset_index()
    counts.columns = ["market_abnormal_status", "count"]
    lines.append(counts.to_markdown(index=False))
    lines.append("")
    lines.append("## Current Stocks")
    show_columns = [
        "stock_id",
        "stock_name",
        "source_market",
        "market_abnormal_status",
        "market_abnormal_risk_level",
        "disposition_period",
        "disposition_reason",
        "attention_reason",
        "attention_accumulation_note",
        "execution_risk_note",
    ]
    lines.append(latest[show_columns].head(120).to_markdown(index=False))
    lines.append("")
    return "\n".join(lines) + "\n"


def run(target_date: str) -> dict[str, Any]:
    target_date = parse_target_date(target_date)
    sources, metadata = materialize_sources(target_date)
    latest = normalize_records(sources, metadata)
    history = build_history(latest)
    markdown = build_markdown(latest, sources, metadata).encode("utf-8")

    csv_payload = dataframe_csv_bytes(latest)
    history_payload = dataframe_csv_bytes(history)
    for path in (OUT_CSV, DOCS_CSV):
        atomic_write_bytes(path, csv_payload)
    atomic_write_bytes(HISTORY_CSV, history_payload)
    for path in (OUT_MD, DOCS_MD):
        atomic_write_bytes(path, markdown)
    return {
        "target_date": target_date,
        "fetch_date": metadata["fetch_date"],
        "fetched_at": metadata["fetched_at"],
        "access_mode": metadata["access_mode"],
        "manifest_path": metadata["manifest_path"],
        "manifest_sha256": metadata["manifest_sha256"],
        "latest_rows": len(latest),
        "history_rows": len(history),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Build exact-target TWSE/TPEx market-abnormal status from a complete "
            "immutable raw bundle."
        )
    )
    parser.add_argument("--target-date", required=True, help="Exact YYYYMMDD target date")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run(args.target_date)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
