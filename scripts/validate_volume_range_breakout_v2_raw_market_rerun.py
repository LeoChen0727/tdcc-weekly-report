from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_raw_market_rerun import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    NEXT_DAY_TRIGGER_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_RESEARCH_ID,
    SOURCE_TIMING_DETAIL_CSV,
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


def require_single(summary: pd.DataFrame, row_type: str, audit_scope: str, audit_key: str) -> pd.Series:
    rows = summary[
        summary["row_type"].astype(str).eq(row_type)
        & summary["audit_scope"].astype(str).eq(audit_scope)
        & summary["audit_key"].astype(str).eq(audit_key)
    ]
    if len(rows) != 1:
        fail(f"expected exactly one summary row for {row_type}/{audit_scope}/{audit_key}; got {len(rows)}")
    return rows.iloc[0]


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame, history_summary: pd.DataFrame, history_detail: pd.DataFrame) -> None:
    if summary.empty:
        fail("summary output must not be empty")
    if detail.empty:
        fail("detail output must not be empty")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"raw rerun outputs must not contain production decision fields: {forbidden}")
    for name, df in [("summary", summary), ("detail", detail)]:
        if set(df["research_id"].astype(str)) != {RESEARCH_ID}:
            fail(f"{name} research_id must be {RESEARCH_ID}")
        if set(df["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
        if set(df["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
            fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
        if set(df["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
            fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
        if set(df["model_id"].astype(str)) != {MODEL_ID}:
            fail(f"{name} model_id must be {MODEL_ID}")
        if set(df["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(df["approved_for_daily"]):
            fail(f"{name} approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame) -> None:
    if detail["source_event_key"].duplicated().any():
        dupes = detail[detail["source_event_key"].duplicated()]["source_event_key"].head(5).tolist()
        fail(f"detail contains duplicate source_event_key values: {dupes}")
    if set(detail["base_v1_signal"].astype(str)) != {"True"}:
        fail("every raw rerun detail row must be a base v1 signal")
    if set(detail["high_breakout_60d_met"].astype(str)) != {"True"}:
        fail("every raw rerun detail row must meet previous 60d high breakout")
    if set(detail["next_day_continuation_confirmed"].astype(str)) != {"True"}:
        fail("every raw rerun detail row must have next_day_continuation_confirmed")
    if set(detail["follow_through_type"].astype(str)) != {"next_day_continuation"}:
        fail("every raw rerun detail row must use the exact matrix follow_through_type=next_day_continuation")
    if set(detail["known_before_entry_open"].astype(str)) != {"True"}:
        fail("every raw rerun detail row must be known before entry open")
    if detail["uses_post_entry_information"].astype(str).eq("True").any():
        fail("raw rerun must not use post-entry information")
    if set(detail["trigger_id_required"].astype(str)) != {NEXT_DAY_TRIGGER_ID}:
        fail(f"trigger_id_required must be {NEXT_DAY_TRIGGER_ID}")
    if set(detail["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("entry_rule_id must remain confirmation_next_open")
    if not (detail["entry_date"].astype(str) > detail["confirmation_date"].astype(str)).all():
        fail("entry_date must be after confirmation_date")
    if not (detail["confirmation_date"].astype(str) > detail["signal_date"].astype(str)).all():
        fail("confirmation_date must be after signal_date")
    if not set(detail["anomaly_flag"].astype(str)) <= {"none", "bottom_1pct_return", "top_1pct_return"}:
        fail("anomaly_flag contains unexpected values")
    if not detail["anomaly_flag"].astype(str).ne("none").any():
        fail("detail must mark top/bottom 1pct anomaly candidates")


def validate_membership(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    timing = read_csv(SOURCE_TIMING_DETAIL_CSV)
    timing_60 = timing[
        timing.get("high_breakout_60d_met", pd.Series(dtype=str)).astype(str).eq("True")
        & timing.get("known_before_entry_open", pd.Series(dtype=str)).astype(str).eq("True")
    ].copy()
    if timing_60.empty:
        fail("source timing audit 60d subset must not be empty")
    raw_keys = set(detail["source_event_key"].astype(str))
    timing_keys = set(timing_60["source_event_key"].astype(str))
    raw_minus_timing = raw_keys - timing_keys
    timing_minus_raw = timing_keys - raw_keys
    timing_max_signal_date = str(timing_60["signal_date"].astype(str).max())
    raw_minus_detail = detail[detail["source_event_key"].astype(str).isin(raw_minus_timing)].copy()
    raw_minus_within_timing = raw_minus_detail[
        raw_minus_detail["signal_date"].astype(str).le(timing_max_signal_date)
    ].copy()
    if timing_minus_raw:
        fail(f"timing audit 60d subset has rows absent from raw rerun: {sorted(timing_minus_raw)[:5]}")
    metrics = require_single(
        summary,
        "raw_market_metrics",
        "all_raw_v2_mature_events",
        "prev60_high_next_day_continuation",
    )
    if int(metrics["sample_size"]) != len(detail):
        fail("raw market summary sample_size must match detail rows")
    if int(metrics["timing_audit_60d_event_count"]) != len(timing_60):
        fail("timing_audit_60d_event_count must match source timing 60d subset rows")
    if int(metrics["timing_minus_raw_count"]) != 0:
        fail("timing_minus_raw_count must be zero")
    if int(metrics["raw_extension_after_timing_count"]) + int(metrics["raw_minus_timing_within_timing_window_count"]) != len(raw_minus_timing):
        fail("raw-minus-timing rows must be fully classified as source gap or freshness extension")
    if int(metrics["future_leak_count"]) != 0:
        fail("future_leak_count must be zero")
    allowed_status = {
        "raw_rerun_matches_timing_window",
        "raw_rerun_matches_timing_window_with_freshness_extension",
        "raw_rerun_detected_timing_source_gap_research_only",
    }
    if metrics["status"] not in allowed_status:
        fail("raw rerun status must record timing-window result")
    timing_minus_row = require_single(summary, "membership_check", "raw_vs_timing_audit_60d", "timing_minus_raw_count")
    if int(timing_minus_row["sample_size"]) != 0 or timing_minus_row["status"] != "match":
        fail("timing_minus_raw_count must be zero/match")
    within_row = require_single(summary, "membership_check", "raw_vs_timing_audit_60d", "raw_minus_timing_within_timing_window_count")
    if int(within_row["sample_size"]) != len(raw_minus_within_timing):
        fail("raw_minus_timing_within_timing_window_count must match classified source-gap rows")
    if raw_minus_within_timing.empty:
        if within_row["status"] != "match":
            fail("zero within-window raw-minus rows must be status=match")
    else:
        if within_row["status"] != "source_gap_detected_promotion_blocker":
            fail("within-window raw-minus rows must be classified as a promotion-blocking source gap")
    for key in ["timing_minus_raw_count"]:
        row = require_single(summary, "membership_check", "raw_vs_timing_audit_60d", key)
        if int(row["sample_size"]) != 0 or row["status"] != "match":
            fail(f"membership check {key} must be zero/match")
    raw_minus_row = require_single(summary, "membership_check", "raw_vs_timing_audit_60d", "raw_minus_timing_count")
    if int(raw_minus_row["sample_size"]) != len(raw_minus_timing):
        fail("raw_minus_timing_count membership row must match raw-minus set size")
    if raw_minus_timing and raw_minus_row["status"] not in {"freshness_extension_after_timing_window", "source_gap_plus_freshness_extension"}:
        fail("raw_minus_timing_count must be classified as freshness extension or source gap plus extension")


def validate_metric_sanity(summary: pd.DataFrame) -> None:
    metrics = require_single(
        summary,
        "raw_market_metrics",
        "all_raw_v2_mature_events",
        "prev60_high_next_day_continuation",
    )
    if int(metrics["scanned_price_files"]) <= 0:
        fail("scanned_price_files must be positive")
    if int(metrics["equity_price_files"]) <= 0:
        fail("equity_price_files must be positive")
    if int(metrics["base_v1_signal_count"]) <= int(metrics["v2_raw_candidate_count"]):
        fail("base_v1_signal_count should exceed v2 candidate count")
    if int(metrics["base_v1_mature_trade_count"]) < int(metrics["v2_raw_mature_event_count"]):
        fail("base_v1_mature_trade_count must cover v2 mature event count")
    if int(metrics["next_day_trigger_mature_count"]) < int(metrics["v2_raw_mature_event_count"]):
        fail("next_day_trigger_mature_count must cover exact follow-through v2 mature events")
    if int(metrics["trigger_only_excluded_by_follow_through_count"]) < 0:
        fail("trigger_only_excluded_by_follow_through_count must not be negative")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct"]:
        value = float(metrics[col])
        if value < 0 or value > 100:
            fail(f"{col} must be in 0..100")
    anomaly = require_single(summary, "anomaly_check", "trim_return_tail", "trim_1pct_each_tail")
    if int(anomaly["anomaly_count"]) <= 0:
        fail("anomaly check must mark at least one row")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only",
        "does not change `stock_model_contract_registry.csv`",
        "previous 60d high + 2pct",
        "confirmation next open entry",
        "Membership is compared against the prior timing-audit 60d subset",
        "source-gap blocker before promotion",
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
    validate_detail(detail)
    validate_membership(summary, detail)
    validate_metric_sanity(summary)
    validate_markdown()
    print(f"volume range breakout v2 raw-market rerun validation passed summary_rows={len(summary)} detail_rows={len(detail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
