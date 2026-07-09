from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_promotion_readiness_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_MATRIX_CSV,
    HISTORY_SUMMARY_CSV,
    HOLD_DAYS,
    LATEST_DETAIL_CSV,
    LATEST_MATRIX_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MATRIX_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    STOP_POLICIES,
    SUMMARY_COLUMNS,
)


REQUIRED_MODELS = {
    "volume_range_breakout_v2_momentum_continuation",
    "volume_range_breakout_v2_low_base_consolidation",
}
REQUIRED_MATRIX_IDS = {
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "tech_dist_ema23_0_to_15",
    "tech_ret20_0_to_25",
    "tech_ma60_gt_ma120",
    "off120_le40_range120_le60",
    "off120_le30_range120_le45",
    "off240_le50_range240_le80",
    "off240_le40_range240_le60",
    "off120_le40_range120_le60_ma60_gt_ma120",
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
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_source() -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source research contract detail must not be empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail must come from research contract")
    if not false_only(source.get("approved_for_daily", pd.Series(dtype=str))):
        fail("source approved_for_daily must remain false")
    source = source[source.get("exit_policy_id", pd.Series(dtype=str)).astype(str).eq("fixed_d20_close_no_stop_reference")]
    if source["source_event_key"].duplicated().any():
        fail("source_event_key must be unique after source exit policy filter")
    if set(source.get("model_id", pd.Series(dtype=str)).astype(str)) != REQUIRED_MODELS:
        fail("source must contain exactly the two v2 model ids")
    return len(source)


def validate_detail(detail: pd.DataFrame, source_rows: int) -> None:
    validate_common(detail, DETAIL_COLUMNS, "detail")
    if set(detail["model_id"].astype(str)) != REQUIRED_MODELS:
        fail("detail must contain exactly the two v2 model ids")
    observed_hold_days = {int_value(value) for value in detail["holding_days"].unique()}
    if observed_hold_days != set(HOLD_DAYS):
        fail(f"detail holding_days mismatch: {observed_hold_days}")
    if set(detail["stop_policy_id"].astype(str)) != set(STOP_POLICIES):
        fail("detail must contain exactly the required stop policies")
    if detail[["source_event_key", "holding_days", "stop_policy_id"]].duplicated().any():
        fail("detail must be unique by source_event_key + holding_days + stop_policy_id")
    expected = source_rows * len(HOLD_DAYS) * len(STOP_POLICIES)
    if len(detail) != expected:
        fail(f"detail row count mismatch: got {len(detail)} expected {expected}")
    if detail["confirmation_rule_id"].astype(str).ne("next_day_continuation_confirmed_close_only").any():
        fail("detail confirmation_rule_id must remain close-only next-day continuation")
    if detail["entry_rule_id"].astype(str).ne("confirmation_next_open").any():
        fail("detail entry_rule_id must remain confirmation_next_open")
    if detail["return_valid"].astype(str).eq("True").sum() == 0:
        fail("detail has no valid returns")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_common(summary, SUMMARY_COLUMNS, "summary")
    required_row_types = {"base_performance", "trimmed_anomaly_sensitivity", "invalid_return_summary"}
    if set(summary["row_type"].astype(str)) != required_row_types:
        fail("summary row_type set mismatch")
    base = summary[summary["row_type"].astype(str).eq("base_performance")]
    expected_pairs = {
        (model, str(days), stop)
        for model in REQUIRED_MODELS
        for days in HOLD_DAYS
        for stop in STOP_POLICIES
    }
    observed_pairs = set(zip(base["model_id"].astype(str), base["holding_days"].astype(str), base["stop_policy_id"].astype(str)))
    if observed_pairs != expected_pairs:
        fail("base_performance does not cover every model/holding/stop pair")
    for _, row in base.iterrows():
        part = detail[
            detail["model_id"].astype(str).eq(row["model_id"])
            & detail["holding_days"].astype(str).eq(str(int_value(row["holding_days"])))
            & detail["stop_policy_id"].astype(str).eq(row["stop_policy_id"])
        ]
        valid = part[part["return_valid"].astype(str).eq("True")]
        invalid = part[part["return_valid"].astype(str).ne("True")]
        if int_value(row["sample_size"]) != len(valid):
            fail("summary sample_size does not match detail valid rows")
        if int_value(row["invalid_return_count"]) != len(invalid):
            fail("summary invalid_return_count does not match detail")
        returns = pd.to_numeric(valid.get("return_pct", pd.Series(dtype=float)), errors="coerce")
        outcomes = valid["return_outcome"].astype(str)
        if int_value(row["win_count"]) != int(outcomes.eq("win").sum()):
            fail("summary win_count does not match detail")
        if int_value(row["loss_count"]) != int(outcomes.eq("loss").sum()):
            fail("summary loss_count does not match detail")
        if not returns.empty and numeric_value(row["p90_return_pct"]) < numeric_value(row["p10_return_pct"]):
            fail("summary p90_return_pct must be >= p10_return_pct")
        if "research_only_not_production_contract" not in str(row["promotion_blockers"]):
            fail("promotion_blockers must always keep research-only blocker")
        for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "invalid_return_rate_pct", "stop_exit_rate_pct"]:
            value = numeric_value(row[col])
            if not pd.isna(value) and (value < 0 or value > 100):
                fail(f"{col} out of range")


def validate_matrix(matrix: pd.DataFrame, summary: pd.DataFrame) -> None:
    validate_common(matrix, MATRIX_COLUMNS, "matrix")
    if set(matrix["condition_role"].astype(str)) != {"stratification_only_not_candidate_or_confirmation_gate"}:
        fail("matrix condition_role must remain stratification-only")
    missing_ids = REQUIRED_MATRIX_IDS - set(matrix["stratification_id"].astype(str))
    if missing_ids:
        fail(f"missing required stratification ids: {sorted(missing_ids)}")
    base_lookup = {
        (row["model_id"], str(int_value(row["holding_days"])), row["stop_policy_id"]): int_value(row["sample_size"])
        for _, row in summary[summary["row_type"].astype(str).eq("base_performance")].iterrows()
    }
    for _, row in matrix.iterrows():
        key = (row["model_id"], str(int_value(row["holding_days"])), row["stop_policy_id"])
        baseline = base_lookup.get(key)
        if baseline is None:
            fail(f"matrix row has no base row: {key}")
        if int_value(row["baseline_sample_size"]) != baseline:
            fail("matrix baseline_sample_size mismatch")
        if int_value(row["sample_size"]) > baseline:
            fail("matrix sample_size exceeds baseline")
        for col in ["coverage_pct", "win_rate_pct", "neutral_rate_pct", "loss_rate_pct"]:
            value = numeric_value(row[col])
            if not pd.isna(value) and (value < 0 or value > 100):
                fail(f"matrix {col} out of range")
    if matrix["decision_hint"].astype(str).str.contains("hidden", case=False, regex=False).any():
        fail("matrix decision_hint must not describe hidden gates")


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
        "D+10/D+15/D+20/D+30",
        "close-confirmed MA20/EMA23 stop",
        "stratification-only, not hidden gates",
        "Low-Base Redefinition Matrix",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    source_rows = validate_source()
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    matrix = read_csv(LATEST_MATRIX_CSV)
    validate_detail(detail, source_rows)
    validate_summary(summary, detail)
    validate_matrix(matrix, summary)
    validate_history(detail, read_csv(HISTORY_DETAIL_CSV), "detail")
    validate_history(summary, read_csv(HISTORY_SUMMARY_CSV), "summary")
    validate_history(matrix, read_csv(HISTORY_MATRIX_CSV), "matrix")
    validate_markdown()
    print(
        "volume range breakout v2 promotion readiness audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} matrix_rows={len(matrix)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
