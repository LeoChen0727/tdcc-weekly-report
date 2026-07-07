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

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
LATEST_MATRIX_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_condition_matrix_latest.csv"
LATEST_MATRIX_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_condition_matrix_latest.md"
HISTORY_MATRIX_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_condition_matrix.csv"

RESEARCH_ID = "volume_range_breakout_v2_condition_matrix"
ARTIFACT_VERSION = "volume_range_breakout_v2_condition_matrix_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

RETURN_KEY = "return_pct"
MIN_REVIEWABLE_SAMPLE = 300
MIN_THIN_SAMPLE = 100

MATRIX_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "matrix_family",
    "condition_set_id",
    "condition_set_label",
    "condition_timing",
    "promotion_guard",
    "high_window_days",
    "high_window_gate",
    "low_base_gate",
    "consolidation_gate",
    "limit_up_gate",
    "volume_gate",
    "risk_gate",
    "follow_through_gate",
    "baseline_sample_size",
    "sample_size",
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
    "trim_sample_size",
    "trim_avg_return_pct",
    "trim_median_return_pct",
    "anomaly_count",
    "sample_status",
    "win_rate_delta_pct",
    "loss_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
    "candidate_interpretation",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class ConditionSet:
    matrix_family: str
    condition_set_id: str
    condition_set_label: str
    condition_timing: str
    promotion_guard: str
    high_window_days: str
    high_window_gate: str
    low_base_gate: str
    consolidation_gate: str
    limit_up_gate: str
    volume_gate: str
    risk_gate: str
    follow_through_gate: str
    note: str


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


def pct_round(value: float, digits: int = 4) -> float | str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return round(float(value), digits)


def false_text() -> str:
    return "False"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def prepare_detail() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        raise SystemExit("ERROR: semantic audit detail is empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: source detail must come from volume_range_breakout_v2_semantic_audit")
    if not set(detail.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain research-only approved_for_daily=False")
    if detail.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        raise SystemExit("ERROR: source detail must be deduped by source_event_key before matrix testing")

    numeric_columns = [
        "return_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
    ]
    for col in numeric_columns:
        detail[col] = pd.to_numeric(detail.get(col, ""), errors="coerce")
    for col in [
        "high_breakout_20d_met",
        "high_breakout_40d_met",
        "high_breakout_60d_met",
        "consolidation_type",
        "limit_up_like",
        "risk_type",
        "follow_through_type",
        "anomaly_flag",
    ]:
        if col not in detail.columns:
            detail[col] = ""
    return detail


def build_condition_sets() -> list[ConditionSet]:
    rows = [
        ConditionSet(
            matrix_family="baseline",
            condition_set_id="baseline_all_dedup",
            condition_set_label="Current deduped mature formal operation sample",
            condition_timing="baseline_reference",
            promotion_guard="baseline_not_a_new_gate",
            high_window_days="",
            high_window_gate="current_source_events",
            low_base_gate="none",
            consolidation_gate="none",
            limit_up_gate="none",
            volume_gate="none",
            risk_gate="none",
            follow_through_gate="none",
            note="baseline uses the semantic audit deduped formal operation sample",
        )
    ]
    for window in [20, 40, 60]:
        prefix = f"prev{window}"
        high_gate = f"close >= previous {window}d high + 2pct"
        rows.extend(
            [
                ConditionSet(
                    matrix_family="high_window_only",
                    condition_set_id=f"{prefix}_high_only",
                    condition_set_label=f"{window}d previous-high breakout only",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="tests whether longer breakout windows improve the existing event sample",
                ),
                ConditionSet(
                    matrix_family="lock_limit_filter",
                    condition_set_id=f"{prefix}_high_not_locked_limit_up",
                    condition_set_label=f"{window}d breakout excluding locked-limit-up-like rows",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="limit_up_like=False",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="tests whether the locked-limit-up subgroup is dragging the sample",
                ),
                ConditionSet(
                    matrix_family="low_base_proxy",
                    condition_set_id=f"{prefix}_high_off60_le50_range60_le45",
                    condition_set_label=f"{window}d breakout with moderate 60d base proxy",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="off_60d_low_pct<=50 and range_width_60_pct<=45",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="low/base proxy; should not be promoted unless it explains payoff",
                ),
                ConditionSet(
                    matrix_family="low_base_proxy",
                    condition_set_id=f"{prefix}_high_off60_le40_range60_le35",
                    condition_set_label=f"{window}d breakout with tight 60d base proxy",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="off_60d_low_pct<=40 and range_width_60_pct<=35",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="stricter low/base proxy; tracks user intent but must prove payoff",
                ),
                ConditionSet(
                    matrix_family="consolidation_proxy",
                    condition_set_id=f"{prefix}_high_consolidated_any",
                    condition_set_label=f"{window}d breakout with any consolidation label",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="short_or_long_consolidation",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="tests whether the existing consolidation label matches better payoff",
                ),
                ConditionSet(
                    matrix_family="consolidation_proxy",
                    condition_set_id=f"{prefix}_high_short_consolidation",
                    condition_set_label=f"{window}d breakout with short consolidation label",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="short_consolidation",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="separates short consolidation from long consolidation",
                ),
                ConditionSet(
                    matrix_family="combined_source_signal",
                    condition_set_id=f"{prefix}_high_not_locked_off60_le50_range60_le45",
                    condition_set_label=f"{window}d breakout, not locked, moderate base proxy",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="off_60d_low_pct<=50 and range_width_60_pct<=45",
                    consolidation_gate="none",
                    limit_up_gate="limit_up_like=False",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="combined source-signal gate candidate, still research-only",
                ),
                ConditionSet(
                    matrix_family="volume_shape",
                    condition_set_id=f"{prefix}_high_volume_ratio_2_to_6",
                    condition_set_label=f"{window}d breakout with volume ratio 2 to 6",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="2<=volume_ratio<=6",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="checks whether extreme volume is hurting payoff",
                ),
                ConditionSet(
                    matrix_family="volume_shape",
                    condition_set_id=f"{prefix}_high_signal_return_lt_9_8",
                    condition_set_label=f"{window}d breakout with signal-day return below 9.8pct",
                    condition_timing="signal_close_available",
                    promotion_guard="source_signal_only_needs_full_raw_backtest",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="limit_up_like mostly excluded by return cap",
                    volume_gate="signal_return_1d_pct<9.8",
                    risk_gate="none",
                    follow_through_gate="none",
                    note="tests a non-lock-limit style proxy without using future data",
                ),
                ConditionSet(
                    matrix_family="confirmation_timing",
                    condition_set_id=f"{prefix}_high_next_day_continuation",
                    condition_set_label=f"{window}d breakout with next-day continuation",
                    condition_timing="confirmation_close_available_needs_contract_review",
                    promotion_guard="confirmation_timing_needs_operation_contract_review",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="next_day_continuation",
                    note="can explain payoff, but cannot be used before its confirmation timing is formalized",
                ),
                ConditionSet(
                    matrix_family="confirmation_timing",
                    condition_set_id=f"{prefix}_high_pullback_5ma_or_10ma",
                    condition_set_label=f"{window}d breakout with 5MA/10MA pullback follow-through",
                    condition_timing="confirmation_close_available_needs_contract_review",
                    promotion_guard="confirmation_timing_needs_operation_contract_review",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="pullback_5ma_or_10ma",
                    note="diagnoses follow-through behavior; not a source-day gate",
                ),
                ConditionSet(
                    matrix_family="diagnostic_only",
                    condition_set_id=f"{prefix}_high_exclude_breakout_failure",
                    condition_set_label=f"{window}d breakout excluding breakout_failure risk label",
                    condition_timing="research_diagnostic_requires_timing_audit",
                    promotion_guard="diagnostic_only_not_promotion_evidence",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="none",
                    volume_gate="none",
                    risk_gate="risk_type!=breakout_failure",
                    follow_through_gate="none",
                    note="risk label is useful for diagnosis but must not become a gate without timing proof",
                ),
                ConditionSet(
                    matrix_family="combined_confirmation",
                    condition_set_id=f"{prefix}_high_not_locked_next_day_continuation",
                    condition_set_label=f"{window}d breakout, not locked, next-day continuation",
                    condition_timing="confirmation_close_available_needs_contract_review",
                    promotion_guard="confirmation_timing_needs_operation_contract_review",
                    high_window_days=str(window),
                    high_window_gate=high_gate,
                    low_base_gate="none",
                    consolidation_gate="none",
                    limit_up_gate="limit_up_like=False",
                    volume_gate="none",
                    risk_gate="none",
                    follow_through_gate="next_day_continuation",
                    note="tests whether continuation explains payoff after removing lock-limit rows",
                ),
            ]
        )
    return rows


def condition_mask(detail: pd.DataFrame, condition: ConditionSet) -> pd.Series:
    mask = pd.Series(True, index=detail.index)
    if condition.high_window_days:
        flag = f"high_breakout_{condition.high_window_days}d_met"
        mask &= detail[flag].astype(str).eq("True")
    if "limit_up_like=False" in condition.limit_up_gate:
        mask &= detail["limit_up_like"].astype(str).eq("False")
    if "off_60d_low_pct<=50" in condition.low_base_gate:
        mask &= detail["off_60d_low_pct"].le(50)
    if "range_width_60_pct<=45" in condition.low_base_gate:
        mask &= detail["range_width_60_pct"].le(45)
    if "off_60d_low_pct<=40" in condition.low_base_gate:
        mask &= detail["off_60d_low_pct"].le(40)
    if "range_width_60_pct<=35" in condition.low_base_gate:
        mask &= detail["range_width_60_pct"].le(35)
    if condition.consolidation_gate == "short_or_long_consolidation":
        mask &= detail["consolidation_type"].isin(["short_consolidation", "long_consolidation"])
    if condition.consolidation_gate == "short_consolidation":
        mask &= detail["consolidation_type"].eq("short_consolidation")
    if condition.volume_gate == "2<=volume_ratio<=6":
        mask &= detail["volume_ratio"].between(2, 6, inclusive="both")
    if condition.volume_gate == "signal_return_1d_pct<9.8":
        mask &= detail["signal_return_1d_pct"].lt(9.8)
    if condition.follow_through_gate == "next_day_continuation":
        mask &= detail["follow_through_type"].eq("next_day_continuation")
    if condition.follow_through_gate == "pullback_5ma_or_10ma":
        mask &= detail["follow_through_type"].isin(["pullback_5ma", "pullback_10ma"])
    if condition.risk_gate == "risk_type!=breakout_failure":
        mask &= ~detail["risk_type"].eq("breakout_failure")
    return mask.fillna(False)


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get(RETURN_KEY, pd.Series(dtype=float)), errors="coerce").dropna()
    sample_size = int(len(returns))
    if sample_size == 0:
        return {
            "sample_size": 0,
            "win_count": 0,
            "neutral_count": 0,
            "loss_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "loss_rate_pct": "",
            "avg_return_pct": "",
            "median_return_pct": "",
            "p10_return_pct": "",
            "p90_return_pct": "",
            "min_return_pct": "",
            "max_return_pct": "",
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
    return {
        "sample_size": sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100.0, 2),
        "loss_rate_pct": pct_round(loss_count / sample_size * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
    }


def sample_status(sample_size: int) -> str:
    if sample_size >= MIN_REVIEWABLE_SAMPLE:
        return "reviewable_sample"
    if sample_size >= MIN_THIN_SAMPLE:
        return "thin_sample"
    return "insufficient_sample"


def interpretation(condition: ConditionSet, row: dict[str, Any]) -> str:
    if condition.matrix_family == "baseline":
        return "baseline_reference"
    if condition.promotion_guard == "diagnostic_only_not_promotion_evidence":
        return "diagnostic_only_not_promotion_evidence"
    sample_size = int(row["sample_size"])
    if sample_size < MIN_THIN_SAMPLE:
        return "insufficient_sample_do_not_use"
    avg_delta = float(row["avg_return_delta_pct"] or 0.0)
    median = float(row["median_return_pct"] or 0.0)
    win_delta = float(row["win_rate_delta_pct"] or 0.0)
    if sample_size >= MIN_REVIEWABLE_SAMPLE and avg_delta >= 2.0 and median >= 0 and win_delta >= 8.0:
        if "confirmation" in condition.promotion_guard:
            return "interesting_confirmation_timing_needs_contract_review"
        return "interesting_source_signal_candidate_needs_full_raw_backtest"
    if avg_delta < 0 and median < 0:
        return "weaker_than_baseline_do_not_promote_as_gate"
    return "mixed_result_research_only"


def row_for_condition(
    condition: ConditionSet,
    detail: pd.DataFrame,
    generated_at: str,
    baseline_metrics: dict[str, Any],
    source_artifact_version: str,
) -> dict[str, Any]:
    mask = condition_mask(detail, condition)
    part = detail[mask]
    metrics = return_metrics(part)
    trim_part = part[part["anomaly_flag"].astype(str).eq("none")]
    trim_metrics = return_metrics(trim_part)
    baseline_sample_size = int(baseline_metrics["sample_size"])
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_artifact_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "matrix_family": condition.matrix_family,
        "condition_set_id": condition.condition_set_id,
        "condition_set_label": condition.condition_set_label,
        "condition_timing": condition.condition_timing,
        "promotion_guard": condition.promotion_guard,
        "high_window_days": condition.high_window_days,
        "high_window_gate": condition.high_window_gate,
        "low_base_gate": condition.low_base_gate,
        "consolidation_gate": condition.consolidation_gate,
        "limit_up_gate": condition.limit_up_gate,
        "volume_gate": condition.volume_gate,
        "risk_gate": condition.risk_gate,
        "follow_through_gate": condition.follow_through_gate,
        "baseline_sample_size": baseline_sample_size,
        "coverage_pct": pct_round(metrics["sample_size"] / baseline_sample_size * 100.0 if baseline_sample_size else math.nan, 2),
        "trim_sample_size": trim_metrics["sample_size"],
        "trim_avg_return_pct": trim_metrics["avg_return_pct"],
        "trim_median_return_pct": trim_metrics["median_return_pct"],
        "anomaly_count": int(part["anomaly_flag"].astype(str).ne("none").sum()) if not part.empty else 0,
        "sample_status": sample_status(int(metrics["sample_size"])),
        "note": condition.note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    for key in ["win_rate_pct", "loss_rate_pct", "avg_return_pct", "median_return_pct"]:
        base_value = baseline_metrics.get(key, "")
        value = row.get(key, "")
        delta_key = key.replace("_pct", "_delta_pct")
        row[delta_key] = pct_round(float(value) - float(base_value)) if value != "" and base_value != "" else ""
    row["candidate_interpretation"] = interpretation(condition, row)
    return row


def build_matrix(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_artifact_version = safe_str(detail["artifact_version"].iloc[0]) if "artifact_version" in detail.columns else ""
    baseline_condition = build_condition_sets()[0]
    baseline = return_metrics(detail[condition_mask(detail, baseline_condition)])
    rows = [
        row_for_condition(condition, detail, generated_at, baseline, source_artifact_version)
        for condition in build_condition_sets()
    ]
    return pd.DataFrame(rows)


def write_markdown(matrix: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    baseline = matrix[matrix["matrix_family"].eq("baseline")]
    high_only = matrix[matrix["matrix_family"].eq("high_window_only")]
    low_base = matrix[matrix["matrix_family"].eq("low_base_proxy")]
    source_signal = matrix[
        matrix["promotion_guard"].eq("source_signal_only_needs_full_raw_backtest")
        & matrix["sample_status"].eq("reviewable_sample")
    ].sort_values(["avg_return_pct", "win_rate_pct"], ascending=[False, False])
    confirmation = matrix[
        matrix["promotion_guard"].eq("confirmation_timing_needs_operation_contract_review")
    ].sort_values(["avg_return_pct", "win_rate_pct"], ascending=[False, False])
    diagnostics = matrix[matrix["matrix_family"].eq("diagnostic_only")]

    lines = [
        "# Volume Range Breakout V2 Condition Matrix",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This matrix is research-only and does not change `stock_model_contract_registry.csv`.",
        "- The matrix consumes the semantic-audit detail artifact; it is not a full raw-market producer rerun.",
        "- 20/40/60 previous-high windows are compared under the same deduped sample and operation return basis.",
        "- Low/base proxies are tested as evidence, not assumed to be correct gates.",
        "- Confirmation-timing and diagnostic rows require operation-contract review before any promotion discussion.",
        "",
        "## Baseline",
        "",
        *md_table(
            baseline,
            [
                "condition_set_id",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
            ],
            limit=5,
        ),
        "",
        "## 20/40/60 High-Window Only",
        "",
        *md_table(
            high_only,
            [
                "condition_set_id",
                "sample_size",
                "coverage_pct",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
            ],
            limit=10,
        ),
        "",
        "## Low/Base Proxy Rows",
        "",
        *md_table(
            low_base,
            [
                "condition_set_id",
                "sample_size",
                "coverage_pct",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_interpretation",
            ],
            limit=20,
        ),
        "",
        "## Best Reviewable Source-Signal Rows",
        "",
        *md_table(
            source_signal,
            [
                "condition_set_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_interpretation",
            ],
            limit=15,
        ),
        "",
        "## Confirmation-Timing Rows",
        "",
        *md_table(
            confirmation,
            [
                "condition_set_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_interpretation",
            ],
            limit=15,
        ),
        "",
        "## Diagnostic-Only Rows",
        "",
        *md_table(
            diagnostics,
            [
                "condition_set_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_interpretation",
            ],
            limit=10,
        ),
        "",
        "## Outputs",
        "",
        f"- matrix_csv: `{LATEST_MATRIX_CSV.as_posix()}`",
        f"- history_csv: `{HISTORY_MATRIX_CSV.as_posix()}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    detail = prepare_detail()
    matrix = build_matrix(detail, generated_at)
    write_csv(matrix, LATEST_MATRIX_CSV, MATRIX_COLUMNS)
    write_csv(matrix, HISTORY_MATRIX_CSV, MATRIX_COLUMNS)
    write_markdown(matrix, LATEST_MATRIX_MD)
    print(f"Saved: {LATEST_MATRIX_CSV} rows={len(matrix)}")
    print(f"Saved: {LATEST_MATRIX_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
