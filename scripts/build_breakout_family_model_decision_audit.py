from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_breakout_family_retest_grid import (
    FORBIDDEN_PRODUCTION_FIELDS,
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "breakout_family_model_decision_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "breakout_family_model_decision_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "breakout_family_model_decision_audit.csv"

RESEARCH_ID = "breakout_family_model_decision_audit"
PARAMETER_SET_ID = "breakout_family_model_decision_audit_20260627"

ENTRY_DIRECT = "direct_breakout_next_open"
ENTRY_RETEST = "retest_hold_then_attack_next_open"
PATTERN_ALL = "ALL"

MIN_RETEST_MATURE_FOR_REVIEW = 50
MIN_RETEST_MATURE_FOR_CANDIDATE = 100
MEANINGFUL_WIN_RATE_LIFT_PCT = 8.0
MEANINGFUL_AVG_RETURN_LIFT_PCT = 0.75

OUTPUT_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "source_research_id",
    "source_parameter_set_id",
    "advisory_status",
    "decision_scope",
    "event_family_id",
    "pattern_subtype",
    "direct_sample_size",
    "direct_mature_sample_size",
    "direct_win_rate_pct",
    "direct_avg_return_pct",
    "direct_median_return_pct",
    "retest_signal_sample_size",
    "retest_mature_sample_size",
    "retest_trigger_rate_pct",
    "retest_win_rate_pct",
    "retest_avg_return_pct",
    "retest_median_return_pct",
    "win_rate_lift_pct",
    "avg_return_lift_pct",
    "retest_not_found_count",
    "retest_found_but_no_attack_count",
    "retest_broken_count",
    "sample_quality",
    "entry_decision",
    "split_decision",
    "next_action",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


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


def metric_text(value: float, digits: int = 4) -> str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def to_num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def read_source_detail() -> pd.DataFrame:
    if not SOURCE_DETAIL_CSV.exists():
        raise SystemExit(f"ERROR: missing source detail: {SOURCE_DETAIL_CSV}")
    detail = pd.read_csv(SOURCE_DETAIL_CSV, dtype=str, keep_default_na=False)
    if detail.empty:
        raise SystemExit(f"ERROR: source detail is empty: {SOURCE_DETAIL_CSV}")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source detail contains production decision fields: {forbidden}")
    return detail


def return_stats(series: pd.Series) -> dict[str, float | int]:
    returns = to_num(series).dropna()
    mature = int(len(returns))
    if mature == 0:
        return {
            "mature": 0,
            "win_rate_pct": math.nan,
            "avg_return_pct": math.nan,
            "median_return_pct": math.nan,
        }
    wins = int((returns > 0).sum())
    return {
        "mature": mature,
        "win_rate_pct": wins / mature * 100.0,
        "avg_return_pct": float(returns.mean()),
        "median_return_pct": float(returns.median()),
    }


def metric_group(detail: pd.DataFrame, family: str, subtype: str) -> dict[str, Any]:
    family_mask = detail["event_family_id"].astype(str).eq(family)
    subtype_mask = pd.Series(True, index=detail.index) if subtype == PATTERN_ALL else detail["pattern_subtype"].astype(str).eq(subtype)
    direct = detail[family_mask & subtype_mask & detail["entry_variant"].astype(str).eq(ENTRY_DIRECT)].copy()
    retest = detail[family_mask & subtype_mask & detail["entry_variant"].astype(str).eq(ENTRY_RETEST)].copy()
    direct_stats = return_stats(direct["direct_return_pct"])
    retest_stats = return_stats(retest["retest_return_pct"])
    retest_sample = int(len(retest))
    retest_trigger_rate = retest_stats["mature"] / retest_sample * 100.0 if retest_sample else math.nan
    statuses = retest["retest_status"].astype(str)
    broken_count = int(
        statuses.isin(
            {
                "neckline_effectively_broken_before_retest",
                "neckline_effectively_broken_after_retest",
            }
        ).sum()
    )
    return {
        "direct_sample_size": int(len(direct)),
        "direct_mature_sample_size": int(direct_stats["mature"]),
        "direct_win_rate_pct": float(direct_stats["win_rate_pct"]),
        "direct_avg_return_pct": float(direct_stats["avg_return_pct"]),
        "direct_median_return_pct": float(direct_stats["median_return_pct"]),
        "retest_signal_sample_size": retest_sample,
        "retest_mature_sample_size": int(retest_stats["mature"]),
        "retest_trigger_rate_pct": retest_trigger_rate,
        "retest_win_rate_pct": float(retest_stats["win_rate_pct"]),
        "retest_avg_return_pct": float(retest_stats["avg_return_pct"]),
        "retest_median_return_pct": float(retest_stats["median_return_pct"]),
        "win_rate_lift_pct": float(retest_stats["win_rate_pct"]) - float(direct_stats["win_rate_pct"]),
        "avg_return_lift_pct": float(retest_stats["avg_return_pct"]) - float(direct_stats["avg_return_pct"]),
        "retest_not_found_count": int(statuses.eq("retest_not_found").sum()),
        "retest_found_but_no_attack_count": int(statuses.eq("retest_found_but_no_attack").sum()),
        "retest_broken_count": broken_count,
    }


def sample_quality(metrics: dict[str, Any]) -> str:
    if metrics["direct_mature_sample_size"] < 100 or metrics["retest_mature_sample_size"] < MIN_RETEST_MATURE_FOR_REVIEW:
        return "thin_sample"
    if metrics["retest_trigger_rate_pct"] < 20.0:
        return "low_retest_conversion"
    return "reviewable_sample"


def entry_decision(metrics: dict[str, Any]) -> str:
    if metrics["retest_mature_sample_size"] < MIN_RETEST_MATURE_FOR_REVIEW:
        return "insufficient_retest_sample"
    if (
        metrics["win_rate_lift_pct"] >= MEANINGFUL_WIN_RATE_LIFT_PCT
        and metrics["avg_return_lift_pct"] >= MEANINGFUL_AVG_RETURN_LIFT_PCT
    ):
        return "prioritize_retest_confirmation_research"
    if metrics["win_rate_lift_pct"] >= 5.0:
        return "mixed_retest_improvement_review"
    return "do_not_prioritize_retest_confirmation"


def split_decision(
    decision_scope: str,
    family: str,
    subtype: str,
    metrics: dict[str, Any],
    family_metrics: dict[str, Any],
) -> str:
    if decision_scope == "family":
        if family == "bottom_base_volume_attack_reference":
            return "keep_as_bottom_base_volume_attack_reference_not_previous_high"
        if family == "descending_resistance_volume_breakout_proxy":
            return "keep_separate_research_surface_line_definition_differs"
        return "keep_broad_neckline_surface_until_subtypes_prove_separation"
    if metrics["retest_mature_sample_size"] < MIN_RETEST_MATURE_FOR_CANDIDATE:
        return "insufficient_evidence_for_separate_model"
    family_win = family_metrics["retest_win_rate_pct"]
    family_avg = family_metrics["retest_avg_return_pct"]
    subtype_win_advantage = metrics["retest_win_rate_pct"] - family_win
    subtype_avg_advantage = metrics["retest_avg_return_pct"] - family_avg
    if subtype_win_advantage >= 8.0 and subtype_avg_advantage >= 1.0:
        return "candidate_subtype_for_further_review"
    return "do_not_split_yet_keep_family_surface"


def next_action(
    decision_scope: str,
    family: str,
    subtype: str,
    metrics: dict[str, Any],
    split: str,
    entry: str,
) -> str:
    if entry == "insufficient_retest_sample":
        return "expand_sample_or_drop_subtype_before_model_discussion"
    if family == "bottom_base_volume_attack_reference" and subtype == "low_position_base_attack":
        return "prioritize_low_position_base_volume_attack_retest_grid"
    if family == "bottom_base_volume_attack_reference" and subtype == "wide_base_review":
        return "review_whether_wide_base_conflicts_with_contracted_base_semantics"
    if family == "bottom_base_volume_attack_reference" and subtype == "base_attack_position_review":
        return "do_not_use_as_volume_range_definition_without_position_gate"
    if family == "structured_neckline_volume_breakout_proxy" and "insufficient" in split:
        return "do_not_promote_double_or_specific_neckline_subtype_yet"
    if family == "structured_neckline_volume_breakout_proxy":
        return "continue_broad_neckline_retest_research_before_splitting_w_triple_other"
    if family == "descending_resistance_volume_breakout_proxy":
        return "continue_as_separate_descending_resistance_retest_research"
    if metrics["retest_mature_sample_size"] < MIN_RETEST_MATURE_FOR_CANDIDATE:
        return "expand_sample_before_next_decision"
    if decision_scope == "family":
        return "use_as_directional_research_only"
    return "review_chart_quality_before_any_promotion"


def row_for(
    detail: pd.DataFrame,
    decision_scope: str,
    family: str,
    subtype: str,
    family_metrics: dict[str, Any],
    generated_at: str,
) -> dict[str, str]:
    metrics = metric_group(detail, family, subtype)
    quality = sample_quality(metrics)
    entry = entry_decision(metrics)
    split = split_decision(decision_scope, family, subtype, metrics, family_metrics)
    action = next_action(decision_scope, family, subtype, metrics, split, entry)
    row = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "decision_scope": decision_scope,
        "event_family_id": family,
        "pattern_subtype": subtype,
        "sample_quality": quality,
        "entry_decision": entry,
        "split_decision": split,
        "next_action": action,
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    for key in [
        "direct_sample_size",
        "direct_mature_sample_size",
        "retest_signal_sample_size",
        "retest_mature_sample_size",
        "retest_not_found_count",
        "retest_found_but_no_attack_count",
        "retest_broken_count",
    ]:
        row[key] = str(metrics[key])
    for key in [
        "direct_win_rate_pct",
        "direct_avg_return_pct",
        "direct_median_return_pct",
        "retest_trigger_rate_pct",
        "retest_win_rate_pct",
        "retest_avg_return_pct",
        "retest_median_return_pct",
        "win_rate_lift_pct",
        "avg_return_lift_pct",
    ]:
        row[key] = metric_text(metrics[key])
    return row


def build_audit(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    family_metrics_by_id: dict[str, dict[str, Any]] = {}
    families = sorted(detail["event_family_id"].astype(str).unique())
    for family in families:
        family_metrics_by_id[family] = metric_group(detail, family, PATTERN_ALL)
        rows.append(row_for(detail, "family", family, PATTERN_ALL, family_metrics_by_id[family], generated_at))
    for family in families:
        subtypes = sorted(detail[detail["event_family_id"].astype(str).eq(family)]["pattern_subtype"].astype(str).unique())
        for subtype in subtypes:
            rows.append(row_for(detail, "subtype", family, subtype, family_metrics_by_id[family], generated_at))
    audit = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in audit.columns:
            audit[column] = ""
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in audit: {forbidden}")
    return audit[OUTPUT_COLUMNS].sort_values(["decision_scope", "event_family_id", "pattern_subtype"]).reset_index(drop=True)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    family = audit[audit["decision_scope"].eq("family")]
    subtype = audit[audit["decision_scope"].eq("subtype")]
    priority = subtype[subtype["entry_decision"].eq("prioritize_retest_confirmation_research")]
    lines = [
        "# Breakout Family Model Decision Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        "- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Decision Summary",
        "",
        "- Primary research direction: keep testing `retest_hold_then_attack_next_open`; retest-not-broken then renewed attack is stronger than direct breakout in most reviewable families.",
        "- Model split direction: do not split W-bottom / triple-bottom / other neckline subtypes yet. The current evidence supports a broad structured-neckline research surface first.",
        "- Volume model meaning: `bottom_base_volume_attack_reference` is bottom/base volume attack after contracted consolidation; it is not a previous-high model definition.",
        "- Volume range breakout research direction: future `volume_range_breakout` research should prioritize `low_position_base_attack`; `base_attack_position_review` is only a broad review bucket and must not define the model because it lacks a low-position gate.",
        "- Production status: all rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "",
        "## Family-Level Decisions",
        "",
        *markdown_table(
            family,
            [
                "event_family_id",
                "direct_win_rate_pct",
                "retest_win_rate_pct",
                "win_rate_lift_pct",
                "retest_trigger_rate_pct",
                "entry_decision",
                "split_decision",
                "next_action",
            ],
        ),
        "",
        "## Subtype-Level Decisions",
        "",
        *markdown_table(
            subtype,
            [
                "event_family_id",
                "pattern_subtype",
                "direct_sample_size",
                "retest_mature_sample_size",
                "direct_win_rate_pct",
                "retest_win_rate_pct",
                "win_rate_lift_pct",
                "sample_quality",
                "entry_decision",
                "split_decision",
                "next_action",
            ],
        ),
        "",
        "## Prioritized Follow-Up Rows",
        "",
        *markdown_table(
            priority,
            [
                "event_family_id",
                "pattern_subtype",
                "retest_mature_sample_size",
                "retest_win_rate_pct",
                "retest_avg_return_pct",
                "win_rate_lift_pct",
                "next_action",
            ],
        ),
        "",
        "## Interpretation",
        "",
        "The practical next step is not production promotion. It is a second research pass focused on retest-confirmed entries, with subtype splitting treated as unproven until a broader replay and chart-quality review show stable separation.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = read_source_detail()
    audit = build_audit(detail, generated_at)
    write_csv(audit, LATEST_CSV)
    write_csv(audit, HISTORY_CSV)
    write_markdown(audit, generated_at)
    print(f"wrote {LATEST_CSV} rows={len(audit)}")
    print(f"wrote {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
