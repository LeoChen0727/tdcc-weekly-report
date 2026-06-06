from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_daily_candidate_model_selection_correctness import audit as selection_audit  # noqa: E402
from build_daily_candidate_model_layer import build_specs  # noqa: E402
from tracking_utils import LATEST_DIR, main_price_date_from_freshness, normalize_date, read_csv, safe_str  # noqa: E402


REPORT_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
SUMMARY = LATEST_DIR / "daily_candidate_model_summary_for_report_latest.csv"
REGISTRY = LATEST_DIR / "daily_report_model_registry_latest.csv"
TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
AUDIT_JSON = LATEST_DIR / "daily_candidate_pipeline_integrity_audit_latest.json"
AUDIT_MD = LATEST_DIR / "daily_candidate_pipeline_integrity_audit_latest.md"


EXPECTED_REPORT_LINES = {"mainstream", "non_mainstream"}
EXPECTED_REPEAT_STATUS = {"new_model_signal", "repeated_same_model_signal"}
ALLOWED_PLACEHOLDER = "欄位尚未完成 / 暫用現有資料"

REQUIRED_REPORT_COLUMNS = {
    "signal_date",
    "report_line",
    "model_id",
    "model_name_zh",
    "stock_id",
    "stock_name",
    "model_score",
    "model_rank",
    "display_rank",
    "why_selected_human_zh",
    "score_components_zh",
    "operation_reminder_zh",
    "source_hit_labels_zh",
    "risk_tags_zh",
    "downgrade_flags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "effective_primary_theme_zh",
    "effective_structural_theme_bucket_zh",
    "tdcc_direction_zh",
    "tdcc_big_holder_summary_zh",
    "same_model_repeat_status",
    "same_model_repeat_status_zh",
    "model_rank_new_signal",
    "model_rank_repeated_signal",
    "display_rank_new_signal",
    "display_rank_repeated_signal",
}

REQUIRED_REGISTRY_COLUMNS = {
    "model_id",
    "model_name_zh",
    "model_registry_order",
    "model_registry_active",
    "report_line_applicability",
    "model_group_zh",
}

REQUIRED_SUMMARY_COLUMNS = {
    "signal_date",
    "report_line",
    "model_id",
    "model_name_zh",
    "model_registry_order",
    "new_signal_stock_display",
    "new_signal_rank_label_zh",
    "repeated_signal_stock_display",
    "repeated_signal_rank_label_zh",
}

REQUIRED_TAXONOMY_COLUMNS = {
    "stock_id",
    "stock_name",
    "basic_theme",
    "mainstream_membership",
    "report_line_memberships",
}

PDF_DISPLAY_COLUMNS = [
    "model_name_zh",
    "source_hit_labels_zh",
    "why_selected_zh",
    "why_selected_human_zh",
    "risk_tags_zh",
    "downgrade_flags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "operation_reminder_zh",
    "effective_primary_theme_zh",
    "effective_structural_theme_bucket_zh",
    "warrant_flow_signal_zh",
    "tdcc_status_zh",
    "tdcc_direction_zh",
    "tdcc_big_holder_summary_zh",
    "tdcc_grade_change_summary_zh",
    "tdcc_risk_text_zh",
    "score_components_zh",
    "same_model_repeat_status_zh",
    "same_model_repeat_note_zh",
    "merged_source_categories_zh",
]

FORBIDDEN_PDF_TEXT = [
    "near 23EMA/support",
    "pullback volume not chasing",
    "pullback entry zone",
    "pullback not volume-chasing",
    "EMA23 slope proxy up",
    "re-attack volume",
    "price in 23-day range",
    "price still in recent range",
    "EPS confirmation tag",
    "catalyst tag",
    "hot theme tag",
    "range_rebound",
    "revenue_pullback",
    "revenue_breakout_low_response",
    "pullback_rebound",
    "short_term_specialty",
    "tdcc_short_term_edge",
    "mild_accumulation",
    "strong_accumulation",
    "call_strong_inflow",
    "call_put_bullish",
    "call_inflow",
    "mixed_flow",
    "no_signal",
    "non_mainstream",
    "mainstream",
    "profile=",
    "base=",
]

RAW_SLUG_RE = re.compile(r"(^|[\s|/、,;:])([a-z]+(?:_[a-z0-9]+){1,})(?=$|[\s|/、,;:])")


def _date_delta_days(later: str, earlier: str) -> int | None:
    try:
        later_dt = datetime.strptime(later, "%Y%m%d")
        earlier_dt = datetime.strptime(earlier, "%Y%m%d")
    except ValueError:
        return None
    return (later_dt - earlier_dt).days


def _safe_unique(df: pd.DataFrame, col: str) -> list[str]:
    if df.empty or col not in df.columns:
        return []
    return sorted({safe_str(v) for v in df[col].astype(str) if safe_str(v)})


def _missing_columns(df: pd.DataFrame, required: set[str]) -> list[str]:
    return sorted(required - set(df.columns))


def _text_has_forbidden(value: str) -> list[str]:
    text = safe_str(value)
    hits = [token for token in FORBIDDEN_PDF_TEXT if token.lower() in text.lower()]
    slug_match = RAW_SLUG_RE.search(text)
    if slug_match:
        token = slug_match.group(2)
        allowed = {"TDCC", "MACD", "RSI", "KD", "OBV", "CMF", "ATR"}
        if token.upper() not in allowed:
            hits.append(token)
    return sorted(set(hits))


def _check_report_display_text(signals: pd.DataFrame, errors: list[str], details: dict[str, Any]) -> None:
    leaks: dict[str, int] = {}
    examples: dict[str, list[str]] = {}
    for col in PDF_DISPLAY_COLUMNS:
        if col not in signals.columns:
            continue
        count = 0
        col_examples: list[str] = []
        for value in signals[col].astype(str):
            hits = _text_has_forbidden(value)
            if not hits:
                continue
            count += 1
            if len(col_examples) < 5:
                col_examples.append(f"{hits[0]} => {safe_str(value)[:120]}")
        if count:
            leaks[col] = count
            examples[col] = col_examples
    details["pdf_facing_text_leak_counts"] = leaks
    if examples:
        details["pdf_facing_text_leak_examples"] = examples
    if leaks:
        errors.append(f"pdf-facing display columns contain raw English slug/text: {leaks}")


def _check_registry_and_summary(
    registry: pd.DataFrame,
    summary: pd.DataFrame,
    main_date: str,
    errors: list[str],
    details: dict[str, Any],
) -> None:
    if registry.empty:
        errors.append(f"missing_or_empty: {REGISTRY}")
        return
    missing = _missing_columns(registry, REQUIRED_REGISTRY_COLUMNS)
    if missing:
        errors.append(f"registry_missing_columns: {missing}")
        return

    active = registry[registry["model_registry_active"].astype(str).str.lower().isin({"1", "true", "yes", "y"})].copy()
    pdf_models = active[active["report_line_applicability"].astype(str).isin(["both", "mainstream", "non_mainstream"])]
    details["registry_active_model_count"] = int(len(active))
    details["registry_pdf_model_count"] = int(len(pdf_models))
    details["registry_model_ids"] = _safe_unique(pdf_models, "model_id")

    bad_applicability = sorted(
        set(registry["report_line_applicability"].astype(str)) - {"both", "mainstream", "non_mainstream", "research_only"}
    )
    if bad_applicability:
        errors.append(f"registry_invalid_report_line_applicability: {bad_applicability}")

    if summary.empty:
        errors.append(f"missing_or_empty: {SUMMARY}")
        return
    missing_summary = _missing_columns(summary, REQUIRED_SUMMARY_COLUMNS)
    if missing_summary:
        errors.append(f"summary_missing_columns: {missing_summary}")
        return

    expected_rows: set[tuple[str, str]] = set()
    for _, row in pdf_models.iterrows():
        model_id = safe_str(row.get("model_id"))
        applicability = safe_str(row.get("report_line_applicability"))
        if applicability in {"both", "mainstream"}:
            expected_rows.add(("mainstream", model_id))
        if applicability in {"both", "non_mainstream"}:
            expected_rows.add(("non_mainstream", model_id))

    actual_rows = {
        (safe_str(row.get("report_line")), safe_str(row.get("model_id")))
        for _, row in summary.iterrows()
        if safe_str(row.get("report_line")) and safe_str(row.get("model_id"))
    }
    missing_rows = sorted(expected_rows - actual_rows)
    extra_rows = sorted(actual_rows - expected_rows)
    details["summary_expected_model_line_rows"] = len(expected_rows)
    details["summary_actual_model_line_rows"] = len(actual_rows)
    if missing_rows:
        errors.append(f"summary_missing_fixed_model_rows: {missing_rows[:20]}")
    if extra_rows:
        errors.append(f"summary_unregistered_model_rows: {extra_rows[:20]}")

    summary_dates = sorted({normalize_date(v) for v in summary["signal_date"].astype(str) if normalize_date(v)})
    details["summary_signal_dates"] = summary_dates
    if main_date and summary_dates != [main_date]:
        errors.append(f"summary_signal_date_mismatch: expected {main_date}, got {summary_dates}")

    dup_summary = int(summary.duplicated(["report_line", "model_id"]).sum())
    if dup_summary:
        errors.append(f"summary_duplicate_report_line_model_rows: {dup_summary}")


def _check_report_signals(signals: pd.DataFrame, registry: pd.DataFrame, main_date: str, errors: list[str], details: dict[str, Any]) -> None:
    if signals.empty:
        errors.append(f"missing_or_empty: {REPORT_SIGNALS}")
        return
    missing = _missing_columns(signals, REQUIRED_REPORT_COLUMNS)
    if missing:
        errors.append(f"report_signals_missing_columns: {missing}")
        return

    dates = sorted({normalize_date(v) for v in signals["signal_date"].astype(str) if normalize_date(v)})
    details["report_signal_dates"] = dates
    if main_date and dates != [main_date]:
        errors.append(f"report_signals_signal_date_mismatch: expected {main_date}, got {dates}")

    bad_lines = sorted(set(signals["report_line"].astype(str)) - EXPECTED_REPORT_LINES)
    if bad_lines:
        errors.append(f"invalid_report_line_values: {bad_lines}")

    dup_count = int(signals.duplicated(["report_line", "model_id", "stock_id"]).sum())
    details["same_report_line_model_stock_duplicates"] = dup_count
    if dup_count:
        errors.append(f"duplicate_report_line_model_stock_rows: {dup_count}")

    bad_repeat = sorted(set(signals["same_model_repeat_status"].astype(str)) - EXPECTED_REPEAT_STATUS)
    if bad_repeat:
        errors.append(f"invalid_same_model_repeat_status_values: {bad_repeat}")

    new_rows = signals["same_model_repeat_status"].astype(str).eq("new_model_signal")
    repeated_rows = signals["same_model_repeat_status"].astype(str).eq("repeated_same_model_signal")
    if signals.loc[new_rows, "display_rank_new_signal"].astype(str).str.strip().eq("").any():
        errors.append("new_model_signal rows missing display_rank_new_signal")
    if signals.loc[new_rows, "display_rank_repeated_signal"].astype(str).str.strip().ne("").any():
        errors.append("new_model_signal rows should not fill display_rank_repeated_signal")
    if signals.loc[repeated_rows, "display_rank_repeated_signal"].astype(str).str.strip().eq("").any():
        errors.append("repeated_same_model_signal rows missing display_rank_repeated_signal")
    if signals.loc[repeated_rows, "display_rank_new_signal"].astype(str).str.strip().ne("").any():
        errors.append("repeated_same_model_signal rows should not fill display_rank_new_signal")

    if signals["why_selected_human_zh"].astype(str).str.contains(r"基礎分\s*=|profile=|base=", regex=True, case=False).any():
        errors.append("why_selected_human_zh contains score breakdown or raw scoring token")
    if signals["operation_reminder_zh"].astype(str).str.strip().isin({"", ALLOWED_PLACEHOLDER}).any():
        errors.append("operation_reminder_zh missing or placeholder")

    active_pdf_models = set()
    if not registry.empty and {"model_id", "model_registry_active", "report_line_applicability"}.issubset(registry.columns):
        active = registry[
            registry["model_registry_active"].astype(str).str.lower().isin({"1", "true", "yes", "y"})
            & registry["report_line_applicability"].astype(str).isin(["both", "mainstream", "non_mainstream"])
        ]
        active_pdf_models = set(active["model_id"].astype(str))
    unknown_models = sorted(set(signals["model_id"].astype(str)) - active_pdf_models) if active_pdf_models else []
    if unknown_models:
        errors.append(f"report_signals_model_not_in_active_registry: {unknown_models}")

    _check_report_display_text(signals, errors, details)


def _check_taxonomy(taxonomy: pd.DataFrame, errors: list[str], details: dict[str, Any]) -> None:
    if taxonomy.empty:
        errors.append(f"missing_or_empty: {TAXONOMY}")
        return
    missing = _missing_columns(taxonomy, REQUIRED_TAXONOMY_COLUMNS)
    if missing:
        errors.append(f"taxonomy_missing_columns: {missing}")
        return
    blank_basic = int(taxonomy["basic_theme"].astype(str).str.strip().eq("").sum())
    blank_membership = int(taxonomy["report_line_memberships"].astype(str).str.strip().eq("").sum())
    details["taxonomy_rows"] = int(len(taxonomy))
    details["taxonomy_blank_basic_theme_rows"] = blank_basic
    details["taxonomy_blank_report_line_memberships"] = blank_membership
    if blank_basic:
        errors.append(f"taxonomy_blank_basic_theme_rows: {blank_basic}")
    if blank_membership:
        errors.append(f"taxonomy_blank_report_line_memberships: {blank_membership}")

    allowed = {"mainstream", "non_mainstream"}
    bad_rows: list[str] = []
    for _, row in taxonomy.iterrows():
        parts = {p.strip() for p in re.split(r"[,|;]", safe_str(row.get("report_line_memberships"))) if p.strip()}
        if not parts or not parts.issubset(allowed):
            bad_rows.append(f"{safe_str(row.get('stock_id'))}:{safe_str(row.get('report_line_memberships'))}")
            if len(bad_rows) >= 20:
                break
    if bad_rows:
        errors.append(f"taxonomy_invalid_report_line_memberships: {bad_rows}")


def _check_model_spec_independence(errors: list[str], details: dict[str, Any]) -> None:
    specs = list(build_specs())
    details["stock_model_spec_count"] = len(specs)
    condition_names = [spec.condition_func.__name__ for spec in specs]
    score_names = [spec.score_func.__name__ for spec in specs]
    details["stock_model_spec_ids"] = [spec.model_id for spec in specs]
    if len(condition_names) != len(set(condition_names)):
        errors.append("stock_models_do_not_have_unique_condition_functions")
    if len(score_names) != len(set(score_names)):
        errors.append("stock_models_do_not_have_unique_score_functions")
    if any(name == "model_score_common" for name in score_names):
        errors.append("stock_model_uses_shared_model_score_common")


def audit() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, Any] = {}
    main_date = main_price_date_from_freshness()
    details["main_price_date"] = main_date

    selection = selection_audit()
    details["selection_audit_status"] = selection.get("status")
    if selection.get("status") != "pass":
        errors.append("selection_correctness_audit_failed")
        for err in selection.get("errors", []):
            errors.append(f"selection_audit: {err}")
    warnings.extend([f"selection_audit: {w}" for w in selection.get("warnings", [])])
    selection_details = selection.get("details", {}) if isinstance(selection.get("details"), dict) else {}
    details["selection_audit"] = {
        key: selection.get(key)
        if key in selection
        else selection_details.get(key)
        for key in [
            "main_price_date",
            "effective_candidate_signal_date",
            "all_candidates_rows",
            "raw_model_signal_rows",
            "report_model_signal_rows",
            "volume_watch_rows",
            "tdcc_short_edge_rows",
            "volume_watch_fresh",
            "tdcc_short_edge_fresh",
            "selected_condition_error_count",
            "selected_condition_warning_count",
        ]
    }

    signals = read_csv(REPORT_SIGNALS, dtype=str, keep_default_na=False)
    summary = read_csv(SUMMARY, dtype=str, keep_default_na=False)
    registry = read_csv(REGISTRY, dtype=str, keep_default_na=False)
    taxonomy = read_csv(TAXONOMY, dtype=str, keep_default_na=False)

    _check_model_spec_independence(errors, details)
    _check_registry_and_summary(registry, summary, main_date, errors, details)
    _check_report_signals(signals, registry, main_date, errors, details)
    _check_taxonomy(taxonomy, errors, details)

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "details": details,
    }
    return result


def write_report(result: dict[str, Any]) -> None:
    AUDIT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Daily Candidate Pipeline Integrity Audit",
        "",
        f"- status: `{result['status']}`",
        f"- main_price_date: `{result.get('details', {}).get('main_price_date', '')}`",
        f"- selection_audit_status: `{result.get('details', {}).get('selection_audit_status', '')}`",
        f"- stock_model_spec_count: `{result.get('details', {}).get('stock_model_spec_count', '')}`",
        f"- registry_pdf_model_count: `{result.get('details', {}).get('registry_pdf_model_count', '')}`",
        f"- summary_expected_model_line_rows: `{result.get('details', {}).get('summary_expected_model_line_rows', '')}`",
        f"- summary_actual_model_line_rows: `{result.get('details', {}).get('summary_actual_model_line_rows', '')}`",
        "",
        "## Errors",
        "",
    ]
    errors = result.get("errors") or []
    lines.extend([f"- {err}" for err in errors] if errors else ["- none"])
    lines.extend(["", "## Warnings", ""])
    warnings = result.get("warnings") or []
    lines.extend([f"- {warn}" for warn in warnings] if warnings else ["- none"])
    lines.append("")
    AUDIT_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    result = audit()
    write_report(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
