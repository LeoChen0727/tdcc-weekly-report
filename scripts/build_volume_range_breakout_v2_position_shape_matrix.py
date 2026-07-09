from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_promotion_readiness_audit_detail_latest.csv"
)

LATEST_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_position_shape_matrix_latest.csv"
)
LATEST_DETAIL_CSV = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_position_shape_matrix_detail_latest.csv"
)
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_position_shape_matrix_latest.md"

HISTORY_MATRIX_CSV = (
    RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_position_shape_matrix.csv"
)
HISTORY_DETAIL_CSV = (
    RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_position_shape_matrix_detail.csv"
)

RESEARCH_ID = "volume_range_breakout_v2_position_shape_matrix"
ARTIFACT_VERSION = "volume_range_breakout_v2_position_shape_matrix_20260709"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_promotion_readiness_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARENT_MODEL_ID = "volume_range_breakout"

BASE_HOLDING_DAYS = 15
BASE_STOP_POLICY_ID = "ma20_ema23_close_stop_4d"
BASE_CONFIRMATION_RULE_ID = "next_day_continuation_confirmed_close_only"
BASE_ENTRY_RULE_ID = "confirmation_next_open"
BASE_SCOPE_ID = "d15_close_only_next_day_continuation_ma20_ema23_stop"

POSITION_BUCKETS = ["low_pos_le40", "mid_pos_40_75", "high_pos_gt75", "unknown_position"]
SHAPE_BUCKETS = ["consolidation", "non_consolidation", "wide_range"]
POSITION_AXES = {
    "position_120d": "position_in_120d_range_pct",
    "position_240d": "position_in_240d_range_pct",
}

WIN_RATE_THRESHOLD_PCT = 60.0

MATRIX_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "analysis_scope_id",
    "position_axis",
    "position_bucket",
    "shape_bucket",
    "position_shape_bucket",
    "condition_expression",
    "condition_role",
    "holding_days",
    "stop_policy_id",
    "confirmation_rule_id",
    "entry_rule_id",
    "source_sample_size",
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
    "p10_return_pct",
    "p90_return_pct",
    "stop_exit_count",
    "stop_exit_rate_pct",
    "meets_win_return_metric",
    "sample_count_context",
    "decision_hint",
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
    "analysis_scope_id",
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
    "source_model_id",
    "source_split_group_id",
    "position_bucket_120d",
    "position_shape_bucket_120d",
    "position_bucket_240d",
    "position_shape_bucket_240d",
    "shape_bucket",
    "bucket_assignment_status",
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
    if value is None:
        return math.nan
    text = str(value).strip()
    if text == "":
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


def pct(value: float | int | None) -> str:
    if value is None:
        return ""
    try:
        if math.isnan(float(value)):
            return ""
    except TypeError:
        return ""
    return str(round(float(value), 4))


def bool_text(value: bool) -> str:
    return "True" if value else "False"


def position_bucket(value: object) -> str:
    parsed = to_float(value)
    if math.isnan(parsed):
        return "unknown_position"
    if parsed <= 40:
        return "low_pos_le40"
    if parsed <= 75:
        return "mid_pos_40_75"
    return "high_pos_gt75"


def shape_bucket(row: pd.Series) -> str:
    range_width_60 = to_float(row.get("range_width_60_pct"))
    consolidation_type = str(row.get("consolidation_type", ""))
    if not math.isnan(range_width_60) and range_width_60 > 80:
        return "wide_range"
    if consolidation_type in {"short_consolidation", "long_consolidation"}:
        return "consolidation"
    return "non_consolidation"


def condition_expression(row_type: str, axis: str, position: str, shape: str) -> str:
    if row_type == "overall_baseline":
        return "all source events in the D+15 close-only continuation scope"
    if row_type == "shape_bucket":
        return f"shape_bucket == {shape}"
    if row_type == "position_bucket":
        return f"{axis} == {position}"
    return f"{axis} == {position} AND shape_bucket == {shape}"


def summarize_bucket(
    detail: pd.DataFrame,
    subset: pd.DataFrame,
    row_type: str,
    axis: str,
    position: str,
    shape: str,
    generated_at: str,
) -> dict[str, object]:
    valid = subset[subset["return_valid"].astype(str).eq("True")]
    invalid = subset[~subset["return_valid"].astype(str).eq("True")]
    returns = pd.to_numeric(valid["return_pct"], errors="coerce").dropna()
    outcomes = valid["return_outcome"].astype(str)
    win_count = int(outcomes.eq("win").sum())
    neutral_count = int(outcomes.eq("neutral").sum())
    loss_count = int(outcomes.eq("loss").sum())
    valid_count = len(valid)
    sample_size = len(subset)
    source_sample_size = len(detail)
    stop_exit_count = int(
        valid["exit_reason"].astype(str).eq("sustained_close_below_lower_ma20_ema23_4pct_4d").sum()
    )
    win_rate = win_count / valid_count * 100 if valid_count else math.nan
    neutral_rate = neutral_count / valid_count * 100 if valid_count else math.nan
    loss_rate = loss_count / valid_count * 100 if valid_count else math.nan
    avg_return = float(returns.mean()) if not returns.empty else math.nan
    median_return = float(returns.median()) if not returns.empty else math.nan
    p10_return = float(returns.quantile(0.10)) if not returns.empty else math.nan
    p90_return = float(returns.quantile(0.90)) if not returns.empty else math.nan
    meets_metric = (
        valid_count > 0
        and win_rate >= WIN_RATE_THRESHOLD_PCT
        and avg_return > 0
        and median_return > 0
    )
    if meets_metric:
        decision_hint = "candidate_bucket_research_only_metric_met"
    elif valid_count == 0:
        decision_hint = "audit_bucket_no_valid_returns"
    elif median_return <= 0:
        decision_hint = "audit_or_risk_bucket_median_not_positive"
    elif win_rate < WIN_RATE_THRESHOLD_PCT:
        decision_hint = "audit_bucket_win_rate_below_metric"
    else:
        decision_hint = "audit_bucket_return_metric_not_met"

    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": detail["source_artifact_version"].iloc[0],
        "advisory_status": ADVISORY_STATUS,
        "row_type": row_type,
        "parent_model_id": PARENT_MODEL_ID,
        "analysis_scope_id": BASE_SCOPE_ID,
        "position_axis": axis,
        "position_bucket": position,
        "shape_bucket": shape,
        "position_shape_bucket": f"{axis}__{position}__{shape}",
        "condition_expression": condition_expression(row_type, axis, position, shape),
        "condition_role": "matrix_bucket_not_hidden_gate",
        "holding_days": BASE_HOLDING_DAYS,
        "stop_policy_id": BASE_STOP_POLICY_ID,
        "confirmation_rule_id": BASE_CONFIRMATION_RULE_ID,
        "entry_rule_id": BASE_ENTRY_RULE_ID,
        "source_sample_size": source_sample_size,
        "sample_size": sample_size,
        "valid_return_count": valid_count,
        "invalid_return_count": len(invalid),
        "coverage_pct": pct(sample_size / source_sample_size * 100 if source_sample_size else math.nan),
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
        "sample_count_context": "reported_not_a_disqualifier",
        "decision_hint": decision_hint,
        "approved_for_daily": "False",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    out = pd.DataFrame()
    direct_columns = [
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
    ]
    for col in direct_columns:
        out[col] = source.get(col, "")
    out["research_id"] = RESEARCH_ID
    out["artifact_version"] = ARTIFACT_VERSION
    out["source_research_id"] = SOURCE_RESEARCH_ID
    out["source_artifact_version"] = source["artifact_version"]
    out["advisory_status"] = ADVISORY_STATUS
    out["parent_model_id"] = PARENT_MODEL_ID
    out["analysis_scope_id"] = BASE_SCOPE_ID
    out["source_model_id"] = source.get("model_id", "")
    out["source_split_group_id"] = source.get("split_group_id", "")
    out["shape_bucket"] = source.apply(shape_bucket, axis=1)
    out["position_bucket_120d"] = source["position_in_120d_range_pct"].map(position_bucket)
    out["position_shape_bucket_120d"] = (
        "position_120d__" + out["position_bucket_120d"] + "__" + out["shape_bucket"]
    )
    out["position_bucket_240d"] = source["position_in_240d_range_pct"].map(position_bucket)
    out["position_shape_bucket_240d"] = (
        "position_240d__" + out["position_bucket_240d"] + "__" + out["shape_bucket"]
    )
    out["bucket_assignment_status"] = "assigned"
    out["approved_for_daily"] = "False"
    out["production_readiness"] = PRODUCTION_READINESS
    out["generated_at"] = generated_at
    return out[DETAIL_COLUMNS]


def build_matrix(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    rows.append(
        summarize_bucket(
            detail,
            detail,
            "overall_baseline",
            "all_positions",
            "all_positions",
            "all_shapes",
            generated_at,
        )
    )
    for shape in SHAPE_BUCKETS:
        rows.append(
            summarize_bucket(
                detail,
                detail[detail["shape_bucket"].eq(shape)],
                "shape_bucket",
                "shape_only",
                "all_positions",
                shape,
                generated_at,
            )
        )
    for axis in POSITION_AXES:
        position_col = f"position_bucket_{axis.split('_')[1]}"
        for position in POSITION_BUCKETS:
            rows.append(
                summarize_bucket(
                    detail,
                    detail[detail[position_col].eq(position)],
                    "position_bucket",
                    axis,
                    position,
                    "all_shapes",
                    generated_at,
                )
            )
        for position in POSITION_BUCKETS:
            for shape in SHAPE_BUCKETS:
                rows.append(
                    summarize_bucket(
                        detail,
                        detail[detail[position_col].eq(position) & detail["shape_bucket"].eq(shape)],
                        "position_shape_bucket",
                        axis,
                        position,
                        shape,
                        generated_at,
                    )
                )
    return pd.DataFrame(rows)[MATRIX_COLUMNS]


def markdown_table(frame: pd.DataFrame, axis: str) -> str:
    lines = [
        "| position_bucket | shape_bucket | sample_size | valid_return_count | win_rate_pct | loss_rate_pct | avg_return_pct | median_return_pct | meets_win_return_metric |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    selected = frame[
        frame["row_type"].eq("position_shape_bucket")
        & frame["position_axis"].eq(axis)
    ]
    for _, row in selected.iterrows():
        lines.append(
            "| {position} | {shape} | {sample} | {valid} | {win} | {loss} | {avg} | {median} | {metric} |".format(
                position=row["position_bucket"],
                shape=row["shape_bucket"],
                sample=row["sample_size"],
                valid=row["valid_return_count"],
                win=row["win_rate_pct"],
                loss=row["loss_rate_pct"],
                avg=row["avg_return_pct"],
                median=row["median_return_pct"],
                metric=row["meets_win_return_metric"],
            )
        )
    return "\n".join(lines)


def write_markdown(matrix: pd.DataFrame, detail: pd.DataFrame) -> None:
    latest_baseline = matrix[matrix["row_type"].eq("overall_baseline")].iloc[0]
    text = "\n".join(
        [
            "# volume_range_breakout_v2_position_shape_matrix",
            "",
            "research-only artifact; no production registry change.",
            "",
            f"Scope: {BASE_SCOPE_ID}",
            f"Source sample size: {len(detail)}",
            f"Valid returns: {latest_baseline['valid_return_count']}",
            "",
            "Bucket assignment is exhaustive and non-overlapping per position axis.",
            "Sample count is reported as context only and is not a disqualifier.",
            "A bucket meets the win/return metric when win_rate >= 60% and both average and median return are positive.",
            "",
            "## 120d Position x Shape Matrix",
            "",
            markdown_table(matrix, "position_120d"),
            "",
            "## 240d Position x Shape Matrix",
            "",
            markdown_table(matrix, "position_240d"),
            "",
        ]
    )
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text(text, encoding="utf-8")


def main() -> None:
    generated_at = now_text()
    source = read_csv(SOURCE_DETAIL_CSV)
    source = source[
        source["holding_days"].astype(str).eq(str(BASE_HOLDING_DAYS))
        & source["stop_policy_id"].astype(str).eq(BASE_STOP_POLICY_ID)
        & source["confirmation_rule_id"].astype(str).eq(BASE_CONFIRMATION_RULE_ID)
        & source["entry_rule_id"].astype(str).eq(BASE_ENTRY_RULE_ID)
    ].copy()
    if source.empty:
        raise SystemExit("ERROR: source filter produced no rows")
    if source["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique in the matrix source scope")
    detail = build_detail(source, generated_at)
    matrix = build_matrix(detail, generated_at)
    write_csv(matrix, LATEST_MATRIX_CSV, MATRIX_COLUMNS)
    write_csv(matrix, HISTORY_MATRIX_CSV, MATRIX_COLUMNS)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_markdown(matrix, detail)
    print(f"Saved: {LATEST_MATRIX_CSV} rows={len(matrix)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")


if __name__ == "__main__":
    main()
