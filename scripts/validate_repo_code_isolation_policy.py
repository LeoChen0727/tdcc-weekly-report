from __future__ import annotations

from pathlib import Path


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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
