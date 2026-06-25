from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

BASELINE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
LATEST_EVENTS_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_events_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_latest.md"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_events.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_rule_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
LEFT_ANCHOR_RULE_ID = "nearest_micro_pressure_45d_min15_before_left_low"
BASELINE_EVENT_SET_ID = "baseline_current_detector"
VARIANT_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
PRODUCTION_READINESS = "not_production_ready_research_only"

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "left_anchor_rule_id",
    "left_anchor_rule_reason",
    "symmetry_ratio",
    "signal_date",
    "stock_id",
    "stock_name",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "breakout_date",
    "late_breakout_not_w",
    "second_arc_volume_ratio",
    "tdcc_any_age7",
    "post_confirmation_trigger_id",
    "a_mature",
    "a_return_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
    "dedup_20d_eligible",
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "comparison_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "baseline_present",
    "variant_present",
    "baseline_left_peak_date",
    "variant_left_peak_date",
    "baseline_left_low_date",
    "variant_left_low_date",
    "baseline_neckline_date",
    "variant_neckline_date",
    "baseline_right_low_date",
    "variant_right_low_date",
    "baseline_breakout_date",
    "variant_breakout_date",
    "baseline_a_mature",
    "variant_a_mature",
    "baseline_a_return_pct",
    "variant_a_return_pct",
    "variant_left_anchor_rule_id",
    "variant_left_anchor_rule_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "summary_type",
    "event_set_id",
    "comparison_status",
    "sample_mode",
    "symmetry_ratio",
    "sample_size",
    "unique_stocks",
    "breakout_signal_count",
    "late_breakout_not_w_count",
    "post_confirmation_count",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "tdcc_any_age7_count",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "delta_sample_size_vs_baseline",
    "delta_win_rate_pct_vs_baseline",
    "delta_avg_a_return_pct_vs_baseline",
    "sample_warning",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

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


def normalize_code(value: object) -> str:
    text = str(value).replace("\ufeff", "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def to_number(value: object) -> float:
    text = str(value).replace(",", "").replace("%", "").strip()
    if not text:
        return float("nan")
    try:
        return float(text)
    except ValueError:
        return float("nan")


def true_mask(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_constants(df: pd.DataFrame, require_approved: bool = False) -> None:
    expected = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, value in expected.items():
        values = set(df[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if require_approved and not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def comparable_events(events: pd.DataFrame) -> pd.DataFrame:
    sample = events[
        events["symmetry_ratio"].astype(float).eq(1.5)
        & true_mask(events["dedup_20d_eligible"])
    ].copy()
    sample["stock_id"] = sample["stock_id"].map(normalize_code)
    sample["signal_date"] = sample["signal_date"].astype(str).str.strip()
    return sample.sort_values(["stock_id", "signal_date"]).drop_duplicates(["stock_id", "signal_date"], keep="first")


def validate_events(events: pd.DataFrame, history: pd.DataFrame) -> None:
    validate_constants(events, require_approved=True)
    validate_constants(history, require_approved=True)
    if len(events) != len(history):
        fail("latest/history event row counts differ")
    if events.empty:
        fail("event replay rows must not be empty")
    if len(events) != 3664:
        fail(f"event replay row count must remain 3664; got {len(events)}")
    if set(events["left_anchor_rule_id"].astype(str)) != {LEFT_ANCHOR_RULE_ID}:
        fail("event replay must use only the nearest micro 45 left-anchor rule")
    if events["left_anchor_rule_reason"].astype(str).str.strip().eq("").any():
        fail("left_anchor_rule_reason must not be blank")
    if set(events["sample_mode"].astype(str)) != {"raw_daily_signal"}:
        fail("events sample_mode must remain raw_daily_signal")
    if not set(events["dedup_20d_eligible"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("dedup_20d_eligible must be true/false")
    if comparable_events(events).empty:
        fail("dedup comparable variant events must not be empty")


def validate_detail(detail: pd.DataFrame, history: pd.DataFrame, baseline_events: pd.DataFrame, variant_events: pd.DataFrame) -> None:
    validate_constants(detail, require_approved=True)
    validate_constants(history, require_approved=True)
    if len(detail) != len(history):
        fail("latest/history detail row counts differ")
    if detail.empty:
        fail("comparison detail must not be empty")
    if len(detail) != 588:
        fail(f"comparison detail row count must remain 588; got {len(detail)}")
    statuses = set(detail["comparison_status"].astype(str))
    expected_statuses = {"common", "variant_only", "baseline_only"}
    if not statuses.issubset(expected_statuses):
        fail(f"unexpected comparison statuses: {sorted(statuses)}")
    if "common" not in statuses:
        fail("comparison detail must include common rows")
    expected_counts = {"common": 254, "variant_only": 118, "baseline_only": 216}
    actual_counts = detail["comparison_status"].value_counts().to_dict()
    for status, expected_count in expected_counts.items():
        actual_count = int(actual_counts.get(status, 0))
        if actual_count != expected_count:
            fail(f"{status} detail count must remain {expected_count}; got {actual_count}")
    if not set(detail["baseline_present"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("baseline_present must be true/false")
    if not set(detail["variant_present"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("variant_present must be true/false")
    variant_rows = detail[detail["variant_present"].astype(str).str.lower().eq("true")]
    if set(variant_rows["variant_left_anchor_rule_id"].astype(str)) != {LEFT_ANCHOR_RULE_ID}:
        fail("variant comparison rows must carry the nearest micro rule id")

    expected_union = set(
        zip(
            comparable_events(baseline_events)["stock_id"],
            comparable_events(baseline_events)["signal_date"],
        )
    ) | set(
        zip(
            comparable_events(variant_events)["stock_id"],
            comparable_events(variant_events)["signal_date"],
        )
    )
    actual_union = set(zip(detail["stock_id"].map(normalize_code), detail["signal_date"].astype(str)))
    if actual_union != expected_union:
        fail("comparison detail key union does not match baseline/variant event sets")


def validate_summary(summary: pd.DataFrame, history: pd.DataFrame, detail: pd.DataFrame, baseline_events: pd.DataFrame, variant_events: pd.DataFrame) -> None:
    validate_constants(summary, require_approved=True)
    validate_constants(history, require_approved=True)
    if len(summary) != len(history):
        fail("latest/history summary row counts differ")
    if len(summary) != 6:
        fail(f"summary must contain 6 rows; got {len(summary)}")
    event_sets = set(summary[summary["summary_type"].eq("event_set")]["event_set_id"].astype(str))
    if event_sets != {BASELINE_EVENT_SET_ID, VARIANT_EVENT_SET_ID}:
        fail(f"unexpected event_set summary rows: {sorted(event_sets)}")
    comparison_statuses = set(summary[summary["summary_type"].eq("candidate_set_comparison")]["comparison_status"].astype(str))
    if comparison_statuses != {"all_union", "common", "variant_only", "baseline_only"}:
        fail(f"unexpected comparison summary rows: {sorted(comparison_statuses)}")

    baseline_dedup = comparable_events(baseline_events)
    variant_dedup = comparable_events(variant_events)
    baseline_row = summary[summary["event_set_id"].eq(BASELINE_EVENT_SET_ID)].iloc[0]
    variant_row = summary[summary["event_set_id"].eq(VARIANT_EVENT_SET_ID)].iloc[0]
    if int(to_number(baseline_row["sample_size"])) != len(baseline_dedup):
        fail("baseline summary sample_size does not match baseline events")
    if int(to_number(variant_row["sample_size"])) != len(variant_dedup):
        fail("variant summary sample_size does not match variant events")
    if int(to_number(baseline_row["sample_size"])) != 470:
        fail("baseline summary sample_size must remain 470")
    if int(to_number(variant_row["sample_size"])) != 372:
        fail("variant summary sample_size must remain 372")
    if int(to_number(variant_row["mature_sample_size"])) != 51:
        fail("variant mature_sample_size must remain 51")
    if abs(to_number(variant_row["win_rate_pct"]) - 33.3333) > 0.0002:
        fail("variant win_rate_pct must remain 33.3333")
    if abs(to_number(variant_row["avg_a_return_pct"]) - 0.6943) > 0.0002:
        fail("variant avg_a_return_pct must remain 0.6943")
    if to_number(variant_row["delta_win_rate_pct_vs_baseline"]) <= 0:
        fail("variant win rate delta should remain directionally positive")
    if to_number(variant_row["delta_avg_a_return_pct_vs_baseline"]) <= 0:
        fail("variant average return delta should remain directionally positive")
    if int(to_number(variant_row["baseline_sample_size"])) != len(baseline_dedup):
        fail("variant baseline_sample_size must reference baseline comparable rows")
    if int(to_number(variant_row["delta_sample_size_vs_baseline"])) != len(variant_dedup) - len(baseline_dedup):
        fail("variant delta_sample_size_vs_baseline is inconsistent")

    for status in ["common", "variant_only", "baseline_only"]:
        row = summary[summary["comparison_status"].eq(status)].iloc[0]
        expected = len(detail[detail["comparison_status"].eq(status)])
        if int(to_number(row["sample_size"])) != expected:
            fail(f"{status} comparison sample_size does not match detail")
    all_union = summary[summary["comparison_status"].eq("all_union")].iloc[0]
    if int(to_number(all_union["sample_size"])) != len(detail):
        fail("all_union sample_size does not match detail")


def main() -> int:
    events = read_csv(LATEST_EVENTS_CSV)
    events_history = read_csv(HISTORY_EVENTS_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    summary_history = read_csv(HISTORY_SUMMARY_CSV)
    baseline_events = read_csv(BASELINE_EVENTS_CSV)
    if not LATEST_MD.exists():
        fail(f"missing required markdown file: {LATEST_MD}")

    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    missing_events_history = sorted(REQUIRED_EVENT_COLUMNS - set(events_history.columns))
    missing_detail = sorted(REQUIRED_DETAIL_COLUMNS - set(detail.columns))
    missing_detail_history = sorted(REQUIRED_DETAIL_COLUMNS - set(detail_history.columns))
    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    missing_summary_history = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary_history.columns))
    if missing_events:
        fail(f"{LATEST_EVENTS_CSV} missing columns: {missing_events}")
    if missing_events_history:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events_history}")
    if missing_detail:
        fail(f"{LATEST_DETAIL_CSV} missing columns: {missing_detail}")
    if missing_detail_history:
        fail(f"{HISTORY_DETAIL_CSV} missing columns: {missing_detail_history}")
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    if missing_summary_history:
        fail(f"{HISTORY_SUMMARY_CSV} missing columns: {missing_summary_history}")

    forbidden = sorted(
        (
            set(events.columns)
            | set(events_history.columns)
            | set(detail.columns)
            | set(detail_history.columns)
            | set(summary.columns)
            | set(summary_history.columns)
        )
        & FORBIDDEN_PRODUCTION_FIELDS
    )
    if forbidden:
        fail(f"nearest-micro event replay must not emit production fields: {forbidden}")

    validate_events(events, events_history)
    validate_detail(detail, detail_history, baseline_events, events)
    validate_summary(summary, summary_history, detail, baseline_events, events)

    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "candidate event replay",
        "180-trading-day history gate remains active",
        LEFT_ANCHOR_RULE_ID,
        "not a production model promotion",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(
        "W-bottom nearest micro anchor event replay validation passed "
        f"event_rows={len(events)} detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
