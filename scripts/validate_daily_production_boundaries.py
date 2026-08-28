from __future__ import annotations

import argparse
import re
import importlib.util
import fnmatch
import posixpath
import shlex
import sys
from collections.abc import Sequence
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RECENT_PRICE_GAP_WORKFLOW = ROOT / ".github" / "workflows" / "repair_recent_daily_price_gaps.yml"
HISTORICAL_SOURCE_REPLAY_WORKFLOW = (
    ROOT / ".github" / "workflows" / "historical_structured_source_replay.yml"
)
DAILY_MODEL_MAINTENANCE_PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
VOLUME_V2_RUNTIME_BUILD_COMMAND = (
    "python scripts/build_volume_v2_warrant_lineage_history_audit.py --phase runtime"
)
VOLUME_V2_RUNTIME_VALIDATE_COMMAND = (
    "python scripts/validate_volume_v2_warrant_lineage_history_audit.py --phase runtime"
)
VOLUME_V2_RUNTIME_ARTIFACT_PATHS = (
    "docs/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
    "docs/latest/volume_v2_warrant_lineage_history_audit_latest.md",
    "output/latest/volume_v2_warrant_lineage_history_audit_latest.csv",
    "output/latest/volume_v2_warrant_lineage_history_audit_latest.md",
)
VOLUME_V2_RETIRED_NORMALIZATION_TOKENS = (
    "run_volume_v2_runtime_markdown_normalization_candidate_only",
    "expected_base_sha:",
    "expected_head_sha:",
    "confirmation:",
    "normalize_volume_v2_runtime_markdown_candidate",
    "volume_v2_runtime_markdown_normalization_candidate_commit",
    "volume-v2-runtime-markdown-normalization-candidate",
    "REPAIR_MODE",
    "REPAIR_RESULT",
    "Volume V2 normalization",
    "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY",
)
DAILY_PDF_REPLAY_PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_pdf_replay_pr_validation.yml"
DAILY_PDF_REPLAY_AUTOMATIC_PATHS = {
    "config/daily_pdf_rendered_model_regression_contract.csv",
    "config/daily_pdf_semantic_golden_cases.csv",
    "scripts/generate_chatgpt_side_daily_reports.py",
    "scripts/validate_chatgpt_side_pdf_contract.py",
}
MODEL_OUTPUT_PATHS_FORBIDDEN_FROM_DFKAI_REPLAY = {
    "output/latest/approved_operation_patterns_latest.csv",
    "output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
    "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
    "output/latest/daily_volume_breakout_operation_section_latest.csv",
    "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
    "output/latest/model_operation_readiness_latest.csv",
}
CANONICAL_CHATGPT_PDF_ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
CANONICAL_CHATGPT_PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
DAILY_MARKET_ARTIFACT_BUILDER = ROOT / "build_daily_market_report_artifacts.py"
DAILY_PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
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
PDF_INVENTORY_FULL_COMMAND = "python scripts/validate_pdf_production_inventory.py"
PDF_INVENTORY_PREBUILD_COMMAND = f"{PDF_INVENTORY_FULL_COMMAND} --phase prebuild"
PDF_INVENTORY_RUNTIME_COMMAND = f"{PDF_INVENTORY_FULL_COMMAND} --phase runtime"
PDF_CONSUMER_FULL_COMMAND = "python scripts/validate_daily_pdf_contract_consumers.py"
PDF_CONSUMER_RUNTIME_COMMAND = f"{PDF_CONSUMER_FULL_COMMAND} --phase runtime"
PDF_COMPLETION_FULL_COMMAND = "python scripts/validate_daily_pdf_completion_hard_gate.py"
PDF_COMPLETION_RUNTIME_COMMAND = f"{PDF_COMPLETION_FULL_COMMAND} --phase runtime"
LEGACY_REMOVAL_GUARD_COMMANDS = (
    "python scripts/validate_daily_legacy_volume_range_breakout_removed.py",
    "python scripts/validate_daily_legacy_mature_model_paths_removed.py",
)
DAILY_MODEL_LEGACY_REMOVAL_GUARD_STEP = "Validate selected production and PDF contracts"
DAILY_MODEL_PRODUCTION_PDF_SCOPE_CONDITION = (
    "needs.scope.outputs.production_pdf_contracts == 'true'"
)

PACKET_ROW_METRIC_REQUIRED_LITERALS = {
    'operation-row performance must consume row_metric_* only',
    '("row_metric_status", "row_metric_status")',
    '("row_metric_scope", "row_metric_scope")',
    '("row_metric_id", "row_metric_id")',
    '("row_metric_label", "row_metric_label_zh")',
    '("row_metric_sample_size", "row_metric_sample_size")',
    '("row_metric_win_rate", "row_metric_win_rate_zh")',
    '("row_metric_neutral_rate", "row_metric_neutral_rate_zh")',
    '("row_metric_failure_rate", "row_metric_failure_rate_zh")',
    '("row_metric_avg_return", "row_metric_avg_return_zh")',
    '("row_metric_median_return", "row_metric_median_return_zh")',
    '("row_metric_source", "row_metric_source")',
    '("row_metric_selection_status", "row_metric_selection_status")',
}
PACKET_ROW_METRIC_FORBIDDEN_BASELINE_LITERALS = {
    '("sample_size", "sample_size")',
    '("win_rate", "win_rate_zh")',
    '("avg_return", "avg_return_zh")',
    '("median_return", "median_return_zh")',
}


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

RETIRED_DAILY_HISTORICAL_DIAGNOSTIC_COMMANDS = (
    "python scripts/validate_daily_candidate_regression_cases.py",
    "python scripts/build_monthly_revenue_coverage_backfill_audit.py",
    "python scripts/validate_monthly_revenue_coverage_backfill_audit.py",
)


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

MODEL_OPERATION_PRICE_CONFIRMATION_RULE_LITERALS = {
    AGENTS_DOC: {
        "Formal operation buy/sell/stop/profit-taking rules": (
            "AGENTS Formal Daily Model Change Rule must require close-confirmed operation rules"
        ),
        "close-confirmed by": (
            "AGENTS Formal Daily Model Change Rule must require close-confirmed operation rules"
        ),
        "next trading day open": (
            "AGENTS Formal Daily Model Change Rule must allow only open/close realizable operation prices"
        ),
        "after a qualifying close confirmation": (
            "AGENTS Formal Daily Model Change Rule must require close confirmation before next-open exits"
        ),
        "same-day close": (
            "AGENTS Formal Daily Model Change Rule must allow close-confirmed same-day close exits"
        ),
        "intraday high/low as formal entry, exit, stop,": (
            "AGENTS Formal Daily Model Change Rule must forbid intraday high/low as formal operation prices"
        ),
        "profit-taking, win, failure, or realized-return prices": (
            "AGENTS Formal Daily Model Change Rule must forbid intraday high/low as formal operation prices"
        ),
        "research-only observation": (
            "AGENTS Formal Daily Model Change Rule must keep intraday high/low evidence advisory"
        ),
        "price_pullback_23ema": (
            "AGENTS Formal Daily Model Change Rule must explicitly protect the 23EMA research variant from promotion by intraday touch"
        ),
        "research_only_intraday_trigger": (
            "AGENTS Formal Daily Model Change Rule must label 23EMA intraday previous-high touch as research-only"
        ),
        "close_prev20_high_break_same_day_close": (
            "AGENTS Formal Daily Model Change Rule must forbid same-day close exit after close-confirmed 23EMA previous-high breakout"
        ),
    },
    STOCK_MODEL_CONTRACT_GOVERNANCE: {
        "Formal operation buy/sell/stop/profit-taking rules": (
            "stock model contract governance must require close-confirmed operation rules"
        ),
        "close-confirmed by default": (
            "stock model contract governance must require close-confirmed operation rules"
        ),
        "next trading day open": (
            "stock model contract governance must allow only open/close realizable operation prices"
        ),
        "after a qualifying close confirmation": (
            "stock model contract governance must require close confirmation before next-open exits"
        ),
        "same-day close": (
            "stock model contract governance must allow close-confirmed same-day close exits"
        ),
        "intraday high/low as formal entry, exit, stop, profit-taking, win, failure, or realized-return prices": (
            "stock model contract governance must forbid intraday high/low as formal operation prices"
        ),
        "research-only observation": (
            "stock model contract governance must keep intraday high/low evidence advisory"
        ),
        "price_pullback_23ema": (
            "stock model contract governance must explicitly protect the 23EMA research variant from promotion by intraday touch"
        ),
        "research_only_intraday_trigger": (
            "stock model contract governance must label 23EMA intraday previous-high touch as research-only"
        ),
        "close_prev20_high_break_same_day_close": (
            "stock model contract governance must forbid same-day close exit after close-confirmed 23EMA previous-high breakout"
        ),
    },
    ROOT / "docs" / "specs" / "price_pullback_23ema_operation_candidate_spec.md": {
        "Formal Price Confirmation Boundary": (
            "price_pullback_23ema operation candidate spec must state the formal price-confirmation boundary"
        ),
        "Intraday high/low observations must not be used as": (
            "price_pullback_23ema operation candidate spec must forbid intraday high/low as realized execution prices"
        ),
        "realized execution prices": (
            "price_pullback_23ema operation candidate spec must forbid intraday high/low as realized execution prices"
        ),
        "intraday high touches the signal-day previous 20-day high": (
            "price_pullback_23ema operation candidate spec must list the intraday-trigger same-day close research option"
        ),
        "research_only_intraday_trigger": (
            "price_pullback_23ema operation candidate spec must label intraday-trigger same-day close as research-only"
        ),
        "close breaks the signal-day previous 20-day high, then sell at the next": (
            "price_pullback_23ema operation candidate spec must list the next-open after close-confirmed exit option"
        ),
        "close_prev20_high_break_same_day_close": (
            "price_pullback_23ema operation candidate spec must forbid same-day close exit after close-confirmed breakout"
        ),
        "known only after that close": (
            "price_pullback_23ema operation candidate spec must explain why same-day close after close confirmation is invalid"
        ),
    },
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def display_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def validate_model_operation_price_confirmation_rules() -> list[str]:
    errors: list[str] = []
    for path, literals in MODEL_OPERATION_PRICE_CONFIRMATION_RULE_LITERALS.items():
        if not path.exists():
            errors.append(f"missing model operation price-confirmation rule file: {display_path(path)}")
            continue
        text = read_text(path)
        for literal, message in literals.items():
            if literal not in text:
                errors.append(f"{message}: missing {literal!r} in {display_path(path)}")
    return errors


def validate_daily_operation_packet_row_metric_contract() -> list[str]:
    if not DAILY_PACKET_BUILDER.exists():
        return [f"missing daily packet builder: {display_path(DAILY_PACKET_BUILDER)}"]
    text = read_text(DAILY_PACKET_BUILDER)
    start = text.find("def build_volume_operation_packet_lines()")
    if start < 0:
        return ["daily packet builder missing build_volume_operation_packet_lines"]
    next_function = text.find("\ndef ", start + 1)
    body = text[start : next_function if next_function >= 0 else len(text)]
    errors: list[str] = []
    missing = sorted(literal for literal in PACKET_ROW_METRIC_REQUIRED_LITERALS if literal not in body)
    if missing:
        errors.append(
            "daily operation packet must consume the model-owned row_metric contract: missing "
            + ";".join(missing)
        )
    forbidden = sorted(
        literal for literal in PACKET_ROW_METRIC_FORBIDDEN_BASELINE_LITERALS if literal in body
    )
    if forbidden:
        errors.append(
            "daily operation packet must not display whole-model baseline metrics in stock rows: "
            + ";".join(forbidden)
        )
    return errors


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


def workflow_job_block(text: str, job_id: str) -> str:
    marker = re.search(rf"(?m)^  {re.escape(job_id)}:\s*(?:#.*)?$", text)
    if marker is None:
        return ""
    start = marker.start()
    next_job = re.search(r"(?m)^  [A-Za-z0-9_-]+:\s*$", text[marker.end() :])
    if next_job is None:
        return text[start:]
    return text[start : marker.end() + next_job.start()]


def workflow_step_block(text: str, step_name: str) -> str:
    marker = f"      - name: {step_name}"
    start = text.find(marker)
    if start < 0:
        return ""
    next_step = text.find("\n      - name:", start + len(marker))
    if next_step < 0:
        return text[start:]
    return text[start:next_step]


def workflow_logical_commands(text: str) -> tuple[str, ...]:
    collapsed = re.sub(r"\\\r?\n\s*", " ", text)
    return tuple(
        command
        for line in collapsed.splitlines()
        if (command := " ".join(line.strip().removeprefix("run: ").split()))
        and not command.startswith("#")
    )


def validate_daily_full_legacy_removal_guard(daily_text: str) -> list[str]:
    logical_commands = workflow_logical_commands(daily_text)
    errors: list[str] = []
    for command in LEGACY_REMOVAL_GUARD_COMMANDS:
        script_path = command.removeprefix("python ")
        active_call = re.compile(
            rf"(?<![A-Za-z0-9_.-])python\s+(?:\./)?{re.escape(script_path)}"
            r"(?=$|[\s;&|)])"
        )
        if any(active_call.search(line) for line in logical_commands):
            errors.append(
                "Daily Full must not run repo-current legacy-removal guards: "
                f"{command}"
            )
    return errors


def validate_daily_model_legacy_removal_guard(pr_workflow_text: str) -> list[str]:
    errors: list[str] = []
    job_match = re.search(
        r"(?m)^  repo_current_contracts:\s*(?:#.*)?$",
        pr_workflow_text,
    )
    if job_match is None:
        return ["Daily Model PR workflow missing repo_current_contracts job"]
    repo_current_job = workflow_job_block(
        pr_workflow_text[job_match.start() :],
        "repo_current_contracts",
    )
    step = workflow_step_block(
        repo_current_job,
        DAILY_MODEL_LEGACY_REMOVAL_GUARD_STEP,
    )
    if not step:
        return [
            "Daily Model repo_current_contracts missing legacy-removal guard step: "
            f"{DAILY_MODEL_LEGACY_REMOVAL_GUARD_STEP}"
        ]

    run_match = re.search(
        r'(?m)^ {8}(?:run|["\']run["\'])\s*:\s*(?P<value>.*)$',
        step,
    )
    if run_match is None:
        return ["Daily Model legacy-removal guard step missing active run body"]
    run_value = run_match.group("value").strip()
    if run_value in {"|", "|-", ">", ">-"}:
        run_lines: list[str] = []
        for line in step[run_match.end() :].lstrip("\n").splitlines():
            indent = len(line) - len(line.lstrip())
            if line.strip() and indent <= 8:
                break
            if indent >= 10:
                run_lines.append(line[10:])
        run_body = "\n".join(run_lines)
    else:
        run_body = run_value.strip('"\'')

    run_commands = workflow_logical_commands(run_body)
    for command in LEGACY_REMOVAL_GUARD_COMMANDS:
        carriers = [line for line in run_commands if command in line]
        if len(carriers) != 1 or carriers[0] != command:
            errors.append(
                "Daily Model repo_current_contracts must run exactly one standalone "
                f"legacy-removal guard: {command}"
            )
    condition_match = re.search(
        r'(?m)^ {8}(?:if|["\']if["\'])\s*:\s*(?P<value>.+?)\s*$',
        step,
    )
    if (
        condition_match is None
        or condition_match.group("value")
        != DAILY_MODEL_PRODUCTION_PDF_SCOPE_CONDITION
    ):
        errors.append(
            "Daily Model legacy-removal guard step must use the exact "
            "production/PDF scope condition"
        )
    if re.search(
        r'(?m)^ {8}(?:continue-on-error|["\']continue-on-error["\'])\s*:',
        step,
    ):
        errors.append(
            "Daily Model legacy-removal guard step must not use continue-on-error"
        )
    if re.search(r'(?m)^ {8}(?:shell|["\']shell["\'])\s*:', step):
        errors.append("Daily Model legacy-removal guard step must not override shell")
    defaults_match = re.search(r"(?m)^    defaults:\s*(?:#.*)?$", repo_current_job)
    if defaults_match is not None:
        defaults_tail = repo_current_job[defaults_match.end() :]
        next_job_field = re.search(r"(?m)^    (?![ #\r\n])", defaults_tail)
        defaults_block = defaults_tail[
            : next_job_field.start() if next_job_field is not None else None
        ]
        if re.search(r"(?m)^      run:\s*(?:#.*)?$", defaults_block) and re.search(
            r"(?m)^        shell\s*:", defaults_block
        ):
            errors.append(
                "Daily Model repo_current_contracts must not override defaults.run.shell"
            )
    return errors


def workflow_pull_request_paths(text: str) -> set[str]:
    pull_request_trigger = text.split("  workflow_dispatch:", 1)[0]
    return {
        match.group(1)
        for line in pull_request_trigger.splitlines()
        if (match := re.fullmatch(r'\s*-\s+"?([^"\s]+)"?\s*', line))
    }


def validate_daily_model_pr_scope_contract(text: str) -> list[str]:
    errors: list[str] = []
    pull_request_match = re.search(r"(?m)^  pull_request:\s*(?:#.*)?$", text)
    if pull_request_match is None:
        errors.append("daily model maintenance PR workflow must run on pull_request")
    else:
        next_event = re.search(
            r"(?m)^  [A-Za-z0-9_-]+:\s*(?:#.*)?$",
            text[pull_request_match.end() :],
        )
        pull_request_block = text[
            pull_request_match.start() : (
                pull_request_match.end() + next_event.start()
                if next_event is not None
                else len(text)
            )
        ]
        if re.search(r"(?m)^\s{4}(?:paths|paths-ignore):", pull_request_block):
            errors.append(
                "daily model maintenance PR workflow pull_request trigger must remain all-PR "
                "without paths or paths-ignore filters"
            )

    if re.search(r"(?m)^  workflow_dispatch:\s*(?:#.*)?$", text) is None:
        errors.append("daily model maintenance PR workflow must support workflow_dispatch")

    scope_block = workflow_job_block(text, "scope")
    if not scope_block:
        errors.append("daily model maintenance PR workflow missing changed-path scope job")
    elif "python scripts/detect_daily_model_pr_validation_scope.py" not in scope_block:
        errors.append("daily model maintenance PR scope job must execute the scope detector")
    else:
        effective_base_output = (
            "effective_base_sha: ${{ steps.scope.outputs.effective_base_sha }}"
        )
        effective_base_consumption = (
            "BASE_SHA: ${{ needs.scope.outputs.effective_base_sha }}"
        )
        required_scope_literals = {
            effective_base_output: (
                "daily model maintenance PR scope must expose its effective base output"
            ),
            'effective_base_sha="origin/main"': (
                "daily model maintenance workflow_dispatch must retain origin/main base semantics"
            ),
            'git --no-replace-objects rev-list --parents -n 1 "$MERGE_SHA"': (
                "daily model maintenance PR scope must inspect the fetched synthetic merge parents"
            ),
            'read -r observed_merge observed_base observed_head unexpected_parent <<< "$merge_identity"': (
                "daily model maintenance PR scope must parse an exact two-parent merge identity"
            ),
            'if [ -z "$observed_merge" ] || [ -z "$observed_base" ] || [ -z "$observed_head" ] || [ -n "${unexpected_parent:-}" ]; then': (
                "daily model maintenance PR scope must reject malformed or extra merge parents"
            ),
            '[ "$observed_merge" != "$MERGE_SHA" ]': (
                "daily model maintenance PR scope must bind the observed merge SHA"
            ),
            '[ "$observed_head" != "$HEAD_SHA" ]': (
                "daily model maintenance PR scope must bind the observed head parent"
            ),
            'effective_base_sha="$observed_base"': (
                "daily model maintenance PR scope must use the synthetic merge first parent"
            ),
            '--base-sha "$effective_base_sha"': (
                "daily model maintenance PR detector must receive the effective first-parent base"
            ),
            'if [ -z "$effective_base_sha" ]; then': (
                "daily model maintenance PR scope must reject a missing effective base"
            ),
            "printf 'effective_base_sha=%s\\n' \"$effective_base_sha\" >> \"$GITHUB_OUTPUT\"": (
                "daily model maintenance PR scope must publish its verified effective base"
            ),
        }
        for literal, message in required_scope_literals.items():
            if literal not in scope_block:
                errors.append(message)
        if scope_block.count(effective_base_output) != 1:
            errors.append(
                "daily model maintenance PR scope effective base job output must be unique"
            )
        effective_base_write = "printf 'effective_base_sha=%s\\n'"
        if scope_block.count(effective_base_write) != 1:
            errors.append(
                "daily model maintenance PR scope effective base step output must be unique"
            )
        detector_call = (
            'python scripts/detect_daily_model_pr_validation_scope.py "${scope_args[@]}"'
        )
        if (
            detector_call in scope_block
            and effective_base_write in scope_block
            and scope_block.index(detector_call) > scope_block.index(effective_base_write)
        ):
            errors.append(
                "daily model maintenance PR scope must validate before publishing its effective base"
            )
        if "${{ github.event.pull_request.base.sha }}" in scope_block:
            errors.append(
                "daily model maintenance PR scope must not reuse the stale event base SHA"
            )
        if any(mask in scope_block for mask in ("|| true", "|| :", "; true")):
            errors.append(
                "daily model maintenance PR scope effective base validation must not be masked"
            )
        if text.count(effective_base_consumption) != 4:
            errors.append(
                "daily model maintenance PR repo/safety/shared/volume jobs must consume exactly four "
                "verified effective base bindings"
            )
        if "github.event.pull_request.base.sha" in text:
            errors.append(
                "daily model maintenance PR selected jobs must not reuse the stale event base"
            )

    aggregate_block = workflow_job_block(
        text,
        "daily-model-maintenance-pr-validation",
    )
    if not aggregate_block:
        errors.append("daily model maintenance PR workflow missing stable aggregate job")
    else:
        if "name: daily-model-maintenance-pr-validation" not in aggregate_block:
            errors.append("daily model maintenance PR aggregate must keep its stable check name")
        if "if: always()" not in aggregate_block:
            errors.append("daily model maintenance PR aggregate must evaluate all domain results")
    return errors


def validate_daily_model_volume_v2_runtime_markdown_contract(text: str) -> list[str]:
    errors: list[str] = []
    volume_job = workflow_job_block(text, "volume_v2_research")
    if not volume_job:
        errors.append("daily model PR workflow missing Volume V2 runtime job")

    for retired_token in VOLUME_V2_RETIRED_NORMALIZATION_TOKENS:
        if retired_token in text:
            errors.append(
                "daily model PR workflow contains retired Volume V2 normalization "
                f"token/job: {retired_token!r}"
            )

    exact_lines = {
        VOLUME_V2_RUNTIME_BUILD_COMMAND: text.count(
            f"          {VOLUME_V2_RUNTIME_BUILD_COMMAND}\n"
        ),
        VOLUME_V2_RUNTIME_VALIDATE_COMMAND: text.count(
            f"          {VOLUME_V2_RUNTIME_VALIDATE_COMMAND}\n"
        ),
    }
    for command, count in exact_lines.items():
        if count != 1:
            errors.append(
                "daily model PR Volume V2 runtime command must appear exactly once: "
                f"command={command!r} count={count}"
            )
    for script_path in (
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
    ):
        reference_count = text.count(script_path)
        if reference_count != 1:
            errors.append(
                "daily model PR Volume V2 builder/validator script reference must be unique: "
                f"script={script_path!r} count={reference_count}"
            )
    if (
        VOLUME_V2_RUNTIME_BUILD_COMMAND in volume_job
        and VOLUME_V2_RUNTIME_VALIDATE_COMMAND in volume_job
        and volume_job.index(VOLUME_V2_RUNTIME_BUILD_COMMAND)
        > volume_job.index(VOLUME_V2_RUNTIME_VALIDATE_COMMAND)
    ):
        errors.append("daily model PR Volume V2 runtime validator must follow its builder")
    required_prefix_commands = (
        "python scripts/validate_volume_breakout_watch.py --latest-only",
        "python scripts/validate_volume_attack_theme_layer.py",
        'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA" $LINEAGE_HISTORY_MODE',
    )
    for command in required_prefix_commands:
        if volume_job.count(command) != 1:
            errors.append(
                "daily model PR Volume V2 prerequisite command must appear exactly once "
                f"in its job: command={command!r} count={volume_job.count(command)}"
            )
        elif (
            VOLUME_V2_RUNTIME_BUILD_COMMAND in volume_job
            and volume_job.index(command) > volume_job.index(VOLUME_V2_RUNTIME_BUILD_COMMAND)
        ):
            errors.append(
                "daily model PR Volume V2 prerequisite must precede runtime build: "
                f"command={command!r}"
            )

    for forbidden in (
        "          python scripts/build_volume_v2_warrant_lineage_history_audit.py\n",
        "          python scripts/validate_volume_v2_warrant_lineage_history_audit.py\n",
        "--phase default",
        "--phase full",
        f"{VOLUME_V2_RUNTIME_BUILD_COMMAND} ||",
        f"{VOLUME_V2_RUNTIME_VALIDATE_COMMAND} ||",
        f"{VOLUME_V2_RUNTIME_BUILD_COMMAND}; true",
        f"{VOLUME_V2_RUNTIME_VALIDATE_COMMAND}; true",
    ):
        if forbidden in text:
            errors.append(
                "daily model PR Volume V2 contract forbids default/full or masked execution: "
                f"found={forbidden!r}"
            )

    diff_gate_lines = ["git --no-replace-objects diff --exit-code -- \\"]
    for index, path in enumerate(VOLUME_V2_RUNTIME_ARTIFACT_PATHS):
        suffix = " \\" if index < len(VOLUME_V2_RUNTIME_ARTIFACT_PATHS) - 1 else ""
        diff_gate_lines.append(f"  {path}{suffix}")
    diff_gate = "\n".join(diff_gate_lines)
    normalized_volume_job = "\n".join(
        line[10:] if line.startswith("          ") else line
        for line in volume_job.splitlines()
    )
    if normalized_volume_job.count(diff_gate) != 1:
        errors.append(
            "daily model PR Volume V2 runtime job must keep one exact4 artifact "
            f"diff gate: count={normalized_volume_job.count(diff_gate)}"
        )
    elif (
        VOLUME_V2_RUNTIME_VALIDATE_COMMAND in normalized_volume_job
        and normalized_volume_job.index(diff_gate)
        < normalized_volume_job.index(VOLUME_V2_RUNTIME_VALIDATE_COMMAND)
    ):
        errors.append("daily model PR Volume V2 exact4 diff gate must follow runtime validation")
    for path in VOLUME_V2_RUNTIME_ARTIFACT_PATHS:
        if volume_job.count(path) != 1:
            errors.append(
                "daily model PR Volume V2 exact4 diff path must appear exactly once "
                f"in its job: path={path!r} count={volume_job.count(path)}"
            )
    return errors


def validate_pdf_replay_automatic_paths(text: str) -> list[str]:
    observed_paths = workflow_pull_request_paths(text)
    errors: list[str] = []
    if observed_paths != DAILY_PDF_REPLAY_AUTOMATIC_PATHS:
        missing = sorted(DAILY_PDF_REPLAY_AUTOMATIC_PATHS - observed_paths)
        unexpected = sorted(observed_paths - DAILY_PDF_REPLAY_AUTOMATIC_PATHS)
        errors.append(
            "PDF replay automatic paths must be renderer/font-contract only: "
            f"missing={missing} unexpected={unexpected}"
        )
    forbidden_model_outputs = sorted(
        observed_paths & MODEL_OUTPUT_PATHS_FORBIDDEN_FROM_DFKAI_REPLAY
    )
    if forbidden_model_outputs:
        errors.append(
            "model-produced operation artifacts must stay on no-font model validation and must not "
            f"trigger DFKai replay: {forbidden_model_outputs}"
        )
    return errors


def validate_dfkai_pdf_replay_job(
    text: str,
    *,
    workflow_label: str,
    needs_job: str,
    output_dir: str,
    upload_step: str,
) -> list[str]:
    errors: list[str] = []
    block = workflow_job_block(text, "daily-pdf-dfkai-replay")
    if not block:
        return [f"{workflow_label} missing daily-pdf-dfkai-replay job"]

    required = {
        f"needs: {needs_job}": "DFKai PDF replay must wait for its upstream validation/production job",
        "runs-on: windows-2025": "DFKai PDF replay must use the pinned Windows 2025 runner",
        "$PSNativeCommandUseErrorActionPreference = $false": (
            "DFKai PDF replay must preserve native DISM exit codes for final-state validation"
        ),
        "Language.Fonts.Hant~~~und-HANT~0.0.1.0": "DFKai PDF replay must install the Traditional Chinese supplemental font capability",
        "DoNotConnectToWindowsUpdateInternetLocations": "DFKai PDF replay must undo the hosted runner policy that blocks Microsoft font capability downloads",
        "DisableWindowsUpdateAccess": "DFKai PDF replay must enable access to the official Windows Update capability source",
        "UseWUServer": "DFKai PDF replay must bypass unavailable hosted-runner WSUS for the official capability source",
        "Set-Service -Name wuauserv -StartupType Manual": "DFKai PDF replay must re-enable the hosted runner Windows Update service",
        "Start-Service -Name wuauserv": "DFKai PDF replay must start Windows Update before capability installation",
        "dism.exe": "DFKai PDF replay must install the official font capability with bounded DISM execution",
        "/Add-Capability": "DFKai PDF replay must install the official Hant font capability",
        "$dismExitCode = 0": "DFKai PDF replay must initialize a final-state installation result",
        "$dismExitCode = $LASTEXITCODE": "DFKai PDF replay must preserve the DISM result for audit",
        "font_capability_install_exit_code=$dismExitCode": "DFKai PDF replay must log the DISM result",
        "C:\\Windows\\Fonts\\kaiu.ttf": "DFKai PDF replay must require the canonical kaiu.ttf path",
        'throw "Required DFKai-SB font file is missing after capability install: $fontPath (DISM exit code $dismExitCode)"': (
            "DFKai PDF replay must fail closed when the canonical font file remains missing"
        ),
        "Prepare Windows long-path PDF replay runtime": "DFKai PDF replay must prepare Windows for the repository's long artifact paths",
        "git config --global core.longpaths true": "DFKai PDF replay must enable Git long-path worktree checkout",
        "C:\\tdcc-pdf-temp": "DFKai PDF replay must use a short temporary root for clean replay worktrees",
        '"TEMP=$shortTemp"': "DFKai PDF replay must route Python temporary worktrees to the short root",
        '"TMP=$shortTemp"': "DFKai PDF replay must route Windows temporary files to the short root",
        "CHATGPT_DAILY_DFKAI_FONT_PATH": "DFKai PDF replay must expose the validated font path to the renderer",
        "from fontTools.ttLib import TTFont": "DFKai PDF replay must inspect the font name table and cmap",
        "DFKai-SB": "DFKai PDF replay must validate the DFKai-SB font identity",
        "DFKaiShu-SB-Estd-BF": "DFKai PDF replay must accept the canonical extracted DFKaiShu font identity",
        "assert names & accepted": "DFKai PDF replay must fail closed on an unexpected font identity",
        "\\u6a19\\u6977\\u9ad4": "DFKai PDF replay must validate a Traditional Chinese glyph canary",
        "assert not missing": "DFKai PDF replay must fail closed when canary glyphs are missing",
        "$fontValidationExitCode = $LASTEXITCODE": "DFKai PDF replay must preserve final font validation status",
        "if ($fontValidationExitCode -ne 0)": "DFKai PDF replay must fail closed when final font validation fails",
        'throw "DFKai-SB final font validation failed with exit code $fontValidationExitCode (DISM exit code $dismExitCode)"': (
            "DFKai PDF replay must throw when final font identity or glyph validation fails"
        ),
        "passed final file, identity, and glyph validation": (
            "DFKai PDF replay may recover a nonzero DISM result only after final font validation"
        ),
        "- name: Replay ChatGPT-side daily PDF new conversation": "DFKai Windows job must own the actual six-PDF replay",
        "shell: bash": "DFKai Windows job must use Git Bash for the bounded replay command",
        "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py": "DFKai Windows job must hard-timeout the replay command",
        f"--output-dir {output_dir}": "DFKai Windows job must write the stable replay evidence folder",
        f"--require-output-dir {output_dir}": "DFKai Windows job must run the generated-output completion gate",
        f"- name: {upload_step}": "DFKai Windows job must upload the replay evidence",
        f"{output_dir}/*.pdf": "DFKai Windows job must upload all six PDF files",
        "if-no-files-found: error": "DFKai Windows job must fail when replay evidence is absent",
    }
    for literal, message in required.items():
        if literal not in block:
            errors.append(f"{workflow_label}: {message}: missing {literal!r}")

    ordered_final_state_literals = (
        'dism.exe" /Online /Add-Capability',
        "$dismExitCode = $LASTEXITCODE",
        "if (-not (Test-Path -LiteralPath $fontPath))",
        "python -c 'from fontTools.ttLib import TTFont",
        "$fontValidationExitCode = $LASTEXITCODE",
        "if ($fontValidationExitCode -ne 0)",
        "if ($dismExitCode -ne 0)",
        "passed final file, identity, and glyph validation",
    )
    cursor = -1
    for literal in ordered_final_state_literals:
        cursor = block.find(literal, cursor + 1)
        if cursor < 0:
            errors.append(
                f"{workflow_label}: DFKai final-state validation order is incomplete at {literal!r}"
            )
            break

    immediate_exit_failure = (
        'throw "DFKai-SB capability installation failed with DISM exit code $LASTEXITCODE"'
    )
    if immediate_exit_failure in block:
        errors.append(
            f"{workflow_label}: DFKai replay must validate the final font state before rejecting a DISM exit code"
        )
    return errors


def validate_pr_pdf_replay_source_pin(text: str) -> list[str]:
    errors: list[str] = []
    block = workflow_job_block(text, "daily-pdf-dfkai-replay")
    if not block:
        return ["PDF replay PR workflow missing daily-pdf-dfkai-replay job"]

    required = {
        "PDF_REPLAY_SOURCE_SHA: ${{ github.event.pull_request.head.sha || github.sha }}": (
            "PR PDF replay must select the immutable PR head SHA and fall back to the dispatch SHA"
        ),
        'checkout_sha="$(git rev-parse HEAD)"': (
            "PR PDF replay must resolve the GitHub checkout commit independently"
        ),
        'if [ "$checkout_sha" != "$GITHUB_SHA" ]; then': (
            "PR PDF replay must fail when checkout HEAD differs from the workflow checkout SHA"
        ),
        'source_sha="$PDF_REPLAY_SOURCE_SHA"': (
            "PR PDF replay must use the event-selected immutable source SHA"
        ),
        'git fetch --no-tags --depth=1 origin "$source_sha"': (
            "PR PDF replay must fetch only the exact immutable source SHA"
        ),
        'fetched_source_sha="$(git rev-parse FETCH_HEAD)"': (
            "PR PDF replay must resolve the exact fetched commit"
        ),
        'if [ "$fetched_source_sha" != "$source_sha" ]; then': (
            "PR PDF replay must fail closed if the exact SHA fetch drifts"
        ),
        'pinned_remote="pinned-replay"': (
            "PR PDF replay must use an isolated runner-local pinned remote"
        ),
        'pinned_branch="workflow-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}"': (
            "PR PDF replay must namespace the pinned ref by immutable workflow run identity"
        ),
        'git branch --force "$pinned_branch" "$source_sha"': (
            "PR PDF replay must bind the runner-local branch to the workflow SHA"
        ),
        'git remote add "$pinned_remote" "$PWD"': (
            "PR PDF replay must expose only the runner-local pinned branch to the source resolver"
        ),
        'git fetch "$pinned_remote" "$pinned_branch"': (
            "PR PDF replay must materialize the pinned remote-tracking ref"
        ),
        'source_ref="$pinned_remote/$pinned_branch"': (
            "PR PDF replay must pass the pinned remote-tracking ref to the official entrypoint"
        ),
        'resolved_source_sha="$(git rev-parse "$source_ref")"': (
            "PR PDF replay must resolve the pinned ref before rendering"
        ),
        'if [ "$resolved_source_sha" != "$source_sha" ]; then': (
            "PR PDF replay must fail closed if the pinned ref drifts"
        ),
        "PDF replay workflow_checkout_sha=$GITHUB_SHA": (
            "PR PDF replay must log the immutable workflow checkout SHA"
        ),
        "PDF replay source_sha=$source_sha": (
            "PR PDF replay must log the resolved source SHA"
        ),
    }
    for literal, message in required.items():
        if literal not in block:
            errors.append(f"{message}: missing {literal!r}")

    forbidden = {
        "GITHUB_HEAD_REF": "PR PDF replay must not resolve a moving pull-request branch ref",
        "GITHUB_REF_NAME": "PR PDF replay must not resolve a moving workflow branch ref",
        'source_ref="origin/': "PR PDF replay must not pass a moving origin ref to the official entrypoint",
        "${source_ref#origin/}": "PR PDF replay must not derive a branch fetch from a moving origin ref",
    }
    for literal, message in forbidden.items():
        if literal in block:
            errors.append(f"{message}: found {literal!r}")
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


HISTORICAL_REPLAY_FRESHNESS_STAGE_STEP = "Stage exact structured-source artifact families"
HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND = (
    "git add output/latest/data_freshness_latest.csv "
    "output/latest/data_freshness_latest.md"
)


def _workflow_step_executable_lines(step_block: str) -> list[str]:
    lines: list[str] = []
    run_indent: int | None = None
    for raw_line in step_block.splitlines():
        stripped = raw_line.strip()
        indent = len(raw_line) - len(raw_line.lstrip())
        if run_indent is None:
            if stripped in {"run: |", "run: |-", "run: |+"}:
                run_indent = indent
            continue
        if stripped and indent <= run_indent:
            break
        if stripped and not stripped.startswith("#"):
            lines.append(stripped)
    return lines


def _validate_historical_replay_freshness_stage(text: str) -> list[str]:
    errors: list[str] = []
    job_block = workflow_job_block(text, "replay-historical-structured-sources")
    if not job_block:
        return ["historical replay workflow is missing replay-historical-structured-sources job"]

    step_marker = f"- name: {HISTORICAL_REPLAY_FRESHNESS_STAGE_STEP}"
    if sum(line.strip() == step_marker for line in job_block.splitlines()) != 1:
        return [
            "historical replay workflow must define exactly one exact artifact-family staging step"
        ]

    step_block = workflow_step_block(job_block, HISTORICAL_REPLAY_FRESHNESS_STAGE_STEP)
    executable_lines = _workflow_step_executable_lines(step_block)
    if sum(
        line == HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND
        for line in executable_lines
    ) != 1:
        errors.append(
            "historical replay freshness markers require one direct exact staging command"
        )
    if text.count(HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND) != 1:
        errors.append(
            "historical replay freshness staging command must occur exactly once in the workflow"
        )

    protected_names = (
        "data_freshness_latest.csv",
        "data_freshness_latest.md",
        "market_session_status_latest.json",
        "daily_authority_release_latest.json",
    )
    for line in executable_lines:
        if any(name in line for name in protected_names) and (
            line != HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND
        ):
            errors.append(
                "historical replay exact artifact-family step contains a non-exact "
                f"authority-surface command: {line}"
            )

    if HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND in executable_lines:
        stage_index = executable_lines.index(HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND)
        validator_indexes = [
            index
            for index, line in enumerate(executable_lines)
            if line.startswith(
                "python scripts/validate_historical_source_replay_staged_paths.py"
            )
        ]
        if not validator_indexes or stage_index >= validator_indexes[0]:
            errors.append(
                "historical replay freshness markers must be staged before staged-path validation"
            )
    return errors


def validate_historical_source_replay_workflow(text: str) -> list[str]:
    errors: list[str] = []
    errors.extend(_validate_historical_replay_freshness_stage(text))
    required_literals = {
        "workflow_dispatch:": "must be manually and explicitly dispatched",
        "expected_main_sha:": "must require an immutable authorized main SHA",
        "github.ref != 'refs/heads/main'": "must reject non-main dispatches",
        "ref: ${{ inputs.expected_main_sha }}": "must checkout the pinned expected SHA",
        "group: historical-structured-source-replay-${{ github.ref }}": "must use an independent replay concurrency group",
        "cancel-in-progress: false": "must not cancel an in-flight official producer",
        "Require production artifact write deploy key": "must fail closed on missing writer credentials",
        "Checkout exact main source": "must checkout only after credential preflight",
        "Install replay dependencies": "must install runtime dependencies before replay",
        '"$base_sha" != "$EXPECTED_MAIN_SHA"': "must bind checkout to expected_main_sha",
        'git merge-base --is-ancestor "$base_sha" "$remote_main_sha"': "must require the pinned base to remain a current-main ancestor",
        "python scripts/replay_historical_structured_sources.py": "must use the canonical replay orchestrator",
        "--repair-market-index-base-date \"$BASE_REPAIR_DATE\"": "must explicitly route the TPEX base repair",
        "--replay-id \"$HISTORICAL_SOURCE_REPLAY_ID\"": "must use the immutable run namespace",
        "--expected-pipeline-sha \"$REPLAY_BASE_SHA\"": "must validate against the code-base SHA",
        "python scripts/validate_historical_source_replay_staged_paths.py": "must fail closed on staged/worktree paths",
        "git add data/daily_price/": "must explicitly stage dated price sources",
        "git add data/stock_price_history/": "must explicitly stage stock histories",
        "git add data/market_index_history.csv data/market_index_ohlc_history.csv": "must explicitly stage market-index histories",
        "git add data/futures_options/": "must explicitly stage TAIFEX histories",
        "git add output/history/warrant_daily/": "must explicitly stage warrant history",
        "git add output/history/warrant_flow/": "must explicitly stage warrant-flow history",
        "REMOTE_MAIN_SHA_PRECOMMIT": "must record the precommit remote SHA",
        "REMOTE_MAIN_SHA_AFTER": "must verify the post-push remote SHA",
        "commit_count_after - commit_count_before": "must prove exactly one output commit",
        'git diff --cached --name-only --no-renames -z > "$staged_paths_file"': "must capture both sides of staged renames",
        '"git", "diff", "--name-only", "--no-renames", "-z"': "must compare moving-main paths without rename ambiguity",
        "moving main overlaps staged historical replay paths": "must fail closed on a publication-path overlap",
        "for push_attempt in 1 2 3": "must bound normal publication attempts",
        "for fetch_attempt in 1 2 3": "must bound fetch convergence independently",
        'candidate_published_head_sha="$(git rev-parse HEAD)"': "must freeze the exact candidate before normal push",
        'git merge --no-edit "$remote_main_sha"': "must integrate non-overlapping main drift with an ordinary merge",
        "git push origin HEAD:refs/heads/main": "must use one fail-closed non-force push",
        'echo "domain_output_commit_sha=$output_commit_sha"': "must expose the unique domain output commit",
        'echo "published_head_sha=$published_head_sha"': "must expose the exact published head separately",
        "Revalidate pushed replay against immutable code base": "must validate again after the output commit is pushed",
    }
    for literal, purpose in required_literals.items():
        if literal not in text:
            errors.append(f"historical structured-source replay {purpose}: missing {literal!r}")

    if text.count("python scripts/validate_historical_structured_source_replay.py") != 2:
        errors.append(
            "historical structured-source replay must run the final validator exactly before commit and after push"
        )
    if len(re.findall(r"(?m)^\s*git commit\s", text)) != 1:
        errors.append("historical structured-source replay must create exactly one Git commit")
    if len(re.findall(r"(?m)^\s*(?:if\s+)?git push\s", text)) != 1:
        errors.append("historical structured-source replay must execute exactly one Git push")
    if text.count("for push_attempt in 1 2 3; do") != 1:
        errors.append("historical structured-source replay must have one bounded push loop")
    if text.count("for fetch_attempt in 1 2 3; do") != 1:
        errors.append("historical structured-source replay must have one bounded fetch loop")
    if text.count('"git", "diff", "--name-only", "--no-renames", "-z"') != 2:
        errors.append("historical structured-source replay must make both overlap checks rename-safe")
    if text.count("git diff --cached --name-only --no-renames -z") != 1:
        errors.append("historical structured-source replay must make its staged path set rename-safe")

    forbidden_literals = {
        "git add -A": "must not broad-stage the repository",
        "ci_push_with_retry.sh": "must not rebase or regenerate on a moving main",
        "git rebase": "must not rebase after replay validation",
        "git reset": "must not reset validated replay output",
        "git push --force": "must not force-push production artifacts",
        "Validate repository automation boundaries": "must not run repo-static governance in production replay",
        "generate_chatgpt_side_daily_reports.py": "must not reconstruct historical PDFs",
        "build_daily_candidate_model_layer.py": "must not reconstruct historical model outputs",
        "build_theme_event_watch.py": "must not reconstruct historical event/catalyst outputs",
        "git add output/latest/all_candidates": "must not stage candidate outputs",
        "git add output/history/daily_model": "must not stage model outputs",
        "git add published_reports": "must not stage published reports",
        "git add chatgpt_side_outputs": "must not stage PDF outputs",
    }
    for literal, purpose in forbidden_literals.items():
        if literal in text:
            errors.append(f"historical structured-source replay {purpose}: found {literal!r}")

    ordered_literals = (
        "Require production artifact write deploy key",
        "Checkout exact main source",
        "Install replay dependencies",
        "python scripts/replay_historical_structured_sources.py",
        "python scripts/validate_historical_structured_source_replay.py",
        "git add data/daily_price/",
        "python scripts/validate_historical_source_replay_staged_paths.py",
        "Validate moving-main path isolation before the domain output commit",
        "git commit -m",
        "git push origin HEAD:refs/heads/main",
        "Verify pushed main and output commit",
        "python scripts/validate_historical_structured_source_replay.py",
    )
    cursor = -1
    for literal in ordered_literals:
        position = text.find(literal, cursor + 1)
        if position < 0:
            errors.append(
                "historical structured-source replay fail-closed order is incomplete or invalid: "
                f"expected {literal!r} after position {cursor}"
            )
            break
        cursor = position
    return errors


AUTHORITY_SURFACE_PATHS = {
    "output/latest/market_session_status_latest.json",
    "output/latest/data_freshness_latest.csv",
    "output/latest/data_freshness_latest.md",
    "output/latest/daily_authority_release_latest.json",
}


def _git_subcommand_tokens(command: str, expected: str) -> list[str] | None:
    try:
        tokens = shlex.split(command, posix=True)
    except ValueError:
        return [] if re.search(r"\bgit\b.*\b" + re.escape(expected) + r"\b", command) else None
    while tokens:
        if tokens[0] == "command":
            tokens = tokens[1:]
            continue
        if tokens[0] == "env":
            tokens = tokens[1:]
            while tokens and (tokens[0].startswith("-") or "=" in tokens[0]):
                tokens = tokens[1:]
            continue
        executable = tokens[0].replace("\\", "/").rsplit("/", 1)[-1]
        if executable in {"bash", "sh"}:
            for option_index, option in enumerate(tokens[1:], start=1):
                if option.startswith("-") and "c" in option[1:]:
                    command_index = option_index + 1
                    if command_index >= len(tokens):
                        return []
                    return _git_subcommand_tokens(tokens[command_index], expected)
        break
    if not tokens or tokens[0].replace("\\", "/").rsplit("/", 1)[-1] not in {"git", "git.exe"}:
        return None
    cursor = 1
    while cursor < len(tokens) and tokens[cursor] != expected:
        token = tokens[cursor]
        if token in {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--config-env"} and cursor + 1 < len(tokens):
            cursor += 2
            continue
        if token.startswith(("-C", "-c", "--git-dir=", "--work-tree=", "--namespace=", "--config-env=")) or token in {"--no-pager", "--literal-pathspecs", "--no-replace-objects"}:
            cursor += 1
            continue
        if token.startswith("-") and expected in tokens[cursor + 1 :]:
            return []
        return None
    if cursor >= len(tokens):
        return None
    return tokens[cursor + 1 :]


def _contains_git_subcommand(command: str, expected: str) -> bool:
    pattern = re.compile(
        r"(?<![A-Za-z0-9_-])(?:[^\s'\";|&()]+[\\/])?git(?:\.exe)?\s+"
        r"(?:(?:(?:-C|-c|--git-dir|--work-tree|--namespace|--config-env)\s+\S+|"
        r"(?:--git-dir|--work-tree|--namespace|--config-env)=\S+|--no-pager|--literal-pathspecs|--no-replace-objects)\s+)*"
        + re.escape(expected)
        + r"(?=\s|$|[;|&])"
    )
    return pattern.search(command) is not None


def git_add_command_covers_authority(command: str) -> bool:
    add_tokens = _git_subcommand_tokens(command, "add")
    if add_tokens is None and not _contains_git_subcommand(command, "add"):
        add_tokens = _git_subcommand_tokens(command, "stage")
        if add_tokens is None:
            return _contains_git_subcommand(command, "stage")
    elif add_tokens is None:
        return True
    if not add_tokens:
        return True
    path_tokens: list[str] = []
    for token in add_tokens:
        if token in {"||", "true"}:
            break
        if token in {"-A", "--all", "-u", "--update"}:
            return True
        if token.startswith("--pathspec-from-file"):
            return True
        if token == "--" or token.startswith("-"):
            continue
        path_tokens.append(token.replace("\\", "/"))
    for token in path_tokens:
        if token.startswith((":", "@")):
            return True
        if "$" in token or "`" in token:
            static_prefix = re.split(r"[$`]", token, maxsplit=1)[0].rstrip("/")
            normalized_prefix = posixpath.normpath(static_prefix.removeprefix("./"))
            if normalized_prefix in {".", "output", "output/latest"} or any(
                path.startswith(normalized_prefix + "/") for path in AUTHORITY_SURFACE_PATHS
            ):
                return True
            continue
        normalized = posixpath.normpath(token.removeprefix("./"))
        if normalized in {".", "output", "output/latest"}:
            return True
        if normalized in AUTHORITY_SURFACE_PATHS:
            return True
        if any(fnmatch.fnmatchcase(path, normalized) for path in AUTHORITY_SURFACE_PATHS):
            return True
    return False


def _path_tokens_cover_authority(path_tokens: list[str]) -> bool:
    synthetic = "git add -- " + " ".join(shlex.quote(token) for token in path_tokens)
    return git_add_command_covers_authority(synthetic)


def git_commit_command_covers_authority(command: str) -> bool:
    commit_tokens = _git_subcommand_tokens(command, "commit")
    if commit_tokens is None:
        return _contains_git_subcommand(command, "commit")
    path_tokens: list[str] = []
    skip_value = False
    value_options = {"-m", "--message", "-F", "--file", "-C", "-c", "--reuse-message", "--fixup", "--squash"}
    for token in commit_tokens:
        if skip_value:
            skip_value = False
            continue
        if token in {"-a", "--all"} or (
            token.startswith("-") and not token.startswith("--") and "a" in token[1:]
        ):
            return True
        if token.startswith("--pathspec-from-file"):
            return True
        if token in value_options:
            skip_value = True
            continue
        if token == "--" or token == "--only" or token.startswith("-"):
            continue
        path_tokens.append(token)
    return bool(path_tokens) and _path_tokens_cover_authority(path_tokens)


def git_update_index_command_may_stage(command: str) -> bool:
    update_tokens = _git_subcommand_tokens(command, "update-index")
    return update_tokens is not None or _contains_git_subcommand(command, "update-index")


def git_native_mutation_may_publish_authority(command: str) -> bool:
    unconditional = {
        "read-tree",
        "reset",
        "checkout",
        "switch",
        "merge",
        "rebase",
        "cherry-pick",
        "revert",
        "am",
        "commit-tree",
        "mktree",
        "update-ref",
    }
    for subcommand in unconditional:
        tokens = _git_subcommand_tokens(command, subcommand)
        if tokens is not None or _contains_git_subcommand(command, subcommand):
            return True

    apply_tokens = _git_subcommand_tokens(command, "apply")
    if apply_tokens is None:
        if _contains_git_subcommand(command, "apply"):
            return True
    elif any(token in {"--cached", "--index", "-3", "--3way"} for token in apply_tokens):
        return True

    restore_tokens = _git_subcommand_tokens(command, "restore")
    if restore_tokens is None:
        if _contains_git_subcommand(command, "restore"):
            return True
    elif any(
        token == "--staged"
        or (token.startswith("-") and not token.startswith("--") and "S" in token[1:])
        or token.startswith("--source")
        for token in restore_tokens
    ):
        return True

    stash_tokens = _git_subcommand_tokens(command, "stash")
    if stash_tokens is None:
        if _contains_git_subcommand(command, "stash"):
            return True
    elif any(token == "--index" for token in stash_tokens):
        return True

    for subcommand in ("rm", "mv"):
        tokens = _git_subcommand_tokens(command, subcommand)
        if tokens is None:
            if _contains_git_subcommand(command, subcommand):
                return True
            continue
        path_tokens = [
            token.replace("\\", "/")
            for token in tokens
            if token != "--" and not token.startswith("-")
        ]
        if not path_tokens or _path_tokens_cover_authority(path_tokens):
            return True
    return False


def workflow_paths(workflow_root: Path) -> list[Path]:
    return sorted({*workflow_root.glob("*.yml"), *workflow_root.glob("*.yaml")})


def validate_authority_workflow_publishers() -> list[str]:
    errors: list[str] = []
    workflow_root = ROOT / ".github" / "workflows"
    allowed_staging_helpers = {"python scripts/stage_daily_published_snapshot_revisions.py"}
    for path in workflow_paths(workflow_root):
        if path == DAILY_WORKFLOW:
            continue
        text = read_text(path)
        if "scripts/daily_authority_release.py publish" in text:
            errors.append(f"only daily_full_pipeline may publish daily authority: {path.name}")
        normalized = re.sub(r"\\\r?\n\s*", " ", text)
        for raw_line in normalized.splitlines():
            command = raw_line.strip()
            if (
                path == HISTORICAL_SOURCE_REPLAY_WORKFLOW
                and command == HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND
            ):
                continue
            if git_add_command_covers_authority(command):
                errors.append(
                    f"non-authority workflow may stage a daily authority surface: {path.name}: {command}"
                )
            if git_commit_command_covers_authority(command):
                errors.append(f"non-authority workflow commit may publish daily authority: {path.name}: {command}")
            if git_update_index_command_may_stage(command):
                errors.append(f"non-authority workflow may stage via update-index: {path.name}: {command}")
            allowed_ordinary_merge = (
                path in {RECENT_PRICE_GAP_WORKFLOW, HISTORICAL_SOURCE_REPLAY_WORKFLOW}
                and command == 'git merge --no-edit "$remote_main_sha"'
            )
            if git_native_mutation_may_publish_authority(command) and not allowed_ordinary_merge:
                errors.append(f"non-authority workflow uses unsafe native Git mutation: {path.name}: {command}")
        for helper in re.findall(r"python\s+scripts/stage_[A-Za-z0-9_./-]+\.py", normalized):
            if helper not in allowed_staging_helpers:
                errors.append(f"non-authority workflow uses an unregistered staging helper: {path.name}: {helper}")
    return errors


def yaml_if_conditions(workflow_text: str) -> list[str]:
    conditions: list[str] = []
    lines = workflow_text.splitlines()
    for index, raw_line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>[ \t]*)if\s*:\s*(?P<value>.*)$",
            raw_line,
            flags=re.IGNORECASE,
        )
        if match is None:
            continue
        value = match.group("value").strip()
        if value == "" or re.fullmatch(r"[>|][+-]?(?:\s+#.*)?", value):
            base_indent = len(match.group("indent").expandtabs(2))
            continuation: list[str] = []
            for candidate in lines[index + 1 :]:
                if not candidate.strip():
                    continue
                candidate_indent = len(candidate) - len(candidate.lstrip(" \t"))
                if candidate_indent <= base_indent:
                    break
                continuation.append(candidate.strip())
            value = " ".join(continuation)
        conditions.append(value)
    return conditions


def validate_recent_price_gap_workflow_contract(repair_text: str) -> list[str]:
    errors: list[str] = []
    repair_literals = {
        "Reject non-main production dispatch": (
            "recent price-gap workflow must reject branch dispatch"
        ),
        "ref: ${{ github.sha }}": "recent price-gap workflow must checkout its pinned event SHA",
        'git merge-base --is-ancestor "$checkout_sha" "$remote_main_sha"': (
            "recent price-gap pinned event SHA must remain a current-main ancestor"
        ),
        "moving main overlaps staged repair source-bundle paths": (
            "recent price-gap publication must reject staged-path overlap"
        ),
        "for push_attempt in 1 2 3": (
            "recent price-gap publication must use bounded normal push attempts"
        ),
        "for fetch_attempt in 1 2 3": (
            "recent price-gap publication must use independent bounded fetch convergence"
        ),
        '"git", "diff", "--name-only", "--no-renames", "-z"': (
            "recent price-gap overlap checks must expose both sides of renames"
        ),
        'git diff --cached --name-only --no-renames -z': (
            "recent price-gap staged sets must expose both sides of renames"
        ),
        'if [ "$head_before_commit" != "$REPAIR_BASE_SHA" ]; then': (
            "recent price-gap domain commit must start at the pinned repair base"
        ),
        'source_bundle_commit_count="$(git rev-list --count "$REPAIR_BASE_SHA..$source_bundle_commit_sha")"': (
            "recent price-gap workflow must create one exact domain commit"
        ),
        'git merge --no-edit "$remote_main_sha"': (
            "recent price-gap publication must ordinary-merge non-overlapping main"
        ),
        "Build immutable current-day source recovery bundle": (
            "recent price-gap workflow must build an immutable current-day source bundle"
        ),
        "resume-daily-full-from-source-bundle:": (
            "recent price-gap workflow must resume Daily Full only from the immutable bundle"
        ),
    }
    for literal, message in repair_literals.items():
        if literal not in repair_text:
            errors.append(f"{message}: missing {literal!r}")
    if repair_text.count("for push_attempt in 1 2 3; do") != 2:
        errors.append("recent price-gap workflow must have exactly two bounded publish loops")
    if repair_text.count("for fetch_attempt in 1 2 3; do") != 2:
        errors.append("recent price-gap workflow must have exactly two bounded fetch loops")
    if repair_text.count('"git", "diff", "--name-only", "--no-renames", "-z"') != 2:
        errors.append("recent price-gap workflow must make both overlap checks rename-safe")
    if repair_text.count("git diff --cached --name-only --no-renames -z") != 2:
        errors.append("recent price-gap workflow must make both staged path sets rename-safe")

    zero_repair_guards = [
        condition
        for condition in yaml_if_conditions(repair_text)
        if "REPAIR_ACTION_COUNT" in condition
    ]
    for zero_repair_guard in zero_repair_guards:
        errors.append(
            "recent price-gap workflow must persist the immutable current-day source bundle "
            "even when repair action count is zero: "
            f"found {zero_repair_guard!r}"
        )

    for forbidden in (
        "MARKET_SESSION_CHANGE_COUNT",
        "git add output/latest/market_session_status_latest.json",
        "git add data/market_calendar/exceptional_non_trading_days.csv",
        "Validate workflow automation boundaries",
    ):
        if forbidden in repair_text:
            errors.append(
                "recent price-gap workflow must not independently publish market authority: "
                f"found {forbidden!r}"
            )
    return errors


def validate_daily_authority_snapshot_publish_contract(daily_text: str) -> list[str]:
    errors: list[str] = []
    fetch_block = workflow_step_block(daily_text, "Fetch market abnormal status")
    exact_fetch = (
        'python scripts/fetch_market_abnormal_status.py --target-date '
        '"$EXPECTED_MAIN_PRICE_DATE"'
    )
    if fetch_block.count(exact_fetch) != 1:
        errors.append(
            "daily market-abnormal fetch must receive the exact expected main price date"
        )
    if f"{exact_fetch} || true" in fetch_block:
        errors.append("daily market-abnormal fetch must fail closed")
    if re.search(r'(?m)^ {8}(?:if|["\']if["\'])\s*:', fetch_block):
        errors.append("daily market-abnormal fetch step must be unconditional")
    continue_values = [
        match.group(1).split("#", 1)[0].strip()
        for line in fetch_block.splitlines()
        if (
            match := re.fullmatch(
                r' {8}(?:continue-on-error|["\']continue-on-error["\'])\s*:\s*(.*)',
                line,
            )
        )
    ]
    if continue_values and continue_values != ["false"]:
        errors.append(
            "daily market-abnormal fetch step continue-on-error must be absent or explicit false"
        )
    ordered_literals = (
        "Prepare daily authority release before immutable snapshot finalization",
        "python scripts/daily_authority_release.py publish",
        "Publish final immutable freshness snapshot revision",
        "python scripts/update_daily_published_model_snapshots.py --artifact-id data_freshness --revision-reason daily_authority_release_final",
        "Stage immutable published snapshot revisions",
        "Validate immutable published snapshot revisions",
        "Commit report artifacts, packets, and rules first",
    )
    cursor = -1
    for literal in ordered_literals:
        position = daily_text.find(literal, cursor + 1)
        if position < 0:
            errors.append(
                "daily authority publish/final snapshot order is incomplete: "
                f"missing {literal!r} after position {cursor}"
            )
            break
        cursor = position

    pinned_checkout_gate = 'if [ "$CURRENT_HEAD" != "$PREFLIGHT_SOURCE_SHA" ]; then'
    if daily_text.count(pinned_checkout_gate) != 2:
        errors.append(
            "closed-market and production checkouts must each remain pinned to PREFLIGHT_SOURCE_SHA"
        )
    if '"$REMOTE_MAIN" != "$PREFLIGHT_SOURCE_SHA"' in daily_text:
        errors.append(
            "daily workflow must not require origin/main to remain globally equal to PREFLIGHT_SOURCE_SHA"
        )
    publish_block = workflow_step_block(
        daily_text,
        "Commit report artifacts, packets, and rules first",
    )
    if not publish_block:
        errors.append("daily workflow is missing the authority artifact publication commit step")
        return errors
    required_publish_literals = {
        "git add data/daily_price/ data/stock_price_history/": (
            "daily publish must stage required price and current-day history data"
        ),
        'git add -- "data/market_abnormal_status/bundles/${EXPECTED_MAIN_PRICE_DATE}/"': (
            "daily publish must stage the exact-target market-abnormal bundle"
        ),
        "git add -- output/history/market_abnormal_status/market_abnormal_status_history.csv": (
            "daily publish must stage target-keyed market-abnormal history"
        ),
        "output/latest/market_abnormal_status_latest.csv": (
            "daily publish must stage the exact-target market-abnormal latest CSV"
        ),
        "output/latest/market_abnormal_status_latest.md": (
            "daily publish must stage the exact-target market-abnormal latest Markdown"
        ),
        "docs/latest/market_abnormal_status_latest.csv": (
            "daily publish must stage the exact-target market-abnormal docs CSV mirror"
        ),
        "docs/latest/market_abnormal_status_latest.md": (
            "daily publish must stage the exact-target market-abnormal docs Markdown mirror"
        ),
        "docs/latest/company_industry_snapshot_latest.csv": (
            "daily publish must stage the generated company-industry snapshot"
        ),
        "docs/latest/market_timing_chatgpt_packet_latest.md": (
            "daily publish must stage the generated market-timing packet"
        ),
        "docs/latest/stock_price_history_manifest.csv": (
            "daily publish must stage every stock-price-history manifest surface"
        ),
        "docs/latest/stock_price_history_manifest.json": (
            "daily publish must stage every stock-price-history manifest surface"
        ),
        "docs/latest/stock_price_history_manifest.md": (
            "daily publish must stage every stock-price-history manifest surface"
        ),
        "docs/latest/stock_theme_authorized_seed_preview_latest.csv": (
            "daily publish must stage every generated stock-theme seed preview surface"
        ),
        "docs/latest/stock_theme_authorized_seed_preview_latest.md": (
            "daily publish must stage every generated stock-theme seed preview surface"
        ),
        "docs/latest/stock_theme_manual_fill_template_latest.csv": (
            "daily publish must stage every generated stock-theme manual-fill template"
        ),
        "docs/latest/stock_theme_manual_fill_template_latest.xlsx": (
            "daily publish must stage every generated stock-theme manual-fill template"
        ),
        "docs/latest/stock_theme_taxonomy_latest.csv": (
            "daily publish must stage every generated stock-theme taxonomy surface"
        ),
        "docs/latest/stock_theme_taxonomy_latest.md": (
            "daily publish must stage every generated stock-theme taxonomy surface"
        ),
        "docs/latest/stock_theme_taxonomy_validation_latest.json": (
            "daily publish must stage every generated stock-theme validation surface"
        ),
        "docs/latest/stock_theme_taxonomy_validation_latest.md": (
            "daily publish must stage every generated stock-theme validation surface"
        ),
        "git add -- output/history/daily_candidates/daily_candidate_signal_log.csv": (
            "daily publish must stage the generated candidate signal history"
        ),
        'git diff --cached --name-only --no-renames -z > "$staged_paths_file"': (
            "daily publish must capture both sides of staged renames"
        ),
        'git diff --name-only --no-renames -z > "$unstaged_paths_file"': (
            "daily publish must capture tracked unstaged writes without rename collapsing"
        ),
        'git ls-files --others --exclude-standard -z > "$untracked_paths_file"': (
            "daily publish must capture nonignored untracked writes"
        ),
        'python - "$staged_paths_file" "$unstaged_paths_file" "$untracked_paths_file" "$write_paths_file"': (
            "daily publish must build one NUL-safe staged and worktree write-path union"
        ),
        "for source in sys.argv[1:4]": (
            "daily publish must include all three write-path sources in its union"
        ),
        'python - "$comparison_base" "$remote_head" "$write_paths_file"': (
            "daily publish must compare moving main with the full write-path union"
        ),
        '["git", "diff", "--name-only", "--no-renames", "-z", sys.argv[1], sys.argv[2], "--"]': (
            "daily publish must compare pinned-source-to-current-main paths"
        ),
        "overlap = sorted(changed & written)": (
            "daily publish must fail closed only on an actual path overlap"
        ),
        "Current main overlaps daily publish write paths": (
            "daily publish must report exact staged or worktree conflicts"
        ),
        'git merge --no-edit "$remote_head"': (
            "daily publish must ordinary-merge a non-overlapping main advance"
        ),
        "for push_attempt in 1 2 3": (
            "daily publish must bound non-force push retries"
        ),
        "fetch_artifact_main_bounded()": (
            "daily publish must isolate transient fetch failures"
        ),
        "for fetch_attempt in 1 2 3": (
            "daily publish must bound remote fetch attempts"
        ),
        "if ! fetch_artifact_main_bounded; then": (
            "daily publish must continue after a bounded transient fetch failure"
        ),
        'candidate_published_head_sha="$(git rev-parse HEAD)"': (
            "daily publish must freeze each exact push candidate"
        ),
        'if git push origin "HEAD:$TARGET_BRANCH"; then': (
            "daily publish must treat a successful normal push as its linearization point"
        ),
        'git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_head"': (
            "daily publish must recognize an accepted push after an acknowledgement failure"
        ),
        "fetch_artifact_main_bounded &&": (
            "daily publish must perform a final bounded remote verification"
        ),
    }
    for literal, message in required_publish_literals.items():
        if literal not in publish_block:
            errors.append(f"{message}: missing {literal!r}")
    exact_counts = {
        'git diff --cached --name-only --no-renames -z > "$staged_paths_file"': 1,
        'git diff --name-only --no-renames -z > "$unstaged_paths_file"': 1,
        'git ls-files --others --exclude-standard -z > "$untracked_paths_file"': 1,
        'python - "$staged_paths_file" "$unstaged_paths_file" "$untracked_paths_file" "$write_paths_file"': 1,
        'python - "$comparison_base" "$remote_head" "$write_paths_file"': 1,
        "fetch_artifact_main_bounded()": 1,
        "for push_attempt in 1 2 3; do": 1,
        'if git push origin "HEAD:$TARGET_BRANCH"; then': 1,
        "fetch_artifact_main_bounded &&": 1,
    }
    for literal, expected_count in exact_counts.items():
        actual_count = publish_block.count(literal)
        if actual_count != expected_count:
            errors.append(
                "daily artifact publish contract count mismatch: "
                f"literal={literal!r} expected={expected_count} actual={actual_count}"
            )
    if publish_block.count(
        'git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_head"'
    ) != 2:
        errors.append(
            "daily artifact publish must prove candidate ancestry both before a new push "
            "and in the final acknowledgement-loss check"
        )
    errors.extend(
        require_workflow_order(
            publish_block,
            [
                "fetch_artifact_main_bounded() {",
                "for push_attempt in 1 2 3; do",
                'if git push origin "HEAD:$TARGET_BRANCH"; then',
                '            done\n            if [ "$publish_succeeded" != true ] &&',
                "fetch_artifact_main_bounded &&",
                'if [ "$publish_succeeded" != true ]; then',
            ],
        )
    )
    forbidden_publish_literals = {
        "git rebase": "daily publish must not rebase validated artifacts",
        "git push --force": "daily publish must not force-push",
        "git push -f": "daily publish must not force-push",
        "git add data/daily_price/ data/stock_price_history/ || true": (
            "daily publish must not ignore required price-history staging failures"
        ),
        'git add -- "data/market_abnormal_status/bundles/${EXPECTED_MAIN_PRICE_DATE}/" || true': (
            "daily publish must not ignore exact-target market-abnormal bundle staging failures"
        ),
        "git add -- output/history/market_abnormal_status/market_abnormal_status_history.csv || true": (
            "daily publish must not ignore target-keyed market-abnormal history staging failures"
        ),
        "docs/latest/daily_signal_performance_": (
            "daily publish must not stage research-owned signal-performance PDFs"
        ),
        "output/debug/": "daily publish must not stage diagnostic output",
    }
    for forbidden, message in forbidden_publish_literals.items():
        if forbidden in publish_block:
            errors.append(f"{message}: found {forbidden!r}")
    if re.search(r"data/market_abnormal_status/(?:bundles/)?20\d{6}", publish_block):
        errors.append("daily publish must not hard-code a wall-date market-abnormal raw path")
    return errors


def validate_daily_readme_publish_contract(daily_text: str) -> list[str]:
    errors: list[str] = []
    block = workflow_step_block(daily_text, "Commit readme and publish check")
    if not block:
        return ["daily workflow is missing the readme publication commit step"]

    required_literals = {
        'readme_publish_base_sha="$(git rev-parse HEAD)"': (
            "readme publish must pin the actual pre-publication base"
        ),
        'git diff --cached --name-only --no-renames -z > "$staged_paths_file"': (
            "readme publish must capture its actual staged paths without rename collapsing"
        ),
        'git diff --name-only --no-renames -z > "$unstaged_paths_file"': (
            "readme publish must capture tracked unstaged writes without rename collapsing"
        ),
        'git ls-files --others --exclude-standard -z > "$untracked_paths_file"': (
            "readme publish must capture nonignored untracked writes"
        ),
        'python - "$staged_paths_file" "$unstaged_paths_file" "$untracked_paths_file" "$write_paths_file"': (
            "readme publish must build one NUL-safe staged and worktree write-path union"
        ),
        "for source in sys.argv[1:4]": (
            "readme publish must include all three write-path sources in its union"
        ),
        'python - "$comparison_base" "$remote_head" "$write_paths_file"': (
            "readme publish must compare moving main with the full write-path union"
        ),
        "docs/latest/daily_candidate_two_line_view_latest.csv": (
            "readme publish must stage every generated candidate two-line view"
        ),
        "docs/latest/daily_candidate_two_line_view_latest.md": (
            "readme publish must stage every generated candidate two-line view"
        ),
        "docs/latest/daily_theme_leadership_latest.csv": (
            "readme publish must stage every generated theme-leadership surface"
        ),
        "docs/latest/daily_theme_leadership_latest.md": (
            "readme publish must stage every generated theme-leadership surface"
        ),
        "docs/rules/rules_index_latest.md": (
            "readme publish must stage the generated rules index"
        ),
        '"docs/history/reports/${SNAPSHOT_REPORT_DATE}_READ_ME_FIRST_DAILY_REPORT.txt"': (
            "readme publish must stage its date-bound docs history mirror"
        ),
        '"output/history/reports/${SNAPSHOT_REPORT_DATE}_READ_ME_FIRST_DAILY_REPORT.txt"': (
            "readme publish must stage its date-bound output history copy"
        ),
        'git merge-base --is-ancestor "$readme_publish_base_sha" "$remote_head"': (
            "readme publish must require moving main to descend from its pinned base"
        ),
        '["git", "diff", "--name-only", "--no-renames", "-z", sys.argv[1], sys.argv[2], "--"]': (
            "readme publish must compare moving-main changes with its write paths"
        ),
        "overlap = sorted(changed & written)": (
            "readme publish must fail only on an actual publication-path overlap"
        ),
        "Current main overlaps readme publish write paths": (
            "readme publish must report the exact conflicting paths"
        ),
        'git merge --no-edit "$remote_head"': (
            "readme publish must ordinary-merge non-overlapping main changes"
        ),
        "for push_attempt in 1 2 3": (
            "readme publish must bound normal push attempts"
        ),
        "fetch_readme_main_bounded()": (
            "readme publish must isolate transient fetch failures"
        ),
        "for fetch_attempt in 1 2 3": (
            "readme publish must bound remote fetch attempts"
        ),
        "if ! fetch_readme_main_bounded; then": (
            "readme publish must continue after a bounded transient fetch failure"
        ),
        'candidate_published_head_sha="$(git rev-parse HEAD)"': (
            "readme publish must freeze each exact push candidate"
        ),
        'if git push origin "HEAD:$TARGET_BRANCH"; then': (
            "readme publish must treat a successful normal push as its linearization point"
        ),
        'git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_head"': (
            "readme publish must recognize an accepted push after an acknowledgement failure"
        ),
        "fetch_readme_main_bounded &&": (
            "readme publish must perform a final bounded remote verification"
        ),
        "Daily readme publish push failed after 3 bounded non-force attempts": (
            "readme publish must fail after its bounded attempts"
        ),
    }
    for literal, message in required_literals.items():
        if literal not in block:
            errors.append(f"{message}: missing {literal!r}")

    forbidden_literals = {
        "Remote branch advanced before readme publication": (
            "readme publish must not reject a non-overlapping main advance"
        ),
        "git rebase": "readme publish must not rebase validated output",
        "git push --force": "readme publish must not force-push",
        "git push -f": "readme publish must not force-push",
        "docs/latest/daily_signal_performance_": (
            "readme publish must not stage research-owned signal-performance PDFs"
        ),
        "output/debug/": "readme publish must not stage diagnostic output",
        "data/market_abnormal_status/": (
            "readme publish must not stage wall-date market-abnormal raw files"
        ),
        "output/history/market_abnormal_status/": (
            "readme publish must not stage wall-date market-abnormal history"
        ),
    }
    for literal, message in forbidden_literals.items():
        if literal in block:
            errors.append(f"{message}: found {literal!r}")

    exact_counts = {
        'git diff --cached --name-only --no-renames -z > "$staged_paths_file"': 1,
        'git diff --name-only --no-renames -z > "$unstaged_paths_file"': 1,
        'git ls-files --others --exclude-standard -z > "$untracked_paths_file"': 1,
        'python - "$staged_paths_file" "$unstaged_paths_file" "$untracked_paths_file" "$write_paths_file"': 1,
        'python - "$comparison_base" "$remote_head" "$write_paths_file"': 1,
        "fetch_readme_main_bounded()": 1,
        "for push_attempt in 1 2 3; do": 1,
        'if git push origin "HEAD:$TARGET_BRANCH"; then': 1,
        "fetch_readme_main_bounded &&": 1,
    }
    for literal, expected_count in exact_counts.items():
        actual_count = block.count(literal)
        if actual_count != expected_count:
            errors.append(
                "daily readme publish contract count mismatch: "
                f"literal={literal!r} expected={expected_count} actual={actual_count}"
            )
    if block.count(
        'git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_head"'
    ) != 2:
        errors.append(
            "daily readme publish must prove candidate ancestry both before a new push "
            "and in the final acknowledgement-loss check"
        )
    errors.extend(
        require_workflow_order(
            block,
            [
                "fetch_readme_main_bounded() {",
                "for push_attempt in 1 2 3; do",
                'if git push origin "HEAD:$TARGET_BRANCH"; then',
                '            done\n            if [ "$readme_publish_succeeded" != true ] &&',
                "fetch_readme_main_bounded &&",
                'if [ "$readme_publish_succeeded" != true ]; then',
            ],
        )
    )

    for literal in (
        "Dispatch and wait for GitHub Pages deploy",
        "gh workflow run pages.yml",
    ):
        if literal in daily_text:
            errors.append(
                "daily workflow must rely on the pages.yml docs push trigger instead of "
                f"dispatching a duplicate Pages run: found {literal!r}"
            )
    if "  actions: read" not in daily_text:
        errors.append("daily workflow must retain read access for recovery run inspection")
    if "  actions: write" in daily_text:
        errors.append("daily workflow must not retain actions: write after removing Pages dispatch")
    return errors


def validate_daily_failed_recovery_retry_contract(daily_text: str) -> list[str]:
    errors: list[str] = []
    expected_concurrency = (
        "  group: ${{ inputs.recovery_retry_of_run_id != '' && "
        "format('daily-full-retry-{0}', inputs.recovery_source_bundle_trading_date) || "
        "inputs.recovery_correlation_id != '' && "
        "format('daily-full-recovery-{0}', inputs.recovery_correlation_id) || "
        "format('daily-full-pipeline-{0}', github.ref) }}"
    )
    required_literals = {
        "recovery_reservation_commit_sha:": (
            "Daily Full must declare the original reservation commit for code-only retry"
        ),
        "recovery_retry_of_run_id:": (
            "Daily Full must declare the exact failed run resumed by code-only retry"
        ),
        "failed-recovery retry run id requires a reservation commit": (
            "Daily Full must fail closed when retry provenance lacks its reservation commit"
        ),
        "failed-recovery retry requires recovery_expected_head_sha": (
            "Daily Full failed-recovery retry must require its exact reviewed event head"
        ),
        "if expected_head and event_head != expected_head:": (
            "Daily Full failed-recovery retry must reject event-head drift"
        ),
        "Validate single failed-recovery retry": (
            "Daily Full must enforce the one-retry run set before production"
        ),
        "daily-full-failed-recovery-runs.json": (
            "Daily Full must use isolated run evidence for retry correlation"
        ),
        "collect-retry-runs": (
            "Daily Full must collect a complete stable paginated workflow run set"
        ),
        "verify-retry-runs": (
            "Daily Full must validate historical failures and current attempt=1"
        ),
        '--reservation-commit-sha "${{ inputs.recovery_reservation_commit_sha }}"': (
            "Daily Full must verify the immutable original reservation commit"
        ),
        '--retry-of-run-id "${{ inputs.recovery_retry_of_run_id }}"': (
            "Daily Full must bind reservation verification to the failed run"
        ),
        "Daily Full Pipeline | recovery=daily-source-{0}": (
            "Daily Full retry must retain the stable date-scoped production title"
        ),
        "daily-full-retry-{0}": (
            "Daily Full retry concurrency must bind the normalized trading date"
        ),
        '--reservation-path "${{ inputs.recovery_reservation_path }}"': (
            "Daily Full run validation must read the immutable reservation payload"
        ),
        '--expected-head-sha "${{ github.sha }}"': (
            "Daily Full reservation verification must use the actual event head"
        ),
    }
    for literal, message in required_literals.items():
        if literal not in daily_text:
            errors.append(f"{message}: missing {literal!r}")
    if daily_text.count("recovery_reservation_commit_sha:") != 1:
        errors.append("Daily Full retry reservation commit input must be declared exactly once")
    if daily_text.count("recovery_retry_of_run_id:") != 1:
        errors.append("Daily Full retry failed-run input must be declared exactly once")
    if daily_text.splitlines().count(expected_concurrency) != 1:
        errors.append(
            "Daily Full retry concurrency must be the exact trading-date identity and must "
            "not depend on raw failed-run id or recovery correlation"
        )
    return errors


def validate_daily_pdf_runtime_inventory_contract(daily_text: str) -> list[str]:
    errors: list[str] = []
    daily_job = workflow_job_block(daily_text, "daily-full-pipeline")
    if not daily_job:
        return ["daily workflow is missing the daily-full-pipeline job"]

    commands = [line.strip() for line in daily_job.splitlines()]
    expected_runtime_commands = (
        PDF_CONSUMER_RUNTIME_COMMAND,
        PDF_COMPLETION_RUNTIME_COMMAND,
        PDF_INVENTORY_RUNTIME_COMMAND,
    )
    if commands.count(PDF_CONSUMER_RUNTIME_COMMAND) != 1:
        errors.append("Daily Full must run exactly one runtime-only PDF consumer validation")
    if commands.count(PDF_COMPLETION_RUNTIME_COMMAND) != 1:
        errors.append("Daily Full must run exactly one runtime-only PDF completion validation")
    if commands.count(PDF_INVENTORY_RUNTIME_COMMAND) != 2:
        errors.append(
            "Daily Full must run exactly two runtime-only PDF inventory validations"
        )
    if commands.count(PDF_INVENTORY_PREBUILD_COMMAND):
        errors.append("Daily Full must not run static PDF prebuild validation")
    for command in (
        PDF_CONSUMER_FULL_COMMAND,
        PDF_COMPLETION_FULL_COMMAND,
        PDF_INVENTORY_FULL_COMMAND,
    ):
        if commands.count(command):
            errors.append(f"Daily Full must not run mixed full PDF validation: {command}")
    if "      - name: Validate PDF prebuild contract" in daily_job:
        errors.append("Daily Full must not retain the static PDF prebuild step")

    post_alias_step_name = "Validate official daily PDF contract"
    post_alias_block = workflow_step_block(daily_job, post_alias_step_name)
    if not post_alias_block:
        errors.append(f"Daily Full is missing PDF runtime step: {post_alias_step_name}")
    else:
        executable_lines = tuple(
            line.strip()
            for line in post_alias_block.splitlines()
            if line.startswith("          ") and line.strip() and not line.strip().startswith("#")
        )
        if executable_lines != expected_runtime_commands:
            errors.append(
                "Daily Full post-alias PDF runtime step must contain only the exact consumer, "
                "completion, and inventory runtime commands in order"
            )

    publish_step_name = "Publish readme and multi-entry URL check"
    publish_block = workflow_step_block(daily_job, publish_step_name)
    if not publish_block:
        errors.append(f"Daily Full is missing PDF runtime step: {publish_step_name}")

    for step_name, block in (
        (post_alias_step_name, post_alias_block),
        (publish_step_name, publish_block),
    ):
        if not block:
            continue
        if step_name == publish_step_name and block.count(PDF_INVENTORY_RUNTIME_COMMAND) != 1:
            errors.append(
                f"Daily Full step must run one exact runtime-only PDF inventory validation: {step_name}"
            )
        if re.search(r'(?m)^ {8}(?:if|["\']if["\'])\s*:', block):
            errors.append(f"Daily Full PDF runtime inventory step must be unconditional: {step_name}")
        if re.search(
            r'(?m)^ {8}(?:continue-on-error|["\']continue-on-error["\'])\s*:',
            block,
        ):
            errors.append(
                f"Daily Full PDF runtime inventory step must not use continue-on-error: {step_name}"
            )
        if "|| true" in block:
            errors.append(f"Daily Full PDF runtime step must fail closed: {step_name}")
        if not block.rstrip().endswith(f"          {PDF_INVENTORY_RUNTIME_COMMAND}"):
            errors.append(
                f"Daily Full PDF runtime inventory command must be the final executable line: {step_name}"
            )

    build_position = daily_job.find("- name: Build daily market report artifacts")
    aliases_position = daily_job.find("- name: Ensure English report aliases")
    post_build_position = daily_job.find("- name: Validate official daily PDF contract")
    artifact_commit_position = daily_job.find("- name: Commit report artifacts, packets, and rules first")
    publish_position = daily_job.find("- name: Publish readme and multi-entry URL check")
    readme_commit_position = daily_job.find("- name: Commit readme and publish check")
    positions = (
        build_position,
        aliases_position,
        post_build_position,
        artifact_commit_position,
        publish_position,
        readme_commit_position,
    )
    if any(position < 0 for position in positions) or list(positions) != sorted(positions):
        errors.append(
            "Daily Full PDF runtime validations must remain after build/aliases and before the "
            "artifact commit, with the second inventory check after publication and before the "
            "readme commit"
        )

    return errors


def validate_daily_retired_historical_diagnostics_contract(
    daily_text: str,
) -> list[str]:
    daily_job = workflow_job_block(daily_text, "daily-full-pipeline")
    if not daily_job:
        return ["daily workflow is missing the daily-full-pipeline job"]

    active_lines = tuple(
        line.strip()
        for line in daily_job.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
    errors: list[str] = []
    for command in RETIRED_DAILY_HISTORICAL_DIAGNOSTIC_COMMANDS:
        if any(command in line for line in active_lines):
            errors.append(
                "Daily Full must not run retired historical diagnostic command: "
                f"{command}"
            )
    return errors


def validate_daily_runtime_current_snapshot_and_volume_contract(
    daily_text: str,
) -> list[str]:
    daily_job = workflow_job_block(daily_text, "daily-full-pipeline")
    if not daily_job:
        return ["daily workflow is missing the daily-full-pipeline job"]

    def python_commands(block: str) -> tuple[str, ...]:
        return tuple(
            command
            for command in workflow_logical_commands(block)
            if command.startswith("python ")
        )

    def step_guard_errors(block: str, step_name: str) -> list[str]:
        found = [
            key
            for key in ("if", "continue-on-error")
            if re.search(rf'(?m)^ {{8}}(?:{key}|["\']{key}["\'])\s*:', block)
        ]
        if "|| true" in block:
            found.append("|| true")
        shells = tuple(
            value.strip()
            for value in re.findall(
                r'(?m)^ {8}(?:shell|["\']shell["\'])\s*:\s*(.*?)\s*$', block
            )
        )
        expected_shells = (
            ("/bin/bash --noprofile --norc -e -o pipefail {0}",)
            if step_name == "Validate immutable published snapshot revisions"
            else ()
        )
        if shells != expected_shells:
            found.append("shell")
        return [] if not found else [
            "Daily Full runtime-current step must be unconditional and fail closed: "
            f"step={step_name} found={','.join(found)}"
        ]

    snapshot_base = "python scripts/validate_daily_published_model_snapshots.py"
    snapshot_runtime = f"{snapshot_base} --phase runtime"
    scoped_snapshot_runtime = (
        f"{snapshot_runtime} --artifact-id model_signals_for_report "
        "--artifact-id all_candidates_source_rows"
    )
    volume_build_runtime = "python scripts/build_volume_v2_warrant_lineage_history_audit.py --phase runtime"
    volume_validate_base = "python scripts/validate_volume_v2_warrant_lineage_history_audit.py"
    volume_validate_runtime = f"{volume_validate_base} --phase runtime"
    lineage_step_name = "Build volume v2 lineage audit from published snapshots"
    step_contracts = (
        ("Publish and validate volume v2 audit-source snapshots", (scoped_snapshot_runtime,), snapshot_base, "snapshot"),
        ("Publish and validate post-audit daily model snapshots", (snapshot_runtime,), snapshot_base, "snapshot"),
        ("Validate immutable published snapshot revisions", (snapshot_runtime,), snapshot_base, "snapshot"),
        (lineage_step_name, (volume_build_runtime, volume_validate_runtime), "python ", "Volume v2"),
    )
    errors: list[str] = []
    if re.search(
        r'(?m)^ {4}(?:defaults|["\']defaults["\'])\s*:\s*\r?\n'
        r' {6}(?:run|["\']run["\'])\s*:\s*\r?\n'
        r' {8}(?:shell|["\']shell["\'])\s*:',
        daily_job,
    ):
        errors.append("Daily Full job must not override defaults.run.shell")
    for step_name, expected, prefix, label in step_contracts:
        block = workflow_step_block(daily_job, step_name)
        if not block:
            errors.append(f"Daily Full is missing runtime {label} step: {step_name}")
            continue
        observed = tuple(
            command for command in python_commands(block) if command.startswith(prefix)
        )
        if observed != expected:
            errors.append(
                f"Daily Full {label} step must contain its exact runtime-current "
                "commands in order: "
                f"step={step_name} actual={observed} expected={expected}"
            )
        errors.extend(step_guard_errors(block, step_name))

    job_commands = python_commands(daily_job)
    snapshot_commands = tuple(
        command for command in job_commands if command.startswith(snapshot_base)
    )
    if sorted(snapshot_commands) != sorted(
        (scoped_snapshot_runtime, snapshot_runtime, snapshot_runtime)
    ):
        errors.append(
            "Daily Full must run exactly three runtime-current snapshot validations "
            "with only the early audit-source call scoped"
        )

    for command, label in (
        (volume_build_runtime, "build"),
        (volume_validate_runtime, "validation"),
    ):
        if job_commands.count(command) != 1:
            errors.append(f"Daily Full must run exactly one runtime-current Volume v2 audit {label}")
    if any(
        command.startswith(volume_validate_base)
        and command != volume_validate_runtime
        for command in job_commands
    ):
        errors.append("Daily Full must not run a full or unphased Volume v2 audit validation")

    ordered_markers = (
        snapshot_base,
        volume_build_runtime,
        volume_validate_runtime,
        "- name: Build volume v2 formal operation adapter",
    )
    positions = tuple(daily_job.find(marker) for marker in ordered_markers)
    if any(position < 0 for position in positions) or list(positions) != sorted(positions):
        errors.append(
            "Daily Full current snapshot validation, Volume v2 build/validate, and "
            "operation adapter must remain in fail-closed order"
        )
    return errors


def validate_daily_runtime_critical_contracts(
    daily_text: str | None = None,
) -> list[str]:
    errors: list[str] = []
    if daily_text is None:
        if not DAILY_WORKFLOW.exists():
            return [f"missing daily workflow: {DAILY_WORKFLOW.relative_to(ROOT)}"]
        daily_text = read_text(DAILY_WORKFLOW)

    errors.extend(validate_daily_authority_snapshot_publish_contract(daily_text))
    errors.extend(validate_daily_readme_publish_contract(daily_text))
    errors.extend(validate_daily_failed_recovery_retry_contract(daily_text))
    errors.extend(validate_daily_pdf_runtime_inventory_contract(daily_text))
    errors.extend(validate_daily_retired_historical_diagnostics_contract(daily_text))
    errors.extend(validate_daily_runtime_current_snapshot_and_volume_contract(daily_text))
    errors.extend(validate_daily_full_legacy_removal_guard(daily_text))

    market_literals = (
        "market-session-preflight:",
        "Reject non-main production dispatch",
        "github.ref_name != 'main'",
        "python scripts/market_session_calendar.py --phase preflight",
        "should_run_daily_pipeline",
        "Verify open-confirmed target date",
        "open_confirmed",
        "OFFICIAL_PRICE_TARGET_DATE: ${{ needs.market-session-preflight.outputs.expected_main_price_date }}",
    )
    for literal in market_literals:
        if literal not in daily_text:
            errors.append(f"daily workflow runtime market-session contract missing: {literal}")

    recovery_literals = (
        "recovery_source_bundle_commit_sha",
        "recovery_source_bundle_manifest_path",
        "recovery_source_bundle_manifest_sha256",
        "recovery_source_bundle_sha",
        "recovery_source_bundle_trading_date",
        "recovery source bundle inputs must be all-or-none",
        "Validate immutable recovery input set",
        "Materialize immutable recovery source bundle for preflight",
        "Materialize immutable recovery source bundle for production",
        "daily_source_recovery_bundle.py verify",
        "--materialize",
    )
    for literal in recovery_literals:
        if literal not in daily_text:
            errors.append(f"daily workflow runtime source-bundle contract missing: {literal}")
    if daily_text.count("ref: ${{ needs.market-session-preflight.outputs.source_sha }}") < 2:
        errors.append(
            "daily workflow runtime production checkouts must remain pinned to the preflight source SHA"
        )
    if daily_text.count('if [ "$CURRENT_HEAD" != "$PREFLIGHT_SOURCE_SHA" ]; then') != 2:
        errors.append(
            "daily workflow runtime must verify both pinned production checkouts against the preflight source SHA"
        )

    if daily_text.count("python scripts/validate_daily_staged_paths.py") < 3:
        errors.append(
            "daily workflow runtime must validate staged publication boundaries before each production commit"
        )
    if not STAGED_PATH_VALIDATOR.exists():
        errors.append(
            f"missing daily staged path validator: {STAGED_PATH_VALIDATOR.relative_to(ROOT)}"
        )
    else:
        staged_validator_text = read_text(STAGED_PATH_VALIDATOR)
        staged_validator_literals = (
            "git\", \"diff\", \"--cached\", \"--name-only",
            "FORBIDDEN_STAGED_PATTERNS",
            '"output/history/research/*"',
            "validate_docs_latest_mirrors()",
            "validate_indicator_guide_counts()",
        )
        for literal in staged_validator_literals:
            if literal not in staged_validator_text:
                errors.append(
                    "daily staged path validator publication boundary missing: "
                    f"{literal}"
                )

    if workflow_job_block(daily_text, "daily-pdf-dfkai-replay"):
        errors.append(
            "daily workflow runtime must not make the non-delivery Windows PDF replay a hard job"
        )
    return errors


def main(argv: Sequence[str] = ()) -> int:
    parser = argparse.ArgumentParser(description="Validate daily production boundaries")
    parser.add_argument(
        "--runtime-critical-only",
        action="store_true",
        help="validate only runtime-critical Daily Full workflow contracts",
    )
    args = parser.parse_args(list(argv))
    if args.runtime_critical_only:
        errors = validate_daily_runtime_critical_contracts()
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("daily production runtime-critical boundary validation passed")
        print(f"validated_workflow={DAILY_WORKFLOW.relative_to(ROOT)}")
        return 0

    errors: list[str] = []
    daily_text = read_text(DAILY_WORKFLOW)
    errors.extend(validate_daily_full_legacy_removal_guard(daily_text))
    errors.extend(validate_daily_authority_snapshot_publish_contract(daily_text))
    errors.extend(validate_daily_readme_publish_contract(daily_text))
    errors.extend(validate_daily_failed_recovery_retry_contract(daily_text))
    errors.extend(validate_daily_retired_historical_diagnostics_contract(daily_text))
    errors.extend(validate_daily_runtime_current_snapshot_and_volume_contract(daily_text))
    errors.extend(validate_authority_workflow_publishers())

    if not HISTORICAL_SOURCE_REPLAY_WORKFLOW.exists():
        errors.append("missing historical structured-source replay workflow")
    else:
        errors.extend(
            validate_historical_source_replay_workflow(
                read_text(HISTORICAL_SOURCE_REPLAY_WORKFLOW)
            )
        )

    errors.extend(run_code_isolation_policy_validation())
    errors.extend(run_repo_production_inventory_validation())
    errors.extend(run_repo_file_lifecycle_inventory_validation())
    errors.extend(run_repo_semantic_integrity_validation())
    errors.extend(run_repo_advanced_integrity_validation())
    errors.extend(validate_model_operation_price_confirmation_rules())
    errors.extend(validate_daily_operation_packet_row_metric_contract())

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
    if staged_path_validation_count < 3:
        errors.append(
            "daily_full_pipeline must validate staged paths before closure and both daily commit steps"
        )

    market_session_workflow_literals = {
        "market-session-preflight:": "daily_full_pipeline must resolve the official market session before production",
        "Reject non-main production dispatch": "daily_full_pipeline must reject branch workflow_dispatch runs",
        "github.ref_name != 'main'": "daily_full_pipeline must make the non-main rejection explicit",
        "python scripts/market_session_calendar.py --phase preflight": (
            "daily_full_pipeline must run the live official market-session preflight"
        ),
        "output/latest/market_session_status_latest.json": (
            "daily_full_pipeline must preserve the market-session status artifact"
        ),
        "data/market_calendar/exceptional_non_trading_days.csv": (
            "daily_full_pipeline must preserve exceptional closure evidence"
        ),
        "should_run_daily_pipeline": "daily_full_pipeline must branch on the market-session decision",
        "record-market-closure:": "daily_full_pipeline must record closed-market evidence without publishing",
        "OFFICIAL_PRICE_TARGET_DATE: ${{ needs.market-session-preflight.outputs.expected_main_price_date }}": (
            "daily_full_pipeline must fetch the exact expected market date"
        ),
        "Verify open-confirmed target date": (
            "daily_full_pipeline must verify open_confirmed before continuing"
        ),
    }
    for literal, message in market_session_workflow_literals.items():
        if literal not in daily_text:
            errors.append(f"{message}: missing {literal!r}")

    preflight_block = workflow_job_block(daily_text, "market-session-preflight")
    for forbidden in ("git commit", "git push", "pages.yml", "generate_chatgpt_side_daily_reports.py"):
        if forbidden in preflight_block:
            errors.append(f"market-session-preflight must not publish artifacts: found {forbidden!r}")

    closure_block = workflow_job_block(daily_text, "record-market-closure")
    for forbidden in (
        "fetch_official_daily_price.py",
        "git add data/daily_price/",
        "generate_chatgpt_side_daily_reports.py",
        "validate_chatgpt_daily_report_new_conversation_replay.py",
        "pages.yml",
    ):
        if forbidden in closure_block:
            errors.append(f"record-market-closure must not fetch, render, or deploy: found {forbidden!r}")

    if not RECENT_PRICE_GAP_WORKFLOW.exists():
        errors.append(f"missing recent price-gap workflow: {RECENT_PRICE_GAP_WORKFLOW.relative_to(ROOT).as_posix()}")
    else:
        repair_text = read_text(RECENT_PRICE_GAP_WORKFLOW)
        errors.extend(validate_recent_price_gap_workflow_contract(repair_text))

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
    if workflow_job_block(daily_text, "daily-pdf-dfkai-replay"):
        errors.append(
            "daily_full_pipeline must leave actual six-PDF rendering to the formal PDF owner; "
            "daily-pdf-dfkai-replay is not a production completion gate"
        )

    source_gate_block = workflow_job_block(
        daily_text,
        "daily-pdf-source-gate-validation",
    )
    required_source_gate_literals = {
        "needs: [market-session-preflight, record-market-closure, daily-full-pipeline]": (
            "closed-day source-gate validation must wait for market-session jobs"
        ),
        "always()": "closed-day source-gate validation must evaluate after skipped production",
        "inputs.validate_latest_daily_pdf_replay == true": (
            "closed-day source-gate validation must require explicit workflow input"
        ),
        "needs.market-session-preflight.result == 'success'": (
            "closed-day source-gate validation must require successful preflight"
        ),
        "needs.record-market-closure.result == 'success'": (
            "closed-day source-gate validation must wait for closure evidence handling"
        ),
        "needs.market-session-preflight.outputs.market_status == 'closed_scheduled'": (
            "closed-day source-gate validation must be limited to scheduled closures"
        ),
        "runs-on: ubuntu-latest": (
            "closed-day source-gate validation must not allocate a Windows font runner"
        ),
        "--source-gate-only": (
            "closed-day source-gate validation must not render PDFs"
        ),
        '--validation-replay-main-price-date "$EXPECTED_MAIN_PRICE_DATE"': (
            "closed-day source-gate validation must bind the exact expected date"
        ),
        "daily-pdf-source-gate-main": (
            "closed-day source-gate validation must upload textual evidence"
        ),
        'source_gate_log="$RUNNER_TEMP/daily_pdf_source_gate_validation.log"': (
            "closed-day source-gate evidence must be written outside the repository"
        ),
        'tee "$source_gate_log"': (
            "closed-day source-gate validation must capture output in the temporary log"
        ),
        "path: ${{ runner.temp }}/daily_pdf_source_gate_validation.log": (
            "closed-day source-gate artifact must upload the temporary log"
        ),
    }
    if "validate_latest_daily_pdf_replay:" not in daily_text:
        errors.append(
            "daily_full_pipeline must expose an explicit closed-day source-gate validation input"
        )
    for literal, message in required_source_gate_literals.items():
        if literal not in source_gate_block:
            errors.append(f"{message}: missing {literal!r}")
    for forbidden in (
        "closed_emergency",
        "Install and validate DFKai-SB",
        "validate_chatgpt_daily_report_new_conversation_replay.py",
        "*.pdf",
        "git commit",
        "git push",
        "pages.yml",
        "tee daily_pdf_source_gate_validation.log",
        "path: daily_pdf_source_gate_validation.log",
    ):
        if forbidden in source_gate_block:
            errors.append(
                "closed-day source-gate validation must remain no-font, no-render, and no-publish; "
                f"found {forbidden!r}"
            )
    if not source_gate_block:
        errors.append(
            "daily_full_pipeline missing daily-pdf-source-gate-validation job"
        )
    daily_pipeline_block = workflow_job_block(daily_text, "daily-full-pipeline")
    if "- name: Replay ChatGPT-side daily PDF new conversation" in daily_pipeline_block:
        errors.append("daily_full_pipeline Ubuntu job must not render the six daily PDFs")

    if not STAGED_PATH_VALIDATOR.exists():
        errors.append(f"missing daily staged path validator: {STAGED_PATH_VALIDATOR}")

    if not DAILY_MODEL_MAINTENANCE_PR_WORKFLOW.exists():
        errors.append(
            "missing daily model maintenance PR validation workflow: "
            f"{DAILY_MODEL_MAINTENANCE_PR_WORKFLOW.relative_to(ROOT).as_posix()}"
        )
    else:
        pr_workflow_text = read_text(DAILY_MODEL_MAINTENANCE_PR_WORKFLOW)
        errors.extend(validate_daily_model_pr_scope_contract(pr_workflow_text))
        errors.extend(validate_daily_model_legacy_removal_guard(pr_workflow_text))
        errors.extend(
            validate_daily_model_volume_v2_runtime_markdown_contract(
                pr_workflow_text
            )
        )
        required_pr_workflow_literals = {
            "python scripts/validate_daily_pdf_contract_consumers.py": (
                "daily model maintenance PR workflow must validate daily PDF consumer contracts"
            ),
            "python scripts/validate_daily_pdf_completion_hard_gate.py": (
                "daily model maintenance PR workflow must validate daily PDF completion hard gates"
            ),
            "python scripts/validate_daily_production_boundaries.py": (
                "daily model maintenance PR workflow must run production boundary validation"
            ),
            'python scripts/validate_daily_published_model_snapshots_pr_safe.py --base-ref "$BASE_SHA"': (
                "daily model maintenance PR workflow must use the PR-safe published snapshot gate"
            ),
            "tests/test_chatgpt_daily_report_new_conversation_replay.py": (
                "daily model maintenance PR workflow must run rendered PDF replay regression tests"
            ),
            "tests/test_daily_report_source_resolver.py": (
                "daily model maintenance PR workflow must run source resolver regression tests"
            ),
            "tests/test_daily_volume_breakout_operation_section.py": (
                "daily model maintenance PR workflow must run volume operation adapter tests"
            ),
            "tests/test_daily_price_pullback_23ema_operation_section.py": (
                "daily model maintenance PR workflow must run 23EMA operation adapter tests"
            ),
        }
        for literal, message in required_pr_workflow_literals.items():
            if literal not in pr_workflow_text:
                errors.append(f"{message}: missing {literal!r}")
        if "daily-pdf-dfkai-replay:" in pr_workflow_text:
            errors.append("daily model maintenance PR workflow must not own the Windows DFKai replay job")
        if "Install and validate DFKai-SB" in pr_workflow_text:
            errors.append("daily model maintenance PR workflow must not install DFKai")
        pr_validation_block = workflow_job_block(
            pr_workflow_text,
            "daily-model-maintenance-pr-validation",
        )
        if "- name: Replay ChatGPT-side daily PDF new conversation" in pr_validation_block:
            errors.append("daily model PR Ubuntu validation job must not render the six daily PDFs")

    if not DAILY_PDF_REPLAY_PR_WORKFLOW.exists():
        errors.append(
            "missing PDF-impact replay PR validation workflow: "
            f"{DAILY_PDF_REPLAY_PR_WORKFLOW.relative_to(ROOT).as_posix()}"
        )
    else:
        pdf_replay_workflow_text = read_text(DAILY_PDF_REPLAY_PR_WORKFLOW)
        required_pdf_replay_literals = {
            "pull_request:": "PDF replay workflow must run automatically for PDF-impact pull requests",
            "workflow_dispatch:": "PDF replay workflow must support explicit manual replay",
            'scripts/generate_chatgpt_side_daily_reports.py': (
                "PDF replay workflow must trigger on the formal daily PDF renderer"
            ),
            'config/daily_pdf_rendered_model_regression_contract.csv': (
                "PDF replay workflow must trigger on the rendered-model PDF contract"
            ),
            'config/daily_pdf_semantic_golden_cases.csv': (
                "PDF replay workflow must trigger on PDF semantic golden cases"
            ),
            'scripts/validate_chatgpt_side_pdf_contract.py': (
                "PDF replay workflow must trigger on its font and PDF contract runtime"
            ),
            "daily-pdf-replay-contract-validation:": (
                "PDF replay workflow must run a cheap contract gate before the Windows job"
            ),
            "python scripts/validate_repo_production_inventory.py": (
                "PDF replay workflow must validate repository ownership inventory"
            ),
            "python scripts/validate_daily_production_boundaries.py": (
                "PDF replay workflow must validate production boundaries"
            ),
            "tests/test_daily_model_maintenance_pr_validation_workflow.py": (
                "PDF replay workflow must test its own routing contract"
            ),
            "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py": (
                "PDF replay workflow must run actual rendered PDF replay validation"
            ),
            "PDF replay source_ref=$source_ref": "PDF replay workflow must log the immutable source ref",
            "PDF replay output_dir=chatgpt_side_outputs_pr_validation": (
                "PDF replay workflow must log the stable replay output directory"
            ),
            "actions/upload-artifact@v4": "PDF replay workflow must preserve generated PDF evidence",
        }
        for literal, message in required_pdf_replay_literals.items():
            if literal not in pdf_replay_workflow_text:
                errors.append(f"{message}: missing {literal!r}")
        pdf_replay_pull_request_trigger = pdf_replay_workflow_text.split(
            "  workflow_dispatch:",
            1,
        )[0]
        errors.extend(validate_pdf_replay_automatic_paths(pdf_replay_workflow_text))
        for forbidden in (
            "data/financial_statement_history/*.csv",
            "scripts/build_financial_statement_pit.py",
            "tests/test_revenue_unreacted_range_*.py",
            "config/git_worktree_materialization_contract.csv",
            "scripts/git_worktree_safety.py",
            "scripts/market_session_calendar.py",
            "scripts/resolve_daily_report_source_state.py",
            "scripts/run_chatgpt_daily_report_entrypoint.py",
            "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
            "scripts/validate_daily_publish_freshness_gate.py",
        ):
            if forbidden in pdf_replay_pull_request_trigger:
                errors.append(
                    "PDF replay workflow must not trigger on non-renderer validation/source paths: "
                    f"{forbidden!r}"
                )
        errors.extend(
            validate_dfkai_pdf_replay_job(
                pdf_replay_workflow_text,
                workflow_label="daily_pdf_replay_pr_validation",
                needs_job="daily-pdf-replay-contract-validation",
                output_dir="chatgpt_side_outputs_pr_validation",
                upload_step="Upload PR daily PDF replay evidence",
            )
        )
        errors.extend(validate_pr_pdf_replay_source_pin(pdf_replay_workflow_text))
    if not CANONICAL_CHATGPT_PDF_ENTRYPOINT.exists():
        errors.append(f"missing canonical ChatGPT-side PDF entrypoint: {CANONICAL_CHATGPT_PDF_ENTRYPOINT}")
    else:
        entrypoint_text = read_text(CANONICAL_CHATGPT_PDF_ENTRYPOINT)
        required_entrypoint_literals = {
            "resolve_daily_report_source_state": "official PDF entrypoint must use the origin/main resolver",
            "create_registered_full_temp_worktree": "official PDF entrypoint must use the guarded clean temporary source worktree helper",
            'consumer_id="chatgpt_daily_report_entrypoint"': "official PDF entrypoint must use its registered full-checkout consumer id",
            "CHATGPT_DAILY_REPORT_ENTRYPOINT": "official PDF entrypoint must be the only allowed renderer caller",
            "SEMANTIC_MANIFEST_NAME": "official PDF entrypoint must require semantic PDF manifest output",
            "semantic_manifest_path": "official PDF entrypoint runtime manifest must record semantic PDF manifest path",
            "PYTHONIOENCODING": "official PDF entrypoint must force UTF-8 subprocess output",
            'reconfigure(encoding="utf-8", errors="replace")': "official PDF entrypoint must force UTF-8 terminal output",
            "source-gate-only": "official PDF entrypoint must expose a source-gate-only diagnostic mode",
            "GENERATOR_RELATIVE_PATH": "official PDF entrypoint must address the renderer relative to the clean source worktree",
            "source_generator = source_root / GENERATOR_RELATIVE_PATH": "official PDF entrypoint must run the renderer from the clean source worktree",
            "cwd=source_root": "official PDF entrypoint must execute the renderer with the clean source worktree as cwd",
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
        "chatgpt_daily_pdf_semantic_manifest.csv": "daily usage prompt must require semantic row manifest evidence",
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
    raise SystemExit(main(sys.argv[1:]))
