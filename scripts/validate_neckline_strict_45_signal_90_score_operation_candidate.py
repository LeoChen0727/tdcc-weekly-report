from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_neckline_strict_45_signal_90_score_operation_candidate import (
    DETAIL_COLUMNS,
    ENTRY_RULE_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    NEUTRAL_DEFINITION,
    OPERATION_CANDIDATE_ID,
    OUTCOME_DEFINITION_VERSION,
    PARAMETER_SET_ID,
    PDF_METRIC_LABEL,
    PDF_SUBTITLE_NOTE,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SCORE_WINDOW_ROLE,
    SIGNAL_WINDOW_ROLE,
    SOURCE_RISK_RULE_ID,
    SUMMARY_COLUMNS,
    LOSS_DEFINITION,
    WIN_DEFINITION,
    build,
    read_csv,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def close_enough(left: str, right: str, tolerance: float = 0.0002) -> bool:
    if not left and not right:
        return True
    try:
        return abs(float(left) - float(right)) <= tolerance
    except ValueError:
        return False


def validate_constants(frame: pd.DataFrame, label: str) -> None:
    constants = {
        "model_id": MODEL_ID,
        "operation_candidate_id": OPERATION_CANDIDATE_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "source_risk_rule_id": SOURCE_RISK_RULE_ID,
        "signal_window_role": SIGNAL_WINDOW_ROLE,
        "score_window_role": SCORE_WINDOW_ROLE,
        "outcome_definition_version": OUTCOME_DEFINITION_VERSION,
        "win_definition": WIN_DEFINITION,
        "neutral_definition": NEUTRAL_DEFINITION,
        "loss_definition": LOSS_DEFINITION,
        "pdf_metric_label": PDF_METRIC_LABEL,
        "pdf_subtitle_note": PDF_SUBTITLE_NOTE,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        if column not in frame.columns:
            continue
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame, label: str) -> None:
    require_columns(detail, DETAIL_COLUMNS, label)
    if detail.empty:
        fail(f"{label} must not be empty")
    validate_constants(detail, label)
    if set(detail["filter_45"].astype(str)) != {"auto_non_bearish"}:
        fail(f"{label} filter_45 must be the entry signal gate and equal auto_non_bearish")
    if "auto_bearish" not in set(detail["filter_90"].astype(str)):
        fail(f"{label} must keep some filter_90=auto_bearish rows to prove 90d is not an entry exclusion")
    if not detail["score_window_role"].astype(str).str.contains("not_entry_exclusion", regex=False).all():
        fail(f"{label} score_window_role must state that 90d is not an entry exclusion")
    statuses = set(detail["tradability_status"].astype(str))
    if not statuses <= {"tradable", "missing_price_history_file", "confirmation_signal_date_missing", "missing_next_open_after_confirmation", "insufficient_exit_window", "invalid_confirmation_entry_price"}:
        fail(f"{label} unexpected tradability_status: {sorted(statuses)}")
    tradable = detail["tradability_status"].astype(str).eq("tradable")
    if not tradable.any():
        fail(f"{label} must include tradable rows")
    outcomes = set(detail.loc[tradable, "outcome_result"].astype(str))
    if not outcomes <= {"win", "neutral", "loss"}:
        fail(f"{label} unexpected outcome_result: {sorted(outcomes)}")
    if len(detail[detail["entry_rule_id"].astype(str).eq(ENTRY_RULE_ID)]) != len(detail):
        fail(f"{label} must contain only selected entry rule {ENTRY_RULE_ID}")
    for column in ["confirmation_entry_price", "return_pct", "max_close_return_pct", "min_close_return_pct", "score_adjustment_points"]:
        values = pd.to_numeric(detail.loc[tradable, column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {column} must be numeric for tradable rows")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_summary(summary: pd.DataFrame, label: str) -> None:
    require_columns(summary, SUMMARY_COLUMNS, label)
    if len(summary) != 1:
        fail(f"{label} must contain one selected operation candidate row; got {len(summary)}")
    validate_constants(summary, label)
    row = summary.iloc[0]
    if int(row["source_candidate_count"]) < int(row["confirmation_candidate_count"]):
        fail(f"{label} source_candidate_count must be >= confirmation_candidate_count")
    if int(row["filter90_auto_bearish_source_count"]) <= 0:
        fail(f"{label} must show 90d bearish source rows were retained for scoring")
    if int(row["filter90_auto_bearish_confirmed_count"]) <= 0:
        fail(f"{label} must show confirmed 90d bearish rows were retained for scoring")
    pure = float(row["pure_win_rate_pct"])
    inclusive = float(row["neutral_inclusive_success_rate_pct"])
    if pure < 50.0:
        fail(f"{label} pure win rate unexpectedly below 50%: {pure}")
    if inclusive < 60.0:
        fail(f"{label} neutral-inclusive success rate unexpectedly below 60%: {inclusive}")
    if "promotion_candidate" not in str(row["candidate_status"]):
        fail(f"{label} candidate_status must remain promotion-candidate only")
    if "research advisory only" not in str(row["promotion_boundary"]):
        fail(f"{label} promotion_boundary must keep research-only boundary")
    if "final return is positive" not in str(row["loss_definition"]):
        fail(f"{label} loss_definition must clarify positive final return can still be an operation-rule loss")
    if "operation-rule" not in str(row["pdf_metric_label"]):
        fail(f"{label} pdf_metric_label must identify operation-rule metrics")
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_rebuild(latest_detail: pd.DataFrame, latest_summary: pd.DataFrame) -> None:
    expected_detail, expected_summary = build("VALIDATION_GENERATED_AT")
    detail_columns = [column for column in DETAIL_COLUMNS if column != "generated_at"]
    summary_columns = [column for column in SUMMARY_COLUMNS if column != "generated_at"]
    latest_detail_cmp = latest_detail[detail_columns].reset_index(drop=True)
    expected_detail_cmp = expected_detail[detail_columns].reset_index(drop=True)
    if len(latest_detail_cmp) != len(expected_detail_cmp):
        fail(f"rebuilt detail row count mismatch: latest={len(latest_detail_cmp)} expected={len(expected_detail_cmp)}")
    metric_columns = {
        "original_entry_price",
        "confirmation_entry_price",
        "exit_price",
        "return_pct",
        "max_close_return_pct",
        "min_close_return_pct",
        "return_45",
        "slope20_45",
        "drawdown_45",
        "return_90",
        "slope20_90",
        "drawdown_90",
        "score_adjustment_points",
        "low_position_120_pct",
        "base_width_pct",
    }
    for idx, row in latest_detail_cmp.iterrows():
        expected = expected_detail_cmp.iloc[idx]
        for column in detail_columns:
            if column in metric_columns:
                if not close_enough(str(row[column]), str(expected[column])):
                    fail(f"detail row {idx} {column} mismatch: latest={row[column]} expected={expected[column]}")
            elif str(row[column]) != str(expected[column]):
                fail(f"detail row {idx} {column} mismatch: latest={row[column]} expected={expected[column]}")
    latest_summary_cmp = latest_summary[summary_columns].reset_index(drop=True)
    expected_summary_cmp = expected_summary[summary_columns].reset_index(drop=True)
    for column in summary_columns:
        left = str(latest_summary_cmp.iloc[0][column])
        right = str(expected_summary_cmp.iloc[0][column])
        if column.endswith("_pct") or column.endswith("_count") or column == "score_adjustment_avg_points":
            if not close_enough(left, right):
                fail(f"summary {column} mismatch: latest={left} expected={right}")
        elif left != right:
            fail(f"summary {column} mismatch: latest={left} expected={right}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = Path(LATEST_MD).read_text(encoding="utf-8", errors="replace")
    required = [
        "production impact: `none`",
        "45-day context is the entry-signal gate",
        "90-day context is score adjustment only, not an entry exclusion",
        "`filter_90=auto_bearish` rows remain eligible",
        "Promotion requires a separate daily_model_maintenance PR",
        "Outcome And PDF Metric Definitions",
        "operation-rule win rate and neutral-inclusive success rate",
        "even if the final return is positive",
        PRODUCTION_READINESS,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    validate_detail(latest_detail, "latest detail")
    validate_detail(history_detail, "history detail")
    validate_summary(latest_summary, "latest summary")
    validate_summary(history_summary, "history summary")
    validate_rebuild(latest_detail, latest_summary)
    validate_markdown()
    row = latest_summary.iloc[0]
    print(
        "neckline strict 45 signal / 90 score operation candidate validation passed "
        f"source={row['source_candidate_count']} confirmed={row['confirmation_candidate_count']} "
        f"tradable={row['tradable_entry_count']} win={row['win_count']} "
        f"neutral={row['neutral_count']} loss={row['loss_count']} "
        f"success={row['neutral_inclusive_success_rate_pct']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
