from __future__ import annotations

import argparse
import math
import re
import time
from io import StringIO
from pathlib import Path
from typing import Any

import pandas as pd
import requests

from tracking_utils import LATEST_DIR, normalize_code, normalize_date, now_text, read_csv, safe_str, to_number, write_csv


TDCC_QUERY_URL = "https://www.tdcc.com.tw/portal/zh/smWeb/qryStock"
TDCC_HISTORY_DIR = Path("output/history/tdcc")
TDCC_STOCK_RAW_DIR = Path("data/tdcc_stock_history_raw")
MANIFEST_CSV = LATEST_DIR / "tdcc_history_backfill_manifest_latest.csv"
MANIFEST_MD = LATEST_DIR / "tdcc_history_backfill_manifest_latest.md"

SUMMARY_COLUMNS = ["date", "code", "name", "over_400_pct", "over_600_pct", "over_800_pct", "over_1000_pct"]
THRESHOLD_LEVEL_START = {
    400: 11,
    600: 12,
    800: 13,
    1000: 14,
}


def fetch_query_form(session: requests.Session) -> tuple[str, str, str, list[str]]:
    response = session.get(TDCC_QUERY_URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    response.raise_for_status()
    html = response.text
    token = extract_required(html, r'name="SYNCHRONIZER_TOKEN" value="([^"]+)"', "SYNCHRONIZER_TOKEN")
    uri = extract_required(html, r'name="SYNCHRONIZER_URI" value="([^"]+)"', "SYNCHRONIZER_URI")
    fir_date = extract_required(html, r'name="firDate" value="([^"]+)"', "firDate")
    dates = sorted(set(re.findall(r'<option value="(20[0-9]{6})"', html)), reverse=True)
    return token, uri, fir_date, dates


def extract_required(text: str, pattern: str, name: str) -> str:
    match = re.search(pattern, text)
    if not match:
        raise RuntimeError(f"Failed to find TDCC form field: {name}")
    return match.group(1)


def load_name_map() -> dict[str, str]:
    result: dict[str, str] = {}
    sources = [
        ("output/latest/tdcc_holder_ratio_latest.csv", "code", "name"),
        ("output/latest/tdcc_stock_history_manifest.csv", "stock_id", "stock_name"),
        ("output/latest/all_candidates_latest.csv", "stock_id", "stock_name"),
        ("config/stock_theme_map.csv", "code", "name"),
    ]
    for path, code_col, name_col in sources:
        df = read_csv(path, dtype=str)
        if df.empty or code_col not in df.columns or name_col not in df.columns:
            continue
        for _, row in df.iterrows():
            code = normalize_code(row.get(code_col, ""))
            name = safe_str(row.get(name_col, ""))
            if code and name and code not in result:
                result[code] = name
    return result


def load_universe(name_map: dict[str, str], universe: str, max_stocks: int | None, explicit_ids: list[str]) -> list[str]:
    selected: list[str] = []
    selected.extend(normalize_code(item) for item in explicit_ids)

    if universe in {"chatgpt-top", "top"}:
        selected.extend(load_codes_from_csv("output/latest/tdcc_pre_move_abm_top_latest.csv", "stock_id"))
        selected.extend(load_codes_from_csv("output/latest/tdcc_strength_ranking_top_latest.csv", "stock_id"))
        selected.extend(load_codes_from_csv("output/latest/tdcc_pre_move_accumulation_latest.csv", "code", sort_col="abm_rank"))
    elif universe == "candidates":
        selected.extend(load_codes_from_csv("output/latest/all_candidates_latest.csv", "stock_id"))
    elif universe == "signals":
        selected.extend(load_codes_from_csv("output/history/tdcc_signals/tdcc_normalized_signal_log.csv", "code"))
    elif universe == "all-known":
        selected.extend(name_map.keys())
    elif universe == "explicit":
        pass
    else:
        raise ValueError(f"Unknown universe: {universe}")

    unique: list[str] = []
    seen: set[str] = set()
    for code in selected:
        code = normalize_code(code)
        if not code or code in seen:
            continue
        seen.add(code)
        unique.append(code)
    if max_stocks is not None and max_stocks > 0:
        unique = unique[:max_stocks]
    return unique


def load_codes_from_csv(path: str, code_col: str, sort_col: str | None = None) -> list[str]:
    df = read_csv(path, dtype=str)
    if df.empty or code_col not in df.columns:
        return []
    if sort_col and sort_col in df.columns:
        temp = df.copy()
        temp["_sort"] = pd.to_numeric(temp[sort_col], errors="coerce")
        df = temp.sort_values("_sort", na_position="last")
    return [normalize_code(value) for value in df[code_col].tolist()]


def choose_dates(available_dates: list[str], weeks: int, start_date: str | None, end_date: str | None, explicit_dates: list[str]) -> list[str]:
    if explicit_dates:
        wanted = {normalize_date(item) for item in explicit_dates}
        return [date for date in available_dates if date in wanted]
    dates = available_dates
    if start_date:
        start = normalize_date(start_date)
        dates = [date for date in dates if date >= start]
    if end_date:
        end = normalize_date(end_date)
        dates = [date for date in dates if date <= end]
    return dates[:weeks]


def fetch_stock_distribution(session: requests.Session, stock_id: str, date: str) -> pd.DataFrame:
    token, uri, fir_date, _ = fetch_query_form(session)
    payload = {
        "SYNCHRONIZER_TOKEN": token,
        "SYNCHRONIZER_URI": uri,
        "method": "submit",
        "firDate": fir_date,
        "scaDate": date,
        "sqlMethod": "StockNo",
        "stockNo": stock_id,
        "stockName": "",
    }
    response = session.post(
        TDCC_QUERY_URL,
        data=payload,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30,
    )
    response.raise_for_status()
    tables = pd.read_html(StringIO(response.text))
    for table in reversed(tables):
        if table.shape[0] >= 15 and table.shape[1] >= 5:
            result = table.copy()
            result.columns = [safe_str(col) for col in result.columns]
            return result
    return pd.DataFrame()


def summarize_distribution(table: pd.DataFrame, date: str, stock_id: str, stock_name: str) -> dict[str, Any]:
    pct = pd.to_numeric(table.iloc[:, -1], errors="coerce")
    result: dict[str, Any] = {
        "date": date,
        "code": stock_id,
        "name": stock_name,
    }
    for threshold, start_idx in THRESHOLD_LEVEL_START.items():
        result[f"over_{threshold}_pct"] = round(float(pct.iloc[start_idx:15].sum()), 2)
    return result


def read_existing_summary(date: str) -> pd.DataFrame:
    path = TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{date}.csv"
    df = read_csv(path, dtype=str)
    if df.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    for col in SUMMARY_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df["date"] = df["date"].map(normalize_date)
    df["code"] = df["code"].map(normalize_code)
    return df[SUMMARY_COLUMNS]


def write_summary_row(row: dict[str, Any]) -> None:
    date = normalize_date(row.get("date", ""))
    path = TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{date}.csv"
    df = read_existing_summary(date)
    new_row = pd.DataFrame([row], columns=SUMMARY_COLUMNS)
    out = new_row if df.empty else pd.concat([df, new_row], ignore_index=True, sort=False)
    out["date"] = out["date"].map(normalize_date)
    out["code"] = out["code"].map(normalize_code)
    out = out.drop_duplicates(["date", "code"], keep="last").sort_values("code").reset_index(drop=True)
    write_csv(out, path)


def raw_history_path(stock_id: str) -> Path:
    return TDCC_STOCK_RAW_DIR / f"{stock_id}.csv"


def write_raw_stock_rows(stock_id: str, date: str, table: pd.DataFrame) -> None:
    raw = table.copy()
    raw.insert(0, "as_of_date", date)
    raw.insert(1, "stock_id", stock_id)
    path = raw_history_path(stock_id)
    old = read_csv(path, dtype=str)
    out = pd.concat([old, raw], ignore_index=True, sort=False) if not old.empty else raw
    subset = ["as_of_date", "stock_id"]
    if out.shape[1] > 3:
        subset.append(out.columns[2])
    out["as_of_date"] = out["as_of_date"].map(normalize_date)
    out["stock_id"] = out["stock_id"].map(normalize_code)
    out = out.drop_duplicates(subset, keep="last").sort_values(["stock_id", "as_of_date"]).reset_index(drop=True)
    write_csv(out, path)


def stock_date_already_present(stock_id: str, date: str) -> bool:
    df = read_existing_summary(date)
    if df.empty:
        return False
    return bool(df["code"].map(normalize_code).eq(stock_id).any())


def build_manifest(rows: list[dict[str, Any]], args: argparse.Namespace, selected_dates: list[str], stock_ids: list[str]) -> None:
    manifest = pd.DataFrame(rows)
    if manifest.empty:
        manifest = pd.DataFrame(
            [
                {
                    "generated_at": now_text(),
                    "status": "no_rows",
                    "message": "No TDCC history rows were fetched.",
                }
            ]
        )
    write_csv(manifest, MANIFEST_CSV)
    ok_count = int((manifest.get("status", pd.Series(dtype=str)) == "ok").sum()) if "status" in manifest.columns else 0
    skip_count = int((manifest.get("status", pd.Series(dtype=str)) == "skipped_existing").sum()) if "status" in manifest.columns else 0
    fail_count = len(manifest) - ok_count - skip_count if not manifest.empty else 0
    lines = [
        "# TDCC History Backfill Manifest",
        "",
        f"- generated_at: {now_text()}",
        f"- universe: {args.universe}",
        f"- stocks_selected: {len(stock_ids)}",
        f"- dates_selected: {len(selected_dates)}",
        f"- date_range: {selected_dates[-1] if selected_dates else ''} ~ {selected_dates[0] if selected_dates else ''}",
        f"- fetched_ok: {ok_count}",
        f"- skipped_existing: {skip_count}",
        f"- failed_or_empty: {fail_count}",
        f"- dry_run: {args.dry_run}",
        "",
        "## Notes",
        "",
        "- TDCC OpenData only exposes latest all-market data. Historical backfill uses the official TDCC query page by stock id and weekly date.",
        "- This script intentionally defaults to a bounded stock universe to avoid thousands of repeated requests against the official site.",
        "- Re-run `python scripts/build_tdcc_stock_history.py` after backfill to rebuild `data/tdcc_stock_history/{stock_id}.csv`.",
        "",
    ]
    if not manifest.empty and {"date", "stock_id", "status"}.issubset(manifest.columns):
        preview = manifest.tail(30).to_markdown(index=False)
        lines.extend(["## Latest Rows", "", preview, ""])
    MANIFEST_MD.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_MD.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill TDCC weekly holder distribution history by stock id.")
    parser.add_argument("--weeks", type=int, default=26, help="Number of latest TDCC weekly dates to fetch. Default: 26.")
    parser.add_argument("--start-date", default=None, help="Optional inclusive YYYYMMDD start date.")
    parser.add_argument("--end-date", default=None, help="Optional inclusive YYYYMMDD end date.")
    parser.add_argument("--date", action="append", default=[], help="Specific TDCC date to fetch. Can be repeated.")
    parser.add_argument("--stock-id", action="append", default=[], help="Specific stock id to include. Can be repeated.")
    parser.add_argument(
        "--universe",
        default="chatgpt-top",
        choices=["chatgpt-top", "top", "candidates", "signals", "all-known", "explicit"],
        help="Stock universe to backfill. Default: chatgpt-top.",
    )
    parser.add_argument("--max-stocks", type=int, default=80, help="Limit number of stocks. Use 0 for no limit.")
    parser.add_argument("--max-requests", type=int, default=0, help="Hard request cap. Use 0 for no cap.")
    parser.add_argument("--sleep", type=float, default=0.15, help="Seconds to sleep between successful requests.")
    parser.add_argument("--force", action="store_true", help="Fetch even if date+stock already exists.")
    parser.add_argument("--dry-run", action="store_true", help="Print selected dates/stocks without fetching.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    max_stocks = None if args.max_stocks == 0 else args.max_stocks
    session = requests.Session()
    _, _, _, available_dates = fetch_query_form(session)
    selected_dates = choose_dates(available_dates, args.weeks, args.start_date, args.end_date, args.date)
    name_map = load_name_map()
    stock_ids = load_universe(name_map, args.universe, max_stocks, args.stock_id)
    print(f"Selected dates: {len(selected_dates)}")
    print(f"Selected stocks: {len(stock_ids)}")
    if selected_dates:
        print(f"Date range: {selected_dates[-1]} ~ {selected_dates[0]}")
    if stock_ids:
        print("Stock preview:", ", ".join(stock_ids[:20]))

    if args.dry_run:
        build_manifest([], args, selected_dates, stock_ids)
        return 0

    manifest_rows: list[dict[str, Any]] = []
    request_count = 0
    for date in selected_dates:
        for stock_id in stock_ids:
            if args.max_requests and request_count >= args.max_requests:
                print(f"Reached max requests: {args.max_requests}")
                build_manifest(manifest_rows, args, selected_dates, stock_ids)
                return 0
            if not args.force and stock_date_already_present(stock_id, date):
                manifest_rows.append(
                    {
                        "generated_at": now_text(),
                        "date": date,
                        "stock_id": stock_id,
                        "stock_name": name_map.get(stock_id, ""),
                        "status": "skipped_existing",
                        "message": "",
                    }
                )
                continue
            request_count += 1
            try:
                table = fetch_stock_distribution(session, stock_id, date)
                if table.empty:
                    raise RuntimeError("empty distribution table")
                stock_name = name_map.get(stock_id, "")
                summary = summarize_distribution(table, date, stock_id, stock_name)
                if any(math.isnan(to_number(summary.get(f"over_{threshold}_pct"))) for threshold in THRESHOLD_LEVEL_START):
                    raise RuntimeError("invalid threshold summary")
                write_summary_row(summary)
                write_raw_stock_rows(stock_id, date, table)
                manifest_rows.append(
                    {
                        "generated_at": now_text(),
                        "date": date,
                        "stock_id": stock_id,
                        "stock_name": stock_name,
                        "status": "ok",
                        "message": "",
                    }
                )
                print(f"OK {date} {stock_id}")
                if args.sleep > 0:
                    time.sleep(args.sleep)
            except Exception as exc:
                manifest_rows.append(
                    {
                        "generated_at": now_text(),
                        "date": date,
                        "stock_id": stock_id,
                        "stock_name": name_map.get(stock_id, ""),
                        "status": "failed",
                        "message": str(exc),
                    }
                )
                print(f"WARNING {date} {stock_id}: {exc}")
    build_manifest(manifest_rows, args, selected_dates, stock_ids)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
