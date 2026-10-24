from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_lowbase_horizon_audit import mark_non_overlap
from build_volume_range_breakout_v2_split_coverage_audit import (
    ADVISORY_STATUS,
    ANOMALY_POLICIES,
    ARTIFACT_VERSION,
    BUCKET_BY_ID,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    MOMENTUM_BREAKOUT_THRESHOLD_PCT,
    OVERLAP_POLICIES,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    SPLIT_BUCKETS,
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


def require_common(name: str, frame: pd.DataFrame) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"{name} model_id must be {MODEL_ID}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame, history_summary: pd.DataFrame, history_detail: pd.DataFrame) -> None:
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"split coverage artifact must not contain production decision fields: {forbidden}")
    require_common("summary", summary)
    require_common("detail", detail)
    if set(summary["overlap_policy"].astype(str)) != set(OVERLAP_POLICIES):
        fail("summary overlap_policy set mismatch")
    if set(summary["anomaly_policy"].astype(str)) != set(ANOMALY_POLICIES):
        fail("summary anomaly_policy set mismatch")


def expected_bucket_ids(detail: pd.DataFrame) -> pd.Series:
    high60 = boolish(detail["high_breakout_60d_met"])
    width40 = numeric(detail["range_width_40_pct"])
    off120 = numeric(detail["off_120d_low_pct"])
    breakout = numeric(detail["breakout_over_prev60_pct"])
    momentum = high60 & width40.gt(40) & breakout.ge(MOMENTUM_BREAKOUT_THRESHOLD_PCT)
    lowbase = high60 & width40.le(40) & off120.le(40)
    expected = pd.Series("legacy_non_prev60_residual", index=detail.index, dtype=object)
    expected.loc[high60] = "prev60_residual_research_pool"
    expected.loc[lowbase] = "lowbase_consolidation_candidate"
    expected.loc[momentum] = "momentum_breakout_candidate"
    return expected


def validate_source_membership(detail: pd.DataFrame) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source semantic detail must not be empty")
    if set(source["research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"source detail research_id must be {SOURCE_RESEARCH_ID}")
    if source["source_event_key"].duplicated().any():
        fail("source source_event_key must be unique")
    if not false_only(source["approved_for_daily"]):
        fail("source detail approved_for_daily must remain false")
    if detail["source_event_key"].duplicated().any():
        fail("detail source_event_key must be unique")
    if set(detail["source_event_key"].astype(str)) != set(source["source_event_key"].astype(str)):
        fail("detail source_event_key set must equal source semantic detail")
    return source


def validate_bucket_exclusivity(detail: pd.DataFrame) -> None:
    valid_bucket_ids = {bucket.bucket_id for bucket in SPLIT_BUCKETS}
    unexpected = sorted(set(detail["bucket_id"].astype(str)) - valid_bucket_ids)
    if unexpected:
        fail(f"detail contains unexpected bucket_id values: {unexpected}")
    expected = expected_bucket_ids(detail)
    mismatch = detail.loc[detail["bucket_id"].astype(str).ne(expected), ["source_event_key", "bucket_id"]].copy()
    if not mismatch.empty:
        fail(f"detail bucket classification mismatch; first={mismatch.head(1).to_dict('records')}")
    if not numeric(detail["bucket_match_count"]).eq(1).all():
        fail("each detail row must have bucket_match_count=1")
    candidate_count = numeric(detail["candidate_bucket_match_count"])
    if candidate_count.lt(0).any() or candidate_count.gt(1).any():
        fail("candidate_bucket_match_count must be 0 or 1")
    flag_cols = [
        "momentum_breakout_candidate_flag",
        "lowbase_consolidation_candidate_flag",
        "prev60_residual_research_pool_flag",
        "legacy_non_prev60_residual_flag",
    ]
    flag_sum = sum(boolish(detail[col]).astype(int) for col in flag_cols)
    if not flag_sum.eq(1).all():
        fail("exactly one bucket flag must be true per source_event_key")
    candidate_flags = (
        boolish(detail["momentum_breakout_candidate_flag"]).astype(int)
        + boolish(detail["lowbase_consolidation_candidate_flag"]).astype(int)
    )
    if not candidate_flags.eq(candidate_count.astype(int)).all():
        fail("candidate bucket flags must match candidate_bucket_match_count")
    overlap = boolish(detail["momentum_breakout_candidate_flag"]) & boolish(detail["lowbase_consolidation_candidate_flag"])
    if overlap.any():
        fail("momentum and lowbase candidate buckets must be mutually exclusive")


def prepare_metric_part(part: pd.DataFrame, overlap_policy: str, anomaly_policy: str) -> tuple[pd.DataFrame, int, int]:
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
        return metric, exception_count, len(work) - len(metric)
    return work, exception_count, 0


def count_return_outcomes(metric: pd.DataFrame) -> tuple[int, int, int, int]:
    returns = numeric(metric["return_pct"]).dropna()
    return int(len(returns)), int((returns > 0).sum()), int((returns == 0).sum()), int((returns < 0).sum())


def validate_summary_counts(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    bucket_rows = summary[summary["row_type"].astype(str).eq("split_bucket_coverage")].copy()
    reason_rows = summary[summary["row_type"].astype(str).eq("residual_reason_coverage")].copy()
    expected_bucket_rows = len(SPLIT_BUCKETS) * len(OVERLAP_POLICIES) * len(ANOMALY_POLICIES)
    if len(bucket_rows) != expected_bucket_rows:
        fail(f"split_bucket_coverage row count must be {expected_bucket_rows}")
    residual_reasons = sorted(
        set(
            detail.loc[
                detail["bucket_id"].astype(str).eq("prev60_residual_research_pool"),
                "residual_reason",
            ].astype(str)
        )
    )
    expected_reason_rows = len(residual_reasons) * len(OVERLAP_POLICIES) * len(ANOMALY_POLICIES)
    if len(reason_rows) != expected_reason_rows:
        fail(f"residual_reason_coverage row count must be {expected_reason_rows}")
    if not numeric(summary["total_source_event_count"]).eq(len(detail)).all():
        fail("summary total_source_event_count must equal detail row count")

    for _, row in summary.iterrows():
        bucket_id = str(row["bucket_id"])
        if bucket_id not in BUCKET_BY_ID:
            fail(f"summary contains unexpected bucket_id={bucket_id}")
        part = detail[detail["bucket_id"].astype(str).eq(bucket_id)].copy()
        if str(row["row_type"]) == "residual_reason_coverage":
            part = part[part["residual_reason"].astype(str).eq(str(row["residual_reason"]))].copy()
        if int(row["source_event_count"]) != len(part):
            fail("summary source_event_count mismatch")
        if int(row["stock_count"]) != int(part["stock_id"].astype(str).nunique()):
            fail("summary stock_count mismatch")
        metric, exception_count, suppressed = prepare_metric_part(
            part,
            str(row["overlap_policy"]),
            str(row["anomaly_policy"]),
        )
        sample_size, win_count, neutral_count, loss_count = count_return_outcomes(metric)
        if int(row["metric_event_count"]) != len(metric):
            fail("summary metric_event_count mismatch")
        if int(row["sample_size"]) != sample_size:
            fail("summary sample_size mismatch")
        if int(row["win_count"]) != win_count or int(row["neutral_count"]) != neutral_count or int(row["loss_count"]) != loss_count:
            fail("summary win/neutral/loss counts mismatch")
        if int(row["data_quality_exception_count"]) != exception_count:
            fail("summary data_quality_exception_count mismatch")
        if int(row["same_stock_overlap_suppressed_count"]) != suppressed:
            fail("summary same_stock_overlap_suppressed_count mismatch")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "every `source_event_key` must be assigned to exactly one split bucket",
        "Candidate buckets are mutually exclusive",
        "The sum of the two candidate buckets is intentionally not required to equal the old v1 source population",
        "residual pool remains research-only",
        "Performance rows are diagnostic",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    validate_common(summary, detail, history_summary, history_detail)
    source = validate_source_membership(detail)
    validate_bucket_exclusivity(detail)
    validate_summary_counts(summary, detail)
    validate_markdown()
    print(
        "volume range breakout v2 split coverage audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} source_rows={len(source)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
