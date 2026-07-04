from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_monthly_revenue_coverage_backfill_audit import (  # noqa: E402
    AUDIT_ID,
    DETAIL_COLUMNS,
    DETAIL_CSV,
    DOCS_SUMMARY_CSV,
    DOCS_SUMMARY_MD,
    REQUIRED_MIN_HISTORY_MONTHS,
    REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT,
    REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT,
    SUMMARY_COLUMNS,
    SUMMARY_CSV,
    SUMMARY_MD,
    TARGET_MODEL_IDS,
)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def to_float(value: object) -> float:
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def to_int(value: object) -> int:
    try:
        return int(float(str(value)))
    except (TypeError, ValueError):
        return 0


def validate_mirrors(errors: list[str]) -> None:
    for left, right in [(SUMMARY_CSV, DOCS_SUMMARY_CSV), (SUMMARY_MD, DOCS_SUMMARY_MD)]:
        if not left.exists():
            errors.append(f"missing monthly revenue coverage audit artifact: {left.as_posix()}")
            continue
        if not right.exists():
            errors.append(f"missing monthly revenue coverage audit mirror: {right.as_posix()}")
            continue
        if left.read_bytes() != right.read_bytes():
            errors.append(f"monthly revenue coverage audit mirror differs: {right.as_posix()}")


def validate_summary(summary: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = set(SUMMARY_COLUMNS) - set(summary.columns)
    if missing:
        errors.append(f"monthly revenue coverage audit summary missing columns: {sorted(missing)}")
        return errors
    if summary.empty:
        errors.append("monthly revenue coverage audit summary is empty")
        return errors
    if set(summary["audit_id"].astype(str)) != {AUDIT_ID}:
        errors.append("monthly revenue coverage audit summary has unexpected audit_id")
    required_scopes = {
        "canonical_monthly_revenue_history",
        "monthly_revenue_point_in_time_panel",
        "daily_model_signal_log_all_models",
        *{f"model:{model_id}" for model_id in TARGET_MODEL_IDS},
    }
    missing_scopes = required_scopes - set(summary["scope"].astype(str))
    if missing_scopes:
        errors.append(f"monthly revenue coverage audit missing required scopes: {sorted(missing_scopes)}")

    for _, row in summary.iterrows():
        ready = str(row.get("formal_model_revenue_gate_ready", "")) == "True"
        backfill_required = str(row.get("backfill_required", "")) == "True"
        history_months = to_int(row.get("history_revenue_period_count"))
        row_coverage = to_float(row.get("asof_row_coverage_pct"))
        stock_coverage = to_float(row.get("asof_stock_coverage_pct"))
        signal_rows = to_int(row.get("signal_rows"))
        if ready:
            if backfill_required:
                errors.append(f"scope {row.get('scope')} cannot be ready while backfill_required=True")
            if history_months < REQUIRED_MIN_HISTORY_MONTHS:
                errors.append(f"scope {row.get('scope')} cannot be ready with insufficient history months")
            if signal_rows > 0 and row_coverage < REQUIRED_MIN_SIGNAL_ROW_COVERAGE_PCT:
                errors.append(f"scope {row.get('scope')} cannot be ready with insufficient row coverage")
            if signal_rows > 0 and stock_coverage < REQUIRED_MIN_SIGNAL_STOCK_COVERAGE_PCT:
                errors.append(f"scope {row.get('scope')} cannot be ready with insufficient stock coverage")
        if backfill_required and not str(row.get("backfill_recommendation", "")):
            errors.append(f"scope {row.get('scope')} requires a backfill recommendation")
    return errors


def validate_detail(detail: pd.DataFrame, summary: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = set(DETAIL_COLUMNS) - set(detail.columns)
    if missing:
        errors.append(f"monthly revenue coverage audit detail missing columns: {sorted(missing)}")
        return errors
    all_scope = summary[summary["scope"].astype(str).eq("daily_model_signal_log_all_models")]
    expected_rows = to_int(all_scope.iloc[0]["signal_rows"]) if not all_scope.empty else 0
    if len(detail) != expected_rows:
        errors.append(f"monthly revenue coverage audit detail row count {len(detail)} != summary signal_rows {expected_rows}")
    statuses = set(detail["coverage_status"].astype(str)) if not detail.empty else set()
    allowed_statuses = {
        "ready_asof_history_row",
        "missing_stock_in_monthly_revenue_history",
        "missing_asof_revenue_on_or_before_signal_date",
    }
    if statuses - allowed_statuses:
        errors.append(f"monthly revenue coverage audit detail has unexpected statuses: {sorted(statuses - allowed_statuses)}")
    ready_detail = detail[detail["formal_model_revenue_gate_ready"].astype(str).eq("True")]
    if not ready_detail.empty:
        errors.append("monthly revenue coverage audit detail must not mark formal_model_revenue_gate_ready=True")
    return errors


def main() -> int:
    errors: list[str] = []
    validate_mirrors(errors)
    try:
        summary = read_csv(SUMMARY_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing monthly revenue coverage audit summary: {exc}")
        summary = pd.DataFrame()
    try:
        detail = read_csv(DETAIL_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing monthly revenue coverage audit detail: {exc}")
        detail = pd.DataFrame()
    if not summary.empty:
        errors.extend(validate_summary(summary))
    if not detail.empty and not summary.empty:
        errors.extend(validate_detail(detail, summary))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_monthly_revenue_coverage_backfill_audit_rows={len(summary)}")
    print(f"validated_monthly_revenue_coverage_backfill_audit_detail_rows={len(detail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
