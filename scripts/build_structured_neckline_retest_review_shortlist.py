from __future__ import annotations

from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import shutil

import pandas as pd

from build_structured_neckline_retest_review_packet import (
    EVENT_FAMILY_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    LATEST_INDEX_CSV as SOURCE_INDEX_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_HISTORY_DIR,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    RESEARCH_LATEST_DIR,
    RESEARCH_VARIANT_ID,
    TARGET_SEGMENT_ID,
    TARGET_STOP_RULE_ID,
    exit_folder,
    metric_text,
    normalize_code,
    normalize_date,
    outcome_folder,
    safe_float,
    safe_path_part,
    safe_str,
)


ROOT = Path(".")
CHART_ROOT = RESEARCH_LATEST_DIR / "structured_neckline_retest_shortlist"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_review_shortlist_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "structured_neckline_retest_review_shortlist_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_retest_review_shortlist.csv"

RESEARCH_ID = "structured_neckline_retest_review_shortlist"
PARAMETER_SET_ID = "structured_neckline_retest_review_shortlist_20260627"
MANUAL_REVIEW_STATUS = "pending_user_chart_review"

FOCUS_EXIT_RULE_IDS = [
    "tp10_intraday_or_fixed_20d_close",
    "tp10_close_or_neutral_after_5pct_close_20d",
]

REASON_ORDER = [
    "top_return_review",
    "bottom_return_review",
    "median_return_review",
    "missed_upside_review",
    "drawdown_risk_review",
    "lowest_position_review",
    "wide_base_review",
]

REASON_FOCUS = {
    "top_return_review": "check whether winners are structurally repeatable, not only one-day spikes",
    "bottom_return_review": "inspect common failure shape before stop or weak exit",
    "median_return_review": "inspect ordinary cases, not only extremes",
    "missed_upside_review": "check rows with high MFE but no win under the chosen exit rule",
    "drawdown_risk_review": "inspect whether stop placement or retest quality creates avoidable drawdown",
    "lowest_position_review": "inspect the lowest-price-position cases for bottom-breakout quality",
    "wide_base_review": "inspect whether wider base structures behave differently",
}

OUTPUT_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_family_id",
    "segment_id",
    "stop_rule_id",
    "exit_rule_id",
    "outcome_rule_id",
    "outcome_result",
    "selection_bucket",
    "selection_reasons",
    "manual_review_focus",
    "source_chart_path",
    "source_chart_path_absolute",
    "shortlist_chart_path",
    "shortlist_chart_path_absolute",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "exit_date",
    "exit_reason",
    "reference_price",
    "stop_level",
    "entry_price",
    "exit_price",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "tdcc_fresh",
    "tdcc_supportive",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_source() -> pd.DataFrame:
    if not SOURCE_INDEX_CSV.exists():
        raise SystemExit(f"ERROR: missing source review packet: {SOURCE_INDEX_CSV}")
    source = pd.read_csv(SOURCE_INDEX_CSV, dtype=str, keep_default_na=False)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stop_rule_id",
        "exit_rule_id",
        "outcome_rule_id",
        "outcome_result",
        "chart_path",
        "chart_path_absolute",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "exit_date",
        "exit_reason",
        "reference_price",
        "stop_level",
        "entry_price",
        "exit_price",
        "holding_days",
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "market_regime",
        "low_position_120_pct",
        "base_width_pct",
        "support_touch_count",
        "tdcc_fresh",
        "tdcc_supportive",
        "manual_review_status",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source review packet missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source review packet contains production fields: {forbidden}")

    rows = source[
        source["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & source["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
        & source["stop_rule_id"].astype(str).eq(TARGET_STOP_RULE_ID)
        & source["exit_rule_id"].astype(str).isin(FOCUS_EXIT_RULE_IDS)
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no rows available for structured neckline retest shortlist")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    for column in [
        "reference_price",
        "stop_level",
        "entry_price",
        "exit_price",
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "low_position_120_pct",
        "base_width_pct",
    ]:
        rows[column] = pd.to_numeric(rows.get(column, ""), errors="coerce")
    return rows.sort_values(["exit_rule_id", "outcome_result", "signal_date", "stock_id"]).reset_index(drop=True)


def key_for(row: pd.Series) -> tuple[str, str, str, str, str]:
    return (
        safe_str(row.get("exit_rule_id")),
        safe_str(row.get("outcome_result")),
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("signal_date")),
        normalize_date(row.get("retest_entry_date")),
    )


def add_rows(
    selected: OrderedDict[tuple[str, str, str, str, str], dict[str, Any]],
    rows: pd.DataFrame,
    reason: str,
) -> None:
    for _, item in rows.iterrows():
        key = key_for(item)
        if key not in selected:
            selected[key] = {"row": item.copy(), "reasons": []}
        if reason not in selected[key]["reasons"]:
            selected[key]["reasons"].append(reason)


def numeric_sorted(group: pd.DataFrame, column: str, ascending: bool) -> pd.DataFrame:
    frame = group.copy()
    frame[f"_{column}_num"] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame[frame[f"_{column}_num"].notna()].copy()
    return frame.sort_values(
        [f"_{column}_num", "signal_date", "stock_id", "retest_entry_date"],
        ascending=[ascending, True, True, True],
    )


def select_median(group: pd.DataFrame, count: int) -> pd.DataFrame:
    frame = group.copy()
    returns = pd.to_numeric(frame["return_pct"], errors="coerce")
    median = returns.median()
    if math.isnan(float(median)):
        return pd.DataFrame(columns=group.columns)
    frame["_median_distance"] = (returns - median).abs()
    return frame.sort_values(["_median_distance", "signal_date", "stock_id", "retest_entry_date"]).head(count)


def select_rows(source: pd.DataFrame) -> OrderedDict[tuple[str, str, str, str, str], dict[str, Any]]:
    selected: OrderedDict[tuple[str, str, str, str, str], dict[str, Any]] = OrderedDict()

    for _, group in source.groupby(["exit_rule_id", "outcome_result"], sort=False):
        add_rows(selected, numeric_sorted(group, "return_pct", ascending=False).head(3), "top_return_review")
        add_rows(selected, numeric_sorted(group, "return_pct", ascending=True).head(3), "bottom_return_review")
        add_rows(selected, select_median(group, count=2), "median_return_review")

    for _, group in source.groupby("exit_rule_id", sort=False):
        non_wins = group[~group["outcome_result"].astype(str).eq("win")].copy()
        add_rows(selected, numeric_sorted(non_wins, "mfe_pct", ascending=False).head(4), "missed_upside_review")
        add_rows(selected, numeric_sorted(group, "mae_pct", ascending=True).head(4), "drawdown_risk_review")
        add_rows(selected, numeric_sorted(group, "low_position_120_pct", ascending=True).head(3), "lowest_position_review")
        add_rows(selected, numeric_sorted(group, "base_width_pct", ascending=False).head(3), "wide_base_review")

    return selected


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear shortlist chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def shortlist_filename(row: pd.Series, reasons: list[str]) -> str:
    parts = [
        normalize_date(row.get("signal_date")),
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("retest_entry_date")),
        safe_path_part(row.get("outcome_result")),
        safe_path_part(metric_text(safe_float(row.get("return_pct")))),
    ]
    return "_".join(parts) + ".png"


def copy_chart(row: pd.Series, reasons: list[str]) -> tuple[Path, Path]:
    source_chart = Path(safe_str(row.get("chart_path")))
    if not source_chart.exists():
        raise SystemExit(f"ERROR: missing source chart: {source_chart}")
    folder = CHART_ROOT / exit_folder(row.get("exit_rule_id")) / outcome_folder(row.get("outcome_result"))
    target_chart = folder / shortlist_filename(row, reasons)
    target_chart.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_chart, target_chart)
    return source_chart, target_chart


def build_shortlist(generated_at: str) -> pd.DataFrame:
    source = read_source()
    selected = select_rows(source)
    if not selected:
        raise SystemExit("ERROR: shortlist selection produced no rows")
    clean_chart_root()

    rows: list[dict[str, Any]] = []
    for item in selected.values():
        row = item["row"]
        reasons = [reason for reason in REASON_ORDER if reason in item["reasons"]]
        source_chart, shortlist_chart = copy_chart(row, reasons)
        focus = "; ".join(REASON_FOCUS[reason] for reason in reasons)
        out = {
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "event_family_id": EVENT_FAMILY_ID,
            "segment_id": TARGET_SEGMENT_ID,
            "stop_rule_id": TARGET_STOP_RULE_ID,
            "exit_rule_id": safe_str(row.get("exit_rule_id")),
            "outcome_rule_id": safe_str(row.get("outcome_rule_id")),
            "outcome_result": safe_str(row.get("outcome_result")),
            "selection_bucket": safe_str(row.get("outcome_result")),
            "selection_reasons": ";".join(reasons),
            "manual_review_focus": focus,
            "source_chart_path": source_chart.as_posix(),
            "source_chart_path_absolute": str(source_chart.resolve()),
            "shortlist_chart_path": shortlist_chart.as_posix(),
            "shortlist_chart_path_absolute": str(shortlist_chart.resolve()),
            "stock_id": normalize_code(row.get("stock_id")),
            "stock_name": safe_str(row.get("stock_name")),
            "signal_date": normalize_date(row.get("signal_date")),
            "retest_date": normalize_date(row.get("retest_date")),
            "retest_attack_date": normalize_date(row.get("retest_attack_date")),
            "retest_entry_date": normalize_date(row.get("retest_entry_date")),
            "exit_date": normalize_date(row.get("exit_date")),
            "exit_reason": safe_str(row.get("exit_reason")),
            "reference_price": metric_text(safe_float(row.get("reference_price"))),
            "stop_level": metric_text(safe_float(row.get("stop_level"))),
            "entry_price": metric_text(safe_float(row.get("entry_price"))),
            "exit_price": metric_text(safe_float(row.get("exit_price"))),
            "holding_days": safe_str(row.get("holding_days")),
            "return_pct": metric_text(safe_float(row.get("return_pct"))),
            "mfe_pct": metric_text(safe_float(row.get("mfe_pct"))),
            "mae_pct": metric_text(safe_float(row.get("mae_pct"))),
            "market_regime": safe_str(row.get("market_regime")),
            "low_position_120_pct": metric_text(safe_float(row.get("low_position_120_pct"))),
            "base_width_pct": metric_text(safe_float(row.get("base_width_pct"))),
            "support_touch_count": safe_str(row.get("support_touch_count")),
            "tdcc_fresh": safe_str(row.get("tdcc_fresh")).lower(),
            "tdcc_supportive": safe_str(row.get("tdcc_supportive")).lower(),
            "manual_review_status": MANUAL_REVIEW_STATUS,
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        rows.append(out)

    index = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in index.columns:
            index[column] = ""
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in shortlist: {forbidden}")
    return index[OUTPUT_COLUMNS].sort_values(
        ["exit_rule_id", "outcome_result", "selection_reasons", "signal_date", "stock_id"]
    )


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def reason_counts(index: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for reason in REASON_ORDER:
        count = int(index["selection_reasons"].astype(str).str.contains(reason, regex=False).sum())
        rows.append({"selection_reason": reason, "row_count": str(count)})
    return pd.DataFrame(rows)


def write_markdown(index: pd.DataFrame, generated_at: str) -> None:
    outcome_summary = (
        index.groupby(["exit_rule_id", "outcome_result"], dropna=False)
        .agg(
            shortlist_rows=("stock_id", "size"),
            unique_stocks=("stock_id", "nunique"),
            avg_return_pct=("return_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
            median_return_pct=("return_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").median())),
            avg_mfe_pct=("mfe_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
            avg_mae_pct=("mae_pct", lambda values: metric_text(pd.to_numeric(values, errors="coerce").mean())),
        )
        .reset_index()
    )
    sample = index[
        [
            "exit_rule_id",
            "outcome_result",
            "stock_id",
            "stock_name",
            "signal_date",
            "retest_entry_date",
            "return_pct",
            "mfe_pct",
            "mae_pct",
            "selection_reasons",
            "shortlist_chart_path",
        ]
    ].copy()
    lines = [
        "# Structured Neckline Retest Review Shortlist",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        f"- focus_exit_rule_ids: `{';'.join(FOCUS_EXIT_RULE_IDS)}`",
        f"- segment_id: `{TARGET_SEGMENT_ID}`",
        f"- stop_rule_id: `{TARGET_STOP_RULE_ID}`",
        f"- chart_root: `{CHART_ROOT}`",
        f"- shortlist_chart_count: `{len(index)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this shortlist does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Selection Purpose",
        "",
        "This shortlist reduces the 380-chart structured-neckline retest packet to a manual review set for the two 10% exit rules. It selects return extremes, median cases, missed-upside cases, drawdown-risk cases, lowest-position cases, and wide-base cases. The selection is evidence triage only; it is not a production model rule.",
        "",
        "## Outcome Summary",
        "",
        *markdown_table(outcome_summary, list(outcome_summary.columns), limit=20),
        "",
        "## Selection Reason Counts",
        "",
        *markdown_table(reason_counts(index), ["selection_reason", "row_count"], limit=20),
        "",
        "## Review Index",
        "",
        *markdown_table(sample, list(sample.columns), limit=120),
        "",
        "## Boundary Notes",
        "",
        "- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "- The shortlist is a subset of `structured_neckline_retest_review_latest.csv`; it does not regenerate signal logic.",
        "- Manual review should compare whether the 10% take-profit rules win because the pattern is repeatable or because of a few non-repeatable spikes.",
    ]
    LATEST_INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_INDEX_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    index = build_shortlist(generated_at)
    write_csv(index, LATEST_INDEX_CSV)
    write_csv(index, HISTORY_INDEX_CSV)
    write_markdown(index, generated_at)
    png_count = len(list(CHART_ROOT.rglob("*.png")))
    print(f"Saved: {LATEST_INDEX_CSV} rows={len(index)}")
    print(f"Saved: {LATEST_INDEX_MD}")
    print(f"Saved chart root: {CHART_ROOT} charts={png_count}")
    print(f"Saved: {HISTORY_INDEX_CSV} rows={len(index)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
