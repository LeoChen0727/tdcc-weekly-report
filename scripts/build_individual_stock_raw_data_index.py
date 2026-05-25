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
REPORT_INDEX_CSV = LATEST_DIR / "individual_stock_reports_index.csv"
REPORT_INDEX_MD = LATEST_DIR / "individual_stock_reports_index.md"


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
            "has_tdcc_history": bool(tdcc_rows),
            "tdcc_history_rows": tdcc_rows,
            "latest_tdcc_date": latest_date_from(tdcc_df, ["as_of_date", "date", "signal_date"]),
            "tdcc_history_status": "ok" if tdcc_rows >= 8 else ("insufficient_tdcc_history" if tdcc_rows else "tdcc_history_missing"),
            "tdcc_history_raw_url": raw_url(tdcc_path),
            "tdcc_history_pages_url": pages_url_for(Path(docs_tdcc_path)) if docs_tdcc_path else "",
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
                    "report_status": report_status,
                    "updated_at": now_text(),
                }
            )

    index = pd.DataFrame(rows).sort_values(["stock_id"]).reset_index(drop=True)
    report_index = pd.DataFrame(report_rows).sort_values(["stock_id"]).reset_index(drop=True)
    write_csv(index, AVAILABLE_INDEX_CSV)
    write_csv(report_index, REPORT_INDEX_CSV)
    write_index_md(index, AVAILABLE_INDEX_MD)
    write_report_index_md(report_index, REPORT_INDEX_MD)
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
            ["stock_id", "stock_name", "has_md", "has_pdf", "has_json", "report_status", "md_raw_url"],
            limit=200,
        )
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    index, report_index = build_indexes()
    print(f"Saved: {AVAILABLE_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {AVAILABLE_INDEX_MD}")
    print(f"Saved: {REPORT_INDEX_CSV} rows={len(report_index)}")
    print(f"Saved: {REPORT_INDEX_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
