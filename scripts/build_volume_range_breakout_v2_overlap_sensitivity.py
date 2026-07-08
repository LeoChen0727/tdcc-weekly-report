from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_deep_low_base_matrix_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_overlap_sensitivity_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_overlap_sensitivity_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_overlap_sensitivity_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_overlap_sensitivity.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_overlap_sensitivity_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_overlap_sensitivity"
ARTIFACT_VERSION = "volume_range_breakout_v2_overlap_sensitivity_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_deep_low_base_matrix"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "condition_set_id",
    "condition_set_label",
    "selection_basis",
    "selection_basis_label",
    "baseline_event_count",
    "sample_size",
    "unique_stocks",
    "stocks_with_multiple_events",
    "suppressed_same_stock_overlap_count",
    "overlap_pair_count",
    "coverage_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "min_return_pct",
    "max_return_pct",
    "sample_status",
    "interpretation",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "event_sequence_for_stock",
    "all_events_overlap_pair_count_for_stock",
    "first_event_per_stock_included",
    "same_stock_non_overlap_included",
    "same_stock_non_overlap_suppression_reason",
    "suppressed_by_source_event_key",
    "suppressed_by_entry_date",
    "suppressed_by_exit_date",
    "deep_low_120_le40",
    "deep_low_240_le40",
    "range60_le25",
    "range120_le25",
    "limit_up_like",
    "consolidation_type",
    "risk_type",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


@dataclass(frozen=True)
class ConditionSet:
    condition_set_id: str
    condition_set_label: str
    note: str


CONDITION_SETS = [
    ConditionSet("baseline_all", "All v2 raw-market events", "Current event-level v2 population."),
    ConditionSet("off120_le40", "Off 120d low <= 40%", "Deep-low proxy requested by semantic audit."),
    ConditionSet("off240_le40", "Off 240d low <= 40%", "Longer deep-low proxy requested by semantic audit."),
    ConditionSet("range60_le25", "60d range width <= 25%", "Narrow 60d consolidation proxy."),
    ConditionSet("range120_le25", "120d range width <= 25%", "Narrow 120d consolidation proxy."),
    ConditionSet(
        "off120_le40_range60_le25",
        "Off 120d low <= 40% and 60d range <= 25%",
        "Deep-low plus narrow-range proxy.",
    ),
    ConditionSet(
        "off240_le40_range60_le25",
        "Off 240d low <= 40% and 60d range <= 25%",
        "Long-window deep-low plus narrow-range proxy.",
    ),
    ConditionSet("limit_up_like", "Limit-up-like signal candle", "Lock-limit behavior diagnostic."),
    ConditionSet("not_limit_up_like", "Not limit-up-like signal candle", "Non-lock-limit diagnostic."),
]

SELECTION_BASIS_LABELS = {
    "event_level_all_events": "Event-level rows; repeated same-stock active windows are not suppressed.",
    "first_event_per_stock": "First event per stock only; sensitivity check, not an operation rule.",
    "same_stock_non_overlap": "Accept one active trade per stock; later rows inside an accepted holding window are suppressed.",
}


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def false_text() -> str:
    return "False"


def pct_round(value: float, digits: int = 4) -> float | str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return round(float(value), digits)


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    return pd.to_datetime(text, format="%Y%m%d", errors="coerce")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def prepare_source() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        raise SystemExit("ERROR: source detail is empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit(f"ERROR: source detail must come from {SOURCE_RESEARCH_ID}")
    if detail.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        raise SystemExit("ERROR: source detail must be unique by source_event_key")
    if not set(detail.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain research-only")
    missing = sorted({"stock_id", "entry_date", "exit_date", "return_pct", "return_outcome"} - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: source detail missing required columns: {missing}")

    source = detail.copy()
    source["_entry_dt"] = parse_yyyymmdd(source["entry_date"])
    source["_exit_dt"] = parse_yyyymmdd(source["exit_date"])
    if source["_entry_dt"].isna().any() or source["_exit_dt"].isna().any():
        raise SystemExit("ERROR: source detail has unparseable entry_date or exit_date")
    source["_return"] = pd.to_numeric(source["return_pct"], errors="coerce")
    if source["_return"].isna().any():
        raise SystemExit("ERROR: source detail has unparseable return_pct")
    source["_source_order"] = range(len(source))
    return source


def condition_mask(source: pd.DataFrame, condition_set_id: str) -> pd.Series:
    true = pd.Series(True, index=source.index)
    if condition_set_id == "baseline_all":
        return true
    if condition_set_id == "off120_le40":
        return source.get("deep_low_120_le40", pd.Series(False, index=source.index)).map(boolish)
    if condition_set_id == "off240_le40":
        return source.get("deep_low_240_le40", pd.Series(False, index=source.index)).map(boolish)
    if condition_set_id == "range60_le25":
        return source.get("range60_le25", pd.Series(False, index=source.index)).map(boolish)
    if condition_set_id == "range120_le25":
        return source.get("range120_le25", pd.Series(False, index=source.index)).map(boolish)
    if condition_set_id == "off120_le40_range60_le25":
        return source.get("deep_low_120_le40", pd.Series(False, index=source.index)).map(boolish) & source.get(
            "range60_le25", pd.Series(False, index=source.index)
        ).map(boolish)
    if condition_set_id == "off240_le40_range60_le25":
        return source.get("deep_low_240_le40", pd.Series(False, index=source.index)).map(boolish) & source.get(
            "range60_le25", pd.Series(False, index=source.index)
        ).map(boolish)
    if condition_set_id == "limit_up_like":
        return source.get("limit_up_like", pd.Series(False, index=source.index)).map(boolish)
    if condition_set_id == "not_limit_up_like":
        return ~source.get("limit_up_like", pd.Series(False, index=source.index)).map(boolish)
    raise KeyError(condition_set_id)


def sorted_events(events: pd.DataFrame) -> pd.DataFrame:
    return events.sort_values(["stock_id", "_entry_dt", "_exit_dt", "signal_date", "source_event_key", "_source_order"]).copy()


def overlap_pair_count(events: pd.DataFrame) -> int:
    if events.empty:
        return 0
    count = 0
    for _, part in sorted_events(events).groupby("stock_id", dropna=False):
        active: list[pd.Series] = []
        for _, row in part.iterrows():
            entry_dt = row["_entry_dt"]
            for prior in active:
                if entry_dt <= prior["_exit_dt"]:
                    count += 1
            active = [prior for prior in active if prior["_exit_dt"] >= entry_dt]
            active.append(row)
    return count


def first_event_per_stock(events: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    if events.empty:
        return events.copy(), 0
    ordered = sorted_events(events)
    selected = ordered.groupby("stock_id", dropna=False, sort=False).head(1).copy()
    suppressed = len(events) - len(selected)
    return selected, suppressed


def same_stock_non_overlap(events: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    if events.empty:
        return events.copy(), 0
    selected_indices: list[int] = []
    suppressed = 0
    for _, part in sorted_events(events).groupby("stock_id", dropna=False):
        last_exit = None
        for idx, row in part.iterrows():
            if last_exit is not None and row["_entry_dt"] <= last_exit:
                suppressed += 1
                continue
            selected_indices.append(idx)
            last_exit = row["_exit_dt"] if last_exit is None or row["_exit_dt"] > last_exit else last_exit
    return events.loc[selected_indices].copy(), suppressed


def apply_selection(events: pd.DataFrame, selection_basis: str) -> tuple[pd.DataFrame, int]:
    if selection_basis == "event_level_all_events":
        return events.copy(), 0
    if selection_basis == "first_event_per_stock":
        return first_event_per_stock(events)
    if selection_basis == "same_stock_non_overlap":
        return same_stock_non_overlap(events)
    raise KeyError(selection_basis)


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    if sample_size >= 30:
        return "thin_sample"
    if sample_size > 0:
        return "very_thin_sample"
    return "insufficient_sample"


def summarize_returns(events: pd.DataFrame) -> dict[str, Any]:
    sample_size = len(events)
    returns = events["_return"] if not events.empty else pd.Series(dtype=float)
    outcomes = events["return_outcome"].astype(str).str.lower() if not events.empty else pd.Series(dtype=str)
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    unique_stocks = int(events["stock_id"].nunique()) if not events.empty else 0
    stock_counts = events.groupby("stock_id", dropna=False).size() if not events.empty else pd.Series(dtype=int)
    return {
        "sample_size": sample_size,
        "unique_stocks": unique_stocks,
        "stocks_with_multiple_events": int((stock_counts > 1).sum()) if not stock_counts.empty else 0,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100, 4) if sample_size else "",
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100, 4) if sample_size else "",
        "loss_rate_pct": pct_round(loss_count / sample_size * 100, 4) if sample_size else "",
        "avg_return_pct": pct_round(float(returns.mean()), 4) if sample_size else "",
        "median_return_pct": pct_round(float(returns.median()), 4) if sample_size else "",
        "p10_return_pct": pct_round(float(returns.quantile(0.10)), 4) if sample_size else "",
        "p90_return_pct": pct_round(float(returns.quantile(0.90)), 4) if sample_size else "",
        "min_return_pct": pct_round(float(returns.min()), 4) if sample_size else "",
        "max_return_pct": pct_round(float(returns.max()), 4) if sample_size else "",
        "sample_status": sample_status(sample_size),
    }


def build_summary(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_artifact_version = safe_str(source["artifact_version"].iloc[0]) if "artifact_version" in source.columns else ""
    baseline_count = len(source)
    rows: list[dict[str, Any]] = []
    for condition in CONDITION_SETS:
        conditioned = source[condition_mask(source, condition.condition_set_id)].copy()
        for selection_basis, label in SELECTION_BASIS_LABELS.items():
            selected, suppressed = apply_selection(conditioned, selection_basis)
            metrics = summarize_returns(selected)
            row = {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_artifact_version": source_artifact_version,
                "advisory_status": ADVISORY_STATUS,
                "model_id": MODEL_ID,
                "condition_set_id": condition.condition_set_id,
                "condition_set_label": condition.condition_set_label,
                "selection_basis": selection_basis,
                "selection_basis_label": label,
                "baseline_event_count": baseline_count,
                "suppressed_same_stock_overlap_count": suppressed,
                "overlap_pair_count": overlap_pair_count(selected),
                "coverage_pct": pct_round(metrics["sample_size"] / baseline_count * 100, 4) if baseline_count else "",
                "interpretation": "research_only_sensitivity_not_production_evidence",
                "note": condition.note,
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
            row.update(metrics)
            rows.append(row)
    return pd.DataFrame(rows)


def build_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    out = source.copy()
    out = sorted_events(out).copy()
    out["event_sequence_for_stock"] = out.groupby("stock_id", dropna=False).cumcount() + 1

    first_selected, _ = first_event_per_stock(out)
    non_overlap_selected, _ = same_stock_non_overlap(out)
    first_keys = set(first_selected["source_event_key"].astype(str))
    non_overlap_keys = set(non_overlap_selected["source_event_key"].astype(str))

    suppressor: dict[str, pd.Series] = {}
    overlap_count_for_stock: dict[str, int] = {}
    for stock_id, part in out.groupby("stock_id", dropna=False):
        active: list[pd.Series] = []
        pair_count = 0
        last_accepted: pd.Series | None = None
        for _, row in part.iterrows():
            for prior in active:
                if row["_entry_dt"] <= prior["_exit_dt"]:
                    pair_count += 1
            if last_accepted is not None and row["_entry_dt"] <= last_accepted["_exit_dt"]:
                suppressor[safe_str(row["source_event_key"])] = last_accepted
            else:
                last_accepted = row
            active = [prior for prior in active if prior["_exit_dt"] >= row["_entry_dt"]]
            active.append(row)
        overlap_count_for_stock[safe_str(stock_id)] = pair_count

    detail_rows: list[dict[str, Any]] = []
    source_artifact_version = safe_str(out["artifact_version"].iloc[0]) if "artifact_version" in out.columns else ""
    for _, row in out.iterrows():
        source_event_key = safe_str(row.get("source_event_key"))
        suppressing = suppressor.get(source_event_key)
        included = source_event_key in non_overlap_keys
        detail_rows.append(
            {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_artifact_version": source_artifact_version,
                "advisory_status": ADVISORY_STATUS,
                "model_id": MODEL_ID,
                "source_event_key": source_event_key,
                "stock_id": safe_str(row.get("stock_id")),
                "stock_name": safe_str(row.get("stock_name")),
                "signal_date": safe_str(row.get("signal_date")),
                "confirmation_date": safe_str(row.get("confirmation_date")),
                "entry_date": safe_str(row.get("entry_date")),
                "exit_date": safe_str(row.get("exit_date")),
                "return_pct": safe_str(row.get("return_pct")),
                "return_outcome": safe_str(row.get("return_outcome")),
                "exit_reason": safe_str(row.get("exit_reason")),
                "event_sequence_for_stock": int(row["event_sequence_for_stock"]),
                "all_events_overlap_pair_count_for_stock": overlap_count_for_stock.get(safe_str(row.get("stock_id")), 0),
                "first_event_per_stock_included": str(source_event_key in first_keys),
                "same_stock_non_overlap_included": str(included),
                "same_stock_non_overlap_suppression_reason": ""
                if included
                else "same_stock_active_position_overlap",
                "suppressed_by_source_event_key": safe_str(suppressing.get("source_event_key")) if suppressing is not None else "",
                "suppressed_by_entry_date": safe_str(suppressing.get("entry_date")) if suppressing is not None else "",
                "suppressed_by_exit_date": safe_str(suppressing.get("exit_date")) if suppressing is not None else "",
                "deep_low_120_le40": safe_str(row.get("deep_low_120_le40")),
                "deep_low_240_le40": safe_str(row.get("deep_low_240_le40")),
                "range60_le25": safe_str(row.get("range60_le25")),
                "range120_le25": safe_str(row.get("range120_le25")),
                "limit_up_like": safe_str(row.get("limit_up_like")),
                "consolidation_type": safe_str(row.get("consolidation_type")),
                "risk_type": safe_str(row.get("risk_type")),
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(detail_rows)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    lines = [
        "# Volume Range Breakout V2 Overlap Sensitivity",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source: `{SOURCE_DETAIL_CSV}`",
        "- status: research-only; not a production registry, daily adapter, or PDF change.",
        "- purpose: separate event-level metrics from same-stock non-overlap metrics.",
        "",
        "## Baseline Rows",
        "",
    ]
    baseline = summary[summary["condition_set_id"].astype(str).eq("baseline_all")].copy()
    if not baseline.empty:
        lines.append(
            baseline[
                [
                    "selection_basis",
                    "sample_size",
                    "unique_stocks",
                    "suppressed_same_stock_overlap_count",
                    "overlap_pair_count",
                    "win_rate_pct",
                    "loss_rate_pct",
                    "avg_return_pct",
                    "median_return_pct",
                ]
            ].to_markdown(index=False)
        )
    lines.extend(["", "## Same-Stock Suppression Examples", ""])
    suppressed = detail[detail["same_stock_non_overlap_included"].astype(str).str.lower().eq("false")].copy()
    if not suppressed.empty:
        lines.append(
            suppressed[
                [
                    "stock_id",
                    "stock_name",
                    "signal_date",
                    "entry_date",
                    "exit_date",
                    "return_pct",
                    "suppressed_by_source_event_key",
                    "suppressed_by_entry_date",
                    "suppressed_by_exit_date",
                ]
            ]
            .head(12)
            .to_markdown(index=False)
        )
    else:
        lines.append("_No suppressed same-stock overlap rows._")
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    source = prepare_source()
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source contains forbidden production decision fields: {forbidden}")

    summary = build_summary(source, generated_at)
    detail = build_detail(source, generated_at)

    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_markdown(summary, detail)

    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
