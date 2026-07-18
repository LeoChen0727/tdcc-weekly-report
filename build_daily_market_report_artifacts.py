from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any
import json
import math
import re
import shutil
from urllib.parse import quote

import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from scripts.tracking_utils import require_daily_report_ready_main_price_date

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image,
)
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics


LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")
DATA_PRICE_DIR = Path("data/daily_price")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
VOLUME_BREAKOUT_WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
CHART_MANIFEST_CSV = LATEST_DIR / "chart_manifest.csv"
PDF_KLINE_DIR = LATEST_DIR / "charts" / "pdf_kline"
PDF_KLINE_STATUS_CSV = LATEST_DIR / "pdf_kline_chart_status_latest.csv"
PDF_KLINE_STATUS_JSON = LATEST_DIR / "pdf_kline_chart_status_latest.json"
PDF_KLINE_STATUS_MD = LATEST_DIR / "pdf_kline_chart_status_latest.md"
PDF_KLINE_DAYS_DEFAULT = 126
PDF_KLINE_MIN_DAYS = 60

# 中文檔名：給人看
LATEST_SUMMARY_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
LATEST_FULL_MD = LATEST_DIR / "完整候選股清單_完整版.md"
PUBLISHED_DAILY_MARKET_DIR = LATEST_DIR / "published_reports" / "daily_market"
PUBLISHED_SUMMARY_PDF_STEM = "每日全市場候選股監測報告_精華版"
PUBLISHED_FULL_PDF_STEM = "完整候選股清單_完整版"
LEGACY_ROOT_DAILY_MARKET_PDFS = (
    LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf",
    LATEST_DIR / "完整候選股清單_完整版表格.pdf",
)

# 英文 alias：給 ChatGPT / raw 工具穩定讀取
LATEST_SUMMARY_ALIAS_MD = LATEST_DIR / "daily_market_summary_latest.md"
LATEST_SUMMARY_ALIAS_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
LATEST_FULL_ALIAS_MD = LATEST_DIR / "daily_market_full_latest.md"
LATEST_FULL_ALIAS_PDF = LATEST_DIR / "daily_market_full_latest.pdf"

MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"

GITHUB_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"

CATEGORY_ORDER = [
    "true_breakout",
    "range_rebound",
    "near_resistance",
    "abnormal_volume_up",
    "revenue_breakout_low_response",
    "revenue_pullback",
    "pullback_rebound",
    "pattern",
]

EXCLUDED_FINAL_REPORT_CATEGORIES = {"chip_flow_positive_streak"}

CATEGORY_CN = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

SUMMARY_LIMIT_BY_CATEGORY = {
    "true_breakout": 5,
    "range_rebound": 5,
    "near_resistance": 5,
    "abnormal_volume_up": 5,
    "revenue_breakout_low_response": 5,
    "revenue_pullback": 5,
    "pullback_rebound": 5,
    "pattern": 5,
}

FULL_PDF_ROWS_PER_PAGE = 18

FULL_PDF_COLUMN_CONFIG = {
    "true_breakout": {
        "headers": ["股票", "族群", "分數", "排名", "突破型態", "量能", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "range_rebound": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "距前高", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "near_resistance": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "距前高", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "abnormal_volume_up": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "量能", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "revenue_breakout_low_response": {
        "headers": ["股票", "族群", "分數", "排名", "優先級", "營收YoY", "TDCC趨勢", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.4, 3.2, 4.0, 6.8],
    },
    "revenue_pullback": {
        "headers": ["股票", "族群", "分數", "排名", "營收YoY", "距均線", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.4, 2.2, 3.0, 4.0, 7.0],
    },
    "pullback_rebound": {
        "headers": ["股票", "族群", "分數", "排名", "轉強訊號", "距均線", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.2, 3.0, 4.0, 6.6],
    },
    "pattern": {
        "headers": ["股票", "族群", "分數", "排名", "型態訊號", "型態狀態", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.4, 3.0, 4.0, 6.4],
    },
    "default": {
        "headers": ["股票", "族群", "分數", "排名", "分類", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.2, 1.4, 1.4, 3.0, 3.0, 4.0, 8.0],
    },
}


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def safe_str(value) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value)
    if text.lower() in ["nan", "none", "<na>"]:
        return ""
    return text.strip()


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def format_num(value, digits: int = 2) -> str:
    number = safe_float(value)
    if math.isnan(number):
        return ""
    return f"{number:.{digits}f}".rstrip("0").rstrip(".")


def normalize_date(value) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return ""


def published_daily_market_summary_pdf(main_date: str) -> Path:
    date_text = normalize_date(main_date)
    if not date_text:
        raise ValueError("main_price_date is required for published daily market summary PDF")
    return PUBLISHED_DAILY_MARKET_DIR / f"{PUBLISHED_SUMMARY_PDF_STEM}_{date_text}.pdf"


def published_daily_market_full_pdf(main_date: str) -> Path:
    date_text = normalize_date(main_date)
    if not date_text:
        raise ValueError("main_price_date is required for published daily market full PDF")
    return PUBLISHED_DAILY_MARKET_DIR / f"{PUBLISHED_FULL_PDF_STEM}_{date_text}.pdf"


def remove_legacy_root_daily_market_pdfs() -> None:
    for path in LEGACY_ROOT_DAILY_MARKET_PDFS:
        if path.exists():
            path.unlink()


def raw_url_for_path(path: str | Path) -> str:
    path_text = safe_str(path).replace("\\", "/").lstrip("/")
    return GITHUB_RAW_PREFIX + quote(path_text, safe="/")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str)
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def get_main_price_date() -> tuple[str, bool, dict]:
    meta = {
        "generated_at": now_taipei(),
        "main_price_date": "",
        "report_ready": False,
        "stock_monitor_price_date": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "warrant_flow_date": "",
        "report_ready_note": "",
    }

    main_date = require_daily_report_ready_main_price_date()
    freshness = read_csv(DATA_FRESHNESS_CSV)
    if freshness.empty:
        raise RuntimeError(f"{DATA_FRESHNESS_CSV.as_posix()} is required for daily market report artifacts")

    row = freshness.iloc[0].to_dict()
    for key in meta:
        if key in row:
            meta[key] = row[key]

    meta["main_price_date"] = main_date
    meta["report_ready"] = True
    return main_date, True, meta


def load_candidates() -> pd.DataFrame:
    df = read_csv(ALL_CANDIDATES_CSV)

    if df.empty:
        return df

    rename_map = {}

    if "stock_id" not in df.columns:
        for col in ["ticker", "code", "股票代號"]:
            if col in df.columns:
                rename_map[col] = "stock_id"
                break

    if "stock_name" not in df.columns:
        for col in ["name", "股票名稱", "證券名稱"]:
            if col in df.columns:
                rename_map[col] = "stock_name"
                break

    if rename_map:
        df = df.rename(columns=rename_map)

    if "stock_id" not in df.columns:
        df["stock_id"] = ""

    if "stock_name" not in df.columns:
        df["stock_name"] = ""

    if "category" not in df.columns:
        df["category"] = "unknown"

    if "category_cn" not in df.columns:
        df["category_cn"] = df["category"].map(lambda x: CATEGORY_CN.get(safe_str(x), safe_str(x)))

    df = df[~df["category"].astype(str).isin(EXCLUDED_FINAL_REPORT_CATEGORIES)].copy()

    if "note" not in df.columns:
        df["note"] = ""

    if "細分族群" not in df.columns:
        df["細分族群"] = ""

    for col in ["score", "rank", "warrant_flow_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)

    return df


def load_chart_manifest() -> pd.DataFrame:
    df = read_csv(CHART_MANIFEST_CSV)

    if df.empty:
        return df

    if "stock_id" not in df.columns:
        for col in ["ticker", "code", "股票代號"]:
            if col in df.columns:
                df = df.rename(columns={col: "stock_id"})
                break

    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)

    return df


def choose_chart_path(row: pd.Series, chart_manifest: pd.DataFrame) -> str:
    for col in ["chart_path", "chart_url"]:
        value = safe_str(row.get(col, ""))
        if value:
            if value.startswith("http"):
                return value
            if Path(value).exists():
                return value

    if chart_manifest.empty or "stock_id" not in chart_manifest.columns:
        return ""

    stock_id = safe_str(row.get("stock_id", "")).zfill(4)
    category = safe_str(row.get("category", ""))

    part = chart_manifest[chart_manifest["stock_id"].astype(str).str.zfill(4) == stock_id].copy()

    if part.empty:
        return ""

    if "category" in part.columns and category:
        same_category = part[part["category"].astype(str) == category]
        if not same_category.empty:
            part = same_category

    for col in ["chart_path", "path", "chart_url"]:
        if col in part.columns:
            value = safe_str(part.iloc[0].get(col, ""))
            if value:
                return value

    return ""


PRICE_HISTORY_CACHE: dict[str, pd.DataFrame] = {}


def normalize_price_stock_id(value) -> str:
    text = safe_str(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9]", "", text)
    if not text:
        return ""
    if len(text) <= 4:
        return text.zfill(4)
    return text


def chart_days_from_row(row: pd.Series) -> int:
    value = safe_str(row.get("chart_days", ""))
    try:
        days = int(float(value))
    except Exception:
        days = PDF_KLINE_DAYS_DEFAULT
    if days < 60:
        return 60
    return min(days, PDF_KLINE_DAYS_DEFAULT)


def safe_chart_filename(text: str) -> str:
    text = safe_str(text)
    text = text.replace("/", "-").replace("\\", "-").replace(":", "-")
    text = re.sub(r"[^\w\u4e00-\u9fff\-_]+", "_", text)
    return text[:80] or "chart"


def standardize_price_history(df: pd.DataFrame, source_path: Path) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    df = df.copy()

    if "stock_id" not in df.columns:
        for col in ["ticker", "code"]:
            if col in df.columns:
                df = df.rename(columns={col: "stock_id"})
                break

    if "stock_id" not in df.columns:
        match = re.search(r"([0-9]{4,6})", source_path.stem)
        df["stock_id"] = match.group(1) if match else ""

    if "date" not in df.columns:
        match = re.search(r"([0-9]{8})", source_path.name)
        df["date"] = match.group(1) if match else ""

    if "stock_name" not in df.columns:
        if "name" in df.columns:
            df = df.rename(columns={"name": "stock_name"})
        else:
            df["stock_name"] = ""

    required = {"date", "stock_id", "open", "high", "low", "close", "volume"}
    if not required.issubset(set(df.columns)):
        return pd.DataFrame()

    df["date"] = df["date"].map(normalize_date)
    df["stock_id"] = df["stock_id"].map(normalize_price_stock_id)

    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("--", "", regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["date", "stock_id", "open", "high", "low", "close", "volume"])
    df = df[(df["date"].astype(str).str.len() == 8) & (df["stock_id"].astype(str) != "")].copy()

    if df.empty:
        return pd.DataFrame()

    return df[["date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"]]


def load_price_history_from_source(source: str | Path) -> pd.DataFrame:
    source_text = safe_str(source)
    if not source_text or source_text.startswith("http"):
        return pd.DataFrame()

    source_path = Path(source_text)
    cache_key = source_path.as_posix()

    if cache_key in PRICE_HISTORY_CACHE:
        return PRICE_HISTORY_CACHE[cache_key]

    if not source_path.exists():
        PRICE_HISTORY_CACHE[cache_key] = pd.DataFrame()
        return PRICE_HISTORY_CACHE[cache_key]

    paths = sorted(source_path.glob("*.csv")) if source_path.is_dir() else [source_path]
    frames = []

    for path in paths:
        if path.suffix.lower() != ".csv":
            continue
        try:
            df = pd.read_csv(path, dtype=str)
        except Exception as exc:
            print(f"Skip price file {path}: {exc}")
            continue

        standardized = standardize_price_history(df, path)
        if not standardized.empty:
            frames.append(standardized)

    if not frames:
        PRICE_HISTORY_CACHE[cache_key] = pd.DataFrame()
        return PRICE_HISTORY_CACHE[cache_key]

    result = pd.concat(frames, ignore_index=True)
    result = result.drop_duplicates(subset=["date", "stock_id"], keep="last")
    result = result.sort_values(["stock_id", "date"]).reset_index(drop=True)

    PRICE_HISTORY_CACHE[cache_key] = result
    return result


def price_source_candidates(row: pd.Series) -> list[str]:
    stock_id = normalize_price_stock_id(row.get("stock_id", ""))
    sources = []

    explicit_path = safe_str(row.get("price_data_path", ""))
    if explicit_path:
        sources.append(explicit_path)

    if stock_id:
        sources.append((DATA_PRICE_DIR / f"{stock_id}.csv").as_posix())

    sources.extend(
        [
            DATA_PRICE_DIR.as_posix(),
            (LATEST_DIR / f"{stock_id}_price_history.csv").as_posix() if stock_id else "",
            (LATEST_DIR / f"{stock_id}_daily_price.csv").as_posix() if stock_id else "",
            (LATEST_DIR / "official_daily_price_latest.csv").as_posix(),
        ]
    )

    result = []
    seen = set()
    for source in sources:
        source = safe_str(source)
        if source and source not in seen:
            result.append(source)
            seen.add(source)
    return result


def select_price_history_for_row(row: pd.Series) -> tuple[pd.DataFrame, str, str]:
    stock_id = normalize_price_stock_id(row.get("stock_id", ""))
    chart_days = chart_days_from_row(row)
    warnings = []

    if not stock_id:
        return pd.DataFrame(), "", "missing stock_id"

    for source in price_source_candidates(row):
        history = load_price_history_from_source(source)
        if history.empty:
            warnings.append(f"{source}: missing_or_unreadable")
            continue

        part = history[history["stock_id"].astype(str) == stock_id].copy()
        part = part.sort_values("date").drop_duplicates(subset=["date"], keep="last")

        if part.empty:
            warnings.append(f"{source}: no_rows_for_{stock_id}")
            continue

        if len(part) < PDF_KLINE_MIN_DAYS:
            warnings.append(f"{source}: insufficient_days_{len(part)}")
            continue

        return part.tail(chart_days).reset_index(drop=True), source, ""

    return pd.DataFrame(), "", "; ".join(warnings[:4])


def draw_pdf_kline_chart(row: pd.Series, price_df: pd.DataFrame, source: str) -> Path:
    stock_id = normalize_price_stock_id(row.get("stock_id", ""))
    stock_name = safe_str(row.get("stock_name", ""))
    category = safe_str(row.get("category", "unknown")) or "unknown"
    chart_days = chart_days_from_row(row)

    df = price_df.copy().tail(chart_days).reset_index(drop=True)
    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["volume_ma20"] = df["volume"].rolling(20).mean()

    PDF_KLINE_DIR.mkdir(parents=True, exist_ok=True)
    chart_path = PDF_KLINE_DIR / f"{stock_id}_{safe_chart_filename(stock_name)}_{safe_chart_filename(category)}_{chart_days}d.png"

    fig = plt.figure(figsize=(8.0, 5.2))
    grid = fig.add_gridspec(5, 1, hspace=0.08)
    ax_price = fig.add_subplot(grid[:4, 0])
    ax_volume = fig.add_subplot(grid[4, 0], sharex=ax_price)

    x_values = list(range(len(df)))
    candle_width = 0.62

    for idx, item in df.iterrows():
        open_price = float(item["open"])
        high_price = float(item["high"])
        low_price = float(item["low"])
        close_price = float(item["close"])
        color = "#d62728" if close_price >= open_price else "#2ca02c"

        ax_price.vlines(idx, low_price, high_price, color=color, linewidth=0.8)
        body_low = min(open_price, close_price)
        body_height = max(abs(close_price - open_price), 0.01)
        ax_price.add_patch(
            Rectangle(
                (idx - candle_width / 2, body_low),
                candle_width,
                body_height,
                facecolor=color,
                edgecolor=color,
                alpha=0.85,
            )
        )

    ax_price.plot(x_values, df["close"], color="#1f77b4", linewidth=1.0, label="Close")
    ax_price.plot(x_values, df["ma20"], color="#ff7f0e", linewidth=0.9, label="MA20")
    ax_price.plot(x_values, df["ma60"], color="#9467bd", linewidth=0.9, label="MA60")

    if len(df) >= 61:
        prev_60_high = df.iloc[-61:-1]["high"].max()
        ax_price.axhline(prev_60_high, color="#7f7f7f", linestyle="--", linewidth=0.9, label="Prev60 High")

    ax_price.set_title(f"{stock_id} | {len(df)} days | {safe_str(source)}", fontsize=9)
    ax_price.legend(loc="upper left", fontsize=7)
    ax_price.grid(True, alpha=0.22)

    volume_colors = ["#d62728" if close >= open_ else "#2ca02c" for open_, close in zip(df["open"], df["close"])]
    ax_volume.bar(x_values, df["volume"], color=volume_colors, alpha=0.65)
    ax_volume.plot(x_values, df["volume_ma20"], color="#1f77b4", linewidth=0.8, label="Vol MA20")
    ax_volume.grid(True, alpha=0.18)

    tick_count = min(6, len(df))
    if tick_count > 0:
        tick_positions = [int(i * (len(df) - 1) / max(tick_count - 1, 1)) for i in range(tick_count)]
        tick_labels = [str(df.iloc[i]["date"])[4:] for i in tick_positions]
        ax_volume.set_xticks(tick_positions)
        ax_volume.set_xticklabels(tick_labels, rotation=35, ha="right", fontsize=7)

    plt.setp(ax_price.get_xticklabels(), visible=False)
    fig.savefig(chart_path, dpi=130, bbox_inches="tight")
    plt.close(fig)

    return chart_path


def local_chart_path_from_reference(value: str) -> Path | None:
    text = safe_str(value)
    if not text:
        return None

    if "contact_sheet" in text.lower():
        return None

    if text.startswith(GITHUB_RAW_PREFIX):
        text = text[len(GITHUB_RAW_PREFIX):]
    elif text.startswith("http"):
        return None

    path = Path(text)
    if path.exists() and path.is_file():
        return path
    return None


def build_chart_item(row: pd.Series, chart_manifest: pd.DataFrame) -> dict:
    stock_id = normalize_price_stock_id(row.get("stock_id", ""))
    stock_name = safe_str(row.get("stock_name", ""))
    title = f"{stock_id} {stock_name}".strip()

    price_df, source, warning = select_price_history_for_row(row)

    if not price_df.empty:
        try:
            chart_path = draw_pdf_kline_chart(row, price_df, source)
            return {
                "title": title,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "category": safe_str(row.get("category", "")),
                "image_path": chart_path,
                "note": f"來源：日價資料重畫；{source}；{len(price_df)} 日",
                "source_type": "local_price_redraw",
                "source": source,
                "chart_days": chart_days_from_row(row),
            }
        except Exception as exc:
            warning = f"{warning}; redraw_failed: {exc}".strip("; ")

    chart_ref = choose_chart_path(row, chart_manifest)
    fallback_path = local_chart_path_from_reference(chart_ref)

    if fallback_path:
        return {
            "title": title,
            "stock_id": stock_id,
            "stock_name": stock_name,
            "category": safe_str(row.get("category", "")),
            "image_path": fallback_path,
            "note": f"備援：日價資料不足或無法重畫，使用既有 chart_path；{warning}",
            "source_type": "chart_path_fallback",
            "source": chart_ref,
            "chart_days": chart_days_from_row(row),
        }

    chart_path = safe_str(row.get("chart_path", ""))
    chart_url = safe_str(row.get("chart_url", ""))

    return {
        "title": title,
        "stock_id": stock_id,
        "stock_name": stock_name,
        "category": safe_str(row.get("category", "")),
        "image_path": None,
        "note": (
            "無法取得日價資料與圖檔，僅保留 chart_path / chart_url。"
            f" 日價資料狀態：{warning or 'unavailable'}"
            f" chart_path：{chart_path or '-'}"
            f" chart_url：{chart_url or chart_ref or '-'}"
        ),
        "source_type": "missing",
        "source": "",
        "chart_days": chart_days_from_row(row),
    }


def path_to_text(value) -> str:
    if isinstance(value, Path):
        return value.as_posix()
    return safe_str(value)


def chart_status_label(source_type: str) -> str:
    if source_type == "local_price_redraw":
        return "redrawn_from_local_price_data"
    if source_type == "chart_path_fallback":
        return "fallback_to_existing_chart_path"
    return "missing_price_data_and_chart_file"


def build_chart_status_row(row: pd.Series, item: dict) -> dict:
    source_type = safe_str(item.get("source_type", ""))
    return {
        "date": safe_str(row.get("date", "")),
        "stock_id": normalize_price_stock_id(row.get("stock_id", "")),
        "stock_name": safe_str(row.get("stock_name", "")),
        "category": safe_str(row.get("category", "")),
        "category_cn": safe_str(row.get("category_cn", "")),
        "chart_status": chart_status_label(source_type),
        "source_type": source_type,
        "chart_days": safe_str(item.get("chart_days", chart_days_from_row(row))),
        "image_path": path_to_text(item.get("image_path", "")),
        "price_source": safe_str(item.get("source", "")),
        "price_data_path": safe_str(row.get("price_data_path", "")),
        "candidate_chart_path": safe_str(row.get("chart_path", "")),
        "candidate_chart_url": safe_str(row.get("chart_url", "")),
        "note": safe_str(item.get("note", "")),
    }


def write_pdf_kline_status(rows: list[dict]) -> dict:
    columns = [
        "date",
        "stock_id",
        "stock_name",
        "category",
        "category_cn",
        "chart_status",
        "source_type",
        "chart_days",
        "image_path",
        "price_source",
        "price_data_path",
        "candidate_chart_path",
        "candidate_chart_url",
        "note",
    ]

    df = pd.DataFrame(rows)
    if df.empty:
        df = pd.DataFrame(columns=columns)
    else:
        for col in columns:
            if col not in df.columns:
                df[col] = ""
        df = df[columns]

    counts = df["source_type"].value_counts().to_dict() if "source_type" in df.columns else {}
    local_count = int(counts.get("local_price_redraw", 0))
    fallback_count = int(counts.get("chart_path_fallback", 0))
    missing_count = int(counts.get("missing", 0))
    total_count = int(len(df))

    summary = {
        "status": "generated" if total_count else "no_summary_candidates",
        "policy": "local_price_redraw_first",
        "pdf_kline_output_dir": PDF_KLINE_DIR.as_posix(),
        "chart_status_csv": PDF_KLINE_STATUS_CSV.as_posix(),
        "chart_status_json": PDF_KLINE_STATUS_JSON.as_posix(),
        "chart_status_md": PDF_KLINE_STATUS_MD.as_posix(),
        "total_charts": total_count,
        "local_price_redraw_count": local_count,
        "chart_path_fallback_count": fallback_count,
        "missing_count": missing_count,
        "chart_path_and_chart_url_are_fallback_only": True,
        "do_not_downgrade_on_chart_url_failure": True,
    }

    PDF_KLINE_STATUS_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PDF_KLINE_STATUS_CSV, index=False, encoding="utf-8-sig")
    PDF_KLINE_STATUS_JSON.write_text(
        json.dumps({"summary": summary, "charts": df.to_dict("records")}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# 精華版 PDF K 線圖產出狀態",
        "",
        f"- status: `{summary['status']}`",
        f"- policy: `{summary['policy']}`",
        f"- total_charts: `{total_count}`",
        f"- local_price_redraw_count: `{local_count}`",
        f"- chart_path_fallback_count: `{fallback_count}`",
        f"- missing_count: `{missing_count}`",
        f"- pdf_kline_output_dir: `{PDF_KLINE_DIR.as_posix()}`",
        "- chart_path/chart_url 僅是備援欄位，不代表精華版 PDF 優先使用外部圖片。",
        "- 若 chart_url 下載失敗，但 local_price_redraw_count 大於 0，不得把精華版 PDF 說成圖片下載失敗版。",
        "",
        "| stock_id | stock_name | category | chart_status | image_path | price_source |",
        "|---|---|---|---|---|---|",
    ]

    for record in df.to_dict("records"):
        lines.append(
            "| "
            + " | ".join(
                [
                    safe_str(record.get("stock_id", "")),
                    safe_str(record.get("stock_name", "")),
                    safe_str(record.get("category", "")),
                    safe_str(record.get("chart_status", "")),
                    f"`{safe_str(record.get('image_path', ''))}`",
                    f"`{safe_str(record.get('price_source', ''))}`",
                ]
            )
            + " |"
        )

    PDF_KLINE_STATUS_MD.write_text("\n".join(lines), encoding="utf-8")
    return summary


def clean_text(text: str, limit: int = 80) -> str:
    text = safe_str(text)
    text = text.replace("\n", " ").replace("|", "/")
    text = re.sub(r"\s+", " ", text)
    if len(text) > limit:
        return text[:limit] + "..."
    return text


REPEAT_LABEL_TEXT = {
    "first_seen": "首次上榜",
    "continued_2_3d": "連續 2-3 日",
    "continued_many_days": "連續多日",
    "repeated_but_no_breakout": "反覆上榜未突破",
    "continued_overheated": "連續上榜但過熱",
    "stale_signal": "訊號鈍化",
}


def repeat_display(row: pd.Series) -> str:
    label = safe_str(row.get("repeat_appear_label", ""))
    days = safe_float(row.get("consecutive_appear_days_any_category", ""), default=math.nan)
    day_text = str(int(days)) if not math.isnan(days) and days > 0 else ""
    if label in {"continued_2_3d", "continued_many_days"} and day_text:
        return f"連續 {day_text} 日"
    if label:
        return REPEAT_LABEL_TEXT.get(label, label)
    return "資料不足"


def repeat_markdown_text(row: pd.Series) -> str:
    parts = [repeat_display(row)]
    count5 = safe_str(row.get("appear_count_5d", ""))
    count10 = safe_str(row.get("appear_count_10d", ""))
    multi = safe_str(row.get("multi_category_flags", ""))
    if count5:
        parts.append(f"近5日 {count5}")
    if count10:
        parts.append(f"近10日 {count10}")
    if multi:
        parts.append(f"多分類 {multi}")
    return "；".join(parts)


def tdcc_short(row: pd.Series) -> str:
    for col in ["tdcc_accumulation_signal", "tdcc_judgement", "tdcc_accumulation_note"]:
        value = safe_str(row.get(col, ""))
        if value:
            if value == "strong_accumulation":
                return "大戶同步增加"
            if value == "mild_accumulation":
                return "大戶溫和增加"
            if value == "distribution_warning":
                return "大戶轉弱"
            if value == "neutral":
                return "中性"
            return clean_text(value, 28)

    note = safe_str(row.get("note", ""))
    if "TDCC近幾週400張與1000張同步累積" in note:
        return "大戶同步增加"
    if "TDCC近幾週大戶溫和增加" in note:
        return "大戶溫和增加"
    if "TDCC近幾週大戶籌碼轉弱" in note or "TDCC轉弱" in note:
        return "大戶轉弱"

    return ""


def warrant_short(row: pd.Series) -> str:
    signal = safe_str(row.get("warrant_flow_signal", ""))
    score = safe_str(row.get("warrant_flow_score", ""))

    if signal == "no_signal":
        return ""

    if signal and score:
        return f"{signal} / {score}"

    return signal or score


def theme_short(row: pd.Series) -> str:
    return (
        safe_str(row.get("細分族群", ""))
        or safe_str(row.get("theme_note", ""))
        or safe_str(row.get("industry", ""))
        or ""
    )


def breakout_type_short(row: pd.Series) -> str:
    value = safe_str(row.get("breakout_type", ""))
    if value:
        return clean_text(value, 22)

    value = safe_str(row.get("category", ""))
    return clean_text(value, 22)


def volume_short(row: pd.Series) -> str:
    volume_ratio = format_num(row.get("volume_ratio", ""), 2)
    volume_ratio_20 = format_num(row.get("volume_ratio_20", ""), 2)

    if volume_ratio:
        return f"{volume_ratio}x"

    if volume_ratio_20:
        return f"{volume_ratio_20}x"

    return ""


def distance_high_short(row: pd.Series) -> str:
    for col in [
        "distance_to_previous_high_pct",
        "distance_to_previous_60d_high_pct",
        "distance_to_high_60_pct",
    ]:
        value = format_num(row.get(col, ""), 2)
        if value:
            return f"{value}%"
    return ""


def revenue_yoy_short(row: pd.Series) -> str:
    latest = format_num(row.get("latest_revenue_yoy", ""), 1)
    cumulative = format_num(row.get("cumulative_revenue_yoy", ""), 1)

    if latest and cumulative:
        return f"單月{latest}% / 累計{cumulative}%"

    if latest:
        return f"單月{latest}%"

    if cumulative:
        return f"累計{cumulative}%"

    return ""


def ma_distance_short(row: pd.Series) -> str:
    d20 = format_num(row.get("distance_to_ma20_pct", ""), 1)
    d23 = format_num(row.get("distance_to_ema23_pct", ""), 1)
    d60 = format_num(row.get("distance_to_ma60_pct", ""), 1)

    parts = []

    if d20:
        parts.append(f"20MA {d20}%")
    if d23:
        parts.append(f"23EMA {d23}%")
    if d60:
        parts.append(f"60MA {d60}%")

    return " / ".join(parts[:2])


def pattern_signal_short(row: pd.Series) -> str:
    for col in [
        "pattern_signal",
        "action_trigger",
        "breakout_type",
        "category_cn",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            return clean_text(value, 24)
    return ""


def pattern_state_short(row: pd.Series) -> str:
    for col in [
        "pattern_state",
        "price_data_warning",
        "risk_note",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            return clean_text(value, 24)
    return ""


def compact_note_tags(row: pd.Series) -> list[str]:
    note = safe_str(row.get("note", ""))
    tags = []

    tag_rules = [
        ("嚴格突破", ["嚴格突破", "true_breakout"]),
        ("挑戰前高", ["挑戰前高", "near_resistance"]),
        ("區間轉強", ["區間內轉強", "range_rebound"]),
        ("營收強", ["單月營收YoY", "累計營收YoY"]),
        ("近期加速", ["近期加速", "明顯加速"]),
        ("低反應", ["股價低反應"]),
        ("貼近均線", ["貼近20MA", "貼近20MA/23EMA", "仍在20MA/23EMA附近"]),
        ("站上均線", ["站上20MA/23EMA"]),
        ("未過前高", ["尚未突破前60日高點"]),
        ("平台整理", ["仍在平台整理區"]),
        ("接近前高", ["接近前高"]),
        ("過熱警示", ["過熱", "already_priced_in", "已反應"]),
        ("TDCC轉弱", ["TDCC近幾週大戶籌碼轉弱", "D_降級_TDCC轉弱"]),
        ("TDCC增加", ["TDCC近幾週400張與1000張同步累積", "TDCC近幾週大戶溫和增加"]),
    ]

    for tag, keywords in tag_rules:
        if any(keyword in note for keyword in keywords):
            tags.append(tag)

    seen = []
    for tag in tags:
        if tag not in seen:
            seen.append(tag)

    return seen[:4]


def compact_reason(row: pd.Series, category: str, limit: int = 70) -> str:
    tags = []

    if category == "true_breakout":
        tags.append("突破")
        vol = volume_short(row)
        if vol:
            tags.append(f"量能{vol}")

    elif category in ["range_rebound", "near_resistance", "abnormal_volume_up"]:
        tags.append("區間轉強")
        dist = distance_high_short(row)
        if dist:
            tags.append(f"距前高{dist}")

    elif category == "revenue_breakout_low_response":
        priority = safe_str(row.get("revaluation_priority", ""))
        if priority:
            tags.append(priority.replace("_", " "))
        if revenue_yoy_short(row):
            tags.append("營收強")
        tags.extend(compact_note_tags(row))

    elif category == "revenue_pullback":
        if revenue_yoy_short(row):
            tags.append("營收成長")
        ma = ma_distance_short(row)
        if ma:
            tags.append("回均線")
        tags.extend(compact_note_tags(row))

    elif category == "pullback_rebound":
        tags.append("回檔轉強")
        signal = pattern_signal_short(row)
        if signal:
            tags.append(signal)

    elif category == "pattern":
        signal = pattern_signal_short(row)
        state = pattern_state_short(row)
        if signal:
            tags.append(signal)
        if state:
            tags.append(state)

    else:
        category_cn = safe_str(row.get("category_cn", ""))
        if category_cn:
            tags.append(category_cn)

    tdcc = tdcc_short(row)
    if tdcc:
        tags.append(tdcc)

    warrant = warrant_short(row)
    if warrant:
        tags.append(warrant)

    if not tags:
        tags = compact_note_tags(row)

    seen = []
    for tag in tags:
        tag = clean_text(tag, 28)
        if tag and tag not in seen:
            seen.append(tag)

    reason = " / ".join(seen[:5])
    return clean_text(reason, limit)


def build_reason(row: pd.Series, limit: int = 150) -> str:
    parts = []

    for col in [
        "revaluation_priority",
        "tdcc_accumulation_note",
        "tdcc_judgement",
        "warrant_flow_signal",
        "warrant_flow_warning",
        "warrant_note",
        "note",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            parts.append(value)

    if not parts:
        for col in [
            "revenue_acceleration_note",
            "pattern_signal",
            "breakout_type",
            "category_cn",
        ]:
            value = safe_str(row.get(col, ""))
            if value:
                parts.append(value)

    reason = "；".join(parts)
    return clean_text(reason, limit)


def truthy_text(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y", "是"}


def catalyst_short(row: pd.Series, limit: int = 100) -> str:
    parts: list[str] = []
    score = safe_str(row.get("catalyst_strength_score", "")) or safe_str(row.get("fundamental_catalyst_score", ""))
    theme_score = safe_str(row.get("theme_strength_score", ""))
    catalyst_tags = safe_str(row.get("catalyst_tags", ""))
    tags = safe_str(row.get("fundamental_catalyst_tags", ""))
    event_tags = safe_str(row.get("event_catalyst_tags", ""))
    calendar_tags = safe_str(row.get("event_calendar_tags", ""))
    nearest_event = safe_str(row.get("nearest_event_date", ""))
    nearest_event_type = safe_str(row.get("nearest_event_type", ""))
    reaction = safe_str(row.get("price_reaction_level", ""))
    quality = safe_str(row.get("catalyst_quality", ""))
    summary = safe_str(row.get("catalyst_summary", ""))

    if score:
        parts.append(f"score {score}")
    if theme_score:
        parts.append(f"theme {theme_score}/5")
    if catalyst_tags:
        parts.append(catalyst_tags)
    if tags:
        parts.append(tags)
    if event_tags:
        parts.append(event_tags)
    if calendar_tags:
        parts.append(calendar_tags)
    if nearest_event:
        parts.append(f"calendar {nearest_event_type or 'event'} {nearest_event}")
    if reaction:
        parts.append(f"reaction {reaction}")
    if truthy_text(row.get("similar_to_shihsinko_flag", "")):
        parts.append("類事欣科型")
    elif truthy_text(row.get("revenue_good_eps_unconfirmed_flag", "")):
        parts.append("營收好但 EPS 尚未確認")
    if truthy_text(row.get("low_reaction_after_catalyst", "")):
        parts.append("利多尚未完全反應")
    if truthy_text(row.get("already_reacted_to_catalyst", "")) or truthy_text(row.get("catalyst_overheated", "")):
        parts.append("利多已反應/過熱")
    if quality:
        parts.append(quality)
    if summary:
        parts.append(summary)
    return clean_text(" / ".join(parts), limit) if parts else ""


def catalyst_candidates(candidates: pd.DataFrame, limit: int = 12) -> pd.DataFrame:
    if candidates.empty or "fundamental_catalyst_score" not in candidates.columns:
        return pd.DataFrame()
    part = candidates.copy()
    score = pd.to_numeric(part.get("catalyst_strength_score", part.get("fundamental_catalyst_score", "")), errors="coerce").fillna(0)
    proximity_score = pd.to_numeric(part.get("event_proximity_score", ""), errors="coerce").fillna(0)
    mask = (
        score.gt(0)
        | proximity_score.gt(0)
        | part.get("similar_to_shihsinko_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("revenue_good_eps_unconfirmed_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("already_reacted_to_catalyst", pd.Series("", index=part.index)).astype(str).eq("True")
    )
    part["_catalyst_score_sort"] = score + proximity_score
    return part[mask].sort_values("_catalyst_score_sort", ascending=False).head(limit)


def category_pdf_row(category: str, row: pd.Series) -> list[str]:
    stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
    theme = clean_text(theme_short(row), 22)
    score = safe_str(row.get("score", ""))
    rank = safe_str(row.get("rank", ""))
    tdcc = tdcc_short(row)
    warrant = clean_text(warrant_short(row), 26)
    reason = compact_reason(row, category, 70)

    if category == "true_breakout":
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            volume_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category in ["range_rebound", "near_resistance"]:
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            distance_high_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "abnormal_volume_up":
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            volume_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "revenue_breakout_low_response":
        return [
            stock,
            theme,
            score,
            rank,
            clean_text(safe_str(row.get("revaluation_priority", "")), 18),
            revenue_yoy_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "revenue_pullback":
        return [
            stock,
            theme,
            score,
            rank,
            revenue_yoy_short(row),
            ma_distance_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "pullback_rebound":
        return [
            stock,
            theme,
            score,
            rank,
            pattern_signal_short(row),
            ma_distance_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "pattern":
        return [
            stock,
            theme,
            score,
            rank,
            pattern_signal_short(row),
            pattern_state_short(row),
            tdcc,
            warrant,
            reason,
        ]

    return [
        stock,
        theme,
        score,
        rank,
        clean_text(safe_str(row.get("category_cn", "")), 24),
        tdcc,
        warrant,
        reason,
    ]


def sort_candidates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "score" not in df.columns:
        df["score"] = pd.NA

    if "rank" not in df.columns:
        df["rank"] = pd.NA

    if "warrant_flow_score" not in df.columns:
        df["warrant_flow_score"] = 0

    df["_score_sort"] = pd.to_numeric(df["score"], errors="coerce").fillna(-999999)
    df["_rank_sort"] = pd.to_numeric(df["rank"], errors="coerce").fillna(999999)
    df["_warrant_sort"] = pd.to_numeric(df["warrant_flow_score"], errors="coerce").fillna(0)

    df = df.sort_values(
        ["_score_sort", "_warrant_sort", "_rank_sort"],
        ascending=[False, False, True],
    )

    return df.drop(columns=["_score_sort", "_rank_sort", "_warrant_sort"], errors="ignore")


def get_category_groups(df: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    groups = []
    used = set()

    for category in CATEGORY_ORDER:
        part = df[df["category"].astype(str) == category].copy()

        if not part.empty:
            groups.append((category, sort_candidates(part)))
            used.add(category)

    remaining = [
        c for c in df["category"].dropna().astype(str).unique().tolist()
        if c not in used and c not in EXCLUDED_FINAL_REPORT_CATEGORIES
    ]

    for category in remaining:
        part = df[df["category"].astype(str) == category].copy()
        if not part.empty:
            groups.append((category, sort_candidates(part)))

    return groups


def register_pdf_fonts() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def escape_pdf_text(text: str) -> str:
    text = safe_str(text)
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return text


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape_pdf_text(text), style)


def create_pdf_styles(font_name: str) -> dict:
    styles = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Title"],
            fontName=font_name,
            fontSize=20,
            leading=26,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=styles["Heading1"],
            fontName=font_name,
            fontSize=15,
            leading=20,
            spaceBefore=12,
            spaceAfter=8,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=10,
            leading=15,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.5,
            leading=12,
            spaceAfter=4,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.5,
            leading=11,
            alignment=TA_CENTER,
        ),
        "table_cell": ParagraphStyle(
            "table_cell",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.2,
            leading=11,
            alignment=TA_LEFT,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            parent=styles["Heading3"],
            fontName=font_name,
            fontSize=11.5,
            leading=15,
            spaceBefore=5,
            spaceAfter=3,
        ),
        "card_body": ParagraphStyle(
            "card_body",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=9.2,
            leading=13,
            spaceAfter=3,
        ),
        "chart_title": ParagraphStyle(
            "chart_title",
            parent=styles["Heading3"],
            fontName=font_name,
            fontSize=14,
            leading=17,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#C00000"),
            spaceAfter=4,
        ),
        "chart_note": ParagraphStyle(
            "chart_note",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=7.2,
            leading=9,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#555555"),
            spaceBefore=3,
        ),
        "chart_placeholder": ParagraphStyle(
            "chart_placeholder",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.4,
            leading=11,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#8A4B00"),
        ),
    }


def create_table(data: list[list[str]], styles: dict, col_widths=None) -> Table:
    wrapped = []

    for row_idx, row in enumerate(data):
        style = styles["table_header"] if row_idx == 0 else styles["table_cell"]
        wrapped.append([p(safe_str(cell), style) for cell in row])

    table = Table(wrapped, colWidths=col_widths, repeatRows=1)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAEAEA")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BBBBBB")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    return table


def add_chart_image(story: list, chart_path: str, styles: dict) -> None:
    if not chart_path or chart_path.startswith("http"):
        return

    path = Path(chart_path)

    if not path.exists():
        return

    try:
        img = Image(str(path))
        max_width = 22.5 * cm
        max_height = 8.8 * cm
        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight)

        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio

        story.append(img)
        story.append(Spacer(1, 0.25 * cm))
    except Exception as exc:
        story.append(p(f"圖表載入失敗：{chart_path} / {exc}", styles["small"]))


def chart_cell_flowables(item: dict, styles: dict) -> list:
    flowables = [p(safe_str(item.get("title", "")), styles["chart_title"])]
    image_path = item.get("image_path")

    if image_path and Path(image_path).exists():
        try:
            img = Image(str(image_path))
            max_width = 8.4 * cm
            max_height = 5.25 * cm
            ratio = min(max_width / img.imageWidth, max_height / img.imageHeight)
            img.drawWidth = img.imageWidth * ratio
            img.drawHeight = img.imageHeight * ratio
            flowables.append(img)
        except Exception as exc:
            flowables.append(p(f"圖表載入失敗：{image_path} / {exc}", styles["chart_placeholder"]))
    elif safe_str(item.get("title", "")):
        flowables.append(Spacer(1, 4.9 * cm))
        flowables.append(p("無法取得日價資料與圖檔", styles["chart_placeholder"]))

    note = safe_str(item.get("note", ""))
    if note:
        flowables.append(p(note, styles["chart_note"]))

    return flowables


def add_chart_grid(story: list, chart_items: list[dict], styles: dict) -> None:
    if not chart_items:
        return

    for start in range(0, len(chart_items), 4):
        chunk = chart_items[start:start + 4]

        while len(chunk) < 4:
            chunk.append({"title": "", "image_path": None, "note": ""})

        rows = [
            [chart_cell_flowables(chunk[0], styles), chart_cell_flowables(chunk[1], styles)],
            [chart_cell_flowables(chunk[2], styles), chart_cell_flowables(chunk[3], styles)],
        ]

        table = Table(rows, colWidths=[9.0 * cm, 9.0 * cm])
        table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D8D8D8")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]
            )
        )

        if start > 0:
            story.append(PageBreak())

        story.append(table)


def build_summary_markdown(
    candidates: pd.DataFrame,
    chart_manifest: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> str:
    lines = []
    lines.append("# 每日全市場候選股監測報告 - 精華版")
    lines.append("")
    lines.append(f"- 主資料日期：`{main_date}`")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 是否可產出正式每日報告：`{report_ready}`")
    lines.append(f"- 判斷說明：{safe_str(meta.get('report_ready_note', ''))}")
    lines.append(f"- 權證資料日期：`{safe_str(meta.get('warrant_flow_date', ''))}`")
    lines.append("")
    lines.append("## 精華版 PDF K 線圖狀態")
    lines.append("")
    lines.append("- PDF K 線圖政策：`local_price_redraw_first`")
    lines.append(f"- PDF K 線圖輸出目錄：`{PDF_KLINE_DIR.as_posix()}`")
    lines.append(f"- PDF K 線圖狀態檔：`{PDF_KLINE_STATUS_MD.as_posix()}`")
    lines.append("- 精華版 PDF 會先使用 repo 內日價資料重畫半年視角 K 線圖（預設約 126 個交易日）；`chart_path` / `chart_url` 只是資料不足時的備援。")
    lines.append("- 不得因候選資料內的 `chart_url` 下載失敗，就把精華版 PDF 判定為圖片下載失敗版。")
    lines.append("")

    if candidates.empty:
        lines.append("目前沒有候選股資料。")
        return "\n".join(lines)

    lines.append("## 今日分類摘要")
    lines.append("")
    lines.append("| 分類 | 檔數 |")
    lines.append("|---|---:|")

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        lines.append(f"| {cn} | {len(part)} |")

    lines.append("")
    lines.append("## 財報 / 事件催化觀察")
    lines.append("")
    lines.append("這是跨分類標籤層，不新增第七大分類；若沒有 EPS / 毛利率 / 重大事件資料來源，只標示待確認，不直接升級。")
    lines.append("")
    catalyst_part = catalyst_candidates(candidates)
    if catalyst_part.empty:
        lines.append("- 今日沒有具備來源確認的財報 / 事件催化候選。")
        lines.append("- 若僅有營收轉強但 EPS 尚未確認，保留在原分類並標示「等 EPS 確認」。")
    else:
        lines.append("| 股票 | 原始分類 | 催化標籤 / 反應程度 | TDCC |")
        lines.append("|---|---|---|---|")
        for _, row in catalyst_part.iterrows():
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
            original_category = safe_str(row.get("category_cn", "")) or safe_str(row.get("category", ""))
            lines.append(
                "| "
                + " | ".join(
                    [
                        stock.replace("|", "/"),
                        original_category.replace("|", "/"),
                        catalyst_short(row, 120).replace("|", "/"),
                        tdcc_short(row).replace("|", "/"),
                    ]
                )
                + " |"
            )
    lines.append("")
    lines.append("## 精華候選股")
    lines.append("")

    for category, part in get_category_groups(candidates):
        show = part.head(SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)).copy()

        if show.empty:
            continue

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)

        lines.append(f"## {cn}")
        lines.append("")

        for _, row in show.iterrows():
            category_value = safe_str(row.get("category", ""))
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
            lines.append(f"### {stock}")
            lines.append(f"- 族群：{theme_short(row)}")
            lines.append(f"- 分數 / 排名：{safe_str(row.get('score', ''))} / {safe_str(row.get('rank', ''))}")
            lines.append(f"- 優先級：{safe_str(row.get('revaluation_priority', ''))}")
            lines.append(f"- 連續上榜：{repeat_markdown_text(row)}")
            lines.append(f"- TDCC：{tdcc_short(row)}")
            lines.append(f"- 權證：{warrant_short(row)}")
            catalyst = catalyst_short(row, 140)
            if catalyst:
                lines.append(f"- 財報 / 事件催化：{catalyst}")
            lines.append(f"- 摘要：{compact_reason(row, category_value, 120)}")
            lines.append(f"- 完整原因：{build_reason(row, 220)}")

            chart_path = choose_chart_path(row, chart_manifest)
            lines.append("- 精華版 PDF K 線圖來源：`local_price_redraw_first`（優先用 repo 日價資料重畫；chart_path/chart_url 僅備援）")
            if chart_path:
                lines.append(f"- 候選資料備援圖表：{chart_path if chart_path.startswith('http') else '`' + chart_path + '`'}")

            lines.append("")

    return "\n".join(lines)


def build_full_markdown(
    candidates: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> str:
    lines = []
    lines.append("# 完整候選股清單 - 完整版")
    lines.append("")
    lines.append(f"- 主資料日期：`{main_date}`")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 是否可產出正式每日報告：`{report_ready}`")
    lines.append(f"- 權證資料日期：`{safe_str(meta.get('warrant_flow_date', ''))}`")
    lines.append("")

    if candidates.empty:
        lines.append("目前沒有候選股資料。")
        return "\n".join(lines)

    display_cols = [
        "date",
        "stock_id",
        "stock_name",
        "細分族群",
        "industry",
        "category_cn",
        "score",
        "rank",
        "revaluation_priority",
        "consecutive_appear_days_any_category",
        "consecutive_appear_days_same_category",
        "appear_count_5d",
        "appear_count_10d",
        "appear_count_20d",
        "first_seen_date",
        "multi_category_flags",
        "repeat_appear_label",
        "tdcc_accumulation_signal",
        "tdcc_judgement",
        "warrant_flow_signal",
        "warrant_flow_score",
        "theme_strength_score",
        "catalyst_strength_score",
        "catalyst_tags",
        "fundamental_catalyst_score",
        "fundamental_catalyst_tags",
        "event_catalyst_tags",
        "event_calendar_tags",
        "event_proximity_score",
        "nearest_event_date",
        "nearest_event_type",
        "nearest_event_name",
        "days_to_nearest_event",
        "price_reaction_level",
        "similar_to_shihsinko_flag",
        "catalyst_quality",
        "catalyst_confidence",
        "already_reacted_to_catalyst",
        "low_reaction_after_catalyst",
        "note",
    ]

    display_cols = [col for col in display_cols if col in candidates.columns]

    if VOLUME_BREAKOUT_WATCH_CSV.exists():
        try:
            volume_watch = pd.read_csv(VOLUME_BREAKOUT_WATCH_CSV, dtype=str, keep_default_na=False)
        except Exception:
            volume_watch = pd.DataFrame()
    else:
        volume_watch = pd.DataFrame()

    lines.append("## 帶量突破 / 放量攻擊觀察")
    lines.append("")
    lines.append("- 這個區塊由程式端從日價 raw data 偵測，會列出嚴格 60 日突破、平台突破、頸線突破、右側放量攻擊與異常放量上漲。")
    lines.append("- 它是完整報告的可見度與回測層，不等於單獨操作依據；仍需搭配 TDCC、連續上榜、過熱與漲幅過低風險。")
    lines.append("")
    volume_cols = [
        "advisory_volume_breakout_rank",
        "stock_id",
        "stock_name",
        "volume_breakout_type",
        "volume_watch_scope",
        "volume_breakout_priority",
        "selection_status",
        "category",
        "pattern_stage",
        "tdcc_status",
        "repeat_appear_label",
        "volume_ratio",
        "return_5d",
        "return_20d",
        "risk_flags",
        "next_volume_breakout_confirmation",
    ]
    volume_cols = [col for col in volume_cols if col in volume_watch.columns]
    if volume_watch.empty or not volume_cols:
        lines.append("_今日沒有產出帶量突破觀察名單。_")
        lines.append("")
    else:
        lines.append(f"- watch_rows: `{len(volume_watch)}`")
        lines.append("")
        lines.append("| " + " | ".join(volume_cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(volume_cols)) + " |")
        for _, row in volume_watch.head(80).iterrows():
            values = []
            for col in volume_cols:
                value = safe_str(row.get(col, "")).replace("\n", " ").replace("|", "/")
                if len(value) > 120:
                    value = value[:120] + "..."
                values.append(value)
            lines.append("| " + " | ".join(values) + " |")
        lines.append("")

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)

        lines.append(f"## {cn}")
        lines.append("")
        lines.append(f"- 檔數：`{len(part)}`")
        lines.append("")
        lines.append("| " + " | ".join(display_cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(display_cols)) + " |")

        for _, row in part.iterrows():
            values = []
            for col in display_cols:
                value = safe_str(row.get(col, ""))
                value = value.replace("\n", " ").replace("|", "/")
                if col == "note" and len(value) > 120:
                    value = value[:120] + "..."
                values.append(value)
            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    return "\n".join(lines)


def build_summary_pdf(
    path: Path,
    candidates: pd.DataFrame,
    chart_manifest: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> None:
    font_name = register_pdf_fonts()
    styles = create_pdf_styles(font_name)

    if PDF_KLINE_DIR.exists():
        for old_chart in PDF_KLINE_DIR.glob("*.png"):
            old_chart.unlink()

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )

    story = []
    story.append(p("每日全市場候選股監測報告 - 精華版", styles["title"]))
    story.append(p(f"主資料日期：{main_date}", styles["normal"]))
    story.append(p(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(p(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(p(f"判斷說明：{safe_str(meta.get('report_ready_note', ''))}", styles["normal"]))
    story.append(p(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(p("PDF K 線圖政策：local_price_redraw_first；chart_path/chart_url 僅作為資料不足時備援。", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    chart_status_rows = []

    if candidates.empty:
        story.append(p("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        write_pdf_kline_status(chart_status_rows)
        return

    summary_rows = [["分類", "檔數"]]

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        summary_rows.append([cn, str(len(part))])

    story.append(p("今日分類摘要", styles["h1"]))
    story.append(create_table(summary_rows, styles, col_widths=[12 * cm, 3 * cm]))
    story.append(Spacer(1, 0.4 * cm))

    first_category = True

    for category, part in get_category_groups(candidates):
        show = part.head(SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)).copy()

        if show.empty:
            continue

        if not first_category:
            story.append(PageBreak())
        first_category = False

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)
        story.append(p(cn, styles["h1"]))

        chart_items = []

        for _, row in show.iterrows():
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
            category_value = safe_str(row.get("category", ""))

            story.append(p(stock, styles["card_title"]))
            story.append(p(f"族群：{theme_short(row)}", styles["card_body"]))
            story.append(p(f"分數 / 排名：{safe_str(row.get('score', ''))} / {safe_str(row.get('rank', ''))}", styles["card_body"]))
            story.append(p(f"優先級：{safe_str(row.get('revaluation_priority', ''))}", styles["card_body"]))
            story.append(p(f"連續上榜：{repeat_markdown_text(row)}", styles["card_body"]))
            story.append(p(f"TDCC：{tdcc_short(row)}", styles["card_body"]))
            story.append(p(f"權證：{warrant_short(row)}", styles["card_body"]))
            story.append(p(f"摘要：{compact_reason(row, category_value, 120)}", styles["card_body"]))

            chart_item = build_chart_item(row, chart_manifest)
            chart_items.append(chart_item)
            chart_status_rows.append(build_chart_status_row(row, chart_item))
            story.append(Spacer(1, 0.2 * cm))

        if chart_items:
            story.append(PageBreak())
            story.append(p(f"{cn} K 線圖", styles["h1"]))
            add_chart_grid(story, chart_items, styles)

    doc.build(story)
    write_pdf_kline_status(chart_status_rows)


def build_full_pdf(
    path: Path,
    candidates: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> None:
    font_name = register_pdf_fonts()
    styles = create_pdf_styles(font_name)

    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        leftMargin=0.9 * cm,
        rightMargin=0.9 * cm,
        topMargin=0.8 * cm,
        bottomMargin=0.8 * cm,
    )

    story = []
    story.append(p("完整候選股清單 - 完整版表格", styles["title"]))
    story.append(p(f"主資料日期：{main_date}", styles["normal"]))
    story.append(p(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(p(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(p(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    if candidates.empty:
        story.append(p("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        return

    for category_index, (category, part) in enumerate(get_category_groups(candidates)):
        cn = CATEGORY_CN.get(
            category,
            safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category,
        )

        config = FULL_PDF_COLUMN_CONFIG.get(category, FULL_PDF_COLUMN_CONFIG["default"])
        headers = config["headers"]
        col_widths = [w * cm for w in config["widths"]]

        chunks = [
            part.iloc[i:i + FULL_PDF_ROWS_PER_PAGE].copy()
            for i in range(0, len(part), FULL_PDF_ROWS_PER_PAGE)
        ]

        for chunk_index, chunk in enumerate(chunks):
            if category_index > 0 or chunk_index > 0:
                story.append(PageBreak())

            story.append(p(f"{cn}（{len(part)} 檔）", styles["h1"]))

            if len(chunks) > 1:
                story.append(p(f"第 {chunk_index + 1} / {len(chunks)} 頁", styles["small"]))

            rows = [headers]

            for _, row in chunk.iterrows():
                rows.append(category_pdf_row(category, row))

            table = create_table(rows, styles, col_widths=col_widths)
            story.append(table)

    doc.build(story)


def read_pdf_kline_status_summary() -> dict:
    if not PDF_KLINE_STATUS_JSON.exists():
        return {}

    try:
        data = json.loads(PDF_KLINE_STATUS_JSON.read_text(encoding="utf-8"))
        if isinstance(data, dict) and isinstance(data.get("summary"), dict):
            return data["summary"]
    except Exception:
        pass

    return {}


def build_manifest(
    main_date: str,
    report_ready: bool,
    meta: dict,
    latest_summary_pdf: Path,
    latest_full_pdf: Path,
    history_summary_md: Path,
    history_summary_pdf: Path,
    history_full_md: Path,
    history_full_pdf: Path,
    history_summary_alias_md: Path,
    history_summary_alias_pdf: Path,
    history_full_alias_md: Path,
    history_full_alias_pdf: Path,
) -> dict:
    kline_status = read_pdf_kline_status_summary()

    return {
        "generated_at": now_taipei() + " Asia/Taipei",
        "main_price_date": main_date,
        "report_ready": bool(report_ready),
        "report_ready_note": safe_str(meta.get("report_ready_note", "")),
        "summary_pdf_kline_policy": kline_status.get("policy", "local_price_redraw_first"),
        "summary_pdf_kline_status": kline_status.get("status", ""),
        "summary_pdf_kline_total_charts": kline_status.get("total_charts", 0),
        "summary_pdf_kline_local_price_redraw_count": kline_status.get("local_price_redraw_count", 0),
        "summary_pdf_kline_chart_path_fallback_count": kline_status.get("chart_path_fallback_count", 0),
        "summary_pdf_kline_missing_count": kline_status.get("missing_count", 0),
        "summary_pdf_kline_output_dir": PDF_KLINE_DIR.as_posix(),
        "summary_pdf_kline_status_csv": str(PDF_KLINE_STATUS_CSV),
        "summary_pdf_kline_status_json": str(PDF_KLINE_STATUS_JSON),
        "summary_pdf_kline_status_md": str(PDF_KLINE_STATUS_MD),

        "recommended_read_order": [
            str(LATEST_SUMMARY_ALIAS_MD),
            str(LATEST_FULL_ALIAS_MD),
            str(LATEST_SUMMARY_ALIAS_PDF),
            str(LATEST_FULL_ALIAS_PDF),
            str(history_summary_alias_md),
            str(history_full_alias_md),
            str(history_summary_alias_pdf),
            str(history_full_alias_pdf),
            str(LATEST_SUMMARY_MD),
            str(LATEST_FULL_MD),
            str(latest_summary_pdf),
            str(latest_full_pdf),
        ],

        "latest_summary_md": str(LATEST_SUMMARY_MD),
        "latest_summary_pdf": str(latest_summary_pdf),
        "latest_full_md": str(LATEST_FULL_MD),
        "latest_full_pdf": str(latest_full_pdf),

        "latest_summary_alias_md": str(LATEST_SUMMARY_ALIAS_MD),
        "latest_summary_alias_pdf": str(LATEST_SUMMARY_ALIAS_PDF),
        "latest_full_alias_md": str(LATEST_FULL_ALIAS_MD),
        "latest_full_alias_pdf": str(LATEST_FULL_ALIAS_PDF),

        "history_summary_md": str(history_summary_md),
        "history_summary_pdf": str(history_summary_pdf),
        "history_full_md": str(history_full_md),
        "history_full_pdf": str(history_full_pdf),

        "history_summary_alias_md": str(history_summary_alias_md),
        "history_summary_alias_pdf": str(history_summary_alias_pdf),
        "history_full_alias_md": str(history_full_alias_md),
        "history_full_alias_pdf": str(history_full_alias_pdf),

        "summary_alias_md_raw_url": raw_url_for_path(LATEST_SUMMARY_ALIAS_MD),
        "summary_alias_pdf_raw_url": raw_url_for_path(LATEST_SUMMARY_ALIAS_PDF),
        "full_alias_md_raw_url": raw_url_for_path(LATEST_FULL_ALIAS_MD),
        "full_alias_pdf_raw_url": raw_url_for_path(LATEST_FULL_ALIAS_PDF),

        "history_summary_alias_md_raw_url": raw_url_for_path(history_summary_alias_md),
        "history_summary_alias_pdf_raw_url": raw_url_for_path(history_summary_alias_pdf),
        "history_full_alias_md_raw_url": raw_url_for_path(history_full_alias_md),
        "history_full_alias_pdf_raw_url": raw_url_for_path(history_full_alias_pdf),

        "summary_md_raw_url": raw_url_for_path(history_summary_md),
        "summary_pdf_raw_url": raw_url_for_path(history_summary_pdf),
        "full_md_raw_url": raw_url_for_path(history_full_md),
        "full_pdf_raw_url": raw_url_for_path(history_full_pdf),

        "data_freshness_raw_url": raw_url_for_path(DATA_FRESHNESS_MD),
        "all_candidates_raw_url": raw_url_for_path(ALL_CANDIDATES_CSV),
        "summary_pdf_kline_status_csv_raw_url": raw_url_for_path(PDF_KLINE_STATUS_CSV),
        "summary_pdf_kline_status_json_raw_url": raw_url_for_path(PDF_KLINE_STATUS_JSON),
        "summary_pdf_kline_status_md_raw_url": raw_url_for_path(PDF_KLINE_STATUS_MD),
    }


def write_manifest_files(manifest: dict) -> None:
    MANIFEST_JSON.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = []
    lines.append("# 每日報告 Manifest")
    lines.append("")
    lines.append(f"- 產生時間：`{manifest.get('generated_at', '')}`")
    lines.append(f"- 主資料日期：`{manifest.get('main_price_date', '')}`")
    lines.append(f"- 是否可產出正式每日報告：`{manifest.get('report_ready', '')}`")
    lines.append(f"- 判斷說明：{manifest.get('report_ready_note', '')}")
    lines.append("")
    lines.append("## 精華版 PDF K 線圖狀態")
    lines.append("")
    lines.append(f"- policy: `{manifest.get('summary_pdf_kline_policy', '')}`")
    lines.append(f"- status: `{manifest.get('summary_pdf_kline_status', '')}`")
    lines.append(f"- total_charts: `{manifest.get('summary_pdf_kline_total_charts', '')}`")
    lines.append(f"- local_price_redraw_count: `{manifest.get('summary_pdf_kline_local_price_redraw_count', '')}`")
    lines.append(f"- chart_path_fallback_count: `{manifest.get('summary_pdf_kline_chart_path_fallback_count', '')}`")
    lines.append(f"- missing_count: `{manifest.get('summary_pdf_kline_missing_count', '')}`")
    lines.append(f"- status_md_raw_url: {manifest.get('summary_pdf_kline_status_md_raw_url', '')}")
    lines.append("- chart_path/chart_url 僅是備援欄位，不代表精華版 PDF 優先使用外部圖片。")
    lines.append("")
    lines.append("## 建議讀取順序")
    lines.append("")
    lines.append("請優先讀英文 alias 檔名，避免 ChatGPT raw 讀取工具對中文檔名 Cache miss。")
    lines.append("")
    lines.append("1. latest 英文精華 MD")
    lines.append("2. latest 英文完整版 MD")
    lines.append("3. latest 英文精華 PDF")
    lines.append("4. latest 英文完整版 PDF")
    lines.append("5. 日期版英文 MD / PDF")
    lines.append("6. 中文檔名僅作人類閱讀備援")
    lines.append("")
    lines.append("## 英文 alias raw URLs")
    lines.append("")
    lines.append(f"- latest summary md: {manifest.get('summary_alias_md_raw_url', '')}")
    lines.append(f"- latest full md: {manifest.get('full_alias_md_raw_url', '')}")
    lines.append(f"- latest summary pdf: {manifest.get('summary_alias_pdf_raw_url', '')}")
    lines.append(f"- latest full pdf: {manifest.get('full_alias_pdf_raw_url', '')}")
    lines.append(f"- history summary md: {manifest.get('history_summary_alias_md_raw_url', '')}")
    lines.append(f"- history full md: {manifest.get('history_full_alias_md_raw_url', '')}")
    lines.append(f"- history summary pdf: {manifest.get('history_summary_alias_pdf_raw_url', '')}")
    lines.append(f"- history full pdf: {manifest.get('history_full_alias_pdf_raw_url', '')}")
    lines.append("")
    lines.append("## 中文檔名 raw URLs")
    lines.append("")
    lines.append(f"- summary_md_raw_url: {manifest.get('summary_md_raw_url', '')}")
    lines.append(f"- summary_pdf_raw_url: {manifest.get('summary_pdf_raw_url', '')}")
    lines.append(f"- full_md_raw_url: {manifest.get('full_md_raw_url', '')}")
    lines.append(f"- full_pdf_raw_url: {manifest.get('full_pdf_raw_url', '')}")
    lines.append("")

    MANIFEST_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLISHED_DAILY_MARKET_DIR.mkdir(parents=True, exist_ok=True)

    main_date, report_ready, meta = get_main_price_date()
    latest_summary_pdf = published_daily_market_summary_pdf(main_date)
    latest_full_pdf = published_daily_market_full_pdf(main_date)
    remove_legacy_root_daily_market_pdfs()

    candidates = load_candidates()
    chart_manifest = load_chart_manifest()

    summary_md = build_summary_markdown(
        candidates=candidates,
        chart_manifest=chart_manifest,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    full_md = build_full_markdown(
        candidates=candidates,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    # 寫中文 latest
    LATEST_SUMMARY_MD.write_text(summary_md, encoding="utf-8")
    LATEST_FULL_MD.write_text(full_md, encoding="utf-8")

    build_summary_pdf(
        path=latest_summary_pdf,
        candidates=candidates,
        chart_manifest=chart_manifest,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    build_full_pdf(
        path=latest_full_pdf,
        candidates=candidates,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    # 寫英文 latest alias
    shutil.copyfile(LATEST_SUMMARY_MD, LATEST_SUMMARY_ALIAS_MD)
    shutil.copyfile(LATEST_FULL_MD, LATEST_FULL_ALIAS_MD)
    shutil.copyfile(latest_summary_pdf, LATEST_SUMMARY_ALIAS_PDF)
    shutil.copyfile(latest_full_pdf, LATEST_FULL_ALIAS_PDF)

    # 中文日期版
    history_summary_md = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.md"
    history_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.pdf"
    history_full_md = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版.md"
    history_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版表格.pdf"

    shutil.copyfile(LATEST_SUMMARY_MD, history_summary_md)
    shutil.copyfile(latest_summary_pdf, history_summary_pdf)
    shutil.copyfile(LATEST_FULL_MD, history_full_md)
    shutil.copyfile(latest_full_pdf, history_full_pdf)

    # 英文日期版 alias
    history_summary_alias_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    history_summary_alias_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    history_full_alias_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    history_full_alias_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    shutil.copyfile(LATEST_SUMMARY_ALIAS_MD, history_summary_alias_md)
    shutil.copyfile(LATEST_SUMMARY_ALIAS_PDF, history_summary_alias_pdf)
    shutil.copyfile(LATEST_FULL_ALIAS_MD, history_full_alias_md)
    shutil.copyfile(LATEST_FULL_ALIAS_PDF, history_full_alias_pdf)

    manifest = build_manifest(
        main_date=main_date,
        report_ready=report_ready,
        meta=meta,
        latest_summary_pdf=latest_summary_pdf,
        latest_full_pdf=latest_full_pdf,
        history_summary_md=history_summary_md,
        history_summary_pdf=history_summary_pdf,
        history_full_md=history_full_md,
        history_full_pdf=history_full_pdf,
        history_summary_alias_md=history_summary_alias_md,
        history_summary_alias_pdf=history_summary_alias_pdf,
        history_full_alias_md=history_full_alias_md,
        history_full_alias_pdf=history_full_alias_pdf,
    )

    write_manifest_files(manifest)

    print(f"Saved: {LATEST_SUMMARY_MD}")
    print(f"Saved: {latest_summary_pdf}")
    print(f"Saved: {LATEST_FULL_MD}")
    print(f"Saved: {latest_full_pdf}")
    print(f"Saved alias: {LATEST_SUMMARY_ALIAS_MD}")
    print(f"Saved alias: {LATEST_SUMMARY_ALIAS_PDF}")
    print(f"Saved alias: {LATEST_FULL_ALIAS_MD}")
    print(f"Saved alias: {LATEST_FULL_ALIAS_PDF}")
    print(f"Saved: {MANIFEST_JSON}")
    print(f"Saved: {MANIFEST_MD}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
