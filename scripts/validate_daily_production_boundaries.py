from __future__ import annotations

import re
import importlib.util
import fnmatch
import posixpath
import shlex
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RECENT_PRICE_GAP_WORKFLOW = ROOT / ".github" / "workflows" / "repair_recent_daily_price_gaps.yml"
HISTORICAL_SOURCE_REPLAY_WORKFLOW = (
    ROOT / ".github" / "workflows" / "historical_structured_source_replay.yml"
)
DAILY_MODEL_MAINTENANCE_PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
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
    marker = f"  {job_id}:"
    start = text.find(marker)
    if start < 0:
        return ""
    next_job = re.search(r"(?m)^  [A-Za-z0-9_-]+:\s*$", text[start + len(marker) :])
    if next_job is None:
        return text[start:]
    return text[start : start + len(marker) + next_job.start()]


def workflow_step_block(text: str, step_name: str) -> str:
    marker = f"      - name: {step_name}"
    start = text.find(marker)
    if start < 0:
        return ""
    next_step = text.find("\n      - name:", start + len(marker))
    if next_step < 0:
        return text[start:]
    return text[start:next_step]


def workflow_pull_request_paths(text: str) -> set[str]:
    pull_request_trigger = text.split("  workflow_dispatch:", 1)[0]
    return {
        match.group(1)
        for line in pull_request_trigger.splitlines()
        if (match := re.fullmatch(r'\s*-\s+"?([^"\s]+)"?\s*', line))
    }


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
        "ref: main": "must checkout main",
        "group: historical-structured-source-replay-${{ github.ref }}": "must use an independent replay concurrency group",
        "cancel-in-progress: false": "must not cancel an in-flight official producer",
        "Require production artifact write deploy key": "must fail closed on missing writer credentials",
        "Checkout exact main source": "must checkout only after credential preflight",
        "Install replay dependencies": "must install runtime dependencies before repository validators",
        "Validate repository automation boundaries": "must validate repository contracts before replay",
        '"$base_sha" != "$EXPECTED_MAIN_SHA"': "must bind checkout to expected_main_sha",
        '"$base_sha" != "$remote_main_sha"': "must bind checkout to remote main",
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
        "git push origin HEAD:refs/heads/main": "must use one fail-closed non-force push",
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
    if len(re.findall(r"(?m)^\s*git push\s", text)) != 1:
        errors.append("historical structured-source replay must execute exactly one Git push")

    forbidden_literals = {
        "git add -A": "must not broad-stage the repository",
        "ci_push_with_retry.sh": "must not rebase or regenerate on a moving main",
        "git rebase": "must not rebase after replay validation",
        "git push --force": "must not force-push production artifacts",
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
        "Validate repository automation boundaries",
        "python scripts/replay_historical_structured_sources.py",
        "python scripts/validate_historical_structured_source_replay.py",
        "git add data/daily_price/",
        "python scripts/validate_historical_source_replay_staged_paths.py",
        "Reject remote-main drift before the only output commit",
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
        if token.startswith(("-C", "-c", "--git-dir=", "--work-tree=", "--namespace=", "--config-env=")) or token in {"--no-pager", "--literal-pathspecs"}:
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
        r"(?:--git-dir|--work-tree|--namespace|--config-env)=\S+|--no-pager|--literal-pathspecs)\s+)*"
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
            if git_native_mutation_may_publish_authority(command):
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
        "ref: main": "recent price-gap workflow must operate on main",
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
    ):
        if forbidden in repair_text:
            errors.append(
                "recent price-gap workflow must not independently publish market authority: "
                f"found {forbidden!r}"
            )
    return errors


def validate_daily_authority_snapshot_publish_contract(daily_text: str) -> list[str]:
    errors: list[str] = []
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
    required_publish_literals = {
        'git diff --cached --name-only -z > "$staged_paths_file"': (
            "daily publish must capture the actual staged path set"
        ),
        'git diff --name-only --no-renames -z "$PREFLIGHT_SOURCE_SHA..$remote_head"': (
            "daily publish must compare pinned-source-to-current-main paths"
        ),
        "overlap = sorted(staged_paths & main_paths)": (
            "daily publish must fail closed only on an actual path overlap"
        ),
        'git merge --no-edit "origin/$TARGET_BRANCH"': (
            "daily publish must ordinary-merge a non-overlapping main advance"
        ),
        "for push_attempt in 1 2 3": (
            "daily publish must bound non-force push retries"
        ),
        'git push origin "HEAD:$TARGET_BRANCH"': (
            "daily publish must retain a normal non-force push"
        ),
    }
    for literal, message in required_publish_literals.items():
        if literal not in daily_text:
            errors.append(f"{message}: missing {literal!r}")
    for forbidden in ("git rebase", "git push --force", "git push -f"):
        if forbidden in daily_text:
            errors.append(
                f"daily publish must not use rebase or force during bounded retry: found {forbidden!r}"
            )
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
        "failed-recovery retry inputs must be paired": (
            "Daily Full must fail closed on a partial retry input pair"
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


def main() -> int:
    errors: list[str] = []
    daily_text = read_text(DAILY_WORKFLOW)
    errors.extend(validate_daily_authority_snapshot_publish_contract(daily_text))
    errors.extend(validate_daily_failed_recovery_retry_contract(daily_text))
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
    errors.extend(
        validate_dfkai_pdf_replay_job(
            daily_text,
            workflow_label="daily_full_pipeline",
            needs_job="[market-session-preflight, record-market-closure, daily-full-pipeline]",
            output_dir="chatgpt_side_outputs_new_conversation_replay",
            upload_step="Upload main daily PDF replay evidence",
        )
    )
    daily_replay_block = workflow_job_block(daily_text, "daily-pdf-dfkai-replay")
    required_main_replay_literals = {
        "always()": "main PDF replay must evaluate after skipped mutually exclusive jobs",
        "needs.market-session-preflight.result == 'success'": (
            "main PDF replay must require a successful live market-session preflight"
        ),
        "needs.daily-full-pipeline.result == 'success'": (
            "main PDF replay must follow a successful open-market production job"
        ),
        "EXPECTED_MAIN_PRICE_DATE: ${{ needs.market-session-preflight.outputs.expected_main_price_date }}": (
            "main PDF replay must bind to the market-session expected date"
        ),
        '--expected-main-price-date "$EXPECTED_MAIN_PRICE_DATE"': (
            "main PDF replay must pass the exact expected date to the replay validator"
        ),
    }
    for literal, message in required_main_replay_literals.items():
        if literal not in daily_replay_block:
            errors.append(f"{message}: missing {literal!r}")
    for forbidden in (
        "inputs.validate_latest_daily_pdf_replay",
        "closed_scheduled",
        "closed_emergency",
    ):
        if forbidden in daily_replay_block:
            errors.append(
                "Windows DFKai replay must be limited to successful open-market production; "
                f"found {forbidden!r}"
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
        required_pr_workflow_literals = {
            "pull_request:": "daily model maintenance PR workflow must run on pull_request",
            "scripts/generate_chatgpt_side_daily_reports.py": (
                "daily model maintenance PR workflow must trigger on PDF renderer changes"
            ),
            "scripts/update_daily_published_model_snapshots.py": (
                "daily model maintenance PR workflow must trigger on published snapshot changes"
            ),
            "scripts/resolve_daily_report_source_state.py": (
                "daily model maintenance PR workflow must trigger on source-gate changes"
            ),
            "config/daily_pdf_rendered_model_regression_contract.csv": (
                "daily model maintenance PR workflow must trigger on rendered PDF regression contract changes"
            ),
            "config/daily_pdf_semantic_golden_cases.csv": (
                "daily model maintenance PR workflow must trigger on semantic PDF golden case changes"
            ),
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
        daily_dfkai_step = workflow_step_block(daily_text, "Install and validate DFKai-SB")
        pr_dfkai_step = workflow_step_block(
            pdf_replay_workflow_text,
            "Install and validate DFKai-SB",
        )
        if daily_dfkai_step and pr_dfkai_step and daily_dfkai_step != pr_dfkai_step:
            errors.append(
                "daily_full_pipeline and daily_pdf_replay_pr_validation must use identical DFKai install and final-validation steps"
            )

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
    raise SystemExit(main())
