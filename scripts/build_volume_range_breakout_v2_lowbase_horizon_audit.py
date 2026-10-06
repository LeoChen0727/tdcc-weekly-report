from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_lowbase_horizon_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_lowbase_horizon_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_lowbase_horizon_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_lowbase_horizon_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_lowbase_horizon_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_lowbase_horizon_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_lowbase_horizon_audit_20260709"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

HORIZONS = [10, 20, 40, 60]
SPLIT_WIN_RATE_GATE = 60.0

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "population_id",
    "population_label",
    "return_basis",
    "entry_rule_id",
    "exit_rule_id",
    "horizon_days",
    "overlap_policy",
    "anomaly_policy",
    "population_definition",
    "baseline_sample_size",
    "source_event_count",
    "simulated_event_count",
    "non_overlap_event_count",
    "sample_size",
    "coverage_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "min_return_pct",
    "max_return_pct",
    "high_return_ge10_count",
    "high_return_ge10_rate_pct",
    "high_return_ge20_count",
    "high_return_ge20_rate_pct",
    "loss_le_minus5_count",
    "loss_le_minus5_rate_pct",
    "median_mfe_pct",
    "p90_mfe_pct",
    "median_mae_pct",
    "data_quality_exception_count",
    "extreme_return_count",
    "same_stock_overlap_suppressed_count",
    "sample_status",
    "split_gate_status",
    "decision_hint",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "current_entry_date",
    "current_exit_date",
    "return_basis",
    "entry_rule_id",
    "exit_rule_id",
    "horizon_days",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "simulated_exit_reason",
    "return_pct",
    "return_outcome",
    "mfe_pct",
    "mae_pct",
    "data_quality_flag",
    "current_operation_return_pct",
    "trigger_id",
    "selected_trigger_id",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_close",
    "previous_60d_high",
    "previous_60d_low",
    "previous_120d_high",
    "previous_120d_low",
    "previous_240d_high",
    "previous_240d_low",
    "off_60d_low_pct",
    "off_120d_low_pct",
    "off_240d_low_pct",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "range_width_120_pct",
    "range_width_240_pct",
    "high_breakout_20d_met",
    "high_breakout_40d_met",
    "high_breakout_60d_met",
    "prev60_high_flag",
    "lowbase_off120_le30_flag",
    "lowbase_off120_le40_flag",
    "deep_low_off240_le30_flag",
    "lowbase_off60_le40_range60_le35_flag",
    "consolidated_any_flag",
    "short_consolidation_flag",
    "long_consolidation_flag",
    "momentum_non_consolidation_flag",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class Population:
    population_id: str
    population_label: str
    definition: str


POPULATIONS = [
    Population("prev60_high_all", "60d previous-high breakout source events", "high_breakout_60d_met=True"),
    Population(
        "general_momentum_non_lowbase",
        "general momentum breakout, excluding strict low-base proxy",
        "high_breakout_60d_met=True and lowbase_off120_le30=False",
    ),
    Population(
        "lowbase_off120_le30",
        "true low-base proxy, off 120d low <=30%",
        "high_breakout_60d_met=True and off_120d_low_pct<=30",
    ),
    Population(
        "lowbase_off120_le40",
        "true low-base proxy, off 120d low <=40%",
        "high_breakout_60d_met=True and off_120d_low_pct<=40",
    ),
    Population(
        "deep_low_off240_le30",
        "deep low-base proxy, off 240d low <=30%",
        "high_breakout_60d_met=True and off_240d_low_pct<=30",
    ),
    Population(
        "lowbase_off60_le40_range60_le35",
        "legacy low/base proxy using 60d low distance and 60d range width",
        "high_breakout_60d_met=True and off_60d_low_pct<=40 and range_width_60_pct<=35",
    ),
    Population(
        "consolidated_any",
        "short or long consolidation breakout",
        "high_breakout_60d_met=True and consolidation_type in short/long",
    ),
    Population(
        "short_consolidation",
        "short consolidation breakout",
        "high_breakout_60d_met=True and consolidation_type=short_consolidation",
    ),
    Population(
        "long_consolidation",
        "long consolidation breakout",
        "high_breakout_60d_met=True and consolidation_type=long_consolidation",
    ),
    Population(
        "lowbase_off120_le40_and_consolidated",
        "true low-base plus consolidation",
        "high_breakout_60d_met=True and off_120d_low_pct<=40 and consolidation_type in short/long",
    ),
    Population(
        "non_consolidation_momentum",
        "non-consolidation momentum breakout",
        "high_breakout_60d_met=True and consolidation_type=non_consolidation",
    ),
]


FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


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
    if text.endswith(".0") and text.replace(".", "", 1).isdigit():
        return text[:-2]
    return text


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def pct_round(value: float | int | None, digits: int = 4) -> float | str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    if math.isnan(number) or math.isinf(number):
        return ""
    return round(number, digits)


def false_text() -> str:
    return "False"


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def source_artifact_version(df: pd.DataFrame) -> str:
    versions = sorted(set(df.get("artifact_version", pd.Series(dtype=str)).astype(str)))
    if len(versions) != 1:
        raise SystemExit(f"ERROR: source detail must have exactly one artifact_version; got {versions[:5]}")
    return versions[0]


def load_source_detail() -> tuple[pd.DataFrame, str]:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        raise SystemExit("ERROR: source semantic detail is empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: source detail must be volume_range_breakout_v2_semantic_audit")
    approved = set(detail.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower())
    if not approved <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain approved_for_daily=False")
    if detail["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique before low-base horizon audit")
    return detail, source_artifact_version(detail)


def load_price_cache(stock_ids: pd.Series) -> dict[str, pd.DataFrame]:
    cache: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(set(stock_ids.astype(str))):
        path = PRICE_DIR / f"{stock_id}.csv"
        if not path.exists():
            cache[stock_id] = pd.DataFrame()
            continue
        price = pd.read_csv(path, dtype=str, keep_default_na=False)
        if price.empty or "date" not in price.columns:
            cache[stock_id] = pd.DataFrame()
            continue
        price = price.copy()
        price["date"] = price["date"].map(normalize_date)
        price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
        for col in ["open", "high", "low", "close", "volume"]:
            price[col] = pd.to_numeric(price.get(col, ""), errors="coerce")
        high = price["high"]
        low = price["low"]
        close = price["close"]
        for window in [60, 120, 240]:
            previous_high = high.shift(1).rolling(window, min_periods=window).max()
            previous_low = low.shift(1).rolling(window, min_periods=window).min()
            price[f"previous_{window}d_high_calc"] = previous_high
            price[f"previous_{window}d_low_calc"] = previous_low
            price[f"off_{window}d_low_pct_calc"] = (close / previous_low.replace(0, pd.NA) - 1.0) * 100.0
            price[f"range_width_{window}_pct_calc"] = (
                (previous_high - previous_low) / previous_low.replace(0, pd.NA) * 100.0
            )
        cache[stock_id] = price
    return cache


def price_row_for_signal(price: pd.DataFrame, signal_date: str) -> tuple[int | None, pd.Series | None]:
    if price.empty:
        return None, None
    matched = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    if not matched:
        return None, None
    idx = int(matched[0])
    return idx, price.iloc[idx]


def prepare_source(detail: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    out = detail.copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    for col in ["signal_date", "confirmation_date", "entry_date", "exit_date"]:
        out[col] = out[col].map(normalize_date)
    numeric_cols = [
        "return_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "signal_close",
        "previous_60d_high",
        "previous_60d_low",
        "off_60d_low_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
    ]
    for col in numeric_cols:
        out[col] = pd.to_numeric(out.get(col, ""), errors="coerce")

    cache = load_price_cache(out["stock_id"])
    rows: list[dict[str, Any]] = []
    for _, row in out.iterrows():
        item = row.to_dict()
        stock_id = normalize_code(row.get("stock_id"))
        signal_date = normalize_date(row.get("signal_date"))
        price = cache.get(stock_id, pd.DataFrame())
        signal_idx, signal_row = price_row_for_signal(price, signal_date)
        item["_signal_idx"] = signal_idx if signal_idx is not None else ""
        item["_price_missing"] = price.empty or signal_idx is None
        if signal_row is not None:
            item["signal_close"] = pct_round(signal_row.get("close"))
            for window in [60, 120, 240]:
                item[f"previous_{window}d_high"] = pct_round(signal_row.get(f"previous_{window}d_high_calc"))
                item[f"previous_{window}d_low"] = pct_round(signal_row.get(f"previous_{window}d_low_calc"))
                item[f"off_{window}d_low_pct"] = pct_round(signal_row.get(f"off_{window}d_low_pct_calc"))
                item[f"range_width_{window}_pct"] = pct_round(signal_row.get(f"range_width_{window}_pct_calc"))
        else:
            for window in [120, 240]:
                item[f"previous_{window}d_high"] = ""
                item[f"previous_{window}d_low"] = ""
                item[f"off_{window}d_low_pct"] = ""
                item[f"range_width_{window}_pct"] = ""
        rows.append(item)

    prepared = pd.DataFrame(rows)
    for col in [
        "return_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "signal_close",
        "previous_60d_high",
        "previous_60d_low",
        "previous_120d_high",
        "previous_120d_low",
        "previous_240d_high",
        "previous_240d_low",
        "off_60d_low_pct",
        "off_120d_low_pct",
        "off_240d_low_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "range_width_120_pct",
        "range_width_240_pct",
    ]:
        prepared[col] = pd.to_numeric(prepared.get(col, ""), errors="coerce")
    prepared["_source_artifact_version"] = source_version
    prepared["_generated_at"] = generated_at
    return prepared


def outcome(return_pct: Any) -> str:
    try:
        value = float(return_pct)
    except (TypeError, ValueError):
        return ""
    if math.isnan(value):
        return ""
    if value > 0:
        return "win"
    if value < 0:
        return "loss"
    return "neutral"


def add_population_flags(detail: pd.DataFrame) -> pd.DataFrame:
    out = detail.copy()
    high60 = out.get("high_breakout_60d_met", pd.Series(dtype=str)).map(boolish)
    consolidated = out.get("consolidation_type", pd.Series(dtype=str)).isin(
        ["short_consolidation", "long_consolidation"]
    )
    short_cons = out.get("consolidation_type", pd.Series(dtype=str)).eq("short_consolidation")
    long_cons = out.get("consolidation_type", pd.Series(dtype=str)).eq("long_consolidation")
    out["prev60_high_flag"] = high60
    out["lowbase_off120_le30_flag"] = high60 & out["off_120d_low_pct"].le(30)
    out["lowbase_off120_le40_flag"] = high60 & out["off_120d_low_pct"].le(40)
    out["deep_low_off240_le30_flag"] = high60 & out["off_240d_low_pct"].le(30)
    out["lowbase_off60_le40_range60_le35_flag"] = (
        high60 & out["off_60d_low_pct"].le(40) & out["range_width_60_pct"].le(35)
    )
    out["consolidated_any_flag"] = high60 & consolidated
    out["short_consolidation_flag"] = high60 & short_cons
    out["long_consolidation_flag"] = high60 & long_cons
    out["momentum_non_consolidation_flag"] = high60 & out.get(
        "consolidation_type", pd.Series(dtype=str)
    ).eq("non_consolidation")
    return out


def population_mask(detail: pd.DataFrame, population_id: str) -> pd.Series:
    if population_id == "prev60_high_all":
        return detail["prev60_high_flag"]
    if population_id == "general_momentum_non_lowbase":
        return detail["prev60_high_flag"] & ~detail["lowbase_off120_le30_flag"]
    if population_id == "lowbase_off120_le30":
        return detail["lowbase_off120_le30_flag"]
    if population_id == "lowbase_off120_le40":
        return detail["lowbase_off120_le40_flag"]
    if population_id == "deep_low_off240_le30":
        return detail["deep_low_off240_le30_flag"]
    if population_id == "lowbase_off60_le40_range60_le35":
        return detail["lowbase_off60_le40_range60_le35_flag"]
    if population_id == "consolidated_any":
        return detail["consolidated_any_flag"]
    if population_id == "short_consolidation":
        return detail["short_consolidation_flag"]
    if population_id == "long_consolidation":
        return detail["long_consolidation_flag"]
    if population_id == "lowbase_off120_le40_and_consolidated":
        return detail["lowbase_off120_le40_flag"] & detail["consolidated_any_flag"]
    if population_id == "non_consolidation_momentum":
        return detail["momentum_non_consolidation_flag"]
    raise KeyError(population_id)


def simulate_fixed_horizon(row: pd.Series, price: pd.DataFrame, horizon_days: int) -> dict[str, Any]:
    stock_id = normalize_code(row.get("stock_id"))
    signal_date = normalize_date(row.get("signal_date"))
    signal_idx, _ = price_row_for_signal(price, signal_date)
    base = {
        "entry_date": "",
        "entry_price": "",
        "exit_date": "",
        "exit_price": "",
        "simulated_exit_reason": "",
        "return_pct": "",
        "return_outcome": "",
        "mfe_pct": "",
        "mae_pct": "",
        "data_quality_flag": "ok",
    }
    if price.empty or signal_idx is None:
        base["data_quality_flag"] = "missing_price_history_or_signal_date"
        return base
    entry_idx = signal_idx + 1
    exit_idx = entry_idx + horizon_days - 1
    if entry_idx >= len(price):
        base["data_quality_flag"] = "missing_next_trading_day_entry"
        return base
    if exit_idx >= len(price):
        base["data_quality_flag"] = "insufficient_forward_price_window"
        return base
    entry = price.iloc[entry_idx]
    exit_row = price.iloc[exit_idx]
    entry_price = pd.to_numeric(pd.Series([entry.get("open")]), errors="coerce").iloc[0]
    exit_price = pd.to_numeric(pd.Series([exit_row.get("close")]), errors="coerce").iloc[0]
    if pd.isna(entry_price) or pd.isna(exit_price) or float(entry_price) <= 0:
        base["data_quality_flag"] = "invalid_entry_or_exit_price"
        return base
    window = price.iloc[entry_idx : exit_idx + 1]
    max_high = pd.to_numeric(window["high"], errors="coerce").max()
    min_low = pd.to_numeric(window["low"], errors="coerce").min()
    ret = (float(exit_price) / float(entry_price) - 1.0) * 100.0
    flag = "ok"
    if abs(ret) >= 80:
        flag = "extreme_return_abs_ge80_review"
    return {
        "entry_date": normalize_date(entry.get("date")),
        "entry_price": pct_round(entry_price),
        "exit_date": normalize_date(exit_row.get("date")),
        "exit_price": pct_round(exit_price),
        "simulated_exit_reason": f"fixed_{horizon_days}d_close_no_stop",
        "return_pct": pct_round(ret),
        "return_outcome": outcome(ret),
        "mfe_pct": pct_round((float(max_high) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(max_high)
        else "",
        "mae_pct": pct_round((float(min_low) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(min_low)
        else "",
        "data_quality_flag": flag,
    }


def simulate_confirmation_fixed_horizon(row: pd.Series, price: pd.DataFrame, horizon_days: int) -> dict[str, Any]:
    confirmation_date = normalize_date(row.get("confirmation_date"))
    confirmation_idx, _ = price_row_for_signal(price, confirmation_date)
    base = {
        "entry_date": "",
        "entry_price": "",
        "exit_date": "",
        "exit_price": "",
        "simulated_exit_reason": "",
        "return_pct": "",
        "return_outcome": "",
        "mfe_pct": "",
        "mae_pct": "",
        "data_quality_flag": "ok",
    }
    if price.empty or confirmation_idx is None:
        base["data_quality_flag"] = "missing_price_history_or_confirmation_date"
        return base
    entry_idx = confirmation_idx + 1
    exit_idx = entry_idx + horizon_days - 1
    if entry_idx >= len(price):
        base["data_quality_flag"] = "missing_next_trading_day_entry"
        return base
    if exit_idx >= len(price):
        base["data_quality_flag"] = "insufficient_forward_price_window"
        return base
    entry = price.iloc[entry_idx]
    exit_row = price.iloc[exit_idx]
    entry_price = pd.to_numeric(pd.Series([entry.get("open")]), errors="coerce").iloc[0]
    exit_price = pd.to_numeric(pd.Series([exit_row.get("close")]), errors="coerce").iloc[0]
    if pd.isna(entry_price) or pd.isna(exit_price) or float(entry_price) <= 0:
        base["data_quality_flag"] = "invalid_entry_or_exit_price"
        return base
    window = price.iloc[entry_idx : exit_idx + 1]
    max_high = pd.to_numeric(window["high"], errors="coerce").max()
    min_low = pd.to_numeric(window["low"], errors="coerce").min()
    ret = (float(exit_price) / float(entry_price) - 1.0) * 100.0
    flag = "ok"
    if abs(ret) >= 80:
        flag = "extreme_return_abs_ge80_review"
    return {
        "entry_date": normalize_date(entry.get("date")),
        "entry_price": pct_round(entry_price),
        "exit_date": normalize_date(exit_row.get("date")),
        "exit_price": pct_round(exit_price),
        "simulated_exit_reason": f"fixed_{horizon_days}d_close_no_stop",
        "return_pct": pct_round(ret),
        "return_outcome": outcome(ret),
        "mfe_pct": pct_round((float(max_high) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(max_high)
        else "",
        "mae_pct": pct_round((float(min_low) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(min_low)
        else "",
        "data_quality_flag": flag,
    }


def simulate_close_confirmed_stop_or_fixed_10d(row: pd.Series, price: pd.DataFrame) -> dict[str, Any]:
    confirmation_date = normalize_date(row.get("confirmation_date"))
    confirmation_idx, _ = price_row_for_signal(price, confirmation_date)
    signal_low = pd.to_numeric(pd.Series([row.get("signal_low")]), errors="coerce").iloc[0]
    base = {
        "entry_date": "",
        "entry_price": "",
        "exit_date": "",
        "exit_price": "",
        "simulated_exit_reason": "",
        "return_pct": "",
        "return_outcome": "",
        "mfe_pct": "",
        "mae_pct": "",
        "data_quality_flag": "ok",
    }
    if pd.isna(signal_low):
        base["data_quality_flag"] = "invalid_stop_level"
        return base
    if price.empty or confirmation_idx is None:
        base["data_quality_flag"] = "missing_price_history_or_confirmation_date"
        return base
    entry_idx = confirmation_idx + 1
    fixed_exit_idx = entry_idx + 10 - 1
    if entry_idx >= len(price):
        base["data_quality_flag"] = "missing_next_trading_day_entry"
        return base
    if fixed_exit_idx >= len(price):
        base["data_quality_flag"] = "insufficient_forward_price_window"
        return base

    entry = price.iloc[entry_idx]
    entry_price = pd.to_numeric(pd.Series([entry.get("open")]), errors="coerce").iloc[0]
    if pd.isna(entry_price) or float(entry_price) <= 0:
        base["data_quality_flag"] = "invalid_entry_or_exit_price"
        return base

    exit_idx = fixed_exit_idx
    simulated_exit_reason = "fixed_10d_close"
    monitor = price.iloc[entry_idx:fixed_exit_idx]
    close_values = pd.to_numeric(monitor["close"], errors="coerce")
    stop_hits = close_values[close_values.lt(float(signal_low))]
    if not stop_hits.empty:
        stop_confirm_idx = int(stop_hits.index[0])
        exit_idx = stop_confirm_idx + 1
        simulated_exit_reason = "close_signal_low_stop_next_open"

    exit_row = price.iloc[exit_idx]
    exit_price_col = "open" if simulated_exit_reason == "close_signal_low_stop_next_open" else "close"
    exit_price = pd.to_numeric(pd.Series([exit_row.get(exit_price_col)]), errors="coerce").iloc[0]
    if pd.isna(exit_price):
        base["data_quality_flag"] = "invalid_entry_or_exit_price"
        return base

    window = price.iloc[entry_idx : exit_idx + 1]
    max_high = pd.to_numeric(window["high"], errors="coerce").max()
    min_low = pd.to_numeric(window["low"], errors="coerce").min()
    ret = (float(exit_price) / float(entry_price) - 1.0) * 100.0
    flag = "ok"
    if abs(ret) >= 80:
        flag = "extreme_return_abs_ge80_review"
    return {
        "entry_date": normalize_date(entry.get("date")),
        "entry_price": pct_round(entry_price),
        "exit_date": normalize_date(exit_row.get("date")),
        "exit_price": pct_round(exit_price),
        "simulated_exit_reason": simulated_exit_reason,
        "return_pct": pct_round(ret),
        "return_outcome": outcome(ret),
        "mfe_pct": pct_round((float(max_high) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(max_high)
        else "",
        "mae_pct": pct_round((float(min_low) / float(entry_price) - 1.0) * 100.0)
        if not pd.isna(min_low)
        else "",
        "data_quality_flag": flag,
    }


def detail_base(row: pd.Series, source_version: str, generated_at: str) -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "source_event_key": safe_str(row.get("source_event_key")),
        "stock_id": normalize_code(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "signal_date": normalize_date(row.get("signal_date")),
        "confirmation_date": normalize_date(row.get("confirmation_date")),
        "current_entry_date": normalize_date(row.get("entry_date")),
        "current_exit_date": normalize_date(row.get("exit_date")),
        "current_operation_return_pct": pct_round(row.get("return_pct")),
        "trigger_id": safe_str(row.get("trigger_id")),
        "selected_trigger_id": safe_str(row.get("selected_trigger_id")),
        "classification_id": safe_str(row.get("classification_id")),
        "attack_method": safe_str(row.get("attack_method")),
        "price_position_type": safe_str(row.get("price_position_type")),
        "consolidation_type": safe_str(row.get("consolidation_type")),
        "risk_type": safe_str(row.get("risk_type")),
        "candle_quality": safe_str(row.get("candle_quality")),
        "follow_through_type": safe_str(row.get("follow_through_type")),
        "limit_up_like": bool_text(boolish(row.get("limit_up_like"))),
        "volume_ratio": pct_round(row.get("volume_ratio")),
        "signal_return_1d_pct": pct_round(row.get("signal_return_1d_pct")),
        "signal_close": pct_round(row.get("signal_close")),
        "previous_60d_high": pct_round(row.get("previous_60d_high")),
        "previous_60d_low": pct_round(row.get("previous_60d_low")),
        "previous_120d_high": pct_round(row.get("previous_120d_high")),
        "previous_120d_low": pct_round(row.get("previous_120d_low")),
        "previous_240d_high": pct_round(row.get("previous_240d_high")),
        "previous_240d_low": pct_round(row.get("previous_240d_low")),
        "off_60d_low_pct": pct_round(row.get("off_60d_low_pct")),
        "off_120d_low_pct": pct_round(row.get("off_120d_low_pct")),
        "off_240d_low_pct": pct_round(row.get("off_240d_low_pct")),
        "range_width_20_pct": pct_round(row.get("range_width_20_pct")),
        "range_width_40_pct": pct_round(row.get("range_width_40_pct")),
        "range_width_60_pct": pct_round(row.get("range_width_60_pct")),
        "range_width_120_pct": pct_round(row.get("range_width_120_pct")),
        "range_width_240_pct": pct_round(row.get("range_width_240_pct")),
        "high_breakout_20d_met": bool_text(boolish(row.get("high_breakout_20d_met"))),
        "high_breakout_40d_met": bool_text(boolish(row.get("high_breakout_40d_met"))),
        "high_breakout_60d_met": bool_text(boolish(row.get("high_breakout_60d_met"))),
        "prev60_high_flag": bool_text(bool(row.get("prev60_high_flag"))),
        "lowbase_off120_le30_flag": bool_text(bool(row.get("lowbase_off120_le30_flag"))),
        "lowbase_off120_le40_flag": bool_text(bool(row.get("lowbase_off120_le40_flag"))),
        "deep_low_off240_le30_flag": bool_text(bool(row.get("deep_low_off240_le30_flag"))),
        "lowbase_off60_le40_range60_le35_flag": bool_text(
            bool(row.get("lowbase_off60_le40_range60_le35_flag"))
        ),
        "consolidated_any_flag": bool_text(bool(row.get("consolidated_any_flag"))),
        "short_consolidation_flag": bool_text(bool(row.get("short_consolidation_flag"))),
        "long_consolidation_flag": bool_text(bool(row.get("long_consolidation_flag"))),
        "momentum_non_consolidation_flag": bool_text(bool(row.get("momentum_non_consolidation_flag"))),
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_detail(source: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    cache = load_price_cache(source["stock_id"])
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        base = detail_base(row, source_version, generated_at)
        current_return = row.get("return_pct")
        current_quality = "ok"
        try:
            current_value = float(current_return)
            if math.isnan(current_value):
                current_quality = "missing_current_operation_return"
        except (TypeError, ValueError):
            current_value = math.nan
            current_quality = "missing_current_operation_return"
        if not math.isnan(current_value) and abs(current_value) >= 80:
            current_quality = "extreme_return_abs_ge80_review"
        current = {
            **base,
            "return_basis": "current_semantic_operation_return",
            "entry_rule_id": "existing_confirmation_next_open",
            "exit_rule_id": "existing_signal_low_stop_or_fixed_10d_close",
            "horizon_days": "current",
            "entry_date": normalize_date(row.get("entry_date")),
            "entry_price": "",
            "exit_date": normalize_date(row.get("exit_date")),
            "exit_price": "",
            "simulated_exit_reason": safe_str(row.get("exit_reason")),
            "return_pct": pct_round(current_value),
            "return_outcome": outcome(current_value),
            "mfe_pct": "",
            "mae_pct": "",
            "data_quality_flag": current_quality,
        }
        rows.append(current)

        price = cache.get(normalize_code(row.get("stock_id")), pd.DataFrame())
        for horizon in HORIZONS:
            simulated = simulate_fixed_horizon(row, price, horizon)
            rows.append(
                {
                    **base,
                    **simulated,
                    "return_basis": "signal_next_open_fixed_close",
                    "entry_rule_id": "signal_next_trading_day_open",
                    "exit_rule_id": f"fixed_{horizon}d_close_no_intraday_stop",
                    "horizon_days": str(horizon),
                }
            )
            confirmation_simulated = simulate_confirmation_fixed_horizon(row, price, horizon)
            rows.append(
                {
                    **base,
                    **confirmation_simulated,
                    "return_basis": "confirmation_next_open_fixed_close",
                    "entry_rule_id": "confirmation_next_trading_day_open",
                    "exit_rule_id": f"fixed_{horizon}d_close_no_intraday_stop",
                    "horizon_days": str(horizon),
                }
            )
        close_stop_simulated = simulate_close_confirmed_stop_or_fixed_10d(row, price)
        rows.append(
            {
                **base,
                **close_stop_simulated,
                "return_basis": "confirmation_next_open_close_signal_low_stop_or_fixed_10d_close",
                "entry_rule_id": "confirmation_next_trading_day_open",
                "exit_rule_id": "close_signal_low_stop_next_open_or_fixed_10d_close",
                "horizon_days": "10",
            }
        )

    detail = pd.DataFrame(rows)
    for col in ["return_pct", "mfe_pct", "mae_pct"]:
        detail[col] = pd.to_numeric(detail.get(col, ""), errors="coerce")
    return detail


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    sample_size = int(len(returns))
    if sample_size == 0:
        return {
            "sample_size": 0,
            "win_count": 0,
            "neutral_count": 0,
            "loss_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "loss_rate_pct": "",
            "avg_return_pct": "",
            "median_return_pct": "",
            "p10_return_pct": "",
            "p90_return_pct": "",
            "min_return_pct": "",
            "max_return_pct": "",
            "high_return_ge10_count": 0,
            "high_return_ge10_rate_pct": "",
            "high_return_ge20_count": 0,
            "high_return_ge20_rate_pct": "",
            "loss_le_minus5_count": 0,
            "loss_le_minus5_rate_pct": "",
            "median_mfe_pct": "",
            "p90_mfe_pct": "",
            "median_mae_pct": "",
            "extreme_return_count": 0,
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
    high10 = int((returns >= 10).sum())
    high20 = int((returns >= 20).sum())
    loss5 = int((returns <= -5).sum())
    mfe = pd.to_numeric(part.get("mfe_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    mae = pd.to_numeric(part.get("mae_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    return {
        "sample_size": sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100.0, 2),
        "loss_rate_pct": pct_round(loss_count / sample_size * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
        "high_return_ge10_count": high10,
        "high_return_ge10_rate_pct": pct_round(high10 / sample_size * 100.0, 2),
        "high_return_ge20_count": high20,
        "high_return_ge20_rate_pct": pct_round(high20 / sample_size * 100.0, 2),
        "loss_le_minus5_count": loss5,
        "loss_le_minus5_rate_pct": pct_round(loss5 / sample_size * 100.0, 2),
        "median_mfe_pct": pct_round(float(mfe.median())) if len(mfe) else "",
        "p90_mfe_pct": pct_round(float(mfe.quantile(0.90))) if len(mfe) else "",
        "median_mae_pct": pct_round(float(mae.median())) if len(mae) else "",
        "extreme_return_count": int(returns.abs().ge(80).sum()),
    }


def mark_non_overlap(part: pd.DataFrame) -> pd.DataFrame:
    if part.empty:
        out = part.copy()
        out["_non_overlap"] = False
        return out
    out = part.copy()
    out["_signal_date_norm"] = out["signal_date"].map(normalize_date)
    out["_exit_date_norm"] = out["exit_date"].map(normalize_date)
    out["_stock_id_norm"] = out["stock_id"].map(normalize_code)
    out = out.sort_values(["_stock_id_norm", "_signal_date_norm", "_exit_date_norm", "source_event_key"])
    included = []
    last_exit_by_stock: dict[str, str] = {}
    for _, row in out.iterrows():
        stock_id = safe_str(row.get("_stock_id_norm"))
        signal_date = safe_str(row.get("_signal_date_norm"))
        exit_date = safe_str(row.get("_exit_date_norm"))
        if not signal_date or not exit_date:
            included.append(False)
            continue
        last_exit = last_exit_by_stock.get(stock_id, "")
        keep = not last_exit or signal_date > last_exit
        included.append(keep)
        if keep:
            last_exit_by_stock[stock_id] = exit_date
    out["_non_overlap"] = included
    return out


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    return "thin_sample"


def split_gate_status(metrics: dict[str, Any]) -> str:
    try:
        win_rate = float(metrics["win_rate_pct"])
        avg_return = float(metrics["avg_return_pct"])
    except (TypeError, ValueError):
        return "insufficient_sample"
    if win_rate >= SPLIT_WIN_RATE_GATE and avg_return > 0:
        return "passes_return_and_win_gate_research_only"
    return "fails_return_or_win_gate"


def decision_hint(population_id: str, metrics: dict[str, Any]) -> str:
    gate = split_gate_status(metrics)
    if gate == "passes_return_and_win_gate_research_only":
        return "split_candidate_needs_feature_separation_and_raw_producer"
    if population_id.startswith("lowbase") or population_id.startswith("deep_low"):
        return "lowbase_not_split_ready_check_horizon_or_watch_surface"
    if population_id in {"short_consolidation", "non_consolidation_momentum"}:
        return "research_only_promising_subgroup_if_sample_survives"
    return "research_only_diagnostic"


def summary_row(
    population: Population,
    source: pd.DataFrame,
    detail: pd.DataFrame,
    source_version: str,
    generated_at: str,
    return_basis: str,
    horizon_days: str,
    overlap_policy: str,
    anomaly_policy: str,
) -> dict[str, Any]:
    source_part = source[population_mask(source, population.population_id)].copy()
    detail_part = detail[
        detail["source_event_key"].isin(set(source_part["source_event_key"].astype(str)))
        & detail["return_basis"].astype(str).eq(return_basis)
        & detail["horizon_days"].astype(str).eq(str(horizon_days))
    ].copy()
    valid_flags = ["ok", "extreme_return_abs_ge80_review"]
    if anomaly_policy == "exclude_extreme_review":
        valid_flags = ["ok"]
    elif anomaly_policy != "include_extreme_review":
        raise ValueError(f"unexpected anomaly_policy: {anomaly_policy}")
    ok_part = detail_part[detail_part["data_quality_flag"].astype(str).isin(valid_flags)]
    simulated_event_count = int(len(ok_part))
    non_overlap_count = ""
    overlap_suppressed = 0
    metric_part = ok_part
    if overlap_policy == "same_stock_non_overlap":
        marked = mark_non_overlap(ok_part)
        metric_part = marked[marked["_non_overlap"]].copy()
        non_overlap_count = int(len(metric_part))
        overlap_suppressed = int(len(ok_part) - len(metric_part))
    metrics = return_metrics(metric_part)
    source_count = int(len(source_part))
    baseline_count = int(len(source[population_mask(source, "prev60_high_all")]))
    if return_basis == "current_semantic_operation_return":
        entry_rule_id = "existing_confirmation_next_open"
        exit_rule_id = "existing_signal_low_stop_or_fixed_10d_close"
    elif return_basis == "confirmation_next_open_close_signal_low_stop_or_fixed_10d_close":
        entry_rule_id = "confirmation_next_trading_day_open"
        exit_rule_id = "close_signal_low_stop_next_open_or_fixed_10d_close"
    elif return_basis == "confirmation_next_open_fixed_close":
        entry_rule_id = "confirmation_next_trading_day_open"
        exit_rule_id = f"fixed_{horizon_days}d_close_no_intraday_stop"
    else:
        entry_rule_id = "signal_next_trading_day_open"
        exit_rule_id = f"fixed_{horizon_days}d_close_no_intraday_stop"
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": "population_horizon_metrics",
        "population_id": population.population_id,
        "population_label": population.population_label,
        "return_basis": return_basis,
        "entry_rule_id": entry_rule_id,
        "exit_rule_id": exit_rule_id,
        "horizon_days": horizon_days,
        "overlap_policy": overlap_policy,
        "anomaly_policy": anomaly_policy,
        "population_definition": population.definition,
        "baseline_sample_size": baseline_count,
        "source_event_count": source_count,
        "simulated_event_count": simulated_event_count,
        "non_overlap_event_count": non_overlap_count,
        "coverage_pct": pct_round(simulated_event_count / source_count * 100.0, 2) if source_count else "",
        "data_quality_exception_count": int(len(detail_part) - simulated_event_count),
        "same_stock_overlap_suppressed_count": overlap_suppressed,
        "sample_status": sample_status(int(metrics["sample_size"])),
        "split_gate_status": split_gate_status(metrics),
        "decision_hint": decision_hint(population.population_id, metrics),
        "note": "Research-only horizon audit. Fixed-close horizons avoid intraday high/low as realized return prices; MFE/MAE are advisory diagnostics. anomaly_policy separates including vs excluding extreme return review rows.",
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    return row


def build_summary(source: pd.DataFrame, detail: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for population in POPULATIONS:
        for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
            rows.append(
                summary_row(
                    population,
                    source,
                    detail,
                    source_version,
                    generated_at,
                    "current_semantic_operation_return",
                    "current",
                    "all_events",
                    anomaly_policy,
                )
            )
            rows.append(
                summary_row(
                    population,
                    source,
                    detail,
                    source_version,
                    generated_at,
                    "current_semantic_operation_return",
                    "current",
                    "same_stock_non_overlap",
                    anomaly_policy,
                )
            )
        for horizon in HORIZONS:
            for overlap_policy in ["all_events", "same_stock_non_overlap"]:
                for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
                    for return_basis in [
                        "signal_next_open_fixed_close",
                        "confirmation_next_open_fixed_close",
                    ]:
                        rows.append(
                            summary_row(
                                population,
                                source,
                                detail,
                                source_version,
                                generated_at,
                                return_basis,
                                str(horizon),
                                overlap_policy,
                                anomaly_policy,
                            )
                        )
        for overlap_policy in ["all_events", "same_stock_non_overlap"]:
            for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
                rows.append(
                    summary_row(
                        population,
                        source,
                        detail,
                        source_version,
                        generated_at,
                        "confirmation_next_open_close_signal_low_stop_or_fixed_10d_close",
                        "10",
                        overlap_policy,
                        anomaly_policy,
                    )
                )
    return pd.DataFrame(rows)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["(empty)"]
    view = df[columns].head(limit).copy()
    return view.to_markdown(index=False).splitlines()


def write_markdown(summary: pd.DataFrame, path: Path) -> None:
    main_cols = [
        "population_id",
        "return_basis",
        "horizon_days",
        "overlap_policy",
        "anomaly_policy",
        "sample_size",
        "win_rate_pct",
        "loss_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "high_return_ge20_rate_pct",
        "split_gate_status",
    ]
    non_overlap_fixed = summary[
        summary["return_basis"].isin(["signal_next_open_fixed_close", "confirmation_next_open_fixed_close"])
        & summary["overlap_policy"].eq("same_stock_non_overlap")
        & summary["anomaly_policy"].eq("exclude_extreme_review")
    ].copy()
    current_non_overlap = summary[
        summary["return_basis"].eq("current_semantic_operation_return")
        & summary["overlap_policy"].eq("same_stock_non_overlap")
        & summary["anomaly_policy"].eq("exclude_extreme_review")
    ].copy()
    close_stop_non_overlap = summary[
        summary["return_basis"].eq("confirmation_next_open_close_signal_low_stop_or_fixed_10d_close")
        & summary["overlap_policy"].eq("same_stock_non_overlap")
        & summary["anomaly_policy"].eq("exclude_extreme_review")
    ].copy()
    candidates = non_overlap_fixed[
        non_overlap_fixed["split_gate_status"].eq("passes_return_and_win_gate_research_only")
    ].copy()
    lowbase = non_overlap_fixed[non_overlap_fixed["population_id"].astype(str).str.contains("lowbase|deep_low")]
    include_extreme = summary[
        summary["return_basis"].isin(["signal_next_open_fixed_close", "confirmation_next_open_fixed_close"])
        & summary["overlap_policy"].eq("same_stock_non_overlap")
        & summary["anomaly_policy"].eq("include_extreme_review")
        & pd.to_numeric(summary["extreme_return_count"], errors="coerce").fillna(0).gt(0)
    ].copy()
    lines = [
        "# Volume Range Breakout V2 Low-Base Horizon Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        f"- approved_for_daily: `False`",
        "- This artifact is research-only and does not change `stock_model_contract_registry.csv`.",
        "- It diagnoses whether low-base consolidation needs a different holding horizon before any model split discussion.",
        "- Fixed-close horizon returns compare signal next trading day open and confirmation next trading day open entries against fixed future close exits.",
        "- Close-confirmed stop test uses confirmation next trading day open entry, close below signal-day low as stop confirmation, next trading day open stop exit, otherwise fixed 10th trading-day close exit.",
        "- MFE/MAE use intraday high/low only as advisory diagnostics, not as realized return or promotion evidence.",
        "- Split gate heuristic here is win_rate_pct >= 60 and avg_return_pct > 0; feature separation still needs review.",
        "- Main tables use `exclude_extreme_review`; rows with `abs(return)>=80%` are summarized separately and are not promotion evidence.",
        "",
        "## Current Semantic Operation Return",
        "",
        *markdown_table(
            current_non_overlap.sort_values(["population_id"]),
            main_cols,
            30,
        ),
        "",
        "## Close-Confirmed Signal-Low Stop Test",
        "",
        *markdown_table(
            close_stop_non_overlap.sort_values(["population_id"]),
            main_cols,
            30,
        ),
        "",
        "## Fixed-Close Horizon Returns, Same-Stock Non-Overlap",
        "",
        *markdown_table(
            non_overlap_fixed.sort_values(["population_id", "horizon_days"]),
            main_cols,
            80,
        ),
        "",
        "## Low-Base Horizon Focus",
        "",
        *markdown_table(
            lowbase.sort_values(["population_id", "horizon_days"]),
            main_cols
            + [
                "high_return_ge10_rate_pct",
                "loss_le_minus5_rate_pct",
                "data_quality_exception_count",
                "same_stock_overlap_suppressed_count",
            ],
            80,
        ),
        "",
        "## Rows Passing Simple Split Gate",
        "",
        *markdown_table(
            candidates.sort_values(["avg_return_pct", "win_rate_pct"], ascending=[False, False]),
            main_cols,
            30,
        ),
        "",
        "## Including Extreme Review Rows",
        "",
        *markdown_table(
            include_extreme.sort_values(["population_id", "horizon_days"]),
            main_cols + ["extreme_return_count", "max_return_pct", "min_return_pct"],
            80,
        ),
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV}`",
        f"- history_summary_csv: `{HISTORY_SUMMARY_CSV}`",
        f"- history_detail_csv: `{HISTORY_DETAIL_CSV}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source_raw, source_version = load_source_detail()
    source = add_population_flags(prepare_source(source_raw, source_version, generated_at))
    detail = build_detail(source, source_version, generated_at)
    summary = build_summary(source, detail, source_version, generated_at)

    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_markdown(summary, LATEST_MD)
    print(
        f"{RESEARCH_ID} written summary_rows={len(summary)} detail_rows={len(detail)} "
        f"source_rows={len(source)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
