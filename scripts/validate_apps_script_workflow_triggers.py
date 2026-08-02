from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPS_SCRIPT = ROOT / "docs" / "apps_script_workflow_trigger.gs"
WORKFLOW_DIR = ROOT / ".github" / "workflows"
MIN_TRIGGER_SPACING_MINUTES = 60
TDCC_CHAIN_POLL_MINUTES = 5
TDCC_WORKFLOW = "tdcc_weekly.yml"
INDIVIDUAL_REFRESH_WORKFLOW = "individual_stock_data_refresh.yml"

EXPECTED_DISPATCHES = {
    "daily_full_pipeline.yml",
    "repair_recent_daily_price_gaps.yml",
    "repair_tdcc_monthly_history_gaps.yml",
    "individual_stock_data_refresh.yml",
    "tdcc_weekly.yml",
    "event_catalyst_update.yml",
    "weekly_theme_review.yml",
    "research_backtest_pipeline.yml",
}

SUNDAY = 0
MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
WEEKDAYS = {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY}
ALL_DAYS = {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY}

SCHEDULED_WORKFLOW_DISPATCHES = [
    ("triggerEventCatalystUpdate morning", ALL_DAYS, 8 * 60 + 10),
    ("triggerTdccHistoryGapRepair", {TUESDAY}, 9 * 60 + 30),
    ("triggerDailyPriceGapRepair", WEEKDAYS, 10 * 60 + 30),
    ("triggerTdccWeeklyReport", {SATURDAY}, 15 * 60 + 30),
    ("triggerEventCatalystUpdate evening", ALL_DAYS, 18 * 60 + 10),
    ("triggerDailyStockMonitor", WEEKDAYS, 19 * 60 + 30),
    ("triggerEveningDataOnlyRepair", WEEKDAYS, 20 * 60 + 30),
    ("triggerWeeklyThemeReview", {SUNDAY}, 19 * 60 + 30),
    ("triggerResearchBacktestPipeline", {SUNDAY}, 21 * 60 + 10),
    ("triggerIndividualStockDataRefresh", ALL_DAYS, 22 * 60 + 20),
]


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def workflow_inputs(workflow_file: str) -> set[str]:
    path = WORKFLOW_DIR / workflow_file
    text = read_text(path)
    match = re.search(r"workflow_dispatch:\s*\n\s+inputs:\s*\n(?P<body>.*?)(?:\n\S|\Z)", text, re.S)
    if not match:
        return set()
    body = match.group("body")
    return set(re.findall(r"^\s{6}([A-Za-z0-9_]+):\s*$", body, re.M))


def workflow_dispatch_input_property(
    workflow_file: str, input_name: str, property_name: str
) -> str | None:
    text = read_text(WORKFLOW_DIR / workflow_file)
    input_block = re.search(
        rf"(?ms)^ {{6}}{re.escape(input_name)}:\s*\n(?P<body>(?: {{8}}.*\n)*?)(?=^ {{6}}\S|\\Z)",
        text,
    )
    if not input_block:
        return None
    body = input_block.group("body")
    property_match = re.search(
        rf"(?ms)^ {{8}}{re.escape(property_name)}:\s*(.+?)\s*$",
        body,
    )
    if not property_match:
        return None
    return property_match.group(1).strip().strip('"').strip("'")


def validate_repair_workflow_yaml_contract(errors: list[str]) -> None:
    workflow_file = "repair_recent_daily_price_gaps.yml"
    workflow_text = read_text(WORKFLOW_DIR / workflow_file)
    expected_run_name = "Repair Recent Daily Price Gaps | correlation=${{ inputs.dispatch_correlation_id }}"
    if not re.search(rf"(?m)^run-name:\\s*{re.escape(expected_run_name)}\\s*$", workflow_text):
        errors.append(
            "Repair workflow run-name must be exactly "
            f"'Repair Recent Daily Price Gaps | correlation=${{{{ inputs.dispatch_correlation_id }}}}'"
        )

    correlation_type = workflow_dispatch_input_property(
        workflow_file, "dispatch_correlation_id", "type"
    )
    if correlation_type is None:
        errors.append(
            "Repair recent daily price gaps workflow must declare workflow_dispatch input dispatch_correlation_id.type"
        )
    elif correlation_type != "string":
        errors.append(
            "Repair recent daily price gaps workflow dispatch_correlation_id.type must be string"
        )

    correlation_default = workflow_dispatch_input_property(
        workflow_file, "dispatch_correlation_id", "default"
    )
    if correlation_default is None:
        errors.append(
            "Repair recent daily price gaps workflow must declare workflow_dispatch input dispatch_correlation_id.default"
        )
    elif correlation_default != "manual":
        errors.append(
            "Repair recent daily price gaps workflow dispatch_correlation_id.default must be manual"
        )


def apps_script_dispatches() -> dict[str, dict[str, str]]:
    text = read_text(APPS_SCRIPT)
    dispatches: dict[str, dict[str, str]] = {}
    string_constants = dict(
        re.findall(r'^const\s+([A-Z][A-Z0-9_]*)\s*=\s*"([^"]+)";\s*$', text, re.M)
    )
    pattern = re.compile(
        r'dispatchWorkflow_\('
        r'(?:(?:"(?P<workflow>[^"]+)")|(?P<workflow_constant>[A-Z][A-Z0-9_]*))'
        r'(?:,\s*\{(?P<inputs>.*?)\})?\);',
        re.S,
    )
    for match in pattern.finditer(text):
        workflow = match.group("workflow")
        if not workflow:
            workflow = string_constants.get(match.group("workflow_constant"), "")
        if not workflow:
            continue
        inputs_body = match.group("inputs") or ""
        inputs = dict(
            re.findall(r'^\s*([A-Za-z0-9_]+)\s*:\s*"([^"]*)"', inputs_body, re.M)
        )
        dispatches[workflow] = inputs
    return dispatches


def apps_script_functions() -> set[str]:
    text = read_text(APPS_SCRIPT)
    return set(re.findall(r"^function\s+([A-Za-z0-9_]+)\s*\(", text, re.M))


def extract_gas_function_body(text: str, function_name: str) -> str:
    declaration_pattern = re.compile(
        rf"^function\s+{re.escape(function_name)}\s*\([^)]*\)\s*\{{",
        re.M,
    )
    match = declaration_pattern.search(text)
    if not match:
        raise ValueError(f"Apps Script function not found: {function_name}")

    start = match.end() - 1
    depth = 0
    in_single_quote = False
    in_double_quote = False
    in_template_quote = False
    in_line_comment = False
    in_block_comment = False
    in_regex = False

    index = start
    while index < len(text):
        char = text[index]

        if in_single_quote:
            if char == "\\" and index + 1 < len(text):
                index += 2
                continue
            if char == "'":
                in_single_quote = False
            index += 1
            continue

        if in_double_quote:
            if char == "\\" and index + 1 < len(text):
                index += 2
                continue
            if char == '"':
                in_double_quote = False
            index += 1
            continue

        if in_template_quote:
            if char == "\\" and index + 1 < len(text):
                index += 2
                continue
            if char == "`":
                in_template_quote = False
            index += 1
            continue

        if in_line_comment:
            if char == "\n":
                in_line_comment = False
            index += 1
            continue

        if in_block_comment:
            if char == "*" and index + 1 < len(text) and text[index + 1] == "/":
                in_block_comment = False
                index += 2
            else:
                index += 1
            continue

        if in_regex:
            if char == "\\" and index + 1 < len(text):
                index += 2
                continue
            if char == "/":
                in_regex = False
            index += 1
            continue

        if char == "'" and not (in_double_quote or in_template_quote):
            in_single_quote = True
        elif char == '"' and not (in_single_quote or in_template_quote):
            in_double_quote = True
        elif char == "`" and not (in_single_quote or in_double_quote):
            in_template_quote = True
        elif char == "/" and index + 1 < len(text):
            if text[index + 1] == "/":
                in_line_comment = True
                index += 1
            elif text[index + 1] == "*":
                in_block_comment = True
                index += 1
            else:
                next_non_ws = index + 1
                while next_non_ws < len(text) and text[next_non_ws].isspace():
                    next_non_ws += 1
                if next_non_ws >= len(text) or text[next_non_ws] in "({[,=:+-*/":
                    in_regex = True

        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1 : index].replace("\r\n", "\n")

        index += 1

    raise ValueError(f"Apps Script function body not closed: {function_name}")


def apps_script_function_body(function_name: str) -> str:
    text = read_text(APPS_SCRIPT)
    return extract_gas_function_body(text, function_name)


def require_text(body: str, expected: str, errors: list[str], message: str) -> None:
    if expected not in body:
        errors.append(message)


def require_regex(body: str, pattern: str, errors: list[str], message: str) -> None:
    if not re.search(pattern, body, re.S):
        errors.append(message)


def validate_trigger_spacing(errors: list[str]) -> None:
    for day in sorted(ALL_DAYS):
        day_items = [
            (name, minutes)
            for name, days, minutes in SCHEDULED_WORKFLOW_DISPATCHES
            if day in days
        ]
        day_items.sort(key=lambda item: item[1])
        for (left_name, left_minutes), (right_name, right_minutes) in zip(day_items, day_items[1:]):
            spacing = right_minutes - left_minutes
            if spacing < MIN_TRIGGER_SPACING_MINUTES:
                errors.append(
                    "Apps Script scheduled workflow dispatches are too close: "
                    f"day={day} {left_name}->{right_name} spacing_minutes={spacing} "
                    f"minimum={MIN_TRIGGER_SPACING_MINUTES}"
                )


def validate_tdcc_individual_refresh_orchestration(errors: list[str]) -> None:
    try:
        tdcc_trigger_body = apps_script_function_body("triggerTdccWeeklyReport")
        orchestrator_body = apps_script_function_body("orchestrateTdccIndividualRefresh")
        evidence_body = apps_script_function_body("readTdccPublishedEvidence_")
        downstream_evidence_body = apps_script_function_body(
            "readWorkflowOutputEvidence_"
        )
        chain_identity_body = apps_script_function_body("tdccChainIdentity_")
        dispatch_history_body = apps_script_function_body(
            "tdccDispatchAlreadyRecorded_"
        )
        run_correlation_body = apps_script_function_body("findCorrelatedWorkflowRuns_")
        active_installer_body = apps_script_function_body("installTdccActivePollTrigger_")
        retry_installer_body = apps_script_function_body("installTdccDataRetryTrigger_")
        cleanup_body = apps_script_function_body(
            "removeTdccIndividualRefreshOrchestratorTriggers_"
        )
        recovery_installer_body = apps_script_function_body(
            "installTdccIndividualRefreshOrchestratorTrigger"
        )
        failure_body = apps_script_function_body("failTdccChain_")
        install_all_body = apps_script_function_body("installAllWorkflowTriggers")
        retry_detector_body = apps_script_function_body("isRetryableTdccDataFailure_")
        retry_scheduler_body = apps_script_function_body("scheduleTdccDataRetry_")
        retry_dispatch_body = apps_script_function_body("dispatchScheduledTdccRetry_")
        initial_dispatch_body = apps_script_function_body("triggerTdccWeeklyReport")
    except ValueError as exc:
        errors.append(str(exc))
        return

    tdcc_trigger_requirements = {
        "withScriptLock_": "TDCC dispatch must use a script lock",
        "tdcc_baseline_run_id": "TDCC dispatch must record the prior run id",
        "tdcc_dispatched_at": "TDCC dispatch must record its dispatch timestamp",
        "tdcc_base_main_sha": "TDCC dispatch must record the main SHA before dispatch",
        "installTdccActivePollTrigger_()": "TDCC dispatch must start the temporary five-minute poller",
        "dispatchWorkflow_(TDCC_WEEKLY_WORKFLOW,": "TDCC dispatch must use the external Apps Script dispatcher",
    }
    for snippet, message in tdcc_trigger_requirements.items():
        require_text(tdcc_trigger_body, snippet, errors, message)
    if "Utilities.sleep" in tdcc_trigger_body:
        errors.append("TDCC chain must not use a fixed sleep as completion evidence")

    orchestration_requirements = {
        "getWorkflowRun_(state.tdcc_run_id)": "TDCC chain must read the tracked upstream run",
        'tdccRun.conclusion !== "success"': "TDCC chain must require upstream conclusion=success",
        "readTdccPublishedEvidence_(tdccRun)": "TDCC chain must verify published main evidence",
        "mainEvidenceWindowExpired_(tdccRun.updated_at)": "TDCC chain must bound main-evidence waiting",
        "tdccDispatchAlreadyRecorded_": "TDCC chain must enforce persistent dispatch idempotency",
        "state.chain_key": "TDCC chain must persist a run/signal-date chain key",
        "state.signal_date": "TDCC chain must track the TDCC signal date",
        "dispatchWorkflow_(INDIVIDUAL_REFRESH_WORKFLOW)": "TDCC chain must dispatch individual refresh externally",
        "state.downstream_baseline_run_id": "TDCC chain must record the prior downstream run id",
        "state.downstream_run_id": "TDCC chain must track the downstream run id",
        "state.tdcc_output_commit_sha": "TDCC chain must require the TDCC output commit in the downstream head",
        "readWorkflowOutputEvidence_": "TDCC chain must verify downstream outputs reached main",
        "mainEvidenceWindowExpired_(downstreamRun.updated_at)": "Downstream main evidence must use a bounded wait",
        'state.phase = "downstream_main_pending"': "Transient downstream main-evidence misses must remain retryable",
        "isRetryableTdccDataFailure_(tdccRun.id)": "TDCC data/readiness failures must be identified for automatic retry",
        "scheduleTdccDataRetry_(state, tdccRun)": "TDCC data/readiness failures must enter retry wait instead of terminal failure",
        'state.phase === "tdcc_data_retry_wait"': "TDCC orchestrator must resume scheduled data retries",
        "dispatchScheduledTdccRetry_(state)": "TDCC orchestrator must redispatch scheduled data retries",
        "removeTdccIndividualRefreshOrchestratorTriggers_()": "TDCC orchestrator must stop temporary triggers in idle or terminal states",
    }
    for snippet, message in orchestration_requirements.items():
        require_text(orchestrator_body, snippet, errors, message)

    for snippet, message in {
        "runId": "TDCC chain identity must include the upstream run id",
        "signalDate": "TDCC chain identity must include the official signal date",
        "outputCommitSha": "TDCC chain identity must include the TDCC output commit",
        '.join(":")': "TDCC chain identity must be deterministic",
    }.items():
        require_text(chain_identity_body, snippet, errors, message)
    for snippet, message in {
        "tdccChainIdentity_(runId, signalDate, outputCommitSha)": "Dispatch duplicate checks must use the exact chain identity",
        "item.chain_key === chainKey": "Dispatch duplicate checks must reject only the exact recorded chain",
    }.items():
        require_text(dispatch_history_body, snippet, errors, message)
    if "||" in dispatch_history_body:
        errors.append(
            "Dispatch duplicate checks must not OR-gate run id or signal_date independently"
        )

    evidence_requirements = {
        "TDCC_RUN_STATUS_PATH": "TDCC main gate must read the run status artifact",
        "TDCC_VALIDATION_PATH": "TDCC main gate must read the validation artifact",
        'validation.status !== "pass"': "TDCC main gate must require validation status=pass",
        "validation.signal_date": "TDCC main gate must read signal_date",
        "validation.date_contract.date_source": "TDCC main gate must enforce the registered date source",
        "TDCC_OFFICIAL_DATE_SOURCE": "TDCC main gate must use the official TDCC date source constant",
        "tdccRun.head_sha": "TDCC main gate must bind evidence to the upstream head SHA",
        "getLatestCommitForPath_": "TDCC main gate must identify the TDCC output commit",
        "getMainRefSha_": "TDCC main gate must read the live main SHA",
        "assertCommitContained_": "TDCC main gate must prove commit ancestry",
    }
    for snippet, message in evidence_requirements.items():
        require_text(evidence_body, snippet, errors, message)

    downstream_evidence_requirements = {
        "getRepositoryTextFile_(runStatusPath": "Downstream gate must read its workflow-owned run-status artifact",
        "runStatus.github_run_id": "Downstream gate must match the tracked run id",
        "runStatus.github_head_sha": "Downstream gate must match the tracked head SHA",
        "runStatus.official_signal_date": "Downstream gate must match the official signal date",
        "runStatus.date_contract.date_source": "Downstream gate must enforce the registered date source",
        "getLatestCommitForPath_(runStatusPath)": "Downstream gate must resolve the run-status output commit",
        "assertCommitContained_": "Downstream gate must prove run-status commit ancestry",
    }
    for snippet, message in downstream_evidence_requirements.items():
        require_text(downstream_evidence_body, snippet, errors, message)

    correlation_requirements = {
        "baselineRunId": "Run correlation must use a baseline run id",
        "dispatchedAt": "Run correlation must use the dispatch timestamp",
        'run.event === "workflow_dispatch"': "Run correlation must require workflow_dispatch",
        "run.head_branch === GITHUB_REF": "Run correlation must require the main branch",
        "TDCC_CHAIN_CORRELATION_WINDOW_MS": "Run correlation must use a bounded window",
    }
    for snippet, message in correlation_requirements.items():
        require_text(run_correlation_body, snippet, errors, message)

    for snippet in [
        'ScriptApp.newTrigger("orchestrateTdccIndividualRefresh")',
        ".timeBased()",
        ".everyMinutes(TDCC_CHAIN_POLL_MINUTES)",
    ]:
        require_text(
            active_installer_body,
            snippet,
            errors,
            f"Active TDCC orchestrator trigger must poll every {TDCC_CHAIN_POLL_MINUTES} minutes",
        )
    for snippet, message in {
        'ScriptApp.newTrigger("resumeTdccIndividualRefreshRetry")': "TDCC data wait must use a dedicated one-time retry handler",
        ".timeBased()": "TDCC data retry must use a time-driven trigger",
        ".at(retryAt)": "TDCC data retry must schedule exactly at next_retry_at",
        'removeTriggersForFunction_("orchestrateTdccIndividualRefresh")': "TDCC data retry scheduling must remove the five-minute poller",
    }.items():
        require_text(retry_installer_body, snippet, errors, message)
    if ".everyMinutes(" in retry_installer_body:
        errors.append("TDCC data retry trigger must not continue five-minute polling")
    for snippet in [
        'removeTriggersForFunction_("orchestrateTdccIndividualRefresh")',
        'removeTriggersForFunction_("resumeTdccIndividualRefreshRetry")',
    ]:
        require_text(
            cleanup_body,
            snippet,
            errors,
            "TDCC temporary-trigger cleanup must remove active and data-retry handlers",
        )
    for snippet, message in {
        "readTdccChainState_()": "Manual TDCC trigger repair must inspect persisted chain state",
        "isTerminalTdccChainPhase_(state.phase)": "Manual TDCC trigger repair must not install an idle terminal poller",
        "installTdccDataRetryTrigger_(state.next_retry_at)": "Manual TDCC trigger repair must restore one-time data waiting",
        "installTdccActivePollTrigger_()": "Manual TDCC trigger repair must restore active polling",
    }.items():
        require_text(recovery_installer_body, snippet, errors, message)
    for snippet, message in {
        "if (state.chain_key)": "Terminal TDCC failures with a chain identity must remain auditable",
        "recordTdccDispatch_(state)": "Terminal TDCC failures must update dispatch history",
        "removeTdccIndividualRefreshOrchestratorTriggers_()": "Terminal TDCC chain failures must remove temporary triggers",
    }.items():
        require_text(failure_body, snippet, errors, message)
    require_text(
        install_all_body,
        "removeTdccIndividualRefreshOrchestratorTriggers_();",
        errors,
        "installAllWorkflowTriggers must remove stale TDCC pollers instead of installing an idle poller",
    )
    if "installTdccActivePollTrigger_();" in install_all_body:
        errors.append("installAllWorkflowTriggers must not install a permanent five-minute TDCC poller")

    apps_script_text = read_text(APPS_SCRIPT)
    for snippet, message in {
        "PropertiesService.getScriptProperties()": "TDCC chain state must persist in Script Properties",
        "LockService.getScriptLock()": "TDCC chain must serialize concurrent trigger executions",
        "TDCC_CHAIN_DISPATCH_HISTORY_PROPERTY": "TDCC chain must persist dispatch history",
        "TDCC_CHAIN_MAIN_EVIDENCE_WINDOW_MS": "TDCC chain must not remain active forever while main evidence is missing",
        "TDCC_DATA_RETRY_DELAY_MS": "TDCC data retry must use an explicit retry interval",
        "TDCC_RETRYABLE_DATA_STEPS": "TDCC retry must be limited to named data/readiness steps",
    }.items():
        require_text(apps_script_text, snippet, errors, message)

    for snippet, message in {
        "failedWorkflowStepNames_(runId)": "TDCC retry classification must inspect failed workflow steps",
        "failedSteps.length > 0 && failedSteps.every": "TDCC retry classification must require every failed step to be retryable",
        "TDCC_RETRYABLE_DATA_STEPS.indexOf(stepName)": "TDCC retry classification must use the allowlisted data steps",
    }.items():
        require_text(retry_detector_body, snippet, errors, message)
    for snippet, message in {
        'state.phase = "tdcc_data_retry_wait"': "Retry scheduling must persist a nonterminal wait phase",
        "state.next_retry_at": "Retry scheduling must persist the next retry time",
        "TDCC_DATA_RETRY_DELAY_MS": "Retry scheduling must use the configured delay",
        "installTdccDataRetryTrigger_(state.next_retry_at)": "Retry scheduling must switch to a one-time 30-minute trigger",
    }.items():
        require_text(retry_scheduler_body, snippet, errors, message)
    for snippet, message in {
        "latestWorkflowRunId_(TDCC_WEEKLY_WORKFLOW)": "Retry dispatch must refresh the run correlation baseline",
        "dispatchWorkflow_(TDCC_WEEKLY_WORKFLOW,": "Retry dispatch must use the external Apps Script dispatcher",
        "target_as_of_date: state.target_as_of_date": "Retry dispatch must preserve the original target report week",
        'state.phase = "tdcc_dispatched"': "Retry dispatch must return to the normal correlation phase",
        "installTdccActivePollTrigger_()": "Retry dispatch must resume temporary five-minute active polling",
    }.items():
        require_text(retry_dispatch_body, snippet, errors, message)
    for snippet, message in {
        "target_as_of_date: taipeiYyyyMmDd_()": "Initial TDCC dispatch must pin the target report week",
        "target_as_of_date: state.target_as_of_date": "Initial TDCC dispatch must send the pinned target date",
    }.items():
        require_text(initial_dispatch_body, snippet, errors, message)

    tdcc_workflow_text = read_text(WORKFLOW_DIR / TDCC_WORKFLOW)
    for snippet, message in {
        "target_as_of_date:": "TDCC workflow must declare the pinned target date input",
        'args+=(--as-of-date "${{ github.event.inputs.target_as_of_date }}")': "TDCC readiness step must consume the pinned target date",
        "python tdcc_holder_ratio_top10.py --fetch-only --use-existing-readiness": "TDCC fetch step must preserve the pinned same-run readiness artifact",
    }.items():
        require_text(tdcc_workflow_text, snippet, errors, message)

    forbidden_self_trigger_patterns = [
        r"\bworkflow_run\s*:",
        r"\brepository_dispatch\s*:",
        r"\bgh\s+workflow\s+run\b",
        r"\bcurl\b.*api\.github\.com",
        r"/actions/workflows/.*/dispatches",
    ]
    for workflow_file in [TDCC_WORKFLOW, INDIVIDUAL_REFRESH_WORKFLOW]:
        workflow_text = read_text(WORKFLOW_DIR / workflow_file)
        if not re.search(r"^on:\s*\n\s{2}workflow_dispatch:\s*$", workflow_text, re.M):
            errors.append(f"{workflow_file} must remain workflow_dispatch-only")
        for pattern in forbidden_self_trigger_patterns:
            if re.search(pattern, workflow_text, re.I | re.S):
                errors.append(
                    f"{workflow_file} contains forbidden in-repo self-trigger pattern: {pattern}"
                )

    individual_workflow_text = read_text(WORKFLOW_DIR / INDIVIDUAL_REFRESH_WORKFLOW)
    run_status_requirements = {
        "Write individual stock refresh run status": "Individual refresh workflow must write run-status evidence",
        'os.environ["GITHUB_RUN_ID"]': "Individual refresh run status must record GITHUB_RUN_ID",
        'os.environ["GITHUB_SHA"]': "Individual refresh run status must record GITHUB_SHA",
        '"official_signal_date": signal_date': "Individual refresh run status must record official signal_date",
        'expected_date_source = "report_ready_csv_signal_date"': "Individual refresh run status must enforce the official date source",
        "individual_stock_refresh_run_status_latest.json": "Individual refresh workflow must write the canonical run-status path",
        "git add output/latest/individual_stock_reports/": "Individual refresh commit must stage the output run-status artifact",
        "git add docs/latest/individual_stock_reports/": "Individual refresh commit must stage the docs run-status mirror",
    }
    for snippet, message in run_status_requirements.items():
        require_text(individual_workflow_text, snippet, errors, message)
    step_order = [
        "Build individual stock packets and windows",
        "Write individual stock refresh run status",
        "Commit individual stock refresh outputs",
    ]
    step_positions = [individual_workflow_text.find(step) for step in step_order]
    if any(position < 0 for position in step_positions) or step_positions != sorted(step_positions):
        errors.append(
            "Individual refresh run-status must be written after builder/validator and before the output commit"
        )


def main() -> int:
    errors: list[str] = []
    dispatches = apps_script_dispatches()
    functions = apps_script_functions()

    missing_dispatches = EXPECTED_DISPATCHES - set(dispatches)
    if missing_dispatches:
        errors.append(f"Apps Script missing workflow dispatches: {sorted(missing_dispatches)}")

    for workflow in sorted(EXPECTED_DISPATCHES):
        if not (WORKFLOW_DIR / workflow).exists():
            errors.append(f"Workflow file missing: {workflow}")

    research_workflow = "research_backtest_pipeline.yml"
    research_inputs = workflow_inputs(research_workflow)
    apps_inputs = set(dispatches.get(research_workflow, {}))
    missing_inputs = research_inputs - apps_inputs
    extra_inputs = apps_inputs - research_inputs
    if missing_inputs:
        errors.append(f"Apps Script research dispatch missing inputs: {sorted(missing_inputs)}")
    if extra_inputs:
        errors.append(f"Apps Script research dispatch has unknown inputs: {sorted(extra_inputs)}")

    daily_workflow = "daily_full_pipeline.yml"
    daily_expected_false_inputs = {
        "run_raw_health_check",
    }
    daily_inputs = dispatches.get(daily_workflow, {})
    missing_daily_inputs = daily_expected_false_inputs - set(daily_inputs)
    bad_daily_values = {
        key: value
        for key, value in daily_inputs.items()
        if key in daily_expected_false_inputs and value != "false"
    }
    if missing_daily_inputs:
        errors.append(f"Apps Script daily dispatch missing false inputs: {sorted(missing_daily_inputs)}")
    if bad_daily_values:
        errors.append(f"Apps Script daily dispatch inputs must be false: {bad_daily_values}")

    repair_workflow = "repair_recent_daily_price_gaps.yml"
    repair_expected_inputs = {
        "lookback_days": "7",
        "max_repair_dates": "5",
    }
    repair_inputs = dispatches.get(repair_workflow, {})
    missing_repair_inputs = set(repair_expected_inputs) - set(repair_inputs)
    bad_repair_values = {
        key: value
        for key, value in repair_inputs.items()
        if key in repair_expected_inputs and value != repair_expected_inputs[key]
    }
    if missing_repair_inputs:
        errors.append(f"Apps Script daily price gap repair dispatch missing inputs: {sorted(missing_repair_inputs)}")
    if bad_repair_values:
        errors.append(f"Apps Script daily price gap repair inputs have unexpected values: {bad_repair_values}")

    tdcc_repair_workflow = "repair_tdcc_monthly_history_gaps.yml"
    tdcc_repair_expected_inputs = {
        "universe": "chatgpt-top",
        "max_stocks": "80",
        "max_requests": "500",
        "rebuild_max_dates": "4",
    }
    tdcc_repair_inputs = dispatches.get(tdcc_repair_workflow, {})
    missing_tdcc_repair_inputs = set(tdcc_repair_expected_inputs) - set(tdcc_repair_inputs)
    bad_tdcc_repair_values = {
        key: value
        for key, value in tdcc_repair_inputs.items()
        if key in tdcc_repair_expected_inputs and value != tdcc_repair_expected_inputs[key]
    }
    if missing_tdcc_repair_inputs:
        errors.append(f"Apps Script TDCC history gap repair dispatch missing inputs: {sorted(missing_tdcc_repair_inputs)}")
    if bad_tdcc_repair_values:
        errors.append(f"Apps Script TDCC history gap repair inputs have unexpected values: {bad_tdcc_repair_values}")

    try:
        daily_trigger_body = apps_script_function_body("triggerDailyStockMonitor")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if not re.search(r"dayOfWeek\s*===\s*0\s*\|\|\s*dayOfWeek\s*===\s*6", daily_trigger_body):
            errors.append("Apps Script daily trigger must skip Saturday and Sunday")
        if not re.search(
            r'dispatchWorkflow_\("daily_full_pipeline\.yml",\s*\{\s*run_raw_health_check:\s*"false"',
            daily_trigger_body,
            re.S,
        ):
            errors.append("Apps Script daily trigger must dispatch daily_full_pipeline with run_raw_health_check=false")

    try:
        repair_trigger_body = apps_script_function_body("triggerDailyPriceGapRepair")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if not re.search(r"dayOfWeek\s*===\s*0\s*\|\|\s*dayOfWeek\s*===\s*6", repair_trigger_body):
            errors.append("Apps Script daily price gap repair trigger must skip Saturday and Sunday")
        if 'dispatchWorkflow_("repair_recent_daily_price_gaps.yml", {' not in repair_trigger_body:
            errors.append("Apps Script daily price gap repair trigger must dispatch repair_recent_daily_price_gaps.yml")
        if 'lookback_days: "7"' not in repair_trigger_body:
            errors.append("Apps Script daily price gap repair trigger must use lookback_days=7")
        if 'max_repair_dates: "5"' not in repair_trigger_body:
            errors.append("Apps Script daily price gap repair trigger must use max_repair_dates=5")

    try:
        tdcc_repair_trigger_body = apps_script_function_body("triggerTdccHistoryGapRepair")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if 'dispatchWorkflow_("repair_tdcc_monthly_history_gaps.yml", {' not in tdcc_repair_trigger_body:
            errors.append("Apps Script TDCC history gap repair trigger must dispatch repair_tdcc_monthly_history_gaps.yml")
        for key, expected_value in tdcc_repair_expected_inputs.items():
            if f'{key}: "{expected_value}"' not in tdcc_repair_trigger_body:
                errors.append(f"Apps Script TDCC history gap repair trigger must use {key}={expected_value}")

    try:
        evening_recovery_body = apps_script_function_body(
            "maybeRecoverEveningDataOnlyRunFromState_"
        )
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if "identity_mismatch" not in evening_recovery_body:
            errors.append(
                "Evening data-only run recovery must classify identity mismatch when state correlation identity contract fails"
            )
        if "dispatch_correlation_id" not in evening_recovery_body:
            errors.append(
                "Evening data-only run recovery must require persisted dispatch_correlation_id for identity contract checks"
            )
        if "expected_run_display_title" not in evening_recovery_body:
            errors.append(
                "Evening data-only run recovery must persist and validate expected_run_display_title for identity"
            )
        if "buildEveningDataOnlyRunDisplayTitle_" not in evening_recovery_body:
            errors.append(
                "Evening data-only run recovery must validate dispatch correlation token against expected run title contract"
            )
        if "isEveningDataOnlyRunMatchedByDisplayTitle_" not in evening_recovery_body:
            errors.append(
                "Evening data-only run recovery must compare workflow run display title for identity validation"
            )

    try:
        evening_trigger_body = apps_script_function_body("triggerEveningDataOnlyRepair")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if not re.search(r"dayOfWeek\s*===\s*0\s*\|\|\s*dayOfWeek\s*===\s*6", evening_trigger_body):
            errors.append("Evening data-only repair trigger must skip Saturday and Sunday")
        if "readEveningDataOnlyMarketSession_" not in evening_trigger_body:
            errors.append(
                "Evening data-only repair trigger must read market session evidence before deciding dispatch"
            )
        if 'isMarketSessionClosed_(targetDate, marketSession)' not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must use closed-market guard")
        if "withScriptLock_(function ()" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must lock decision and dispatch critical section")
        dispatch_call_pos = evening_trigger_body.find('dispatchWorkflow_(EVENING_DATA_ONLY_WORKFLOW, {')
        write_state_positions = [
            evening_trigger_body.find('writeEveningDataOnlyRepairState_(currentState);'),
            evening_trigger_body.find('writeEveningDataOnlyRepairState_(stateForDispatch);'),
            evening_trigger_body.find('writeEveningDataOnlyRepairState_(stateForDispatch'),
        ]
        if dispatch_call_pos >= 0 and any(position >= 0 for position in write_state_positions):
            if not any(
                state_write_position >= 0 and state_write_position < dispatch_call_pos
                for state_write_position in write_state_positions
            ):
                errors.append(
                    "Evening data-only repair trigger must persist dispatching state before posting workflow_dispatch"
                )
        elif dispatch_call_pos >= 0:
            errors.append(
                "Evening data-only repair trigger must persist dispatching state before posting workflow_dispatch"
            )
        if (
            'currentState.phase = "dispatching"' not in evening_trigger_body
            and 'stateForDispatch.phase = "dispatching"' not in evening_trigger_body
            and 'phase: "dispatching"' not in evening_trigger_body
        ):
            errors.append("Evening data-only repair trigger must set phase=dispatching before POST")
        if 'dispatchWorkflow_(EVENING_DATA_ONLY_WORKFLOW, {' not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must dispatch repair_recent_daily_price_gaps.yml")
        if 'lookback_days: "7"' not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must use lookback_days=7")
        if 'max_repair_dates: "5"' not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must use max_repair_dates=5")
        if 'dispatchWorkflow_(EVENING_DATA_ONLY_WORKFLOW' not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must dispatch through the data-only workflow constant")
        if "dispatch_correlation_id:" not in evening_trigger_body:
            errors.append(
                "Evening data-only repair trigger must include dispatch_correlation_id input for identity correlation"
            )
        if "findCorrelatedWorkflowRuns_(" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must validate dispatch response run correlation")
        if "correlatedRuns.length === 0" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must fail when no correlated workflow run is found")
        if "correlatedRuns.length > 1" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must fail when multiple correlated workflow runs are found")
        if "readEveningDataOnlyRepairState_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must persist state for in-flight and guard")
        if "writeEveningDataOnlyRepairState_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must persist state updates")
        if "recordEveningDataOnlyRepairDispatch_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must record dispatch evidence for audit")
        if (
            "currentState.workflow_main_sha" not in evening_trigger_body
            and "stateForDispatch.workflow_main_sha" not in evening_trigger_body
        ):
            errors.append("Evening data-only repair trigger must persist dispatch-time main SHA for correlation")
        if "correlationWindowExpired_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must guard duplicate dispatch before correlation window expires")
        if "dispatch_uncertain" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must expose dispatch_uncertain reconciliation state")
        if not re.search(
            r"findCorrelatedWorkflowRuns_\(\s*EVENING_DATA_ONLY_WORKFLOW,\s*.*,\s*.*,\s*(stateForDispatch|currentState)\.workflow_main_sha",
            evening_trigger_body,
            re.S,
        ):
            errors.append(
                "Evening data-only repair trigger must correlate dispatch response using current-state main SHA"
            )
        if "isEveningDataOnlyRunMatchedByHeadSha_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must validate correlated run head SHA")
        if "isEveningDataOnlyRunInFlight_" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must account for correlated run in-flight")
        if "dispatch_uncertain" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must track dispatch_uncertain outcome")
        if "max_attempts_exceeded" not in evening_trigger_body:
            errors.append("Evening data-only repair trigger must fail closed after bounded retry attempts")
        if 'dispatch_failed' in evening_trigger_body:
            errors.append("Evening data-only repair trigger must not use dispatch_failed phase")

    try:
        market_session_body = apps_script_function_body("isMarketSessionClosed_")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if "closed_scheduled" not in market_session_body or "closed_emergency" not in market_session_body:
            errors.append(
                "Evening market session guard must only treat closed_scheduled/closed_emergency as closed"
            )
        if "assessment_date" not in market_session_body:
            errors.append(
                "Evening market session guard must require assessment_date to match target date"
            )

    fixture_path = ROOT / "tests" / "fixtures" / "evening_data_only_early_gas_hashes.json"
    try:
        expected_hashes = json.loads(fixture_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Unable to load morning gas hash fixture: {exc}")
    else:
        for function_name, expected_hash in expected_hashes.items():
            try:
                function_body = apps_script_function_body(function_name)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            actual_hash = hashlib.sha256(function_body.encode("utf-8")).hexdigest()
            if actual_hash != expected_hash:
                errors.append(
                    f"Apps Script function hash drift for {function_name}: {actual_hash} != {expected_hash}"
                )

    try:
        tdcc_repair_install_body = apps_script_function_body("installTdccHistoryGapRepairTrigger_")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if "ScriptApp.WeekDay.TUESDAY" not in tdcc_repair_install_body:
            errors.append("Apps Script TDCC history gap repair trigger must run on Tuesday")
        if ".atHour(9)" not in tdcc_repair_install_body:
            errors.append("Apps Script TDCC history gap repair trigger must run at hour 9 Asia/Taipei")
        if ".nearMinute(30)" not in tdcc_repair_install_body:
            errors.append("Apps Script TDCC history gap repair trigger must run near minute 30 Asia/Taipei")

    trigger_time_expectations = {
        "installDailyStockMonitorTrigger_": (
            [".everyDays(1)", ".atHour(19)", ".nearMinute(30)"],
            "Apps Script daily stock monitor trigger must run daily at 19:30 Asia/Taipei",
        ),
        "installDailyPriceGapRepairTrigger_": (
            [".everyDays(1)", ".atHour(10)", ".nearMinute(30)"],
            "Apps Script daily price gap repair trigger must run daily at 10:30 Asia/Taipei",
        ),
        "installEveningDataOnlyRepairTrigger_": (
            [".everyDays(1)", ".atHour(20)", ".nearMinute(30)"],
            "Apps Script evening data-only repair trigger must run daily at 20:30 Asia/Taipei",
        ),
        "installIndividualStockDataRefreshTrigger_": (
            [".everyDays(1)", ".atHour(22)", ".nearMinute(20)"],
            "Apps Script individual stock data refresh trigger must run daily at 22:20 Asia/Taipei",
        ),
        "installTdccWeeklyReportTrigger_": (
            ["ScriptApp.WeekDay.SATURDAY", ".atHour(15)", ".nearMinute(30)"],
            "Apps Script TDCC weekly report trigger must run Saturday at 15:30 Asia/Taipei",
        ),
        "installWeeklyThemeReviewTrigger_": (
            ["ScriptApp.WeekDay.SUNDAY", ".atHour(19)", ".nearMinute(30)"],
            "Apps Script weekly theme review trigger must run Sunday at 19:30 Asia/Taipei",
        ),
        "installBiweeklyResearchBacktestTrigger": (
            [".everyWeeks(2)", "ScriptApp.WeekDay.SUNDAY", ".atHour(21)", ".nearMinute(10)"],
            "Apps Script research/backtest trigger must run every 2 weeks Sunday at 21:10 Asia/Taipei",
        ),
    }
    for function_name, (expected_snippets, message) in trigger_time_expectations.items():
        try:
            install_body = apps_script_function_body(function_name)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        for expected_snippet in expected_snippets:
            require_text(install_body, expected_snippet, errors, message)

    try:
        event_install_body = apps_script_function_body("installEventCatalystUpdateTriggers_")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        require_regex(
            event_install_body,
            r"\.everyDays\(1\).*?\.atHour\(8\).*?\.nearMinute\(10\).*?\.everyDays\(1\).*?\.atHour\(18\).*?\.nearMinute\(10\)",
            errors,
            "Apps Script event catalyst update triggers must run daily at 08:10 and 18:10 Asia/Taipei",
        )

    try:
        install_all_body = apps_script_function_body("installAllWorkflowTriggers")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if "installEveningDataOnlyRepairTrigger_()" in install_all_body:
            errors.append("installAllWorkflowTriggers must not auto-install evening data-only repair trigger")

    validate_trigger_spacing(errors)
    validate_tdcc_individual_refresh_orchestration(errors)

    research_text = read_text(WORKFLOW_DIR / research_workflow)
    forbidden_research_auto_commit_patterns = [
        r"git add\s+scripts/",
        r"git add\s+\.github/workflows/",
        r"git add\s+\.github\\workflows\\",
    ]
    for pattern in forbidden_research_auto_commit_patterns:
        if re.search(pattern, research_text):
            errors.append(
                "Research workflow must not auto-stage code/workflow files during output commits: "
                f"{pattern}"
            )

    required_functions = {
        "triggerDailyStockMonitor",
        "triggerDailyFullPipeline",
        "triggerDailyPriceGapRepair",
        "triggerEveningDataOnlyRepair",
        "triggerTdccHistoryGapRepair",
        "triggerIndividualStockDataRefresh",
        "triggerTdccWeeklyReport",
        "orchestrateTdccIndividualRefresh",
        "resumeTdccIndividualRefreshRetry",
        "diagnoseTdccIndividualRefreshOrchestration",
        "triggerEventCatalystUpdate",
        "triggerWeeklyThemeReview",
        "triggerResearchBacktestPipeline",
        "diagnoseDailyStockMonitorTrigger",
        "diagnoseDailyPriceGapRepairTrigger",
        "diagnoseTdccHistoryGapRepairTrigger",
        "installDailyStockMonitorTrigger",
        "installDailyPriceGapRepairTrigger",
        "installEveningDataOnlyRepairTrigger",
        "installTdccHistoryGapRepairTrigger",
        "removeDailyStockMonitorTrigger",
        "removeDailyPriceGapRepairTrigger",
        "removeEveningDataOnlyRepairTrigger",
        "removeTdccHistoryGapRepairTrigger",
        "installAllWorkflowTriggers",
        "installTdccIndividualRefreshOrchestratorTrigger",
        "removeTdccIndividualRefreshOrchestratorTrigger",
        "installTdccActivePollTrigger_",
        "installTdccDataRetryTrigger_",
        "removeTdccIndividualRefreshOrchestratorTriggers_",
        "installDailyPriceGapRepairTrigger_",
        "installTdccHistoryGapRepairTrigger_",
        "installEveningDataOnlyRepairTrigger_",
        "installIndividualStockDataRefreshTrigger_",
        "installBiweeklyResearchBacktestTrigger",
        "listAllTriggers",
    }
    missing_functions = required_functions - functions
    if missing_functions:
        errors.append(f"Apps Script missing functions: {sorted(missing_functions)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("apps_script_workflow_trigger validation passed")
    print(f"validated_dispatches={sorted(dispatches)}")
    print(f"research_inputs={sorted(research_inputs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
