from __future__ import annotations

import re
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
CANONICAL_CHATGPT_PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
STAGED_PATH_VALIDATOR = ROOT / "scripts" / "validate_daily_staged_paths.py"
THREAD_WORKFLOW_DOC = ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md"
RULES_DAILY = ROOT / "rules" / "daily_stock_candidate_rules.md"
DOCS_RULES_DAILY = ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md"
RULES_MASTER = ROOT / "rules" / "master_priority_rules.md"
DOCS_RULES_MASTER = ROOT / "docs" / "rules" / "master_priority_rules.md"
CODE_ISOLATION_POLICY_VALIDATOR = ROOT / "scripts" / "validate_repo_code_isolation_policy.py"


FORBIDDEN_DAILY_SCRIPT_PATTERNS = {
    "market timing backtest": r"scripts/build_market_timing_technical_backtest\.py",
    "weekly surge research": r"scripts/research_weekly_",
    "explosive-volume research": r"scripts/research_explosive_volume_up\.py",
    "surge precondition research model": r"scripts/build_surge_precondition_model\.py",
    "daily signal performance research": r"scripts/update_daily_candidate_signal_performance\.py",
    "daily signal performance report": r"scripts/generate_daily_signal_performance_report\.py",
    "catalyst performance backtest": r"scripts/update_catalyst_performance\.py",
    "MSCI rebalance backtest": r"scripts/build_msci_taiwan_rebalance_backtest\.py",
    "daily model parameter research": r"scripts/build_daily_model_parameter_research\.py",
    "daily model parameter recommendations research": r"scripts/build_daily_model_parameter_recommendations\.py",
    "daily candidate decision layer": r"scripts/build_daily_candidate_decision_layer\.py",
    "daily candidate decision validation": r"scripts/validate_daily_candidate_decision_layer\.py",
    "TDCC normalized signal structures": r"scripts/build_tdcc_signal_structures\.py",
    "TDCC normalized signal performance": r"scripts/update_tdcc_normalized_signal_performance\.py",
    "TDCC signal effectiveness report": r"scripts/build_tdcc_signal_effectiveness_report\.py",
    "TDCC ChatGPT tracking outputs": r"scripts/build_tdcc_chatgpt_tracking_outputs\.py",
    "TDCC weekly candidate reports": r"scripts/build_tdcc_weekly_candidate_reports\.py",
    "per-stock TDCC history": r"scripts/build_tdcc_stock_history\.py",
    "TDCC history backfill": r"scripts/backfill_tdcc_history\.py",
    "TDCC weekly holder fetch": r"tdcc_holder_ratio_top10\.py",
    "TDCC weekly signal tracker": r"tdcc_signal_tracker\.py",
}

FORBIDDEN_DAILY_STAGE_PATTERNS = {
    "research history outputs": r"git add\s+output/history/research/",
    "surge model outputs": r"git add\s+output/history/surge_model/",
    "TDCC signal history outputs": r"git add\s+output/history/tdcc_signals/",
    "TDCC weekly latest outputs": r"git add\s+output/latest/tdcc_",
    "code files during output commit": r"git add\s+scripts/",
    "workflow files during output commit": r"git add\s+\.github/workflows/",
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def run_code_isolation_policy_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_code_isolation_policy",
        CODE_ISOLATION_POLICY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo code-isolation policy validator: {CODE_ISOLATION_POLICY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return list(module.validate())


def main() -> int:
    errors: list[str] = []
    daily_text = read_text(DAILY_WORKFLOW)

    errors.extend(run_code_isolation_policy_validation())

    for label, pattern in FORBIDDEN_DAILY_SCRIPT_PATTERNS.items():
        if re.search(pattern, daily_text):
            errors.append(f"daily_full_pipeline must not run {label}: {pattern}")

    for label, pattern in FORBIDDEN_DAILY_STAGE_PATTERNS.items():
        if re.search(pattern, daily_text):
            errors.append(f"daily_full_pipeline must not auto-stage {label}: {pattern}")

    volume_watch_commands = re.findall(r"python\s+scripts/build_volume_breakout_watch\.py(?P<args>[^\n]*)", daily_text)
    for args in volume_watch_commands:
        if "--latest-only" not in args:
            errors.append("daily_full_pipeline may run build_volume_breakout_watch.py only with --latest-only")

    staged_path_validation_count = daily_text.count("python scripts/validate_daily_staged_paths.py")
    if staged_path_validation_count < 2:
        errors.append("daily_full_pipeline must validate staged paths before both daily commit steps")

    if not STAGED_PATH_VALIDATOR.exists():
        errors.append(f"missing daily staged path validator: {STAGED_PATH_VALIDATOR}")

    if not CANONICAL_CHATGPT_PDF_GENERATOR.exists():
        errors.append(f"missing canonical ChatGPT-side PDF generator: {CANONICAL_CHATGPT_PDF_GENERATOR}")
    else:
        generator_text = read_text(CANONICAL_CHATGPT_PDF_GENERATOR)
        if "CATEGORY_SPECS" in generator_text:
            errors.append("canonical ChatGPT-side PDF generator must not contain legacy CATEGORY_SPECS fallback")
        if 'REPO = ROOT / "tdcc-weekly-report-git"' in generator_text:
            errors.append("canonical ChatGPT-side PDF generator must not hard-code tdcc-weekly-report-git sibling path")
        forbidden_chart_literals = {
            "tail(180)": "ChatGPT-side daily PDF K-line charts must use the half-year 126-trading-day view",
            "kline_180": "ChatGPT-side daily PDF chart filenames must not imply a 180-day display window",
            "180日K線": "ChatGPT-side daily PDF chart titles must not label the display as 180 days",
        }
        for literal, message in forbidden_chart_literals.items():
            if literal in generator_text:
                errors.append(f"{message}: found {literal!r}")
        raw_readme = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT"
        pages_readme = "https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT"
        raw_index = generator_text.find(raw_readme)
        pages_index = generator_text.find(pages_readme)
        if raw_index == -1:
            errors.append("ChatGPT-side daily PDF generator must include raw GitHub README source")
        if pages_index != -1 and raw_index != -1 and pages_index < raw_index:
            errors.append("ChatGPT-side daily PDF generator must try raw GitHub README before Pages README")

    thread_workflow_text = read_text(THREAD_WORKFLOW_DOC)
    if "generate_repo_chatgpt_side_reports.py" in thread_workflow_text:
        errors.append("thread workflow doc must point to canonical repo PDF generator, not the old OneDrive helper")

    if read_text(RULES_DAILY) != read_text(DOCS_RULES_DAILY):
        errors.append("docs/rules/daily_stock_candidate_rules.md must match rules/daily_stock_candidate_rules.md")

    daily_rules_text = read_text(RULES_DAILY)
    if "180-day windows" in daily_rules_text:
        errors.append("daily stock candidate rules must not instruct daily PDF K-line charts to use 180-day windows")

    if read_text(RULES_MASTER) != read_text(DOCS_RULES_MASTER):
        errors.append("docs/rules/master_priority_rules.md must match rules/master_priority_rules.md")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("daily production boundary validation passed")
    print(f"validated_workflow={DAILY_WORKFLOW.relative_to(ROOT).as_posix()}")
    print(f"validated_generator={CANONICAL_CHATGPT_PDF_GENERATOR.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
