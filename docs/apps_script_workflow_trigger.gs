const GITHUB_OWNER = "LeoChen0727";
const GITHUB_REPO = "tdcc-weekly-report";
const GITHUB_REF = "main";
const GITHUB_API_VERSION = "2022-11-28";
const GITHUB_PAT_PROPERTY = "GITHUB_PAT";
const GITHUB_TOKEN_FALLBACK_PROPERTY = "GITHUB_TOKEN";
const RESPONSE_PREVIEW_MAX_CHARS = 1200;
const TDCC_CHAIN_STATE_PROPERTY = "TDCC_INDIVIDUAL_REFRESH_CHAIN_STATE";
const TDCC_CHAIN_DISPATCH_HISTORY_PROPERTY = "TDCC_INDIVIDUAL_REFRESH_DISPATCH_HISTORY";
const TDCC_CHAIN_HISTORY_LIMIT = 16;
const TDCC_CHAIN_CORRELATION_WINDOW_MS = 10 * 60 * 1000;
const TDCC_CHAIN_MAIN_EVIDENCE_WINDOW_MS = 30 * 60 * 1000;
const TDCC_CHAIN_POLL_MINUTES = 5;
const TDCC_DATA_RETRY_DELAY_MS = 30 * 60 * 1000;
const TDCC_RETRYABLE_DATA_STEPS = [
  "Wait for expected TDCC period",
  "Fetch current TDCC snapshot",
  "Repair TDCC weekly history continuity",
];
const TDCC_WEEKLY_WORKFLOW = "tdcc_weekly.yml";
const INDIVIDUAL_REFRESH_WORKFLOW = "individual_stock_data_refresh.yml";
const TDCC_RUN_STATUS_PATH = "output/latest/tdcc_weekly_run_status.md";
const TDCC_VALIDATION_PATH = "output/latest/tdcc_weekly_candidate_report_validation_latest.json";
const TDCC_OFFICIAL_DATE_SOURCE = "report_ready_csv_signal_date";
const INDIVIDUAL_REFRESH_RUN_STATUS_PATH =
  "output/latest/individual_stock_reports/individual_stock_refresh_run_status_latest.json";

function getGithubToken_() {
  const properties = PropertiesService.getScriptProperties();
  const token =
    properties.getProperty(GITHUB_PAT_PROPERTY) ||
    properties.getProperty(GITHUB_TOKEN_FALLBACK_PROPERTY);
  if (!token) {
    throw new Error(
      "Missing Script Property: " +
        GITHUB_PAT_PROPERTY +
        " (preferred) or " +
        GITHUB_TOKEN_FALLBACK_PROPERTY +
        ". Configure a token with repository Actions read/write and Contents read permissions for " +
        GITHUB_OWNER +
        "/" +
        GITHUB_REPO +
        "."
    );
  }
  return token.trim();
}

function responsePreview_(responseBody) {
  if (!responseBody) {
    return "";
  }
  if (responseBody.length <= RESPONSE_PREVIEW_MAX_CHARS) {
    return responseBody;
  }
  return responseBody.slice(0, RESPONSE_PREVIEW_MAX_CHARS) + "...[truncated]";
}

function githubStatusHint_(statusCode) {
  if (statusCode === 401) {
    return "token missing, expired, or invalid";
  }
  if (statusCode === 403) {
    return "token lacks Actions read/write or Contents read permission, or is blocked by policy";
  }
  if (statusCode === 404) {
    return "repo or workflow is not visible to the token";
  }
  if (statusCode === 422) {
    return "invalid workflow dispatch payload or ref";
  }
  return "unexpected GitHub API status";
}

function githubApi_(method, path, payload) {
  const token = getGithubToken_();
  const url = "https://api.github.com" + path;
  const options = {
    method: method,
    headers: {
      Accept: "application/vnd.github+json",
      Authorization: "Bearer " + token,
      "X-GitHub-Api-Version": GITHUB_API_VERSION,
    },
    muteHttpExceptions: true,
  };

  if (payload !== undefined && payload !== null) {
    options.contentType = "application/json";
    options.payload = JSON.stringify(payload);
  }

  const response = UrlFetchApp.fetch(url, options);
  const statusCode = response.getResponseCode();
  const responseBody = response.getContentText();

  Logger.log("GitHub API: " + method + " " + url);
  Logger.log("Status code: " + statusCode);
  Logger.log("Response body: " + responsePreview_(responseBody));

  return {
    statusCode: statusCode,
    responseBody: responseBody,
  };
}

function assertGithubSuccess_(result, actionName) {
  if (result.statusCode === 200 || result.statusCode === 201 || result.statusCode === 202 || result.statusCode === 204) {
    return;
  }
  throw new Error(
    actionName +
      " failed: HTTP " +
      result.statusCode +
      " (" +
      githubStatusHint_(result.statusCode) +
      ") " +
      responsePreview_(result.responseBody)
  );
}

function dispatchWorkflow_(workflowFile, inputs) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/workflows/" +
    encodeURIComponent(workflowFile) +
    "/dispatches";

  const payload = {
    ref: GITHUB_REF,
  };

  if (inputs && Object.keys(inputs).length > 0) {
    payload.inputs = inputs;
  }

  const result = githubApi_("post", path, payload);
  assertGithubSuccess_(result, "Dispatch " + workflowFile);
  Logger.log("Dispatched workflow: " + workflowFile + " ref=" + GITHUB_REF);
  return result;
}

function githubJson_(method, path, payload, actionName) {
  const result = githubApi_(method, path, payload);
  assertGithubSuccess_(result, actionName);
  if (!result.responseBody) {
    return {};
  }
  return JSON.parse(result.responseBody);
}

function listWorkflowRuns_(workflowFile, perPage) {
  const runLimit = perPage || 5;
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/workflows/" +
    encodeURIComponent(workflowFile) +
    "/runs?branch=" +
    encodeURIComponent(GITHUB_REF) +
    "&event=workflow_dispatch&per_page=" +
    encodeURIComponent(String(runLimit));

  return githubJson_("get", path, null, "List runs " + workflowFile);
}

function getWorkflowRun_(runId) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/runs/" +
    encodeURIComponent(String(runId));
  return githubJson_("get", path, null, "Read workflow run " + runId);
}

function getWorkflowJobs_(runId) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/runs/" +
    encodeURIComponent(String(runId)) +
    "/jobs?per_page=100";
  return githubJson_("get", path, null, "Read workflow jobs " + runId);
}

function failedWorkflowStepNames_(runId) {
  const data = getWorkflowJobs_(runId);
  const failed = [];
  (data.jobs || []).forEach(function (job) {
    (job.steps || []).forEach(function (step) {
      if (step.conclusion === "failure") {
        failed.push(step.name);
      }
    });
  });
  return failed;
}

function isRetryableTdccDataFailure_(runId) {
  const failedSteps = failedWorkflowStepNames_(runId);
  return failedSteps.length > 0 && failedSteps.every(function (stepName) {
    return TDCC_RETRYABLE_DATA_STEPS.indexOf(stepName) >= 0;
  });
}

function getMainRefSha_() {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/git/ref/heads/" +
    encodeURIComponent(GITHUB_REF);
  const data = githubJson_("get", path, null, "Read main ref");
  if (!data.object || !data.object.sha) {
    throw new Error("GitHub main ref response did not contain object.sha");
  }
  return data.object.sha;
}

function encodeRepositoryPath_(filePath) {
  return filePath
    .split("/")
    .map(function (part) {
      return encodeURIComponent(part);
    })
    .join("/");
}

function getRepositoryTextFile_(filePath, refName) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/contents/" +
    encodeRepositoryPath_(filePath) +
    "?ref=" +
    encodeURIComponent(refName || GITHUB_REF);
  const data = githubJson_("get", path, null, "Read repository file " + filePath);
  if (data.type !== "file" || !data.content) {
    throw new Error("Repository contents response is not a file: " + filePath);
  }
  const compactBase64 = data.content.replace(/\s/g, "");
  return Utilities.newBlob(Utilities.base64Decode(compactBase64)).getDataAsString("UTF-8");
}

function getLatestCommitForPath_(filePath) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/commits?sha=" +
    encodeURIComponent(GITHUB_REF) +
    "&path=" +
    encodeURIComponent(filePath) +
    "&per_page=1";
  const commits = githubJson_("get", path, null, "Read latest commit for " + filePath);
  if (!Array.isArray(commits) || commits.length !== 1 || !commits[0].sha) {
    throw new Error("No main commit found for path: " + filePath);
  }
  return commits[0].sha;
}

function compareCommits_(baseSha, headSha) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/compare/" +
    encodeURIComponent(baseSha) +
    "..." +
    encodeURIComponent(headSha);
  return githubJson_("get", path, null, "Compare commits " + baseSha + "..." + headSha);
}

function assertCommitContained_(baseSha, headSha, description) {
  const comparison = compareCommits_(baseSha, headSha);
  if (comparison.status !== "ahead" && comparison.status !== "identical") {
    throw new Error(
      description +
        " is not contained in the required head: base=" +
        baseSha +
        " head=" +
        headSha +
        " status=" +
        comparison.status
    );
  }
}

function latestWorkflowRunId_(workflowFile) {
  const runs = listWorkflowRuns_(workflowFile, 20).workflow_runs || [];
  return runs.reduce(function (latest, run) {
    return Math.max(latest, Number(run.id) || 0);
  }, 0);
}

function findCorrelatedWorkflowRuns_(workflowFile, baselineRunId, dispatchedAt) {
  const dispatchedAtMs = new Date(dispatchedAt).getTime();
  const earliestMs = dispatchedAtMs - 15000;
  const latestMs = dispatchedAtMs + TDCC_CHAIN_CORRELATION_WINDOW_MS;
  const runs = listWorkflowRuns_(workflowFile, 20).workflow_runs || [];
  return runs
    .filter(function (run) {
      const createdAtMs = new Date(run.created_at).getTime();
      return (
        Number(run.id) > Number(baselineRunId || 0) &&
        run.event === "workflow_dispatch" &&
        run.head_branch === GITHUB_REF &&
        createdAtMs >= earliestMs &&
        createdAtMs <= latestMs
      );
    })
    .sort(function (left, right) {
      return Number(left.id) - Number(right.id);
    });
}

function nowIso_() {
  return new Date().toISOString();
}

function taipeiYyyyMmDd_() {
  return Utilities.formatDate(new Date(), "Asia/Taipei", "yyyyMMdd");
}

function readTdccChainState_() {
  const raw = PropertiesService.getScriptProperties().getProperty(TDCC_CHAIN_STATE_PROPERTY);
  return raw ? JSON.parse(raw) : null;
}

function writeTdccChainState_(state) {
  state.updated_at = nowIso_();
  PropertiesService.getScriptProperties().setProperty(TDCC_CHAIN_STATE_PROPERTY, JSON.stringify(state));
  Logger.log("TDCC chain state: " + JSON.stringify(state));
}

function readTdccDispatchHistory_() {
  const raw = PropertiesService.getScriptProperties().getProperty(
    TDCC_CHAIN_DISPATCH_HISTORY_PROPERTY
  );
  if (!raw) {
    return [];
  }
  const history = JSON.parse(raw);
  return Array.isArray(history) ? history : [];
}

function writeTdccDispatchHistory_(history) {
  PropertiesService.getScriptProperties().setProperty(
    TDCC_CHAIN_DISPATCH_HISTORY_PROPERTY,
    JSON.stringify(history.slice(-TDCC_CHAIN_HISTORY_LIMIT))
  );
}

function tdccChainIdentity_(runId, signalDate, outputCommitSha) {
  if (!runId || !/^\d{8}$/.test(String(signalDate || ""))) {
    throw new Error("TDCC chain identity requires a run id and eight-digit signal_date");
  }
  if (!/^[0-9a-f]{40}$/.test(String(outputCommitSha || ""))) {
    throw new Error("TDCC chain identity requires a 40-character output commit SHA");
  }
  return [String(runId), String(signalDate), String(outputCommitSha)].join(":");
}

function tdccDispatchAlreadyRecorded_(runId, signalDate, outputCommitSha) {
  const chainKey = tdccChainIdentity_(runId, signalDate, outputCommitSha);
  return readTdccDispatchHistory_().some(function (item) {
    return item.chain_key === chainKey;
  });
}

function recordTdccDispatch_(state) {
  const history = readTdccDispatchHistory_();
  const existingIndex = history.findIndex(function (item) {
    return item.chain_key === state.chain_key;
  });
  const entry = {
    chain_key: state.chain_key,
    tdcc_run_id: state.tdcc_run_id,
    signal_date: state.signal_date,
    tdcc_head_sha: state.tdcc_head_sha,
    tdcc_output_commit_sha: state.tdcc_output_commit_sha,
    downstream_dispatched_at: state.downstream_dispatched_at,
    downstream_run_id: state.downstream_run_id || null,
    downstream_head_sha: state.downstream_head_sha || null,
    downstream_output_commit_sha: state.downstream_output_commit_sha || null,
    phase: state.phase,
    conclusion: state.downstream_conclusion || null,
    error: state.error || null,
    recorded_at: nowIso_(),
  };
  if (existingIndex >= 0) {
    history[existingIndex] = entry;
  } else {
    history.push(entry);
  }
  writeTdccDispatchHistory_(history);
}

function isTerminalTdccChainPhase_(phase) {
  return [
    "complete",
    "duplicate_skipped",
    "tdcc_dispatch_failed",
    "tdcc_failed",
    "tdcc_run_ambiguous",
    "tdcc_run_unconfirmed",
    "tdcc_main_gate_failed",
    "downstream_run_ambiguous",
    "downstream_run_unconfirmed",
    "downstream_failed",
    "downstream_main_gate_failed",
  ].indexOf(phase) >= 0;
}

function failTdccChain_(state, phase, message) {
  state.phase = phase;
  state.error = message;
  writeTdccChainState_(state);
  throw new Error(message);
}

function scheduleTdccDataRetry_(state, tdccRun) {
  state.phase = "tdcc_data_retry_wait";
  state.retry_count = Number(state.retry_count || 0) + 1;
  state.last_retryable_run_id = String(tdccRun.id);
  state.last_retryable_run_url = tdccRun.html_url;
  state.last_retryable_conclusion = tdccRun.conclusion;
  state.next_retry_at = new Date(Date.now() + TDCC_DATA_RETRY_DELAY_MS).toISOString();
  delete state.error;
  writeTdccChainState_(state);
}

function dispatchScheduledTdccRetry_(state) {
  if (!state.next_retry_at || Date.now() < new Date(state.next_retry_at).getTime()) {
    Logger.log("Waiting for TDCC data retry window: " + state.next_retry_at);
    return false;
  }
  state.tdcc_baseline_run_id = latestWorkflowRunId_(TDCC_WEEKLY_WORKFLOW);
  state.tdcc_dispatched_at = nowIso_();
  delete state.tdcc_run_id;
  delete state.tdcc_head_sha;
  delete state.tdcc_run_url;
  delete state.tdcc_status;
  delete state.tdcc_conclusion;
  delete state.next_retry_at;
  state.phase = "tdcc_retry_dispatching";
  writeTdccChainState_(state);
  try {
    dispatchWorkflow_(TDCC_WEEKLY_WORKFLOW, {
      target_as_of_date: state.target_as_of_date,
    });
  } catch (error) {
    state.phase = "tdcc_retry_dispatch_uncertain";
    state.error = error.message;
    writeTdccChainState_(state);
    throw error;
  }
  state.phase = "tdcc_dispatched";
  writeTdccChainState_(state);
  return true;
}

function readTdccPublishedEvidence_(tdccRun) {
  const statusText = getRepositoryTextFile_(TDCC_RUN_STATUS_PATH, GITHUB_REF);
  const runMatch = statusText.match(/actions\/runs\/(\d+)/);
  const commitMatch = statusText.match(/- commit: `([0-9a-f]{40})`/);
  if (!runMatch || !commitMatch) {
    throw new Error("TDCC main status file is missing github_run or commit evidence");
  }
  if (String(runMatch[1]) !== String(tdccRun.id) || commitMatch[1] !== tdccRun.head_sha) {
    return null;
  }

  const validation = JSON.parse(getRepositoryTextFile_(TDCC_VALIDATION_PATH, GITHUB_REF));
  if (validation.status !== "pass" || !/^\d{8}$/.test(String(validation.signal_date || ""))) {
    throw new Error("TDCC main validation must contain status=pass and an eight-digit signal_date");
  }
  if (
    !validation.date_contract ||
    validation.date_contract.date_source !== TDCC_OFFICIAL_DATE_SOURCE
  ) {
    throw new Error(
      "TDCC main validation date source must be " + TDCC_OFFICIAL_DATE_SOURCE
    );
  }

  const outputCommitSha = getLatestCommitForPath_(TDCC_RUN_STATUS_PATH);
  const mainSha = getMainRefSha_();
  assertCommitContained_(tdccRun.head_sha, outputCommitSha, "TDCC workflow head");
  assertCommitContained_(outputCommitSha, mainSha, "TDCC output commit");

  return {
    signal_date: String(validation.signal_date),
    tdcc_output_commit_sha: outputCommitSha,
    main_sha_at_gate: mainSha,
  };
}

function readWorkflowOutputEvidence_(workflowRun, runStatusPath, expectedSignalDate) {
  const runStatus = JSON.parse(getRepositoryTextFile_(runStatusPath, GITHUB_REF));
  if (
    runStatus.status !== "pass" ||
    runStatus.workflow !== INDIVIDUAL_REFRESH_WORKFLOW ||
    String(runStatus.github_run_id) !== String(workflowRun.id) ||
    runStatus.github_head_sha !== workflowRun.head_sha ||
    runStatus.official_signal_date !== expectedSignalDate ||
    !runStatus.date_contract ||
    runStatus.date_contract.date_source !== TDCC_OFFICIAL_DATE_SOURCE
  ) {
    throw new Error(
      "Individual refresh main run-status does not uniquely match the tracked run and signal date"
    );
  }

  const outputCommitSha = getLatestCommitForPath_(runStatusPath);
  const mainSha = getMainRefSha_();
  assertCommitContained_(workflowRun.head_sha, outputCommitSha, "Workflow output commit");
  assertCommitContained_(outputCommitSha, mainSha, "Workflow output commit on main");
  return {
    output_commit_sha: outputCommitSha,
    main_sha: mainSha,
  };
}

function correlationWindowExpired_(dispatchedAt) {
  return Date.now() > new Date(dispatchedAt).getTime() + TDCC_CHAIN_CORRELATION_WINDOW_MS;
}

function mainEvidenceWindowExpired_(runUpdatedAt) {
  return Date.now() > new Date(runUpdatedAt).getTime() + TDCC_CHAIN_MAIN_EVIDENCE_WINDOW_MS;
}

function withScriptLock_(callback) {
  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    return callback();
  } finally {
    lock.releaseLock();
  }
}

function logLatestWorkflowRuns_(workflowFile) {
  const runs = listWorkflowRuns_(workflowFile);
  const items = runs.workflow_runs || [];

  Logger.log("Latest workflow_dispatch runs for " + workflowFile + ":");
  items.forEach(function (run) {
    Logger.log(
      [
        "id=" + run.id,
        "status=" + run.status,
        "conclusion=" + run.conclusion,
        "created_at=" + run.created_at,
        "html_url=" + run.html_url,
      ].join(" | ")
    );
  });
}

function logLatestWorkflowRunsSafe_(workflowFile) {
  try {
    logLatestWorkflowRuns_(workflowFile);
  } catch (error) {
    Logger.log("Non-fatal: could not list latest runs for " + workflowFile + ": " + error.message);
  }
}

function assertWorkflowAccessible_(workflowFile) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/workflows/" +
    encodeURIComponent(workflowFile);
  const result = githubApi_("get", path, null);
  assertGithubSuccess_(result, "Access workflow " + workflowFile);
}

function testGithubTokenAndWorkflowAccess() {
  const path = "/repos/" + GITHUB_OWNER + "/" + GITHUB_REPO + "/actions/workflows";
  const result = githubApi_("get", path, null);
  assertGithubSuccess_(result, "List workflows");
  Logger.log("GitHub token and workflow access OK.");
}

function diagnoseDailyStockMonitorTrigger() {
  testGithubTokenAndWorkflowAccess();
  assertWorkflowAccessible_("daily_full_pipeline.yml");
  logLatestWorkflowRunsSafe_("daily_full_pipeline.yml");
  Logger.log("Daily stock monitor diagnostics OK. If the scheduled trigger still fails, run installDailyStockMonitorTrigger().");
}

function diagnoseDailyPriceGapRepairTrigger() {
  testGithubTokenAndWorkflowAccess();
  assertWorkflowAccessible_("repair_recent_daily_price_gaps.yml");
  logLatestWorkflowRunsSafe_("repair_recent_daily_price_gaps.yml");
  Logger.log("Daily price gap repair diagnostics OK. If the scheduled trigger still fails, run installDailyPriceGapRepairTrigger().");
}

function diagnoseTdccHistoryGapRepairTrigger() {
  testGithubTokenAndWorkflowAccess();
  assertWorkflowAccessible_("repair_tdcc_monthly_history_gaps.yml");
  logLatestWorkflowRunsSafe_("repair_tdcc_monthly_history_gaps.yml");
  Logger.log("TDCC monthly history gap repair diagnostics OK. If the scheduled trigger still fails, run installTdccHistoryGapRepairTrigger().");
}

function triggerDailyStockMonitor() {
  const dayOfWeek = new Date().getDay();
  if (dayOfWeek === 0 || dayOfWeek === 6) {
    Logger.log("Skip daily full pipeline on weekend.");
    return;
  }
  dispatchWorkflow_("daily_full_pipeline.yml", {
    run_raw_health_check: "false",
  });
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("daily_full_pipeline.yml");
}

function triggerDailyFullPipeline() {
  triggerDailyStockMonitor();
}

function triggerDailyPriceGapRepair() {
  const dayOfWeek = new Date().getDay();
  if (dayOfWeek === 0 || dayOfWeek === 6) {
    Logger.log("Skip recent daily price gap repair on weekend.");
    return;
  }
  dispatchWorkflow_("repair_recent_daily_price_gaps.yml", {
    lookback_days: "7",
    max_repair_dates: "5",
  });
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("repair_recent_daily_price_gaps.yml");
}

function triggerTdccWeeklyReport() {
  withScriptLock_(function () {
    const existing = readTdccChainState_();
    if (existing && !isTerminalTdccChainPhase_(existing.phase)) {
      throw new Error(
        "TDCC-to-individual refresh chain is already active: " + JSON.stringify(existing)
      );
    }

    const state = {
      version: 1,
      phase: "tdcc_dispatching",
      tdcc_dispatched_at: nowIso_(),
      target_as_of_date: taipeiYyyyMmDd_(),
      tdcc_baseline_run_id: latestWorkflowRunId_(TDCC_WEEKLY_WORKFLOW),
      tdcc_base_main_sha: getMainRefSha_(),
    };
    writeTdccChainState_(state);
    try {
      dispatchWorkflow_(TDCC_WEEKLY_WORKFLOW, {
        target_as_of_date: state.target_as_of_date,
      });
    } catch (error) {
      state.phase = "tdcc_dispatch_failed";
      state.error = error.message;
      writeTdccChainState_(state);
      throw error;
    }
    state.phase = "tdcc_dispatched";
    writeTdccChainState_(state);
  });
  Logger.log("TDCC weekly dispatch accepted; state-aware orchestration will poll run and main evidence.");
}

function orchestrateTdccIndividualRefresh() {
  return withScriptLock_(function () {
    const state = readTdccChainState_();
    if (!state) {
      Logger.log("No TDCC-to-individual refresh chain state exists.");
      return;
    }
    if (isTerminalTdccChainPhase_(state.phase)) {
      Logger.log("TDCC-to-individual refresh chain is terminal: " + state.phase);
      return;
    }
    if (state.phase === "tdcc_data_retry_wait") {
      dispatchScheduledTdccRetry_(state);
      return;
    }

    if (!state.tdcc_run_id) {
      const candidates = findCorrelatedWorkflowRuns_(
        TDCC_WEEKLY_WORKFLOW,
        state.tdcc_baseline_run_id,
        state.tdcc_dispatched_at
      );
      if (candidates.length > 1) {
        failTdccChain_(
          state,
          "tdcc_run_ambiguous",
          "More than one TDCC run matched the dispatch window: " +
            candidates.map(function (run) { return run.id; }).join(",")
        );
      }
      if (candidates.length === 0) {
        if (correlationWindowExpired_(state.tdcc_dispatched_at)) {
          failTdccChain_(state, "tdcc_run_unconfirmed", "No TDCC run appeared for the accepted dispatch");
        }
        Logger.log("Waiting for TDCC workflow run id.");
        return;
      }
      state.tdcc_run_id = String(candidates[0].id);
      state.tdcc_head_sha = candidates[0].head_sha;
      state.tdcc_run_url = candidates[0].html_url;
      state.phase = "tdcc_running";
      writeTdccChainState_(state);
    }

    const tdccRun = getWorkflowRun_(state.tdcc_run_id);
    state.tdcc_status = tdccRun.status;
    state.tdcc_conclusion = tdccRun.conclusion || null;
    state.tdcc_head_sha = tdccRun.head_sha;
    state.tdcc_run_url = tdccRun.html_url;
    if (tdccRun.status !== "completed") {
      state.phase = "tdcc_running";
      writeTdccChainState_(state);
      return;
    }
    if (tdccRun.conclusion !== "success") {
      if (isRetryableTdccDataFailure_(tdccRun.id)) {
        scheduleTdccDataRetry_(state, tdccRun);
        Logger.log(
          "TDCC data is not ready or continuity repair did not finish; retry remains automatic."
        );
        return;
      }
      failTdccChain_(
        state,
        "tdcc_failed",
        "TDCC workflow did not succeed: run_id=" + tdccRun.id + " conclusion=" + tdccRun.conclusion
      );
    }

    if (!state.tdcc_output_commit_sha) {
      let publishedEvidence;
      try {
        publishedEvidence = readTdccPublishedEvidence_(tdccRun);
      } catch (error) {
        failTdccChain_(state, "tdcc_main_gate_failed", error.message);
      }
      if (!publishedEvidence) {
        if (mainEvidenceWindowExpired_(tdccRun.updated_at)) {
          failTdccChain_(
            state,
            "tdcc_main_gate_failed",
            "TDCC run succeeded but matching run/head evidence did not appear on main within 30 minutes"
          );
        }
        Logger.log("TDCC run succeeded but matching status evidence is not yet visible on main.");
        return;
      }
      state.signal_date = publishedEvidence.signal_date;
      state.tdcc_output_commit_sha = publishedEvidence.tdcc_output_commit_sha;
      state.main_sha_at_gate = publishedEvidence.main_sha_at_gate;
      state.chain_key = tdccChainIdentity_(
        tdccRun.id,
        state.signal_date,
        state.tdcc_output_commit_sha
      );
      state.phase = "tdcc_published_on_main";
      writeTdccChainState_(state);
    }

    if (!state.downstream_dispatched_at) {
      if (
        tdccDispatchAlreadyRecorded_(
          state.tdcc_run_id,
          state.signal_date,
          state.tdcc_output_commit_sha
        )
      ) {
        state.phase = "duplicate_skipped";
        state.duplicate_reason = "Exact TDCC run/date/output chain already dispatched";
        writeTdccChainState_(state);
        return;
      }

      state.downstream_baseline_run_id = latestWorkflowRunId_(INDIVIDUAL_REFRESH_WORKFLOW);
      state.downstream_dispatched_at = nowIso_();
      state.phase = "downstream_dispatching";
      writeTdccChainState_(state);
      try {
        dispatchWorkflow_(INDIVIDUAL_REFRESH_WORKFLOW);
      } catch (error) {
        state.phase = "downstream_dispatch_uncertain";
        state.error = error.message;
        writeTdccChainState_(state);
        throw error;
      }
      state.phase = "downstream_dispatched";
      writeTdccChainState_(state);
      recordTdccDispatch_(state);
      return;
    }

    if (!state.downstream_run_id) {
      const downstreamCandidates = findCorrelatedWorkflowRuns_(
        INDIVIDUAL_REFRESH_WORKFLOW,
        state.downstream_baseline_run_id,
        state.downstream_dispatched_at
      );
      if (downstreamCandidates.length > 1) {
        failTdccChain_(
          state,
          "downstream_run_ambiguous",
          "More than one individual refresh run matched the dispatch window: " +
            downstreamCandidates.map(function (run) { return run.id; }).join(",")
        );
      }
      if (downstreamCandidates.length === 0) {
        if (correlationWindowExpired_(state.downstream_dispatched_at)) {
          failTdccChain_(
            state,
            "downstream_run_unconfirmed",
            "No individual refresh run appeared for the accepted dispatch"
          );
        }
        Logger.log("Waiting for individual refresh workflow run id.");
        return;
      }
      const downstreamCandidate = downstreamCandidates[0];
      assertCommitContained_(
        state.tdcc_output_commit_sha,
        downstreamCandidate.head_sha,
        "TDCC output commit in individual refresh head"
      );
      state.downstream_run_id = String(downstreamCandidate.id);
      state.downstream_head_sha = downstreamCandidate.head_sha;
      state.downstream_run_url = downstreamCandidate.html_url;
      state.phase = "downstream_running";
      writeTdccChainState_(state);
      recordTdccDispatch_(state);
    }

    const downstreamRun = getWorkflowRun_(state.downstream_run_id);
    state.downstream_status = downstreamRun.status;
    state.downstream_conclusion = downstreamRun.conclusion || null;
    state.downstream_head_sha = downstreamRun.head_sha;
    state.downstream_run_url = downstreamRun.html_url;
    if (downstreamRun.status !== "completed") {
      state.phase = "downstream_running";
      writeTdccChainState_(state);
      recordTdccDispatch_(state);
      return;
    }
    if (downstreamRun.conclusion !== "success") {
      state.phase = "downstream_failed";
      state.error =
        "Individual refresh workflow did not succeed: run_id=" +
        downstreamRun.id +
        " conclusion=" +
        downstreamRun.conclusion;
      writeTdccChainState_(state);
      recordTdccDispatch_(state);
      throw new Error(state.error);
    }

    let downstreamEvidence;
    try {
      downstreamEvidence = readWorkflowOutputEvidence_(
        downstreamRun,
        INDIVIDUAL_REFRESH_RUN_STATUS_PATH,
        state.signal_date
      );
    } catch (error) {
      state.downstream_main_last_error = error.message;
      if (mainEvidenceWindowExpired_(downstreamRun.updated_at)) {
        state.phase = "downstream_main_gate_failed";
        state.error =
          "Individual refresh succeeded but matching run-status evidence did not reach main " +
          "within 30 minutes: " +
          error.message;
        writeTdccChainState_(state);
        recordTdccDispatch_(state);
        throw new Error(state.error);
      }
      state.phase = "downstream_main_pending";
      writeTdccChainState_(state);
      recordTdccDispatch_(state);
      Logger.log(
        "Individual refresh succeeded but matching run-status evidence is not yet visible on main: " +
          error.message
      );
      return;
    }
    state.downstream_output_commit_sha = downstreamEvidence.output_commit_sha;
    state.main_sha_at_completion = downstreamEvidence.main_sha;
    delete state.downstream_main_last_error;
    delete state.error;
    state.phase = "complete";
    state.completed_at = nowIso_();
    writeTdccChainState_(state);
    recordTdccDispatch_(state);
  });
}

function diagnoseTdccIndividualRefreshOrchestration() {
  testGithubTokenAndWorkflowAccess();
  assertWorkflowAccessible_(TDCC_WEEKLY_WORKFLOW);
  assertWorkflowAccessible_(INDIVIDUAL_REFRESH_WORKFLOW);
  Logger.log("chain_state=" + JSON.stringify(readTdccChainState_()));
  Logger.log("dispatch_history=" + JSON.stringify(readTdccDispatchHistory_()));
  logLatestWorkflowRuns_(TDCC_WEEKLY_WORKFLOW);
  logLatestWorkflowRuns_(INDIVIDUAL_REFRESH_WORKFLOW);
}

function triggerTdccHistoryGapRepair() {
  dispatchWorkflow_("repair_tdcc_monthly_history_gaps.yml", {
    universe: "chatgpt-top",
    max_stocks: "80",
    max_requests: "500",
    rebuild_max_dates: "4",
  });
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("repair_tdcc_monthly_history_gaps.yml");
}

function triggerEventCatalystUpdate() {
  dispatchWorkflow_("event_catalyst_update.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("event_catalyst_update.yml");
}

function triggerWeeklyThemeReview() {
  dispatchWorkflow_("weekly_theme_review.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("weekly_theme_review.yml");
}

function triggerResearchBacktestPipeline() {
  dispatchWorkflow_("research_backtest_pipeline.yml", {
    run_market_timing: "true",
    run_weekly_surge: "true",
    run_explosive_volume: "true",
    run_surge_model: "true",
    run_signal_performance: "true",
    run_volume_breakout: "true",
    run_catalyst_performance: "true",
    run_msci_rebalance: "true",
    run_tdcc_signal_performance: "true",
    run_tdcc_short_term_edge: "true",
    run_short_term_specialty_packet: "true",
    run_shared_model_research_data_refresh: "true",
    run_price_pullback_23ema_research: "true",
    run_revenue_unreacted_range_research: "true",
    run_volume_range_breakout_v2_research: "true",
  });
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("research_backtest_pipeline.yml");
}

function triggerIndividualStockDataRefresh() {
  dispatchWorkflow_("individual_stock_data_refresh.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("individual_stock_data_refresh.yml");
}

function installDailyStockMonitorTrigger() {
  installDailyStockMonitorTrigger_();
  Logger.log("Installed daily stock monitor trigger: daily 19:30 Asia/Taipei, self-skips weekends.");
  listAllTriggers();
}

function installDailyPriceGapRepairTrigger() {
  installDailyPriceGapRepairTrigger_();
  Logger.log("Installed daily price gap repair trigger: daily 10:30 Asia/Taipei, self-skips weekends.");
  listAllTriggers();
}

function installTdccHistoryGapRepairTrigger() {
  installTdccHistoryGapRepairTrigger_();
  Logger.log("Installed TDCC monthly history gap repair trigger: Tuesday 09:30 Asia/Taipei.");
  listAllTriggers();
}

function removeDailyStockMonitorTrigger() {
  removeTriggersForFunction_("triggerDailyStockMonitor");
  Logger.log("Removed daily stock monitor triggers.");
  listAllTriggers();
}

function removeDailyPriceGapRepairTrigger() {
  removeTriggersForFunction_("triggerDailyPriceGapRepair");
  Logger.log("Removed daily price gap repair triggers.");
  listAllTriggers();
}

function removeTdccHistoryGapRepairTrigger() {
  removeTriggersForFunction_("triggerTdccHistoryGapRepair");
  Logger.log("Removed TDCC monthly history gap repair triggers.");
  listAllTriggers();
}

function installBiweeklyResearchBacktestTrigger() {
  removeTriggersForFunction_("triggerResearchBacktestPipeline");
  ScriptApp.newTrigger("triggerResearchBacktestPipeline")
    .timeBased()
    .everyWeeks(2)
    .onWeekDay(ScriptApp.WeekDay.SUNDAY)
    .atHour(21)
    .nearMinute(10)
    .inTimezone("Asia/Taipei")
    .create();
  Logger.log("Installed biweekly research backtest trigger: Sunday 21:10 Asia/Taipei, every 2 weeks.");
}

function installAllWorkflowTriggers() {
  installDailyPriceGapRepairTrigger_();
  installDailyStockMonitorTrigger_();
  installIndividualStockDataRefreshTrigger_();
  installTdccHistoryGapRepairTrigger_();
  installTdccWeeklyReportTrigger_();
  installTdccIndividualRefreshOrchestratorTrigger_();
  installEventCatalystUpdateTriggers_();
  installWeeklyThemeReviewTrigger_();
  installBiweeklyResearchBacktestTrigger();
  Logger.log("Installed all workflow triggers.");
  listAllTriggers();
}

function installTdccIndividualRefreshOrchestratorTrigger() {
  installTdccIndividualRefreshOrchestratorTrigger_();
  Logger.log(
    "Installed TDCC-to-individual refresh orchestrator: every " +
      TDCC_CHAIN_POLL_MINUTES +
      " minutes; dispatch occurs only after run/main gates pass."
  );
  listAllTriggers();
}

function removeTdccIndividualRefreshOrchestratorTrigger() {
  removeTriggersForFunction_("orchestrateTdccIndividualRefresh");
  Logger.log("Removed TDCC-to-individual refresh orchestrator trigger.");
  listAllTriggers();
}

function installDailyStockMonitorTrigger_() {
  removeTriggersForFunction_("triggerDailyStockMonitor");
  ScriptApp.newTrigger("triggerDailyStockMonitor")
    .timeBased()
    .everyDays(1)
    .atHour(19)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
}

function installDailyPriceGapRepairTrigger_() {
  removeTriggersForFunction_("triggerDailyPriceGapRepair");
  ScriptApp.newTrigger("triggerDailyPriceGapRepair")
    .timeBased()
    .everyDays(1)
    .atHour(10)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
}

function installIndividualStockDataRefreshTrigger_() {
  removeTriggersForFunction_("triggerIndividualStockDataRefresh");
  ScriptApp.newTrigger("triggerIndividualStockDataRefresh")
    .timeBased()
    .everyDays(1)
    .atHour(22)
    .nearMinute(20)
    .inTimezone("Asia/Taipei")
    .create();
}

function installTdccWeeklyReportTrigger_() {
  removeTriggersForFunction_("triggerTdccWeeklyReport");
  ScriptApp.newTrigger("triggerTdccWeeklyReport")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.SATURDAY)
    .atHour(15)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
}

function installTdccIndividualRefreshOrchestratorTrigger_() {
  removeTriggersForFunction_("orchestrateTdccIndividualRefresh");
  ScriptApp.newTrigger("orchestrateTdccIndividualRefresh")
    .timeBased()
    .everyMinutes(TDCC_CHAIN_POLL_MINUTES)
    .create();
}

function installTdccHistoryGapRepairTrigger_() {
  removeTriggersForFunction_("triggerTdccHistoryGapRepair");
  ScriptApp.newTrigger("triggerTdccHistoryGapRepair")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.TUESDAY)
    .atHour(9)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
}

function installEventCatalystUpdateTriggers_() {
  removeTriggersForFunction_("triggerEventCatalystUpdate");
  ScriptApp.newTrigger("triggerEventCatalystUpdate")
    .timeBased()
    .everyDays(1)
    .atHour(8)
    .nearMinute(10)
    .inTimezone("Asia/Taipei")
    .create();
  ScriptApp.newTrigger("triggerEventCatalystUpdate")
    .timeBased()
    .everyDays(1)
    .atHour(18)
    .nearMinute(10)
    .inTimezone("Asia/Taipei")
    .create();
}

function installWeeklyThemeReviewTrigger_() {
  removeTriggersForFunction_("triggerWeeklyThemeReview");
  ScriptApp.newTrigger("triggerWeeklyThemeReview")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.SUNDAY)
    .atHour(19)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
}

function listAllTriggers() {
  ScriptApp.getProjectTriggers().forEach(function (trigger) {
    Logger.log(
      [
        "handler=" + trigger.getHandlerFunction(),
        "eventType=" + trigger.getEventType(),
        "source=" + trigger.getTriggerSource(),
      ].join(" | ")
    );
  });
}

function removeTriggersForFunction_(functionName) {
  ScriptApp.getProjectTriggers().forEach(function (trigger) {
    if (trigger.getHandlerFunction() === functionName) {
      ScriptApp.deleteTrigger(trigger);
    }
  });
}
