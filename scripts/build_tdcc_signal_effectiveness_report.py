from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    TDCC_SIGNALS_DIR,
    append_update_csv,
    markdown_table,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


NORMALIZED_LOG = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
ABM_HISTORY = TDCC_SIGNALS_DIR / "tdcc_pre_move_accumulation_history.csv"
PERFORMANCE_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_performance.csv"
LATEST_MD = LATEST_DIR / "tdcc_signal_effectiveness_latest.md"
LATEST_CSV = LATEST_DIR / "tdcc_signal_effectiveness_latest.csv"
MONTHLY_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_factor_stats_monthly.csv"
HORIZONS = [1, 2, 5, 10, 20]


FACTOR_GROUPS = [
    "all_thresholds",
    "consecutive_2w_all_thresholds",
    "consecutive_3w_all_thresholds",
    "over_1000_only",
    "over_800_or_above",
    "over_400_only",
    "all_thresholds_not_overheated",
    "all_thresholds_overheated",
    "theme_breadth_A",
    "theme_breadth_B",
    "theme_single_name_concentration",
    "price_confirmed",
    "price_not_confirmed",
    "pre_5d_return_lt_5",
    "pre_5d_return_5_15",
    "pre_5d_return_15_25",
    "pre_5d_return_gt_25",
    "abm_score_ge_80",
    "abm_score_70_80",
    "abm_score_60_70",
    "setup_quiet_accumulation",
    "setup_early_breakout",
    "setup_strong_momentum",
    "setup_overheated",
    "tdcc_strong_but_price_not_reacted",
    "tdcc_strong_and_overheated",
    "phase_tdcc_leading_price",
    "phase_tdcc_price_confirmed",
    "phase_price_leading_tdcc",
    "phase_tdcc_price_divergence",
    "phase_overheated_after_tdcc",
    "phase_failed_after_tdcc",
    "phase_insufficient_price_context",
    "consecutive_up_ge_2_tdcc_leading_price",
    "all_thresholds_up_tdcc_leading_price",
    "high_thresholds_up_tdcc_leading_price",
]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


def first_non_empty(series: pd.Series) -> Any:
    for value in series:
        if safe_str(value):
            return value
    return ""


def load_factor_base() -> pd.DataFrame:
    normalized = read_csv(NORMALIZED_LOG, dtype=str)
    abm = read_csv(ABM_HISTORY, dtype=str)
    if normalized.empty and abm.empty:
        return pd.DataFrame()
    if normalized.empty:
        base = abm.copy()
        base["signal_id"] = base["signal_date"].astype(str) + "_" + base["code"].astype(str) + "_normalized"
    else:
        base = normalized.copy()
    if not abm.empty:
        abm["signal_id"] = abm["signal_date"].astype(str) + "_" + abm["code"].astype(str) + "_normalized"
        keep = ["signal_id", "abm_score", "setup_type", "priority_group"]
        base = base.merge(abm[[c for c in keep if c in abm.columns]], on="signal_id", how="left", suffixes=("", "_abm"))
        for col in ["abm_score", "setup_type", "priority_group"]:
            alt = f"{col}_abm"
            if alt in base.columns:
                current = base[col] if col in base.columns else pd.Series("", index=base.index)
                base[col] = base[alt].combine_first(current)
                base = base.drop(columns=[alt])
    return base


def normalize_performance(perf: pd.DataFrame) -> pd.DataFrame:
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


def load_performance() -> pd.DataFrame:
    perf = read_csv(PERFORMANCE_CSV, dtype=str)
    return normalize_performance(perf)


def merge_base_perf(base: pd.DataFrame, perf: pd.DataFrame) -> pd.DataFrame:
    if base.empty or perf.empty:
        return base
    if "signal_id" in perf.columns:
        return base.merge(perf, on="signal_id", how="left", suffixes=("", "_perf"))
    return base.merge(perf, on=["signal_date", "code"], how="left", suffixes=("", "_perf"))


def factor_mask(df: pd.DataFrame, factor: str) -> pd.Series:
    idx = pd.Series(False, index=df.index)
    if df.empty:
        return idx
    if factor == "all_thresholds":
        return df.get("is_all_thresholds", "").map(as_bool)
    if factor == "consecutive_2w_all_thresholds":
        return df.get("is_consecutive_2w", "").map(as_bool)
    if factor == "consecutive_3w_all_thresholds":
        return df.get("is_consecutive_3w", "").map(as_bool)
    if factor == "over_1000_only":
        return df.get("has_1000", "").map(as_bool) & ~df.get("has_800", "").map(as_bool)
    if factor == "over_800_or_above":
        return df.get("has_800", "").map(as_bool) | df.get("has_1000", "").map(as_bool)
    if factor == "over_400_only":
        return (
            df.get("has_400", "").map(as_bool)
            & ~df.get("has_600", "").map(as_bool)
            & ~df.get("has_800", "").map(as_bool)
            & ~df.get("has_1000", "").map(as_bool)
        )
    if factor == "all_thresholds_not_overheated":
        return df.get("is_all_thresholds", "").map(as_bool) & (df.get("overheat_bucket", "").astype(str) != "overheated")
    if factor == "all_thresholds_overheated":
        return df.get("is_all_thresholds", "").map(as_bool) & (df.get("overheat_bucket", "").astype(str) == "overheated")
    if factor == "theme_breadth_A":
        return pd.to_numeric(df.get("theme_breadth_score", 0), errors="coerce") >= 5
    if factor == "theme_breadth_B":
        score = pd.to_numeric(df.get("theme_breadth_score", 0), errors="coerce")
        return (score >= 3) & (score < 5)
    if factor == "theme_single_name_concentration":
        return df.get("theme_sync_status", "").astype(str).eq("single_name_concentration")
    if factor == "price_confirmed":
        return df.get("price_confirm_bucket", "").astype(str).eq("confirmed")
    if factor == "price_not_confirmed":
        return ~df.get("price_confirm_bucket", "").astype(str).eq("confirmed")
    pre5 = pd.to_numeric(df.get("pre_5d_return", df.get("pre_signal_5d_return_pct", "")), errors="coerce")
    if factor == "pre_5d_return_lt_5":
        return pre5 < 5
    if factor == "pre_5d_return_5_15":
        return (pre5 >= 5) & (pre5 < 15)
    if factor == "pre_5d_return_15_25":
        return (pre5 >= 15) & (pre5 <= 25)
    if factor == "pre_5d_return_gt_25":
        return pre5 > 25
    abm = pd.to_numeric(df.get("abm_score", ""), errors="coerce")
    setup = df.get("setup_type", "").astype(str)
    if factor == "abm_score_ge_80":
        return abm >= 80
    if factor == "abm_score_70_80":
        return (abm >= 70) & (abm < 80)
    if factor == "abm_score_60_70":
        return (abm >= 60) & (abm < 70)
    if factor == "setup_quiet_accumulation":
        return setup.eq("quiet_accumulation")
    if factor == "setup_early_breakout":
        return setup.eq("early_breakout")
    if factor == "setup_strong_momentum":
        return setup.eq("strong_momentum")
    if factor == "setup_overheated":
        return setup.eq("overheated")
    if factor == "tdcc_strong_but_price_not_reacted":
        return (df.get("is_all_thresholds", "").map(as_bool) | df.get("is_consecutive_2w", "").map(as_bool)) & (
            pd.to_numeric(df.get("price_return_20d", ""), errors="coerce") <= 10
        )
    if factor == "tdcc_strong_and_overheated":
        return (df.get("is_all_thresholds", "").map(as_bool) | df.get("is_consecutive_2w", "").map(as_bool)) & setup.eq("overheated")
    phase = df.get("tdcc_price_phase", "").astype(str)
    if factor.startswith("phase_"):
        return phase.eq(factor.replace("phase_", "", 1))
    tdcc_weeks = pd.to_numeric(df.get("tdcc_consecutive_up_weeks", ""), errors="coerce")
    if factor == "consecutive_up_ge_2_tdcc_leading_price":
        return (tdcc_weeks >= 2) & phase.eq("tdcc_leading_price")
    if factor == "all_thresholds_up_tdcc_leading_price":
        return df.get("all_thresholds_up", "").map(as_bool) & phase.eq("tdcc_leading_price")
    if factor == "high_thresholds_up_tdcc_leading_price":
        return df.get("high_thresholds_up", "").map(as_bool) & phase.eq("tdcc_leading_price")
    return idx


def return_col(df: pd.DataFrame, horizon: int) -> str:
    for col in [f"d{horizon}_return_pct", f"return_d{horizon}"]:
        if col in df.columns:
            return col
    return f"d{horizon}_return_pct"


def drawdown_col(df: pd.DataFrame, horizon: int) -> str:
    for col in [f"max_drawdown_{horizon}d", f"max_drawdown_d{horizon}", f"mae_d{horizon}"]:
        if col in df.columns:
            return col
    return f"max_drawdown_{horizon}d"


def mature_mask(df: pd.DataFrame, horizon: int, fallback_col: str) -> pd.Series:
    if df.empty:
        return pd.Series(False, index=df.index)
    mature_col = f"mature_d{horizon}"
    if mature_col in df.columns:
        return df[mature_col].astype(str).str.lower().isin(["true", "1", "yes"])
    if fallback_col in df.columns:
        return pd.to_numeric(df[fallback_col], errors="coerce").notna()
    return pd.Series(False, index=df.index)


def factor_stats(df: pd.DataFrame) -> pd.DataFrame:
    required = [
        "is_all_thresholds",
        "is_consecutive_2w",
        "is_consecutive_3w",
        "has_400",
        "has_600",
        "has_800",
        "has_1000",
        "overheat_bucket",
        "theme_breadth_score",
        "theme_sync_status",
        "price_confirm_bucket",
        "pre_5d_return",
        "pre_signal_5d_return_pct",
        "abm_score",
        "setup_type",
        "price_return_20d",
        "tdcc_price_phase",
        "tdcc_consecutive_up_weeks",
        "all_thresholds_up",
        "high_thresholds_up",
        "theme_breadth_level",
        "market_regime",
    ]
    for col in required:
        if col not in df.columns:
            df[col] = ""
    month = safe_str(df["signal_date"].dropna().astype(str).max())[:6] if not df.empty and "signal_date" in df.columns else ""
    rows: list[dict[str, Any]] = []
    for factor in FACTOR_GROUPS:
        part = df[factor_mask(df, factor)].copy() if not df.empty else pd.DataFrame()
        row: dict[str, Any] = {
            "month": month,
            "factor_group": factor,
            "sample_size": len(part),
            "sample_status": "ok" if len(part) >= 5 else "insufficient_sample",
            "last_updated": now_text(),
        }
        for horizon in HORIZONS:
            ret_name = return_col(part, horizon)
            dd_name = drawdown_col(part, horizon)
            rel_name = f"relative_return_vs_benchmark_d{horizon}"
            mature = mature_mask(part, horizon, ret_name)
            ret = pd.to_numeric(part[ret_name], errors="coerce")[mature] if not part.empty and ret_name in part.columns else pd.Series(dtype=float)
            dd = pd.to_numeric(part[dd_name], errors="coerce")[mature] if not part.empty and dd_name in part.columns else pd.Series(dtype=float)
            rel = pd.to_numeric(part[rel_name], errors="coerce")[mature] if not part.empty and rel_name in part.columns else pd.Series(dtype=float)
            clean = ret.dropna()
            clean_rel = rel.dropna()
            row[f"mature_sample_d{horizon}"] = len(clean)
            row[f"win_rate_d{horizon}"] = (clean > 0).mean() * 100 if not clean.empty else math.nan
            row[f"avg_return_d{horizon}"] = clean.mean()
            row[f"median_return_d{horizon}"] = clean.median()
            row[f"avg_drawdown_d{horizon}"] = dd.dropna().mean()
            row[f"avg_relative_return_vs_benchmark_d{horizon}"] = clean_rel.mean()
            row[f"benchmark_outperform_rate_d{horizon}"] = (clean_rel > 0).mean() * 100 if not clean_rel.empty else math.nan
        rows.append(row)
    return pd.DataFrame(rows)


def group_phase_stats(df: pd.DataFrame, group_cols: list[str], horizon: int = 10) -> pd.DataFrame:
    if df.empty or any(col not in df.columns for col in group_cols):
        return pd.DataFrame()
    ret_name = return_col(df, horizon)
    rel_name = f"relative_return_vs_benchmark_d{horizon}"
    if ret_name not in df.columns:
        return pd.DataFrame()
    work = df.copy()
    work[ret_name] = pd.to_numeric(work[ret_name], errors="coerce")
    work[rel_name] = pd.to_numeric(work[rel_name], errors="coerce") if rel_name in work.columns else math.nan
    work = work[mature_mask(work, horizon, ret_name)].copy()
    if work.empty:
        return pd.DataFrame()
    out = (
        work.groupby(group_cols, dropna=False)
        .agg(
            signal_count=("signal_id", "nunique"),
            avg_return=(ret_name, "mean"),
            win_rate=(ret_name, lambda s: (pd.to_numeric(s, errors="coerce") > 0).mean() * 100),
            avg_relative_return_vs_benchmark=(rel_name, "mean"),
            benchmark_outperform_rate=(rel_name, lambda s: (pd.to_numeric(s, errors="coerce") > 0).mean() * 100),
        )
        .reset_index()
        .sort_values(["signal_count", "avg_relative_return_vs_benchmark"], ascending=[False, False])
    )
    out["horizon"] = f"D+{horizon}"
    return out


def phase_distribution(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty or "tdcc_price_phase" not in df.columns:
        return pd.DataFrame()
    work = df.copy()
    if "tdcc_consecutive_up_weeks" not in work.columns:
        work["tdcc_consecutive_up_weeks"] = ""
    return (
        work.groupby(["tdcc_consecutive_up_weeks", "tdcc_price_phase"], dropna=False)
        .agg(signal_count=("signal_id", "nunique"))
        .reset_index()
        .sort_values(["tdcc_consecutive_up_weeks", "signal_count"], ascending=[False, False])
    )


def main() -> int:
    base = load_factor_base()
    perf = load_performance()
    merged = merge_base_perf(base, perf)
    stats = factor_stats(merged)
    write_csv(stats, LATEST_CSV)
    append_update_csv(stats, MONTHLY_CSV, ["month", "factor_group"], ["month", "factor_group"])

    phase_perf = pd.concat([group_phase_stats(merged, ["tdcc_price_phase"], h) for h in [5, 10, 20]], ignore_index=True)

    lines = [
        "# TDCC Signal Effectiveness Report",
        "",
        f"- generated_at: `{now_text()}`",
        f"- factor_rows: `{len(stats)}`",
        "",
        "## Factor Stats",
        "",
        markdown_table(
            stats,
            [
                "factor_group",
                "sample_size",
                "sample_status",
                "mature_sample_d5",
                "win_rate_d5",
                "avg_return_d5",
                "avg_relative_return_vs_benchmark_d5",
                "benchmark_outperform_rate_d5",
                "mature_sample_d10",
                "win_rate_d10",
                "avg_return_d10",
                "avg_relative_return_vs_benchmark_d10",
                "mature_sample_d20",
                "win_rate_d20",
                "avg_return_d20",
                "avg_relative_return_vs_benchmark_d20",
            ],
            120,
        ),
        "",
        "## TDCC Consecutive Weeks x Price Phase Distribution",
        "",
        markdown_table(phase_distribution(merged), ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"], 120),
        "",
        "## TDCC-price Phase D+5 / D+10 / D+20 Performance",
        "",
        markdown_table(
            phase_perf,
            [
                "horizon",
                "tdcc_price_phase",
                "signal_count",
                "avg_return",
                "avg_relative_return_vs_benchmark",
                "win_rate",
                "benchmark_outperform_rate",
            ],
            120,
        ),
        "",
        "## TDCC Conditions x Phase Performance",
        "",
        markdown_table(
            group_phase_stats(merged, ["all_thresholds_up", "high_thresholds_up", "tdcc_price_phase"], 10),
            ["all_thresholds_up", "high_thresholds_up", "tdcc_price_phase", "signal_count", "avg_return", "avg_relative_return_vs_benchmark", "win_rate", "benchmark_outperform_rate"],
            120,
        ),
        "",
        "## Setup Type x Phase",
        "",
        markdown_table(
            group_phase_stats(merged, ["setup_type", "tdcc_price_phase"], 10),
            ["setup_type", "tdcc_price_phase", "signal_count", "avg_return", "avg_relative_return_vs_benchmark", "win_rate", "benchmark_outperform_rate"],
            120,
        ),
        "",
        "## Theme Breadth Level x Phase",
        "",
        markdown_table(
            group_phase_stats(merged, ["theme_breadth_level", "tdcc_price_phase"], 10),
            ["theme_breadth_level", "tdcc_price_phase", "signal_count", "avg_return", "avg_relative_return_vs_benchmark", "win_rate", "benchmark_outperform_rate"],
            120,
        ),
        "",
        "## Market Regime x Phase",
        "",
        markdown_table(
            group_phase_stats(merged, ["market_regime", "tdcc_price_phase"], 10),
            ["market_regime", "tdcc_price_phase", "signal_count", "avg_return", "avg_relative_return_vs_benchmark", "win_rate", "benchmark_outperform_rate"],
            120,
        ),
        "",
        "## Notes",
        "",
        "- TDCC-price phase is frozen at signal_date. D+N stats use only mature_dN=True rows; pending rows are not positive or negative.",
        "- Return stats include absolute returns and relative returns versus TWSE/TPEx benchmark when available.",
        "- sample_size is the signal count; mature_sample_dN is the count actually used for D+N performance statistics.",
        "- Newly phase-tagged signals will show blank D+10/D+20 performance until enough future trading days mature.",
        "- quiet_accumulation should mainly map to tdcc_leading_price; overheated / strong_momentum should be checked against price_leading_tdcc or overheated_after_tdcc.",
        "- ABM factor groups are included so quiet_accumulation and overheated setups can be compared by D+10/D+20 later.",
    ]
    LATEST_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {LATEST_CSV}")
    print(f"Saved: {MONTHLY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
