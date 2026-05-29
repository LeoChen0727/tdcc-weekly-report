from __future__ import annotations

from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import argparse
import re

import pandas as pd
import requests
from pypdf import PdfReader


ROOT = Path(".")
DATA_DIR = ROOT / "data" / "msci_index_reviews"
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
HISTORY_DIR = ROOT / "output" / "history" / "msci_index_reviews"
PRICE_DIR = ROOT / "data" / "stock_price_history"
INDEX_OHLC = ROOT / "data" / "market_index_ohlc_history.csv"

EVENTS_CSV = DATA_DIR / "msci_taiwan_rebalance_events.csv"
EVENTS_LATEST_CSV = LATEST_DIR / "msci_taiwan_rebalance_events_latest.csv"
BACKTEST_CSV = HISTORY_DIR / "msci_taiwan_rebalance_event_backtest.csv"
BACKTEST_LATEST_CSV = LATEST_DIR / "msci_taiwan_rebalance_backtest_latest.csv"
BACKTEST_LATEST_MD = LATEST_DIR / "msci_taiwan_rebalance_backtest_latest.md"
DOCS_BACKTEST_CSV = DOCS_LATEST_DIR / BACKTEST_LATEST_CSV.name
DOCS_BACKTEST_MD = DOCS_LATEST_DIR / BACKTEST_LATEST_MD.name

USER_AGENT = "Mozilla/5.0 (compatible; tdcc-weekly-report-msci-research/1.0)"

DEFAULT_REVIEW_CODES = [
    "Feb25",
    "May25",
    "Aug25",
    "Nov25",
    "Feb26",
    "May26",
]

MSCI_SOURCES = {
    "global_standard": "https://www.msci.com/eqb/gimi/stdindex/MSCI_{code}_STPublicList.pdf",
    "small_cap": "https://www.msci.com/eqb/gimi/smallcap/MSCI_{code}_SCPublicList.pdf",
}

# MSCI public lists use English issuer names. Keep the mapping explicit and
# conservative; unmatched names stay in the event file but are excluded from
# price-return backtests until verified.
MSCI_TAIWAN_NAME_TO_ID = {
    "ABILITY ENTERPRISE CO": "2374",
    "ACER": "2353",
    "ADLINK TECHNOLOGY": "6166",
    "ADVANCETEK ENTERPRISE CO": "1442",
    "ALL RING TECH": "6187",
    "ANDES TECHNOLOGY": "6533",
    "ASIA CEMENT CORP": "1102",
    "ASPEED TECHNOLOGY": "5274",
    "AUO CORP": "2409",
    "BIZLINK HOLDING": "3665",
    "CALIWAY BIOPHARMA": "6919",
    "CATCHER TECH CO": "2474",
    "CHANNEL WELL TECH CO": "3078",
    "CHENG SHIN RUBBER IND": "2105",
    "CHINA AIRLINES": "2610",
    "CHROMA ATE": "2360",
    "COMPAL ELECTRONICS": "2324",
    "DONG FANG OFFSHORE": "7786",
    "DYNAMIC HOLDING": "3715",
    "ECLAT TEXTILE COMPANY": "1476",
    "EIRGENIX": "6589",
    "ELITE MATERIAL CO": "2383",
    "EZCONN": "6442",
    "FAR EASTERN NEW CENTURY": "1402",
    "FENG TAY ENTERPRISE CO": "9910",
    "FORMOSA ADVANCED TECH": "8131",
    "FULGENT SUN INTL HLDG": "9802",
    "FULLTECH FIBER GLASS": "1815",
    "GALLANT MICRO MACHINING": "6640",
    "GENERAL INTERFACE SOLN": "6456",
    "GOLD CIRCUIT ELECTRONICS": "2368",
    "GREAT TREE PHARMACY": "6469",
    "HD RENEWABLE ENERGY": "6873",
    "HONPRECISION": "2317",
    "HON HAI PRECISION": "2317",
    "HOTA INDUSTRIAL MFG CO": "1536",
    "HU LANE ASSOCIATE": "6279",
    "J&V ENERGY TECHNOLOGY": "6869",
    "KENMEC MECHANICAL ENGR": "6125",
    "KERRY TJ LOGISTICS CO": "2608",
    "KING SLIDE WORKS CO": "2059",
    "KING YUAN ELECTRONICS CO": "2449",
    "LELON ELECTRONICS CORP": "2472",
    "LONGWELL CO": "6290",
    "LUNG YEN CO": "5530",
    "MICRO-STAR INTERNATIONAL": "2377",
    "MPI CORP": "6223",
    "NANYA TECHNOLOGY": "2408",
    "NICHIDENBO": "3090",
    "NIEN MADE ENTERPRISE CO": "8464",
    "PAN GERMAN UNIVERSAL": "3687",
    "PLAYNITRIDE": "6854",
    "POLARIS GROUP": "6550",
    "POSIFLEX": "8114",
    "POU CHEN CORP": "9904",
    "RUENTEX DEVELOPMENT CO": "9945",
    "SDI CORPORATION": "2351",
    "SHINFOX ENERGY": "6806",
    "SILERGY CORP": "6415",
    "SINCERE NAVIGATION": "2605",
    "SPORTS GEAR": "6768",
    "STARLUX AIRLINES": "2646",
    "SYNNEX TECHNOLOGY INTL": "2347",
    "SYNTEC TECHNOLOGY": "7751",
    "TAIFLEX SCIENTIFIC": "8039",
    "TAIMED BIOLOGICS": "4147",
    "TAIWAN HIGH SPEED RAIL": "2633",
    "TAIWAN MICROLOOPS": "6835",
    "TAIWAN PAIHO": "9938",
    "TAIWAN SPECIALITY CHEM": "4772",
    "TECO ELECTRIC & MACH": "1504",
    "TIGERAIR TAIWAN": "6757",
    "TOPKEY CORP": "4536",
    "TOPOINT TECHNOLOGY CO": "8021",
    "TPK HOLDING CO": "3673",
    "VOLTRONIC POWER TECH": "6409",
    "WALSIN LIHWA CORP": "1605",
    "WPG HOLDINGS CO": "3702",
    "YUNGSHIN CONST & DEV": "5508",
}


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def ensure_dirs() -> None:
    for path in [DATA_DIR, LATEST_DIR, DOCS_LATEST_DIR, HISTORY_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def normalize_name(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "").strip().upper())
    return text


def normalize_stock_id(value: Any) -> str:
    text = str(value or "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    m = re.search(r"(?<!\d)(\d{4})(?!\d)", text)
    return m.group(1) if m else ""


def parse_effective_date(text: str) -> str:
    m = re.search(r"close of ([A-Za-z]+ \d{1,2}, \d{4})", text)
    if not m:
        return ""
    dt = datetime.strptime(m.group(1), "%B %d, %Y")
    return dt.strftime("%Y%m%d")


def fetch_pdf_text(url: str) -> str:
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=45)
    resp.raise_for_status()
    if not resp.content.startswith(b"%PDF"):
        raise RuntimeError(f"not a PDF: {url}")
    reader = PdfReader(BytesIO(resp.content))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


def extract_taiwan_section(text: str) -> str:
    m = re.search(r"MSCI TAIWAN INDEX\n(.*?)(?:\nMSCI [A-Z ][A-Z ]+ INDEX|\nPage)", text, re.S)
    return m.group(1) if m else ""


def parse_two_column_section(section: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    started = False
    for raw_line in section.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if "Additions" in line and "Deletions" in line:
            started = True
            continue
        if not started:
            continue
        if line.strip() == "None":
            continue
        add = line[:40].strip()
        delete = line[40:].strip()
        # pypdf sometimes collapses spacing. Fall back to 2+ spaces split.
        if not delete:
            parts = re.split(r"\s{2,}", line.strip())
            if len(parts) >= 2:
                add, delete = parts[0].strip(), parts[1].strip()
            elif raw_line.startswith(" "):
                add, delete = "", line.strip()
        if add and add.upper() != "NONE":
            rows.append(("addition", normalize_name(add)))
        if delete and delete.upper() != "NONE":
            rows.append(("deletion", normalize_name(delete)))
    return rows


def build_events(review_codes: list[str]) -> pd.DataFrame:
    records: list[dict[str, Any]] = []
    for code in review_codes:
        for segment, template in MSCI_SOURCES.items():
            url = template.format(code=code)
            try:
                text = fetch_pdf_text(url)
                effective_date = parse_effective_date(text)
                section = extract_taiwan_section(text)
                events = parse_two_column_section(section)
            except Exception as exc:
                records.append(
                    {
                        "review_code": code,
                        "msci_index_segment": segment,
                        "effective_date": "",
                        "action": "",
                        "msci_company_name": "",
                        "stock_id": "",
                        "mapping_status": "source_fetch_failed",
                        "event_type": "msci_index_rebalance",
                        "source_url": url,
                        "error_message": str(exc),
                    }
                )
                continue
            for action, company_name in events:
                stock_id = normalize_stock_id(MSCI_TAIWAN_NAME_TO_ID.get(company_name, ""))
                records.append(
                    {
                        "review_code": code,
                        "msci_index_segment": segment,
                        "effective_date": effective_date,
                        "action": action,
                        "msci_company_name": company_name,
                        "stock_id": stock_id,
                        "mapping_status": "mapped" if stock_id else "unmatched_name",
                        "event_type": "msci_index_rebalance",
                        "source_url": url,
                        "error_message": "",
                    }
                )
    df = pd.DataFrame(records)
    if df.empty:
        return df
    df = df.drop_duplicates(
        subset=["review_code", "msci_index_segment", "effective_date", "action", "msci_company_name"],
        keep="first",
    )
    return df.sort_values(["effective_date", "msci_index_segment", "action", "msci_company_name"])


def read_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{stock_id}.csv"
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path, dtype={"date": str, "stock_id": str})
    if "date" not in df.columns and "trade_date" in df.columns:
        df = df.rename(columns={"trade_date": "date"})
    needed = ["date", "open", "close"]
    missing = [col for col in needed if col not in df.columns]
    if missing:
        return pd.DataFrame()
    for col in ["open", "close", "high", "low"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["date", "open", "close"]).sort_values("date").reset_index(drop=True)


def read_index_ohlc() -> pd.DataFrame:
    if not INDEX_OHLC.exists():
        return pd.DataFrame()
    df = pd.read_csv(INDEX_OHLC, dtype={"date": str, "index_code": str})
    for col in ["open", "close"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["date", "index_code", "open", "close"]).sort_values(["index_code", "date"])


def read_stock_meta() -> dict[str, dict[str, str]]:
    files = sorted((ROOT / "data" / "daily_price").glob("*.csv"), reverse=True)
    meta: dict[str, dict[str, str]] = {}
    for path in files[:20]:
        try:
            df = pd.read_csv(path, dtype={"stock_id": str})
        except Exception:
            continue
        if not {"stock_id", "stock_name", "market"}.issubset(df.columns):
            continue
        for _, row in df.iterrows():
            stock_id = str(row.get("stock_id", "") or "").strip()
            if not stock_id or stock_id in meta:
                continue
            meta[stock_id] = {
                "stock_name": str(row.get("stock_name", "") or "").strip(),
                "market": str(row.get("market", "") or "").strip(),
            }
        if len(meta) > 1500:
            break
    return meta


def pct_return(start: float, end: float) -> float | None:
    if pd.isna(start) or pd.isna(end) or start == 0:
        return None
    return round((end / start - 1) * 100, 4)


def benchmark_code(market: str) -> str:
    return "TPEX" if str(market).upper() == "TPEX" else "TWSE"


def benchmark_return(index_df: pd.DataFrame, code: str, entry_date: str, exit_date: str) -> float | None:
    if index_df.empty:
        return None
    sub = index_df[index_df["index_code"].eq(code)].reset_index(drop=True)
    if sub.empty:
        return None
    entry_rows = sub[sub["date"].eq(entry_date)]
    exit_rows = sub[sub["date"].eq(exit_date)]
    if entry_rows.empty or exit_rows.empty:
        return None
    return pct_return(float(entry_rows.iloc[0]["open"]), float(exit_rows.iloc[0]["close"]))


def backtest_events(events: pd.DataFrame) -> pd.DataFrame:
    index_df = read_index_ohlc()
    stock_meta = read_stock_meta()
    rows: list[dict[str, Any]] = []
    horizons = {"ret_d5": 5, "ret_d10": 10, "ret_d15": 15, "ret_d20": 20}
    for _, event in events.iterrows():
        stock_id = normalize_stock_id(event.get("stock_id", ""))
        effective_date = str(event.get("effective_date", "") or "").strip()
        if not stock_id or not effective_date:
            continue
        price = read_price(stock_id)
        if price.empty:
            rows.append({**event.to_dict(), "sample_status": "price_missing"})
            continue
        future = price[price["date"] > effective_date].reset_index(drop=True)
        if future.empty:
            rows.append({**event.to_dict(), "sample_status": "pending_no_next_trade"})
            continue
        entry = future.iloc[0]
        entry_dt = datetime.strptime(str(entry["date"]), "%Y%m%d")
        effective_dt = datetime.strptime(effective_date, "%Y%m%d")
        if (entry_dt - effective_dt).days > 10:
            rows.append(
                {
                    **event.to_dict(),
                    "entry_date": entry["date"],
                    "entry_open": entry["open"],
                    "sample_status": "price_history_starts_after_event",
                }
            )
            continue
        meta = stock_meta.get(stock_id, {})
        market = meta.get("market") or str(entry.get("market", ""))
        bmk = benchmark_code(market)
        out: dict[str, Any] = {
            **event.to_dict(),
            "stock_name": meta.get("stock_name") or entry.get("stock_name", ""),
            "market": market,
            "entry_date": entry["date"],
            "entry_open": entry["open"],
            "benchmark_code": bmk,
            "sample_status": "ok",
        }
        for prefix, horizon in horizons.items():
            idx = horizon - 1
            mature = len(future) > idx
            out[f"mature_{prefix}"] = bool(mature)
            if not mature:
                out[f"{prefix}_exit_date"] = ""
                out[f"{prefix}_close"] = None
                out[f"{prefix}_return"] = None
                out[f"{prefix}_benchmark_return"] = None
                out[f"{prefix}_relative_return"] = None
                continue
            exit_row = future.iloc[idx]
            stock_ret = pct_return(float(entry["open"]), float(exit_row["close"]))
            bmk_ret = benchmark_return(index_df, bmk, str(entry["date"]), str(exit_row["date"]))
            out[f"{prefix}_exit_date"] = exit_row["date"]
            out[f"{prefix}_close"] = exit_row["close"]
            out[f"{prefix}_return"] = stock_ret
            out[f"{prefix}_benchmark_return"] = bmk_ret
            out[f"{prefix}_relative_return"] = round(stock_ret - bmk_ret, 4) if stock_ret is not None and bmk_ret is not None else None
        rows.append(out)
    return pd.DataFrame(rows)


def summarize(backtest: pd.DataFrame) -> pd.DataFrame:
    if backtest.empty:
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    group_cols = ["msci_index_segment", "action"]
    horizons = ["ret_d5", "ret_d10", "ret_d15", "ret_d20"]
    for keys, group in backtest.groupby(group_cols, dropna=False):
        row: dict[str, Any] = {
            "msci_index_segment": keys[0],
            "action": keys[1],
            "sample_count": len(group),
            "ok_count": int(group["sample_status"].eq("ok").sum()) if "sample_status" in group else 0,
        }
        for prefix in horizons:
            mature_col = f"mature_{prefix}"
            ret_col = f"{prefix}_return"
            rel_col = f"{prefix}_relative_return"
            mature = group[group.get(mature_col, False).eq(True)] if mature_col in group else pd.DataFrame()
            returns = pd.to_numeric(mature.get(ret_col, pd.Series(dtype=float)), errors="coerce").dropna()
            rel = pd.to_numeric(mature.get(rel_col, pd.Series(dtype=float)), errors="coerce").dropna()
            row[f"{prefix}_mature_count"] = len(returns)
            row[f"{prefix}_win_rate"] = round((returns.gt(0).mean() * 100), 2) if len(returns) else None
            row[f"{prefix}_avg_return"] = round(returns.mean(), 2) if len(returns) else None
            row[f"{prefix}_median_return"] = round(returns.median(), 2) if len(returns) else None
            row[f"{prefix}_avg_relative_return"] = round(rel.mean(), 2) if len(rel) else None
        rows.append(row)
    return pd.DataFrame(rows)


def write_markdown(events: pd.DataFrame, backtest: pd.DataFrame, summary: pd.DataFrame) -> None:
    lines: list[str] = []
    lines.append("# MSCI Taiwan Rebalance Event Backtest")
    lines.append("")
    lines.append(f"- generated_at: {now_text()}")
    lines.append("- event_type: msci_index_rebalance")
    lines.append("- source: MSCI official Global Standard / Small Cap public list PDFs")
    lines.append("- entry rule: first trading day after MSCI effective date, entry at open")
    lines.append("- exit rule: D+5 / D+10 / D+15 / D+20 trading-day close; entry day is D+1")
    lines.append("- deletion return is not inverted; it is the stock's post-deletion long-side performance.")
    lines.append("- this is an event tag / research layer, not a buy or sell signal.")
    lines.append("")
    if events.empty:
        lines.append("No MSCI Taiwan events were parsed.")
    else:
        mapped = int(events["mapping_status"].eq("mapped").sum())
        unmatched = int(events["mapping_status"].eq("unmatched_name").sum())
        lines.append("## Data Quality")
        lines.append("")
        lines.append(f"- parsed_events: {len(events)}")
        lines.append(f"- mapped_events: {mapped}")
        lines.append(f"- unmatched_events: {unmatched}")
        lines.append(f"- backtested_rows: {len(backtest)}")
        lines.append("")
    if not summary.empty:
        lines.append("## Summary By MSCI Segment And Action")
        lines.append("")
        display_cols = [
            "msci_index_segment",
            "action",
            "sample_count",
            "ok_count",
            "ret_d5_mature_count",
            "ret_d5_win_rate",
            "ret_d5_avg_return",
            "ret_d10_mature_count",
            "ret_d10_win_rate",
            "ret_d10_avg_return",
            "ret_d20_mature_count",
            "ret_d20_win_rate",
            "ret_d20_avg_return",
        ]
        lines.append(summary[display_cols].to_markdown(index=False))
        lines.append("")
    if not backtest.empty:
        lines.append("## Recent Backtest Rows")
        lines.append("")
        cols = [
            "effective_date",
            "msci_index_segment",
            "action",
            "stock_id",
            "stock_name",
            "entry_date",
            "entry_open",
            "ret_d5_return",
            "ret_d10_return",
            "ret_d15_return",
            "ret_d20_return",
            "sample_status",
        ]
        recent = backtest.sort_values(["effective_date", "msci_index_segment", "action", "stock_id"], ascending=False).head(40)
        lines.append(recent[[c for c in cols if c in recent.columns]].to_markdown(index=False))
        lines.append("")
    BACKTEST_LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    DOCS_BACKTEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build MSCI Taiwan add/delete event backtest.")
    parser.add_argument("--review-codes", nargs="*", default=DEFAULT_REVIEW_CODES)
    args = parser.parse_args()
    ensure_dirs()
    events = build_events(args.review_codes)
    events.to_csv(EVENTS_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    events.to_csv(EVENTS_LATEST_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    backtest = backtest_events(events)
    backtest.to_csv(BACKTEST_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    backtest.to_csv(BACKTEST_LATEST_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    DOCS_BACKTEST_CSV.parent.mkdir(parents=True, exist_ok=True)
    backtest.to_csv(DOCS_BACKTEST_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    summary = summarize(backtest)
    write_markdown(events, backtest, summary)
    print(f"Saved {EVENTS_CSV} rows={len(events)}")
    print(f"Saved {BACKTEST_LATEST_CSV} rows={len(backtest)}")
    print(f"Saved {BACKTEST_LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
