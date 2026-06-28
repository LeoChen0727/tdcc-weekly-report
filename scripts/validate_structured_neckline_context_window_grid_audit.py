from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_context_window_grid_audit import (
    CONTEXT_WINDOW_GRID_SCOPE_ID,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_MANUAL_ALIGNMENT_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MANUAL_ALIGNMENT_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MANUAL_ALIGNMENT_COLUMNS,
    MANUAL_LABEL_SCOPE_ID,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    WINDOWS,
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


EXPECTED_CONTEXTS = {
    "bearish",
    "sideways_or_consolidation",
    "slow_uptrend",
    "volatile_mixed",
    "unknown",
}
EXPECTED_FILTERS = {"auto_bearish", "auto_non_bearish", "unknown"}


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


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_constants(frame: pd.DataFrame, label: str, requires_manual_scope: bool = False) -> None:
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "context_window_grid_scope_id": CONTEXT_WINDOW_GRID_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    if requires_manual_scope:
        constants["manual_label_scope_id"] = MANUAL_LABEL_SCOPE_ID
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_windows(frame: pd.DataFrame, label: str) -> None:
    got = sorted(int(value) for value in set(frame["window_sessions_requested"].astype(str)))
    if got != WINDOWS:
        fail(f"{label} windows must be {WINDOWS}; got {got}")


def validate_detail(detail: pd.DataFrame) -> None:
    require_columns(detail, DETAIL_COLUMNS, "detail")
    validate_constants(detail, "detail", requires_manual_scope=True)
    validate_windows(detail, "detail")

    source_events = detail["source_event_key"].nunique()
    expected_rows = source_events * len(WINDOWS)
    if len(detail) != expected_rows:
        fail(f"detail rows must equal source_events * windows; got {len(detail)} vs {expected_rows}")
    if source_events < 300:
        fail(f"detail source events too small for expanded context grid: {source_events}")

    contexts = set(detail["auto_pre_signal_context"].astype(str))
    if not contexts <= EXPECTED_CONTEXTS:
        fail(f"unexpected contexts: {sorted(contexts - EXPECTED_CONTEXTS)}")
    filters = set(detail["auto_context_filter_result"].astype(str))
    if not filters <= EXPECTED_FILTERS:
        fail(f"unexpected context filter values: {sorted(filters - EXPECTED_FILTERS)}")

    manual_rows = detail.loc[detail["manual_label_status"].ne("unlabeled")]
    if manual_rows["source_event_key"].nunique() < 10:
        fail("detail must retain at least 10 manually labeled unique events")

    if FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns):
        fail(f"detail contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns))}")


def validate_summary(summary: pd.DataFrame) -> None:
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    if summary.empty:
        fail("summary must not be empty")
    validate_constants(summary, "summary")
    validate_windows(summary, "summary")
    if "low_position_le60_market_bull" not in set(summary["analysis_scope_id"].astype(str)):
        fail("summary must include low_position_le60_market_bull scope")
    if FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns):
        fail(f"summary contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns))}")


def validate_manual_alignment(alignment: pd.DataFrame) -> None:
    require_columns(alignment, MANUAL_ALIGNMENT_COLUMNS, "manual_alignment")
    if alignment.empty:
        fail("manual_alignment must not be empty")
    validate_constants(alignment, "manual_alignment", requires_manual_scope=True)
    validate_windows(alignment, "manual_alignment")
    if "window_non_conflict_total" not in set(alignment["alignment_scope_id"].astype(str)):
        fail("manual_alignment must include window_non_conflict_total")
    totals = alignment.loc[alignment["alignment_scope_id"].eq("window_non_conflict_total")]
    if totals.empty or not (pd.to_numeric(totals["manual_good_rows"], errors="coerce").fillna(0) > 0).all():
        fail("manual_alignment window_non_conflict_total must contain manual good rows")
    if FORBIDDEN_PRODUCTION_FIELDS & set(alignment.columns):
        fail(f"manual_alignment contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(alignment.columns))}")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    alignment = read_csv(LATEST_MANUAL_ALIGNMENT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_alignment = read_csv(HISTORY_MANUAL_ALIGNMENT_CSV)

    validate_detail(detail)
    validate_detail(history_detail)
    validate_summary(summary)
    validate_summary(history_summary)
    validate_manual_alignment(alignment)
    validate_manual_alignment(history_alignment)

    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")

    print(
        "structured neckline context window grid audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)} manual_alignment_rows={len(alignment)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
