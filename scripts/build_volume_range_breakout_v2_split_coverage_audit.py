from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import math

import pandas as pd

from build_volume_range_breakout_v2_lowbase_horizon_audit import (
    ADVISORY_STATUS,
    MODEL_ID,
    PRODUCTION_READINESS,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    load_source_detail,
    mark_non_overlap,
    now_text,
    pct_round,
    prepare_source,
    safe_str,
    write_csv,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_coverage_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_coverage_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_split_coverage_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_split_coverage_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_split_coverage_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_split_coverage_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_split_coverage_audit_20260709"
MOMENTUM_BREAKOUT_THRESHOLD_PCT = 2.0


@dataclass(frozen=True)
class SplitBucket:
    bucket_id: str
    bucket_label: str
    bucket_definition: str
    priority: int


SPLIT_BUCKETS = [
    SplitBucket(
        "momentum_breakout_candidate",
        "strong momentum volume breakout candidate",
        "high_breakout_60d_met=True and range_width_40_pct>40 and breakout_over_prev60_pct>=2",
        1,
    ),
    SplitBucket(
        "lowbase_consolidation_candidate",
        "low-base consolidation volume breakout candidate",
        "high_breakout_60d_met=True and off_120d_low_pct<=40 and range_width_40_pct<=40",
        2,
    ),
    SplitBucket(
        "prev60_residual_research_pool",
        "60d breakout residual research pool",
        "high_breakout_60d_met=True and not classified into the two v2 candidates",
        3,
    ),
    SplitBucket(
        "legacy_non_prev60_residual",
        "legacy v1 residual that does not meet the 60d breakout direction",
        "high_breakout_60d_met=False",
        4,
    ),
]
BUCKET_BY_ID = {bucket.bucket_id: bucket for bucket in SPLIT_BUCKETS}
OVERLAP_POLICIES = ["all_source_events", "same_stock_non_overlap"]
ANOMALY_POLICIES = ["include_extreme_review", "exclude_extreme_review"]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "bucket_id",
    "bucket_label",
    "bucket_definition",
    "residual_reason",
    "overlap_policy",
    "anomaly_policy",
    "total_source_event_count",
    "source_event_count",
    "stock_count",
    "source_coverage_pct",
    "metric_event_count",
    "sample_size",
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
    "high_return_ge20_count",
    "high_return_ge20_rate_pct",
    "loss_le_minus5_count",
    "loss_le_minus5_rate_pct",
    "data_quality_exception_count",
    "same_stock_overlap_suppressed_count",
    "sample_status",
    "split_gate_status",
    "decision_hint",
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
    "data_quality_flag",
    "bucket_id",
    "bucket_label",
    "bucket_definition",
    "residual_reason",
    "bucket_match_count",
    "candidate_bucket_match_count",
    "momentum_breakout_candidate_flag",
    "lowbase_consolidation_candidate_flag",
    "prev60_residual_research_pool_flag",
    "legacy_non_prev60_residual_flag",
    "high_breakout_60d_met",
    "breakout_over_prev60_pct",
    "range_width_40_pct",
    "off_120d_low_pct",
    "signal_close",
    "previous_60d_high",
    "previous_60d_low",
    "previous_120d_high",
    "previous_120d_low",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "volume_ratio",
    "signal_return_1d_pct",
    "anomaly_flag",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def false_text() -> str:
    return "False"


def boolish(value: Any) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def numeric(value: Any) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return math.nan
    return number if not math.isnan(number) and not math.isinf(number) else math.nan


def outcome(return_pct: Any) -> str:
    value = numeric(return_pct)
    if math.isnan(value):
        return ""
    if value > 0:
        return "win"
    if value < 0:
        return "loss"
    return "neutral"


def data_quality_flag(row: pd.Series) -> str:
    anomaly = safe_str(row.get("anomaly_flag")).lower()
    ret = numeric(row.get("return_pct"))
    if anomaly and anomaly != "none":
        return "extreme_return_abs_ge80_review"
    if not math.isnan(ret) and abs(ret) >= 80:
        return "extreme_return_abs_ge80_review"
    return "ok"


def classify_residual_reason(row: pd.Series, high60: bool, momentum: bool, lowbase: bool) -> str:
    if momentum:
        return "selected_momentum_breakout_candidate"
    if lowbase:
        return "selected_lowbase_consolidation_candidate"
    if not high60:
        return "not_prev60_high"
    width40 = numeric(row.get("range_width_40_pct"))
    off120 = numeric(row.get("off_120d_low_pct"))
    breakout = numeric(row.get("breakout_over_prev60_pct"))
    if math.isnan(width40):
        return "prev60_width40_missing"
    if width40 > 40 and not math.isnan(breakout) and breakout < MOMENTUM_BREAKOUT_THRESHOLD_PCT:
        return "wide_breakout_below_2pct"
    if width40 <= 40 and math.isnan(off120):
        return "consolidated_but_off120_missing"
    if width40 <= 40 and off120 > 40:
        return "consolidated_but_not_lowbase_off120_gt40"
    return "prev60_other_unassigned"


def classify_bucket(row: pd.Series) -> dict[str, Any]:
    high60 = boolish(row.get("high_breakout_60d_met"))
    width40 = numeric(row.get("range_width_40_pct"))
    off120 = numeric(row.get("off_120d_low_pct"))
    breakout = numeric(row.get("breakout_over_prev60_pct"))
    momentum = (
        high60
        and not math.isnan(width40)
        and not math.isnan(breakout)
        and width40 > 40
        and breakout >= MOMENTUM_BREAKOUT_THRESHOLD_PCT
    )
    lowbase = high60 and not math.isnan(width40) and not math.isnan(off120) and width40 <= 40 and off120 <= 40
    if momentum:
        bucket_id = "momentum_breakout_candidate"
    elif lowbase:
        bucket_id = "lowbase_consolidation_candidate"
    elif high60:
        bucket_id = "prev60_residual_research_pool"
    else:
        bucket_id = "legacy_non_prev60_residual"
    residual_reason = classify_residual_reason(row, high60, momentum, lowbase)
    bucket = BUCKET_BY_ID[bucket_id]
    return {
        "bucket_id": bucket.bucket_id,
        "bucket_label": bucket.bucket_label,
        "bucket_definition": bucket.bucket_definition,
        "residual_reason": residual_reason,
        "bucket_match_count": 1,
        "candidate_bucket_match_count": int(momentum) + int(lowbase),
        "momentum_breakout_candidate_flag": str(momentum),
        "lowbase_consolidation_candidate_flag": str(lowbase),
        "prev60_residual_research_pool_flag": str(bucket_id == "prev60_residual_research_pool"),
        "legacy_non_prev60_residual_flag": str(bucket_id == "legacy_non_prev60_residual"),
    }


def recompute_breakout_over_prev60_pct(frame: pd.DataFrame) -> pd.Series:
    signal_close = pd.to_numeric(frame.get("signal_close", ""), errors="coerce")
    previous_high = pd.to_numeric(frame.get("previous_60d_high", ""), errors="coerce")
    source_breakout = pd.to_numeric(frame.get("breakout_over_prev60_pct", ""), errors="coerce")
    recomputed = (signal_close / previous_high.replace(0, pd.NA) - 1.0) * 100.0
    return source_breakout.where(source_breakout.notna(), recomputed)


def build_detail(source: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    work = prepare_source(source, source_version, generated_at)
    work["breakout_over_prev60_pct"] = recompute_breakout_over_prev60_pct(work)
    for col in ["return_pct", "range_width_40_pct", "off_120d_low_pct", "breakout_over_prev60_pct"]:
        work[col] = pd.to_numeric(work.get(col, ""), errors="coerce")

    classified = work.apply(classify_bucket, axis=1, result_type="expand")
    out = pd.concat([work.reset_index(drop=True), classified.reset_index(drop=True)], axis=1)
    out["research_id"] = RESEARCH_ID
    out["artifact_version"] = ARTIFACT_VERSION
    out["source_research_id"] = SOURCE_RESEARCH_ID
    out["source_artifact_version"] = source_version
    out["advisory_status"] = ADVISORY_STATUS
    out["model_id"] = MODEL_ID
    out["return_outcome"] = out["return_pct"].map(outcome)
    out["data_quality_flag"] = out.apply(data_quality_flag, axis=1)
    out["approved_for_daily"] = false_text()
    out["production_readiness"] = PRODUCTION_READINESS
    out["generated_at"] = generated_at
    for col in [
        "return_pct",
        "breakout_over_prev60_pct",
        "range_width_40_pct",
        "off_120d_low_pct",
        "signal_close",
        "previous_60d_high",
        "previous_60d_low",
        "previous_120d_high",
        "previous_120d_low",
        "volume_ratio",
        "signal_return_1d_pct",
    ]:
        out[col] = out[col].map(pct_round)
    return out


def metric_part(part: pd.DataFrame, overlap_policy: str, anomaly_policy: str) -> tuple[pd.DataFrame, int, int]:
    work = part.copy()
    if anomaly_policy == "exclude_extreme_review":
        before = len(work)
        work = work[work["data_quality_flag"].astype(str).eq("ok")].copy()
        exception_count = before - len(work)
    else:
        exception_count = int(work["data_quality_flag"].astype(str).ne("ok").sum())
    if overlap_policy == "same_stock_non_overlap":
        marked = mark_non_overlap(work)
        metric = marked[marked["_non_overlap"]].copy() if not marked.empty else marked
        suppressed = len(work) - len(metric)
        return metric, exception_count, suppressed
    return work, exception_count, 0


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    n = int(len(returns))
    if n == 0:
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
            "high_return_ge20_count": 0,
            "high_return_ge20_rate_pct": "",
            "loss_le_minus5_count": 0,
            "loss_le_minus5_rate_pct": "",
        }
    win = int((returns > 0).sum())
    neutral = int((returns == 0).sum())
    loss = int((returns < 0).sum())
    high20 = int(returns.ge(20).sum())
    loss5 = int(returns.le(-5).sum())
    return {
        "sample_size": n,
        "win_count": win,
        "neutral_count": neutral,
        "loss_count": loss,
        "win_rate_pct": pct_round(win / n * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral / n * 100.0, 2),
        "loss_rate_pct": pct_round(loss / n * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
        "high_return_ge20_count": high20,
        "high_return_ge20_rate_pct": pct_round(high20 / n * 100.0, 2),
        "loss_le_minus5_count": loss5,
        "loss_le_minus5_rate_pct": pct_round(loss5 / n * 100.0, 2),
    }


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    return "thin_sample"


def split_gate_status(metrics: dict[str, Any]) -> str:
    try:
        win_rate = float(metrics["win_rate_pct"])
        avg_return = float(metrics["avg_return_pct"])
    except (TypeError, ValueError):
        return "insufficient_sample"
    if win_rate >= 60.0 and avg_return > 0:
        return "passes_return_and_win_gate_research_only"
    return "fails_return_or_win_gate"


def decision_hint(row_type: str, bucket_id: str, residual_reason: str, metrics: dict[str, Any]) -> str:
    if bucket_id == "momentum_breakout_candidate":
        return "primary_v2_candidate_continue_exit_and_raw_producer_research"
    if bucket_id == "lowbase_consolidation_candidate":
        return "semantic_candidate_but_not_performance_ready"
    if row_type == "residual_reason_coverage" and residual_reason == "consolidated_but_off120_missing":
        return "audit_data_coverage_before_model_discussion"
    if bucket_id == "prev60_residual_research_pool":
        return "research_pool_only_do_feature_audit_before_model_split"
    if bucket_id == "legacy_non_prev60_residual":
        return "low_priority_legacy_baseline_only"
    if split_gate_status(metrics) == "passes_return_and_win_gate_research_only":
        return "research_only_candidate_needs_semantic_separation"
    return "research_only_diagnostic"


def summary_row(
    detail: pd.DataFrame,
    source_version: str,
    generated_at: str,
    row_type: str,
    bucket_id: str,
    residual_reason: str,
    overlap_policy: str,
    anomaly_policy: str,
) -> dict[str, Any]:
    total = len(detail)
    bucket = BUCKET_BY_ID[bucket_id]
    source_part = detail[detail["bucket_id"].astype(str).eq(bucket_id)].copy()
    if row_type == "residual_reason_coverage":
        source_part = source_part[source_part["residual_reason"].astype(str).eq(residual_reason)].copy()
    metric, exception_count, suppressed = metric_part(source_part, overlap_policy, anomaly_policy)
    metrics = return_metrics(metric)
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "bucket_id": bucket.bucket_id,
        "bucket_label": bucket.bucket_label,
        "bucket_definition": bucket.bucket_definition,
        "residual_reason": residual_reason,
        "overlap_policy": overlap_policy,
        "anomaly_policy": anomaly_policy,
        "total_source_event_count": total,
        "source_event_count": len(source_part),
        "stock_count": int(source_part["stock_id"].astype(str).nunique()) if not source_part.empty else 0,
        "source_coverage_pct": pct_round(len(source_part) / total * 100.0, 2) if total else "",
        "metric_event_count": len(metric),
        "data_quality_exception_count": exception_count,
        "same_stock_overlap_suppressed_count": suppressed,
        "sample_status": sample_status(int(metrics["sample_size"])),
        "split_gate_status": split_gate_status(metrics),
        "decision_hint": decision_hint(row_type, bucket_id, residual_reason, metrics),
        "note": "Research-only split coverage on existing v1 source events; every source_event_key is assigned to exactly one bucket and production registry is not changed.",
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    return row


def build_summary(detail: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for bucket in SPLIT_BUCKETS:
        for overlap_policy in OVERLAP_POLICIES:
            for anomaly_policy in ANOMALY_POLICIES:
                rows.append(
                    summary_row(
                        detail,
                        source_version,
                        generated_at,
                        "split_bucket_coverage",
                        bucket.bucket_id,
                        "",
                        overlap_policy,
                        anomaly_policy,
                    )
                )
    residual = detail[detail["bucket_id"].astype(str).eq("prev60_residual_research_pool")]
    for residual_reason in sorted(set(residual["residual_reason"].astype(str))):
        for overlap_policy in OVERLAP_POLICIES:
            for anomaly_policy in ANOMALY_POLICIES:
                rows.append(
                    summary_row(
                        detail,
                        source_version,
                        generated_at,
                        "residual_reason_coverage",
                        "prev60_residual_research_pool",
                        residual_reason,
                        overlap_policy,
                        anomaly_policy,
                    )
                )
    return pd.DataFrame(rows)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["(empty)"]
    return df[columns].head(limit).copy().fillna("NA").to_markdown(index=False).splitlines()


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, path: Path) -> None:
    bucket_rows = summary[
        summary["row_type"].astype(str).eq("split_bucket_coverage")
        & summary["overlap_policy"].astype(str).eq("same_stock_non_overlap")
        & summary["anomaly_policy"].astype(str).eq("exclude_extreme_review")
    ].copy()
    reason_rows = summary[
        summary["row_type"].astype(str).eq("residual_reason_coverage")
        & summary["overlap_policy"].astype(str).eq("same_stock_non_overlap")
        & summary["anomaly_policy"].astype(str).eq("exclude_extreme_review")
    ].copy()
    detail_counts = detail["bucket_id"].value_counts().rename_axis("bucket_id").reset_index(name="detail_event_count")
    lines = [
        "# Volume Range Breakout V2 Split Coverage Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- Scope: research-only split coverage on existing v1 source events; this is not a production registry change.",
        "- Rule: every `source_event_key` must be assigned to exactly one split bucket.",
        "- Candidate buckets are mutually exclusive by explicit width/position rules, not by the legacy `consolidation_type` label.",
        "",
        "## Split Definitions",
        "",
        "- `momentum_breakout_candidate`: 60d breakout, `range_width_40_pct > 40`, and `breakout_over_prev60_pct >= 2`.",
        "- `lowbase_consolidation_candidate`: 60d breakout, `off_120d_low_pct <= 40`, and `range_width_40_pct <= 40`.",
        "- `prev60_residual_research_pool`: 60d breakout but not in the two candidate buckets.",
        "- `legacy_non_prev60_residual`: old v1 source events outside the new 60d breakout direction.",
        "",
        "## Detail Coverage",
        "",
        *markdown_table(detail_counts, ["bucket_id", "detail_event_count"], 20),
        "",
        "## Same-Stock Non-Overlap Metrics",
        "",
        *markdown_table(
            bucket_rows.sort_values(["bucket_id"]),
            [
                "bucket_id",
                "source_event_count",
                "stock_count",
                "source_coverage_pct",
                "metric_event_count",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "split_gate_status",
                "decision_hint",
            ],
            20,
        ),
        "",
        "## Prev60 Residual Reasons",
        "",
        *markdown_table(
            reason_rows.sort_values(["residual_reason"]),
            [
                "residual_reason",
                "source_event_count",
                "stock_count",
                "source_coverage_pct",
                "metric_event_count",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            20,
        ),
        "",
        "## Governance Notes",
        "",
        "- The sum of the two candidate buckets is intentionally not required to equal the old v1 source population.",
        "- The residual pool remains research-only until a feature audit proves a separate semantic edge.",
        "- Performance rows are diagnostic; they use current v1 operation returns and must not be treated as promotion evidence.",
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV}`",
        f"- history_summary_csv: `{HISTORY_SUMMARY_CSV}`",
        f"- history_detail_csv: `{HISTORY_DETAIL_CSV}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source, source_version = load_source_detail()
    detail = build_detail(source, source_version, generated_at)
    summary = build_summary(detail, source_version, generated_at)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_markdown(summary, detail, LATEST_MD)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    print(
        "built volume range breakout v2 split coverage audit "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
