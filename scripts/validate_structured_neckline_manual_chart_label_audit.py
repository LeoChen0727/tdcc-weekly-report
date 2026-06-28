from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_manual_chart_label_audit import (
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
        fail("detail must contain at least one manual label row")
    validate_constants(detail, "detail")

    labels = set(detail["manual_label"].astype(str))
    if not {"good", "bad"} <= labels:
        fail(f"detail must contain both good and bad labels; got {sorted(labels)}")

    if set(detail["source_match_status"].astype(str)) != {"matched_source_index"}:
        bad = detail.loc[detail["source_match_status"] != "matched_source_index"]
        fail(f"all manual labels must map back to source index rows; bad_rows={len(bad)}")

    missing_paths = [
        path
        for path in detail["manual_label_chart_path_absolute"].astype(str)
        if not Path(path).exists()
    ]
    if missing_paths:
        fail(f"manual label chart files missing: {missing_paths[:5]}")

    bad_names = detail.loc[detail["stock_name"].astype(str).str.contains(r"\?", regex=True)]
    if not bad_names.empty:
        fail(f"stock_name contains mojibake question-mark artifacts; rows={len(bad_names)}")

    if FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns):
        fail(f"detail contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns))}")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    if summary.empty:
        fail("summary must not be empty")
    validate_constants(summary, "summary")

    label_count = pd.to_numeric(summary["label_rows"], errors="coerce").fillna(0).sum()
    if label_count < len(detail):
        fail("summary label_rows should cover at least the detail row count across scopes")

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

    conflicts = int(detail["label_conflict_for_event"].eq("true").sum())
    print(
        "structured neckline manual chart label audit validation passed "
        f"label_rows={len(detail)} summary_rows={len(summary)} conflict_rows={conflicts}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
