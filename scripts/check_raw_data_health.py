from __future__ import annotations

from argparse import ArgumentParser
from base64 import b64decode
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from hashlib import sha256
from io import StringIO
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo
import json
import os
import re

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"
API_PREFIX = f"https://api.github.com/repos/{OWNER_REPO}/contents"
BLOB_PREFIX = f"https://github.com/{OWNER_REPO}/blob/main"

LATEST_DIR = Path("output/latest")
FETCH_STATUS_CSV = LATEST_DIR / "raw_data_fetch_status_latest.csv"
FETCH_STATUS_MD = LATEST_DIR / "raw_data_fetch_status_latest.md"
DOCS_FETCH_STATUS_CSV = Path("docs/latest/raw_data_fetch_status_latest.csv")
DOCS_FETCH_STATUS_MD = Path("docs/latest/raw_data_fetch_status_latest.md")

DATE_COLUMNS = [
    "date",
    "trade_date",
    "signal_date",
    "report_date",
    "as_of_date",
    "event_date",
    "main_price_date",
]


CORE_PATHS = [
    ("readme_first", Path("output/latest/READ_ME_FIRST_DAILY_REPORT.txt")),
    ("daily_report_packet", Path("output/latest/chatgpt_daily_report_packet_latest.txt")),
    ("daily_market_summary", Path("output/latest/daily_market_summary_latest.md")),
    ("daily_market_full", Path("output/latest/daily_market_full_latest.md")),
    ("stock_monitor", Path("output/latest/stock_monitor_latest.md")),
    ("all_candidates", Path("output/latest/all_candidates_latest.csv")),
    ("candidate_repeat_appearance", Path("output/latest/candidate_repeat_appearance_latest.csv")),
    ("warrant_market_report", Path("output/latest/warrant_market_report_latest.md")),
    ("warrant_flow_by_stock", Path("output/latest/warrant_flow_by_stock_latest.csv")),
    ("tdcc_tracking_packet", Path("output/latest/tdcc_chatgpt_tracking_packet_latest.md")),
    ("tdcc_strength_ranking_top", Path("output/latest/tdcc_strength_ranking_top_latest.csv")),
    ("tdcc_pre_move_abm_top", Path("output/latest/tdcc_pre_move_abm_top_latest.csv")),
    ("tdcc_phase_distribution", Path("output/latest/tdcc_phase_distribution_latest.csv")),
    ("tdcc_top_risk_list", Path("output/latest/tdcc_top_risk_list_latest.csv")),
    ("surge_model_packet", Path("output/latest/surge_model_chatgpt_packet_latest.md")),
    ("surge_precondition_candidates", Path("output/latest/surge_precondition_candidates_latest.csv")),
    ("surge_model_backtest", Path("output/latest/surge_model_backtest_latest.csv")),
    ("surge_model_feature_importance", Path("output/latest/surge_model_feature_importance_latest.csv")),
    ("daily_signal_performance_summary", Path("output/latest/daily_signal_performance_summary_latest.md")),
    ("individual_stock_available_raw_data_index", Path("output/latest/individual_stock_available_raw_data_index.csv")),
    ("individual_stock_available_raw_data_index_slim", Path("output/latest/individual_stock_available_raw_data_index_slim.csv")),
    ("individual_stock_reports_index", Path("output/latest/individual_stock_reports_index.csv")),
    ("individual_stock_chatgpt_packet_index", Path("output/latest/individual_stock_chatgpt_packet_index.csv")),
    ("individual_stock_chatgpt_packet_index_md", Path("output/latest/individual_stock_chatgpt_packet_index.md")),
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


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    text = path.as_posix()
    if text.startswith("docs/"):
        text = path.relative_to("docs").as_posix()
    elif text.startswith("output/latest/"):
        text = path.relative_to("output").as_posix()
    return f"{PAGES_PREFIX}/{text}"


def api_url(path: Path) -> str:
    return f"{API_PREFIX}/{path.as_posix()}?ref=main"


def blob_url(path: Path) -> str:
    return f"{BLOB_PREFIX}/{path.as_posix()}"


def fetch_text(url: str, *, expect_api: bool = False, timeout: int = 20) -> dict[str, Any]:
    headers = {"User-Agent": "tdcc-weekly-report-health-check"}
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/vnd.github+json"
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    request = Request(url, headers=headers)
    try:
        with urlopen(request, timeout=timeout) as response:
            status = int(getattr(response, "status", 0) or 0)
            raw = response.read()
            if expect_api:
                body = raw.decode("utf-8", errors="replace")
                try:
                    payload = json.loads(body)
                    content = payload.get("content", "")
                    encoding = payload.get("encoding", "")
                    if encoding == "base64" and content:
                        decoded = b64decode(content).decode("utf-8-sig", errors="replace")
                        return {"ok": True, "http_status": status, "text": decoded, "error": ""}
                    return {"ok": False, "http_status": status, "text": "", "error": "api_decode_failed"}
                except Exception as exc:
                    return {"ok": False, "http_status": status, "text": "", "error": f"api_decode_failed: {exc}"}
            text = raw.decode("utf-8-sig", errors="replace")
            return {"ok": 200 <= status < 300, "http_status": status, "text": text, "error": ""}
    except HTTPError as exc:
        try:
            error_text = exc.read().decode("utf-8", errors="replace")
        except Exception:
            error_text = str(exc)
        return {"ok": False, "http_status": int(exc.code), "text": "", "error": error_text[:300]}
    except URLError as exc:
        return {"ok": False, "http_status": "", "text": "", "error": str(exc.reason)}
    except Exception as exc:
        return {"ok": False, "http_status": "", "text": "", "error": str(exc)}


def local_text(path: Path) -> str:
    if not path.exists() or path.is_dir():
        return ""
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")
    except Exception:
        try:
            return path.read_text(encoding="cp950", errors="replace")
        except Exception:
            return ""


def file_size(path: Path) -> int:
    try:
        return int(path.stat().st_size)
    except Exception:
        return 0


def parse_table_stats(text: str, suffix: str) -> dict[str, Any]:
    lines = text.splitlines()
    line_count = len(lines)
    rows = 0
    columns = 0
    latest_date = ""
    empty_table = False
    if suffix.lower() == ".csv" and text.strip():
        try:
            df = pd.read_csv(StringIO(text), dtype=str).fillna("")
            rows = int(len(df))
            columns = int(len(df.columns))
            empty_table = rows == 0
            for col in DATE_COLUMNS:
                if col in df.columns:
                    dates = [normalize_date(x) for x in df[col].tolist()]
                    dates = [x for x in dates if x]
                    if dates:
                        latest_date = max(dates)
                        break
        except Exception:
            rows = 0
            columns = 0
            empty_table = True
    elif suffix.lower() in {".md", ".txt"}:
        rows = line_count
        columns = 1 if text.strip() else 0
    return {
        "line_count": line_count,
        "rows": rows,
        "columns": columns,
        "latest_date": latest_date,
        "empty_table": empty_table,
    }


def classify_status(
    *,
    source_type: str,
    ok: bool,
    http_status: Any,
    error: str,
    text: str,
    path: Path,
    local_line_count: int,
    blob_exists: bool,
) -> str:
    lowered = error.lower()
    if ok and text:
        stats = parse_table_stats(text, path.suffix)
        if path.suffix.lower() in {".csv", ".md", ".txt"} and stats["line_count"] <= 1 and local_line_count > 1:
            return "suspicious_single_line"
        if path.suffix.lower() == ".csv" and stats["columns"] <= 1 and local_line_count > 1:
            return "content_not_expanded"
        return "success"
    if source_type == "api" and "api_decode_failed" in lowered:
        return "api_decode_failed"
    if "rate limit" in lowered:
        if source_type == "api":
            return "api_fetch_failed"
        if source_type == "raw":
            return "raw_fetch_failed"
        if source_type == "pages":
            return "pages_fetch_failed"
    if "cache miss" in lowered:
        return "cache_miss"
    if "internal error" in lowered:
        return "internal_fetch_error"
    if str(http_status) == "404":
        return "missing_file"
    if blob_exists and source_type != "blob":
        return "file_exists_but_content_unreadable"
    if source_type == "raw":
        return "raw_fetch_failed"
    if source_type == "pages":
        return "pages_fetch_failed"
    if source_type == "api":
        return "api_fetch_failed"
    return "missing_file" if str(http_status) == "404" else "content_not_expanded"


def check_one(logical_source: str, path: Path, stock_id: str = "", source_types: list[str] | None = None) -> list[dict[str, Any]]:
    local = local_text(path)
    local_stats = parse_table_stats(local, path.suffix)
    local_line_count = int(local_stats["line_count"])
    local_exists = path.exists()
    checked_at = now_text()

    all_sources = [
        ("raw", raw_url(path), False),
        ("pages", pages_url(path), False),
        ("api", api_url(path), True),
        ("blob", blob_url(path), False),
    ]
    wanted = set(source_types or ["raw", "pages", "api", "blob"])
    sources = [source for source in all_sources if source[0] in wanted]
    if not sources:
        sources = [all_sources[0]]

    blob = fetch_text(blob_url(path), timeout=15) if "blob" in wanted else {"ok": local_exists, "http_status": "", "text": "", "error": ""}
    blob_exists = bool(blob.get("ok")) or local_exists
    rows: list[dict[str, Any]] = []
    for source_type, url, is_api in sources:
        fetched = blob if source_type == "blob" else fetch_text(url, expect_api=is_api, timeout=20)
        text = safe_str(fetched.get("text", ""))
        ok = bool(fetched.get("ok")) and bool(text or source_type == "blob")
        status = classify_status(
            source_type=source_type,
            ok=ok,
            http_status=fetched.get("http_status", ""),
            error=safe_str(fetched.get("error", "")),
            text=text,
            path=path,
            local_line_count=local_line_count,
            blob_exists=blob_exists,
        )
        stats = parse_table_stats(text, path.suffix)
        if source_type == "blob" and ok:
            stats = {
                "line_count": "",
                "rows": "",
                "columns": "",
                "latest_date": "",
                "empty_table": "",
            }
        rows.append(
            {
                "logical_source": logical_source,
                "stock_id": stock_id,
                "expected_path": path.as_posix(),
                "url": url,
                "source_type": source_type,
                "success": status == "success" or (source_type == "blob" and blob_exists),
                "status_category": status,
                "http_status": fetched.get("http_status", ""),
                "error_message": safe_str(fetched.get("error", ""))[:300],
                "rows": stats.get("rows", ""),
                "columns": stats.get("columns", ""),
                "line_count": stats.get("line_count", ""),
                "local_file_exists": local_exists,
                "local_line_count": local_line_count,
                "local_rows": local_stats.get("rows", ""),
                "local_columns": local_stats.get("columns", ""),
                "file_size": file_size(path),
                "latest_date": stats.get("latest_date", "") or local_stats.get("latest_date", ""),
                "empty_table": stats.get("empty_table", ""),
                "newline_ok": bool(local_line_count != 1 or file_size(path) < 512),
                "chatgpt_friendly": bool(status == "success" and stats.get("line_count", 0) != 1),
                "sample_status": sample_status(path, local_stats),
                "mature_sample_status": "",
                "content_preview_hash": sha256(text[:4096].encode("utf-8", errors="ignore")).hexdigest()[:16] if text else "",
                "checked_at": checked_at,
            }
        )
    return rows


def sample_status(path: Path, stats: dict[str, Any]) -> str:
    rows = int(stats.get("rows") or 0)
    if path.as_posix().startswith("data/stock_price_history/"):
        if rows >= 60:
            return "ok"
        if rows > 0:
            return "insufficient_price_history"
        return "missing_or_unreadable"
    if path.as_posix().startswith("data/tdcc_stock_history/"):
        if rows >= 8:
            return "ok"
        if rows > 0:
            return "insufficient_tdcc_history"
        return "missing_or_unreadable"
    if path.suffix.lower() == ".csv":
        return "ok" if rows > 0 else "empty_table"
    return "ok" if int(stats.get("line_count") or 0) > 1 else "content_not_expanded"


def stock_paths(stock_id: str) -> list[tuple[str, Path]]:
    stock_id = normalize_stock_id(stock_id)
    return [
        ("stock_price_history", Path(f"data/stock_price_history/{stock_id}.csv")),
        ("tdcc_stock_history", Path(f"data/tdcc_stock_history/{stock_id}.csv")),
        ("individual_stock_chatgpt_packet", Path(f"output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md")),
        ("individual_stock_report_md", Path(f"output/latest/individual_stock_reports/{stock_id}_latest.md")),
        ("sell_strategy_summary", Path(f"output/history/sell_strategy_backtest/{stock_id}_sell_strategy_summary.md")),
        ("sell_strategy_backtest", Path(f"output/history/sell_strategy_backtest/{stock_id}_sell_strategy_backtest.csv")),
    ]


def build_check_list(stock_ids: list[str], include_all_core: bool) -> list[tuple[str, Path, str]]:
    items: list[tuple[str, Path, str]] = []
    if include_all_core:
        items.extend((label, path, "") for label, path in CORE_PATHS)
        for report_path in sorted(Path("output/latest/individual_stock_reports").glob("*_latest.md")):
            stock_id = normalize_stock_id(report_path.stem.replace("_latest", ""))
            if stock_id:
                items.extend((label, path, stock_id) for label, path in stock_paths(stock_id))
    for stock_id in stock_ids:
        normalized = normalize_stock_id(stock_id)
        items.extend((label, path, normalized) for label, path in stock_paths(normalized))
    seen: set[tuple[str, str, str]] = set()
    unique: list[tuple[str, Path, str]] = []
    for label, path, stock_id in items:
        key = (label, path.as_posix(), stock_id)
        if key not in seen:
            unique.append((label, path, stock_id))
            seen.add(key)
    return unique


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def md_table(df: pd.DataFrame, columns: list[str], limit: int = 120) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    use = df[[c for c in columns if c in df.columns]].head(limit).copy()
    cols = list(use.columns)
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join(["---"] * len(cols)) + " |",
    ]
    for _, row in use.iterrows():
        values = [safe_str(row.get(c)).replace("|", "/") for c in cols]
        lines.append("| " + " | ".join(values) + " |")
    if len(df) > limit:
        lines.append(f"\n_Only first {limit} rows shown. Use CSV for all rows._")
    return lines


def write_status_md(df: pd.DataFrame, source_types: list[str]) -> None:
    status_counts = df["status_category"].value_counts().to_dict() if not df.empty else {}
    logical = (
        df.groupby("logical_source")["status_category"]
        .apply(lambda s: "success" if (s == "success").any() else safe_str(s.iloc[0]))
        .reset_index(name="best_status")
        if not df.empty
        else pd.DataFrame()
    )
    lines = [
        "# Raw Data Fetch Status",
        "",
        f"- generated_at: {now_text()}",
        f"- sources_checked: {', '.join(source_types)}",
        f"- checked_rows: {len(df)}",
        f"- success_rows: {status_counts.get('success', 0)}",
        f"- suspicious_single_line_rows: {status_counts.get('suspicious_single_line', 0)}",
        f"- content_not_expanded_rows: {status_counts.get('content_not_expanded', 0)}",
        f"- cache_miss_rows: {status_counts.get('cache_miss', 0)}",
        f"- internal_fetch_error_rows: {status_counts.get('internal_fetch_error', 0)}",
        f"- csv_raw_url: {RAW_PREFIX}/{FETCH_STATUS_CSV.as_posix()}",
        "",
        "## Meaning",
        "",
        "- `missing_file` means a 404 was observed.",
        "- `raw_fetch_failed`, `cache_miss`, `internal_fetch_error`, and `content_not_expanded` do not prove the repo lacks data.",
        "- `file_exists_but_content_unreadable` means a fallback existence check found the file, but content retrieval failed.",
        "- `standard_rawdata_report` requires stock price history rows >= 60; TDCC fewer than 8 rows is `insufficient_tdcc_history`.",
        "",
        "## Logical Source Summary",
        "",
    ]
    lines.extend(md_table(logical, ["logical_source", "best_status"], limit=200))
    lines.extend(["", "## Detail Preview", ""])
    lines.extend(
        md_table(
            df,
            [
                "logical_source",
                "stock_id",
                "source_type",
                "status_category",
                "http_status",
                "rows",
                "columns",
                "line_count",
                "local_line_count",
                "sample_status",
                "chatgpt_friendly",
            ],
            limit=200,
        )
    )
    FETCH_STATUS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(stock_ids: list[str], include_all_core: bool, source_types: list[str], max_workers: int) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    items = build_check_list(stock_ids, include_all_core)
    workers = max(1, min(max_workers, len(items) or 1))
    if workers == 1:
        for logical_source, path, stock_id in items:
            rows.extend(check_one(logical_source, path, stock_id, source_types))
    else:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(check_one, logical_source, path, stock_id, source_types): (logical_source, path, stock_id)
                for logical_source, path, stock_id in items
            }
            for future in as_completed(futures):
                rows.extend(future.result())
    df = pd.DataFrame(rows)
    if not df.empty:
        df = df.sort_values(["logical_source", "stock_id", "source_type", "expected_path"]).reset_index(drop=True)
    write_csv(df, FETCH_STATUS_CSV)
    write_status_md(df, source_types)
    write_csv(df, DOCS_FETCH_STATUS_CSV)
    DOCS_FETCH_STATUS_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_FETCH_STATUS_MD.write_text(FETCH_STATUS_MD.read_text(encoding="utf-8"), encoding="utf-8")
    return df


def parse_args() -> Any:
    parser = ArgumentParser(description="Check GitHub raw/API/Pages readability for ChatGPT-facing data files.")
    parser.add_argument("--stock-id", action="append", default=[], help="Stock id to check. Can be repeated.")
    parser.add_argument("--all", action="store_true", help="Check core ChatGPT-facing files.")
    parser.add_argument(
        "--sources",
        default="raw,pages,api,blob",
        help="Comma-separated sources to check: raw,pages,api,blob. Use raw for a faster daily health check.",
    )
    parser.add_argument("--max-workers", type=int, default=8, help="Parallel fetch workers.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    stock_ids = [normalize_stock_id(x) for x in args.stock_id if normalize_stock_id(x)]
    if not stock_ids and not args.all:
        args.all = True
    source_types = [safe_str(x).lower() for x in safe_str(args.sources).split(",") if safe_str(x)]
    valid_sources = {"raw", "pages", "api", "blob"}
    source_types = [x for x in source_types if x in valid_sources] or ["raw"]
    df = run(stock_ids, args.all, source_types, args.max_workers)
    print(f"Saved: {FETCH_STATUS_CSV} rows={len(df)}")
    print(f"Saved: {FETCH_STATUS_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
