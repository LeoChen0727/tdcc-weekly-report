from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_manual_label_context_classifier_audit import (
    CLASSIFIER_AUDIT_SCOPE_ID,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MANUAL_LABEL_SCOPE_ID,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
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

EXPECTED_ALIGNMENTS = {
    "manual_good_auto_non_bearish_match",
    "manual_good_auto_bearish_false_negative",
    "manual_bad_auto_bearish_match",
    "manual_bad_auto_non_bearish_false_positive",
    "manual_label_conflict_not_scored",
    "unscored_or_unknown",
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


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_constants(frame: pd.DataFrame, label: str) -> None:
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "manual_label_scope_id": MANUAL_LABEL_SCOPE_ID,
        "classifier_audit_scope_id": CLASSIFIER_AUDIT_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame) -> None:
    require_columns(detail, DETAIL_COLUMNS, "detail")
    if detail.empty:
        fail("detail must contain manual label classifier rows")
    validate_constants(detail, "detail")

    if set(detail["source_match_status"].astype(str)) != {"matched_auto_context"}:
        bad = detail.loc[detail["source_match_status"] != "matched_auto_context"]
        fail(f"all manual labels must match auto context rows; bad_rows={len(bad)}")

    labels = set(detail["manual_label"].astype(str))
    if not {"good", "bad"} <= labels:
        fail(f"detail must contain both good and bad labels; got {sorted(labels)}")

    alignments = set(detail["classifier_alignment"].astype(str))
    if not alignments <= EXPECTED_ALIGNMENTS:
        fail(f"unexpected classifier alignments: {sorted(alignments - EXPECTED_ALIGNMENTS)}")

    if not set(detail["auto_context_filter_result"].astype(str)) <= {"auto_bearish", "auto_non_bearish", "unknown"}:
        fail("auto_context_filter_result has unexpected values")

    if FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns):
        fail(f"detail contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns))}")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    if summary.empty:
        fail("summary must not be empty")
    validate_constants(summary, "summary")

    alignment_rows = summary.loc[summary["summary_scope_id"].eq("by_classifier_alignment")]
    if alignment_rows.empty:
        fail("summary must include by_classifier_alignment rows")

    total = pd.to_numeric(alignment_rows["label_rows"], errors="coerce").fillna(0).sum()
    if int(total) != len(detail):
        fail(f"by_classifier_alignment label_rows must equal detail rows; got {total} vs {len(detail)}")

    if FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns):
        fail(f"summary contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns))}")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    validate_detail(detail)
    validate_detail(history_detail)
    validate_summary(summary, detail)
    validate_summary(history_summary, history_detail)

    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")

    print(
        "structured neckline manual label context classifier audit validation passed "
        f"label_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
