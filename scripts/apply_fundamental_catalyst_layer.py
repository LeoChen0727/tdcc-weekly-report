from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import re

import pandas as pd


LATEST_DIR = Path("output/latest")
DATA_DIR = Path("data")
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
OUTPUT_MD = LATEST_DIR / "fundamental_catalyst_layer_latest.md"

FINANCIAL_SOURCE_FILES = [
    DATA_DIR / "fundamentals" / "quarterly_financials.csv",
    DATA_DIR / "fundamentals" / "eps_quarterly.csv",
    LATEST_DIR / "quarterly_financials_latest.csv",
    LATEST_DIR / "fundamental_catalyst_source_latest.csv",
]

EVENT_SOURCE_FILES = [
    DATA_DIR / "events" / "catalyst_events.csv",
    DATA_DIR / "events" / "material_events.csv",
    LATEST_DIR / "event_catalyst_source_latest.csv",
]

PRICE_HISTORY_DIR = DATA_DIR / "stock_price_history"

REVENUE_CATEGORIES = {"revenue_breakout_low_response", "revenue_pullback"}
CONSTRUCTION_RECOGNITION_TYPES = {"營建認列型", "交屋認列型"}
SUPPORTIVE_TDCC = {"strong_accumulation", "mild_accumulation"}

CATALYST_COLUMNS = [
    "fundamental_catalyst_score",
    "fundamental_catalyst_tags",
    "event_catalyst_tags",
    "pre_breakout_catalyst_flag",
    "similar_to_shihsinko_flag",
    "eps_surprise_flag",
    "earnings_acceleration_flag",
    "margin_improvement_flag",
    "profit_turnaround_flag",
    "undervalued_after_eps_flag",
    "revenue_good_eps_unconfirmed_flag",
    "theme_catalyst_flag",
    "theme_catalyst_tags",
    "catalyst_date",
    "catalyst_source",
    "catalyst_summary",
    "price_reaction_after_catalyst",
    "already_reacted_to_catalyst",
    "catalyst_quality",
    "catalyst_confidence",
    "price_return_1d_after_catalyst",
    "price_return_3d_after_catalyst",
    "price_return_5d_after_catalyst",
    "price_return_20d_after_catalyst",
    "volume_ratio_after_catalyst",
    "long_upper_shadow_after_catalyst",
    "gap_up_failed_after_catalyst",
    "low_reaction_after_catalyst",
    "catalyst_overheated",
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
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Za-z]", "", text)
    if text.isdigit():
        return text.zfill(4)
    return text


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return ""


def to_number(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "")
    if not text:
        return default
    try:
        return float(text)
    except Exception:
        return default


def truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y", "是"}


def bool_text(value: bool) -> str:
    return "True" if value else "False"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    for enc in ["utf-8-sig", "utf-8", "cp950"]:
        try:
            return pd.read_csv(path, dtype=str, keep_default_na=False, encoding=enc)
        except Exception:
            continue
    return pd.DataFrame()


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def write_xlsx(df: pd.DataFrame, path: Path) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all_candidates", index=False)
    except Exception as exc:
        print(f"WARNING: failed to write {path}: {exc}")


def first_value(row: pd.Series, names: list[str], default: str = "") -> str:
    for name in names:
        if name in row.index:
            value = safe_str(row.get(name, ""))
            if value:
                return value
    return default


def latest_by_stock(df: pd.DataFrame, date_columns: list[str]) -> pd.DataFrame:
    if df.empty:
        return df
    df = df.copy()
    code_col = next((c for c in ["stock_id", "code", "ticker"] if c in df.columns), "")
    if not code_col:
        return pd.DataFrame()
    df["stock_id"] = df[code_col].map(normalize_code)
    date_col = next((c for c in date_columns if c in df.columns), "")
    if date_col:
        df["_source_date"] = df[date_col].map(normalize_date)
        df = df.sort_values(["stock_id", "_source_date"])
    return df[df["stock_id"] != ""].drop_duplicates("stock_id", keep="last")


def load_source(paths: list[Path], date_columns: list[str]) -> tuple[pd.DataFrame, str]:
    for path in paths:
        df = read_csv(path)
        if not df.empty:
            return latest_by_stock(df, date_columns), path.as_posix()
    return pd.DataFrame(), ""


def load_price_history(stock_id: str) -> pd.DataFrame:
    path = PRICE_HISTORY_DIR / f"{normalize_code(stock_id)}.csv"
    df = read_csv(path)
    if df.empty or "date" not in df.columns:
        return pd.DataFrame()
    df = df.copy()
    df["date"] = df["date"].map(normalize_date)
    for col in ["open", "high", "low", "close", "volume", "volume_ratio"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df[df["date"] != ""].sort_values("date").reset_index(drop=True)


def return_after(price: pd.DataFrame, base_pos: int, horizon: int, base_close: float) -> str:
    target = base_pos + horizon
    if target >= len(price) or math.isnan(base_close) or base_close <= 0:
        return ""
    close_h = to_number(price.loc[target, "close"])
    if math.isnan(close_h):
        return ""
    return f"{(close_h / base_close - 1) * 100:.2f}"


def price_reaction(stock_id: str, catalyst_date: str, row: pd.Series) -> dict[str, str]:
    out = {
        "price_return_1d_after_catalyst": "",
        "price_return_3d_after_catalyst": "",
        "price_return_5d_after_catalyst": "",
        "price_return_20d_after_catalyst": "",
        "volume_ratio_after_catalyst": "",
        "long_upper_shadow_after_catalyst": "",
        "gap_up_failed_after_catalyst": "",
        "low_reaction_after_catalyst": "",
        "already_reacted_to_catalyst": "",
        "catalyst_overheated": "",
        "price_reaction_after_catalyst": "",
    }
    date = normalize_date(catalyst_date)
    if not date:
        ret_5d = to_number(first_value(row, ["return_5d", "return_5d_pct"]))
        ret_20d = to_number(first_value(row, ["return_20d", "return_20d_pct"]))
        volume_ratio = to_number(first_value(row, ["volume_ratio"]))
        already = truthy(first_value(row, ["already_priced_in"])) or ret_20d > 25
        overheated = ret_5d > 20 or ret_20d > 30 or (volume_ratio > 4 and ret_5d > 12)
        low_reaction = not already and not overheated and (math.isnan(ret_20d) or ret_20d <= 15)
        out["already_reacted_to_catalyst"] = bool_text(already)
        out["catalyst_overheated"] = bool_text(overheated)
        out["low_reaction_after_catalyst"] = bool_text(low_reaction)
        out["price_reaction_after_catalyst"] = "no_catalyst_date; use current price reaction fields"
        return out

    price = load_price_history(stock_id)
    if price.empty:
        out["price_reaction_after_catalyst"] = "price history unavailable"
        return out

    candidates = price[price["date"] <= date]
    if candidates.empty:
        out["price_reaction_after_catalyst"] = "no price row on or before catalyst_date"
        return out

    base_pos = int(candidates.index[-1])
    base_close = to_number(price.loc[base_pos, "close"])
    for horizon in [1, 3, 5, 20]:
        out[f"price_return_{horizon}d_after_catalyst"] = return_after(price, base_pos, horizon, base_close)

    window = price.iloc[base_pos + 1 : min(len(price), base_pos + 6)].copy()
    if not window.empty:
        if "volume_ratio" in window.columns and pd.to_numeric(window["volume_ratio"], errors="coerce").notna().any():
            out["volume_ratio_after_catalyst"] = f"{pd.to_numeric(window['volume_ratio'], errors='coerce').max():.2f}"
        long_upper = False
        for _, item in window.iterrows():
            high = to_number(item.get("high"))
            close = to_number(item.get("close"))
            open_ = to_number(item.get("open"))
            if not math.isnan(high) and not math.isnan(close) and close > 0 and (high - close) / close >= 0.06:
                long_upper = True
            if not math.isnan(open_) and not math.isnan(close) and not math.isnan(base_close):
                if open_ > base_close * 1.03 and close < open_:
                    out["gap_up_failed_after_catalyst"] = "True"
        out["long_upper_shadow_after_catalyst"] = bool_text(long_upper)
        if not out["gap_up_failed_after_catalyst"]:
            out["gap_up_failed_after_catalyst"] = "False"

    ret_1d = to_number(out["price_return_1d_after_catalyst"])
    ret_3d = to_number(out["price_return_3d_after_catalyst"])
    ret_5d = to_number(out["price_return_5d_after_catalyst"])
    ret_20d = to_number(out["price_return_20d_after_catalyst"])
    volume_ratio = to_number(out["volume_ratio_after_catalyst"])
    already = ret_5d > 15 or ret_20d > 25 or truthy(out["gap_up_failed_after_catalyst"]) or truthy(out["long_upper_shadow_after_catalyst"])
    overheated = ret_5d > 20 or ret_20d > 30 or (volume_ratio > 4 and ret_5d > 12)
    low_reaction = (
        (math.isnan(ret_1d) or ret_1d <= 5)
        and (math.isnan(ret_3d) or ret_3d <= 8)
        and (math.isnan(ret_5d) or ret_5d <= 10)
        and (math.isnan(ret_20d) or ret_20d <= 15)
        and not already
        and not overheated
    )
    out["already_reacted_to_catalyst"] = bool_text(already)
    out["catalyst_overheated"] = bool_text(overheated)
    out["low_reaction_after_catalyst"] = bool_text(low_reaction)
    out["price_reaction_after_catalyst"] = (
        f"1d={out['price_return_1d_after_catalyst'] or 'n/a'}%, "
        f"5d={out['price_return_5d_after_catalyst'] or 'n/a'}%, "
        f"20d={out['price_return_20d_after_catalyst'] or 'n/a'}%"
    )
    return out


def financial_flags(fin: pd.Series | None) -> dict[str, Any]:
    if fin is None:
        return {
            "has_financial_source": False,
            "eps_surprise_flag": False,
            "earnings_acceleration_flag": False,
            "margin_improvement_flag": False,
            "profit_turnaround_flag": False,
            "undervalued_after_eps_flag": False,
            "tags": [],
            "summary_parts": [],
            "date": "",
            "source": "",
        }

    eps = to_number(first_value(fin, ["eps", "latest_eps", "quarter_eps"]))
    eps_yoy = to_number(first_value(fin, ["eps_yoy_change", "eps_yoy", "eps_yoy_pct"]))
    eps_qoq = to_number(first_value(fin, ["eps_qoq_change", "eps_qoq", "eps_qoq_pct"]))
    eps_avg = to_number(first_value(fin, ["eps_4q_avg", "eps_last_4q_avg", "eps_four_quarter_avg"]))
    gross_yoy = to_number(first_value(fin, ["gross_margin_yoy_change", "gross_margin_yoy_diff"]))
    gross_qoq = to_number(first_value(fin, ["gross_margin_qoq_change", "gross_margin_qoq_diff"]))
    op_yoy = to_number(first_value(fin, ["operating_margin_yoy_change", "operating_margin_yoy_diff"]))
    op_qoq = to_number(first_value(fin, ["operating_margin_qoq_change", "operating_margin_qoq_diff"]))
    prior_eps = to_number(first_value(fin, ["previous_eps", "prior_quarter_eps", "last_year_same_quarter_eps"]))

    eps_surprise = (
        (not math.isnan(eps) and not math.isnan(eps_avg) and eps > eps_avg)
        or (not math.isnan(eps_yoy) and eps_yoy > 0 and not math.isnan(eps_qoq) and eps_qoq > 0)
    )
    earnings_accel = (
        (not math.isnan(eps_yoy) and eps_yoy > 0)
        and (not math.isnan(eps_qoq) and eps_qoq > 0)
    )
    margin_improve = any(value > 0.5 for value in [gross_yoy, gross_qoq, op_yoy, op_qoq] if not math.isnan(value))
    profit_turn = truthy(first_value(fin, ["profit_turnaround", "turnaround_flag"])) or (
        not math.isnan(prior_eps) and not math.isnan(eps) and prior_eps <= 0 < eps
    )

    tags: list[str] = []
    if eps_surprise:
        tags.append("EPS_surprise")
    if earnings_accel:
        tags.append("earnings_acceleration")
    if margin_improve:
        tags.append("margin_improvement")
    if profit_turn:
        tags.append("profit_turnaround")

    summary_parts: list[str] = []
    if not math.isnan(eps):
        summary_parts.append(f"EPS {eps:.2f}")
    if not math.isnan(eps_yoy):
        summary_parts.append(f"EPS YoY {eps_yoy:.2f}")
    if not math.isnan(eps_qoq):
        summary_parts.append(f"EPS QoQ {eps_qoq:.2f}")
    if margin_improve:
        summary_parts.append("margin improvement")
    if profit_turn:
        summary_parts.append("profit turnaround")

    return {
        "has_financial_source": True,
        "eps_surprise_flag": eps_surprise,
        "earnings_acceleration_flag": earnings_accel,
        "margin_improvement_flag": margin_improve,
        "profit_turnaround_flag": profit_turn,
        "undervalued_after_eps_flag": False,
        "tags": tags,
        "summary_parts": summary_parts,
        "date": normalize_date(first_value(fin, ["catalyst_date", "announcement_date", "release_date", "report_date", "quarter_date"])),
        "source": first_value(fin, ["catalyst_source", "source", "source_file"], "financial_source"),
    }


def event_flags(event: pd.Series | None, row: pd.Series) -> dict[str, Any]:
    theme_tags = first_value(row, ["theme_catalyst_tags", "theme_group", "細分族群", "industry"])
    if event is None:
        return {
            "has_event_source": False,
            "event_tags": "",
            "theme_tags": theme_tags,
            "theme_flag": False,
            "date": "",
            "source": "",
            "summary": "",
            "quality": "",
            "confidence": "",
        }
    event_tags = first_value(event, ["event_catalyst_tags", "catalyst_tags", "tags", "event_tags"])
    return {
        "has_event_source": True,
        "event_tags": event_tags,
        "theme_tags": first_value(event, ["theme_catalyst_tags", "theme_tags"], theme_tags),
        "theme_flag": bool(event_tags),
        "date": normalize_date(first_value(event, ["catalyst_date", "event_date", "announcement_date", "date"])),
        "source": first_value(event, ["catalyst_source", "source", "url"], "event_source"),
        "summary": first_value(event, ["catalyst_summary", "event_summary", "summary", "title"]),
        "quality": first_value(event, ["catalyst_quality", "quality"]),
        "confidence": first_value(event, ["catalyst_confidence", "confidence"]),
    }


def is_construction_recognition(row: pd.Series) -> bool:
    rec_type = first_value(row, ["recognition_type"])
    if rec_type in CONSTRUCTION_RECOGNITION_TYPES:
        return True
    if truthy(first_value(row, ["is_construction_recognition"])):
        return True
    text = " ".join(
        first_value(row, [col])
        for col in ["industry", "theme_group", "細分族群", "revenue_signal_type"]
    )
    return any(keyword in text for keyword in ["營建", "建材營造", "不動產", "工程承攬", "交屋"])


def is_financial_or_asset_revenue_type(row: pd.Series) -> bool:
    text = " ".join(
        first_value(row, [col])
        for col in ["industry", "theme_group", "細分族群", "revenue_signal_type", "stock_name"]
    )
    return any(keyword in text for keyword in ["金融", "保險", "證券", "金控", "投資控股", "資產型"])


def derive_row(row: pd.Series, fin: pd.Series | None, event: pd.Series | None) -> dict[str, str]:
    stock_id = normalize_code(first_value(row, ["stock_id", "code", "ticker"]))
    category = first_value(row, ["category"])
    tdcc = first_value(row, ["tdcc_accumulation_signal", "tdcc_judgement", "tdcc_status"])
    already_priced = truthy(first_value(row, ["already_priced_in"]))
    construction = is_construction_recognition(row)
    financial_or_asset = is_financial_or_asset_revenue_type(row)

    fin_info = financial_flags(fin)
    event_info = event_flags(event, row)

    revenue_yoy = to_number(first_value(row, ["latest_revenue_yoy", "revenue_yoy_pct", "revenue_yoy"]))
    cum_revenue_yoy = to_number(first_value(row, ["cumulative_revenue_yoy", "cumulative_yoy_pct", "cum_revenue_yoy"]))
    revenue_good = category in REVENUE_CATEGORIES and not financial_or_asset and (
        (not math.isnan(revenue_yoy) and revenue_yoy >= 20)
        or (not math.isnan(cum_revenue_yoy) and cum_revenue_yoy >= 10)
        or first_value(row, ["revaluation_priority"]).startswith("A_")
    )
    has_real_financial = bool(fin_info["tags"])
    revenue_unconfirmed = revenue_good and not has_real_financial

    catalyst_date = fin_info["date"] or event_info["date"]
    catalyst_source = "; ".join([x for x in [fin_info["source"], event_info["source"]] if x])
    reaction = price_reaction(stock_id, catalyst_date, row)

    tags = list(fin_info["tags"])
    if revenue_unconfirmed:
        tags.append("revenue_good_eps_unconfirmed")
    if reaction["low_reaction_after_catalyst"] == "True" and tags:
        tags.append("low_reaction_after_catalyst")

    score = 0
    score += 25 if fin_info["eps_surprise_flag"] else 0
    score += 18 if fin_info["earnings_acceleration_flag"] else 0
    score += 18 if fin_info["margin_improvement_flag"] else 0
    score += 22 if fin_info["profit_turnaround_flag"] else 0
    score += 12 if event_info["theme_flag"] else 0
    score += 10 if reaction["low_reaction_after_catalyst"] == "True" and tags else 0
    score += 8 if tdcc in SUPPORTIVE_TDCC and tags else 0
    score += 10 if revenue_unconfirmed else 0
    if revenue_unconfirmed and not has_real_financial and not event_info["theme_flag"]:
        score = min(score, 30)
    if tdcc == "distribution_warning":
        score -= 25
    if already_priced or reaction["already_reacted_to_catalyst"] == "True":
        score -= 25
    if reaction["catalyst_overheated"] == "True":
        score -= 20
    if construction and revenue_unconfirmed and not has_real_financial:
        score = min(score, 15)
    score = max(0, min(100, int(round(score))))

    catalyst_summary_parts = list(fin_info["summary_parts"])
    if event_info["summary"]:
        catalyst_summary_parts.append(event_info["summary"])
    if revenue_unconfirmed:
        catalyst_summary_parts.append("營收轉強但 EPS / 毛利率尚未有結構化資料確認")
    if construction and revenue_unconfirmed:
        catalyst_summary_parts.append("營建/交屋認列型，單月營收不升級為類事欣科型")

    has_real_catalyst = has_real_financial or event_info["theme_flag"]
    low_reaction = reaction["low_reaction_after_catalyst"] == "True"
    tdcc_ok = tdcc in SUPPORTIVE_TDCC
    tdcc_bad = tdcc == "distribution_warning"
    distance_ma20 = to_number(first_value(row, ["distance_to_ma20_pct", "gap_ma20_pct"]))
    return_20d = to_number(first_value(row, ["return_20d", "return_20d_pct"]))
    in_platform = truthy(first_value(row, ["in_platform", "near_platform"]))
    technical_ok = in_platform or (not math.isnan(distance_ma20) and distance_ma20 <= 10) or category in {"range_rebound", "revenue_pullback"}
    overheated = reaction["catalyst_overheated"] == "True" or (not math.isnan(return_20d) and return_20d > 25)

    similar_to_shihsinko = (
        has_real_catalyst
        and low_reaction
        and tdcc_ok
        and technical_ok
        and not already_priced
        and not overheated
        and not tdcc_bad
        and not (construction and revenue_unconfirmed)
    )
    pre_breakout = bool(tags) and low_reaction and technical_ok and tdcc_ok and not overheated and not already_priced

    if has_real_financial and event_info["theme_flag"]:
        quality = event_info["quality"] or "high"
        confidence = event_info["confidence"] or "0.80"
    elif has_real_financial:
        quality = event_info["quality"] or "medium"
        confidence = event_info["confidence"] or "0.65"
    elif event_info["theme_flag"]:
        quality = event_info["quality"] or "medium"
        confidence = event_info["confidence"] or "0.55"
    elif revenue_unconfirmed:
        quality = "needs_eps_confirmation"
        confidence = "0.30"
    else:
        quality = ""
        confidence = ""

    return {
        "fundamental_catalyst_score": str(score),
        "fundamental_catalyst_tags": ";".join(dict.fromkeys(tags)),
        "event_catalyst_tags": event_info["event_tags"],
        "pre_breakout_catalyst_flag": bool_text(pre_breakout),
        "similar_to_shihsinko_flag": bool_text(similar_to_shihsinko),
        "eps_surprise_flag": bool_text(fin_info["eps_surprise_flag"]),
        "earnings_acceleration_flag": bool_text(fin_info["earnings_acceleration_flag"]),
        "margin_improvement_flag": bool_text(fin_info["margin_improvement_flag"]),
        "profit_turnaround_flag": bool_text(fin_info["profit_turnaround_flag"]),
        "undervalued_after_eps_flag": bool_text(False),
        "revenue_good_eps_unconfirmed_flag": bool_text(revenue_unconfirmed),
        "theme_catalyst_flag": bool_text(event_info["theme_flag"]),
        "theme_catalyst_tags": event_info["theme_tags"],
        "catalyst_date": catalyst_date,
        "catalyst_source": catalyst_source,
        "catalyst_summary": "；".join([x for x in catalyst_summary_parts if x]),
        "catalyst_quality": quality,
        "catalyst_confidence": confidence,
        **reaction,
    }


def build_markdown(df: pd.DataFrame, financial_source_path: str, event_source_path: str) -> str:
    lines = [
        "# 財報 / 事件催化層",
        "",
        f"- generated_at: `{now_text()}`",
        f"- candidate_rows: `{len(df)}`",
        f"- financial_source: `{financial_source_path or 'missing'}`",
        f"- event_source: `{event_source_path or 'missing'}`",
        "- note: 這是跨分類標籤層，不是第七大分類；候選股仍保留原本六大分類。",
        "- note: 若沒有 EPS / 毛利率 / 重大事件資料來源，系統只標示「營收好但 EPS 尚未確認」，不自動升級為類事欣科型。",
        "",
    ]

    if df.empty:
        lines.append("無候選資料。")
        return "\n".join(lines)

    count_similar = int(df.get("similar_to_shihsinko_flag", pd.Series(dtype=str)).astype(str).eq("True").sum())
    count_revenue_unconfirmed = int(df.get("revenue_good_eps_unconfirmed_flag", pd.Series(dtype=str)).astype(str).eq("True").sum())
    count_overheated = int(df.get("already_reacted_to_catalyst", pd.Series(dtype=str)).astype(str).eq("True").sum())

    lines.extend(
        [
            "## 今日催化層摘要",
            "",
            f"- 類事欣科型候選: `{count_similar}`",
            f"- 營收好但 EPS 尚未確認: `{count_revenue_unconfirmed}`",
            f"- 利多已反應 / 過熱需降級: `{count_overheated}`",
            "",
        ]
    )

    def table(title: str, part: pd.DataFrame, limit: int = 15) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if part.empty:
            lines.append("無。")
            lines.append("")
            return
        cols = [
            "date",
            "stock_id",
            "stock_name",
            "category_cn",
            "fundamental_catalyst_score",
            "fundamental_catalyst_tags",
            "event_catalyst_tags",
            "tdcc_accumulation_signal",
            "low_reaction_after_catalyst",
            "already_reacted_to_catalyst",
            "catalyst_quality",
            "catalyst_summary",
        ]
        cols = [col for col in cols if col in part.columns]
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
        for _, row in part.head(limit).iterrows():
            values = []
            for col in cols:
                value = safe_str(row.get(col, "")).replace("\n", " ").replace("|", "/")
                if len(value) > 90:
                    value = value[:90] + "..."
                values.append(value)
            lines.append("| " + " | ".join(values) + " |")
        lines.append("")

    scored = df.copy()
    scored["_catalyst_score_sort"] = pd.to_numeric(scored.get("fundamental_catalyst_score", ""), errors="coerce").fillna(0)
    scored = scored.sort_values("_catalyst_score_sort", ascending=False)

    table("類事欣科型候選股", scored[scored["similar_to_shihsinko_flag"].astype(str) == "True"])
    table("財報 / 事件催化候選股", scored[scored["fundamental_catalyst_score"].astype(str).ne("0")])
    table("營收好但 EPS 尚未確認", scored[scored["revenue_good_eps_unconfirmed_flag"].astype(str) == "True"])
    table("利多已反應 / 過熱需降級", scored[scored["already_reacted_to_catalyst"].astype(str) == "True"])

    return "\n".join(lines)


def main() -> int:
    if not ALL_CANDIDATES.exists():
        raise FileNotFoundError(f"Missing {ALL_CANDIDATES}")

    df = pd.read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    for col in CATALYST_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    financial, financial_source_path = load_source(
        FINANCIAL_SOURCE_FILES,
        ["catalyst_date", "announcement_date", "release_date", "report_date", "quarter_date", "date"],
    )
    events, event_source_path = load_source(
        EVENT_SOURCE_FILES,
        ["catalyst_date", "event_date", "announcement_date", "date"],
    )

    financial_map = {safe_str(row.get("stock_id")): row for _, row in financial.iterrows()} if not financial.empty else {}
    event_map = {safe_str(row.get("stock_id")): row for _, row in events.iterrows()} if not events.empty else {}

    derived_rows: list[dict[str, str]] = []
    for _, row in df.iterrows():
        code = normalize_code(first_value(row, ["stock_id", "code", "ticker"]))
        derived_rows.append(derive_row(row, financial_map.get(code), event_map.get(code)))

    derived = pd.DataFrame(derived_rows)
    for col in CATALYST_COLUMNS:
        df[col] = derived[col] if col in derived.columns else ""

    extra_cols = [col for col in df.columns if col not in CATALYST_COLUMNS]
    out_df = df[extra_cols + CATALYST_COLUMNS]
    write_csv(out_df, ALL_CANDIDATES)
    write_xlsx(out_df, ALL_CANDIDATES_XLSX)
    OUTPUT_MD.write_text(build_markdown(df, financial_source_path, event_source_path), encoding="utf-8")

    print(f"Saved: {ALL_CANDIDATES}")
    print(f"Saved: {ALL_CANDIDATES_XLSX}")
    print(f"Saved: {OUTPUT_MD}")
    print(f"financial_source={financial_source_path or 'missing'}")
    print(f"event_source={event_source_path or 'missing'}")
    print(f"similar_to_shihsinko_count={int(df['similar_to_shihsinko_flag'].astype(str).eq('True').sum())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
