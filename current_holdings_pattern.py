from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import math
import re

import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


CONFIG_JSON = Path("config/current_holdings.json")
CONFIG_CSV = Path("config/current_holdings.csv")

DATA_PRICE_DIR = Path("data/daily_price")

OUTPUT_DIR = Path("output/latest")
CHART_DIR = OUTPUT_DIR / "charts" / "current_holdings"

OUTPUT_CSV = OUTPUT_DIR / "current_holdings_pattern_latest.csv"
OUTPUT_MD = OUTPUT_DIR / "current_holdings_pattern_latest.md"

MIN_PLATFORM_DAYS = 20
MAX_PLATFORM_DAYS = 60
PLATFORM_WIDTH_LIMIT = 18.0
STRICT_PLATFORM_WIDTH_LIMIT = 12.0


OUTPUT_COLUMNS = [
    "stock_id",
    "stock_name",
    "date",
    "available_days",

    "open",
    "high",
    "low",
    "close",
    "volume",
    "trading_value",

    "cost",
    "lots",
    "margin",
    "unrealized_pnl",
    "unrealized_pnl_pct",

    "high_180",
    "low_180",
    "high_60",
    "low_60",
    "high_20",
    "low_20",

    "swing_high_recent",
    "swing_low_recent",

    "platform_start_date",
    "platform_end_date",
    "platform_high",
    "platform_low",
    "platform_days",
    "platform_width_pct",

    "close_vs_platform",
    "is_above_platform",
    "is_inside_platform",
    "is_below_platform",

    "break_above_platform_high",
    "break_below_platform_low",

    "false_breakdown",
    "false_breakdown_date",
    "false_breakdown_recovery_days",

    "break_prior_high",
    "break_prior_high_date",
    "break_prior_high_hold",

    "upper_shadow_pct",
    "lower_shadow_pct",
    "is_high_volume_upper_shadow",
    "is_high_volume_breakdown",

    "volume_ma5",
    "volume_ma20",
    "volume_ratio_20",

    "ema23",
    "ma20",
    "ma60",

    "pattern_state",
    "pattern_signal",
    "action_trigger",
    "risk_note",
    "chart_path",
]


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


def normalize_bool(value) -> bool:
    if isinstance(value, bool):
        return value

    text = str(value).strip().lower()

    return text in ["true", "1", "yes", "y", "是", "融資"]


def to_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("+", "")
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


def round_value(value, digits=2):
    if pd.isna(value):
        return pd.NA

    try:
        return round(float(value), digits)
    except Exception:
        return pd.NA


def pick_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col

    return None


def load_current_holdings() -> list[dict]:
    if CONFIG_JSON.exists():
        data = json.loads(CONFIG_JSON.read_text(encoding="utf-8"))

        holdings = []

        for item in data:
            holdings.append(
                {
                    "stock_id": normalize_code(item.get("stock_id", "")),
                    "stock_name": str(item.get("stock_name", "")).strip(),
                    "lots": safe_float(item.get("lots", 0), 0),
                    "cost": safe_float(item.get("cost", 0), 0),
                    "margin": normalize_bool(item.get("margin", False)),
                }
            )

        return [h for h in holdings if h["stock_id"]]

    if CONFIG_CSV.exists():
        df = pd.read_csv(CONFIG_CSV, dtype={"stock_id": str})
        holdings = []

        for _, row in df.iterrows():
            holdings.append(
                {
                    "stock_id": normalize_code(row.get("stock_id", "")),
                    "stock_name": str(row.get("stock_name", "")).strip(),
                    "lots": safe_float(row.get("lots", 0), 0),
                    "cost": safe_float(row.get("cost", 0), 0),
                    "margin": normalize_bool(row.get("margin", False)),
                }
            )

        return [h for h in holdings if h["stock_id"]]

    raise FileNotFoundError(
        "找不到 config/current_holdings.json 或 config/current_holdings.csv"
    )


def load_daily_price_history() -> pd.DataFrame:
    frames = []

    for path in sorted(DATA_PRICE_DIR.glob("*.csv")):
        try:
            df = pd.read_csv(
                path,
                dtype={
                    "stock_id": str,
                    "ticker": str,
                    "code": str,
                    "date": str,
                },
            )
        except Exception as exc:
            print(f"Skip price file {path}: {exc}")
            continue

        if df.empty:
            continue

        code_col = pick_column(df, ["stock_id", "ticker", "code", "證券代號", "股票代號"])
        name_col = pick_column(df, ["stock_name", "name", "證券名稱", "股票名稱"])
        date_col = pick_column(df, ["date", "日期", "資料日期"])

        open_col = pick_column(df, ["open", "開盤價", "開盤"])
        high_col = pick_column(df, ["high", "最高價", "最高"])
        low_col = pick_column(df, ["low", "最低價", "最低"])
        close_col = pick_column(df, ["close", "收盤價", "收盤"])
        volume_col = pick_column(df, ["volume", "成交股數", "成交量"])
        trading_value_col = pick_column(df, ["trading_value", "成交金額", "成交值"])

        if not all([code_col, open_col, high_col, low_col, close_col, volume_col]):
            continue

        out = pd.DataFrame()
        out["stock_id"] = df[code_col].map(normalize_code)
        out["stock_name"] = df[name_col].astype(str).str.strip() if name_col else ""

        if date_col:
            out["date"] = df[date_col].astype(str).str.replace(r"[^0-9]", "", regex=True)
        else:
            match = re.search(r"(\d{8})", path.name)
            out["date"] = match.group(1) if match else ""

        out["open"] = df[open_col].map(to_number)
        out["high"] = df[high_col].map(to_number)
        out["low"] = df[low_col].map(to_number)
        out["close"] = df[close_col].map(to_number)
        out["volume"] = df[volume_col].map(to_number)
        out["trading_value"] = df[trading_value_col].map(to_number) if trading_value_col else pd.NA

        out = out.dropna(subset=["date", "stock_id", "open", "high", "low", "close"])
        out = out[out["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

        frames.append(out)

    if not frames:
        return pd.DataFrame()

    price = pd.concat(frames, ignore_index=True)
    price = price.drop_duplicates(subset=["date", "stock_id"], keep="last")
    price = price.sort_values(["stock_id", "date"]).reset_index(drop=True)

    return price


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["ma20"] = df["close"].rolling(20).mean()
    df["ma60"] = df["close"].rolling(60).mean()
    df["ema23"] = df["close"].ewm(span=23, adjust=False).mean()

    df["volume_ma5"] = df["volume"].rolling(5).mean()
    df["volume_ma20"] = df["volume"].rolling(20).mean()
    df["volume_ratio_20"] = df["volume"] / df["volume_ma20"]

    return df


def detect_platform(df: pd.DataFrame) -> dict:
    if len(df) < MIN_PLATFORM_DAYS + 1:
        recent = df.copy()
    else:
        recent = df.iloc[:-1].copy()

    if recent.empty:
        return {
            "platform_start_date": "",
            "platform_end_date": "",
            "platform_high": pd.NA,
            "platform_low": pd.NA,
            "platform_days": 0,
            "platform_width_pct": pd.NA,
            "platform_quality": "insufficient",
        }

    best = None

    for days in [60, 50, 40, 30, 20]:
        if len(recent) < days:
            continue

        part = recent.tail(days)
        high = safe_float(part["high"].max())
        low = safe_float(part["low"].min())

        if low <= 0:
            continue

        width_pct = (high / low - 1) * 100

        if width_pct <= PLATFORM_WIDTH_LIMIT:
            best = {
                "platform_start_date": str(part.iloc[0]["date"]),
                "platform_end_date": str(part.iloc[-1]["date"]),
                "platform_high": high,
                "platform_low": low,
                "platform_days": days,
                "platform_width_pct": width_pct,
                "platform_quality": "strict" if width_pct <= STRICT_PLATFORM_WIDTH_LIMIT else "normal",
            }
            break

    if best is not None:
        return best

    fallback_days = min(20, len(recent))
    part = recent.tail(fallback_days)
    high = safe_float(part["high"].max())
    low = safe_float(part["low"].min())
    width_pct = (high / low - 1) * 100 if low > 0 else pd.NA

    return {
        "platform_start_date": str(part.iloc[0]["date"]),
        "platform_end_date": str(part.iloc[-1]["date"]),
        "platform_high": high,
        "platform_low": low,
        "platform_days": fallback_days,
        "platform_width_pct": width_pct,
        "platform_quality": "wide_reference",
    }


def detect_false_breakdown(df: pd.DataFrame, platform_low: float) -> tuple[bool, str, int]:
    if pd.isna(platform_low) or platform_low <= 0 or len(df) < 5:
        return False, "", 0

    recent = df.tail(12).reset_index(drop=True)

    for i in range(len(recent)):
        row = recent.iloc[i]

        if safe_float(row["low"]) < platform_low and safe_float(row["close"]) < platform_low:
            breakdown_date = str(row["date"])

            for j in range(i + 1, min(i + 4, len(recent))):
                recover_row = recent.iloc[j]

                if safe_float(recover_row["close"]) > platform_low:
                    return True, breakdown_date, j - i

    return False, "", 0


def detect_break_prior_high_hold(df: pd.DataFrame, prior_high: float) -> tuple[bool, str, bool]:
    if pd.isna(prior_high) or prior_high <= 0 or len(df) < 3:
        return False, "", False

    recent = df.tail(10).reset_index(drop=True)

    for i in range(len(recent)):
        if safe_float(recent.iloc[i]["close"]) > prior_high:
            break_date = str(recent.iloc[i]["date"])
            after = recent.iloc[i:]
            hold_days = min(3, len(after))
            hold = bool((after.head(hold_days)["close"] > prior_high).all())

            return True, break_date, hold

    return False, "", False


def calc_pattern_state_and_signal(
    close: float,
    platform_high: float,
    platform_low: float,
    break_above_platform_high: bool,
    break_below_platform_low: bool,
    false_breakdown: bool,
    break_prior_high: bool,
    break_prior_high_hold: bool,
    is_high_volume_upper_shadow: bool,
    is_high_volume_breakdown: bool,
    ma20: float,
    ema23: float,
    ma60: float,
) -> tuple[str, str, str, str]:
    action_trigger = []
    risk_note = []

    if false_breakdown:
        pattern_state = "false_breakdown_recovered"
        pattern_signal = "假跌破後收回，先不視為型態破壞"
        action_trigger.append("若後續守住平台下緣，可續抱觀察")
        action_trigger.append("若再度跌破平台且 3 日內收不回，轉為型態破壞")
    elif is_high_volume_breakdown:
        pattern_state = "breakdown"
        pattern_signal = "爆量跌破平台，型態風險升高"
        action_trigger.append("若 1～3 日內無法站回平台下緣，降低持股風險")
        risk_note.append("爆量跌破代表賣壓明確，不宜加碼")
    elif break_below_platform_low:
        pattern_state = "below_platform"
        pattern_signal = "收盤跌破平台下緣，等待是否快速收回"
        action_trigger.append("若 3 日內站回平台下緣，可視為假跌破")
        action_trigger.append("若 3 日內站不回，視為型態破壞")
        risk_note.append("跌破平台期間禁止加碼")
    elif is_high_volume_upper_shadow:
        pattern_state = "failed_breakout_risk"
        pattern_signal = "爆量長上影，疑似突破失敗或高檔換手"
        action_trigger.append("若隔日收復長上影高點，可解除部分疑慮")
        action_trigger.append("若跌回平台內且放量跌破平台，轉弱")
        risk_note.append("長上影後不追價加碼")
    elif break_prior_high and break_prior_high_hold:
        pattern_state = "prior_high_breakout_hold"
        pattern_signal = "突破前高且短線站穩"
        action_trigger.append("若回測前高不破，可續抱")
        action_trigger.append("若跌回前高下方且放量，視為突破失敗")
    elif break_prior_high:
        pattern_state = "prior_high_breakout_unconfirmed"
        pattern_signal = "突破前高但尚未確認站穩"
        action_trigger.append("等 1～3 日確認是否站穩突破價")
        risk_note.append("尚未站穩前不追價加碼")
    elif break_above_platform_high:
        pattern_state = "platform_breakout"
        pattern_signal = "收盤突破平台上緣"
        action_trigger.append("若 1～3 日守住平台上緣，型態轉強")
        action_trigger.append("若跌回平台內且出現長上影，視為突破失敗")
    elif not math.isnan(platform_high) and not math.isnan(platform_low) and close >= platform_low and close <= platform_high:
        pattern_state = "inside_platform"
        pattern_signal = "平台整理中"
        action_trigger.append("上緣突破站穩才轉強")
        action_trigger.append("下緣跌破後 3 日站不回才轉弱")
    elif not math.isnan(platform_high) and close > platform_high:
        pattern_state = "above_platform"
        pattern_signal = "位於平台上方"
        action_trigger.append("守住平台上緣可續抱")
    else:
        pattern_state = "weakening"
        pattern_signal = "低於主要平台，型態偏弱"
        action_trigger.append("站回平台下緣前，不建議加碼")
        risk_note.append("平台下方容易反彈失敗")

    if not math.isnan(ma20) and not math.isnan(ema23):
        if close < ma20 and close < ema23:
            risk_note.append("收盤低於 20MA 與 23EMA，短線結構偏弱")
        elif close > ma20 or close > ema23:
            action_trigger.append("仍在 20MA / 23EMA 附近或上方，觀察是否守穩")

    if not math.isnan(ma60) and close < ma60:
        risk_note.append("收盤低於 60MA，中期結構偏弱")

    return (
        pattern_state,
        pattern_signal,
        "；".join(action_trigger),
        "；".join(risk_note),
    )


def analyze_one_holding(price_df: pd.DataFrame, holding: dict) -> dict:
    stock_id = holding["stock_id"]
    stock_name = holding["stock_name"]

    stock_df = price_df[price_df["stock_id"] == stock_id].copy()
    stock_df = stock_df.sort_values("date").tail(180).reset_index(drop=True)

    if stock_df.empty:
        return {
            "stock_id": stock_id,
            "stock_name": stock_name,
            "date": "",
            "available_days": 0,
            "cost": holding["cost"],
            "lots": holding["lots"],
            "margin": holding["margin"],
            "pattern_state": "no_price_data",
            "pattern_signal": "找不到價格資料",
            "action_trigger": "確認 data/daily_price 是否已有此股票日線資料",
            "risk_note": "資料不足，不能做型態判斷",
            "chart_path": "",
        }

    stock_df = add_indicators(stock_df)

    latest = stock_df.iloc[-1]
    previous = stock_df.iloc[:-1].copy()

    available_days = len(stock_df)

    open_price = safe_float(latest["open"])
    high = safe_float(latest["high"])
    low = safe_float(latest["low"])
    close = safe_float(latest["close"])
    volume = safe_float(latest["volume"])
    trading_value = safe_float(latest["trading_value"])

    cost = safe_float(holding["cost"])
    lots = safe_float(holding["lots"])
    margin = bool(holding["margin"])

    unrealized_pnl = (close - cost) * lots * 1000 if cost > 0 else pd.NA
    unrealized_pnl_pct = (close / cost - 1) * 100 if cost > 0 else pd.NA

    high_180 = safe_float(stock_df["high"].max())
    low_180 = safe_float(stock_df["low"].min())
    high_60 = safe_float(stock_df.tail(60)["high"].max())
    low_60 = safe_float(stock_df.tail(60)["low"].min())
    high_20 = safe_float(stock_df.tail(20)["high"].max())
    low_20 = safe_float(stock_df.tail(20)["low"].min())

    if not previous.empty:
        swing_high_recent = safe_float(previous.tail(20)["high"].max())
        swing_low_recent = safe_float(previous.tail(20)["low"].min())
        prior_60_high = safe_float(previous.tail(60)["high"].max())
    else:
        swing_high_recent = pd.NA
        swing_low_recent = pd.NA
        prior_60_high = pd.NA

    platform = detect_platform(stock_df)
    platform_high = safe_float(platform["platform_high"])
    platform_low = safe_float(platform["platform_low"])

    close_vs_platform = ""
    is_above_platform = False
    is_inside_platform = False
    is_below_platform = False

    if not math.isnan(platform_high) and not math.isnan(platform_low):
        if close > platform_high:
            close_vs_platform = "above_platform"
            is_above_platform = True
        elif close < platform_low:
            close_vs_platform = "below_platform"
            is_below_platform = True
        else:
            close_vs_platform = "inside_platform"
            is_inside_platform = True

    break_above_platform_high = bool(not math.isnan(platform_high) and close > platform_high)
    break_below_platform_low = bool(not math.isnan(platform_low) and close < platform_low)

    false_breakdown, false_breakdown_date, false_breakdown_recovery_days = detect_false_breakdown(
        stock_df,
        platform_low,
    )

    break_prior_high, break_prior_high_date, break_prior_high_hold = detect_break_prior_high_hold(
        stock_df,
        prior_60_high,
    )

    upper_shadow_pct = (high - close) / high * 100 if high > 0 else pd.NA
    lower_shadow_pct = (close - low) / low * 100 if low > 0 else pd.NA

    volume_ma5 = safe_float(latest["volume_ma5"])
    volume_ma20 = safe_float(latest["volume_ma20"])
    volume_ratio_20 = safe_float(latest["volume_ratio_20"])

    is_high_volume_upper_shadow = bool(
        not math.isnan(upper_shadow_pct)
        and upper_shadow_pct >= 3
        and not math.isnan(volume_ratio_20)
        and volume_ratio_20 >= 1.5
        and close <= high * 0.97
    )

    is_high_volume_breakdown = bool(
        break_below_platform_low
        and not math.isnan(volume_ratio_20)
        and volume_ratio_20 >= 1.5
    )

    ema23 = safe_float(latest["ema23"])
    ma20 = safe_float(latest["ma20"])
    ma60 = safe_float(latest["ma60"])

    pattern_state, pattern_signal, action_trigger, risk_note = calc_pattern_state_and_signal(
        close=close,
        platform_high=platform_high,
        platform_low=platform_low,
        break_above_platform_high=break_above_platform_high,
        break_below_platform_low=break_below_platform_low,
        false_breakdown=false_breakdown,
        break_prior_high=break_prior_high,
        break_prior_high_hold=break_prior_high_hold,
        is_high_volume_upper_shadow=is_high_volume_upper_shadow,
        is_high_volume_breakdown=is_high_volume_breakdown,
        ma20=ma20,
        ema23=ema23,
        ma60=ma60,
    )

    if available_days < 180:
        if risk_note:
            risk_note += "；"
        risk_note += f"目前可用交易日數 {available_days} 日，未達 180 日"

    chart_path = CHART_DIR / f"{stock_id}_pattern.png"

    row = {
        "stock_id": stock_id,
        "stock_name": stock_name or str(latest.get("stock_name", "")),
        "date": str(latest["date"]),
        "available_days": available_days,

        "open": round_value(open_price),
        "high": round_value(high),
        "low": round_value(low),
        "close": round_value(close),
        "volume": round_value(volume, 0),
        "trading_value": round_value(trading_value, 0),

        "cost": round_value(cost),
        "lots": lots,
        "margin": margin,
        "unrealized_pnl": round_value(unrealized_pnl, 0),
        "unrealized_pnl_pct": round_value(unrealized_pnl_pct),

        "high_180": round_value(high_180),
        "low_180": round_value(low_180),
        "high_60": round_value(high_60),
        "low_60": round_value(low_60),
        "high_20": round_value(high_20),
        "low_20": round_value(low_20),

        "swing_high_recent": round_value(swing_high_recent),
        "swing_low_recent": round_value(swing_low_recent),

        "platform_start_date": platform["platform_start_date"],
        "platform_end_date": platform["platform_end_date"],
        "platform_high": round_value(platform_high),
        "platform_low": round_value(platform_low),
        "platform_days": platform["platform_days"],
        "platform_width_pct": round_value(platform["platform_width_pct"]),

        "close_vs_platform": close_vs_platform,
        "is_above_platform": is_above_platform,
        "is_inside_platform": is_inside_platform,
        "is_below_platform": is_below_platform,

        "break_above_platform_high": break_above_platform_high,
        "break_below_platform_low": break_below_platform_low,

        "false_breakdown": false_breakdown,
        "false_breakdown_date": false_breakdown_date,
        "false_breakdown_recovery_days": false_breakdown_recovery_days,

        "break_prior_high": break_prior_high,
        "break_prior_high_date": break_prior_high_date,
        "break_prior_high_hold": break_prior_high_hold,

        "upper_shadow_pct": round_value(upper_shadow_pct),
        "lower_shadow_pct": round_value(lower_shadow_pct),
        "is_high_volume_upper_shadow": is_high_volume_upper_shadow,
        "is_high_volume_breakdown": is_high_volume_breakdown,

        "volume_ma5": round_value(volume_ma5, 0),
        "volume_ma20": round_value(volume_ma20, 0),
        "volume_ratio_20": round_value(volume_ratio_20),

        "ema23": round_value(ema23),
        "ma20": round_value(ma20),
        "ma60": round_value(ma60),

        "pattern_state": pattern_state,
        "pattern_signal": pattern_signal,
        "action_trigger": action_trigger,
        "risk_note": risk_note,
        "chart_path": str(chart_path),
    }

    generate_chart(stock_df, row, chart_path)

    return row


def generate_chart(stock_df: pd.DataFrame, row: dict, chart_path: Path) -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    df = stock_df.copy().reset_index(drop=True)
    df["x"] = range(len(df))

    fig, (ax_price, ax_volume) = plt.subplots(
        2,
        1,
        figsize=(15, 8),
        sharex=True,
        gridspec_kw={"height_ratios": [3, 1]},
    )

    stock_id = row["stock_id"]
    stock_name = row["stock_name"]

    for _, r in df.iterrows():
        x = r["x"]
        open_price = safe_float(r["open"])
        high = safe_float(r["high"])
        low = safe_float(r["low"])
        close = safe_float(r["close"])

        color = "#d62728" if close >= open_price else "#2ca02c"

        ax_price.vlines(x, low, high, color=color, linewidth=0.8)
        ax_price.vlines(x, min(open_price, close), max(open_price, close), color=color, linewidth=3)

    ax_price.plot(df["x"], df["close"], linewidth=1.2, label="Close")

    for col, label in [
        ("ema23", "23EMA"),
        ("ma20", "20MA"),
        ("ma60", "60MA"),
    ]:
        if col in df.columns:
            ax_price.plot(df["x"], df[col], linewidth=1.0, label=label)

    cost = safe_float(row.get("cost"))
    platform_high = safe_float(row.get("platform_high"))
    platform_low = safe_float(row.get("platform_low"))
    high_60 = safe_float(row.get("high_60"))
    low_60 = safe_float(row.get("low_60"))

    if cost > 0:
        ax_price.axhline(cost, linestyle="--", linewidth=1.1, label=f"Cost {cost:.2f}")

    if not math.isnan(platform_high):
        ax_price.axhline(platform_high, linestyle="--", linewidth=1.0, label=f"Platform High {platform_high:.2f}")

    if not math.isnan(platform_low):
        ax_price.axhline(platform_low, linestyle="--", linewidth=1.0, label=f"Platform Low {platform_low:.2f}")

    if not math.isnan(high_60):
        ax_price.axhline(high_60, linestyle=":", linewidth=1.0, label=f"High60 {high_60:.2f}")

    if not math.isnan(low_60):
        ax_price.axhline(low_60, linestyle=":", linewidth=1.0, label=f"Low60 {low_60:.2f}")

    latest_x = df.iloc[-1]["x"]
    latest_close = safe_float(df.iloc[-1]["close"])

    ax_price.scatter([latest_x], [latest_close], s=50, zorder=5)
    ax_price.annotate(
        f"Close {latest_close:.2f}",
        xy=(latest_x, latest_close),
        xytext=(10, 10),
        textcoords="offset points",
        fontsize=9,
    )

    if row.get("false_breakdown") and row.get("false_breakdown_date"):
        event_date = str(row["false_breakdown_date"])
        event_rows = df[df["date"].astype(str) == event_date]

        if not event_rows.empty:
            ex = event_rows.iloc[0]["x"]
            ey = safe_float(event_rows.iloc[0]["low"])
            ax_price.scatter([ex], [ey], marker="v", s=80, zorder=6)
            ax_price.annotate("False breakdown", xy=(ex, ey), xytext=(5, -20), textcoords="offset points", fontsize=8)

    if row.get("break_prior_high") and row.get("break_prior_high_date"):
        event_date = str(row["break_prior_high_date"])
        event_rows = df[df["date"].astype(str) == event_date]

        if not event_rows.empty:
            ex = event_rows.iloc[0]["x"]
            ey = safe_float(event_rows.iloc[0]["high"])
            ax_price.scatter([ex], [ey], marker="^", s=80, zorder=6)
            ax_price.annotate("Break high", xy=(ex, ey), xytext=(5, 10), textcoords="offset points", fontsize=8)

    if row.get("is_high_volume_upper_shadow"):
        ax_price.annotate(
            "High vol upper shadow",
            xy=(latest_x, safe_float(df.iloc[-1]["high"])),
            xytext=(-120, 20),
            textcoords="offset points",
            fontsize=8,
        )

    if row.get("is_high_volume_breakdown"):
        ax_price.annotate(
            "High vol breakdown",
            xy=(latest_x, safe_float(df.iloc[-1]["low"])),
            xytext=(-120, -25),
            textcoords="offset points",
            fontsize=8,
        )

    ax_price.set_title(
        f"{stock_id} {stock_name} - 180D Pattern | {row.get('pattern_state', '')}",
        fontsize=13,
    )
    ax_price.set_ylabel("Price")
    ax_price.grid(True, alpha=0.25)
    ax_price.legend(loc="best", fontsize=8)

    ax_volume.bar(df["x"], df["volume"], width=0.8)

    if "volume_ma20" in df.columns:
        ax_volume.plot(df["x"], df["volume_ma20"], linewidth=1.0, label="Volume MA20")

    ax_volume.set_ylabel("Volume")
    ax_volume.grid(True, alpha=0.25)
    ax_volume.legend(loc="best", fontsize=8)
    ax_volume.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{x/1000:.0f}k"))

    tick_count = min(10, len(df))
    tick_positions = [int(i * (len(df) - 1) / max(tick_count - 1, 1)) for i in range(tick_count)]
    tick_labels = [str(df.iloc[i]["date"]) for i in tick_positions]

    ax_volume.set_xticks(tick_positions)
    ax_volume.set_xticklabels(tick_labels, rotation=45, ha="right")

    fig.tight_layout()
    fig.savefig(chart_path, dpi=140, bbox_inches="tight")
    plt.close(fig)


def write_markdown(rows: list[dict]) -> None:
    lines = []

    lines.append("# 目前持股 180 日型態分析")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- CSV：`{OUTPUT_CSV}`")
    lines.append(f"- 圖表資料夾：`{CHART_DIR}`")
    lines.append("")
    lines.append("說明：本報告只分析 `config/current_holdings.json` 內的目前持股，不找新標的。判斷語言以型態、價格、成交量、成本線、平台、假跌破、突破失敗、爆量跌破為主。")
    lines.append("")

    if not rows:
        lines.append("目前沒有可分析的持股。")
        OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
        return

    lines.append("## 總覽")
    lines.append("")
    lines.append("| 股票 | 收盤 | 成本 | 張數 | 損益 | 損益率% | 型態狀態 | 型態訊號 | 圖 |")
    lines.append("|---|---:|---:|---:|---:|---:|---|---|---|")

    for row in rows:
        chart_path = row.get("chart_path", "")
        chart_link = f"[圖]({chart_path})" if chart_path else ""

        lines.append(
            f"| {row.get('stock_id')} {row.get('stock_name')} "
            f"| {row.get('close', '')} "
            f"| {row.get('cost', '')} "
            f"| {row.get('lots', '')} "
            f"| {row.get('unrealized_pnl', '')} "
            f"| {row.get('unrealized_pnl_pct', '')} "
            f"| {row.get('pattern_state', '')} "
            f"| {row.get('pattern_signal', '')} "
            f"| {chart_link} |"
        )

    lines.append("")

    for row in rows:
        stock_id = row.get("stock_id", "")
        stock_name = row.get("stock_name", "")

        lines.append(f"## {stock_id} {stock_name}")
        lines.append("")
        lines.append(f"- 資料日期：`{row.get('date', '')}`")
        lines.append(f"- 可用交易日數：`{row.get('available_days', '')}`")
        lines.append(f"- 目前收盤：`{row.get('close', '')}`")
        lines.append(f"- 我的成本：`{row.get('cost', '')}`")
        lines.append(f"- 張數：`{row.get('lots', '')}`")
        lines.append(f"- 目前損益：`{row.get('unrealized_pnl', '')}`")
        lines.append(f"- 目前損益率：`{row.get('unrealized_pnl_pct', '')}%`")
        lines.append(f"- 圖表：`{row.get('chart_path', '')}`")
        lines.append("")

        lines.append("### 型態結構")
        lines.append("")
        lines.append(f"- 近 180 日高低：`{row.get('high_180', '')}` / `{row.get('low_180', '')}`")
        lines.append(f"- 近 60 日高低：`{row.get('high_60', '')}` / `{row.get('low_60', '')}`")
        lines.append(f"- 近 20 日高低：`{row.get('high_20', '')}` / `{row.get('low_20', '')}`")
        lines.append(
            f"- 目前平台：`{row.get('platform_low', '')}`～`{row.get('platform_high', '')}`，"
            f"平台天數 `{row.get('platform_days', '')}`，"
            f"寬度 `{row.get('platform_width_pct', '')}%`"
        )
        lines.append(f"- 是否突破前高：`{row.get('break_prior_high', '')}`")
        lines.append(f"- 是否跌破平台：`{row.get('break_below_platform_low', '')}`")
        lines.append(f"- 是否假跌破：`{row.get('false_breakdown', '')}`")
        lines.append(f"- 是否爆量長上影：`{row.get('is_high_volume_upper_shadow', '')}`")
        lines.append(f"- 是否爆量跌破：`{row.get('is_high_volume_breakdown', '')}`")
        lines.append("")

        lines.append("### 型態判斷")
        lines.append("")
        lines.append(f"- pattern_state：`{row.get('pattern_state', '')}`")
        lines.append(f"- pattern_signal：{row.get('pattern_signal', '')}")
        lines.append("")

        lines.append("### 交易觸發條件")
        lines.append("")

        trigger = row.get("action_trigger", "")

        if trigger:
            for item in str(trigger).split("；"):
                if item.strip():
                    lines.append(f"- {item.strip()}")
        else:
            lines.append("- 尚無明確觸發條件。")

        lines.append("")

        risk_note = row.get("risk_note", "")

        if risk_note:
            lines.append("### 風險註記")
            lines.append("")

            for item in str(risk_note).split("；"):
                if item.strip():
                    lines.append(f"- {item.strip()}")

            lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    holdings = load_current_holdings()
    price_df = load_daily_price_history()

    rows = []

    for holding in holdings:
        print(f"Analyze holding: {holding['stock_id']} {holding['stock_name']}")
        row = analyze_one_holding(price_df, holding)
        rows.append(row)

    out = pd.DataFrame(rows)

    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = pd.NA

    out = out[OUTPUT_COLUMNS].copy()
    out.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    write_markdown(rows)

    print(f"Saved CSV: {OUTPUT_CSV}")
    print(f"Saved Markdown: {OUTPUT_MD}")
    print(f"Saved charts: {CHART_DIR}")
    print(f"Rows: {len(rows)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
