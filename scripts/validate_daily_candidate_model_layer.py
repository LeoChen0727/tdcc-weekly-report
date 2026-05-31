from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, read_csv, safe_str  # noqa: E402


PARAMETERS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_latest.csv"
ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"
REPEAT_CSV = LATEST_DIR / "daily_candidate_same_model_repeat_latest.csv"
PACKET_MD = LATEST_DIR / "daily_candidate_model_layer_packet_latest.md"
VALIDATION_JSON = LATEST_DIR / "daily_candidate_model_layer_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_candidate_model_layer_validation_latest.md"


REQUIRED_PARAMETER_MODELS = {
    "volume_range_breakout",
    "price_pullback_23ema",
    "revenue_unreacted_range",
    "w_bottom_right_side",
    "near_high_neckline_challenge",
    "platform_strengthening",
    "pullback_short_reclaim",
    "tdcc_stealth_accumulation",
    "tdcc_short_term_continuation_d5_d10",
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
    "report_bucket",
    "model_id",
    "model_name_zh",
    "main_condition_met",
    "entry_basis",
    "effective_primary_theme",
    "effective_structural_theme_bucket",
    "effective_mainstream_label",
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
    "same_model_consecutive_days",
    "same_model_appear_count_5d",
    "same_model_appear_count_10d",
}


def line_count(path: Path) -> int:
    if not path.exists():
        return 0
    return path.read_text(encoding="utf-8", errors="replace").count("\n") + 1


def validate() -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    params = read_csv(PARAMETERS_CSV, dtype=str, keep_default_na=False)
    signals = read_csv(SIGNALS_CSV, dtype=str, keep_default_na=False)
    rotation = read_csv(ROTATION_CSV, dtype=str, keep_default_na=False)
    repeat = read_csv(REPEAT_CSV, dtype=str, keep_default_na=False)

    if params.empty:
        errors.append(f"missing_or_empty: {PARAMETERS_CSV}")
    else:
        missing_models = sorted(REQUIRED_PARAMETER_MODELS - set(params.get("model_id", pd.Series(dtype=str)).astype(str)))
        if missing_models:
            errors.append(f"missing_parameter_models: {missing_models}")
        if params["main_conditions"].astype(str).str.len().lt(5).any():
            errors.append("parameter rows must include readable main_conditions")

    if signals.empty:
        warnings.append("model signal table is empty for current date")
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
        score = pd.to_numeric(signals.get("model_score", ""), errors="coerce")
        if score.notna().any() and ((score < 0) | (score > 100)).any():
            errors.append("model_score must be between 0 and 100")
        dup_count = int(signals.duplicated(["model_id", "report_bucket", "stock_id"]).sum())
        if dup_count:
            errors.append(f"duplicate_model_bucket_stock_rows: {dup_count}")
        repeat_status_values = set(signals.get("same_model_repeat_status", pd.Series(dtype=str)).astype(str))
        invalid_repeat_status = sorted(repeat_status_values - {"", "new_model_signal", "repeated_same_model_signal"})
        if invalid_repeat_status:
            errors.append(f"invalid_same_model_repeat_status: {invalid_repeat_status}")
        text_cols = ["model_name_zh", "next_confirmation", "model_operation_guidance"]
        for col in text_cols:
            if col in signals.columns and signals[col].astype(str).str.contains(r"\?\?\?|\ufffd", regex=True).any():
                errors.append(f"suspicious_unreadable_text_in_signal_column: {col}")

    if not rotation.empty and "volume_expansion_ratio" in rotation.columns:
        ratio = pd.to_numeric(rotation["volume_expansion_ratio"], errors="coerce")
        if ratio.notna().any() and (ratio < 1 / 3 - 0.0001).any():
            errors.append("group rotation rows must satisfy volume_expansion_ratio >= 1/3")

    if line_count(PACKET_MD) <= 10:
        errors.append(f"packet_missing_or_too_short: {PACKET_MD}")

    result = {
        "status": "pass" if not errors else "fail",
        "parameter_rows": 0 if params.empty else int(len(params)),
        "signal_rows": 0 if signals.empty else int(len(signals)),
        "same_model_repeat_rows": 0 if repeat.empty else int(len(repeat)),
        "rotation_rows": 0 if rotation.empty else int(len(rotation)),
        "packet_lines": line_count(PACKET_MD),
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
