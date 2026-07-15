from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_price_pullback_23ema_operation_section import (  # noqa: E402
    APPROVAL_VERSION,
    AUDIT_CSV,
    AUDIT_MD,
    BUY_FILTER_ID,
    ENTRY_RULE_ID,
    EXIT_RULE_ID,
    MODEL_ID,
    OPERATION_MODULE_ID,
    OUT_CSV,
    OUT_MD,
    SECTION_EMPTY_NOTE_ZH,
    STOP_LOSS_RULE_ID,
)
from tracking_utils import DOCS_LATEST_DIR, read_csv  # noqa: E402
from validate_daily_operation_adapter_protected_fields import validate_adapter_frame  # noqa: E402


REQUIRED_COLUMNS = {
    "model_id",
    "model_name_zh",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "report_line",
    "display_order",
    "stock_id",
    "stock_display",
    "operation_quality",
    "row_action_status",
    "buy_rank_eligible",
    "signal_date",
    "entry_rule_id",
    "entry_basis_zh",
    "stop_loss_rule_id",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "technical_package_win_rate_zh",
    "technical_package_avg_return_zh",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "buy_filter_id",
    "adapter_source_status",
}

REQUIRED_AUDIT_COLUMNS = {
    "model_id",
    "operation_asof_date",
    "stock_id",
    "signal_date",
    "operation_lifecycle_state",
    "audit_status",
    "included_in_daily_adapter",
    "reason",
}


def validate_mirror(path: Path, errors: list[str]) -> None:
    mirror = DOCS_LATEST_DIR / path.name
    if not mirror.exists():
        errors.append(f"missing docs/latest mirror: {mirror}")
        return
    if path.read_bytes() != mirror.read_bytes():
        errors.append(f"docs/latest mirror differs: {mirror}")


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, AUDIT_CSV, AUDIT_MD]:
        if not path.exists():
            errors.append(f"missing price_pullback operation adapter artifact: {path}")
        else:
            validate_mirror(path, errors)
    return errors


def validate_section(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if df.empty:
        return [f"empty price_pullback operation adapter: {OUT_CSV}"]
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        return [f"price_pullback operation adapter missing columns: {missing}"]
    models = sorted(set(df["model_id"].astype(str)))
    if models != [MODEL_ID]:
        errors.append(f"price_pullback adapter must contain only {MODEL_ID}, got {models}")
    errors.extend(validate_adapter_frame(df, MODEL_ID))
    views = set(df["pdf_view"].astype(str))
    if views != {"highlight", "full"}:
        errors.append(f"price_pullback adapter must contain highlight and full views, got {sorted(views)}")
    sections = set(df["pdf_section"].astype(str))
    if sections != {"confirmed_operation", "active_operation"}:
        errors.append(f"price_pullback adapter must contain confirmed_operation and active_operation only, got {sorted(sections)}")
    for view in ["highlight", "full"]:
        for section in ["confirmed_operation", "active_operation"]:
            part = df[(df["pdf_view"].astype(str).eq(view)) & (df["pdf_section"].astype(str).eq(section))]
            if part.empty:
                errors.append(f"price_pullback adapter missing view/section: {view}/{section}")
            if part["row_type"].astype(str).eq("empty_state").any():
                empty = part[part["row_type"].astype(str).eq("empty_state")]
                expected = SECTION_EMPTY_NOTE_ZH[section]
                if not empty["stock_display"].astype(str).eq(expected).all():
                    errors.append(f"{view}/{section} empty_state must use {expected!r}")
    expected = {
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": OPERATION_MODULE_ID,
        "approval_version": APPROVAL_VERSION,
        "operation_directive_level": "approved_daily_operation_guidance",
        "buy_filter_id": BUY_FILTER_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "adapter_source_status": "ready",
    }
    for col, value in expected.items():
        unexpected = sorted(set(df[col].astype(str)) - {value})
        if unexpected:
            errors.append(f"price_pullback adapter {col} must be {value!r}, got {unexpected}")
    buy_rows = df[df["buy_rank_eligible"].astype(str).eq("True")]
    bad_buy = buy_rows[
        ~(
            buy_rows["pdf_section"].astype(str).eq("confirmed_operation")
            & buy_rows["row_type"].astype(str).eq("data")
            & buy_rows["row_action_status"].astype(str).eq("confirmed_buy_candidate")
        )
    ]
    if not bad_buy.empty:
        errors.append("buy_rank_eligible=True must be limited to confirmed_operation data rows")
    if df.astype(str).agg("|".join, axis=1).str.contains("intraday", case=False, regex=False).any():
        errors.append("price_pullback operation adapter must not use intraday execution semantics")
    if df["row_type"].astype(str).eq("data").any():
        data = df[df["row_type"].astype(str).eq("data")]
        if data["operation_quality"].astype(str).isin(["", "empty_state"]).any():
            errors.append("price_pullback data rows must expose operation_quality")
        confirmed = data[data["pdf_section"].astype(str).eq("confirmed_operation")]
        active = data[data["pdf_section"].astype(str).eq("active_operation")]
        if not confirmed.empty and not active.empty:
            confirmed_keys = set(
                tuple(item)
                for item in confirmed[["pdf_view", "report_line", "stock_id"]]
                .astype(str)
                .itertuples(index=False, name=None)
            )
            active_keys = set(
                tuple(item)
                for item in active[["pdf_view", "report_line", "stock_id"]]
                .astype(str)
                .itertuples(index=False, name=None)
            )
            overlap = sorted(confirmed_keys & active_keys)
            if overlap:
                errors.append(f"price_pullback stock cannot be both confirmed and active in the same view/report line: {overlap}")
    return errors


def validate_audit(audit: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if audit.empty:
        return [f"empty price_pullback operation audit: {AUDIT_CSV}"]
    missing = sorted(REQUIRED_AUDIT_COLUMNS - set(audit.columns))
    if missing:
        return [f"price_pullback operation audit missing columns: {missing}"]
    models = sorted(set(audit["model_id"].astype(str)))
    if models != [MODEL_ID]:
        errors.append(f"price_pullback audit must contain only {MODEL_ID}, got {models}")
    return errors


def main() -> int:
    errors = validate_files()
    section = read_csv(OUT_CSV, dtype=str).fillna("") if OUT_CSV.exists() else pd.DataFrame()
    audit = read_csv(AUDIT_CSV, dtype=str).fillna("") if AUDIT_CSV.exists() else pd.DataFrame()
    if not section.empty:
        errors.extend(validate_section(section))
    if not audit.empty:
        errors.extend(validate_audit(audit))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("price_pullback_23ema operation section validation passed")
    print(f"validated_output={OUT_CSV}")
    print(f"rows={len(section)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
