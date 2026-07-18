from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_code, normalize_date, safe_str, to_number, write_csv  # noqa: E402
from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract, require_dataset_id  # noqa: E402


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_LATEST_DIR = LATEST_DIR / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

OPERATION_EVENTS_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
CLASSIFICATION_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification_events.csv"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_breakout_tdcc_confluence_backtest_latest.csv"
LATEST_SUMMARY_MD = RESEARCH_LATEST_DIR / "volume_breakout_tdcc_confluence_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_tdcc_confluence_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_tdcc_confluence_events.csv"

MODEL_ID = "volume_range_breakout"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "volume_breakout_tdcc_confluence"
MAX_TDCC_SIGNAL_AGE_DAYS = 7
RANK_BUCKETS = [10, 20, 50]

ZH = {
    "weekly_increase": "\u7576\u9031\u5927\u6236\u589e\u5e45\u6392\u540d",
    "consecutive_accumulation": "\u9023\u7e8c\u7d2f\u7a4d\u6392\u540d",
    "top_10": "\u524d10\u540d",
    "top_20": "\u524d20\u540d",
    "top_50": "\u524d50\u540d",
    "tdcc_rank_only": "\u50c5TDCC\u6392\u540d",
    "tdcc_classification": "TDCC+\u653e\u91cf\u653b\u64ca\u7d30\u5206",
    "tdcc_attack_method": "TDCC+\u653b\u64ca\u65b9\u5f0f",
    "tdcc_price_position": "TDCC+\u4f4d\u968e",
    "tdcc_follow_through": "TDCC+\u5f8c\u7e8c\u8d70\u6cd5",
    "tdcc_risk_type": "TDCC+\u98a8\u96aa\u578b\u614b",
    "tdcc_candle_quality": "TDCC+K\u68d2\u54c1\u8cea",
    "tdcc_consolidation": "TDCC+\u76e4\u6574\u578b\u614b",
    "tdcc_attack_follow": "TDCC+\u653b\u64ca\u65b9\u5f0f+\u5f8c\u7e8c\u8d70\u6cd5",
    "all_current_volume_breakout": "\u73fe\u884c\u653e\u91cf\u653b\u64ca\u5168\u90e8\u547d\u4e2d",
}

SUMMARY_COLUMNS = [
    "source_tdcc_dataset_id",
    "model_id",
    "overlay_model_id",
    "research_id",
    "tdcc_list_type",
    "tdcc_list_name_zh",
    "rank_bucket",
    "rank_bucket_name_zh",
    "confluence_scope",
    "confluence_scope_zh",
    "confluence_id",
    "confluence_name_zh",
    "pattern_id",
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
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "ranking_research_score",
    "ranking_research_rank",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
]

EVENT_COLUMNS = [
    "source_tdcc_dataset_id",
    "model_id",
    "overlay_model_id",
    "research_id",
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
    "classification_id",
    "classification_name_zh",
    "attack_method",
    "attack_method_name_zh",
    "price_position_type",
    "price_position_name_zh",
    "follow_through_type",
    "follow_through_name_zh",
    "risk_type",
    "risk_name_zh",
    "candle_quality",
    "candle_quality_name_zh",
    "consolidation_type",
    "consolidation_name_zh",
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
    "theme",
    "theme_mainstream_status",
    "approved_for_daily",
]

DIMENSION_SCOPES = [
    ("tdcc_rank_only", None, None),
    ("tdcc_classification", "classification_id", "classification_name_zh"),
    ("tdcc_attack_method", "attack_method", "attack_method_name_zh"),
    ("tdcc_price_position", "price_position_type", "price_position_name_zh"),
    ("tdcc_follow_through", "follow_through_type", "follow_through_name_zh"),
    ("tdcc_risk_type", "risk_type", "risk_name_zh"),
    ("tdcc_candle_quality", "candle_quality", "candle_quality_name_zh"),
    ("tdcc_consolidation", "consolidation_type", "consolidation_name_zh"),
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def pct_round(value: Any, digits: int = 4) -> float | str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return round(num, digits)


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def normalize_inputs(ops: pd.DataFrame, classification: pd.DataFrame, tdcc: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    ops = ops.copy()
    classification = classification.copy()
    tdcc = tdcc.copy()

    for df, date_col in [(ops, "event_date"), (classification, "event_date"), (tdcc, "signal_date")]:
        if date_col in df.columns:
            df[date_col] = df[date_col].map(normalize_date)
        if "stock_id" in df.columns:
            df["stock_id"] = df["stock_id"].map(normalize_code)

    ops = ops[
        ops.get("model_id", "").astype(str).eq(MODEL_ID)
        & ops.get("event_filter_id", "").astype(str).eq("current_model_hit_all")
        & ops.get("model_hit_status", "").astype(str).eq("current_model_hit")
    ].copy()
    ops = ops[(ops["event_date"] != "") & (ops["stock_id"] != "")]

    classification = classification[(classification["event_date"] != "") & (classification["stock_id"] != "")].copy()
    tdcc = tdcc[(tdcc["signal_date"] != "") & (tdcc["stock_id"] != "")].copy()
    tdcc = tdcc[tdcc.get("model_id", "").astype(str).eq(OVERLAY_MODEL_ID)].copy()
    return ops, classification, tdcc


def attach_classification(ops: pd.DataFrame, classification: pd.DataFrame) -> pd.DataFrame:
    keep_cols = [
        "event_date",
        "stock_id",
        "classification_id",
        "classification_name_zh",
        "attack_method",
        "attack_method_name_zh",
        "price_position_type",
        "price_position_name_zh",
        "follow_through_type",
        "follow_through_name_zh",
        "risk_type",
        "risk_name_zh",
        "candle_quality",
        "candle_quality_name_zh",
        "consolidation_type",
        "consolidation_name_zh",
    ]
    for col in keep_cols:
        if col not in classification.columns:
            classification[col] = ""
    dims = classification[keep_cols].drop_duplicates(["event_date", "stock_id"], keep="last")
    return ops.merge(dims, on=["event_date", "stock_id"], how="left")


def attach_tdcc_asof(ops: pd.DataFrame, tdcc: pd.DataFrame) -> pd.DataFrame:
    if ops.empty or tdcc.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    ops = ops.copy()
    tdcc = tdcc.copy()
    ops["event_dt"] = pd.to_datetime(ops["event_date"], format="%Y%m%d", errors="coerce")
    tdcc["signal_dt"] = pd.to_datetime(tdcc["signal_date"], format="%Y%m%d", errors="coerce")
    ops = ops.dropna(subset=["event_dt"])
    tdcc = tdcc.dropna(subset=["signal_dt"])

    rows: list[pd.DataFrame] = []
    tdcc_list_types = sorted(set(tdcc["tdcc_list_type"].astype(str)) - {""})
    for list_type in tdcc_list_types:
        part = tdcc[tdcc["tdcc_list_type"].astype(str).eq(list_type)].copy()
        if part.empty:
            continue
        part = part.sort_values(["signal_dt", "stock_id"])
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
        merged = merged[merged["signal_date"].map(safe_str) != ""].copy()
        if merged.empty:
            continue
        merged["tdcc_signal_date"] = merged["signal_date"]
        merged["tdcc_signal_age_days"] = (merged["event_dt"] - merged["signal_dt"]).dt.days
        merged["tdcc_list_type"] = list_type
        rows.append(merged)

    if not rows:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    out = pd.concat(rows, ignore_index=True, sort=False)
    out["overlay_model_id"] = OVERLAY_MODEL_ID
    out["research_id"] = RESEARCH_ID
    out["approved_for_daily"] = False
    for col in EVENT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    return out[EVENT_COLUMNS].sort_values(["event_date", "stock_id", "tdcc_list_type", "pattern_id"]).reset_index(drop=True)


def profit_factor(returns: pd.Series) -> float | str:
    ret = pd.to_numeric(returns, errors="coerce").dropna()
    if ret.empty:
        return ""
    gains = ret[ret > 0].sum()
    losses = ret[ret < 0].sum()
    if losses == 0:
        return "" if gains == 0 else round(999.0, 4)
    return round(float(gains / abs(losses)), 4)


def confidence(sample_size: int, out_of_sample_size: int) -> str:
    if sample_size >= 100 and out_of_sample_size >= 30:
        return "high"
    if sample_size >= 30 and out_of_sample_size >= 10:
        return "medium"
    return "low"


def out_of_sample_pass(part: pd.DataFrame) -> bool:
    oos = part[part["out_of_sample"].map(boolish)]
    if len(oos) < 10:
        return False
    returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
    if len(returns) < 10:
        return False
    return bool((returns > 0).mean() >= 0.5 and returns.mean() > 0 and returns.median() > 0)


def ranking_score(row: dict[str, Any]) -> float:
    win = to_number(row.get("win_rate"))
    avg = to_number(row.get("avg_return"))
    median = to_number(row.get("median_return"))
    sample = to_number(row.get("sample_size"))
    if any(math.isnan(x) for x in [win, avg, median, sample]):
        return -999.0
    if sample < 10:
        return -100.0 + round(sample, 4)
    score = median * 2.0 + avg + max(0.0, win - 50.0) * 0.3 + min(math.log10(max(sample, 1.0)), 2.0)
    if row.get("confidence_status") == "low":
        score *= 0.45
    elif row.get("confidence_status") == "medium":
        score *= 0.75
    if not row.get("out_of_sample_pass"):
        score -= 2.0
    return round(score, 4)


def metric_row(
    part: pd.DataFrame,
    tdcc_list_type: str,
    rank_bucket: int,
    confluence_scope: str,
    confluence_id: str,
    confluence_name_zh: str,
    pattern_id: str,
    generated_at: str,
    data_start: str,
    data_end: str,
) -> dict[str, Any]:
    returns = pd.to_numeric(part["return_pct"], errors="coerce").dropna()
    mfe = pd.to_numeric(part.get("mfe_pct"), errors="coerce")
    mae = pd.to_numeric(part.get("mae_pct"), errors="coerce")
    holding = pd.to_numeric(part.get("holding_days"), errors="coerce")
    tdcc_rank = pd.to_numeric(part.get("tdcc_rank"), errors="coerce")
    tdcc_score = pd.to_numeric(part.get("tdcc_ranking_score"), errors="coerce")
    tdcc_age = pd.to_numeric(part.get("tdcc_signal_age_days"), errors="coerce")
    oos = part[part["out_of_sample"].map(boolish)]
    oos_returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
    sample_size = int(len(returns))
    out_size = int(len(oos_returns))
    row: dict[str, Any] = {
        "source_tdcc_dataset_id": safe_str(part.get("source_tdcc_dataset_id", pd.Series(dtype=str)).iloc[0])
        if "source_tdcc_dataset_id" in part.columns and not part.empty
        else "",
        "model_id": MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "tdcc_list_type": tdcc_list_type,
        "tdcc_list_name_zh": ZH.get(tdcc_list_type, tdcc_list_type),
        "rank_bucket": f"top_{rank_bucket}",
        "rank_bucket_name_zh": ZH.get(f"top_{rank_bucket}", f"top_{rank_bucket}"),
        "confluence_scope": confluence_scope,
        "confluence_scope_zh": ZH.get(confluence_scope, confluence_scope),
        "confluence_id": confluence_id,
        "confluence_name_zh": confluence_name_zh,
        "pattern_id": pattern_id,
        "sample_size": sample_size,
        "unique_signal_events": int(part[["event_date", "stock_id"]].drop_duplicates().shape[0]),
        "unique_stocks": int(part["stock_id"].astype(str).nunique()),
        "win_rate": pct_round((returns > 0).mean() * 100 if sample_size else math.nan, 2),
        "avg_return": pct_round(returns.mean() if sample_size else math.nan),
        "median_return": pct_round(returns.median() if sample_size else math.nan),
        "max_drawdown": pct_round(mae.min()),
        "avg_mfe": pct_round(mfe.mean()),
        "avg_mae": pct_round(mae.mean()),
        "avg_holding_days": pct_round(holding.mean(), 2),
        "profit_factor": profit_factor(returns),
        "avg_tdcc_rank": pct_round(tdcc_rank.mean(), 2),
        "avg_tdcc_ranking_score": pct_round(tdcc_score.mean()),
        "avg_tdcc_signal_age_days": pct_round(tdcc_age.mean(), 2),
        "out_of_sample_size": out_size,
        "out_of_sample_win_rate": pct_round((oos_returns > 0).mean() * 100 if out_size else math.nan, 2),
        "out_of_sample_avg_return": pct_round(oos_returns.mean() if out_size else math.nan),
        "out_of_sample_median_return": pct_round(oos_returns.median() if out_size else math.nan),
        "approved_for_daily": False,
        "risk_notes_zh": "research only; TDCC uses as-of historical signal_date <= volume event_date; approved_for_daily remains False",
        "generated_at": generated_at,
        "data_start_date": data_start,
        "data_end_date": data_end,
    }
    row["confidence_status"] = confidence(sample_size, out_size)
    row["out_of_sample_pass"] = out_of_sample_pass(part)
    row["ranking_research_score"] = ranking_score(row)
    row["ranking_research_rank"] = ""
    return row


def scope_summary(events: pd.DataFrame, generated_at: str, data_start: str, data_end: str) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    rows: list[dict[str, Any]] = []
    events = events.copy()
    events["tdcc_rank_num"] = pd.to_numeric(events["tdcc_rank"], errors="coerce")
    for tdcc_list_type, list_part in events.groupby("tdcc_list_type", dropna=False):
        for bucket in RANK_BUCKETS:
            bucket_part = list_part[list_part["tdcc_rank_num"] <= bucket].copy()
            if bucket_part.empty:
                continue
            for pattern_id, part in bucket_part.groupby("pattern_id", dropna=False):
                rows.append(
                    metric_row(
                        part,
                        safe_str(tdcc_list_type),
                        bucket,
                        "tdcc_rank_only",
                        "all_current_volume_breakout",
                        ZH["all_current_volume_breakout"],
                        safe_str(pattern_id),
                        generated_at,
                        data_start,
                        data_end,
                    )
                )
            for scope, value_col, name_col in DIMENSION_SCOPES[1:]:
                if value_col is None or value_col not in bucket_part.columns:
                    continue
                for (dimension_id, pattern_id), part in bucket_part.groupby([value_col, "pattern_id"], dropna=False):
                    dimension_id = safe_str(dimension_id) or "unknown"
                    name = safe_str(part[name_col].iloc[0]) if name_col and name_col in part.columns else dimension_id
                    rows.append(
                        metric_row(
                            part,
                            safe_str(tdcc_list_type),
                            bucket,
                            scope,
                            dimension_id,
                            name,
                            safe_str(pattern_id),
                            generated_at,
                            data_start,
                            data_end,
                        )
                    )
            if {"attack_method", "follow_through_type"}.issubset(bucket_part.columns):
                combo = bucket_part.copy()
                combo["attack_follow_id"] = combo["attack_method"].map(safe_str) + "__" + combo["follow_through_type"].map(safe_str)
                combo["attack_follow_name_zh"] = combo.get("attack_method_name_zh", "").map(safe_str) + " + " + combo.get("follow_through_name_zh", "").map(safe_str)
                for (dimension_id, pattern_id), part in combo.groupby(["attack_follow_id", "pattern_id"], dropna=False):
                    rows.append(
                        metric_row(
                            part,
                            safe_str(tdcc_list_type),
                            bucket,
                            "tdcc_attack_follow",
                            safe_str(dimension_id),
                            safe_str(part["attack_follow_name_zh"].iloc[0]),
                            safe_str(pattern_id),
                            generated_at,
                            data_start,
                            data_end,
                        )
                    )
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    out = out[SUMMARY_COLUMNS].copy()
    out["_sample"] = pd.to_numeric(out["sample_size"], errors="coerce").fillna(0)
    out["_score"] = pd.to_numeric(out["ranking_research_score"], errors="coerce").fillna(-999)
    out = out.sort_values(
        ["tdcc_list_type", "rank_bucket", "_score", "_sample"],
        ascending=[True, True, False, False],
    ).reset_index(drop=True)
    out["ranking_research_rank"] = out.groupby(["tdcc_list_type", "rank_bucket"]).cumcount() + 1
    return out.drop(columns=["_sample", "_score"])[SUMMARY_COLUMNS]


def markdown_table(df: pd.DataFrame, cols: list[str], limit: int) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        vals = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:140] for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, events: pd.DataFrame) -> None:
    best = summary.copy()
    if not best.empty:
        best = best[
            pd.to_numeric(best["sample_size"], errors="coerce").fillna(0).ge(10)
            & best["confluence_scope"].isin(["tdcc_rank_only", "tdcc_attack_method", "tdcc_classification", "tdcc_follow_through", "tdcc_attack_follow"])
        ].copy()
        best["_rank"] = pd.to_numeric(best["ranking_research_rank"], errors="coerce").fillna(999999)
        best = best.sort_values(["tdcc_list_type", "rank_bucket", "_rank"]).drop(columns=["_rank"])
    counts = (
        events.groupby(["tdcc_list_type"], dropna=False)
        .agg(operation_rows=("stock_id", "size"), unique_signal_events=("event_date", lambda s: events.loc[s.index, ["event_date", "stock_id"]].drop_duplicates().shape[0]))
        .reset_index()
    ) if not events.empty else pd.DataFrame()
    lines = [
        "# Volume Breakout TDCC Confluence Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- source_tdcc_dataset_id: `{events['source_tdcc_dataset_id'].iloc[0] if not events.empty else ''}`",
        f"- model_id: `{MODEL_ID}`",
        f"- overlay_model_id: `{OVERLAY_MODEL_ID}`",
        f"- tdcc_as_of_rule: `tdcc_signal_date <= event_date and tdcc_signal_age_days <= {MAX_TDCC_SIGNAL_AGE_DAYS}`",
        f"- confluence_event_rows: `{len(events)}`",
        f"- summary_rows: `{len(summary)}`",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "",
        "## Matched Event Counts",
        "",
        *markdown_table(counts, ["tdcc_list_type", "operation_rows", "unique_signal_events"], 20),
        "",
        "## Best Confluence Rows",
        "",
        *markdown_table(
            best,
            [
                "tdcc_list_type",
                "rank_bucket",
                "confluence_scope",
                "confluence_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "confidence_status",
                "out_of_sample_pass",
                "ranking_research_score",
                "ranking_research_rank",
            ],
            80,
        ),
    ]
    LATEST_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    contract = load_research_tdcc_dataset_contract()
    ops = read_csv(OPERATION_EVENTS_CSV)
    classification = read_csv(CLASSIFICATION_EVENTS_CSV)
    tdcc = read_csv(TDCC_EVENTS_CSV)
    require_dataset_id(tdcc, contract, label=TDCC_EVENTS_CSV.as_posix())
    ops, classification, tdcc = normalize_inputs(ops, classification, tdcc)
    ops = attach_classification(ops, classification)
    events = attach_tdcc_asof(ops, tdcc)
    generated_at = now_text()
    data_start = safe_str(events["event_date"].min()) if not events.empty else ""
    data_end = safe_str(events["event_date"].max()) if not events.empty else ""
    summary = scope_summary(events, generated_at, data_start, data_end)
    events["source_tdcc_dataset_id"] = contract.dataset_id
    summary["source_tdcc_dataset_id"] = contract.dataset_id

    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_markdown(summary, events)

    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
