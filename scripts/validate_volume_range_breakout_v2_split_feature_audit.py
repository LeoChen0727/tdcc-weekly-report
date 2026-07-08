from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_split_feature_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_OVERLAP_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    SUMMARY_COLUMNS,
)


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


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "yes", "y"})


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    return pd.to_datetime(text, format="%Y%m%d", errors="coerce")


def overlap_pair_count(frame: pd.DataFrame) -> int:
    if frame.empty:
        return 0
    work = frame.copy()
    work["_entry_dt"] = parse_yyyymmdd(work["entry_date"])
    work["_exit_dt"] = parse_yyyymmdd(work["exit_date"])
    if work["_entry_dt"].isna().any() or work["_exit_dt"].isna().any():
        fail("detail has unparseable entry_date or exit_date")
    count = 0
    for _, part in work.sort_values(["stock_id", "_entry_dt", "_exit_dt", "source_event_key"]).groupby(
        "stock_id", dropna=False
    ):
        active: list[pd.Series] = []
        for _, row in part.iterrows():
            for prior in active:
                if row["_entry_dt"] <= prior["_exit_dt"]:
                    count += 1
            active = [prior for prior in active if prior["_exit_dt"] >= row["_entry_dt"]]
            active.append(row)
    return count


def require_common_frame(frame_name: str, frame: pd.DataFrame) -> None:
    if frame.empty:
        fail(f"{frame_name} must not be empty")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{frame_name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{frame_name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{frame_name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{frame_name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"{frame_name} model_id must be {MODEL_ID}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{frame_name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{frame_name} approved_for_daily must remain false")


def validate_common(summary: pd.DataFrame, history: pd.DataFrame, detail: pd.DataFrame, detail_history: pd.DataFrame) -> None:
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    if len(summary) != len(history):
        fail("latest/history summary row counts differ")
    if len(detail) != len(detail_history):
        fail("latest/history detail row counts differ")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"research artifact must not contain production decision fields: {forbidden}")
    require_common_frame("summary", summary)
    require_common_frame("detail", detail)


def validate_source_membership(detail: pd.DataFrame) -> None:
    source = read_csv(SOURCE_OVERLAP_DETAIL_CSV)
    if source.empty:
        fail("source overlap detail must not be empty")
    if source["source_event_key"].duplicated().any():
        fail("source overlap detail source_event_key must be unique")
    if not boolish(source["same_stock_non_overlap_included"]).any():
        fail("source overlap detail has no same-stock non-overlap accepted rows")
    if not (~boolish(source["same_stock_non_overlap_included"])).any():
        fail("source overlap detail must preserve at least one suppressed overlap row for this guardrail")

    accepted = source[boolish(source["same_stock_non_overlap_included"])]
    if len(detail) != len(accepted):
        fail(f"detail row count {len(detail)} must match accepted non-overlap rows {len(accepted)}")
    if set(detail["source_event_key"].astype(str)) != set(accepted["source_event_key"].astype(str)):
        fail("detail source_event_key set must equal accepted non-overlap source keys")
    if not boolish(detail["same_stock_non_overlap_included"]).all():
        fail("detail must contain only same_stock_non_overlap_included=True rows")
    if overlap_pair_count(detail) != 0:
        fail("detail must have zero same-stock active-window overlap pairs")

    source_8454 = source[source["stock_id"].astype(str).eq("8454")]
    if not source_8454.empty:
        accepted_8454 = detail[detail["stock_id"].astype(str).eq("8454")]
        if len(source_8454) < 3:
            fail("8454 regression source must contain the historical three-row overlap case")
        if len(accepted_8454) != 1:
            fail(f"8454 non-overlap detail must keep exactly one accepted row; got {len(accepted_8454)}")


def validate_summary_rows(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    required_row_types = {
        "group_baseline",
        "success_common_feature",
        "failure_common_feature",
        "discriminative_feature",
        "candidate_condition_matrix",
        "numeric_success_failure_gap",
        "anomaly_check",
    }
    row_types = set(summary["row_type"].astype(str))
    missing = sorted(required_row_types - row_types)
    if missing:
        fail(f"summary missing required row_type values: {missing}")

    baseline = summary[summary["row_type"].eq("group_baseline")]
    required_groups = {"baseline_non_overlap", "low_base_consolidated", "momentum_continuation"}
    if set(baseline["split_group_id"].astype(str)) != required_groups:
        fail("group_baseline rows must cover baseline_non_overlap, low_base_consolidated, momentum_continuation")
    baseline_row = baseline[baseline["split_group_id"].eq("baseline_non_overlap")].iloc[0]
    if int(baseline_row["sample_size"]) != len(detail):
        fail("baseline_non_overlap sample_size must equal detail row count")
    for group_id in ["low_base_consolidated", "momentum_continuation"]:
        expected = int(detail["split_group_id"].eq(group_id).sum())
        actual = int(baseline[baseline["split_group_id"].eq(group_id)].iloc[0]["sample_size"])
        if actual != expected:
            fail(f"{group_id} sample_size mismatch: summary={actual}, detail={expected}")

    for col in [
        "win_rate_pct",
        "neutral_rate_pct",
        "loss_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "high_return_ge10_rate_pct",
        "loss_le_minus5_rate_pct",
    ]:
        if summary[col].astype(str).eq("").all():
            fail(f"summary must not be win-rate-only; {col} is entirely blank")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
        values = numeric(summary[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")


def validate_success_failure_feature_guardrail(summary: pd.DataFrame) -> None:
    success = summary[summary["row_type"].eq("success_common_feature")]
    failure = summary[summary["row_type"].eq("failure_common_feature")]
    diff = summary[summary["row_type"].eq("discriminative_feature")]
    if success.empty or failure.empty or diff.empty:
        fail("success/failure/discriminative feature rows must all exist")
    for name, frame in [("success", success), ("failure", failure), ("diff", diff)]:
        for col in [
            "success_with_feature_count",
            "failure_with_feature_count",
            "success_share_pct",
            "failure_share_pct",
            "success_minus_failure_share_pct",
        ]:
            if frame[col].astype(str).eq("").any():
                fail(f"{name} feature rows must include {col}")
    if "failure_common_flag" not in success.columns or success["failure_common_flag"].astype(str).eq("").any():
        fail("success_common_feature rows must include failure_common_flag")
    common_success = success[success["failure_common_flag"].astype(str).str.lower().eq("true")]
    if not common_success.empty and not common_success["decision_hint"].astype(str).str.contains(
        "common_in_success_and_failure"
    ).any():
        fail("success_common_feature rows with failure_common_flag=True must surface the failure-overlap warning")
    if not success["decision_hint"].astype(str).str.contains("common_in_success_and_failure|success|mixed", regex=True).all():
        fail("success_common_feature rows must carry a decision_hint that accounts for failure overlap")

    required_features = {"close_loc_ge95", "close_gt_ma20", "dist_ma60_gt30"}
    present = set(summary["feature_id"].astype(str))
    missing = sorted(required_features - present)
    if missing:
        fail(f"technical-analysis features missing from summary: {missing}")


def validate_candidate_matrix(summary: pd.DataFrame) -> None:
    candidates = summary[summary["row_type"].eq("candidate_condition_matrix")]
    required = {
        "momentum_volume_control_wide20",
        "momentum_locked_wide_nonconsolidation",
        "momentum_close_loc95_volume2to6",
        "momentum_volume_gt6_overheat",
        "lowbase_vol2to6_confirm3",
        "lowbase_closehigh_confirm3",
        "lowbase_ma60_gt_ma120",
        "lowbase_off60_le35",
    }
    present = set(candidates["candidate_id"].astype(str))
    missing = sorted(required - present)
    if missing:
        fail(f"candidate matrix missing required candidate rows: {missing}")
    if not set(candidates["split_group_id"].astype(str)) >= {"low_base_consolidated", "momentum_continuation"}:
        fail("candidate matrix must include both low-base and momentum groups")
    allowed_status_prefixes = ("research_only_", "rejected_as_")
    bad = candidates[~candidates["candidate_status"].astype(str).str.startswith(allowed_status_prefixes)]
    if not bad.empty:
        fail("candidate matrix must remain research-only or rejected-as-hard-gate")
    for col in ["baseline_win_rate_pct", "uplift_win_rate_pp", "uplift_avg_return_pct", "decision_hint"]:
        if candidates[col].astype(str).eq("").any():
            fail(f"candidate matrix rows must include {col}")


def validate_detail_technical_columns(detail: pd.DataFrame) -> None:
    required = [
        "close_location_pct",
        "signal_body_return_pct",
        "confirm_vs_signal_close_pct",
        "hist_ma20",
        "hist_ma60",
        "hist_ma120",
        "hist_ema23",
        "dist_ma20_pct",
        "dist_ma60_pct",
        "dist_high60_pct",
        "close_gt_ma20",
        "close_gt_ma60",
        "ma20_gt_ma60",
    ]
    missing = [col for col in required if col not in detail.columns]
    if missing:
        fail(f"detail missing technical-analysis columns: {missing}")
    for col in ["close_location_pct", "hist_ma20", "dist_ma60_pct", "dist_high60_pct"]:
        values = numeric(detail[col])
        if values.notna().sum() < max(50, int(len(detail) * 0.5)):
            fail(f"technical column {col} has insufficient populated rows")
    if set(detail["split_group_id"].astype(str)) != {"low_base_consolidated", "momentum_continuation"}:
        fail("detail split_group_id must contain low_base_consolidated and momentum_continuation")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    for needle in ["research-only", "same-stock non-overlap", "failure_share_pct", "Candidate Condition Matrix"]:
        if needle not in text:
            fail(f"markdown summary missing required text: {needle}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)

    validate_common(summary, history, detail, detail_history)
    validate_source_membership(detail)
    validate_summary_rows(summary, detail)
    validate_success_failure_feature_guardrail(summary)
    validate_candidate_matrix(summary)
    validate_detail_technical_columns(detail)
    validate_markdown()

    print(f"Validated {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Validated {LATEST_DETAIL_CSV} rows={len(detail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
