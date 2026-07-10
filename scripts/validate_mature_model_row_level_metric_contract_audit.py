from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_mature_model_row_level_metric_contract_audit import (
    ADAPTER_BY_MODEL,
    AUDIT_ID,
    AUDIT_VERSION,
    GENERIC_COMBO_PREFIXES,
    HIGH_POSITION_AUDIT_CSV,
    LATEST_CSV,
    LATEST_MD,
    MATURE_OPERATION_SECTIONS,
    OUTPUT_COLUMNS,
    READINESS_CSV,
    TECHNICAL_PACKAGE_COLUMNS,
    approved_pattern_for,
    generic_combo_policy_status,
    mature_operation_rows,
    mature_readiness_rows,
    pct_number,
    price_pullback_source_status,
    read_csv,
    technical_package_worse_status,
    truthy,
)


ROOT = Path(__file__).resolve().parents[1]
APPROVED_PATTERNS_CSV = ROOT / "output" / "latest" / "approved_operation_patterns_latest.csv"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def require_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path.relative_to(ROOT).as_posix()}")


def load_audit() -> pd.DataFrame:
    require_file(LATEST_CSV)
    require_file(LATEST_MD)
    audit = read_csv(LATEST_CSV)
    if audit.empty:
        fail("mature model row-level metric audit must not be empty")
    missing = sorted(set(OUTPUT_COLUMNS) - set(audit.columns))
    if missing:
        fail(f"audit CSV missing columns: {missing}")
    if set(audit["audit_id"].astype(str)) != {AUDIT_ID}:
        fail(f"audit_id must be {AUDIT_ID}")
    if set(audit["audit_version"].astype(str)) != {AUDIT_VERSION}:
        fail(f"audit_version must be {AUDIT_VERSION}")
    issue_rows = audit[audit["issues"].astype(str).str.strip().ne("")]
    if not issue_rows.empty:
        fail(
            "audit contains issues: "
            + "; ".join(
                f"{row.model_id}={row.issues}"
                for row in issue_rows[["model_id", "issues"]].itertuples(index=False)
            )
        )
    return audit


def validate_mature_model_coverage(audit: pd.DataFrame) -> pd.DataFrame:
    readiness = read_csv(READINESS_CSV)
    mature = mature_readiness_rows(readiness)
    mature_ids = set(mature["model_id"].astype(str))
    audit_mature = audit[audit["audit_scope"].eq("mature_model")]
    audit_ids = set(audit_mature["model_id"].astype(str))
    missing = sorted(mature_ids - audit_ids)
    extra = sorted(audit_ids - mature_ids)
    if missing:
        fail(f"audit missing mature models: {missing}")
    if extra:
        fail(f"audit has unexpected mature models: {extra}")
    return mature


def combo_groups(columns: list[str]) -> list[str]:
    return [prefix for prefix in GENERIC_COMBO_PREFIXES if any(column.startswith(prefix) for column in columns)]


def validate_adapter_model(model_id: str, approved: pd.DataFrame) -> None:
    adapter_path = ADAPTER_BY_MODEL.get(model_id)
    if adapter_path is None:
        fail(f"{model_id}: missing adapter mapping")
    require_file(adapter_path)
    adapter = read_csv(adapter_path)
    rows = mature_operation_rows(adapter, model_id)
    if rows.empty:
        return
    if "win_rate_zh" not in rows.columns:
        fail(f"{model_id}: operation data rows must carry baseline win_rate_zh")
    if rows["win_rate_zh"].astype(str).str.strip().eq("").any():
        fail(f"{model_id}: operation data rows must not have blank baseline win_rate_zh")

    if "operation_quality" in rows.columns:
        technical = rows[rows["operation_quality"].astype(str).eq("technical_strength")]
    else:
        technical = rows.iloc[0:0].copy()

    if not technical.empty:
        missing = sorted(TECHNICAL_PACKAGE_COLUMNS - set(technical.columns))
        if missing:
            fail(f"{model_id}: technical_strength rows missing technical metric columns: {missing}")
        blank = sorted(
            column for column in TECHNICAL_PACKAGE_COLUMNS if technical[column].astype(str).str.strip().eq("").any()
        )
        if blank:
            fail(f"{model_id}: technical_strength rows have blank technical metric columns: {blank}")
        source_status = price_pullback_source_status(approved_pattern_for(model_id, approved), technical)
        if source_status.startswith("fail"):
            fail(f"{model_id}: {source_status}")
        worse_status = technical_package_worse_status(technical)
        if worse_status.startswith("fail"):
            fail(f"{model_id}: {worse_status}")
        first = technical.iloc[0]
        rate_sum = sum(
            pct_number(first.get(column)) or 0.0
            for column in [
                "technical_package_win_rate_zh",
                "technical_package_neutral_rate_zh",
                "technical_package_failure_rate_zh",
            ]
        )
        if abs(rate_sum - 100.0) > 0.05:
            fail(f"{model_id}: technical package win/neutral/failure rates must sum to 100, got {rate_sum}")

    groups = combo_groups(list(rows.columns))
    recompute_status, worse_status, issues = generic_combo_policy_status(rows, groups)
    if issues:
        fail(f"{model_id}: generic combo metric errors: {issues}")
    if any(part.endswith("fail_missing_metric_id") for part in recompute_status.split("|")):
        fail(f"{model_id}: generic combo metric group missing id column")
    if any("fail_combo_worse_than_baseline" in part for part in worse_status.split("|")):
        fail(f"{model_id}: generic combo metric group is worse than baseline")


def validate_promoted_high_position(audit: pd.DataFrame) -> None:
    rows = audit[audit["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")]
    if len(rows) != 1:
        fail("high-position volume attack must have exactly one mature-model audit row")
    row = rows.iloc[0]
    if row["audit_scope"] != "mature_model":
        fail("high-position volume attack must be audited as mature_model after promotion")
    if str(row["approved_for_daily"]).lower() not in {"true", "1", "yes"}:
        fail("high-position mature row must be approved_for_daily")
    if row["production_readiness"] != "production_adapter_contract_checked":
        fail("high-position mature row must check the production adapter contract")
    if row["pdf_row_display_policy_status"] != (
        "pass_pdf_rows_must_use_row_level_metric_when_operation_quality_or_combo_id_matches"
    ):
        fail("high-position mature row must enforce row-level metric display policy")
    require_file(HIGH_POSITION_AUDIT_CSV)
    research = read_csv(HIGH_POSITION_AUDIT_CSV)
    combos = research[research["row_type"].eq("pdf_bonus_combo")]
    if combos.empty:
        fail("high-position research audit must keep exact pdf_bonus_combo rows")
    if not combos["condition_role"].astype(str).eq("pdf_metric_combo_research_only_not_hidden_gate").all():
        fail("high-position pdf_bonus_combo rows must remain research-only non-gate diagnostics")
    if not set(combos["approved_for_daily"].astype(str).str.lower()) <= {"false", "0", ""}:
        fail("high-position pdf_bonus_combo rows must not be approved_for_daily")
    if not combos["production_readiness"].astype(str).eq("not_production_ready_research_only").all():
        fail("high-position pdf_bonus_combo rows remain promotion evidence and must not be direct production rows")


def validate_markdown(audit: pd.DataFrame) -> None:
    text = LATEST_MD.read_text(encoding="utf-8")
    required = [
        "Single add-score item may use the approved single-item metric.",
        "Multi-item add-score combinations must use the exact recomputed combination metric.",
        "A promoted row-level combination must not be worse than the baseline",
        "Research-only combo rows must remain unavailable to PDF operation rows",
    ]
    for token in required:
        if token not in text:
            fail(f"markdown audit missing contract token: {token}")
    for model_id in audit["model_id"].astype(str):
        if model_id not in text:
            fail(f"markdown audit missing model_id: {model_id}")


def main() -> int:
    audit = load_audit()
    validate_mature_model_coverage(audit)
    approved = read_csv(APPROVED_PATTERNS_CSV)
    for model_id in audit[audit["audit_scope"].eq("mature_model")]["model_id"].astype(str):
        validate_adapter_model(model_id, approved)
    validate_promoted_high_position(audit)
    validate_markdown(audit)
    print(f"mature_model_row_level_metric_contract_audit validation passed rows={len(audit)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
