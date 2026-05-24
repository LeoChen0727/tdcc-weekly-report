from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DAILY_SIGNALS_DIR,
    HORIZONS,
    load_market_index_history,
    load_price_history,
    market_return_after,
    normalize_code,
    normalize_date,
    now_text,
    pct_return,
    safe_str,
    to_number,
    write_csv,
)


SIGNAL_LOG = DAILY_SIGNALS_DIR / "daily_candidate_signal_log.csv"
PERFORMANCE_CSV = DAILY_SIGNALS_DIR / "daily_candidate_signal_performance.csv"


BASE_COLUMNS = [
    "signal_id",
    "signal_date",
    "stock_id",
    "stock_name",
    "category",
    "score",
    "rank",
    "priority",
    "sector",
    "sub_theme",
    "tdcc_status",
    "warrant_status",
    "close_at_signal",
    "benchmark_index",
    "market_regime",
    "is_construction_recognition",
    "recognition_type",
    "revenue_signal_type",
    "theme_strength_score",
    "catalyst_strength_score",
    "catalyst_tags",
    "fundamental_catalyst_score",
    "fundamental_catalyst_tags",
    "event_catalyst_tags",
    "price_reaction_level",
    "similar_to_shihsinko_flag",
    "eps_surprise_flag",
    "earnings_acceleration_flag",
    "margin_improvement_flag",
    "profit_turnaround_flag",
    "revenue_good_eps_unconfirmed_flag",
    "theme_catalyst_flag",
    "theme_catalyst_tags",
    "catalyst_date",
    "low_reaction_after_catalyst",
    "already_reacted_to_catalyst",
    "catalyst_quality",
    "catalyst_confidence",
]


def base_position(price: pd.DataFrame, signal_date: str) -> int | None:
    if price.empty:
        return None
    signal_date = normalize_date(signal_date)
    candidates = price[price["date"] <= signal_date]
    if candidates.empty:
        return None
    return int(candidates.index[-1])


def value_or_blank(value: Any) -> Any:
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    if isinstance(value, float) and math.isnan(value):
        return ""
    return value


def compute_stock_metrics(row: pd.Series) -> dict[str, Any]:
    stock_id = normalize_code(row.get("stock_id", ""))
    signal_date = normalize_date(row.get("signal_date", ""))
    price = load_price_history(stock_id)
    pos = base_position(price, signal_date)
    out: dict[str, Any] = {
        "updated_at": now_text(),
        "available_days_after_signal": 0,
        "break_high_after_signal": "",
        "failed_breakout": "",
        "gap_up_failed": "",
        "volume_follow_through": "",
    }
    if pos is None:
        return out

    signal_close = to_number(row.get("close_at_signal"))
    if math.isnan(signal_close) or signal_close <= 0:
        signal_close = to_number(price.loc[pos, "close"])
    out["close_at_signal"] = signal_close
    out["available_days_after_signal"] = max(0, len(price) - pos - 1)
    signal_high = to_number(price.loc[pos, "high"])

    next_window = price.iloc[pos + 1 : min(len(price), pos + 21)].copy()
    out["break_high_after_signal"] = "True" if not next_window.empty and next_window["high"].max() > signal_high else "False"
    out["failed_breakout"] = "True" if out["break_high_after_signal"] == "True" and out["available_days_after_signal"] >= 5 and to_number(next_window.iloc[min(4, len(next_window) - 1)].get("close")) < signal_close else "False"
    if out["available_days_after_signal"] >= 1 and pos + 1 < len(price):
        next_row = price.loc[pos + 1]
        next_open = to_number(next_row.get("open"))
        next_close = to_number(next_row.get("close"))
        out["gap_up_failed"] = "True" if next_open > signal_close * 1.03 and next_close < next_open else "False"
    if not next_window.empty and "volume_ratio" in next_window.columns:
        out["volume_follow_through"] = "True" if pd.to_numeric(next_window["volume_ratio"], errors="coerce").max() >= 1.2 else "False"

    for horizon in HORIZONS:
        target = pos + horizon
        if target < len(price):
            close_h = to_number(price.loc[target, "close"])
            out[f"close_d{horizon}"] = close_h
            out[f"return_d{horizon}"] = pct_return(close_h, signal_close)
        else:
            out[f"close_d{horizon}"] = ""
            out[f"return_d{horizon}"] = ""

        window = price.iloc[pos + 1 : min(len(price), pos + horizon + 1)].copy()
        if window.empty:
            out[f"max_high_d{horizon}"] = ""
            out[f"mfe_d{horizon}"] = ""
            out[f"max_drawdown_d{horizon}"] = ""
            out[f"mae_d{horizon}"] = ""
        else:
            max_high = to_number(window["high"].max())
            min_low = to_number(window["low"].min())
            out[f"max_high_d{horizon}"] = max_high
            out[f"mfe_d{horizon}"] = pct_return(max_high, signal_close)
            out[f"max_drawdown_d{horizon}"] = pct_return(min_low, signal_close)
            out[f"mae_d{horizon}"] = pct_return(min_low, signal_close)

    out["hit_3pct_d5"] = "True" if to_number(out.get("mfe_d5")) >= 3 else "False"
    out["hit_5pct_d10"] = "True" if to_number(out.get("mfe_d10")) >= 5 else "False"
    out["hit_10pct_d20"] = "True" if to_number(out.get("mfe_d20")) >= 10 else "False"
    return out


def compute_market_metrics(row: pd.Series, index_df: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {}
    signal_date = normalize_date(row.get("signal_date", ""))
    benchmark = safe_str(row.get("benchmark_index", "unknown")).upper()
    for index_code, prefix in [("TWSE", "twse"), ("TPEX", "tpex")]:
        for horizon in HORIZONS:
            close_h, ret = market_return_after(index_df, index_code, signal_date, horizon)
            out[f"{prefix}_close_d{horizon}"] = value_or_blank(close_h)
            out[f"{prefix}_return_d{horizon}"] = value_or_blank(ret)
            stock_ret = to_number(row.get(f"return_d{horizon}"))
            if math.isnan(stock_ret) or math.isnan(ret):
                out[f"relative_return_vs_{prefix}_d{horizon}"] = ""
            else:
                out[f"relative_return_vs_{prefix}_d{horizon}"] = stock_ret - ret
    for horizon in HORIZONS:
        if benchmark == "TPEX":
            out[f"relative_return_vs_benchmark_d{horizon}"] = out.get(f"relative_return_vs_tpex_d{horizon}", "")
        elif benchmark == "TWSE":
            out[f"relative_return_vs_benchmark_d{horizon}"] = out.get(f"relative_return_vs_twse_d{horizon}", "")
        else:
            out[f"relative_return_vs_benchmark_d{horizon}"] = ""
    return out


def build_performance(log: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    index_df = load_market_index_history(update_if_missing=True)
    for _, source in log.iterrows():
        row = {col: source.get(col, "") for col in BASE_COLUMNS if col in log.columns}
        row["signal_id"] = safe_str(source.get("signal_id", "")) or f"{normalize_date(source.get('signal_date'))}_{normalize_code(source.get('stock_id'))}_{safe_str(source.get('category'))}"
        row["signal_date"] = normalize_date(source.get("signal_date", ""))
        row["stock_id"] = normalize_code(source.get("stock_id", ""))
        stock_metrics = compute_stock_metrics(pd.Series({**source.to_dict(), **row}))
        row.update(stock_metrics)
        row.update(compute_market_metrics(pd.Series(row), index_df))
        rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    for col in ["signal_date", "category", "stock_id"]:
        if col not in out.columns:
            out[col] = ""
    return out.sort_values(["signal_date", "category", "stock_id"]).reset_index(drop=True)


def main() -> int:
    if not SIGNAL_LOG.exists():
        raise FileNotFoundError(f"Missing {SIGNAL_LOG}")
    log = pd.read_csv(SIGNAL_LOG, dtype=str, keep_default_na=False)
    if log.empty:
        raise RuntimeError("daily candidate signal log is empty")
    perf = build_performance(log)
    write_csv(perf, PERFORMANCE_CSV)
    print(f"Saved: {PERFORMANCE_CSV}, rows={len(perf)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
