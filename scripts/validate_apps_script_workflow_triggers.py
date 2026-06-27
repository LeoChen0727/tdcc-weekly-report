from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APPS_SCRIPT = ROOT / "docs" / "apps_script_workflow_trigger.gs"
WORKFLOW_DIR = ROOT / ".github" / "workflows"

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


def apps_script_dispatches() -> dict[str, dict[str, str]]:
    text = read_text(APPS_SCRIPT)
    dispatches: dict[str, dict[str, str]] = {}
    pattern = re.compile(
        r'dispatchWorkflow_\("(?P<workflow>[^"]+)"(?:,\s*\{(?P<inputs>.*?)\})?\);',
        re.S,
    )
    for match in pattern.finditer(text):
        workflow = match.group("workflow")
        inputs_body = match.group("inputs") or ""
        inputs = dict(
            re.findall(r'^\s*([A-Za-z0-9_]+)\s*:\s*"([^"]*)"', inputs_body, re.M)
        )
        dispatches[workflow] = inputs
    return dispatches


def apps_script_functions() -> set[str]:
    text = read_text(APPS_SCRIPT)
    return set(re.findall(r"^function\s+([A-Za-z0-9_]+)\s*\(", text, re.M))


def apps_script_function_body(function_name: str) -> str:
    text = read_text(APPS_SCRIPT)
    match = re.search(
        rf"^function\s+{re.escape(function_name)}\s*\([^)]*\)\s*\{{(?P<body>.*?)(?:^}}\s*$)",
        text,
        re.M | re.S,
    )
    if not match:
        raise ValueError(f"Apps Script function not found: {function_name}")
    return match.group("body")


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
        tdcc_repair_install_body = apps_script_function_body("installTdccHistoryGapRepairTrigger_")
    except ValueError as exc:
        errors.append(str(exc))
    else:
        if "ScriptApp.WeekDay.TUESDAY" not in tdcc_repair_install_body:
            errors.append("Apps Script TDCC history gap repair trigger must run on Tuesday")
        if ".atHour(9)" not in tdcc_repair_install_body:
            errors.append("Apps Script TDCC history gap repair trigger must run at hour 9 Asia/Taipei")

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
        "triggerTdccHistoryGapRepair",
        "triggerIndividualStockDataRefresh",
        "triggerTdccWeeklyReport",
        "triggerEventCatalystUpdate",
        "triggerWeeklyThemeReview",
        "triggerResearchBacktestPipeline",
        "diagnoseDailyStockMonitorTrigger",
        "diagnoseDailyPriceGapRepairTrigger",
        "diagnoseTdccHistoryGapRepairTrigger",
        "installDailyStockMonitorTrigger",
        "installDailyPriceGapRepairTrigger",
        "installTdccHistoryGapRepairTrigger",
        "removeDailyStockMonitorTrigger",
        "removeDailyPriceGapRepairTrigger",
        "removeTdccHistoryGapRepairTrigger",
        "installAllWorkflowTriggers",
        "installDailyPriceGapRepairTrigger_",
        "installTdccHistoryGapRepairTrigger_",
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
