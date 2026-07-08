from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_w_bottom_operation_sections import (  # noqa: E402
    AUDIT_COLUMNS,
    MODEL_CONFIGS,
    OUTPUT_COLUMNS,
    PDF_SECTIONS,
    PDF_VIEWS,
    SECTION_EMPTY_NOTE_ZH,
    output_paths,
)
from tracking_utils import read_csv, safe_str  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
DAILY_SIGNALS_CSV = ROOT / "output" / "latest" / "daily_candidate_model_signals_for_report_latest.csv"

REQUIRED_ACTIVE_EXIT_RULE_TOKENS = {
    "w_bottom_right_side": ("D+20", "+10%", "D+40"),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def normalize_date_text(value: object) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    text = text.replace("-", "").replace("/", "")
    return text if len(text) == 8 and text.isdigit() else ""


def check_docs_copy(path: Path, errors: list[str]) -> None:
    docs_path = DOCS_LATEST_DIR / path.name
    if not docs_path.exists():
        errors.append(f"missing docs/latest copy: {docs_path.relative_to(ROOT).as_posix()}")
        return
    if path.read_text(encoding="utf-8-sig") != docs_path.read_text(encoding="utf-8-sig"):
        errors.append(f"docs/latest copy does not match output/latest artifact: {path.name}")


def expected_current_signal_count(model_id: str) -> int:
    signals = read_csv(DAILY_SIGNALS_CSV, dtype=str).fillna("")
    if signals.empty or "model_id" not in signals.columns:
        return 0
    part = signals[signals["model_id"].astype(str).str.strip().eq(model_id)].copy()
    if part.empty or "stock_id" not in part.columns:
        return 0
    if {"stock_id", "report_bucket"}.issubset(part.columns):
        return len(part.drop_duplicates(["stock_id", "report_bucket"]))
    return int(part["stock_id"].astype(str).str.strip().replace("", pd.NA).dropna().nunique())


def validate_active_exit_rule_tokens(active: pd.DataFrame, csv_name: str, model_id: str) -> list[str]:
    required_tokens = REQUIRED_ACTIVE_EXIT_RULE_TOKENS.get(model_id, ())
    if not required_tokens or active.empty:
        return []
    errors: list[str] = []
    for _, row in active.iterrows():
        exit_rule = safe_str(row.get("exit_rule_zh"))
        missing = [token for token in required_tokens if token not in exit_rule]
        if missing:
            location = "/".join(
                safe_str(row.get(column)) or "-"
                for column in ("pdf_view", "report_line", "stock_id")
            )
            errors.append(
                f"{csv_name} active row {location} exit_rule_zh missing tokens {missing}: {exit_rule!r}"
            )
    return errors


def validate_section(model_id: str) -> list[str]:
    config = MODEL_CONFIGS[model_id]
    csv_path, md_path, audit_csv_path, audit_md_path = output_paths(config)
    errors: list[str] = []
    for path in (csv_path, md_path, audit_csv_path, audit_md_path):
        if not path.exists():
            errors.append(f"missing W-bottom operation artifact: {path.relative_to(ROOT).as_posix()}")
        else:
            check_docs_copy(path, errors)
    if errors:
        return errors

    section = read_csv(csv_path, dtype=str).fillna("")
    audit = read_csv(audit_csv_path, dtype=str).fillna("")
    if section.empty:
        errors.append(f"{csv_path.name} must not be empty")
        return errors
    missing = sorted(set(OUTPUT_COLUMNS) - set(section.columns))
    if missing:
        errors.append(f"{csv_path.name} missing columns: {missing}")
        return errors
    missing_audit = sorted(set(AUDIT_COLUMNS) - set(audit.columns))
    if missing_audit:
        errors.append(f"{audit_csv_path.name} missing columns: {missing_audit}")

    model_ids = sorted(set(section["model_id"].astype(str)))
    if model_ids != [model_id]:
        errors.append(f"{csv_path.name} must contain only {model_id}, got {model_ids}")

    views = sorted(set(section["pdf_view"].astype(str)))
    if views != sorted(PDF_VIEWS):
        errors.append(f"{csv_path.name} pdf_view must be {sorted(PDF_VIEWS)}, got {views}")
    sections = sorted(set(section["pdf_section"].astype(str)))
    if sections != sorted(PDF_SECTIONS):
        errors.append(f"{csv_path.name} pdf_section must be {sorted(PDF_SECTIONS)}, got {sections}")
    if "pending_confirmation" in sections or "confirmed_unranked_operation" in sections:
        errors.append(f"{csv_path.name} must not expose pending/unranked as W-bottom digest operation sections")

    for pdf_view in PDF_VIEWS:
        for pdf_section in PDF_SECTIONS:
            part = section[
                section["pdf_view"].astype(str).eq(pdf_view)
                & section["pdf_section"].astype(str).eq(pdf_section)
            ]
            if part.empty:
                errors.append(f"{csv_path.name} missing {pdf_view}/{pdf_section} rows")
            if part["row_type"].astype(str).eq("empty_state").any():
                empty = part[part["row_type"].astype(str).eq("empty_state")].iloc[0]
                expected = SECTION_EMPTY_NOTE_ZH[pdf_section]
                if safe_str(empty.get("stock_display")) != expected:
                    errors.append(f"{csv_path.name} {pdf_view}/{pdf_section} empty-state row must say {expected!r}")

    allowed_row_types = {"data", "empty_state"}
    bad_row_types = sorted(set(section["row_type"].astype(str)) - allowed_row_types)
    if bad_row_types:
        errors.append(f"{csv_path.name} has invalid row_type values: {bad_row_types}")
    bad_source_statuses = sorted(set(section["adapter_source_status"].astype(str)) - {"ready"})
    if bad_source_statuses:
        errors.append(f"{csv_path.name} adapter_source_status must be ready, got {bad_source_statuses}")

    expected_metadata = {
        "entry_rule_id": config.entry_rule_id,
        "stop_loss_rule_id": config.stop_loss_rule_id,
        "exit_rule_id": config.exit_rule_id,
        "exit_rule_zh": config.exit_rule_zh,
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "operation_directive_level": "approved_daily_operation_guidance",
    }
    for column, expected in expected_metadata.items():
        observed = sorted(set(section[column].astype(str)))
        if observed != [expected]:
            errors.append(f"{csv_path.name} {column} must be {expected!r}, got {observed}")

    data = section[section["row_type"].astype(str).eq("data")].copy()
    confirmed = data[data["pdf_section"].astype(str).eq("confirmed_operation")]
    active = data[data["pdf_section"].astype(str).eq("active_operation")]
    expected_signal_count = expected_current_signal_count(model_id)
    confirmed_highlight = confirmed[confirmed["pdf_view"].astype(str).eq("highlight")]
    suppressed_current = pd.DataFrame()
    if not audit.empty and "reason" in audit.columns:
        suppressed_current = audit[
            audit["audit_status"].astype(str).eq("lifecycle_suppressed")
            & audit["included_in_daily_adapter"].astype(str).eq("False")
            & audit["reason"].astype(str).eq("same_stock_already_active_operation")
        ].copy()
    confirmed_or_suppressed = len(confirmed_highlight) + len(
        suppressed_current[["stock_id", "report_line"]].drop_duplicates()
    )
    if expected_signal_count and confirmed_or_suppressed != expected_signal_count:
        errors.append(
            f"{csv_path.name} current published signals must become confirmed rows or audited active suppressions: "
            f"expected={expected_signal_count}, got_confirmed={len(confirmed_highlight)}, "
            f"got_suppressed={len(suppressed_current)}"
        )
    if not confirmed.empty:
        if sorted(set(confirmed["row_action_status"].astype(str))) != ["confirmed_buy_candidate"]:
            errors.append(f"{csv_path.name} confirmed data rows must use row_action_status=confirmed_buy_candidate")
        if sorted(set(confirmed["buy_rank_eligible"].astype(str))) != ["True"]:
            errors.append(f"{csv_path.name} confirmed data rows must be buy_rank_eligible=True")
    if not active.empty:
        if sorted(set(active["row_action_status"].astype(str))) != ["active_tracking"]:
            errors.append(f"{csv_path.name} active data rows must use row_action_status=active_tracking")
        if sorted(set(active["buy_rank_eligible"].astype(str))) != ["False"]:
            errors.append(f"{csv_path.name} active data rows must be buy_rank_eligible=False")
        missing_entry = active[active["entry_date"].map(normalize_date_text).eq("")]
        if not missing_entry.empty:
            errors.append(f"{csv_path.name} active rows must have entry_date")
        errors.extend(validate_active_exit_rule_tokens(active, csv_path.name, model_id))
    if not confirmed.empty and not active.empty:
        confirmed_keys = set(
            tuple(item)
            for item in confirmed[["pdf_view", "report_line", "stock_id"]].astype(str).itertuples(index=False, name=None)
        )
        active_keys = set(
            tuple(item)
            for item in active[["pdf_view", "report_line", "stock_id"]].astype(str).itertuples(index=False, name=None)
        )
        overlap = sorted(confirmed_keys & active_keys)
        if overlap:
            errors.append(f"{csv_path.name} stock cannot be both confirmed and active in the same view/report line: {overlap}")

    empty = section[section["row_type"].astype(str).eq("empty_state")]
    if not empty.empty:
        bad_empty_action = empty[empty["row_action_status"].astype(str).ne("empty_state")]
        if not bad_empty_action.empty:
            errors.append(f"{csv_path.name} empty-state rows must use row_action_status=empty_state")
        bad_empty_buy = empty[empty["buy_rank_eligible"].astype(str).ne("False")]
        if not bad_empty_buy.empty:
            errors.append(f"{csv_path.name} empty-state rows must not be buy-rank eligible")

    if audit.empty:
        errors.append(f"{audit_csv_path.name} must not be empty; lifecycle decisions need an audit trail")
    elif sorted(set(audit["model_id"].astype(str))) != [model_id]:
        errors.append(f"{audit_csv_path.name} must contain only {model_id}")
    return errors


def main() -> int:
    errors: list[str] = []
    for model_id in MODEL_CONFIGS:
        errors.extend(validate_section(model_id))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily W-bottom operation section validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
