from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_position_shape_matrix_detail_latest.csv"
)

LATEST_CONTRACT_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_candidate_bucket_contract_latest.csv"
)
LATEST_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_candidate_bucket_contract_detail_latest.csv"
)
LATEST_STRATIFICATION_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_candidate_bucket_contract_stratification_latest.csv"
)
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_candidate_bucket_contract_latest.md"

HISTORY_CONTRACT_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_candidate_bucket_contract.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_candidate_bucket_contract_detail.csv"
HISTORY_STRATIFICATION_CSV = (
    RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_candidate_bucket_contract_stratification.csv"
)

RESEARCH_ID = "volume_range_breakout_v2_candidate_bucket_contract"
ARTIFACT_VERSION = "volume_range_breakout_v2_candidate_bucket_contract_20260709"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_position_shape_matrix"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARENT_MODEL_ID = "volume_range_breakout"

CONFIRMATION_RULE_ID = "next_day_continuation_confirmed_close_only"
CONFIRMATION_RULE_ZH = (
    "訊號隔日收盤高於訊號日收盤，且收盤不低於訊號日最高價；"
    "資訊只在確認日收盤後成立，隔日開盤進場。"
)
ENTRY_RULE_ID = "confirmation_next_open"
ENTRY_RULE_ZH = "確認日收盤成立後，下一個交易日開盤進場。"
EXIT_POLICY_ID = "fixed_d15_close_with_23ema_close_stop"
EXIT_RULE_ID = "ema23_close_stop_or_fixed_15d_close"
EXIT_RULE_ZH = "確認後隔日開盤進場；若未觸發停損，固定第15個交易日收盤出場。"
STOP_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
STOP_RULE_ZH = "收盤連續4天低於MA20/EMA23較低者的4%，隔日開盤停損。"
BASE_SCOPE_ID = "d15_close_only_next_day_continuation_ma20_ema23_stop"
WIN_RATE_THRESHOLD_PCT = 60.0

CONTRACT_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "model_id",
    "model_zh",
    "candidate_condition_id",
    "candidate_condition_zh",
    "confirmation_rule_id",
    "confirmation_rule_zh",
    "entry_rule_id",
    "entry_rule_zh",
    "exit_policy_id",
    "exit_rule_id",
    "exit_rule_zh",
    "stop_rule_id",
    "stop_rule_zh",
    "base_metric_scope",
    "position_axis",
    "included_buckets",
    "sample_size",
    "valid_return_count",
    "invalid_return_count",
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
    "stop_exit_count",
    "stop_exit_rate_pct",
    "meets_win_return_metric",
    "sample_count_context",
    "production_registry_change",
    "membership_note",
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
    "parent_model_id",
    "model_id",
    "model_zh",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "planned_exit_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "holding_days",
    "stop_policy_id",
    "stop_rule_id",
    "stop_price",
    "stop_confirmed_days",
    "candidate_condition_id",
    "confirmation_rule_id",
    "entry_rule_id",
    "source_analysis_scope_id",
    "position_bucket_120d",
    "position_shape_bucket_120d",
    "shape_bucket",
    "breakout_over_prev60_pct",
    "volume_ratio",
    "signal_return_1d_pct",
    "range_width_20_pct",
    "range_width_60_pct",
    "off_60d_low_pct",
    "position_in_60d_range_pct",
    "off_120d_low_pct",
    "range_width_120_pct",
    "position_in_120d_range_pct",
    "off_240d_low_pct",
    "range_width_240_pct",
    "position_in_240d_range_pct",
    "consolidation_type",
    "follow_through_type",
    "limit_up_like",
    "low_base_loose_flag",
    "consolidated_any_flag",
    "hist_return_20d_pct",
    "hist_return_60d_pct",
    "dist_ema23_pct",
    "close_gt_ema23",
    "close_gt_ma20",
    "ma20_gt_ma60",
    "ma60_gt_ma120",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "return_valid",
    "invalid_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

STRATIFICATION_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "subject_type",
    "subject_id",
    "subject_zh",
    "condition_id",
    "condition_zh",
    "condition_expression",
    "condition_role",
    "baseline_sample_size",
    "sample_size",
    "valid_return_count",
    "invalid_return_count",
    "coverage_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_win_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "win_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
    "meets_win_return_metric",
    "sample_count_context",
    "decision_hint",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class ModelSpec:
    model_id: str
    model_zh: str
    candidate_condition_id: str
    candidate_condition_zh: str
    included_buckets: str
    mask: Callable[[pd.DataFrame], pd.Series]


@dataclass(frozen=True)
class SubjectSpec:
    subject_type: str
    subject_id: str
    subject_zh: str
    mask: Callable[[pd.DataFrame], pd.Series]


@dataclass(frozen=True)
class ConditionSpec:
    condition_id: str
    condition_zh: str
    expression: str
    mask: Callable[[pd.DataFrame], pd.Series]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required source: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(frame: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = frame.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def to_float(value: object) -> float:
    text = str(value).strip()
    if text == "":
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def bool_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "yes"})


def pct(value: float | int | None) -> str:
    if value is None:
        return ""
    try:
        parsed = float(value)
    except TypeError:
        return ""
    if math.isnan(parsed):
        return ""
    return str(round(parsed, 4))


def bool_text(value: bool) -> str:
    return "True" if value else "False"


def metric_row(source: pd.DataFrame) -> dict[str, object]:
    valid = source[source["return_valid"].astype(str).eq("True")]
    invalid = source[~source["return_valid"].astype(str).eq("True")]
    returns = pd.to_numeric(valid["return_pct"], errors="coerce").dropna()
    outcomes = valid["return_outcome"].astype(str)
    sample_size = len(source)
    valid_count = len(valid)
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    win_rate = win_count / valid_count * 100 if valid_count else math.nan
    neutral_rate = neutral_count / valid_count * 100 if valid_count else math.nan
    loss_rate = loss_count / valid_count * 100 if valid_count else math.nan
    avg_return = float(returns.mean()) if not returns.empty else math.nan
    median_return = float(returns.median()) if not returns.empty else math.nan
    p10_return = float(returns.quantile(0.10)) if not returns.empty else math.nan
    p90_return = float(returns.quantile(0.90)) if not returns.empty else math.nan
    stop_exit_count = int(
        valid["exit_reason"].astype(str).eq("sustained_close_below_lower_ma20_ema23_4pct_4d").sum()
    )
    meets_metric = (
        valid_count > 0
        and win_rate >= WIN_RATE_THRESHOLD_PCT
        and avg_return > 0
        and median_return > 0
    )
    return {
        "sample_size": sample_size,
        "valid_return_count": valid_count,
        "invalid_return_count": len(invalid),
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct(win_rate),
        "neutral_rate_pct": pct(neutral_rate),
        "loss_rate_pct": pct(loss_rate),
        "avg_return_pct": pct(avg_return),
        "median_return_pct": pct(median_return),
        "p10_return_pct": pct(p10_return),
        "p90_return_pct": pct(p90_return),
        "stop_exit_count": stop_exit_count,
        "stop_exit_rate_pct": pct(stop_exit_count / valid_count * 100 if valid_count else math.nan),
        "meets_win_return_metric": bool_text(meets_metric),
    }


def model_specs() -> list[ModelSpec]:
    return [
        ModelSpec(
            model_id="volume_range_breakout_v2_low_position_volume_attack",
            model_zh="低位放量攻擊",
            candidate_condition_id="pos120_low_all_shapes",
            candidate_condition_zh=(
                "D+15 close-only隔日續攻基準中，120日位階<=40；"
                "盤整、非盤整、寬幅三種shape都可進入。"
            ),
            included_buckets="position_120d=low_pos_le40; shape=consolidation|non_consolidation|wide_range",
            mask=lambda d: d["position_bucket_120d"].eq("low_pos_le40"),
        ),
        ModelSpec(
            model_id="volume_range_breakout_v2_mid_position_momentum_attack",
            model_zh="中位動能放量攻擊",
            candidate_condition_id="pos120_mid_non_consolidation_or_wide",
            candidate_condition_zh=(
                "D+15 close-only隔日續攻基準中，120日位階>40且<=75，"
                "且shape為非盤整或寬幅；排除中位盤整。"
            ),
            included_buckets="position_120d=mid_pos_40_75; shape=non_consolidation|wide_range",
            mask=lambda d: d["position_bucket_120d"].eq("mid_pos_40_75")
            & d["shape_bucket"].isin(["non_consolidation", "wide_range"]),
        ),
    ]


def high_position_subjects() -> list[SubjectSpec]:
    return [
        SubjectSpec(
            subject_type="high_position_audit_bucket",
            subject_id="high_pos_gt75_non_consolidation",
            subject_zh="高位非盤整放量攻擊觀察桶",
            mask=lambda d: d["position_bucket_120d"].eq("high_pos_gt75")
            & d["shape_bucket"].eq("non_consolidation"),
        ),
        SubjectSpec(
            subject_type="high_position_audit_bucket",
            subject_id="high_pos_gt75_wide_range",
            subject_zh="高位寬幅放量攻擊觀察桶",
            mask=lambda d: d["position_bucket_120d"].eq("high_pos_gt75")
            & d["shape_bucket"].eq("wide_range"),
        ),
    ]


def condition_specs() -> list[ConditionSpec]:
    return [
        ConditionSpec(
            "tdcc_weekly_increase_top20",
            "TDCC weekly_increase rank <= 20",
            "tdcc_weekly_increase_top20 == True",
            lambda d: bool_series(d["tdcc_weekly_increase_top20"]),
        ),
        ConditionSpec(
            "tdcc_any_top20",
            "TDCC any list rank <= 20",
            "tdcc_any_top20 == True",
            lambda d: bool_series(d["tdcc_any_top20"]),
        ),
        ConditionSpec(
            "tech_ma60_gt_ma120",
            "MA60 > MA120",
            "ma60_gt_ma120 == True",
            lambda d: bool_series(d["ma60_gt_ma120"]),
        ),
        ConditionSpec(
            "tech_ret20_0_to_25",
            "20日漲幅 0% 到 25%",
            "0 <= hist_return_20d_pct <= 25",
            lambda d: numeric(d["hist_return_20d_pct"]).between(0, 25, inclusive="both"),
        ),
        ConditionSpec(
            "tech_dist_ema23_0_to_15",
            "距 EMA23 0% 到 15%",
            "0 <= dist_ema23_pct <= 15",
            lambda d: numeric(d["dist_ema23_pct"]).between(0, 15, inclusive="both"),
        ),
        ConditionSpec(
            "volume_ratio_2_to_6",
            "量比 2 到 6",
            "2 <= volume_ratio <= 6",
            lambda d: numeric(d["volume_ratio"]).between(2, 6, inclusive="both"),
        ),
        ConditionSpec(
            "not_limit_up_like",
            "非鎖漲停型態",
            "limit_up_like != True",
            lambda d: ~bool_series(d["limit_up_like"]),
        ),
        ConditionSpec(
            "breakout_over_prev60_2_to_10",
            "突破前60日高點 2% 到 10%",
            "2 <= breakout_over_prev60_pct <= 10",
            lambda d: numeric(d["breakout_over_prev60_pct"]).between(2, 10, inclusive="both"),
        ),
    ]


def base_contract_row(spec: ModelSpec, subset: pd.DataFrame, generated_at: str) -> dict[str, object]:
    metrics = metric_row(subset)
    base = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": subset["artifact_version"].iloc[0] if not subset.empty else "",
        "advisory_status": ADVISORY_STATUS,
        "row_type": "base_performance",
        "parent_model_id": PARENT_MODEL_ID,
        "model_id": spec.model_id,
        "model_zh": spec.model_zh,
        "candidate_condition_id": spec.candidate_condition_id,
        "candidate_condition_zh": spec.candidate_condition_zh,
        "confirmation_rule_id": CONFIRMATION_RULE_ID,
        "confirmation_rule_zh": CONFIRMATION_RULE_ZH,
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_rule_zh": ENTRY_RULE_ZH,
        "exit_policy_id": EXIT_POLICY_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule_zh": EXIT_RULE_ZH,
        "stop_rule_id": STOP_RULE_ID,
        "stop_rule_zh": STOP_RULE_ZH,
        "base_metric_scope": BASE_SCOPE_ID,
        "position_axis": "position_120d",
        "included_buckets": spec.included_buckets,
        "sample_count_context": "reported_not_a_disqualifier",
        "production_registry_change": "False",
        "membership_note": "research-only candidate bucket model; no production registry change",
        "approved_for_daily": "False",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    base.update(metrics)
    return base


def model_contract_row(spec: ModelSpec, subset: pd.DataFrame, generated_at: str) -> dict[str, object]:
    row = base_contract_row(spec, subset, generated_at)
    row["row_type"] = "model_contract"
    return row


def build_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for spec in model_specs():
        subset = source[spec.mask(source)].copy()
        subset["research_id"] = RESEARCH_ID
        subset["artifact_version"] = ARTIFACT_VERSION
        subset["source_research_id"] = SOURCE_RESEARCH_ID
        subset["source_artifact_version"] = subset["artifact_version"]
        subset["advisory_status"] = ADVISORY_STATUS
        subset["parent_model_id"] = PARENT_MODEL_ID
        subset["model_id"] = spec.model_id
        subset["model_zh"] = spec.model_zh
        subset["source_analysis_scope_id"] = subset["analysis_scope_id"]
        subset["candidate_condition_id"] = spec.candidate_condition_id
        subset["approved_for_daily"] = "False"
        subset["production_readiness"] = PRODUCTION_READINESS
        subset["generated_at"] = generated_at
        rows.append(subset[DETAIL_COLUMNS])
    if not rows:
        return pd.DataFrame(columns=DETAIL_COLUMNS)
    return pd.concat(rows, ignore_index=True)[DETAIL_COLUMNS]


def build_contract(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for spec in model_specs():
        subset = source[spec.mask(source)].copy()
        rows.append(model_contract_row(spec, subset, generated_at))
        rows.append(base_contract_row(spec, subset, generated_at))
    return pd.DataFrame(rows)[CONTRACT_COLUMNS]


def decision_hint(metrics: dict[str, object]) -> str:
    if str(metrics["meets_win_return_metric"]) == "True":
        return "stratification_metric_met_research_only"
    valid = int(metrics["valid_return_count"])
    if valid == 0:
        return "audit_condition_no_valid_returns"
    if to_float(metrics["median_return_pct"]) <= 0:
        return "audit_condition_median_not_positive"
    if to_float(metrics["win_rate_pct"]) < WIN_RATE_THRESHOLD_PCT:
        return "audit_condition_win_rate_below_metric"
    return "audit_condition_return_metric_not_met"


def stratification_row(
    subject: SubjectSpec,
    baseline: pd.DataFrame,
    condition: ConditionSpec,
    generated_at: str,
) -> dict[str, object]:
    subset = baseline[condition.mask(baseline)].copy()
    base_metrics = metric_row(baseline)
    metrics = metric_row(subset)
    baseline_valid = int(base_metrics["valid_return_count"])
    sample_size = int(metrics["sample_size"])
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": baseline["artifact_version"].iloc[0] if not baseline.empty else "",
        "advisory_status": ADVISORY_STATUS,
        "row_type": "condition_stratification",
        "parent_model_id": PARENT_MODEL_ID,
        "subject_type": subject.subject_type,
        "subject_id": subject.subject_id,
        "subject_zh": subject.subject_zh,
        "condition_id": condition.condition_id,
        "condition_zh": condition.condition_zh,
        "condition_expression": condition.expression,
        "condition_role": "stratification_only_not_candidate_or_confirmation_gate",
        "baseline_sample_size": int(base_metrics["sample_size"]),
        "coverage_pct": pct(sample_size / int(base_metrics["sample_size"]) * 100 if int(base_metrics["sample_size"]) else math.nan),
        "baseline_win_rate_pct": base_metrics["win_rate_pct"],
        "baseline_avg_return_pct": base_metrics["avg_return_pct"],
        "baseline_median_return_pct": base_metrics["median_return_pct"],
        "win_rate_delta_pct": pct(to_float(metrics["win_rate_pct"]) - to_float(base_metrics["win_rate_pct"])),
        "avg_return_delta_pct": pct(to_float(metrics["avg_return_pct"]) - to_float(base_metrics["avg_return_pct"])),
        "median_return_delta_pct": pct(to_float(metrics["median_return_pct"]) - to_float(base_metrics["median_return_pct"])),
        "sample_count_context": "reported_not_a_disqualifier",
        "approved_for_daily": "False",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    row["decision_hint"] = decision_hint(metrics)
    if baseline_valid == 0:
        row["coverage_pct"] = ""
    return row


def build_stratification(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    subjects: list[SubjectSpec] = []
    for spec in model_specs():
        subjects.append(
            SubjectSpec(
                subject_type="candidate_model",
                subject_id=spec.model_id,
                subject_zh=spec.model_zh,
                mask=spec.mask,
            )
        )
    subjects.extend(high_position_subjects())
    rows: list[dict[str, object]] = []
    for subject in subjects:
        baseline = source[subject.mask(source)].copy()
        for condition in condition_specs():
            rows.append(stratification_row(subject, baseline, condition, generated_at))
    return pd.DataFrame(rows)[STRATIFICATION_COLUMNS]


def markdown_table(frame: pd.DataFrame) -> str:
    lines = [
        "| model_id | model_zh | sample_size | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | meets_win_return_metric |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    base = frame[frame["row_type"].eq("base_performance")]
    for _, row in base.iterrows():
        lines.append(
            "| {model_id} | {model_zh} | {sample_size} | {win_rate_pct} | {loss_rate_pct} | {avg_return_pct} | {median_return_pct} | {metric} |".format(
                model_id=row["model_id"],
                model_zh=row["model_zh"],
                sample_size=row["sample_size"],
                win_rate_pct=row["win_rate_pct"],
                loss_rate_pct=row["loss_rate_pct"],
                avg_return_pct=row["avg_return_pct"],
                median_return_pct=row["median_return_pct"],
                metric=row["meets_win_return_metric"],
            )
        )
    return "\n".join(lines)


def write_markdown(contract: pd.DataFrame, stratification: pd.DataFrame) -> None:
    high = stratification[stratification["subject_type"].eq("high_position_audit_bucket")]
    high_hits = high[high["meets_win_return_metric"].astype(str).eq("True")]
    text = "\n".join(
        [
            "# volume_range_breakout_v2_candidate_bucket_contract",
            "",
            "research-only artifact; no production registry change.",
            "",
            "Candidate buckets are based on the 120d position-shape matrix under the D+15 close-only next-day continuation baseline.",
            "Sample count is reported as context only and is not a disqualifier.",
            "",
            "## Candidate Models",
            "",
            markdown_table(contract),
            "",
            "## High Position Rescue/Audit Stratification",
            "",
            f"High-position stratification rows meeting the metric: {len(high_hits)}",
            "High-position buckets remain audit-only until a separate promotion decision.",
            "",
        ]
    )
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text(text, encoding="utf-8")


def main() -> None:
    generated_at = now_text()
    source = read_csv(SOURCE_DETAIL_CSV)
    source = source[source["return_valid"].astype(str).eq("True")].copy()
    if source.empty:
        raise SystemExit("ERROR: source has no valid-return rows")
    if source["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique in source scope")
    contract = build_contract(source, generated_at)
    detail = build_detail(source, generated_at)
    stratification = build_stratification(source, generated_at)
    write_csv(contract, LATEST_CONTRACT_CSV, CONTRACT_COLUMNS)
    write_csv(contract, HISTORY_CONTRACT_CSV, CONTRACT_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(stratification, LATEST_STRATIFICATION_CSV, STRATIFICATION_COLUMNS)
    write_csv(stratification, HISTORY_STRATIFICATION_CSV, STRATIFICATION_COLUMNS)
    write_markdown(contract, stratification)
    print(f"Saved: {LATEST_CONTRACT_CSV} rows={len(contract)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_STRATIFICATION_CSV} rows={len(stratification)}")
    print(f"Saved: {LATEST_MD}")


if __name__ == "__main__":
    main()
