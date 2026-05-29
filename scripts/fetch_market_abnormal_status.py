from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import re

import pandas as pd
import requests


LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_DIR = Path("output/history/market_abnormal_status")
DATA_DIR = Path("data/market_abnormal_status")

OUT_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"
OUT_MD = LATEST_DIR / "market_abnormal_status_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
HISTORY_CSV = HISTORY_DIR / "market_abnormal_status_history.csv"

SOURCE_URLS = {
    "twse_disposition": "https://openapi.twse.com.tw/v1/announcement/punish",
    "twse_attention": "https://openapi.twse.com.tw/v1/announcement/notice",
    "twse_attention_note": "https://openapi.twse.com.tw/v1/announcement/notetrans",
    "tpex_disposition": "https://www.tpex.org.tw/openapi/v1/tpex_disposal_information",
    "tpex_attention": "https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_information",
    "tpex_attention_note": "https://www.tpex.org.tw/openapi/v1/tpex_trading_warning_note",
    "tpex_trading_mode": "https://www.tpex.org.tw/openapi/v1/tpex_cmode",
}


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def today_key() -> str:
    return now_taipei().strftime("%Y%m%d")


def normalize_stock_id(value: Any) -> str:
    text = str(value or "").strip()
    m = re.search(r"(?<!\d)(\d{4})(?!\d)", text)
    return m.group(1) if m else ""


def normalize_source_date(value: Any) -> str:
    text = str(value or "").strip()
    digits = re.sub(r"\D", "", text)
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    if len(digits) >= 7:
        # ROC date, e.g. 1150528.
        try:
            year = int(digits[:3]) + 1911
            return f"{year}{digits[3:5]}{digits[5:7]}"
        except Exception:
            return digits
    return digits


def fetch_source(name: str, url: str) -> pd.DataFrame:
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, list):
            return pd.DataFrame()
        df = pd.DataFrame(data)
        snapshot = DATA_DIR / f"{today_key()}_{name}.csv"
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(snapshot, index=False, encoding="utf-8-sig", lineterminator="\n")
        return df
    except Exception as exc:
        return pd.DataFrame(
            [
                {
                    "_fetch_error": str(exc),
                    "_source_name": name,
                    "_source_url": url,
                }
            ]
        )


def add_record(records: list[dict[str, Any]], **kwargs: Any) -> None:
    stock_id = normalize_stock_id(kwargs.get("stock_id", ""))
    if not stock_id:
        return
    record = {
        "fetch_date": today_key(),
        "fetched_at": now_text(),
        "source_market": kwargs.get("source_market", ""),
        "stock_id": stock_id,
        "stock_name": str(kwargs.get("stock_name", "") or "").strip(),
        "is_disposition": bool(kwargs.get("is_disposition", False)),
        "is_attention": bool(kwargs.get("is_attention", False)),
        "is_attention_accumulation": bool(kwargs.get("is_attention_accumulation", False)),
        "is_altered_trading": bool(kwargs.get("is_altered_trading", False)),
        "is_periodic_trading": bool(kwargs.get("is_periodic_trading", False)),
        "is_managed_stock": bool(kwargs.get("is_managed_stock", False)),
        "is_suspension": bool(kwargs.get("is_suspension", False)),
        "announcement_date": normalize_source_date(kwargs.get("announcement_date", "")),
        "source_date_raw": str(kwargs.get("announcement_date", "") or "").strip(),
        "number_of_announcement": str(kwargs.get("number_of_announcement", "") or "").strip(),
        "disposition_period": str(kwargs.get("disposition_period", "") or "").strip(),
        "disposition_measures": str(kwargs.get("disposition_measures", "") or "").strip(),
        "disposition_reason": str(kwargs.get("disposition_reason", "") or "").strip(),
        "attention_reason": str(kwargs.get("attention_reason", "") or "").strip(),
        "attention_accumulation_note": str(kwargs.get("attention_accumulation_note", "") or "").strip(),
        "trading_mode_note": str(kwargs.get("trading_mode_note", "") or "").strip(),
        "source_name": kwargs.get("source_name", ""),
        "source_url": kwargs.get("source_url", ""),
        "data_quality_status": "ok",
    }
    records.append(record)


def normalize_records(sources: dict[str, pd.DataFrame]) -> pd.DataFrame:
    records: list[dict[str, Any]] = []

    for _, row in sources.get("twse_disposition", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TWSE",
            stock_id=row.get("Code"),
            stock_name=row.get("Name"),
            is_disposition=True,
            announcement_date=row.get("Date"),
            number_of_announcement=row.get("NumberOfAnnouncement"),
            disposition_period=row.get("DispositionPeriod"),
            disposition_measures=row.get("DispositionMeasures"),
            disposition_reason=row.get("ReasonsOfDisposition") or row.get("Detail"),
            source_name="twse_disposition",
            source_url=SOURCE_URLS["twse_disposition"],
        )

    for _, row in sources.get("twse_attention", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TWSE",
            stock_id=row.get("Code"),
            stock_name=row.get("Name"),
            is_attention=True,
            announcement_date=row.get("Date"),
            number_of_announcement=row.get("NumberOfAnnouncement"),
            attention_reason=row.get("TradingInfoForAttention"),
            source_name="twse_attention",
            source_url=SOURCE_URLS["twse_attention"],
        )

    for _, row in sources.get("twse_attention_note", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TWSE",
            stock_id=row.get("Code"),
            stock_name=row.get("Name"),
            is_attention_accumulation=True,
            attention_accumulation_note=row.get("RecentlyMetAttentionSecuritiesCriteria"),
            source_name="twse_attention_note",
            source_url=SOURCE_URLS["twse_attention_note"],
        )

    for _, row in sources.get("tpex_disposition", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TPEx",
            stock_id=row.get("SecuritiesCompanyCode"),
            stock_name=row.get("CompanyName"),
            is_disposition=True,
            announcement_date=row.get("Date"),
            disposition_period=row.get("DispositionPeriod"),
            disposition_reason=row.get("DispositionReasons") or row.get("DisposalCondition"),
            disposition_measures=row.get("DisposalCondition"),
            source_name="tpex_disposition",
            source_url=SOURCE_URLS["tpex_disposition"],
        )

    for _, row in sources.get("tpex_attention", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TPEx",
            stock_id=row.get("SecuritiesCompanyCode"),
            stock_name=row.get("CompanyName"),
            is_attention=True,
            announcement_date=row.get("Date"),
            attention_reason=row.get("TradingInformation"),
            source_name="tpex_attention",
            source_url=SOURCE_URLS["tpex_attention"],
        )

    for _, row in sources.get("tpex_attention_note", pd.DataFrame()).iterrows():
        add_record(
            records,
            source_market="TPEx",
            stock_id=row.get("SecuritiesCompanyCode"),
            stock_name=row.get("CompanyName"),
            is_attention_accumulation=True,
            announcement_date=row.get("Date"),
            attention_accumulation_note=row.get("AccumulationSituation"),
            source_name="tpex_attention_note",
            source_url=SOURCE_URLS["tpex_attention_note"],
        )

    for _, row in sources.get("tpex_trading_mode", pd.DataFrame()).iterrows():
        altered = str(row.get("AlteredTrading", "")).strip().upper() == "Ｙ"
        periodic = str(row.get("PeriodicTrading", "")).strip().upper() == "Ｙ"
        managed = str(row.get("ManagedStock", "")).strip().upper() == "Ｙ"
        suspended = str(row.get("SuspensionOfTrading", "")).strip().upper() == "Ｙ"
        if not any([altered, periodic, managed, suspended]):
            continue
        add_record(
            records,
            source_market="TPEx",
            stock_id=row.get("SecuritiesCompanyCode"),
            stock_name=row.get("CompanyName"),
            is_altered_trading=altered,
            is_periodic_trading=periodic,
            is_managed_stock=managed,
            is_suspension=suspended,
            announcement_date=row.get("Date"),
            trading_mode_note=f"altered={altered}; periodic={periodic}; managed={managed}; suspension={suspended}; matching_frequency={row.get('MatchingFrequency', '')}",
            source_name="tpex_trading_mode",
            source_url=SOURCE_URLS["tpex_trading_mode"],
        )

    if not records:
        return pd.DataFrame()

    raw = pd.DataFrame(records)
    bool_cols = [
        "is_disposition",
        "is_attention",
        "is_attention_accumulation",
        "is_altered_trading",
        "is_periodic_trading",
        "is_managed_stock",
        "is_suspension",
    ]
    for col in bool_cols:
        raw[col] = raw[col].astype(bool)

    agg: dict[str, Any] = {
        "fetch_date": "max",
        "fetched_at": "max",
        "source_market": lambda s: "/".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "stock_name": lambda s: next((str(x) for x in s if str(x).strip()), ""),
        "announcement_date": "max",
        "source_date_raw": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "number_of_announcement": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "disposition_period": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "disposition_measures": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "disposition_reason": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "attention_reason": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "attention_accumulation_note": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "trading_mode_note": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "source_name": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "source_url": lambda s: "; ".join(sorted(set(str(x) for x in s if str(x).strip()))),
        "data_quality_status": "first",
    }
    for col in bool_cols:
        agg[col] = "max"

    out = raw.groupby("stock_id", as_index=False).agg(agg)

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
        if bool(row.get("is_attention")) or bool(row.get("is_attention_accumulation")):
            return "C_attention"
        if bool(row.get("is_altered_trading")) or bool(row.get("is_managed_stock")):
            return "B_trading_mode_watch"
        return "A_normal"

    out["market_abnormal_status"] = out.apply(status, axis=1)
    out["market_abnormal_risk_level"] = out.apply(severity, axis=1)
    out["execution_risk_note"] = out.apply(
        lambda row: (
            "處置/分盤或注意交易標的；短線回測需獨立分層，實際進出可能受撮合、保證金或流動性影響。"
            if row["market_abnormal_status"] != "normal"
            else ""
        ),
        axis=1,
    )
    order_cols = [
        "fetch_date",
        "fetched_at",
        "stock_id",
        "stock_name",
        "source_market",
        "market_abnormal_status",
        "market_abnormal_risk_level",
        *bool_cols,
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
    return out[order_cols].sort_values(["market_abnormal_risk_level", "stock_id"], ascending=[False, True]).reset_index(drop=True)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")


def append_history(latest: pd.DataFrame) -> pd.DataFrame:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    if HISTORY_CSV.exists():
        hist = pd.read_csv(HISTORY_CSV, dtype=str, keep_default_na=False)
        combined = pd.concat([hist, latest.astype(str)], ignore_index=True)
    else:
        combined = latest.astype(str).copy()
    combined = combined.drop_duplicates(subset=["fetch_date", "stock_id"], keep="last")
    write_csv(combined, HISTORY_CSV)
    return combined


def build_markdown(latest: pd.DataFrame, sources: dict[str, pd.DataFrame]) -> str:
    lines: list[str] = []
    lines.append("# Market Abnormal Status Latest")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- source: TWSE / TPEx official OpenAPI")
    lines.append("- usage: execution-risk flag for daily candidate, short-term research, and backtest segmentation.")
    lines.append("- limitation: historical backtests can only use this flag after daily snapshots accumulate or a verified historical source is backfilled.")
    lines.append("")
    source_rows = []
    for name, url in SOURCE_URLS.items():
        df = sources.get(name, pd.DataFrame())
        status = "ok" if not df.empty and "_fetch_error" not in df.columns else "fetch_failed"
        source_rows.append([name, status, len(df), url])
    lines.append("## Source Status")
    lines.append(pd.DataFrame(source_rows, columns=["source", "status", "rows", "url"]).to_markdown(index=False))
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
    show_cols = [
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
    lines.append(latest[show_cols].head(120).to_markdown(index=False))
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    sources = {name: fetch_source(name, url) for name, url in SOURCE_URLS.items()}
    latest = normalize_records(sources)
    for path in [OUT_CSV, DOCS_CSV]:
        write_csv(latest, path)
    append_history(latest)
    md = build_markdown(latest, sources)
    for path in [OUT_MD, DOCS_MD]:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(md, encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(latest)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
