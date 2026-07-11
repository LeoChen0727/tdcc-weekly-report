from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from build_daily_volume_breakout_operation_section import (
    HIGH_POSITION_BONUS_FEATURE_ORDER,
    HIGH_POSITION_COMBO_BONUS_METRICS,
    HIGH_POSITION_SINGLE_BONUS_METRICS,
    combo_metric_not_worse,
    metric_rank,
    select_high_position_bonus_metric,
)


ROOT = Path(__file__).resolve().parents[1]
READINESS_CSV = ROOT / "output" / "latest" / "model_operation_readiness_latest.csv"
APPROVED_PATTERNS_CSV = ROOT / "output" / "latest" / "approved_operation_patterns_latest.csv"
HIGH_POSITION_AUDIT_CSV = (
    ROOT
    / "output"
    / "latest"
    / "research_backtest"
    / "volume_range_breakout_v2_high_position_improvement_audit_latest.csv"
)
HIGH_POSITION_DETAIL_CSV = (
    ROOT
    / "output"
    / "latest"
    / "research_backtest"
    / "volume_range_breakout_v2_high_position_improvement_audit_detail_latest.csv"
)
LATEST_CSV = ROOT / "output" / "latest" / "mature_model_row_level_metric_contract_audit_latest.csv"
LATEST_MD = ROOT / "output" / "latest" / "mature_model_row_level_metric_contract_audit_latest.md"
ROW_AUDIT_CSV = ROOT / "output" / "latest" / "mature_model_row_level_metric_row_audit_latest.csv"
ROW_AUDIT_MD = ROOT / "output" / "latest" / "mature_model_row_level_metric_row_audit_latest.md"

AUDIT_ID = "mature_model_row_level_metric_contract_audit_20260711"
AUDIT_VERSION = "v2"

MATURE_OPERATION_SECTIONS = {"confirmed_operation", "active_operation"}
TRUTHY = {"true", "1", "yes", "y"}

ADAPTER_BY_MODEL = {
    "volume_range_breakout_v2_low_position_volume_attack": ROOT
    / "output"
    / "latest"
    / "daily_volume_breakout_operation_section_latest.csv",
    "volume_range_breakout_v2_mid_position_momentum_attack": ROOT
    / "output"
    / "latest"
    / "daily_volume_breakout_operation_section_latest.csv",
    "volume_range_breakout_v2_high_position_volume_attack": ROOT
    / "output"
    / "latest"
    / "daily_volume_breakout_operation_section_latest.csv",
    "w_bottom_right_side": ROOT / "output" / "latest" / "daily_w_bottom_right_side_operation_section_latest.csv",
    "neckline_volume_breakout_confirmation": ROOT
    / "output"
    / "latest"
    / "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
    "price_pullback_23ema": ROOT / "output" / "latest" / "daily_price_pullback_23ema_operation_section_latest.csv",
}

BASE_METRIC_COLUMNS = {
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "loss_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "median_return_zh",
}

TECHNICAL_PACKAGE_COLUMNS = {
    "technical_package_sample_size",
    "technical_package_win_rate_zh",
    "technical_package_neutral_rate_zh",
    "technical_package_failure_rate_zh",
    "technical_package_avg_return_zh",
}

GENERIC_COMBO_PREFIXES = (
    "pdf_bonus_combo",
    "pdf_combo",
    "row_level_combo",
    "add_score_combo",
)

ROW_METRIC_COLUMNS = {
    "row_metric_status",
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
}

ROW_METRIC_REQUIRED_WHEN_READY = {
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
}

SCORE_ADD_ITEM_POLICY = {
    "w_bottom_right_side": {
        "score_add_item_ids": "second_low_quality|right_side_volume|right_side_rebound|second_attack_strength|second_arc_volume|red_candle_ratio|low_position",
        "validated_row_metric_add_item_ids": "",
        "policy": "ranking_only_unvalidated_not_performance_metric",
    },
    "neckline_volume_breakout_confirmation": {
        "score_add_item_ids": "context90|second_arc_volume|locked_limit_up|volume_confirmation|red_candle_ratio|breakout_distance|close_location|red_body",
        "validated_row_metric_add_item_ids": "",
        "policy": "ranking_only_unvalidated_not_performance_metric",
    },
    "price_pullback_23ema": {
        "score_add_item_ids": "technical_strength_rsi60_macd_positive",
        "validated_row_metric_add_item_ids": "rsi14_ge60|macd_hist_gt0",
        "policy": "approved_exact_combo_only",
    },
    "volume_range_breakout_v2_low_position_volume_attack": {
        "score_add_item_ids": "volume_ratio|breakout_magnitude|close_position|red_body|base_width|base_duration",
        "validated_row_metric_add_item_ids": "",
        "policy": "ranking_only_unvalidated_not_performance_metric",
    },
    "volume_range_breakout_v2_mid_position_momentum_attack": {
        "score_add_item_ids": "volume_ratio|breakout_magnitude|close_position|red_body|base_width|base_duration",
        "validated_row_metric_add_item_ids": "",
        "policy": "ranking_only_unvalidated_not_performance_metric",
    },
    "volume_range_breakout_v2_high_position_volume_attack": {
        "score_add_item_ids": "mild_bull|tdcc_weekly_increase_top20|ma20_gt_ma60|volume_lt2|not_limit_up_like|breakout_2_5|close_location_le80|signal_body_le3|confirmation_return_3_7|kdj_overheated|dist_ema23_0_15",
        "validated_row_metric_add_item_ids": "mild_bull|tdcc_weekly_increase_top20|ma20_gt_ma60|volume_lt2|not_limit_up_like|breakout_2_5|close_location_le80|signal_body_le3|confirmation_return_3_7|kdj_overheated|dist_ema23_0_15",
        "policy": "approved_single_or_exact_combo_with_best_single_fallback",
    },
}

OUTPUT_COLUMNS = [
    "generated_at",
    "audit_id",
    "audit_version",
    "audit_scope",
    "model_id",
    "model_name_zh",
    "approved_for_daily",
    "presentation_allowed",
    "pdf_integration_status",
    "adapter_path",
    "adapter_exists",
    "adapter_row_count",
    "adapter_data_row_count",
    "mature_operation_data_row_count",
    "unique_stock_lifecycle_count",
    "metric_scope",
    "baseline_metric_status",
    "row_level_metric_status",
    "single_add_score_metric_status",
    "combo_recompute_policy_status",
    "combo_worse_policy_status",
    "pdf_row_display_policy_status",
    "technical_strength_row_count",
    "base_row_count",
    "generic_combo_metric_group_count",
    "approved_metric_source_status",
    "production_score_add_item_ids",
    "validated_row_metric_add_item_ids",
    "score_add_item_governance_status",
    "row_metric_contract_columns_status",
    "row_metric_ready_count",
    "row_metric_unavailable_count",
    "row_metric_invalid_count",
    "row_metric_baseline_misuse_count",
    "row_metric_duplicate_key_count",
    "metric_source_parity_status",
    "non_overlap_status",
    "numerical_anomaly_status",
    "research_only_combo_candidate_count",
    "research_only_combo_not_candidate_count",
    "research_only_combo_positive_but_below_threshold_count",
    "production_readiness",
    "issues",
]

ROW_AUDIT_COLUMNS = [
    "generated_at",
    "audit_id",
    "audit_version",
    "model_id",
    "pdf_view",
    "pdf_section",
    "report_line",
    "operation_asof_date",
    "stock_id",
    "stock_name",
    "signal_date",
    "operation_quality",
    "baseline_metric_present",
    "formal_bonus_metric_present",
    "row_metric_status",
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
    "metric_rate_sum_pct",
    "baseline_misuse_status",
    "validation_status",
    "issues",
]


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def truthy(value: object) -> bool:
    return str(value or "").strip().lower() in TRUTHY


def clean_text(value: object) -> str:
    return "" if value is None else str(value).strip()


def pct_number(value: object) -> float | None:
    text = clean_text(value).replace("%", "").replace("+", "").strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def non_blank(frame: pd.DataFrame, column: str) -> bool:
    return column in frame.columns and frame[column].astype(str).str.strip().ne("").any()


def all_non_blank(frame: pd.DataFrame, columns: set[str]) -> bool:
    return all(column in frame.columns and frame[column].astype(str).str.strip().ne("").all() for column in columns)


def mature_readiness_rows(readiness: pd.DataFrame) -> pd.DataFrame:
    if readiness.empty:
        return readiness
    required = {"model_id", "approved_for_daily", "presentation_allowed", "pdf_integration_status"}
    missing = required - set(readiness.columns)
    if missing:
        raise RuntimeError(f"model_operation_readiness_latest.csv missing columns: {sorted(missing)}")
    mask = (
        readiness["approved_for_daily"].map(truthy)
        & readiness["presentation_allowed"].map(truthy)
        & readiness["pdf_integration_status"].eq("pdf_integrated_daily_adapter")
    )
    return readiness[mask].copy()


def adapter_data_rows(adapter: pd.DataFrame, model_id: str) -> pd.DataFrame:
    if adapter.empty:
        return adapter
    data = adapter.copy()
    if "model_id" in data.columns:
        data = data[data["model_id"].eq(model_id)]
    if "row_type" in data.columns:
        data = data[data["row_type"].eq("data")]
    return data


def mature_operation_rows(adapter: pd.DataFrame, model_id: str) -> pd.DataFrame:
    data = adapter_data_rows(adapter, model_id)
    if data.empty or "pdf_section" not in data.columns:
        return data.iloc[0:0].copy()
    return data[data["pdf_section"].isin(MATURE_OPERATION_SECTIONS)].copy()


def generic_combo_groups(columns: list[str]) -> list[str]:
    found: list[str] = []
    for prefix in GENERIC_COMBO_PREFIXES:
        if any(column.startswith(prefix) for column in columns):
            found.append(prefix)
    return found


def status_from_missing(frame: pd.DataFrame, columns: set[str], pass_status: str, missing_status: str) -> str:
    missing = sorted(column for column in columns if column not in frame.columns)
    if missing:
        return f"{missing_status}:missing_columns={';'.join(missing)}"
    blank = sorted(column for column in columns if frame[column].astype(str).str.strip().eq("").any())
    if blank:
        return f"{missing_status}:blank_columns={';'.join(blank)}"
    return pass_status


def high_position_metric_source_parity() -> tuple[str, list[str]]:
    research = read_csv(HIGH_POSITION_AUDIT_CSV)
    if research.empty:
        return "fail_missing_high_position_research_audit", ["missing_high_position_research_audit"]
    issues: list[str] = []
    mappings = [
        ("sample_size", "sample_size"),
        ("win_rate", "win_rate_pct"),
        ("neutral_rate", "neutral_rate_pct"),
        ("loss_rate", "loss_rate_pct"),
        ("avg_return", "avg_return_pct"),
        ("median_return", "median_return_pct"),
    ]
    metric_groups = [
        ("candidate_condition", HIGH_POSITION_SINGLE_BONUS_METRICS),
        ("pdf_bonus_combo", HIGH_POSITION_COMBO_BONUS_METRICS),
    ]
    for row_type, metrics in metric_groups:
        for metric in metrics.values():
            metric_id = clean_text(metric.get("metric_id"))
            matched = research[
                research["row_type"].eq(row_type)
                & research["feature_id"].eq(metric_id)
            ]
            if len(matched) != 1:
                issues.append(f"{metric_id}:research_row_count={len(matched)}")
                continue
            source = matched.iloc[0]
            if clean_text(source.get("candidate_status")) != "research_only_candidate_metric_met":
                issues.append(f"{metric_id}:source_not_candidate_metric_met")
            for metric_key, source_column in mappings:
                expected = pct_number(metric.get(metric_key))
                actual = pct_number(source.get(source_column))
                tolerance = 0.0001 if metric_key != "sample_size" else 0.0
                if expected is None or actual is None or abs(expected - actual) > tolerance:
                    issues.append(f"{metric_id}:{metric_key}_mismatch={expected}!={actual}")
    if issues:
        return "fail_high_position_metric_source_mismatch", issues
    return "pass_all_promoted_high_position_metrics_match_research_source", []


def high_position_selection_policy_status() -> tuple[str, list[str]]:
    issues: list[str] = []
    feature_order = list(HIGH_POSITION_BONUS_FEATURE_ORDER)
    for mask in range(1 << len(feature_order)):
        flags = {feature: bool(mask & (1 << index)) for index, feature in enumerate(feature_order)}
        metric, source = select_high_position_bonus_metric(flags)
        matched_singles = [
            candidate
            for feature, candidate in HIGH_POSITION_SINGLE_BONUS_METRICS.items()
            if flags.get(feature)
        ]
        best_single = max(matched_singles, key=metric_rank) if matched_singles else None
        combo_id = "pdf_combo__" + "__".join(feature for feature in feature_order if flags.get(feature))
        combo = HIGH_POSITION_COMBO_BONUS_METRICS.get(combo_id)
        if combo is not None and combo_metric_not_worse(combo, best_single):
            if metric is not combo or source != "exact_combo_metric":
                issues.append(f"{combo_id}:exact_combo_not_selected")
        elif best_single is not None:
            if metric is not best_single or source != "single_bonus_metric":
                issues.append(f"{combo_id}:best_single_fallback_not_selected")
        elif metric is not None or source:
            issues.append(f"{combo_id}:unexpected_metric_without_match")
    if issues:
        return "fail_high_position_combo_selection_policy", issues
    return "pass_exact_combo_or_best_single_fallback_policy", []


def high_position_detail_quality_status() -> tuple[str, str, list[str]]:
    detail = read_csv(HIGH_POSITION_DETAIL_CSV)
    if detail.empty:
        return (
            "fail_missing_high_position_detail",
            "fail_missing_high_position_detail",
            ["missing_high_position_detail"],
        )
    rows = detail[detail["base_model_member"].map(truthy)].copy()
    issues: list[str] = []
    duplicate_count = int(rows.duplicated(subset=["source_event_key"], keep=False).sum())
    if len(rows) != 231:
        issues.append(f"base_member_count={len(rows)}!=231")
    if duplicate_count:
        issues.append(f"duplicate_source_event_key_rows={duplicate_count}")
    returns = pd.to_numeric(rows["return_pct"], errors="coerce")
    if returns.isna().any():
        issues.append(f"non_numeric_return_rows={int(returns.isna().sum())}")
    outcome_count = int(rows["return_outcome"].isin({"win", "neutral", "loss"}).sum())
    if outcome_count != len(rows):
        issues.append(f"invalid_outcome_rows={len(rows) - outcome_count}")
    if returns.dropna().empty:
        anomaly_status = "fail_no_numeric_returns"
        issues.append("no_numeric_returns")
    else:
        total = float(returns.sum())
        top = float(returns.max())
        mean_all = float(returns.mean())
        mean_without_top = float(returns[returns.ne(top)].mean()) if len(returns) > 1 else mean_all
        top_share = abs(top / total) if total else 0.0
        if top_share > 0.10 or abs(mean_all - mean_without_top) > 1.0:
            anomaly_status = (
                f"fail_dominant_return_top={top:.4f};top_share={top_share:.4f};"
                f"mean={mean_all:.4f};mean_without_top={mean_without_top:.4f}"
            )
            issues.append("dominant_return_changes_conclusion")
        else:
            anomaly_status = (
                f"pass_no_single_return_dominates_top={top:.4f};top_share={top_share:.4f};"
                f"mean={mean_all:.4f};mean_without_top={mean_without_top:.4f}"
            )
    non_overlap_status = (
        "pass_source_event_key_unique_same_stock_non_overlap_basis"
        if not duplicate_count
        else f"fail_duplicate_source_event_key_rows={duplicate_count}"
    )
    return non_overlap_status, anomaly_status, issues


def row_metric_audit_rows(
    model_id: str,
    operation_rows: pd.DataFrame,
    generated_at: str,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for _, source in operation_rows.iterrows():
        issues: list[str] = []
        missing_contract_columns = sorted(ROW_METRIC_COLUMNS - set(operation_rows.columns))
        status = clean_text(source.get("row_metric_status"))
        formal_bonus_present = bool(
            clean_text(source.get("pdf_bonus_combo_id"))
            or clean_text(source.get("row_metric_id"))
            or clean_text(source.get("operation_quality")) == "technical_strength"
        )
        rate_sum: float | None = None
        if missing_contract_columns:
            issues.append("missing_contract_columns=" + "|".join(missing_contract_columns))
        elif status == "ready":
            blank = sorted(
                column
                for column in ROW_METRIC_REQUIRED_WHEN_READY
                if not clean_text(source.get(column))
            )
            if blank:
                issues.append("blank_ready_columns=" + "|".join(blank))
            rates = [
                pct_number(source.get("row_metric_win_rate_zh")),
                pct_number(source.get("row_metric_neutral_rate_zh")),
                pct_number(source.get("row_metric_failure_rate_zh")),
            ]
            if any(value is None for value in rates):
                issues.append("non_numeric_ready_rates")
            else:
                rate_sum = sum(value for value in rates if value is not None)
                if abs(rate_sum - 100.0) > 0.05:
                    issues.append(f"ready_rate_sum={rate_sum:.4f}")
            baseline_misuse_status = "pass_formal_row_metric_selected"
        elif status == "unavailable_no_approved_add_score_metric":
            payload_columns = ROW_METRIC_COLUMNS - {"row_metric_status", "row_metric_selection_status"}
            populated = sorted(column for column in payload_columns if clean_text(source.get(column)))
            if populated:
                issues.append("unavailable_row_has_metric_payload=" + "|".join(populated))
            if formal_bonus_present:
                issues.append("formal_bonus_present_but_row_metric_unavailable")
                baseline_misuse_status = "fail_formal_bonus_would_fall_back_to_baseline"
            else:
                baseline_misuse_status = "pass_adapter_explicitly_blocks_baseline_fallback"
        else:
            baseline_misuse_status = "fail_missing_explicit_row_metric_status"
            issues.append(f"invalid_row_metric_status={status or 'blank'}")
        rows.append(
            {
                "generated_at": generated_at,
                "audit_id": AUDIT_ID,
                "audit_version": AUDIT_VERSION,
                "model_id": model_id,
                "pdf_view": clean_text(source.get("pdf_view")),
                "pdf_section": clean_text(source.get("pdf_section")),
                "report_line": clean_text(source.get("report_line")),
                "operation_asof_date": clean_text(source.get("operation_asof_date")),
                "stock_id": clean_text(source.get("stock_id")),
                "stock_name": clean_text(source.get("stock_name")),
                "signal_date": clean_text(source.get("signal_date")),
                "operation_quality": clean_text(source.get("operation_quality")),
                "baseline_metric_present": str(bool(clean_text(source.get("win_rate_zh")))),
                "formal_bonus_metric_present": str(formal_bonus_present),
                "row_metric_status": status,
                "row_metric_scope": clean_text(source.get("row_metric_scope")),
                "row_metric_id": clean_text(source.get("row_metric_id")),
                "row_metric_label_zh": clean_text(source.get("row_metric_label_zh")),
                "row_metric_matched_add_score_ids": clean_text(source.get("row_metric_matched_add_score_ids")),
                "row_metric_sample_size": clean_text(source.get("row_metric_sample_size")),
                "row_metric_win_rate_zh": clean_text(source.get("row_metric_win_rate_zh")),
                "row_metric_neutral_rate_zh": clean_text(source.get("row_metric_neutral_rate_zh")),
                "row_metric_failure_rate_zh": clean_text(source.get("row_metric_failure_rate_zh")),
                "row_metric_avg_return_zh": clean_text(source.get("row_metric_avg_return_zh")),
                "row_metric_median_return_zh": clean_text(source.get("row_metric_median_return_zh")),
                "row_metric_source": clean_text(source.get("row_metric_source")),
                "row_metric_selection_status": clean_text(source.get("row_metric_selection_status")),
                "metric_rate_sum_pct": "" if rate_sum is None else f"{rate_sum:.4f}",
                "baseline_misuse_status": baseline_misuse_status,
                "validation_status": "pass" if not issues else "fail",
                "issues": ";".join(sorted(set(issues))),
            }
        )
    return rows


def approved_pattern_for(model_id: str, approved: pd.DataFrame) -> pd.Series | None:
    if approved.empty or "model_id" not in approved.columns:
        return None
    rows = approved[approved["model_id"].eq(model_id)]
    if rows.empty:
        return None
    return rows.iloc[0]


def price_pullback_source_status(row: pd.Series | None, adapter_rows: pd.DataFrame) -> str:
    if row is None:
        return "fail_missing_approved_operation_pattern"
    mapping = {
        "sample_size": "price_pullback_mature_sample_size",
        "win_rate_zh": "price_pullback_win_rate_pct",
        "neutral_rate_zh": "price_pullback_neutral_rate_pct",
        "failure_rate_zh": "price_pullback_failure_rate_pct",
        "avg_return_zh": "price_pullback_avg_return_pct",
        "technical_package_sample_size": "price_pullback_technical_package_sample_size",
        "technical_package_win_rate_zh": "price_pullback_technical_package_win_rate_pct",
        "technical_package_neutral_rate_zh": "price_pullback_technical_package_neutral_rate_pct",
        "technical_package_failure_rate_zh": "price_pullback_technical_package_failure_rate_pct",
        "technical_package_avg_return_zh": "price_pullback_technical_package_avg_return_pct",
    }
    issues: list[str] = []
    first = adapter_rows.iloc[0] if not adapter_rows.empty else None
    for adapter_col, approved_col in mapping.items():
        if approved_col not in row.index:
            issues.append(f"missing_approved:{approved_col}")
            continue
        if first is None or adapter_col not in first.index:
            issues.append(f"missing_adapter:{adapter_col}")
            continue
        approved_value = pct_number(row.get(approved_col))
        adapter_value = pct_number(first.get(adapter_col))
        if approved_value is None or adapter_value is None:
            issues.append(f"non_numeric:{adapter_col}")
            continue
        if abs(approved_value - adapter_value) > 0.01:
            issues.append(f"mismatch:{adapter_col}!={approved_col}")
    return "pass_matches_approved_operation_patterns" if not issues else "fail_" + ";".join(issues)


def technical_package_worse_status(rows: pd.DataFrame) -> str:
    if rows.empty or not TECHNICAL_PACKAGE_COLUMNS <= set(rows.columns):
        return "not_applicable"
    first = rows.iloc[0]
    base_win = pct_number(first.get("win_rate_zh"))
    base_avg = pct_number(first.get("avg_return_zh"))
    tech_win = pct_number(first.get("technical_package_win_rate_zh"))
    tech_avg = pct_number(first.get("technical_package_avg_return_zh"))
    if None in {base_win, base_avg, tech_win, tech_avg}:
        return "fail_non_numeric_technical_or_base_metric"
    if tech_win < base_win and tech_avg < base_avg:
        return "fail_technical_package_worse_than_baseline"
    if tech_win >= base_win and tech_avg >= base_avg:
        return "pass_improves_win_and_avg_vs_baseline"
    return "pass_improves_one_primary_metric_vs_baseline"


def generic_combo_policy_status(rows: pd.DataFrame, groups: list[str]) -> tuple[str, str, list[str]]:
    if not groups:
        return "not_applicable", "not_applicable", []
    issues: list[str] = []
    recompute_statuses: list[str] = []
    worse_statuses: list[str] = []
    for prefix in groups:
        id_candidates = [f"{prefix}_id", f"{prefix}_metric_id", f"{prefix}_feature_id"]
        id_col = next((column for column in id_candidates if column in rows.columns), "")
        sample_col = f"{prefix}_sample_size"
        win_col = f"{prefix}_win_rate_zh"
        avg_col = f"{prefix}_avg_return_zh"
        median_col = f"{prefix}_median_return_zh"
        metric_cols = [sample_col, win_col, avg_col]
        if not id_col:
            issues.append(f"{prefix}:missing_metric_id_column")
            recompute_statuses.append(f"{prefix}:fail_missing_metric_id")
            continue
        if any(column not in rows.columns for column in metric_cols):
            missing = [column for column in metric_cols if column not in rows.columns]
            issues.append(f"{prefix}:missing_metric_columns={';'.join(missing)}")
            recompute_statuses.append(f"{prefix}:fail_missing_metric_columns")
            continue
        metric_rows = rows[rows[id_col].astype(str).str.strip().ne("")]
        metric_rows = metric_rows[~metric_rows[id_col].astype(str).str.lower().isin({"none", "base"})]
        if metric_rows.empty:
            recompute_statuses.append(f"{prefix}:no_current_metric_rows")
            worse_statuses.append(f"{prefix}:not_applicable_no_current_metric_rows")
            continue
        blank_cols = [column for column in metric_cols if metric_rows[column].astype(str).str.strip().eq("").any()]
        if blank_cols:
            issues.append(f"{prefix}:blank_metric_columns={';'.join(blank_cols)}")
            recompute_statuses.append(f"{prefix}:fail_blank_metric_columns")
            continue
        recompute_statuses.append(f"{prefix}:pass_exact_row_level_metric_fields_present")

        for _, row in metric_rows.iterrows():
            base_win = pct_number(row.get("win_rate_zh"))
            base_avg = pct_number(row.get("avg_return_zh"))
            combo_win = pct_number(row.get(win_col))
            combo_avg = pct_number(row.get(avg_col))
            combo_median = pct_number(row.get(median_col)) if median_col in row.index else None
            base_median = pct_number(row.get("median_return_zh"))
            worsened = []
            if base_win is not None and combo_win is not None and combo_win < base_win:
                worsened.append("win_rate")
            if base_avg is not None and combo_avg is not None and combo_avg < base_avg:
                worsened.append("avg_return")
            if base_median is not None and combo_median is not None and combo_median < base_median:
                worsened.append("median_return")
            if worsened:
                issues.append(f"{prefix}:{row.get(id_col)}:combo_worse_than_baseline")
                worse_statuses.append(f"{prefix}:fail_combo_worse_than_baseline={';'.join(worsened)}")
            else:
                worse_statuses.append(f"{prefix}:pass_combo_not_worse_than_baseline")
    return "|".join(recompute_statuses), "|".join(worse_statuses), issues


def audit_mature_model(row: pd.Series, approved: pd.DataFrame, generated_at: str) -> dict[str, object]:
    model_id = clean_text(row.get("model_id"))
    adapter_path = ADAPTER_BY_MODEL.get(model_id)
    adapter = read_csv(adapter_path) if adapter_path else pd.DataFrame()
    model_adapter_rows = adapter[adapter["model_id"].eq(model_id)] if not adapter.empty and "model_id" in adapter.columns else adapter
    all_data_rows = adapter_data_rows(adapter, model_id)
    operation_rows = mature_operation_rows(adapter, model_id)
    groups = generic_combo_groups(list(adapter.columns)) if not adapter.empty else []
    issues: list[str] = []

    if adapter_path is None:
        issues.append("missing_adapter_mapping")
    elif not adapter_path.exists():
        issues.append("adapter_file_missing")

    missing_row_metric_columns = sorted(ROW_METRIC_COLUMNS - set(adapter.columns))
    row_metric_columns_status = (
        "pass_adapter_row_metric_contract_columns_present"
        if not missing_row_metric_columns
        else "fail_missing_row_metric_columns=" + ";".join(missing_row_metric_columns)
    )
    if missing_row_metric_columns:
        issues.append(row_metric_columns_status)
    row_audit = row_metric_audit_rows(model_id, operation_rows, generated_at)
    invalid_row_count = sum(1 for item in row_audit if item["validation_status"] != "pass")
    ready_row_count = sum(1 for item in row_audit if item["row_metric_status"] == "ready")
    unavailable_row_count = sum(
        1
        for item in row_audit
        if item["row_metric_status"] == "unavailable_no_approved_add_score_metric"
    )
    baseline_misuse_count = sum(
        1
        for item in row_audit
        if clean_text(item.get("baseline_misuse_status")).startswith("fail")
    )
    duplicate_key_count = 0
    unique_stock_lifecycle_count = 0
    if not operation_rows.empty:
        duplicate_key_columns = [
            column
            for column in [
                "model_id",
                "pdf_view",
                "pdf_section",
                "report_line",
                "operation_asof_date",
                "stock_id",
            ]
            if column in operation_rows.columns
        ]
        duplicate_key_count = int(operation_rows.duplicated(subset=duplicate_key_columns, keep=False).sum())
        unique_columns = [
            column
            for column in ["model_id", "pdf_section", "report_line", "operation_asof_date", "stock_id"]
            if column in operation_rows.columns
        ]
        unique_stock_lifecycle_count = len(operation_rows.drop_duplicates(subset=unique_columns))
    if invalid_row_count:
        issues.append(f"invalid_row_metric_rows={invalid_row_count}")
    if baseline_misuse_count:
        issues.append(f"row_metric_baseline_misuse_rows={baseline_misuse_count}")
    if duplicate_key_count:
        issues.append(f"duplicate_operation_row_keys={duplicate_key_count}")

    if operation_rows.empty:
        baseline_status = "no_current_confirmed_or_active_data_rows"
    else:
        present_base_columns = BASE_METRIC_COLUMNS & set(operation_rows.columns)
        if "win_rate_zh" not in present_base_columns:
            baseline_status = "fail_missing_required_baseline_win_rate"
            issues.append("missing_required_baseline_win_rate")
        elif operation_rows["win_rate_zh"].astype(str).str.strip().eq("").any():
            baseline_status = "fail_blank_required_baseline_win_rate"
            issues.append("blank_required_baseline_win_rate")
        else:
            missing_optional = sorted(BASE_METRIC_COLUMNS - set(operation_rows.columns))
            baseline_status = (
                "pass_baseline_metrics_present"
                if not missing_optional
                else "pass_baseline_win_rate_present_optional_missing=" + ";".join(missing_optional)
            )

    technical_rows = (
        operation_rows[operation_rows.get("operation_quality", pd.Series(dtype=str)).astype(str).eq("technical_strength")]
        if not operation_rows.empty and "operation_quality" in operation_rows.columns
        else operation_rows.iloc[0:0].copy()
    )
    base_rows = (
        operation_rows[operation_rows.get("operation_quality", pd.Series(dtype=str)).astype(str).eq("base")]
        if not operation_rows.empty and "operation_quality" in operation_rows.columns
        else operation_rows.iloc[0:0].copy()
    )

    if not technical_rows.empty:
        technical_status = status_from_missing(
            technical_rows,
            TECHNICAL_PACKAGE_COLUMNS,
            "pass_technical_package_metrics_present_for_technical_strength_rows",
            "fail_technical_package_metrics_incomplete",
        )
        if technical_status.startswith("fail"):
            issues.append(technical_status)
        single_status = "pass_single_add_score_rows_use_matching_package_metric"
        combo_status = (
            "pass_exact_package_metric_required_for_multi_feature_technical_strength"
            if "technical_strength" in set(technical_rows["operation_quality"].astype(str))
            else "not_applicable"
        )
        combo_worse = technical_package_worse_status(technical_rows)
        if combo_worse.startswith("fail"):
            issues.append(combo_worse)
        approved_status = price_pullback_source_status(
            approved_pattern_for(model_id, approved),
            technical_rows,
        )
        if approved_status.startswith("fail"):
            issues.append(approved_status)
        metric_scope = "baseline_plus_technical_package"
    else:
        technical_status = "not_applicable_no_formal_row_level_add_score_metric"
        single_status = "not_applicable_no_formal_row_level_add_score_metric"
        combo_status = "not_applicable_no_formal_row_level_add_score_metric"
        combo_worse = "not_applicable_no_formal_row_level_add_score_metric"
        approved_status = "not_applicable_no_formal_row_level_add_score_metric"
        metric_scope = "baseline_only_no_formal_add_score_metric"

    generic_recompute, generic_worse, generic_issues = generic_combo_policy_status(operation_rows, groups)
    issues.extend(generic_issues)
    if groups:
        if combo_status.startswith("not_applicable"):
            combo_status = generic_recompute
        if combo_worse.startswith("not_applicable"):
            combo_worse = generic_worse
        metric_scope = "baseline_plus_generic_row_level_combo"

    policy = SCORE_ADD_ITEM_POLICY.get(
        model_id,
        {"score_add_item_ids": "", "validated_row_metric_add_item_ids": "", "policy": "missing_policy"},
    )
    if policy["policy"] == "missing_policy":
        issues.append("missing_score_add_item_policy")
    if policy["policy"] == "ranking_only_unvalidated_not_performance_metric":
        score_governance_status = (
            "pass_unvalidated_ranking_items_cannot_populate_row_metric"
            if ready_row_count == 0
            else "fail_unvalidated_ranking_items_populated_row_metric"
        )
        if score_governance_status.startswith("fail"):
            issues.append(score_governance_status)
        single_status = "not_available_unvalidated_ranking_score_components"
        combo_status = "not_available_unvalidated_ranking_score_components"
        combo_worse = "not_applicable_no_approved_combo_metric"
    else:
        score_governance_status = "pass_only_approved_performance_add_score_items_may_populate_row_metric"

    metric_source_status = approved_status
    non_overlap_status = "not_applicable_no_high_position_detail_scope"
    anomaly_status = "not_applicable_no_high_position_detail_scope"
    if model_id == "volume_range_breakout_v2_high_position_volume_attack":
        metric_source_status, source_issues = high_position_metric_source_parity()
        selection_status, selection_issues = high_position_selection_policy_status()
        non_overlap_status, anomaly_status, detail_issues = high_position_detail_quality_status()
        issues.extend(source_issues + selection_issues + detail_issues)
        single_status = "pass_promoted_single_item_metrics_match_research_source"
        combo_status = "pass_exact_recomputed_combo_metrics_match_research_source"
        combo_worse = selection_status
    elif model_id != "price_pullback_23ema":
        metric_source_status = "not_applicable_no_approved_row_metric"

    if invalid_row_count:
        row_level_status = f"fail_invalid_row_metric_rows={invalid_row_count}"
    elif ready_row_count:
        row_level_status = "pass_ready_rows_use_formal_row_metric"
    else:
        row_level_status = "pass_explicit_unavailable_no_baseline_substitution"

    ready_scopes = sorted(
        {
            clean_text(item.get("row_metric_scope"))
            for item in row_audit
            if item.get("row_metric_status") == "ready" and clean_text(item.get("row_metric_scope"))
        }
    )
    metric_scope = "|".join(ready_scopes) if ready_scopes else "no_current_formal_row_metric"
    display_status = "pass_adapter_exposes_row_metric_and_forbids_baseline_substitution"

    return {
        "generated_at": generated_at,
        "audit_id": AUDIT_ID,
        "audit_version": AUDIT_VERSION,
        "audit_scope": "mature_model",
        "model_id": model_id,
        "model_name_zh": clean_text(row.get("model_name_zh")),
        "approved_for_daily": clean_text(row.get("approved_for_daily")),
        "presentation_allowed": clean_text(row.get("presentation_allowed")),
        "pdf_integration_status": clean_text(row.get("pdf_integration_status")),
        "adapter_path": rel(adapter_path) if adapter_path else "",
        "adapter_exists": str(bool(adapter_path and adapter_path.exists())),
        "adapter_row_count": len(model_adapter_rows),
        "adapter_data_row_count": len(all_data_rows),
        "mature_operation_data_row_count": len(operation_rows),
        "unique_stock_lifecycle_count": unique_stock_lifecycle_count,
        "metric_scope": metric_scope,
        "baseline_metric_status": baseline_status,
        "row_level_metric_status": row_level_status,
        "single_add_score_metric_status": single_status,
        "combo_recompute_policy_status": combo_status,
        "combo_worse_policy_status": combo_worse,
        "pdf_row_display_policy_status": display_status,
        "technical_strength_row_count": len(technical_rows),
        "base_row_count": len(base_rows),
        "generic_combo_metric_group_count": len(groups),
        "approved_metric_source_status": approved_status,
        "production_score_add_item_ids": policy["score_add_item_ids"],
        "validated_row_metric_add_item_ids": policy["validated_row_metric_add_item_ids"],
        "score_add_item_governance_status": score_governance_status,
        "row_metric_contract_columns_status": row_metric_columns_status,
        "row_metric_ready_count": ready_row_count,
        "row_metric_unavailable_count": unavailable_row_count,
        "row_metric_invalid_count": invalid_row_count,
        "row_metric_baseline_misuse_count": baseline_misuse_count,
        "row_metric_duplicate_key_count": duplicate_key_count,
        "metric_source_parity_status": metric_source_status,
        "non_overlap_status": non_overlap_status,
        "numerical_anomaly_status": anomaly_status,
        "research_only_combo_candidate_count": "",
        "research_only_combo_not_candidate_count": "",
        "research_only_combo_positive_but_below_threshold_count": "",
        "production_readiness": "adapter_contract_ready_pending_pdf_layout_consumer",
        "issues": ";".join(sorted(set(issues))),
    }


def audit_high_position_research(generated_at: str) -> dict[str, object] | None:
    if not HIGH_POSITION_AUDIT_CSV.exists():
        return None
    audit = read_csv(HIGH_POSITION_AUDIT_CSV)
    if audit.empty or "row_type" not in audit.columns:
        return None
    combos = audit[audit["row_type"].eq("pdf_bonus_combo")].copy()
    if combos.empty:
        return None
    candidate_count = int(combos["candidate_status"].eq("research_only_candidate_metric_met").sum())
    not_candidate_count = int(combos["candidate_status"].eq("research_only_not_candidate_metric").sum())
    positive_below_count = int(
        combos["candidate_status"].eq("research_only_positive_return_but_win_below_threshold").sum()
    )
    production_states = set(combos.get("production_readiness", pd.Series(dtype=str)).astype(str))
    approved_values = set(combos.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower())
    issues: list[str] = []
    if production_states - {"not_production_ready_research_only"}:
        issues.append("high_position_combo_not_strictly_research_only")
    if not approved_values <= {"false", "0", ""}:
        issues.append("high_position_combo_has_approved_for_daily_true")

    return {
        "generated_at": generated_at,
        "audit_id": AUDIT_ID,
        "audit_version": AUDIT_VERSION,
        "audit_scope": "research_only_candidate_not_mature_model",
        "model_id": "volume_range_breakout_v2_high_position_volume_attack",
        "model_name_zh": "高位階放量攻擊研究候選",
        "approved_for_daily": "False",
        "presentation_allowed": "False",
        "pdf_integration_status": "not_integrated_research_only",
        "adapter_path": rel(HIGH_POSITION_AUDIT_CSV),
        "adapter_exists": "True",
        "adapter_row_count": len(audit),
        "adapter_data_row_count": "",
        "mature_operation_data_row_count": "",
        "metric_scope": "research_only_pdf_bonus_combo",
        "baseline_metric_status": "not_mature_model_reference_only",
        "row_level_metric_status": "research_only_not_pdf_adapter_metric",
        "single_add_score_metric_status": "research_only_single_item_metrics_available_not_production",
        "combo_recompute_policy_status": "pass_research_pdf_bonus_combo_rows_are_exact_recomputed_metrics",
        "combo_worse_policy_status": "pass_non_candidate_combos_remain_research_only_not_used_for_pdf",
        "pdf_row_display_policy_status": "pass_not_allowed_for_pdf_operation_rows_without_promotion",
        "technical_strength_row_count": "",
        "base_row_count": "",
        "generic_combo_metric_group_count": int(len(combos)),
        "approved_metric_source_status": "not_applicable_research_only",
        "research_only_combo_candidate_count": candidate_count,
        "research_only_combo_not_candidate_count": not_candidate_count,
        "research_only_combo_positive_but_below_threshold_count": positive_below_count,
        "production_readiness": "not_production_ready_research_only",
        "issues": ";".join(sorted(set(issues))),
    }


def build_rows(generated_at: str | None = None) -> list[dict[str, object]]:
    generated_at = generated_at or now_taipei()
    readiness = read_csv(READINESS_CSV)
    approved = read_csv(APPROVED_PATTERNS_CSV)
    mature = mature_readiness_rows(readiness)
    rows = [audit_mature_model(row, approved, generated_at) for _, row in mature.iterrows()]
    return rows


def build_row_rows(generated_at: str | None = None) -> list[dict[str, object]]:
    generated_at = generated_at or now_taipei()
    readiness = mature_readiness_rows(read_csv(READINESS_CSV))
    rows: list[dict[str, object]] = []
    for model_id in readiness["model_id"].astype(str):
        adapter_path = ADAPTER_BY_MODEL.get(model_id)
        adapter = read_csv(adapter_path) if adapter_path else pd.DataFrame()
        rows.extend(row_metric_audit_rows(model_id, mature_operation_rows(adapter, model_id), generated_at))
    return rows


def write_csv(rows: list[dict[str, object]]) -> None:
    LATEST_CSV.parent.mkdir(parents=True, exist_ok=True)
    with LATEST_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in OUTPUT_COLUMNS})


def write_row_csv(rows: list[dict[str, object]]) -> None:
    ROW_AUDIT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with ROW_AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=ROW_AUDIT_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in ROW_AUDIT_COLUMNS})


def write_md(rows: list[dict[str, object]]) -> None:
    lines = [
        "# Mature Model Row-Level Metric Contract Audit",
        "",
        f"- audit_id: `{AUDIT_ID}`",
        f"- audit_version: `{AUDIT_VERSION}`",
        f"- generated_at: `{rows[0]['generated_at'] if rows else now_taipei()}`",
        "",
        "## Contract",
        "",
        "- Single add-score item may use the approved single-item metric.",
        "- Multi-item add-score combinations must use the exact recomputed combination metric.",
        "- A promoted exact combination may be used only when it is not worse than the best matching single item on win rate, average return, and median return; otherwise use that best single item.",
        "- Whole-model baseline performance is header-only and must never substitute for a stock-row add-score metric.",
        "- PDF and packet operation rows must consume only adapter `row_metric_*` fields.",
        "- Research-only combo rows must remain unavailable to PDF operation rows until a model-specific promotion PR wires an approved adapter metric.",
        "",
        "## Findings",
        "",
        f"- Mature operation stock rows audited: `{sum(int(row.get('mature_operation_data_row_count', 0) or 0) for row in rows)}`.",
        f"- Unique stock lifecycle rows after removing highlight/full view duplication: `{sum(int(row.get('unique_stock_lifecycle_count', 0) or 0) for row in rows)}`.",
        f"- Ready row-level metrics: `{sum(int(row.get('row_metric_ready_count', 0) or 0) for row in rows)}`; explicit unavailable rows: `{sum(int(row.get('row_metric_unavailable_count', 0) or 0) for row in rows)}`.",
        f"- Invalid row metrics: `{sum(int(row.get('row_metric_invalid_count', 0) or 0) for row in rows)}`; baseline misuse rows: `{sum(int(row.get('row_metric_baseline_misuse_count', 0) or 0) for row in rows)}`; duplicate adapter keys: `{sum(int(row.get('row_metric_duplicate_key_count', 0) or 0) for row in rows)}`.",
        "- W-bottom, W-bottom neckline, low-position volume attack, and mid-position momentum score components remain ranking-only until same-basis performance packages are promoted.",
        "- PDF layout integration remains pending; this artifact validates the model-owned adapter contract and does not claim final PDF rendering completion.",
        "",
        "## Audit Rows",
        "",
        "| scope | model_id | consumer rows | unique stock lifecycle | ready | unavailable | metric_scope | row_level_metric_status | combo_policy | production_readiness | issues |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        issues = clean_text(row.get("issues")) or "none"
        lines.append(
            "| {audit_scope} | `{model_id}` | {operation_rows} | {unique_rows} | {ready_rows} | {unavailable_rows} | {metric_scope} | {row_level_metric_status} | {combo_recompute_policy_status} / {combo_worse_policy_status} | {production_readiness} | {issues} |".format(
                audit_scope=row.get("audit_scope", ""),
                model_id=row.get("model_id", ""),
                operation_rows=row.get("mature_operation_data_row_count", ""),
                unique_rows=row.get("unique_stock_lifecycle_count", ""),
                ready_rows=row.get("row_metric_ready_count", ""),
                unavailable_rows=row.get("row_metric_unavailable_count", ""),
                metric_scope=row.get("metric_scope", ""),
                row_level_metric_status=row.get("row_level_metric_status", ""),
                combo_recompute_policy_status=row.get("combo_recompute_policy_status", ""),
                combo_worse_policy_status=row.get("combo_worse_policy_status", ""),
                production_readiness=row.get("production_readiness", ""),
                issues=issues,
            )
        )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_row_md(rows: list[dict[str, object]]) -> None:
    model_counts: dict[str, dict[str, int]] = {}
    for row in rows:
        counts = model_counts.setdefault(
            clean_text(row.get("model_id")),
            {"rows": 0, "ready": 0, "unavailable": 0, "invalid": 0, "baseline_misuse": 0},
        )
        counts["rows"] += 1
        if row.get("row_metric_status") == "ready":
            counts["ready"] += 1
        elif row.get("row_metric_status") == "unavailable_no_approved_add_score_metric":
            counts["unavailable"] += 1
        if row.get("validation_status") != "pass":
            counts["invalid"] += 1
        if clean_text(row.get("baseline_misuse_status")).startswith("fail"):
            counts["baseline_misuse"] += 1
    lines = [
        "# Mature Model Row-Level Metric Row Audit",
        "",
        f"- audit_id: `{AUDIT_ID}`",
        f"- audit_version: `{AUDIT_VERSION}`",
        f"- generated_at: `{rows[0]['generated_at'] if rows else now_taipei()}`",
        f"- stock operation rows audited: `{len(rows)}`",
        "",
        "## Model Counts",
        "",
        "| model_id | rows | ready metric | explicit unavailable | invalid | baseline misuse |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for model_id, counts in sorted(model_counts.items()):
        lines.append(
            f"| `{model_id}` | {counts['rows']} | {counts['ready']} | {counts['unavailable']} | {counts['invalid']} | {counts['baseline_misuse']} |"
        )
    lines.extend(
        [
            "",
            "## Row Evidence",
            "",
            "| model_id | section | stock | row metric | scope | validation | baseline policy |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in rows:
        stock = f"{row.get('stock_id', '')} {row.get('stock_name', '')}".strip()
        lines.append(
            "| `{model_id}` | {section} | {stock} | `{metric_id}` | {scope} | {validation} | {baseline} |".format(
                model_id=row.get("model_id", ""),
                section=row.get("pdf_section", ""),
                stock=stock,
                metric_id=row.get("row_metric_id", "") or row.get("row_metric_status", ""),
                scope=row.get("row_metric_scope", ""),
                validation=row.get("validation_status", ""),
                baseline=row.get("baseline_misuse_status", ""),
            )
        )
    ROW_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_taipei()
    rows = build_rows(generated_at)
    row_rows = build_row_rows(generated_at)
    write_csv(rows)
    write_md(rows)
    write_row_csv(row_rows)
    write_row_md(row_rows)
    print(f"wrote {rel(LATEST_CSV)} rows={len(rows)}")
    print(f"wrote {rel(LATEST_MD)}")
    print(f"wrote {rel(ROW_AUDIT_CSV)} rows={len(row_rows)}")
    print(f"wrote {rel(ROW_AUDIT_MD)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
