from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
from collections import defaultdict

import pytest

from scripts import stage_daily_latest_mirrors
from scripts import validate_apps_script_workflow_triggers
from scripts import validate_daily_production_boundaries as boundaries
from scripts import validate_daily_staged_paths
from scripts import validate_research_production_boundaries


ROOT = Path(__file__).resolve().parents[1]
BUNDLED_NODE = Path(r"C:\Users\p4693\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe")


def resolve_test_node() -> str:
    node = shutil.which("node")
    if node:
        return node
    assert BUNDLED_NODE.exists(), "Bundled Node.js is required to execute the Apps Script behavioral test"
    return str(BUNDLED_NODE)
DAILY_DECISION_LAYER_FIELDS = [
    "decision_priority",
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
]
DAILY_OPERATION_CONCLUSION_PHRASES = [
    "推薦可買",
    "可買候選",
    "買進條件",
    "不買條件",
    "目前不買",
    "條件式買進",
    "買進後",
    "先不買",
    "排除買進",
]


def _collect_workflow_validation_steps(file_path: Path) -> tuple[dict[str, list[int]], dict[str, list[int]]]:
    installs_by_job: dict[str, list[int]] = defaultdict(list)
    validator_steps_by_job: dict[str, list[int]] = defaultdict(list)

    lines = file_path.read_text(encoding="utf-8").splitlines()
    in_jobs_block = False
    in_steps_block = False
    current_job: str | None = None
    current_step_index = 0
    current_step_is_install = False

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        if line.startswith("jobs:"):
            in_jobs_block = True
            continue

        if in_jobs_block and line.startswith("  ") and not line.startswith("    "):
            if line.rstrip().endswith(":") and line.strip() != "jobs:":
                current_job = line.strip()[:-1]
                in_steps_block = False
            else:
                current_job = None
                in_steps_block = False
            continue

        if line.startswith("    steps:") and current_job is not None:
            in_steps_block = True
            continue

        if not in_steps_block or current_job is None:
            continue

        if line.startswith("      - name:"):
            current_step_index += 1
            current_step_is_install = line.split(":", 1)[1].strip() == "Install dependencies"
            continue

        if current_step_is_install and "pip install" in line:
            if current_step_index not in installs_by_job[current_job]:
                installs_by_job[current_job].append(current_step_index)

        if "python scripts/validate_daily_production_boundaries.py" in line:
            validator_steps_by_job[current_job].append(current_step_index)

    return installs_by_job, validator_steps_by_job


@pytest.mark.parametrize(
    "workflow_file",
    [
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/repair_recent_daily_price_gaps.yml",
    ],
)
def test_workflow_dependency_install_precedes_boundary_validator(
    workflow_file: str,
) -> None:
    workflow_path = ROOT / workflow_file
    installs_by_job, validator_steps_by_job = _collect_workflow_validation_steps(workflow_path)

    assert validator_steps_by_job, f"{workflow_path} missing validate_daily_production_boundaries.py"

    for job, validator_steps in validator_steps_by_job.items():
        for validator_step_index in validator_steps:
            install_before = [idx for idx in installs_by_job[job] if idx < validator_step_index]
            assert install_before, (
                f"{workflow_path} job={job}: no Install dependencies step before validator step "
                f"{validator_step_index}"
            )


def test_daily_production_boundary_validator_passes_current_repo() -> None:
    assert boundaries.main() == 0


def test_daily_operation_packet_uses_row_metric_contract_without_baseline_fallback() -> None:
    assert boundaries.validate_daily_operation_packet_row_metric_contract() == []


def test_research_production_boundary_validator_passes_current_repo() -> None:
    assert validate_research_production_boundaries.main() == 0


def test_apps_script_workflow_trigger_validator_passes_current_repo() -> None:
    assert validate_apps_script_workflow_triggers.main() == 0


def test_apps_script_research_dispatch_registry_is_forward_compatible() -> None:
    validator = validate_apps_script_workflow_triggers
    registry = validator.load_research_dispatch_registry()
    workflow_inputs = validator.workflow_inputs("research_backtest_pipeline.yml")
    apps_inputs, guarded_inputs = validator.apps_script_research_dispatch_inputs()
    staged_input = "run_revenue_unreacted_range_source_snapshot_projection_chain_only"

    assert registry[staged_input]["activation_mode"] == "when_declared"
    assert staged_input in workflow_inputs
    assert staged_input in apps_inputs
    assert guarded_inputs == {staged_input}

    errors: list[str] = []
    validator.validate_research_dispatch_contract(
        errors,
        workflow_input_names=workflow_inputs,
        apps_inputs=set(apps_inputs),
        guarded_inputs=guarded_inputs,
        registry=registry,
    )
    assert errors == []

    undeclared_errors: list[str] = []
    validator.validate_research_dispatch_contract(
        undeclared_errors,
        workflow_input_names=workflow_inputs - {staged_input},
        apps_inputs=set(apps_inputs),
        guarded_inputs=guarded_inputs,
        registry=registry,
    )
    assert undeclared_errors == []

    unknown_errors: list[str] = []
    validator.validate_research_dispatch_contract(
        unknown_errors,
        workflow_input_names={*workflow_inputs, "run_unregistered_research"},
        apps_inputs=set(apps_inputs),
        guarded_inputs=guarded_inputs,
        registry=registry,
    )
    assert any("unregistered Apps Script inputs" in error for error in unknown_errors)

    helper_body = validator.apps_script_function_body("researchBacktestInputs_")
    schema_body = validator.apps_script_function_body("workflowDispatchInputNames_")
    assert "if (!declaredInputs[inputName])" in helper_body
    assert "if (declaredInputs[inputName])" in helper_body
    assert 'githubJson_(\n    "get"' in schema_body
    assert 'payload.encoding !== "base64"' in schema_body


def test_apps_script_daily_trigger_skips_weekends_and_disables_raw_health_check() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerDailyStockMonitor"
    )

    assert "dayOfWeek === 0 || dayOfWeek === 6" in body
    assert 'dispatchWorkflow_("daily_full_pipeline.yml", {' in body
    assert 'run_raw_health_check: "false"' in body


def test_apps_script_recent_daily_price_gap_repair_trigger_is_weekday_only() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerDailyPriceGapRepair"
    )

    assert "dayOfWeek === 0 || dayOfWeek === 6" in body
    assert 'dispatchWorkflow_("repair_recent_daily_price_gaps.yml", {' in body
    assert 'lookback_days: "7"' in body
    assert 'max_repair_dates: "5"' in body


def test_apps_script_morning_handler_and_price_gap_install_remove_hashes_are_stable() -> None:
    fixture = (
        ROOT / "tests" / "fixtures" / "evening_data_only_early_gas_hashes.json"
    )
    expected_hashes = json.loads(fixture.read_text(encoding="utf-8"))
    actual_hashes = {
        function_name: hashlib.sha256(
            validate_apps_script_workflow_triggers.apps_script_function_body(function_name).encode(
                "utf-8"
            )
        ).hexdigest()
        for function_name in expected_hashes
    }

    assert actual_hashes == expected_hashes


def test_apps_script_evening_data_only_trigger_is_weekday_deterministic() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerEveningDataOnlyRepair"
    )

    assert "const dayOfWeek = currentWeekday_();" in body
    assert "new Date().getDay()" not in body


def test_apps_script_evening_data_only_repair_retry_and_reconciliation_behavior(
    tmp_path: Path,
) -> None:
    node = resolve_test_node()

    source = (ROOT / "docs" / "apps_script_workflow_trigger.gs").read_text(
        encoding="utf-8"
    )
    harness = r'''
const TARGET_DATE = "20260721";
const WORKFLOW = "repair_recent_daily_price_gaps.yml";
const BASE_SHA = "a".repeat(40);
const ALT_SHA = "b".repeat(40);
const START_TIME = new Date("2026-07-21T20:30:00.000Z").getTime();

let scriptProperties = {};
let dispatches = [];
let workflowRuns = {};
let correlationRuns = [];
let marketSessionProvider = function () { return { assessment_date: TARGET_DATE, market_status: "open" }; };
let dispatchError = null;
let nowCursorMs = START_TIME;
let mainShaValue = BASE_SHA;
let preflightMode = "";
let formatDateWeekdayOverride = null;
let historyPropertyFailureMode = "";
let correlationApiFailureMode = "";
let harnessUuidCounter = 0;

function setNow(iso) {
  nowCursorMs = new Date(iso).getTime();
}

function setCorrelationRuns(values) {
  correlationRuns = values.slice();
}

function setWorkflowRuns(values) {
  workflowRuns = {};
  Object.keys(values).forEach(function (runId) {
    workflowRuns[runId] = values[runId];
  });
}

function setHistoryPropertyFailureMode(mode) {
  historyPropertyFailureMode = mode || "";
}

function setCorrelationApiFailureMode(mode) {
  correlationApiFailureMode = mode || "";
}

  function setState(state) {
    if (!state) {
      delete scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY];
      return;
    }
    scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY] = JSON.stringify(state);
  }

  function setStateWithEveningIdentity(state) {
    if (!state) {
      setState(null);
      return;
    }
    const clone = JSON.parse(JSON.stringify(state));
    const attemptedCorrelationId = clone.dispatch_correlation_id == null ? null : String(clone.dispatch_correlation_id);
    const correlationId = attemptedCorrelationId != null ? attemptedCorrelationId : buildHarnessCorrelationId(Number(clone.attempt_count || 1));
    clone.dispatch_correlation_id = correlationId;
    clone.expected_run_display_title = buildEveningDataOnlyRunDisplayTitle_(correlationId);
    setState(clone);
  }

function setHistory(stateRows) {
  if (!stateRows) {
    delete scriptProperties[EVENING_DATA_ONLY_DISPATCH_HISTORY_PROPERTY];
    return;
  }
  scriptProperties[EVENING_DATA_ONLY_DISPATCH_HISTORY_PROPERTY] = JSON.stringify(stateRows);
}

function resetHarness() {
    scriptProperties = {};
    scriptProperties[GITHUB_PAT_PROPERTY] = "local-dev-token";
    scriptProperties[GITHUB_TOKEN_FALLBACK_PROPERTY] = "local-dev-token";
  dispatches = [];
  workflowRuns = {};
  correlationRuns = [];
  dispatchError = null;
  nowCursorMs = START_TIME;
  mainShaValue = BASE_SHA;
  preflightMode = "";
  formatDateWeekdayOverride = null;
  historyPropertyFailureMode = "";
  correlationApiFailureMode = "";
  harnessUuidCounter = 0;
  currentDate_ = function () { return new Date("2026-07-21T12:00:00.000Z"); };
  taipeiYyyyMmDd_ = function () { return TARGET_DATE; };
  marketSessionProvider = function () { return { assessment_date: TARGET_DATE, market_status: "open" }; };
  delete scriptProperties[EVENING_DATA_ONLY_DISPATCH_HISTORY_PROPERTY];
}

global.Date.now = function () { return nowCursorMs; };

global.PropertiesService = {
  getScriptProperties: function () {
    return {
      getProperty: function (key) {
        if (key === EVENING_DATA_ONLY_DISPATCH_HISTORY_PROPERTY) {
          if (historyPropertyFailureMode === "get") {
            throw new Error("simulated history property get failure");
          }
          if (historyPropertyFailureMode === "parse") {
            return "{not-json";
          }
        }
        return scriptProperties[key] || null;
      },
      setProperty: function (key, value) {
        if (key === EVENING_DATA_ONLY_DISPATCH_HISTORY_PROPERTY && historyPropertyFailureMode === "set") {
          throw new Error("simulated history property set failure");
        }
        scriptProperties[key] = String(value);
      },
    };
  },
};

global.LockService = {
  getScriptLock: function () {
    return {
      waitLock: function () {},
      releaseLock: function () {},
    };
  },
};

function currentFormatDateWeekday_(dateObj) {
  if (formatDateWeekdayOverride != null) {
    return String(formatDateWeekdayOverride);
  }
  const date = dateObj ? new Date(dateObj) : currentDate_();
  const jsWeekday = date.getUTCDay();
  return String(jsWeekday === 0 ? 7 : jsWeekday);
}

function setCurrentWeekdayFormatDate_(value) {
  formatDateWeekdayOverride = value == null ? null : Number(value);
}

global.Utilities = {
  sleep: function () {},
  getUuid: function () {
    harnessUuidCounter += 1;
    return "u" + String(harnessUuidCounter);
  },
  formatDate: function (date, timezone, format) {
    if (format === "u") {
      return currentFormatDateWeekday_(date);
    }
    if (format === "yyyyMMdd") {
      return TARGET_DATE;
    }
    return new Date(date).toISOString();
  },
};
global.UrlFetchApp = {
  fetch: function () {
    return {
      getResponseCode: function () {
        return 204;
      },
      getContentText: function () {
        return "{}";
      },
    };
  },
};
global.Logger = { log: function () {} };

function buildHarnessCorrelationId(attemptCount) {
  const resolvedAttemptCount = Math.max(Number(attemptCount || 1), 1);
  return (
    "evening-" +
    TARGET_DATE +
    "-attempt-" +
    String(resolvedAttemptCount) +
    "-u" +
    String(resolvedAttemptCount)
  );
}

function buildHarnessDisplayTitle(attemptCount) {
  return buildEveningDataOnlyRunDisplayTitle_(buildHarnessCorrelationId(attemptCount));
}

function currentEveningDispatchAttemptFromState_() {
  if (!scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY]) {
    return 1;
  }
  try {
    const state = JSON.parse(scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY]);
    return Number(state.attempt_count || 1);
  } catch {
    return 1;
  }
}

function currentEveningExpectedDisplayTitleFromState_() {
  if (!scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY]) {
    return "";
  }
  try {
    const state = JSON.parse(scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY]);
    return String(state.expected_run_display_title || "");
  } catch {
    return "";
  }
}

function buildHarnessDefaultRunDisplayTitle_() {
  const stateRaw = scriptProperties[EVENING_DATA_ONLY_STATE_PROPERTY];
  if (!stateRaw) {
    return buildHarnessDisplayTitle(1);
  }
  try {
    const state = JSON.parse(stateRaw);
    const phase = String(state.phase || "");
    const attemptCount = Number(state.attempt_count || 1);
    if (phase === "run_completed_non_success") {
      return buildHarnessDisplayTitle(attemptCount + 1);
    }
    return String(state.expected_run_display_title || buildHarnessDisplayTitle(attemptCount));
  } catch {
    return buildHarnessDisplayTitle(1);
  }
}

currentDate_ = function () { return new Date("2026-07-21T12:00:00.000Z"); };
taipeiYyyyMmDd_ = function () { return TARGET_DATE; };
nowIso_ = function () { return new Date(nowCursorMs).toISOString(); };
setPreflightMode = function (value) {
  preflightMode = value || "";
};
getMainRefSha_ = function () {
  if (preflightMode === "main_sha") {
    throw new Error("main SHA unavailable");
  }
  return mainShaValue;
};
listWorkflowRuns_ = function (workflowFile, perPage) {
  return { workflow_runs: correlationRuns.slice() };
};
latestWorkflowRunId_ = function (workflowFile) {
  if (preflightMode === "baseline_run") {
    throw new Error("latest workflow run id unavailable");
  }
  return 0;
};
findCorrelatedWorkflowRuns_ = function (
  workflowFile,
  baselineRunId,
  dispatchedAt,
  expectedHeadSha,
  expectedDisplayTitle
) {
  if (correlationApiFailureMode === "list_failure") {
    throw new Error("simulated correlation API failure");
  }
  const resolvedExpectedTitle =
    expectedDisplayTitle === undefined ? null : String(expectedDisplayTitle);
  return correlationRuns.filter(function (run) {
    if (!run || run.id === undefined) {
      return false;
    }
    if (expectedDisplayTitle && String(run.display_title || "") !== resolvedExpectedTitle) {
      return false;
    }
    if (expectedHeadSha && String(run.head_sha || "") !== String(expectedHeadSha)) {
      return false;
    }
    return true;
  });
};
getWorkflowRun_ = function (runId) {
  const key = String(runId);
  if (!(key in workflowRuns)) {
    throw new Error("workflow run not found: " + key);
  }
  return workflowRuns[key];
};
dispatchWorkflow_ = function (workflow, inputs) {
  dispatches.push({ workflow: workflow, inputs: inputs });
  if (dispatchError) {
    throw dispatchError;
  }
  return { statusCode: 204, responseBody: "ok" };
};
responsePreview_ = function (body) { return body ? String(body) : ""; };
readEveningDataOnlyMarketSession_ = function () {
  return marketSessionProvider();
};

  function workflowRun(id, status, conclusion, headSha, displayTitle) {
    const resolvedDisplayTitle =
      displayTitle === undefined ? buildHarnessDefaultRunDisplayTitle_() : displayTitle;
    return {
      id: String(id),
      status: status,
      conclusion: conclusion,
      head_sha: headSha || BASE_SHA,
      display_title: resolvedDisplayTitle,
      html_url: "https://example/" + String(id),
    };
  }

function requireBehavior(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function runInvocation(label) {
  const beforeDispatch = dispatches.length;
  let threw = false;
  let message = "";
  try {
    triggerEveningDataOnlyRepair();
  } catch (error) {
    threw = true;
    message = String(error.message || error);
  }
  const state = readEveningDataOnlyRepairState_();
  const history = readEveningDataOnlyRepairDispatchHistory_();
  return {
    label: label,
    threw: threw,
    error: message,
    dispatches: dispatches.length - beforeDispatch,
    state: state,
    history: history,
  };
}

function includesAttempt(history, attempt) {
  for (let i = 0; i < history.length; i++) {
    if (
      history[i].target_date === TARGET_DATE &&
      history[i].workflow === WORKFLOW &&
      history[i].attempt_count === attempt
    ) {
      return true;
    }
  }
  return false;
}

let step;
resetHarness();
setPreflightMode("baseline_run");
step = runInvocation("attempt1_preflight_error");
requireBehavior(step.threw, step.label + " should throw on preflight baseline run id failure");
requireBehavior(step.dispatches === 0, step.label + " should not POST on preflight error");
requireBehavior(
  step.state === null,
  step.label + " should not persist authoritative state after initial preflight failure"
);
requireBehavior(
  Array.isArray(step.history) && step.history.length === 0,
  step.label + " should not persist dispatch history row on initial preflight failure"
);

setPreflightMode("");
const queuedRunForPreflightRetry = workflowRun("111", "in_progress", null, BASE_SHA);
setCorrelationRuns([queuedRunForPreflightRetry]);
setWorkflowRuns({ "111": queuedRunForPreflightRetry });
step = runInvocation("attempt1_preflight_retry");
requireBehavior(!step.threw, step.label + " should recover on preflight success");
requireBehavior(step.dispatches === 1, step.label + " should POST once after preflight retry");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should be dispatched after recovery");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should remain attempt 1");

resetHarness();
setHistoryPropertyFailureMode("get");
setCorrelationRuns([workflowRun("111", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "111": workflowRun("111", "in_progress", null, BASE_SHA) });
step = runInvocation("history_get_failure");
requireBehavior(!step.threw, step.label + " should still dispatch when history get fails");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should dispatch by state/correlation path");
requireBehavior(step.dispatches === 1, step.label + " should POST once with history get failure");
setHistoryPropertyFailureMode("");

resetHarness();
setHistoryPropertyFailureMode("parse");
setCorrelationRuns([workflowRun("112", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "112": workflowRun("112", "in_progress", null, BASE_SHA) });
step = runInvocation("history_parse_failure");
requireBehavior(!step.threw, step.label + " should still dispatch when history parse fails");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should dispatch by state/correlation path with parse failure");
requireBehavior(step.dispatches === 1, step.label + " should POST once with history parse failure");
setHistoryPropertyFailureMode("");

resetHarness();
setHistoryPropertyFailureMode("set");
setCorrelationRuns([workflowRun("113", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "113": workflowRun("113", "in_progress", null, BASE_SHA) });
step = runInvocation("history_set_failure");
requireBehavior(!step.threw, step.label + " should still dispatch when history set fails");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should dispatch by state/correlation path with set failure");
requireBehavior(step.dispatches === 1, step.label + " should POST once with history set failure");
setHistoryPropertyFailureMode("");

  setState({
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 1,
    phase: "run_completed_non_success",
    baseline_run_id: "200",
    workflow_main_sha: BASE_SHA,
    workflow_run_id: "201",
    workflow_run_head_sha: BASE_SHA,
    workflow_run_status: "completed",
    workflow_run_conclusion: "failure",
    dispatch_correlation_id: "evening-" + TARGET_DATE + "-attempt-1-u1",
    expected_run_display_title: buildHarnessDisplayTitle(1),
  });
    setWorkflowRuns({ "201": workflowRun("201", "completed", "failure", BASE_SHA, buildHarnessDisplayTitle(1)) });
    setPreflightMode("baseline_run");
    step = runInvocation("attempt2_preflight_error");
    requireBehavior(step.threw, step.label + " should throw on attempt 2 preflight baseline run id failure");
    requireBehavior(step.dispatches === 0, step.label + " should not POST on attempt 2 preflight error");
    requireBehavior(step.state && step.state.phase === "run_completed_non_success", step.label + " should remain retryable attempt 2 state");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1 evidence");
    requireBehavior(step.state && step.state.workflow_run_id === "201", step.label + " should retain prior run id");
requireBehavior(step.state && step.state.workflow_run_conclusion === "failure", step.label + " should retain prior failure conclusion");
requireBehavior(step.state && includesAttempt(step.history, 1), step.label + " should keep attempt 1 history");
requireBehavior(!includesAttempt(step.history, 2), step.label + " should not create attempt 2 before preflight success");

    setPreflightMode("");
    setCorrelationRuns([workflowRun("202", "in_progress", null, BASE_SHA)]);
    setWorkflowRuns({
      "201": workflowRun("201", "completed", "failure", BASE_SHA, buildHarnessDisplayTitle(1)),
      "202": workflowRun("202", "in_progress", null, BASE_SHA, buildHarnessDisplayTitle(2)),
    });
    step = runInvocation("attempt2_preflight_retry");
requireBehavior(!step.threw, step.label + " should recover on attempt 2 preflight success");
requireBehavior(step.dispatches === 1, step.label + " should POST once for attempt 2");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should be dispatched for attempt 2");
requireBehavior(step.state && step.state.attempt_count === 2, step.label + " should be attempt 2");

resetHarness();
  setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  dispatched_at: "2026-07-21T20:00:00.000Z",
});
setCorrelationRuns([workflowRun("401", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "401": workflowRun("401", "in_progress", null, BASE_SHA) });
setCorrelationApiFailureMode("list_failure");
step = runInvocation("dispatching_no_runid_correlation_api_error");
requireBehavior(step.threw, step.label + " should throw when correlation API is unavailable");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should become dispatch_uncertain");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
requireBehavior(step.dispatches === 0, step.label + " should not POST when recovery correlation lookup fails");
setCorrelationApiFailureMode("");
setCorrelationRuns([workflowRun("501", "completed", "failure", BASE_SHA)]);
setWorkflowRuns({ "501": workflowRun("501", "completed", "failure", BASE_SHA) });
step = runInvocation("dispatching_no_runid_correlation_api_error_reinvoke");
requireBehavior(!step.threw, step.label + " should stay fail-closed after correlation API recovery");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt count");
requireBehavior(step.dispatches === 0, step.label + " should not POST on reinvoke");

resetHarness();
const queuedRun = workflowRun("111", "in_progress", null, BASE_SHA);
setCorrelationRuns([queuedRun]);
setWorkflowRuns({ "111": queuedRun });
step = runInvocation("attempt1_inflight");
requireBehavior(!step.threw, step.label + " should not throw on first dispatch: " + step.error);
requireBehavior(step.dispatches === 1, step.label + " must POST once");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should be dispatched");

step = runInvocation("attempt1_inflight_reinvoke");
requireBehavior(!step.threw, step.label + " should not throw when inflight is seen");
requireBehavior(step.dispatches === 0, step.label + " must not re-post for inflight state");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should stay dispatched");

const successRun = workflowRun("111", "completed", "success", BASE_SHA);
setWorkflowRuns({ "111": successRun });
setCorrelationRuns([successRun]);
step = runInvocation("attempt1_success");
requireBehavior(!step.threw, step.label + " should not throw on completed success");
requireBehavior(step.dispatches === 0, step.label + " must not re-post after success");
requireBehavior(step.state && step.state.phase === "duplicate_skipped", step.label + " should mark duplicate_skipped");
const successState = step.state;

step = runInvocation("attempt1_success_reinvoke");
requireBehavior(!step.threw, step.label + " should not throw on duplicate_skipped");
requireBehavior(step.dispatches === 0, step.label + " should stay no POST after duplicate_skipped");
setState(successState);
setCorrelationRuns([successRun]);
setWorkflowRuns({ "111": successRun });
step = runInvocation("attempt1_success_reinvoke_with_state");
requireBehavior(!step.threw, step.label + " should remain fail-closed after duplicate_skipped");
requireBehavior(step.dispatches === 0, step.label + " should still not POST after duplicate_skipped");
requireBehavior(step.state && step.state.phase === "duplicate_skipped", step.label + " should remain duplicate_skipped");

resetHarness();
const firstFailure = workflowRun("201", "completed", "failure", BASE_SHA);
setCorrelationRuns([firstFailure]);
setWorkflowRuns({ "201": firstFailure });
step = runInvocation("attempt1_failure");
requireBehavior(!step.threw, step.label + " should recover to run_completed_non_success");
requireBehavior(step.dispatches === 1, step.label + " must POST once");
requireBehavior(step.state && step.state.phase === "run_completed_non_success", step.label + " should be non-success");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should stay attempt 1");
const attempt1FailureState = step.state;
requireBehavior(attempt1FailureState && attempt1FailureState.workflow_run_id === "201", step.label + " should persist first failure run id");
requireBehavior(includesAttempt(step.history, 1), step.label + " should write attempt 1 history row");

setPreflightMode("baseline_run");
step = runInvocation("attempt2_preflight_error_after_attempt1_failure");
requireBehavior(step.threw, step.label + " should throw on attempt 2 preflight failure");
requireBehavior(step.dispatches === 0, step.label + " should not POST during attempt 2 preflight failure");
requireBehavior(step.state && step.state.phase === "run_completed_non_success", step.label + " should stay at attempt 1");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1 attempt_count");
requireBehavior(step.state && step.state.workflow_run_id === "201", step.label + " should keep attempt 1 run id");
requireBehavior(step.state && step.state.workflow_run_conclusion === "failure", step.label + " should keep attempt 1 failure conclusion");
requireBehavior(includesAttempt(step.history, 1), step.label + " should still have attempt 1 history");
requireBehavior(!includesAttempt(step.history, 2), step.label + " should not create attempt 2 preflight history row");
requireBehavior(
  step.history.some(
    function (entry) {
      return entry && entry.attempt_count === 1 && entry.workflow_run_id === "201" && entry.workflow_run_conclusion === "failure";
    }
  ),
  step.label + " should preserve attempt 1 terminal evidence"
);

setPreflightMode("");
const secondAttempt = workflowRun("202", "in_progress", null, BASE_SHA);
setCorrelationRuns([secondAttempt]);
setWorkflowRuns({
  "201": firstFailure,
  "202": secondAttempt,
});
step = runInvocation("attempt2_dispatch");
requireBehavior(!step.threw, step.label + " should dispatch attempt 2");
requireBehavior(step.dispatches === 1, step.label + " should POST once for attempt 2");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should be dispatched");
requireBehavior(step.state && step.state.attempt_count === 2, step.label + " should be attempt 2");
requireBehavior(includesAttempt(step.history, 1), "history must retain attempt 1");
requireBehavior(includesAttempt(step.history, 2), "history must retain attempt 2");
requireBehavior(step.state.workflow_run_id !== "201", step.label + " should not bind attempt 2 to stale attempt 1 run id");

const attempt2FailureState = step.state;
attempt2FailureState.phase = "run_completed_non_success";
attempt2FailureState.workflow_run_status = "completed";
attempt2FailureState.workflow_run_conclusion = "failure";
attempt2FailureState.workflow_run_id = "202";
setState(attempt2FailureState);
setCorrelationRuns([]);
setWorkflowRuns({
  "201": firstFailure,
  "202": workflowRun("202", "completed", "failure", BASE_SHA, buildHarnessDisplayTitle(2)),
});
step = runInvocation("attempt2_max");
requireBehavior(step.threw, step.label + " should throw on max attempts");
requireBehavior(step.state && step.state.phase === "max_attempts_exceeded", step.label + " should be max_attempts_exceeded");
requireBehavior(step.state && step.state.attempt_count === 2, step.label + " should remain at attempt 2");
requireBehavior(step.dispatches === 0, step.label + " must not POST again after max attempts");

resetHarness();
  setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "run_completed_non_success",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  workflow_run_id: "201",
  workflow_run_head_sha: BASE_SHA,
  workflow_run_status: "completed",
  workflow_run_conclusion: "failure",
  dispatched_at: "2026-07-21T20:00:00.000Z",
});
setWorkflowRuns({});
setCorrelationRuns([workflowRun("1000", "completed", "failure", BASE_SHA)]);
step = runInvocation("run_completed_non_success_direct_lookup_error_with_different_id_candidate");
requireBehavior(!step.threw, step.label + " should stay fail-closed for run_completed_non_success without exact same run");
requireBehavior(step.state && step.state.phase === "run_completed_non_success", step.label + " should remain run_completed_non_success");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
requireBehavior(step.state && step.state.workflow_run_id === "201", step.label + " should keep authoritative run id 201");
requireBehavior(step.dispatches === 0, step.label + " should not POST for non-exact run");
step = runInvocation("run_completed_non_success_direct_lookup_error_with_different_id_candidate_reinvoke");
requireBehavior(!step.threw, step.label + " should remain fail-closed");
requireBehavior(step.state && step.state.phase === "run_completed_non_success", step.label + " should remain run_completed_non_success");
requireBehavior(step.state && step.state.workflow_run_id === "201", step.label + " should keep authoritative run id 201");
requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

resetHarness();
const queuedHistoryFailure = [
  {
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 2,
    phase: "run_completed_non_success",
    workflow_run_id: "999",
    workflow_run_conclusion: "failure",
    workflow_run_head_sha: BASE_SHA,
  },
];
setHistory(queuedHistoryFailure);
setCorrelationRuns([workflowRun("401", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "401": workflowRun("401", "in_progress", null, BASE_SHA) });
step = runInvocation("history_only_forged_attempt_2_not_short_circuit");
requireBehavior(!step.threw, step.label + " should not use history-only terminal row as authoritative");
requireBehavior(step.dispatches === 1, step.label + " should dispatch when only history is present");
requireBehavior(step.state && step.state.phase === "dispatched", step.label + " should be dispatched on first attempt");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should start at attempt 1");
requireBehavior(includesAttempt(step.history, 2), "forged attempt 2 history row should remain");
requireBehavior(includesAttempt(step.history, 1), "new attempt 1 history row should be recorded");

resetHarness();
  setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  workflow_run_id: "999",
  dispatched_at: "2026-07-21T20:00:00.000Z",
  workflow_run_head_sha: ALT_SHA,
});
setWorkflowRuns({ "999": workflowRun("999", "completed", "success", ALT_SHA) });
setCorrelationRuns([]);
step = runInvocation("head_sha_mismatch");
requireBehavior(step.threw, step.label + " should throw on head SHA mismatch");
requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should be dispatch_ambiguous");
requireBehavior(step.dispatches === 0, step.label + " must not POST on mismatch");
step = runInvocation("head_sha_mismatch_reinvoke");
requireBehavior(!step.threw, step.label + " should stay fail-closed after head SHA mismatch");
requireBehavior(step.dispatches === 0, step.label + " should remain no POST on mismatch reinvoke");
requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");

resetHarness();
  setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  dispatched_at: "2026-07-21T20:00:00.000Z",
});
setCorrelationRuns([
  workflowRun("601", "completed", "success", BASE_SHA),
  workflowRun("602", "completed", "success", BASE_SHA),
]);
setWorkflowRuns({
  "601": workflowRun("601", "completed", "success", BASE_SHA),
  "602": workflowRun("602", "completed", "success", BASE_SHA),
});
step = runInvocation("multiple_correlation_ambiguity");
requireBehavior(step.threw, step.label + " should throw on multiple matching workflow runs");
requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should be dispatch_ambiguous");
requireBehavior(step.dispatches === 0, step.label + " should not POST when ambiguous");
step = runInvocation("multiple_correlation_ambiguity_reinvoke");
requireBehavior(!step.threw, step.label + " should stay fail-closed on reinvoke");
requireBehavior(step.dispatches === 0, step.label + " should not POST on reinvoke");
requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");

resetHarness();
setCorrelationRuns([workflowRun("301", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "301": workflowRun("301", "in_progress", null, BASE_SHA) });
dispatchError = new Error("network failure");
step = runInvocation("dispatch_exception");
requireBehavior(step.threw, step.label + " must throw on dispatch exception");
requireBehavior(step.dispatches === 1, step.label + " should record one attempted dispatch");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should enter dispatch_uncertain");

dispatchError = null;
setCorrelationRuns([]);
setNow("2026-07-21T20:45:00.000Z");
step = runInvocation("dispatch_uncertain_followup");
requireBehavior(!step.threw, step.label + " should stay fail-closed");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should stay dispatch_uncertain");
requireBehavior(step.dispatches === 0, step.label + " should not re-dispatch");

resetHarness();
setCorrelationApiFailureMode("list_failure");
step = runInvocation("polling_api_error_after_post");
requireBehavior(step.threw, step.label + " should throw when polling correlation API fails");
requireBehavior(step.dispatches === 1, step.label + " should record one dispatch");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should become dispatch_uncertain");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
setCorrelationApiFailureMode("");
setCorrelationRuns([workflowRun("701", "completed", "failure", BASE_SHA)]);
setWorkflowRuns({ "701": workflowRun("701", "completed", "failure", BASE_SHA) });
step = runInvocation("polling_api_error_after_post_reinvoke");
requireBehavior(!step.threw, step.label + " should stay fail-closed after polling API recovery");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt count");
requireBehavior(step.dispatches === 0, step.label + " should remain no-POST on reinvoke");

resetHarness();
  setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  workflow_run_id: "missing",
  dispatched_at: "2026-07-21T20:00:00.000Z",
});
setCorrelationRuns([]);
setWorkflowRuns({});
setNow("2026-07-21T20:20:00.000Z");
step = runInvocation("api_error_uncertain");
requireBehavior(step.threw, step.label + " should throw when recovery API fails");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should be dispatch_uncertain");
requireBehavior(step.dispatches === 0, step.label + " should not POST after API uncertainty");

    step = runInvocation("api_error_uncertain_reinvoke");
    requireBehavior(!step.threw, step.label + " should stay fail-closed after uncertain API");
    requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
    requireBehavior(step.dispatches === 0, step.label + " should not POST on uncertainty reinvoke");
    setWorkflowRuns({ "missing": workflowRun("missing", "completed", "failure", BASE_SHA) });
    step = runInvocation("api_error_uncertain_reinvoke_failed_lookup");
    requireBehavior(!step.threw, step.label + " should remain fail-closed on failed lookup recovery");
    requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should stay dispatch_uncertain after direct failure recovery");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
    requireBehavior(step.dispatches === 0, step.label + " should still not POST after API uncertainty with failed lookup");

    resetHarness();
    setStateWithEveningIdentity({
      target_date: TARGET_DATE,
      workflow: WORKFLOW,
      attempt_count: 1,
      phase: "dispatch_uncertain",
      baseline_run_id: "200",
      workflow_main_sha: BASE_SHA,
      workflow_run_id: "801",
      workflow_run_head_sha: BASE_SHA,
      dispatched_at: "2026-07-21T20:00:00.000Z",
    });
    setCorrelationRuns([]);
    setWorkflowRuns({});
    step = runInvocation("dispatch_uncertain_recovery_fallback_failed_run");
    requireBehavior(!step.threw, step.label + " should not throw for dispatch_uncertain terminal state");
    requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should stay dispatch_uncertain");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
    requireBehavior(step.dispatches === 0, step.label + " should not POST from dispatch_uncertain");
    setWorkflowRuns({ "801": workflowRun("801", "completed", "failure", BASE_SHA) });
    step = runInvocation("dispatch_uncertain_recovery_fallback_failed_run_reinvoke");
    requireBehavior(!step.threw, step.label + " should stay fail-closed when failed run is now discoverable");
    requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should not increase attempt count");
    requireBehavior(step.dispatches === 0, step.label + " should stay 0 POST");

    resetHarness();
    setStateWithEveningIdentity({
      target_date: TARGET_DATE,
      workflow: WORKFLOW,
      attempt_count: 1,
      phase: "dispatch_ambiguous",
      baseline_run_id: "200",
      workflow_main_sha: BASE_SHA,
      workflow_run_id: "901",
      workflow_run_head_sha: BASE_SHA,
      dispatched_at: "2026-07-21T20:00:00.000Z",
    });
    setCorrelationRuns([]);
    setWorkflowRuns({});
    step = runInvocation("dispatch_ambiguous_recovery_fallback_failed_run");
    requireBehavior(!step.threw, step.label + " should not throw for dispatch_ambiguous terminal state");
    requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should stay dispatch_ambiguous");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should keep attempt 1");
    requireBehavior(step.dispatches === 0, step.label + " should not POST from dispatch_ambiguous");
    setWorkflowRuns({ "901": workflowRun("901", "completed", "failure", BASE_SHA) });
    step = runInvocation("dispatch_ambiguous_recovery_fallback_failed_run_reinvoke");
    requireBehavior(!step.threw, step.label + " should stay fail-closed when failed run is now discoverable");
    requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");
    requireBehavior(step.state && step.state.attempt_count === 1, step.label + " should not increase attempt count");
    requireBehavior(step.dispatches === 0, step.label + " should stay 0 POST");

    resetHarness();
    setStateWithEveningIdentity({
      target_date: TARGET_DATE,
      workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  dispatched_at: "not-a-timestamp",
});
setCorrelationRuns([]);
setWorkflowRuns({});
step = runInvocation("invalid_dispatched_at");
requireBehavior(step.threw, step.label + " should throw on invalid dispatched_at");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should become dispatch_uncertain");
requireBehavior(step.dispatches === 0, step.label + " should avoid POST for invalid dispatched_at");
step = runInvocation("invalid_dispatched_at_reinvoke");
requireBehavior(!step.threw, step.label + " should stay fail-closed on reinvoke");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

resetHarness();
    setStateWithEveningIdentity({
  target_date: TARGET_DATE,
  workflow: WORKFLOW,
  attempt_count: 1,
  phase: "dispatching",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
});
setCorrelationRuns([]);
setWorkflowRuns({});
step = runInvocation("missing_dispatched_at");
requireBehavior(step.threw, step.label + " should throw on missing dispatched_at");
requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should become dispatch_uncertain");
requireBehavior(step.dispatches === 0, step.label + " should avoid POST for missing dispatched_at");
  step = runInvocation("missing_dispatched_at_reinvoke");
  requireBehavior(!step.threw, step.label + " should stay fail-closed on reinvoke");
  requireBehavior(step.state && step.state.phase === "dispatch_uncertain", step.label + " should remain dispatch_uncertain");
  requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

  resetHarness();
  setStateWithEveningIdentity({
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 1,
    phase: "dispatching",
    baseline_run_id: "200",
    workflow_main_sha: BASE_SHA,
    workflow_run_id: "701",
    dispatched_at: null,
    dispatch_correlation_id: "mismatch-token",
  });
  setCorrelationRuns([]);
  setWorkflowRuns({
    "701": workflowRun("701", "completed", "failure", BASE_SHA, "workflow-title-different"),
  });
  step = runInvocation("identity_mismatch_token_title");
  requireBehavior(!step.threw, step.label + " should fail closed on title contract mismatch");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should become dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should avoid POST when title mismatches");
  step = runInvocation("identity_mismatch_token_title_reinvoke");
  requireBehavior(!step.threw, step.label + " should remain fail-closed after title mismatch");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

  resetHarness();
  setState({
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 1,
    phase: "dispatching",
    baseline_run_id: "200",
    workflow_main_sha: BASE_SHA,
    workflow_run_id: "702",
    dispatched_at: null,
  });
  setCorrelationRuns([]);
  setWorkflowRuns({
    "702": workflowRun("702", "completed", "failure", BASE_SHA),
  });
  step = runInvocation("identity_mismatch_missing_token");
  requireBehavior(!step.threw, step.label + " should fail closed when token is missing");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should become dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should avoid POST without token");
  step = runInvocation("identity_mismatch_missing_token_reinvoke");
  requireBehavior(!step.threw, step.label + " should remain fail-closed after missing token");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

  resetHarness();
  setState({
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 1,
    phase: "dispatched",
    baseline_run_id: "200",
    workflow_main_sha: BASE_SHA,
    workflow_run_id: "703",
    dispatched_at: null,
    dispatch_correlation_id: "token-dispatched-phase",
    expected_run_display_title: buildEveningDataOnlyRunDisplayTitle_("other-token"),
  });
  setCorrelationRuns([]);
  setWorkflowRuns({
    "703": workflowRun("703", "completed", "failure", BASE_SHA, "workflow-title-different"),
  });
  step = runInvocation("identity_mismatch_dispatched_phase");
  requireBehavior(!step.threw, step.label + " should fail closed on dispatched phase mismatch");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should become dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should avoid POST when dispatched phase has identity mismatch");
  step = runInvocation("identity_mismatch_dispatched_phase_reinvoke");
  requireBehavior(!step.threw, step.label + " should remain fail-closed after dispatched identity mismatch");
  requireBehavior(step.state && step.state.phase === "dispatch_ambiguous", step.label + " should remain dispatch_ambiguous");
  requireBehavior(step.dispatches === 0, step.label + " should still avoid POST on reinvoke");

  resetHarness();
  currentDate_ = function () { return new Date("2026-07-19T12:00:00.000Z"); };
setCorrelationRuns([]);
step = runInvocation("weekend_skip");
requireBehavior(!step.threw, step.label + " should not throw on weekend guard");
requireBehavior(step.dispatches === 0, step.label + " must skip weekend");
requireBehavior(step.state && step.state.phase === "skipped_weekend", step.label + " should persist skipped_weekend");

resetHarness();
currentDate_ = function () { return new Date("2026-07-21T12:00:00.000Z"); };
marketSessionProvider = function () { return { assessment_date: TARGET_DATE, market_status: "closed_scheduled" }; };
setCorrelationRuns([]);
step = runInvocation("closed_scheduled_skip");
requireBehavior(!step.threw, step.label + " should not throw on closed_scheduled");
requireBehavior(step.dispatches === 0, step.label + " should skip closed_scheduled");
requireBehavior(step.state && step.state.phase === "skipped_closed_market", step.label + " should persist skipped_closed_market");

resetHarness();
currentDate_ = function () { return new Date("2026-07-21T12:00:00.000Z"); };
marketSessionProvider = function () { return { assessment_date: TARGET_DATE, market_status: "closed_emergency" }; };
setCorrelationRuns([]);
step = runInvocation("closed_emergency_skip");
requireBehavior(!step.threw, step.label + " should not throw on closed_emergency");
requireBehavior(step.dispatches === 0, step.label + " should skip closed_emergency");
requireBehavior(step.state && step.state.phase === "skipped_closed_market", step.label + " should persist skipped_closed_market");

  resetHarness();
  currentDate_ = function () { return new Date("2026-07-21T12:00:00.000Z"); };
  setCorrelationRuns([workflowRun("401", "in_progress", null, BASE_SHA)]);
  setWorkflowRuns({ "401": workflowRun("401", "in_progress", null, BASE_SHA) });
  marketSessionProvider = function () {
    return { assessment_date: "20260720", market_status: "closed_scheduled" };
  };
  step = runInvocation("stale_session_still_dispatch");
  requireBehavior(!step.threw, step.label + " should not throw: " + step.error);
  requireBehavior(
    step.state && step.state.phase === "dispatched",
    step.label + " should be dispatched but got phase=" + JSON.stringify(step.state)
  );
  requireBehavior(step.dispatches === 1, step.label + " should dispatch for stale market session");

resetHarness();
setCorrelationRuns([workflowRun("402", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "402": workflowRun("402", "in_progress", null, BASE_SHA) });
marketSessionProvider = function () { return {}; };
step = runInvocation("missing_session_still_dispatch");
requireBehavior(step.dispatches === 1, step.label + " should dispatch when session is missing");

resetHarness();
setCorrelationRuns([workflowRun("403", "in_progress", null, BASE_SHA)]);
setWorkflowRuns({ "403": workflowRun("403", "in_progress", null, BASE_SHA) });
marketSessionProvider = function () { throw new Error("read failed"); };
  step = runInvocation("read_error_session_still_dispatch");
  requireBehavior(step.dispatches === 1, step.label + " should dispatch when session read fails");

  resetHarness();
  setStateWithEveningIdentity({
    target_date: TARGET_DATE,
    workflow: WORKFLOW,
    attempt_count: 1,
    phase: "duplicate_skipped",
  baseline_run_id: "200",
  workflow_main_sha: BASE_SHA,
  workflow_run_id: "999",
  workflow_run_head_sha: BASE_SHA,
  dispatched_at: "2026-07-21T20:00:00.000Z",
});
setWorkflowRuns({});
setCorrelationRuns([workflowRun("999", "completed", "failure", BASE_SHA)]);
step = runInvocation("success_state_direct_lookup_error_with_window_candidate");
requireBehavior(!step.threw, step.label + " should stay fail-closed for stale terminal state");
requireBehavior(step.state && step.state.phase === "duplicate_skipped", step.label + " should remain duplicate_skipped");
requireBehavior(step.dispatches === 0, step.label + " should not POST when direct lookup fails");
step = runInvocation("success_state_direct_lookup_error_with_window_candidate_reinvoke");
requireBehavior(!step.threw, step.label + " should remain fail-closed on reinvoke");
requireBehavior(step.state && step.state.phase === "duplicate_skipped", step.label + " should remain duplicate_skipped");
requireBehavior(step.dispatches === 0, step.label + " should still not POST on reinvoke");

process.stdout.write("evening-data-only-behavior-pass");
'''
    script = tmp_path / "apps_script_evening_data_only_behavior.js"
    script.write_text(source + "\n" + harness, encoding="utf-8")
    result = subprocess.run(
        [node, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "evening-data-only-behavior-pass"


def test_apps_script_tdcc_history_gap_repair_trigger_is_tuesday_monthly_guard() -> None:
    body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerTdccHistoryGapRepair"
    )
    install_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "installTdccHistoryGapRepairTrigger_"
    )

    assert 'dispatchWorkflow_("repair_tdcc_monthly_history_gaps.yml", {' in body
    assert 'universe: "chatgpt-top"' in body
    assert 'max_stocks: "80"' in body
    assert 'max_requests: "500"' in body
    assert 'rebuild_max_dates: "4"' in body
    assert "ScriptApp.WeekDay.TUESDAY" in install_body
    assert ".atHour(9)" in install_body


def test_apps_script_tdcc_chain_requires_success_main_evidence_before_dispatch() -> None:
    trigger_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerTdccWeeklyReport"
    )
    orchestrator_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "orchestrateTdccIndividualRefresh"
    )
    evidence_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "readTdccPublishedEvidence_"
    )

    assert "tdcc_baseline_run_id" in trigger_body
    assert "tdcc_dispatched_at" in trigger_body
    assert "Utilities.sleep" not in trigger_body
    assert 'tdccRun.conclusion !== "success"' in orchestrator_body
    assert "readTdccPublishedEvidence_(tdccRun)" in orchestrator_body
    assert "mainEvidenceWindowExpired_(tdccRun.updated_at)" in orchestrator_body
    assert "TDCC_RUN_STATUS_PATH" in evidence_body
    assert "TDCC_VALIDATION_PATH" in evidence_body
    assert 'validation.status !== "pass"' in evidence_body
    assert "validation.date_contract.date_source" in evidence_body
    assert "TDCC_OFFICIAL_DATE_SOURCE" in evidence_body
    assert "assertCommitContained_" in evidence_body
    assert "getMainRefSha_" in evidence_body


def test_apps_script_tdcc_chain_is_idempotent_and_tracks_one_downstream_run() -> None:
    orchestrator_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "orchestrateTdccIndividualRefresh"
    )
    history_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "tdccDispatchAlreadyRecorded_"
    )
    identity_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "tdccChainIdentity_"
    )
    active_installer_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "installTdccActivePollTrigger_"
    )
    retry_installer_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "installTdccDataRetryTrigger_"
    )
    cleanup_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "removeTdccIndividualRefreshOrchestratorTriggers_"
    )
    install_all_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "installAllWorkflowTriggers"
    )
    downstream_evidence_body = (
        validate_apps_script_workflow_triggers.apps_script_function_body(
            "readWorkflowOutputEvidence_"
        )
    )

    assert "tdccDispatchAlreadyRecorded_" in orchestrator_body
    assert "state.chain_key" in orchestrator_body
    assert "state.downstream_baseline_run_id" in orchestrator_body
    assert "state.downstream_run_id" in orchestrator_body
    assert "state.tdcc_output_commit_sha" in orchestrator_body
    assert "dispatchWorkflow_(INDIVIDUAL_REFRESH_WORKFLOW)" in orchestrator_body
    assert "readWorkflowOutputEvidence_" in orchestrator_body
    assert "tdccChainIdentity_(runId, signalDate, outputCommitSha)" in history_body
    assert "item.chain_key === chainKey" in history_body
    assert "||" not in history_body
    assert "runId" in identity_body
    assert "signalDate" in identity_body
    assert "outputCommitSha" in identity_body
    assert "mainEvidenceWindowExpired_(downstreamRun.updated_at)" in orchestrator_body
    assert 'state.phase = "downstream_main_pending"' in orchestrator_body
    assert '.everyMinutes(TDCC_CHAIN_POLL_MINUTES)' in active_installer_body
    assert 'ScriptApp.newTrigger("resumeTdccIndividualRefreshRetry")' in retry_installer_body
    assert ".at(retryAt)" in retry_installer_body
    assert ".everyMinutes(" not in retry_installer_body
    assert 'removeTriggersForFunction_("orchestrateTdccIndividualRefresh")' in cleanup_body
    assert 'removeTriggersForFunction_("resumeTdccIndividualRefreshRetry")' in cleanup_body
    assert "removeTdccIndividualRefreshOrchestratorTriggers_();" in install_all_body
    assert "installTdccActivePollTrigger_();" not in install_all_body
    assert "runStatus.github_run_id" in downstream_evidence_body
    assert "runStatus.github_head_sha" in downstream_evidence_body
    assert "runStatus.official_signal_date" in downstream_evidence_body
    assert "runStatus.date_contract.date_source" in downstream_evidence_body


def test_apps_script_tdcc_chain_identity_is_retryable_after_failed_attempt(
    tmp_path: Path,
) -> None:
    node = resolve_test_node()

    source = (ROOT / "docs" / "apps_script_workflow_trigger.gs").read_text(
        encoding="utf-8"
    )
    harness = r'''
const properties = {};
global.PropertiesService = {
  getScriptProperties: function () {
    return {
      getProperty: function (key) { return properties[key] || null; },
      setProperty: function (key, value) { properties[key] = String(value); },
    };
  },
};

function requireBehavior(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

const signalDate = "20260717";
const firstCommit = "a".repeat(40);
const correctedCommit = "b".repeat(40);
const firstChain = {
  chain_key: tdccChainIdentity_("1001", signalDate, firstCommit),
  tdcc_run_id: "1001",
  signal_date: signalDate,
  tdcc_head_sha: "c".repeat(40),
  tdcc_output_commit_sha: firstCommit,
  downstream_dispatched_at: "2026-07-18T08:00:00.000Z",
  downstream_conclusion: "failure",
  phase: "downstream_failed",
  error: "simulated downstream failure",
};
recordTdccDispatch_(firstChain);

requireBehavior(
  tdccDispatchAlreadyRecorded_("1001", signalDate, firstCommit),
  "the same exact chain must not dispatch twice"
);
requireBehavior(
  !tdccDispatchAlreadyRecorded_("1002", signalDate, firstCommit),
  "a new TDCC run must remain dispatchable after a failed same-date chain"
);
requireBehavior(
  !tdccDispatchAlreadyRecorded_("1001", signalDate, correctedCommit),
  "a corrected TDCC output commit must remain dispatchable for the same date"
);
process.stdout.write("behavior-pass");
'''
    script = tmp_path / "apps_script_chain_behavior.js"
    script.write_text(source + "\n" + harness, encoding="utf-8")
    result = subprocess.run(
        [node, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "behavior-pass"


def test_apps_script_tdcc_reconciliation_trigger_lifecycle_behavior(
    tmp_path: Path,
) -> None:
    node = resolve_test_node()

    source = (ROOT / "docs" / "apps_script_workflow_trigger.gs").read_text(
        encoding="utf-8"
    )
    harness = r'''
const properties = {};
const triggers = [];
const dispatches = [];

function removeArrayItem(array, item) {
  const index = array.indexOf(item);
  if (index >= 0) array.splice(index, 1);
}

function triggerBuilder(handler) {
  const spec = { handler: handler };
  const builder = {
    timeBased: function () { spec.timeBased = true; return builder; },
    everyMinutes: function (value) { spec.everyMinutes = value; return builder; },
    everyDays: function (value) { spec.everyDays = value; return builder; },
    everyWeeks: function (value) { spec.everyWeeks = value; return builder; },
    onWeekDay: function (value) { spec.onWeekDay = value; return builder; },
    atHour: function (value) { spec.atHour = value; return builder; },
    nearMinute: function (value) { spec.nearMinute = value; return builder; },
    inTimezone: function (value) { spec.timezone = value; return builder; },
    at: function (value) { spec.at = value; return builder; },
    create: function () {
      const trigger = Object.assign({}, spec, {
        getHandlerFunction: function () { return handler; },
        getEventType: function () { return "CLOCK"; },
        getTriggerSource: function () { return "CLOCK"; },
      });
      triggers.push(trigger);
      return trigger;
    },
  };
  return builder;
}

global.ScriptApp = {
  WeekDay: {
    SUNDAY: "SUNDAY",
    TUESDAY: "TUESDAY",
    SATURDAY: "SATURDAY",
  },
  newTrigger: triggerBuilder,
  getProjectTriggers: function () { return triggers.slice(); },
  deleteTrigger: function (trigger) { removeArrayItem(triggers, trigger); },
};
global.PropertiesService = {
  getScriptProperties: function () {
    return {
      getProperty: function (key) { return properties[key] || null; },
      setProperty: function (key, value) { properties[key] = String(value); },
    };
  },
};
global.LockService = {
  getScriptLock: function () {
    return { waitLock: function () {}, releaseLock: function () {} };
  },
};
global.Logger = { log: function () {} };

latestWorkflowRunId_ = function () { return "100"; };
getMainRefSha_ = function () { return "a".repeat(40); };
taipeiYyyyMmDd_ = function () { return "20260718"; };
nowIso_ = function () { return new Date().toISOString(); };
dispatchWorkflow_ = function (workflow, inputs) {
  dispatches.push({ workflow: workflow, inputs: inputs || {} });
  return { statusCode: 204 };
};

function requireBehavior(condition, message) {
  if (!condition) throw new Error(message);
}
function triggersFor(handler) {
  return triggers.filter(function (trigger) { return trigger.handler === handler; });
}

triggerTdccWeeklyReport();
requireBehavior(triggers.length === 1, "Saturday start must create exactly one temporary trigger");
requireBehavior(
  triggersFor("orchestrateTdccIndividualRefresh").length === 1 &&
    triggers[0].everyMinutes === 5,
  "active TDCC work must use the five-minute poller"
);

let state = readTdccChainState_();
scheduleTdccDataRetry_(state, {
  id: "200",
  html_url: "https://example.invalid/200",
  conclusion: "failure",
});
state = readTdccChainState_();
requireBehavior(triggers.length === 1, "data wait must replace the active poller");
requireBehavior(
  triggersFor("resumeTdccIndividualRefreshRetry").length === 1 &&
    triggers[0].at instanceof Date &&
    !Object.prototype.hasOwnProperty.call(triggers[0], "everyMinutes"),
  "official-data wait must use one one-time retry trigger"
);
const retryDelayMs = new Date(state.next_retry_at).getTime() - Date.now();
requireBehavior(
  retryDelayMs > 29 * 60 * 1000 && retryDelayMs <= 30 * 60 * 1000,
  "official-data retry must be approximately 30 minutes"
);

state.next_retry_at = new Date(Date.now() - 1000).toISOString();
writeTdccChainState_(state);
dispatchScheduledTdccRetry_(state);
requireBehavior(triggers.length === 1, "retry dispatch must leave one active poller");
requireBehavior(
  triggersFor("orchestrateTdccIndividualRefresh").length === 1 &&
    triggers[0].everyMinutes === 5,
  "retry dispatch must restore five-minute active polling"
);

try {
  failTdccChain_(state, "tdcc_failed", "simulated terminal failure");
} catch (error) {
  requireBehavior(error.message === "simulated terminal failure", "terminal error must propagate");
}
requireBehavior(triggers.length === 0, "terminal failure must remove all temporary triggers");

installTdccActivePollTrigger_();
state.phase = "complete";
delete state.error;
writeTdccChainState_(state);
orchestrateTdccIndividualRefresh();
requireBehavior(triggers.length === 0, "completed state must remove all temporary triggers");

installAllWorkflowTriggers();
requireBehavior(
  triggersFor("orchestrateTdccIndividualRefresh").length === 0 &&
    triggersFor("resumeTdccIndividualRefreshRetry").length === 0,
  "recurring trigger installation must not create an idle TDCC poller"
);
const safety = triggersFor("triggerIndividualStockDataRefresh");
requireBehavior(
  safety.length === 1 && safety[0].atHour === 22 && safety[0].nearMinute === 20,
  "daily 22:20 individual refresh safety trigger must remain installed"
);
process.stdout.write("trigger-lifecycle-pass");
'''
    script = tmp_path / "apps_script_trigger_lifecycle.js"
    script.write_text(source + "\n" + harness, encoding="utf-8")
    result = subprocess.run(
        [node, str(script)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "trigger-lifecycle-pass"


def test_apps_script_tdcc_chain_uses_only_event_scoped_temporary_triggers() -> None:
    trigger_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "triggerTdccWeeklyReport"
    )
    orchestrator_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "orchestrateTdccIndividualRefresh"
    )
    retry_scheduler_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "scheduleTdccDataRetry_"
    )
    retry_dispatch_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "dispatchScheduledTdccRetry_"
    )
    failure_body = validate_apps_script_workflow_triggers.apps_script_function_body(
        "failTdccChain_"
    )

    assert "installTdccActivePollTrigger_();" in trigger_body
    assert "installTdccDataRetryTrigger_(state.next_retry_at);" in retry_scheduler_body
    assert "installTdccActivePollTrigger_();" in retry_dispatch_body
    assert orchestrator_body.count("removeTdccIndividualRefreshOrchestratorTriggers_();") >= 3
    assert "recordTdccDispatch_(state);" in failure_body
    assert "removeTdccIndividualRefreshOrchestratorTriggers_();" in failure_body


def test_individual_refresh_workflow_commits_unique_run_status_evidence() -> None:
    workflow_text = (
        ROOT / ".github" / "workflows" / "individual_stock_data_refresh.yml"
    ).read_text(encoding="utf-8")

    assert "Write individual stock refresh run status" in workflow_text
    assert "python scripts/validate_apps_script_workflow_triggers.py" in workflow_text
    assert 'os.environ["GITHUB_RUN_ID"]' in workflow_text
    assert 'os.environ["GITHUB_SHA"]' in workflow_text
    assert '"official_signal_date": signal_date' in workflow_text
    assert '"source_tdcc_dataset_id": dataset_id' in workflow_text
    assert 'expected_date_source = "report_ready_csv_signal_date"' in workflow_text
    assert "python scripts/validate_tdcc_dataset_manifest.py" in workflow_text
    assert "tdcc_dataset_manifest_latest.json" in workflow_text
    assert "individual_stock_refresh_run_status_latest.json" in workflow_text
    assert "git add output/latest/individual_stock_reports/" in workflow_text
    assert "git add docs/latest/individual_stock_reports/" in workflow_text
    assert workflow_text.index("Build individual stock packets and windows") < workflow_text.index(
        "Write individual stock refresh run status"
    )
    assert workflow_text.index("Write individual stock refresh run status") < workflow_text.index(
        "Commit individual stock refresh outputs"
    )


def test_tdcc_and_individual_workflows_remain_external_dispatch_only() -> None:
    forbidden = [
        "workflow_run:",
        "repository_dispatch:",
        "gh workflow run",
        "api.github.com",
        "/dispatches",
    ]
    for workflow_file in ["tdcc_weekly.yml", "individual_stock_data_refresh.yml"]:
        text = (ROOT / ".github" / "workflows" / workflow_file).read_text(
            encoding="utf-8"
        )
        assert "on:\n  workflow_dispatch:" in text
        for pattern in forbidden:
            assert pattern not in text


def test_canonical_chatgpt_side_generator_is_tracked_and_not_legacy_six_category() -> None:
    entrypoint = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
    entrypoint_text = entrypoint.read_text(encoding="utf-8", errors="replace")
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")

    assert entrypoint.exists()
    assert "resolve_daily_report_source_state" in entrypoint_text
    assert "create_registered_full_temp_worktree" in entrypoint_text
    assert 'consumer_id="chatgpt_daily_report_entrypoint"' in entrypoint_text
    assert "CHATGPT_DAILY_REPORT_ENTRYPOINT" in entrypoint_text
    assert "CHATGPT_DAILY_SOURCE_REF" in entrypoint_text
    assert "PYTHONIOENCODING" in entrypoint_text
    assert "reconfigure(encoding=\"utf-8\", errors=\"replace\")" in entrypoint_text
    assert "source-gate-only" in entrypoint_text
    assert path.exists()
    assert "CATEGORY_SPECS" not in text
    assert 'REPO = ROOT / "tdcc-weekly-report-git"' not in text
    assert "daily_report_model_registry_latest.csv" in text
    assert "CHATGPT_DAILY_SOURCE_REF" in text
    assert "daily_candidate_model_signals_for_report_latest.csv" in text
    assert "model_score" in text
    assert "risk_tags" in text
    for field in DAILY_DECISION_LAYER_FIELDS:
        assert field not in text
    assert "mainstream_curated_recommendation_rows" in text
    assert "non_mainstream_curated_recommendation_rows" in text
    assert "資金進入族群觀察" in text
    assert "daily_candidate_group_rotation_latest.csv" in text
    assert "CHATGPT_SIDE_KLINE_DAYS = 126" in text
    assert ".tail(CHATGPT_SIDE_KLINE_DAYS)" in text
    assert "kline_180" not in text
    assert "tail(180)" not in text
    assert "180日K線" not in text
    assert "resolve_daily_report_source_state" in text
    assert "require_entrypoint_invocation" in text
    assert "run_chatgpt_daily_report_entrypoint.py" in text
    assert "--request-date" not in text
    assert "args.request_date" not in text
    assert "fetch_remote_readme_values" not in text
    assert "REMOTE_README_URLS" not in text
    assert 'REQUEST_DATE = datetime.now().strftime("%Y%m%d")' not in text

    resolver = ROOT / "scripts" / "resolve_daily_report_source_state.py"
    resolver_text = resolver.read_text(encoding="utf-8", errors="replace")
    assert resolver.exists()
    assert "origin/main" in resolver_text
    assert "git show" in resolver_text
    assert "data_freshness_latest.csv" in resolver_text
    assert "READ_ME_FIRST_DAILY_REPORT.txt" in resolver_text
    assert "chatgpt_daily_report_packet_latest.txt" in resolver_text
    assert "OneDrive" in resolver_text

    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8", errors="replace")
    assert "chatgpt_side_outputs*/" in gitignore


def test_observation_list_is_row_per_stock_not_joined_cell() -> None:
    path = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    text = path.read_text(encoding="utf-8", errors="replace")
    start = text.index("def mainstream_curated_front_observation_rows(")
    end = text.index("\ndef non_mainstream_curated_front_observation_rows(", start)
    function_text = text[start:end]

    assert 'rows = [["榜別", "模型", "股票", "模型狀態", "分數 / 風險"]]' in function_text
    assert "listing_status_label(row, stage)" in function_text
    assert "listing_status_sort_key(listing_label)" in function_text
    assert '"新上榜": 0' in text
    assert '"重複上榜": 1' in text
    assert "model_rows += 1" in function_text
    assert '".join(lines)' not in function_text

    non_mainstream_pdf = text[
        text.index("def build_non_mainstream_curated_pdf(") : text.index(
            "\ndef build_mainstream_full_candidate_pdf(",
            text.index("def build_non_mainstream_curated_pdf("),
        )
    ]
    assert "non_mainstream_curated_front_observation_rows(" not in non_mainstream_pdf
    assert "non_mainstream_curated_recommendation_rows(" not in non_mainstream_pdf


def test_daily_pdf_packet_and_rules_do_not_depend_on_decision_layer() -> None:
    paths = [
        ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py",
        ROOT / "build_chatgpt_daily_report_packet.py",
        ROOT / "build_daily_market_report_artifacts.py",
        ROOT / "build_chatgpt_daily_report_rules.py",
        ROOT / "scripts" / "build_chatgpt_indicator_usage_guide.py",
        ROOT / "scripts" / "build_volume_breakout_watch.py",
        ROOT / "rules" / "daily_stock_candidate_rules.md",
        ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        for field in DAILY_DECISION_LAYER_FIELDS:
            assert field not in text, f"{path.name} still references {field}"
        for phrase in DAILY_OPERATION_CONCLUSION_PHRASES:
            assert phrase not in text, f"{path.name} still emits {phrase}"

    packet_text = (ROOT / "build_chatgpt_daily_report_packet.py").read_text(
        encoding="utf-8"
    )
    assert "daily_candidate_model_signals_for_report_latest.csv" in packet_text
    assert "model_score" in packet_text
    assert "risk_penalty_tags" in packet_text


def test_daily_market_report_consumes_advisory_volume_watch_rank() -> None:
    source = (ROOT / "build_daily_market_report_artifacts.py").read_text(
        encoding="utf-8"
    )
    volume_columns = source.split("volume_cols = [", 1)[1].split("]", 1)[0]

    assert '"advisory_volume_breakout_rank"' in volume_columns
    assert '"volume_breakout_rank"' not in volume_columns


def test_daily_production_sources_do_not_build_or_depend_on_decision_layer() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )
    assert "build_daily_candidate_decision_layer.py" not in workflow
    assert "validate_daily_candidate_decision_layer.py" not in workflow

    assert not (ROOT / "scripts" / "build_daily_candidate_decision_layer.py").exists()
    assert not (ROOT / "scripts" / "validate_daily_candidate_decision_layer.py").exists()

    paths = [
        ROOT / "scripts" / "build_daily_candidate_model_layer.py",
        ROOT / "scripts" / "build_daily_theme_leadership_layer.py",
        ROOT / "scripts" / "validate_daily_theme_leadership_layer.py",
        ROOT / "scripts" / "build_non_revenue_momentum_watch.py",
        ROOT / "scripts" / "build_theme_event_watch.py",
        ROOT / "scripts" / "update_daily_theme_status_history.py",
        ROOT / "scripts" / "check_raw_data_health.py",
        ROOT / "publish_chatgpt_report_readme_and_check.py",
    ]

    for path in paths:
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name == "build_daily_theme_leadership_layer.py":
            start = text.index("DEPRECATED_DECISION_COLUMNS = [")
            end = text.index("\n\nBULLISH_WARRANT_SIGNALS", start)
            cleanup_block = text[start:end]
            for field in DAILY_DECISION_LAYER_FIELDS:
                if field != "daily_candidate_decision":
                    assert field in cleanup_block
            text = text[:start] + text[end:]
        for field in DAILY_DECISION_LAYER_FIELDS:
            assert field not in text, f"{path.as_posix()} still references {field}"


def test_formal_daily_report_dates_use_freshness_hard_gate_without_fallbacks() -> None:
    tracking_text = (ROOT / "scripts" / "tracking_utils.py").read_text(encoding="utf-8")
    start = tracking_text.index("def require_daily_report_ready_main_price_date(")
    end = tracking_text.index("\n\ndef load_price_history(", start)
    hard_gate_body = tracking_text[start:end]

    for field in ["main_price_date", "report_ready", "warrant_ready", "daily_pdf_ready"]:
        assert field in hard_gate_body
    assert "latest_stock_price_history_date" not in hard_gate_body
    assert "latest_price_date" not in hard_gate_body

    files = {
        ROOT / "build_daily_market_report_artifacts.py": [
            "require_daily_report_ready_main_price_date",
        ],
        ROOT / "scripts" / "build_theme_event_watch.py": [
            "main_price_date_from_freshness",
        ],
    }
    for path, required in files.items():
        text = path.read_text(encoding="utf-8")
        for literal in required:
            assert literal in text, f"{path.as_posix()} missing {literal}"

    forbidden = {
        ROOT / "build_daily_market_report_artifacts.py": [
            'dates = candidates["date"].map(normalize_date)',
            "all_candidates_latest.csv date 最大值",
            'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")',
        ],
        ROOT / "scripts" / "build_theme_event_watch.py": [
            'return datetime.now().strftime("%Y%m%d")',
            "or datetime.now()",
        ],
        ROOT / "build_warrant_flow_latest.py": [
            'datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")',
        ],
    }
    for path, literals in forbidden.items():
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            assert literal not in text, f"{path.as_posix()} still has date fallback {literal}"


def test_daily_workflow_uses_latest_only_volume_breakout_watch() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/build_volume_breakout_watch.py --latest-only" in text
    assert "python scripts/build_volume_breakout_watch.py\n" not in text
    assert text.count("python scripts/validate_daily_staged_paths.py") == 3
    assert "git add docs/latest/ || true" not in text
    assert "git add output/latest/ docs/latest/ || true" not in text


def test_daily_workflow_stages_complete_mirror_registry_before_first_commit_validation() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    commit_block = text[
        text.index("- name: Commit report artifacts, packets, and rules first") :
        text.index("- name: Wait briefly for GitHub Pages and raw propagation")
    ]

    stage_command = "python scripts/stage_daily_latest_mirrors.py"
    validate_command = "python scripts/validate_daily_staged_paths.py"
    assert commit_block.count(stage_command) == 1
    assert commit_block.index(stage_command) < commit_block.index(validate_command)


def test_complete_mirror_registry_stager_repairs_the_production_index_failure(
    tmp_path,
    monkeypatch,
) -> None:
    output_dir = tmp_path / "output" / "latest"
    docs_dir = tmp_path / "docs" / "latest"
    output_dir.mkdir(parents=True)
    docs_dir.mkdir(parents=True)
    mirror_names = validate_daily_staged_paths.registered_mirror_files()

    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.name", "mirror-registry-test"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.email", "mirror-registry-test@example.invalid"],
        cwd=tmp_path,
        check=True,
    )
    for index, name in enumerate(mirror_names):
        content = f"old-{index}\n".encode()
        (output_dir / name).write_bytes(content)
        (docs_dir / name).write_bytes(content)
    subprocess.run(
        ["git", "add", "--", "output/latest", "docs/latest"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "commit", "-m", "baseline"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    for index, name in enumerate(mirror_names):
        content = f"new-{index}\n".encode()
        (output_dir / name).write_bytes(content)
        (docs_dir / name).write_bytes(content)
    subprocess.run(["git", "add", "--", "output/latest"], cwd=tmp_path, check=True)
    non_indicator_docs = [
        f"docs/latest/{name}"
        for name in mirror_names
        if name not in validate_daily_staged_paths.INDICATOR_GUIDE_MIRROR_FILES
    ]
    subprocess.run(["git", "add", "--", *non_indicator_docs], cwd=tmp_path, check=True)

    monkeypatch.setattr(validate_daily_staged_paths, "ROOT", tmp_path)
    monkeypatch.setattr(validate_daily_staged_paths, "LATEST_DIR", output_dir)
    monkeypatch.setattr(validate_daily_staged_paths, "DOCS_LATEST_DIR", docs_dir)
    monkeypatch.setattr(stage_daily_latest_mirrors, "ROOT", tmp_path)
    monkeypatch.setattr(stage_daily_latest_mirrors, "LATEST_DIR", output_dir)
    monkeypatch.setattr(stage_daily_latest_mirrors, "DOCS_LATEST_DIR", docs_dir)

    errors_before = validate_daily_staged_paths.validate_docs_latest_mirrors()
    assert errors_before == [
        "git index docs/latest mirror differs from git index output/latest: "
        f"docs/latest/{name}"
        for name in validate_daily_staged_paths.INDICATOR_GUIDE_MIRROR_FILES
    ]

    assert stage_daily_latest_mirrors.main() == 0
    assert validate_daily_staged_paths.validate_docs_latest_mirrors() == []
    staged = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    expected = {
        path
        for name in mirror_names
        for path in (f"output/latest/{name}", f"docs/latest/{name}")
    }
    assert set(staged) == expected


def test_complete_mirror_registry_stager_rejects_a_missing_pair(
    tmp_path,
    monkeypatch,
) -> None:
    output_dir = tmp_path / "output" / "latest"
    docs_dir = tmp_path / "docs" / "latest"
    output_dir.mkdir(parents=True)
    docs_dir.mkdir(parents=True)
    missing_name = validate_daily_staged_paths.registered_mirror_files()[0]

    monkeypatch.setattr(stage_daily_latest_mirrors, "ROOT", tmp_path)
    monkeypatch.setattr(stage_daily_latest_mirrors, "LATEST_DIR", output_dir)
    monkeypatch.setattr(stage_daily_latest_mirrors, "DOCS_LATEST_DIR", docs_dir)
    monkeypatch.setattr(
        stage_daily_latest_mirrors,
        "registered_mirror_files",
        lambda: (missing_name,),
    )

    paths, errors = stage_daily_latest_mirrors.collect_mirror_paths()
    assert paths == []
    assert errors == [f"missing registered mirror pair: output/latest/{missing_name}"]


def test_daily_workflow_market_session_gate_is_main_only_and_fail_closed() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "market-session-preflight:" in text
    assert "Reject non-main production dispatch" in text
    assert "github.ref_name != 'main'" in text
    assert "python scripts/market_session_calendar.py --phase preflight" in text
    assert "record-market-closure:" in text
    assert "if: needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'" in text
    assert (
        "OFFICIAL_PRICE_TARGET_DATE: "
        "${{ needs.market-session-preflight.outputs.expected_main_price_date }}"
    ) in text
    assert "Verify open-confirmed target date" in text

    preflight_start = text.index("  market-session-preflight:")
    closure_start = text.index("  record-market-closure:")
    replay_start = text.index("  daily-pdf-dfkai-replay:")
    preflight_block = text[preflight_start:closure_start]
    closure_block = text[closure_start:replay_start]

    for forbidden in ("git commit", "git push", "pages.yml"):
        assert forbidden not in preflight_block
    for forbidden in (
        "fetch_official_daily_price.py",
        "git add data/daily_price/",
        "build_data_freshness_latest.py",
        "generate_chatgpt_side_daily_reports.py",
        "validate_chatgpt_daily_report_new_conversation_replay.py",
        "pages.yml",
    ):
        assert forbidden not in closure_block

    replay_block = boundaries.workflow_job_block(text, "daily-pdf-dfkai-replay")
    source_gate_block = boundaries.workflow_job_block(
        text,
        "daily-pdf-source-gate-validation",
    )
    assert "needs: [market-session-preflight, record-market-closure, daily-full-pipeline]" in replay_block
    assert "always()" in replay_block
    assert "needs.daily-full-pipeline.result == 'success'" in replay_block
    assert "inputs.validate_latest_daily_pdf_replay" not in replay_block
    assert "closed_scheduled" not in replay_block
    assert "closed_emergency" not in replay_block
    assert (
        "EXPECTED_MAIN_PRICE_DATE: "
        "${{ needs.market-session-preflight.outputs.expected_main_price_date }}"
    ) in replay_block
    assert '--expected-main-price-date "$EXPECTED_MAIN_PRICE_DATE"' in replay_block

    assert "runs-on: ubuntu-latest" in source_gate_block
    assert "inputs.validate_latest_daily_pdf_replay == true" in source_gate_block
    assert "needs.record-market-closure.result == 'success'" in source_gate_block
    assert "needs.market-session-preflight.outputs.market_status == 'closed_scheduled'" in source_gate_block
    assert "--source-gate-only" in source_gate_block
    assert '--validation-replay-main-price-date "$EXPECTED_MAIN_PRICE_DATE"' in source_gate_block
    assert 'source_gate_log="$RUNNER_TEMP/daily_pdf_source_gate_validation.log"' in source_gate_block
    assert 'tee "$source_gate_log"' in source_gate_block
    assert "path: ${{ runner.temp }}/daily_pdf_source_gate_validation.log" in source_gate_block
    assert "tee daily_pdf_source_gate_validation.log" not in source_gate_block
    assert "path: daily_pdf_source_gate_validation.log" not in source_gate_block
    assert "Install and validate DFKai-SB" not in source_gate_block
    assert "validate_chatgpt_daily_report_new_conversation_replay.py" not in source_gate_block
    assert "*.pdf" not in source_gate_block
    assert "closed_emergency" not in source_gate_block
    for forbidden in ("git commit", "git push", "pages.yml"):
        assert forbidden not in source_gate_block


def test_recent_price_gap_workflow_persists_shared_market_session_evidence() -> None:
    text = (ROOT / ".github" / "workflows" / "repair_recent_daily_price_gaps.yml").read_text(
        encoding="utf-8"
    )

    assert "Reject non-main production dispatch" in text
    assert "github.ref_name != 'main'" in text
    assert "ref: main" in text
    assert "data/market_calendar/exceptional_non_trading_days.csv" in text
    assert "output/latest/market_session_status_latest.json" in text
    assert "MARKET_SESSION_CHANGE_COUNT" in text
    assert "bash scripts/ci_push_with_retry.sh main 5" in text


def test_daily_workflow_requires_current_usable_warrant_fetch_with_evidence() -> None:
    daily_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    warrant_text = (ROOT / ".github" / "workflows" / "warrant_flow.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/fetch_official_warrant_daily.py --require-current-usable" in daily_text
    assert "timeout-minutes: 18" in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_MAX_SECONDS: "180"' in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_ATTEMPTS: "3"' in daily_text
    assert 'OFFICIAL_WARRANT_FETCH_RETRY_SLEEP_SECONDS: "180"' in daily_text
    assert "python scripts/validate_warrant_source_status.py --allow-noncritical-grace" in daily_text
    assert "- name: Upload warrant fetch evidence" in daily_text
    assert "output/latest/warrant_daily_fetch_latest.md" in daily_text
    assert "output/latest/warrant_source_status_latest.md" in daily_text
    assert "output/latest/warrant_source_status_latest.json" in daily_text
    assert "output/debug/warrant_fetch_debug_latest.md" in daily_text
    assert "output/debug/warrant_fetch_debug_latest.csv" in daily_text
    assert "python scripts/fetch_official_warrant_daily.py --require-current-usable" in warrant_text
    assert "python scripts/validate_warrant_source_status.py --require-formal-current" in warrant_text
    assert "validate_warrant_source_status.py --allow-noncritical-grace" not in warrant_text


def test_daily_workflow_publishes_as_published_model_snapshots() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    audit_source_publish_start = text.index(
        "- name: Publish and validate volume v2 audit-source snapshots"
    )
    lineage_audit_start = text.index(
        "- name: Build volume v2 lineage audit from published snapshots"
    )
    operation_adapter_start = text.index(
        "- name: Build volume v2 formal operation adapter"
    )
    remaining_artifacts_start = text.index("- name: Build remaining daily model artifacts")
    post_audit_publish_start = text.index(
        "- name: Publish and validate post-audit daily model snapshots"
    )
    monthly_revenue_start = text.index(
        "- name: Build monthly revenue coverage/backfill audit"
    )

    audit_source_publish_block = text[
        audit_source_publish_start:lineage_audit_start
    ]
    lineage_audit_block = text[lineage_audit_start:operation_adapter_start]
    operation_adapter_block = text[
        operation_adapter_start:remaining_artifacts_start
    ]
    post_audit_publish_block = text[
        post_audit_publish_start:monthly_revenue_start
    ]

    assert text.count("python scripts/update_daily_published_model_snapshots.py") == 2
    assert text.count("python scripts/build_volume_v2_warrant_lineage_history_audit.py") == 1
    assert text.count("python scripts/build_daily_volume_breakout_operation_section.py") == 1

    assert audit_source_publish_block.count("--artifact-id model_signals_for_report") == 2
    assert audit_source_publish_block.count("--artifact-id all_candidates_source_rows") == 2
    assert "--revision-reason daily_full_volume_v2_audit_sources" in (
        audit_source_publish_block
    )
    assert "--artifact-id data_freshness" not in audit_source_publish_block
    assert "--artifact-id volume_breakout_operation_section" not in (
        audit_source_publish_block
    )
    assert "python scripts/validate_daily_canonical_field_lineage.py" in (
        audit_source_publish_block
    )
    assert (
        audit_source_publish_block.index(
            "python scripts/update_daily_published_model_snapshots.py"
        )
        < audit_source_publish_block.index(
            "python scripts/validate_daily_published_model_snapshots.py"
        )
        < audit_source_publish_block.index(
            "python scripts/validate_daily_canonical_field_lineage.py"
        )
    )

    assert "python scripts/build_volume_v2_warrant_lineage_history_audit.py" in (
        lineage_audit_block
    )
    assert "python scripts/validate_volume_v2_warrant_lineage_history_audit.py" in (
        lineage_audit_block
    )
    assert "python scripts/build_daily_volume_breakout_operation_section.py" in (
        operation_adapter_block
    )
    assert (
        "python scripts/validate_daily_volume_breakout_operation_section.py --output-only"
        in operation_adapter_block
    )

    for artifact_id in (
        "data_freshness",
        "model_summary_for_report",
        "model_registry",
        "model_parameters",
        "volume_breakout_operation_section",
        "volume_breakout_operation_evidence_audit",
        "w_bottom_right_side_operation_section",
        "neckline_volume_breakout_confirmation_operation_section",
    ):
        assert post_audit_publish_block.count(f"--artifact-id {artifact_id}") == 1
    assert "--revision-reason daily_full_post_audit_artifacts" in (
        post_audit_publish_block
    )
    assert "--artifact-id model_signals_for_report" not in post_audit_publish_block
    assert "--artifact-id all_candidates_source_rows" not in post_audit_publish_block
    assert (
        "python scripts/build_volume_v2_warrant_lineage_history_audit.py"
        not in post_audit_publish_block
    )
    assert any(
        line.strip() == "python scripts/validate_daily_published_model_snapshots.py"
        for line in post_audit_publish_block.splitlines()
    )
    assert (
        post_audit_publish_block.index(
            "python scripts/update_daily_published_model_snapshots.py"
        )
        < post_audit_publish_block.index(
            "python scripts/validate_daily_published_model_snapshots.py"
        )
        < post_audit_publish_block.index(
            "python scripts/validate_daily_canonical_field_lineage.py"
        )
        < post_audit_publish_block.index(
            "python scripts/validate_volume_v2_warrant_lineage_history_audit.py"
        )
    )

    assert "git add output/history/daily_candidate_models/ || true" in text
    assert "git add output/history/daily_model_snapshots/ || true" not in text
    assert (
        "git add output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv"
    ) not in text
    assert "python scripts/stage_daily_published_snapshot_revisions.py" in text
    assert (
        text.index("- name: Build daily candidate model layer")
        < audit_source_publish_start
        < lineage_audit_start
        < operation_adapter_start
        < remaining_artifacts_start
        < text.index("- name: Guard daily freshness before publishing")
        < text.index("- name: Build daily market report artifacts")
        < post_audit_publish_start
        < text.index("- name: Commit report artifacts, packets, and rules first")
    )
    commit_block = text[
        text.index("- name: Commit report artifacts, packets, and rules first") :
        text.index("- name: Wait briefly for GitHub Pages and raw propagation")
    ]
    assert "python scripts/validate_daily_published_model_snapshots.py" in commit_block


def test_docs_daily_rules_match_authoritative_rules() -> None:
    authoritative = (ROOT / "rules" / "daily_stock_candidate_rules.md").read_text(
        encoding="utf-8"
    )
    published = (ROOT / "docs" / "rules" / "daily_stock_candidate_rules.md").read_text(
        encoding="utf-8"
    )

    assert published == authoritative
    assert "six ChatGPT-side PDF deliverables" in published
    assert "four ChatGPT-side PDF deliverables" not in published
    assert "approximately 126 trading days" in published
    assert "180-day windows" not in published


def test_docs_master_rules_match_authoritative_rules() -> None:
    authoritative = (ROOT / "rules" / "master_priority_rules.md").read_text(
        encoding="utf-8"
    )
    published = (ROOT / "docs" / "rules" / "master_priority_rules.md").read_text(
        encoding="utf-8"
    )

    assert published == authoritative


def test_thread_workflow_points_to_canonical_pdf_generator() -> None:
    text = (ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md").read_text(encoding="utf-8")

    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in text
    assert "scripts/generate_chatgpt_side_daily_reports.py" in text
    assert "renderer, not the official entrypoint" in text
    assert "generate_repo_chatgpt_side_reports.py" not in text


def test_chatgpt_daily_usage_prompt_uses_official_entrypoint_not_pages_first() -> None:
    text = (ROOT / "docs" / "CHATGPT_DAILY_REPORT_USAGE_PROMPT.md").read_text(
        encoding="utf-8"
    )

    assert "scripts/run_chatgpt_daily_report_entrypoint.py --source-gate-only" in text
    assert "git show origin/main" in text
    assert "chatgpt_daily_report_packet_latest.txt" in text
    assert "六份" in text
    assert "chatgpt_daily_report_runtime_manifest.json" in text
    assert "優先讀 GitHub Pages" not in text
    assert "如果 Pages 讀不到，再讀 raw" not in text
    assert "請同時提供四份成品" not in text
    assert "daily_market_curated_pdf_pages_url" not in text


def test_repo_agent_rules_default_to_independent_business_surfaces() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    workflow_text = (ROOT / "docs" / "CODEX_THREAD_WORKFLOW.md").read_text(
        encoding="utf-8"
    )

    assert "All business-facing code in this repository defaults to independent ownership." in text
    assert "Changing A must not silently change B." in text
    assert "Stock model parameters, thresholds, scoring weights, ranking rules, and gates" in text
    assert "Business-facing code defaults to independent ownership." in workflow_text


def test_repo_agent_rules_require_completion_claim_evidence() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    assert "Completion Claim Evidence Gate" in text
    assert "completion_state=complete" in text
    assert "PR number and URL" in text
    assert "Merge commit on `main`" in text
    assert "Post-merge official `main` workflow run id and conclusion" in text
    assert "Local post-merge validators or tests" in text
    assert "Runtime behavior or user-facing artifact inspection result" in text
    assert "Direct clickable links to generated PDF files" in text
    assert "folder plus exact PDF filenames" in text
    assert "Final `git status --short --branch` state" in text
    assert "`remaining blocker`" in text
    assert "main_workflow_passed_pending_artifact_inspection" in text
    assert "renderer consumed the dedicated adapter" in text
    assert "PDF contract/replay validation passed after merge" in text
    assert "produced PDF link evidence" in text
    assert "no generated PDF file" in text
    assert "PDF folder\nlink is available" in text


def test_formal_model_change_rules_include_pdf_operation_adapter_gate() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    model_contract = (ROOT / "docs" / "stock_model_contract_governance.md").read_text(
        encoding="utf-8"
    )
    pdf_contract = (ROOT / "docs" / "daily_pdf_contract_consumer_governance.md").read_text(
        encoding="utf-8"
    )

    for text in (agents, model_contract):
        assert "operation-row adapter" in text
        assert "model_operation_readiness_latest.csv" in text
        assert "pdf_integration_status=pdf_integrated_daily_adapter" in text

    assert "presentation_allowed=False" in agents
    assert "PDF renderer must not convert candidate signal rows" in agents
    assert "daily PDF renderer must not infer buyable, active, pending, exit, or stop-loss lifecycle rows" in model_contract
    assert "Registry approval alone does not authorize the PDF renderer to infer lifecycle" in pdf_contract


def test_formal_model_change_rules_require_close_confirmed_operation_prices() -> None:
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    model_contract = (ROOT / "docs" / "stock_model_contract_governance.md").read_text(
        encoding="utf-8"
    )
    price_pullback_spec = (
        ROOT / "docs" / "specs" / "price_pullback_23ema_operation_candidate_spec.md"
    ).read_text(encoding="utf-8")

    for text in (agents, model_contract):
        assert "Formal operation buy/sell/stop/profit-taking rules" in text
        assert "close-confirmed by" in text
        assert "next trading day open" in text
        assert "after a qualifying close confirmation" in text
        assert "same-day close" in text
        assert "intraday high/low as formal entry" in text
        assert "profit-taking, win, failure, or realized-return prices" in text
        assert "research-only observation" in text
        assert "price_pullback_23ema" in text
        assert "research_only_intraday_trigger" in text
        assert "close_prev20_high_break_same_day_close" in text

    assert "Formal Price Confirmation Boundary" in price_pullback_spec
    assert "Intraday high/low observations must not be used as" in price_pullback_spec
    assert "realized execution prices" in price_pullback_spec
    assert "intraday high touches the signal-day previous 20-day high" in price_pullback_spec
    assert "research_only_intraday_trigger" in price_pullback_spec
    assert "close breaks the signal-day previous 20-day high, then sell at the next" in price_pullback_spec
    assert "close_prev20_high_break_same_day_close" in price_pullback_spec
    assert "known only after that close" in price_pullback_spec
    assert boundaries.validate_model_operation_price_confirmation_rules() == []


def test_operation_price_confirmation_validator_fails_closed_when_rule_missing(
    tmp_path,
    monkeypatch,
) -> None:
    rule_file = tmp_path / "rule.md"
    rule_file.write_text(
        "Formal operation buy/sell/stop/profit-taking rules must be close-confirmed by default.",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        boundaries,
        "MODEL_OPERATION_PRICE_CONFIRMATION_RULE_LITERALS",
        {
            rule_file: {
                "must not use intraday high/low as formal entry, exit, stop, profit-taking, win, failure, or realized-return prices": (
                    "test operation price rule"
                ),
            },
        },
    )

    errors = boundaries.validate_model_operation_price_confirmation_rules()

    assert errors
    assert "test operation price rule" in errors[0]


def test_daily_staged_path_validator_accepts_current_staged_set() -> None:
    result = subprocess.run(
        ["python", "scripts/validate_daily_staged_paths.py"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_daily_staged_path_forbidden_patterns_cover_tdcc_and_research_outputs() -> None:
    examples = [
        "output/latest/tdcc_weekly_candidate_full_latest.pdf",
        "docs/latest/tdcc_signal_effectiveness_latest.md",
        "output/history/research/daily_model_parameter_research.csv",
        "output/latest/weekly_surge_strict_parameter_search_latest.csv",
        "output/latest/daily_model_parameter_recommendations_latest.md",
    ]

    for example in examples:
        assert any(
            validate_daily_staged_paths.fnmatch.fnmatch(example, pattern)
            for pattern in validate_daily_staged_paths.FORBIDDEN_STAGED_PATTERNS
        ), example


def test_research_workflow_does_not_stage_generated_recommendations_as_config() -> None:
    workflow = (ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml").read_text(
        encoding="utf-8"
    )
    recommender = (ROOT / "scripts" / "build_daily_model_parameter_recommendations.py").read_text(
        encoding="utf-8"
    )

    assert "git add config/daily_model_parameter_recommendations.csv" not in workflow
    assert "CONFIG_CSV" not in recommender
    assert 'Path("config/daily_model_parameter_recommendations.csv")' not in recommender


def test_historical_structured_source_replay_workflow_is_fail_closed() -> None:
    text = boundaries.HISTORICAL_SOURCE_REPLAY_WORKFLOW.read_text(encoding="utf-8")

    assert boundaries.validate_historical_source_replay_workflow(text) == []


def test_historical_structured_source_replay_workflow_wires_optional_price_high_water() -> None:
    text = boundaries.HISTORICAL_SOURCE_REPLAY_WORKFLOW.read_text(encoding="utf-8")

    assert "price_history_high_water_date:" in text
    assert "PRICE_HISTORY_HIGH_WATER_DATE: ${{ inputs.price_history_high_water_date }}" in text
    assert text.count(
        '--price-history-high-water-date "$PRICE_HISTORY_HIGH_WATER_DATE"'
    ) == 4
    assert 'if [ -z "$PRICE_HISTORY_HIGH_WATER_DATE" ]; then\n            git add data/daily_price/' in text
    assert "git add output/latest/official_daily_price_latest.csv" in text


def test_historical_structured_source_replay_rejects_broad_stage_and_retry_push() -> None:
    text = boundaries.HISTORICAL_SOURCE_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    text += "\nrun: git add -A\nrun: scripts/ci_push_with_retry.sh\n"

    errors = boundaries.validate_historical_source_replay_workflow(text)

    assert any("broad-stage" in error for error in errors)
    assert any("moving main" in error for error in errors)


def test_historical_structured_source_replay_rejects_dependency_validator_order_swap() -> None:
    text = boundaries.HISTORICAL_SOURCE_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    text = text.replace("Install replay dependencies", "TEMP STEP NAME", 1)
    text = text.replace(
        "Validate repository automation boundaries",
        "Install replay dependencies",
        1,
    )
    text = text.replace("TEMP STEP NAME", "Validate repository automation boundaries", 1)

    errors = boundaries.validate_historical_source_replay_workflow(text)

    assert any("fail-closed order" in error for error in errors)
