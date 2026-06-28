from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_context_filter_entry_exit_audit import (
    EVENT_FAMILY_ID,
    LATEST_EVENT_CSV as CONTEXT_EVENT_CSV,
    PARAMETER_SET_ID as CONTEXT_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as CONTEXT_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    TARGET_SEGMENT_ID,
    metric_text,
    safe_str,
)
from build_structured_neckline_non_bearish_exit_rule_comparison_audit import (
    COMPARISON_SCOPE_ID,
    LATEST_COMPARISON_CSV,
    PARAMETER_SET_ID as COMPARISON_PARAMETER_SET_ID,
    RESEARCH_ID as COMPARISON_RESEARCH_ID,
    RESEARCH_SELECTION_REASON,
    SELECTED_EXIT_RULE_COMPARISON_ID,
)
from build_structured_neckline_retest_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    RESEARCH_HISTORY_DIR,
    RESEARCH_LATEST_DIR,
)


ROOT = Path(__file__).resolve().parents[1]

RESEARCH_ID = "structured_neckline_selected_exit_loss_diagnostics"
PARAMETER_SET_ID = "structured_neckline_selected_exit_loss_diagnostics_20260629"
DIAGNOSTIC_SCOPE_ID = "selected_close_based_exit_loss_to_loss_diagnostics"

LATEST_EVENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_selected_exit_loss_diagnostics_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_selected_exit_loss_diagnostics_summary_latest.csv"
LATEST_FLAG_CSV = RESEARCH_LATEST_DIR / "structured_neckline_selected_exit_loss_diagnostic_flags_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_selected_exit_loss_diagnostics_latest.md"
HISTORY_EVENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_selected_exit_loss_diagnostics.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_selected_exit_loss_diagnostics_summary.csv"
HISTORY_FLAG_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_selected_exit_loss_diagnostic_flags.csv"

EVENT_KEY_COLUMNS = ["stock_id", "signal_date", "retest_entry_date"]
NUMERIC_FEATURES = [
    "visual_pre_signal_return_pct",
    "visual_pre_signal_range_pct",
    "base_age_sessions",
    "support_pair_span_sessions",
    "neckline_anchor_age_sessions",
    "base_width_pct",
    "low_position_120_pct",
    "selected_mfe_pct",
    "selected_mae_pct",
]

EVENT_COLUMNS = [
    "research_id",
    "source_comparison_research_id",
    "source_comparison_parameter_set_id",
    "source_context_research_id",
    "source_context_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "diagnostic_scope_id",
    "selected_exit_rule_comparison_id",
    "research_selection_reason",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "visual_pre_signal_context",
    "selected_outcome",
    "selected_return_pct",
    "selected_mfe_pct",
    "selected_mae_pct",
    "diagnostic_cohort",
    "visual_pre_signal_return_pct",
    "visual_pre_signal_range_pct",
    "base_age_sessions",
    "support_pair_span_sessions",
    "neckline_anchor_age_sessions",
    "base_width_pct",
    "low_position_120_pct",
    "diagnostic_flags",
    "diagnostic_note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "diagnostic_scope_id",
    "selected_exit_rule_comparison_id",
    "diagnostic_cohort",
    "sample_size",
    "unique_stock_count",
    "mixed_context_count",
    "bullish_context_count",
    "avg_selected_return_pct",
    "median_selected_return_pct",
    "avg_selected_mfe_pct",
    "median_selected_mfe_pct",
    "avg_selected_mae_pct",
    "median_selected_mae_pct",
    "median_visual_pre_signal_return_pct",
    "median_visual_pre_signal_range_pct",
    "median_base_age_sessions",
    "median_support_pair_span_sessions",
    "median_neckline_anchor_age_sessions",
    "median_base_width_pct",
    "median_low_position_120_pct",
    "top_diagnostic_flags",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FLAG_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "diagnostic_scope_id",
    "selected_exit_rule_comparison_id",
    "diagnostic_flag",
    "loss_event_count",
    "success_or_neutral_event_count",
    "total_event_count",
    "loss_share_with_flag_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def event_key(row: pd.Series) -> str:
    return "|".join(str(row.get(column, "")) for column in EVENT_KEY_COLUMNS)


def format_float(value: Any) -> str:
    return metric_text(to_float(value))


def is_clean_stock_name(value: Any) -> bool:
    text = safe_str(value)
    return bool(text) and "�" not in text and "嚙" not in text and "?" not in text


def load_stock_name_lookup(stock_ids: list[str]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for stock_id in sorted(set(stock_ids)):
        history_path = ROOT / "data" / "stock_price_history" / f"{stock_id}.csv"
        if not history_path.exists():
            continue
        try:
            history = pd.read_csv(history_path, dtype=str, keep_default_na=False, encoding="utf-8-sig", nrows=1)
        except Exception:
            continue
        if "stock_name" not in history.columns or history.empty:
            continue
        stock_name = safe_str(history["stock_name"].iloc[0])
        if is_clean_stock_name(stock_name):
            lookup[stock_id] = stock_name
    seed_path = ROOT / "config" / "stock_theme_authorized_seed.csv"
    if seed_path.exists():
        try:
            seed = pd.read_csv(seed_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
        except Exception:
            seed = pd.DataFrame()
        if {"stock_id", "stock_name"} <= set(seed.columns):
            for _, row in seed.iterrows():
                stock_id = safe_str(row.get("stock_id"))
                stock_name = safe_str(row.get("stock_name"))
                if stock_id not in lookup and is_clean_stock_name(stock_name):
                    lookup[stock_id] = stock_name
    return lookup


def load_joined_source() -> pd.DataFrame:
    comparison = read_csv(LATEST_COMPARISON_CSV)
    context = read_csv(CONTEXT_EVENT_CSV)
    comparison_required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "comparison_scope_id",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "visual_pre_signal_context",
        "close_neutral_outcome",
        "close_neutral_return_pct",
        "close_neutral_mfe_pct",
        "close_neutral_mae_pct",
        "approved_for_daily",
        "production_readiness",
    }
    context_required = {
        "research_id",
        "parameter_set_id",
        "stock_id",
        "signal_date",
        "retest_entry_date",
        "visual_pre_signal_return_pct",
        "visual_pre_signal_range_pct",
        "base_age_sessions",
        "support_pair_span_sessions",
        "neckline_anchor_age_sessions",
        "base_width_pct",
        "low_position_120_pct",
    }
    missing_comparison = sorted(comparison_required - set(comparison.columns))
    missing_context = sorted(context_required - set(context.columns))
    if missing_comparison:
        raise SystemExit(f"ERROR: comparison source missing columns: {missing_comparison}")
    if missing_context:
        raise SystemExit(f"ERROR: context source missing columns: {missing_context}")
    forbidden = sorted((set(comparison.columns) | set(context.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source contains production fields: {forbidden}")

    comparison = comparison[
        comparison["research_id"].astype(str).eq(COMPARISON_RESEARCH_ID)
        & comparison["parameter_set_id"].astype(str).eq(COMPARISON_PARAMETER_SET_ID)
        & comparison["comparison_scope_id"].astype(str).eq(COMPARISON_SCOPE_ID)
        & comparison["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & comparison["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & comparison["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & comparison["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
        & ~comparison["visual_pre_signal_context"].astype(str).eq("bearish")
    ].copy()
    if comparison.empty:
        raise SystemExit("ERROR: no comparison rows found")
    context = context[
        context["research_id"].astype(str).eq(CONTEXT_RESEARCH_ID)
        & context["parameter_set_id"].astype(str).eq(CONTEXT_PARAMETER_SET_ID)
    ].copy()
    comparison["_key"] = comparison.apply(event_key, axis=1)
    context["_key"] = context.apply(event_key, axis=1)
    if comparison["_key"].duplicated().any():
        raise SystemExit("ERROR: duplicate comparison event key")
    if context["_key"].duplicated().any():
        raise SystemExit("ERROR: duplicate context event key")
    joined = comparison.merge(
        context[
            [
                "_key",
                "visual_pre_signal_return_pct",
                "visual_pre_signal_range_pct",
                "base_age_sessions",
                "support_pair_span_sessions",
                "neckline_anchor_age_sessions",
                "base_width_pct",
                "low_position_120_pct",
            ]
        ],
        on="_key",
        how="left",
        validate="one_to_one",
    )
    if joined[["visual_pre_signal_return_pct", "base_width_pct", "low_position_120_pct"]].eq("").any().any():
        raise SystemExit("ERROR: joined diagnostics missing context features")
    return joined


def success_quantiles(source: pd.DataFrame) -> dict[str, tuple[float, float]]:
    success = source[~source["close_neutral_outcome"].astype(str).eq("loss")]
    quantiles: dict[str, tuple[float, float]] = {}
    for feature in NUMERIC_FEATURES:
        values = pd.to_numeric(success[feature], errors="coerce").dropna()
        if values.empty:
            quantiles[feature] = (math.nan, math.nan)
        else:
            quantiles[feature] = (float(values.quantile(0.25)), float(values.quantile(0.75)))
    return quantiles


def diagnostic_flags(row: pd.Series, quantiles: dict[str, tuple[float, float]]) -> list[str]:
    flags: list[str] = []
    visual_return = to_float(row.get("visual_pre_signal_return_pct"))
    visual_range = to_float(row.get("visual_pre_signal_range_pct"))
    base_age = to_float(row.get("base_age_sessions"))
    support_span = to_float(row.get("support_pair_span_sessions"))
    neckline_age = to_float(row.get("neckline_anchor_age_sessions"))
    base_width = to_float(row.get("base_width_pct"))
    low_position = to_float(row.get("low_position_120_pct"))
    mfe = to_float(row.get("selected_mfe_pct"))
    mae = to_float(row.get("selected_mae_pct"))
    if visual_return >= 50:
        flags.append("large_pre_signal_runup_over_50pct")
    if visual_range >= 60:
        flags.append("wide_pre_signal_range_over_60pct")
    if base_age >= 55:
        flags.append("older_base_age_over_55_sessions")
    if support_span >= 25:
        flags.append("wide_support_pair_span_over_25_sessions")
    if neckline_age <= 1:
        flags.append("neckline_anchor_very_recent_le1_session")
    if base_width >= 20:
        flags.append("wide_base_over_20pct")
    if low_position >= 50:
        flags.append("near_upper_low_position_band_over_50pct")
    if mfe < 5:
        flags.append("weak_follow_through_mfe_below_5pct")
    if mae <= -10:
        flags.append("large_adverse_move_mae_below_minus10pct")
    for feature, (q25, q75) in quantiles.items():
        value = to_float(row.get(feature))
        if math.isnan(value) or math.isnan(q25) or math.isnan(q75):
            continue
        if value < q25:
            flags.append(f"below_success_p25_{feature}")
        if value > q75:
            flags.append(f"above_success_p75_{feature}")
    return sorted(set(flags))


def build_events(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    enriched = source.copy()
    enriched["selected_outcome"] = enriched["close_neutral_outcome"].astype(str)
    enriched["selected_return_pct"] = enriched["close_neutral_return_pct"].map(format_float)
    enriched["selected_mfe_pct"] = enriched["close_neutral_mfe_pct"].map(format_float)
    enriched["selected_mae_pct"] = enriched["close_neutral_mae_pct"].map(format_float)
    quantiles = success_quantiles(enriched)
    stock_name_lookup = load_stock_name_lookup(enriched["stock_id"].astype(str).tolist())
    rows: list[dict[str, str]] = []
    for _, item in enriched.sort_values(["selected_outcome", "signal_date", "stock_id"]).iterrows():
        outcome = safe_str(item.get("selected_outcome"))
        if outcome == "loss":
            cohort = "selected_rule_loss"
        elif outcome == "win":
            cohort = "selected_rule_win"
        elif outcome == "neutral":
            cohort = "selected_rule_neutral"
        else:
            cohort = "selected_rule_other"
        flags = diagnostic_flags(item, quantiles)
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_comparison_research_id": COMPARISON_RESEARCH_ID,
                "source_comparison_parameter_set_id": COMPARISON_PARAMETER_SET_ID,
                "source_context_research_id": CONTEXT_RESEARCH_ID,
                "source_context_parameter_set_id": CONTEXT_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "diagnostic_scope_id": DIAGNOSTIC_SCOPE_ID,
                "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
                "research_selection_reason": RESEARCH_SELECTION_REASON,
                "event_family_id": EVENT_FAMILY_ID,
                "segment_id": TARGET_SEGMENT_ID,
                "stock_id": safe_str(item.get("stock_id")),
                "stock_name": stock_name_lookup.get(safe_str(item.get("stock_id")), safe_str(item.get("stock_name"))),
                "signal_date": safe_str(item.get("signal_date")),
                "retest_date": safe_str(item.get("retest_date")),
                "retest_attack_date": safe_str(item.get("retest_attack_date")),
                "retest_entry_date": safe_str(item.get("retest_entry_date")),
                "visual_pre_signal_context": safe_str(item.get("visual_pre_signal_context")),
                "selected_outcome": outcome,
                "selected_return_pct": safe_str(item.get("selected_return_pct")),
                "selected_mfe_pct": safe_str(item.get("selected_mfe_pct")),
                "selected_mae_pct": safe_str(item.get("selected_mae_pct")),
                "diagnostic_cohort": cohort,
                "visual_pre_signal_return_pct": format_float(item.get("visual_pre_signal_return_pct")),
                "visual_pre_signal_range_pct": format_float(item.get("visual_pre_signal_range_pct")),
                "base_age_sessions": format_float(item.get("base_age_sessions")),
                "support_pair_span_sessions": format_float(item.get("support_pair_span_sessions")),
                "neckline_anchor_age_sessions": format_float(item.get("neckline_anchor_age_sessions")),
                "base_width_pct": format_float(item.get("base_width_pct")),
                "low_position_120_pct": format_float(item.get("low_position_120_pct")),
                "diagnostic_flags": ";".join(flags),
                "diagnostic_note": "loss_focus_review" if outcome == "loss" else "comparison_reference_row",
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    events = pd.DataFrame(rows)
    for column in EVENT_COLUMNS:
        if column not in events.columns:
            events[column] = ""
    return events[EVENT_COLUMNS]


def cohort_rows(events: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    success_or_neutral = events[events["selected_outcome"].isin(["win", "neutral"])].copy()
    return [
        ("selected_rule_loss", events[events["selected_outcome"].eq("loss")].copy()),
        ("selected_rule_success_or_neutral", success_or_neutral),
        ("selected_rule_win", events[events["selected_outcome"].eq("win")].copy()),
        ("selected_rule_neutral", events[events["selected_outcome"].eq("neutral")].copy()),
    ]


def numeric_summary(group: pd.DataFrame, column: str, stat: str) -> str:
    values = pd.to_numeric(group[column], errors="coerce").dropna()
    if values.empty:
        return metric_text(math.nan)
    if stat == "avg":
        return metric_text(float(values.mean()))
    return metric_text(float(values.median()))


def top_flags(group: pd.DataFrame) -> str:
    counts: dict[str, int] = {}
    for value in group["diagnostic_flags"].astype(str):
        for flag in [item for item in value.split(";") if item]:
            counts[flag] = counts.get(flag, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:5]
    return ";".join(f"{flag}:{count}" for flag, count in ranked)


def build_summary(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for cohort, group in cohort_rows(events):
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "diagnostic_scope_id": DIAGNOSTIC_SCOPE_ID,
                "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
                "diagnostic_cohort": cohort,
                "sample_size": str(len(group)),
                "unique_stock_count": str(int(group["stock_id"].nunique())) if not group.empty else "0",
                "mixed_context_count": str(int(group["visual_pre_signal_context"].eq("mixed").sum())) if not group.empty else "0",
                "bullish_context_count": str(int(group["visual_pre_signal_context"].eq("bullish").sum())) if not group.empty else "0",
                "avg_selected_return_pct": numeric_summary(group, "selected_return_pct", "avg"),
                "median_selected_return_pct": numeric_summary(group, "selected_return_pct", "median"),
                "avg_selected_mfe_pct": numeric_summary(group, "selected_mfe_pct", "avg"),
                "median_selected_mfe_pct": numeric_summary(group, "selected_mfe_pct", "median"),
                "avg_selected_mae_pct": numeric_summary(group, "selected_mae_pct", "avg"),
                "median_selected_mae_pct": numeric_summary(group, "selected_mae_pct", "median"),
                "median_visual_pre_signal_return_pct": numeric_summary(group, "visual_pre_signal_return_pct", "median"),
                "median_visual_pre_signal_range_pct": numeric_summary(group, "visual_pre_signal_range_pct", "median"),
                "median_base_age_sessions": numeric_summary(group, "base_age_sessions", "median"),
                "median_support_pair_span_sessions": numeric_summary(group, "support_pair_span_sessions", "median"),
                "median_neckline_anchor_age_sessions": numeric_summary(group, "neckline_anchor_age_sessions", "median"),
                "median_base_width_pct": numeric_summary(group, "base_width_pct", "median"),
                "median_low_position_120_pct": numeric_summary(group, "low_position_120_pct", "median"),
                "top_diagnostic_flags": top_flags(group) if not group.empty else "",
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    return summary[SUMMARY_COLUMNS]


def build_flags(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    all_flags = sorted(
        {
            flag
            for value in events["diagnostic_flags"].astype(str)
            for flag in value.split(";")
            if flag
        }
    )
    rows: list[dict[str, str]] = []
    for flag in all_flags:
        has_flag = events["diagnostic_flags"].astype(str).str.split(";").apply(lambda parts: flag in parts)
        loss_count = int((has_flag & events["selected_outcome"].eq("loss")).sum())
        success_count = int((has_flag & events["selected_outcome"].isin(["win", "neutral"])).sum())
        total = loss_count + success_count
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "diagnostic_scope_id": DIAGNOSTIC_SCOPE_ID,
                "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
                "diagnostic_flag": flag,
                "loss_event_count": str(loss_count),
                "success_or_neutral_event_count": str(success_count),
                "total_event_count": str(total),
                "loss_share_with_flag_pct": metric_text(loss_count / total * 100.0 if total else math.nan),
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    flags = pd.DataFrame(rows).sort_values(
        ["loss_event_count", "loss_share_with_flag_pct", "diagnostic_flag"],
        ascending=[False, False, True],
    )
    for column in FLAG_COLUMNS:
        if column not in flags.columns:
            flags[column] = ""
    return flags[FLAG_COLUMNS]


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


def write_markdown(events: pd.DataFrame, summary: pd.DataFrame, flags: pd.DataFrame, generated_at: str) -> None:
    loss_rows = events[events["selected_outcome"].eq("loss")].copy()
    loss_flags = flags[pd.to_numeric(flags["loss_event_count"], errors="coerce").fillna(0).gt(0)].copy()
    lines = [
        "# Structured Neckline Selected Exit Loss Diagnostics",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- selected_exit_rule_comparison_id: `{SELECTED_EXIT_RULE_COMPARISON_ID}`",
        f"- research_selection_reason: `{RESEARCH_SELECTION_REASON}`",
        f"- sample_size: `{len(events)}`",
        f"- loss_count: `{len(loss_rows)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Interpretation",
        "",
        "- This audit compares the five selected-rule losses against the remaining win/neutral rows.",
        "- Diagnostic flags are candidate failure features only; they are not production filters.",
        "- The strongest next step is manual chart review of the five loss rows before promoting any additional exclusion.",
        "",
        "## Cohort Summary",
        "",
        *markdown_table(
            summary,
            [
                "diagnostic_cohort",
                "sample_size",
                "mixed_context_count",
                "bullish_context_count",
                "median_selected_return_pct",
                "median_selected_mfe_pct",
                "median_selected_mae_pct",
                "median_visual_pre_signal_return_pct",
                "median_visual_pre_signal_range_pct",
                "median_base_width_pct",
                "median_low_position_120_pct",
                "top_diagnostic_flags",
            ],
        ),
        "",
        "## Loss Rows",
        "",
        *markdown_table(
            loss_rows,
            [
                "stock_id",
                "stock_name",
                "signal_date",
                "retest_entry_date",
                "visual_pre_signal_context",
                "selected_return_pct",
                "selected_mfe_pct",
                "selected_mae_pct",
                "visual_pre_signal_return_pct",
                "visual_pre_signal_range_pct",
                "base_width_pct",
                "low_position_120_pct",
                "diagnostic_flags",
            ],
            limit=20,
        ),
        "",
        "## Loss Flag Counts",
        "",
        *markdown_table(
            loss_flags,
            [
                "diagnostic_flag",
                "loss_event_count",
                "success_or_neutral_event_count",
                "total_event_count",
                "loss_share_with_flag_pct",
            ],
            limit=40,
        ),
        "",
        "## Boundary Notes",
        "",
        "- This is research/backtest advisory-only output.",
        "- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "- No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source = load_joined_source()
    events = build_events(source, generated_at)
    summary = build_summary(events, generated_at)
    flags = build_flags(events, generated_at)
    write_csv(events, LATEST_EVENT_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(flags, LATEST_FLAG_CSV)
    write_csv(events, HISTORY_EVENT_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(flags, HISTORY_FLAG_CSV)
    write_markdown(events, summary, flags, generated_at)
    print(f"Saved: {LATEST_EVENT_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_FLAG_CSV} rows={len(flags)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
