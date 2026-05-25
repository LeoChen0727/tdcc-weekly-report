from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DAILY_SIGNALS_DIR,
    HORIZONS,
    LATEST_DIR,
    append_update_csv,
    classify_market_regime,
    infer_benchmark_index,
    is_construction_like,
    load_market_index_history,
    load_price_history,
    main_price_date_from_freshness,
    market_row_on_or_before,
    normalize_code,
    normalize_date,
    now_text,
    recognition_type,
    resolve_candidate_signal_date,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
SIGNAL_LOG = DAILY_SIGNALS_DIR / "daily_candidate_signal_log.csv"
SIGNAL_LOG_ALIAS = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")


OUTPUT_COLUMNS = [
    "signal_id",
    "signal_date",
    "report_date",
    "stock_id",
    "stock_name",
    "market",
    "industry",
    "sector",
    "sub_theme",
    "category",
    "category_cn",
    "score",
    "rank",
    "priority",
    "revaluation_priority",
    "tdcc_status",
    "tdcc_400_delta",
    "tdcc_1000_delta",
    "warrant_status",
    "warrant_call_amount",
    "revenue_yoy",
    "cum_revenue_yoy",
    "recent_revenue_accel",
    "close",
    "close_at_signal",
    "volume",
    "volume_ratio",
    "ma20",
    "ma60",
    "ema23",
    "distance_to_ma20",
    "distance_to_ma60",
    "distance_to_high_20",
    "distance_to_high_60",
    "near_platform",
    "break_prior_high",
    "already_priced_in",
    "overheat_flag",
    "distribution_warning",
    "downgrade_reason",
    "is_construction_recognition",
    "recognition_type",
    "revenue_signal_type",
    "theme_strength_score",
    "catalyst_strength_score",
    "catalyst_tags",
    "fundamental_catalyst_score",
    "fundamental_catalyst_tags",
    "event_catalyst_tags",
    "event_calendar_tags",
    "event_proximity_score",
    "nearest_event_date",
    "nearest_event_type",
    "nearest_event_name",
    "days_to_nearest_event",
    "event_calendar_source",
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
    "catalyst_source",
    "catalyst_summary",
    "low_reaction_after_catalyst",
    "already_reacted_to_catalyst",
    "catalyst_quality",
    "catalyst_confidence",
    "source_file",
    "signal_source_file",
    "pipeline_commit_sha",
    "twse_close_at_signal",
    "tpex_close_at_signal",
    "twse_5d_return_at_signal",
    "twse_10d_return_at_signal",
    "twse_20d_return_at_signal",
    "tpex_5d_return_at_signal",
    "tpex_10d_return_at_signal",
    "tpex_20d_return_at_signal",
    "twse_above_ma20",
    "twse_above_ma60",
    "tpex_above_ma20",
    "tpex_above_ma60",
    "market_regime",
    "benchmark_index",
    "created_at",
    "updated_at",
]


def first_value(row: pd.Series, names: list[str], default: str = "") -> str:
    for name in names:
        if name in row.index:
            value = safe_str(row.get(name, ""))
            if value:
                return value
    return default


def git_sha() -> str:
    env = os.environ.get("GITHUB_SHA", "").strip()
    if env:
        return env
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return ""


def bool_from_text(value: Any) -> str:
    text = safe_str(value).lower()
    return "True" if text in {"true", "1", "yes", "y"} else "False"


def market_meta(index_df: pd.DataFrame, date: str, market: str) -> dict[str, str]:
    twse = market_row_on_or_before(index_df, "TWSE", date)
    tpex = market_row_on_or_before(index_df, "TPEX", date)
    bench = infer_benchmark_index(market)
    regime_row = tpex if bench == "TPEX" else twse
    out: dict[str, str] = {
        "benchmark_index": bench,
        "market_regime": classify_market_regime(regime_row),
    }
    for prefix, row in [("twse", twse), ("tpex", tpex)]:
        out[f"{prefix}_close_at_signal"] = safe_str(row.get("close", "")) if row is not None else ""
        for horizon in [5, 10, 20]:
            out[f"{prefix}_{horizon}d_return_at_signal"] = safe_str(row.get(f"return_{horizon}d", "")) if row is not None else ""
        out[f"{prefix}_above_ma20"] = safe_str(row.get("above_ma20", "")) if row is not None else ""
        out[f"{prefix}_above_ma60"] = safe_str(row.get("above_ma60", "")) if row is not None else ""
    return out


def stock_market_from_history(stock_id: str, fallback: str) -> str:
    if fallback:
        return fallback
    price = load_price_history(stock_id)
    if price.empty or "market" not in price.columns:
        return ""
    values = price["market"].dropna().astype(str)
    values = values[values.str.len() > 0]
    return values.iloc[-1] if not values.empty else ""


def row_to_signal(row: pd.Series, main_date: str, index_df: pd.DataFrame, sha: str) -> dict[str, str]:
    stock_id = normalize_code(first_value(row, ["stock_id", "ticker", "code"]))
    stock_name = first_value(row, ["stock_name", "name"])
    category = first_value(row, ["category", "category_cn"])
    market = stock_market_from_history(stock_id, first_value(row, ["market"]))
    construction = is_construction_like(row)
    is_recognition = first_value(row, ["is_construction_recognition"]) or ("True" if construction else "False")
    rec_type = first_value(row, ["recognition_type"]) or (recognition_type(row) if construction else "")
    signal_id = f"{main_date}_{stock_id}_{category}".replace(" ", "_").replace("/", "_")
    meta = market_meta(index_df, main_date, market)

    close = first_value(row, ["close", "close_at_signal"])
    if not close:
        price = load_price_history(stock_id)
        pos = price.index[price["date"] <= main_date].tolist()[-1] if not price.empty and (price["date"] <= main_date).any() else None
        if pos is not None:
            close = safe_str(price.loc[pos, "close"])

    return {
        "signal_id": signal_id,
        "signal_date": main_date,
        "report_date": main_date,
        "stock_id": stock_id,
        "stock_name": stock_name,
        "market": market,
        "industry": first_value(row, ["industry"]),
        "sector": first_value(row, ["sector", "theme_group"]),
        "sub_theme": first_value(row, ["sub_theme", "細分族群", "theme_group"]),
        "category": category,
        "category_cn": first_value(row, ["category_cn"]),
        "score": first_value(row, ["score", "pattern_score"]),
        "rank": first_value(row, ["rank", "stage_order"]),
        "priority": first_value(row, ["priority"]),
        "revaluation_priority": first_value(row, ["revaluation_priority"]),
        "tdcc_status": first_value(row, ["tdcc_judgement", "tdcc_accumulation_signal", "tdcc_judge", "tdcc_status"]),
        "tdcc_400_delta": first_value(row, ["holder_400_change", "tdcc_400_change_sum", "tdcc_over_400_change"]),
        "tdcc_1000_delta": first_value(row, ["holder_1000_change", "tdcc_1000_change_sum", "tdcc_over_1000_change"]),
        "warrant_status": first_value(row, ["warrant_flow_signal", "warrant_status"]),
        "warrant_call_amount": first_value(row, ["call_turnover"]),
        "revenue_yoy": first_value(row, ["latest_revenue_yoy", "revenue_yoy_pct", "revenue_yoy"]),
        "cum_revenue_yoy": first_value(row, ["cumulative_revenue_yoy", "cumulative_yoy_pct", "cum_revenue_yoy"]),
        "recent_revenue_accel": first_value(row, ["revenue_acceleration_note"]),
        "close": close,
        "close_at_signal": close,
        "volume": first_value(row, ["volume"]),
        "volume_ratio": first_value(row, ["volume_ratio"]),
        "ma20": first_value(row, ["ma20"]),
        "ma60": first_value(row, ["ma60"]),
        "ema23": first_value(row, ["ema23"]),
        "distance_to_ma20": first_value(row, ["distance_to_ma20_pct", "gap_ma20_pct"]),
        "distance_to_ma60": first_value(row, ["distance_to_ma60_pct", "gap_ma60_pct"]),
        "distance_to_high_20": first_value(row, ["distance_to_high_20_pct"]),
        "distance_to_high_60": first_value(row, ["distance_to_high_60_pct"]),
        "near_platform": bool_from_text(first_value(row, ["in_platform", "near_platform"])),
        "break_prior_high": bool_from_text(first_value(row, ["break_prior_high", "limit_up_breakout"])),
        "already_priced_in": bool_from_text(first_value(row, ["already_priced_in"])),
        "overheat_flag": "True" if to_number(first_value(row, ["return_20d", "return_20d_pct"])) > 30 else "False",
        "distribution_warning": "True" if "distribution" in first_value(row, ["tdcc_judgement", "tdcc_accumulation_signal", "tdcc_judge"]).lower() else "False",
        "downgrade_reason": first_value(row, ["downgrade_reason", "priced_in_reason", "revenue_warning"]),
        "is_construction_recognition": is_recognition,
        "recognition_type": rec_type,
        "revenue_signal_type": first_value(row, ["revenue_signal_type"]),
        "theme_strength_score": first_value(row, ["theme_strength_score"]),
        "catalyst_strength_score": first_value(row, ["catalyst_strength_score"]),
        "catalyst_tags": first_value(row, ["catalyst_tags"]),
        "fundamental_catalyst_score": first_value(row, ["fundamental_catalyst_score"]),
        "fundamental_catalyst_tags": first_value(row, ["fundamental_catalyst_tags"]),
        "event_catalyst_tags": first_value(row, ["event_catalyst_tags"]),
        "event_calendar_tags": first_value(row, ["event_calendar_tags"]),
        "event_proximity_score": first_value(row, ["event_proximity_score"]),
        "nearest_event_date": first_value(row, ["nearest_event_date"]),
        "nearest_event_type": first_value(row, ["nearest_event_type"]),
        "nearest_event_name": first_value(row, ["nearest_event_name"]),
        "days_to_nearest_event": first_value(row, ["days_to_nearest_event"]),
        "event_calendar_source": first_value(row, ["event_calendar_source"]),
        "price_reaction_level": first_value(row, ["price_reaction_level"]),
        "similar_to_shihsinko_flag": bool_from_text(first_value(row, ["similar_to_shihsinko_flag"])),
        "eps_surprise_flag": bool_from_text(first_value(row, ["eps_surprise_flag"])),
        "earnings_acceleration_flag": bool_from_text(first_value(row, ["earnings_acceleration_flag"])),
        "margin_improvement_flag": bool_from_text(first_value(row, ["margin_improvement_flag"])),
        "profit_turnaround_flag": bool_from_text(first_value(row, ["profit_turnaround_flag"])),
        "revenue_good_eps_unconfirmed_flag": bool_from_text(first_value(row, ["revenue_good_eps_unconfirmed_flag"])),
        "theme_catalyst_flag": bool_from_text(first_value(row, ["theme_catalyst_flag"])),
        "theme_catalyst_tags": first_value(row, ["theme_catalyst_tags"]),
        "catalyst_date": first_value(row, ["catalyst_date"]),
        "catalyst_source": first_value(row, ["catalyst_source"]),
        "catalyst_summary": first_value(row, ["catalyst_summary"]),
        "low_reaction_after_catalyst": bool_from_text(first_value(row, ["low_reaction_after_catalyst"])),
        "already_reacted_to_catalyst": bool_from_text(first_value(row, ["already_reacted_to_catalyst"])),
        "catalyst_quality": first_value(row, ["catalyst_quality"]),
        "catalyst_confidence": first_value(row, ["catalyst_confidence"]),
        "source_file": ALL_CANDIDATES.as_posix(),
        "signal_source_file": ALL_CANDIDATES.as_posix(),
        "pipeline_commit_sha": sha,
        "created_at": now_text(),
        "updated_at": now_text(),
        **meta,
    }


def main() -> int:
    if not ALL_CANDIDATES.exists():
        raise FileNotFoundError(f"Missing {ALL_CANDIDATES}")
    preferred_date = main_price_date_from_freshness()
    df = pd.read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if df.empty:
        raise RuntimeError("all_candidates_latest.csv is empty")
    main_date, date_notes = resolve_candidate_signal_date(df, preferred_date)
    if not main_date:
        raise RuntimeError("cannot resolve signal_date from all_candidates_latest.csv or data freshness")
    for note in date_notes:
        print(f"WARNING: {note}")

    index_df = load_market_index_history(update_if_missing=True)
    sha = git_sha()
    rows = [row_to_signal(row, main_date, index_df, sha) for _, row in df.iterrows()]
    out = pd.DataFrame(rows)
    for col in OUTPUT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out = out[OUTPUT_COLUMNS]
    combined = append_update_csv(out, SIGNAL_LOG, ["signal_id"], ["signal_date", "category", "stock_id"])
    write_csv(combined, SIGNAL_LOG_ALIAS)
    print(f"Saved: {SIGNAL_LOG}, rows={len(combined)}, appended_or_updated={len(out)}")
    print(f"Saved: {SIGNAL_LOG_ALIAS}, rows={len(combined)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
