from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, TDCC_SIGNALS_DIR, append_update_csv, markdown_table, now_text, read_csv, safe_str, to_number, write_csv  # noqa: E402


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
]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


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
                base[col] = base[alt].combine_first(base[col] if col in base.columns else pd.Series("", index=base.index))
                base = base.drop(columns=[alt])
    return base


def load_performance() -> pd.DataFrame:
    perf = read_csv(PERFORMANCE_CSV, dtype=str)
    if perf.empty:
        return perf
    if "signal_id" not in perf.columns:
        perf["signal_id"] = perf["signal_date"].astype(str) + "_" + perf["code"].astype(str) + "_normalized"
    if "code" not in perf.columns and "stock_id" in perf.columns:
        perf["code"] = perf["stock_id"]
    return perf


def merge_base_perf(base: pd.DataFrame, perf: pd.DataFrame) -> pd.DataFrame:
    if base.empty:
        return base
    if perf.empty:
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
        return df.get("has_400", "").map(as_bool) & ~df.get("has_600", "").map(as_bool) & ~df.get("has_800", "").map(as_bool) & ~df.get("has_1000", "").map(as_bool)
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
        return (df.get("is_all_thresholds", "").map(as_bool) | df.get("is_consecutive_2w", "").map(as_bool)) & (pd.to_numeric(df.get("price_return_20d", ""), errors="coerce") <= 10)
    if factor == "tdcc_strong_and_overheated":
        return (df.get("is_all_thresholds", "").map(as_bool) | df.get("is_consecutive_2w", "").map(as_bool)) & setup.eq("overheated")
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


def factor_stats(df: pd.DataFrame) -> pd.DataFrame:
    for col in [
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
    ]:
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
        for h in HORIZONS:
            ret = pd.to_numeric(part[return_col(part, h)], errors="coerce") if not part.empty and return_col(part, h) in part.columns else pd.Series(dtype=float)
            dd_col = drawdown_col(part, h)
            dd = pd.to_numeric(part[dd_col], errors="coerce") if not part.empty and dd_col in part.columns else pd.Series(dtype=float)
            clean = ret.dropna()
            row[f"win_rate_d{h}"] = (clean > 0).mean() * 100 if not clean.empty else math.nan
            row[f"avg_return_d{h}"] = clean.mean()
            row[f"median_return_d{h}"] = clean.median()
            row[f"avg_drawdown_d{h}"] = dd.dropna().mean()
        rows.append(row)
    return pd.DataFrame(rows)


def main() -> int:
    base = load_factor_base()
    perf = load_performance()
    merged = merge_base_perf(base, perf)
    stats = factor_stats(merged)
    write_csv(stats, LATEST_CSV)
    append_update_csv(stats, MONTHLY_CSV, ["month", "factor_group"], ["month", "factor_group"])

    lines = [
        "# TDCC Signal Effectiveness Report",
        "",
        f"- generated_at: `{now_text()}`",
        f"- factor_rows: `{len(stats)}`",
        "",
        "## Factor Stats",
        "",
        markdown_table(stats, ["factor_group", "sample_size", "sample_status", "win_rate_d5", "avg_return_d5", "median_return_d5", "avg_drawdown_d5", "win_rate_d10", "avg_return_d10", "win_rate_d20", "avg_return_d20"], 80),
        "",
        "## Notes",
        "",
        "- sample_size 太小時標示 insufficient_sample，不硬下結論。",
        "- 最新未成熟批次不視為正面或負面訊號。",
        "- ABM factor groups 已納入，未來可比較 quiet_accumulation 與 overheated 的 D+10 / D+20 差異。",
    ]
    LATEST_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {LATEST_CSV}")
    print(f"Saved: {MONTHLY_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
