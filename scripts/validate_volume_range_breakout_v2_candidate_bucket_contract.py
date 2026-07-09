from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_candidate_bucket_contract import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    BASE_SCOPE_ID,
    CONTRACT_COLUMNS,
    DETAIL_COLUMNS,
    HISTORY_CONTRACT_CSV,
    HISTORY_DETAIL_CSV,
    HISTORY_STRATIFICATION_CSV,
    LATEST_CONTRACT_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_STRATIFICATION_CSV,
    PARENT_MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    STRATIFICATION_COLUMNS,
    WIN_RATE_THRESHOLD_PCT,
    condition_specs,
    high_position_subjects,
    model_specs,
)


ROOT = Path(".")

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "buy_rank_eligible",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def int_value(value: object) -> int:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        fail(f"expected numeric integer value, got {value!r}")
    return int(parsed)


def numeric_value(value: object) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        return float("nan")
    return float(parsed)


def validate_common(frame: pd.DataFrame, columns: list[str], name: str) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(frame.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} contains forbidden production fields: {forbidden}")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["parent_model_id"].astype(str)) != {PARENT_MODEL_ID}:
        fail(f"{name} parent_model_id must be {PARENT_MODEL_ID}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def source_scope() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source position-shape detail must not be empty")
    if set(source["research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail must come from position-shape matrix")
    source = source[source["return_valid"].astype(str).eq("True")].copy()
    if source.empty:
        fail("source valid-return scope must not be empty")
    if source["source_event_key"].duplicated().any():
        fail("source valid-return scope must be unique by source_event_key")
    if not false_only(source.get("approved_for_daily", pd.Series(dtype=str))):
        fail("source approved_for_daily must remain false")
    return source


def metric_expected(row: pd.Series) -> bool:
    valid = int_value(row["valid_return_count"])
    if valid <= 0:
        return False
    return (
        numeric_value(row["win_rate_pct"]) >= WIN_RATE_THRESHOLD_PCT
        and numeric_value(row["avg_return_pct"]) > 0
        and numeric_value(row["median_return_pct"]) > 0
    )


def validate_metric_formula(row: pd.Series) -> None:
    observed = str(row["meets_win_return_metric"]).lower() == "true"
    if observed != metric_expected(row):
        fail("meets_win_return_metric must depend only on win rate and positive average/median return")


def validate_contract(contract: pd.DataFrame, source: pd.DataFrame) -> None:
    validate_common(contract, CONTRACT_COLUMNS, "contract")
    expected_model_ids = {spec.model_id for spec in model_specs()}
    if set(contract["model_id"].astype(str)) != expected_model_ids:
        fail("contract model_id set must match candidate model specs")
    if contract["row_type"].value_counts().to_dict() != {
        "model_contract": len(expected_model_ids),
        "base_performance": len(expected_model_ids),
    }:
        fail("contract must contain one model_contract and one base_performance row per candidate model")
    if set(contract["production_registry_change"].astype(str)) != {"False"}:
        fail("contract production_registry_change must remain False")
    if set(contract["sample_count_context"].astype(str)) != {"reported_not_a_disqualifier"}:
        fail("contract sample_count_context must not disqualify small samples")
    if set(contract["base_metric_scope"].astype(str)) != {BASE_SCOPE_ID}:
        fail(f"contract base_metric_scope must be {BASE_SCOPE_ID}")

    for spec in model_specs():
        expected_count = int(spec.mask(source).sum())
        rows = contract[contract["model_id"].astype(str).eq(spec.model_id)]
        if len(rows) != 2:
            fail(f"contract must have exactly two rows for {spec.model_id}")
        if set(rows["candidate_condition_id"].astype(str)) != {spec.candidate_condition_id}:
            fail(f"contract candidate_condition_id mismatch for {spec.model_id}")
        if set(rows["included_buckets"].astype(str)) != {spec.included_buckets}:
            fail(f"contract included_buckets mismatch for {spec.model_id}")
        if set(rows["sample_size"].map(int_value)) != {expected_count}:
            fail(f"contract sample_size mismatch for {spec.model_id}")
        for _, row in rows.iterrows():
            validate_metric_formula(row)


def validate_detail(detail: pd.DataFrame, source: pd.DataFrame) -> None:
    validate_common(detail, DETAIL_COLUMNS, "detail")
    expected_by_model = {
        spec.model_id: set(source.loc[spec.mask(source), "source_event_key"].astype(str))
        for spec in model_specs()
    }
    expected_union = set().union(*expected_by_model.values())
    if detail["source_event_key"].duplicated().any():
        fail("detail source_event_key must not overlap across candidate models")
    if set(detail["source_event_key"].astype(str)) != expected_union:
        fail("detail source_event_key set must equal the candidate-model union")
    if len(detail) != len(expected_union):
        fail("detail row count must equal the non-overlapping candidate-model union")
    if set(detail["source_analysis_scope_id"].astype(str)) != {BASE_SCOPE_ID}:
        fail(f"detail source_analysis_scope_id must be {BASE_SCOPE_ID}")

    for spec in model_specs():
        rows = detail[detail["model_id"].astype(str).eq(spec.model_id)]
        if set(rows["source_event_key"].astype(str)) != expected_by_model[spec.model_id]:
            fail(f"detail source_event_key mismatch for {spec.model_id}")
        if set(rows["candidate_condition_id"].astype(str)) != {spec.candidate_condition_id}:
            fail(f"detail candidate_condition_id mismatch for {spec.model_id}")

    low = expected_by_model["volume_range_breakout_v2_low_position_volume_attack"]
    mid = expected_by_model["volume_range_breakout_v2_mid_position_momentum_attack"]
    if low & mid:
        fail("candidate model event sets must be disjoint")


def validate_stratification(stratification: pd.DataFrame, source: pd.DataFrame) -> None:
    validate_common(stratification, STRATIFICATION_COLUMNS, "stratification")
    expected_subjects = {spec.model_id for spec in model_specs()}
    expected_subjects.update(subject.subject_id for subject in high_position_subjects())
    expected_conditions = {condition.condition_id for condition in condition_specs()}
    if set(stratification["subject_id"].astype(str)) != expected_subjects:
        fail("stratification subject_id set must include candidate models and high-position audit buckets")
    if set(stratification["condition_id"].astype(str)) != expected_conditions:
        fail("stratification condition_id set must match configured tests")
    if set(stratification["condition_role"].astype(str)) != {"stratification_only_not_candidate_or_confirmation_gate"}:
        fail("stratification conditions must not become hidden gates")
    if set(stratification["sample_count_context"].astype(str)) != {"reported_not_a_disqualifier"}:
        fail("stratification sample_count_context must not disqualify small samples")
    if stratification["decision_hint"].astype(str).str.lower().str.contains("sample").any():
        fail("stratification decision_hint must not reject by sample size")

    subject_masks = {
        spec.model_id: spec.mask
        for spec in model_specs()
    }
    subject_masks.update({subject.subject_id: subject.mask for subject in high_position_subjects()})
    condition_masks = {condition.condition_id: condition.mask for condition in condition_specs()}

    for _, row in stratification.iterrows():
        subject_source = source[subject_masks[row["subject_id"]](source)].copy()
        expected_baseline = len(subject_source)
        expected_count = len(subject_source[condition_masks[row["condition_id"]](subject_source)])
        if int_value(row["baseline_sample_size"]) != expected_baseline:
            fail(f"stratification baseline_sample_size mismatch for {row['subject_id']}")
        if int_value(row["sample_size"]) != expected_count:
            fail(f"stratification sample_size mismatch for {row['subject_id']} {row['condition_id']}")
        validate_metric_formula(row)


def validate_history(latest: pd.DataFrame, history: pd.DataFrame, name: str) -> None:
    if len(latest) != len(history):
        fail(f"{name} latest/history row counts differ")
    if list(latest.columns) != list(history.columns):
        fail(f"{name} latest/history columns differ")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only artifact; no production registry change.",
        "Sample count is reported as context only and is not a disqualifier.",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
        "High-position buckets remain audit-only until a separate promotion decision.",
    ]
    for token in required:
        if token not in text:
            fail(f"markdown missing required token: {token}")


def main() -> None:
    source = source_scope()
    contract = read_csv(LATEST_CONTRACT_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    stratification = read_csv(LATEST_STRATIFICATION_CSV)
    history_contract = read_csv(HISTORY_CONTRACT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_stratification = read_csv(HISTORY_STRATIFICATION_CSV)

    validate_contract(contract, source)
    validate_detail(detail, source)
    validate_stratification(stratification, source)
    validate_history(contract, history_contract, "contract")
    validate_history(detail, history_detail, "detail")
    validate_history(stratification, history_stratification, "stratification")
    validate_markdown()

    print("volume_range_breakout_v2_candidate_bucket_contract validation passed")


if __name__ == "__main__":
    main()
