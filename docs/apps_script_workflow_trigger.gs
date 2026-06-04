const GITHUB_OWNER = "LeoChen0727";
const GITHUB_REPO = "tdcc-weekly-report";
const GITHUB_REF = "main";
const GITHUB_API_VERSION = "2022-11-28";

function getGithubToken_() {
  const token = PropertiesService.getScriptProperties().getProperty("GITHUB_PAT");
  if (!token) {
    throw new Error("Missing Script Property: GITHUB_PAT");
  }
  return token;
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
  Logger.log("Response body: " + responseBody);

  return {
    statusCode: statusCode,
    responseBody: responseBody,
  };
}

function assertGithubSuccess_(result, actionName) {
  if (result.statusCode === 200 || result.statusCode === 201 || result.statusCode === 202 || result.statusCode === 204) {
    return;
  }
  throw new Error(actionName + " failed: " + result.statusCode + " " + result.responseBody);
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
}

function listWorkflowRuns_(workflowFile) {
  const path =
    "/repos/" +
    GITHUB_OWNER +
    "/" +
    GITHUB_REPO +
    "/actions/workflows/" +
    encodeURIComponent(workflowFile) +
    "/runs?branch=" +
    encodeURIComponent(GITHUB_REF) +
    "&event=workflow_dispatch&per_page=5";

  const result = githubApi_("get", path, null);
  assertGithubSuccess_(result, "List runs " + workflowFile);
  return JSON.parse(result.responseBody);
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

function testGithubTokenAndWorkflowAccess() {
  const path = "/repos/" + GITHUB_OWNER + "/" + GITHUB_REPO + "/actions/workflows";
  const result = githubApi_("get", path, null);
  assertGithubSuccess_(result, "List workflows");
  Logger.log("GitHub token and workflow access OK.");
}

function triggerDailyStockMonitor() {
  if (new Date().getDay() === 0) {
    Logger.log("Skip daily full pipeline on Sunday.");
    return;
  }
  dispatchWorkflow_("daily_full_pipeline.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRuns_("daily_full_pipeline.yml");
}

function triggerDailyFullPipeline() {
  triggerDailyStockMonitor();
}

function triggerTdccWeeklyReport() {
  dispatchWorkflow_("tdcc_weekly.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRuns_("tdcc_weekly.yml");
}

function triggerEventCatalystUpdate() {
  dispatchWorkflow_("event_catalyst_update.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRuns_("event_catalyst_update.yml");
}

function triggerWeeklyThemeReview() {
  dispatchWorkflow_("weekly_theme_review.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRuns_("weekly_theme_review.yml");
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
    run_model_parameter_research: "true",
  });
  Utilities.sleep(5000);
  logLatestWorkflowRuns_("research_backtest_pipeline.yml");
}

function installBiweeklyResearchBacktestTrigger() {
  removeTriggersForFunction_("triggerResearchBacktestPipeline");
  ScriptApp.newTrigger("triggerResearchBacktestPipeline")
    .timeBased()
    .everyWeeks(2)
    .onWeekDay(ScriptApp.WeekDay.SUNDAY)
    .atHour(20)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
  Logger.log("Installed biweekly research backtest trigger: Sunday 20:30 Asia/Taipei, every 2 weeks.");
}

function installAllWorkflowTriggers() {
  installDailyStockMonitorTrigger_();
  installTdccWeeklyReportTrigger_();
  installEventCatalystUpdateTriggers_();
  installWeeklyThemeReviewTrigger_();
  installBiweeklyResearchBacktestTrigger();
  Logger.log("Installed all workflow triggers.");
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
    .atHour(18)
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
