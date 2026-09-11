from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_lowbase_horizon_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    HORIZONS,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    POPULATIONS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
    SUMMARY_COLUMNS,
    mark_non_overlap,
    normalize_date,
    population_mask,
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

REQUIRED_RETURN_BASIS = {
    "current_semantic_operation_return",
    "signal_next_open_fixed_close",
    "confirmation_next_open_fixed_close",
    "confirmation_next_open_close_signal_low_stop_or_fixed_10d_close",
}
VALID_DATA_QUALITY_FLAGS = {
    "ok",
    "extreme_return_abs_ge80_review",
    "missing_price_history_or_signal_date",
    "missing_price_history_or_confirmation_date",
    "missing_next_trading_day_entry",
    "insufficient_forward_price_window",
    "invalid_entry_or_exit_price",
    "missing_current_operation_return",
    "invalid_stop_level",
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
    text = series.astype(str).map(normalize_date)
    return pd.to_datetime(text, format="%Y%m%d", errors="coerce")


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
        fail(f"research artifact must not contain production decision fields: {forbidden}")
    require_common_frame("summary", summary)
    require_common_frame("detail", detail)
    if set(summary["return_basis"].astype(str)) != REQUIRED_RETURN_BASIS:
        fail("summary must contain current operation and fixed-close return bases")
    if set(detail["return_basis"].astype(str)) != REQUIRED_RETURN_BASIS:
        fail("detail must contain current operation and fixed-close return bases")
    if set(summary["anomaly_policy"].astype(str)) != {"include_extreme_review", "exclude_extreme_review"}:
        fail("summary must contain include_extreme_review and exclude_extreme_review anomaly policies")
    unexpected_quality = sorted(set(detail["data_quality_flag"].astype(str)) - VALID_DATA_QUALITY_FLAGS)
    if unexpected_quality:
        fail(f"detail contains unexpected data_quality_flag values: {unexpected_quality}")


def validate_source_and_detail_membership(detail: pd.DataFrame) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source semantic detail must not be empty")
    if set(source["research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"source detail research_id must be {SOURCE_RESEARCH_ID}")
    if source["source_event_key"].duplicated().any():
        fail("source detail source_event_key must be unique before horizon audit")
    if not false_only(source["approved_for_daily"]):
        fail("source detail approved_for_daily must remain false")

    expected_rows = len(source) * (1 + len(HORIZONS) * 2 + 1)
    if len(detail) != expected_rows:
        fail(f"detail row count {len(detail)} must equal source rows * return bases {expected_rows}")
    if set(detail["source_event_key"].astype(str)) != set(source["source_event_key"].astype(str)):
        fail("detail source_event_key set must match source semantic detail")

    counts = detail.groupby(["source_event_key", "return_basis"], dropna=False).size().reset_index(name="count")
    current_counts = counts[counts["return_basis"].eq("current_semantic_operation_return")]
    signal_fixed_counts = counts[counts["return_basis"].eq("signal_next_open_fixed_close")]
    confirmation_fixed_counts = counts[counts["return_basis"].eq("confirmation_next_open_fixed_close")]
    close_stop_counts = counts[
        counts["return_basis"].eq("confirmation_next_open_close_signal_low_stop_or_fixed_10d_close")
    ]
    if not current_counts["count"].eq(1).all() or len(current_counts) != len(source):
        fail("each source event must have exactly one current_semantic_operation_return detail row")
    if not signal_fixed_counts["count"].eq(len(HORIZONS)).all() or len(signal_fixed_counts) != len(source):
        fail("each source event must have one signal fixed-close detail row for every horizon")
    if not confirmation_fixed_counts["count"].eq(len(HORIZONS)).all() or len(confirmation_fixed_counts) != len(source):
        fail("each source event must have one confirmation fixed-close detail row for every horizon")
    if not close_stop_counts["count"].eq(1).all() or len(close_stop_counts) != len(source):
        fail("each source event must have exactly one close-confirmed stop detail row")

    fixed = detail[detail["return_basis"].isin(["signal_next_open_fixed_close", "confirmation_next_open_fixed_close"])]
    if set(fixed["horizon_days"].astype(str)) != {str(x) for x in HORIZONS}:
        fail("fixed-close detail rows must cover all configured horizons")
    if not fixed["exit_rule_id"].astype(str).str.contains("no_intraday_stop").all():
        fail("fixed-close return rows must not use intraday stop semantics")
    close_stop = detail[
        detail["return_basis"].eq("confirmation_next_open_close_signal_low_stop_or_fixed_10d_close")
    ]
    if set(close_stop["horizon_days"].astype(str)) != {"10"}:
        fail("close-confirmed stop rows must use horizon_days=10")
    if set(close_stop["exit_rule_id"].astype(str)) != {"close_signal_low_stop_next_open_or_fixed_10d_close"}:
        fail("close-confirmed stop rows must use the close-confirmed stop exit rule")
    event_frame = detail.drop_duplicates("source_event_key").copy()
    if len(event_frame) != len(source):
        fail("detail must provide exactly one source-event flag snapshot per source_event_key")
    required_flags = [
        "prev60_high_flag",
        "lowbase_off120_le30_flag",
        "lowbase_off120_le40_flag",
        "deep_low_off240_le30_flag",
        "lowbase_off60_le40_range60_le35_flag",
        "consolidated_any_flag",
        "short_consolidation_flag",
        "long_consolidation_flag",
        "momentum_non_consolidation_flag",
    ]
    missing_flags = sorted(set(required_flags) - set(event_frame.columns))
    if missing_flags:
        fail(f"detail source-event snapshots missing population flags: {missing_flags}")
    for flag in required_flags:
        event_frame[flag] = boolish(event_frame[flag])
    return event_frame


def validate_summary_grid(summary: pd.DataFrame, event_frame: pd.DataFrame) -> None:
    population_ids = [population.population_id for population in POPULATIONS]
    expected_rows = len(population_ids) * (2 + len(HORIZONS) * 4 + 2) * 2
    if len(summary) != expected_rows:
        fail(f"summary row count {len(summary)} must equal expected grid rows {expected_rows}")
    missing_populations = sorted(set(population_ids) - set(summary["population_id"].astype(str)))
    if missing_populations:
        fail(f"summary missing populations: {missing_populations}")

    for population in POPULATIONS:
        pop_rows = summary[summary["population_id"].astype(str).eq(population.population_id)]
        if len(pop_rows) != (2 + len(HORIZONS) * 4 + 2) * 2:
            fail(f"{population.population_id} has unexpected row count {len(pop_rows)}")
        current = pop_rows[pop_rows["return_basis"].eq("current_semantic_operation_return")]
        fixed = pop_rows[pop_rows["return_basis"].isin(["signal_next_open_fixed_close", "confirmation_next_open_fixed_close"])]
        close_stop = pop_rows[
            pop_rows["return_basis"].eq("confirmation_next_open_close_signal_low_stop_or_fixed_10d_close")
        ]
        if set(current["horizon_days"].astype(str)) != {"current"}:
            fail(f"{population.population_id} current rows must use horizon_days=current")
        if set(current["overlap_policy"].astype(str)) != {"all_events", "same_stock_non_overlap"}:
            fail(f"{population.population_id} current rows must include both overlap policies")
        for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
            if len(current[current["anomaly_policy"].astype(str).eq(anomaly_policy)]) != 2:
                fail(f"{population.population_id} current rows missing anomaly_policy={anomaly_policy}")
        for horizon in HORIZONS:
            for return_basis in ["signal_next_open_fixed_close", "confirmation_next_open_fixed_close"]:
                rows = fixed[
                    fixed["horizon_days"].astype(str).eq(str(horizon))
                    & fixed["return_basis"].astype(str).eq(return_basis)
                ]
                if set(rows["overlap_policy"].astype(str)) != {"all_events", "same_stock_non_overlap"}:
                    fail(f"{population.population_id} {return_basis} horizon {horizon} must include both overlap policies")
                for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
                    if len(rows[rows["anomaly_policy"].astype(str).eq(anomaly_policy)]) != 2:
                        fail(
                            f"{population.population_id} {return_basis} horizon {horizon} "
                            f"missing anomaly_policy={anomaly_policy}"
                        )
        if set(close_stop["horizon_days"].astype(str)) != {"10"}:
            fail(f"{population.population_id} close-confirmed stop rows must use horizon 10")
        if set(close_stop["overlap_policy"].astype(str)) != {"all_events", "same_stock_non_overlap"}:
            fail(f"{population.population_id} close-confirmed stop rows must include both overlap policies")
        for anomaly_policy in ["include_extreme_review", "exclude_extreme_review"]:
            if len(close_stop[close_stop["anomaly_policy"].astype(str).eq(anomaly_policy)]) != 2:
                fail(f"{population.population_id} close-confirmed stop rows missing anomaly_policy={anomaly_policy}")

        source_count = int(population_mask(event_frame, population.population_id).sum())
        if numeric(pop_rows["source_event_count"]).dropna().nunique() != 1:
            fail(f"{population.population_id} source_event_count must be stable across rows")
        if int(numeric(pop_rows["source_event_count"]).dropna().iloc[0]) != source_count:
            fail(f"{population.population_id} source_event_count does not match source mask")


def overlap_pair_count(frame: pd.DataFrame) -> int:
    if frame.empty:
        return 0
    work = frame.copy()
    work["_signal_dt"] = parse_yyyymmdd(work["signal_date"])
    work["_exit_dt"] = parse_yyyymmdd(work["exit_date"])
    if work["_signal_dt"].isna().any() or work["_exit_dt"].isna().any():
        fail("non-overlap frame has unparseable signal_date or exit_date")
    count = 0
    for _, part in work.sort_values(["stock_id", "_signal_dt", "_exit_dt", "source_event_key"]).groupby(
        "stock_id", dropna=False
    ):
        active: list[pd.Series] = []
        for _, row in part.iterrows():
            for prior in active:
                if row["_signal_dt"] <= prior["_exit_dt"]:
                    count += 1
            active = [prior for prior in active if prior["_exit_dt"] >= row["_signal_dt"]]
            active.append(row)
    return count


def validate_non_overlap_replay(summary: pd.DataFrame, detail: pd.DataFrame, event_frame: pd.DataFrame) -> None:
    for population in POPULATIONS:
        source_keys = set(event_frame.loc[population_mask(event_frame, population.population_id), "source_event_key"].astype(str))
        for _, summary_row in summary[summary["population_id"].astype(str).eq(population.population_id)].iterrows():
            basis = str(summary_row["return_basis"])
            horizon = str(summary_row["horizon_days"])
            policy = str(summary_row["overlap_policy"])
            anomaly_policy = str(summary_row["anomaly_policy"])
            detail_part = detail[
                detail["source_event_key"].astype(str).isin(source_keys)
                & detail["return_basis"].astype(str).eq(basis)
                & detail["horizon_days"].astype(str).eq(horizon)
            ].copy()
            valid_flags = ["ok", "extreme_return_abs_ge80_review"]
            if anomaly_policy == "exclude_extreme_review":
                valid_flags = ["ok"]
            elif anomaly_policy != "include_extreme_review":
                fail(f"unexpected anomaly_policy: {anomaly_policy}")
            ok_part = detail_part[detail_part["data_quality_flag"].astype(str).isin(valid_flags)].copy()
            if int(summary_row["simulated_event_count"]) != len(ok_part):
                fail(f"{population.population_id}/{basis}/{horizon}/{policy} simulated_event_count mismatch")
            if int(summary_row["data_quality_exception_count"]) != len(detail_part) - len(ok_part):
                fail(f"{population.population_id}/{basis}/{horizon}/{policy} data_quality_exception_count mismatch")
            if policy == "all_events":
                if int(summary_row["sample_size"]) != len(ok_part):
                    fail(f"{population.population_id}/{basis}/{horizon}/all_events sample_size mismatch")
                if str(summary_row["same_stock_overlap_suppressed_count"]) not in {"0", ""}:
                    fail(f"{population.population_id}/{basis}/{horizon}/all_events must not suppress overlaps")
                continue

            marked = mark_non_overlap(ok_part)
            accepted = marked[marked["_non_overlap"]].copy()
            suppressed = len(ok_part) - len(accepted)
            if int(summary_row["sample_size"]) != len(accepted):
                fail(f"{population.population_id}/{basis}/{horizon}/same_stock_non_overlap sample_size mismatch")
            if int(summary_row["non_overlap_event_count"]) != len(accepted):
                fail(f"{population.population_id}/{basis}/{horizon}/same_stock_non_overlap count mismatch")
            if int(summary_row["same_stock_overlap_suppressed_count"]) != suppressed:
                fail(f"{population.population_id}/{basis}/{horizon}/same_stock_overlap_suppressed_count mismatch")
            if overlap_pair_count(accepted) != 0:
                fail(f"{population.population_id}/{basis}/{horizon} still has same-stock overlapping windows")


def validate_metrics(summary: pd.DataFrame) -> None:
    for col in ["sample_size", "source_event_count", "simulated_event_count", "data_quality_exception_count"]:
        values = numeric(summary[col])
        if values.isna().any() or values.lt(0).any():
            fail(f"{col} must be non-negative numeric")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
        values = numeric(summary[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")
    non_empty = summary[numeric(summary["sample_size"]).gt(0)]
    rate_sum = (
        numeric(non_empty["win_rate_pct"])
        + numeric(non_empty["neutral_rate_pct"])
        + numeric(non_empty["loss_rate_pct"])
    )
    if ((rate_sum - 100.0).abs() > 0.25).any():
        fail("win/neutral/loss rates must sum to about 100 for non-empty rows")
    if summary["sample_status"].astype(str).eq("").any():
        fail("sample_status must be populated")
    if summary["decision_hint"].astype(str).eq("").any():
        fail("decision_hint must be populated")
    if not summary["population_id"].astype(str).str.contains("lowbase|deep_low").any():
        fail("summary must include explicit low-base populations")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only",
        "does not change `stock_model_contract_registry.csv`",
        "Fixed-close horizon returns compare signal next trading day open and confirmation next trading day open entries against fixed future close exits",
        "Close-confirmed stop test uses confirmation next trading day open entry",
        "MFE/MAE use intraday high/low only as advisory diagnostics",
        "Split gate heuristic here is win_rate_pct >= 60 and avg_return_pct > 0",
        "Main tables use `exclude_extreme_review`",
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
    event_frame = validate_source_and_detail_membership(detail)
    validate_summary_grid(summary, event_frame)
    validate_non_overlap_replay(summary, detail, event_frame)
    validate_metrics(summary)
    validate_markdown()
    print(
        "volume range breakout v2 lowbase horizon audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} source_rows={len(event_frame)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
