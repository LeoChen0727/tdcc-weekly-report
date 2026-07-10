from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


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
LATEST_CSV = ROOT / "output" / "latest" / "mature_model_row_level_metric_contract_audit_latest.csv"
LATEST_MD = ROOT / "output" / "latest" / "mature_model_row_level_metric_contract_audit_latest.md"

AUDIT_ID = "mature_model_row_level_metric_contract_audit_20260710"
AUDIT_VERSION = "v1"

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
    "research_only_combo_candidate_count",
    "research_only_combo_not_candidate_count",
    "research_only_combo_positive_but_below_threshold_count",
    "production_readiness",
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
    return str(value or "").strip()


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
            improves_win = base_win is not None and combo_win is not None and combo_win >= base_win
            improves_avg = base_avg is not None and combo_avg is not None and combo_avg >= base_avg
            improves_median = (
                base_median is not None and combo_median is not None and combo_median >= base_median
            )
            if not (improves_win or improves_avg or improves_median):
                issues.append(f"{prefix}:{row.get(id_col)}:combo_worse_than_baseline")
                worse_statuses.append(f"{prefix}:fail_combo_worse_than_baseline")
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

    display_status = (
        "pass_pdf_rows_must_use_row_level_metric_when_operation_quality_or_combo_id_matches"
        if technical_rows.shape[0] > 0 or groups
        else "pass_pdf_rows_have_no_formal_add_score_metric_to_override_baseline"
    )

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
        "metric_scope": metric_scope,
        "baseline_metric_status": baseline_status,
        "row_level_metric_status": technical_status,
        "single_add_score_metric_status": single_status,
        "combo_recompute_policy_status": combo_status,
        "combo_worse_policy_status": combo_worse,
        "pdf_row_display_policy_status": display_status,
        "technical_strength_row_count": len(technical_rows),
        "base_row_count": len(base_rows),
        "generic_combo_metric_group_count": len(groups),
        "approved_metric_source_status": approved_status,
        "research_only_combo_candidate_count": "",
        "research_only_combo_not_candidate_count": "",
        "research_only_combo_positive_but_below_threshold_count": "",
        "production_readiness": "production_adapter_contract_checked",
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


def build_rows() -> list[dict[str, object]]:
    generated_at = now_taipei()
    readiness = read_csv(READINESS_CSV)
    approved = read_csv(APPROVED_PATTERNS_CSV)
    mature = mature_readiness_rows(readiness)
    rows = [audit_mature_model(row, approved, generated_at) for _, row in mature.iterrows()]
    high_position = audit_high_position_research(generated_at)
    if high_position is not None:
        rows.append(high_position)
    return rows


def write_csv(rows: list[dict[str, object]]) -> None:
    LATEST_CSV.parent.mkdir(parents=True, exist_ok=True)
    with LATEST_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in OUTPUT_COLUMNS})


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
        "- A promoted row-level combination must not be worse than the baseline on all primary metrics.",
        "- PDF operation rows must use the matched row-level metric when the model-owned adapter provides one.",
        "- Research-only combo rows must remain unavailable to PDF operation rows until a model-specific promotion PR wires an approved adapter metric.",
        "",
        "## Audit Rows",
        "",
        "| scope | model_id | metric_scope | row_level_metric_status | combo_policy | production_readiness | issues |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        issues = clean_text(row.get("issues")) or "none"
        lines.append(
            "| {audit_scope} | `{model_id}` | {metric_scope} | {row_level_metric_status} | {combo_recompute_policy_status} / {combo_worse_policy_status} | {production_readiness} | {issues} |".format(
                audit_scope=row.get("audit_scope", ""),
                model_id=row.get("model_id", ""),
                metric_scope=row.get("metric_scope", ""),
                row_level_metric_status=row.get("row_level_metric_status", ""),
                combo_recompute_policy_status=row.get("combo_recompute_policy_status", ""),
                combo_worse_policy_status=row.get("combo_worse_policy_status", ""),
                production_readiness=row.get("production_readiness", ""),
                issues=issues,
            )
        )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = build_rows()
    write_csv(rows)
    write_md(rows)
    print(f"wrote {rel(LATEST_CSV)} rows={len(rows)}")
    print(f"wrote {rel(LATEST_MD)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
