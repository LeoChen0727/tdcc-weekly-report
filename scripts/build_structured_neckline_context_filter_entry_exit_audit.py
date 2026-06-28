from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_retest_entry_exit_grid import (
    EVENT_FAMILY_ID,
    LATEST_DETAIL_CSV as ENTRY_EXIT_DETAIL_CSV,
    PARAMETER_SET_ID as ENTRY_EXIT_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as ENTRY_EXIT_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    normalize_code,
    normalize_date,
    safe_str,
)
from build_structured_neckline_retest_evidence_shortlist import (
    LATEST_INDEX_CSV as EVIDENCE_SHORTLIST_CSV,
    PARAMETER_SET_ID as EVIDENCE_PARAMETER_SET_ID,
    RESEARCH_ID as EVIDENCE_RESEARCH_ID,
)
from build_structured_neckline_retest_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    RESEARCH_HISTORY_DIR,
    RESEARCH_LATEST_DIR,
    TARGET_SEGMENT_ID,
    metric_text,
)


RESEARCH_ID = "structured_neckline_context_filter_entry_exit_audit"
PARAMETER_SET_ID = "structured_neckline_context_filter_entry_exit_audit_20260629"

LATEST_EVENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_filter_entry_exit_events_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_filter_entry_exit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_context_filter_entry_exit_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_context_filter_entry_exit_audit_latest.md"
HISTORY_EVENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_filter_entry_exit_events.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_filter_entry_exit_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_context_filter_entry_exit_audit.csv"

TARGET_CONTEXT_EXCLUSION = "bearish"
PASS_COHORT_ID = "visual_context_non_bearish"
ALL_COHORT_ID = "all_review_shortlist_events"
EXCLUDED_COHORT_ID = "visual_context_bearish_excluded"
TARGET_CURRENT_STOP_RULE = "signal_low_stop"
TARGET_CURRENT_EXIT_RULE = "tp10_close_or_neutral_after_5pct_close_20d"
TARGET_CURRENT_OUTCOME_RULE = "tp10_close_win_5pct_pullback_neutral"

EVENT_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "reference_price",
    "visual_pre_signal_context",
    "visual_context_filter_result",
    "visual_context_filter_reason",
    "visible_context_start",
    "visible_context_end",
    "visual_pre_signal_sessions",
    "visual_pre_signal_return_pct",
    "visual_pre_signal_range_pct",
    "base_age_sessions",
    "support_pair_span_sessions",
    "neckline_anchor_age_sessions",
    "base_width_pct",
    "low_position_120_pct",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "source_evidence_research_id",
    "source_evidence_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "cohort_id",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "visual_pre_signal_context",
    "visual_context_filter_result",
    "stop_rule_id",
    "exit_rule_id",
    "outcome_rule_id",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_reason",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "outcome_result",
    "positive_return_result",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "cohort_id",
    "event_family_id",
    "segment_id",
    "stop_rule_id",
    "exit_rule_id",
    "outcome_rule_id",
    "sample_size",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "avg_mfe_pct",
    "avg_mae_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def event_key(row: pd.Series) -> tuple[str, str, str]:
    return (
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("signal_date")),
        normalize_date(row.get("retest_entry_date")),
    )


def build_events(generated_at: str) -> pd.DataFrame:
    source = read_csv(EVIDENCE_SHORTLIST_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "reference_price",
        "visual_pre_signal_context",
        "visible_context_start",
        "visible_context_end",
        "visual_pre_signal_sessions",
        "visual_pre_signal_return_pct",
        "visual_pre_signal_range_pct",
        "base_age_sessions",
        "support_pair_span_sessions",
        "neckline_anchor_age_sessions",
        "base_width_pct",
        "low_position_120_pct",
        "manual_review_status",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: evidence shortlist missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: evidence shortlist contains production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(EVIDENCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(EVIDENCE_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & source["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: evidence shortlist has no target rows")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    rows["_key"] = rows.apply(event_key, axis=1)
    rows = rows.sort_values(["signal_date", "stock_id", "retest_entry_date"]).drop_duplicates("_key", keep="first")
    event_rows: list[dict[str, Any]] = []
    for _, item in rows.iterrows():
        context = safe_str(item.get("visual_pre_signal_context"))
        passed = context != TARGET_CONTEXT_EXCLUSION
        event_rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_research_id": EVIDENCE_RESEARCH_ID,
                "source_parameter_set_id": EVIDENCE_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "event_family_id": EVENT_FAMILY_ID,
                "segment_id": TARGET_SEGMENT_ID,
                "stock_id": normalize_code(item.get("stock_id")),
                "stock_name": safe_str(item.get("stock_name")),
                "signal_date": normalize_date(item.get("signal_date")),
                "retest_date": normalize_date(item.get("retest_date")),
                "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                "reference_price": safe_str(item.get("reference_price")),
                "visual_pre_signal_context": context,
                "visual_context_filter_result": "pass" if passed else "excluded",
                "visual_context_filter_reason": "not_bearish_visual_pre_signal_context" if passed else "bearish_visual_pre_signal_context",
                "visible_context_start": normalize_date(item.get("visible_context_start")),
                "visible_context_end": normalize_date(item.get("visible_context_end")),
                "visual_pre_signal_sessions": safe_str(item.get("visual_pre_signal_sessions")),
                "visual_pre_signal_return_pct": safe_str(item.get("visual_pre_signal_return_pct")),
                "visual_pre_signal_range_pct": safe_str(item.get("visual_pre_signal_range_pct")),
                "base_age_sessions": safe_str(item.get("base_age_sessions")),
                "support_pair_span_sessions": safe_str(item.get("support_pair_span_sessions")),
                "neckline_anchor_age_sessions": safe_str(item.get("neckline_anchor_age_sessions")),
                "base_width_pct": safe_str(item.get("base_width_pct")),
                "low_position_120_pct": safe_str(item.get("low_position_120_pct")),
                "manual_review_status": "pending_user_chart_review",
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    events = pd.DataFrame(event_rows)
    for column in EVENT_COLUMNS:
        if column not in events.columns:
            events[column] = ""
    return events[EVENT_COLUMNS]


def build_detail(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source = read_csv(ENTRY_EXIT_DETAIL_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "stop_rule_id",
        "exit_rule_id",
        "outcome_rule_id",
        "entry_price",
        "exit_date",
        "exit_price",
        "exit_reason",
        "holding_days",
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "outcome_result",
        "positive_return_result",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: entry/exit detail missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: entry/exit detail contains production fields: {forbidden}")
    event_context = {
        (row["stock_id"], row["signal_date"], row["retest_entry_date"]): {
            "visual_pre_signal_context": row["visual_pre_signal_context"],
            "visual_context_filter_result": row["visual_context_filter_result"],
        }
        for _, row in events.iterrows()
    }
    event_keys = set(event_context)
    rows = source[
        source["research_id"].astype(str).eq(ENTRY_EXIT_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(ENTRY_EXIT_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & source["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
    ].copy()
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    rows["signal_date"] = rows["signal_date"].map(normalize_date)
    rows["retest_entry_date"] = rows["retest_entry_date"].map(normalize_date)
    rows["_key"] = list(zip(rows["stock_id"], rows["signal_date"], rows["retest_entry_date"]))
    rows = rows[rows["_key"].isin(event_keys)].copy()
    if rows.empty:
        raise SystemExit("ERROR: no entry/exit rows matched evidence shortlist events")

    detail_rows: list[dict[str, Any]] = []
    for _, item in rows.iterrows():
        context = event_context[item["_key"]]
        cohorts = [ALL_COHORT_ID]
        if context["visual_context_filter_result"] == "pass":
            cohorts.append(PASS_COHORT_ID)
        else:
            cohorts.append(EXCLUDED_COHORT_ID)
        for cohort_id in cohorts:
            detail_rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_research_id": ENTRY_EXIT_RESEARCH_ID,
                    "source_parameter_set_id": ENTRY_EXIT_PARAMETER_SET_ID,
                    "source_evidence_research_id": EVIDENCE_RESEARCH_ID,
                    "source_evidence_parameter_set_id": EVIDENCE_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "cohort_id": cohort_id,
                    "event_family_id": EVENT_FAMILY_ID,
                    "segment_id": TARGET_SEGMENT_ID,
                    "stock_id": normalize_code(item.get("stock_id")),
                    "stock_name": safe_str(item.get("stock_name")),
                    "signal_date": normalize_date(item.get("signal_date")),
                    "retest_date": normalize_date(item.get("retest_date")),
                    "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                    "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                    "visual_pre_signal_context": context["visual_pre_signal_context"],
                    "visual_context_filter_result": context["visual_context_filter_result"],
                    "stop_rule_id": safe_str(item.get("stop_rule_id")),
                    "exit_rule_id": safe_str(item.get("exit_rule_id")),
                    "outcome_rule_id": safe_str(item.get("outcome_rule_id")),
                    "entry_price": safe_str(item.get("entry_price")),
                    "exit_date": normalize_date(item.get("exit_date")),
                    "exit_price": safe_str(item.get("exit_price")),
                    "exit_reason": safe_str(item.get("exit_reason")),
                    "holding_days": safe_str(item.get("holding_days")),
                    "return_pct": safe_str(item.get("return_pct")),
                    "mfe_pct": safe_str(item.get("mfe_pct")),
                    "mae_pct": safe_str(item.get("mae_pct")),
                    "outcome_result": safe_str(item.get("outcome_result")),
                    "positive_return_result": safe_str(item.get("positive_return_result")),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    detail = pd.DataFrame(detail_rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    return detail[DETAIL_COLUMNS]


def summary_for(group: pd.DataFrame) -> dict[str, str]:
    outcome = group["outcome_result"].astype(str)
    wins = int(outcome.eq("win").sum())
    neutral = int(outcome.eq("neutral").sum())
    losses = int(outcome.eq("loss").sum())
    evaluated = wins + neutral + losses
    mature = wins + losses
    returns = pd.to_numeric(group["return_pct"], errors="coerce").dropna()
    mfe = pd.to_numeric(group["mfe_pct"], errors="coerce").dropna()
    mae = pd.to_numeric(group["mae_pct"], errors="coerce").dropna()
    positives = pd.to_numeric(group["positive_return_result"].astype(str).eq("positive"), errors="coerce")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "cohort_id": safe_str(group["cohort_id"].iloc[0]),
        "event_family_id": EVENT_FAMILY_ID,
        "segment_id": TARGET_SEGMENT_ID,
        "stop_rule_id": safe_str(group["stop_rule_id"].iloc[0]),
        "exit_rule_id": safe_str(group["exit_rule_id"].iloc[0]),
        "outcome_rule_id": safe_str(group["outcome_rule_id"].iloc[0]),
        "sample_size": str(len(group)),
        "unique_stock_count": str(int(group["stock_id"].nunique())),
        "win_count": str(wins),
        "neutral_count": str(neutral),
        "loss_count": str(losses),
        "pure_win_rate_pct": metric_text(wins / mature * 100.0 if mature else math.nan),
        "neutral_inclusive_success_rate_pct": metric_text((wins + neutral) / evaluated * 100.0 if evaluated else math.nan),
        "positive_return_rate_pct": metric_text(float(positives.mean()) * 100.0 if len(positives) else math.nan),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "avg_mfe_pct": metric_text(float(mfe.mean()) if len(mfe) else math.nan),
        "avg_mae_pct": metric_text(float(mae.mean()) if len(mae) else math.nan),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": safe_str(group["generated_at"].iloc[0]),
    }


def build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    rows = [
        summary_for(group)
        for _, group in detail.groupby(["cohort_id", "stop_rule_id", "exit_rule_id", "outcome_rule_id"], sort=False)
    ]
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    summary["_sample"] = pd.to_numeric(summary["sample_size"], errors="coerce").fillna(0)
    summary["_win"] = pd.to_numeric(summary["pure_win_rate_pct"], errors="coerce").fillna(-1)
    summary["_neutral_success"] = pd.to_numeric(summary["neutral_inclusive_success_rate_pct"], errors="coerce").fillna(-1)
    summary["_median"] = pd.to_numeric(summary["median_return_pct"], errors="coerce").fillna(-999)
    summary = summary.sort_values(
        ["cohort_id", "_sample", "_win", "_neutral_success", "_median"],
        ascending=[True, False, False, False, False],
    ).drop(columns=["_sample", "_win", "_neutral_success", "_median"])
    return summary[SUMMARY_COLUMNS]


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


def write_markdown(events: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    context_counts = (
        events.groupby(["visual_context_filter_result", "visual_pre_signal_context"], dropna=False)
        .agg(events=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
    )
    current_rule = summary[
        summary["stop_rule_id"].eq(TARGET_CURRENT_STOP_RULE)
        & summary["exit_rule_id"].eq(TARGET_CURRENT_EXIT_RULE)
        & summary["outcome_rule_id"].eq(TARGET_CURRENT_OUTCOME_RULE)
    ].copy()
    top_pass = summary[summary["cohort_id"].eq(PASS_COHORT_ID)].copy()
    top_pass["_win"] = pd.to_numeric(top_pass["pure_win_rate_pct"], errors="coerce").fillna(-1)
    top_pass["_neutral"] = pd.to_numeric(top_pass["neutral_inclusive_success_rate_pct"], errors="coerce").fillna(-1)
    top_pass["_median"] = pd.to_numeric(top_pass["median_return_pct"], errors="coerce").fillna(-999)
    top_pass = top_pass.sort_values(["_win", "_neutral", "_median"], ascending=[False, False, False]).drop(
        columns=["_win", "_neutral", "_median"]
    )
    lines = [
        "# Structured Neckline Context Filter Entry/Exit Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_entry_exit_research_id: `{ENTRY_EXIT_RESEARCH_ID}`",
        f"- source_evidence_research_id: `{EVIDENCE_RESEARCH_ID}`",
        f"- target_segment_id: `{TARGET_SEGMENT_ID}`",
        f"- exclusion_rule: `visual_pre_signal_context != {TARGET_CONTEXT_EXCLUSION}`",
        f"- evidence_event_count: `{len(events)}`",
        f"- pass_event_count: `{int(events['visual_context_filter_result'].eq('pass').sum())}`",
        f"- excluded_event_count: `{int(events['visual_context_filter_result'].eq('excluded').sum())}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Interpretation",
        "",
        "- This audit treats bearish pre-signal context as the first-pass exclusion before comparing entry/exit/neutral rules.",
        "- The three e04 folders are outcome buckets from the current exit rule: win, neutral, and loss. They are not manual pattern folders.",
        "- Because the user's visual conclusion came from the evidence charts, the filter uses `visual_pre_signal_context`, which is computed from the same visible chart span.",
        "- This is not a production gate. It is a research-only candidate filter for the next entry/exit grid discussion.",
        "",
        "## Context Filter Counts",
        "",
        *markdown_table(context_counts, list(context_counts.columns), limit=40),
        "",
        "## Current e04 Rule Before/After Filter",
        "",
        *markdown_table(
            current_rule,
            [
                "cohort_id",
                "sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "avg_mae_pct",
            ],
            limit=20,
        ),
        "",
        "## Top Non-Bearish Entry/Exit Rows",
        "",
        *markdown_table(
            top_pass,
            [
                "stop_rule_id",
                "exit_rule_id",
                "outcome_rule_id",
                "sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "avg_mae_pct",
            ],
            limit=30,
        ),
        "",
        "## Boundary Notes",
        "",
        "- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "- This audit only filters existing evidence-shortlist events. It does not change the structured-neckline detector or production stock model registry.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = build_events(generated_at)
    detail = build_detail(events, generated_at)
    summary = build_summary(detail)
    write_csv(events, LATEST_EVENT_CSV)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(events, HISTORY_EVENT_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(events, summary, generated_at)
    print(f"Saved: {LATEST_EVENT_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
