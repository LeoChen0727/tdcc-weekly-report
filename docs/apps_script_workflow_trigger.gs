const GITHUB_OWNER = "LeoChen0727";
const GITHUB_REPO = "tdcc-weekly-report";
const GITHUB_REF = "main";
const GITHUB_API_VERSION = "2022-11-28";
const GITHUB_PAT_PROPERTY = "GITHUB_PAT";
const GITHUB_TOKEN_FALLBACK_PROPERTY = "GITHUB_TOKEN";
const RESPONSE_PREVIEW_MAX_CHARS = 1200;

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
        ". Configure a token with repository Actions read/write permission for " +
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
    return "token lacks Actions read/write permission or is blocked by policy";
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
  dispatchWorkflow_("tdcc_weekly.yml");
  Utilities.sleep(5000);
  logLatestWorkflowRunsSafe_("tdcc_weekly.yml");
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
    run_model_parameter_research: "true",
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
  Logger.log("Installed daily price gap repair trigger: daily 08:30 Asia/Taipei, self-skips weekends.");
  listAllTriggers();
}

function installTdccHistoryGapRepairTrigger() {
  installTdccHistoryGapRepairTrigger_();
  Logger.log("Installed TDCC monthly history gap repair trigger: Tuesday 09:00 Asia/Taipei.");
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
    .atHour(20)
    .nearMinute(30)
    .inTimezone("Asia/Taipei")
    .create();
  Logger.log("Installed biweekly research backtest trigger: Sunday 20:30 Asia/Taipei, every 2 weeks.");
}

function installAllWorkflowTriggers() {
  installDailyPriceGapRepairTrigger_();
  installDailyStockMonitorTrigger_();
  installIndividualStockDataRefreshTrigger_();
  installTdccHistoryGapRepairTrigger_();
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

function installDailyPriceGapRepairTrigger_() {
  removeTriggersForFunction_("triggerDailyPriceGapRepair");
  ScriptApp.newTrigger("triggerDailyPriceGapRepair")
    .timeBased()
    .everyDays(1)
    .atHour(8)
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

function installTdccHistoryGapRepairTrigger_() {
  removeTriggersForFunction_("triggerTdccHistoryGapRepair");
  ScriptApp.newTrigger("triggerTdccHistoryGapRepair")
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.TUESDAY)
    .atHour(9)
    .nearMinute(0)
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
