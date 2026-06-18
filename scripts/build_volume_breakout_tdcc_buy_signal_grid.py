from __future__ import annotations

from datetime import datetime
import math
from pathlib import Path
import sys
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_volume_breakout_buy_signal_grid import (  # noqa: E402
    MODEL_ID,
    PATTERN_SPECS,
    SIGNAL_UNIVERSE_ID,
    avg_return,
    bool_value,
    candidate_status,
    confidence_status,
    feature_groups,
    load_detail_events,
    markdown_table,
    median_return,
    numeric,
    out_of_sample_pass,
    profit_factor,
    research_score,
    safe_float,
    safe_str,
    win_rate,
    write_csv,
)
from build_historical_pattern_operation_registry import out_of_sample_start_date  # noqa: E402


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "volume_breakout_tdcc_buy_signal_grid"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

GRID_CSV = LATEST_DIR / "volume_breakout_tdcc_buy_signal_grid_latest.csv"
GRID_MD = LATEST_DIR / "volume_breakout_tdcc_buy_signal_grid_summary_latest.md"
BEST_CSV = LATEST_DIR / "volume_breakout_tdcc_buy_signal_best_candidates_latest.csv"
REGISTRY_CSV = LATEST_DIR / "volume_breakout_tdcc_buy_signal_evidence_registry_latest.csv"
PROPOSAL_MD = LATEST_DIR / "volume_breakout_tdcc_buy_signal_proposal_latest.md"
DETAIL_HISTORY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_tdcc_buy_signal_grid_events.csv"

MAX_TDCC_SIGNAL_AGE_DAYS = 7
TDCC_LIST_TYPES = ["weekly_increase", "consecutive_accumulation"]
TDCC_RANK_BUCKETS = [10, 20, 50]

ZH = {
    "no_tdcc": "未疊加TDCC",
    "weekly_increase": "當週大戶增幅排名",
    "consecutive_accumulation": "連續累積排名",
    "all": "全體",
    "top_10": "前10名",
    "top_20": "前20名",
    "top_50": "前50名",
    "tdcc_only": "TDCC分組",
    "tdcc_event_filter": "TDCC+突破型態",
    "tdcc_price_position": "TDCC+位階",
    "tdcc_attack_method": "TDCC+攻擊方式",
    "tdcc_volume_ratio": "TDCC+量比",
    "tdcc_consolidation": "TDCC+盤整",
    "tdcc_attack_position": "TDCC+攻擊方式+位階",
    "all_current_model_hits": "現行放量攻擊全部命中",
}

DIMENSION_SCOPE_MAP = {
    "event_filter": "tdcc_event_filter",
    "price_position": "tdcc_price_position",
    "attack_method": "tdcc_attack_method",
    "volume_ratio": "tdcc_volume_ratio",
    "consolidation": "tdcc_consolidation",
}

EVENT_COLUMNS = [
    "model_id",
    "overlay_model_id",
    "research_id",
    "signal_universe_id",
    "event_date",
    "tdcc_signal_date",
    "tdcc_signal_age_days",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_reason",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "out_of_sample",
    "volume_ratio",
    "signal_return_1d_pct",
    "range_width_40_pct",
    "low_position_60_pct",
    "limit_up_like",
    "source_signal_universe_id",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_ranking_score",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    "tdcc_effective_increase_count",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
    "tdcc_theme",
    "tdcc_theme_mainstream_status",
    "approved_for_daily",
]

GRID_COLUMNS = [
    "model_id",
    "overlay_model_id",
    "research_id",
    "signal_universe_id",
    "tdcc_asof_rule",
    "tdcc_list_type",
    "tdcc_list_name_zh",
    "rank_bucket",
    "rank_bucket_name_zh",
    "tdcc_feature_scope",
    "tdcc_feature_scope_zh",
    "tdcc_feature_id",
    "tdcc_feature_name_zh",
    "pattern_id",
    "pattern_name_zh",
    "entry_rule_zh",
    "stop_loss_rule_zh",
    "hold_rule_zh",
    "exit_rule_zh",
    "sample_size",
    "unique_signal_events",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
    "avg_tdcc_rank",
    "avg_tdcc_ranking_score",
    "avg_tdcc_signal_age_days",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "out_of_sample_median_return",
    "out_of_sample_pass",
    "confidence_status",
    "research_score",
    "research_rank",
    "recommended_rank_weight",
    "candidate_status",
    "approved_for_daily_candidate",
    "approved_for_daily",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
    "out_of_sample_start_date",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_date_text(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def read_tdcc_events() -> pd.DataFrame:
    if not TDCC_EVENTS_CSV.exists():
        return pd.DataFrame()
    tdcc = pd.read_csv(TDCC_EVENTS_CSV, dtype=str, keep_default_na=False)
    if tdcc.empty:
        return tdcc
    tdcc = tdcc.copy()
    tdcc["model_id"] = tdcc.get("model_id", "").map(safe_str)
    tdcc = tdcc[tdcc["model_id"].eq(OVERLAY_MODEL_ID)].copy()
    tdcc["signal_date"] = tdcc.get("signal_date", "").map(normalize_date_text)
    tdcc["stock_id"] = tdcc.get("stock_id", "").map(normalize_stock_id)
    tdcc["tdcc_list_type"] = tdcc.get("tdcc_list_type", "").map(safe_str)
    tdcc = tdcc[
        tdcc["signal_date"].ne("")
        & tdcc["stock_id"].ne("")
        & tdcc["tdcc_list_type"].isin(TDCC_LIST_TYPES)
    ].copy()
    tdcc["tdcc_rank_num"] = pd.to_numeric(tdcc.get("tdcc_rank", ""), errors="coerce")
    tdcc = tdcc[tdcc["tdcc_rank_num"].between(1, 50, inclusive="both")].copy()
    tdcc = tdcc.sort_values(["signal_date", "stock_id", "tdcc_list_type", "tdcc_rank_num"])
    return tdcc


def tdcc_rank_buckets_for_rank(rank: float) -> list[tuple[str, str]]:
    if math.isnan(rank):
        return []
    buckets: list[tuple[str, str]] = []
    for cutoff in TDCC_RANK_BUCKETS:
        if rank <= cutoff:
            key = f"top_{cutoff}"
            buckets.append((key, ZH[key]))
    return buckets


def rank_buckets_for_row(row: pd.Series | dict[str, Any]) -> list[tuple[str, str]]:
    list_type = safe_str(row.get("tdcc_list_type"))
    if list_type == "no_tdcc":
        return [("all", ZH["all"])]
    return tdcc_rank_buckets_for_rank(safe_float(row.get("tdcc_rank")))


def attach_tdcc_asof(detail: pd.DataFrame, tdcc: pd.DataFrame) -> pd.DataFrame:
    if detail.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    base = detail.copy()
    base["event_date"] = base["event_date"].map(normalize_date_text)
    base["stock_id"] = base["stock_id"].map(normalize_stock_id)
    base = base[(base["event_date"].ne("")) & (base["stock_id"].ne(""))].copy()
    for col in EVENT_COLUMNS:
        if col not in base.columns:
            base[col] = ""
    base["overlay_model_id"] = OVERLAY_MODEL_ID
    base["research_id"] = RESEARCH_ID
    base["signal_universe_id"] = SIGNAL_UNIVERSE_ID
    base["tdcc_signal_date"] = ""
    base["tdcc_signal_age_days"] = ""
    base["tdcc_list_type"] = "no_tdcc"
    base["approved_for_daily"] = "False"
    rows: list[pd.DataFrame] = [base[EVENT_COLUMNS].copy()]

    if tdcc.empty:
        return pd.concat(rows, ignore_index=True, sort=False)

    ops = detail.copy()
    ops["event_date"] = ops["event_date"].map(normalize_date_text)
    ops["stock_id"] = ops["stock_id"].map(normalize_stock_id)
    ops["event_dt"] = pd.to_datetime(ops["event_date"], format="%Y%m%d", errors="coerce")
    ops = ops[(ops["event_date"].ne("")) & (ops["stock_id"].ne(""))].dropna(subset=["event_dt"]).copy()

    tdcc = tdcc.copy()
    tdcc["signal_dt"] = pd.to_datetime(tdcc["signal_date"], format="%Y%m%d", errors="coerce")
    tdcc = tdcc.dropna(subset=["signal_dt"]).copy()

    for list_type in TDCC_LIST_TYPES:
        part = tdcc[tdcc["tdcc_list_type"].eq(list_type)].copy()
        if part.empty:
            continue
        merged = pd.merge_asof(
            ops.sort_values(["event_dt", "stock_id"]),
            part.sort_values(["signal_dt", "stock_id"]),
            by="stock_id",
            left_on="event_dt",
            right_on="signal_dt",
            direction="backward",
            tolerance=pd.Timedelta(days=MAX_TDCC_SIGNAL_AGE_DAYS),
            suffixes=("", "_tdcc"),
        )
        merged = merged[merged.get("signal_date", "").map(safe_str).ne("")].copy()
        if merged.empty:
            continue
        merged["overlay_model_id"] = OVERLAY_MODEL_ID
        merged["research_id"] = RESEARCH_ID
        merged["signal_universe_id"] = SIGNAL_UNIVERSE_ID
        merged["tdcc_signal_date"] = merged["signal_date"].map(normalize_date_text)
        merged["tdcc_signal_age_days"] = (merged["event_dt"] - merged["signal_dt"]).dt.days
        merged["tdcc_list_type"] = list_type
        merged["tdcc_theme"] = merged.get("theme_tdcc", merged.get("theme", ""))
        merged["tdcc_theme_mainstream_status"] = merged.get(
            "theme_mainstream_status_tdcc",
            merged.get("theme_mainstream_status", ""),
        )
        merged["approved_for_daily"] = "False"
        for col in EVENT_COLUMNS:
            if col not in merged.columns:
                merged[col] = ""
        rows.append(merged[EVENT_COLUMNS].copy())

    out = pd.concat(rows, ignore_index=True, sort=False)
    out = out.sort_values(["event_date", "stock_id", "pattern_id", "tdcc_list_type"]).reset_index(drop=True)
    return out[EVENT_COLUMNS]


def tdcc_feature_groups(row: pd.Series) -> list[dict[str, str]]:
    groups: list[dict[str, str]] = []
    list_type = safe_str(row.get("tdcc_list_type")) or "no_tdcc"
    list_name = ZH.get(list_type, list_type)
    for rank_bucket, rank_bucket_name in rank_buckets_for_row(row):
        prefix = f"{list_type}__{rank_bucket}"
        groups.append(
            {
                "tdcc_list_type": list_type,
                "tdcc_list_name_zh": list_name,
                "rank_bucket": rank_bucket,
                "rank_bucket_name_zh": rank_bucket_name,
                "tdcc_feature_scope": "tdcc_only",
                "tdcc_feature_scope_zh": ZH["tdcc_only"],
                "tdcc_feature_id": f"{prefix}__all",
                "tdcc_feature_name_zh": f"{list_name}/{rank_bucket_name}/{ZH['all_current_model_hits']}",
            }
        )

        dimensions: dict[str, tuple[str, str]] = {}
        for scope, group_id, group_name in feature_groups(row):
            if scope not in DIMENSION_SCOPE_MAP:
                continue
            tdcc_scope = DIMENSION_SCOPE_MAP[scope]
            feature_id = f"{prefix}__{scope}_{safe_str(group_id)}"
            feature_name = f"{list_name}/{rank_bucket_name}/{safe_str(group_name) or safe_str(group_id)}"
            groups.append(
                {
                    "tdcc_list_type": list_type,
                    "tdcc_list_name_zh": list_name,
                    "rank_bucket": rank_bucket,
                    "rank_bucket_name_zh": rank_bucket_name,
                    "tdcc_feature_scope": tdcc_scope,
                    "tdcc_feature_scope_zh": ZH[tdcc_scope],
                    "tdcc_feature_id": feature_id,
                    "tdcc_feature_name_zh": feature_name,
                }
            )
            dimensions[scope] = (safe_str(group_id), safe_str(group_name) or safe_str(group_id))

        if "attack_method" in dimensions and "price_position" in dimensions:
            attack_id, attack_name = dimensions["attack_method"]
            position_id, position_name = dimensions["price_position"]
            combo_id = f"{prefix}__attack_{attack_id}__position_{position_id}"
            combo_name = f"{list_name}/{rank_bucket_name}/{attack_name}+{position_name}"
            groups.append(
                {
                    "tdcc_list_type": list_type,
                    "tdcc_list_name_zh": list_name,
                    "rank_bucket": rank_bucket,
                    "rank_bucket_name_zh": rank_bucket_name,
                    "tdcc_feature_scope": "tdcc_attack_position",
                    "tdcc_feature_scope_zh": ZH["tdcc_attack_position"],
                    "tdcc_feature_id": combo_id,
                    "tdcc_feature_name_zh": combo_name,
                }
            )
    return groups


def expand_detail(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in events.iterrows():
        for group in tdcc_feature_groups(row):
            item = row.to_dict()
            item.update(group)
            rows.append(item)
    return pd.DataFrame(rows)


def summarize_grid(expanded: pd.DataFrame) -> pd.DataFrame:
    generated_at = now_text()
    if expanded.empty:
        return pd.DataFrame(columns=GRID_COLUMNS)
    pattern_map = {item.pattern_id: item for item in PATTERN_SPECS}
    data_start = min(expanded["event_date"])
    data_end = max(expanded["event_date"])
    split_date = out_of_sample_start_date(expanded)
    rows: list[dict[str, Any]] = []
    group_cols = [
        "tdcc_list_type",
        "tdcc_list_name_zh",
        "rank_bucket",
        "rank_bucket_name_zh",
        "tdcc_feature_scope",
        "tdcc_feature_scope_zh",
        "tdcc_feature_id",
        "tdcc_feature_name_zh",
        "pattern_id",
    ]
    for keys, part in expanded.groupby(group_cols, dropna=False):
        (
            list_type,
            list_name,
            rank_bucket,
            rank_bucket_name,
            feature_scope,
            feature_scope_zh,
            feature_id,
            feature_name,
            pattern_id,
        ) = keys
        spec = pattern_map.get(safe_str(pattern_id))
        if spec is None:
            continue
        returns = numeric(part["return_pct"])
        mfe = numeric(part["mfe_pct"])
        mae = numeric(part["mae_pct"])
        holding = numeric(part["holding_days"])
        tdcc_rank = numeric(part["tdcc_rank"])
        tdcc_score = numeric(part["tdcc_ranking_score"])
        tdcc_age = numeric(part["tdcc_signal_age_days"])
        oos = part[part["out_of_sample"].map(bool_value)]
        sample = int(len(part))
        oos_size = int(len(oos))
        win = win_rate(returns)
        avg = avg_return(returns)
        med = median_return(returns)
        max_dd = round(float(mae.min()), 4) if not mae.dropna().empty else math.nan
        pf = profit_factor(returns)
        oos_win = win_rate(oos["return_pct"]) if not oos.empty else math.nan
        oos_avg = avg_return(oos["return_pct"]) if not oos.empty else math.nan
        oos_med = median_return(oos["return_pct"]) if not oos.empty else math.nan
        oos_ok = out_of_sample_pass(part)
        raw_score = research_score(sample, win, avg, med, max_dd, pf, oos_ok)
        score = raw_score
        if sample < 30 and raw_score > -900:
            score = round(raw_score * 0.45 - (30 - sample) * 0.5, 4)
            score = min(score, round(12.0 + sample * 0.35, 4))
        if (not math.isnan(med) and med <= 0) or (not math.isnan(win) and win < 50):
            score = min(score, 0.0)
        status = candidate_status(sample, win, med, avg, oos_ok)
        rows.append(
            {
                "model_id": MODEL_ID,
                "overlay_model_id": OVERLAY_MODEL_ID,
                "research_id": RESEARCH_ID,
                "signal_universe_id": SIGNAL_UNIVERSE_ID,
                "tdcc_asof_rule": f"tdcc_signal_date <= event_date and tdcc_signal_age_days <= {MAX_TDCC_SIGNAL_AGE_DAYS}",
                "tdcc_list_type": list_type,
                "tdcc_list_name_zh": list_name,
                "rank_bucket": rank_bucket,
                "rank_bucket_name_zh": rank_bucket_name,
                "tdcc_feature_scope": feature_scope,
                "tdcc_feature_scope_zh": feature_scope_zh,
                "tdcc_feature_id": feature_id,
                "tdcc_feature_name_zh": feature_name,
                "pattern_id": spec.pattern_id,
                "pattern_name_zh": spec.pattern_name_zh,
                "entry_rule_zh": spec.entry_rule_zh,
                "stop_loss_rule_zh": spec.stop_loss_rule_zh,
                "hold_rule_zh": spec.hold_rule_zh,
                "exit_rule_zh": spec.exit_rule_zh,
                "sample_size": sample,
                "unique_signal_events": int(part[["event_date", "stock_id"]].drop_duplicates().shape[0]),
                "unique_stocks": part["stock_id"].astype(str).nunique(),
                "win_rate": win,
                "avg_return": avg,
                "median_return": med,
                "max_drawdown": max_dd,
                "avg_mfe": round(float(mfe.mean()), 4) if not mfe.dropna().empty else "",
                "avg_mae": round(float(mae.mean()), 4) if not mae.dropna().empty else "",
                "avg_holding_days": round(float(holding.mean()), 2) if not holding.dropna().empty else "",
                "profit_factor": pf,
                "avg_tdcc_rank": round(float(tdcc_rank.mean()), 2) if not tdcc_rank.dropna().empty else "",
                "avg_tdcc_ranking_score": round(float(tdcc_score.mean()), 4) if not tdcc_score.dropna().empty else "",
                "avg_tdcc_signal_age_days": round(float(tdcc_age.mean()), 2) if not tdcc_age.dropna().empty else "",
                "out_of_sample_size": oos_size,
                "out_of_sample_win_rate": oos_win,
                "out_of_sample_avg_return": oos_avg,
                "out_of_sample_median_return": oos_med,
                "out_of_sample_pass": oos_ok,
                "confidence_status": confidence_status(sample, oos_size, win, med, pf),
                "research_score": score,
                "research_rank": "",
                "recommended_rank_weight": max(0.0, round(score / 10.0, 4)) if score > 0 else 0.0,
                "candidate_status": status,
                "approved_for_daily_candidate": "True" if status == "promotion_candidate" else "False",
                "approved_for_daily": "False",
                "risk_notes_zh": "research only; TDCC uses historical as-of signal state and requires separate production approval.",
                "generated_at": generated_at,
                "data_start_date": data_start,
                "data_end_date": data_end,
                "out_of_sample_start_date": split_date,
            }
        )
    out = pd.DataFrame(rows, columns=GRID_COLUMNS)
    out["_score"] = pd.to_numeric(out["research_score"], errors="coerce").fillna(-999)
    out["_sample"] = pd.to_numeric(out["sample_size"], errors="coerce").fillna(0)
    out = out.sort_values(["_score", "_sample"], ascending=[False, False]).reset_index(drop=True)
    out["research_rank"] = range(1, len(out) + 1)
    return out.drop(columns=["_score", "_sample"])


def write_markdown(grid: pd.DataFrame, best: pd.DataFrame, events: pd.DataFrame) -> None:
    counts = (
        events.groupby("tdcc_list_type", dropna=False)
        .agg(
            operation_rows=("stock_id", "size"),
            unique_signal_events=("event_date", lambda s: events.loc[s.index, ["event_date", "stock_id"]].drop_duplicates().shape[0]),
        )
        .reset_index()
    ) if not events.empty else pd.DataFrame()

    lines = [
        "# Volume Breakout TDCC Buy Signal Grid",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_universe_id: `{SIGNAL_UNIVERSE_ID}`",
        f"- tdcc_asof_rule: `tdcc_signal_date <= event_date and tdcc_signal_age_days <= {MAX_TDCC_SIGNAL_AGE_DAYS}`",
        "- scope: research/backtest only; no production parameter, daily adapter, or PDF ranking is changed.",
        f"- event_rows: `{len(events)}`",
        f"- grid_rows: `{len(grid)}`",
        f"- best_candidate_rows: `{len(best)}`",
        "",
        "## Matched Event Counts",
        "",
        markdown_table(counts, ["tdcc_list_type", "operation_rows", "unique_signal_events"], 20),
        "",
        "## Top Grid Rows",
        "",
        markdown_table(
            grid,
            [
                "research_rank",
                "tdcc_list_type",
                "rank_bucket",
                "tdcc_feature_scope",
                "tdcc_feature_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "profit_factor",
                "out_of_sample_pass",
                "confidence_status",
                "candidate_status",
                "research_score",
            ],
            60,
        ),
    ]
    GRID_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    proposal_lines = [
        "# Volume Breakout TDCC Buy Signal Proposal",
        "",
        f"- generated_at: `{now_text()}`",
        "- decision: research proposal only. Rows with `approved_for_daily_candidate=True` still need a separate production approval PR.",
        "- interpretation: compare `no_tdcc/all` against TDCC top buckets. Prefer positive median return, adequate sample size, and out-of-sample pass.",
        "- data rule: TDCC grouping uses only the latest historical TDCC signal available on or before the volume breakout event date.",
        "",
        "## Promotion Candidates And TDCC Watch Rows",
        "",
        markdown_table(
            best,
            [
                "research_rank",
                "tdcc_list_type",
                "rank_bucket",
                "tdcc_feature_scope",
                "tdcc_feature_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "out_of_sample_pass",
                "confidence_status",
                "candidate_status",
                "recommended_rank_weight",
                "research_score",
            ],
            80,
        ),
    ]
    PROPOSAL_MD.write_text("\n".join(proposal_lines) + "\n", encoding="utf-8", newline="\n")


def build() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    detail = load_detail_events()
    tdcc = read_tdcc_events()
    events = attach_tdcc_asof(detail, tdcc)
    expanded = expand_detail(events)
    grid = summarize_grid(expanded)
    promotion = grid[grid["candidate_status"].eq("promotion_candidate")].copy()
    tdcc_watch = grid[
        grid["tdcc_list_type"].ne("no_tdcc")
        & pd.to_numeric(grid["sample_size"], errors="coerce").fillna(0).ge(30)
        & pd.to_numeric(grid["win_rate"], errors="coerce").fillna(0).ge(50)
        & pd.to_numeric(grid["avg_return"], errors="coerce").fillna(-999).gt(0)
        & pd.to_numeric(grid["median_return"], errors="coerce").fillna(-999).gt(0)
    ].copy()
    best = pd.concat([promotion, tdcc_watch.head(80)], ignore_index=True, sort=False)
    if best.empty:
        best = grid[grid["candidate_status"].isin(["positive_but_oos_not_passed"])].head(80).copy()
    key_cols = ["tdcc_list_type", "rank_bucket", "tdcc_feature_scope", "tdcc_feature_id", "pattern_id"]
    best = best.drop_duplicates(key_cols, keep="first").reset_index(drop=True)
    registry = grid.copy()
    return events, grid, best, registry


def main() -> int:
    DETAIL_HISTORY_CSV.parent.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    events, grid, best, registry = build()
    write_csv(events, DETAIL_HISTORY_CSV)
    write_csv(grid, GRID_CSV)
    write_csv(best, BEST_CSV)
    write_csv(registry, REGISTRY_CSV)
    write_markdown(grid, best, events)

    for path in [GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        target = DOCS_LATEST_DIR / path.name
        target.write_bytes(path.read_bytes())

    print(f"Saved: {DETAIL_HISTORY_CSV} rows={len(events)}")
    print(f"Saved: {GRID_CSV} rows={len(grid)}")
    print(f"Saved: {BEST_CSV} rows={len(best)}")
    print(f"Saved: {REGISTRY_CSV} rows={len(registry)}")
    print(f"Saved: {GRID_MD}")
    print(f"Saved: {PROPOSAL_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
