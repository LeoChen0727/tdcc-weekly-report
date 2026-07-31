from __future__ import annotations

from datetime import datetime
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo
import hashlib
import json
import math
import re
from typing import Any

import pandas as pd
import requests


REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

LATEST_DIR = Path("output/latest")
RESEARCH_LATEST_DIR = LATEST_DIR / "research_backtest"
DOCS_LATEST_DIR = Path("docs/latest")
DATA_DIR = Path("data")
HISTORY_DIR = Path("output/history")
DAILY_SIGNALS_DIR = HISTORY_DIR / "daily_signals"
TDCC_SIGNALS_DIR = HISTORY_DIR / "tdcc_signals"
DAILY_PRICE_DIR = DATA_DIR / "daily_price"
STOCK_PRICE_HISTORY_DIR = DATA_DIR / "stock_price_history"
MARKET_INDEX_PATH = DATA_DIR / "market_index_history.csv"
MARKET_INDEX_OHLC_PATH = DATA_DIR / "market_index_ohlc_history.csv"
MARKET_INDEX_SOURCE_PROVENANCE: list[dict[str, Any]] = []

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
    df.to_csv(p, index=False, encoding="utf-8", lineterminator="\n")


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
    actual = latest_stock_price_history_date()
    if actual:
        return actual
    for path in DAILY_PRICE_DIR.glob("*.csv"):
        date = normalize_date(path.stem)
        if date:
            dates.append(date)
    return max(dates) if dates else now_taipei().strftime("%Y%m%d")


@lru_cache(maxsize=1)
def latest_stock_price_history_date() -> str:
    """Return the newest real stock-history trade date.

    Daily price fetches can create weekend/report-date CSVs that repeat the
    previous trading day's prices. Per-stock histories are the safer guardrail
    because they are only appended with accepted trading rows.
    """
    dates: list[str] = []
    if not STOCK_PRICE_HISTORY_DIR.exists():
        return ""
    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        try:
            df = pd.read_csv(path, dtype=str, usecols=["date"])
        except Exception:
            continue
        if df.empty:
            continue
        series = df["date"].map(normalize_date)
        series = series[series.astype(str).str.len().eq(8)]
        if not series.empty:
            dates.append(str(series.max()))
    return max(dates) if dates else ""


def resolve_candidate_signal_date(candidates: pd.DataFrame, preferred_date: str = "") -> tuple[str, list[str]]:
    """Resolve the effective signal date for daily candidate tracking.

    `all_candidates_latest.csv` can contain dates copied from category source
    files or from the workflow execution date. The canonical daily candidate
    signal date is the latest accepted market price date (`preferred_date`).
    Use it whenever available so weekend/report execution dates cannot leak
    into model signals.
    """
    preferred = normalize_date(preferred_date)
    notes: list[str] = []
    if candidates.empty:
        return preferred, ["empty_candidates"]

    signal_dates: set[str] = set()
    if "signal_date" in candidates.columns:
        signal_dates = {normalize_date(x) for x in candidates["signal_date"].tolist()}
        signal_dates.discard("")
        if preferred:
            if signal_dates and signal_dates != {preferred}:
                notes.append(
                    f"candidate signal_date values={sorted(signal_dates)} differ from preferred_date={preferred}; "
                    "using preferred_date"
                )
            return preferred, notes
        if len(signal_dates) == 1:
            resolved = next(iter(signal_dates))
            return resolved, notes
        if signal_dates:
            resolved = max(signal_dates)
            notes.append(f"multiple signal_date values={sorted(signal_dates)}; using latest={resolved}")
            return resolved, notes

    candidate_dates: set[str] = set()
    if "date" in candidates.columns:
        candidate_dates = {normalize_date(x) for x in candidates["date"].tolist()}
        candidate_dates.discard("")
        if preferred:
            if candidate_dates and candidate_dates != {preferred}:
                notes.append(
                    f"candidate date column has source dates={sorted(candidate_dates)}; using preferred_date={preferred}"
                )
            return preferred, notes
        if candidate_dates:
            resolved = max(candidate_dates)
            return resolved, notes

    return preferred, notes


def normalize_report_candidate_dates(df: pd.DataFrame, preferred_date: str = "") -> pd.DataFrame:
    """Keep report-facing candidate dates aligned with the accepted price date.

    `build_all_candidates_latest.py` is responsible for source-level date
    gating.  Later enrichment scripts rewrite the same table to add warrant,
    catalyst, repeat, theme, and decision fields; those rewrites must not
    reintroduce stale source dates or the workflow execution date into public
    report columns.
    """
    out = df.copy()
    if out.empty:
        return out

    target_date = normalize_date(preferred_date) or main_price_date_from_freshness()
    if not target_date:
        return out

    if "source_date" in out.columns:
        source_values = out["source_date"].map(normalize_date)
    elif "date" in out.columns:
        source_values = out["date"].map(normalize_date)
    else:
        source_values = pd.Series([""] * len(out), index=out.index, dtype="object")

    if "raw_source_date" not in out.columns:
        out["raw_source_date"] = source_values
    else:
        out["raw_source_date"] = out["raw_source_date"].where(
            out["raw_source_date"].astype(str).str.strip() != "",
            source_values,
        )
        out["raw_source_date"] = out["raw_source_date"].map(normalize_date)

    for col in ["main_price_date", "signal_date", "date", "source_date"]:
        out[col] = target_date

    return out


def main_price_date_from_freshness() -> str:
    freshness = read_csv(LATEST_DIR / "data_freshness_latest.csv", dtype=str)
    if not freshness.empty:
        row = freshness.iloc[0]
        for col in ["main_price_date", "actual_stock_price_history_date", "all_candidates_date", "official_price_fetch_date"]:
            if col in freshness.columns:
                date = normalize_date(row.get(col, ""))
                if date:
                    return date
    actual_price_date = latest_stock_price_history_date()
    if actual_price_date:
        return actual_price_date
    return latest_price_date()


def require_daily_report_ready_main_price_date() -> str:
    freshness_path = LATEST_DIR / "data_freshness_latest.csv"
    freshness = read_csv(freshness_path, dtype=str, keep_default_na=False)
    if freshness.empty:
        raise RuntimeError(f"{freshness_path.as_posix()} is required for formal daily report generation")

    row = freshness.iloc[0]
    main_date = normalize_date(row.get("main_price_date", ""))
    if not main_date:
        raise RuntimeError("data_freshness_latest.csv must contain main_price_date for formal daily report generation")

    for col in ["report_ready", "daily_pdf_ready"]:
        value = safe_str(row.get(col, "")).lower()
        if value not in {"true", "1", "yes", "y"}:
            raise RuntimeError(f"{col} must be True before formal daily report generation; observed={row.get(col, '')!r}")

    warrant_ready = safe_str(row.get("warrant_ready", "")).lower() in {"true", "1", "yes", "y"}
    warrant_grace = (
        safe_str(row.get("warrant_source_status", "")) == "warning_grace"
        and safe_str(row.get("warrant_daily_publish_allowed", "")).lower() in {"true", "1", "yes", "y"}
        and safe_str(row.get("warrant_pdf_visibility", "")) == "hidden_unavailable"
        and safe_str(row.get("warrant_model_effect_allowed", "")).lower() not in {"true", "1", "yes", "y"}
        and safe_str(row.get("warrant_pdf_effect_allowed", "")).lower() not in {"true", "1", "yes", "y"}
    )
    if not warrant_ready and not warrant_grace:
        raise RuntimeError(
            "warrant_ready must be True before formal daily report generation unless bounded "
            f"warrant_unavailable grace hides warrant effects; observed={row.get('warrant_ready', '')!r}"
        )

    return main_date


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


def recent_market_index_fetch_months(
    latest_date: str,
    old: pd.DataFrame,
    months: int = 18,
    refresh_recent_months: int = 2,
) -> list[str]:
    """Return month starts that should be fetched for market index history.

    The initial build still backfills the requested history window.  Once a
    usable history exists, daily pipeline runs only refresh the newest months;
    otherwise the workflow repeatedly re-downloads 18 months of TWSE/TPEx
    market data and can stall on official endpoints.
    """

    all_months = month_starts_back(latest_date, months)
    if old.empty:
        return all_months

    needs_full_refresh = False
    if "ohlc_available" not in old.columns:
        needs_full_refresh = True
    else:
        available = old["ohlc_available"].astype(str).str.lower().isin(["true", "1", "yes"])
        known_codes = set(old.loc[available, "index_code"].astype(str)) if "index_code" in old.columns else set()
        if not {"TWSE", "TPEX"}.issubset(known_codes):
            needs_full_refresh = True

    if needs_full_refresh:
        return all_months

    latest = normalize_date(latest_date) or now_taipei().strftime("%Y%m%d")
    latest_month = latest[:6]
    if "date" in old.columns:
        old_dates = old["date"].map(normalize_date)
        old_dates = old_dates[old_dates.astype(str).str.len().eq(8)]
        old_latest = str(old_dates.max()) if not old_dates.empty else ""
    else:
        old_latest = ""

    recent = all_months[-max(1, refresh_recent_months) :]
    if old_latest and old_latest[:6] == latest_month and old_latest >= latest:
        return recent

    # If the latest trading day is not present yet, refresh every missing month
    # from the newest known month through the latest month.
    if old_latest and old_latest[:6] in {m[:6] for m in all_months}:
        old_month_start = f"{old_latest[:6]}01"
        missing_forward = [m for m in all_months if m >= old_month_start]
        return sorted(set(recent + missing_forward))

    return recent


def reset_market_index_source_provenance() -> None:
    MARKET_INDEX_SOURCE_PROVENANCE.clear()


def market_index_source_provenance() -> list[dict[str, Any]]:
    return [dict(row) for row in MARKET_INDEX_SOURCE_PROVENANCE]


def fetch_json_with_provenance(url: str, *, timeout: int = 30) -> Any:
    response = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()
    raw = getattr(response, "content", None)
    if not isinstance(raw, bytes):
        raw = json.dumps(data, ensure_ascii=False, sort_keys=True).encode("utf-8")
    normalized = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    MARKET_INDEX_SOURCE_PROVENANCE.append(
        {
            "endpoint": url,
            "params": {},
            "fetched_at": now_text(),
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "normalized_sha256": hashlib.sha256(normalized).hexdigest(),
        }
    )
    return data


def fetch_twse_index_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date={month_start}&response=json"
    try:
        data = fetch_json_with_provenance(url)
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


def fetch_twse_index_ohlc_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.twse.com.tw/rwd/zh/TAIEX/MI_5MINS_HIST?date={month_start}&response=json"
    try:
        data = fetch_json_with_provenance(url)
    except Exception as exc:
        print(f"WARNING: TWSE index OHLC fetch failed {month_start}: {exc}")
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
        rows.append(
            {
                "date": date,
                "index_code": "TWSE",
                "index_name": "TAIEX",
                "open": to_number(item[1]),
                "high": to_number(item[2]),
                "low": to_number(item[3]),
                "close": to_number(item[4]),
                "ohlc_source": url,
                "ohlc_available": True,
            }
        )
    return pd.DataFrame(rows)


def fetch_twse_index_turnover_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/FMTQIK?date={month_start}&response=json"
    try:
        data = fetch_json_with_provenance(url)
    except Exception as exc:
        print(f"WARNING: TWSE index turnover fetch failed {month_start}: {exc}")
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
        rows.append(
            {
                "date": date,
                "index_code": "TWSE",
                "volume": to_number(item[1]) if len(item) > 1 else math.nan,
                "turnover_value": to_number(item[2]) if len(item) > 2 else math.nan,
                "transactions": to_number(item[3]) if len(item) > 3 else math.nan,
                "turnover_source": url,
            }
        )
    return pd.DataFrame(rows)


def fetch_tpex_index_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.tpex.org.tw/www/zh-tw/indexInfo/inx?date={roc_month_from_yyyymmdd(month_start)}&response=json"
    try:
        data = fetch_json_with_provenance(url)
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


def fetch_tpex_index_ohlc_month(month_start: str) -> pd.DataFrame:
    url = f"https://www.tpex.org.tw/www/zh-tw/indexInfo/inx?date={roc_month_from_yyyymmdd(month_start)}&response=json"
    try:
        data = fetch_json_with_provenance(url)
    except Exception as exc:
        print(f"WARNING: TPEx index OHLC fetch failed {month_start}: {exc}")
        return pd.DataFrame()

    rows: list[dict[str, Any]] = []
    for table in data.get("tables", []) or []:
        for item in table.get("data", []) or []:
            if len(item) < 5:
                continue
            rows.append(
                {
                    "date": normalize_date(item[0]),
                    "index_code": "TPEX",
                    "index_name": "TPEx",
                    "open": to_number(item[1]),
                    "high": to_number(item[2]),
                    "low": to_number(item[3]),
                    "close": to_number(item[4]),
                    "ohlc_source": url,
                    "ohlc_available": True,
                }
            )
    return pd.DataFrame(rows)


def fetch_tpex_index_turnover_latest() -> pd.DataFrame:
    url = "https://www.tpex.org.tw/openapi/v1/tpex_daily_trading_index"
    try:
        data = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"}).json()
    except Exception as exc:
        print(f"WARNING: TPEx index turnover fetch failed: {exc}")
        return pd.DataFrame()

    if not isinstance(data, list):
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for item in data:
        date_raw = safe_str(item.get("Date", ""))
        if len(date_raw) == 7 and date_raw[:3].isdigit():
            date = f"{int(date_raw[:3]) + 1911:04d}{date_raw[3:5]}{date_raw[5:7]}"
        else:
            date = normalize_date(date_raw)
        rows.append(
            {
                "date": date,
                "index_code": "TPEX",
                "volume": to_number(item.get("TradeVolume", "")),
                "turnover_value": to_number(item.get("TradeAmount", "")),
                "transactions": to_number(item.get("NumberOfTransactions", "")),
                "turnover_source": url,
            }
        )
    return pd.DataFrame(rows)


def build_market_index_ohlc_history(
    months: int = 18,
    target_date: str = "",
    target_index_codes: set[str] | None = None,
) -> pd.DataFrame:
    target = normalize_date(target_date)
    if target_date and not target:
        raise RuntimeError(f"invalid market-index target_date: {target_date}")
    latest = target or latest_price_date()
    requested_codes = set(target_index_codes or {"TWSE", "TPEX"})
    if not requested_codes or not requested_codes.issubset({"TWSE", "TPEX"}):
        raise RuntimeError(f"invalid market-index target codes: {sorted(requested_codes)}")
    frames: list[pd.DataFrame] = []
    old = read_csv(MARKET_INDEX_OHLC_PATH, dtype=str)
    if not old.empty:
        frames.append(old)
    fetch_months = (
        [f"{target[:6]}01"]
        if target
        else recent_market_index_fetch_months(latest, old, months=months)
    )
    print(
        "Market index OHLC fetch months="
        f"{len(fetch_months)} latest={latest} months={','.join(fetch_months)}"
    )
    fetched_ohlc_frames: list[pd.DataFrame] = []
    for month_start in fetch_months:
        if "TWSE" in requested_codes:
            fetched_ohlc_frames.append(fetch_twse_index_ohlc_month(month_start))
        if "TPEX" in requested_codes:
            fetched_ohlc_frames.append(fetch_tpex_index_ohlc_month(month_start))
    fetched_ohlc_frames = [df for df in fetched_ohlc_frames if not df.empty]
    if target:
        exact_frames = []
        for frame in fetched_ohlc_frames:
            exact = frame.copy()
            exact["date"] = exact["date"].map(normalize_date)
            exact = exact[exact["date"].eq(target)].copy()
            if not exact.empty:
                exact_frames.append(exact)
        fetched_ohlc_frames = exact_frames
        observed_codes = {
            safe_str(value)
            for frame in fetched_ohlc_frames
            for value in frame.get("index_code", pd.Series(dtype=str)).tolist()
        }
        if observed_codes != requested_codes:
            raise RuntimeError(
                "market-index historical fetch requires exact TWSE/TPEX target rows: "
                f"target_date={target} observed={','.join(sorted(observed_codes))}"
            )
    if not fetched_ohlc_frames and target:
        raise RuntimeError(f"market-index historical fetch returned no target rows: {target}")
    if not frames and not fetched_ohlc_frames:
        return pd.DataFrame()
    fetched_ohlc = pd.concat(fetched_ohlc_frames, ignore_index=True, sort=False)
    fetched_ohlc["date"] = fetched_ohlc["date"].map(normalize_date)
    fetched_ohlc = fetched_ohlc[fetched_ohlc["date"] != ""].copy()
    fetched_ohlc = fetched_ohlc.drop_duplicates(["date", "index_code"], keep="last")

    turnover_frames: list[pd.DataFrame] = []
    if "TWSE" in requested_codes:
        for month_start in fetch_months:
            turnover_frames.append(fetch_twse_index_turnover_month(month_start))
    if not target and "TPEX" in requested_codes:
        turnover_frames.append(fetch_tpex_index_turnover_latest())
    turnover_frames = [df for df in turnover_frames if not df.empty]
    if turnover_frames:
        turnover = pd.concat(turnover_frames, ignore_index=True, sort=False)
        turnover["date"] = turnover["date"].map(normalize_date)
        turnover = turnover[turnover["date"] != ""].copy()
        if target:
            turnover = turnover[turnover["date"].eq(target)].copy()
        turnover = turnover.drop_duplicates(["date", "index_code"], keep="last")
        fetched_ohlc = fetched_ohlc.merge(
            turnover,
            on=["date", "index_code"],
            how="left",
            suffixes=("", "_turnover"),
        )
        for col in ["volume", "turnover_value", "transactions", "turnover_source"]:
            turnover_col = f"{col}_turnover"
            if turnover_col in fetched_ohlc.columns:
                if col in fetched_ohlc.columns:
                    fetched_ohlc[col] = fetched_ohlc[col].where(
                        fetched_ohlc[col].notna() & (fetched_ohlc[col].astype(str) != ""),
                        fetched_ohlc[turnover_col],
                    )
                else:
                    fetched_ohlc[col] = fetched_ohlc[turnover_col]
                fetched_ohlc = fetched_ohlc.drop(columns=[turnover_col])

    for col in ["open", "high", "low", "close", "volume", "turnover_value", "transactions"]:
        if col not in fetched_ohlc.columns:
            fetched_ohlc[col] = math.nan
        fetched_ohlc[col] = pd.to_numeric(fetched_ohlc[col], errors="coerce")
    fetched_ohlc["ohlc_available"] = fetched_ohlc[["open", "high", "low", "close"]].notna().all(axis=1)
    fetched_ohlc["volume_available"] = fetched_ohlc["volume"].notna()
    if target:
        if old.empty:
            ohlc = fetched_ohlc
        else:
            # Historical point repair must not expand the persisted schema and
            # thereby mutate untouched index rows merely because an endpoint
            # returned an additional source-only field.
            for col in old.columns:
                if col not in fetched_ohlc.columns:
                    fetched_ohlc[col] = ""
            fetched_ohlc = fetched_ohlc[list(old.columns)].copy()
            old_dates = old["date"].map(normalize_date)
            replace_mask = old_dates.eq(target) & old["index_code"].astype(str).isin(requested_codes)
            old_non_target = old[~replace_mask].copy()
            ohlc = pd.concat([old_non_target, fetched_ohlc], ignore_index=True, sort=False)
    else:
        ohlc = pd.concat([*frames, fetched_ohlc], ignore_index=True, sort=False)
        ohlc["date"] = ohlc["date"].map(normalize_date)
        ohlc = ohlc[ohlc["date"] != ""].copy()
        ohlc = ohlc.drop_duplicates(["date", "index_code"], keep="last")
    ohlc = ohlc.sort_values(["index_code", "date"]).reset_index(drop=True)
    write_csv(ohlc, MARKET_INDEX_OHLC_PATH)
    return ohlc


def update_market_index_history(
    months: int = 18,
    target_date: str = "",
    target_index_codes: set[str] | None = None,
) -> pd.DataFrame:
    target = normalize_date(target_date)
    if target_date and not target:
        raise RuntimeError(f"invalid market-index target_date: {target_date}")
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    requested_codes = set(target_index_codes or {"TWSE", "TPEX"})
    if not requested_codes or not requested_codes.issubset({"TWSE", "TPEX"}):
        raise RuntimeError(f"invalid market-index target codes: {sorted(requested_codes)}")
    ohlc = build_market_index_ohlc_history(
        months=months,
        target_date=target,
        target_index_codes=requested_codes,
    )
    latest = target or latest_price_date()
    old = read_csv(MARKET_INDEX_PATH, dtype=str)
    frames: list[pd.DataFrame] = [old] if not old.empty else []
    if ohlc.empty:
        # Close-only endpoints are a fallback for environments where the
        # official OHLC endpoints are temporarily unavailable.
        for month_start in month_starts_back(latest, months):
            frames.append(fetch_twse_index_month(month_start))
            frames.append(fetch_tpex_index_month(month_start))
    if not ohlc.empty and not target:
        # Keep official OHLC rows last so close-only legacy sources cannot
        # overwrite candlestick-ready data for the same index/date.
        frames.append(ohlc)
    if target:
        target_ohlc = ohlc[
            ohlc["date"].map(normalize_date).eq(target)
            & ohlc["index_code"].astype(str).isin(requested_codes)
        ].copy()
        target_codes = set(target_ohlc["index_code"].astype(str))
        if target_codes != requested_codes or len(target_ohlc) != len(requested_codes):
            raise RuntimeError(
                "market-index histories must receive one exact TWSE/TPEX OHLC row for "
                f"target_date={target}"
            )
        old_dates = old["date"].map(normalize_date) if not old.empty else pd.Series(dtype=str)
        replace_mask = (
            old_dates.eq(target) & old["index_code"].astype(str).isin(requested_codes)
            if not old.empty
            else pd.Series(dtype=bool)
        )
        old_non_target = old[~replace_mask].copy() if not old.empty else pd.DataFrame()
        calculation = pd.concat(
            [old[old_dates.lt(target)].copy() if not old.empty else pd.DataFrame(), target_ohlc],
            ignore_index=True,
            sort=False,
        )
        calculation["date"] = calculation["date"].map(normalize_date)
        calculation["close"] = pd.to_numeric(calculation["close"], errors="coerce")
        calculation = calculation.dropna(subset=["date", "index_code", "close"])
        calculation = calculation.drop_duplicates(["date", "index_code"], keep="last")
        calculation = calculation.sort_values(["index_code", "date"]).reset_index(drop=True)
        calculation_context_max_date_by_index = {
            code: str(
                calculation[calculation["index_code"].astype(str).eq(code)]["date"].max()
            )
            for code in sorted(requested_codes)
        }
        if calculation_context_max_date_by_index != {
            code: target for code in sorted(requested_codes)
        }:
            raise RuntimeError(
                "market-index calculation context max date mismatch: "
                f"target={target} observed={calculation_context_max_date_by_index}"
            )
        for col in ["open", "high", "low", "volume", "turnover_value", "transactions"]:
            if col not in target_ohlc.columns:
                target_ohlc[col] = math.nan
            target_ohlc[col] = pd.to_numeric(target_ohlc[col], errors="coerce")
        target_ohlc["close"] = pd.to_numeric(target_ohlc["close"], errors="coerce")
        for col in ["open", "high", "low"]:
            target_ohlc[col] = target_ohlc[col].fillna(target_ohlc["close"])
        target_ohlc["ohlc_available"] = target_ohlc[["open", "high", "low", "close"]].notna().all(axis=1)
        target_ohlc["volume_available"] = target_ohlc["volume"].notna()
        for code in sorted(requested_codes):
            part = calculation[calculation["index_code"].astype(str).eq(code)].sort_values("date")
            target_mask = target_ohlc["index_code"].astype(str).eq(code)
            for window in [5, 10, 20, 60]:
                values = part["close"].pct_change(window) * 100
                target_ohlc.loc[target_mask, f"return_{window}d"] = values.iloc[-1]
            target_ohlc.loc[target_mask, "ma20"] = part["close"].rolling(20).mean().iloc[-1]
            target_ohlc.loc[target_mask, "ma60"] = part["close"].rolling(60).mean().iloc[-1]
            target_ohlc.loc[target_mask, "above_ma20"] = bool(
                part["close"].iloc[-1] >= part["close"].rolling(20).mean().iloc[-1]
            )
            target_ohlc.loc[target_mask, "above_ma60"] = bool(
                part["close"].iloc[-1] >= part["close"].rolling(60).mean().iloc[-1]
            )
        df = pd.concat([old_non_target, target_ohlc], ignore_index=True, sort=False)
        df = df.sort_values(["index_code", "date"]).reset_index(drop=True)
        df.attrs["target_calculation_context_max_date_by_index"] = (
            calculation_context_max_date_by_index
        )
    else:
        frames = [df for df in frames if not df.empty]
        if not frames:
            return pd.DataFrame()
        df = pd.concat(frames, ignore_index=True, sort=False)
        df["date"] = df["date"].map(normalize_date)
        for col in ["open", "high", "low", "close", "volume", "turnover_value", "transactions"]:
            if col not in df.columns:
                df[col] = math.nan
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df = df.dropna(subset=["date", "index_code", "close"])
        df = df.drop_duplicates(["date", "index_code"], keep="last")
        df = df.sort_values(["index_code", "date"]).reset_index(drop=True)
        if "ohlc_available" in df.columns:
            source_ohlc_available = df["ohlc_available"].astype(str).str.lower().isin(["true", "1", "yes"])
        else:
            source_ohlc_available = pd.Series(False, index=df.index)
        raw_ohlc_available = df[["open", "high", "low", "close"]].notna().all(axis=1)
        for col in ["open", "high", "low"]:
            df[col] = df[col].fillna(df["close"])
        df["ohlc_available"] = source_ohlc_available | raw_ohlc_available
        df["volume_available"] = df["volume"].notna()
        for window in [5, 10, 20, 60]:
            col = f"return_{window}d"
            df[col] = pd.to_numeric(df[col], errors="coerce") if col in df.columns else math.nan
        for col in ["ma20", "ma60"]:
            df[col] = pd.to_numeric(df[col], errors="coerce") if col in df.columns else math.nan
        for col in ["above_ma20", "above_ma60"]:
            if col in df.columns:
                df[col] = df[col].astype(str).str.lower().isin(["true", "1", "yes"])
            else:
                df[col] = False
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
    latest_path = LATEST_DIR / "market_benchmark_latest.csv"
    existing_latest = read_csv(latest_path, dtype=str)
    existing_latest_date = ""
    if not existing_latest.empty and "date" in existing_latest.columns:
        existing_dates = existing_latest["date"].map(normalize_date)
        existing_dates = existing_dates[existing_dates != ""]
        existing_latest_date = str(existing_dates.max()) if not existing_dates.empty else ""
    if not target or not existing_latest_date or target >= existing_latest_date:
        write_csv(latest_rows, latest_path)
    return df


def load_market_index_history(update_if_missing: bool = True) -> pd.DataFrame:
    df = read_csv(MARKET_INDEX_PATH, dtype=str)
    if df.empty and update_if_missing:
        df = update_market_index_history()
    if df.empty:
        return df
    df["date"] = df["date"].map(normalize_date)
    for col in ["open", "high", "low", "close", "volume", "turnover_value", "ma20", "ma60", "return_5d", "return_10d", "return_20d", "return_60d"]:
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
