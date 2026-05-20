from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re
import math

import pandas as pd


DATA_PRICE_DIR = Path("data/daily_price")
LATEST_DIR = Path("output/latest")

OUTPUT_CSV = LATEST_DIR / "revenue_breakout_low_response_latest.csv"
OUTPUT_MD = LATEST_DIR / "revenue_breakout_low_response_latest.md"
DEBUG_MD = LATEST_DIR / "revenue_breakout_low_response_debug_latest.md"

CATEGORY = "revenue_breakout_low_response"
CATEGORY_CN = "營收爆發低反應股"

MIN_VOLUME_LOTS = 1000


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    text = re.sub(r"[^0-9]", "", text)
    return text.zfill(4) if text else ""


def normalize_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def to_number(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("+", "")
    text = text.replace("--", "")
    text = text.replace(" ", "")
    if text == "":
        return pd.NA
    return pd.to_numeric(text, errors="coerce")


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def pick_first_existing_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def load_daily_price_history() -> pd.DataFrame:
    frames = []

    for path in sorted(DATA_PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str, "date": str})
        except Exception as exc:
            print(f"Skip price file {path}: {exc}")
            continue

        if df.empty:
            continue

        if "stock_id" not in df.columns:
            if "ticker" in df.columns:
                df = df.rename(columns={"ticker": "stock_id"})
            elif "code" in df.columns:
                df = df.rename(columns={"code": "stock_id"})

        if "stock_id" not in df.columns:
            continue

        if "date" not in df.columns:
            match = re.search(r"([0-9]{8})", path.name)
            if match:
                df["date"] = match.group(1)

        if "name" not in df.columns:
            df["name"] = ""

        if "trading_value" not in df.columns:
            df["trading_value"] = pd.NA

        required = {"date", "stock_id", "open", "high", "low", "close", "volume"}

        if not required.issubset(set(df.columns)):
            continue

        df = df.copy()
        df["date"] = df["date"].astype(str).str.replace(r"[^0-9]", "", regex=True)
        df["stock_id"] = df["stock_id"].map(normalize_code)
        df["name"] = df["name"].map(normalize_text)

        for col in ["open", "high", "low", "close", "volume", "trading_value"]:
            df[col] = df[col].map(to_number)

        df = df.dropna(subset=["date", "stock_id", "open", "high", "low", "close"])
        df = df[df["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

        frames.append(
            df[
                [
                    "date",
                    "stock_id",
                    "name",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "trading_value",
                ]
            ]
        )

    if not frames:
        return pd.DataFrame()

    price = pd.concat(frames, ignore_index=True)
    price = price.drop_duplicates(subset=["date", "stock_id"], keep="last")
    price = price.sort_values(["stock_id", "date"]).reset_index(drop=True)

    return price


def load_revenue_data() -> pd.DataFrame:
    try:
        from stock_daily_monitor import fetch_monthly_revenue
    except Exception as exc:
        print(f"Cannot import fetch_monthly_revenue: {exc}")
        return pd.DataFrame()

    try:
        revenue_df = fetch_monthly_revenue()
    except Exception as exc:
        print(f"fetch_monthly_revenue failed: {exc}")
        return pd.DataFrame()

    if revenue_df is None or revenue_df.empty:
        return pd.DataFrame()

    return revenue_df.copy()


def standardize_revenue_data(revenue_df: pd.DataFrame, debug: dict) -> pd.DataFrame:
    if revenue_df.empty:
        debug["revenue_schema_status"] = "raw_revenue_empty"
        return pd.DataFrame()

    df = revenue_df.copy()
    debug["raw_revenue_columns"] = list(df.columns)

    code_col = pick_first_existing_column(
        df,
        [
            "stock_id",
            "ticker",
            "code",
            "公司代號",
            "股票代號",
        ],
    )

    name_col = pick_first_existing_column(
        df,
        [
            "stock_name",
            "name",
            "company_name",
            "公司名稱",
            "股票名稱",
        ],
    )

    industry_col = pick_first_existing_column(
        df,
        [
            "industry",
            "產業別",
            "細分族群",
        ],
    )

    date_col = pick_first_existing_column(
        df,
        [
            "date",
            "revenue_date",
            "年月",
            "資料年月",
            "營收年月",
        ],
    )

    latest_revenue_col = pick_first_existing_column(
        df,
        [
            "latest_revenue",
            "monthly_revenue",
            "revenue",
            "當月營收",
            "營業收入-當月營收",
            "營收",
        ],
    )

    latest_yoy_col = pick_first_existing_column(
        df,
        [
            "latest_revenue_yoy",
            "monthly_revenue_yoy",
            "revenue_yoy",
            "yoy",
            "YoY",
            "當月營收年增率",
            "營收年增率",
            "去年同月增減%",
        ],
    )

    cumulative_yoy_col = pick_first_existing_column(
        df,
        [
            "cumulative_revenue_yoy",
            "accumulated_revenue_yoy",
            "cumulative_yoy",
            "累計營收年增率",
            "累計營收增減%",
            "前期比較增減%",
        ],
    )

    debug["selected_revenue_columns"] = {
        "code_col": code_col,
        "name_col": name_col,
        "industry_col": industry_col,
        "date_col": date_col,
        "latest_revenue_col": latest_revenue_col,
        "latest_yoy_col": latest_yoy_col,
        "cumulative_yoy_col": cumulative_yoy_col,
    }

    if code_col is None or latest_yoy_col is None:
        debug["revenue_schema_status"] = "missing_code_or_latest_yoy"
        return pd.DataFrame()

    out = pd.DataFrame()
    out["stock_id"] = df[code_col].map(normalize_code)
    out["stock_name"] = df[name_col].map(normalize_text) if name_col else ""
    out["industry"] = df[industry_col].map(normalize_text) if industry_col else ""
    out["revenue_release_date"] = df[date_col].astype(str) if date_col else ""

    out["latest_revenue"] = df[latest_revenue_col].map(to_number) if latest_revenue_col else pd.NA
    out["latest_revenue_yoy"] = df[latest_yoy_col].map(to_number)
    out["cumulative_revenue_yoy"] = df[cumulative_yoy_col].map(to_number) if cumulative_yoy_col else pd.NA

    out = out[out["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()
    out = out.dropna(subset=["latest_revenue_yoy"])

    debug["revenue_schema_status"] = "ok"

    return out


def load_tdcc_latest() -> pd.DataFrame:
    path = LATEST_DIR / "tdcc_holder_ratio_latest.csv"

    if not path.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(path, dtype={"stock_id": str, "ticker": str, "code": str})
    except Exception as exc:
        print(f"Read TDCC failed: {exc}")
        return pd.DataFrame()

    if df.empty:
        return pd.DataFrame()

    if "stock_id" not in df.columns:
        if "ticker" in df.columns:
            df = df.rename(columns={"ticker": "stock_id"})
        elif "code" in df.columns:
            df = df.rename(columns={"code": "stock_id"})

    if "stock_id" not in df.columns:
        return pd.DataFrame()

    df["stock_id"] = df["stock_id"].map(normalize_code)

    return df


def get_tdcc_value(row: pd.Series, candidates: list[str], default=pd.NA):
    for col in candidates:
        if col in row.index:
            return row[col]
    return default


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["ema23"] = df["close"].ewm(span=23, adjust=False).mean()
    df["volume_ma20"] = df["volume"].rolling(20).mean()
    df["volume_ratio"] = df["volume"] / df["volume_ma20"]

    return df


def calc_stock_price_metrics(price_df: pd.DataFrame, stock_id: str) -> dict | None:
    stock_price = price_df[price_df["stock_id"] == stock_id].copy()
    stock_price = stock_price.sort_values("date").tail(180).reset_index(drop=True)

    if stock_price.empty or len(stock_price) < 60:
        return None

    stock_price = add_indicators(stock_price)

    latest = stock_price.iloc[-1]
    prev = stock_price.iloc[-2] if len(stock_price) >= 2 else latest

    close = safe_float(latest["close"])
    ma20 = safe_float(latest["ma20"])
    ma60 = safe_float(latest["ma60"])
    ema23 = safe_float(latest["ema23"])
    volume_ratio = safe_float(latest["volume_ratio"], 0)

    if math.isnan(close) or math.isnan(ma20) or math.isnan(ma60) or math.isnan(ema23):
        return None

    high_20 = stock_price.tail(20)["high"].max()
    low_20 = stock_price.tail(20)["low"].min()
    high_60 = stock_price.tail(60)["high"].max()
    low_60 = stock_price.tail(60)["low"].min()

    return_5d = (
        (close / safe_float(stock_price.iloc[-6]["close"]) - 1) * 100
        if len(stock_price) >= 6 and safe_float(stock_price.iloc[-6]["close"]) > 0
        else pd.NA
    )

    return_3d = (
        (close / safe_float(stock_price.iloc[-4]["close"]) - 1) * 100
        if len(stock_price) >= 4 and safe_float(stock_price.iloc[-4]["close"]) > 0
        else pd.NA
    )

    return_1d = (
        (close / safe_float(prev["close"]) - 1) * 100
        if safe_float(prev["close"]) > 0
        else pd.NA
    )

    distance_to_ma20_pct = (close / ma20 - 1) * 100 if ma20 > 0 else pd.NA
    distance_to_ma60_pct = (close / ma60 - 1) * 100 if ma60 > 0 else pd.NA
    distance_to_ema23_pct = (close / ema23 - 1) * 100 if ema23 > 0 else pd.NA
    distance_to_high_60_pct = (close / high_60 - 1) * 100 if high_60 > 0 else pd.NA

    recent_60 = stock_price.tail(60)
    platform_high = recent_60["high"].max()
    platform_low = recent_60["low"].min()
    platform_width_pct = (platform_high / platform_low - 1) * 100 if platform_low > 0 else pd.NA

    in_platform = platform_width_pct <= 25 and close <= platform_high * 1.03 and close >= platform_low * 0.97
    near_ma = -5 <= distance_to_ma20_pct <= 15 or -5 <= distance_to_ema23_pct <= 15
    close_above_ma = close > ma20 or close > ema23
    near_high_not_overheated = distance_to_high_60_pct >= -10 and distance_to_high_60_pct <= 5

    high_today = safe_float(latest["high"])
    low_today = safe_float(latest["low"])

    if high_today > low_today and high_today > 0:
        upper_shadow_pct = (high_today - close) / high_today * 100
        intraday_range_pct = (high_today - low_today) / low_today * 100 if low_today > 0 else 0
        high_volume_upper_shadow = upper_shadow_pct >= 3 and intraday_range_pct >= 5 and volume_ratio >= 1.5
    else:
        upper_shadow_pct = pd.NA
        high_volume_upper_shadow = False

    price_data_warning = "ok"

    if len(stock_price) < 120:
        price_data_warning = "available_days_too_few"

    return {
        "date": latest["date"],
        "available_days": len(stock_price),
        "close": round(close, 2),
        "volume": safe_float(latest["volume"], 0),
        "volume_ratio": round(volume_ratio, 2),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "ema23": round(ema23, 2),
        "distance_to_ma20_pct": round(distance_to_ma20_pct, 2),
        "distance_to_ma60_pct": round(distance_to_ma60_pct, 2),
        "distance_to_ema23_pct": round(distance_to_ema23_pct, 2),
        "high_20": round(high_20, 2),
        "low_20": round(low_20, 2),
        "high_60": round(high_60, 2),
        "low_60": round(low_60, 2),
        "return_after_revenue_1d": round(return_1d, 2) if not pd.isna(return_1d) else pd.NA,
        "return_after_revenue_3d": round(return_3d, 2) if not pd.isna(return_3d) else pd.NA,
        "return_5d": round(return_5d, 2) if not pd.isna(return_5d) else pd.NA,
        "distance_to_high_60_pct": round(distance_to_high_60_pct, 2),
        "platform_high": round(platform_high, 2),
        "platform_low": round(platform_low, 2),
        "platform_width_pct": round(platform_width_pct, 2),
        "in_platform": bool(in_platform),
        "near_ma": bool(near_ma),
        "close_above_ma": bool(close_above_ma),
        "near_high_not_overheated": bool(near_high_not_overheated),
        "high_volume_upper_shadow": bool(high_volume_upper_shadow),
        "price_data_warning": price_data_warning,
    }


def calc_revenue_score(row: pd.Series, price_metrics: dict, tdcc_row: pd.Series | None) -> tuple[int, list[str], list[str]]:
    score = 0
    notes = []
    warnings = []

    latest_yoy = safe_float(row.get("latest_revenue_yoy"))
    cumulative_yoy = safe_float(row.get("cumulative_revenue_yoy"))

    if latest_yoy >= 100:
        score += 3
        notes.append("單月營收YoY>=100%")
    elif latest_yoy >= 50:
        score += 2
        notes.append("單月營收YoY 50%~100%")
    elif latest_yoy >= 30:
        score += 1
        notes.append("單月營收YoY 30%~50%")

    if cumulative_yoy >= 30:
        score += 2
        notes.append("累計營收YoY>=30%")
    elif cumulative_yoy >= 10:
        score += 1
        notes.append("累計營收YoY 10%~30%")

    if not math.isnan(latest_yoy) and not math.isnan(cumulative_yoy):
        if latest_yoy >= cumulative_yoy + 20:
            score += 1
            notes.append("單月YoY明顯高於累計YoY，近期加速")

    return_3d = safe_float(price_metrics.get("return_after_revenue_3d"))
    return_5d = safe_float(price_metrics.get("return_5d"))
    distance_to_ma20_pct = safe_float(price_metrics.get("distance_to_ma20_pct"))
    distance_to_ema23_pct = safe_float(price_metrics.get("distance_to_ema23_pct"))

    if not math.isnan(return_3d) and return_3d < 10:
        score += 2
        notes.append("近3日漲幅低於10%，股價低反應")

    if not math.isnan(return_5d) and return_5d < 15:
        score += 1
        notes.append("近5日漲幅低於15%")

    if -5 <= distance_to_ma20_pct <= 10 or -5 <= distance_to_ema23_pct <= 10:
        score += 1
        notes.append("股價仍在20MA/23EMA附近")

    if distance_to_ma20_pct > 20 or distance_to_ema23_pct > 20:
        score -= 2
        warnings.append("距20MA/23EMA過遠")

    if not math.isnan(return_5d) and return_5d > 25:
        score -= 3
        warnings.append("近5日漲幅超過25%，可能已過熱")

    if price_metrics.get("in_platform"):
        score += 2
        notes.append("仍在平台整理區")

    if price_metrics.get("close_above_ma"):
        score += 1
        notes.append("站上20MA/23EMA")

    if price_metrics.get("near_high_not_overheated"):
        score += 1
        notes.append("接近前高但未大幅過熱")

    if price_metrics.get("high_volume_upper_shadow"):
        score -= 2
        warnings.append("疑似高位爆量長上影")

    if tdcc_row is not None:
        tdcc_400_change = to_number(
            get_tdcc_value(tdcc_row, ["holder_400_change", "400張變化", "tdcc_over_400_change", "over_400_change"], pd.NA)
        )
        tdcc_1000_change = to_number(
            get_tdcc_value(tdcc_row, ["holder_1000_change", "1000張變化", "tdcc_over_1000_change", "over_1000_change"], pd.NA)
        )

        c400 = safe_float(tdcc_400_change)
        c1000 = safe_float(tdcc_1000_change)

        if c400 > 0 and c1000 > 0:
            score += 2
            notes.append("TDCC 400張與1000張同步增加")
        elif c400 > 0 or c1000 > 0:
            score += 1
            notes.append("TDCC 大戶級距部分增加")
        elif c400 < 0 and c1000 < 0:
            score -= 2
            warnings.append("TDCC 400張與1000張同步減少")
        elif c400 < 0 or c1000 < 0:
            score -= 1
            warnings.append("TDCC 大戶級距部分減少")

    return score, notes, warnings


def write_debug_report(debug: dict, sample_rows: list[dict]) -> None:
    lines = []
    lines.append("# 營收爆發低反應股 Debug Report")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append("")
    lines.append("## 診斷統計")
    lines.append("")
    lines.append("| item | value |")
    lines.append("|---|---:|")

    for key in [
        "raw_revenue_rows",
        "standardized_revenue_rows",
        "price_rows",
        "tdcc_rows",
        "revenue_condition_pass",
        "price_metrics_pass",
        "low_response_pass",
        "overheat_pass",
        "score_pass",
        "final_rows",
    ]:
        lines.append(f"| {key} | {debug.get(key, 0)} |")

    lines.append("")
    lines.append("## 營收欄位狀態")
    lines.append("")
    lines.append(f"- revenue_schema_status：`{debug.get('revenue_schema_status', '')}`")
    lines.append("")
    lines.append("### selected_revenue_columns")
    lines.append("")
    selected = debug.get("selected_revenue_columns", {})
    lines.append("| field | selected column |")
    lines.append("|---|---|")
    for key, value in selected.items():
        lines.append(f"| {key} | `{value}` |")

    lines.append("")
    lines.append("### raw_revenue_columns")
    lines.append("")
    for col in debug.get("raw_revenue_columns", []):
        lines.append(f"- `{col}`")

    lines.append("")
    lines.append("## 主要刷掉原因")
    lines.append("")
    reason_counts = debug.get("reason_counts", {})
    lines.append("| reason | count |")
    lines.append("|---|---:|")
    for reason, count in sorted(reason_counts.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {reason} | {count} |")

    lines.append("")
    lines.append("## 樣本資料")
    lines.append("")
    if not sample_rows:
        lines.append("沒有樣本資料。")
    else:
        cols = [
            "stock_id",
            "stock_name",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "return_5d",
            "distance_to_ma20_pct",
            "score",
            "reason",
        ]
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
        for row in sample_rows[:50]:
            values = []
            for col in cols:
                value = row.get(col, "")
                if pd.isna(value):
                    value = ""
                values.append(str(value))
            lines.append("| " + " | ".join(values) + " |")

    DEBUG_MD.write_text("\n".join(lines), encoding="utf-8")


def build_revenue_breakout_low_response_candidates() -> tuple[pd.DataFrame, dict, list[dict]]:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    debug = {
        "raw_revenue_rows": 0,
        "standardized_revenue_rows": 0,
        "price_rows": 0,
        "tdcc_rows": 0,
        "revenue_condition_pass": 0,
        "price_metrics_pass": 0,
        "low_response_pass": 0,
        "overheat_pass": 0,
        "score_pass": 0,
        "final_rows": 0,
        "reason_counts": {},
    }

    sample_rows = []

    def add_reason(reason: str):
        debug["reason_counts"][reason] = debug["reason_counts"].get(reason, 0) + 1

    price_df = load_daily_price_history()
    revenue_raw = load_revenue_data()
    tdcc_df = load_tdcc_latest()

    debug["raw_revenue_rows"] = len(revenue_raw)
    debug["price_rows"] = len(price_df)
    debug["tdcc_rows"] = len(tdcc_df)

    revenue_df = standardize_revenue_data(revenue_raw, debug)
    debug["standardized_revenue_rows"] = len(revenue_df)

    if price_df.empty or revenue_df.empty:
        add_reason("price_or_revenue_empty")
        write_debug_report(debug, sample_rows)
        return pd.DataFrame(), debug, sample_rows

    tdcc_map = {}

    if not tdcc_df.empty:
        tdcc_map = {
            normalize_code(row["stock_id"]): row
            for _, row in tdcc_df.iterrows()
            if normalize_code(row.get("stock_id", ""))
        }

    candidates = []

    for _, rev_row in revenue_df.iterrows():
        stock_id = normalize_code(rev_row.get("stock_id", ""))
        stock_name = rev_row.get("stock_name", "")

        if not stock_id:
            add_reason("missing_stock_id")
            continue

        latest_yoy = safe_float(rev_row.get("latest_revenue_yoy"))
        cumulative_yoy = safe_float(rev_row.get("cumulative_revenue_yoy"))

        revenue_condition = (
            latest_yoy >= 50
            or (
                latest_yoy >= 30
                and not math.isnan(cumulative_yoy)
                and cumulative_yoy >= 20
            )
        )

        if not revenue_condition:
            add_reason("fail_revenue_condition")
            continue

        debug["revenue_condition_pass"] += 1

        price_metrics = calc_stock_price_metrics(price_df, stock_id)

        if price_metrics is None:
            add_reason("missing_or_insufficient_price_metrics")
            sample_rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "latest_revenue_yoy": latest_yoy,
                    "cumulative_revenue_yoy": cumulative_yoy,
                    "reason": "missing_or_insufficient_price_metrics",
                }
            )
            continue

        debug["price_metrics_pass"] += 1

        return_5d = safe_float(price_metrics.get("return_5d"))
        distance_to_ma20_pct = safe_float(price_metrics.get("distance_to_ma20_pct"))
        distance_to_ema23_pct = safe_float(price_metrics.get("distance_to_ema23_pct"))

        low_response_condition = (
            (
                not math.isnan(return_5d)
                and return_5d < 20
            )
            and (
                distance_to_ma20_pct < 20
                or distance_to_ema23_pct < 20
            )
        )

        if not low_response_condition:
            add_reason("fail_low_response_condition")
            sample_rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "latest_revenue_yoy": latest_yoy,
                    "cumulative_revenue_yoy": cumulative_yoy,
                    "return_5d": return_5d,
                    "distance_to_ma20_pct": distance_to_ma20_pct,
                    "reason": "fail_low_response_condition",
                }
            )
            continue

        debug["low_response_pass"] += 1

        if return_5d > 25:
            add_reason("fail_overheat_return_5d")
            continue

        if distance_to_ma20_pct > 25 and distance_to_ema23_pct > 25:
            add_reason("fail_overheat_ma_distance")
            continue

        debug["overheat_pass"] += 1

        tdcc_row = tdcc_map.get(stock_id)

        score, notes, warnings = calc_revenue_score(rev_row, price_metrics, tdcc_row)

        if score < 4:
            add_reason("fail_score_lt_4")
            sample_rows.append(
                {
                    "stock_id": stock_id,
                    "stock_name": stock_name,
                    "latest_revenue_yoy": latest_yoy,
                    "cumulative_revenue_yoy": cumulative_yoy,
                    "return_5d": return_5d,
                    "distance_to_ma20_pct": distance_to_ma20_pct,
                    "score": score,
                    "reason": "fail_score_lt_4",
                }
            )
            continue

        debug["score_pass"] += 1

        tdcc_date = ""
        holder_400_change = pd.NA
        holder_1000_change = pd.NA
        holder_400_pct = pd.NA
        holder_1000_pct = pd.NA
        tdcc_judgement = ""

        if tdcc_row is not None:
            tdcc_date = get_tdcc_value(tdcc_row, ["tdcc_date", "date", "TDCC日"], "")
            holder_400_change = get_tdcc_value(tdcc_row, ["holder_400_change", "400張變化", "tdcc_over_400_change", "over_400_change"], pd.NA)
            holder_1000_change = get_tdcc_value(tdcc_row, ["holder_1000_change", "1000張變化", "tdcc_over_1000_change", "over_1000_change"], pd.NA)
            holder_400_pct = get_tdcc_value(tdcc_row, ["holder_400_pct", "400張以上%", "tdcc_over_400_pct", "over_400_pct"], pd.NA)
            holder_1000_pct = get_tdcc_value(tdcc_row, ["holder_1000_pct", "1000張以上%", "tdcc_over_1000_pct", "over_1000_pct"], pd.NA)
            tdcc_judgement = get_tdcc_value(tdcc_row, ["tdcc_judgement", "TDCC判斷", "tdcc_judge"], "")

        row = {
            "date": price_metrics["date"],
            "category": CATEGORY,
            "category_cn": CATEGORY_CN,
            "breakout_type": CATEGORY,
            "stock_id": stock_id,
            "stock_name": stock_name,
            "industry": rev_row.get("industry", ""),
            "score": score,
            "rank": pd.NA,
            "latest_revenue_yoy": round(latest_yoy, 2),
            "cumulative_revenue_yoy": round(cumulative_yoy, 2) if not math.isnan(cumulative_yoy) else pd.NA,
            "revenue_acceleration_note": "；".join(notes),
            "revenue_warning": "；".join(warnings),
            "revenue_release_date": rev_row.get("revenue_release_date", ""),
            "return_after_revenue_1d": price_metrics.get("return_after_revenue_1d"),
            "return_after_revenue_3d": price_metrics.get("return_after_revenue_3d"),
            "return_5d": price_metrics.get("return_5d"),
            "distance_to_ma20_pct": price_metrics.get("distance_to_ma20_pct"),
            "distance_to_ma60_pct": price_metrics.get("distance_to_ma60_pct"),
            "distance_to_ema23_pct": price_metrics.get("distance_to_ema23_pct"),
            "close": price_metrics.get("close"),
            "volume": price_metrics.get("volume"),
            "volume_ratio": price_metrics.get("volume_ratio"),
            "ma20": price_metrics.get("ma20"),
            "ma60": price_metrics.get("ma60"),
            "ema23": price_metrics.get("ema23"),
            "high_20": price_metrics.get("high_20"),
            "low_20": price_metrics.get("low_20"),
            "high_60": price_metrics.get("high_60"),
            "low_60": price_metrics.get("low_60"),
            "platform_high": price_metrics.get("platform_high"),
            "platform_low": price_metrics.get("platform_low"),
            "platform_width_pct": price_metrics.get("platform_width_pct"),
            "in_platform": price_metrics.get("in_platform"),
            "near_ma": price_metrics.get("near_ma"),
            "tdcc_date": tdcc_date,
            "holder_400_pct": holder_400_pct,
            "holder_400_change": holder_400_change,
            "holder_1000_pct": holder_1000_pct,
            "holder_1000_change": holder_1000_change,
            "tdcc_judgement": tdcc_judgement,
            "price_data_warning": price_metrics.get("price_data_warning", "ok"),
            "chart_path": "",
            "chart_url": "",
            "note": "；".join(notes + warnings),
        }

        candidates.append(row)
        sample_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "latest_revenue_yoy": latest_yoy,
                "cumulative_revenue_yoy": cumulative_yoy,
                "return_5d": return_5d,
                "distance_to_ma20_pct": distance_to_ma20_pct,
                "score": score,
                "reason": "selected",
            }
        )

    result = pd.DataFrame(candidates)

    if result.empty:
        debug["final_rows"] = 0
        write_debug_report(debug, sample_rows)
        return result, debug, sample_rows

    result = result.sort_values(["score", "latest_revenue_yoy"], ascending=[False, False]).reset_index(drop=True)
    result["rank"] = range(1, len(result) + 1)

    debug["final_rows"] = len(result)
    write_debug_report(debug, sample_rows)

    return result, debug, sample_rows


def write_markdown(df: pd.DataFrame) -> None:
    lines = []
    lines.append("# 營收爆發低反應股")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 輸出 CSV：`{OUTPUT_CSV}`")
    lines.append(f"- Debug：`{DEBUG_MD}`")
    lines.append("")

    if df.empty:
        lines.append("目前沒有符合條件的營收爆發低反應股。")
    else:
        lines.append("## 篩選邏輯")
        lines.append("")
        lines.append("- 單月營收 YoY >= 50%，或單月 YoY >= 30% 且累計 YoY >= 20%。")
        lines.append("- 股價尚未明顯過熱，近 5 日漲幅與均線乖離需在可接受範圍。")
        lines.append("- TDCC 未明顯惡化者加分，大戶同步減少者降級。")
        lines.append("")
        lines.append("## 完整名單")
        lines.append("")
        cols = [
            "rank",
            "stock_id",
            "stock_name",
            "industry",
            "score",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "return_5d",
            "distance_to_ma20_pct",
            "close",
            "volume_ratio",
            "tdcc_judgement",
            "price_data_warning",
            "note",
        ]

        lines.append("| " + " | ".join(cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")

        for _, row in df.iterrows():
            values = []
            for col in cols:
                value = row.get(col, "")
                if pd.isna(value):
                    value = ""
                values.append(str(value))
            lines.append("| " + " | ".join(values) + " |")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def empty_output_df() -> pd.DataFrame:
    return pd.DataFrame(
        columns=[
            "date",
            "category",
            "category_cn",
            "breakout_type",
            "stock_id",
            "stock_name",
            "industry",
            "score",
            "rank",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "revenue_acceleration_note",
            "revenue_warning",
            "revenue_release_date",
            "return_after_revenue_1d",
            "return_after_revenue_3d",
            "return_5d",
            "distance_to_ma20_pct",
            "distance_to_ma60_pct",
            "distance_to_ema23_pct",
            "close",
            "volume",
            "volume_ratio",
            "ma20",
            "ma60",
            "ema23",
            "high_20",
            "low_20",
            "high_60",
            "low_60",
            "platform_high",
            "platform_low",
            "platform_width_pct",
            "in_platform",
            "near_ma",
            "tdcc_date",
            "holder_400_pct",
            "holder_400_change",
            "holder_1000_pct",
            "holder_1000_change",
            "tdcc_judgement",
            "price_data_warning",
            "chart_path",
            "chart_url",
            "note",
        ]
    )


def main() -> int:
    df, debug, sample_rows = build_revenue_breakout_low_response_candidates()

    if df.empty:
        df = empty_output_df()

    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    write_markdown(df)

    print(f"Saved: {OUTPUT_CSV}")
    print(f"Saved: {OUTPUT_MD}")
    print(f"Saved: {DEBUG_MD}")
    print(f"Rows: {len(df)}")
    print(f"Debug: {debug}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
