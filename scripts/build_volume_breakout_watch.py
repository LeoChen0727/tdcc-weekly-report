from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import argparse
import math
import os
from typing import Any

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
HISTORY_DIR = ROOT / "output" / "history" / "volume_breakout"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
WARRANT_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"

WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
WATCH_MD = LATEST_DIR / "volume_breakout_watch_latest.md"
BACKTEST_CSV = LATEST_DIR / "volume_breakout_backtest_latest.csv"
BACKTEST_MD = LATEST_DIR / "volume_breakout_backtest_latest.md"
EVENT_LOG_CSV = HISTORY_DIR / "volume_breakout_event_log.csv"
PACKET_MD = LATEST_DIR / "volume_breakout_chatgpt_packet_latest.md"

RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"
VOLUME_BREAKOUT_RULE_VERSION = "bottom_volume_attack_v2_locked_limit_up"

HORIZONS = [1, 3, 5, 10, 20]

WATCH_COLUMNS = [
    "volume_breakout_rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "market",
    "close",
    "open",
    "high",
    "low",
    "volume",
    "volume_ma20",
    "volume_ratio",
    "return_1d",
    "return_5d",
    "return_20d",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "distance_to_previous_20d_high_pct",
    "distance_to_previous_60d_high_pct",
    "ma20",
    "ma60",
    "ema23",
    "previous_20d_high",
    "previous_60d_high",
    "previous_20d_low",
    "previous_60d_low",
    "range_window",
    "range_high",
    "range_low",
    "range_width_pct",
    "range_breakout_pct",
    "close_above_range_high",
    "high_above_range_high",
    "volume_breakout_type",
    "volume_watch_scope",
    "volume_breakout_score",
    "volume_breakout_notes",
    "false_breakout_risk_calc",
    "overheated_breakout",
    "industry",
    "category",
    "pattern_stage",
    "tdcc_status",
    "repeat_appear_label",
    "warrant_flow_signal",
    "volume_breakout_priority",
    "selection_status",
    "not_selected_reason",
    "risk_flags",
    "next_volume_breakout_confirmation",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


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


def safe_bool(value: Any) -> bool:
    text = safe_str(value).lower()
    return text in {"1", "true", "t", "yes", "y", "是"}


def pct_text(value: Any, digits: int = 1) -> str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}%"


def num_text(value: Any, digits: int = 2) -> str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()
    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_stock_id)
    return df


def normalize_date(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def latest_main_date() -> str:
    df = read_csv(FRESHNESS_CSV)
    if not df.empty and "main_price_date" in df.columns:
        return normalize_date(df.iloc[0].get("main_price_date", ""))
    return ""


def ensure_numeric(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def add_price_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = df["date"].map(normalize_date)
    df = df[df["date"] != ""].sort_values("date").reset_index(drop=True)
    numeric_cols = ["open", "high", "low", "close", "volume", "ma5", "ma10", "ma20", "ma60", "ema23", "volume_ma20"]
    df = ensure_numeric(df, numeric_cols)
    if "ma5" not in df.columns or df["ma5"].isna().all():
        df["ma5"] = df["close"].rolling(5, min_periods=5).mean()
    if "ma10" not in df.columns or df["ma10"].isna().all():
        df["ma10"] = df["close"].rolling(10, min_periods=10).mean()
    if "ma20" not in df.columns or df["ma20"].isna().all():
        df["ma20"] = df["close"].rolling(20, min_periods=20).mean()
    if "ma60" not in df.columns or df["ma60"].isna().all():
        df["ma60"] = df["close"].rolling(60, min_periods=60).mean()
    if "ema23" not in df.columns or df["ema23"].isna().all():
        df["ema23"] = df["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    if "volume_ma20" not in df.columns or df["volume_ma20"].isna().all():
        df["volume_ma20"] = df["volume"].rolling(20, min_periods=20).mean()
    df["volume_ratio_calc"] = df["volume"] / df["volume_ma20"].replace(0, pd.NA)
    if "volume_ratio" not in df.columns:
        df["volume_ratio"] = df["volume_ratio_calc"]
    else:
        df["volume_ratio"] = pd.to_numeric(df["volume_ratio"], errors="coerce").fillna(df["volume_ratio_calc"])
    for days in [1, 5, 20, 60]:
        df[f"return_{days}d_calc"] = (df["close"] / df["close"].shift(days) - 1.0) * 100.0
        col = f"return_{days}d"
        if col not in df.columns:
            df[col] = df[f"return_{days}d_calc"]
        else:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(df[f"return_{days}d_calc"])
    df["previous_20d_high_calc"] = df["high"].shift(1).rolling(20, min_periods=20).max()
    df["previous_60d_high_calc"] = df["high"].shift(1).rolling(60, min_periods=60).max()
    df["previous_20d_low_calc"] = df["low"].shift(1).rolling(20, min_periods=20).min()
    df["previous_60d_low_calc"] = df["low"].shift(1).rolling(60, min_periods=60).min()
    df["previous_close_calc"] = df["close"].shift(1)
    df["distance_to_ma20_calc"] = (df["close"] / df["ma20"] - 1.0) * 100.0
    df["distance_to_ma60_calc"] = (df["close"] / df["ma60"] - 1.0) * 100.0
    df["distance_to_previous_20d_high_calc"] = (df["close"] / df["previous_20d_high_calc"] - 1.0) * 100.0
    df["distance_to_previous_60d_high_calc"] = (df["close"] / df["previous_60d_high_calc"] - 1.0) * 100.0
    df["close_position_in_range"] = (df["close"] - df["low"]) / (df["high"] - df["low"]).replace(0, pd.NA)
    df["upper_shadow_pct"] = (df["high"] - df[["close", "open"]].max(axis=1)) / df["close"].replace(0, pd.NA) * 100.0
    df["daily_return_calc"] = (df["close"] / df["close"].shift(1) - 1.0) * 100.0
    return df


@dataclass
class BreakoutSignal:
    event_type: str
    score: float
    notes: list[str]
    scope: str = ""


def normalize_volume_ma20_lots(value: Any) -> float:
    raw = safe_float(value)
    if math.isnan(raw):
        return math.nan
    return raw / 1000.0 if raw >= 100000 else raw


def bottom_volume_breakout_level(value: Any) -> float:
    prev20 = safe_float(value)
    if math.isnan(prev20) or prev20 <= 0:
        return math.nan
    return prev20 * 1.02


def signal_return_pct(row: pd.Series) -> float:
    ret = safe_float(row.get("daily_return_calc"))
    if not math.isnan(ret):
        return ret
    ret = safe_float(row.get("return_1d"))
    if not math.isnan(ret):
        return ret
    close = safe_float(row.get("close"))
    prev_close = safe_float(row.get("previous_close_calc"))
    if math.isnan(close) or math.isnan(prev_close) or prev_close <= 0:
        return math.nan
    return (close / prev_close - 1.0) * 100.0


def locked_limit_up_breakout(row: pd.Series) -> bool:
    close = safe_float(row.get("close"))
    open_ = safe_float(row.get("open"))
    high = safe_float(row.get("high"))
    low = safe_float(row.get("low"))
    prev_close = safe_float(row.get("previous_close_calc"))
    breakout_level = bottom_volume_breakout_level(row.get("previous_20d_high_calc"))
    ret = signal_return_pct(row)
    if any(
        math.isnan(x)
        for x in [close, open_, high, low, breakout_level, ret]
    ):
        return False
    if high == low:
        range_pct = 0.0
    else:
        if math.isnan(prev_close) or prev_close <= 0:
            return False
        range_pct = (high - low) / prev_close * 100.0
    locked_or_tight_range = high == low or range_pct <= 1.0
    return (
        close >= breakout_level
        and ret >= 9.0
        and close >= high * 0.995
        and open_ >= close * 0.995
        and locked_or_tight_range
    )


def locked_limit_up_breakout_mask(df: pd.DataFrame) -> pd.Series:
    close = pd.to_numeric(df["close"], errors="coerce")
    open_ = pd.to_numeric(df["open"], errors="coerce")
    high = pd.to_numeric(df["high"], errors="coerce")
    low = pd.to_numeric(df["low"], errors="coerce")
    prev_close = pd.to_numeric(df["previous_close_calc"], errors="coerce")
    prev20 = pd.to_numeric(df["previous_20d_high_calc"], errors="coerce")
    ret = pd.to_numeric(df["daily_return_calc"], errors="coerce")
    if "return_1d" in df.columns:
        ret = ret.fillna(pd.to_numeric(df["return_1d"], errors="coerce"))
    ret = ret.fillna((close / prev_close.replace(0, pd.NA) - 1.0) * 100.0)
    range_pct = (high - low) / prev_close.replace(0, pd.NA) * 100.0
    locked_or_tight_range = high.eq(low) | range_pct.le(1.0)
    return (
        (close >= prev20 * 1.02)
        & (ret >= 9.0)
        & (close >= high * 0.995)
        & (open_ >= close * 0.995)
        & locked_or_tight_range
    ).fillna(False)


def scope_for_event_type(event_type: Any) -> str:
    text = safe_str(event_type)
    if text == "bottom_volume_attack":
        return "bottom_volume_attack"
    return ""


def detect_volume_breakout(row: pd.Series) -> BreakoutSignal | None:
    close = safe_float(row.get("close"))
    open_ = safe_float(row.get("open"))
    high = safe_float(row.get("high"))
    low = safe_float(row.get("low"))
    volume_ratio = safe_float(row.get("volume_ratio"))
    prev20 = safe_float(row.get("previous_20d_high_calc"))
    prev_close = safe_float(row.get("previous_close_calc"))
    volume_ma20_lots = normalize_volume_ma20_lots(row.get("volume_ma20"))
    close_pos = safe_float(row.get("close_position_in_range"))
    upper_shadow = safe_float(row.get("upper_shadow_pct"))

    breakout_level = bottom_volume_breakout_level(prev20)
    if any(math.isnan(x) for x in [close, open_, high, low, breakout_level]):
        return None
    bullish_candle = close > open_ or (close == open_ and not math.isnan(prev_close) and close > prev_close)
    locked_limit_attack = locked_limit_up_breakout(row)
    normal_volume_attack = (
        not any(math.isnan(x) for x in [volume_ratio, volume_ma20_lots])
        and close >= breakout_level
        and volume_ratio >= 2.0
        and volume_ma20_lots >= 1000
        and bullish_candle
    )
    if not (normal_volume_attack or locked_limit_attack):
        return None

    notes: list[str] = []
    score = 35.0
    notes.append("close_ge_prior20_high_102pct")
    if normal_volume_attack:
        notes.append("volume_ma20_lots_ge_1000")
        notes.append("volume_ratio_ge_2")
    else:
        notes.append("locked_limit_up_breakout")
        notes.append("locked_limit_no_volume_gate")
        score += 8
        if high == low:
            notes.append("one_price_limit_up")
            score += 4
    breakout_pct = (close / breakout_level - 1.0) * 100.0
    score += min(12.0, max(0.0, breakout_pct * 1.5))
    if normal_volume_attack:
        score += min(20.0, max(0.0, (volume_ratio - 2.0) * 4.0))
    if not math.isnan(close_pos):
        if close_pos >= 0.97:
            score += 5
            notes.append("close_near_day_high")
        elif close_pos >= 0.85:
            score += 3
            notes.append("close_high_position")
        elif close_pos >= 0.70:
            score += 1
            notes.append("close_above_mid_high")
    if high > low and close > open_:
        body_ratio = (close - open_) / (high - low)
        if body_ratio >= 0.65:
            score += 5
            notes.append("strong_red_body")
        elif body_ratio >= 0.35:
            score += 2
            notes.append("red_body_confirmed")
    if upper_shadow >= 3:
        score -= 6
        notes.append("long_upper_shadow_quality_penalty")
    score = max(0.0, min(100.0, score))
    return BreakoutSignal(event_type="bottom_volume_attack", score=round(score, 2), notes=notes, scope="bottom_volume_attack")


def _select_latest_signal_row(df: pd.DataFrame, target_date: str) -> pd.Series | None:
    """Return the row that is eligible for latest outputs.

    Latest report files must not silently fall back to stale per-stock history.
    If the report main_price_date is known, only that exact trading-date row is
    eligible.  Historical scans/backtests remain handled separately.
    """
    if df.empty:
        return None
    if target_date:
        dated = df[df["date"].map(normalize_date).eq(target_date)]
        if dated.empty:
            return None
        return dated.iloc[-1]
    return df.iloc[-1]


def merge_context(watch: pd.DataFrame) -> pd.DataFrame:
    if watch.empty:
        return watch
    out = watch.copy()
    all_candidates = read_csv(ALL_CANDIDATES_CSV)
    repeat = read_csv(REPEAT_CSV)
    warrant = read_csv(WARRANT_CSV)

    if not all_candidates.empty:
        keep = [
            "stock_id",
            "category",
            "category_cn",
            "breakout_type",
            "pattern_stage",
            "volume_confirmed_breakout",
            "platform_breakout_flag",
            "neckline_breakout_flag",
            "breakout_close_near_high_flag",
            "false_breakout_risk",
            "tdcc_status",
            "revaluation_priority",
            "score",
            "rank",
            "細分族群",
            "theme_group",
            "already_priced_in",
            "distribution_warning",
        ]
        existing = [c for c in keep if c in all_candidates.columns]
        ac = all_candidates[existing].drop_duplicates("stock_id", keep="first")
        out = out.merge(ac, on="stock_id", how="left")

    if not repeat.empty:
        keep = [
            "stock_id",
            "consecutive_appear_days_any_category",
            "consecutive_appear_days_same_category",
            "appear_count_5d",
            "appear_count_10d",
            "appear_count_20d",
            "repeat_appear_label",
            "repeat_appear_note",
            "multi_category_flags",
        ]
        existing = [c for c in keep if c in repeat.columns]
        rep = repeat[existing].drop_duplicates("stock_id", keep="first")
        out = out.merge(rep, on="stock_id", how="left")

    if not warrant.empty:
        keep = ["stock_id", "warrant_flow_signal", "warrant_flow_score", "warrant_flow_warning", "call_warrant_count", "put_warrant_count"]
        existing = [c for c in keep if c in warrant.columns]
        war = warrant[existing].drop_duplicates("stock_id", keep="first")
        out = out.merge(war, on="stock_id", how="left")

    return classify_watch(out)


def classify_watch(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in df.iterrows():
        d = row.to_dict()
        tdcc_status = safe_str(row.get("tdcc_status"))
        repeat_label = safe_str(row.get("repeat_appear_label"))

        risk_flags: list[str] = []
        if tdcc_status == "distribution_warning":
            risk_flags.append("tdcc_distribution_warning")
        if repeat_label in {"stale_signal", "continued_overheated"}:
            risk_flags.append(repeat_label)
        notes = safe_str(row.get("volume_breakout_notes"))
        if "long_upper_shadow_quality_penalty" in notes:
            risk_flags.append("long_upper_shadow_quality_penalty")
        if safe_str(row.get("already_priced_in")).lower() == "true":
            risk_flags.append("already_priced_in")

        priority = "A_bottom_volume_attack"
        if "tdcc_distribution_warning" in risk_flags:
            priority = "B_bottom_volume_attack_with_risk"
        next_confirmation = "以訊號日隔天開盤作為研究觀察基準；若跌回前20日高點突破基準、量價失敗或TDCC轉弱，則標記風險升高。"

        d.update(
            {
                "volume_breakout_priority": priority,
                "selection_status": "selected",
                "not_selected_reason": "",
                "risk_flags": "|".join(dict.fromkeys(risk_flags)),
                "next_volume_breakout_confirmation": next_confirmation,
            }
        )
        rows.append(d)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    order = {"A_bottom_volume_attack": 0, "B_bottom_volume_attack_with_risk": 1}
    out["_priority_order"] = out["volume_breakout_priority"].map(order).fillna(9)
    out["_score"] = pd.to_numeric(out["volume_breakout_score"], errors="coerce").fillna(0)
    out = out.sort_values(["_priority_order", "_score", "volume_ratio"], ascending=[True, False, False]).drop(columns=["_priority_order", "_score"])
    out.insert(0, "volume_breakout_rank", range(1, len(out) + 1))
    return out


def build_event_log() -> pd.DataFrame:
    events: list[dict[str, Any]] = []
    for path in sorted(PRICE_HISTORY_DIR.glob("*.csv")):
        df = read_csv(path)
        if df.empty or len(df) < 80:
            continue
        if not {"date", "stock_id", "stock_name", "close", "high", "low", "volume"}.issubset(df.columns):
            continue
        df = add_price_metrics(df)
        close = pd.to_numeric(df["close"], errors="coerce")
        open_ = pd.to_numeric(df["open"], errors="coerce")
        volume_ratio = pd.to_numeric(df["volume_ratio"], errors="coerce")
        prev_close = pd.to_numeric(df["previous_close_calc"], errors="coerce")
        prev20 = pd.to_numeric(df["previous_20d_high_calc"], errors="coerce")
        volume_ma20 = pd.to_numeric(df["volume_ma20"], errors="coerce")
        volume_ma20_lots = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
        breakout_level = prev20 * 1.02
        bullish = (close > open_) | ((close == open_) & (close > prev_close))
        normal_volume_attack = (
            (close >= breakout_level)
            & (volume_ratio >= 2.0)
            & (volume_ma20_lots >= 1000)
            & bullish
        )
        bottom_volume_attack = normal_volume_attack | locked_limit_up_breakout_mask(df)
        event_type = pd.Series("", index=df.index, dtype="object")
        event_type.loc[bottom_volume_attack] = "bottom_volume_attack"

        event_indices = event_type[event_type != ""].index.tolist()
        for idx in event_indices:
            row = df.iloc[idx]
            close = safe_float(row.get("close"))
            if math.isnan(close) or close <= 0:
                continue
            signal = detect_volume_breakout(row)
            score = signal.score if signal else 0
            signal_notes = signal.notes if signal else []
            signal_type = event_type.loc[idx]
            signal_scope = signal.scope if signal and signal.scope else scope_for_event_type(signal_type)
            event: dict[str, Any] = {
                "event_date": normalize_date(row.get("date")),
                "stock_id": normalize_stock_id(row.get("stock_id")),
                "stock_name": safe_str(row.get("stock_name")),
                "market": safe_str(row.get("market")),
                "volume_breakout_type": signal_type,
                "volume_watch_scope": signal_scope,
                "volume_breakout_rule_version": VOLUME_BREAKOUT_RULE_VERSION,
                "volume_breakout_score": score,
                "volume_ratio": row.get("volume_ratio"),
                "return_5d_before": row.get("return_5d"),
                "return_20d_before": row.get("return_20d"),
                "distance_to_ma20_pct": row.get("distance_to_ma20_calc"),
                "false_breakout_risk": "False",
                "overheated_breakout": "False",
                "close_on_event": close,
            }
            for horizon in HORIZONS:
                future = df.iloc[idx + 1 : idx + 1 + horizon]
                matured = len(future) >= horizon
                event[f"mature_d{horizon}"] = bool(matured)
                if matured:
                    close_d = safe_float(future.iloc[horizon - 1].get("close"))
                    max_high = pd.to_numeric(future["high"], errors="coerce").max()
                    min_low = pd.to_numeric(future["low"], errors="coerce").min()
                    event[f"return_d{horizon}"] = (close_d / close - 1.0) * 100.0 if close_d and not math.isnan(close_d) else math.nan
                    event[f"mfe_d{horizon}"] = (max_high / close - 1.0) * 100.0 if max_high and not math.isnan(max_high) else math.nan
                    event[f"mae_d{horizon}"] = (min_low / close - 1.0) * 100.0 if min_low and not math.isnan(min_low) else math.nan
                else:
                    event[f"return_d{horizon}"] = math.nan
                    event[f"mfe_d{horizon}"] = math.nan
                    event[f"mae_d{horizon}"] = math.nan
            events.append(event)
    return pd.DataFrame(events)


def _process_price_history_path(path: Path, target_date: str = "") -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    latest_rows: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    df = read_csv(path)
    if df.empty or len(df) < 40:
        return latest_rows, events
    if not {"date", "stock_id", "stock_name", "close", "high", "low", "volume"}.issubset(df.columns):
        return latest_rows, events
    df = add_price_metrics(df)
    if df.empty:
        return latest_rows, events

    latest_row = _select_latest_signal_row(df, target_date)
    latest_signal = detect_volume_breakout(latest_row) if latest_row is not None else None
    if latest_row is not None and latest_signal is not None:
        latest_rows.append(
            {
                "signal_date": normalize_date(latest_row.get("date")),
                "stock_id": normalize_stock_id(latest_row.get("stock_id")),
                "stock_name": safe_str(latest_row.get("stock_name")),
                "market": safe_str(latest_row.get("market")),
                "close": latest_row.get("close"),
                "open": latest_row.get("open"),
                "high": latest_row.get("high"),
                "low": latest_row.get("low"),
                "volume": latest_row.get("volume"),
                "volume_ratio": latest_row.get("volume_ratio"),
                "return_1d": latest_row.get("return_1d"),
                "return_5d": latest_row.get("return_5d"),
                "return_20d": latest_row.get("return_20d"),
                "distance_to_ma20_pct": latest_row.get("distance_to_ma20_calc"),
                "distance_to_ma60_pct": latest_row.get("distance_to_ma60_calc"),
                "distance_to_previous_20d_high_pct": latest_row.get("distance_to_previous_20d_high_calc"),
                "distance_to_previous_60d_high_pct": latest_row.get("distance_to_previous_60d_high_calc"),
                "ma20": latest_row.get("ma20"),
                "ma60": latest_row.get("ma60"),
                "ema23": latest_row.get("ema23"),
                "volume_ma20": latest_row.get("volume_ma20"),
                "previous_20d_high": latest_row.get("previous_20d_high_calc"),
                "previous_60d_high": latest_row.get("previous_60d_high_calc"),
                "previous_20d_low": latest_row.get("previous_20d_low_calc"),
                "previous_60d_low": latest_row.get("previous_60d_low_calc"),
                "volume_breakout_type": latest_signal.event_type,
                "volume_watch_scope": latest_signal.scope,
                "volume_breakout_score": latest_signal.score,
                "volume_breakout_notes": "|".join(latest_signal.notes),
                "false_breakout_risk_calc": "False",
                "overheated_breakout": "False",
            }
        )

    if len(df) < 80:
        return latest_rows, events

    close_s = pd.to_numeric(df["close"], errors="coerce")
    open_s = pd.to_numeric(df["open"], errors="coerce")
    volume_ratio = pd.to_numeric(df["volume_ratio"], errors="coerce")
    prev_close = pd.to_numeric(df["previous_close_calc"], errors="coerce")
    prev20 = pd.to_numeric(df["previous_20d_high_calc"], errors="coerce")
    volume_ma20 = pd.to_numeric(df["volume_ma20"], errors="coerce")
    volume_ma20_lots = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
    breakout_level = prev20 * 1.02
    bullish = (close_s > open_s) | ((close_s == open_s) & (close_s > prev_close))
    normal_volume_attack = (
        (close_s >= breakout_level)
        & (volume_ratio >= 2.0)
        & (volume_ma20_lots >= 1000)
        & bullish
    )
    bottom_volume_attack = normal_volume_attack | locked_limit_up_breakout_mask(df)

    event_type = pd.Series("", index=df.index, dtype="object")
    event_type.loc[bottom_volume_attack] = "bottom_volume_attack"

    event_indices = event_type[event_type != ""].index.tolist()
    for idx in event_indices:
        row = df.iloc[idx]
        close_value = safe_float(row.get("close"))
        if math.isnan(close_value) or close_value <= 0:
            continue
        signal = detect_volume_breakout(row)
        signal_notes = signal.notes if signal else []
        signal_scope = signal.scope if signal and signal.scope else scope_for_event_type(event_type.loc[idx])
        event: dict[str, Any] = {
            "event_date": normalize_date(row.get("date")),
            "stock_id": normalize_stock_id(row.get("stock_id")),
            "stock_name": safe_str(row.get("stock_name")),
            "market": safe_str(row.get("market")),
            "volume_breakout_type": safe_str(event_type.loc[idx]),
            "volume_watch_scope": signal_scope,
            "volume_breakout_rule_version": VOLUME_BREAKOUT_RULE_VERSION,
            "volume_breakout_score": signal.score if signal else 0,
            "volume_ratio": row.get("volume_ratio"),
            "return_5d_before": row.get("return_5d"),
            "return_20d_before": row.get("return_20d"),
            "distance_to_ma20_pct": row.get("distance_to_ma20_calc"),
            "false_breakout_risk": "False",
            "overheated_breakout": "False",
            "close_on_event": close_value,
        }
        for horizon in HORIZONS:
            future = df.iloc[idx + 1 : idx + 1 + horizon]
            matured = len(future) >= horizon
            event[f"mature_d{horizon}"] = bool(matured)
            if matured:
                close_d = safe_float(future.iloc[horizon - 1].get("close"))
                max_high = pd.to_numeric(future["high"], errors="coerce").max()
                min_low = pd.to_numeric(future["low"], errors="coerce").min()
                event[f"return_d{horizon}"] = (close_d / close_value - 1.0) * 100.0 if close_d and not math.isnan(close_d) else math.nan
                event[f"mfe_d{horizon}"] = (max_high / close_value - 1.0) * 100.0 if max_high and not math.isnan(max_high) else math.nan
                event[f"mae_d{horizon}"] = (min_low / close_value - 1.0) * 100.0 if min_low and not math.isnan(min_low) else math.nan
            else:
                event[f"return_d{horizon}"] = math.nan
                event[f"mfe_d{horizon}"] = math.nan
                event[f"mae_d{horizon}"] = math.nan
        events.append(event)
    return latest_rows, events


def build_latest_and_event_frames(target_date: str = "", max_workers: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    workers = max_workers or min(12, max(2, (os.cpu_count() or 4)))
    latest_rows: list[dict[str, Any]] = []
    event_rows: list[dict[str, Any]] = []
    worker = partial(_process_price_history_path, target_date=target_date)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for latest_part, events_part in executor.map(worker, paths):
            latest_rows.extend(latest_part)
            event_rows.extend(events_part)
    return pd.DataFrame(latest_rows), pd.DataFrame(event_rows)


def _process_latest_path(path: Path, target_date: str = "") -> list[dict[str, Any]]:
    df = read_csv(path)
    if df.empty or len(df) < 40:
        return []
    if not {"date", "stock_id", "stock_name", "close", "high", "low", "volume"}.issubset(df.columns):
        return []
    df = add_price_metrics(df)
    if df.empty:
        return []
    row = _select_latest_signal_row(df, target_date)
    if row is None:
        return []
    signal = detect_volume_breakout(row)
    if signal is None:
        return []
    return [
        {
            "signal_date": normalize_date(row.get("date")),
            "stock_id": normalize_stock_id(row.get("stock_id")),
            "stock_name": safe_str(row.get("stock_name")),
            "market": safe_str(row.get("market")),
            "close": row.get("close"),
            "open": row.get("open"),
            "high": row.get("high"),
            "low": row.get("low"),
            "volume": row.get("volume"),
            "volume_ratio": row.get("volume_ratio"),
            "return_1d": row.get("return_1d"),
            "return_5d": row.get("return_5d"),
            "return_20d": row.get("return_20d"),
            "distance_to_ma20_pct": row.get("distance_to_ma20_calc"),
            "distance_to_ma60_pct": row.get("distance_to_ma60_calc"),
            "distance_to_previous_20d_high_pct": row.get("distance_to_previous_20d_high_calc"),
            "distance_to_previous_60d_high_pct": row.get("distance_to_previous_60d_high_calc"),
            "ma20": row.get("ma20"),
            "ma60": row.get("ma60"),
            "ema23": row.get("ema23"),
            "volume_ma20": row.get("volume_ma20"),
            "previous_20d_high": row.get("previous_20d_high_calc"),
            "previous_60d_high": row.get("previous_60d_high_calc"),
            "previous_20d_low": row.get("previous_20d_low_calc"),
            "previous_60d_low": row.get("previous_60d_low_calc"),
            "volume_breakout_type": signal.event_type,
            "volume_watch_scope": signal.scope,
            "volume_breakout_score": signal.score,
            "volume_breakout_notes": "|".join(signal.notes),
            "false_breakout_risk_calc": "False",
            "overheated_breakout": "False",
        }
    ]


def build_latest_frame_fast(target_date: str = "", max_workers: int | None = None) -> pd.DataFrame:
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    workers = max_workers or min(12, max(2, (os.cpu_count() or 4)))
    latest_rows: list[dict[str, Any]] = []
    worker = partial(_process_latest_path, target_date=target_date)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for latest_part in executor.map(worker, paths):
            latest_rows.extend(latest_part)
    return pd.DataFrame(latest_rows)


def filter_latest_to_effective_signal_date(latest: pd.DataFrame, main_date: str) -> tuple[pd.DataFrame, str]:
    """Filter latest price-derived signals to the report trading date."""
    if latest.empty or "signal_date" not in latest.columns:
        return latest, main_date
    out = latest.copy()
    out["signal_date"] = out["signal_date"].map(normalize_date)
    available = sorted(d for d in out["signal_date"].dropna().unique().tolist() if d)
    if not available:
        return out.iloc[0:0].copy(), main_date
    if main_date and main_date in available:
        effective_date = main_date
    elif main_date:
        return out.iloc[0:0].copy(), main_date
    else:
        effective_date = available[-1]
    return out[out["signal_date"] == effective_date].copy(), effective_date


def append_latest_events_to_history(events: pd.DataFrame, latest: pd.DataFrame) -> pd.DataFrame:
    if latest.empty:
        return events
    latest_events: list[dict[str, Any]] = []
    for _, row in latest.iterrows():
        close_value = safe_float(row.get("close"))
        event: dict[str, Any] = {
            "event_date": normalize_date(row.get("signal_date")),
            "stock_id": normalize_stock_id(row.get("stock_id")),
            "stock_name": safe_str(row.get("stock_name")),
            "market": safe_str(row.get("market")),
            "volume_breakout_type": safe_str(row.get("volume_breakout_type")),
            "volume_watch_scope": safe_str(row.get("volume_watch_scope")),
            "volume_breakout_rule_version": VOLUME_BREAKOUT_RULE_VERSION,
            "volume_breakout_score": row.get("volume_breakout_score"),
            "volume_ratio": row.get("volume_ratio"),
            "return_5d_before": row.get("return_5d"),
            "return_20d_before": row.get("return_20d"),
            "distance_to_ma20_pct": row.get("distance_to_ma20_pct"),
            "false_breakout_risk": "False",
            "overheated_breakout": "False",
            "close_on_event": close_value,
        }
        for horizon in HORIZONS:
            event[f"mature_d{horizon}"] = False
            event[f"return_d{horizon}"] = math.nan
            event[f"mfe_d{horizon}"] = math.nan
            event[f"mae_d{horizon}"] = math.nan
        latest_events.append(event)
    additions = pd.DataFrame(latest_events)
    if events.empty:
        return additions
    combined = pd.concat([events, additions], ignore_index=True)
    key_cols = ["event_date", "stock_id", "volume_breakout_type"]
    existing = [c for c in key_cols if c in combined.columns]
    if existing:
        combined = combined.drop_duplicates(existing, keep="first")
    return combined


def summarize_backtest(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame()
    events = events.copy()
    if "volume_watch_scope" not in events.columns:
        events["volume_watch_scope"] = ""
    if "volume_breakout_type" in events.columns:
        scope = events["volume_watch_scope"].map(safe_str)
        events.loc[scope == "", "volume_watch_scope"] = events.loc[scope == "", "volume_breakout_type"].map(scope_for_event_type)
    rows: list[dict[str, Any]] = []
    group_specs = [("volume_breakout_type", events.groupby("volume_breakout_type", dropna=False))]
    if "volume_watch_scope" in events.columns:
        group_specs.append(("volume_watch_scope", events.groupby("volume_watch_scope", dropna=False)))
    for group_name, grouped in group_specs:
        for value, part in grouped:
            row: dict[str, Any] = {"group_name": group_name, "group_value": safe_str(value), "sample_count": len(part)}
            best_horizon = ""
            best_ret = -10**9
            for horizon in HORIZONS:
                mature_col = f"mature_d{horizon}"
                mature = part[part[mature_col].map(safe_bool)] if mature_col in part.columns else pd.DataFrame()
                row[f"mature_d{horizon}_count"] = len(mature)
                if not mature.empty:
                    returns = pd.to_numeric(mature[f"return_d{horizon}"], errors="coerce")
                    mfe = pd.to_numeric(mature[f"mfe_d{horizon}"], errors="coerce")
                    mae = pd.to_numeric(mature[f"mae_d{horizon}"], errors="coerce")
                    avg_ret = returns.mean()
                    row[f"avg_return_d{horizon}"] = round(avg_ret, 4)
                    row[f"median_return_d{horizon}"] = round(returns.median(), 4)
                    row[f"win_rate_d{horizon}"] = round((returns > 0).mean() * 100.0, 2)
                    row[f"avg_mfe_d{horizon}"] = round(mfe.mean(), 4)
                    row[f"avg_mae_d{horizon}"] = round(mae.mean(), 4)
                    if horizon in {5, 10, 20} and avg_ret > best_ret:
                        best_ret = avg_ret
                        best_horizon = f"D+{horizon}"
                else:
                    row[f"avg_return_d{horizon}"] = ""
                    row[f"median_return_d{horizon}"] = ""
                    row[f"win_rate_d{horizon}"] = ""
                    row[f"avg_mfe_d{horizon}"] = ""
                    row[f"avg_mae_d{horizon}"] = ""
            d5 = int(row.get("mature_d5_count", 0) or 0)
            d10 = int(row.get("mature_d10_count", 0) or 0)
            row["sample_status"] = "ok" if d5 >= 30 and d10 >= 30 else "insufficient_sample"
            row["best_horizon"] = best_horizon
            rows.append(row)
    return pd.DataFrame(rows)


def ensure_watch_schema(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    def numeric_series(col: str) -> pd.Series:
        if col in out.columns:
            return pd.to_numeric(out[col], errors="coerce")
        return pd.Series([pd.NA] * len(out), index=out.index, dtype="Float64")

    if "range_window" not in out.columns:
        out["range_window"] = "20"
    if "range_high" not in out.columns:
        out["range_high"] = out.get("previous_20d_high", "")
    if "range_low" not in out.columns:
        out["range_low"] = out.get("previous_20d_low", "")
    high = numeric_series("range_high")
    low = numeric_series("range_low")
    close = numeric_series("close")
    intraday_high = numeric_series("high")
    if "range_width_pct" not in out.columns:
        out["range_width_pct"] = ((high - low) / low.replace(0, pd.NA) * 100.0).round(4)
    if "range_breakout_pct" not in out.columns:
        out["range_breakout_pct"] = ((close / high.replace(0, pd.NA) - 1.0) * 100.0).round(4)
    if "close_above_range_high" not in out.columns:
        out["close_above_range_high"] = close.gt(high).map({True: "True", False: "False"})
    if "high_above_range_high" not in out.columns:
        out["high_above_range_high"] = intraday_high.gt(high).map({True: "True", False: "False"})
    for col in WATCH_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    extra_cols = [col for col in out.columns if col not in WATCH_COLUMNS]
    return out[WATCH_COLUMNS + extra_cols]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path == WATCH_CSV:
        df = ensure_watch_schema(df)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def table_lines(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    cols = [c for c in columns if c in df.columns]
    if not cols:
        return ["_No matching columns._"]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        vals = [safe_str(row.get(c)).replace("|", "/").replace("\n", " ")[:140] for c in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_watch_md(watch: pd.DataFrame, main_date: str) -> None:
    counts = {
        "rows": len(watch),
        "priority": watch["volume_breakout_priority"].value_counts().to_dict() if "volume_breakout_priority" in watch.columns else {},
        "type": watch["volume_breakout_type"].value_counts().to_dict() if "volume_breakout_type" in watch.columns else {},
        "scope": watch["volume_watch_scope"].value_counts().to_dict() if "volume_watch_scope" in watch.columns else {},
        "selection": watch["selection_status"].value_counts().to_dict() if "selection_status" in watch.columns else {},
    }
    cols = [
        "volume_breakout_rank",
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
        "distance_to_ma20_pct",
        "risk_flags",
        "next_volume_breakout_confirmation",
    ]
    lines = [
        "# Volume Attack Watch",
        "",
        f"- generated_at: `{now_text()}`",
        f"- main_price_date: `{main_date}`",
        f"- total_watch_rows: `{counts['rows']}`",
        f"- priority_distribution: `{counts['priority']}`",
        f"- type_distribution: `{counts['type']}`",
        f"- scope_distribution: `{counts['scope']}`",
        f"- selection_status_distribution: `{counts['selection']}`",
        "",
        "## Interpretation",
        "",
        "- Official model type is `bottom_volume_attack` only.",
        "- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.",
        "- No 60D-high gate, no moving-average gate, no same-day fake-breakout classification, and no selected/watch/risk sub-status.",
        "- Long upper shadow or TDCC deterioration can reduce score or add risk tags, but they do not change the model hit into another model.",
        "- Research observation basis is next trading day open after the signal date.",
        "- This list is a model-selected universe and backtest layer. It is not standalone buy advice.",
        "",
        "## Top Watch List",
        "",
        *table_lines(watch, cols, limit=80),
        "",
    ]
    WATCH_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_backtest_md(summary: pd.DataFrame, events: pd.DataFrame, main_date: str) -> None:
    lines = [
        "# Volume Breakout Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- main_price_date: `{main_date}`",
        f"- event_log_rows: `{len(events)}`",
        "- rule: Features are detected on event date only. Future data is used only for D+N performance labels.",
        "- rule: Pending horizons are excluded from mature D+N statistics.",
        "",
        "## Summary",
        "",
        *table_lines(
            summary,
            [
                "group_name",
                "group_value",
                "sample_count",
                "mature_d5_count",
                "avg_return_d5",
                "win_rate_d5",
                "avg_mfe_d5",
                "avg_mae_d5",
                "mature_d10_count",
                "avg_return_d10",
                "win_rate_d10",
                "mature_d20_count",
                "avg_return_d20",
                "win_rate_d20",
                "sample_status",
                "best_horizon",
            ],
            limit=80,
        ),
        "",
    ]
    BACKTEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_packet(watch: pd.DataFrame, summary: pd.DataFrame, main_date: str) -> None:
    bottom_count = int((watch.get("volume_breakout_type", pd.Series(dtype=str)) == "bottom_volume_attack").sum()) if not watch.empty else 0
    risk_count = int(watch.get("risk_flags", pd.Series(dtype=str)).map(lambda v: bool(safe_str(v))).sum()) if not watch.empty else 0
    lines = [
        "# VOLUME ATTACK CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: `{now_text()}`",
        f"- main_price_date: `{main_date}`",
        f"- watch_rows: `{len(watch)}`",
        f"- bottom_volume_attack_count: `{bottom_count}`",
        f"- selected_rows: `{len(watch)}`",
        f"- rows_with_risk_tags: `{risk_count}`",
        f"- watch_csv_raw_url: {raw_url(WATCH_CSV)}",
        f"- watch_md_raw_url: {raw_url(WATCH_MD)}",
        f"- backtest_csv_raw_url: {raw_url(BACKTEST_CSV)}",
        f"- backtest_md_raw_url: {raw_url(BACKTEST_MD)}",
        "",
        "## Model Definition",
        "",
        "- Model display name: 放量攻擊模型.",
        "- Hard gates: normal attack requires close >= prior 20 trading day high excluding signal day * 1.02, 20D average volume >= 1000 lots, volume_ratio >= 2.0, and bullish candle; locked limit-up breakout uses the same breakout price plus limit-up shape and does not require volume_ratio or 20D average volume.",
        "- The model intentionally does not require a 60D high breakout or moving-average reclaim.",
        "- The model emits selected rows only. Risk flags and score components are ranking/operation context, not a separate watch/risk status.",
        "- Same-day fake breakout is not confirmed on the signal date. Do not label a selected row as failed breakout until later price action confirms failure.",
        "- Research observation basis is signal date next trading day open.",
        "",
        "## Top Volume Attack",
        "",
        *table_lines(
            watch,
            [
                "volume_breakout_rank",
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
            ],
            limit=40,
        ),
        "",
        "## Backtest Summary",
        "",
        *table_lines(
            summary,
            [
                "group_name",
                "group_value",
                "sample_count",
                "mature_d5_count",
                "avg_return_d5",
                "win_rate_d5",
                "mature_d10_count",
                "avg_return_d10",
                "win_rate_d10",
                "mature_d20_count",
                "avg_return_d20",
                "win_rate_d20",
                "sample_status",
            ],
            limit=50,
        ),
        "",
        "## Rules",
        "",
        "- Do not mix this model with W-bottom, neckline watch, MA reclaim, strict 60D high breakout, or pullback models.",
        "- Do not use price moved too much, short-term overheat, or not breaking 60D high as hard vetoes for this model.",
        "- A long upper shadow can reduce attack quality once; avoid duplicate penalties for the same candle issue.",
        "- TDCC, warrant, revenue, consolidation length, breakout magnitude, and position context are ranking components.",
        "- If the stock falls back below the prior-20D-high breakout threshold after the signal, later reports may tag failure or higher risk.",
        "",
    ]
    PACKET_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def latest_only_summary() -> pd.DataFrame:
    if BACKTEST_CSV.exists():
        summary = read_csv(BACKTEST_CSV)
        if not summary.empty and "group_value" in summary.columns:
            bottom = summary[summary["group_value"].map(safe_str).eq("bottom_volume_attack")].copy()
            if not bottom.empty:
                return bottom
        return summary.head(0)
    return pd.DataFrame()


def event_log_has_formal_bottom_history(events: pd.DataFrame) -> bool:
    return (
        not events.empty
        and "volume_breakout_type" in events.columns
        and "volume_breakout_rule_version" in events.columns
        and events["volume_breakout_type"].map(safe_str).eq("bottom_volume_attack").any()
        and events["volume_breakout_rule_version"].map(safe_str).eq(VOLUME_BREAKOUT_RULE_VERSION).any()
    )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build daily volume breakout watch outputs and optional research backtest outputs.")
    parser.add_argument(
        "--latest-only",
        action="store_true",
        help="Only refresh latest watch/packet outputs. Do not rewrite event log or backtest files.",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    main_date = latest_main_date()

    if args.latest_only:
        latest = build_latest_frame_fast(target_date=main_date)
        latest, effective_date = filter_latest_to_effective_signal_date(latest, main_date)
        watch = merge_context(latest)
        summary = latest_only_summary()

        write_csv(watch, WATCH_CSV)
        write_watch_md(watch, effective_date)
        write_packet(watch, summary, effective_date)

        print(f"Saved: {WATCH_CSV} rows={len(watch)}")
        print(f"Saved: {WATCH_MD}")
        print(f"Saved: {PACKET_MD}")
        if effective_date != main_date:
            print(f"Using effective volume signal date {effective_date} for main_price_date {main_date}")
        if summary.empty:
            print("Skipped backtest refresh: --latest-only and no existing backtest summary found")
        else:
            print(f"Loaded existing backtest summary rows={len(summary)}")
        return 0

    full_rebuild = os.environ.get("VOLUME_BREAKOUT_FULL_REBUILD", "").strip().lower() in {"1", "true", "yes"}
    if EVENT_LOG_CSV.exists() and not full_rebuild:
        latest = build_latest_frame_fast(target_date=main_date)
        events = read_csv(EVENT_LOG_CSV)
        if event_log_has_formal_bottom_history(events):
            events = append_latest_events_to_history(events, latest)
        else:
            print(
                "Existing volume breakout event log has no bottom_volume_attack history; "
                "rebuilding from price history."
            )
            latest, events = build_latest_and_event_frames(target_date=main_date)
    else:
        latest, events = build_latest_and_event_frames(target_date=main_date)
    if not events.empty and "volume_breakout_type" in events.columns:
        events = events[events["volume_breakout_type"].map(safe_str).eq("bottom_volume_attack")].copy()
    latest, effective_date = filter_latest_to_effective_signal_date(latest, main_date)
    watch = merge_context(latest)
    if not events.empty and "volume_breakout_type" in events.columns:
        if "volume_watch_scope" not in events.columns:
            events["volume_watch_scope"] = ""
        blank_scope = events["volume_watch_scope"].map(safe_str) == ""
        events.loc[blank_scope, "volume_watch_scope"] = events.loc[blank_scope, "volume_breakout_type"].map(scope_for_event_type)

    summary = summarize_backtest(events)

    write_csv(watch, WATCH_CSV)
    write_csv(events, EVENT_LOG_CSV)
    write_csv(summary, BACKTEST_CSV)
    write_watch_md(watch, effective_date)
    write_backtest_md(summary, events, effective_date)
    write_packet(watch, summary, effective_date)

    print(f"Saved: {WATCH_CSV} rows={len(watch)}")
    print(f"Saved: {WATCH_MD}")
    print(f"Saved: {EVENT_LOG_CSV} rows={len(events)}")
    print(f"Saved: {BACKTEST_CSV} rows={len(summary)}")
    print(f"Saved: {BACKTEST_MD}")
    print(f"Saved: {PACKET_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
