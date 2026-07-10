from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, main_price_date_from_freshness, normalize_date, read_csv, safe_str  # noqa: E402


PARAMETERS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_latest.csv"
REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"
REPEAT_CSV = LATEST_DIR / "daily_candidate_same_model_repeat_latest.csv"
PACKET_MD = LATEST_DIR / "daily_candidate_model_layer_packet_latest.md"
VALIDATION_JSON = LATEST_DIR / "daily_candidate_model_layer_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_candidate_model_layer_validation_latest.md"


REQUIRED_PARAMETER_MODELS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
    "price_pullback_23ema",
    "revenue_unreacted_range",
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
    "pullback_short_reclaim",
    "tdcc_stealth_accumulation",
    "tdcc_short_term_continuation_d5_d10",
    "hot_theme_pullback",
    "short_term_surge_d5_d10",
    "group_fund_rotation",
    "explosive_volume_red_candle",
    "five_day_20pct_precursor",
    "disposition_attention_event_tag",
    "msci_event_tag",
}

REQUIRED_SIGNAL_COLUMNS = {
    "signal_date",
    "stock_id",
    "stock_name",
    "report_line",
    "report_bucket",
    "report_bucket_zh",
    "model_id",
    "model_name_zh",
    "display_rank",
    "main_condition_met",
    "entry_basis",
    "effective_primary_theme",
    "source_category_zh",
    "effective_primary_theme_zh",
    "effective_structural_theme_bucket",
    "effective_structural_theme_bucket_zh",
    "effective_mainstream_label",
    "tdcc_status_zh",
    "warrant_flow_signal_zh",
    "risk_tags_zh",
    "downgrade_flags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "why_selected",
    "why_selected_zh",
    "why_selected_human_zh",
    "operation_reminder_zh",
    "source_hit_count",
    "source_hit_labels",
    "source_hit_labels_zh",
    "source_row_indices",
    "merged_same_model_source_count",
    "merged_source_categories_zh",
    "mainstream_report_eligible",
    "non_mainstream_report_eligible",
    "dual_report_membership_flag",
    "report_line_memberships",
    "tdcc_direction_zh",
    "tdcc_big_holder_summary_zh",
    "tdcc_grade_change_summary_zh",
    "tdcc_risk_text_zh",
    "score_components_zh",
    "model_score",
    "model_rank",
    "model_main_conditions",
    "model_add_score_items",
    "model_operation_guidance",
    "selection_semantics",
    "recommended_usage",
    "recommended_close_exit_horizon",
    "best_close_win_rate_pct",
    "best_avg_close_return_pct",
    "model_revision_note",
    "same_model_repeat_status",
    "same_model_repeat_status_zh",
    "same_model_repeat_note_zh",
    "same_model_consecutive_days",
    "same_model_appear_count_5d",
    "same_model_appear_count_10d",
    "model_rank_overall",
    "model_rank_new_signal",
    "model_rank_repeated_signal",
    "display_rank_new_signal",
    "display_rank_repeated_signal",
}

DISPLAY_COLUMNS = [
    "report_bucket_zh",
    "source_category_zh",
    "effective_primary_theme_zh",
    "effective_structural_theme_bucket_zh",
    "tdcc_status_zh",
    "warrant_flow_signal_zh",
    "risk_tags_zh",
    "downgrade_flags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "why_selected_zh",
    "why_selected_human_zh",
    "operation_reminder_zh",
    "source_hit_labels_zh",
    "merged_source_categories_zh",
    "same_model_repeat_status_zh",
    "same_model_repeat_note_zh",
    "tdcc_direction_zh",
    "tdcc_big_holder_summary_zh",
    "tdcc_grade_change_summary_zh",
    "tdcc_risk_text_zh",
    "score_components_zh",
]

CRITICAL_DISPLAY_COLUMNS = ["report_bucket_zh", "source_category_zh", "model_name_zh", "why_selected_human_zh", "operation_reminder_zh"]
RAW_SLUG_PATTERN = re.compile(r"(^|[\s|/、,;])([a-z]+(?:_[a-z0-9]+){1,})(?=$|[\s|/、,;])")
RAW_THEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_ -]*$")
UNRESOLVED_THEME_VALUES = {"", "其他", "其他業", "other", "theme_unknown", "unclassified", "needs_manual_review"}
REQUIRED_ROTATION_COLUMNS = {"theme", "theme_display_zh", "theme_resolution_status", "theme_key"}

FORBIDDEN_DISPLAY_TOKENS = [
    "neckline",
    "breakout",
    "hot theme tag",
    "hot_theme_tag",
    "range_rebound",
    "short_term_specialty",
    "mild_accumulation",
    "strong_accumulation",
    "call_strong_inflow",
    "call_put_bullish",
    "non_mainstream",
    "mainstream",
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
]


def has_cjk_text(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def unresolved_theme_value(value: object) -> bool:
    text = safe_str(value).strip()
    if text in UNRESOLVED_THEME_VALUES:
        return True
    if text.isdigit():
        return True
    if RAW_THEME_PATTERN.fullmatch(text) and not has_cjk_text(text):
        return True
    return False


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8", errors="replace").count("\n") + 1


def validate() -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    expected_signal_date = main_price_date_from_freshness()

    params = read_csv(PARAMETERS_CSV, dtype=str, keep_default_na=False)
    raw_signals = read_csv(SIGNALS_CSV, dtype=str, keep_default_na=False)
    signals = read_csv(REPORT_SIGNALS_CSV, dtype=str, keep_default_na=False)
    rotation = read_csv(ROTATION_CSV, dtype=str, keep_default_na=False)
    repeat = read_csv(REPEAT_CSV, dtype=str, keep_default_na=False)

    if params.empty:
        errors.append(f"missing_or_empty: {PARAMETERS_CSV}")
    else:
        missing_models = sorted(REQUIRED_PARAMETER_MODELS - set(params.get("model_id", pd.Series(dtype=str)).astype(str)))
        if missing_models:
            errors.append(f"missing_parameter_models: {missing_models}")
        legacy = params[params.get("model_id", pd.Series(dtype=str)).astype(str).eq("volume_range_breakout")]
        if not legacy.empty and set(legacy.get("pdf_visibility", pd.Series(dtype=str)).astype(str)) & {"pdf_core_model"}:
            errors.append("legacy volume_range_breakout must not remain an active pdf_core_model parameter")
        if params["main_conditions"].astype(str).str.len().lt(5).any():
            errors.append("parameter rows must include readable main_conditions")

    if signals.empty:
        warnings.append("report-ready model signal table is empty for current date")
    else:
        missing_cols = sorted(REQUIRED_SIGNAL_COLUMNS - set(signals.columns))
        if missing_cols:
            errors.append(f"missing_signal_columns: {missing_cols}")
        bad_semantics = signals[
            ~signals["selection_semantics"].astype(str).str.contains("condition_met", na=False)
        ]
        if not bad_semantics.empty:
            errors.append("selection_semantics must state condition_met semantics")
        valid_buckets = {"mainstream", "non_mainstream", "unclassified"}
        bad_buckets = sorted(set(signals["report_bucket"].astype(str)) - valid_buckets)
        if bad_buckets:
            errors.append(f"invalid_report_bucket: {bad_buckets}")
        valid_report_lines = {"mainstream", "non_mainstream"}
        bad_report_lines = sorted(set(signals["report_line"].astype(str)) - valid_report_lines)
        if bad_report_lines:
            errors.append(f"invalid_report_line: {bad_report_lines}")
        score = pd.to_numeric(signals.get("model_score", ""), errors="coerce")
        if score.notna().any() and ((score < 0) | (score > 100)).any():
            errors.append("model_score must be between 0 and 100")
        dup_count = int(signals.duplicated(["report_line", "model_id", "stock_id"]).sum())
        if dup_count:
            errors.append(f"duplicate_report_line_model_stock_rows: {dup_count}")
        repeat_status_values = set(signals.get("same_model_repeat_status", pd.Series(dtype=str)).astype(str))
        invalid_repeat_status = sorted(repeat_status_values - {"", "new_model_signal", "repeated_same_model_signal"})
        if invalid_repeat_status:
            errors.append(f"invalid_same_model_repeat_status: {invalid_repeat_status}")
        text_cols = ["model_name_zh", "next_confirmation", "model_operation_guidance"]
        for col in text_cols:
            if col in signals.columns and signals[col].astype(str).str.contains(r"\?\?\?|\ufffd", regex=True).any():
                errors.append(f"suspicious_unreadable_text_in_signal_column: {col}")
        for col in DISPLAY_COLUMNS:
            if col not in signals.columns:
                continue
            values = signals[col].astype(str)
            if values.str.contains(r"\?\?\?|\ufffd", regex=True).any():
                errors.append(f"suspicious_unreadable_text_in_display_column: {col}")
            if values.map(lambda value: bool(RAW_SLUG_PATTERN.search(value))).any():
                errors.append(f"raw_slug_leaked_in_display_column: {col}")
            leaked = [
                token
                for token in FORBIDDEN_DISPLAY_TOKENS
                if values.str.contains(re.escape(token), case=False, regex=True).any()
            ]
            if leaked:
                errors.append(f"forbidden_pdf_token_in_display_column: {col}: {leaked}")
        pending_display_value = "\u6b04\u4f4d\u5c1a\u672a\u5b8c\u6210"
        for col in CRITICAL_DISPLAY_COLUMNS:
            if col in signals.columns and signals[col].astype(str).eq(pending_display_value).any():
                errors.append(f"critical_display_column_pending: {col}")
        if "why_selected_human_zh" in signals.columns:
            reasons = signals["why_selected_human_zh"].astype(str)
            if reasons.str.contains(r"基礎分\s*=|base\s*=", regex=True, case=False).any():
                errors.append("why_selected_human_zh_must_not_be_score_breakdown")
        if "operation_reminder_zh" in signals.columns:
            reminders = signals["operation_reminder_zh"].astype(str).str.strip()
            if reminders.eq("").any() or reminders.eq(pending_display_value).any():
                errors.append("operation_reminder_zh_missing_or_pending")
        if expected_signal_date and "signal_date" in signals.columns:
            report_dates = sorted(
                {normalize_date(value) for value in signals["signal_date"].astype(str).tolist() if normalize_date(value)}
            )
            if report_dates != [expected_signal_date]:
                errors.append(
                    f"report_model_signals signal_date mismatch: expected {expected_signal_date}, got {report_dates}"
                )

    if not raw_signals.empty and expected_signal_date and "signal_date" in raw_signals.columns:
        raw_dates = sorted(
            {normalize_date(value) for value in raw_signals["signal_date"].astype(str).tolist() if normalize_date(value)}
        )
        if raw_dates != [expected_signal_date]:
            errors.append(f"raw_model_signals signal_date mismatch: expected {expected_signal_date}, got {raw_dates}")

    if not rotation.empty:
        missing_rotation_cols = sorted(REQUIRED_ROTATION_COLUMNS - set(rotation.columns))
        if missing_rotation_cols:
            errors.append(f"missing_group_rotation_columns: {missing_rotation_cols}")
        rotation_model = rotation.get("rotation_model_id", pd.Series([""] * len(rotation))).astype(str)
        volume_ratio = pd.to_numeric(rotation.get("volume_expansion_ratio", ""), errors="coerce")
        slow_ratio = pd.to_numeric(rotation.get("slow_inflow_ratio", ""), errors="coerce")
        count_15 = pd.to_numeric(rotation.get("volume_expansion_1_5x_count", ""), errors="coerce").fillna(0)

        launch_rows = rotation_model.eq("group_fund_rotation_launch")
        if launch_rows.any() and (volume_ratio[launch_rows] < 1 / 3 - 0.0001).any():
            errors.append("group_fund_rotation_launch rows must satisfy volume_expansion_ratio >= 1/3")

        slow_rows = rotation_model.eq("group_slow_inflow_rotation")
        if slow_rows.any():
            bad_slow = slow_rows & ((slow_ratio < 1 / 3 - 0.0001) | (count_15 <= 0))
            if bad_slow.any():
                errors.append(
                    "group_slow_inflow_rotation rows must satisfy slow_inflow_ratio >= 1/3 "
                    "and include at least one 1.5x volume expansion stock"
                )

        valid_rotation_models = {"group_fund_rotation_launch", "group_slow_inflow_rotation"}
        bad_rotation_models = sorted(set(rotation_model) - valid_rotation_models)
        if bad_rotation_models:
            errors.append(f"invalid_rotation_model_id: {bad_rotation_models}")
        if not missing_rotation_cols:
            unresolved_rows = rotation[
                rotation["theme_resolution_status"].astype(str).ne("resolved")
                | rotation["theme"].map(unresolved_theme_value)
                | rotation["theme_display_zh"].map(unresolved_theme_value)
            ]
            if not unresolved_rows.empty:
                sample = unresolved_rows[["theme", "theme_display_zh", "theme_resolution_status", "theme_key"]].head(8).to_dict("records")
                errors.append(f"group rotation unresolved/raw theme rows: count={len(unresolved_rows)} sample={sample}")

    if line_count(PACKET_MD) <= 10:
        errors.append(f"packet_missing_or_too_short: {PACKET_MD}")

    result = {
        "status": "pass" if not errors else "fail",
        "parameter_rows": 0 if params.empty else int(len(params)),
        "raw_signal_rows": 0 if raw_signals.empty else int(len(raw_signals)),
        "signal_rows": 0 if signals.empty else int(len(signals)),
        "same_model_repeat_rows": 0 if repeat.empty else int(len(repeat)),
        "rotation_rows": 0 if rotation.empty else int(len(rotation)),
        "packet_lines": line_count(PACKET_MD),
        "expected_signal_date": expected_signal_date,
        "errors": errors,
        "warnings": warnings,
    }
    return result


def write_report(result: dict[str, object]) -> None:
    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Daily Candidate Model Layer Validation",
        "",
        f"- status: `{result['status']}`",
        f"- parameter_rows: `{result['parameter_rows']}`",
        f"- raw_signal_rows: `{result['raw_signal_rows']}`",
        f"- signal_rows: `{result['signal_rows']}`",
        f"- same_model_repeat_rows: `{result['same_model_repeat_rows']}`",
        f"- rotation_rows: `{result['rotation_rows']}`",
        f"- packet_lines: `{result['packet_lines']}`",
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
    VALIDATION_MD.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    result = validate()
    write_report(result)
    print(f"Saved: {VALIDATION_JSON}")
    print(f"Saved: {VALIDATION_MD}")
    if result["status"] != "pass":
        for error in result.get("errors", []):
            print(f"ERROR: {error}")
        return 1
    print("Daily candidate model layer validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
