from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor
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
DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
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

HORIZONS = [1, 3, 5, 10, 20]


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


def scope_for_event_type(event_type: Any) -> str:
    text = safe_str(event_type)
    if text == "strict_60d_volume_breakout":
        return "strict_breakout"
    if text in {"platform_volume_breakout", "neckline_volume_breakout"}:
        return "confirmed_attack"
    if text in {"abnormal_volume_up", "right_side_volume_attack", "volume_expansion_watch"}:
        return "volume_attack"
    if text.startswith("loose_"):
        return "broad_watch"
    return ""


def detect_volume_breakout(row: pd.Series) -> BreakoutSignal | None:
    close = safe_float(row.get("close"))
    open_ = safe_float(row.get("open"))
    high = safe_float(row.get("high"))
    ma20 = safe_float(row.get("ma20"))
    ma60 = safe_float(row.get("ma60"))
    ema23 = safe_float(row.get("ema23"))
    volume_ratio = safe_float(row.get("volume_ratio"))
    ret_1d = safe_float(row.get("return_1d"), safe_float(row.get("daily_return_calc")))
    ret_5d = safe_float(row.get("return_5d"))
    ret_20d = safe_float(row.get("return_20d"))
    prev20 = safe_float(row.get("previous_20d_high_calc"))
    prev60 = safe_float(row.get("previous_60d_high_calc"))
    dist_ma20 = safe_float(row.get("distance_to_ma20_calc"))
    dist_prev20 = safe_float(row.get("distance_to_previous_20d_high_calc"))
    close_pos = safe_float(row.get("close_position_in_range"))
    upper_shadow = safe_float(row.get("upper_shadow_pct"))

    if any(math.isnan(x) for x in [close, high, volume_ratio, prev20]):
        return None
    above_ma = (math.isnan(ma20) or close >= ma20) and (math.isnan(ema23) or close >= ema23)
    near_high_close = math.isnan(close_pos) or close_pos >= 0.70
    close_above_open = math.isnan(open_) or close >= open_

    notes: list[str] = []
    event_type = ""
    scope = ""
    score = 0.0

    if not math.isnan(prev60) and close > prev60 and volume_ratio >= 1.5 and near_high_close:
        event_type = "strict_60d_volume_breakout"
        scope = "strict_breakout"
        score = 92
        notes.append("close_above_previous_60d_high")
    elif close > prev20 and volume_ratio >= 1.5 and near_high_close and above_ma:
        event_type = "platform_volume_breakout"
        scope = "confirmed_attack"
        score = 84
        notes.append("close_above_previous_20d_high")
    elif not math.isnan(prev60) and close >= prev60 * 0.95 and volume_ratio >= 1.5 and above_ma and close_above_open:
        event_type = "neckline_volume_breakout"
        scope = "confirmed_attack"
        score = 76
        notes.append("near_previous_60d_high_with_volume")
    elif volume_ratio >= 3.0 and ret_1d >= 5 and above_ma and close_above_open:
        event_type = "abnormal_volume_up"
        scope = "volume_attack"
        score = 68
        notes.append("abnormal_volume_and_price_up")
    elif volume_ratio >= 1.2 and ret_1d >= 4 and above_ma and near_high_close:
        event_type = "right_side_volume_attack"
        scope = "volume_attack"
        score = 62
        notes.append("right_side_attack_with_volume")
    elif volume_ratio >= 1.5 and above_ma and ret_1d > 0:
        event_type = "volume_expansion_watch"
        scope = "volume_attack"
        score = 55
        notes.append("volume_expansion_above_ma")
    elif (
        not math.isnan(dist_prev20)
        and -6 <= dist_prev20 <= 2
        and volume_ratio >= 1.10
        and above_ma
        and (close_above_open or near_high_close)
    ):
        event_type = "loose_platform_volume_watch"
        scope = "broad_watch"
        score = 50
        notes.append("loose_platform_or_neckline_area")
    elif (
        volume_ratio >= 1.05
        and ret_5d >= 3
        and above_ma
        and near_high_close
        and (math.isnan(dist_ma20) or -3 <= dist_ma20 <= 18)
    ):
        event_type = "loose_right_side_volume_watch"
        scope = "broad_watch"
        score = 48
        notes.append("loose_right_side_follow_through")
    elif (
        volume_ratio >= 1.10
        and ret_1d >= 0
        and above_ma
        and (math.isnan(dist_ma20) or -2 <= dist_ma20 <= 8)
    ):
        event_type = "loose_ma_reclaim_volume_watch"
        scope = "broad_watch"
        score = 45
        notes.append("loose_ma_reclaim_or_support_volume")
    else:
        return None

    if volume_ratio >= 2.0:
        score += 4
        notes.append("volume_ratio_ge_2")
    if ret_5d >= 8:
        score += 3
        notes.append("five_day_momentum")
    if not math.isnan(dist_ma20) and dist_ma20 > 20:
        score -= 15
        notes.append("far_above_ma20")
    if ret_20d > 30:
        score -= 15
        notes.append("twenty_day_overheated")
    if upper_shadow >= 3:
        score -= 10
        notes.append("long_upper_shadow_risk")
    if not near_high_close:
        score -= 8
        notes.append("not_close_near_high")
    return BreakoutSignal(event_type=event_type, score=round(score, 2), notes=notes, scope=scope)


def build_latest_price_signal_frame() -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for path in sorted(PRICE_HISTORY_DIR.glob("*.csv")):
        df = read_csv(path)
        if df.empty or len(df) < 40:
            continue
        if not {"date", "stock_id", "stock_name", "close", "high", "low", "volume"}.issubset(df.columns):
            continue
        df = add_price_metrics(df)
        if df.empty:
            continue
        row = df.iloc[-1]
        signal = detect_volume_breakout(row)
        if signal is None:
            continue
        stock_id = normalize_stock_id(row.get("stock_id"))
        rows.append(
            {
                "signal_date": normalize_date(row.get("date")),
                "stock_id": stock_id,
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
                "previous_20d_high": row.get("previous_20d_high_calc"),
                "previous_60d_high": row.get("previous_60d_high_calc"),
                "volume_breakout_type": signal.event_type,
                "volume_watch_scope": signal.scope,
                "volume_breakout_score": signal.score,
                "volume_breakout_notes": "|".join(signal.notes),
                "false_breakout_risk_calc": "True" if "long_upper_shadow_risk" in signal.notes or "not_close_near_high" in signal.notes else "False",
                "overheated_breakout": "True" if safe_float(row.get("return_20d")) > 30 or safe_float(row.get("distance_to_ma20_calc")) > 20 else "False",
            }
        )
    return pd.DataFrame(rows)


def merge_context(watch: pd.DataFrame) -> pd.DataFrame:
    if watch.empty:
        return watch
    out = watch.copy()
    all_candidates = read_csv(ALL_CANDIDATES_CSV)
    decision = read_csv(DECISION_CSV)
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

    if not decision.empty:
        keep = [
            "stock_id",
            "original_category",
            "pattern_mapped_category",
            "decision_priority",
            "decision_score",
            "decision_rank_in_category",
            "downgrade_flags",
            "risk_tags",
            "why_selected",
            "why_downgraded",
            "next_confirmation",
            "must_not_overstate",
        ]
        existing = [c for c in keep if c in decision.columns]
        dec = decision[existing].drop_duplicates("stock_id", keep="first")
        out = out.merge(dec, on="stock_id", how="left", suffixes=("", "_decision"))

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
        selected = safe_str(row.get("category")) or safe_str(row.get("original_category"))
        decision_priority = safe_str(row.get("decision_priority"))
        tdcc_status = safe_str(row.get("tdcc_status"))
        repeat_label = safe_str(row.get("repeat_appear_label"))
        event_type = safe_str(row.get("volume_breakout_type"))
        watch_scope = safe_str(row.get("volume_watch_scope"))
        score = safe_float(row.get("volume_breakout_score"), 0)
        ret_20d = safe_float(row.get("return_20d"))
        dist_ma20 = safe_float(row.get("distance_to_ma20_pct"))
        volume_ratio = safe_float(row.get("volume_ratio"))
        false_breakout = safe_bool(row.get("false_breakout_risk")) or safe_bool(row.get("false_breakout_risk_calc"))
        overheated = safe_bool(row.get("overheated_breakout")) or ret_20d > 30 or dist_ma20 > 20

        risk_flags: list[str] = []
        if not selected:
            risk_flags.append("not_in_candidate_model")
        if tdcc_status == "distribution_warning":
            risk_flags.append("tdcc_distribution_warning")
        if repeat_label in {"stale_signal", "continued_overheated"}:
            risk_flags.append(repeat_label)
        if false_breakout:
            risk_flags.append("false_breakout_risk")
        if overheated:
            risk_flags.append("overheated_breakout")
        if safe_str(row.get("already_priced_in")).lower() == "true":
            risk_flags.append("already_priced_in")
        if decision_priority == "D_risk_downgrade":
            risk_flags.append("decision_layer_downgrade")

        if "not_in_candidate_model" in risk_flags:
            selection_status = "not_selected_by_candidate_model"
            not_selected_reason = "volume breakout detected from price history but not selected by existing candidate filters"
        elif selected == "true_breakout":
            selection_status = "selected_as_strict_breakout"
            not_selected_reason = ""
        elif selected:
            selection_status = "selected_but_routed_to_other_category"
            not_selected_reason = f"routed_to_{selected}; strict_breakout_requires_60d_high_breakout"
        else:
            selection_status = "unknown"
            not_selected_reason = ""

        severe_risk = any(x in risk_flags for x in ["overheated_breakout", "tdcc_distribution_warning", "false_breakout_risk", "decision_layer_downgrade"])
        priority = "B_confirm_needed"
        if severe_risk:
            priority = "D_risk_downgrade"
        elif event_type == "strict_60d_volume_breakout" and not risk_flags and score >= 85:
            priority = "A_valid_breakout_watch"
        elif event_type in {"platform_volume_breakout", "neckline_volume_breakout"} and not risk_flags and score >= 70:
            priority = "A_valid_breakout_watch"
        elif watch_scope == "broad_watch":
            priority = "C_watch_only" if "not_in_candidate_model" in risk_flags else "B_confirm_needed"
        elif "not_in_candidate_model" in risk_flags:
            priority = "B_confirm_needed"
        elif event_type in {"right_side_volume_attack", "volume_expansion_watch", "abnormal_volume_up"}:
            priority = "C_watch_only"

        if priority == "A_valid_breakout_watch":
            next_confirmation = "next day holds breakout area; volume does not collapse; TDCC not distribution_warning"
        elif priority == "B_confirm_needed":
            next_confirmation = "confirm close above MA20/EMA23 and avoid long upper shadow"
        elif priority == "C_watch_only":
            next_confirmation = "broad recall only: wait for platform/neckline breakout, stronger volume, and benchmark-relative strength"
        else:
            next_confirmation = "risk first: avoid chasing until heat/TDCC/repeat risk improves"

        d.update(
            {
                "volume_breakout_priority": priority,
                "selection_status": selection_status,
                "not_selected_reason": not_selected_reason,
                "risk_flags": "|".join(dict.fromkeys(risk_flags)),
                "next_volume_breakout_confirmation": next_confirmation,
            }
        )
        rows.append(d)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    order = {"A_valid_breakout_watch": 0, "B_confirm_needed": 1, "C_watch_only": 2, "D_risk_downgrade": 3}
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
        high = pd.to_numeric(df["high"], errors="coerce")
        ma20 = pd.to_numeric(df["ma20"], errors="coerce")
        ema23 = pd.to_numeric(df["ema23"], errors="coerce")
        volume_ratio = pd.to_numeric(df["volume_ratio"], errors="coerce")
        ret_1d = pd.to_numeric(df.get("return_1d", df.get("daily_return_calc")), errors="coerce")
        ret_5d = pd.to_numeric(df.get("return_5d"), errors="coerce")
        prev20 = pd.to_numeric(df["previous_20d_high_calc"], errors="coerce")
        prev60 = pd.to_numeric(df["previous_60d_high_calc"], errors="coerce")
        dist_ma20 = pd.to_numeric(df["distance_to_ma20_calc"], errors="coerce")
        dist_prev20 = pd.to_numeric(df["distance_to_previous_20d_high_calc"], errors="coerce")
        close_pos = pd.to_numeric(df["close_position_in_range"], errors="coerce").fillna(1)
        above_ma = ((ma20.isna()) | (close >= ma20)) & ((ema23.isna()) | (close >= ema23))
        near_high_close = close_pos >= 0.70
        close_above_open = (open_.isna()) | (close >= open_)

        strict = (close > prev60) & (volume_ratio >= 1.5) & near_high_close
        platform = (~strict) & (close > prev20) & (volume_ratio >= 1.5) & near_high_close & above_ma
        neckline = (~strict) & (~platform) & (close >= prev60 * 0.95) & (volume_ratio >= 1.5) & above_ma & close_above_open
        abnormal = (~strict) & (~platform) & (~neckline) & (volume_ratio >= 3.0) & (ret_1d >= 5) & above_ma & close_above_open
        right_side = (~strict) & (~platform) & (~neckline) & (~abnormal) & (volume_ratio >= 1.2) & (ret_1d >= 4) & above_ma & near_high_close
        expansion = (~strict) & (~platform) & (~neckline) & (~abnormal) & (~right_side) & (volume_ratio >= 1.5) & above_ma & (ret_1d > 0)
        loose_platform = (
            (~strict)
            & (~platform)
            & (~neckline)
            & (~abnormal)
            & (~right_side)
            & (~expansion)
            & (dist_prev20 >= -6)
            & (dist_prev20 <= 2)
            & (volume_ratio >= 1.10)
            & above_ma
            & (close_above_open | near_high_close)
        )
        loose_right_side = (
            (~strict)
            & (~platform)
            & (~neckline)
            & (~abnormal)
            & (~right_side)
            & (~expansion)
            & (~loose_platform)
            & (volume_ratio >= 1.05)
            & (ret_5d >= 3)
            & above_ma
            & near_high_close
            & ((dist_ma20.isna()) | ((dist_ma20 >= -3) & (dist_ma20 <= 18)))
        )
        loose_ma_reclaim = (
            (~strict)
            & (~platform)
            & (~neckline)
            & (~abnormal)
            & (~right_side)
            & (~expansion)
            & (~loose_platform)
            & (~loose_right_side)
            & (volume_ratio >= 1.10)
            & (ret_1d >= 0)
            & above_ma
            & ((dist_ma20.isna()) | ((dist_ma20 >= -2) & (dist_ma20 <= 8)))
        )

        event_type = pd.Series("", index=df.index, dtype="object")
        event_type.loc[strict] = "strict_60d_volume_breakout"
        event_type.loc[platform] = "platform_volume_breakout"
        event_type.loc[neckline] = "neckline_volume_breakout"
        event_type.loc[abnormal] = "abnormal_volume_up"
        event_type.loc[right_side] = "right_side_volume_attack"
        event_type.loc[expansion] = "volume_expansion_watch"
        event_type.loc[loose_platform] = "loose_platform_volume_watch"
        event_type.loc[loose_right_side] = "loose_right_side_volume_watch"
        event_type.loc[loose_ma_reclaim] = "loose_ma_reclaim_volume_watch"

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
                "volume_breakout_score": score,
                "volume_ratio": row.get("volume_ratio"),
                "return_5d_before": row.get("return_5d"),
                "return_20d_before": row.get("return_20d"),
                "distance_to_ma20_pct": row.get("distance_to_ma20_calc"),
                "false_breakout_risk": "True" if "long_upper_shadow_risk" in signal_notes or "not_close_near_high" in signal_notes else "False",
                "overheated_breakout": "True" if safe_float(row.get("return_20d")) > 30 or safe_float(row.get("distance_to_ma20_calc")) > 20 else "False",
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


def _process_price_history_path(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
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

    latest_row = df.iloc[-1]
    latest_signal = detect_volume_breakout(latest_row)
    if latest_signal is not None:
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
                "previous_20d_high": latest_row.get("previous_20d_high_calc"),
                "previous_60d_high": latest_row.get("previous_60d_high_calc"),
                "volume_breakout_type": latest_signal.event_type,
                "volume_watch_scope": latest_signal.scope,
                "volume_breakout_score": latest_signal.score,
                "volume_breakout_notes": "|".join(latest_signal.notes),
                "false_breakout_risk_calc": "True" if "long_upper_shadow_risk" in latest_signal.notes or "not_close_near_high" in latest_signal.notes else "False",
                "overheated_breakout": "True" if safe_float(latest_row.get("return_20d")) > 30 or safe_float(latest_row.get("distance_to_ma20_calc")) > 20 else "False",
            }
        )

    if len(df) < 80:
        return latest_rows, events

    close_s = pd.to_numeric(df["close"], errors="coerce")
    open_s = pd.to_numeric(df["open"], errors="coerce")
    ma20 = pd.to_numeric(df["ma20"], errors="coerce")
    ema23 = pd.to_numeric(df["ema23"], errors="coerce")
    volume_ratio = pd.to_numeric(df["volume_ratio"], errors="coerce")
    ret_1d = pd.to_numeric(df.get("return_1d", df.get("daily_return_calc")), errors="coerce")
    ret_5d = pd.to_numeric(df.get("return_5d"), errors="coerce")
    prev20 = pd.to_numeric(df["previous_20d_high_calc"], errors="coerce")
    prev60 = pd.to_numeric(df["previous_60d_high_calc"], errors="coerce")
    dist_ma20 = pd.to_numeric(df["distance_to_ma20_calc"], errors="coerce")
    dist_prev20 = pd.to_numeric(df["distance_to_previous_20d_high_calc"], errors="coerce")
    close_pos = pd.to_numeric(df["close_position_in_range"], errors="coerce").fillna(1)
    above_ma = ((ma20.isna()) | (close_s >= ma20)) & ((ema23.isna()) | (close_s >= ema23))
    near_high_close = close_pos >= 0.70
    close_above_open = (open_s.isna()) | (close_s >= open_s)

    strict = (close_s > prev60) & (volume_ratio >= 1.5) & near_high_close
    platform = (~strict) & (close_s > prev20) & (volume_ratio >= 1.5) & near_high_close & above_ma
    neckline = (~strict) & (~platform) & (close_s >= prev60 * 0.95) & (volume_ratio >= 1.5) & above_ma & close_above_open
    abnormal = (~strict) & (~platform) & (~neckline) & (volume_ratio >= 3.0) & (ret_1d >= 5) & above_ma & close_above_open
    right_side = (~strict) & (~platform) & (~neckline) & (~abnormal) & (volume_ratio >= 1.2) & (ret_1d >= 4) & above_ma & near_high_close
    expansion = (~strict) & (~platform) & (~neckline) & (~abnormal) & (~right_side) & (volume_ratio >= 1.5) & above_ma & (ret_1d > 0)
    loose_platform = (
        (~strict)
        & (~platform)
        & (~neckline)
        & (~abnormal)
        & (~right_side)
        & (~expansion)
        & (dist_prev20 >= -6)
        & (dist_prev20 <= 2)
        & (volume_ratio >= 1.10)
        & above_ma
        & (close_above_open | near_high_close)
    )
    loose_right_side = (
        (~strict)
        & (~platform)
        & (~neckline)
        & (~abnormal)
        & (~right_side)
        & (~expansion)
        & (~loose_platform)
        & (volume_ratio >= 1.05)
        & (ret_5d >= 3)
        & above_ma
        & near_high_close
        & ((dist_ma20.isna()) | ((dist_ma20 >= -3) & (dist_ma20 <= 18)))
    )
    loose_ma_reclaim = (
        (~strict)
        & (~platform)
        & (~neckline)
        & (~abnormal)
        & (~right_side)
        & (~expansion)
        & (~loose_platform)
        & (~loose_right_side)
        & (volume_ratio >= 1.10)
        & (ret_1d >= 0)
        & above_ma
        & ((dist_ma20.isna()) | ((dist_ma20 >= -2) & (dist_ma20 <= 8)))
    )

    event_type = pd.Series("", index=df.index, dtype="object")
    event_type.loc[strict] = "strict_60d_volume_breakout"
    event_type.loc[platform] = "platform_volume_breakout"
    event_type.loc[neckline] = "neckline_volume_breakout"
    event_type.loc[abnormal] = "abnormal_volume_up"
    event_type.loc[right_side] = "right_side_volume_attack"
    event_type.loc[expansion] = "volume_expansion_watch"
    event_type.loc[loose_platform] = "loose_platform_volume_watch"
    event_type.loc[loose_right_side] = "loose_right_side_volume_watch"
    event_type.loc[loose_ma_reclaim] = "loose_ma_reclaim_volume_watch"

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
            "volume_breakout_score": signal.score if signal else 0,
            "volume_ratio": row.get("volume_ratio"),
            "return_5d_before": row.get("return_5d"),
            "return_20d_before": row.get("return_20d"),
            "distance_to_ma20_pct": row.get("distance_to_ma20_calc"),
            "false_breakout_risk": "True" if "long_upper_shadow_risk" in signal_notes or "not_close_near_high" in signal_notes else "False",
            "overheated_breakout": "True" if safe_float(row.get("return_20d")) > 30 or safe_float(row.get("distance_to_ma20_calc")) > 20 else "False",
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


def build_latest_and_event_frames(max_workers: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    workers = max_workers or min(12, max(2, (os.cpu_count() or 4)))
    latest_rows: list[dict[str, Any]] = []
    event_rows: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for latest_part, events_part in executor.map(_process_price_history_path, paths):
            latest_rows.extend(latest_part)
            event_rows.extend(events_part)
    return pd.DataFrame(latest_rows), pd.DataFrame(event_rows)


def _process_latest_path(path: Path) -> list[dict[str, Any]]:
    df = read_csv(path)
    if df.empty or len(df) < 40:
        return []
    if not {"date", "stock_id", "stock_name", "close", "high", "low", "volume"}.issubset(df.columns):
        return []
    df = add_price_metrics(df)
    if df.empty:
        return []
    row = df.iloc[-1]
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
            "previous_20d_high": row.get("previous_20d_high_calc"),
            "previous_60d_high": row.get("previous_60d_high_calc"),
            "volume_breakout_type": signal.event_type,
            "volume_watch_scope": signal.scope,
            "volume_breakout_score": signal.score,
            "volume_breakout_notes": "|".join(signal.notes),
            "false_breakout_risk_calc": "True" if "long_upper_shadow_risk" in signal.notes or "not_close_near_high" in signal.notes else "False",
            "overheated_breakout": "True" if safe_float(row.get("return_20d")) > 30 or safe_float(row.get("distance_to_ma20_calc")) > 20 else "False",
        }
    ]


def build_latest_frame_fast(max_workers: int | None = None) -> pd.DataFrame:
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    workers = max_workers or min(12, max(2, (os.cpu_count() or 4)))
    latest_rows: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for latest_part in executor.map(_process_latest_path, paths):
            latest_rows.extend(latest_part)
    return pd.DataFrame(latest_rows)


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
            "volume_breakout_score": row.get("volume_breakout_score"),
            "volume_ratio": row.get("volume_ratio"),
            "return_5d_before": row.get("return_5d"),
            "return_20d_before": row.get("return_20d"),
            "distance_to_ma20_pct": row.get("distance_to_ma20_pct"),
            "false_breakout_risk": row.get("false_breakout_risk_calc"),
            "overheated_breakout": row.get("overheated_breakout"),
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
    if "false_breakout_risk" in events.columns:
        group_specs.append(("false_breakout_risk", events.groupby("false_breakout_risk", dropna=False)))
    if "overheated_breakout" in events.columns:
        group_specs.append(("overheated_breakout", events.groupby("overheated_breakout", dropna=False)))
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


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
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
        "decision_priority",
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
        "# Volume Breakout Watch",
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
        "- `strict_60d_volume_breakout` is the strict breakout bucket used by the original breakout list.",
        "- `platform_volume_breakout`, `neckline_volume_breakout`, and `right_side_volume_attack` are volume-confirmed attacks that may be routed to range rebound or pattern watch instead of strict breakout.",
        "- Loose event types are broad recall rows. They intentionally catch early W-bottom/right-side/platform setups, then rely on score, TDCC, repeat appearance, and overheat risk for ranking.",
        "- This list is a visibility and backtest layer. It is not a standalone buy list.",
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
    strict_count = int((watch.get("volume_breakout_type", pd.Series(dtype=str)) == "strict_60d_volume_breakout").sum()) if not watch.empty else 0
    broad_count = int((watch.get("volume_watch_scope", pd.Series(dtype=str)) == "broad_watch").sum()) if not watch.empty else 0
    selected_other_count = int((watch.get("selection_status", pd.Series(dtype=str)) == "selected_but_routed_to_other_category").sum()) if not watch.empty else 0
    not_selected_count = int((watch.get("selection_status", pd.Series(dtype=str)) == "not_selected_by_candidate_model").sum()) if not watch.empty else 0
    lines = [
        "# VOLUME BREAKOUT CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: `{now_text()}`",
        f"- main_price_date: `{main_date}`",
        f"- watch_rows: `{len(watch)}`",
        f"- strict_60d_volume_breakout_count: `{strict_count}`",
        f"- broad_recall_watch_count: `{broad_count}`",
        f"- selected_but_routed_to_other_category_count: `{selected_other_count}`",
        f"- not_selected_by_candidate_model_count: `{not_selected_count}`",
        f"- watch_csv_raw_url: {raw_url(WATCH_CSV)}",
        f"- watch_md_raw_url: {raw_url(WATCH_MD)}",
        f"- backtest_csv_raw_url: {raw_url(BACKTEST_CSV)}",
        f"- backtest_md_raw_url: {raw_url(BACKTEST_MD)}",
        "",
        "## Why Strict Breakout May Look Empty",
        "",
        "- `breakout_latest.csv` only reflects strict 60-day volume-confirmed breakout logic.",
        "- Many volume attacks are routed to `range_rebound` or `pattern_watch` when they are near a neckline/platform but not a strict 60-day breakout.",
        "- Broad recall rows are intentionally listed to reduce missed W-bottom/right-side/platform setups; they must be ranked by score and risk context before interpretation.",
        "- ChatGPT should read this packet when the user asks about 帶量突破 / 放量突破 / 放量攻擊.",
        "",
        "## Top Volume Breakout Watch",
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
                "decision_priority",
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
        "## Not Selected / Routed Elsewhere Diagnostics",
        "",
        *table_lines(
            watch[watch.get("selection_status", "") != "selected_as_strict_breakout"] if not watch.empty and "selection_status" in watch.columns else pd.DataFrame(),
            [
                "stock_id",
                "stock_name",
                "volume_breakout_type",
                "volume_watch_scope",
                "selection_status",
                "not_selected_reason",
                "category",
                "pattern_stage",
                "risk_flags",
            ],
            limit=30,
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
        "- This layer is for visibility and performance tracking, not standalone buy advice.",
        "- Broad recall rows are allowed to be noisy. Treat them as a second-layer universe, not as strict breakouts.",
        "- Use `volume_breakout_priority` to separate valid watch, confirmation-needed, watch-only, and risk-downgrade names.",
        "- Do not call a stock strict breakout unless `volume_breakout_type=strict_60d_volume_breakout` or original `category=true_breakout`.",
        "- If `selection_status=selected_but_routed_to_other_category`, explain the route instead of saying the model missed it.",
        "- If `selection_status=not_selected_by_candidate_model`, list the price-derived signal and its `not_selected_reason`.",
        "- TDCC distribution, stale repeat appearance, long upper shadows, and overheating should downgrade the interpretation.",
        "",
    ]
    PACKET_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def latest_only_summary() -> pd.DataFrame:
    if BACKTEST_CSV.exists():
        return read_csv(BACKTEST_CSV)
    return pd.DataFrame()


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
        latest = build_latest_frame_fast()
        if main_date and not latest.empty:
            latest = latest[latest["signal_date"] == main_date].copy()
        watch = merge_context(latest)
        summary = latest_only_summary()

        write_csv(watch, WATCH_CSV)
        write_watch_md(watch, main_date)
        write_packet(watch, summary, main_date)

        print(f"Saved: {WATCH_CSV} rows={len(watch)}")
        print(f"Saved: {WATCH_MD}")
        print(f"Saved: {PACKET_MD}")
        if summary.empty:
            print("Skipped backtest refresh: --latest-only and no existing backtest summary found")
        else:
            print(f"Loaded existing backtest summary rows={len(summary)}")
        return 0

    full_rebuild = os.environ.get("VOLUME_BREAKOUT_FULL_REBUILD", "").strip().lower() in {"1", "true", "yes"}
    if EVENT_LOG_CSV.exists() and not full_rebuild:
        latest = build_latest_frame_fast()
        events = read_csv(EVENT_LOG_CSV)
        events = append_latest_events_to_history(events, latest)
    else:
        latest, events = build_latest_and_event_frames()
    if main_date and not latest.empty:
        latest = latest[latest["signal_date"] == main_date].copy()
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
    write_watch_md(watch, main_date)
    write_backtest_md(summary, events, main_date)
    write_packet(watch, summary, main_date)

    print(f"Saved: {WATCH_CSV} rows={len(watch)}")
    print(f"Saved: {WATCH_MD}")
    print(f"Saved: {EVENT_LOG_CSV} rows={len(events)}")
    print(f"Saved: {BACKTEST_CSV} rows={len(summary)}")
    print(f"Saved: {BACKTEST_MD}")
    print(f"Saved: {PACKET_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
