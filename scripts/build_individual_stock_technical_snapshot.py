from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pandas as pd

from tracking_utils import LATEST_DIR, main_price_date_from_freshness, normalize_code, read_csv, safe_str, write_csv


PRICE_DIR = Path("data/stock_price_history")
ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
OUT_CSV = LATEST_DIR / "individual_stock_technical_snapshot_latest.csv"
OUT_MD = LATEST_DIR / "individual_stock_technical_snapshot_latest.md"


SNAPSHOT_COLUMNS = [
    "signal_date",
    "stock_id",
    "stock_name",
    "close",
    "volume",
    "volume_ratio",
    "ema23",
    "ma20",
    "ma60",
    "ma120",
    "distance_to_ema23_pct",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "high_20",
    "high_60",
    "high_120",
    "low_20",
    "low_60",
    "low_120",
    "support_1",
    "support_2",
    "resistance_1",
    "resistance_2",
    "macd_dif",
    "macd_dea",
    "macd_hist",
    "rsi6",
    "rsi14",
    "kd_k",
    "kd_d",
    "kd_j",
    "boll_mid",
    "boll_upper",
    "boll_lower",
    "atr",
    "atr_pct",
    "obv",
    "obv_ma20",
    "obv_vs_ma20",
    "mfi",
    "cmf",
    "price_position_summary_zh",
    "technical_summary_zh",
    "support_resistance_summary_zh",
    "buy_condition_text_zh",
    "take_profit_text_zh",
    "exit_condition_text_zh",
    "risk_control_text_zh",
]


def num(value: Any) -> float:
    try:
        if value is None or value == "":
            return math.nan
        return float(value)
    except Exception:
        return math.nan


def pct(value: float) -> str:
    if math.isnan(value):
        return "資料不足"
    return f"{value:.2f}%"


def round_or_blank(value: float, digits: int = 4) -> Any:
    if math.isnan(value):
        return ""
    return round(value, digits)


def rsi(close: pd.Series, window: int) -> pd.Series:
    diff = close.diff()
    gain = diff.clip(lower=0).rolling(window).mean()
    loss = (-diff.clip(upper=0)).rolling(window).mean()
    rs = gain / loss.replace(0, math.nan)
    return 100 - (100 / (1 + rs))


def compute_snapshot(path: Path, signal_date: str, fallback_name: str = "") -> dict[str, Any] | None:
    try:
        df = pd.read_csv(path, dtype={"stock_id": str})
    except Exception:
        return None
    required = {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}
    if not required.issubset(df.columns):
        return None
    df = df.copy()
    df["date"] = df["date"].astype(str)
    df = df[df["date"] <= signal_date].sort_values("date")
    if len(df) < 35:
        return None
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["open", "high", "low", "close"])
    if df.empty:
        return None

    close = df["close"]
    high = df["high"]
    low = df["low"]
    volume = df["volume"].fillna(0)

    df["ema23_calc"] = close.ewm(span=23, adjust=False).mean()
    df["ma20_calc"] = close.rolling(20).mean()
    df["ma60_calc"] = close.rolling(60).mean()
    df["ma120_calc"] = close.rolling(120).mean()
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    df["macd_dif_calc"] = ema12 - ema26
    df["macd_dea_calc"] = df["macd_dif_calc"].ewm(span=9, adjust=False).mean()
    df["macd_hist_calc"] = df["macd_dif_calc"] - df["macd_dea_calc"]
    df["rsi6_calc"] = rsi(close, 6)
    df["rsi14_calc"] = rsi(close, 14)

    low9 = low.rolling(9).min()
    high9 = high.rolling(9).max()
    rsv = (close - low9) / (high9 - low9).replace(0, math.nan) * 100
    df["kd_k_calc"] = rsv.ewm(alpha=1 / 3, adjust=False).mean()
    df["kd_d_calc"] = df["kd_k_calc"].ewm(alpha=1 / 3, adjust=False).mean()
    df["kd_j_calc"] = 3 * df["kd_k_calc"] - 2 * df["kd_d_calc"]

    mid = close.rolling(20).mean()
    std = close.rolling(20).std()
    df["boll_mid_calc"] = mid
    df["boll_upper_calc"] = mid + 2 * std
    df["boll_lower_calc"] = mid - 2 * std

    prev_close = close.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)
    df["atr_calc"] = tr.rolling(14).mean()

    direction = close.diff().fillna(0).map(lambda x: 1 if x > 0 else -1 if x < 0 else 0)
    df["obv_calc"] = (direction * volume).cumsum()
    df["obv_ma20_calc"] = df["obv_calc"].rolling(20).mean()

    typical = (high + low + close) / 3
    money_flow = typical * volume
    positive = money_flow.where(typical.diff() > 0, 0).rolling(14).sum()
    negative = money_flow.where(typical.diff() < 0, 0).rolling(14).sum().abs()
    money_ratio = positive / negative.replace(0, math.nan)
    df["mfi_calc"] = 100 - (100 / (1 + money_ratio))

    mfv = (((close - low) - (high - close)) / (high - low).replace(0, math.nan)) * volume
    df["cmf_calc"] = mfv.rolling(20).sum() / volume.rolling(20).sum().replace(0, math.nan)

    latest = df.iloc[-1]
    latest_date = safe_str(latest.get("date"))
    if signal_date and latest_date != signal_date:
        return None
    stock_id = normalize_code(latest.get("stock_id", path.stem))
    stock_name = safe_str(latest.get("stock_name", "")) or fallback_name
    close_v = num(latest.get("close"))
    ema23 = num(latest.get("ema23", latest.get("ema23_calc")))
    ma20 = num(latest.get("ma20", latest.get("ma20_calc")))
    ma60 = num(latest.get("ma60", latest.get("ma60_calc")))
    ma120 = num(latest.get("ma120", latest.get("ma120_calc")))
    vol_ratio = num(latest.get("volume_ratio"))
    if math.isnan(vol_ratio):
        vol_ma20 = volume.tail(20).mean()
        vol_ratio = num(latest.get("volume")) / vol_ma20 if vol_ma20 else math.nan

    high_20 = num(latest.get("high_20", high.tail(20).max()))
    high_60 = num(latest.get("high_60", high.tail(60).max()))
    high_120 = num(latest.get("high_120", high.tail(120).max()))
    low_20 = num(latest.get("low_20", low.tail(20).min()))
    low_60 = num(latest.get("low_60", low.tail(60).min()))
    low_120 = num(latest.get("low_120", low.tail(120).min()))

    support_1 = max([v for v in [ema23, ma20, low_20] if not math.isnan(v)], default=math.nan)
    support_2 = max([v for v in [ma60, low_60] if not math.isnan(v)], default=math.nan)
    resistance_1 = high_20
    resistance_2 = high_60

    distance_ema23 = (close_v / ema23 - 1) * 100 if ema23 and not math.isnan(ema23) else math.nan
    distance_ma20 = (close_v / ma20 - 1) * 100 if ma20 and not math.isnan(ma20) else math.nan
    distance_ma60 = (close_v / ma60 - 1) * 100 if ma60 and not math.isnan(ma60) else math.nan
    atr = num(latest.get("atr_calc"))
    atr_pct = atr / close_v * 100 if close_v and not math.isnan(atr) else math.nan
    macd_hist = num(latest.get("macd_hist_calc"))
    rsi14 = num(latest.get("rsi14_calc"))
    kd_k = num(latest.get("kd_k_calc"))
    kd_d = num(latest.get("kd_d_calc"))
    obv = num(latest.get("obv_calc"))
    obv_ma20 = num(latest.get("obv_ma20_calc"))
    obv_vs = "高於20日均" if not math.isnan(obv) and not math.isnan(obv_ma20) and obv >= obv_ma20 else "低於20日均" if not math.isnan(obv) and not math.isnan(obv_ma20) else "資料不足"

    position_parts = [
        f"收盤{close_v:.2f}" if not math.isnan(close_v) else "收盤資料不足",
        f"距23EMA {pct(distance_ema23)}",
        f"距MA20 {pct(distance_ma20)}",
        f"量比{vol_ratio:.2f}x" if not math.isnan(vol_ratio) else "量比資料不足",
    ]
    technical_parts = [
        "MACD柱狀體偏多" if macd_hist > 0 else "MACD柱狀體偏弱" if not math.isnan(macd_hist) else "MACD資料不足",
        "RSI偏熱" if rsi14 >= 70 else "RSI中性偏強" if rsi14 >= 50 else "RSI偏弱" if not math.isnan(rsi14) else "RSI資料不足",
        "KD多方" if kd_k > kd_d else "KD偏弱" if not math.isnan(kd_k) and not math.isnan(kd_d) else "KD資料不足",
        f"OBV{obv_vs}",
    ]
    sr = f"支撐觀察 {round_or_blank(support_1, 2)} / {round_or_blank(support_2, 2)}；壓力觀察 {round_or_blank(resistance_1, 2)} / {round_or_blank(resistance_2, 2)}"
    buy_text = f"若回測支撐{round_or_blank(support_1, 2)}不破或放量站上壓力{round_or_blank(resistance_1, 2)}，可依模型條件執行第一筆。"
    take_profit = f"接近壓力{round_or_blank(resistance_1, 2)}到{round_or_blank(resistance_2, 2)}且爆量不漲時，分批停利。"
    exit_text = f"跌破{round_or_blank(support_1, 2)}且隔日站不回，或放量長黑跌破近期低點，退出或降風險。"

    return {
        "signal_date": safe_str(latest.get("date")),
        "stock_id": stock_id,
        "stock_name": stock_name,
        "close": round_or_blank(close_v, 4),
        "volume": round_or_blank(num(latest.get("volume")), 2),
        "volume_ratio": round_or_blank(vol_ratio, 4),
        "ema23": round_or_blank(ema23, 4),
        "ma20": round_or_blank(ma20, 4),
        "ma60": round_or_blank(ma60, 4),
        "ma120": round_or_blank(ma120, 4),
        "distance_to_ema23_pct": round_or_blank(distance_ema23, 4),
        "distance_to_ma20_pct": round_or_blank(distance_ma20, 4),
        "distance_to_ma60_pct": round_or_blank(distance_ma60, 4),
        "high_20": round_or_blank(high_20, 4),
        "high_60": round_or_blank(high_60, 4),
        "high_120": round_or_blank(high_120, 4),
        "low_20": round_or_blank(low_20, 4),
        "low_60": round_or_blank(low_60, 4),
        "low_120": round_or_blank(low_120, 4),
        "support_1": round_or_blank(support_1, 4),
        "support_2": round_or_blank(support_2, 4),
        "resistance_1": round_or_blank(resistance_1, 4),
        "resistance_2": round_or_blank(resistance_2, 4),
        "macd_dif": round_or_blank(num(latest.get("macd_dif_calc")), 4),
        "macd_dea": round_or_blank(num(latest.get("macd_dea_calc")), 4),
        "macd_hist": round_or_blank(macd_hist, 4),
        "rsi6": round_or_blank(num(latest.get("rsi6_calc")), 4),
        "rsi14": round_or_blank(rsi14, 4),
        "kd_k": round_or_blank(kd_k, 4),
        "kd_d": round_or_blank(kd_d, 4),
        "kd_j": round_or_blank(num(latest.get("kd_j_calc")), 4),
        "boll_mid": round_or_blank(num(latest.get("boll_mid_calc")), 4),
        "boll_upper": round_or_blank(num(latest.get("boll_upper_calc")), 4),
        "boll_lower": round_or_blank(num(latest.get("boll_lower_calc")), 4),
        "atr": round_or_blank(atr, 4),
        "atr_pct": round_or_blank(atr_pct, 4),
        "obv": round_or_blank(obv, 2),
        "obv_ma20": round_or_blank(obv_ma20, 2),
        "obv_vs_ma20": obv_vs,
        "mfi": round_or_blank(num(latest.get("mfi_calc")), 4),
        "cmf": round_or_blank(num(latest.get("cmf_calc")), 4),
        "price_position_summary_zh": "；".join(position_parts),
        "technical_summary_zh": "；".join(technical_parts),
        "support_resistance_summary_zh": sr,
        "buy_condition_text_zh": buy_text,
        "take_profit_text_zh": take_profit,
        "exit_condition_text_zh": exit_text,
        "risk_control_text_zh": "模型入選後仍需依支撐、23EMA、量價失敗與TDCC轉弱做管理；風險標籤不作為事後否決模型命中。",
    }


def candidate_universe() -> dict[str, str]:
    names: dict[str, str] = {}
    for path in [ALL_CANDIDATES, MODEL_SIGNALS]:
        df = read_csv(path, dtype={"stock_id": str})
        if df.empty:
            continue
        for _, row in df.iterrows():
            code = normalize_code(row.get("stock_id", ""))
            if code:
                names.setdefault(code, safe_str(row.get("stock_name", "")))
    if names:
        return names
    for path in PRICE_DIR.glob("*.csv"):
        names[path.stem] = ""
    return names


def write_md(df: pd.DataFrame) -> None:
    lines = [
        "# Individual Stock Technical Snapshot",
        "",
        "- One row per stock currently needed by the daily candidate reports.",
        "- This is a PDF-ready technical context table. It does not select stocks.",
        "",
    ]
    preview_cols = [
        "stock_id",
        "stock_name",
        "close",
        "volume_ratio",
        "ema23",
        "ma20",
        "support_1",
        "resistance_1",
        "technical_summary_zh",
    ]
    if df.empty:
        lines.append("No snapshot rows.")
    else:
        lines.append(df[preview_cols].head(80).to_markdown(index=False))
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    signal_date = main_price_date_from_freshness()
    names = candidate_universe()
    rows: list[dict[str, Any]] = []
    for stock_id, name in sorted(names.items()):
        path = PRICE_DIR / f"{stock_id}.csv"
        if not path.exists():
            continue
        row = compute_snapshot(path, signal_date, name)
        if row:
            rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        df = pd.DataFrame(columns=SNAPSHOT_COLUMNS)
    else:
        for col in SNAPSHOT_COLUMNS:
            if col not in df.columns:
                df[col] = ""
        df = df[SNAPSHOT_COLUMNS].sort_values("stock_id")
    write_csv(df, OUT_CSV)
    write_md(df)
    print(f"Saved: {OUT_CSV} rows={len(df)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
