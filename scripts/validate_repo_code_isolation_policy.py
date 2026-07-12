from __future__ import annotations

import csv
from pathlib import Path

try:
    from validate_model_data_independence import validate as validate_model_data_independence
except ModuleNotFoundError:  # Imported as scripts.validate_repo_code_isolation_policy in pytest.
    from scripts.validate_model_data_independence import validate as validate_model_data_independence


ROOT = Path(__file__).resolve().parents[1]

AGENTS = ROOT / "AGENTS.md"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RESEARCH_WORKFLOW = ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml"
BOUNDARY_VALIDATOR = ROOT / "scripts" / "validate_daily_production_boundaries.py"
PDF_LAYOUT_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_side_pdf_layout_independence.py"
PDF_SHARED_PATH_VALIDATOR = ROOT / "scripts" / "validate_daily_pdf_shared_path_isolation.py"
PDF_COMPLETION_HARD_GATE = ROOT / "scripts" / "validate_daily_pdf_completion_hard_gate.py"
THREAD_WORKFLOW_DOC = ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md"
RULES_MASTER = ROOT / "rules" / "master_priority_rules.md"
DOCS_RULES_MASTER = ROOT / "docs" / "rules" / "master_priority_rules.md"
RULES_DAILY = ROOT / "rules" / "daily_stock_candidate_rules.md"
DOCS_RULES_DAILY = ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md"
POLICY_TEST = ROOT / "tests" / "test_repo_code_isolation_policy.py"
MODEL_RESEARCH_OWNERSHIP_REGISTRY = ROOT / "config" / "model_research_artifact_ownership.csv"
MODEL_RESEARCH_SENTINEL_REGISTRY = ROOT / "config" / "model_research_protected_sentinels.csv"
MODEL_RESEARCH_SHARED_UTILITY_REGISTRY = ROOT / "config" / "model_research_shared_utility_registry.csv"
MODEL_RESEARCH_SHARED_MIGRATION_REGISTRY = ROOT / "config" / "model_research_shared_utility_migrations.csv"
MODEL_RESEARCH_WORKFLOW_REGISTRY = ROOT / "config" / "model_research_workflow_entrypoints.csv"
FORMAL_EVIDENCE_PIN_REGISTRY = ROOT / "config" / "formal_model_evidence_pins.csv"
MODEL_RESEARCH_OWNERSHIP_VALIDATOR = ROOT / "scripts" / "validate_model_research_artifact_ownership.py"
MODEL_RESEARCH_SHARED_UTILITY_VALIDATOR = ROOT / "scripts" / "validate_model_research_shared_utilities.py"
MODEL_RESEARCH_WORKFLOW_VALIDATOR = ROOT / "scripts" / "validate_model_research_workflow_isolation.py"
FORMAL_EVIDENCE_PIN_VALIDATOR = ROOT / "scripts" / "validate_formal_model_evidence_pins.py"
MODEL_SEMANTIC_OWNERSHIP_REGISTRY = ROOT / "config" / "daily_model_semantic_ownership.csv"
MODEL_SHARED_SEMANTIC_REGISTRY = ROOT / "config" / "daily_model_shared_semantic_registry.csv"
MODEL_SEMANTIC_MIGRATION_REGISTRY = ROOT / "config" / "daily_model_semantic_migrations.csv"
MODEL_DATA_SHARING_REGISTRY = ROOT / "config" / "daily_model_data_sharing_registry.csv"
MODEL_DATA_SHARING_MIGRATION_REGISTRY = ROOT / "config" / "daily_model_data_sharing_migrations.csv"
MODEL_VALIDATOR_INDEPENDENCE_REGISTRY = ROOT / "config" / "daily_model_validator_independence.csv"
MODEL_DATA_INDEPENDENCE_CORE = ROOT / "scripts" / "model_data_independence.py"
MODEL_DATA_INDEPENDENCE_VALIDATOR = ROOT / "scripts" / "validate_model_data_independence.py"
MODEL_DATA_INDEPENDENCE_AUDIT_BUILDER = ROOT / "scripts" / "build_model_data_independence_audit.py"
NUMERICAL_ANOMALY_DISPOSITION_CONTRACT = (
    ROOT / "config" / "daily_model_numerical_anomaly_disposition_contract.csv"
)
REVENUE_ANOMALY_MODULE = ROOT / "scripts" / "revenue_unreacted_range_extreme_return_path_audit.py"
REVENUE_FIXED_FEATURE_MODULE = (
    ROOT / "scripts" / "revenue_unreacted_range_fixed_confirmation_feature_contrast.py"
)
REVENUE_CLOSE_TIMING_MODULE = (
    ROOT / "scripts" / "revenue_unreacted_range_close_confirmation_timing.py"
)
REVENUE_LAG_STRENGTH_MODULE = ROOT / "scripts" / "revenue_unreacted_range_lag_strength_matrix.py"
LEGACY_MODEL_RESEARCH_MODULE = ROOT / "scripts" / "build_daily_model_parameter_research.py"
REVENUE_ANOMALY_ARTIFACT = (
    ROOT
    / "output"
    / "latest"
    / "research_backtest"
    / "revenue_unreacted_range_extreme_return_path_audit_latest.csv"
)

ANOMALY_ROOT_CHECKS = (
    "identity_dedup_non_overlap",
    "formal_operation_replay",
    "point_in_time_and_trading_calendar",
    "raw_source_lineage_and_hash",
    "units_formula_and_adjustment_basis",
    "authoritative_business_event_history",
    "independent_source_corroboration",
    "reproducible_evidence_reference",
)

EXPECTED_ANOMALY_DISPOSITIONS = {
    "anomaly_candidate": (
        False,
        True,
        "retain_in_primary_metrics_pending_root_cause",
        "blocked_pending_root_cause",
    ),
    "unresolved_anomaly_candidate": (
        False,
        True,
        "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only",
        "blocked_pending_root_cause",
    ),
    "verified_real_extreme": (
        True,
        False,
        "retain_in_primary_metrics",
        "eligible_only_after_all_other_model_gates",
    ),
    "verified_data_error": (
        True,
        False,
        "repair_source_and_rerun_old_metrics_forbidden",
        "blocked_until_repaired_rerun",
    ),
    "verified_non_comparable": (
        True,
        False,
        "exclude_only_with_approved_reason_and_rerun",
        "requires_model_governance_review",
    ),
}


REQUIRED_POLICY_TEXT = {
    AGENTS: [
        "精確.按照規則辦事",
        "All business-facing code in this repository defaults to independent ownership.",
        "Do not share business-semantic code across unrelated reports, models, parameters,",
        "Shared code is allowed only for low-level technical utilities",
        "Before editing any shared function, parameter table, helper, or workflow step,",
        "Stock model parameters, thresholds, scoring weights, ranking rules, and gates",
        "Changing A must not silently change B.",
        "Model research producers must be model-owned entrypoints with model-owned",
        "Formal model evidence must be bound",
        "Every cross-model business-semantic utility must be registered",
        "cross-model utility migration",
        "protected mature-model artifact hashes",
        "Each model-research workflow input must default to `false`",
        "legacy cross-model aggregate producer",
        "New formal daily models must use a model-owned production module",
        "daily_model_semantic_ownership.csv",
        "daily_model_data_sharing_registry.csv",
        "daily_model_data_sharing_migrations.csv",
        "Independent promotion evidence validators must not import",
        "may only create an `anomaly_candidate`",
        "lowest available evidence layer",
        "unresolved_anomaly_candidate",
        "retained in the primary metrics",
        "verified_real_extreme",
        "Threshold-excluded metrics are sensitivity analysis only",
        "daily_model_numerical_anomaly_disposition_contract.csv",
        "retroactively treated as `anomaly_candidate`",
        "cannot be cited as final anomaly evidence or pinned formal",
    ],
    RULES_MASTER: [
        "## Default Code Isolation",
        "Program code must default to independent business surfaces.",
        "must not share business-semantic code across unrelated outputs",
        "Shared code is allowed only for low-level technical utilities",
        "A request to adjust one report, model, parameter, or field must not silently change another surface.",
        "Model research must use model-owned producer entrypoints and artifact allowlists.",
        "Formal model evidence must identify an immutable artifact version and canonical SHA-256",
        "Cross-model business-semantic utilities must be registered",
        "cross-model utility migration record",
        "protected mature-model artifact hashes",
        "Every model-research workflow input must default to `false`",
        "legacy cross-model aggregate producer",
        "New formal daily models must use a model-owned production module",
        "daily_model_semantic_ownership.csv",
        "daily_model_data_sharing_registry.csv",
        "daily_model_data_sharing_migrations.csv",
        "Independent promotion evidence validators must not import",
        "Numerical magnitude is an investigation trigger, not an anomaly disposition.",
        "unresolved_anomaly_candidate",
        "row remains in primary metrics",
        "verified_real_extreme",
        "Threshold-excluded metrics are sensitivity analysis only",
        "daily_model_numerical_anomaly_disposition_contract.csv",
        "retroactively `anomaly_candidate`",
        "forbidden as final anomaly evidence or pinned formal promotion evidence",
        "This policy is enforced by `scripts/validate_repo_code_isolation_policy.py`",
    ],
    RULES_DAILY: [
        "## ChatGPT-Side PDF Layout Isolation",
        "The six ChatGPT-side daily PDFs must have independent report builder and layout boundaries.",
        "must each have an explicit builder entrypoint",
        "Only low-level rendering utilities may be shared across the six PDFs",
        "Shared utilities must not choose report sections, columns, ranking, model interpretation, risk wording, or output-specific row limits.",
        "Daily PDF layout independence is enforced by `scripts/validate_chatgpt_side_pdf_layout_independence.py`",
    ],
    THREAD_WORKFLOW_DOC: [
        "Business-facing code defaults to independent ownership.",
        "Stock screening models must remain independent at the code and parameter",
        "Do not invent buy/sell decisions, mainstream/non-mainstream labels, ranking,",
        "Repository-level code-isolation policy is enforced by `scripts/validate_repo_code_isolation_policy.py`",
    ],
}


REQUIRED_WORKFLOW_COMMANDS = [
    "python scripts/validate_repo_code_isolation_policy.py",
    "python scripts/validate_model_research_workflow_isolation.py",
    "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    "python scripts/validate_daily_pdf_shared_path_isolation.py",
    "python scripts/validate_daily_pdf_completion_hard_gate.py",
    "python scripts/validate_daily_production_boundaries.py",
]


FORBIDDEN_RESEARCH_WORKFLOW_SNIPPETS = [
    "python build_chatgpt_daily_report_packet.py",
    "python build_chatgpt_daily_report_rules.py",
    "python publish_chatgpt_report_readme_and_check.py",
    "git add output/latest/CHATGPT_DAILY_REPORT",
    "git add output/latest/READ_ME_FIRST_DAILY_REPORT",
    "git add docs/latest/ || true",
]


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def read_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def _bool_text(value: str) -> bool | None:
    normalized = str(value).strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    return None


def validate_numerical_anomaly_governance() -> list[str]:
    errors: list[str] = []
    if not NUMERICAL_ANOMALY_DISPOSITION_CONTRACT.exists():
        return ["missing numerical anomaly disposition contract"]

    expected_fields = [
        "disposition_id",
        "is_final",
        "threshold_only_allowed",
        "primary_metric_policy",
        "promotion_policy",
        "required_root_checks",
        "description",
    ]
    fields, rows = read_csv_rows(NUMERICAL_ANOMALY_DISPOSITION_CONTRACT)
    if fields != expected_fields:
        errors.append("numerical anomaly disposition contract schema drift")
        return errors
    by_id = {row["disposition_id"]: row for row in rows}
    if set(by_id) != set(EXPECTED_ANOMALY_DISPOSITIONS):
        errors.append("numerical anomaly disposition membership drift")
        return errors
    if len(by_id) != len(rows):
        errors.append("numerical anomaly disposition contract has duplicate ids")

    expected_checks = set(ANOMALY_ROOT_CHECKS)
    for disposition_id, expected in EXPECTED_ANOMALY_DISPOSITIONS.items():
        row = by_id[disposition_id]
        is_final = _bool_text(row["is_final"])
        threshold_allowed = _bool_text(row["threshold_only_allowed"])
        if (is_final, threshold_allowed, row["primary_metric_policy"], row["promotion_policy"]) != expected:
            errors.append(f"numerical anomaly disposition policy drift: {disposition_id}")
        checks = {item for item in row["required_root_checks"].split(";") if item}
        if disposition_id == "anomaly_candidate":
            if checks:
                errors.append("anomaly_candidate must not pretend root-cause checks are complete")
        elif checks != expected_checks:
            errors.append(f"numerical anomaly root checks drift: {disposition_id}")

    source_contracts = {
        REVENUE_ANOMALY_MODULE: {
            "required": (
                "ANOMALY_CANDIDATE_ABS_RETURN_PCT",
                "unresolved_anomaly_candidate",
                "partial_root_checks_incomplete",
                "retain_observed_candidate_and_block_promotion_until_resolved",
                "threshold_sensitivity_only_not_anomaly_disposition",
            ),
            "forbidden": (
                "EXTREME_ABS_RETURN_PCT",
                "plausible_extreme_continuous_gain",
                "exclude_abs_ge80_to_show_tail_dependence",
            ),
        },
        REVENUE_FIXED_FEATURE_MODULE: {
            "required": (
                "SOURCE_ANOMALY_CANDIDATE_SENSITIVITY_BASIS",
                "RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS",
                "feature_context_candidate_values_retained_in_feature_evidence",
                "blocked_pending_root_cause_anomaly_candidate_review",
            ),
            "forbidden": (
                "EXTREME_SENSITIVITY_BASIS",
                "blocked_pending_extreme_return_row_review",
                "feature_context_revenue_anomalies_excluded_from_feature_evidence",
            ),
        },
        REVENUE_CLOSE_TIMING_MODULE: {
            "required": (
                "including_unresolved_anomaly_candidates_primary",
                "excluding_unresolved_anomaly_candidates_sensitivity_only",
                "return_abs_ge80_anomaly_candidate_count",
                "blocked_pending_root_cause_anomaly_candidate_review",
            ),
            "forbidden": ("return_abs_ge80_count", '"blocked_return_dominance_review"'),
        },
        REVENUE_LAG_STRENGTH_MODULE: {
            "required": (
                "ANOMALY_CANDIDATE_ABS_RETURN_PCT",
                "abs_ge80_anomaly_candidate_flag",
                "blocked_pending_root_cause_anomaly_candidate_review",
            ),
            "forbidden": ("EXTREME_ABS_RETURN_PCT", "abs_ge80_return_flag"),
        },
        LEGACY_MODEL_RESEARCH_MODULE: {
            "required": (
                "PRIMARY_ANOMALY_BASIS",
                "ANOMALY_CANDIDATE_SENSITIVITY_BASIS",
                "_full_monthly_revenue_anomaly_candidate_mask",
                "return_abs_ge80_anomaly_candidate_count",
                "blocked_pending_root_cause_anomaly_candidate_review",
            ),
            "forbidden": (
                "return_abs_ge80_count",
                "blocked_pending_extreme_return_row_review",
                "excluding_known_price_or_revenue_anomalies",
                "excluding_known_revenue_and_price_anomalies",
                "excluding_revenue_numerical_anomalies",
                "excluding_known_data_quality_exceptions",
            ),
        },
    }
    for path, contract in source_contracts.items():
        if not path.exists():
            errors.append(f"missing numerical anomaly governed source: {path.relative_to(ROOT).as_posix()}")
            continue
        text = read_text(path)
        for snippet in contract["required"]:
            if snippet not in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} missing anomaly governance token: {snippet}")
        for snippet in contract["forbidden"]:
            if snippet in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} retains forbidden threshold-only token: {snippet}")

    if not REVENUE_ANOMALY_ARTIFACT.exists():
        errors.append("missing revenue anomaly root-cause artifact")
        return errors
    fields, artifact_rows = read_csv_rows(REVENUE_ANOMALY_ARTIFACT)
    required_artifact_fields = {
        "statistical_trigger_status",
        "root_cause_verification_status",
        "root_cause_checks_completed",
        "root_cause_checks_missing",
        "final_disposition",
        "primary_metric_handling",
        "candidate_threshold_sensitivity_handling",
    }
    missing_fields = required_artifact_fields - set(fields)
    if missing_fields:
        errors.append(f"revenue anomaly artifact missing root-cause fields: {sorted(missing_fields)}")
        return errors
    for row in artifact_rows:
        key = row.get("episode_key", "unknown")
        if row["statistical_trigger_status"] != "anomaly_candidate":
            errors.append(f"revenue anomaly threshold over-classified row: {key}")
        if row["root_cause_verification_status"] != "partial_root_checks_incomplete":
            errors.append(f"revenue anomaly root status drift: {key}")
        if row["final_disposition"] != "unresolved_anomaly_candidate":
            errors.append(f"revenue anomaly received premature final disposition: {key}")
        if not row["root_cause_checks_completed"] or not row["root_cause_checks_missing"]:
            errors.append(f"revenue anomaly root check evidence incomplete: {key}")
        if row["primary_metric_handling"] != "retain_observed_candidate_and_block_promotion_until_resolved":
            errors.append(f"revenue anomaly primary metric handling drift: {key}")
        if row["candidate_threshold_sensitivity_handling"] != "threshold_sensitivity_only_not_anomaly_disposition":
            errors.append(f"revenue anomaly sensitivity handling drift: {key}")

    formal_pin_text = read_text(FORMAL_EVIDENCE_PIN_REGISTRY)
    legacy_threshold_only_artifacts = (
        "volume_range_breakout_v2_semantic_audit",
        "volume_range_breakout_v2_raw_market_rerun",
        "volume_range_breakout_v2_condition_matrix",
    )
    for artifact_id in legacy_threshold_only_artifacts:
        if artifact_id in formal_pin_text:
            errors.append(
                "formal evidence pin points to a legacy threshold-only anomaly artifact: "
                f"{artifact_id}"
            )
    return errors


def validate() -> list[str]:
    errors: list[str] = []

    required_files = [
        AGENTS,
        DAILY_WORKFLOW,
        RESEARCH_WORKFLOW,
        BOUNDARY_VALIDATOR,
        PDF_LAYOUT_VALIDATOR,
        PDF_SHARED_PATH_VALIDATOR,
        PDF_COMPLETION_HARD_GATE,
        THREAD_WORKFLOW_DOC,
        RULES_MASTER,
        DOCS_RULES_MASTER,
        RULES_DAILY,
        DOCS_RULES_DAILY,
        POLICY_TEST,
        MODEL_RESEARCH_OWNERSHIP_REGISTRY,
        MODEL_RESEARCH_SENTINEL_REGISTRY,
        MODEL_RESEARCH_SHARED_UTILITY_REGISTRY,
        MODEL_RESEARCH_SHARED_MIGRATION_REGISTRY,
        MODEL_RESEARCH_WORKFLOW_REGISTRY,
        FORMAL_EVIDENCE_PIN_REGISTRY,
        MODEL_RESEARCH_OWNERSHIP_VALIDATOR,
        MODEL_RESEARCH_SHARED_UTILITY_VALIDATOR,
        MODEL_RESEARCH_WORKFLOW_VALIDATOR,
        FORMAL_EVIDENCE_PIN_VALIDATOR,
        MODEL_SEMANTIC_OWNERSHIP_REGISTRY,
        MODEL_SHARED_SEMANTIC_REGISTRY,
        MODEL_SEMANTIC_MIGRATION_REGISTRY,
        MODEL_DATA_SHARING_REGISTRY,
        MODEL_DATA_SHARING_MIGRATION_REGISTRY,
        MODEL_VALIDATOR_INDEPENDENCE_REGISTRY,
        MODEL_DATA_INDEPENDENCE_CORE,
        MODEL_DATA_INDEPENDENCE_VALIDATOR,
        MODEL_DATA_INDEPENDENCE_AUDIT_BUILDER,
        NUMERICAL_ANOMALY_DISPOSITION_CONTRACT,
        REVENUE_ANOMALY_MODULE,
        REVENUE_FIXED_FEATURE_MODULE,
        REVENUE_CLOSE_TIMING_MODULE,
        REVENUE_LAG_STRENGTH_MODULE,
        LEGACY_MODEL_RESEARCH_MODULE,
        REVENUE_ANOMALY_ARTIFACT,
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing required code-isolation policy file: {path.relative_to(ROOT).as_posix()}")

    for path, required_snippets in REQUIRED_POLICY_TEXT.items():
        if not path.exists():
            continue
        text = read_text(path)
        for snippet in required_snippets:
            if snippet not in text:
                errors.append(
                    f"{path.relative_to(ROOT).as_posix()} missing required code-isolation text: {snippet}"
                )

    if RULES_MASTER.exists() and DOCS_RULES_MASTER.exists():
        if read_text(RULES_MASTER) != read_text(DOCS_RULES_MASTER):
            errors.append("docs/rules/master_priority_rules.md must match rules/master_priority_rules.md")

    if RULES_DAILY.exists() and DOCS_RULES_DAILY.exists():
        if read_text(RULES_DAILY) != read_text(DOCS_RULES_DAILY):
            errors.append("docs/rules/daily_stock_candidate_rules.md must match rules/daily_stock_candidate_rules.md")

    if DAILY_WORKFLOW.exists():
        workflow_text = read_text(DAILY_WORKFLOW)
        for command in REQUIRED_WORKFLOW_COMMANDS:
            if command not in workflow_text:
                errors.append(f"daily_full_pipeline.yml must run {command}")

    if RESEARCH_WORKFLOW.exists():
        research_workflow_text = read_text(RESEARCH_WORKFLOW)
        for snippet in FORBIDDEN_RESEARCH_WORKFLOW_SNIPPETS:
            if snippet in research_workflow_text:
                errors.append(
                    "research_backtest_pipeline.yml must not rebuild or stage daily production route files: "
                    f"{snippet}"
                )

    if BOUNDARY_VALIDATOR.exists():
        boundary_text = read_text(BOUNDARY_VALIDATOR)
        if "validate_repo_code_isolation_policy.py" not in boundary_text:
            errors.append("daily production boundary validator must invoke repo code-isolation policy validation")

    if POLICY_TEST.exists():
        policy_test_text = read_text(POLICY_TEST)
        if "validate_repo_code_isolation_policy" not in policy_test_text:
            errors.append("pytest coverage must import validate_repo_code_isolation_policy")

    errors.extend(
        f"model/data independence: {error}"
        for error in validate_model_data_independence()
    )
    errors.extend(
        f"numerical anomaly governance: {error}"
        for error in validate_numerical_anomaly_governance()
    )

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("repo code-isolation policy validation passed")
    print(f"validated_agents={AGENTS.relative_to(ROOT).as_posix()}")
    print(f"validated_master_rules={RULES_MASTER.relative_to(ROOT).as_posix()}")
    print(f"validated_daily_rules={RULES_DAILY.relative_to(ROOT).as_posix()}")
    print(f"validated_pdf_shared_path={PDF_SHARED_PATH_VALIDATOR.relative_to(ROOT).as_posix()}")
    print(f"validated_workflow={DAILY_WORKFLOW.relative_to(ROOT).as_posix()}")
    print(f"validated_research_workflow={RESEARCH_WORKFLOW.relative_to(ROOT).as_posix()}")
    print(
        "validated_numerical_anomaly_contract="
        f"{NUMERICAL_ANOMALY_DISPOSITION_CONTRACT.relative_to(ROOT).as_posix()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
