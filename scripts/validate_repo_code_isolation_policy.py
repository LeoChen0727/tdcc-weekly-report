from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

AGENTS = ROOT / "AGENTS.md"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
BOUNDARY_VALIDATOR = ROOT / "scripts" / "validate_daily_production_boundaries.py"
PDF_LAYOUT_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_side_pdf_layout_independence.py"
THREAD_WORKFLOW_DOC = ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md"
RULES_MASTER = ROOT / "rules" / "master_priority_rules.md"
DOCS_RULES_MASTER = ROOT / "docs" / "rules" / "master_priority_rules.md"
RULES_DAILY = ROOT / "rules" / "daily_stock_candidate_rules.md"
DOCS_RULES_DAILY = ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md"
POLICY_TEST = ROOT / "tests" / "test_repo_code_isolation_policy.py"


REQUIRED_POLICY_TEXT = {
    AGENTS: [
        "精確.按照規則辦事",
        "All business-facing code in this repository defaults to independent ownership.",
        "Do not share business-semantic code across unrelated reports, models, parameters,",
        "Shared code is allowed only for low-level technical utilities",
        "Before editing any shared function, parameter table, helper, or workflow step,",
        "Stock model parameters, thresholds, scoring weights, ranking rules, and gates",
        "Changing A must not silently change B.",
    ],
    RULES_MASTER: [
        "## Default Code Isolation",
        "Program code must default to independent business surfaces.",
        "must not share business-semantic code across unrelated outputs",
        "Shared code is allowed only for low-level technical utilities",
        "A request to adjust one report, model, parameter, or field must not silently change another surface.",
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
    "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    "python scripts/validate_daily_production_boundaries.py",
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
        BOUNDARY_VALIDATOR,
        PDF_LAYOUT_VALIDATOR,
        THREAD_WORKFLOW_DOC,
        RULES_MASTER,
        DOCS_RULES_MASTER,
        RULES_DAILY,
        DOCS_RULES_DAILY,
        POLICY_TEST,
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
    print(f"validated_workflow={DAILY_WORKFLOW.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
