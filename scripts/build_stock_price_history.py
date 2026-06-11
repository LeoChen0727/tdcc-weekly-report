from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import argparse
import json
import math
import re
import shutil

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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    limit = {normalize_stock_id(x) for x in args.stock_id} if args.stock_id else None
    if args.incremental_latest:
        manifest = build_history_files_incremental_latest(limit)
    else:
        manifest = build_history_files(limit)
    print(f"Saved {len(manifest)} stock history files under {STOCK_HISTORY_DIR}")
    print(f"Saved manifest: {MANIFEST_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
