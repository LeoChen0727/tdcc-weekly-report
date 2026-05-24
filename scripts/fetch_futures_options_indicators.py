from __future__ import annotations

from io import StringIO
from pathlib import Path
from typing import Any
import json
import math

import pandas as pd
import requests

from tracking_utils import (
    LATEST_DIR,
    DATA_DIR,
    append_update_csv,
    latest_price_date,
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
    return append_update_csv(df, HISTORY_FILES[name], key_cols=key_cols, sort_cols=key_cols)


def fetch_vix_month(yyyymm: str) -> pd.DataFrame:
    url = VIX_FILE_URL.format(yyyymm=yyyymm)
    response = requests.get(url, timeout=45, headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    text = decode_response(response.content)
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
                "source": url,
            }
        )
    return pd.DataFrame(rows)


def fetch_vix_history(months: int = 6) -> pd.DataFrame:
    latest = latest_price_date()
    frames: list[pd.DataFrame] = []
    for month_start in month_starts_back(latest, months):
        frames.append(fetch_vix_month(month_start[:6]))
    frames = [df for df in frames if not df.empty]
    if not frames:
        return pd.DataFrame(columns=["date", "taiwan_vix", "source"])
    df = pd.concat(frames, ignore_index=True, sort=False)
    df["date"] = df["date"].map(normalize_date)
    df["taiwan_vix"] = pd.to_numeric(df["taiwan_vix"], errors="coerce")
    df = df.dropna(subset=["date", "taiwan_vix"])
    df = df.drop_duplicates(["date"], keep="last").sort_values("date").reset_index(drop=True)
    for window in [5, 10, 20]:
        df[f"vix_return_{window}d"] = df["taiwan_vix"].pct_change(window) * 100
    return df


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


def build_indicator_row(
    institutional_fo: pd.DataFrame,
    futures_contracts: pd.DataFrame,
    options_call_put: pd.DataFrame,
    put_call_ratio: pd.DataFrame,
    vix: pd.DataFrame,
    source_status: dict[str, Any],
) -> pd.DataFrame:
    pc = latest_row(put_call_ratio)
    vix_latest = latest_row(vix, "date")
    fo_date = latest_date_from_df(institutional_fo) if not institutional_fo.empty else ""
    pc_date = safe_str(pc.get("日期", "")) if pc is not None else ""
    vix_date = safe_str(vix_latest.get("date", "")) if vix_latest is not None else ""
    date = max([d for d in [fo_date, pc_date, vix_date] if d] or [latest_price_date()])
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
    row["source_status"] = "ready" if all(source_status.get(k) == "ok" for k in SOURCES) else "partial"
    return pd.DataFrame([row])


def write_status(status: dict[str, Any]) -> None:
    STATUS_JSON.parent.mkdir(parents=True, exist_ok=True)
    STATUS_JSON.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
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
    STATUS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    FO_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    status: dict[str, Any] = {"generated_at": now_text(), "sources": {}}
    frames: dict[str, pd.DataFrame] = {}

    key_map = {
        "institutional_fo": ["日期", "身份別"],
        "futures_contracts": ["日期", "商品名稱", "身份別"],
        "options_call_put": ["日期", "商品名稱", "買賣權別", "身份別"],
        "put_call_ratio": ["日期"],
    }

    for name, data_name in SOURCES.items():
        try:
            df = fetch_open_data(data_name)
            frames[name] = save_source(name, df, key_map[name])
            status["sources"][name] = {
                "status": "ok",
                "rows": len(df),
                "latest_date": latest_date_from_df(df),
                "message": "",
            }
        except Exception as exc:
            frames[name] = read_csv(HISTORY_FILES.get(name, Path("")), dtype=str)
            status["sources"][name] = {
                "status": "fallback_history" if not frames[name].empty else "missing",
                "rows": len(frames[name]),
                "latest_date": latest_date_from_df(frames[name]) if not frames[name].empty else "",
                "message": str(exc),
            }

    try:
        vix = fetch_vix_history(months=6)
        if not vix.empty:
            write_csv(vix, LATEST_FILES["taiwan_vix"])
            frames["taiwan_vix"] = append_update_csv(vix, HISTORY_FILES["taiwan_vix"], key_cols=["date"], sort_cols=["date"])
            status["sources"]["taiwan_vix"] = {
                "status": "ok",
                "rows": len(vix),
                "latest_date": latest_date_from_df(vix.rename(columns={"date": "日期"})),
                "message": "",
            }
        else:
            raise RuntimeError("TAIFEX VIX monthly files returned no usable rows")
    except Exception as exc:
        frames["taiwan_vix"] = read_csv(HISTORY_FILES["taiwan_vix"], dtype=str)
        status["sources"]["taiwan_vix"] = {
            "status": "fallback_history" if not frames["taiwan_vix"].empty else "missing",
            "rows": len(frames["taiwan_vix"]),
            "latest_date": latest_date_from_df(frames["taiwan_vix"].rename(columns={"date": "日期"})) if not frames["taiwan_vix"].empty else "",
            "message": str(exc),
        }

    indicator = build_indicator_row(
        frames.get("institutional_fo", pd.DataFrame()),
        frames.get("futures_contracts", pd.DataFrame()),
        frames.get("options_call_put", pd.DataFrame()),
        frames.get("put_call_ratio", pd.DataFrame()),
        frames.get("taiwan_vix", pd.DataFrame()),
        {k: v.get("status") for k, v in status["sources"].items()},
    )
    write_csv(indicator, INDICATORS_CSV)

    status["overall_status"] = "ready" if indicator.iloc[0].get("source_status") == "ready" else "partial"
    status["indicator_path"] = INDICATORS_CSV.as_posix()
    write_status(status)
    print(f"Saved: {INDICATORS_CSV}")
    print(f"Saved: {STATUS_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
