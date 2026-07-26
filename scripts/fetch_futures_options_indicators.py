from __future__ import annotations

from io import StringIO
from pathlib import Path
import tempfile
from datetime import datetime
from typing import Any
import shutil
import argparse
import json
import math
import hashlib

import pandas as pd
import requests

from tracking_utils import (
    LATEST_DIR,
    DATA_DIR,
    append_update_csv,
    latest_price_date,
    main_price_date_from_freshness,
    month_starts_back,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


FO_DIR = DATA_DIR / "futures_options"
RAW_DIR = FO_DIR / "raw"

TAIFEX_OPEN_DATA_URL = "https://www.taifex.com.tw/data_gov/taifex_open_data.asp"
VIX_FILE_URL = "https://www.taifex.com.tw/file/taifex/Dailydownload/vix/log2data/{yyyymm}new.txt"
TAIFEX_HISTORICAL_ENDPOINTS = {
    "institutional_fo": "https://www.taifex.com.tw/cht/3/futAndOptDateDown",
    "futures_contracts": "https://www.taifex.com.tw/cht/3/futContractsDateDown",
    "options_call_put": "https://www.taifex.com.tw/cht/3/callsAndPutsDateDown",
    "put_call_ratio": "https://www.taifex.com.tw/cht/3/pcRatioDown",
}

SOURCES = {
    "institutional_fo": "MarketDataOfMajorInstitutionalTradersDividedByFuturesAndOptionsBytheDate",
    "futures_contracts": "MarketDataOfMajorInstitutionalTradersDetailsOfFuturesContractsBytheDate",
    "options_call_put": "MarketDataOfMajorInstitutionalTradersDetailsOfCallsAndPutsBytheDate",
    "put_call_ratio": "PutCallRatio",
}

HISTORY_FILES = {
    "institutional_fo": FO_DIR / "taifex_institutional_fo_history.csv",
    "futures_contracts": FO_DIR / "taifex_futures_contracts_history.csv",
    "options_call_put": FO_DIR / "taifex_options_call_put_history.csv",
    "put_call_ratio": FO_DIR / "put_call_ratio_history.csv",
    "taiwan_vix": FO_DIR / "taiwan_vix_history.csv",
}

LATEST_FILES = {
    "institutional_fo": LATEST_DIR / "futures_options_institutional_fo_latest.csv",
    "futures_contracts": LATEST_DIR / "futures_options_contracts_latest.csv",
    "options_call_put": LATEST_DIR / "futures_options_call_put_latest.csv",
    "put_call_ratio": LATEST_DIR / "futures_options_put_call_ratio_latest.csv",
    "taiwan_vix": LATEST_DIR / "taiwan_vix_latest.csv",
}

INDICATORS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
STATUS_JSON = LATEST_DIR / "futures_options_source_status_latest.json"
STATUS_MD = LATEST_DIR / "futures_options_source_status_latest.md"


def decode_response(content: bytes) -> str:
    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5"]:
        try:
            return content.decode(encoding)
        except UnicodeDecodeError:
            continue
    return content.decode("utf-8", errors="replace")


def decode_response_with_metadata(content: bytes) -> tuple[str, str]:
    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5"]:
        try:
            return content.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    return content.decode("utf-8", errors="replace"), "utf-8-replace"


def sha256_hex(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def commit_staged_paths(staged_paths: list[tuple[Path, Path]], rollback_root: Path) -> None:
    """Replace a staged artifact set with verified rollback on any failure.

    The files are staged on the repository volume.  Every staged file is hashed
    before the first destination is touched; existing destinations are copied
    into a private rollback directory.  A failed replace or a post-replace hash
    mismatch restores every already-touched destination before re-raising.
    """

    if not staged_paths:
        return
    targets = [target.resolve() for _, target in staged_paths]
    if len(targets) != len(set(targets)):
        raise RuntimeError("duplicate destination in staged commit set")
    rollback_root.mkdir(parents=True, exist_ok=False)
    manifest: list[dict[str, Any]] = []
    for index, (staged_path, target_path) in enumerate(staged_paths):
        if not staged_path.is_file():
            raise RuntimeError(f"staged artifact missing before commit: {staged_path}")
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
            actual_sha = file_sha256(target_path)
            if actual_sha != item["sha256"]:
                raise RuntimeError(
                    f"post-replace SHA-256 mismatch for {target_path}: "
                    f"{actual_sha} != {item['sha256']}"
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
                "staged commit failed and rollback was incomplete: " + "; ".join(rollback_errors)
            )
        raise


def normalize_taifex_query_date(date_text: str) -> str:
    normalized = normalize_date(date_text)
    if not normalized:
        raise RuntimeError(f"TAIFEX historical date invalid: {date_text}")
    return f"{normalized[0:4]}/{normalized[4:6]}/{normalized[6:8]}"


def detect_date_column(df: pd.DataFrame) -> str | None:
    candidates = []
    explicit = ["日期", "交易日期", "date"]
    for col in explicit:
        if col in df.columns:
            candidates.append(col)
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        raise RuntimeError(f"ambiguous date columns: {', '.join(candidates)}")
    heuristic = []
    for col in df.columns:
        text = safe_str(col)
        if "交" in text and "日" in text:
            heuristic.append(col)
    if len(heuristic) == 1:
        return heuristic[0]
    if len(heuristic) > 1:
        raise RuntimeError(f"ambiguous date columns: {', '.join(heuristic)}")
    raise RuntimeError("missing date column")


def requested_trading_dates(start_date: str, end_date: str) -> list[str]:
    if normalize_date(start_date) > normalize_date(end_date):
        raise RuntimeError(f"TAIFEX historical date range invalid: {start_date} > {end_date}")
    dates = pd.date_range(start_date, end_date, freq="B").strftime("%Y%m%d").tolist()
    return [d for d in map(safe_str, dates)]


def parse_cli_date(raw_value: str, arg_name: str) -> str:
    normalized = normalize_date(raw_value)
    if not normalized:
        raise RuntimeError(f"{arg_name} must be YYYYMMDD (calendar-valid)")
    try:
        datetime.strptime(normalized, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError(f"{arg_name} must be YYYYMMDD (calendar-valid): {raw_value}") from exc
    return normalized


def filter_rows_exact_dates(
    df: pd.DataFrame,
    start_date: str,
    end_date: str,
    required_dates: list[str] | None = None,
) -> tuple[pd.DataFrame, list[str], list[str]]:
    date_col = detect_date_column(df)
    if date_col is None:
        raise RuntimeError("TAIFEX historical data missing expected date column")
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[work[date_col] != ""]
    if required_dates is None:
        required_dates = requested_trading_dates(start_date, end_date)
    observed_dates = sorted(set(safe_str(v) for v in work[date_col].dropna().tolist()))
    required_set = set(required_dates)
    observed_set = set(observed_dates)
    if missing_dates := sorted(required_set - observed_set):
        raise RuntimeError(f"TAIFEX historical fetch missing requested dates: {','.join(missing_dates)}")
    out_of_range_dates = sorted(observed_set - required_set)
    if out_of_range_dates:
        raise RuntimeError(f"TAIFEX historical fetch contains out-of-range dates: {','.join(out_of_range_dates)}")
    filtered = work[work[date_col].isin(required_dates)].copy()
    if filtered.empty:
        raise RuntimeError("TAIFEX historical fetch returned no in-range rows")
    return filtered, required_dates, sorted(set(safe_str(v) for v in filtered[date_col].tolist()))


def filter_rows_for_target_date(df: pd.DataFrame, target_date: str, source_name: str) -> pd.DataFrame:
    if df.empty or not target_date:
        return df
    date_col = detect_date_column(df)
    if date_col is None:
        return df
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[work[date_col] == target_date]
    if work.empty:
        raise RuntimeError(f"{source_name} has no rows for requested target_date={target_date}")
    return work


def fetch_taifex_historical(
    source_name: str,
    start_date: str,
    end_date: str,
    require_exact_source_dates: bool = True,
) -> tuple[pd.DataFrame, dict[str, Any]]:
    if source_name not in TAIFEX_HISTORICAL_ENDPOINTS:
        raise RuntimeError(f"Unsupported TAIFEX historical source: {source_name}")
    endpoint = TAIFEX_HISTORICAL_ENDPOINTS[source_name]
    params = {
        "queryStartDate": normalize_taifex_query_date(start_date),
        "queryEndDate": normalize_taifex_query_date(end_date),
    }
    response = requests.post(
        endpoint,
        data=params,
        timeout=45,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    raw_content = response.content
    text, encoding = decode_response_with_metadata(raw_content)
    if "<html" in text.lower():
        raise RuntimeError(f"TAIFEX historical endpoint returned non-CSV payload for {source_name}")
    if not text.strip():
        raise RuntimeError(f"TAIFEX historical endpoint returned empty payload for {source_name}")
    try:
        df = pd.read_csv(StringIO(text), dtype=str)
    except Exception as exc:
        raise RuntimeError(f"TAIFEX historical endpoint parse failed for {source_name}: {exc}") from exc
    if df.empty:
        raise RuntimeError(f"TAIFEX historical endpoint returned empty rows for {source_name}")
    df = normalize_dates(df)
    required_dates = requested_trading_dates(start_date, end_date)
    if require_exact_source_dates:
        df, required_dates, observed_dates = filter_rows_exact_dates(df, start_date, end_date, required_dates=required_dates)
    else:
        date_col = detect_date_column(df)
        if date_col is None:
            raise RuntimeError("TAIFEX historical data missing expected date column")
        temp = df.copy()
        temp[date_col] = temp[date_col].map(normalize_date)
        temp = temp[temp[date_col] != ""]
        observed_dates = sorted(set(safe_str(v) for v in temp[date_col].tolist()))
        df = temp
    provenance = {
        "source": source_name,
        "status": "ok",
        "fetched_at": now_text(),
        "endpoint": endpoint,
        "params": params,
        "encoding": encoding,
        "raw_sha256": sha256_hex(raw_content),
        "normalized_sha256": sha256_hex(text.encode("utf-8")),
        "requested_dates": required_dates,
        "observed_dates": observed_dates,
        "rows": len(df),
    }
    return df, provenance


def rows_have_unique_keys(df: pd.DataFrame, key_cols: list[str]) -> bool:
    missing = [col for col in key_cols if col not in df.columns]
    if missing:
        raise RuntimeError(f"missing required key columns: {','.join(missing)}")
    return not df.duplicated(subset=key_cols).any()


def fetch_open_data(data_name: str) -> pd.DataFrame:
    response = requests.get(
        TAIFEX_OPEN_DATA_URL,
        params={"data_name": data_name},
        timeout=45,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    text = decode_response(response.content)
    if "no such data" in text.lower() or "<html" in text.lower():
        raise RuntimeError(f"TAIFEX open data returned no CSV for {data_name}")
    df = pd.read_csv(StringIO(text), dtype=str)
    if df.empty:
        raise RuntimeError(f"TAIFEX open data empty for {data_name}")
    return normalize_dates(df)


def normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ["日期", "交易日期", "開始日期", "結束日期", "date"]:
        if col in out.columns:
            out[col] = out[col].map(normalize_date)
    return out


def latest_date_from_df(df: pd.DataFrame) -> str:
    for col in ["日期", "交易日期", "date"]:
        if col in df.columns:
            dates = [normalize_date(x) for x in df[col].dropna().tolist()]
            dates = [d for d in dates if d]
            if dates:
                return max(dates)
    return latest_price_date()


def raw_snapshot_path(name: str, date: str) -> Path:
    return RAW_DIR / f"{name}_{date}.csv"


def save_source(name: str, df: pd.DataFrame, key_cols: list[str]) -> pd.DataFrame:
    date = latest_date_from_df(df)
    write_csv(df, raw_snapshot_path(name, date))
    write_csv(df, LATEST_FILES[name])
    append_update_csv(df, HISTORY_FILES[name], key_cols=key_cols, sort_cols=key_cols)
    return df


def parse_vix_payload(text: str, source_url: str) -> pd.DataFrame:
    if "<html" in text.lower():
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for line in text.splitlines():
        parts = [safe_str(x) for x in line.replace(",", "\t").split("\t")]
        if not parts:
            continue
        date = normalize_date(parts[0])
        if not date:
            continue
        numeric_values = [to_number(x) for x in parts[1:]]
        numeric_values = [x for x in numeric_values if not math.isnan(x)]
        if not numeric_values:
            continue
        rows.append(
            {
                "date": date,
                "taiwan_vix": numeric_values[-1],
                "source": source_url,
            }
        )
    return pd.DataFrame(rows)


def fetch_vix_month_with_provenance(yyyymm: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    url = VIX_FILE_URL.format(yyyymm=yyyymm)
    response = requests.get(url, timeout=45, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    raw_content = response.content
    text, encoding = decode_response_with_metadata(raw_content)
    frame = parse_vix_payload(text, url)
    return frame, {
        "endpoint": url,
        "yyyymm": yyyymm,
        "encoding": encoding,
        "raw_sha256": sha256_hex(raw_content),
        "normalized_sha256": sha256_hex(text.encode("utf-8")),
        "rows": len(frame),
    }


def fetch_vix_month(yyyymm: str) -> pd.DataFrame:
    frame, _ = fetch_vix_month_with_provenance(yyyymm)
    return frame


def fetch_vix_history_with_provenance(months: int = 6) -> tuple[pd.DataFrame, dict[str, Any]]:
    latest = latest_price_date()
    frames: list[pd.DataFrame] = []
    source_files: list[dict[str, Any]] = []
    for month_start in month_starts_back(latest, months):
        frame, provenance = fetch_vix_month_with_provenance(month_start[:6])
        frames.append(frame)
        source_files.append(provenance)
    frames = [df for df in frames if not df.empty]
    if not frames:
        return pd.DataFrame(columns=["date", "taiwan_vix", "source"]), {
            "source_files": source_files,
            "rows": 0,
        }
    df = pd.concat(frames, ignore_index=True, sort=False)
    df["date"] = df["date"].map(normalize_date)
    df["taiwan_vix"] = pd.to_numeric(df["taiwan_vix"], errors="coerce")
    df = df.dropna(subset=["date", "taiwan_vix"])
    df = df.drop_duplicates(["date"], keep="last").sort_values("date").reset_index(drop=True)
    for window in [5, 10, 20]:
        df[f"vix_return_{window}d"] = df["taiwan_vix"].pct_change(window) * 100
    provenance_bytes = json.dumps(
        source_files,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return df, {
        "source_files": source_files,
        "source_manifest_sha256": sha256_hex(provenance_bytes),
        "rows": len(df),
    }


def fetch_vix_history(months: int = 6) -> pd.DataFrame:
    frame, _ = fetch_vix_history_with_provenance(months=months)
    return frame


def filter_vix_candidate_exact_dates(
    vix: pd.DataFrame,
    start_date: str,
    end_date: str,
    required_dates: list[str] | None = None,
) -> tuple[pd.DataFrame, list[str], list[str]]:
    if "date" not in vix.columns:
        raise RuntimeError("TAIFEX VIX payload missing expected date column")
    work = vix.copy()
    work["date"] = work["date"].map(normalize_date)
    work = work[work["date"] != ""]
    if required_dates is None:
        required_dates = requested_trading_dates(start_date, end_date)
    candidate = work[(work["date"] >= start_date) & (work["date"] <= end_date)].copy()
    if candidate.empty:
        raise RuntimeError("TAIFEX VIX has no rows in requested window")
    duplicate_dates = sorted(set(
        safe_str(x)
        for x in candidate["date"].tolist()
        if safe_str(x) and candidate["date"].tolist().count(safe_str(x)) > 1
    ))
    if duplicate_dates:
        raise RuntimeError(f"TAIFEX VIX has duplicate rows for dates: {','.join(duplicate_dates)}")
    return filter_rows_exact_dates(
        candidate,
        start_date,
        end_date,
        required_dates=required_dates,
    )


def identity_mask(df: pd.DataFrame, label: str) -> pd.Series:
    if "身份別" not in df.columns:
        return pd.Series(False, index=df.index)
    return df["身份別"].astype(str).str.contains(label, na=False)


def product_mask(df: pd.DataFrame, label: str) -> pd.Series:
    if "商品名稱" not in df.columns:
        return pd.Series(False, index=df.index)
    return df["商品名稱"].astype(str).str.contains(label, na=False)


def value_for(df: pd.DataFrame, identity: str, col: str, product: str | None = None, call_put: str | None = None) -> float:
    if df.empty or col not in df.columns:
        return math.nan
    part = df[identity_mask(df, identity)].copy()
    if product:
        part = part[product_mask(part, product)].copy()
    if call_put and "買賣權別" in part.columns:
        part = part[part["買賣權別"].astype(str).str.upper() == call_put.upper()].copy()
    if part.empty:
        return math.nan
    return float(sum(to_number(v) for v in part[col].tolist()))


def sum_valid(values: list[float]) -> float:
    nums = [value for value in values if not math.isnan(value)]
    if not nums:
        return math.nan
    return float(sum(nums))


def retail_mtx_proxy_from_institutional_net_oi(futures_contracts: pd.DataFrame) -> dict[str, float | str]:
    product = "小型臺指期貨"
    col = "多空未平倉口數淨額"
    dealer = value_for(futures_contracts, "自營商", col, product=product)
    trust = value_for(futures_contracts, "投信", col, product=product)
    foreign = value_for(futures_contracts, "外資", col, product=product)
    three_institution = sum_valid([dealer, trust, foreign])
    retail_proxy = -three_institution if not math.isnan(three_institution) else math.nan
    return {
        "dealer_mtx_futures_net_oi": dealer,
        "trust_mtx_futures_net_oi": trust,
        "foreign_mtx_futures_net_oi": foreign,
        "three_institution_mtx_net_oi": three_institution,
        "retail_mtx_net_oi_proxy": retail_proxy,
        "retail_mtx_proxy_method": "negative_sum_of_three_institution_mtx_net_oi",
    }


def latest_row(df: pd.DataFrame, date_col: str = "日期") -> pd.Series | None:
    if df.empty or date_col not in df.columns:
        return None
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[work[date_col] != ""].sort_values(date_col)
    if work.empty:
        return None
    return work.iloc[-1]


def latest_row_at_or_before(df: pd.DataFrame, target_date: str, date_col: str = "日期") -> pd.Series | None:
    if df.empty or date_col not in df.columns:
        return None
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[(work[date_col] != "") & (work[date_col] <= target_date)].sort_values(date_col)
    if work.empty:
        return None
    return work.iloc[-1]


def build_indicator_row(
    institutional_fo: pd.DataFrame,
    futures_contracts: pd.DataFrame,
    options_call_put: pd.DataFrame,
    put_call_ratio: pd.DataFrame,
    vix: pd.DataFrame,
    source_status: dict[str, Any],
    target_date: str | None = None,
) -> pd.DataFrame:
    is_reconstruction_target = bool(target_date)
    target_date = normalize_date(target_date or "")
    if target_date == "":
        target_date = ""
    if is_reconstruction_target and not target_date:
        raise RuntimeError("target_date must be YYYYMMDD when provided")
    if is_reconstruction_target:
        futures_contracts = filter_rows_for_target_date(futures_contracts, target_date, "futures_contracts")
        options_call_put = filter_rows_for_target_date(options_call_put, target_date, "options_call_put")
        put_call_ratio = filter_rows_for_target_date(put_call_ratio, target_date, "put_call_ratio")
        institutional_fo = filter_rows_for_target_date(institutional_fo, target_date, "institutional_fo")
    fo_date = latest_date_from_df(institutional_fo) if not institutional_fo.empty else ""
    futures_contracts_date = latest_date_from_df(futures_contracts) if not futures_contracts.empty else ""
    options_call_put_date = latest_date_from_df(options_call_put) if not options_call_put.empty else ""
    put_call_ratio_date = latest_date_from_df(put_call_ratio) if not put_call_ratio.empty else ""
    if is_reconstruction_target:
        for name, candidate_date in [
            ("institutional_fo", fo_date),
            ("futures_contracts", futures_contracts_date),
            ("options_call_put", options_call_put_date),
            ("put_call_ratio", put_call_ratio_date),
        ]:
            if candidate_date != target_date:
                raise RuntimeError(
                    f"target_date reconciliation failed for {name}: {candidate_date} != {target_date}"
                )
        date = target_date
    else:
        date = ""

    pc = latest_row(put_call_ratio)
    pc_date = safe_str(pc.get("日期", "")) if pc is not None else ""
    if not is_reconstruction_target:
        report_date = main_price_date_from_freshness() or latest_price_date()
        date = max([d for d in [fo_date, pc_date] if d] or [report_date])
        if report_date and date > report_date:
            date = report_date
    vix_latest = latest_row_at_or_before(vix, date, "date")
    vix_date = safe_str(vix_latest.get("date", "")) if vix_latest is not None else ""
    retail_mtx = retail_mtx_proxy_from_institutional_net_oi(futures_contracts)

    row = {
        "date": date,
        "generated_at": now_text(),
        "taifex_institutional_date": fo_date,
        "put_call_ratio_date": pc_date,
        "taiwan_vix_date": vix_date,
        "dealer_futures_net_oi": value_for(institutional_fo, "自營商", "期貨多空未平倉口數淨額"),
        "trust_futures_net_oi": value_for(institutional_fo, "投信", "期貨多空未平倉口數淨額"),
        "foreign_futures_net_oi": value_for(institutional_fo, "外資", "期貨多空未平倉口數淨額"),
        "dealer_options_net_oi": value_for(institutional_fo, "自營商", "選擇權多空未平倉口數淨額"),
        "trust_options_net_oi": value_for(institutional_fo, "投信", "選擇權多空未平倉口數淨額"),
        "foreign_options_net_oi": value_for(institutional_fo, "外資", "選擇權多空未平倉口數淨額"),
        "foreign_tx_futures_net_oi": value_for(futures_contracts, "外資", "多空未平倉口數淨額", product="臺股期貨"),
        "dealer_tx_futures_net_oi": value_for(futures_contracts, "自營商", "多空未平倉口數淨額", product="臺股期貨"),
        "trust_tx_futures_net_oi": value_for(futures_contracts, "投信", "多空未平倉口數淨額", product="臺股期貨"),
        "dealer_mtx_futures_net_oi": retail_mtx["dealer_mtx_futures_net_oi"],
        "trust_mtx_futures_net_oi": retail_mtx["trust_mtx_futures_net_oi"],
        "foreign_mtx_futures_net_oi": retail_mtx["foreign_mtx_futures_net_oi"],
        "three_institution_mtx_net_oi": retail_mtx["three_institution_mtx_net_oi"],
        "retail_mtx_net_oi_proxy": retail_mtx["retail_mtx_net_oi_proxy"],
        "retail_mtx_proxy_method": retail_mtx["retail_mtx_proxy_method"],
        "foreign_txo_call_net_oi": value_for(options_call_put, "外資", "未平倉口數買賣淨額", product="臺指選擇權", call_put="CALL"),
        "foreign_txo_put_net_oi": value_for(options_call_put, "外資", "未平倉口數買賣淨額", product="臺指選擇權", call_put="PUT"),
        "put_volume": to_number(pc.get("賣權成交量", "")) if pc is not None else math.nan,
        "call_volume": to_number(pc.get("買權成交量", "")) if pc is not None else math.nan,
        "put_call_volume_ratio_pct": to_number(pc.get("買賣權成交量比率%", "")) if pc is not None else math.nan,
        "put_oi": to_number(pc.get("賣權未平倉量", "")) if pc is not None else math.nan,
        "call_oi": to_number(pc.get("買權未平倉量", "")) if pc is not None else math.nan,
        "put_call_oi_ratio_pct": to_number(pc.get("買賣權未平倉量比率%", "")) if pc is not None else math.nan,
        "taiwan_vix": to_number(vix_latest.get("taiwan_vix", "")) if vix_latest is not None else math.nan,
        "vix_return_5d": to_number(vix_latest.get("vix_return_5d", "")) if vix_latest is not None else math.nan,
        "vix_return_10d": to_number(vix_latest.get("vix_return_10d", "")) if vix_latest is not None else math.nan,
        "vix_return_20d": to_number(vix_latest.get("vix_return_20d", "")) if vix_latest is not None else math.nan,
    }

    row["foreign_txo_synthetic_net_oi"] = row["foreign_txo_call_net_oi"] - row["foreign_txo_put_net_oi"]
    core_sources_ready = all(source_status.get(k) == "ok" for k in SOURCES)
    row["source_status"] = "ready" if core_sources_ready and vix_latest is not None else "partial"
    return pd.DataFrame([row])


def write_status(
    status: dict[str, Any],
    status_json: Path = STATUS_JSON,
    status_md: Path = STATUS_MD,
) -> None:
    status_json.parent.mkdir(parents=True, exist_ok=True)
    status_json.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Futures / Options Source Status",
        "",
        f"- generated_at: `{status.get('generated_at', '')}`",
        f"- overall_status: `{status.get('overall_status', '')}`",
        "",
        "| source | status | rows | latest_date | message |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for name, info in status.get("sources", {}).items():
        lines.append(
            f"| {name} | {info.get('status', '')} | {info.get('rows', 0)} | "
            f"{info.get('latest_date', '')} | {safe_str(info.get('message', '')).replace('|', '/')} |"
        )
    status_md.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", default="")
    parser.add_argument("--end-date", default="")
    parser.add_argument("--require-exact-source-dates", action="store_true", default=True)
    args = parser.parse_args()

    has_start_arg = args.start_date is not None and str(args.start_date) != ""
    has_end_arg = args.end_date is not None and str(args.end_date) != ""
    if has_start_arg != has_end_arg:
        raise RuntimeError("--start-date and --end-date must be provided together")
    historical_mode = has_start_arg and has_end_arg
    if historical_mode:
        start_date = parse_cli_date(args.start_date, "--start-date")
        end_date = parse_cli_date(args.end_date, "--end-date")
        requested_dates = requested_trading_dates(start_date, end_date)
        if start_date > end_date:
            raise RuntimeError(f"invalid date window: {start_date} > {end_date}")
    else:
        start_date = ""
        end_date = ""
        requested_dates = []

    FO_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    status: dict[str, Any] = {
        "generated_at": now_text(),
        "mode": "reconstructed_source_tail_gap" if historical_mode else "open_data_latest",
        "requested_window": {"start_date": start_date, "end_date": end_date},
        "sources": {},
    }
    frames: dict[str, pd.DataFrame] = {}
    source_fetched_ok: dict[str, bool] = {}

    key_map = {
        "institutional_fo": ["日期", "身份別"],
        "futures_contracts": ["日期", "商品名稱", "身份別"],
        "options_call_put": ["日期", "商品名稱", "買賣權別", "身份別"],
        "put_call_ratio": ["日期"],
    }

    pending_source_status: dict[str, Any] = {}
    for name, data_name in SOURCES.items():
        try:
            if historical_mode:
                df, provenance = fetch_taifex_historical(
                    name,
                    start_date,
                    end_date,
                    require_exact_source_dates=args.require_exact_source_dates,
                )
                provenance["publication_status"] = "reconstructed_not_as_published"
                if not rows_have_unique_keys(df, key_map[name]):
                    raise RuntimeError(f"{name} TAIFEX data has duplicated PK rows")
            else:
                df = fetch_open_data(data_name)
                provenance = {
                    "source": name,
                    "status": "ok",
                    "fetched_at": now_text(),
                    "endpoint": TAIFEX_OPEN_DATA_URL,
                    "params": {"data_name": data_name},
                    "encoding": "utf-8",
                    "raw_sha256": "",
                    "normalized_sha256": "",
                    "requested_dates": [],
                    "observed_dates": [],
                    "rows": len(df),
                    "publication_status": "as_published",
                    "pk_unique": rows_have_unique_keys(df, key_map[name]),
                }
            source_fetched_ok[name] = True
            if not rows_have_unique_keys(df, key_map[name]):
                raise RuntimeError(f"{name} TAIFEX data missing complete PK columns")
            frames[name] = df
            pending_source_status[name] = {
                "status": "ok",
                "rows": len(df),
                "latest_date": latest_date_from_df(df),
                "message": "",
                "requested_dates": provenance.get("requested_dates", []),
                "observed_dates": provenance.get("observed_dates", []),
                "provenance": {
                    "endpoint": provenance.get("endpoint", ""),
                    "params": provenance.get("params", {}),
                    "fetched_at": provenance.get("fetched_at", now_text()),
                    "encoding": provenance.get("encoding", ""),
                    "raw_sha256": provenance.get("raw_sha256", ""),
                    "normalized_sha256": provenance.get("normalized_sha256", ""),
                    "rows": provenance.get("rows", len(df)),
                    "pk_unique": rows_have_unique_keys(df, key_map[name]),
                    "publication_status": provenance.get("publication_status", "as_published"),
                },
            }
        except Exception as exc:
            if historical_mode:
                raise
            source_fetched_ok[name] = False
            frames[name] = read_csv(HISTORY_FILES.get(name, Path("")), dtype=str)
            pending_source_status[name] = {
                "status": "fallback_history" if not frames[name].empty else "missing",
                "rows": len(frames[name]),
                "latest_date": latest_date_from_df(frames[name]) if not frames[name].empty else "",
                "message": str(exc),
                "publication_status": "as_published",
            }

    for source_name in (
        "institutional_fo",
        "futures_contracts",
        "options_call_put",
        "put_call_ratio",
    ):
        if source_name in frames:
            status["sources"][source_name] = pending_source_status[source_name]

    try:
        vix, vix_provenance = fetch_vix_history_with_provenance(months=6)
        if historical_mode:
            vix, _, observed_vix_dates = filter_vix_candidate_exact_dates(
                vix,
                start_date,
                end_date,
                required_dates=requested_dates,
            )
            vix_fetched_ok = True
            frames["taiwan_vix"] = vix
            if vix.empty:
                raise RuntimeError("TAIFEX VIX has no rows in requested window")
            pending_source_status["taiwan_vix"] = {
                "status": "ok",
                "rows": len(vix),
                "latest_date": latest_date_from_df(vix.rename(columns={"date": "日期"})),
                "message": "",
                "publication_status": "reconstructed_not_as_published",
                "requested_dates": requested_dates,
                "observed_dates": observed_vix_dates,
                "provenance": {
                    "endpoint": VIX_FILE_URL,
                    "params": {
                        "start_date": start_date,
                        "end_date": end_date,
                    },
                    "fetched_at": now_text(),
                    "source_files": vix_provenance.get("source_files", []),
                    "source_manifest_sha256": vix_provenance.get("source_manifest_sha256", ""),
                    "rows": len(vix),
                    "publication_status": "reconstructed_not_as_published",
                },
            }
        else:
            if vix.empty:
                raise RuntimeError("TAIFEX VIX monthly files returned no usable rows")
            vix_fetched_ok = True
            frames["taiwan_vix"] = vix
            pending_source_status["taiwan_vix"] = {
                "status": "ok",
                "rows": len(vix),
                "latest_date": latest_date_from_df(vix.rename(columns={"date": "日期"})),
                "message": "",
                "provenance": {
                    "endpoint": VIX_FILE_URL,
                    "source_files": vix_provenance.get("source_files", []),
                    "source_manifest_sha256": vix_provenance.get("source_manifest_sha256", ""),
                    "rows": len(vix),
                    "publication_status": "as_published",
                },
            }
    except Exception as exc:
        if historical_mode:
            raise
        vix_fetched_ok = False
        frames["taiwan_vix"] = read_csv(HISTORY_FILES["taiwan_vix"], dtype=str)
        pending_source_status["taiwan_vix"] = {
            "status": "fallback_history" if not frames["taiwan_vix"].empty else "missing",
            "rows": len(frames["taiwan_vix"]),
            "latest_date": latest_date_from_df(frames["taiwan_vix"].rename(columns={"date": "日期"})) if not frames["taiwan_vix"].empty else "",
            "message": str(exc),
            "publication_status": "as_published",
        }

    status["sources"]["taiwan_vix"] = pending_source_status["taiwan_vix"]

    indicator = build_indicator_row(
        frames.get("institutional_fo", pd.DataFrame()),
        frames.get("futures_contracts", pd.DataFrame()),
        frames.get("options_call_put", pd.DataFrame()),
        frames.get("put_call_ratio", pd.DataFrame()),
        frames.get("taiwan_vix", pd.DataFrame()),
        {k: v.get("status") for k, v in status["sources"].items()},
        target_date=end_date or "",
    )
    if historical_mode and indicator.iloc[0].get("source_status") != "ready":
        raise RuntimeError("historical source rebuild requires source_status=ready")
    if historical_mode and safe_str(indicator.iloc[0].get("taiwan_vix_date")) != end_date:
        raise RuntimeError("historical source rebuild requires taiwan_vix_date == end_date")

    staging_root = Path(tempfile.mkdtemp(prefix="futures-options-indicators-", dir=DATA_DIR))
    staged_paths: list[tuple[Path, Path]] = []
    try:
        staging_raw = staging_root / "futures_options" / "raw"
        staging_latest = staging_root / "latest"
        staging_history = staging_root / "futures_options"

        for source_name in (
            "institutional_fo",
            "futures_contracts",
            "options_call_put",
            "put_call_ratio",
        ):
            if not source_fetched_ok.get(source_name, False):
                continue
            frame = frames.get(source_name, pd.DataFrame())
            if frame.empty:
                continue
            target_date = latest_date_from_df(frame)
            staged_raw_path = staging_raw / f"{source_name}_{target_date}.csv"
            staged_latest_path = staging_latest / LATEST_FILES[source_name].name
            staged_history_path = staging_history / HISTORY_FILES[source_name].name
            write_csv(frame, staged_raw_path)
            write_csv(frame, staged_latest_path)
            if HISTORY_FILES[source_name].exists():
                write_csv(read_csv(HISTORY_FILES[source_name], dtype=str), staged_history_path)
            append_update_csv(
                frame,
                staged_history_path,
                key_cols=key_map[source_name],
                sort_cols=key_map[source_name],
            )
            staged_paths.extend(
                [
                    (staged_raw_path, raw_snapshot_path(source_name, target_date)),
                    (staged_latest_path, LATEST_FILES[source_name]),
                    (staged_history_path, HISTORY_FILES[source_name]),
                ]
            )

        if vix_fetched_ok and not frames.get("taiwan_vix", pd.DataFrame()).empty:
            frame = frames["taiwan_vix"]
            staged_latest_vix = staging_latest / LATEST_FILES["taiwan_vix"].name
            staged_history_vix = staging_history / HISTORY_FILES["taiwan_vix"].name
            write_csv(frame, staged_latest_vix)
            if HISTORY_FILES["taiwan_vix"].exists():
                write_csv(read_csv(HISTORY_FILES["taiwan_vix"], dtype=str), staged_history_vix)
            append_update_csv(
                frame,
                staged_history_vix,
                key_cols=["date"],
                sort_cols=["date"],
            )
            staged_paths.extend(
                [
                    (staged_latest_vix, LATEST_FILES["taiwan_vix"]),
                    (staged_history_vix, HISTORY_FILES["taiwan_vix"]),
                ]
            )

        status["overall_status"] = "ready" if indicator.iloc[0].get("source_status") == "ready" else "partial"
        status["indicator_path"] = INDICATORS_CSV.as_posix()
        staged_indicator = staging_latest / INDICATORS_CSV.name
        staged_status_json = staging_root / "latest" / STATUS_JSON.name
        staged_status_md = staging_root / "latest" / STATUS_MD.name
        write_csv(indicator, staged_indicator)
        write_status(status, status_json=staged_status_json, status_md=staged_status_md)
        staged_paths.extend(
            [
                (staged_indicator, INDICATORS_CSV),
                (staged_status_json, STATUS_JSON),
                (staged_status_md, STATUS_MD),
            ]
        )

        commit_staged_paths(staged_paths, staging_root / "rollback")
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)

    print(f"Saved: {INDICATORS_CSV}")
    print(f"Saved: {STATUS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
