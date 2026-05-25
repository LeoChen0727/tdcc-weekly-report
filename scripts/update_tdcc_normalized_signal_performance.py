from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    TDCC_SIGNALS_DIR,
    classify_market_regime,
    load_market_index_history,
    load_price_history,
    market_return_after,
    market_row_on_or_before,
    normalize_code,
    normalize_date,
    now_text,
    pct_return,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


NORMALIZED_LOG = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
PERFORMANCE_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_performance.csv"
HORIZONS = [1, 2, 5, 10, 20]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


def infer_benchmark(row: pd.Series, price_row: pd.Series | None) -> str:
    text = safe_str(row.get("benchmark_index", "")).upper()
    if text in {"TWSE", "TPEX"}:
        return text
    if price_row is not None:
        market = safe_str(price_row.get("market", "")).upper()
        if "TPEX" in market or "OTC" in market:
            return "TPEX"
        if "TWSE" in market:
            return "TWSE"
    return "TWSE"


def price_position(price: pd.DataFrame, signal_date: str) -> int | None:
    if price.empty or "date" not in price.columns:
        return None
    subset = price[price["date"] <= signal_date]
    if subset.empty:
        return None
    return int(subset.index[-1])


def signal_performance_row(row: pd.Series, price_cache: dict[str, pd.DataFrame], index_history: pd.DataFrame) -> dict[str, Any]:
    signal_date = normalize_date(row.get("signal_date", ""))
    code = normalize_code(row.get("code", row.get("stock_id", "")))
    signal_id = safe_str(row.get("signal_id")) or f"{signal_date}_{code}_normalized"
    price = price_cache.setdefault(code, load_price_history(code))
    pos = price_position(price, signal_date)

    out: dict[str, Any] = {
        "signal_id": signal_id,
        "signal_date": signal_date,
        "code": code,
        "name": safe_str(row.get("name", "")),
        "signal_type": "tdcc_normalized_accumulation",
        "threshold_group": threshold_group(row),
        "rank": "",
        "current_pct": "",
        "previous_pct": "",
        "weekly_change_pct": row.get("weekly_change_1000", row.get("tdcc_1w_change_1000", "")),
        "is_consecutive_2w": as_bool(row.get("is_consecutive_2w")) or to_number(row.get("tdcc_consecutive_up_weeks"), 0) >= 2,
        "consecutive_score": row.get("tdcc_consecutive_up_weeks", ""),
        "source_tdcc_date": signal_date,
        "source_compare_date": "",
        "created_at": now_text(),
        "signal_trade_date": signal_date,
        "tdcc_price_phase": row.get("tdcc_price_phase", ""),
        "setup_type": row.get("setup_type", ""),
        "abm_score": row.get("abm_score", ""),
    }

    if pos is None:
        out["benchmark_index"] = safe_str(row.get("benchmark_index", "")) or "unknown"
        out["market_regime"] = "unknown"
        out["signal_close"] = ""
        out["pre_signal_5d_return_pct"] = ""
        out["status"] = "missing_price"
        for horizon in HORIZONS:
            fill_empty_horizon(out, horizon)
        return out

    price_row = price.loc[pos]
    signal_close = to_number(price_row.get("close"))
    benchmark = infer_benchmark(row, price_row)
    market_row = market_row_on_or_before(index_history, benchmark, signal_date)
    out["benchmark_index"] = benchmark
    out["market_regime"] = classify_market_regime(market_row)
    out["signal_close"] = signal_close
    if pos >= 5:
        out["pre_signal_5d_return_pct"] = pct_return(signal_close, price.loc[pos - 5, "close"])
    else:
        out["pre_signal_5d_return_pct"] = ""

    available = max(0, len(price) - pos - 1)
    out["available_days_after_signal"] = available
    for horizon in HORIZONS:
        add_horizon(out, price, pos, signal_close, index_history, benchmark, horizon)
    out["status"] = maturity_status(out)
    return out


def threshold_group(row: pd.Series) -> str:
    parts: list[str] = []
    for threshold in [400, 600, 800, 1000]:
        if as_bool(row.get(f"has_{threshold}", "")):
            parts.append(str(threshold))
    return "over_" + "_".join(parts) if parts else "normalized"


def fill_empty_horizon(out: dict[str, Any], horizon: int) -> None:
    for key in [
        f"d{horizon}_close",
        f"d{horizon}_return_pct",
        f"twse_close_d{horizon}",
        f"twse_return_d{horizon}",
        f"relative_return_vs_twse_d{horizon}",
        f"tpex_close_d{horizon}",
        f"tpex_return_d{horizon}",
        f"relative_return_vs_tpex_d{horizon}",
        f"relative_return_vs_benchmark_d{horizon}",
        f"max_high_after_signal_{horizon}d",
        f"max_return_{horizon}d",
        f"min_low_after_signal_{horizon}d",
        f"max_drawdown_{horizon}d",
    ]:
        out[key] = ""
    out[f"mature_d{horizon}"] = False


def add_horizon(
    out: dict[str, Any],
    price: pd.DataFrame,
    pos: int,
    signal_close: float,
    index_history: pd.DataFrame,
    benchmark: str,
    horizon: int,
) -> None:
    fill_empty_horizon(out, horizon)
    if math.isnan(signal_close) or signal_close <= 0:
        return
    target_pos = pos + horizon
    mature = target_pos < len(price)
    if mature:
        close_h = to_number(price.loc[target_pos, "close"])
        out[f"d{horizon}_close"] = close_h
        out[f"d{horizon}_return_pct"] = pct_return(close_h, signal_close)
    window = price.iloc[pos + 1 : min(len(price), target_pos + 1)]
    if not window.empty:
        out[f"max_high_after_signal_{horizon}d"] = to_number(window["high"].max()) if "high" in window.columns else ""
        out[f"max_return_{horizon}d"] = pct_return(out[f"max_high_after_signal_{horizon}d"], signal_close)
        out[f"min_low_after_signal_{horizon}d"] = to_number(window["low"].min()) if "low" in window.columns else ""
        out[f"max_drawdown_{horizon}d"] = pct_return(out[f"min_low_after_signal_{horizon}d"], signal_close)

    twse_close, twse_return = market_return_after(index_history, "TWSE", out["signal_date"], horizon)
    tpex_close, tpex_return = market_return_after(index_history, "TPEX", out["signal_date"], horizon)
    out[f"twse_close_d{horizon}"] = twse_close
    out[f"twse_return_d{horizon}"] = twse_return
    out[f"tpex_close_d{horizon}"] = tpex_close
    out[f"tpex_return_d{horizon}"] = tpex_return
    stock_return = to_number(out.get(f"d{horizon}_return_pct"))
    out[f"relative_return_vs_twse_d{horizon}"] = "" if math.isnan(stock_return) or math.isnan(twse_return) else stock_return - twse_return
    out[f"relative_return_vs_tpex_d{horizon}"] = "" if math.isnan(stock_return) or math.isnan(tpex_return) else stock_return - tpex_return
    benchmark_return = twse_return if benchmark == "TWSE" else tpex_return if benchmark == "TPEX" else math.nan
    out[f"relative_return_vs_benchmark_d{horizon}"] = "" if math.isnan(stock_return) or math.isnan(benchmark_return) else stock_return - benchmark_return
    out[f"mature_d{horizon}"] = bool(mature and not math.isnan(stock_return))


def maturity_status(row: dict[str, Any]) -> str:
    mature = [h for h in HORIZONS if as_bool(row.get(f"mature_d{h}"))]
    if not mature:
        return "pending"
    return f"mature_{max(mature)}d"


def normalize_existing_perf(perf: pd.DataFrame) -> pd.DataFrame:
    if perf.empty:
        return perf
    if "code" not in perf.columns and "stock_id" in perf.columns:
        perf["code"] = perf["stock_id"]
    if "signal_date" in perf.columns:
        perf["signal_date"] = perf["signal_date"].map(normalize_date)
    if "code" in perf.columns:
        perf["code"] = perf["code"].map(normalize_code)
    if "signal_id" not in perf.columns:
        perf["signal_id"] = ""
    perf["signal_id"] = perf["signal_id"].where(
        perf["signal_id"].astype(str).str.len() > 0,
        perf["signal_date"].astype(str) + "_" + perf["code"].astype(str) + "_normalized",
    )
    return perf


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update normalized TDCC signal performance using stock price history.")
    parser.add_argument("--overwrite", action="store_true", help="Drop old performance rows and write normalized rows only.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    normalized = read_csv(NORMALIZED_LOG, dtype=str)
    if normalized.empty:
        raise FileNotFoundError(f"Missing or empty {NORMALIZED_LOG}. Run build_tdcc_signal_structures.py first.")
    normalized["signal_date"] = normalized["signal_date"].map(normalize_date)
    normalized["code"] = normalized["code"].map(normalize_code)
    normalized = normalized.drop_duplicates(["signal_date", "code"], keep="last")
    index_history = load_market_index_history(update_if_missing=True)
    price_cache: dict[str, pd.DataFrame] = {}
    rows = [signal_performance_row(row, price_cache, index_history) for _, row in normalized.iterrows()]
    new_perf = pd.DataFrame(rows)

    if args.overwrite:
        out = new_perf
    else:
        old = normalize_existing_perf(read_csv(PERFORMANCE_CSV, dtype=str))
        out = pd.concat([old, new_perf], ignore_index=True, sort=False) if not old.empty else new_perf
        out = normalize_existing_perf(out)
        out = out.drop_duplicates("signal_id", keep="last")

    out = out.sort_values(["signal_date", "code"]).reset_index(drop=True)
    write_csv(out, PERFORMANCE_CSV)
    print(f"Saved: {PERFORMANCE_CSV}")
    print(f"normalized_signals: {len(normalized)}")
    print(f"performance_rows: {len(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
