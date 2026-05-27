from __future__ import annotations

import math
import shutil
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    MARKET_INDEX_OHLC_PATH,
    STOCK_PRICE_HISTORY_DIR,
    TDCC_SIGNALS_DIR,
    markdown_table,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
PERFORMANCE_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_performance.csv"

LATEST_STATS_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.csv"
LATEST_CANDIDATES_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
LATEST_MD = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.md"

DOCS_STATS_CSV = DOCS_LATEST_DIR / LATEST_STATS_CSV.name
DOCS_CANDIDATES_CSV = DOCS_LATEST_DIR / LATEST_CANDIDATES_CSV.name
DOCS_MD = DOCS_LATEST_DIR / LATEST_MD.name

HORIZONS = [5, 10]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


def num_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series(math.nan, index=df.index)
    return pd.to_numeric(df[col], errors="coerce")


def first_non_empty(series: pd.Series) -> Any:
    for value in series:
        if safe_str(value):
            return value
    return ""


def load_performance() -> pd.DataFrame:
    perf = read_csv(PERFORMANCE_CSV, dtype=str)
    if perf.empty:
        return perf
    if "code" not in perf.columns and "stock_id" in perf.columns:
        perf["code"] = perf["stock_id"]
    for col in ["signal_date", "code", "signal_id"]:
        if col not in perf.columns:
            perf[col] = ""
    perf["signal_id"] = perf["signal_id"].where(
        perf["signal_id"].astype(str).str.len() > 0,
        perf["signal_date"].astype(str) + "_" + perf["code"].astype(str) + "_normalized",
    )
    value_cols = [col for col in perf.columns if col != "signal_id"]
    return perf.groupby("signal_id", as_index=False).agg({col: first_non_empty for col in value_cols})


def load_base() -> pd.DataFrame:
    snap = read_csv(SNAPSHOT_CSV, dtype=str)
    perf = load_performance()
    if snap.empty:
        return pd.DataFrame()
    if "signal_id" not in snap.columns:
        snap["signal_id"] = snap["signal_date"].astype(str) + "_" + snap["code"].astype(str) + "_normalized"
    if not perf.empty:
        snap = snap.merge(perf, on="signal_id", how="left", suffixes=("", "_perf"))
    for col in ["code", "name", "signal_date", "signal_trade_date", "tdcc_price_phase", "benchmark_index"]:
        if col not in snap.columns:
            snap[col] = ""
    snap["event_date"] = snap["signal_trade_date"].where(
        snap["signal_trade_date"].astype(str).str.len() > 0,
        snap["signal_date"],
    )
    snap["event_date"] = snap["event_date"].map(normalize_date)
    snap["code"] = snap["code"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(4)
    return snap


def price_technical_for_rows(rows: pd.DataFrame) -> pd.DataFrame:
    if rows.empty:
        return pd.DataFrame()
    required_pairs = set(zip(rows["code"].astype(str), rows["event_date"].astype(str)))
    out: list[dict[str, Any]] = []
    for code in sorted(rows["code"].astype(str).unique()):
        path = STOCK_PRICE_HISTORY_DIR / f"{code}.csv"
        if not path.exists():
            continue
        try:
            price = pd.read_csv(path, dtype={"date": str})
        except Exception:
            continue
        if price.empty:
            continue
        price["date"] = price["date"].map(normalize_date)
        price = price.sort_values("date").reset_index(drop=True)
        for col in ["open", "high", "low", "close", "volume"]:
            if col not in price.columns:
                price[col] = math.nan
            price[col] = pd.to_numeric(price[col], errors="coerce")

        close = price["close"]
        high = price["high"]
        low = price["low"]

        ema12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
        ema26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
        dif = ema12 - ema26
        dea = dif.ewm(span=9, adjust=False, min_periods=9).mean()
        price["macd_hist"] = dif - dea

        low9 = low.rolling(9, min_periods=9).min()
        high9 = high.rolling(9, min_periods=9).max()
        rsv9 = ((close - low9) / (high9 - low9) * 100).replace([np.inf, -np.inf], np.nan)
        price["k_value"] = rsv9.ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()
        price["d_value"] = price["k_value"].ewm(alpha=1 / 3, adjust=False, min_periods=1).mean()

        ma20 = close.rolling(20, min_periods=20).mean()
        std20 = close.rolling(20, min_periods=20).std()
        bb_width = ((ma20 + 2 * std20) - (ma20 - 2 * std20)) / ma20 * 100
        price["bb_width_20d"] = bb_width
        price["bb_width_percentile_120d"] = bb_width.rolling(120, min_periods=20).apply(
            lambda arr: (arr <= arr[-1]).mean() * 100 if not np.isnan(arr[-1]) else np.nan,
            raw=True,
        )

        for horizon in HORIZONS:
            price[f"d{horizon}_close_from_price"] = price["close"].shift(-horizon)
            price[f"next_open_to_d{horizon}_close_return"] = (
                price[f"d{horizon}_close_from_price"] / price["open"].shift(-1) - 1
            ) * 100
        price["next_open"] = price["open"].shift(-1)
        price["signal_close_to_next_open_gap"] = (price["next_open"] / price["close"] - 1) * 100

        keep_cols = [
            "date",
            "open",
            "close",
            "next_open",
            "signal_close_to_next_open_gap",
            "macd_hist",
            "k_value",
            "d_value",
            "bb_width_20d",
            "bb_width_percentile_120d",
        ] + [f"next_open_to_d{h}_close_return" for h in HORIZONS]
        for _, row in price[keep_cols].iterrows():
            date = safe_str(row.get("date"))
            if (code, date) not in required_pairs:
                continue
            record = {"code": code, "event_date": date}
            record.update({col: row.get(col) for col in keep_cols if col != "date"})
            out.append(record)
    return pd.DataFrame(out)


def benchmark_next_open_returns(rows: pd.DataFrame) -> pd.DataFrame:
    if rows.empty or not MARKET_INDEX_OHLC_PATH.exists():
        return pd.DataFrame()
    index_df = read_csv(MARKET_INDEX_OHLC_PATH, dtype=str)
    if index_df.empty:
        return pd.DataFrame()
    index_df["date"] = index_df["date"].map(normalize_date)
    for col in ["open", "close"]:
        index_df[col] = pd.to_numeric(index_df[col], errors="coerce")
    out: list[pd.DataFrame] = []
    wanted = rows[["benchmark_index", "event_date"]].drop_duplicates()
    for index_code, part in index_df.groupby("index_code"):
        dates = set(wanted.loc[wanted["benchmark_index"].astype(str).eq(str(index_code)), "event_date"].astype(str))
        if not dates:
            continue
        work = part.sort_values("date").reset_index(drop=True).copy()
        work["benchmark_index"] = index_code
        for horizon in HORIZONS:
            work[f"benchmark_next_open_to_d{horizon}_close_return"] = (
                work["close"].shift(-horizon) / work["open"].shift(-1) - 1
            ) * 100
        cols = ["benchmark_index", "date"] + [f"benchmark_next_open_to_d{h}_close_return" for h in HORIZONS]
        out.append(work.loc[work["date"].isin(dates), cols])
    if not out:
        return pd.DataFrame()
    result = pd.concat(out, ignore_index=True)
    result = result.rename(columns={"date": "event_date"})
    return result


def add_technical_context(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    phase = df["tdcc_price_phase"].astype(str)
    pre_mask_1 = (
        phase.eq("overheated_after_tdcc")
        & num_series(df, "price_ret_2w").between(20, 50, inclusive="both")
        & num_series(df, "tdcc_consecutive_up_weeks").eq(1)
    )
    pre_mask_2 = (
        phase.eq("overheated_after_tdcc")
        & num_series(df, "price_ret_1w").between(10, 30, inclusive="both")
        & num_series(df, "price_ret_2w").between(20, 50, inclusive="both")
    )
    pre_mask_3 = (
        df.get("is_all_thresholds", pd.Series(False, index=df.index)).map(as_bool)
        & df.get("overheat_bucket", pd.Series("", index=df.index)).astype(str).eq("overheated")
        & num_series(df, "price_ret_1w").between(10, 30, inclusive="both")
    )
    needed = df[pre_mask_1 | pre_mask_2 | pre_mask_3][["signal_id", "code", "event_date", "benchmark_index"]].copy()
    tech = price_technical_for_rows(needed)
    if not tech.empty:
        df = df.merge(tech, on=["code", "event_date"], how="left")
    bench = benchmark_next_open_returns(needed)
    if not bench.empty:
        df = df.merge(bench, on=["benchmark_index", "event_date"], how="left")
    for horizon in HORIZONS:
        stock_col = f"next_open_to_d{horizon}_close_return"
        bench_col = f"benchmark_next_open_to_d{horizon}_close_return"
        rel_col = f"next_open_relative_return_vs_benchmark_d{horizon}"
        if stock_col in df.columns and bench_col in df.columns:
            df[rel_col] = pd.to_numeric(df[stock_col], errors="coerce") - pd.to_numeric(df[bench_col], errors="coerce")
    return df


def rule_masks(df: pd.DataFrame) -> dict[str, pd.Series]:
    phase = df["tdcc_price_phase"].astype(str)
    k_value = num_series(df, "k_value")
    d_value = num_series(df, "d_value")
    return {
        "phase_overheated_bb_normal_2w20_50_tdcc1w": (
            phase.eq("overheated_after_tdcc")
            & num_series(df, "bb_width_percentile_120d").between(0, 80, inclusive="both")
            & num_series(df, "price_ret_2w").between(20, 50, inclusive="both")
            & num_series(df, "tdcc_consecutive_up_weeks").eq(1)
        ),
        "phase_overheated_kd_bull_not_hot_1w10_30_2w20_50": (
            phase.eq("overheated_after_tdcc")
            & (k_value > d_value)
            & (k_value < 90)
            & num_series(df, "price_ret_1w").between(10, 30, inclusive="both")
            & num_series(df, "price_ret_2w").between(20, 50, inclusive="both")
        ),
        "all_thresholds_overheated_1w10_30_macd_hist_pos": (
            df.get("is_all_thresholds", pd.Series(False, index=df.index)).map(as_bool)
            & df.get("overheat_bucket", pd.Series("", index=df.index)).astype(str).eq("overheated")
            & num_series(df, "price_ret_1w").between(10, 30, inclusive="both")
            & (num_series(df, "macd_hist") > 0)
        ),
    }


RULE_META: dict[str, dict[str, str]] = {
    "phase_overheated_bb_normal_2w20_50_tdcc1w": {
        "rule_name": "phase_overheated_after_tdcc + Bollinger width pct<=80 + 2w return 20~50 + TDCC 1w",
        "rule_name_zh": "TDCC 過熱 phase + 布林寬度未極端 + 2週漲20~50% + TDCC連續1週",
        "rule_definition": "tdcc_price_phase=overheated_after_tdcc; bb_width_percentile_120d<=80; price_ret_2w between 20 and 50; tdcc_consecutive_up_weeks=1",
    },
    "phase_overheated_kd_bull_not_hot_1w10_30_2w20_50": {
        "rule_name": "phase_overheated_after_tdcc + KD bullish K<90 + 1w return 10~30 + 2w return 20~50",
        "rule_name_zh": "TDCC 過熱 phase + KD多方但未過熱 + 1週漲10~30% + 2週漲20~50%",
        "rule_definition": "tdcc_price_phase=overheated_after_tdcc; K>D and K<90; price_ret_1w between 10 and 30; price_ret_2w between 20 and 50",
    },
    "all_thresholds_overheated_1w10_30_macd_hist_pos": {
        "rule_name": "all_thresholds_overheated + 1w return 10~30 + MACD hist > 0",
        "rule_name_zh": "四級距同步過熱 + 1週漲10~30% + MACD histogram > 0",
        "rule_definition": "is_all_thresholds=True; overheat_bucket=overheated; price_ret_1w between 10 and 30; MACD histogram > 0",
    },
}


def mature_mask(part: pd.DataFrame, horizon: int) -> pd.Series:
    mature_col = f"mature_d{horizon}"
    ret_col = f"d{horizon}_return_pct"
    if mature_col not in part.columns or ret_col not in part.columns:
        return pd.Series(False, index=part.index)
    return part[mature_col].astype(str).str.lower().isin(["true", "1", "yes"]) & pd.to_numeric(part[ret_col], errors="coerce").notna()


def sample_status(count: int) -> str:
    if count >= 30:
        return "ok_initial_sample"
    if count > 0:
        return "insufficient_sample"
    return "pending_only"


def stats_for_rule(df: pd.DataFrame, rule_id: str, mask: pd.Series, horizon: int) -> dict[str, Any]:
    part = df[mask].copy()
    mature = mature_mask(part, horizon)
    ret = pd.to_numeric(part.get(f"d{horizon}_return_pct", pd.Series(index=part.index)), errors="coerce")[mature].dropna()
    rel = pd.to_numeric(part.get(f"relative_return_vs_benchmark_d{horizon}", pd.Series(index=part.index)), errors="coerce")[mature].dropna()
    mfe = pd.to_numeric(part.get(f"max_return_{horizon}d", pd.Series(index=part.index)), errors="coerce")[mature].dropna()
    mae = pd.to_numeric(part.get(f"max_drawdown_{horizon}d", pd.Series(index=part.index)), errors="coerce")[mature].dropna()

    next_col = f"next_open_to_d{horizon}_close_return"
    next_rel_col = f"next_open_relative_return_vs_benchmark_d{horizon}"
    next_open_ret = pd.to_numeric(part.get(next_col, pd.Series(index=part.index)), errors="coerce")[mature].dropna()
    next_open_rel = pd.to_numeric(part.get(next_rel_col, pd.Series(index=part.index)), errors="coerce")[mature].dropna()
    gap = pd.to_numeric(part.get("signal_close_to_next_open_gap", pd.Series(index=part.index)), errors="coerce")[mature].dropna()

    meta = RULE_META[rule_id]
    return {
        "rule_id": rule_id,
        "rule_name": meta["rule_name"],
        "rule_name_zh": meta["rule_name_zh"],
        "rule_definition": meta["rule_definition"],
        "horizon": f"D+{horizon}",
        "signal_count": int(mask.sum()),
        "mature_count": int(len(ret)),
        "win_rate_close_to_close_pct": (ret > 0).mean() * 100 if not ret.empty else math.nan,
        "avg_return_close_to_close_pct": ret.mean(),
        "median_return_close_to_close_pct": ret.median(),
        "avg_relative_return_vs_benchmark_pct": rel.mean(),
        "median_relative_return_vs_benchmark_pct": rel.median(),
        "benchmark_outperform_rate_pct": (rel > 0).mean() * 100 if not rel.empty else math.nan,
        "avg_mfe_pct": mfe.mean(),
        "avg_mae_pct": mae.mean(),
        "next_open_mature_count": int(len(next_open_ret)),
        "win_rate_next_open_to_close_pct": (next_open_ret > 0).mean() * 100 if not next_open_ret.empty else math.nan,
        "avg_next_open_to_close_return_pct": next_open_ret.mean(),
        "median_next_open_to_close_return_pct": next_open_ret.median(),
        "avg_next_open_relative_return_vs_benchmark_pct": next_open_rel.mean(),
        "median_next_open_relative_return_vs_benchmark_pct": next_open_rel.median(),
        "signal_close_to_next_open_gap_avg_pct": gap.mean(),
        "signal_close_to_next_open_gap_median_pct": gap.median(),
        "sample_status": sample_status(len(ret)),
        "calculation_method": "close_to_close uses signal close to D+N close. next_open uses next trading day's open to D+N close. Relative next-open subtracts benchmark next-open-to-D+N close return when benchmark OHLC is available.",
        "tuning_status": "not_ready",
        "allowed_changes": "reporting_priority_only",
    }


def build_stats(df: pd.DataFrame) -> pd.DataFrame:
    masks = rule_masks(df)
    rows: list[dict[str, Any]] = []
    for rule_id, mask in masks.items():
        for horizon in HORIZONS:
            rows.append(stats_for_rule(df, rule_id, mask, horizon))
    return pd.DataFrame(rows)


def build_current_candidates(df: pd.DataFrame, stats: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()
    latest_date = max([d for d in df["signal_date"].map(normalize_date).tolist() if d] or [""])
    if not latest_date:
        return pd.DataFrame()
    masks = rule_masks(df)
    stat_lookup: dict[tuple[str, str], pd.Series] = {}
    for _, row in stats.iterrows():
        stat_lookup[(safe_str(row.get("rule_id")), safe_str(row.get("horizon")))] = row
    rows: list[dict[str, Any]] = []
    for rule_id, mask in masks.items():
        part = df[mask & df["signal_date"].map(normalize_date).eq(latest_date)].copy()
        if part.empty:
            continue
        for _, row in part.iterrows():
            d5 = stat_lookup.get((rule_id, "D+5"), pd.Series(dtype=object))
            d10 = stat_lookup.get((rule_id, "D+10"), pd.Series(dtype=object))
            rows.append(
                {
                    "signal_date": latest_date,
                    "stock_id": safe_str(row.get("code")),
                    "stock_name": safe_str(row.get("name")),
                    "theme": safe_str(row.get("primary_theme")),
                    "market_regime": safe_str(row.get("market_regime")),
                    "benchmark_index": safe_str(row.get("benchmark_index")),
                    "rule_id": rule_id,
                    "rule_name_zh": RULE_META[rule_id]["rule_name_zh"],
                    "tdcc_price_phase": safe_str(row.get("tdcc_price_phase")),
                    "overheat_bucket": safe_str(row.get("overheat_bucket")),
                    "tdcc_consecutive_up_weeks": safe_str(row.get("tdcc_consecutive_up_weeks")),
                    "price_ret_1w": to_number(row.get("price_ret_1w")),
                    "price_ret_2w": to_number(row.get("price_ret_2w")),
                    "bb_width_percentile_120d": to_number(row.get("bb_width_percentile_120d")),
                    "k_value": to_number(row.get("k_value")),
                    "d_value": to_number(row.get("d_value")),
                    "macd_hist": to_number(row.get("macd_hist")),
                    "d5_mature_count": safe_str(d5.get("mature_count", "")),
                    "d5_win_rate_pct": to_number(d5.get("win_rate_close_to_close_pct")),
                    "d5_avg_relative_return_pct": to_number(d5.get("avg_relative_return_vs_benchmark_pct")),
                    "d10_mature_count": safe_str(d10.get("mature_count", "")),
                    "d10_win_rate_pct": to_number(d10.get("win_rate_close_to_close_pct")),
                    "d10_avg_relative_return_pct": to_number(d10.get("avg_relative_return_vs_benchmark_pct")),
                    "sample_note": "short-term TDCC overheated edge; reporting-only until more market regimes mature",
                }
            )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out = out.sort_values(["d10_win_rate_pct", "d5_win_rate_pct", "price_ret_2w"], ascending=[False, False, False])
    return out


def fmt_num(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def format_for_md(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        if col.endswith("_pct") or col in {"avg_mfe_pct", "avg_mae_pct"}:
            out[col] = out[col].map(lambda x: fmt_num(x, 2))
    return out


def write_outputs(stats: pd.DataFrame, candidates: pd.DataFrame) -> None:
    write_csv(stats, LATEST_STATS_CSV)
    write_csv(candidates, LATEST_CANDIDATES_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(LATEST_STATS_CSV, DOCS_STATS_CSV)
    shutil.copyfile(LATEST_CANDIDATES_CSV, DOCS_CANDIDATES_CSV)

    stats_md = format_for_md(stats)
    d5 = stats_md[stats_md["horizon"].eq("D+5")]
    d10 = stats_md[stats_md["horizon"].eq("D+10")]
    cand_md = format_for_md(candidates)
    lines = [
        "# TDCC Overheated Short-Term Edge",
        "",
        f"- generated_at: `{now_text()}`",
        "- tuning_status: `not_ready`",
        "- allowed_changes: `reporting_priority_only`",
        "- forbidden_changes: `core_weight_change`",
        "",
        "## Calculation Method",
        "",
        "- close-to-close win rate: `dN_return_pct > 0`, from signal close to D+N close, only mature_dN=True rows.",
        "- close-to-close relative return: stock D+N return minus TWSE/TPEx benchmark D+N return.",
        "- next-open return: next trading day's open to D+N close.",
        "- next-open relative return: stock next-open return minus benchmark next-open return when benchmark OHLC is available.",
        "- pending rows are not counted as success or failure.",
        "- These rules are a short-term reporting specialty, not a core TDCC/ABM weight change.",
        "",
        "## Current Matching Stocks",
        "",
        markdown_table(
            cand_md,
            [
                "signal_date",
                "stock_id",
                "stock_name",
                "theme",
                "rule_name_zh",
                "price_ret_1w",
                "price_ret_2w",
                "d5_mature_count",
                "d5_win_rate_pct",
                "d5_avg_relative_return_pct",
                "d10_mature_count",
                "d10_win_rate_pct",
                "d10_avg_relative_return_pct",
                "sample_note",
            ],
            80,
        ),
        "",
        "## D+5 Table",
        "",
        markdown_table(
            d5,
            [
                "rule_name_zh",
                "mature_count",
                "win_rate_close_to_close_pct",
                "avg_return_close_to_close_pct",
                "median_return_close_to_close_pct",
                "avg_relative_return_vs_benchmark_pct",
                "next_open_mature_count",
                "win_rate_next_open_to_close_pct",
                "avg_next_open_to_close_return_pct",
                "avg_next_open_relative_return_vs_benchmark_pct",
                "sample_status",
            ],
            20,
        ),
        "",
        "## D+10 Table",
        "",
        markdown_table(
            d10,
            [
                "rule_name_zh",
                "mature_count",
                "win_rate_close_to_close_pct",
                "avg_return_close_to_close_pct",
                "median_return_close_to_close_pct",
                "avg_relative_return_vs_benchmark_pct",
                "next_open_mature_count",
                "win_rate_next_open_to_close_pct",
                "avg_next_open_to_close_return_pct",
                "avg_next_open_relative_return_vs_benchmark_pct",
                "sample_status",
            ],
            20,
        ),
    ]
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    shutil.copyfile(LATEST_MD, DOCS_MD)


def main() -> int:
    base = load_base()
    if base.empty:
        write_outputs(pd.DataFrame(), pd.DataFrame())
        return 0
    enriched = add_technical_context(base)
    stats = build_stats(enriched)
    candidates = build_current_candidates(enriched, stats)
    write_outputs(stats, candidates)
    print(f"Saved: {LATEST_STATS_CSV} rows={len(stats)}")
    print(f"Saved: {LATEST_CANDIDATES_CSV} rows={len(candidates)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
