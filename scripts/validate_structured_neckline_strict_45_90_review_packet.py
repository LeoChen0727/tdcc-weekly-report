from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_strict_45_90_review_packet import (
    CHART_ROOT,
    FLAG_COLUMNS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_FLAG_CSV,
    HISTORY_INDEX_CSV,
    HISTORY_SUMMARY_CSV,
    INDEX_COLUMNS,
    LATEST_FLAG_CSV,
    LATEST_INDEX_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MANUAL_REVIEW_STATUS,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    TARGET_RISK_RULE_ID,
    TARGET_SEGMENT_ID,
    load_source_rows,
    normalize_code,
    normalize_date,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def source_keys() -> set[tuple[str, str, str, str, str]]:
    source = load_source_rows()
    return {
        (
            normalize_code(row.get("stock_id")),
            normalize_date(row.get("signal_date")),
            normalize_date(row.get("retest_date")),
            normalize_date(row.get("retest_attack_date")),
            normalize_date(row.get("retest_entry_date")),
        )
        for _, row in source.iterrows()
    }


def packet_keys(packet: pd.DataFrame) -> set[tuple[str, str, str, str, str]]:
    return {
        (
            normalize_code(row.get("stock_id")),
            normalize_date(row.get("signal_date")),
            normalize_date(row.get("retest_date")),
            normalize_date(row.get("retest_attack_date")),
            normalize_date(row.get("retest_entry_date")),
        )
        for _, row in packet.iterrows()
    }


def validate_index(index: pd.DataFrame, label: str) -> None:
    require_columns(index, INDEX_COLUMNS, label)
    if index.empty:
        fail(f"{label} must not be empty")
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
        "segment_id": TARGET_SEGMENT_ID,
        "manual_review_status": MANUAL_REVIEW_STATUS,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(index[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(index["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")
    outcomes = index["outcome_result"].astype(str).value_counts().to_dict()
    expected_outcomes = {"win": 27, "neutral": 11, "loss": 10}
    if outcomes != expected_outcomes:
        fail(f"{label} outcome counts changed: got={outcomes} expected={expected_outcomes}")
    if packet_keys(index) != source_keys():
        fail(f"{label} event keys do not match strict 45/90 source rows")
    if index.loc[index["outcome_result"].eq("loss"), "review_tags"].astype(str).eq("").any():
        fail(f"{label} loss rows must have review_tags")
    for numeric_column in ["return_pct", "max_close_return_pct", "min_close_return_pct", "reference_price", "stop_level"]:
        values = pd.to_numeric(index[numeric_column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {numeric_column} must be numeric for every row")
    forbidden = sorted(set(index.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_summary(summary: pd.DataFrame, label: str) -> None:
    require_columns(summary, SUMMARY_COLUMNS, label)
    if summary.empty:
        fail(f"{label} must not be empty")
    if "overall" not in set(summary["summary_scope_id"].astype(str)):
        fail(f"{label} must contain overall summary")
    if not false_only(summary["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")
    if set(summary["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{label} production_readiness must be {PRODUCTION_READINESS}")
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_flags(flags: pd.DataFrame, label: str) -> None:
    require_columns(flags, FLAG_COLUMNS, label)
    if flags.empty:
        fail(f"{label} must not be empty")
    if not false_only(flags["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")
    loss_counts = pd.to_numeric(flags["loss_event_count"], errors="coerce").fillna(0)
    if not loss_counts.gt(0).any():
        fail(f"{label} must include at least one loss-linked review flag")
    forbidden = sorted(set(flags.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_charts(index: pd.DataFrame) -> None:
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    png_paths = list(CHART_ROOT.rglob("*.png"))
    if len(png_paths) != len(index):
        fail(f"chart png count mismatch: png={len(png_paths)} rows={len(index)}")
    folders = {path.parent.name for path in png_paths}
    if not {"01_win", "02_neutral", "03_loss"} <= folders:
        fail(f"chart folders missing outcome groups: {sorted(folders)}")
    for row_number, row in index.iterrows():
        chart_path = Path(str(row.get("chart_path", "")))
        if not chart_path.exists():
            fail(f"missing chart at row {row_number}: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"chart must be png at row {row_number}: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"chart suspiciously small at row {row_number}: {chart_path}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown packet: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "production impact: `none`",
        "strict 45/90",
        "review_tags",
        "research-only evidence",
        "does not promote",
        PRODUCTION_READINESS,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    latest_flags = read_csv(LATEST_FLAG_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_flags = read_csv(HISTORY_FLAG_CSV)

    validate_index(latest, "latest index")
    validate_index(history, "history index")
    if len(latest) != len(history):
        fail("latest/history index row counts differ")
    validate_summary(latest_summary, "latest summary")
    validate_summary(history_summary, "history summary")
    validate_flags(latest_flags, "latest flags")
    validate_flags(history_flags, "history flags")
    validate_charts(latest)
    validate_markdown()

    print(
        "structured neckline strict 45/90 review packet validation passed "
        f"rows={len(latest)} charts={len(list(CHART_ROOT.rglob('*.png')))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
