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
    main_price_date_from_freshness,
    markdown_table,
    now_text,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
NORMALIZED_LOG_CSV = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
PERFORMANCE_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_performance.csv"
ABM_HISTORY_CSV = TDCC_SIGNALS_DIR / "tdcc_pre_move_accumulation_history.csv"
ABM_LATEST_CSV = LATEST_DIR / "tdcc_pre_move_accumulation_latest.csv"
EFFECTIVENESS_MD = LATEST_DIR / "tdcc_signal_effectiveness_latest.md"

STRENGTH_MD = LATEST_DIR / "tdcc_strength_ranking_top_latest.md"
STRENGTH_CSV = LATEST_DIR / "tdcc_strength_ranking_top_latest.csv"
ABM_TOP_MD = LATEST_DIR / "tdcc_pre_move_abm_top_latest.md"
ABM_TOP_CSV = LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv"
PHASE_MD = LATEST_DIR / "tdcc_phase_distribution_latest.md"
PHASE_CSV = LATEST_DIR / "tdcc_phase_distribution_latest.csv"
PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"

README_PATHS = [
    LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
    Path("docs/latest/READ_ME_FIRST_DAILY_REPORT.txt"),
]

TOP_N = 50
PACKET_N = 30

REQUIRED_COLUMNS = [
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "abm_score",
    "abm_rank",
    "price_return_5d",
    "price_return_20d",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "relative_return_vs_benchmark",
]

STRENGTH_COLUMNS = [
    "rank",
    "stock_id",
    "stock_name",
    "theme",
    "tdcc_strength_score",
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "abm_score",
    "price_return_5d",
    "price_return_20d",
    "relative_return_vs_benchmark",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "risk_label",
    "interpretation",
]

ABM_COLUMNS = [
    "abm_rank",
    "stock_id",
    "stock_name",
    "theme",
    "abm_score",
    "tdcc_strength_score",
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "setup_type",
    "price_return_5d",
    "price_return_20d",
    "relative_return_vs_benchmark",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "theme_breadth_score",
    "accumulation_label",
    "interpretation",
]


def as_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def fmt_num(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def numeric_series(df: pd.DataFrame, column: str, default: float = math.nan) -> pd.Series:
    if column not in df.columns:
        return pd.Series(default, index=df.index, dtype="float64")
    return pd.to_numeric(df[column], errors="coerce")


def bool_series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(False, index=df.index)
    return df[column].map(as_bool)


def latest_date(df: pd.DataFrame) -> str:
    if df.empty or "signal_date" not in df.columns:
        return ""
    dates = [safe_str(v) for v in df["signal_date"].dropna().tolist()]
    return max(dates) if dates else ""


def signal_id_frame(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "code" not in out.columns and "stock_id" in out.columns:
        out["code"] = out["stock_id"]
    if "stock_id" not in out.columns and "code" in out.columns:
        out["stock_id"] = out["code"]
    if "signal_date" not in out.columns:
        out["signal_date"] = ""
    if "signal_id" not in out.columns:
        out["signal_id"] = (
            out["signal_date"].astype(str)
            + "_"
            + out.get("code", "").astype(str)
            + "_normalized"
        )
    return out


def combine_prefer_left(left: pd.Series, right: pd.Series) -> pd.Series:
    left_text = left.astype(str)
    empty = left.isna() | left_text.isin(["", "nan", "None", "<NA>"])
    return left.where(~empty, right)


def prepare_latest_frame() -> tuple[pd.DataFrame, dict[str, Any]]:
    snapshot = signal_id_frame(read_csv(SNAPSHOT_CSV, dtype=str))
    abm = signal_id_frame(read_csv(ABM_LATEST_CSV, dtype=str))
    sources = {
        "snapshot_rows": len(snapshot),
        "abm_latest_rows": len(abm),
        "ranking_quality": "complete",
        "missing_columns": [],
        "latest_signal_date": "",
    }

    if snapshot.empty and abm.empty:
        sources["ranking_quality"] = "no_data"
        return pd.DataFrame(), sources

    if snapshot.empty:
        base = abm.copy()
    else:
        signal_date = latest_date(snapshot)
        base = snapshot[snapshot["signal_date"].astype(str) == signal_date].copy()
        if not abm.empty:
            merge_cols = [
                "signal_id",
                "abm_score",
                "abm_rank",
                "setup_type",
                "priority_group",
                "tdcc_price_phase",
                "price_return_5d",
                "price_return_20d",
                "distance_ma20_pct",
                "volume_ratio_20d",
                "relative_ret_2w",
                "theme_breadth_score",
            ]
            keep = [c for c in merge_cols if c in abm.columns]
            if keep:
                base = base.merge(
                    abm[keep].drop_duplicates("signal_id", keep="last"),
                    on="signal_id",
                    how="left",
                    suffixes=("", "_abm"),
                )
                for col in merge_cols:
                    alt = f"{col}_abm"
                    if alt in base.columns:
                        current = base[col] if col in base.columns else pd.Series("", index=base.index)
                        base[col] = combine_prefer_left(current, base[alt])
                        base = base.drop(columns=[alt])

    if "stock_id" not in base.columns:
        base["stock_id"] = base.get("code", "")
    if "stock_name" not in base.columns:
        base["stock_name"] = base.get("name", "")
    if "theme" not in base.columns:
        base["theme"] = base.get("primary_theme", "")
    if "tdcc_price_phase" not in base.columns:
        base["tdcc_price_phase"] = ""
    if "setup_type" not in base.columns:
        base["setup_type"] = ""
    if "relative_return_vs_benchmark" not in base.columns:
        if "relative_ret_2w" in base.columns:
            base["relative_return_vs_benchmark"] = base["relative_ret_2w"]
        else:
            base["relative_return_vs_benchmark"] = ""
    if "all_thresholds_up" not in base.columns:
        base["all_thresholds_up"] = base.get("is_all_thresholds", "")
    if "high_thresholds_up" not in base.columns:
        high = bool_series(base, "has_800") | bool_series(base, "has_1000")
        base["high_thresholds_up"] = high.map(lambda v: "True" if v else "False")

    for col in REQUIRED_COLUMNS:
        if col not in base.columns:
            base[col] = ""
            sources["missing_columns"].append(col)

    sources["latest_signal_date"] = latest_date(base)
    if sources["missing_columns"]:
        sources["ranking_quality"] = "partial"

    base = base.drop_duplicates("signal_id", keep="last").reset_index(drop=True)
    add_strength_fields(base)
    return base, sources


def add_strength_fields(df: pd.DataFrame) -> None:
    all_up = bool_series(df, "all_thresholds_up")
    high_up = bool_series(df, "high_thresholds_up")
    weeks = numeric_series(df, "tdcc_consecutive_up_weeks", 0).fillna(0)
    breadth = numeric_series(df, "theme_breadth_score", 0).fillna(0)
    over_1000_up = bool_series(df, "has_1000")
    over_800_up = bool_series(df, "has_800")
    if "tdcc_1w_change_1000" in df.columns:
        over_1000_up = over_1000_up | (numeric_series(df, "tdcc_1w_change_1000", 0) > 0)
    if "tdcc_1w_change_800" in df.columns:
        over_800_up = over_800_up | (numeric_series(df, "tdcc_1w_change_800", 0) > 0)

    score = (
        all_up.astype(int) * 30
        + high_up.astype(int) * 20
        + weeks * 10
        + breadth * 10
        + over_1000_up.astype(int) * 10
        + over_800_up.astype(int) * 5
    )
    df["tdcc_strength_score"] = score.round(2)


def risk_label(phase: Any) -> str:
    phase_text = safe_str(phase)
    return {
        "tdcc_leading_price": "potential_accumulation",
        "tdcc_price_confirmed": "confirmed_move",
        "price_leading_tdcc": "late_or_chasing_risk",
        "overheated_after_tdcc": "overheated",
        "tdcc_price_divergence": "divergence_failed_watch",
        "failed_after_tdcc": "divergence_failed_watch",
        "insufficient_price_context": "insufficient_data",
        "insufficient_tdcc_history": "insufficient_data",
        "neutral_or_unclear": "neutral",
    }.get(phase_text, "neutral")


def phase_interpretation(phase: Any) -> str:
    phase_text = safe_str(phase)
    return {
        "tdcc_leading_price": "籌碼強，但股價尚未明顯反應。",
        "tdcc_price_confirmed": "籌碼強且股價已開始確認。",
        "price_leading_tdcc": "股價已先漲，TDCC 訊號可能偏晚。",
        "overheated_after_tdcc": "籌碼強但股價已過熱，防追高。",
        "tdcc_price_divergence": "TDCC 增加但股價轉弱，需防失效。",
        "failed_after_tdcc": "訊號後價格走弱，列為失效觀察。",
        "insufficient_price_context": "價格或 benchmark 資料不足，不列入強弱判斷。",
        "insufficient_tdcc_history": "TDCC 歷史不足，不列入強弱判斷。",
        "neutral_or_unclear": "訊號中性或尚不明確。",
    }.get(phase_text, "資料不足或訊號不明確。")


def accumulation_label(row: pd.Series) -> str:
    phase = safe_str(row.get("tdcc_price_phase"))
    setup = safe_str(row.get("setup_type"))
    abm = to_number(row.get("abm_score"), 0)
    if phase == "tdcc_leading_price" and setup == "quiet_accumulation" and abm >= 80:
        return "prime_pre_move"
    if phase == "tdcc_leading_price" and abm >= 60:
        return "watch_pre_move"
    if phase == "tdcc_price_confirmed":
        return "confirmed_not_pre_move"
    if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
        return "not_pre_move_overheated"
    if phase in {"tdcc_price_divergence", "failed_after_tdcc"}:
        return "divergence_risk"
    if phase in {"insufficient_price_context", "insufficient_tdcc_history"}:
        return "insufficient_data"
    return "watch_only"


def write_strength_top(df: pd.DataFrame, meta: dict[str, Any]) -> pd.DataFrame:
    if df.empty:
        write_csv(pd.DataFrame(columns=STRENGTH_COLUMNS), STRENGTH_CSV)
        STRENGTH_MD.write_text("# TDCC Strength Ranking Top\n\n目前沒有可用資料。\n", encoding="utf-8")
        return pd.DataFrame(columns=STRENGTH_COLUMNS)

    top = df.copy()
    top["risk_label"] = top["tdcc_price_phase"].map(risk_label)
    top["interpretation"] = top["tdcc_price_phase"].map(phase_interpretation)
    top = top.sort_values(["tdcc_strength_score", "tdcc_consecutive_up_weeks", "stock_id"], ascending=[False, False, True])
    top = top.head(TOP_N).copy()
    top["rank"] = range(1, len(top) + 1)
    for col in STRENGTH_COLUMNS:
        if col not in top.columns:
            top[col] = ""
    out = top[STRENGTH_COLUMNS].copy()
    for col in [
        "tdcc_strength_score",
        "abm_score",
        "price_return_5d",
        "price_return_20d",
        "relative_return_vs_benchmark",
        "distance_ma20_pct",
        "volume_ratio_20d",
        "theme_breadth_score",
    ]:
        out[col] = out[col].map(lambda v: fmt_num(v, 2))
    write_csv(out, STRENGTH_CSV)
    lines = [
        "# TDCC Strength Ranking Top",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_date: {meta.get('latest_signal_date', '')}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "說明：這是籌碼強弱榜，不等於潛伏吸籌榜。若 phase 是 price_leading_tdcc 或 overheated_after_tdcc，不可解讀成潛伏吸籌。",
        "",
        markdown_table(out, STRENGTH_COLUMNS),
        "",
    ]
    STRENGTH_MD.write_text("\n".join(lines), encoding="utf-8")
    return out


def write_abm_top(df: pd.DataFrame, meta: dict[str, Any]) -> tuple[pd.DataFrame, bool]:
    if df.empty:
        write_csv(pd.DataFrame(columns=ABM_COLUMNS), ABM_TOP_CSV)
        ABM_TOP_MD.write_text("# TDCC Pre-Move Accumulation / ABM Top\n\n目前沒有可用資料。\n", encoding="utf-8")
        return pd.DataFrame(columns=ABM_COLUMNS), False

    work = df.copy()
    work["accumulation_label"] = work.apply(accumulation_label, axis=1)
    work["interpretation"] = work["tdcc_price_phase"].map(phase_interpretation)

    strict = (
        work["tdcc_price_phase"].astype(str).eq("tdcc_leading_price")
        & (numeric_series(work, "abm_score", 0) >= 60)
        & (numeric_series(work, "tdcc_consecutive_up_weeks", 0) >= 2)
        & (numeric_series(work, "distance_ma20_pct", 999) <= 15)
        & (numeric_series(work, "volume_ratio_20d", 999) <= 1.8)
        & (numeric_series(work, "price_return_20d", 999) <= 25)
        & (numeric_series(work, "relative_return_vs_benchmark", 0) >= -5)
    )
    filtered = work[strict].copy()
    relaxed = False
    if len(filtered) < 10:
        relaxed = True
        relaxed_mask = (
            work["tdcc_price_phase"].astype(str).isin(["tdcc_leading_price", "tdcc_price_confirmed"])
            | work["setup_type"].astype(str).eq("quiet_accumulation")
            | (numeric_series(work, "abm_score", 0) >= 60)
        )
        filtered = work[
            relaxed_mask
            & (numeric_series(work, "price_return_20d", 999) <= 30)
            & (numeric_series(work, "distance_ma20_pct", 999) <= 20)
        ].copy()

    label_order = {
        "prime_pre_move": 0,
        "watch_pre_move": 1,
        "confirmed_not_pre_move": 2,
        "watch_only": 3,
        "divergence_risk": 4,
        "insufficient_data": 5,
        "not_pre_move_overheated": 6,
    }
    filtered["_label_order"] = filtered["accumulation_label"].map(label_order).fillna(9)
    filtered = filtered.sort_values(
        ["_label_order", "tdcc_price_phase", "setup_type", "abm_score", "tdcc_strength_score", "stock_id"],
        ascending=[True, True, True, False, False, True],
    ).head(TOP_N)
    filtered["abm_rank"] = range(1, len(filtered) + 1)
    for col in ABM_COLUMNS:
        if col not in filtered.columns:
            filtered[col] = ""
    out = filtered[ABM_COLUMNS].copy()
    for col in [
        "abm_score",
        "tdcc_strength_score",
        "price_return_5d",
        "price_return_20d",
        "relative_return_vs_benchmark",
        "distance_ma20_pct",
        "volume_ratio_20d",
        "theme_breadth_score",
    ]:
        out[col] = out[col].map(lambda v: fmt_num(v, 2))
    write_csv(out, ABM_TOP_CSV)
    lines = [
        "# TDCC Pre-Move Accumulation / ABM Top",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_date: {meta.get('latest_signal_date', '')}",
        f"- relaxed_filter: {relaxed}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "說明：這份名單才是用來找大戶持續增加但股價尚未明顯反應的潛伏吸籌候選。price_leading_tdcc / overheated_after_tdcc 不可寫成潛伏吸籌。",
        "",
        markdown_table(out, ABM_COLUMNS),
        "",
    ]
    ABM_TOP_MD.write_text("\n".join(lines), encoding="utf-8")
    return out, relaxed


def merge_snapshot_performance(snapshot: pd.DataFrame) -> pd.DataFrame:
    perf = signal_id_frame(read_csv(PERFORMANCE_CSV, dtype=str))
    if snapshot.empty:
        return pd.DataFrame()
    base = signal_id_frame(snapshot.copy())
    if perf.empty:
        return base
    keep_cols = [c for c in perf.columns if c == "signal_id" or c.startswith(("d", "mature_", "relative_", "max_", "min_")) or c in {"status"}]
    perf = perf[keep_cols].drop_duplicates("signal_id", keep="last")
    return base.merge(perf, on="signal_id", how="left", suffixes=("", "_perf"))


def maturity_mask(df: pd.DataFrame, horizon: int) -> pd.Series:
    col = f"mature_d{horizon}"
    ret_col = f"d{horizon}_return_pct"
    if col in df.columns:
        return df[col].map(as_bool)
    if ret_col in df.columns:
        return numeric_series(df, ret_col).notna()
    return pd.Series(False, index=df.index)


def avg_col(df: pd.DataFrame, col: str) -> str:
    if df.empty or col not in df.columns:
        return ""
    value = pd.to_numeric(df[col], errors="coerce").mean()
    if math.isnan(value):
        return ""
    return f"{value:.2f}"


def write_phase_distribution(latest_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    total = len(latest_df)

    if not latest_df.empty:
        phase_counts = latest_df["tdcc_price_phase"].fillna("").replace("", "unknown").value_counts().reset_index()
        phase_counts.columns = ["tdcc_price_phase", "sample_count"]
        for _, row in phase_counts.iterrows():
            count = int(row["sample_count"])
            rows.append(
                {
                    "section": "phase_distribution",
                    "tdcc_price_phase": row["tdcc_price_phase"],
                    "sample_count": count,
                    "pct_of_total": f"{(count / total * 100) if total else 0:.2f}",
                }
            )

        weeks_phase = (
            latest_df.groupby(["tdcc_consecutive_up_weeks", "tdcc_price_phase"], dropna=False)
            .size()
            .reset_index(name="signal_count")
        )
        for _, row in weeks_phase.iterrows():
            rows.append(
                {
                    "section": "consecutive_weeks_x_phase",
                    "tdcc_consecutive_up_weeks": safe_str(row.get("tdcc_consecutive_up_weeks")),
                    "tdcc_price_phase": safe_str(row.get("tdcc_price_phase")) or "unknown",
                    "signal_count": int(row["signal_count"]),
                }
            )

        conditions = {
            "all_thresholds_up": bool_series(latest_df, "all_thresholds_up"),
            "high_thresholds_up": bool_series(latest_df, "high_thresholds_up"),
            "over_800_or_above": bool_series(latest_df, "has_800") | bool_series(latest_df, "has_1000"),
            "over_1000_only": bool_series(latest_df, "has_1000") & ~bool_series(latest_df, "has_800"),
            "consecutive_2w": numeric_series(latest_df, "tdcc_consecutive_up_weeks", 0) >= 2,
            "consecutive_3w": numeric_series(latest_df, "tdcc_consecutive_up_weeks", 0) >= 3,
            "quiet_accumulation": latest_df["setup_type"].astype(str).eq("quiet_accumulation"),
            "early_breakout": latest_df["setup_type"].astype(str).eq("early_breakout"),
            "strong_momentum": latest_df["setup_type"].astype(str).eq("strong_momentum"),
            "overheated": latest_df["setup_type"].astype(str).eq("overheated")
            | latest_df["tdcc_price_phase"].astype(str).eq("overheated_after_tdcc"),
        }
        for name, mask in conditions.items():
            part = latest_df[mask]
            counts = part["tdcc_price_phase"].fillna("").replace("", "unknown").value_counts()
            if counts.empty:
                rows.append({"section": "condition_x_phase", "condition_name": name, "tdcc_price_phase": "none", "signal_count": 0})
            for phase, count in counts.items():
                rows.append(
                    {
                        "section": "condition_x_phase",
                        "condition_name": name,
                        "tdcc_price_phase": phase,
                        "signal_count": int(count),
                    }
                )

    all_snapshot = signal_id_frame(read_csv(SNAPSHOT_CSV, dtype=str))
    perf_base = merge_snapshot_performance(all_snapshot)
    if not perf_base.empty and "tdcc_price_phase" in perf_base.columns:
        for phase, group in perf_base.groupby("tdcc_price_phase", dropna=False):
            row: dict[str, Any] = {
                "section": "phase_performance",
                "tdcc_price_phase": safe_str(phase) or "unknown",
            }
            for horizon in [5, 10, 20]:
                mature = group[maturity_mask(group, horizon)].copy()
                row[f"mature_sample_d{horizon}"] = len(mature)
                row[f"avg_ret_d{horizon}"] = avg_col(mature, f"d{horizon}_return_pct")
                row[f"avg_relative_ret_d{horizon}"] = avg_col(mature, f"relative_return_vs_benchmark_d{horizon}")
            row["avg_mfe_d10"] = avg_col(group[maturity_mask(group, 10)], "max_return_10d")
            row["avg_mae_d10"] = avg_col(group[maturity_mask(group, 10)], "max_drawdown_10d")
            rows.append(row)

    out = pd.DataFrame(rows)
    write_csv(out, PHASE_CSV)

    phase_dist = out[out["section"] == "phase_distribution"]
    weeks_phase = out[out["section"] == "consecutive_weeks_x_phase"]
    condition_phase = out[out["section"] == "condition_x_phase"]
    performance = out[out["section"] == "phase_performance"]
    mature_cols = [
        "tdcc_price_phase",
        "mature_sample_d5",
        "avg_ret_d5",
        "avg_relative_ret_d5",
        "mature_sample_d10",
        "avg_ret_d10",
        "avg_relative_ret_d10",
        "mature_sample_d20",
        "avg_ret_d20",
        "avg_relative_ret_d20",
        "avg_mfe_d10",
        "avg_mae_d10",
    ]
    matured_total = 0
    for col in ["mature_sample_d5", "mature_sample_d10", "mature_sample_d20"]:
        if col in performance.columns:
            matured_total += pd.to_numeric(performance[col], errors="coerce").fillna(0).sum()
    pending_note = ""
    if matured_total == 0:
        pending_note = "D+5 / D+10 / D+20 尚未成熟，pending 不可視為正面或負面。"
    lines = [
        "# TDCC Phase Distribution",
        "",
        f"- generated_at: {now_text()}",
        f"- latest_signal_count: {total}",
        "",
        "## Phase 分布",
        "",
        markdown_table(phase_dist, ["tdcc_price_phase", "sample_count", "pct_of_total"]),
        "",
        "## 連續週數 x Phase",
        "",
        markdown_table(weeks_phase, ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"]),
        "",
        "## TDCC 條件 x Phase",
        "",
        markdown_table(condition_phase, ["condition_name", "tdcc_price_phase", "signal_count"]),
        "",
        "## Phase 後續績效",
        "",
        pending_note,
        "",
        markdown_table(performance, mature_cols),
        "",
    ]
    PHASE_MD.write_text("\n".join(lines), encoding="utf-8")
    return out


def count_mature(perf: pd.DataFrame, horizon: int) -> int:
    if perf.empty:
        return 0
    return int(maturity_mask(signal_id_frame(perf), horizon).sum())


def file_ok(path: Path) -> str:
    return "yes" if path.exists() and path.stat().st_size > 0 else "no"


def write_packet(
    meta: dict[str, Any],
    strength_top: pd.DataFrame,
    abm_top: pd.DataFrame,
    phase_table: pd.DataFrame,
) -> None:
    perf = read_csv(PERFORMANCE_CSV, dtype=str)
    pending_count = 0
    if not perf.empty:
        mature_any = pd.Series(False, index=perf.index)
        for horizon in [5, 10, 20]:
            mature_any = mature_any | maturity_mask(signal_id_frame(perf), horizon)
        pending_count = int((~mature_any).sum())
    insufficient_count = 0
    if not phase_table.empty and "tdcc_price_phase" in phase_table.columns:
        insufficient_count = int(
            phase_table[
                (phase_table.get("section", "") == "phase_distribution")
                & phase_table["tdcc_price_phase"].astype(str).isin(["insufficient_price_context", "insufficient_tdcc_history"])
            ]
            .get("sample_count", pd.Series(dtype=float))
            .astype(float)
            .sum()
        )

    phase_dist = phase_table[phase_table.get("section", "") == "phase_distribution"] if not phase_table.empty else pd.DataFrame()
    weeks_phase = phase_table[phase_table.get("section", "") == "consecutive_weeks_x_phase"] if not phase_table.empty else pd.DataFrame()
    performance = phase_table[phase_table.get("section", "") == "phase_performance"] if not phase_table.empty else pd.DataFrame()
    mature_cols = [
        "tdcc_price_phase",
        "mature_sample_d5",
        "avg_ret_d5",
        "avg_relative_ret_d5",
        "mature_sample_d10",
        "avg_ret_d10",
        "avg_relative_ret_d10",
        "mature_sample_d20",
        "avg_ret_d20",
        "avg_relative_ret_d20",
    ]

    lines = [
        "# TDCC CHATGPT TRACKING PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- main_price_date: {main_price_date_from_freshness()}",
        f"- latest_tdcc_signal_date: {meta.get('latest_signal_date', '')}",
        "- source_files: tdcc_signal_snapshot.csv, tdcc_normalized_signal_log.csv, tdcc_signal_performance.csv, tdcc_pre_move_accumulation_latest.csv, tdcc_signal_effectiveness_latest.md",
        f"- mature_d5_count: {count_mature(perf, 5)}",
        f"- mature_d10_count: {count_mature(perf, 10)}",
        f"- mature_d20_count: {count_mature(perf, 20)}",
        f"- pending_count: {pending_count}",
        f"- insufficient_sample_count: {insufficient_count}",
        f"- ranking_quality: {meta.get('ranking_quality', '')}",
        f"- missing_columns: {','.join(meta.get('missing_columns', [])) or 'none'}",
        "",
        "## Data Availability",
        f"- tdcc_signal_snapshot.csv: {file_ok(SNAPSHOT_CSV)}",
        f"- tdcc_normalized_signal_log.csv: {file_ok(NORMALIZED_LOG_CSV)}",
        f"- tdcc_signal_performance.csv: {file_ok(PERFORMANCE_CSV)}",
        f"- tdcc_pre_move_accumulation_history.csv: {file_ok(ABM_HISTORY_CSV)}",
        f"- tdcc_pre_move_accumulation_latest.csv: {file_ok(ABM_LATEST_CSV)}",
        f"- tdcc_signal_effectiveness_latest.md: {file_ok(EFFECTIVENESS_MD)}",
        "",
        "## TDCC Strength Ranking Top 30",
        "",
        markdown_table(strength_top.head(PACKET_N), STRENGTH_COLUMNS),
        "",
        "## Pre-Move Accumulation / ABM Top 30",
        "",
        markdown_table(abm_top.head(PACKET_N), ABM_COLUMNS),
        "",
        "## Phase Distribution",
        "",
        markdown_table(phase_dist, ["tdcc_price_phase", "sample_count", "pct_of_total"]),
        "",
        "## Consecutive Weeks x Phase",
        "",
        markdown_table(weeks_phase, ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"]),
        "",
        "## Mature Performance Summary",
        "",
        "只使用 mature_dN=True 的資料。若 mature sample = 0，目前不能下績效結論。",
        "",
        markdown_table(performance, mature_cols),
        "",
        "## Interpretation Rules",
        "- pending 不可視為正面或負面。",
        "- same stock_id + signal_date 只能算一筆 normalized signal。",
        "- TDCC Strength Ranking 找籌碼最強，不等於潛伏吸籌。",
        "- Pre-Move / ABM Ranking 才是找潛伏吸籌。",
        "- price_leading_tdcc / overheated_after_tdcc 不可寫成潛伏吸籌。",
        "- tdcc_price_divergence 要列為失效觀察。",
        "- 必須同時看絕對報酬與相對 TWSE / TPEx benchmark。",
        "",
    ]
    PACKET_MD.write_text("\n".join(lines), encoding="utf-8")


def upsert_readme_fields() -> None:
    fields = {
        "tdcc_strength_ranking_top_md_raw_url": raw_url(STRENGTH_MD),
        "tdcc_strength_ranking_top_csv_raw_url": raw_url(STRENGTH_CSV),
        "tdcc_pre_move_abm_top_md_raw_url": raw_url(ABM_TOP_MD),
        "tdcc_pre_move_abm_top_csv_raw_url": raw_url(ABM_TOP_CSV),
        "tdcc_phase_distribution_md_raw_url": raw_url(PHASE_MD),
        "tdcc_phase_distribution_csv_raw_url": raw_url(PHASE_CSV),
        "tdcc_chatgpt_tracking_packet_raw_url": raw_url(PACKET_MD),
    }
    for path in README_PATHS:
        existing_lines = []
        if path.exists():
            existing_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        seen = set(fields)
        new_lines = []
        inserted = False
        for line in existing_lines:
            key = line.split("=", 1)[0] if "=" in line else ""
            if key in fields:
                if key not in seen:
                    continue
                new_lines.append(f"{key}={fields[key]}")
                seen.discard(key)
            elif line == "RULES:" and not inserted:
                for missing_key, value in fields.items():
                    if missing_key in seen:
                        new_lines.append(f"{missing_key}={value}")
                seen.clear()
                inserted = True
                new_lines.append(line)
            else:
                new_lines.append(line)
        if not existing_lines:
            for key, value in fields.items():
                new_lines.append(f"{key}={value}")
        elif seen:
            for key, value in fields.items():
                if key in seen:
                    new_lines.append(f"{key}={value}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    latest_df, meta = prepare_latest_frame()
    strength_top = write_strength_top(latest_df, meta)
    abm_top, relaxed = write_abm_top(latest_df, meta)
    meta["relaxed_filter"] = relaxed
    phase_table = write_phase_distribution(latest_df)
    write_packet(meta, strength_top, abm_top, phase_table)
    upsert_readme_fields()
    print(f"Saved: {STRENGTH_MD}")
    print(f"Saved: {STRENGTH_CSV}")
    print(f"Saved: {ABM_TOP_MD}")
    print(f"Saved: {ABM_TOP_CSV}")
    print(f"Saved: {PHASE_MD}")
    print(f"Saved: {PHASE_CSV}")
    print(f"Saved: {PACKET_MD}")
    print(f"ranking_quality={meta.get('ranking_quality')}")
    print(f"missing_columns={','.join(meta.get('missing_columns', [])) or 'none'}")


if __name__ == "__main__":
    main()
