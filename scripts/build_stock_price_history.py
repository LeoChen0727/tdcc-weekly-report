from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import argparse
import hashlib
import json
import math
import os
import re
import shutil
import tempfile

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

DATA_DAILY_PRICE_DIR = Path("data/daily_price")
STOCK_HISTORY_DIR = Path("data/stock_price_history")
LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")

MANIFEST_CSV = LATEST_DIR / "stock_price_history_manifest.csv"
MANIFEST_JSON = LATEST_DIR / "stock_price_history_manifest.json"
MANIFEST_MD = LATEST_DIR / "stock_price_history_manifest.md"
DOCS_MANIFEST_CSV = DOCS_LATEST_DIR / MANIFEST_CSV.name
DOCS_MANIFEST_JSON = DOCS_LATEST_DIR / MANIFEST_JSON.name
DOCS_MANIFEST_MD = DOCS_LATEST_DIR / MANIFEST_MD.name
SOURCE_RECOVERY_JSON = LATEST_DIR / "daily_price_source_recovery_latest.json"
RANGE_REPAIR_JSON_NAME = "repair_daily_price_range_latest.json"
RANGE_REPAIR_MD_NAME = "repair_daily_price_range_latest.md"

NUMERIC_COLUMNS = ["open", "high", "low", "close", "volume", "trading_value"]
BASE_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "market",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "trading_value",
    "source",
    "source_file",
]
INDICATOR_COLUMNS = [
    "ma5",
    "ma20",
    "ma60",
    "ma120",
    "ema23",
    "return_1d",
    "return_5d",
    "return_20d",
    "return_60d",
    "return_120d",
    "volume_ma20",
    "volume_ratio",
    "high_20",
    "high_60",
    "high_120",
    "low_20",
    "low_60",
    "low_120",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "distance_to_ma120_pct",
    "distance_to_ema23_pct",
    "distance_to_high_20_pct",
    "distance_to_high_60_pct",
    "distance_to_high_120_pct",
    "distance_to_low_60_pct",
    "distance_to_low_120_pct",
]


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def dataframe_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False, encoding="utf-8", lineterminator="\n").encode("utf-8")


def canonical_source_file(value: Any) -> str:
    text = safe_str(value).replace("\\", "/")
    marker = "/data/daily_price/"
    if marker in text:
        return "data/daily_price/" + text.split(marker, 1)[1]
    return text


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value).upper()
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Z]", "", text)
    if text.isdigit() and len(text) < 4:
        text = text.zfill(4)
    return text


def is_supported_security_id(stock_id: str) -> bool:
    """Keep regular 4-digit equities plus 00-prefixed ETF/index products; exclude warrants."""
    text = normalize_stock_id(stock_id)
    if not text.isdigit():
        return False
    if len(text) == 4:
        return True
    if text.startswith("00") and 5 <= len(text) <= 6:
        return True
    return False


def to_number(series: pd.Series) -> pd.Series:
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False).str.replace("--", "", regex=False),
        errors="coerce",
    )


def first_existing(columns: list[str], candidates: list[str]) -> str:
    for candidate in candidates:
        if candidate in columns:
            return candidate
    return ""


def normalize_daily_price_file(path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype=str).fillna("")
    except Exception as exc:
        print(f"Skip {path}: read failed: {exc}")
        return pd.DataFrame()

    columns = list(df.columns)
    code_col = first_existing(columns, ["stock_id", "ticker", "code"])
    name_col = first_existing(columns, ["stock_name", "name"])
    if not code_col or "date" not in columns or "close" not in columns:
        print(f"Skip {path}: missing date/code/close columns")
        return pd.DataFrame()

    result = pd.DataFrame()
    result["date"] = df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
    result["stock_id"] = df[code_col].map(normalize_stock_id)
    result["stock_name"] = df[name_col].astype(str).str.strip() if name_col else ""
    result["market"] = df["market"].astype(str).str.strip() if "market" in columns else ""

    for col in NUMERIC_COLUMNS:
        if col in columns:
            result[col] = to_number(df[col])
        elif col == "trading_value" and "turnover" in columns:
            result[col] = to_number(df["turnover"])
        else:
            result[col] = math.nan

    result["source"] = df["source"].astype(str).str.strip() if "source" in columns else ""
    result["source_file"] = path.as_posix()
    result = result[result["date"].ne("") & result["stock_id"].ne("")]
    result = result[result["stock_id"].map(is_supported_security_id)]
    result = result.dropna(subset=["close"])
    result = result[~result["date"].map(is_weekend_yyyymmdd)]
    result = normalize_source_volume_units(result)
    return result


def is_weekend_yyyymmdd(value: Any) -> bool:
    text = safe_str(value)
    if not re.fullmatch(r"\d{8}", text):
        return False
    parsed = pd.to_datetime(text, format="%Y%m%d", errors="coerce")
    if pd.isna(parsed):
        return False
    return int(parsed.weekday()) >= 5


def normalize_source_volume_units(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize all stock histories to share count.

    The TPEx legacy daily JSON source reports trading volume in board lots.
    Older daily files and TWSE files use shares. Without this conversion,
    high-price TPEx names such as 8299 show a fake volume collapse from
    millions of shares to a few thousand lots.
    """
    result = df.copy()
    if "source" not in result.columns or "volume" not in result.columns:
        return result
    source = result["source"].astype(str).str.upper()
    legacy_tpex = source.eq("TPEX_OLD_DAILY_JSON")
    result.loc[legacy_tpex, "volume"] = pd.to_numeric(result.loc[legacy_tpex, "volume"], errors="coerce") * 1000
    return result


def read_history_latest_date(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        df = pd.read_csv(path, dtype=str, usecols=["date"]).fillna("")
    except Exception:
        return ""
    if df.empty:
        return ""
    dates = df["date"].map(safe_str)
    dates = dates[dates.ne("")]
    return str(dates.max()) if not dates.empty else ""


def load_all_daily_prices() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(DATA_DAILY_PRICE_DIR.glob("*.csv")):
        normalized = normalize_daily_price_file(path)
        if not normalized.empty:
            frames.append(normalized)
    if not frames:
        return pd.DataFrame(columns=BASE_COLUMNS)

    df = pd.concat(frames, ignore_index=True)
    df["_source_priority"] = df["source_file"].astype(str).str.contains("daily_price_").astype(int)
    df = df.sort_values(["stock_id", "date", "_source_priority", "source_file"])
    df = df.drop_duplicates(["stock_id", "date"], keep="last")
    df = df.drop(columns=["_source_priority"])
    df = drop_stale_duplicate_dates(df)
    return df.sort_values(["stock_id", "date"]).reset_index(drop=True)


def load_latest_trading_daily_prices() -> pd.DataFrame:
    """Load the newest daily price file that has usable trading rows."""
    all_prices = load_all_daily_prices()
    if not all_prices.empty:
        latest_date = all_prices["date"].astype(str).max()
        return all_prices[all_prices["date"].astype(str).eq(latest_date)].copy()
    return pd.DataFrame(columns=BASE_COLUMNS)


def drop_stale_duplicate_dates(df: pd.DataFrame, same_threshold: float = 0.98, min_common_rows: int = 300) -> pd.DataFrame:
    """Drop synthetic date/market snapshots that duplicate the previous day.

    Some fallback fetches write a file with the requested date even when the
    exchange has only published the previous trading day's prices. The stale
    segment can affect TPEx while TWSE is already fresh, so this filter works
    per market instead of dropping or keeping an entire date.
    """
    if df.empty:
        return df
    keep_mask = pd.Series(True, index=df.index)
    previous_by_market: dict[str, tuple[str, pd.DataFrame]] = {}
    compare_cols = ["open", "high", "low", "close", "volume"]
    for date in sorted(df["date"].dropna().astype(str).unique()):
        current = df[df["date"].astype(str).eq(date)].copy()
        current_keep_mask = pd.Series(True, index=current.index)
        for market, market_current in current.groupby(current["market"].astype(str), sort=True):
            previous_info = previous_by_market.get(market)
            if previous_info is None:
                continue
            previous_date, previous = previous_info
            merged = previous[["stock_id"] + compare_cols].merge(
                market_current[["stock_id"] + compare_cols],
                on="stock_id",
                suffixes=("_prev", "_cur"),
            )
            if len(merged) >= min_common_rows:
                same = pd.Series(True, index=merged.index)
                for col in compare_cols:
                    prev = pd.to_numeric(merged[f"{col}_prev"], errors="coerce")
                    cur = pd.to_numeric(merged[f"{col}_cur"], errors="coerce")
                    same &= (prev - cur).abs().fillna(math.inf) <= 1e-9
                same_ratio = float(same.mean()) if len(same) else 0.0
                if same_ratio >= same_threshold:
                    print(
                        f"Skip stale duplicate daily price date {date} market {market}: "
                        f"{same_ratio:.1%} rows match previous kept date {previous_date}"
                    )
                    current_keep_mask.loc[market_current.index] = False
                    keep_mask.loc[market_current.index] = False
        kept_current = current[current_keep_mask]
        for market, market_current in kept_current.groupby(kept_current["market"].astype(str), sort=True):
            previous_by_market[market] = (date, market_current.copy())
    return df[keep_mask].copy()


def rolling_mean(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window, min_periods=min(5, window)).mean()


def pct_change(series: pd.Series, periods: int) -> pd.Series:
    return series.pct_change(periods=periods) * 100


def distance_to(close: pd.Series, target: pd.Series) -> pd.Series:
    return (close / target - 1) * 100


def add_indicators(stock_df: pd.DataFrame) -> pd.DataFrame:
    df = stock_df.sort_values("date").copy()
    close = df["close"]
    df["ma5"] = rolling_mean(close, 5)
    df["ma20"] = rolling_mean(close, 20)
    df["ma60"] = rolling_mean(close, 60)
    df["ma120"] = rolling_mean(close, 120)
    df["ema23"] = close.ewm(span=23, adjust=False, min_periods=5).mean()
    for days in [1, 5, 20, 60, 120]:
        df[f"return_{days}d"] = pct_change(close, days)

    df["volume_ma20"] = rolling_mean(df["volume"], 20)
    df["volume_ratio"] = df["volume"] / df["volume_ma20"]
    for days in [20, 60, 120]:
        df[f"high_{days}"] = df["high"].rolling(days, min_periods=min(5, days)).max()
        df[f"low_{days}"] = df["low"].rolling(days, min_periods=min(5, days)).min()

    df["distance_to_ma20_pct"] = distance_to(close, df["ma20"])
    df["distance_to_ma60_pct"] = distance_to(close, df["ma60"])
    df["distance_to_ma120_pct"] = distance_to(close, df["ma120"])
    df["distance_to_ema23_pct"] = distance_to(close, df["ema23"])
    df["distance_to_high_20_pct"] = distance_to(close, df["high_20"])
    df["distance_to_high_60_pct"] = distance_to(close, df["high_60"])
    df["distance_to_high_120_pct"] = distance_to(close, df["high_120"])
    df["distance_to_low_60_pct"] = distance_to(close, df["low_60"])
    df["distance_to_low_120_pct"] = distance_to(close, df["low_120"])
    return df[BASE_COLUMNS + INDICATOR_COLUMNS]


def round_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for col in result.columns:
        if col in {"date", "stock_id", "stock_name", "market", "source", "source_file"}:
            continue
        result[col] = pd.to_numeric(result[col], errors="coerce").round(4)
    return result


def normalize_base_frame(df: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame(index=df.index)
    for column in BASE_COLUMNS:
        if column in df.columns:
            result[column] = df[column]
        elif column in NUMERIC_COLUMNS:
            result[column] = math.nan
        else:
            result[column] = ""
    result["date"] = result["date"].map(safe_str)
    result["stock_id"] = result["stock_id"].map(normalize_stock_id)
    for column in ("stock_name", "market", "source", "source_file"):
        result[column] = result[column].map(safe_str)
    result["source_file"] = result["source_file"].map(canonical_source_file)
    for column in NUMERIC_COLUMNS:
        result[column] = pd.to_numeric(result[column], errors="coerce")
    return result[BASE_COLUMNS]


def canonical_base_records(df: pd.DataFrame, *, excluded_dates: set[str] | None = None) -> list[dict[str, str]]:
    excluded_dates = excluded_dates or set()
    base = normalize_base_frame(df)
    base = base[~base["date"].isin(excluded_dates)].sort_values(["stock_id", "date"])
    records: list[dict[str, str]] = []
    for _, row in base.iterrows():
        record: dict[str, str] = {}
        for column in BASE_COLUMNS:
            if column in NUMERIC_COLUMNS:
                value = row[column]
                record[column] = "" if pd.isna(value) else format(float(value), ".15g")
            else:
                record[column] = safe_str(row[column])
        records.append(record)
    return records


def base_records_sha256(df: pd.DataFrame, *, excluded_dates: set[str] | None = None) -> str:
    payload = (
        json.dumps(
            canonical_base_records(df, excluded_dates=excluded_dates),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    return sha256_bytes(payload)


def canonical_indicator_records(df: pd.DataFrame, *, before_date: str) -> list[dict[str, str]]:
    if "date" not in df.columns:
        return []
    records: list[dict[str, str]] = []
    filtered = df[df["date"].map(safe_str).lt(before_date)].copy()
    filtered = filtered.sort_values("date")
    for _, row in filtered.iterrows():
        record = {
            "date": safe_str(row.get("date")),
            "stock_id": normalize_stock_id(row.get("stock_id")),
        }
        for column in INDICATOR_COLUMNS:
            value = pd.to_numeric(pd.Series([row.get(column, "")]), errors="coerce").iloc[0]
            record[column] = "" if pd.isna(value) else format(float(value), ".15g")
        records.append(record)
    return records


def indicator_records_sha256(df: pd.DataFrame, *, before_date: str) -> str:
    payload = (
        json.dumps(
            canonical_indicator_records(df, before_date=before_date),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")
    return sha256_bytes(payload)


def aggregate_file_hashes(paths: list[Path], *, root: Path) -> str:
    rows = []
    for path in sorted(paths):
        relative = path.resolve().relative_to(root.resolve()).as_posix()
        rows.append(f"{relative}\t{sha256_path(path)}")
    return sha256_bytes(("\n".join(rows) + ("\n" if rows else "")).encode("utf-8"))


def load_selected_daily_prices(repair_dates: list[str]) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for date_text in repair_dates:
        path = DATA_DAILY_PRICE_DIR / f"daily_price_{date_text}.csv"
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"selected repair canonical daily file is missing or unsafe: {path}")
        normalized = normalize_daily_price_file(path)
        if normalized.empty:
            raise ValueError(f"selected repair canonical daily file has no eligible rows: {path}")
        observed_dates = set(normalized["date"].astype(str))
        if observed_dates != {date_text}:
            raise ValueError(
                f"selected repair canonical daily file date mismatch {path}: {sorted(observed_dates)}"
            )
        normalized["source_file"] = f"data/daily_price/daily_price_{date_text}.csv"
        frames.append(normalized)
    selected = pd.concat(frames, ignore_index=True)
    selected = selected[selected["stock_id"].map(is_supported_security_id)].copy()
    duplicates = selected.duplicated(["stock_id", "date"], keep=False)
    if duplicates.any():
        keys = sorted(
            selected.loc[duplicates, ["stock_id", "date"]]
            .astype(str)
            .agg("/".join, axis=1)
            .unique()
        )
        raise ValueError(f"selected repair daily rows contain duplicate stock/date keys: {keys[:20]}")
    return selected.sort_values(["stock_id", "date"]).reset_index(drop=True)


def scan_raw_daily_source_dates_for_stock_ids(stock_ids: set[str]) -> pd.DataFrame:
    """Scan raw CSV identity/date cells without quality, stale, or duplicate filtering."""

    normalized_ids = {normalize_stock_id(value) for value in stock_ids}
    matches: list[dict[str, str]] = []
    for path in sorted(DATA_DAILY_PRICE_DIR.glob("*.csv")):
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"selected history repair raw source path is unsafe: {path}")
        try:
            frame = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
        except Exception as exc:
            raise ValueError(f"selected history repair cannot scan raw source: {path}") from exc
        code_column = first_existing(list(frame.columns), ["stock_id", "ticker", "code"])
        if not code_column or "date" not in frame.columns:
            raise ValueError(f"selected history repair raw source lacks identity/date: {path}")
        normalized_stock_ids = frame[code_column].map(normalize_stock_id)
        matched = frame.loc[normalized_stock_ids.isin(normalized_ids), ["date"]].copy()
        matched["stock_id"] = normalized_stock_ids.loc[matched.index]
        for row in matched.itertuples(index=False):
            stock_id = safe_str(row.stock_id)
            date_text = re.sub(r"[^0-9]", "", safe_str(row.date))
            if not re.fullmatch(r"20\d{6}", date_text):
                raise ValueError(
                    f"selected history repair raw source candidate date is invalid: {path}/{stock_id}"
                )
            matches.append(
                {
                    "stock_id": stock_id,
                    "date": date_text,
                    "source_file": path.as_posix(),
                }
            )
    return pd.DataFrame(matches, columns=["stock_id", "date", "source_file"])


def validate_selected_daily_source_binding(
    report: dict[str, Any], repair_dates: list[str]
) -> None:
    """Bind every selected canonical/legacy file to its transactional source report."""

    if report.get("schema_version") != "repair_daily_price_range_v2":
        raise ValueError("selected history repair source report schema mismatch")
    rows = report.get("rows")
    if not isinstance(rows, list) or len(rows) != len(repair_dates):
        raise ValueError("selected history repair source report row count mismatch")
    rows_by_date: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("selected history repair source report row is malformed")
        date_text = safe_str(row.get("date"))
        if date_text in rows_by_date:
            raise ValueError(f"selected history repair source report duplicate date: {date_text}")
        rows_by_date[date_text] = row
    if set(rows_by_date) != set(repair_dates):
        raise ValueError("selected history repair source report date set mismatch")

    for date_text in repair_dates:
        row = rows_by_date[date_text]
        canonical_relative = f"data/daily_price/daily_price_{date_text}.csv"
        legacy_relative = f"data/daily_price/{date_text}.csv"
        if row.get("status") != "repaired":
            raise ValueError(f"selected history repair source status is not repaired: {date_text}")
        if safe_str(row.get("canonical_path")).replace("\\", "/") != canonical_relative:
            raise ValueError(f"selected history repair canonical path mismatch: {date_text}")
        if safe_str(row.get("legacy_path")).replace("\\", "/") != legacy_relative:
            raise ValueError(f"selected history repair legacy path mismatch: {date_text}")
        saved_files = {
            item.replace("\\", "/")
            for item in safe_str(row.get("saved_files")).split(";")
            if item
        }
        if saved_files != {canonical_relative, legacy_relative}:
            raise ValueError(f"selected history repair saved-file set mismatch: {date_text}")

        canonical = DATA_DAILY_PRICE_DIR / f"daily_price_{date_text}.csv"
        legacy = DATA_DAILY_PRICE_DIR / f"{date_text}.csv"
        if any(not path.is_file() or path.is_symlink() for path in (canonical, legacy)):
            raise ValueError(f"selected history repair source file is missing or unsafe: {date_text}")
        canonical_payload = canonical.read_bytes()
        legacy_payload = legacy.read_bytes()
        if canonical_payload != legacy_payload:
            raise ValueError(f"selected history repair canonical/legacy payload mismatch: {date_text}")
        observed_sha = sha256_bytes(canonical_payload)
        expected_sha = safe_str(row.get("price_sha256"))
        if not re.fullmatch(r"[0-9a-f]{64}", expected_sha) or observed_sha != expected_sha:
            raise ValueError(f"selected history repair source SHA-256 mismatch: {date_text}")
        frame = pd.read_csv(canonical, dtype=str).fillna("")
        try:
            expected_rows = int(row.get("total_rows", -1))
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"selected history repair source row count is invalid: {date_text}"
            ) from exc
        if len(frame) != expected_rows or set(frame.get("date", pd.Series(dtype=str)).astype(str)) != {
            date_text
        }:
            raise ValueError(f"selected history repair source row/date mismatch: {date_text}")
        provenance = row.get("fetch_response_provenance")
        if not isinstance(provenance, list) or not provenance:
            raise ValueError(f"selected history repair source provenance is missing: {date_text}")
        successful_sources: set[str] = set()
        for item in provenance:
            if not isinstance(item, dict):
                raise ValueError(
                    f"selected history repair source provenance row is malformed: {date_text}"
                )
            if item.get("expected_response_date") != date_text:
                raise ValueError(
                    f"selected history repair source provenance date mismatch: {date_text}"
                )
            if any(
                not re.fullmatch(r"[0-9a-f]{64}", safe_str(item.get(field)))
                for field in ("raw_sha256", "normalized_sha256")
            ):
                raise ValueError(
                    f"selected history repair source provenance hash mismatch: {date_text}"
                )
            try:
                status_code = int(item.get("status_code", 0))
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"selected history repair source provenance status mismatch: {date_text}"
                ) from exc
            if status_code == 200 and item.get("exact_date_match") is True:
                successful_sources.add(safe_str(item.get("source_name")))
        if not any(name.startswith("TWSE_") for name in successful_sources) or not any(
            name.startswith("TPEX_") for name in successful_sources
        ):
            raise ValueError(
                f"selected history repair lacks exact TWSE/TPEx source provenance: {date_text}"
            )
        observed_sources = {
            safe_str(value) for value in frame.get("source", pd.Series(dtype=str)) if safe_str(value)
        }
        if not observed_sources or not observed_sources.issubset(successful_sources):
            raise ValueError(
                f"selected history repair frame/provenance source mismatch: {date_text}"
            )


def _safe_target(root: Path, target: Path) -> Path:
    root = root.resolve()
    resolved = target.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"selected history repair target escapes repository: {target}") from exc
    current = root
    for part in resolved.relative_to(root).parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"selected history repair target contains symlink: {target}")
    if resolved.exists() and not resolved.is_file():
        raise ValueError(f"selected history repair target is not a regular file: {target}")
    return resolved


def publish_prepared_files_transaction(
    root: Path,
    prepared: dict[Path, Path],
    *,
    transaction_root: Path,
    fail_after_replace: int = 0,
) -> None:
    if not prepared:
        return
    root = root.resolve()
    backups = transaction_root / "backups"
    backups.mkdir(parents=True, exist_ok=True)
    ordered: list[tuple[Path, Path, Path | None]] = []
    for index, (target, next_path) in enumerate(
        sorted(prepared.items(), key=lambda item: item[0].as_posix())
    ):
        safe_target = _safe_target(root, target)
        if not next_path.is_file() or next_path.is_symlink():
            raise ValueError(f"selected history repair prepared file is unsafe: {next_path}")
        previous: Path | None = None
        if safe_target.exists():
            previous = backups / f"previous-{index}.bin"
            shutil.copyfile(safe_target, previous)
        ordered.append((safe_target, next_path, previous))
    replaced: list[tuple[Path, Path | None]] = []
    try:
        for target, next_path, previous in ordered:
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(next_path, target)
            replaced.append((target, previous))
            if fail_after_replace and len(replaced) >= fail_after_replace:
                raise OSError("injected selected history repair transaction failure")
    except Exception as exc:
        rollback_errors: list[str] = []
        for target, previous in reversed(replaced):
            try:
                if previous is None:
                    target.unlink(missing_ok=True)
                else:
                    restore = previous.with_name(previous.name + ".restore")
                    shutil.copyfile(previous, restore)
                    os.replace(restore, target)
            except Exception as rollback_exc:  # pragma: no cover - catastrophic filesystem failure
                rollback_errors.append(f"{target}: {rollback_exc}")
        if rollback_errors:
            raise RuntimeError(
                "selected history repair failed and rollback failed: "
                f"original={exc}; rollback={rollback_errors}"
            ) from exc
        raise


def manifest_row_from_history(stock_id: str, history: pd.DataFrame, file_path: Path) -> dict[str, Any]:
    latest = history.iloc[-1]
    nonempty_names = history["stock_name"].replace("", pd.NA).dropna()
    nonempty_markets = history["market"].replace("", pd.NA).dropna()
    return {
        "stock_id": stock_id,
        "stock_name": safe_str(nonempty_names.iloc[-1]) if not nonempty_names.empty else "",
        "market": safe_str(nonempty_markets.iloc[-1]) if not nonempty_markets.empty else "",
        "rows": len(history),
        "start_date": safe_str(history["date"].iloc[0]),
        "end_date": safe_str(history["date"].iloc[-1]),
        "latest_close": latest.get("close", ""),
        "latest_volume": latest.get("volume", ""),
        "file_path": f"data/stock_price_history/{stock_id}.csv",
        "raw_url": raw_url(Path(f"data/stock_price_history/{stock_id}.csv")),
    }


def manifest_markdown_bytes(manifest: pd.DataFrame, generated_at: str) -> bytes:
    top = manifest.sort_values(["rows", "stock_id"], ascending=[False, True]).head(30)
    lines = [
        "# Stock Price History Manifest",
        "",
        f"- generated_at: `{generated_at}`",
        f"- stock_count: `{len(manifest)}`",
        "- history_dir: `data/stock_price_history/`",
        f"- manifest_csv: `{MANIFEST_CSV.as_posix()}`",
        f"- manifest_raw_url: {raw_url(Path('output/latest/stock_price_history_manifest.csv'))}",
        "",
        "## Usage",
        "",
        "- Individual stock CSV raw URL format:",
        "  `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv`",
        "- Example:",
        "  `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2353.csv`",
        "",
        "## Top Files By Row Count",
        "",
        "| stock_id | stock_name | rows | start_date | end_date | file_path |",
        "|---|---|---:|---|---|---|",
    ]
    for _, row in top.iterrows():
        lines.append(
            f"| {row['stock_id']} | {row['stock_name']} | {row['rows']} | "
            f"{row['start_date']} | {row['end_date']} | `{row['file_path']}` |"
        )
    return ("\n".join(lines) + "\n").encode("utf-8")


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    elif path.as_posix().startswith("output/latest/"):
        rel = path.relative_to("output").as_posix()
    else:
        rel = path.as_posix()
    return f"{PAGES_PREFIX}/{rel}"


def build_history_files(limit_stock_ids: set[str] | None = None) -> pd.DataFrame:
    STOCK_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    all_prices = load_all_daily_prices()
    if all_prices.empty:
        raise SystemExit("No daily price data found under data/daily_price")

    manifest_rows: list[dict[str, Any]] = []
    grouped = all_prices.groupby("stock_id", sort=True)
    for stock_id, stock_df in grouped:
        if limit_stock_ids and stock_id not in limit_stock_ids:
            continue
        history = round_numeric_columns(add_indicators(stock_df))
        stock_name = safe_str(history["stock_name"].dropna().replace("", pd.NA).dropna().iloc[-1]) if history["stock_name"].replace("", pd.NA).dropna().size else ""
        market = safe_str(history["market"].dropna().replace("", pd.NA).dropna().iloc[-1]) if history["market"].replace("", pd.NA).dropna().size else ""
        file_path = STOCK_HISTORY_DIR / f"{stock_id}.csv"
        history.to_csv(file_path, index=False, encoding="utf-8", lineterminator="\n")
        latest = history.iloc[-1]
        manifest_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "market": market,
                "rows": len(history),
                "start_date": safe_str(history["date"].iloc[0]),
                "end_date": safe_str(history["date"].iloc[-1]),
                "latest_close": latest.get("close", ""),
                "latest_volume": latest.get("volume", ""),
                "file_path": file_path.as_posix(),
                "raw_url": raw_url(file_path),
            }
        )

    manifest = pd.DataFrame(manifest_rows).sort_values(["stock_id"]).reset_index(drop=True)
    manifest.to_csv(MANIFEST_CSV, index=False, encoding="utf-8", lineterminator="\n")
    MANIFEST_JSON.write_text(
        json.dumps(
            {
                "generated_at": now_text(),
                "status": "generated",
                "stock_count": int(len(manifest)),
                "daily_price_file_count": int(len(list(DATA_DAILY_PRICE_DIR.glob("*.csv")))),
                "manifest_csv": MANIFEST_CSV.as_posix(),
                "manifest_raw_url": raw_url(MANIFEST_CSV),
                "manifest_pages_url": pages_url(DOCS_MANIFEST_CSV),
                "history_dir": STOCK_HISTORY_DIR.as_posix(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_manifest_md(manifest)
    shutil.copyfile(MANIFEST_CSV, DOCS_MANIFEST_CSV)
    shutil.copyfile(MANIFEST_JSON, DOCS_MANIFEST_JSON)
    shutil.copyfile(MANIFEST_MD, DOCS_MANIFEST_MD)
    return manifest


def build_manifest_from_existing() -> pd.DataFrame:
    manifest_rows: list[dict[str, Any]] = []
    for file_path in sorted(STOCK_HISTORY_DIR.glob("*.csv")):
        try:
            history = pd.read_csv(file_path, dtype=str).fillna("")
        except Exception as exc:
            print(f"Skip manifest row {file_path}: read failed: {exc}")
            continue
        if history.empty or "date" not in history.columns:
            continue
        latest = history.iloc[-1]
        stock_id = normalize_stock_id(latest.get("stock_id") or file_path.stem)
        manifest_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": safe_str(latest.get("stock_name", "")),
                "market": safe_str(latest.get("market", "")),
                "rows": len(history),
                "start_date": safe_str(history["date"].iloc[0]),
                "end_date": safe_str(history["date"].iloc[-1]),
                "latest_close": latest.get("close", ""),
                "latest_volume": latest.get("volume", ""),
                "file_path": file_path.as_posix(),
                "raw_url": raw_url(file_path),
            }
        )

    manifest = pd.DataFrame(manifest_rows)
    if not manifest.empty:
        manifest = manifest.sort_values(["stock_id"]).reset_index(drop=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest.to_csv(MANIFEST_CSV, index=False, encoding="utf-8", lineterminator="\n")
    MANIFEST_JSON.write_text(
        json.dumps(
            {
                "generated_at": now_text(),
                "status": "generated_from_existing_history",
                "stock_count": int(len(manifest)),
                "daily_price_file_count": int(len(list(DATA_DAILY_PRICE_DIR.glob("*.csv")))),
                "manifest_csv": MANIFEST_CSV.as_posix(),
                "manifest_raw_url": raw_url(MANIFEST_CSV),
                "manifest_pages_url": pages_url(DOCS_MANIFEST_CSV),
                "history_dir": STOCK_HISTORY_DIR.as_posix(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_manifest_md(manifest)
    shutil.copyfile(MANIFEST_CSV, DOCS_MANIFEST_CSV)
    shutil.copyfile(MANIFEST_JSON, DOCS_MANIFEST_JSON)
    shutil.copyfile(MANIFEST_MD, DOCS_MANIFEST_MD)
    return manifest


def write_manifest_files(manifest: pd.DataFrame, status: str) -> pd.DataFrame:
    if not manifest.empty:
        manifest = manifest.sort_values(["stock_id"]).reset_index(drop=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    manifest.to_csv(MANIFEST_CSV, index=False, encoding="utf-8", lineterminator="\n")
    MANIFEST_JSON.write_text(
        json.dumps(
            {
                "generated_at": now_text(),
                "status": status,
                "stock_count": int(len(manifest)),
                "daily_price_file_count": int(len(list(DATA_DAILY_PRICE_DIR.glob("*.csv")))),
                "manifest_csv": MANIFEST_CSV.as_posix(),
                "manifest_raw_url": raw_url(MANIFEST_CSV),
                "manifest_pages_url": pages_url(DOCS_MANIFEST_CSV),
                "history_dir": STOCK_HISTORY_DIR.as_posix(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    write_manifest_md(manifest)
    shutil.copyfile(MANIFEST_CSV, DOCS_MANIFEST_CSV)
    shutil.copyfile(MANIFEST_JSON, DOCS_MANIFEST_JSON)
    shutil.copyfile(MANIFEST_MD, DOCS_MANIFEST_MD)
    return manifest


def build_history_files_incremental_latest(limit_stock_ids: set[str] | None = None) -> pd.DataFrame:
    """Append/replace the newest trading daily file instead of rebuilding all history."""
    STOCK_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    latest_prices = load_latest_trading_daily_prices()
    if latest_prices.empty:
        raise SystemExit("No non-weekend daily price data found under data/daily_price")

    manifest = pd.read_csv(MANIFEST_CSV, dtype=str).fillna("") if MANIFEST_CSV.exists() else pd.DataFrame()
    manifest_rows: dict[str, dict[str, Any]] = {}
    if not manifest.empty and "stock_id" in manifest.columns:
        for _, row in manifest.iterrows():
            stock_id = normalize_stock_id(row.get("stock_id"))
            if stock_id:
                manifest_rows[stock_id] = row.to_dict()
    existing_history_count = len(list(STOCK_HISTORY_DIR.glob("*.csv")))
    if not limit_stock_ids and existing_history_count and len(manifest_rows) < existing_history_count * 0.8:
        print(
            "Existing manifest is incomplete for incremental update; "
            "rebuilding manifest from existing stock histories once."
        )
        manifest = build_manifest_from_existing()
        manifest_rows = {}
        for _, row in manifest.iterrows():
            stock_id = normalize_stock_id(row.get("stock_id"))
            if stock_id:
                manifest_rows[stock_id] = row.to_dict()

    touched = 0
    skipped = 0
    for stock_id, latest_df in latest_prices.groupby("stock_id", sort=True):
        stock_id = normalize_stock_id(stock_id)
        if limit_stock_ids and stock_id not in limit_stock_ids:
            continue
        latest_row = latest_df.sort_values("date").iloc[-1]
        latest_date = safe_str(latest_row.get("date"))
        file_path = STOCK_HISTORY_DIR / f"{stock_id}.csv"
        manifest_row = manifest_rows.get(stock_id, {})
        manifest_end_date = safe_str(manifest_row.get("end_date"))
        actual_end_date = read_history_latest_date(file_path)
        if file_path.exists() and manifest_end_date and actual_end_date and manifest_end_date != actual_end_date:
            print(
                "Stock history manifest mismatch "
                f"{stock_id}: manifest_end_date={manifest_end_date}, "
                f"actual_end_date={actual_end_date}; updating from daily price data"
            )
        if (
            not limit_stock_ids
            and file_path.exists()
            and manifest_end_date == latest_date
            and actual_end_date == latest_date
        ):
            skipped += 1
            continue
        if not limit_stock_ids and file_path.exists() and actual_end_date and latest_date < actual_end_date:
            print(
                "Skip older latest daily price for "
                f"{stock_id}: latest_daily_price_date={latest_date}, "
                f"actual_history_end_date={actual_end_date}"
            )
            skipped += 1
            continue
        if file_path.exists():
            try:
                existing = pd.read_csv(file_path, dtype=str).fillna("")
            except Exception as exc:
                print(f"Rebuild {stock_id} from latest row only because existing read failed: {exc}")
                existing = pd.DataFrame(columns=BASE_COLUMNS)
        else:
            existing = pd.DataFrame(columns=BASE_COLUMNS)

        if limit_stock_ids and not existing.empty and "date" in existing.columns and safe_str(existing["date"].iloc[-1]) == latest_date:
            existing_latest = existing.iloc[-1]
            unchanged = True
            for col in ["open", "high", "low", "close", "volume", "trading_value"]:
                old_value = pd.to_numeric(pd.Series([existing_latest.get(col, "")]), errors="coerce").iloc[0]
                new_value = pd.to_numeric(pd.Series([latest_row.get(col, "")]), errors="coerce").iloc[0]
                if pd.isna(old_value) and pd.isna(new_value):
                    continue
                if pd.isna(old_value) or pd.isna(new_value) or abs(float(old_value) - float(new_value)) > 1e-9:
                    unchanged = False
                    break
            if unchanged:
                skipped += 1
                continue

        base_existing = existing[[c for c in BASE_COLUMNS if c in existing.columns]].copy()
        for col in BASE_COLUMNS:
            if col not in base_existing.columns:
                base_existing[col] = math.nan if col in NUMERIC_COLUMNS else ""

        combined = pd.concat([base_existing[BASE_COLUMNS], latest_df[BASE_COLUMNS]], ignore_index=True, sort=False)
        combined["date"] = combined["date"].map(safe_str)
        combined = combined[combined["date"].ne("")]
        for col in NUMERIC_COLUMNS:
            combined[col] = pd.to_numeric(combined[col], errors="coerce")
        combined = combined.sort_values(["stock_id", "date"]).drop_duplicates(["stock_id", "date"], keep="last")
        history = round_numeric_columns(add_indicators(combined))
        history.to_csv(file_path, index=False, encoding="utf-8", lineterminator="\n")
        latest_history = history.iloc[-1]
        manifest_rows[stock_id] = {
            "stock_id": stock_id,
            "stock_name": safe_str(latest_history.get("stock_name", "")),
            "market": safe_str(latest_history.get("market", "")),
            "rows": len(history),
            "start_date": safe_str(history["date"].iloc[0]),
            "end_date": safe_str(history["date"].iloc[-1]),
            "latest_close": latest_history.get("close", ""),
            "latest_volume": latest_history.get("volume", ""),
            "file_path": file_path.as_posix(),
            "raw_url": raw_url(file_path),
        }
        touched += 1

    if manifest_rows:
        manifest = pd.DataFrame(manifest_rows.values())
        manifest = write_manifest_files(manifest, "incremental_latest")
    else:
        manifest = build_manifest_from_existing()
    print(f"Incremental latest update touched {touched} stock history files; skipped unchanged {skipped}")
    return manifest


def build_history_files_selected_dates(
    repair_dates: list[str],
    *,
    allowed_create_stock_ids: set[str] | None = None,
    expected_stock_union_count: int | None = None,
    expected_selected_row_count: int | None = None,
    expected_existing_history_count: int | None = None,
    expected_created_history_count: int | None = None,
    expected_untouched_history_count: int | None = None,
    fail_after_replace: int = 0,
) -> pd.DataFrame:
    """Inject exact historical dates without rebuilding unrelated stock histories."""

    root = Path.cwd().resolve()
    repair_dates = [safe_str(value) for value in repair_dates]
    if not repair_dates or repair_dates != sorted(set(repair_dates)):
        raise ValueError("repair dates must be non-empty, unique, and strictly ascending")
    for date_text in repair_dates:
        try:
            datetime.strptime(date_text, "%Y%m%d")
        except ValueError as exc:
            raise ValueError(f"invalid repair date: {date_text}") from exc
    repair_date_set = set(repair_dates)
    allowed_create_stock_ids = {
        normalize_stock_id(value) for value in (allowed_create_stock_ids or set())
    }

    selected = load_selected_daily_prices(repair_dates)
    selected_stock_ids = sorted(set(selected["stock_id"].map(normalize_stock_id)))
    selected_key_count = len(selected)
    if expected_stock_union_count is not None and len(selected_stock_ids) != expected_stock_union_count:
        raise ValueError(
            "selected repair eligible stock union mismatch: "
            f"expected={expected_stock_union_count} observed={len(selected_stock_ids)}"
        )
    if expected_selected_row_count is not None and selected_key_count != expected_selected_row_count:
        raise ValueError(
            "selected repair eligible stock/date row mismatch: "
            f"expected={expected_selected_row_count} observed={selected_key_count}"
        )

    existing_paths = {
        normalize_stock_id(path.stem): path
        for path in STOCK_HISTORY_DIR.glob("*.csv")
        if path.is_file() and not path.is_symlink()
    }
    existing_selected_ids = sorted(set(selected_stock_ids) & set(existing_paths))
    missing_ids = sorted(set(selected_stock_ids) - set(existing_paths))
    unexpected_missing = sorted(set(missing_ids) - allowed_create_stock_ids)
    if unexpected_missing:
        raise ValueError(
            "selected repair found unapproved missing stock histories: "
            + ",".join(unexpected_missing)
        )
    if (
        expected_existing_history_count is not None
        and len(existing_selected_ids) != expected_existing_history_count
    ):
        raise ValueError(
            "selected repair existing-history count mismatch: "
            f"expected={expected_existing_history_count} observed={len(existing_selected_ids)}"
        )
    if expected_created_history_count is not None and len(missing_ids) != expected_created_history_count:
        raise ValueError(
            "selected repair missing-history count mismatch: "
            f"expected={expected_created_history_count} observed={len(missing_ids)}"
        )

    untouched_paths = [
        path for stock_id, path in existing_paths.items() if stock_id not in set(selected_stock_ids)
    ]
    if (
        expected_untouched_history_count is not None
        and len(untouched_paths) != expected_untouched_history_count
    ):
        raise ValueError(
            "selected repair untouched-history count mismatch: "
            f"expected={expected_untouched_history_count} observed={len(untouched_paths)}"
        )
    untouched_before_sha = aggregate_file_hashes(untouched_paths, root=root)

    report_json = LATEST_DIR / RANGE_REPAIR_JSON_NAME
    report_md = LATEST_DIR / RANGE_REPAIR_MD_NAME
    if not report_json.is_file() or report_json.is_symlink():
        raise ValueError("selected history repair requires the exact range-repair JSON report")
    report = json.loads(report_json.read_text(encoding="utf-8-sig"))
    if report.get("mode") != "selected_dates" or report.get("selected_dates") != repair_dates:
        raise ValueError("selected history repair report date identity mismatch")
    validate_selected_daily_source_binding(report, repair_dates)

    if not MANIFEST_CSV.is_file() or MANIFEST_CSV.is_symlink():
        raise ValueError("selected history repair requires the existing stock history manifest")
    manifest = pd.read_csv(MANIFEST_CSV, dtype=str).fillna("")
    if "stock_id" not in manifest.columns:
        raise ValueError("selected history repair manifest lacks stock_id")
    manifest["stock_id"] = manifest["stock_id"].map(normalize_stock_id)
    manifest_ids = set(manifest["stock_id"])
    if manifest_ids != set(existing_paths):
        raise ValueError(
            "selected history repair manifest/file identity mismatch: "
            f"manifest_only={sorted(manifest_ids - set(existing_paths))[:20]} "
            f"file_only={sorted(set(existing_paths) - manifest_ids)[:20]}"
        )

    raw_prices_for_missing = pd.DataFrame(columns=["stock_id", "date", "source_file"])
    if missing_ids:
        raw_prices_for_missing = scan_raw_daily_source_dates_for_stock_ids(set(missing_ids))
        outside = raw_prices_for_missing[
            ~raw_prices_for_missing["date"].astype(str).isin(repair_date_set)
        ]
        if not outside.empty:
            outside_keys = sorted(
                outside[["stock_id", "date"]].astype(str).agg("/".join, axis=1).unique()
            )
            raise ValueError(
                "approved missing history has source rows outside selected dates; separate repair required: "
                + ",".join(outside_keys[:20])
            )

    generated_at = now_text()
    changed_history_paths: list[str] = []
    changed_history_sha256s: dict[str, str] = {}
    created_history_ids: list[str] = []
    selected_rows_existing = 0
    selected_rows_created = 0
    nonselected_before_rows: list[str] = []
    nonselected_after_rows: list[str] = []
    pre_repair_indicator_before_rows: list[str] = []
    pre_repair_indicator_after_rows: list[str] = []
    manifest_updates: dict[str, dict[str, Any]] = {}
    new_history_coverage: list[dict[str, Any]] = []

    with tempfile.TemporaryDirectory(
        prefix=".selected-stock-history-", dir=root
    ) as temp_text:
        temp_root = Path(temp_text)
        next_root = temp_root / "next"
        next_root.mkdir(parents=True)
        prepared: dict[Path, Path] = {}
        next_counter = 0

        def prepare(target: Path, payload: bytes) -> None:
            nonlocal next_counter
            next_path = next_root / f"next-{next_counter}.bin"
            next_counter += 1
            next_path.write_bytes(payload)
            prepared[target] = next_path

        for stock_id, selected_stock in selected.groupby("stock_id", sort=True):
            stock_id = normalize_stock_id(stock_id)
            selected_stock = normalize_base_frame(selected_stock)
            selected_stock = selected_stock.sort_values("date")
            file_path = STOCK_HISTORY_DIR / f"{stock_id}.csv"
            existed = file_path.is_file() and not file_path.is_symlink()
            if existed:
                existing = pd.read_csv(file_path, dtype=str).fillna("")
                if existing.empty or "date" not in existing.columns:
                    raise ValueError(f"selected repair existing history is invalid: {file_path}")
                existing_base = normalize_base_frame(existing)
                observed_ids = set(existing_base["stock_id"].map(normalize_stock_id))
                if observed_ids != {stock_id}:
                    raise ValueError(
                        f"selected repair history stock identity mismatch {stock_id}: {sorted(observed_ids)}"
                    )
                if existing_base.duplicated(["stock_id", "date"]).any():
                    raise ValueError(f"selected repair existing history has duplicate dates: {stock_id}")
                existing_selected = existing_base[existing_base["date"].isin(repair_date_set)]
                if not existing_selected.empty:
                    source_by_date = selected_stock[selected_stock["date"].isin(existing_selected["date"])]
                    if canonical_base_records(existing_selected) != canonical_base_records(source_by_date):
                        raise ValueError(
                            f"selected repair existing target-date base row conflicts with source: {stock_id}"
                        )
                before_sha = base_records_sha256(existing_base, excluded_dates=repair_date_set)
                indicator_before_sha = indicator_records_sha256(
                    existing, before_date=repair_dates[0]
                )
                combined = pd.concat(
                    [
                        existing_base[~existing_base["date"].isin(repair_date_set)],
                        selected_stock,
                    ],
                    ignore_index=True,
                )
                selected_rows_existing += len(selected_stock)
            else:
                if stock_id not in allowed_create_stock_ids:
                    raise ValueError(f"selected repair may not create history for {stock_id}")
                source_rows = selected_stock.copy()
                combined = source_rows
                before_sha = base_records_sha256(
                    pd.DataFrame(columns=BASE_COLUMNS), excluded_dates=repair_date_set
                )
                indicator_before_sha = ""
                created_history_ids.append(stock_id)
                selected_rows_created += len(selected_stock)
                new_history_coverage.append(
                    {
                        "stock_id": stock_id,
                        "new_history_source_coverage": "target_dates_only",
                        "source_rows": len(source_rows),
                        "outside_selected_date_source_rows": 0,
                    }
                )

            combined = normalize_base_frame(combined)
            combined = combined.sort_values(["stock_id", "date"])
            if combined.duplicated(["stock_id", "date"]).any():
                raise ValueError(f"selected repair combined history has duplicate dates: {stock_id}")
            history = round_numeric_columns(add_indicators(combined))
            after_sha = base_records_sha256(history, excluded_dates=repair_date_set)
            if before_sha != after_sha:
                raise ValueError(f"selected repair changed non-selected base rows: {stock_id}")
            if existed:
                indicator_after_sha = indicator_records_sha256(
                    history, before_date=repair_dates[0]
                )
                if indicator_before_sha != indicator_after_sha:
                    raise ValueError(
                        f"selected repair changed pre-repair indicators: {stock_id}"
                    )
                pre_repair_indicator_before_rows.append(
                    f"{stock_id}\t{indicator_before_sha}"
                )
                pre_repair_indicator_after_rows.append(
                    f"{stock_id}\t{indicator_after_sha}"
                )
            actual_selected = history[history["date"].astype(str).isin(repair_date_set)]
            if canonical_base_records(actual_selected) != canonical_base_records(selected_stock):
                raise ValueError(f"selected repair target-date history/source mismatch: {stock_id}")
            nonselected_before_rows.append(f"{stock_id}\t{before_sha}")
            nonselected_after_rows.append(f"{stock_id}\t{after_sha}")

            payload = dataframe_csv_bytes(history)
            previous_payload = file_path.read_bytes() if existed else None
            if previous_payload != payload:
                prepare(file_path, payload)
                relative_history_path = f"data/stock_price_history/{stock_id}.csv"
                changed_history_paths.append(relative_history_path)
                changed_history_sha256s[relative_history_path] = sha256_bytes(payload)
            manifest_updates[stock_id] = manifest_row_from_history(stock_id, history, file_path)

        nonselected_before_sha = sha256_bytes(
            ("\n".join(sorted(nonselected_before_rows)) + "\n").encode("utf-8")
        )
        nonselected_after_sha = sha256_bytes(
            ("\n".join(sorted(nonselected_after_rows)) + "\n").encode("utf-8")
        )
        if nonselected_before_sha != nonselected_after_sha:
            raise ValueError("selected repair aggregate non-selected base-row identity drifted")
        pre_repair_indicator_before_sha = sha256_bytes(
            ("\n".join(sorted(pre_repair_indicator_before_rows)) + "\n").encode("utf-8")
        )
        pre_repair_indicator_after_sha = sha256_bytes(
            ("\n".join(sorted(pre_repair_indicator_after_rows)) + "\n").encode("utf-8")
        )
        if pre_repair_indicator_before_sha != pre_repair_indicator_after_sha:
            raise ValueError("selected repair aggregate pre-repair indicator identity drifted")

        if not changed_history_paths:
            print("Selected-date history repair is already current; preserving manifest timestamps.")
            return manifest

        manifest_by_id = {
            normalize_stock_id(row["stock_id"]): row.to_dict() for _, row in manifest.iterrows()
        }
        manifest_by_id.update(manifest_updates)
        next_manifest = pd.DataFrame(manifest_by_id.values())
        next_manifest = next_manifest[list(manifest.columns)]
        next_manifest = next_manifest.sort_values("stock_id").reset_index(drop=True)
        manifest_csv_payload = dataframe_csv_bytes(next_manifest)
        manifest_json = json.loads(MANIFEST_JSON.read_text(encoding="utf-8-sig"))
        manifest_json.update(
            {
                "generated_at": generated_at,
                "status": "selected_date_repair",
                "stock_count": len(next_manifest),
                "daily_price_file_count": len(list(DATA_DAILY_PRICE_DIR.glob("*.csv"))),
            }
        )
        manifest_json_payload = (
            json.dumps(manifest_json, ensure_ascii=False, indent=2) + "\n"
        ).encode("utf-8")
        manifest_md_payload = manifest_markdown_bytes(next_manifest, generated_at)
        manifest_sha256s = {
            "output/latest/stock_price_history_manifest.csv": sha256_bytes(manifest_csv_payload),
            "output/latest/stock_price_history_manifest.json": sha256_bytes(manifest_json_payload),
            "output/latest/stock_price_history_manifest.md": sha256_bytes(manifest_md_payload),
            "docs/latest/stock_price_history_manifest.csv": sha256_bytes(manifest_csv_payload),
            "docs/latest/stock_price_history_manifest.json": sha256_bytes(manifest_json_payload),
            "docs/latest/stock_price_history_manifest.md": sha256_bytes(manifest_md_payload),
        }
        for target, payload in (
            (MANIFEST_CSV, manifest_csv_payload),
            (MANIFEST_JSON, manifest_json_payload),
            (MANIFEST_MD, manifest_md_payload),
            (DOCS_MANIFEST_CSV, manifest_csv_payload),
            (DOCS_MANIFEST_JSON, manifest_json_payload),
            (DOCS_MANIFEST_MD, manifest_md_payload),
        ):
            prepare(target, payload)

        eligible_history_paths = [
            f"data/stock_price_history/{stock_id}.csv" for stock_id in selected_stock_ids
        ]
        history_report = {
            "mode": "selected_dates_controlled_history_repair",
            "repair_dates": repair_dates,
            "eligible_stock_union_count": len(selected_stock_ids),
            "eligible_stock_date_row_count": selected_key_count,
            "existing_history_count": len(existing_selected_ids),
            "created_history_count": len(created_history_ids),
            "created_history_stock_ids": sorted(created_history_ids),
            "eligible_history_paths": eligible_history_paths,
            "changed_history_paths": sorted(changed_history_paths),
            "changed_history_sha256s": {
                path: changed_history_sha256s[path] for path in sorted(changed_history_sha256s)
            },
            "selected_rows_injected_existing_histories": selected_rows_existing,
            "selected_rows_created_histories": selected_rows_created,
            "new_history_source_coverage": new_history_coverage,
            "non_selected_base_before_sha256": nonselected_before_sha,
            "non_selected_base_after_sha256": nonselected_after_sha,
            "pre_repair_indicator_before_sha256": pre_repair_indicator_before_sha,
            "pre_repair_indicator_after_sha256": pre_repair_indicator_after_sha,
            "untouched_history_count": len(untouched_paths),
            "untouched_history_before_sha256": untouched_before_sha,
            "untouched_history_after_sha256": untouched_before_sha,
            "manifest_paths": [
                "output/latest/stock_price_history_manifest.csv",
                "output/latest/stock_price_history_manifest.json",
                "output/latest/stock_price_history_manifest.md",
                "docs/latest/stock_price_history_manifest.csv",
                "docs/latest/stock_price_history_manifest.json",
                "docs/latest/stock_price_history_manifest.md",
            ],
            "manifest_sha256s": manifest_sha256s,
            "generated_at": generated_at,
        }
        report["history_repair"] = history_report
        report_json_payload = (
            json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8")
        base_markdown = report_md.read_text(encoding="utf-8-sig") if report_md.exists() else ""
        marker = "## Selected-Date Stock History Repair"
        base_markdown = base_markdown.split(marker, 1)[0].rstrip()
        history_markdown = [
            marker,
            "",
            f"- repair_dates: `{','.join(repair_dates)}`",
            f"- eligible_stock_union_count: `{len(selected_stock_ids)}`",
            f"- eligible_stock_date_row_count: `{selected_key_count}`",
            f"- existing_history_count: `{len(existing_selected_ids)}`",
            f"- created_history_stock_ids: `{','.join(sorted(created_history_ids))}`",
            f"- changed_history_count: `{len(changed_history_paths)}`",
            f"- untouched_history_count: `{len(untouched_paths)}`",
            f"- non_selected_base_sha256: `{nonselected_after_sha}`",
            f"- pre_repair_indicator_sha256: `{pre_repair_indicator_after_sha}`",
            f"- untouched_history_sha256: `{untouched_before_sha}`",
            "- new_history_source_coverage: `target_dates_only`",
            "",
        ]
        report_md_payload = (base_markdown + "\n\n" + "\n".join(history_markdown)).encode("utf-8")
        prepare(report_json, report_json_payload)
        prepare(report_md, report_md_payload)

        publish_prepared_files_transaction(
            root,
            prepared,
            transaction_root=temp_root,
            fail_after_replace=fail_after_replace,
        )

    untouched_after_sha = aggregate_file_hashes(untouched_paths, root=root)
    if untouched_after_sha != untouched_before_sha:
        raise ValueError("selected repair changed a history outside the eligible stock union")
    print(
        "Selected-date history repair completed: "
        f"eligible={len(selected_stock_ids)} changed={len(changed_history_paths)} "
        f"created={len(created_history_ids)} untouched={len(untouched_paths)}"
    )
    return next_manifest


def write_manifest_md(manifest: pd.DataFrame) -> None:
    top = manifest.sort_values(["rows", "stock_id"], ascending=[False, True]).head(30)
    lines = [
        "# Stock Price History Manifest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- stock_count: `{len(manifest)}`",
        f"- history_dir: `data/stock_price_history/`",
        f"- manifest_csv: `{MANIFEST_CSV.as_posix()}`",
        f"- manifest_raw_url: {raw_url(MANIFEST_CSV)}",
        "",
        "## Usage",
        "",
        "- Individual stock CSV raw URL format:",
        "  `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv`",
        "- Example:",
        "  `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2353.csv`",
        "",
        "## Top Files By Row Count",
        "",
        "| stock_id | stock_name | rows | start_date | end_date | file_path |",
        "|---|---|---:|---|---|---|",
    ]
    for _, row in top.iterrows():
        lines.append(
            f"| {row['stock_id']} | {row['stock_name']} | {row['rows']} | {row['start_date']} | {row['end_date']} | `{row['file_path']}` |"
        )
    MANIFEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def source_recovery_has_repair_action(path: Path | None = None) -> bool:
    path = path or SOURCE_RECOVERY_JSON
    if not path.exists():
        return False
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        return False
    if safe_str(payload.get("status")) != "repaired":
        return False
    actions = payload.get("actions", [])
    return isinstance(actions, list) and bool(actions)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build per-stock historical price CSV files from daily market CSV files.")
    parser.add_argument(
        "--stock-id",
        action="append",
        default=None,
        help="Optional stock id to build. Can be repeated. Default: build every stock.",
    )
    parser.add_argument(
        "--incremental-latest",
        action="store_true",
        help="Update from the newest trading daily-price file only. Use for daily pipeline; default remains full rebuild.",
    )
    parser.add_argument(
        "--full-rebuild-if-source-recovered",
        action="store_true",
        help=(
            "When source recovery repaired missing daily price files, rebuild full stock history instead of "
            "updating only the newest daily price file."
        ),
    )
    parser.add_argument(
        "--repair-date",
        action="append",
        default=None,
        help=(
            "Repair one exact historical date in existing stock histories. May be repeated. "
            "This controlled mode never runs the full history rebuild."
        ),
    )
    parser.add_argument(
        "--allow-create-stock-id",
        action="append",
        default=None,
        help=(
            "Allow a missing selected-date stock history to be created only when all available "
            "source rows for that stock are confined to --repair-date values."
        ),
    )
    parser.add_argument("--expected-stock-union-count", type=int, default=None)
    parser.add_argument("--expected-selected-row-count", type=int, default=None)
    parser.add_argument("--expected-existing-history-count", type=int, default=None)
    parser.add_argument("--expected-created-history-count", type=int, default=None)
    parser.add_argument("--expected-untouched-history-count", type=int, default=None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    stock_ids = getattr(args, "stock_id", None)
    limit = {normalize_stock_id(x) for x in stock_ids} if stock_ids else None
    repair_dates = getattr(args, "repair_date", None)
    if repair_dates:
        if getattr(args, "incremental_latest", False) or getattr(
            args, "full_rebuild_if_source_recovered", False
        ):
            raise ValueError(
                "--repair-date is mutually exclusive with incremental/full-rebuild modes"
            )
        if limit:
            raise ValueError("--repair-date derives its exact stock union from selected source files")
        manifest = build_history_files_selected_dates(
            repair_dates,
            allowed_create_stock_ids=set(getattr(args, "allow_create_stock_id", None) or []),
            expected_stock_union_count=getattr(args, "expected_stock_union_count", None),
            expected_selected_row_count=getattr(args, "expected_selected_row_count", None),
            expected_existing_history_count=getattr(args, "expected_existing_history_count", None),
            expected_created_history_count=getattr(args, "expected_created_history_count", None),
            expected_untouched_history_count=getattr(args, "expected_untouched_history_count", None),
        )
    elif getattr(args, "incremental_latest", False):
        if getattr(args, "full_rebuild_if_source_recovered", False) and source_recovery_has_repair_action():
            print("Source recovery repaired daily price files; rebuilding full stock price history.")
            manifest = build_history_files(limit)
        else:
            manifest = build_history_files_incremental_latest(limit)
    else:
        manifest = build_history_files(limit)
    print(f"Saved {len(manifest)} stock history files under {STOCK_HISTORY_DIR}")
    print(f"Saved manifest: {MANIFEST_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
