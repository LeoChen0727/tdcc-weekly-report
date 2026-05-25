from __future__ import annotations

import argparse
import html
import json
import math
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    Image as PdfImage,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from tdcc_stock_history_utils import (
    plot_tdcc_history_chart,
    tdcc_history_analysis,
)


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

DATA_DAILY_PRICE_DIR = Path("data/daily_price")
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")
LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_DIR = Path("output/history/individual_stock_reports")
LATEST_CHART_DIR = LATEST_DIR / "charts"
SELL_BACKTEST_DIR = Path("output/history/sell_strategy_backtest")
SELL_PERFORMANCE_CSV = LATEST_DIR / "sell_strategy_performance_latest.csv"
SELL_PERFORMANCE_MD = LATEST_DIR / "sell_strategy_performance_latest.md"
DAILY_CANDIDATE_SIGNAL_LOG = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")

INDIVIDUAL_LATEST_DIR = LATEST_DIR / "individual_stock_reports"
DOCS_INDIVIDUAL_DIR = DOCS_LATEST_DIR / "individual_stock_reports"

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
TDCC_TREND_CSV = LATEST_DIR / "tdcc_trend_debug_latest.csv"
TDCC_HOLDER_RATIO_CSV = LATEST_DIR / "tdcc_holder_ratio_latest.csv"

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

CATEGORY_LABEL = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

BULLISH_WARRANT_SIGNALS = {
    "call_strong_inflow",
    "call_inflow",
    "call_put_bullish",
    "low_float_call_spike",
}

RISK_WARRANT_SIGNALS = {
    "put_inflow",
    "call_profit_exit_risk",
    "warrant_overheat",
}


@dataclass
class ReportPaths:
    latest_md: Path
    latest_pdf: Path
    latest_png: Path
    latest_json: Path
    docs_md: Path
    docs_pdf: Path
    docs_png: Path
    docs_json: Path
    history_md: Path
    history_pdf: Path
    history_png: Path
    history_json: Path


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
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def safe_float(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "")
    if not text:
        return default
    try:
        return float(text)
    except Exception:
        return default


def fmt_num(value: Any, digits: int = 2, empty: str = "-") -> str:
    num = safe_float(value)
    if math.isnan(num):
        return empty
    return f"{num:.{digits}f}"


def fmt_pct(value: Any, digits: int = 1, empty: str = "-") -> str:
    num = safe_float(value)
    if math.isnan(num):
        return empty
    return f"{num:.{digits}f}%"


def clean_text(value: Any, limit: int | None = None) -> str:
    text = safe_str(value)
    text = text.replace("\n", " ").replace("\r", " ").replace("|", "/")
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: max(0, limit - 1)] + "…"
    return text


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value).upper()
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Z]", "", text)
    if text.isdigit() and len(text) < 4:
        text = text.zfill(4)
    return text


def code_matches(series: pd.Series, stock_id: str) -> pd.Series:
    normalized = series.astype(str).map(normalize_stock_id)
    wanted = normalize_stock_id(stock_id)
    alternatives = {wanted}
    if wanted.isdigit():
        alternatives.add(wanted.lstrip("0") or wanted)
        if len(wanted) <= 4:
            alternatives.add(wanted.zfill(4))
        if len(wanted) <= 6:
            alternatives.add(wanted.zfill(6))
    return normalized.isin(alternatives)


def read_csv(path: Path, **kwargs: Any) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, **kwargs).fillna("")


def normalize_price_columns(df: pd.DataFrame, source_file: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    columns = list(df.columns)
    code_col = ""
    for candidate in ["stock_id", "ticker", "code"]:
        if candidate in columns:
            code_col = candidate
            break
    if not code_col or "date" not in columns or "close" not in columns:
        return pd.DataFrame()

    result = df.copy()
    if "stock_id" not in result.columns:
        result["stock_id"] = result[code_col].map(normalize_stock_id)
    else:
        result["stock_id"] = result["stock_id"].map(normalize_stock_id)
    if "stock_name" not in result.columns and "name" in result.columns:
        result["stock_name"] = result["name"]
    if "stock_name" not in result.columns:
        result["stock_name"] = ""
    if "market" not in result.columns:
        result["market"] = ""
    if "source" not in result.columns:
        result["source"] = ""
    if "source_file" not in result.columns:
        result["source_file"] = source_file

    result["date"] = result["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        if col in result.columns:
            result[col] = pd.to_numeric(result[col].astype(str).str.replace(",", ""), errors="coerce")
        else:
            result[col] = math.nan
    result = result.dropna(subset=["date", "close"])
    return result


def load_freshness() -> dict[str, str]:
    df = read_csv(DATA_FRESHNESS_CSV)
    if df.empty:
        return {}
    return {str(k): safe_str(v) for k, v in df.iloc[0].to_dict().items()}


def main_price_date(freshness: dict[str, str], price_history: pd.DataFrame) -> str:
    for key in ["main_price_date", "all_candidates_date", "official_price_fetch_date"]:
        value = re.sub(r"[^0-9]", "", safe_str(freshness.get(key)))
        if value:
            return value
    if not price_history.empty:
        return safe_str(price_history["date"].iloc[-1])
    return now_taipei().strftime("%Y%m%d")


def load_price_history(stock_id: str) -> pd.DataFrame:
    stock_history_path = STOCK_PRICE_HISTORY_DIR / f"{normalize_stock_id(stock_id)}.csv"
    if stock_history_path.exists():
        history = read_csv(stock_history_path)
        history = normalize_price_columns(history, stock_history_path.as_posix())
        if not history.empty:
            history = history[code_matches(history["stock_id"], stock_id)].copy()
            return history.sort_values("date").reset_index(drop=True)

    frames: list[pd.DataFrame] = []
    for path in sorted(DATA_DAILY_PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(path, dtype=str).fillna("")
        except Exception:
            continue
        normalized = normalize_price_columns(df, path.as_posix())
        if normalized.empty:
            continue
        hit = normalized[code_matches(normalized["stock_id"], stock_id)].copy()
        if not hit.empty:
            hit["source_file"] = path.as_posix()
            frames.append(hit)
    if not frames:
        return pd.DataFrame()

    result = pd.concat(frames, ignore_index=True)
    result["date"] = result["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        if col in result.columns:
            result[col] = pd.to_numeric(result[col].astype(str).str.replace(",", ""), errors="coerce")
    result = result.dropna(subset=["date", "close"])
    result = result.sort_values(["date", "source_file"]).drop_duplicates("date", keep="last")
    return result.sort_values("date").reset_index(drop=True)


def moving_average(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window, min_periods=max(2, min(window, 5))).mean()


def add_price_indicators(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    close = result["close"]
    result["ma5"] = moving_average(close, 5)
    result["ma20"] = moving_average(close, 20)
    result["ma60"] = moving_average(close, 60)
    result["ma120"] = moving_average(close, 120)
    result["ema23"] = close.ewm(span=23, adjust=False, min_periods=5).mean()
    result["vol_ma20"] = moving_average(result["volume"], 20) if "volume" in result.columns else math.nan
    return result


def pct_change_from(df: pd.DataFrame, days: int) -> float:
    if len(df) <= days:
        return math.nan
    latest = safe_float(df["close"].iloc[-1])
    past = safe_float(df["close"].iloc[-1 - days])
    if math.isnan(latest) or math.isnan(past) or past == 0:
        return math.nan
    return (latest / past - 1) * 100


def distance_pct(value: float, base: float) -> float:
    if math.isnan(value) or math.isnan(base) or base == 0:
        return math.nan
    return (value / base - 1) * 100


def summarize_price(df: pd.DataFrame) -> dict[str, Any]:
    if df.empty:
        return {"status": "no_price_data"}

    enriched = add_price_indicators(df)
    latest = enriched.iloc[-1]
    prev_close = safe_float(enriched["close"].iloc[-2]) if len(enriched) >= 2 else math.nan
    close = safe_float(latest.get("close"))
    high_20 = safe_float(enriched.tail(20)["high"].max()) if "high" in enriched.columns else math.nan
    high_60 = safe_float(enriched.tail(60)["high"].max()) if "high" in enriched.columns else math.nan
    high_120 = safe_float(enriched.tail(120)["high"].max()) if "high" in enriched.columns else math.nan
    low_20 = safe_float(enriched.tail(20)["low"].min()) if "low" in enriched.columns else math.nan
    low_60 = safe_float(enriched.tail(60)["low"].min()) if "low" in enriched.columns else math.nan
    ma20 = safe_float(latest.get("ma20"))
    ma60 = safe_float(latest.get("ma60"))
    ema23 = safe_float(latest.get("ema23"))
    volume = safe_float(latest.get("volume"))
    vol_ma20 = safe_float(latest.get("vol_ma20"))
    volume_ratio = volume / vol_ma20 if vol_ma20 and not math.isnan(vol_ma20) else math.nan
    return_1d = distance_pct(close, prev_close)

    metrics = {
        "status": "ok",
        "available_days": len(enriched),
        "latest_date": safe_str(latest.get("date")),
        "stock_name": safe_str(latest.get("stock_name")),
        "market": safe_str(latest.get("market")),
        "close": close,
        "open": safe_float(latest.get("open")),
        "high": safe_float(latest.get("high")),
        "low": safe_float(latest.get("low")),
        "volume": volume,
        "volume_ratio": volume_ratio,
        "ma20": ma20,
        "ma60": ma60,
        "ma120": safe_float(latest.get("ma120")),
        "ema23": ema23,
        "high_20": high_20,
        "high_60": high_60,
        "high_120": high_120,
        "low_20": low_20,
        "low_60": low_60,
        "return_1d": return_1d,
        "return_5d": pct_change_from(enriched, 5),
        "return_20d": pct_change_from(enriched, 20),
        "return_60d": pct_change_from(enriched, 60),
        "return_120d": pct_change_from(enriched, 120),
        "distance_ma20": distance_pct(close, ma20),
        "distance_ma60": distance_pct(close, ma60),
        "distance_ema23": distance_pct(close, ema23),
        "distance_high_20": distance_pct(close, high_20),
        "distance_high_60": distance_pct(close, high_60),
        "distance_high_120": distance_pct(close, high_120),
        "distance_low_60": distance_pct(close, low_60),
    }
    metrics["price_state"] = price_state(metrics)
    metrics["confirmation"] = confirmation_conditions(metrics)
    metrics["price_risks"] = price_risks(metrics)
    return metrics


def price_state(metrics: dict[str, Any]) -> str:
    close = safe_float(metrics.get("close"))
    ma20 = safe_float(metrics.get("ma20"))
    ma60 = safe_float(metrics.get("ma60"))
    dist_high_60 = safe_float(metrics.get("distance_high_60"))
    vol_ratio = safe_float(metrics.get("volume_ratio"))
    dist_ma20 = safe_float(metrics.get("distance_ma20"))

    if not math.isnan(close) and not math.isnan(ma20) and not math.isnan(ma60):
        if close > ma20 > ma60 and not math.isnan(vol_ratio) and vol_ratio >= 1.2:
            return "價格站上 20MA/60MA 且量能高於近期均量，短中期結構偏強。"
        if close > ma20 > ma60:
            return "價格站上 20MA/60MA，結構偏強但仍需觀察量能是否延續。"
        if close < ma20 and close < ma60:
            return "價格位於 20MA/60MA 下方，尚未轉為明確強勢。"
        if close > ma20 and close < ma60:
            return "價格站回 20MA 但仍低於 60MA，屬於反彈觀察。"
    if not math.isnan(dist_high_60) and dist_high_60 >= -3:
        return "價格接近 60 日前高，重點是能否帶量突破或站穩。"
    if not math.isnan(dist_ma20) and abs(dist_ma20) <= 3:
        return "價格貼近 20MA，適合觀察支撐與量能變化。"
    return "價格結構需要搭配均線、前高與量能進一步確認。"


def confirmation_conditions(metrics: dict[str, Any]) -> list[str]:
    close = safe_float(metrics.get("close"))
    high_20 = safe_float(metrics.get("high_20"))
    high_60 = safe_float(metrics.get("high_60"))
    ma20 = safe_float(metrics.get("ma20"))
    ema23 = safe_float(metrics.get("ema23"))
    conditions: list[str] = []
    if not math.isnan(high_20):
        conditions.append(f"能否站上或逼近 20 日高點 {high_20:.2f}。")
    if not math.isnan(high_60):
        conditions.append(f"能否挑戰 60 日高點 {high_60:.2f}，且不是只有盤中觸碰。")
    if not math.isnan(ma20):
        conditions.append(f"回檔時 20MA {ma20:.2f} 是否能提供支撐。")
    if not math.isnan(ema23):
        conditions.append(f"23EMA {ema23:.2f} 附近是否能守住。")
    conditions.append("成交量是否維持在 20 日均量附近或放大，而不是價漲量縮。")
    return conditions[:5]


def price_risks(metrics: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    dist_ma20 = safe_float(metrics.get("distance_ma20"))
    dist_high_60 = safe_float(metrics.get("distance_high_60"))
    volume_ratio = safe_float(metrics.get("volume_ratio"))
    return_20d = safe_float(metrics.get("return_20d"))
    if not math.isnan(dist_ma20) and dist_ma20 >= 12:
        risks.append("股價短線明顯高於 20MA，追價容易遇到震盪。")
    if not math.isnan(dist_high_60) and -3 <= dist_high_60 <= 0:
        risks.append("接近 60 日前高，若量能不足可能遇到壓力。")
    if not math.isnan(volume_ratio) and volume_ratio < 0.75:
        risks.append("成交量低於近期均量，轉強訊號尚不夠紮實。")
    if not math.isnan(return_20d) and return_20d >= 25:
        risks.append("20 日漲幅偏高，需要注意短線過熱。")
    if not risks:
        risks.append("主要風險在於量能延續性與關鍵均線支撐是否失守。")
    return risks


def load_candidate_rows(stock_id: str) -> pd.DataFrame:
    df = read_csv(ALL_CANDIDATES_CSV)
    if df.empty or "stock_id" not in df.columns:
        return pd.DataFrame()
    rows = df[code_matches(df["stock_id"], stock_id)].copy()
    if rows.empty:
        return rows
    rows["_category_order"] = rows.get("category", "").map(
        {cat: idx for idx, cat in enumerate(CATEGORY_ORDER)}
    ).fillna(99)
    rows["_score_num"] = pd.to_numeric(rows.get("score", ""), errors="coerce").fillna(-999999)
    return rows.sort_values(["_category_order", "_score_num"], ascending=[True, False])


def load_warrant_row(stock_id: str) -> dict[str, Any]:
    df = read_csv(WARRANT_FLOW_CSV)
    if df.empty or "stock_id" not in df.columns:
        return {}
    rows = df[code_matches(df["stock_id"], stock_id)]
    if rows.empty:
        return {}
    return rows.iloc[0].to_dict()


def load_tdcc_info(stock_id: str) -> dict[str, Any]:
    info: dict[str, Any] = {}
    trend = read_csv(TDCC_TREND_CSV)
    if not trend.empty and "stock_id" in trend.columns:
        rows = trend[code_matches(trend["stock_id"], stock_id)]
        if not rows.empty:
            info.update(rows.iloc[0].to_dict())
    holder = read_csv(TDCC_HOLDER_RATIO_CSV)
    if not holder.empty and "code" in holder.columns:
        rows = holder[code_matches(holder["code"], stock_id)]
        if not rows.empty:
            latest = rows.iloc[0].to_dict()
            info.update({f"latest_{key}": value for key, value in latest.items()})
    return info


def infer_stock_name(
    stock_id: str,
    price_metrics: dict[str, Any],
    candidate_rows: pd.DataFrame,
    warrant: dict[str, Any],
    tdcc: dict[str, Any],
) -> str:
    for value in [
        price_metrics.get("stock_name"),
        candidate_rows["stock_name"].iloc[0] if not candidate_rows.empty and "stock_name" in candidate_rows.columns else "",
        warrant.get("stock_name"),
        tdcc.get("stock_name"),
        tdcc.get("latest_name"),
    ]:
        text = clean_text(value)
        if text:
            return text
    return stock_id


def candidate_summary(candidate_rows: pd.DataFrame) -> tuple[str, list[dict[str, str]]]:
    if candidate_rows.empty:
        return (
            "未進入今日候選分類，不代表無法分析；僅代表它今天沒有符合全市場候選股篩選條件。以下仍依價格、量能、營收、TDCC、權證資料進行個股狀態分析。",
            [],
        )
    summaries: list[dict[str, str]] = []
    for _, row in candidate_rows.iterrows():
        category = clean_text(row.get("category"))
        label = clean_text(row.get("category_cn")) or CATEGORY_LABEL.get(category, category)
        score_rank = " / ".join(
            part
            for part in [
                f"score {fmt_num(row.get('score'), 1)}" if clean_text(row.get("score")) else "",
                f"rank {fmt_num(row.get('rank'), 0)}" if clean_text(row.get("rank")) else "",
                clean_text(row.get("revaluation_priority")),
            ]
            if part and part != "-"
        )
        summaries.append(
            {
                "category": label,
                "score_rank": score_rank or "-",
                "tdcc": clean_text(row.get("tdcc_accumulation_signal")) or clean_text(row.get("tdcc_judgement")) or "-",
                "warrant": clean_text(row.get("warrant_flow_signal")) or "-",
                "note": clean_text(row.get("note"), 180) or "-",
            }
        )
    labels = "、".join(item["category"] for item in summaries[:4])
    return f"今日有出現在候選資料中，分類為：{labels}。這是附加訊號，不是分析的唯一前提。", summaries


def revenue_summary(candidate_rows: pd.DataFrame) -> dict[str, str]:
    if candidate_rows.empty:
        return {
            "status": "今日候選資料未提供這檔的營收分類訊號。",
            "latest_yoy": "-",
            "cumulative_yoy": "-",
            "note": "若後續需要完整營收歷史，可再把全市場營收資料納入個股 Action。",
        }
    preferred = candidate_rows.copy()
    if "category" in preferred.columns:
        order = {"revenue_breakout_low_response": 0, "revenue_pullback": 1}
        preferred["_rev_order"] = preferred["category"].map(order).fillna(9)
        preferred = preferred.sort_values("_rev_order")
    row = preferred.iloc[0]
    latest = (
        fmt_pct(row.get("latest_revenue_yoy"))
        if clean_text(row.get("latest_revenue_yoy"))
        else fmt_pct(row.get("revenue_yoy_pct"))
    )
    cumulative = (
        fmt_pct(row.get("cumulative_revenue_yoy"))
        if clean_text(row.get("cumulative_revenue_yoy"))
        else fmt_pct(row.get("cumulative_yoy_pct"))
    )
    note = clean_text(row.get("revenue_acceleration_note")) or clean_text(row.get("note"), 160)
    already = clean_text(row.get("already_priced_in"))
    if already:
        note = f"{note}；already_priced_in={already}" if note else f"already_priced_in={already}"
    return {
        "status": "使用今日候選資料中的營收欄位判斷。",
        "latest_yoy": latest,
        "cumulative_yoy": cumulative,
        "note": note or "-",
    }


def tdcc_summary(tdcc: dict[str, Any], candidate_rows: pd.DataFrame) -> dict[str, str]:
    if not tdcc and not candidate_rows.empty:
        row = candidate_rows.iloc[0]
        signal = clean_text(row.get("tdcc_accumulation_signal"))
        note = clean_text(row.get("tdcc_accumulation_note"))
    else:
        signal = clean_text(tdcc.get("tdcc_accumulation_signal"))
        note = clean_text(tdcc.get("tdcc_accumulation_note"))
    if not signal:
        return {
            "signal": "資料不足",
            "status": "TDCC 資料不足，今日不作為主要判斷。",
            "note": "-",
            "over_400": "-",
            "over_1000": "-",
        }
    status_map = {
        "strong_accumulation": "大戶強累積，對訊號可靠度加分。",
        "mild_accumulation": "大戶溫和增加，屬於支撐觀察。",
        "neutral": "籌碼中性，需回到價格與量能確認。",
        "distribution_warning": "大戶轉弱，需降低追蹤優先度。",
    }
    return {
        "signal": signal,
        "status": status_map.get(signal, "TDCC 訊號需搭配價格與量能判斷。"),
        "note": note or "-",
        "over_400": fmt_pct(tdcc.get("latest_over_400_pct")),
        "over_1000": fmt_pct(tdcc.get("latest_over_1000_pct")),
    }


def warrant_summary(warrant: dict[str, Any]) -> dict[str, str]:
    if not warrant:
        return {
            "signal": "資料不足",
            "status": "權證資料不足 / 今日不作為主要判斷。",
            "note": "-",
            "score": "-",
            "date": "-",
        }
    signal = clean_text(warrant.get("warrant_flow_signal")) or "no_signal"
    warning = clean_text(warrant.get("warrant_flow_warning"))
    if signal in BULLISH_WARRANT_SIGNALS:
        status = "權證資金偏多，可作為短線熱度加分，但仍需看位階與 TDCC。"
    elif signal in RISK_WARRANT_SIGNALS or warning:
        status = "權證顯示風險或過熱，需避免只因權證熱度而升級。"
    elif signal == "no_signal":
        status = "今日權證沒有明確加分訊號。"
    else:
        status = "權證訊號僅作輔助參考。"
    return {
        "signal": signal,
        "status": status,
        "note": clean_text(warrant.get("note")) or warning or "-",
        "score": fmt_num(warrant.get("warrant_flow_score"), 1),
        "date": clean_text(warrant.get("date")) or "-",
        "call_turnover": fmt_num(warrant.get("call_turnover"), 0),
        "put_turnover": fmt_num(warrant.get("put_turnover"), 0),
    }


def overall_priority(
    metrics: dict[str, Any],
    candidate_rows: pd.DataFrame,
    tdcc_info: dict[str, str],
    warrant_info: dict[str, str],
) -> str:
    close = safe_float(metrics.get("close"))
    ma20 = safe_float(metrics.get("ma20"))
    ma60 = safe_float(metrics.get("ma60"))
    vol_ratio = safe_float(metrics.get("volume_ratio"))
    dist_high_60 = safe_float(metrics.get("distance_high_60"))
    tdcc_signal = tdcc_info.get("signal", "")
    warrant_signal = warrant_info.get("signal", "")
    candidate_text = " ".join(candidate_rows.astype(str).agg(" ".join, axis=1).tolist()) if not candidate_rows.empty else ""

    if tdcc_signal == "distribution_warning":
        return "僅觀察 / 暫避降級"
    if "D_降級" in candidate_text:
        return "僅觀察 / 暫避降級"
    if (
        not math.isnan(close)
        and not math.isnan(ma20)
        and not math.isnan(ma60)
        and close > ma20 > ma60
        and tdcc_signal in {"strong_accumulation", "mild_accumulation"}
        and (math.isnan(vol_ratio) or vol_ratio >= 0.9)
    ):
        return "最優先追蹤"
    if not math.isnan(dist_high_60) and dist_high_60 >= -5:
        return "可等確認"
    if warrant_signal in BULLISH_WARRANT_SIGNALS and tdcc_signal != "distribution_warning":
        return "可等確認"
    return "僅觀察"


def build_risks(
    price_metrics: dict[str, Any],
    tdcc_info: dict[str, str],
    warrant_info: dict[str, str],
    candidate_rows: pd.DataFrame,
) -> list[str]:
    risks = list(price_metrics.get("price_risks") or [])
    if tdcc_info.get("signal") == "distribution_warning":
        risks.append("TDCC 顯示大戶轉弱，需降低訊號可信度。")
    if warrant_info.get("signal") in RISK_WARRANT_SIGNALS:
        risks.append("權證訊號偏風險或過熱，不能只看短線熱度。")
    if not candidate_rows.empty and "already_priced_in" in candidate_rows.columns:
        if any(str(x).lower() == "true" for x in candidate_rows["already_priced_in"].tolist()):
            risks.append("候選資料標記 already_priced_in=True，代表部分利多可能已反映。")
    clean: list[str] = []
    for item in risks:
        if item not in clean:
            clean.append(item)
    return clean[:6]


SELL_STRATEGIES = [
    ("prior_high", "碰前高賣"),
    ("high_20d", "碰 20日高賣"),
    ("high_60d", "碰 60日高賣"),
    ("high_120d", "碰 120日高賣"),
    ("resistance_scale_out", "壓力區分批賣"),
    ("broker_target_median", "券商目標價中位數賣"),
    ("broker_target_average", "券商目標價平均數賣"),
    ("tdcc_weakening", "TDCC 大戶轉弱賣"),
    ("shareholders_surge", "股東人數暴增賣"),
    ("margin_surge", "融資快速增加賣"),
    ("break_ema23", "跌破 EMA23 賣"),
    ("break_ma20", "跌破 MA20 賣"),
    ("break_neckline", "跌破頸線賣"),
    ("break_breakout_low", "跌破突破K低點賣"),
    ("high_volume_black", "放量長黑賣"),
    ("fixed_d5", "固定 D+5 賣"),
    ("fixed_d10", "固定 D+10 賣"),
    ("fixed_d20", "固定 D+20 賣"),
    ("atr_trailing_stop", "ATR trailing stop 賣"),
    ("percent_trailing_stop", "固定百分比 trailing stop 賣"),
]


def atr_14_from_history(df: pd.DataFrame) -> float:
    if df.empty or not {"high", "low", "close"}.issubset(df.columns):
        return math.nan
    data = df.copy()
    prev_close = data["close"].shift(1)
    tr = pd.concat(
        [
            (data["high"] - data["low"]).abs(),
            (data["high"] - prev_close).abs(),
            (data["low"] - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return safe_float(tr.rolling(14, min_periods=3).mean().iloc[-1])


def price_level_text(value: Any, empty: str = "資料不足") -> str:
    num = safe_float(value)
    if math.isnan(num):
        return empty
    return f"{num:.2f}"


def sorted_levels_above(close: float, levels: list[tuple[str, float]]) -> list[tuple[str, float]]:
    valid = []
    for label, value in levels:
        if not math.isnan(value) and value > close * 1.003:
            valid.append((label, value))
    return sorted(valid, key=lambda item: item[1])


def build_sell_framework(
    stock_id: str,
    stock_name: str,
    price_history: pd.DataFrame,
    price_metrics: dict[str, Any],
    candidate_rows: pd.DataFrame,
    tdcc_info: dict[str, str],
    warrant_info: dict[str, str],
) -> dict[str, Any]:
    close = safe_float(price_metrics.get("close"))
    high_20 = safe_float(price_metrics.get("high_20"))
    high_60 = safe_float(price_metrics.get("high_60"))
    high_120 = safe_float(price_metrics.get("high_120"))
    ma20 = safe_float(price_metrics.get("ma20"))
    ma60 = safe_float(price_metrics.get("ma60"))
    ema23 = safe_float(price_metrics.get("ema23"))
    latest_low = safe_float(price_metrics.get("low"))
    atr14 = atr_14_from_history(price_history)
    atr_stop = close - atr14 * 2 if not math.isnan(close) and not math.isnan(atr14) else math.nan
    levels = sorted_levels_above(close, [("20日高", high_20), ("60日高", high_60), ("120日高", high_120)])
    first_take = levels[0] if levels else ("移動停利", math.nan)
    second_take = levels[1] if len(levels) >= 2 else (levels[0] if levels else ("等待重新形成壓力區", math.nan))
    dist_ma20 = safe_float(price_metrics.get("distance_ma20"))
    ret20 = safe_float(price_metrics.get("return_20d"))
    tdcc_signal = tdcc_info.get("signal", "")
    warrant_signal = warrant_info.get("signal", "")

    if not math.isnan(ret20) and ret20 >= 25:
        exit_style = "分批停利 / 移動停利"
        max_risk = "追高 / 短線過熱"
    elif tdcc_signal == "distribution_warning":
        exit_style = "僅觀察 / 等籌碼修復"
        max_risk = "TDCC 轉弱"
    elif not math.isnan(dist_ma20) and dist_ma20 >= 12:
        exit_style = "分批停利 / 移動停利"
        max_risk = "乖離過大"
    else:
        exit_style = "分批停利 / 移動停利"
        max_risk = "TDCC 轉弱 / 題材退燒 / 營收不如預期"

    technical_exit_parts = []
    if not math.isnan(ema23):
        technical_exit_parts.append(f"跌破 EMA23 {ema23:.2f}")
    if not math.isnan(ma20):
        technical_exit_parts.append(f"跌破 MA20 {ma20:.2f}")
    if not math.isnan(latest_low):
        technical_exit_parts.append(f"跌破近期低點 {latest_low:.2f}")
    if not math.isnan(atr_stop):
        technical_exit_parts.append(f"ATR 風控參考 {atr_stop:.2f}")
    if not technical_exit_parts:
        technical_exit_parts.append("價格資料不足，僅能用條件觀察")

    tdcc_exit = "TDCC >400 / >600 / >800 / >1000 大戶級距轉弱，或大戶連續 2 週下降。"
    if tdcc_signal == "distribution_warning":
        tdcc_exit = "TDCC 已出現 distribution_warning，需優先降低追蹤強度。"
    warrant_exit = "權證認購過熱但股價不漲，或 put_inflow / warrant_overheat 出現時降級。"
    if warrant_signal in RISK_WARRANT_SIGNALS:
        warrant_exit = f"權證已出現 {warrant_signal}，需防短線資金退潮。"

    candidate_text = " ".join(candidate_rows.astype(str).agg(" ".join, axis=1).tolist()) if not candidate_rows.empty else ""
    fundamental_exit = "月營收 YoY / MoM 轉弱、EPS 不如市場預期、題材公布後股價不漲。"
    if "revenue_good_eps_unconfirmed" in candidate_text:
        fundamental_exit = "營收好但 EPS 尚未確認，若後續 EPS 未跟上需降級。"

    framework = {
        "strategy_assumption": "以下為策略假設，不是保證價格，也不是投資建議。",
        "first_take_profit_zone": f"{first_take[0]} {price_level_text(first_take[1])}",
        "second_take_profit_zone": f"{second_take[0]} {price_level_text(second_take[1])}",
        "strong_hold_conditions": "站穩 MA20 / EMA23、TDCC 未轉弱、量價續強，且未出現爆量長上影。",
        "technical_exit": "；".join(technical_exit_parts),
        "tdcc_exit": tdcc_exit,
        "institutional_exit": "外資、投信或主力由買超轉賣超時降級；主力 / 分點資料若 unavailable 不硬判斷。",
        "warrant_exit": warrant_exit,
        "fundamental_exit": fundamental_exit,
        "broker_target_price_note": "無可用券商目標價資料。",
        "suggested_exit_style": exit_style,
        "take_profit_reference": f"{price_level_text(first_take[1])} / {price_level_text(second_take[1])}",
        "failure_exit": "；".join(technical_exit_parts[:2]) if technical_exit_parts else "資料不足，僅能提出觀察條件",
        "hold_to_target_price": "需觀察",
        "max_risk": max_risk,
        "levels": [
            {"name": "close", "value": price_level_text(close)},
            {"name": "20日高", "value": price_level_text(high_20)},
            {"name": "60日高", "value": price_level_text(high_60)},
            {"name": "120日高", "value": price_level_text(high_120)},
            {"name": "MA20", "value": price_level_text(ma20)},
            {"name": "EMA23", "value": price_level_text(ema23)},
            {"name": "MA60", "value": price_level_text(ma60)},
            {"name": "ATR 2倍風控", "value": price_level_text(atr_stop)},
        ],
    }
    return framework


def signal_dates_for_stock(stock_id: str) -> list[str]:
    df = read_csv(DAILY_CANDIDATE_SIGNAL_LOG)
    if df.empty:
        return []
    code_col = "stock_id" if "stock_id" in df.columns else "code" if "code" in df.columns else ""
    date_col = "signal_date" if "signal_date" in df.columns else "report_date" if "report_date" in df.columns else ""
    if not code_col or not date_col:
        return []
    rows = df[code_matches(df[code_col], stock_id)].copy()
    dates = sorted({re.sub(r"[^0-9]", "", safe_str(v))[:8] for v in rows[date_col].tolist() if safe_str(v)})
    return [d for d in dates if len(d) == 8]


def entry_position(price_history: pd.DataFrame, date: str) -> int | None:
    if price_history.empty or "date" not in price_history.columns:
        return None
    date = re.sub(r"[^0-9]", "", safe_str(date))[:8]
    candidates = price_history[price_history["date"].astype(str) <= date]
    if candidates.empty:
        return None
    return int(candidates.index[-1])


def level_hit_exit(window: pd.DataFrame, level: float) -> tuple[str, float, str]:
    if window.empty or math.isnan(level) or "high" not in window.columns:
        return "", math.nan, "level_unavailable"
    hit = window[window["high"] >= level]
    if hit.empty:
        return "", math.nan, "not_hit"
    row = hit.iloc[0]
    return safe_str(row.get("date")), level, "hit"


def simulate_sell_strategy(price_history: pd.DataFrame, entry_date: str, strategy_key: str) -> dict[str, Any]:
    pos = entry_position(price_history, entry_date)
    if pos is None:
        return {"status": "insufficient_price_data", "mature": False}
    data = add_price_indicators(price_history).reset_index(drop=True)
    if pos >= len(data):
        return {"status": "insufficient_price_data", "mature": False}
    entry = data.iloc[pos]
    entry_close = safe_float(entry.get("close"))
    if math.isnan(entry_close) or entry_close <= 0:
        return {"status": "invalid_entry_price", "mature": False}
    available = len(data) - pos - 1
    future = data.iloc[pos + 1 : min(len(data), pos + 21)].copy()
    status = "pending"
    exit_date = ""
    exit_price = math.nan
    reference_level = math.nan

    lookback = data.iloc[: pos + 1]
    high_20 = safe_float(lookback.tail(20)["high"].max())
    high_60 = safe_float(lookback.tail(60)["high"].max())
    high_120 = safe_float(lookback.tail(120)["high"].max())

    if strategy_key in {"prior_high", "high_20d"}:
        reference_level = high_20
        exit_date, exit_price, status = level_hit_exit(future, reference_level)
    elif strategy_key == "high_60d":
        reference_level = high_60
        exit_date, exit_price, status = level_hit_exit(future, reference_level)
    elif strategy_key in {"high_120d", "resistance_scale_out"}:
        reference_level = high_120
        exit_date, exit_price, status = level_hit_exit(future, reference_level)
    elif strategy_key == "fixed_d5":
        horizon = 5
        if available >= horizon:
            row = data.iloc[pos + horizon]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "fixed_horizon"
    elif strategy_key == "fixed_d10":
        horizon = 10
        if available >= horizon:
            row = data.iloc[pos + horizon]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "fixed_horizon"
    elif strategy_key == "fixed_d20":
        horizon = 20
        if available >= horizon:
            row = data.iloc[pos + horizon]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "fixed_horizon"
    elif strategy_key in {"break_ma20", "break_neckline"}:
        hit = future[future["close"] < future["ma20"]]
        if not hit.empty:
            row = hit.iloc[0]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "ma20_break"
    elif strategy_key == "break_ema23":
        hit = future[future["close"] < future["ema23"]]
        if not hit.empty:
            row = hit.iloc[0]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "ema23_break"
    elif strategy_key == "break_breakout_low":
        reference_level = safe_float(entry.get("low"))
        hit = future[future["low"] < reference_level]
        if not hit.empty:
            row = hit.iloc[0]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "breakout_low_break"
    elif strategy_key == "high_volume_black":
        hit = future[(future["close"] < future["open"]) & (future["volume"] > future["vol_ma20"] * 1.5)]
        if not hit.empty:
            row = hit.iloc[0]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(row.get("close")), "high_volume_black"
    elif strategy_key == "atr_trailing_stop":
        atr = atr_14_from_history(lookback)
        if not math.isnan(atr):
            rolling_high = future["high"].cummax()
            stop = rolling_high - atr * 2
            hit = future[future["low"] < stop]
            if not hit.empty:
                idx = hit.index[0]
                row = future.loc[idx]
                exit_date, exit_price, status = safe_str(row.get("date")), safe_float(stop.loc[idx]), "atr_trailing_stop"
    elif strategy_key == "percent_trailing_stop":
        rolling_high = future["high"].cummax()
        stop = rolling_high * 0.92
        hit = future[future["low"] < stop]
        if not hit.empty:
            idx = hit.index[0]
            row = future.loc[idx]
            exit_date, exit_price, status = safe_str(row.get("date")), safe_float(stop.loc[idx]), "percent_trailing_stop"
    else:
        return {"status": "source_unavailable_or_not_implemented", "mature": False}

    if not exit_date and available >= 20 and not future.empty:
        row = future.iloc[-1]
        exit_date, exit_price = safe_str(row.get("date")), safe_float(row.get("close"))
        status = f"{status}_fallback_d20" if status not in {"pending", ""} else "fallback_d20"
    mature = bool(exit_date and not math.isnan(exit_price))
    ret = (exit_price / entry_close - 1) * 100 if mature else math.nan
    if future.empty:
        mfe = mae = math.nan
    else:
        mfe = (safe_float(future["high"].max()) / entry_close - 1) * 100
        mae = (safe_float(future["low"].min()) / entry_close - 1) * 100
    return {
        "status": status,
        "mature": mature,
        "entry_date": safe_str(entry.get("date")),
        "entry_price": entry_close,
        "exit_date": exit_date,
        "exit_price": exit_price,
        "return_pct": ret,
        "mfe_pct": mfe,
        "mae_pct": mae,
        "holding_days": available if not mature else max(1, len(data[(data["date"] > safe_str(entry.get("date"))) & (data["date"] <= exit_date)])),
        "reference_level": reference_level,
        "available_days_after_entry": available,
    }


def write_sell_strategy_outputs(
    stock_id: str,
    stock_name: str,
    main_date: str,
    price_history: pd.DataFrame,
    framework: dict[str, Any],
) -> dict[str, str]:
    SELL_BACKTEST_DIR.mkdir(parents=True, exist_ok=True)
    signal_dates = signal_dates_for_stock(stock_id)
    if not signal_dates:
        signal_dates = [main_date]
    rows: list[dict[str, Any]] = []
    for date in signal_dates[-30:]:
        for key, name in SELL_STRATEGIES:
            result = simulate_sell_strategy(price_history, date, key)
            rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "entry_date": result.get("entry_date", date),
                    "strategy_key": key,
                    "strategy_name": name,
                    "entry_price": result.get("entry_price", ""),
                    "exit_date": result.get("exit_date", ""),
                    "exit_price": result.get("exit_price", ""),
                    "return_pct": result.get("return_pct", ""),
                    "mfe_pct": result.get("mfe_pct", ""),
                    "mae_pct": result.get("mae_pct", ""),
                    "holding_days": result.get("holding_days", ""),
                    "reference_level": result.get("reference_level", ""),
                    "mature": result.get("mature", False),
                    "status": result.get("status", ""),
                    "generated_at": now_text(),
                }
            )
    detail = pd.DataFrame(rows)
    detail_path = SELL_BACKTEST_DIR / f"{stock_id}_sell_strategy_backtest.csv"
    detail.to_csv(detail_path, index=False, encoding="utf-8", lineterminator="\n")

    summary_rows: list[dict[str, Any]] = []
    for key, name in SELL_STRATEGIES:
        part = detail[(detail["strategy_key"] == key) & (detail["mature"].astype(str).str.lower() == "true")].copy()
        returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce")
        mfe = pd.to_numeric(part.get("mfe_pct", pd.Series(dtype=float)), errors="coerce")
        mae = pd.to_numeric(part.get("mae_pct", pd.Series(dtype=float)), errors="coerce")
        holding = pd.to_numeric(part.get("holding_days", pd.Series(dtype=float)), errors="coerce")
        sample = int(returns.notna().sum())
        summary_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "strategy_key": key,
                "strategy_name": name,
                "sample_count": sample,
                "avg_return_pct": returns.mean() if sample else "",
                "median_return_pct": returns.median() if sample else "",
                "win_rate_pct": (returns.gt(0).mean() * 100) if sample else "",
                "avg_mfe_pct": mfe.mean() if sample else "",
                "avg_mae_pct": mae.mean() if sample else "",
                "avg_holding_days": holding.mean() if sample else "",
                "sample_status": "ok" if sample >= 3 else "insufficient_sample",
                "last_updated": now_text(),
            }
        )
    summary = pd.DataFrame(summary_rows)
    summary_path = SELL_BACKTEST_DIR / f"{stock_id}_sell_strategy_summary.md"
    md_lines = [
        f"# Sell Strategy Backtest Summary - {stock_id} {stock_name}",
        "",
        f"- generated_at: {now_text()}",
        f"- signal_sample_dates: {len(signal_dates)}",
        "- note: 賣出規則為策略假設，不是保證價格，也不是投資建議。",
        "",
        "| strategy | sample | avg_return | win_rate | avg_mfe | avg_mae | status |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for _, row in summary.iterrows():
        md_lines.append(
            f"| {row['strategy_name']} | {row['sample_count']} | {fmt_pct(row['avg_return_pct'])} | {fmt_pct(row['win_rate_pct'])} | {fmt_pct(row['avg_mfe_pct'])} | {fmt_pct(row['avg_mae_pct'])} | {row['sample_status']} |"
        )
    summary_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    old = read_csv(SELL_PERFORMANCE_CSV)
    if not old.empty and "stock_id" in old.columns:
        old = old[~code_matches(old["stock_id"], stock_id)]
    combined = pd.concat([old, summary], ignore_index=True, sort=False) if not old.empty else summary
    combined.to_csv(SELL_PERFORMANCE_CSV, index=False, encoding="utf-8", lineterminator="\n")
    latest_lines = [
        "# Sell Strategy Performance Latest",
        "",
        f"- generated_at: {now_text()}",
        "- note: 這是賣出規則回測資料，不是買賣建議。",
        "",
        "| stock_id | stock_name | strategy | sample | avg_return | win_rate | status |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for _, row in combined.tail(80).iterrows():
        latest_lines.append(
            f"| {row.get('stock_id', '')} | {row.get('stock_name', '')} | {row.get('strategy_name', '')} | {row.get('sample_count', '')} | {fmt_pct(row.get('avg_return_pct'))} | {fmt_pct(row.get('win_rate_pct'))} | {row.get('sample_status', '')} |"
        )
    SELL_PERFORMANCE_MD.write_text("\n".join(latest_lines) + "\n", encoding="utf-8")
    return {
        "detail_path": detail_path.as_posix(),
        "summary_path": summary_path.as_posix(),
        "latest_performance_csv": SELL_PERFORMANCE_CSV.as_posix(),
        "latest_performance_md": SELL_PERFORMANCE_MD.as_posix(),
    }


def sell_framework_markdown(framework: dict[str, Any]) -> str:
    lines = [
        "## 買入後的賣出 / 停利初步框架",
        "",
        f"> {framework.get('strategy_assumption', '以下為策略假設，不是保證價格，也不是投資建議。')}",
        "",
        "### 初步停利區",
        "",
        f"- 第一停利區：{framework.get('first_take_profit_zone', '資料不足')}",
        f"- 第二停利區：{framework.get('second_take_profit_zone', '資料不足')}",
        f"- 強勢續抱條件：{framework.get('strong_hold_conditions', '-')}",
        f"- 券商目標價：{framework.get('broker_target_price_note', '無可用券商目標價資料。')}",
        "",
        "### 風險退出條件",
        "",
        f"- 技術退出：{framework.get('technical_exit', '-')}",
        f"- 籌碼退出：{framework.get('tdcc_exit', '-')}",
        f"- 法人 / 主力退出：{framework.get('institutional_exit', '-')}",
        f"- 權證退出：{framework.get('warrant_exit', '-')}",
        f"- 基本面退出：{framework.get('fundamental_exit', '-')}",
        "",
        "### 初步結論",
        "",
        f"- 建議停利方式：{framework.get('suggested_exit_style', '-')}",
        f"- 停利參考區：{framework.get('take_profit_reference', '-')}",
        f"- 失敗退出點：{framework.get('failure_exit', '-')}",
        f"- 是否適合抱到目標價：{framework.get('hold_to_target_price', '-')}",
        f"- 最大風險：{framework.get('max_risk', '-')}",
        "",
    ]
    return "\n".join(lines)


def append_sell_framework_pdf_section(story: list[Any], style_map: dict[str, ParagraphStyle], framework: dict[str, Any]) -> None:
    story.append(paragraph("買入後的賣出 / 停利初步框架", style_map["h1"]))
    story.append(paragraph(framework.get("strategy_assumption", "以下為策略假設，不是保證價格，也不是投資建議。"), style_map["small"]))
    rows = [
        ["項目", "內容"],
        ["第一停利區", framework.get("first_take_profit_zone", "資料不足")],
        ["第二停利區", framework.get("second_take_profit_zone", "資料不足")],
        ["強勢續抱條件", framework.get("strong_hold_conditions", "-")],
        ["技術退出", framework.get("technical_exit", "-")],
        ["籌碼退出", framework.get("tdcc_exit", "-")],
        ["法人 / 主力退出", framework.get("institutional_exit", "-")],
        ["權證退出", framework.get("warrant_exit", "-")],
        ["基本面退出", framework.get("fundamental_exit", "-")],
        ["券商目標價", framework.get("broker_target_price_note", "無可用券商目標價資料。")],
        ["建議停利方式", framework.get("suggested_exit_style", "-")],
        ["停利參考區", framework.get("take_profit_reference", "-")],
        ["失敗退出點", framework.get("failure_exit", "-")],
        ["是否適合抱到目標價", framework.get("hold_to_target_price", "-")],
        ["最大風險", framework.get("max_risk", "-")],
    ]
    story.append(pdf_table(rows, [4.0 * cm, 13.5 * cm], style_map))


def plot_price_chart(df: pd.DataFrame, stock_id: str, stock_name: str, days: int, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if df.empty:
        return
    data = add_price_indicators(df).tail(days).copy()
    data["x"] = range(len(data))

    fig, (ax_price, ax_vol) = plt.subplots(
        2,
        1,
        figsize=(10, 6),
        dpi=150,
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 1]},
    )
    ax_price.plot(data["x"], data["close"], color="#1f77b4", linewidth=1.6, label="Close")
    for col, color, label in [
        ("ma20", "#ff7f0e", "MA20"),
        ("ma60", "#2ca02c", "MA60"),
        ("ema23", "#9467bd", "EMA23"),
    ]:
        if col in data.columns and data[col].notna().any():
            ax_price.plot(data["x"], data[col], color=color, linewidth=1.0, label=label)
    high_60 = safe_float(data.tail(min(60, len(data)))["high"].max())
    if not math.isnan(high_60):
        ax_price.axhline(high_60, color="#d62728", linewidth=0.9, linestyle="--", alpha=0.7, label="60D High")
    ax_price.set_title(f"{stock_id} - {min(days, len(data))}D Price", fontsize=12, weight="bold")
    ax_price.grid(True, alpha=0.25)
    ax_price.legend(loc="upper left", fontsize=8)

    colors_vol = ["#d9534f" if c >= o else "#2ca02c" for c, o in zip(data["close"], data["open"])]
    ax_vol.bar(data["x"], data["volume"], color=colors_vol, alpha=0.65, width=0.8)
    ax_vol.yaxis.set_major_formatter(FuncFormatter(lambda x, _pos: f"{x/1000:.0f}k"))
    ax_vol.grid(True, axis="y", alpha=0.25)
    ax_vol.set_ylabel("Volume")

    tick_count = min(8, len(data))
    if tick_count > 0:
        tick_positions = [round(i * (len(data) - 1) / max(1, tick_count - 1)) for i in range(tick_count)]
        ax_vol.set_xticks(tick_positions)
        ax_vol.set_xticklabels([safe_str(data["date"].iloc[i]) for i in tick_positions], rotation=35, ha="right")

    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def register_font() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def styles() -> dict[str, ParagraphStyle]:
    font = register_font()
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName=font,
            fontSize=21,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1D3557"),
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName=font,
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#44546A"),
            spaceAfter=8,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName=font,
            fontSize=15,
            leading=21,
            textColor=colors.HexColor("#1D3557"),
            spaceBefore=10,
            spaceAfter=7,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName=font,
            fontSize=12,
            leading=17,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=7,
            spaceAfter=5,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName=font,
            fontSize=10,
            leading=14.5,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName=font,
            fontSize=8.2,
            leading=11,
            spaceAfter=3,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            parent=base["Normal"],
            fontName=font,
            fontSize=8,
            leading=10,
            alignment=TA_CENTER,
            textColor=colors.white,
        ),
        "table_cell": ParagraphStyle(
            "table_cell",
            parent=base["Normal"],
            fontName=font,
            fontSize=8,
            leading=10,
            alignment=TA_LEFT,
        ),
    }


def paragraph(text: Any, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(clean_text(text)), style)


def pdf_table(rows: list[list[Any]], widths: list[float], style_map: dict[str, ParagraphStyle]) -> Table:
    wrapped: list[list[Any]] = []
    for ridx, row in enumerate(rows):
        wrapped.append([
            paragraph(cell, style_map["table_header" if ridx == 0 else "table_cell"])
            for cell in row
        ])
    table = Table(wrapped, colWidths=widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1D3557")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C9D3DF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#FAFBFC")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {clean_text(item)}" for item in items if clean_text(item))


def format_bool(value: Any) -> str:
    text = safe_str(value).lower()
    if text in {"true", "1", "yes"}:
        return "True"
    if text in {"false", "0", "no"}:
        return "False"
    return "-"


def tdcc_panel_table_rows(panel: pd.DataFrame, limit: int = 12) -> list[list[str]]:
    rows = [[
        "as_of_date",
        ">400",
        ">600",
        ">800",
        ">1000",
        "chg400",
        "chg800",
        "chg1000",
        "up_wks",
        "ret_1w",
        "ret_2w",
        "rel_2w",
        "phase",
    ]]
    if panel.empty:
        return rows
    for _, row in panel.tail(limit).iterrows():
        rows.append(
            [
                safe_str(row.get("as_of_date")),
                fmt_num(row.get("over_400_ratio")),
                fmt_num(row.get("over_600_ratio")),
                fmt_num(row.get("over_800_ratio")),
                fmt_num(row.get("over_1000_ratio")),
                fmt_num(row.get("over_400_change_1w")),
                fmt_num(row.get("over_800_change_1w")),
                fmt_num(row.get("over_1000_change_1w")),
                fmt_num(row.get("tdcc_consecutive_up_weeks"), 0),
                fmt_pct(row.get("price_ret_1w")),
                fmt_pct(row.get("price_ret_2w")),
                fmt_pct(row.get("relative_ret_2w")),
                safe_str(row.get("tdcc_price_phase")) or "-",
            ]
        )
    return rows


def latest_tdcc_weeks(latest: Any) -> float:
    if latest is None:
        return math.nan
    return safe_float(latest.get("tdcc_consecutive_up_weeks"))


def tdcc_history_markdown(analysis: dict[str, Any], tdcc_chart_path: Path | None) -> str:
    panel: pd.DataFrame = analysis.get("panel", pd.DataFrame())
    status: dict[str, Any] = analysis.get("status", {})
    latest = analysis.get("latest")
    backtest: pd.DataFrame = analysis.get("backtest", pd.DataFrame())
    latest_phase = analysis.get("phase", "insufficient_tdcc_history")
    weeks = latest_tdcc_weeks(latest)
    lines = [
        "## TDCC 歷史籌碼 × 股價反應分析",
        "",
        "### 資料狀態",
        "",
        f"- TDCC history 可用週數：`{status.get('tdcc_history_weeks', 0)}`",
        f"- 最新 TDCC 日期：`{status.get('latest_tdcc_date', '-')}`",
        f"- 連續 2 週 / 3 週資料：`{format_bool(not math.isnan(weeks) and weeks >= 2)} / {format_bool(not math.isnan(weeks) and weeks >= 3)}`",
        f"- 價格資料對齊：`{format_bool(status.get('price_aligned'))}`",
        f"- benchmark 可用：`{format_bool(status.get('benchmark_available'))}`",
        f"- TDCC-price phase：`{latest_phase}`",
    ]
    if status.get("insufficient_tdcc_history"):
        lines.append("- 狀態：`insufficient_tdcc_history`，TDCC 週資料不足，不能硬下結論。")
    if tdcc_chart_path and tdcc_chart_path.exists():
        lines.extend(["", f"![TDCC history]({tdcc_chart_path.as_posix()})"])
    else:
        lines.extend(["", "TDCC history 資料不足，未產生 TDCC 時序圖。"])

    table_rows = tdcc_panel_table_rows(panel, 12)
    lines.extend(["", "### 最近 8～12 週 TDCC 時序表", ""])
    lines.append("| " + " | ".join(table_rows[0]) + " |")
    lines.append("| " + " | ".join(["---"] * len(table_rows[0])) + " |")
    if len(table_rows) > 1:
        for row in table_rows[1:]:
            lines.append("| " + " | ".join(row) + " |")
    else:
        lines.append("| - | - | - | - | - | - | - | - | - | - | - | - | insufficient_tdcc_history |")

    lines.extend(["", "### TDCC 趨勢判讀", ""])
    if latest is None:
        lines.append("- TDCC history 不足，無法判斷連續增加、同步增加或股價反應。")
    else:
        lines.extend(
            [
                f"- 大戶是否連續增加：`{fmt_num(latest.get('tdcc_consecutive_up_weeks'), 0)}` 週。",
                f"- >800 / >1000 高級距同步增加：`{format_bool(latest.get('high_thresholds_up'))}`。",
                f"- 四級距同步增加：`{format_bool(latest.get('four_thresholds_sync_up'))}`。",
                f"- 散戶比例是否下降：`{'NA' if not safe_str(latest.get('retail_ratio_change_1w')) else fmt_num(latest.get('retail_ratio_change_1w'))}`。",
                f"- 股東人數是否下降或上升：`{'NA' if not safe_str(latest.get('total_shareholders_change_1w')) else fmt_num(latest.get('total_shareholders_change_1w'))}`。",
                f"- 是否出現集中化：`{format_bool(not math.isnan(weeks) and weeks >= 2 and str(latest.get('high_thresholds_up')).lower() == 'true')}`。",
                f"- 股價反應階段：`{analysis.get('price_reaction_stage', '-')}`。",
            ]
        )

    lines.extend(["", "### 該股歷史類似型態回測", ""])
    if backtest.empty:
        lines.append("- `insufficient_sample`")
    else:
        row = backtest.iloc[0]
        lines.extend(
            [
                f"- phase：`{safe_str(row.get('phase'))}`",
                f"- sample_count：`{safe_str(row.get('sample_count'))}` / sample_status：`{safe_str(row.get('sample_status'))}`",
                f"- avg_ret_d5 / d10 / d20：{fmt_pct(row.get('avg_ret_d5'))} / {fmt_pct(row.get('avg_ret_d10'))} / {fmt_pct(row.get('avg_ret_d20'))}",
                f"- win_rate_d10：{fmt_pct(row.get('win_rate_d10'))}",
                f"- avg_relative_ret_d10：{fmt_pct(row.get('avg_relative_ret_d10'))}",
                f"- MFE_D10 / MAE_D10：{fmt_pct(row.get('avg_mfe_d10'))} / {fmt_pct(row.get('avg_mae_d10'))}",
            ]
        )

    lines.extend(
        [
            "",
            "### 結論",
            "",
            f"- TDCC 支持度：{analysis.get('tdcc_support', '資料不足')}",
            f"- 股價反應階段：{analysis.get('price_reaction_stage', '資料不足')}",
            f"- 是否符合潛伏吸籌：{analysis.get('is_quiet_accumulation', '樣本不足')}",
            f"- 是否可視為加分因子：{analysis.get('is_positive_factor', '只能觀察')}",
            f"- 主要風險：{' / '.join(analysis.get('main_risks', []))}",
        ]
    )
    return "\n".join(lines)


def append_tdcc_history_pdf_section(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    analysis: dict[str, Any],
    tdcc_chart_path: Path | None,
) -> None:
    panel: pd.DataFrame = analysis.get("panel", pd.DataFrame())
    status: dict[str, Any] = analysis.get("status", {})
    latest = analysis.get("latest")
    backtest: pd.DataFrame = analysis.get("backtest", pd.DataFrame())
    weeks = latest_tdcc_weeks(latest)
    story.append(paragraph("TDCC 歷史籌碼 × 股價反應分析", style_map["h1"]))
    status_rows = [
        ["項目", "內容"],
        ["TDCC history 可用週數", status.get("tdcc_history_weeks", 0)],
        ["最新 TDCC 日期", status.get("latest_tdcc_date", "-")],
        ["連續 2/3 週資料", f"{format_bool(not math.isnan(weeks) and weeks >= 2)} / {format_bool(not math.isnan(weeks) and weeks >= 3)}"],
        ["價格資料對齊", format_bool(status.get("price_aligned"))],
        ["benchmark 可用", format_bool(status.get("benchmark_available"))],
        ["TDCC-price phase", analysis.get("phase", "insufficient_tdcc_history")],
    ]
    story.append(pdf_table(status_rows, [4.3 * cm, 13.2 * cm], style_map))
    story.append(Spacer(1, 0.15 * cm))
    if tdcc_chart_path and tdcc_chart_path.exists():
        story.append(PdfImage(str(tdcc_chart_path), width=17.2 * cm, height=8.8 * cm))
        story.append(Spacer(1, 0.15 * cm))
    else:
        story.append(paragraph("TDCC history 資料不足，未產生 TDCC 時序圖。", style_map["normal"]))

    rows = tdcc_panel_table_rows(panel, 10)
    if len(rows) > 1:
        story.append(paragraph("最近 8～12 週 TDCC 時序表", style_map["h2"]))
        story.append(pdf_table(rows, [1.65 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 0.9 * cm, 1.2 * cm, 1.2 * cm, 1.2 * cm, 3.0 * cm], style_map))

    story.append(paragraph("TDCC 趨勢判讀", style_map["h2"]))
    if latest is None:
        trend_text = "TDCC history 不足，無法判斷連續增加、同步增加或股價反應。"
    else:
        trend_text = (
            f"連續增加 {fmt_num(latest.get('tdcc_consecutive_up_weeks'), 0)} 週；"
            f"高級距同步增加={format_bool(latest.get('high_thresholds_up'))}；"
            f"四級距同步增加={format_bool(latest.get('four_thresholds_sync_up'))}；"
            f"股價反應階段={analysis.get('price_reaction_stage', '-')}。"
        )
    story.append(paragraph(trend_text, style_map["normal"]))

    story.append(paragraph("該股歷史類似型態回測", style_map["h2"]))
    if backtest.empty:
        story.append(paragraph("insufficient_sample", style_map["normal"]))
    else:
        row = backtest.iloc[0]
        backtest_rows = [
            ["phase", "sample", "avg D5/D10/D20", "win D10", "rel D10", "MFE/MAE D10"],
            [
                row.get("phase", "-"),
                f"{row.get('sample_count', 0)} / {row.get('sample_status', '-')}",
                f"{fmt_pct(row.get('avg_ret_d5'))} / {fmt_pct(row.get('avg_ret_d10'))} / {fmt_pct(row.get('avg_ret_d20'))}",
                fmt_pct(row.get("win_rate_d10")),
                fmt_pct(row.get("avg_relative_ret_d10")),
                f"{fmt_pct(row.get('avg_mfe_d10'))} / {fmt_pct(row.get('avg_mae_d10'))}",
            ],
        ]
        story.append(pdf_table(backtest_rows, [3.0 * cm, 2.6 * cm, 4.0 * cm, 2.2 * cm, 2.4 * cm, 3.3 * cm], style_map))

    conclusion_rows = [
        ["結論項目", "判斷"],
        ["TDCC 支持度", analysis.get("tdcc_support", "資料不足")],
        ["股價反應階段", analysis.get("price_reaction_stage", "資料不足")],
        ["是否符合潛伏吸籌", analysis.get("is_quiet_accumulation", "樣本不足")],
        ["是否可視為加分因子", analysis.get("is_positive_factor", "只能觀察")],
        ["主要風險", " / ".join(analysis.get("main_risks", []))],
    ]
    story.append(pdf_table(conclusion_rows, [4.0 * cm, 13.5 * cm], style_map))


def build_markdown(
    stock_id: str,
    stock_name: str,
    days: int,
    freshness: dict[str, str],
    main_date: str,
    price_metrics: dict[str, Any],
    candidate_intro: str,
    candidate_items: list[dict[str, str]],
    revenue: dict[str, str],
    tdcc: dict[str, str],
    warrant: dict[str, str],
    priority: str,
    risks: list[str],
    chart_path: Path,
    tdcc_history: dict[str, Any],
    tdcc_chart_path: Path | None,
    sell_framework: dict[str, Any],
    paths: ReportPaths,
) -> str:
    page_pdf_url = pages_url(paths.docs_pdf)
    raw_pdf_url = raw_url(paths.latest_pdf)
    lines = [
        f"# 個股分析報告 - {stock_id} {stock_name}",
        "",
        f"- 產生時間：`{now_text()}`",
        f"- 主資料日期：`{main_date}`",
        f"- 分析天數：`{days}`",
        f"- 報告狀態：`generated`",
        f"- PDF Pages URL：{page_pdf_url}",
        f"- PDF Raw URL：{raw_pdf_url}",
        "",
        "## 一、資料狀態",
        "",
        f"- report_ready：`{freshness.get('report_ready', '-')}`",
        f"- 日價資料：`{price_metrics.get('available_days', 0)}` 筆，最新日期 `{price_metrics.get('latest_date', '-')}`",
        f"- 候選分類狀態：{candidate_intro}",
        f"- TDCC：{tdcc['signal']} / {tdcc['status']}",
        f"- 權證：{warrant['signal']} / {warrant['status']}",
        "",
        "## 二、個股總結",
        "",
        f"- 綜合優先度：**{priority}**",
        f"- 價格狀態：{price_metrics.get('price_state', '-')}",
        "- 本報告只依公開市場資料與系統訊號分析，非買賣建議。",
        "",
        "## 三、價格與型態",
        "",
        f"![{stock_id} price chart]({chart_path.as_posix()})",
        "",
        "| 指標 | 數值 |",
        "|---|---:|",
        f"| 收盤價 | {fmt_num(price_metrics.get('close'))} |",
        f"| 1日 / 5日 / 20日 | {fmt_pct(price_metrics.get('return_1d'))} / {fmt_pct(price_metrics.get('return_5d'))} / {fmt_pct(price_metrics.get('return_20d'))} |",
        f"| 60日 / 120日 | {fmt_pct(price_metrics.get('return_60d'))} / {fmt_pct(price_metrics.get('return_120d'))} |",
        f"| 20MA / 60MA / 23EMA | {fmt_num(price_metrics.get('ma20'))} / {fmt_num(price_metrics.get('ma60'))} / {fmt_num(price_metrics.get('ema23'))} |",
        f"| 距 60 日高點 | {fmt_pct(price_metrics.get('distance_high_60'))} |",
        f"| 量比 | {fmt_num(price_metrics.get('volume_ratio'), 2)}x |",
        "",
        "## 四、候選分類訊號",
        "",
    ]
    if candidate_items:
        lines.extend(["| 分類 | 分數 / 排名 / priority | TDCC | 權證 | 精簡理由 |", "|---|---|---|---|---|"])
        for item in candidate_items:
            lines.append(
                f"| {item['category']} | {item['score_rank']} | {item['tdcc']} | {item['warrant']} | {item['note']} |"
            )
    else:
        lines.append(candidate_intro)

    lines.extend(
        [
            "",
            "## 五、營收判斷",
            "",
            f"- 狀態：{revenue['status']}",
            f"- 單月 YoY：{revenue['latest_yoy']}",
            f"- 累計 YoY：{revenue['cumulative_yoy']}",
            f"- 說明：{revenue['note']}",
            "",
            "## 六、TDCC 判斷",
            "",
            f"- 訊號：{tdcc['signal']}",
            f"- 判讀：{tdcc['status']}",
            f"- 400 張以上：{tdcc['over_400']}",
            f"- 1000 張以上：{tdcc['over_1000']}",
            f"- 說明：{tdcc['note']}",
            "",
            "## 七、權證判斷",
            "",
            f"- 日期：{warrant['date']}",
            f"- 訊號：{warrant['signal']}",
            f"- 分數：{warrant['score']}",
            f"- 判讀：{warrant['status']}",
            f"- 說明：{warrant['note']}",
            "",
            "## 八、風險提醒",
            "",
            bullet_list(risks),
            "",
            tdcc_history_markdown(tdcc_history, tdcc_chart_path),
            "",
            sell_framework_markdown(sell_framework),
            "",
            "## 九、明日觀察條件",
            "",
            bullet_list(price_metrics.get("confirmation", [])),
            "",
        ]
    )
    return "\n".join(lines)


def build_pdf(
    stock_id: str,
    stock_name: str,
    days: int,
    freshness: dict[str, str],
    main_date: str,
    price_metrics: dict[str, Any],
    candidate_intro: str,
    candidate_items: list[dict[str, str]],
    revenue: dict[str, str],
    tdcc: dict[str, str],
    warrant: dict[str, str],
    priority: str,
    risks: list[str],
    chart_path: Path,
    tdcc_history: dict[str, Any],
    tdcc_chart_path: Path | None,
    sell_framework: dict[str, Any],
    path: Path,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    style_map = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        rightMargin=1.25 * cm,
        leftMargin=1.25 * cm,
        topMargin=1.15 * cm,
        bottomMargin=1.1 * cm,
        title=f"{stock_id} {stock_name} individual stock report",
    )
    story: list[Any] = []
    story.append(paragraph(f"個股分析報告 - {stock_id} {stock_name}", style_map["title"]))
    story.append(paragraph(f"主資料日期 {main_date}｜產生時間 {now_text()}｜分析天數 {days}", style_map["subtitle"]))
    story.append(paragraph(f"綜合優先度：{priority}", style_map["h1"]))
    story.append(paragraph(price_metrics.get("price_state", "-"), style_map["normal"]))
    story.append(paragraph("本報告只依公開市場資料與系統訊號分析，非買賣建議。", style_map["small"]))

    story.append(paragraph("一、資料狀態", style_map["h1"]))
    status_rows = [
        ["項目", "狀態"],
        ["report_ready", freshness.get("report_ready", "-")],
        ["日價資料", f"{price_metrics.get('available_days', 0)} 筆，最新日期 {price_metrics.get('latest_date', '-')}"],
        ["候選分類", candidate_intro],
        ["TDCC", f"{tdcc['signal']} / {tdcc['status']}"],
        ["權證", f"{warrant['signal']} / {warrant['status']}"],
    ]
    story.append(pdf_table(status_rows, [3.0 * cm, 14.5 * cm], style_map))
    story.append(Spacer(1, 0.2 * cm))

    story.append(paragraph("二、價格與型態", style_map["h1"]))
    if chart_path.exists():
        story.append(PdfImage(str(chart_path), width=17.2 * cm, height=10.2 * cm))
        story.append(Spacer(1, 0.15 * cm))
    price_rows = [
        ["指標", "數值", "指標", "數值"],
        ["收盤價", fmt_num(price_metrics.get("close")), "量比", f"{fmt_num(price_metrics.get('volume_ratio'), 2)}x"],
        ["1日 / 5日", f"{fmt_pct(price_metrics.get('return_1d'))} / {fmt_pct(price_metrics.get('return_5d'))}", "20日 / 60日", f"{fmt_pct(price_metrics.get('return_20d'))} / {fmt_pct(price_metrics.get('return_60d'))}"],
        ["20MA / 60MA", f"{fmt_num(price_metrics.get('ma20'))} / {fmt_num(price_metrics.get('ma60'))}", "23EMA", fmt_num(price_metrics.get("ema23"))],
        ["距20MA / 距60MA", f"{fmt_pct(price_metrics.get('distance_ma20'))} / {fmt_pct(price_metrics.get('distance_ma60'))}", "距60日高點", fmt_pct(price_metrics.get("distance_high_60"))],
    ]
    story.append(pdf_table(price_rows, [3.2 * cm, 5.6 * cm, 3.2 * cm, 5.5 * cm], style_map))

    story.append(paragraph("三、候選分類訊號", style_map["h1"]))
    if candidate_items:
        rows = [["分類", "分數 / 排名 / priority", "TDCC", "權證", "精簡理由"]]
        rows.extend([[i["category"], i["score_rank"], i["tdcc"], i["warrant"], i["note"]] for i in candidate_items])
        story.append(pdf_table(rows, [3.3 * cm, 3.2 * cm, 2.5 * cm, 2.5 * cm, 6.0 * cm], style_map))
    else:
        story.append(paragraph(candidate_intro, style_map["normal"]))

    story.append(PageBreak())
    story.append(paragraph("四、營收判斷", style_map["h1"]))
    revenue_rows = [
        ["項目", "內容"],
        ["狀態", revenue["status"]],
        ["單月 YoY", revenue["latest_yoy"]],
        ["累計 YoY", revenue["cumulative_yoy"]],
        ["說明", revenue["note"]],
    ]
    story.append(pdf_table(revenue_rows, [3.0 * cm, 14.5 * cm], style_map))

    story.append(paragraph("五、TDCC 判斷", style_map["h1"]))
    tdcc_rows = [
        ["項目", "內容"],
        ["訊號", tdcc["signal"]],
        ["判讀", tdcc["status"]],
        ["400 張以上", tdcc["over_400"]],
        ["1000 張以上", tdcc["over_1000"]],
        ["說明", tdcc["note"]],
    ]
    story.append(pdf_table(tdcc_rows, [3.0 * cm, 14.5 * cm], style_map))

    story.append(paragraph("六、權證判斷", style_map["h1"]))
    warrant_rows = [
        ["項目", "內容"],
        ["日期", warrant["date"]],
        ["訊號 / 分數", f"{warrant['signal']} / {warrant['score']}"],
        ["判讀", warrant["status"]],
        ["說明", warrant["note"]],
    ]
    story.append(pdf_table(warrant_rows, [3.0 * cm, 14.5 * cm], style_map))

    story.append(paragraph("七、風險提醒", style_map["h1"]))
    for item in risks:
        story.append(paragraph(f"- {item}", style_map["normal"]))

    append_tdcc_history_pdf_section(story, style_map, tdcc_history, tdcc_chart_path)
    append_sell_framework_pdf_section(story, style_map, sell_framework)

    story.append(paragraph("八、明日觀察條件", style_map["h1"]))
    for item in price_metrics.get("confirmation", []):
        story.append(paragraph(f"- {item}", style_map["normal"]))

    doc.build(story)


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    elif path.as_posix().startswith("output/latest/"):
        rel = path.relative_to("output").as_posix()
    else:
        rel = path.as_posix()
    return f"{PAGES_PREFIX}/{rel}"


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def make_paths(stock_id: str, main_date: str) -> ReportPaths:
    latest_stem = f"{stock_id}_latest"
    history_stem = f"{main_date}_{stock_id}"
    return ReportPaths(
        latest_md=INDIVIDUAL_LATEST_DIR / f"{latest_stem}.md",
        latest_pdf=INDIVIDUAL_LATEST_DIR / f"{latest_stem}.pdf",
        latest_png=INDIVIDUAL_LATEST_DIR / f"{latest_stem}.png",
        latest_json=INDIVIDUAL_LATEST_DIR / f"{latest_stem}.json",
        docs_md=DOCS_INDIVIDUAL_DIR / f"{latest_stem}.md",
        docs_pdf=DOCS_INDIVIDUAL_DIR / f"{latest_stem}.pdf",
        docs_png=DOCS_INDIVIDUAL_DIR / f"{latest_stem}.png",
        docs_json=DOCS_INDIVIDUAL_DIR / f"{latest_stem}.json",
        history_md=HISTORY_DIR / f"{history_stem}.md",
        history_pdf=HISTORY_DIR / f"{history_stem}.pdf",
        history_png=HISTORY_DIR / f"{history_stem}.png",
        history_json=HISTORY_DIR / f"{history_stem}.json",
    )


def copy_outputs(paths: ReportPaths) -> None:
    for path in [
        paths.docs_md,
        paths.docs_pdf,
        paths.docs_png,
        paths.docs_json,
        paths.history_md,
        paths.history_pdf,
        paths.history_png,
        paths.history_json,
    ]:
        path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(paths.latest_md, paths.docs_md)
    shutil.copyfile(paths.latest_pdf, paths.docs_pdf)
    shutil.copyfile(paths.latest_png, paths.docs_png)
    shutil.copyfile(paths.latest_json, paths.docs_json)
    shutil.copyfile(paths.latest_md, paths.history_md)
    shutil.copyfile(paths.latest_pdf, paths.history_pdf)
    shutil.copyfile(paths.latest_png, paths.history_png)
    shutil.copyfile(paths.latest_json, paths.history_json)


def write_manifest(
    paths: ReportPaths,
    stock_id: str,
    stock_name: str,
    main_date: str,
    days: int,
    price_metrics: dict[str, Any],
    priority: str,
    tdcc_history: dict[str, Any] | None = None,
    tdcc_chart_path: Path | None = None,
    sell_outputs: dict[str, str] | None = None,
) -> None:
    tdcc_history = tdcc_history or {}
    sell_outputs = sell_outputs or {}
    tdcc_status = tdcc_history.get("status", {})
    manifest = {
        "generated_at": now_text(),
        "status": "generated",
        "stock_id": stock_id,
        "stock_name": stock_name,
        "main_price_date": main_date,
        "analysis_days": days,
        "available_price_days": price_metrics.get("available_days", 0),
        "priority": priority,
        "latest_md_path": paths.latest_md.as_posix(),
        "latest_pdf_path": paths.latest_pdf.as_posix(),
        "latest_chart_path": paths.latest_png.as_posix(),
        "pages_md_url": pages_url(paths.docs_md),
        "pages_pdf_url": pages_url(paths.docs_pdf),
        "pages_chart_url": pages_url(paths.docs_png),
        "raw_md_url": raw_url(paths.latest_md),
        "raw_pdf_url": raw_url(paths.latest_pdf),
        "raw_chart_url": raw_url(paths.latest_png),
        "tdcc_history_source": tdcc_status.get("source", ""),
        "tdcc_history_weeks": tdcc_status.get("tdcc_history_weeks", 0),
        "tdcc_price_phase": tdcc_history.get("phase", ""),
        "tdcc_history_chart_path": tdcc_chart_path.as_posix() if tdcc_chart_path and tdcc_chart_path.exists() else "",
        "tdcc_history_chart_raw_url": raw_url(tdcc_chart_path) if tdcc_chart_path and tdcc_chart_path.exists() else "",
        "sell_strategy_backtest_path": sell_outputs.get("detail_path", ""),
        "sell_strategy_summary_path": sell_outputs.get("summary_path", ""),
        "sell_strategy_performance_latest_csv": sell_outputs.get("latest_performance_csv", ""),
        "sell_strategy_performance_latest_md": sell_outputs.get("latest_performance_md", ""),
        "history_md_path": paths.history_md.as_posix(),
        "history_pdf_path": paths.history_pdf.as_posix(),
    }
    paths.latest_json.parent.mkdir(parents=True, exist_ok=True)
    paths.latest_json.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def generate(stock_id_input: str, days: int) -> ReportPaths:
    stock_id = normalize_stock_id(stock_id_input)
    if not stock_id:
        raise SystemExit("stock_id is required")
    days = max(60, min(int(days), 260))

    freshness = load_freshness()
    price_history = load_price_history(stock_id)
    if price_history.empty:
        raise SystemExit(f"No daily price data found for stock_id={stock_id}")

    price_metrics = summarize_price(price_history)
    main_date = main_price_date(freshness, price_history)
    candidate_rows = load_candidate_rows(stock_id)
    warrant_row = load_warrant_row(stock_id)
    tdcc_raw = load_tdcc_info(stock_id)
    stock_name = infer_stock_name(stock_id, price_metrics, candidate_rows, warrant_row, tdcc_raw)

    candidate_intro, candidate_items = candidate_summary(candidate_rows)
    revenue = revenue_summary(candidate_rows)
    tdcc = tdcc_summary(tdcc_raw, candidate_rows)
    warrant = warrant_summary(warrant_row)
    priority = overall_priority(price_metrics, candidate_rows, tdcc, warrant)
    risks = build_risks(price_metrics, tdcc, warrant, candidate_rows)
    tdcc_history = tdcc_history_analysis(stock_id)
    sell_framework = build_sell_framework(
        stock_id=stock_id,
        stock_name=stock_name,
        price_history=price_history,
        price_metrics=price_metrics,
        candidate_rows=candidate_rows,
        tdcc_info=tdcc,
        warrant_info=warrant,
    )
    sell_outputs = write_sell_strategy_outputs(stock_id, stock_name, main_date, price_history, sell_framework)
    paths = make_paths(stock_id, main_date)
    tdcc_chart_path = LATEST_CHART_DIR / f"{stock_id}_tdcc_history.png"

    for path in [paths.latest_md, paths.latest_pdf, paths.latest_png, paths.latest_json]:
        path.parent.mkdir(parents=True, exist_ok=True)

    plot_price_chart(price_history, stock_id, stock_name, days, paths.latest_png)
    tdcc_chart_created = plot_tdcc_history_chart(
        stock_id,
        stock_name,
        tdcc_history.get("panel", pd.DataFrame()),
        tdcc_chart_path,
    )
    if not tdcc_chart_created and tdcc_chart_path.exists():
        tdcc_chart_path.unlink()
    md = build_markdown(
        stock_id=stock_id,
        stock_name=stock_name,
        days=days,
        freshness=freshness,
        main_date=main_date,
        price_metrics=price_metrics,
        candidate_intro=candidate_intro,
        candidate_items=candidate_items,
        revenue=revenue,
        tdcc=tdcc,
        warrant=warrant,
        priority=priority,
        risks=risks,
        chart_path=paths.latest_png,
        tdcc_history=tdcc_history,
        tdcc_chart_path=tdcc_chart_path if tdcc_chart_created else None,
        sell_framework=sell_framework,
        paths=paths,
    )
    paths.latest_md.write_text(md, encoding="utf-8")
    build_pdf(
        stock_id=stock_id,
        stock_name=stock_name,
        days=days,
        freshness=freshness,
        main_date=main_date,
        price_metrics=price_metrics,
        candidate_intro=candidate_intro,
        candidate_items=candidate_items,
        revenue=revenue,
        tdcc=tdcc,
        warrant=warrant,
        priority=priority,
        risks=risks,
        chart_path=paths.latest_png,
        tdcc_history=tdcc_history,
        tdcc_chart_path=tdcc_chart_path if tdcc_chart_created else None,
        sell_framework=sell_framework,
        path=paths.latest_pdf,
    )
    write_manifest(
        paths,
        stock_id,
        stock_name,
        main_date,
        days,
        price_metrics,
        priority,
        tdcc_history=tdcc_history,
        tdcc_chart_path=tdcc_chart_path if tdcc_chart_created else None,
        sell_outputs=sell_outputs,
    )
    copy_outputs(paths)

    print(f"Saved: {paths.latest_md}")
    print(f"Saved: {paths.latest_pdf}")
    print(f"Saved: {paths.latest_png}")
    print(f"Pages PDF: {pages_url(paths.docs_pdf)}")
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a fixed-format individual stock analysis report.")
    parser.add_argument("--stock-id", required=True, help="Taiwan stock id, for example 2353 or 2330.")
    parser.add_argument("--days", type=int, default=180, help="Price chart lookback days. Default: 180.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generate(args.stock_id, args.days)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
