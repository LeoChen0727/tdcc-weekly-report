from __future__ import annotations

import re
import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
CANONICAL_CHATGPT_PDF_ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
CANONICAL_CHATGPT_PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
DAILY_MARKET_ARTIFACT_BUILDER = ROOT / "build_daily_market_report_artifacts.py"
THEME_EVENT_WATCH_BUILDER = ROOT / "scripts" / "build_theme_event_watch.py"
WARRANT_FLOW_BUILDER = ROOT / "build_warrant_flow_latest.py"
DAILY_REPORT_SOURCE_RESOLVER = ROOT / "scripts" / "resolve_daily_report_source_state.py"
STAGED_PATH_VALIDATOR = ROOT / "scripts" / "validate_daily_staged_paths.py"
THREAD_WORKFLOW_DOC = ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md"
CHATGPT_DAILY_REPORT_USAGE_PROMPT = ROOT / "docs" / "CHATGPT_DAILY_REPORT_USAGE_PROMPT.md"
AGENTS_DOC = ROOT / "AGENTS.md"
STOCK_MODEL_CONTRACT_GOVERNANCE = ROOT / "docs" / "stock_model_contract_governance.md"
DAILY_PDF_CONSUMER_GOVERNANCE = ROOT / "docs" / "daily_pdf_contract_consumer_governance.md"
RULES_DAILY = ROOT / "rules" / "daily_stock_candidate_rules.md"
DOCS_RULES_DAILY = ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md"
RULES_MASTER = ROOT / "rules" / "master_priority_rules.md"
DOCS_RULES_MASTER = ROOT / "docs" / "rules" / "master_priority_rules.md"
CODE_ISOLATION_POLICY_VALIDATOR = ROOT / "scripts" / "validate_repo_code_isolation_policy.py"
REPO_PRODUCTION_INVENTORY_VALIDATOR = ROOT / "scripts" / "validate_repo_production_inventory.py"
REPO_FILE_LIFECYCLE_INVENTORY_VALIDATOR = ROOT / "scripts" / "validate_repo_file_lifecycle_inventory.py"
REPO_SEMANTIC_INTEGRITY_VALIDATOR = ROOT / "scripts" / "validate_repo_semantic_integrity.py"
REPO_ADVANCED_INTEGRITY_VALIDATOR = ROOT / "scripts" / "validate_repo_advanced_integrity.py"


FORBIDDEN_DAILY_SCRIPT_PATTERNS = {
    "retired fixed daily market PDF generator": r"scripts/generate_daily_market_pdf\.py",
    "retired fixed daily market PDF validator": r"scripts/validate_daily_market_report\.py",
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
    "all docs/latest outputs": r"git add\s+docs/latest/\s*\|\|\s*true",
    "all output/latest and docs/latest outputs": r"git add\s+output/latest/\s+docs/latest/\s*\|\|\s*true",
}


FORMAL_REPORT_DATE_HARD_GATE_FILES = {
    DAILY_MARKET_ARTIFACT_BUILDER: [
        "require_daily_report_ready_main_price_date",
    ],
    THEME_EVENT_WATCH_BUILDER: [
        "main_price_date_from_freshness",
    ],
}

FORBIDDEN_FORMAL_REPORT_DATE_FALLBACKS = {
    DAILY_MARKET_ARTIFACT_BUILDER: {
        'dates = candidates["date"].map(normalize_date)': "daily market artifact date must not fall back to all_candidates_latest.csv",
        "all_candidates_latest.csv date 最大值": "daily market artifact date must not fall back to all_candidates_latest.csv",
        'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")': "daily market artifact date must not fall back to wall-clock dates",
    },
    THEME_EVENT_WATCH_BUILDER: {
        'return datetime.now().strftime("%Y%m%d")': "theme event watch signal_date must not fall back to wall-clock dates",
        "or datetime.now()": "theme event watch base day must not fall back to wall-clock dates",
    },
    WARRANT_FLOW_BUILDER: {
        'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")': "warrant flow history date must come from warrant data, not wall-clock dates",
    },
}

DAILY_REPORT_SURFACES = [
    CANONICAL_CHATGPT_PDF_GENERATOR,
    DAILY_MARKET_ARTIFACT_BUILDER,
    ROOT / "build_chatgpt_daily_report_packet.py",
    ROOT / "build_chatgpt_daily_report_rules.py",
]

FORBIDDEN_DAILY_REPORT_DEPENDENCIES = {
    "action_decision_utils": "daily report surfaces must not import or call the old action/decision helper",
    "compute_action_decision": "daily report surfaces must not compute second-layer action decisions",
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def require_workflow_order(text: str, labels: list[str]) -> list[str]:
    errors: list[str] = []
    last_index = -1
    for label in labels:
        index = text.find(label, last_index + 1)
        if index < 0:
            errors.append(f"daily_full_pipeline missing workflow marker: {label}")
            continue
        last_index = index
    return errors


def run_code_isolation_policy_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_code_isolation_policy",
        CODE_ISOLATION_POLICY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo code-isolation policy validator: {CODE_ISOLATION_POLICY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return list(module.validate())


def run_repo_production_inventory_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_production_inventory",
        REPO_PRODUCTION_INVENTORY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo production inventory validator: {REPO_PRODUCTION_INVENTORY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return list(module.validate())


def run_repo_file_lifecycle_inventory_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_file_lifecycle_inventory",
        REPO_FILE_LIFECYCLE_INVENTORY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo file lifecycle inventory validator: {REPO_FILE_LIFECYCLE_INVENTORY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return list(module.validate())


def run_repo_semantic_integrity_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_semantic_integrity",
        REPO_SEMANTIC_INTEGRITY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo semantic integrity validator: {REPO_SEMANTIC_INTEGRITY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return list(module.validate())


def run_repo_advanced_integrity_validation() -> list[str]:
    spec = importlib.util.spec_from_file_location(
        "validate_repo_advanced_integrity",
        REPO_ADVANCED_INTEGRITY_VALIDATOR,
    )
    if spec is None or spec.loader is None:
        return [f"cannot load repo advanced integrity validator: {REPO_ADVANCED_INTEGRITY_VALIDATOR}"]

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return list(module.validate(include_external_sources=False))


def main() -> int:
    errors: list[str] = []
    daily_text = read_text(DAILY_WORKFLOW)

    errors.extend(run_code_isolation_policy_validation())
    errors.extend(run_repo_production_inventory_validation())
    errors.extend(run_repo_file_lifecycle_inventory_validation())
    errors.extend(run_repo_semantic_integrity_validation())
    errors.extend(run_repo_advanced_integrity_validation())

    for path, required_literals in FORMAL_REPORT_DATE_HARD_GATE_FILES.items():
        if not path.exists():
            errors.append(f"missing formal report date hard-gate file: {path.relative_to(ROOT).as_posix()}")
            continue
        text = read_text(path)
        for literal in required_literals:
            if literal not in text:
                errors.append(
                    f"{path.relative_to(ROOT).as_posix()} must use the formal daily freshness hard gate: missing {literal!r}"
                )

    for path, forbidden_literals in FORBIDDEN_FORMAL_REPORT_DATE_FALLBACKS.items():
        if not path.exists():
            continue
        text = read_text(path)
        for literal, message in forbidden_literals.items():
            if literal in text:
                errors.append(f"{message}: {path.relative_to(ROOT).as_posix()} contains {literal!r}")

    for path in DAILY_REPORT_SURFACES:
        if not path.exists():
            errors.append(f"missing daily report surface: {path.relative_to(ROOT).as_posix()}")
            continue
        text = read_text(path)
        for literal, message in FORBIDDEN_DAILY_REPORT_DEPENDENCIES.items():
            if literal in text:
                errors.append(f"{message}: {path.relative_to(ROOT).as_posix()} contains {literal!r}")

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

    calendar_precheck_literals = {
        "Record calendar source status before integrity gate": "daily_full_pipeline must record calendar status before the external-source hard gate",
        "Upload calendar source precheck evidence": "daily_full_pipeline must upload calendar precheck evidence before the external-source hard gate",
        "calendar-source-integrity-precheck": "daily_full_pipeline must expose a stable calendar-source evidence artifact",
        "GITHUB_STEP_SUMMARY": "daily_full_pipeline must write calendar-source hard-gate evidence to the step summary",
        "GITHUB_RUN_ID": "daily_full_pipeline calendar-source evidence must include the GitHub run id",
        "actions/upload-artifact@v4": "daily_full_pipeline must upload hard-gate precheck artifacts",
        "output/debug/external_source_integrity_precheck": "daily_full_pipeline must keep calendar-source hard-gate evidence in a stable debug path",
        "retention-days: 30": "daily_full_pipeline must retain calendar-source precheck evidence long enough for debugging",
        "continue-on-error: true": "daily_full_pipeline diagnostic artifact upload must not become a new production hard gate",
    }
    for literal, message in calendar_precheck_literals.items():
        if literal not in daily_text:
            errors.append(f"{message}: missing {literal!r}")
    errors.extend(
        require_workflow_order(
            daily_text,
            [
                "- name: Update catalyst data tables",
                "- name: Record calendar source status before integrity gate",
                "- name: Upload calendar source precheck evidence",
                "- name: Refresh data freshness before external-source integrity gate",
                "python build_data_freshness_latest.py",
                "python scripts/validate_data_freshness_latest.py",
                "- name: Validate refreshed external-source integrity",
            ],
        )
    )

    if not STAGED_PATH_VALIDATOR.exists():
        errors.append(f"missing daily staged path validator: {STAGED_PATH_VALIDATOR}")

    if not CANONICAL_CHATGPT_PDF_ENTRYPOINT.exists():
        errors.append(f"missing canonical ChatGPT-side PDF entrypoint: {CANONICAL_CHATGPT_PDF_ENTRYPOINT}")
    else:
        entrypoint_text = read_text(CANONICAL_CHATGPT_PDF_ENTRYPOINT)
        required_entrypoint_literals = {
            "resolve_daily_report_source_state": "official PDF entrypoint must use the origin/main resolver",
            '"worktree", "add", "--detach"': "official PDF entrypoint must use a clean temporary source worktree",
            "CHATGPT_DAILY_REPORT_ENTRYPOINT": "official PDF entrypoint must be the only allowed renderer caller",
            "PYTHONIOENCODING": "official PDF entrypoint must force UTF-8 subprocess output",
            'reconfigure(encoding="utf-8", errors="replace")': "official PDF entrypoint must force UTF-8 terminal output",
            "source-gate-only": "official PDF entrypoint must expose a source-gate-only diagnostic mode",
        }
        for literal, message in required_entrypoint_literals.items():
            if literal not in entrypoint_text:
                errors.append(f"{message}: missing {literal!r}")

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
        if "resolve_daily_report_source_state" not in generator_text:
            errors.append("ChatGPT-side daily PDF generator must use the origin/main daily report source resolver")
        if "require_entrypoint_invocation" not in generator_text:
            errors.append("ChatGPT-side daily PDF generator CLI must be blocked unless called by the official entrypoint")
        if "run_chatgpt_daily_report_entrypoint.py" not in generator_text:
            errors.append("blocked generator CLI must tell users to use the official entrypoint")
        if "--request-date" in generator_text or "args.request_date" in generator_text:
            errors.append("ChatGPT-side daily PDF generator must not accept manual request-date overrides")
        if "fetch_remote_readme_values" in generator_text:
            errors.append("ChatGPT-side daily PDF generator must not resolve freshness from raw/Pages README fallback")
        if "REMOTE_README_URLS" in generator_text:
            errors.append("ChatGPT-side daily PDF generator must not keep raw/Pages README fallback URL order")
        if 'REQUEST_DATE = datetime.now().strftime("%Y%m%d")' in generator_text:
            errors.append("ChatGPT-side daily PDF generator must not derive report date from wall-clock time")

    if not DAILY_REPORT_SOURCE_RESOLVER.exists():
        errors.append(f"missing daily report source resolver: {DAILY_REPORT_SOURCE_RESOLVER}")
    else:
        resolver_text = read_text(DAILY_REPORT_SOURCE_RESOLVER)
        required_resolver_literals = {
            "git fetch": "daily report source resolver must fetch origin/main before official generation",
            "git show": "daily report source resolver must read origin/main files through git show",
            "origin/main": "daily report source resolver must default to origin/main",
            "data_freshness_latest.csv": "daily report source resolver must gate on freshness CSV",
            "READ_ME_FIRST_DAILY_REPORT.txt": "daily report source resolver must cross-check README fields",
            "chatgpt_daily_report_packet_latest.txt": "daily report source resolver must cross-check the daily packet",
            "OneDrive": "daily report source resolver must reject OneDrive/helper source paths",
        }
        for literal, message in required_resolver_literals.items():
            if literal not in resolver_text:
                errors.append(f"{message}: missing {literal!r}")

    thread_workflow_text = read_text(THREAD_WORKFLOW_DOC)
    if "scripts/run_chatgpt_daily_report_entrypoint.py" not in thread_workflow_text:
        errors.append("thread workflow doc must point official daily PDF generation to the entrypoint")
    if "renderer, not the official entrypoint" not in thread_workflow_text:
        errors.append("thread workflow doc must distinguish the PDF renderer from the official entrypoint")
    if "generate_repo_chatgpt_side_reports.py" in thread_workflow_text:
        errors.append("thread workflow doc must point to canonical repo PDF generator, not the old OneDrive helper")

    usage_prompt_text = read_text(CHATGPT_DAILY_REPORT_USAGE_PROMPT)
    required_usage_literals = {
        "scripts/run_chatgpt_daily_report_entrypoint.py --source-gate-only": "daily usage prompt must require source-gate-only before official PDF generation",
        "scripts/run_chatgpt_daily_report_entrypoint.py": "daily usage prompt must point official PDF generation to the entrypoint",
        "git show origin/main": "daily usage prompt must use git show origin/main as the hard source gate",
        "chatgpt_daily_report_packet_latest.txt": "daily usage prompt must include packet consistency in the hard source gate",
        "六份": "daily usage prompt must state the six formal ChatGPT-side PDFs",
        "chatgpt_daily_report_runtime_manifest.json": "daily usage prompt must require runtime lineage manifest evidence",
    }
    for literal, message in required_usage_literals.items():
        if literal not in usage_prompt_text:
            errors.append(f"{message}: missing {literal!r}")

    forbidden_usage_literals = {
        "優先讀 GitHub Pages": "daily usage prompt must not tell new conversations to read Pages first",
        "如果 Pages 讀不到，再讀 raw": "daily usage prompt must not use Pages-first fallback wording",
        "請同時提供四份成品": "daily usage prompt must not use the retired four-PDF contract",
        "daily_market_curated_pdf_pages_url": "daily usage prompt must not present repo artifact PDF URLs as formal ChatGPT-side deliverables",
    }
    for literal, message in forbidden_usage_literals.items():
        if literal in usage_prompt_text:
            errors.append(f"{message}: found {literal!r}")

    if read_text(RULES_DAILY) != read_text(DOCS_RULES_DAILY):
        errors.append("docs/rules/daily_stock_candidate_rules.md must match rules/daily_stock_candidate_rules.md")

    daily_rules_text = read_text(RULES_DAILY)
    if "180-day windows" in daily_rules_text:
        errors.append("daily stock candidate rules must not instruct daily PDF K-line charts to use 180-day windows")

    if read_text(RULES_MASTER) != read_text(DOCS_RULES_MASTER):
        errors.append("docs/rules/master_priority_rules.md must match rules/master_priority_rules.md")

    model_change_pdf_rule_literals = {
        AGENTS_DOC: {
            "formal daily operation-row adapter": (
                "AGENTS Formal Daily Model Change Rule must require model-owned operation-row adapters"
            ),
            "model_operation_readiness_latest.csv": (
                "AGENTS Formal Daily Model Change Rule must bind PDF presentation to model readiness"
            ),
            "pdf_integration_status=pdf_integrated_daily_adapter": (
                "AGENTS Formal Daily Model Change Rule must require integrated PDF adapter readiness"
            ),
            "presentation_allowed=False": (
                "AGENTS Formal Daily Model Change Rule must keep unintegrated models hidden from PDF presentation"
            ),
            "PDF renderer must not convert candidate signal rows": (
                "AGENTS Formal Daily Model Change Rule must forbid PDF-side lifecycle inference"
            ),
        },
        STOCK_MODEL_CONTRACT_GOVERNANCE: {
            "model-owned daily operation-row adapter contract": (
                "stock model contract governance must require model-owned PDF operation adapter contracts"
            ),
            "approved_for_daily_pdf=true": (
                "stock model contract governance must say registry approval alone is not lifecycle approval"
            ),
            "model_operation_readiness_latest.csv": (
                "stock model contract governance must bind operation PDF use to readiness artifacts"
            ),
            "pdf_integration_status=pdf_integrated_daily_adapter": (
                "stock model contract governance must require integrated PDF adapter readiness"
            ),
            "daily PDF renderer must not infer buyable, active, pending, exit, or stop-loss lifecycle rows": (
                "stock model contract governance must forbid PDF-side lifecycle inference"
            ),
        },
        DAILY_PDF_CONSUMER_GOVERNANCE: {
            "Model promotions that make an operation-oriented model visible in the daily PDF": (
                "daily PDF consumer governance must point operation-model visibility back to model promotion rules"
            ),
            "formal daily operation-row adapter contract": (
                "daily PDF consumer governance must require a model-owned operation adapter before rendering"
            ),
            "Registry approval alone does not authorize the PDF renderer to infer lifecycle": (
                "daily PDF consumer governance must forbid lifecycle inference from registry approval alone"
            ),
        },
    }
    for path, literals in model_change_pdf_rule_literals.items():
        text = read_text(path)
        for literal, message in literals.items():
            if literal not in text:
                errors.append(f"{message}: missing {literal!r} in {path.relative_to(ROOT).as_posix()}")

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
