from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_research_contract import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    CONTRACT_COLUMNS,
    DETAIL_COLUMNS,
    EMA23_STOP_EXIT_POLICY_ID,
    HISTORY_CONTRACT_CSV,
    HISTORY_DETAIL_CSV,
    HISTORY_STRATIFICATION_CSV,
    LATEST_CONTRACT_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_STRATIFICATION_CSV,
    NO_STOP_EXIT_POLICY_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    STRATIFICATION_COLUMNS,
)


REQUIRED_MODELS = {
    "volume_range_breakout_v2_momentum_continuation",
    "volume_range_breakout_v2_low_base_consolidation",
}
REQUIRED_EXIT_POLICIES = {
    NO_STOP_EXIT_POLICY_ID,
    EMA23_STOP_EXIT_POLICY_ID,
}
REQUIRED_STRATIFICATIONS = {
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "tech_close_gt_ema23",
    "tech_dist_ema23_0_to_15",
    "tech_ret20_0_to_25",
}
FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
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
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def int_value(value: object) -> int:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(parsed):
        fail(f"expected numeric integer value, got {value!r}")
    return int(parsed)


def validate_common(frame: pd.DataFrame, columns: list[str], name: str) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(frame.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} must not contain production decision fields: {forbidden}")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_source() -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source split feature detail must not be empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail must come from split feature audit")
    if not false_only(source.get("approved_for_daily", pd.Series(dtype=str))):
        fail("source detail approved_for_daily must remain false")
    if source.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        fail("source detail source_event_key must be unique")
    source = source[source.get("same_stock_non_overlap_included", pd.Series(dtype=str)).astype(str).eq("True")]
    groups = set(source.get("split_group_id", pd.Series(dtype=str)).astype(str))
    if groups != {"momentum_continuation", "low_base_consolidated"}:
        fail(f"source same-stock non-overlap rows must split into the two expected groups; got {groups}")
    return len(source)


def validate_detail(detail: pd.DataFrame, source_rows: int) -> None:
    validate_common(detail, DETAIL_COLUMNS, "detail")
    if set(detail["model_id"].astype(str)) != REQUIRED_MODELS:
        fail("detail must contain exactly the two v2 research model ids")
    if set(detail["exit_policy_id"].astype(str)) != REQUIRED_EXIT_POLICIES:
        fail("detail must contain both required exit policies")
    if detail[["source_event_key", "exit_policy_id"]].duplicated().any():
        fail("detail must be unique by source_event_key + exit_policy_id")
    if len(detail) != source_rows * len(REQUIRED_EXIT_POLICIES):
        fail(f"detail row count must equal source rows x exit policies; got {len(detail)} vs {source_rows}")
    for exit_policy in REQUIRED_EXIT_POLICIES:
        part = detail[detail["exit_policy_id"].astype(str).eq(exit_policy)]
        overlap = part.groupby("source_event_key")["model_id"].nunique()
        if overlap.gt(1).any():
            fail(f"one source_event_key appears in both models for exit_policy={exit_policy}")
        if part["source_event_key"].nunique() != source_rows:
            fail(f"union of two models must equal source sample for exit_policy={exit_policy}")
    invalid = detail[detail["return_valid"].astype(str).ne("True")]
    if len(invalid) >= len(detail):
        fail("all detail returns are invalid")
    if detail["confirmation_rule_id"].astype(str).ne("next_day_continuation_confirmed_close_only").any():
        fail("detail confirmation_rule_id must be close-only next_day_continuation")
    if detail["entry_rule_id"].astype(str).ne("confirmation_next_open").any():
        fail("detail entry_rule_id must be confirmation_next_open")


def validate_contract(contract: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_common(contract, CONTRACT_COLUMNS, "contract")
    model_contract = contract[contract["row_type"].astype(str).eq("model_contract")]
    if set(model_contract["model_id"].astype(str)) != REQUIRED_MODELS or len(model_contract) != 2:
        fail("contract must contain exactly two model_contract rows")
    if set(model_contract["production_registry_change"].astype(str)) != {"False"}:
        fail("model_contract rows must explicitly set production_registry_change=False")
    if set(model_contract["extra_condition_policy"].astype(str)) != {"stratification_only_no_hidden_gate"}:
        fail("model_contract rows must forbid hidden gates")
    if set(model_contract["base_metric_scope"].astype(str)) != {"confirmed_same_stock_non_overlap_only"}:
        fail("model_contract rows must define confirmed-only base metric scope")

    base = contract[contract["row_type"].astype(str).eq("base_performance")]
    expected_pairs = {(model, exit_policy) for model in REQUIRED_MODELS for exit_policy in REQUIRED_EXIT_POLICIES}
    observed_pairs = set(zip(base["model_id"].astype(str), base["exit_policy_id"].astype(str)))
    if observed_pairs != expected_pairs:
        fail(f"base_performance rows mismatch: {observed_pairs}")
    for _, row in base.iterrows():
        model_id = row["model_id"]
        exit_policy = row["exit_policy_id"]
        part = detail[
            detail["model_id"].astype(str).eq(model_id)
            & detail["exit_policy_id"].astype(str).eq(exit_policy)
            & detail["return_valid"].astype(str).eq("True")
        ]
        if int_value(row["sample_size"]) != len(part):
            fail(f"base sample_size mismatch for {model_id} {exit_policy}")
        outcomes = part["return_outcome"].astype(str)
        if int_value(row["win_count"]) != int(outcomes.eq("win").sum()):
            fail(f"win_count mismatch for {model_id} {exit_policy}")
        if int_value(row["loss_count"]) != int(outcomes.eq("loss").sum()):
            fail(f"loss_count mismatch for {model_id} {exit_policy}")
        for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct"]:
            values = numeric(pd.Series([row[col]]))
            if values.dropna().lt(0).any() or values.dropna().gt(100).any():
                fail(f"{col} out of range for {model_id} {exit_policy}")


def validate_stratification(stratification: pd.DataFrame, contract: pd.DataFrame) -> None:
    validate_common(stratification, STRATIFICATION_COLUMNS, "stratification")
    if set(stratification["condition_role"].astype(str)) != {"stratification_only_not_candidate_or_confirmation_gate"}:
        fail("every stratification row must be stratification-only")
    required_pairs = {(model, exit_policy, strat) for model in REQUIRED_MODELS for exit_policy in REQUIRED_EXIT_POLICIES for strat in REQUIRED_STRATIFICATIONS}
    observed_pairs = set(
        zip(
            stratification["model_id"].astype(str),
            stratification["exit_policy_id"].astype(str),
            stratification["stratification_id"].astype(str),
        )
    )
    missing = sorted(required_pairs - observed_pairs)
    if missing:
        fail(f"missing required stratification rows: {missing[:5]}")
    base = contract[contract["row_type"].astype(str).eq("base_performance")]
    base_lookup = {
        (row["model_id"], row["exit_policy_id"]): int_value(row["sample_size"])
        for _, row in base.iterrows()
    }
    for _, row in stratification.iterrows():
        key = (row["model_id"], row["exit_policy_id"])
        baseline = base_lookup.get(key)
        if baseline is None:
            fail(f"stratification has no matching base row: {key}")
        if int_value(row["baseline_sample_size"]) != baseline:
            fail(f"baseline_sample_size mismatch for stratification {key}")
        if int_value(row["sample_size"]) > baseline:
            fail(f"stratification sample_size exceeds baseline for {key}")
        for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
            values = numeric(pd.Series([row[col]])).dropna()
            if values.lt(0).any() or values.gt(100).any():
                fail(f"{col} out of range in stratification")
    if stratification["decision_hint"].astype(str).str.contains("hidden", case=False, regex=False).any():
        fail("decision_hint must not describe hidden gates")


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
        "research-only",
        "does not change `stock_model_contract_registry.csv`",
        "confirmed same-stock non-overlap samples only",
        "TDCC top20 and 23EMA-like technical conditions are stratification-only rows",
        "not hidden gates",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    source_rows = validate_source()
    detail = read_csv(LATEST_DETAIL_CSV)
    contract = read_csv(LATEST_CONTRACT_CSV)
    stratification = read_csv(LATEST_STRATIFICATION_CSV)
    validate_detail(detail, source_rows)
    validate_contract(contract, detail)
    validate_stratification(stratification, contract)
    validate_history(contract, read_csv(HISTORY_CONTRACT_CSV), "contract")
    validate_history(detail, read_csv(HISTORY_DETAIL_CSV), "detail")
    validate_history(stratification, read_csv(HISTORY_STRATIFICATION_CSV), "stratification")
    validate_markdown()
    print(
        "volume range breakout v2 research contract validation passed "
        f"contract_rows={len(contract)} detail_rows={len(detail)} stratification_rows={len(stratification)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
