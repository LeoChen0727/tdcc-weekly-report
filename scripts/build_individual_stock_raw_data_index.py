from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import re
import shutil

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

DATA_PRICE_DIR = Path("data/stock_price_history")
DATA_TDCC_DIR = Path("data/tdcc_stock_history")
DOCS_DATA_PRICE_DIR = Path("docs/data/stock_price_history")
DOCS_DATA_TDCC_DIR = Path("docs/data/tdcc_stock_history")
LATEST_DIR = Path("output/latest")
REPORT_DIR = LATEST_DIR / "individual_stock_reports"
DOCS_REPORT_DIR = Path("docs/latest/individual_stock_reports")
SELL_DIR = Path("output/history/sell_strategy_backtest")
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
DAILY_CANDIDATE_LOG = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")

AVAILABLE_INDEX_CSV = LATEST_DIR / "individual_stock_available_raw_data_index.csv"
AVAILABLE_INDEX_MD = LATEST_DIR / "individual_stock_available_raw_data_index.md"
AVAILABLE_INDEX_SLIM_CSV = LATEST_DIR / "individual_stock_available_raw_data_index_slim.csv"
AVAILABLE_INDEX_SLIM_MD = LATEST_DIR / "individual_stock_available_raw_data_index_slim.md"
READ_PROTOCOL_MD = LATEST_DIR / "individual_stock_read_protocol_latest.md"
REPORT_INDEX_CSV = LATEST_DIR / "individual_stock_reports_index.csv"
REPORT_INDEX_MD = LATEST_DIR / "individual_stock_reports_index.md"
DOCS_AVAILABLE_INDEX_CSV = Path("docs/latest/individual_stock_available_raw_data_index.csv")
DOCS_AVAILABLE_INDEX_MD = Path("docs/latest/individual_stock_available_raw_data_index.md")
DOCS_AVAILABLE_INDEX_SLIM_CSV = Path("docs/latest/individual_stock_available_raw_data_index_slim.csv")
DOCS_AVAILABLE_INDEX_SLIM_MD = Path("docs/latest/individual_stock_available_raw_data_index_slim.md")
DOCS_READ_PROTOCOL_MD = Path("docs/latest/individual_stock_read_protocol_latest.md")
DOCS_REPORT_INDEX_CSV = Path("docs/latest/individual_stock_reports_index.csv")
DOCS_REPORT_INDEX_MD = Path("docs/latest/individual_stock_reports_index.md")


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
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value).upper()
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Z]", "", text)
    if text.isdigit() and len(text) < 4:
        return text.zfill(4)
    return text


def normalize_date(value: Any) -> str:
    digits = re.sub(r"[^0-9]", "", safe_str(value))
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    if len(digits) == 7 and digits.startswith("1"):
        return f"{int(digits[:3]) + 1911:04d}{digits[3:]}"
    return ""


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5"]:
        try:
            return pd.read_csv(path, dtype=str, encoding=encoding).fillna("")
        except Exception:
            continue
    return pd.DataFrame()


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def github_api_url(path: Path) -> str:
    return f"https://api.github.com/repos/{OWNER_REPO}/contents/{path.as_posix()}?ref=main"


def pages_url_for(path: Path) -> str:
    text = path.as_posix()
    if text.startswith("docs/"):
        text = path.relative_to("docs").as_posix()
    elif text.startswith("output/latest/"):
        text = path.relative_to("output").as_posix()
    return f"{PAGES_PREFIX}/{text}"


def first_existing(df: pd.DataFrame, candidates: list[str]) -> str:
    for col in candidates:
        if col in df.columns:
            return col
    return ""


def code_mask(df: pd.DataFrame, code_col: str, stock_id: str) -> pd.Series:
    target = normalize_stock_id(stock_id)
    values = df[code_col].map(normalize_stock_id)
    alternatives = {target, target.lstrip("0")}
    if target.isdigit():
        alternatives.add(target.zfill(4))
        alternatives.add(target.zfill(6))
    return values.isin({x for x in alternatives if x})


def latest_date_from(df: pd.DataFrame, candidates: list[str]) -> str:
    for col in candidates:
        if col in df.columns:
            dates = [normalize_date(x) for x in df[col].tolist()]
            dates = [x for x in dates if x]
            if dates:
                return max(dates)
    return ""


def stock_name_from_df(df: pd.DataFrame) -> str:
    for col in ["stock_name", "name", "company_name"]:
        if col in df.columns:
            values = [safe_str(x) for x in df[col].tolist()]
            values = [x for x in values if x]
            if values:
                return values[-1]
    return ""


def collect_stock_ids() -> set[str]:
    stock_ids: set[str] = set()
    for folder in [DATA_PRICE_DIR, DATA_TDCC_DIR]:
        for path in folder.glob("*.csv"):
            stock_id = normalize_stock_id(path.stem)
            if stock_id:
                stock_ids.add(stock_id)
    for path in REPORT_DIR.glob("*_latest.md"):
        stock_id = normalize_stock_id(path.stem.replace("_latest", ""))
        if stock_id:
            stock_ids.add(stock_id)
    for path in SELL_DIR.glob("*_sell_strategy_summary.md"):
        stock_id = normalize_stock_id(path.stem.replace("_sell_strategy_summary", ""))
        if stock_id:
            stock_ids.add(stock_id)

    for path in [ALL_CANDIDATES_CSV, WARRANT_FLOW_CSV, DAILY_CANDIDATE_LOG]:
        df = read_csv(path)
        code_col = first_existing(df, ["stock_id", "code", "ticker"])
        if code_col:
            stock_ids.update(normalize_stock_id(x) for x in df[code_col].tolist() if normalize_stock_id(x))
    return stock_ids


def market_data_flags(stock_id: str, candidates: pd.DataFrame, warrants: pd.DataFrame, signals: pd.DataFrame) -> dict[str, Any]:
    flags = {
        "has_warrant_data": False,
        "has_revenue_data": False,
        "has_candidate_signal": False,
    }
    code_col = first_existing(warrants, ["stock_id", "code", "ticker"])
    if code_col:
        flags["has_warrant_data"] = bool(code_mask(warrants, code_col, stock_id).any())

    code_col = first_existing(candidates, ["stock_id", "code", "ticker"])
    if code_col:
        rows = candidates[code_mask(candidates, code_col, stock_id)]
        flags["has_candidate_signal"] = not rows.empty
        if not rows.empty:
            text = " ".join(rows.astype(str).agg(" ".join, axis=1).tolist()).lower()
            flags["has_revenue_data"] = any(token in text for token in ["revenue", "營收", "yoy", "mom"])

    code_col = first_existing(signals, ["stock_id", "code", "ticker"])
    if code_col and not signals.empty:
        flags["has_candidate_signal"] = flags["has_candidate_signal"] or bool(code_mask(signals, code_col, stock_id).any())
    return flags


def mirror_stock_raw_files(stock_id: str, has_individual_report: bool) -> tuple[str, str]:
    if not has_individual_report:
        return "", ""
    price_src = DATA_PRICE_DIR / f"{stock_id}.csv"
    tdcc_src = DATA_TDCC_DIR / f"{stock_id}.csv"
    price_dst = DOCS_DATA_PRICE_DIR / f"{stock_id}.csv"
    tdcc_dst = DOCS_DATA_TDCC_DIR / f"{stock_id}.csv"
    mirrored_price = ""
    mirrored_tdcc = ""
    if price_src.exists():
        price_dst.parent.mkdir(parents=True, exist_ok=True)
        copy_csv_standard(price_src, price_dst)
        mirrored_price = price_dst.as_posix()
    if tdcc_src.exists():
        tdcc_dst.parent.mkdir(parents=True, exist_ok=True)
        copy_csv_standard(tdcc_src, tdcc_dst)
        mirrored_tdcc = tdcc_dst.as_posix()
    return mirrored_price, mirrored_tdcc


def copy_csv_standard(src: Path, dst: Path) -> None:
    df = read_csv(src)
    if df.empty:
        shutil.copyfile(src, dst)
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(dst, index=False, encoding="utf-8", lineterminator="\n")


def build_indexes() -> tuple[pd.DataFrame, pd.DataFrame]:
    candidates = read_csv(ALL_CANDIDATES_CSV)
    warrants = read_csv(WARRANT_FLOW_CSV)
    signals = read_csv(DAILY_CANDIDATE_LOG)
    rows: list[dict[str, Any]] = []
    report_rows: list[dict[str, Any]] = []

    for stock_id in sorted(collect_stock_ids()):
        price_path = DATA_PRICE_DIR / f"{stock_id}.csv"
        tdcc_path = DATA_TDCC_DIR / f"{stock_id}.csv"
        latest_md = REPORT_DIR / f"{stock_id}_latest.md"
        latest_pdf = REPORT_DIR / f"{stock_id}_latest.pdf"
        latest_json = REPORT_DIR / f"{stock_id}_latest.json"
        sell_detail = SELL_DIR / f"{stock_id}_sell_strategy_backtest.csv"
        sell_summary = SELL_DIR / f"{stock_id}_sell_strategy_summary.md"

        price_df = read_csv(price_path)
        tdcc_df = read_csv(tdcc_path)
        stock_name = stock_name_from_df(price_df) or stock_name_from_df(tdcc_df)
        has_individual_md = latest_md.exists()
        docs_price_path, docs_tdcc_path = mirror_stock_raw_files(stock_id, has_individual_md)

        flags = market_data_flags(stock_id, candidates, warrants, signals)
        price_rows = int(len(price_df)) if not price_df.empty else 0
        tdcc_rows = int(len(tdcc_df)) if not tdcc_df.empty else 0
        notes: list[str] = []
        if price_rows < 60:
            notes.append("insufficient_price_history" if price_rows else "price_history_missing")
        if 0 < tdcc_rows < 8:
            notes.append("insufficient_tdcc_history")
        elif tdcc_rows == 0:
            notes.append("tdcc_history_missing")

        if price_rows >= 60:
            report_status = "standard_rawdata_report"
        elif price_rows > 0:
            report_status = "partial_rawdata_report"
        elif has_individual_md:
            report_status = "event_only_report"
        else:
            report_status = "insufficient_data"

        data_quality = "ok"
        if report_status != "standard_rawdata_report" or notes:
            data_quality = "partial" if price_rows else "insufficient_data"

        row = {
            "stock_id": stock_id,
            "stock_name": stock_name,
            "has_price_history": bool(price_rows),
            "price_history_rows": price_rows,
            "latest_price_date": latest_date_from(price_df, ["date", "trade_date"]),
            "price_history_raw_url": raw_url(price_path),
            "price_history_pages_url": pages_url_for(Path(docs_price_path)) if docs_price_path else "",
            "price_history_github_api_url": github_api_url(price_path),
            "has_tdcc_history": bool(tdcc_rows),
            "tdcc_history_rows": tdcc_rows,
            "latest_tdcc_date": latest_date_from(tdcc_df, ["as_of_date", "date", "signal_date"]),
            "tdcc_history_status": "ok" if tdcc_rows >= 8 else ("insufficient_tdcc_history" if tdcc_rows else "tdcc_history_missing"),
            "tdcc_history_raw_url": raw_url(tdcc_path),
            "tdcc_history_pages_url": pages_url_for(Path(docs_tdcc_path)) if docs_tdcc_path else "",
            "tdcc_history_github_api_url": github_api_url(tdcc_path),
            "has_individual_md": has_individual_md,
            "has_individual_pdf": latest_pdf.exists(),
            "has_individual_json": latest_json.exists(),
            "has_sell_strategy_backtest": sell_detail.exists(),
            "has_sell_strategy_summary": sell_summary.exists(),
            "has_warrant_data": flags["has_warrant_data"],
            "has_revenue_data": flags["has_revenue_data"],
            "has_candidate_signal": flags["has_candidate_signal"],
            "individual_md_raw_url": raw_url(latest_md),
            "individual_pdf_raw_url": raw_url(latest_pdf),
            "individual_md_pages_url": pages_url_for(Path("docs/latest/individual_stock_reports") / latest_md.name) if has_individual_md else "",
            "individual_md_github_api_url": github_api_url(latest_md),
            "individual_json_github_api_url": github_api_url(latest_json),
            "report_status": report_status,
            "data_quality_status": data_quality,
            "notes": "; ".join(notes),
            "updated_at": now_text(),
        }
        rows.append(row)
        if has_individual_md or latest_pdf.exists() or latest_json.exists():
            report_rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "has_md": has_individual_md,
                    "has_pdf": latest_pdf.exists(),
                    "has_json": latest_json.exists(),
                    "md_path": latest_md.as_posix(),
                    "pdf_path": latest_pdf.as_posix(),
                    "json_path": latest_json.as_posix(),
                    "md_raw_url": raw_url(latest_md),
                    "pdf_raw_url": raw_url(latest_pdf),
                    "md_pages_url": pages_url_for(Path("docs/latest/individual_stock_reports") / latest_md.name) if has_individual_md else "",
                    "md_github_api_url": github_api_url(latest_md),
                    "json_github_api_url": github_api_url(latest_json),
                    "report_status": report_status,
                    "updated_at": now_text(),
                }
            )

    index = pd.DataFrame(rows).sort_values(["stock_id"]).reset_index(drop=True)
    report_index = pd.DataFrame(report_rows).sort_values(["stock_id"]).reset_index(drop=True)
    slim_cols = [
        "stock_id",
        "stock_name",
        "price_history_rows",
        "latest_price_date",
        "tdcc_history_rows",
        "latest_tdcc_date",
        "tdcc_history_status",
        "has_individual_md",
        "has_individual_pdf",
        "has_sell_strategy_summary",
        "has_warrant_data",
        "has_revenue_data",
        "has_candidate_signal",
        "report_status",
        "data_quality_status",
        "notes",
        "updated_at",
    ]
    slim_index = index[[col for col in slim_cols if col in index.columns]].copy()
    write_csv(index, AVAILABLE_INDEX_CSV)
    write_csv(index, DOCS_AVAILABLE_INDEX_CSV)
    write_csv(slim_index, AVAILABLE_INDEX_SLIM_CSV)
    write_csv(slim_index, DOCS_AVAILABLE_INDEX_SLIM_CSV)
    write_csv(report_index, REPORT_INDEX_CSV)
    write_csv(report_index, DOCS_REPORT_INDEX_CSV)
    write_index_md(index, AVAILABLE_INDEX_MD)
    write_index_md(index, DOCS_AVAILABLE_INDEX_MD)
    write_slim_index_md(slim_index, AVAILABLE_INDEX_SLIM_MD)
    write_slim_index_md(slim_index, DOCS_AVAILABLE_INDEX_SLIM_MD)
    write_read_protocol_md(READ_PROTOCOL_MD)
    write_read_protocol_md(DOCS_READ_PROTOCOL_MD)
    write_report_index_md(report_index, REPORT_INDEX_MD)
    write_report_index_md(report_index, DOCS_REPORT_INDEX_MD)
    return index, report_index


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 120) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    use = df[[col for col in columns if col in df.columns]].head(limit).copy()
    cols = list(use.columns)
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join(["---"] * len(cols)) + " |",
    ]
    for _, row in use.iterrows():
        values = [safe_str(row.get(col)).replace("|", "/") for col in cols]
        lines.append("| " + " | ".join(values) + " |")
    if len(df) > limit:
        lines.append(f"\n_Only first {limit} rows shown. Use the CSV for the full index._")
    return lines


def write_index_md(index: pd.DataFrame, path: Path) -> None:
    status_counts = index["report_status"].value_counts().to_dict() if "report_status" in index.columns else {}
    tdcc_insufficient = int((index.get("tdcc_history_status", pd.Series(dtype=str)) == "insufficient_tdcc_history").sum())
    lines = [
        "# Individual Stock Available Raw Data Index",
        "",
        f"- generated_at: {now_text()}",
        f"- total_stocks: {len(index)}",
        f"- standard_rawdata_report: {status_counts.get('standard_rawdata_report', 0)}",
        f"- partial_rawdata_report: {status_counts.get('partial_rawdata_report', 0)}",
        f"- insufficient_data: {status_counts.get('insufficient_data', 0)}",
        f"- insufficient_tdcc_history: {tdcc_insufficient}",
        f"- csv_raw_url: {raw_url(AVAILABLE_INDEX_CSV)}",
        "",
        "## Columns",
        "",
        "- `report_status=standard_rawdata_report` means price raw data has at least 60 rows.",
        "- `insufficient_tdcc_history` means TDCC history has fewer than 8 weekly rows.",
        "- Missing individual Markdown does not mean missing raw data; use price/TDCC raw first.",
        "- If a `raw.githubusercontent.com/.../main/...` URL returns stale content, use the matching `*_github_api_url` and base64-decode the `content` field.",
        "",
        "## Preview",
        "",
    ]
    preview_cols = [
        "stock_id",
        "stock_name",
        "price_history_rows",
        "tdcc_history_rows",
        "latest_price_date",
        "latest_tdcc_date",
        "has_individual_md",
        "has_sell_strategy_summary",
        "report_status",
        "notes",
    ]
    lines.extend(markdown_table(index, preview_cols, limit=200))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report_index_md(report_index: pd.DataFrame, path: Path) -> None:
    lines = [
        "# Individual Stock Reports Index",
        "",
        f"- generated_at: {now_text()}",
        f"- report_count: {len(report_index)}",
        f"- csv_raw_url: {raw_url(REPORT_INDEX_CSV)}",
        "",
    ]
    lines.extend(
        markdown_table(
            report_index,
            ["stock_id", "stock_name", "has_md", "has_pdf", "has_json", "report_status", "md_raw_url", "md_github_api_url"],
            limit=200,
        )
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_slim_index_md(index: pd.DataFrame, path: Path) -> None:
    status_counts = index["report_status"].value_counts().to_dict() if "report_status" in index.columns else {}
    lines = [
        "# Individual Stock Raw Data Index Slim",
        "",
        f"- generated_at: {now_text()}",
        f"- total_stocks: {len(index)}",
        f"- standard_rawdata_report: {status_counts.get('standard_rawdata_report', 0)}",
        f"- partial_rawdata_report: {status_counts.get('partial_rawdata_report', 0)}",
        f"- insufficient_data: {status_counts.get('insufficient_data', 0)}",
        f"- csv_raw_url: {raw_url(AVAILABLE_INDEX_SLIM_CSV)}",
        f"- csv_pages_url: {pages_url_for(Path('docs/latest/individual_stock_available_raw_data_index_slim.csv'))}",
        f"- csv_github_api_url: {github_api_url(AVAILABLE_INDEX_SLIM_CSV)}",
        "",
        "## Usage",
        "",
        "- Use this slim index first to check whether a stock has price history, TDCC history, and individual reports.",
        "- Use READ_ME_FIRST URL templates to fetch the exact stock raw CSV or GitHub API contents endpoint.",
        "- If full index is too large for GitHub API content decoding, this slim index is the ChatGPT-safe fallback.",
        "",
        "## Preview",
        "",
    ]
    preview_cols = [
        "stock_id",
        "stock_name",
        "price_history_rows",
        "latest_price_date",
        "tdcc_history_rows",
        "latest_tdcc_date",
        "tdcc_history_status",
        "has_individual_md",
        "report_status",
        "notes",
    ]
    lines.extend(markdown_table(index, preview_cols, limit=220))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_read_protocol_md(path: Path) -> None:
    lines = [
        "# Individual Stock Raw Data Read Protocol",
        "",
        f"- generated_at: {now_text()}",
        "- scope: every Taiwan stock id with repo raw data",
        "- individual_report_md_is_optional: True",
        "- individual_stock_chatgpt_packet_is_primary_read_entry: True",
        "- price_and_tdcc_raw_are_primary_source_tables: True",
        "",
        "## Core Rule",
        "",
        "For any `stock_id`, use the same fixed packet-first, raw-data-backed flow. Do not require `output/latest/individual_stock_reports/{stock_id}_latest.md` to exist before analysis.",
        "",
        "## Universal URL Templates",
        "",
        "| logical_source | first_url | fallback_url | final_fallback |",
        "| --- | --- | --- | --- |",
        "| individual_chatgpt_packet | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` | GitHub API contents + base64 decode |",
        "| price_window_180_html | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html` | GitHub API contents + base64 decode |",
        "| price_window_180_txt | `https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt` | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt` | GitHub API contents + base64 decode |",
        "| price_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |",
        "| tdcc_history | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/{stock_id}.csv` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/{stock_id}.csv?ref=main` | decode GitHub API JSON `content` from base64 |",
        "| individual_report_md_optional | `https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/{stock_id}_latest.md` | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.md?ref=main` | if missing, continue with raw price / TDCC |",
        "| individual_report_json_optional | `https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.json?ref=main` | none | optional convenience only |",
        "",
        "## Recommended Fixed Flow",
        "",
        "1. Normalize stock id to four digits when applicable.",
        "2. Read the individual ChatGPT packet first. It gives stable URLs, latest snapshot, recent TDCC rows, candidate context, repeat appearance, and warrant context.",
        "3. For any K-line, 23EMA, volume, support/resistance, or pattern conclusion, always read `price_window_180_html` first. The 20-row packet preview is not enough for technical analysis.",
        "   Main chart/conclusion rule: use 23EMA as the primary moving-average observation line. MA20 / MA60 / MA120 are backend auxiliary/backtest fields unless the user explicitly asks for them.",
        "4. For the main individual-stock report K-line chart, draw only the latest half-year trading window by default: `126` trading days. Keep the 180-day window for analysis context, not for the main chart length.",
        "5. If packet/raw/pages returns Cache miss, Internal Error, stale content, or `Total lines: 1`, read the matching GitHub API URL and base64-decode `content`.",
        "6. Use full price / TDCC raw CSV only for programmatic backtests or extra columns. Do not require ChatGPT to expand full raw CSV before ordinary single-stock analysis.",
        "7. If raw price history returns Cache miss, Internal Error, stale content, or `Total lines: 1` while the file is expected to be multi-line, use the `price_window_180_html` or GitHub API fallback before downgrading the report.",
        "8. If price rows >= 60, the stock can be analyzed as `standard_rawdata_report` even when the individual Markdown/PDF report does not exist.",
        "9. Read TDCC history from the packet first, then TDCC raw/API fallback if needed.",
        "10. If TDCC rows < 8 weekly rows, mark `insufficient_tdcc_history`; do not make 8-12 week TDCC backtest conclusions.",
        "11. Read individual report Markdown only as an optional prepared report. If it is missing, continue with packet/raw data.",
        "12. External websites may supplement news, announcements, broker targets, or events, but must not replace repo price history or repo TDCC history as primary data.",
        "",
        "## Status Definitions",
        "",
        "| status | meaning |",
        "| --- | --- |",
        "| standard_rawdata_report | price raw data exists and has at least 60 rows |",
        "| partial_rawdata_report | price raw data exists but is short, or supporting raw data is limited |",
        "| insufficient_tdcc_history | TDCC history exists but has fewer than 8 weekly rows |",
        "| individual_md_missing | prepared Markdown report is missing, but raw data may still support analysis |",
        "| raw_fetch_failed | raw URL failed; try GitHub API contents fallback |",
        "| content_not_expanded | URL opened but content did not expand into a usable table |",
        "",
        "## ChatGPT Instruction",
        "",
        "If a prepared individual report is missing, do not say the repo lacks data. Read `individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` first. If packet/raw URLs fail, use GitHub API contents and base64 decode. Only after packet and price raw/API both fail should the report be downgraded to event-only or insufficient-data.",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    index, report_index = build_indexes()
    print(f"Saved: {AVAILABLE_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {AVAILABLE_INDEX_MD}")
    print(f"Saved: {REPORT_INDEX_CSV} rows={len(report_index)}")
    print(f"Saved: {REPORT_INDEX_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
