from __future__ import annotations

from argparse import ArgumentParser
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
LATEST_DIR = Path("output/latest")
PACKET_DIR = LATEST_DIR / "individual_stock_chatgpt_packets"
DOCS_PACKET_DIR = Path("docs/latest/individual_stock_chatgpt_packets")
PRICE_WINDOW_DIR = LATEST_DIR / "individual_stock_price_windows"
DOCS_PRICE_WINDOW_DIR = Path("docs/latest/individual_stock_price_windows")
TDCC_WINDOW_DIR = LATEST_DIR / "individual_stock_tdcc_windows"
DOCS_TDCC_WINDOW_DIR = Path("docs/latest/individual_stock_tdcc_windows")
PACKET_INDEX_CSV = LATEST_DIR / "individual_stock_chatgpt_packet_index.csv"
PACKET_INDEX_MD = LATEST_DIR / "individual_stock_chatgpt_packet_index.md"
DOCS_PACKET_INDEX_CSV = Path("docs/latest/individual_stock_chatgpt_packet_index.csv")
DOCS_PACKET_INDEX_MD = Path("docs/latest/individual_stock_chatgpt_packet_index.md")
REPORT_DIR = LATEST_DIR / "individual_stock_reports"
DOCS_REPORT_DIR = Path("docs/latest/individual_stock_reports")
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
SELL_DIR = Path("output/history/sell_strategy_backtest")


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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_blankline_kv_window(df: pd.DataFrame, path: Path, prefix: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    display_prefix = f"PRICE_WINDOW_{len(df)}" if prefix.startswith("PRICE_WINDOW") else prefix
    lines = [f"# {display_prefix}"]
    if df.empty:
        lines.extend(["", "status=no_rows"])
    else:
        header = ",".join(df.columns)
        lines.extend(["", f"columns={header}"])
        for i, (_, row) in enumerate(df.iterrows(), start=1):
            values = [safe_str(row[col]).replace("\n", " ").replace("\r", " ").replace(",", " ") for col in df.columns]
            lines.extend(["", f"{prefix}_ROW_{i:03d}=" + ",".join(values)])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def row_kv_text(row: pd.Series, columns: list[str]) -> str:
    parts = []
    for col in columns:
        value = safe_str(row[col]).replace("\n", " ").replace("\r", " ")
        parts.append(f"{col}={value}")
    return "|".join(parts)


def html_escape(value: Any) -> str:
    text = safe_str(value)
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def write_html_table(df: pd.DataFrame, path: Path, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "<!doctype html>",
        '<html lang="zh-Hant">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{html_escape(title)}</title>",
        "<style>",
        "body{font-family:Arial,'Noto Sans TC',sans-serif;margin:24px;line-height:1.45;color:#111}",
        ".note{color:#555;font-size:13px;margin:8px 0 16px}",
        ".data-row{font-family:Consolas,monospace;font-size:12px;white-space:normal;border-bottom:1px solid #eee;padding:4px 0}",
        "</style>",
        "</head>",
        "<body>",
        f"<h1>{html_escape(title)}</h1>",
        f'<p class="note">Rows: {len(df)}. This 180-day HTML mirror is for ChatGPT/browser extraction. Full raw CSV remains available for programmatic backtests.</p>',
    ]
    if df.empty:
        lines.append('<p class="data-row">status=no_rows</p>')
    else:
        lines.append(f'<p class="data-row">columns={"|".join(html_escape(col) for col in df.columns)}</p>')
        columns = list(df.columns)
        for i, (_, row) in enumerate(df.iterrows(), start=1):
            lines.append(f'<p class="data-row">PRICE_ROW_{i:03d}={html_escape(row_kv_text(row, columns))}</p>')
    lines.extend(["</body>", "</html>"])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


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


def sort_by_date(df: pd.DataFrame, candidates: list[str]) -> pd.DataFrame:
    date_col = first_existing(df, candidates)
    if not date_col or df.empty:
        return df.copy()
    out = df.copy()
    out["_date_key"] = out[date_col].map(normalize_date)
    out = out.sort_values("_date_key").drop(columns=["_date_key"])
    return out


def code_mask(df: pd.DataFrame, code_col: str, stock_id: str) -> pd.Series:
    target = normalize_stock_id(stock_id)
    values = df[code_col].map(normalize_stock_id)
    alternatives = {target, target.lstrip("0")}
    if target.isdigit():
        alternatives.add(target.zfill(4))
        alternatives.add(target.zfill(6))
    return values.isin({x for x in alternatives if x})


def filter_stock_df(df: pd.DataFrame, stock_id: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    code_col = first_existing(df, ["stock_id", "code", "證券代號", "股票代號"])
    if not code_col:
        return pd.DataFrame()
    return df[code_mask(df, code_col, stock_id)].copy()


def pick_value(row: pd.Series | dict[str, Any], candidates: list[str]) -> str:
    for col in candidates:
        if col in row:
            text = safe_str(row[col])
            if text:
                return text
    return ""


def numeric_text(value: Any) -> str:
    text = safe_str(value).replace(",", "")
    if not text:
        return ""
    try:
        number = float(text)
    except Exception:
        return safe_str(value)
    if abs(number) >= 1000 and number.is_integer():
        return str(int(number))
    if number.is_integer():
        return str(int(number))
    return f"{number:.2f}".rstrip("0").rstrip(".")


def csv_block(df: pd.DataFrame, columns: list[str], limit: int | None = None) -> list[str]:
    existing = [col for col in columns if col in df.columns]
    if not existing or df.empty:
        return ["```csv", "status,no_rows", "no_rows,True", "```"]
    out = df[existing].copy()
    if limit is not None:
        out = out.tail(limit)
    for col in existing:
        out[col] = out[col].map(numeric_text)
    lines = ["```csv", ",".join(existing)]
    for _, row in out.iterrows():
        values = [safe_str(row[col]).replace("\n", " ").replace("\r", " ").replace(",", " ") for col in existing]
        lines.append(",".join(values))
    lines.append("```")
    return lines


def select_columns(df: pd.DataFrame, columns: list[str], limit: int | None = None) -> pd.DataFrame:
    existing = [col for col in columns if col in df.columns]
    if not existing or df.empty:
        return pd.DataFrame(columns=existing or columns)
    out = df[existing].copy()
    if limit is not None:
        out = out.tail(limit)
    return out


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    existing = [col for col in columns if col in df.columns]
    if not existing or df.empty:
        return ["| status |", "| --- |", "| no rows |"]
    out = df[existing].head(limit).copy()
    for col in existing:
        out[col] = out[col].map(lambda x: safe_str(x).replace("\n", " ").replace("|", "/"))
    lines = ["| " + " | ".join(existing) + " |", "| " + " | ".join(["---"] * len(existing)) + " |"]
    for _, row in out.iterrows():
        lines.append("| " + " | ".join(safe_str(row[col]) for col in existing) + " |")
    return lines


def stock_name_from_frames(stock_id: str, frames: list[pd.DataFrame]) -> str:
    for df in frames:
        if df.empty:
            continue
        stock_df = filter_stock_df(df, stock_id)
        if stock_df.empty:
            continue
        name_col = first_existing(stock_df, ["stock_name", "name", "股票名稱", "證券名稱"])
        if name_col:
            names = [safe_str(x) for x in stock_df[name_col].tolist() if safe_str(x)]
            if names:
                return names[-1]
    return ""


def collect_stock_ids(frames: list[pd.DataFrame]) -> list[str]:
    ids: set[str] = set()
    for path in DATA_PRICE_DIR.glob("*.csv"):
        ids.add(normalize_stock_id(path.stem))
    for path in DATA_TDCC_DIR.glob("*.csv"):
        ids.add(normalize_stock_id(path.stem))
    for path in REPORT_DIR.glob("*_latest.md"):
        ids.add(normalize_stock_id(path.name.split("_", 1)[0]))
    for df in frames:
        if df.empty:
            continue
        code_col = first_existing(df, ["stock_id", "code", "證券代號", "股票代號"])
        if code_col:
            ids.update(normalize_stock_id(x) for x in df[code_col].tolist() if normalize_stock_id(x))
    return sorted(ids)


def status_from_rows(price_rows: int, tdcc_rows: int) -> tuple[str, str, str]:
    if price_rows >= 120:
        packet_status = "standard_120d_plus_packet"
    elif price_rows >= 60:
        packet_status = "standard_rawdata_packet"
    elif price_rows > 0:
        packet_status = "partial_rawdata_packet"
    else:
        packet_status = "insufficient_price_data"

    if tdcc_rows >= 8:
        tdcc_status = "tdcc_history_ready"
    elif tdcc_rows > 0:
        tdcc_status = "insufficient_tdcc_history"
    else:
        tdcc_status = "tdcc_missing"

    notes = []
    if packet_status == "insufficient_price_data":
        notes.append("price history missing; do not produce standard technical conclusions")
    elif price_rows < 120:
        notes.append("price history shorter than 120 rows; K-line context is partial")
    if tdcc_status == "insufficient_tdcc_history":
        notes.append("TDCC history fewer than 8 weeks; do not make 8-12 week TDCC backtest conclusions")
    if tdcc_status == "tdcc_missing":
        notes.append("TDCC history missing")
    return packet_status, tdcc_status, "; ".join(notes)


def latest_date(df: pd.DataFrame, candidates: list[str]) -> str:
    date_col = first_existing(df, candidates)
    if not date_col or df.empty:
        return ""
    dates = [normalize_date(x) for x in df[date_col].tolist()]
    dates = [x for x in dates if x]
    return max(dates) if dates else ""


def build_packet(
    stock_id: str,
    price_df: pd.DataFrame,
    tdcc_df: pd.DataFrame,
    all_candidates_df: pd.DataFrame,
    warrant_df: pd.DataFrame,
    repeat_df: pd.DataFrame,
    price_days: int,
    tdcc_weeks: int,
) -> tuple[str, dict[str, Any]]:
    price_df = sort_by_date(price_df, ["date", "trade_date"])
    tdcc_df = sort_by_date(tdcc_df, ["as_of_date", "date"])
    candidate_df = sort_by_date(filter_stock_df(all_candidates_df, stock_id), ["date", "signal_date", "report_date"])
    warrant_stock_df = sort_by_date(filter_stock_df(warrant_df, stock_id), ["date"])
    repeat_stock_df = sort_by_date(filter_stock_df(repeat_df, stock_id), ["signal_date", "date"])

    stock_name = stock_name_from_frames(stock_id, [price_df, tdcc_df, candidate_df, warrant_stock_df, repeat_stock_df])
    price_rows = len(price_df)
    tdcc_rows = len(tdcc_df)
    packet_status, tdcc_status, notes = status_from_rows(price_rows, tdcc_rows)
    latest_price_date = latest_date(price_df, ["date", "trade_date"])
    latest_tdcc_date = latest_date(tdcc_df, ["as_of_date", "date"])

    packet_path = PACKET_DIR / f"{stock_id}_packet_latest.md"
    docs_packet_path = DOCS_PACKET_DIR / f"{stock_id}_packet_latest.md"
    price_window_path = PRICE_WINDOW_DIR / f"{stock_id}_price_window_{price_days}_latest.csv"
    price_window_txt_path = PRICE_WINDOW_DIR / f"{stock_id}_price_window_{price_days}_latest.txt"
    price_window_html_path = PRICE_WINDOW_DIR / f"{stock_id}_price_window_{price_days}_latest.html"
    docs_price_window_path = DOCS_PRICE_WINDOW_DIR / price_window_path.name
    docs_price_window_txt_path = DOCS_PRICE_WINDOW_DIR / price_window_txt_path.name
    docs_price_window_html_path = DOCS_PRICE_WINDOW_DIR / price_window_html_path.name
    tdcc_window_path = TDCC_WINDOW_DIR / f"{stock_id}_tdcc_window_latest.csv"
    tdcc_window_txt_path = TDCC_WINDOW_DIR / f"{stock_id}_tdcc_window_latest.txt"
    docs_tdcc_window_path = DOCS_TDCC_WINDOW_DIR / tdcc_window_path.name
    docs_tdcc_window_txt_path = DOCS_TDCC_WINDOW_DIR / tdcc_window_txt_path.name
    price_path = DATA_PRICE_DIR / f"{stock_id}.csv"
    tdcc_path = DATA_TDCC_DIR / f"{stock_id}.csv"
    report_md = REPORT_DIR / f"{stock_id}_latest.md"
    sell_summary = SELL_DIR / f"{stock_id}_sell_strategy_summary.md"

    latest_price = price_df.iloc[-1].to_dict() if not price_df.empty else {}
    latest_tdcc = tdcc_df.iloc[-1].to_dict() if not tdcc_df.empty else {}

    price_window_df = select_columns(
        price_df,
        [
            "date",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "ma5",
            "ma20",
            "ma60",
            "ma120",
            "ema23",
            "return_1d",
            "return_5d",
            "return_20d",
            "volume_ratio",
            "distance_to_ma20_pct",
            "distance_to_high_60_pct",
        ],
        limit=price_days,
    )
    tdcc_window_df = select_columns(
        tdcc_df,
        [
            "as_of_date",
            "over_400_ratio",
            "over_400_change_1w",
            "over_600_ratio",
            "over_600_change_1w",
            "over_800_ratio",
            "over_800_change_1w",
            "over_1000_ratio",
            "over_1000_change_1w",
            "tdcc_consecutive_up_weeks",
            "all_thresholds_up",
            "high_thresholds_up",
            "four_thresholds_sync_up",
            "retail_ratio",
            "total_shareholders",
        ],
        limit=tdcc_weeks,
    )
    write_csv(price_window_df, price_window_path)
    write_csv(price_window_df, docs_price_window_path)
    price_window_prefix = f"PRICE_WINDOW_{price_days}"
    write_blankline_kv_window(price_window_df, price_window_txt_path, price_window_prefix)
    write_blankline_kv_window(price_window_df, docs_price_window_txt_path, price_window_prefix)
    write_html_table(price_window_df, price_window_html_path, f"{stock_id} {stock_name} price window {len(price_window_df)} rows")
    write_html_table(price_window_df, docs_price_window_html_path, f"{stock_id} {stock_name} price window {len(price_window_df)} rows")
    write_csv(tdcc_window_df, tdcc_window_path)
    write_csv(tdcc_window_df, docs_tdcc_window_path)
    write_blankline_kv_window(tdcc_window_df, tdcc_window_txt_path, "TDCC_WINDOW")
    write_blankline_kv_window(tdcc_window_df, docs_tdcc_window_txt_path, "TDCC_WINDOW")

    lines: list[str] = [
        f"# INDIVIDUAL STOCK CHATGPT PACKET - {stock_id} {stock_name}".rstrip(),
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- stock_id: {stock_id}",
        f"- stock_name: {stock_name}",
        f"- packet_status: {packet_status}",
        f"- latest_price_date: {latest_price_date}",
        f"- price_rows: {price_rows}",
        f"- latest_tdcc_date: {latest_tdcc_date}",
        f"- tdcc_rows: {tdcc_rows}",
        f"- tdcc_history_status: {tdcc_status}",
        f"- individual_report_md_exists: {report_md.exists()}",
        f"- sell_strategy_summary_exists: {sell_summary.exists()}",
        f"- notes: {notes}",
        "",
        "## Stable Read URLs",
        f"- packet_pages_url: {pages_url_for(docs_packet_path)}",
        f"- packet_raw_url: {raw_url(packet_path)}",
        f"- packet_github_api_url: {github_api_url(packet_path)}",
        f"- price_window_{price_days}_pages_url: {pages_url_for(docs_price_window_path)}",
        f"- price_window_{price_days}_raw_url: {raw_url(price_window_path)}",
        f"- price_window_{price_days}_github_api_url: {github_api_url(price_window_path)}",
        f"- price_window_{price_days}_txt_pages_url: {pages_url_for(docs_price_window_txt_path)}",
        f"- price_window_{price_days}_txt_raw_url: {raw_url(price_window_txt_path)}",
        f"- price_window_{price_days}_txt_github_api_url: {github_api_url(price_window_txt_path)}",
        f"- price_window_{price_days}_html_pages_url: {pages_url_for(docs_price_window_html_path)}",
        f"- price_window_{price_days}_html_raw_url: {raw_url(price_window_html_path)}",
        f"- price_window_{price_days}_html_github_api_url: {github_api_url(price_window_html_path)}",
        f"- tdcc_window_pages_url: {pages_url_for(docs_tdcc_window_path)}",
        f"- tdcc_window_raw_url: {raw_url(tdcc_window_path)}",
        f"- tdcc_window_github_api_url: {github_api_url(tdcc_window_path)}",
        f"- tdcc_window_txt_pages_url: {pages_url_for(docs_tdcc_window_txt_path)}",
        f"- tdcc_window_txt_raw_url: {raw_url(tdcc_window_txt_path)}",
        f"- tdcc_window_txt_github_api_url: {github_api_url(tdcc_window_txt_path)}",
        f"- price_raw_url: {raw_url(price_path)}",
        f"- price_pages_url: {pages_url_for(Path('docs/data/stock_price_history') / price_path.name)}",
        f"- price_github_api_url: {github_api_url(price_path)}",
        f"- tdcc_raw_url: {raw_url(tdcc_path)}",
        f"- tdcc_pages_url: {pages_url_for(Path('docs/data/tdcc_stock_history') / tdcc_path.name)}",
        f"- tdcc_github_api_url: {github_api_url(tdcc_path)}",
        f"- individual_report_md_raw_url: {raw_url(report_md)}",
        f"- individual_report_md_pages_url: {pages_url_for(DOCS_REPORT_DIR / report_md.name)}",
        f"- individual_report_md_github_api_url: {github_api_url(report_md)}",
        "",
        "## Data Quality Rules",
        "- This packet is generated from repo raw CSV files so ChatGPT does not need to expand large CSV files first.",
        "- Use this packet first for single-stock analysis. Use raw/pages/API URLs only when deeper inspection is needed.",
        f"- For chart or K-line work, always read `price_window_{price_days}_html_pages_url` or `price_window_{price_days}_txt_*` first. The 20-row preview is not enough for technical analysis.",
        "- The full historical CSV remains available for Python backtests.",
        "- If price_rows < 60, do not produce a standard technical report.",
        "- If tdcc_rows < 8, mark insufficient_tdcc_history and do not make 8-12 week TDCC backtest conclusions.",
        "- External news can supplement events, but must not replace repo price history or repo TDCC history as primary data.",
        "",
        "## Latest Price Snapshot",
        f"- date: {pick_value(latest_price, ['date', 'trade_date'])}",
        f"- open: {numeric_text(pick_value(latest_price, ['open']))}",
        f"- high: {numeric_text(pick_value(latest_price, ['high']))}",
        f"- low: {numeric_text(pick_value(latest_price, ['low']))}",
        f"- close: {numeric_text(pick_value(latest_price, ['close']))}",
        f"- volume: {numeric_text(pick_value(latest_price, ['volume']))}",
        f"- ma5: {numeric_text(pick_value(latest_price, ['ma5']))}",
        f"- ma20: {numeric_text(pick_value(latest_price, ['ma20']))}",
        f"- ma60: {numeric_text(pick_value(latest_price, ['ma60']))}",
        f"- ma120: {numeric_text(pick_value(latest_price, ['ma120']))}",
        f"- ema23: {numeric_text(pick_value(latest_price, ['ema23']))}",
        f"- return_5d: {numeric_text(pick_value(latest_price, ['return_5d']))}",
        f"- return_20d: {numeric_text(pick_value(latest_price, ['return_20d']))}",
        f"- volume_ratio: {numeric_text(pick_value(latest_price, ['volume_ratio']))}",
        f"- distance_to_ma20_pct: {numeric_text(pick_value(latest_price, ['distance_to_ma20_pct']))}",
        f"- distance_to_high_60_pct: {numeric_text(pick_value(latest_price, ['distance_to_high_60_pct']))}",
        "",
        "## Recent Price Preview",
        f"This is a short preview only. For K-line/chart work read price_window_{price_days}_txt_* above.",
    ]
    lines.extend(csv_block(price_df, ["date", "open", "high", "low", "close", "volume", "ma5", "ma20", "ma60", "ema23", "volume_ratio"], limit=20))
    lines.extend(
        [
            "",
            "## Latest TDCC Snapshot",
            f"- as_of_date: {pick_value(latest_tdcc, ['as_of_date', 'date'])}",
            f"- over_400_ratio: {numeric_text(pick_value(latest_tdcc, ['over_400_ratio']))}",
            f"- over_600_ratio: {numeric_text(pick_value(latest_tdcc, ['over_600_ratio']))}",
            f"- over_800_ratio: {numeric_text(pick_value(latest_tdcc, ['over_800_ratio']))}",
            f"- over_1000_ratio: {numeric_text(pick_value(latest_tdcc, ['over_1000_ratio']))}",
            f"- over_400_change_1w: {numeric_text(pick_value(latest_tdcc, ['over_400_change_1w']))}",
            f"- over_800_change_1w: {numeric_text(pick_value(latest_tdcc, ['over_800_change_1w']))}",
            f"- over_1000_change_1w: {numeric_text(pick_value(latest_tdcc, ['over_1000_change_1w']))}",
            f"- tdcc_consecutive_up_weeks: {numeric_text(pick_value(latest_tdcc, ['tdcc_consecutive_up_weeks']))}",
            f"- all_thresholds_up: {pick_value(latest_tdcc, ['all_thresholds_up'])}",
            f"- high_thresholds_up: {pick_value(latest_tdcc, ['high_thresholds_up'])}",
            "",
            f"## TDCC Preview",
            "This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.",
        ]
    )
    lines.extend(csv_block(tdcc_df, ["as_of_date", "over_400_ratio", "over_400_change_1w", "over_800_ratio", "over_800_change_1w", "over_1000_ratio", "over_1000_change_1w", "tdcc_consecutive_up_weeks", "all_thresholds_up", "high_thresholds_up"], limit=tdcc_weeks))

    lines.extend(["", "## Candidate Context"])
    lines.extend(
        markdown_table(
            candidate_df.tail(10).iloc[::-1] if not candidate_df.empty else candidate_df,
            [
                "date",
                "stock_id",
                "stock_name",
                "category",
                "category_cn",
                "score",
                "rank",
                "priority",
                "revaluation_priority",
                "pattern_stage",
                "tdcc_judgement",
                "warrant_flow_signal",
                "repeat_appear_label",
                "catalyst_summary",
            ],
            limit=10,
        )
    )
    lines.extend(["", "## Repeat Appearance Context"])
    lines.extend(
        markdown_table(
            repeat_stock_df.tail(5).iloc[::-1] if not repeat_stock_df.empty else repeat_stock_df,
            [
                "signal_date",
                "stock_id",
                "stock_name",
                "consecutive_appear_days_any_category",
                "consecutive_appear_days_same_category",
                "appear_count_5d",
                "appear_count_10d",
                "appear_count_20d",
                "repeat_appear_label",
                "repeat_appear_note",
            ],
            limit=5,
        )
    )
    lines.extend(["", "## Warrant Context"])
    lines.extend(
        markdown_table(
            warrant_stock_df.tail(5).iloc[::-1] if not warrant_stock_df.empty else warrant_stock_df,
            [
                "date",
                "stock_id",
                "stock_name",
                "call_warrant_count",
                "put_warrant_count",
                "call_turnover",
                "put_turnover",
                "call_put_turnover_ratio",
                "warrant_flow_signal",
                "warrant_flow_score",
                "warrant_flow_warning",
            ],
            limit=5,
        )
    )
    lines.extend(
        [
            "",
            "## Interpretation Guardrails",
            "- This packet supports analysis; it is not a buy/sell recommendation by itself.",
            "- For K-line or technical conclusions, use PRICE_WINDOW data first; do not rely on external price websites unless repo price data is unavailable.",
            "- For TDCC conclusions, use TDCC_WINDOW data first; if tdcc_history_status=insufficient_tdcc_history, only make short-term observations.",
            "- Candidate Context shows whether the stock entered the daily model; absence from candidates does not mean price/TDCC raw data is unavailable.",
            "- Warrant signals are auxiliary only and must not be used as a standalone reason.",
            "",
        ]
    )

    text = "\n".join(lines)
    line_count = text.count("\n") + 1
    index_row = {
        "stock_id": stock_id,
        "stock_name": stock_name,
        "packet_status": packet_status,
        "price_rows": price_rows,
        "latest_price_date": latest_price_date,
        "tdcc_rows": tdcc_rows,
        "latest_tdcc_date": latest_tdcc_date,
        "tdcc_history_status": tdcc_status,
        "has_candidate_context": not candidate_df.empty,
        "has_repeat_context": not repeat_stock_df.empty,
        "has_warrant_context": not warrant_stock_df.empty,
        "has_individual_md": report_md.exists(),
        "has_sell_strategy_summary": sell_summary.exists(),
        "packet_lines": line_count,
        "packet_raw_url": raw_url(packet_path),
        "packet_pages_url": pages_url_for(docs_packet_path),
        "packet_github_api_url": github_api_url(packet_path),
        f"price_window_{price_days}_raw_url": raw_url(price_window_path),
        f"price_window_{price_days}_pages_url": pages_url_for(docs_price_window_path),
        f"price_window_{price_days}_github_api_url": github_api_url(price_window_path),
        f"price_window_{price_days}_txt_raw_url": raw_url(price_window_txt_path),
        f"price_window_{price_days}_txt_pages_url": pages_url_for(docs_price_window_txt_path),
        f"price_window_{price_days}_txt_github_api_url": github_api_url(price_window_txt_path),
        f"price_window_{price_days}_html_raw_url": raw_url(price_window_html_path),
        f"price_window_{price_days}_html_pages_url": pages_url_for(docs_price_window_html_path),
        f"price_window_{price_days}_html_github_api_url": github_api_url(price_window_html_path),
        "tdcc_window_raw_url": raw_url(tdcc_window_path),
        "tdcc_window_pages_url": pages_url_for(docs_tdcc_window_path),
        "tdcc_window_github_api_url": github_api_url(tdcc_window_path),
        "tdcc_window_txt_raw_url": raw_url(tdcc_window_txt_path),
        "tdcc_window_txt_pages_url": pages_url_for(docs_tdcc_window_txt_path),
        "tdcc_window_txt_github_api_url": github_api_url(tdcc_window_txt_path),
        "price_raw_url": raw_url(price_path),
        "tdcc_raw_url": raw_url(tdcc_path),
        "data_quality_status": packet_status if tdcc_status != "insufficient_tdcc_history" else f"{packet_status}+insufficient_tdcc_history",
        "notes": notes,
    }
    return text, index_row


def write_index(rows: list[dict[str, Any]], merge_existing: bool) -> pd.DataFrame:
    new_index = pd.DataFrame(rows)
    if merge_existing and PACKET_INDEX_CSV.exists():
        existing = read_csv(PACKET_INDEX_CSV)
        if not existing.empty:
            combined = pd.concat([existing, new_index], ignore_index=True)
            combined["_stock_id_norm"] = combined["stock_id"].map(normalize_stock_id)
            combined = combined.drop_duplicates("_stock_id_norm", keep="last").drop(columns=["_stock_id_norm"])
            new_index = combined
    if not new_index.empty:
        new_index = new_index.sort_values("stock_id")
    write_csv(new_index, PACKET_INDEX_CSV)
    write_csv(new_index, DOCS_PACKET_INDEX_CSV)
    return new_index


def write_index_md(index: pd.DataFrame) -> None:
    status_counts = index["packet_status"].value_counts().to_dict() if "packet_status" in index.columns else {}
    lines = [
        "# Individual Stock ChatGPT Packet Index",
        "",
        f"- generated_at: {now_text()}",
        f"- total_packets: {len(index)}",
        f"- standard_120d_plus_packet: {status_counts.get('standard_120d_plus_packet', 0)}",
        f"- standard_rawdata_packet: {status_counts.get('standard_rawdata_packet', 0)}",
        f"- partial_rawdata_packet: {status_counts.get('partial_rawdata_packet', 0)}",
        f"- insufficient_price_data: {status_counts.get('insufficient_price_data', 0)}",
        f"- csv_raw_url: {raw_url(PACKET_INDEX_CSV)}",
        f"- csv_pages_url: {pages_url_for(DOCS_PACKET_INDEX_CSV)}",
        f"- csv_github_api_url: {github_api_url(PACKET_INDEX_CSV)}",
        "",
        "## Usage",
        "",
        "1. For any stock, read `output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md` first.",
        "2. If raw/pages packet does not expand, read the GitHub API contents endpoint and base64-decode `content`.",
        "3. Use the embedded 180-day compact OHLCV window for K-line, MA, volume, support/resistance, and pattern checks.",
        "4. Use full raw CSV only when deeper backtest or additional columns are needed.",
        "",
        "## Preview",
        "",
    ]
    lines.extend(
        markdown_table(
            index,
            [
                "stock_id",
                "stock_name",
                "packet_status",
                "price_rows",
                "latest_price_date",
                "tdcc_rows",
                "latest_tdcc_date",
                "tdcc_history_status",
                "packet_lines",
                "packet_raw_url",
                "packet_github_api_url",
            ],
            limit=220,
        )
    )
    text = "\n".join(lines) + "\n"
    write_text(PACKET_INDEX_MD, text)
    write_text(DOCS_PACKET_INDEX_MD, text)


def clear_packet_dirs() -> None:
    for directory in [PACKET_DIR, DOCS_PACKET_DIR, PRICE_WINDOW_DIR, DOCS_PRICE_WINDOW_DIR, TDCC_WINDOW_DIR, DOCS_TDCC_WINDOW_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
        for path in (
            list(directory.glob("*_packet_latest.md"))
            + list(directory.glob("*_price_window_120_latest.csv"))
            + list(directory.glob("*_price_window_120_latest.txt"))
            + list(directory.glob("*_price_window_120_latest.html"))
            + list(directory.glob("*_price_window_180_latest.csv"))
            + list(directory.glob("*_price_window_180_latest.txt"))
            + list(directory.glob("*_price_window_180_latest.html"))
            + list(directory.glob("*_tdcc_window_latest.csv"))
            + list(directory.glob("*_tdcc_window_latest.txt"))
        ):
            path.unlink()


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("--stock-id", action="append", default=[], help="Generate only selected stock id. May be repeated.")
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for dry runs.")
    parser.add_argument("--price-days", type=int, default=180)
    parser.add_argument("--tdcc-weeks", type=int, default=12)
    args = parser.parse_args()

    all_candidates_df = read_csv(ALL_CANDIDATES_CSV)
    warrant_df = read_csv(WARRANT_FLOW_CSV)
    repeat_df = read_csv(REPEAT_CSV)
    shared_frames = [all_candidates_df, warrant_df, repeat_df]

    selected = [normalize_stock_id(x) for x in args.stock_id if normalize_stock_id(x)]
    if selected:
        stock_ids = sorted(set(selected))
        merge_existing = True
    else:
        stock_ids = collect_stock_ids(shared_frames)
        merge_existing = False
        clear_packet_dirs()
    if args.limit and args.limit > 0:
        stock_ids = stock_ids[: args.limit]

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_PACKET_DIR.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for stock_id in stock_ids:
        price_df = read_csv(DATA_PRICE_DIR / f"{stock_id}.csv")
        tdcc_df = read_csv(DATA_TDCC_DIR / f"{stock_id}.csv")
        text, index_row = build_packet(
            stock_id=stock_id,
            price_df=price_df,
            tdcc_df=tdcc_df,
            all_candidates_df=all_candidates_df,
            warrant_df=warrant_df,
            repeat_df=repeat_df,
            price_days=args.price_days,
            tdcc_weeks=args.tdcc_weeks,
        )
        packet_path = PACKET_DIR / f"{stock_id}_packet_latest.md"
        docs_packet_path = DOCS_PACKET_DIR / f"{stock_id}_packet_latest.md"
        write_text(packet_path, text)
        shutil.copyfile(packet_path, docs_packet_path)
        rows.append(index_row)

    index = write_index(rows, merge_existing=merge_existing)
    write_index_md(index)
    print(f"Saved packets: {len(rows)}")
    print(f"Saved: {PACKET_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {PACKET_INDEX_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
