from __future__ import annotations

from datetime import datetime
import math
from pathlib import Path
import sys
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_historical_pattern_operation_registry import (  # noqa: E402
    EVENT_FILTERS,
    MODEL_ID,
    PATTERN_SPECS,
    build_detail_events,
    out_of_sample_start_date,
    safe_float,
    safe_str,
    write_csv,
)


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "volume_breakout_buy_signal_grid"
SIGNAL_UNIVERSE_ID = "current_daily_production_volume_range_breakout_v1"

HISTORICAL_DETAIL_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
GRID_CSV = LATEST_DIR / "volume_breakout_buy_signal_grid_latest.csv"
GRID_MD = LATEST_DIR / "volume_breakout_buy_signal_grid_summary_latest.md"
BEST_CSV = LATEST_DIR / "volume_breakout_buy_signal_best_candidates_latest.csv"
REGISTRY_CSV = LATEST_DIR / "volume_breakout_buy_signal_evidence_registry_latest.csv"
PROPOSAL_MD = LATEST_DIR / "volume_breakout_buy_signal_proposal_latest.md"
DETAIL_HISTORY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_buy_signal_grid_events.csv"

MIN_CANDIDATE_SAMPLE = 30
MIN_CANDIDATE_WIN_RATE = 50.0
MIN_CANDIDATE_MEDIAN_RETURN = 0.0

GRID_COLUMNS = [
    "model_id",
    "research_id",
    "signal_universe_id",
    "feature_group_scope",
    "feature_group_id",
    "feature_group_name_zh",
    "pattern_id",
    "pattern_name_zh",
    "entry_rule_zh",
    "stop_loss_rule_zh",
    "hold_rule_zh",
    "exit_rule_zh",
    "sample_size",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
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


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def win_rate(returns: pd.Series) -> float:
    nums = numeric(returns).dropna()
    if nums.empty:
        return math.nan
    return round(float((nums > 0).mean() * 100.0), 2)


def avg_return(returns: pd.Series) -> float:
    nums = numeric(returns).dropna()
    if nums.empty:
        return math.nan
    return round(float(nums.mean()), 4)


def median_return(returns: pd.Series) -> float:
    nums = numeric(returns).dropna()
    if nums.empty:
        return math.nan
    return round(float(nums.median()), 4)


def profit_factor(returns: pd.Series) -> float:
    nums = numeric(returns).dropna()
    if nums.empty:
        return math.nan
    gains = nums[nums > 0].sum()
    losses = nums[nums < 0].sum()
    if losses == 0:
        return 999.0 if gains > 0 else math.nan
    return round(float(gains / abs(losses)), 4)


def confidence_status(sample_size: int, oos_size: int, win: float, med: float, pf: float) -> str:
    if sample_size >= 300 and oos_size >= 80 and win >= 52 and med > 0 and pf >= 1.2:
        return "high"
    if sample_size >= 100 and oos_size >= 30 and win >= 50 and med > 0 and pf >= 1.05:
        return "medium"
    return "low"


def out_of_sample_pass(part: pd.DataFrame) -> bool:
    oos = part[part["out_of_sample"].map(bool_value)]
    if len(part) < 100 or len(oos) < 30:
        return False
    all_avg = avg_return(part["return_pct"])
    oos_avg = avg_return(oos["return_pct"])
    oos_win = win_rate(oos["return_pct"])
    return not any(math.isnan(v) for v in [all_avg, oos_avg, oos_win]) and all_avg > 0 and oos_avg > 0 and oos_win >= 45


def feature_groups(row: pd.Series) -> list[tuple[str, str, str]]:
    groups = [("all_current_model_hits", "all", "全部現行放量攻擊")]
    event_filter_map = {item.event_filter_id: item.event_filter_zh for item in EVENT_FILTERS}
    groups.append(("event_filter", "current_model_hit_all", event_filter_map.get("current_model_hit_all", "current_model_hit_all")))

    low_position = safe_float(row.get("low_position_60_pct"))
    width40 = safe_float(row.get("range_width_40_pct"))
    if not math.isnan(low_position):
        if low_position <= 40:
            groups.append(("price_position", "low_position", "低位階"))
        elif low_position >= 80:
            groups.append(("price_position", "high_position", "高位階"))
        else:
            groups.append(("price_position", "middle_position", "中位階"))

    long_base_low = (
        not math.isnan(width40)
        and not math.isnan(low_position)
        and width40 <= 25
        and low_position <= 60
    )
    if long_base_low:
        groups.append(("event_filter", "long_base_low_position", event_filter_map.get("long_base_low_position", "long_base_low_position")))
    else:
        groups.append(
            (
                "event_filter",
                "simple_or_high_position_breakout",
                event_filter_map.get("simple_or_high_position_breakout", "simple_or_high_position_breakout"),
            )
        )

    if bool_value(row.get("limit_up_like")):
        groups.append(("attack_method", "locked_limit_up", "鎖量漲停"))
        groups.append(("event_filter", "limit_up_like_current_hit", event_filter_map.get("limit_up_like_current_hit", "limit_up_like_current_hit")))
    else:
        vol = safe_float(row.get("volume_ratio"))
        groups.append(("attack_method", "volume_attack", "放量攻擊" if not math.isnan(vol) and vol >= 2 else "一般突破"))

    vol = safe_float(row.get("volume_ratio"))
    if not math.isnan(vol):
        if vol < 2:
            bucket = ("volume_ratio", "lt_2", "量比低於2")
        elif vol < 3:
            bucket = ("volume_ratio", "2_to_3", "量比2到3")
        elif vol < 5:
            bucket = ("volume_ratio", "3_to_5", "量比3到5")
        else:
            bucket = ("volume_ratio", "ge_5", "量比5以上")
        groups.append(bucket)

    if not math.isnan(width40):
        if width40 <= 20:
            groups.append(("consolidation", "long_tight_base", "長盤整窄幅"))
        elif width40 <= 35:
            groups.append(("consolidation", "medium_base", "中等盤整"))
        else:
            groups.append(("consolidation", "wide_or_non_base", "寬幅或非盤整"))

    return groups


def expand_detail(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in detail.iterrows():
        for scope, group_id, group_name in feature_groups(row):
            item = row.to_dict()
            item.update(
                {
                    "feature_group_scope": scope,
                    "feature_group_id": group_id,
                    "feature_group_name_zh": group_name,
                }
            )
            rows.append(item)
    return pd.DataFrame(rows)


def load_detail_events() -> pd.DataFrame:
    if HISTORICAL_DETAIL_CSV.exists():
        detail = pd.read_csv(HISTORICAL_DETAIL_CSV, dtype=str, keep_default_na=False)
    else:
        detail = build_detail_events()
    if detail.empty:
        return detail
    out = detail[
        detail["model_hit_status"].astype(str).eq("current_model_hit")
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
    ].copy()
    if not out.empty:
        out["source_signal_universe_id"] = SIGNAL_UNIVERSE_ID
    return out


def research_score(sample_size: int, win: float, avg: float, med: float, max_dd: float, pf: float, oos_pass: bool) -> float:
    if any(math.isnan(v) for v in [win, avg, med, max_dd, pf]):
        return -999.0
    sample_bonus = min(sample_size, 300) / 30.0
    oos_bonus = 8.0 if oos_pass else 0.0
    return round((win - 50.0) * 0.35 + avg * 0.8 + med * 1.2 + min(pf, 3.0) * 2.0 + sample_bonus + max_dd * 0.08 + oos_bonus, 4)


def candidate_status(sample_size: int, win: float, med: float, avg: float, oos_pass: bool) -> str:
    if sample_size < MIN_CANDIDATE_SAMPLE:
        return "sample_too_small"
    if math.isnan(win) or math.isnan(med) or math.isnan(avg):
        return "metric_missing"
    if win < MIN_CANDIDATE_WIN_RATE or med <= MIN_CANDIDATE_MEDIAN_RETURN or avg <= 0:
        return "not_positive_expectancy"
    if not oos_pass:
        return "positive_but_oos_not_passed"
    return "promotion_candidate"


def summarize_grid(expanded: pd.DataFrame) -> pd.DataFrame:
    generated_at = now_text()
    if expanded.empty:
        return pd.DataFrame(columns=GRID_COLUMNS)
    pattern_map = {item.pattern_id: item for item in PATTERN_SPECS}
    data_start = min(expanded["event_date"])
    data_end = max(expanded["event_date"])
    split_date = out_of_sample_start_date(expanded)
    rows: list[dict[str, Any]] = []

    group_cols = ["feature_group_scope", "feature_group_id", "feature_group_name_zh", "pattern_id"]
    for keys, part in expanded.groupby(group_cols, dropna=False):
        scope, group_id, group_name, pattern_id = keys
        spec = pattern_map.get(safe_str(pattern_id))
        if spec is None:
            continue
        returns = numeric(part["return_pct"])
        mfe = numeric(part["mfe_pct"])
        mae = numeric(part["mae_pct"])
        holding = numeric(part["holding_days"])
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
        score = research_score(sample, win, avg, med, max_dd, pf, oos_ok)
        status = candidate_status(sample, win, med, avg, oos_ok)
        rows.append(
            {
                "model_id": MODEL_ID,
                "research_id": RESEARCH_ID,
                "signal_universe_id": SIGNAL_UNIVERSE_ID,
                "feature_group_scope": scope,
                "feature_group_id": group_id,
                "feature_group_name_zh": group_name,
                "pattern_id": spec.pattern_id,
                "pattern_name_zh": spec.pattern_name_zh,
                "entry_rule_zh": spec.entry_rule_zh,
                "stop_loss_rule_zh": spec.stop_loss_rule_zh,
                "hold_rule_zh": spec.hold_rule_zh,
                "exit_rule_zh": spec.exit_rule_zh,
                "sample_size": sample,
                "unique_stocks": part["stock_id"].astype(str).nunique(),
                "win_rate": win,
                "avg_return": avg,
                "median_return": med,
                "max_drawdown": max_dd,
                "avg_mfe": round(float(mfe.mean()), 4) if not mfe.dropna().empty else "",
                "avg_mae": round(float(mae.mean()), 4) if not mae.dropna().empty else "",
                "avg_holding_days": round(float(holding.mean()), 2) if not holding.dropna().empty else "",
                "profit_factor": pf,
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
                "risk_notes_zh": "research only; production promotion requires a separate approval PR.",
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


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    part = df.loc[:, [col for col in columns if col in df.columns]].head(limit).copy()
    try:
        return part.to_markdown(index=False)
    except Exception:
        return part.to_string(index=False)


def write_markdown(grid: pd.DataFrame, best: pd.DataFrame) -> None:
    lines = [
        "# Volume Breakout Buy Signal Grid",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_universe_id: `{SIGNAL_UNIVERSE_ID}`",
        "- scope: research/backtest only; no production parameter or PDF ranking is changed.",
        f"- grid_rows: `{len(grid)}`",
        f"- best_candidate_rows: `{len(best)}`",
        "",
        "## Top Grid Rows",
        "",
        markdown_table(
            grid,
            [
                "research_rank",
                "feature_group_scope",
                "feature_group_id",
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
            40,
        ),
    ]
    GRID_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    proposal_lines = [
        "# Volume Breakout Buy Signal Proposal",
        "",
        f"- generated_at: `{now_text()}`",
        "- decision: research proposal only. Rows with `approved_for_daily_candidate=True` still need a separate production approval PR.",
        "- interpretation: prefer rows with positive median return, adequate sample size, and out-of-sample pass. Avoid using high average return with negative median as ranking evidence.",
        "",
        "## Promotion Candidates",
        "",
        markdown_table(
            best,
            [
                "research_rank",
                "feature_group_scope",
                "feature_group_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "out_of_sample_pass",
                "confidence_status",
                "recommended_rank_weight",
                "research_score",
            ],
            50,
        ),
    ]
    PROPOSAL_MD.write_text("\n".join(proposal_lines) + "\n", encoding="utf-8", newline="\n")


def build() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    detail = load_detail_events()
    expanded = expand_detail(detail)
    grid = summarize_grid(expanded)
    best = grid[grid["candidate_status"].eq("promotion_candidate")].copy()
    if best.empty:
        best = grid[grid["candidate_status"].isin(["positive_but_oos_not_passed"])].head(50).copy()
    registry = grid.copy()
    return detail, grid, best, registry


def main() -> int:
    DETAIL_HISTORY_CSV.parent.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    detail, grid, best, registry = build()
    write_csv(detail, DETAIL_HISTORY_CSV)
    write_csv(grid, GRID_CSV)
    write_csv(best, BEST_CSV)
    write_csv(registry, REGISTRY_CSV)
    write_markdown(grid, best)

    for path in [GRID_CSV, GRID_MD, BEST_CSV, REGISTRY_CSV, PROPOSAL_MD]:
        target = DOCS_LATEST_DIR / path.name
        target.write_bytes(path.read_bytes())

    print(f"Saved: {DETAIL_HISTORY_CSV} rows={len(detail)}")
    print(f"Saved: {GRID_CSV} rows={len(grid)}")
    print(f"Saved: {BEST_CSV} rows={len(best)}")
    print(f"Saved: {REGISTRY_CSV} rows={len(registry)}")
    print(f"Saved: {GRID_MD}")
    print(f"Saved: {PROPOSAL_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
