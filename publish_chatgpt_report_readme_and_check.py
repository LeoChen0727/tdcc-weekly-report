from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import base64
import json
import os
import re
import subprocess
from typing import Any

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")
DOCS_LATEST_DIR = Path("docs/latest")
DOCS_HISTORY_REPORT_DIR = Path("docs/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
PACKET_MANIFEST_JSON = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"
PDF_KLINE_STATUS_MD = LATEST_DIR / "pdf_kline_chart_status_latest.md"
PDF_KLINE_STATUS_JSON = LATEST_DIR / "pdf_kline_chart_status_latest.json"
DOCS_PDF_KLINE_STATUS_MD = DOCS_LATEST_DIR / "pdf_kline_chart_status_latest.md"
FIXED_PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"
FIXED_PDF_VALIDATION_MD = LATEST_DIR / "daily_market_report_validation_latest.md"
FIXED_PDF_VALIDATION_JSON = LATEST_DIR / "daily_market_report_validation_latest.json"
CURATED_REPORT_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_REPORT_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
DOCS_CURATED_REPORT_PDF = DOCS_LATEST_DIR / "daily_market_curated_report_latest.pdf"
DOCS_FULL_TABLE_REPORT_PDF = DOCS_LATEST_DIR / "daily_market_full_table_report_latest.pdf"
DOCS_FIXED_PDF_VALIDATION_MD = DOCS_LATEST_DIR / "daily_market_report_validation_latest.md"

README_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
DOCS_README_TXT = DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt"
README_INDEX_TXT = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt"
README_INDEX_JSON = LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT_INDEX.json"
DOCS_README_INDEX_TXT = DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT_INDEX.txt"
DOCS_README_INDEX_JSON = DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT_INDEX.json"

PUBLISH_CHECK_MD = LATEST_DIR / "report_publish_check_latest.md"
PUBLISH_CHECK_JSON = LATEST_DIR / "report_publish_check_latest.json"

LATEST_PACKET = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
DOCS_LATEST_PACKET = DOCS_LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"

RULES_LATEST = LATEST_DIR / "CHATGPT_DAILY_REPORT_RULES.txt"
RULES_DOCS = DOCS_LATEST_DIR / "CHATGPT_DAILY_REPORT_RULES.txt"
RULES_DIR = Path("rules")
DOCS_RULES_DIR = Path("docs/rules")
MASTER_PRIORITY_RULES = RULES_DIR / "master_priority_rules.md"
DAILY_STOCK_CANDIDATE_RULES = RULES_DIR / "daily_stock_candidate_rules.md"
ASTROLOGY_RULES = RULES_DIR / "astrology_rules.md"
RULES_INDEX = RULES_DIR / "rules_index_latest.md"
DOCS_MASTER_PRIORITY_RULES = DOCS_RULES_DIR / "master_priority_rules.md"
DOCS_DAILY_STOCK_CANDIDATE_RULES = DOCS_RULES_DIR / "daily_stock_candidate_rules.md"
DOCS_ASTROLOGY_RULES = DOCS_RULES_DIR / "astrology_rules.md"
DOCS_RULES_INDEX = DOCS_RULES_DIR / "rules_index_latest.md"
ASTROLOGY_PROTOCOL = LATEST_DIR / "astrology_read_protocol_latest.md"
DOCS_ASTROLOGY_PROTOCOL = DOCS_LATEST_DIR / "astrology_read_protocol_latest.md"

LATEST_SUMMARY_MD = LATEST_DIR / "daily_market_summary_latest.md"
LATEST_FULL_MD = LATEST_DIR / "daily_market_full_latest.md"
DAILY_SIGNAL_SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
DAILY_SIGNAL_WEEKLY_MD = LATEST_DIR / "daily_signal_performance_weekly_latest.md"
DAILY_SIGNAL_WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DAILY_SIGNAL_MONTHLY_MD = LATEST_DIR / "daily_signal_performance_monthly_latest.md"
DAILY_SIGNAL_MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
DAILY_CANDIDATE_SIGNAL_LOG = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")
CANDIDATE_REPEAT_APPEARANCE_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
CANDIDATE_REPEAT_APPEARANCE_MD = LATEST_DIR / "candidate_repeat_appearance_latest.md"
DAILY_CANDIDATE_DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
DAILY_CANDIDATE_DECISION_MD = LATEST_DIR / "daily_candidate_decision_latest.md"
DAILY_CANDIDATE_DECISION_PACKET_MD = LATEST_DIR / "daily_candidate_decision_chatgpt_packet_latest.md"
DAILY_THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
DAILY_THEME_LEADERSHIP_MD = LATEST_DIR / "daily_theme_leadership_latest.md"
DAILY_CANDIDATE_TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
DAILY_CANDIDATE_TWO_LINE_VIEW_MD = LATEST_DIR / "daily_candidate_two_line_view_latest.md"
DOCS_DAILY_THEME_LEADERSHIP_CSV = DOCS_LATEST_DIR / "daily_theme_leadership_latest.csv"
DOCS_DAILY_THEME_LEADERSHIP_MD = DOCS_LATEST_DIR / "daily_theme_leadership_latest.md"
DOCS_DAILY_CANDIDATE_TWO_LINE_VIEW_CSV = DOCS_LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
DOCS_DAILY_CANDIDATE_TWO_LINE_VIEW_MD = DOCS_LATEST_DIR / "daily_candidate_two_line_view_latest.md"
INDICATOR_USAGE_GUIDE_MD = LATEST_DIR / "chatgpt_indicator_usage_guide_latest.md"
INDICATOR_USAGE_GUIDE_TXT = LATEST_DIR / "CHATGPT_INDICATOR_USAGE_GUIDE.txt"
DOCS_DAILY_SIGNAL_WEEKLY_PDF = DOCS_LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DOCS_DAILY_SIGNAL_MONTHLY_PDF = DOCS_LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
FUNDAMENTAL_CATALYST_MD = LATEST_DIR / "fundamental_catalyst_layer_latest.md"
CATALYST_SUMMARY_MD = LATEST_DIR / "catalyst_summary_latest.md"
CATALYST_SUMMARY_CSV = LATEST_DIR / "catalyst_summary_latest.csv"
CATALYST_VALIDATION_MD = LATEST_DIR / "catalyst_layer_validation_latest.md"
CATALYST_PERFORMANCE_CSV = Path("output/history/catalyst_performance/catalyst_performance.csv")
THEME_EVENT_CALENDAR = Path("data/theme_events/theme_event_calendar.csv")
COMPANY_THEME_MAPPING = Path("data/theme_events/company_theme_mapping.csv")
QUARTERLY_CATALYST = Path("data/fundamental_catalysts/quarterly_catalyst.csv")
EVENT_CATALYST_LOG = Path("data/event_catalysts/event_catalyst_log.csv")
COMPANY_EVENT_CALENDAR = Path("data/company_calendar/company_event_calendar.csv")
MACRO_EVENT_CALENDAR = Path("data/macro_events/macro_event_calendar.csv")
UPCOMING_CATALYST_CALENDAR = LATEST_DIR / "upcoming_catalyst_calendar_latest.csv"
UPCOMING_MACRO_EVENT_CALENDAR = LATEST_DIR / "upcoming_macro_event_calendar_latest.csv"
CALENDAR_DATA_SOURCE_STATUS_MD = LATEST_DIR / "calendar_data_source_status_latest.md"
EVENT_CALENDAR_VALIDATION_MD = LATEST_DIR / "event_calendar_validation_latest.md"
CATALYST_NEEDS_REVIEW_CSV = LATEST_DIR / "catalyst_needs_review_latest.csv"
CATALYST_NEEDS_REVIEW_MD = LATEST_DIR / "catalyst_needs_review_latest.md"
WARRANT_MARKET_MD = LATEST_DIR / "warrant_market_report_latest.md"
WARRANT_MARKET_PDF = LATEST_DIR / "warrant_market_report_latest.pdf"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_SECTOR_HEAT_CSV = LATEST_DIR / "warrant_sector_heat_latest.csv"
WARRANT_SIGNAL_PERFORMANCE_MD = LATEST_DIR / "warrant_signal_performance_latest.md"
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
MARKET_RISK_DASHBOARD_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
MARKET_RISK_DASHBOARD_PDF = LATEST_DIR / "market_risk_dashboard_latest.pdf"
MARKET_INDEX_HISTORY_CSV = Path("data/market_index_history.csv")
MARKET_INDEX_OHLC_HISTORY_CSV = Path("data/market_index_ohlc_history.csv")
FUTURES_OPTIONS_INDICATORS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
FUTURES_OPTIONS_SOURCE_STATUS_MD = LATEST_DIR / "futures_options_source_status_latest.md"
MARKET_TIMING_PACKET_MD = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"
MARKET_TIMING_BACKTEST_MD = LATEST_DIR / "market_timing_backtest_latest.md"
MARKET_TIMING_BACKTEST_CSV = LATEST_DIR / "market_timing_backtest_latest.csv"
MARKET_TIMING_COMPOSITE_MD = LATEST_DIR / "market_timing_composite_backtest_latest.md"
MARKET_TIMING_COMPOSITE_CSV = LATEST_DIR / "market_timing_composite_backtest_latest.csv"
MARKET_TIMING_REGIME_MD = LATEST_DIR / "market_timing_regime_effectiveness_latest.md"
MARKET_TIMING_REGIME_CSV = LATEST_DIR / "market_timing_regime_effectiveness_latest.csv"
MARKET_TECHNICAL_FEATURE_PANEL = Path("output/history/market_timing/market_technical_feature_panel.csv")
MARKET_TECHNICAL_EVENT_LOG = Path("output/history/market_timing/market_technical_event_log.csv")
MARKET_BREADTH_HISTORY = Path("output/history/market_timing/market_breadth_history.csv")
TDCC_STRENGTH_RANKING_TOP_MD = LATEST_DIR / "tdcc_strength_ranking_top_latest.md"
TDCC_STRENGTH_RANKING_TOP_CSV = LATEST_DIR / "tdcc_strength_ranking_top_latest.csv"
TDCC_PRE_MOVE_ABM_TOP_MD = LATEST_DIR / "tdcc_pre_move_abm_top_latest.md"
TDCC_PRE_MOVE_ABM_TOP_CSV = LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv"
TDCC_PHASE_DISTRIBUTION_MD = LATEST_DIR / "tdcc_phase_distribution_latest.md"
TDCC_PHASE_DISTRIBUTION_CSV = LATEST_DIR / "tdcc_phase_distribution_latest.csv"
TDCC_TOP_RISK_LIST_MD = LATEST_DIR / "tdcc_top_risk_list_latest.md"
TDCC_TOP_RISK_LIST_CSV = LATEST_DIR / "tdcc_top_risk_list_latest.csv"
TDCC_CHATGPT_TRACKING_PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"
SURGE_MODEL_PACKET_MD = LATEST_DIR / "surge_model_chatgpt_packet_latest.md"
SURGE_PRECONDITION_CANDIDATES_MD = LATEST_DIR / "surge_precondition_candidates_latest.md"
SURGE_PRECONDITION_CANDIDATES_CSV = LATEST_DIR / "surge_precondition_candidates_latest.csv"
SURGE_MODEL_BACKTEST_MD = LATEST_DIR / "surge_model_backtest_latest.md"
SURGE_MODEL_BACKTEST_CSV = LATEST_DIR / "surge_model_backtest_latest.csv"
SURGE_MODEL_FEATURE_IMPORTANCE_MD = LATEST_DIR / "surge_model_feature_importance_latest.md"
SURGE_MODEL_FEATURE_IMPORTANCE_CSV = LATEST_DIR / "surge_model_feature_importance_latest.csv"
SURGE_MODEL_VALIDATION_MD = LATEST_DIR / "surge_model_validation_latest.md"
VOLUME_BREAKOUT_WATCH_MD = LATEST_DIR / "volume_breakout_watch_latest.md"
VOLUME_BREAKOUT_WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
VOLUME_BREAKOUT_BACKTEST_MD = LATEST_DIR / "volume_breakout_backtest_latest.md"
VOLUME_BREAKOUT_BACKTEST_CSV = LATEST_DIR / "volume_breakout_backtest_latest.csv"
VOLUME_BREAKOUT_PACKET_MD = LATEST_DIR / "volume_breakout_chatgpt_packet_latest.md"
VOLUME_ATTACK_THEME_LAYER_CSV = LATEST_DIR / "volume_attack_theme_layer_latest.csv"
VOLUME_ATTACK_THEME_LAYER_MD = LATEST_DIR / "volume_attack_theme_layer_latest.md"
VOLUME_ATTACK_THEME_STOCKS_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
VOLUME_ATTACK_THEME_STOCKS_MD = LATEST_DIR / "volume_attack_theme_stocks_latest.md"
TDCC_OVERHEATED_EDGE_MD = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.md"
TDCC_OVERHEATED_EDGE_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.csv"
TDCC_OVERHEATED_EDGE_CANDIDATES_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
RAW_DATA_FETCH_STATUS_CSV = LATEST_DIR / "raw_data_fetch_status_latest.csv"
RAW_DATA_FETCH_STATUS_MD = LATEST_DIR / "raw_data_fetch_status_latest.md"
INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_CSV = LATEST_DIR / "individual_stock_available_raw_data_index.csv"
INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_MD = LATEST_DIR / "individual_stock_available_raw_data_index.md"
INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_CSV = LATEST_DIR / "individual_stock_available_raw_data_index_slim.csv"
INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_MD = LATEST_DIR / "individual_stock_available_raw_data_index_slim.md"
INDIVIDUAL_STOCK_READ_PROTOCOL_MD = LATEST_DIR / "individual_stock_read_protocol_latest.md"
INDIVIDUAL_STOCK_REPORTS_INDEX_CSV = LATEST_DIR / "individual_stock_reports_index.csv"
INDIVIDUAL_STOCK_REPORTS_INDEX_MD = LATEST_DIR / "individual_stock_reports_index.md"
INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_CSV = LATEST_DIR / "individual_stock_chatgpt_packet_index.csv"
INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_MD = LATEST_DIR / "individual_stock_chatgpt_packet_index.md"


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_date(value: Any) -> str:
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass

    text = str(value).strip()
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def run_command(args: list[str], timeout: int = 40) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        return 124, exc.stdout or "", exc.stderr or "timeout"
    except Exception as exc:
        return 1, "", str(exc)


def curl_auth_args(url: str) -> list[str]:
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token and "api.github.com" in url:
        return [
            "-H",
            f"Authorization: Bearer {token}",
            "-H",
            "Accept: application/vnd.github+json",
            "-H",
            "X-GitHub-Api-Version: 2022-11-28",
        ]
    return []


def raw_url(ref: str, path: Path) -> str:
    return f"{RAW_PREFIX}/{ref}/{path.as_posix()}"


def pages_url(path_under_docs: str) -> str:
    return f"{PAGES_PREFIX}/{path_under_docs.lstrip('/')}"


def github_api_url(path: Path, ref: str = "main") -> str:
    return f"https://api.github.com/repos/{OWNER_REPO}/contents/{path.as_posix()}?ref={ref}"


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    return {}


def extract_data_freshness() -> dict[str, str]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
    }

    if DATA_FRESHNESS_CSV.exists():
        try:
            df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str)
            if not df.empty:
                row = df.iloc[0].to_dict()
                result["main_price_date"] = normalize_date(row.get("main_price_date", ""))
                result["report_ready"] = str(row.get("report_ready", "")).strip()
                result["all_candidates_date"] = normalize_date(row.get("all_candidates_date", ""))
                result["official_price_fetch_date"] = normalize_date(row.get("official_price_fetch_date", ""))
                result["stock_monitor_date"] = normalize_date(row.get("stock_monitor_price_date", ""))
                result["warrant_flow_date"] = normalize_date(row.get("warrant_flow_date", ""))
                return result
        except Exception:
            pass

    if DATA_FRESHNESS_MD.exists():
        text = DATA_FRESHNESS_MD.read_text(encoding="utf-8", errors="ignore")

        m = re.search(r"主資料日期[：:\s`]*([0-9/\-]{8,10})", text)
        if m:
            result["main_price_date"] = normalize_date(m.group(1))

        m = re.search(r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)", text)
        if m:
            result["report_ready"] = m.group(1)

    return result


def get_artifact_commit_sha() -> str:
    env_sha = os.environ.get("ARTIFACT_COMMIT_SHA", "").strip()

    if env_sha:
        return env_sha

    code, out, _ = run_command(["git", "rev-parse", "HEAD"])
    if code == 0:
        return out.strip()

    return ""


def curl_head(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-I", "-L", "--max-time", "30", *curl_auth_args(url), url],
        timeout=45,
    )

    status_code = ""

    for line in out.splitlines():
        if line.startswith("HTTP/"):
            parts = line.split()
            if len(parts) >= 2:
                status_code = parts[1]

    return {
        "command": f"curl -I -L --max-time 30 {url}",
        "returncode": code,
        "http_status": status_code,
        "stdout": out,
        "stderr": err,
        "ok": code == 0 and status_code == "200",
    }


def curl_body(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-L", "--max-time", "30", *curl_auth_args(url), url],
        timeout=45,
    )

    contains_packet = "CHATGPT DAILY REPORT PACKET" in out
    contains_summary = "EMBEDDED SUMMARY REPORT" in out
    contains_full = "EMBEDDED FULL REPORT" in out

    return {
        "command": f"curl -L --max-time 30 {url}",
        "returncode": code,
        "stdout_head": "\n".join(out.splitlines()[:50]),
        "stderr": err,
        "contains_packet": contains_packet,
        "contains_summary": contains_summary,
        "contains_full": contains_full,
        "ok": code == 0 and contains_packet and contains_summary and contains_full,
    }


def curl_github_api_packet(url: str) -> dict[str, Any]:
    code, out, err = run_command(
        ["curl", "-L", "--max-time", "30", *curl_auth_args(url), url],
        timeout=45,
    )

    decoded_text = ""
    api_parse_ok = False

    if code == 0:
        try:
            data = json.loads(out)
            content = data.get("content", "")
            encoding = data.get("encoding", "")

            if encoding == "base64" and content:
                decoded_bytes = base64.b64decode(content)
                decoded_text = decoded_bytes.decode("utf-8", errors="replace")
                api_parse_ok = True
        except Exception as exc:
            err = (err + "\n" + f"api decode failed: {exc}").strip()

    contains_packet = "CHATGPT DAILY REPORT PACKET" in decoded_text
    contains_summary = "EMBEDDED SUMMARY REPORT" in decoded_text
    contains_full = "EMBEDDED FULL REPORT" in decoded_text

    return {
        "command": f"curl -L --max-time 30 {url}",
        "returncode": code,
        "stdout_head": "\n".join(out.splitlines()[:50]),
        "decoded_head": "\n".join(decoded_text.splitlines()[:50]),
        "stderr": err,
        "api_parse_ok": api_parse_ok,
        "contains_packet": contains_packet,
        "contains_summary": contains_summary,
        "contains_full": contains_full,
        "ok": code == 0 and api_parse_ok and contains_packet and contains_summary and contains_full,
    }


def check_plain_packet_url(label: str, url: str) -> dict[str, Any]:
    head = curl_head(url)
    body = curl_body(url)

    return {
        "label": label,
        "url": url,
        "type": "plain",
        "head": head,
        "body": body,
        "ok": bool(head.get("ok")) and bool(body.get("ok")),
    }


def check_api_packet_url(label: str, url: str) -> dict[str, Any]:
    head = curl_head(url)
    body = curl_github_api_packet(url)

    return {
        "label": label,
        "url": url,
        "type": "github_api",
        "head": head,
        "body": body,
        "ok": bool(head.get("ok")) and bool(body.get("ok")),
    }


def choose_preferred(checks: list[dict[str, Any]]) -> str:
    for item in checks:
        if item.get("ok"):
            return str(item.get("url", ""))

    for item in checks:
        if item.get("label") == "packet_commit_raw_url":
            return str(item.get("url", ""))

    return ""


def build_readme(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    readme_date_stamped_pages_url: str,
    readme_date_stamped_raw_url: str,
    readme_date_stamped_github_api_url: str,
    readme_history_pages_url: str,
    readme_history_raw_url: str,
    packet_pages_url: str,
    packet_latest_raw_url: str,
    packet_commit_raw_url: str,
    packet_github_api_url: str,
    summary_latest_raw_url: str,
    full_latest_raw_url: str,
    daily_market_curated_pdf_pages_url: str,
    daily_market_curated_pdf_raw_url: str,
    daily_market_full_table_pdf_pages_url: str,
    daily_market_full_table_pdf_raw_url: str,
    fixed_pdf_validation_status: str,
    fixed_pdf_validation_raw_url: str,
    pdf_kline_status_pages_url: str,
    pdf_kline_status_raw_url: str,
    pdf_kline_policy: str,
    pdf_kline_status: str,
    pdf_kline_total_charts: Any,
    pdf_kline_local_price_redraw_count: Any,
    fundamental_catalyst_layer_raw_url: str,
    theme_event_calendar_raw_url: str,
    company_theme_mapping_raw_url: str,
    quarterly_catalyst_raw_url: str,
    event_catalyst_log_raw_url: str,
    catalyst_summary_raw_url: str,
    catalyst_summary_csv_raw_url: str,
    catalyst_performance_raw_url: str,
    catalyst_layer_validation_raw_url: str,
    company_event_calendar_raw_url: str,
    macro_event_calendar_raw_url: str,
    upcoming_catalyst_calendar_raw_url: str,
    upcoming_macro_event_calendar_raw_url: str,
    calendar_data_source_status_raw_url: str,
    event_calendar_validation_raw_url: str,
    catalyst_needs_review_csv_raw_url: str,
    catalyst_needs_review_md_raw_url: str,
    daily_signal_performance_summary_raw_url: str,
    daily_signal_performance_weekly_md_raw_url: str,
    daily_signal_performance_weekly_pdf_pages_url: str,
    daily_signal_performance_weekly_pdf_raw_url: str,
    daily_signal_performance_monthly_md_raw_url: str,
    daily_signal_performance_monthly_pdf_pages_url: str,
    daily_signal_performance_monthly_pdf_raw_url: str,
    daily_candidate_signal_log_raw_url: str,
    candidate_repeat_appearance_raw_url: str,
    candidate_repeat_appearance_md_raw_url: str,
    warrant_market_report_md_raw_url: str,
    warrant_market_report_pdf_pages_url: str,
    warrant_market_report_pdf_raw_url: str,
    warrant_flow_by_stock_raw_url: str,
    warrant_sector_heat_raw_url: str,
    warrant_signal_performance_raw_url: str,
    market_regime_raw_url: str,
    market_risk_dashboard_md_raw_url: str,
    market_risk_dashboard_pdf_pages_url: str,
    market_risk_dashboard_pdf_raw_url: str,
    futures_options_indicators_raw_url: str,
    futures_options_source_status_raw_url: str,
    rules_pages_url: str,
    rules_raw_url: str,
    preferred_chatgpt_url: str,
    checks: list[dict[str, Any]],
) -> str:
    status_map = {item["label"]: item.get("ok") for item in checks}

    lines = [
        f"astrology_read_protocol_raw_url={raw_url('main', ASTROLOGY_PROTOCOL)}",
        f"astrology_read_protocol_pages_url={pages_url('latest/astrology_read_protocol_latest.md')}",
        "astrology_high_priority_guard=for_astrology_zi_wei_ba_zi_tasks_do_not_start_with_data_status_or_repo_status",
        "astrology_first_visible_heading_rule=first_visible_heading_must_be_fixed_chart_or_today_bazi_not_data_status",
        "astrology_forbidden_opening_heading_keys=data_status,flow_status,repo_entry_status,readme_status",
        "astrology_market_data_note_rule=market_data_status_may_appear_only_as_one_sentence_in_wealth_stock_section_or_final_data_note",
        f"main_price_date={main_price_date}",
        f"report_ready={report_ready}",
        f"commit_sha={commit_sha}",
        f"readme_latest_pages_url={pages_url('latest/READ_ME_FIRST_DAILY_REPORT.txt')}",
        f"readme_latest_raw_url={raw_url('main', README_TXT)}",
        f"readme_index_pages_url={pages_url('latest/READ_ME_FIRST_DAILY_REPORT_INDEX.txt')}",
        f"readme_index_raw_url={raw_url('main', README_INDEX_TXT)}",
        f"readme_index_json_raw_url={raw_url('main', README_INDEX_JSON)}",
        f"readme_index_github_api_url={github_api_url(README_INDEX_JSON, ref='main')}",
        f"readme_date_stamped_pages_url={readme_date_stamped_pages_url}",
        f"readme_date_stamped_raw_url={readme_date_stamped_raw_url}",
        f"readme_date_stamped_github_api_url={readme_date_stamped_github_api_url}",
        f"readme_history_pages_url={readme_history_pages_url}",
        f"readme_history_raw_url={readme_history_raw_url}",
        "readme_cache_bypass_order=readme_date_stamped_pages_url,readme_date_stamped_raw_url,readme_date_stamped_github_api_url,readme_index_github_api_url,readme_history_pages_url,readme_history_raw_url,readme_latest_pages_url,readme_latest_raw_url",
        f"rules_index_raw_url={raw_url('main', RULES_INDEX)}",
        f"rules_index_pages_url={pages_url('rules/rules_index_latest.md')}",
        f"rules_master_priority_raw_url={raw_url('main', MASTER_PRIORITY_RULES)}",
        f"rules_master_priority_pages_url={pages_url('rules/master_priority_rules.md')}",
        f"rules_daily_stock_candidate_raw_url={raw_url('main', DAILY_STOCK_CANDIDATE_RULES)}",
        f"rules_daily_stock_candidate_pages_url={pages_url('rules/daily_stock_candidate_rules.md')}",
        f"rules_astrology_raw_url={raw_url('main', ASTROLOGY_RULES)}",
        f"rules_astrology_pages_url={pages_url('rules/astrology_rules.md')}",
        "astrology_task_rule=calendar_date_task_read_astrology_rules_do_not_use_daily_market_report_format",
        "astrology_visible_report_rule=start_with_astrology_content_not_repo_data_status",
        "astrology_debug_status_rule=do_not_show_raw_fetch_pages_cache_or_api_status_unless_user_asks_for_diagnostics",
        "chatgpt_delivery_contract=repo_artifacts_are_sources_not_final_chatgpt_deliverables",
        "repo_pdf_artifact_role=source_validation_shareable_reference_only",
        "report_ready_meaning=repo_data_packet_and_repo_artifacts_available_not_chatgpt_task_done",
        "fixed_pdf_validation_meaning=repo_pipeline_pdf_validation_only_not_chatgpt_deliverable_pdf",
        "chatgpt_status_only_request=report_repo_status_and_links_only",
        "chatgpt_daily_task_request=must_read_repo_structured_data_and_produce_new_chatgpt_side_deliverables",
        "daily_full_market_default_chatgpt_deliverables=每日推薦分析 PDF|完整候選清單補充 PDF|權證市場輔助分析 PDF|市場風險與大盤期權背景 PDF",
        "repo_artifacts_do_not_satisfy_chatgpt_pdf_delivery=True",
        "do_not_paste_full_text_instead_of_required_pdf=True",
        f"preferred_chatgpt_url={preferred_chatgpt_url}",
        f"packet_pages_url={packet_pages_url}",
        f"packet_commit_raw_url={packet_commit_raw_url}",
        f"packet_latest_raw_url={packet_latest_raw_url}",
        f"packet_github_api_url={packet_github_api_url}",
        f"summary_latest_raw_url={summary_latest_raw_url}",
        f"full_latest_raw_url={full_latest_raw_url}",
        f"daily_market_curated_pdf_pages_url={daily_market_curated_pdf_pages_url}",
        f"daily_market_curated_pdf_raw_url={daily_market_curated_pdf_raw_url}",
        f"daily_market_full_table_pdf_pages_url={daily_market_full_table_pdf_pages_url}",
        f"daily_market_full_table_pdf_raw_url={daily_market_full_table_pdf_raw_url}",
        f"fixed_pdf_validation_status={fixed_pdf_validation_status}",
        f"fixed_pdf_validation_raw_url={fixed_pdf_validation_raw_url}",
        f"pdf_kline_status_pages_url={pdf_kline_status_pages_url}",
        f"pdf_kline_status_raw_url={pdf_kline_status_raw_url}",
        f"summary_pdf_kline_policy={pdf_kline_policy}",
        f"summary_pdf_kline_status={pdf_kline_status}",
        f"summary_pdf_kline_total_charts={pdf_kline_total_charts}",
        f"summary_pdf_kline_local_price_redraw_count={pdf_kline_local_price_redraw_count}",
        "summary_pdf_chart_path_and_chart_url_are_fallback_only=True",
        "do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed=True",
        f"fundamental_catalyst_layer_raw_url={fundamental_catalyst_layer_raw_url}",
        f"theme_event_calendar_raw_url={theme_event_calendar_raw_url}",
        f"company_theme_mapping_raw_url={company_theme_mapping_raw_url}",
        f"quarterly_catalyst_raw_url={quarterly_catalyst_raw_url}",
        f"event_catalyst_log_raw_url={event_catalyst_log_raw_url}",
        f"catalyst_summary_raw_url={catalyst_summary_raw_url}",
        f"catalyst_summary_csv_raw_url={catalyst_summary_csv_raw_url}",
        f"catalyst_performance_raw_url={catalyst_performance_raw_url}",
        f"catalyst_layer_validation_raw_url={catalyst_layer_validation_raw_url}",
        f"company_event_calendar_raw_url={company_event_calendar_raw_url}",
        f"macro_event_calendar_raw_url={macro_event_calendar_raw_url}",
        f"upcoming_catalyst_calendar_raw_url={upcoming_catalyst_calendar_raw_url}",
        f"upcoming_macro_event_calendar_raw_url={upcoming_macro_event_calendar_raw_url}",
        f"calendar_data_source_status_raw_url={calendar_data_source_status_raw_url}",
        f"event_calendar_validation_raw_url={event_calendar_validation_raw_url}",
        f"catalyst_needs_review_csv_raw_url={catalyst_needs_review_csv_raw_url}",
        f"catalyst_needs_review_md_raw_url={catalyst_needs_review_md_raw_url}",
        "data_source_priority=raw_structured_data_first,pdf_auxiliary_only,pdf_only_if_raw_unavailable",
        "pdf_only_disclosure_required=True",
        "pdf_only_disclosure_text=本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。",
        f"daily_signal_performance_summary_raw_url={daily_signal_performance_summary_raw_url}",
        f"daily_signal_performance_weekly_md_raw_url={daily_signal_performance_weekly_md_raw_url}",
        f"daily_signal_performance_weekly_pdf_pages_url={daily_signal_performance_weekly_pdf_pages_url}",
        f"daily_signal_performance_weekly_pdf_raw_url={daily_signal_performance_weekly_pdf_raw_url}",
        f"daily_signal_performance_monthly_md_raw_url={daily_signal_performance_monthly_md_raw_url}",
        f"daily_signal_performance_monthly_pdf_pages_url={daily_signal_performance_monthly_pdf_pages_url}",
        f"daily_signal_performance_monthly_pdf_raw_url={daily_signal_performance_monthly_pdf_raw_url}",
        f"daily_candidate_signal_log_raw_url={daily_candidate_signal_log_raw_url}",
        f"candidate_repeat_appearance_raw_url={candidate_repeat_appearance_raw_url}",
        f"candidate_repeat_appearance_md_raw_url={candidate_repeat_appearance_md_raw_url}",
        f"daily_candidate_decision_raw_url={raw_url('main', DAILY_CANDIDATE_DECISION_CSV)}",
        f"daily_candidate_decision_md_raw_url={raw_url('main', DAILY_CANDIDATE_DECISION_MD)}",
        f"daily_candidate_decision_chatgpt_packet_raw_url={raw_url('main', DAILY_CANDIDATE_DECISION_PACKET_MD)}",
        f"daily_theme_leadership_pages_url={pages_url('latest/daily_theme_leadership_latest.csv')}",
        f"daily_theme_leadership_raw_url={raw_url('main', DAILY_THEME_LEADERSHIP_CSV)}",
        f"daily_theme_leadership_md_pages_url={pages_url('latest/daily_theme_leadership_latest.md')}",
        f"daily_theme_leadership_md_raw_url={raw_url('main', DAILY_THEME_LEADERSHIP_MD)}",
        f"daily_candidate_two_line_view_pages_url={pages_url('latest/daily_candidate_two_line_view_latest.csv')}",
        f"daily_candidate_two_line_view_raw_url={raw_url('main', DAILY_CANDIDATE_TWO_LINE_VIEW_CSV)}",
        f"daily_candidate_two_line_view_md_pages_url={pages_url('latest/daily_candidate_two_line_view_latest.md')}",
        f"daily_candidate_two_line_view_md_raw_url={raw_url('main', DAILY_CANDIDATE_TWO_LINE_VIEW_MD)}",
        f"chatgpt_indicator_usage_guide_md_raw_url={raw_url('main', INDICATOR_USAGE_GUIDE_MD)}",
        f"chatgpt_indicator_usage_guide_txt_raw_url={raw_url('main', INDICATOR_USAGE_GUIDE_TXT)}",
        f"chatgpt_indicator_usage_guide_pages_url={pages_url('latest/chatgpt_indicator_usage_guide_latest.md')}",
        f"chatgpt_indicator_usage_guide_txt_pages_url={pages_url('latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt')}",
        f"volume_breakout_watch_md_raw_url={raw_url('main', VOLUME_BREAKOUT_WATCH_MD)}",
        f"volume_breakout_watch_csv_raw_url={raw_url('main', VOLUME_BREAKOUT_WATCH_CSV)}",
        f"volume_breakout_backtest_md_raw_url={raw_url('main', VOLUME_BREAKOUT_BACKTEST_MD)}",
        f"volume_breakout_backtest_csv_raw_url={raw_url('main', VOLUME_BREAKOUT_BACKTEST_CSV)}",
        f"volume_breakout_chatgpt_packet_raw_url={raw_url('main', VOLUME_BREAKOUT_PACKET_MD)}",
        f"volume_attack_theme_layer_md_raw_url={raw_url('main', VOLUME_ATTACK_THEME_LAYER_MD)}",
        f"volume_attack_theme_layer_csv_raw_url={raw_url('main', VOLUME_ATTACK_THEME_LAYER_CSV)}",
        f"volume_attack_theme_layer_md_pages_url={pages_url('latest/volume_attack_theme_layer_latest.md')}",
        f"volume_attack_theme_layer_csv_pages_url={pages_url('latest/volume_attack_theme_layer_latest.csv')}",
        f"volume_attack_theme_stocks_md_raw_url={raw_url('main', VOLUME_ATTACK_THEME_STOCKS_MD)}",
        f"volume_attack_theme_stocks_csv_raw_url={raw_url('main', VOLUME_ATTACK_THEME_STOCKS_CSV)}",
        f"volume_attack_theme_stocks_md_pages_url={pages_url('latest/volume_attack_theme_stocks_latest.md')}",
        f"volume_attack_theme_stocks_csv_pages_url={pages_url('latest/volume_attack_theme_stocks_latest.csv')}",
        f"tdcc_overheated_short_term_edge_md_raw_url={raw_url('main', TDCC_OVERHEATED_EDGE_MD)}",
        f"tdcc_overheated_short_term_edge_csv_raw_url={raw_url('main', TDCC_OVERHEATED_EDGE_CSV)}",
        f"tdcc_overheated_short_term_edge_candidates_csv_raw_url={raw_url('main', TDCC_OVERHEATED_EDGE_CANDIDATES_CSV)}",
        f"tdcc_overheated_short_term_edge_md_pages_url={pages_url('latest/tdcc_overheated_short_term_edge_latest.md')}",
        f"tdcc_overheated_short_term_edge_csv_pages_url={pages_url('latest/tdcc_overheated_short_term_edge_latest.csv')}",
        f"tdcc_overheated_short_term_edge_candidates_csv_pages_url={pages_url('latest/tdcc_overheated_short_term_edge_candidates_latest.csv')}",
        f"raw_data_fetch_status_raw_url={raw_url('main', RAW_DATA_FETCH_STATUS_CSV)}",
        f"raw_data_fetch_status_md_raw_url={raw_url('main', RAW_DATA_FETCH_STATUS_MD)}",
        f"raw_data_fetch_status_pages_url={pages_url('latest/raw_data_fetch_status_latest.csv')}",
        f"raw_data_fetch_status_md_pages_url={pages_url('latest/raw_data_fetch_status_latest.md')}",
        f"raw_data_fetch_status_github_api_url={github_api_url(RAW_DATA_FETCH_STATUS_CSV, ref='main')}",
        f"raw_data_fetch_status_md_github_api_url={github_api_url(RAW_DATA_FETCH_STATUS_MD, ref='main')}",
        f"individual_stock_available_raw_data_index_raw_url={raw_url('main', INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_CSV)}",
        f"individual_stock_available_raw_data_index_md_raw_url={raw_url('main', INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_MD)}",
        f"individual_stock_available_raw_data_index_pages_url={pages_url('latest/individual_stock_available_raw_data_index.csv')}",
        f"individual_stock_available_raw_data_index_md_pages_url={pages_url('latest/individual_stock_available_raw_data_index.md')}",
        f"individual_stock_available_raw_data_index_github_api_url={github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_CSV, ref='main')}",
        f"individual_stock_available_raw_data_index_md_github_api_url={github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_MD, ref='main')}",
        f"individual_stock_available_raw_data_index_slim_raw_url={raw_url('main', INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_CSV)}",
        f"individual_stock_available_raw_data_index_slim_md_raw_url={raw_url('main', INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_MD)}",
        f"individual_stock_available_raw_data_index_slim_pages_url={pages_url('latest/individual_stock_available_raw_data_index_slim.csv')}",
        f"individual_stock_available_raw_data_index_slim_md_pages_url={pages_url('latest/individual_stock_available_raw_data_index_slim.md')}",
        f"individual_stock_available_raw_data_index_slim_github_api_url={github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_CSV, ref='main')}",
        f"individual_stock_available_raw_data_index_slim_md_github_api_url={github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_MD, ref='main')}",
        f"individual_stock_read_protocol_raw_url={raw_url('main', INDIVIDUAL_STOCK_READ_PROTOCOL_MD)}",
        f"individual_stock_read_protocol_pages_url={pages_url('latest/individual_stock_read_protocol_latest.md')}",
        f"individual_stock_read_protocol_github_api_url={github_api_url(INDIVIDUAL_STOCK_READ_PROTOCOL_MD, ref='main')}",
        f"individual_stock_reports_index_raw_url={raw_url('main', INDIVIDUAL_STOCK_REPORTS_INDEX_CSV)}",
        f"individual_stock_reports_index_md_raw_url={raw_url('main', INDIVIDUAL_STOCK_REPORTS_INDEX_MD)}",
        f"individual_stock_reports_index_pages_url={pages_url('latest/individual_stock_reports_index.csv')}",
        f"individual_stock_reports_index_md_pages_url={pages_url('latest/individual_stock_reports_index.md')}",
        f"individual_stock_reports_index_github_api_url={github_api_url(INDIVIDUAL_STOCK_REPORTS_INDEX_CSV, ref='main')}",
        f"individual_stock_reports_index_md_github_api_url={github_api_url(INDIVIDUAL_STOCK_REPORTS_INDEX_MD, ref='main')}",
        f"individual_stock_chatgpt_packet_index_raw_url={raw_url('main', INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_CSV)}",
        f"individual_stock_chatgpt_packet_index_md_raw_url={raw_url('main', INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_MD)}",
        f"individual_stock_chatgpt_packet_index_pages_url={pages_url('latest/individual_stock_chatgpt_packet_index.csv')}",
        f"individual_stock_chatgpt_packet_index_md_pages_url={pages_url('latest/individual_stock_chatgpt_packet_index.md')}",
        f"individual_stock_chatgpt_packet_index_github_api_url={github_api_url(INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_CSV, ref='main')}",
        f"individual_stock_chatgpt_packet_index_md_github_api_url={github_api_url(INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_MD, ref='main')}",
        "individual_stock_chatgpt_packet_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md",
        "individual_stock_chatgpt_packet_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md",
        "individual_stock_chatgpt_packet_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md?ref=main",
        "individual_stock_price_window_180_html_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html",
        "individual_stock_price_window_180_html_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html",
        "individual_stock_price_window_180_html_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html?ref=main",
        "individual_stock_price_window_180_txt_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt",
        "individual_stock_price_window_180_txt_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt",
        "individual_stock_price_window_180_txt_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt?ref=main",
        "individual_stock_tdcc_window_txt_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt",
        "individual_stock_tdcc_window_txt_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt",
        "individual_stock_tdcc_window_txt_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt?ref=main",
        "individual_stock_primary_read_order=individual_stock_chatgpt_packet_pages_url_template,individual_stock_chatgpt_packet_raw_url_template,individual_stock_chatgpt_packet_github_api_url_template,individual_stock_price_window_180_html_pages_url_template,individual_stock_price_window_180_html_raw_url_template,individual_stock_price_window_180_html_github_api_url_template,individual_stock_price_github_api_url_template,individual_stock_tdcc_github_api_url_template",
        "individual_stock_price_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv",
        "individual_stock_price_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/{stock_id}.csv",
        "individual_stock_price_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/{stock_id}.csv?ref=main",
        "individual_stock_tdcc_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/{stock_id}.csv",
        "individual_stock_tdcc_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/{stock_id}.csv",
        "individual_stock_tdcc_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/{stock_id}.csv?ref=main",
        "individual_stock_report_md_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/{stock_id}_latest.md",
        "individual_stock_report_md_pages_url_template=https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/{stock_id}_latest.md",
        "individual_stock_report_md_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.md?ref=main",
        "individual_stock_report_json_github_api_url_template=https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.json?ref=main",
        "individual_stock_sell_strategy_summary_raw_url_template=https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/history/sell_strategy_backtest/{stock_id}_sell_strategy_summary.md",
        "individual_stock_raw_cache_rule=if raw/pages returns cache_miss, internal_error, stale date, or Total lines 1 for a known multi-line CSV, use the GitHub API contents URL and base64-decode content; do not replace repo price/TDCC raw data with external websites.",
        "individual_stock_github_api_decode_required=True",
        f"warrant_market_report_md_raw_url={warrant_market_report_md_raw_url}",
        f"warrant_market_report_pdf_pages_url={warrant_market_report_pdf_pages_url}",
        f"warrant_market_report_pdf_raw_url={warrant_market_report_pdf_raw_url}",
        f"warrant_flow_by_stock_raw_url={warrant_flow_by_stock_raw_url}",
        f"warrant_sector_heat_raw_url={warrant_sector_heat_raw_url}",
        f"warrant_signal_performance_raw_url={warrant_signal_performance_raw_url}",
        f"market_regime_raw_url={market_regime_raw_url}",
        f"market_index_history_raw_url={raw_url('main', MARKET_INDEX_HISTORY_CSV)}",
        f"market_index_ohlc_history_raw_url={raw_url('main', MARKET_INDEX_OHLC_HISTORY_CSV)}",
        f"market_risk_dashboard_md_raw_url={market_risk_dashboard_md_raw_url}",
        f"market_risk_dashboard_pdf_pages_url={market_risk_dashboard_pdf_pages_url}",
        f"market_risk_dashboard_pdf_raw_url={market_risk_dashboard_pdf_raw_url}",
        f"futures_options_indicators_raw_url={futures_options_indicators_raw_url}",
        f"futures_options_source_status_raw_url={futures_options_source_status_raw_url}",
        f"market_timing_chatgpt_packet_raw_url={raw_url('main', MARKET_TIMING_PACKET_MD)}",
        f"market_timing_backtest_md_raw_url={raw_url('main', MARKET_TIMING_BACKTEST_MD)}",
        f"market_timing_backtest_csv_raw_url={raw_url('main', MARKET_TIMING_BACKTEST_CSV)}",
        f"market_timing_composite_backtest_md_raw_url={raw_url('main', MARKET_TIMING_COMPOSITE_MD)}",
        f"market_timing_composite_backtest_csv_raw_url={raw_url('main', MARKET_TIMING_COMPOSITE_CSV)}",
        f"market_timing_regime_effectiveness_md_raw_url={raw_url('main', MARKET_TIMING_REGIME_MD)}",
        f"market_timing_regime_effectiveness_csv_raw_url={raw_url('main', MARKET_TIMING_REGIME_CSV)}",
        f"market_technical_feature_panel_raw_url={raw_url('main', MARKET_TECHNICAL_FEATURE_PANEL)}",
        f"market_technical_event_log_raw_url={raw_url('main', MARKET_TECHNICAL_EVENT_LOG)}",
        f"market_breadth_history_raw_url={raw_url('main', MARKET_BREADTH_HISTORY)}",
        f"tdcc_strength_ranking_top_md_raw_url={raw_url('main', TDCC_STRENGTH_RANKING_TOP_MD)}",
        f"tdcc_strength_ranking_top_csv_raw_url={raw_url('main', TDCC_STRENGTH_RANKING_TOP_CSV)}",
        f"tdcc_pre_move_abm_top_md_raw_url={raw_url('main', TDCC_PRE_MOVE_ABM_TOP_MD)}",
        f"tdcc_pre_move_abm_top_csv_raw_url={raw_url('main', TDCC_PRE_MOVE_ABM_TOP_CSV)}",
        f"tdcc_phase_distribution_md_raw_url={raw_url('main', TDCC_PHASE_DISTRIBUTION_MD)}",
        f"tdcc_phase_distribution_csv_raw_url={raw_url('main', TDCC_PHASE_DISTRIBUTION_CSV)}",
        f"tdcc_top_risk_list_md_raw_url={raw_url('main', TDCC_TOP_RISK_LIST_MD)}",
        f"tdcc_top_risk_list_csv_raw_url={raw_url('main', TDCC_TOP_RISK_LIST_CSV)}",
        f"tdcc_chatgpt_tracking_packet_raw_url={raw_url('main', TDCC_CHATGPT_TRACKING_PACKET_MD)}",
        f"surge_model_chatgpt_packet_raw_url={raw_url('main', SURGE_MODEL_PACKET_MD)}",
        f"surge_precondition_candidates_md_raw_url={raw_url('main', SURGE_PRECONDITION_CANDIDATES_MD)}",
        f"surge_precondition_candidates_csv_raw_url={raw_url('main', SURGE_PRECONDITION_CANDIDATES_CSV)}",
        f"surge_model_backtest_md_raw_url={raw_url('main', SURGE_MODEL_BACKTEST_MD)}",
        f"surge_model_backtest_csv_raw_url={raw_url('main', SURGE_MODEL_BACKTEST_CSV)}",
        f"surge_model_feature_importance_md_raw_url={raw_url('main', SURGE_MODEL_FEATURE_IMPORTANCE_MD)}",
        f"surge_model_feature_importance_csv_raw_url={raw_url('main', SURGE_MODEL_FEATURE_IMPORTANCE_CSV)}",
        f"surge_model_validation_raw_url={raw_url('main', SURGE_MODEL_VALIDATION_MD)}",
        f"rules_pages_url={rules_pages_url}",
        f"rules_raw_url={rules_raw_url}",
        f"packet_pages_ok={status_map.get('packet_pages_url')}",
        f"packet_commit_raw_ok={status_map.get('packet_commit_raw_url')}",
        f"packet_latest_raw_ok={status_map.get('packet_latest_raw_url')}",
        f"packet_github_api_ok={status_map.get('packet_github_api_url')}",
        "read_order=packet_pages_url,packet_commit_raw_url,packet_latest_raw_url,packet_github_api_url",
        "",
        "RULES:",
        "1. Read this entry file first.",
        "1a. If latest READ_ME_FIRST appears stale, read readme_date_stamped_pages_url, then readme_date_stamped_raw_url, then readme_date_stamped_github_api_url.",
        "1b. If the date-stamped GitHub API URL is used, decode the JSON content field from base64 before parsing key=value lines.",
        "1c. Repo pipeline PDFs / Markdown / packets are source artifacts, not the final ChatGPT deliverable when the user asks to do today's report.",
        "1d. report_ready=True and fixed_pdf_validation_status=pass mean repo artifacts are available/validated; they do not mean ChatGPT has delivered the requested PDFs.",
        "2. Read rules_master_priority_pages_url or rules_master_priority_raw_url before any generated task rules.",
        "2a. Read rules_daily_stock_candidate_pages_url or rules_daily_stock_candidate_raw_url for the daily full-market candidate task.",
        "2b. Read rules_astrology_pages_url or rules_astrology_raw_url for Zi Wei / Ba Zi calendar-date tasks; main_price_date is only auxiliary market-data status for those tasks.",
        "2c. For astrology / Zi Wei / Ba Zi tasks, do not use CHATGPT_DAILY_REPORT_RULES.txt, rules_pages_url, rules_raw_url, or the daily market 'data status' opening format.",
        "2d. Read rules_pages_url or rules_raw_url only after the master and task-specific rule files, and only for daily market candidate tasks.",
        "3. Read preferred_chatgpt_url for the packet.",
        "4. If preferred_chatgpt_url fails, follow read_order.",
        "5. If the URL is packet_github_api_url, decode the JSON content field from base64 before reading the packet.",
        "6. If packet is readable, use EMBEDDED SUMMARY REPORT and EMBEDDED FULL REPORT as source of truth.",
        "7. Use raw structured data first: CSV files, packet fields, signal logs, warrant tables, market tables, catalyst source logs, and raw URLs.",
        "8. PDFs are auxiliary/shareable outputs. Use PDFs only if raw data cannot be read, or if the user explicitly asks for the PDF artifact.",
        "9. If only PDF data is used, start the response with: 本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。",
        "10. If the user asks 做今天報告 / 四份 PDF / 重新分析 / 執行今天任務, produce new ChatGPT-side deliverable PDFs after reading repo data; do not stop at repo PDF links.",
        "10a. Default daily full-market ChatGPT deliverables are: 每日推薦分析 PDF, 完整候選清單補充 PDF, 權證市場輔助分析 PDF, 市場風險與大盤期權背景 PDF.",
        "10b. For status-only requests, cite daily_market_curated_pdf_pages_url and daily_market_full_table_pdf_pages_url as repo artifacts.",
        "11. For pending catalyst/data-source items, read catalyst_needs_review_* and do not use rows with model_effect_allowed=False or pdf_effect_allowed=False as recommendation reasons.",
        "12. For the summary PDF K-line charts, use summary_pdf_kline_policy/status/counts above. Do not downgrade the PDF to chart_path/image-download-failed if local_price_redraw_count is greater than 0.",
        "13. If all URLs fail, say tool reading failed. Do not say GitHub data is not updated.",
        "14. Do not use older report dates to recreate a newer report.",
        "",
    ]

    return "\n".join(lines)


def build_publish_check_md(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    preferred_chatgpt_url: str,
    checks: list[dict[str, Any]],
    rules_pages_url: str,
    rules_raw_url: str,
    daily_market_curated_pdf_pages_url: str,
    daily_market_curated_pdf_raw_url: str,
    daily_market_full_table_pdf_pages_url: str,
    daily_market_full_table_pdf_raw_url: str,
    fixed_pdf_validation_status: str,
    fixed_pdf_validation_raw_url: str,
    pdf_kline_status_pages_url: str,
    pdf_kline_status_raw_url: str,
    pdf_kline_policy: str,
    pdf_kline_status: str,
    pdf_kline_total_charts: Any,
    pdf_kline_local_price_redraw_count: Any,
) -> str:
    lines: list[str] = []

    lines.append("# Report Publish Check")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append(f"- main_price_date: `{main_price_date}`")
    lines.append(f"- report_ready: `{report_ready}`")
    lines.append(f"- artifact_commit_sha: `{commit_sha}`")
    lines.append(f"- preferred_chatgpt_url: `{preferred_chatgpt_url}`")
    lines.append(f"- rules_pages_url: `{rules_pages_url}`")
    lines.append(f"- rules_raw_url: `{rules_raw_url}`")
    lines.append(f"- daily_market_curated_pdf_pages_url: `{daily_market_curated_pdf_pages_url}`")
    lines.append(f"- daily_market_curated_pdf_raw_url: `{daily_market_curated_pdf_raw_url}`")
    lines.append(f"- daily_market_full_table_pdf_pages_url: `{daily_market_full_table_pdf_pages_url}`")
    lines.append(f"- daily_market_full_table_pdf_raw_url: `{daily_market_full_table_pdf_raw_url}`")
    lines.append(f"- fixed_pdf_validation_status: `{fixed_pdf_validation_status}`")
    lines.append(f"- fixed_pdf_validation_raw_url: `{fixed_pdf_validation_raw_url}`")
    lines.append(f"- pdf_kline_status_pages_url: `{pdf_kline_status_pages_url}`")
    lines.append(f"- pdf_kline_status_raw_url: `{pdf_kline_status_raw_url}`")
    lines.append(f"- summary_pdf_kline_policy: `{pdf_kline_policy}`")
    lines.append(f"- summary_pdf_kline_status: `{pdf_kline_status}`")
    lines.append(f"- summary_pdf_kline_total_charts: `{pdf_kline_total_charts}`")
    lines.append(f"- summary_pdf_kline_local_price_redraw_count: `{pdf_kline_local_price_redraw_count}`")
    lines.append("")
    lines.append("## Read Order")
    lines.append("")
    lines.append("1. packet_pages_url")
    lines.append("2. packet_commit_raw_url")
    lines.append("3. packet_latest_raw_url")
    lines.append("4. packet_github_api_url")
    lines.append("")

    for item in checks:
        label = item.get("label", "")
        url = item.get("url", "")
        ok = item.get("ok", False)
        body = item.get("body", {})
        head = item.get("head", {})

        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"- ok: `{ok}`")
        lines.append(f"- type: `{item.get('type')}`")
        lines.append(f"- url: `{url}`")
        lines.append("")
        lines.append("### curl -I")
        lines.append("")
        lines.append("```text")
        lines.append(head.get("command", ""))
        lines.append(head.get("stdout", ""))
        if head.get("stderr"):
            lines.append("STDERR:")
            lines.append(head.get("stderr", ""))
        lines.append("```")
        lines.append("")
        lines.append("### curl -L | head -50")
        lines.append("")
        lines.append("```text")
        lines.append(body.get("command", ""))
        lines.append(body.get("stdout_head", ""))
        if body.get("decoded_head"):
            lines.append("")
            lines.append("DECODED_HEAD:")
            lines.append(body.get("decoded_head", ""))
        if body.get("stderr"):
            lines.append("STDERR:")
            lines.append(body.get("stderr", ""))
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def build_readme_index(
    *,
    main_price_date: str,
    report_ready: str,
    commit_sha: str,
    readme_date_stamped_pages_url: str,
    readme_date_stamped_raw_url: str,
    readme_date_stamped_github_api_url: str,
    readme_history_pages_url: str,
    readme_history_raw_url: str,
    preferred_chatgpt_url: str,
) -> dict[str, Any]:
    return {
        "generated_at": now_text(),
        "main_price_date": main_price_date,
        "report_ready": report_ready,
        "commit_sha": commit_sha,
        "latest_readme_pages_url": pages_url("latest/READ_ME_FIRST_DAILY_REPORT.txt"),
        "latest_readme_raw_url": raw_url("main", README_TXT),
        "latest_readme_github_api_url": github_api_url(README_TXT, ref="main"),
        "date_stamped_readme_pages_url": readme_date_stamped_pages_url,
        "date_stamped_readme_raw_url": readme_date_stamped_raw_url,
        "date_stamped_readme_github_api_url": readme_date_stamped_github_api_url,
        "history_readme_pages_url": readme_history_pages_url,
        "history_readme_raw_url": readme_history_raw_url,
        "astrology_read_protocol_pages_url": pages_url("latest/astrology_read_protocol_latest.md"),
        "astrology_read_protocol_raw_url": raw_url("main", ASTROLOGY_PROTOCOL),
        "preferred_chatgpt_url": preferred_chatgpt_url,
        "recommended_read_order": [
            "astrology_read_protocol_pages_url only for Zi Wei / Ba Zi / astrology tasks",
            "astrology_read_protocol_raw_url only for Zi Wei / Ba Zi / astrology tasks",
            "date_stamped_readme_pages_url",
            "date_stamped_readme_raw_url",
            "date_stamped_readme_github_api_url",
            "history_readme_pages_url",
            "history_readme_raw_url",
            "latest_readme_pages_url",
            "latest_readme_raw_url",
            "latest_readme_github_api_url",
        ],
        "daily_task_fallback_rule": (
            "If latest_readme_* returns an older main_price_date, do not stop. "
            "Try the date-stamped README for the expected Taiwan trading date. "
            "If that fails, try the previous 7 calendar dates through raw and GitHub API. "
            "Use only a report_ready=True entry and state the actual main_price_date used."
        ),
    }


def build_readme_index_text(index: dict[str, Any]) -> str:
    lines: list[str] = []
    for key, value in index.items():
        if isinstance(value, list):
            lines.append(f"{key}={','.join(str(item) for item in value)}")
        else:
            lines.append(f"{key}={value}")
    lines.append("")
    lines.append("RULES:")
    lines.append("1. Prefer date-stamped README URLs over latest URLs when a daily task expects a specific date.")
    lines.append("2. If latest is stale, try the expected YYYYMMDD date-stamped README, then previous 7 calendar dates.")
    lines.append("3. GitHub API contents URLs must be base64 decoded before parsing key=value.")
    lines.append("4. Never use an old main_price_date as a newer-date report.")
    return "\n".join(lines)


def build_astrology_protocol() -> str:
    return "\n".join(
        [
            "# Astrology Read Protocol",
            "",
            "This file is the first protocol for Zi Wei / Ba Zi / astrology calendar-date tasks.",
            "",
            "## Stop Rule",
            "",
            "If the task is astrology / Zi Wei / Ba Zi, do not use the daily stock candidate report structure.",
            "Do not start with data status, repo status, READ_ME_FIRST status, raw status, Pages status, GitHub API status, main_price_date, or report_ready.",
            "",
            "## Required Visible Opening",
            "",
            "Start the visible report with astrology content. The first visible section after the title must be one of:",
            "",
            "- Fixed chart verification",
            "- Today's Ba Zi",
            "- Today's Zi Wei",
            "- What is different today",
            "",
            "A market-data note may appear only inside the wealth / stock paragraph or at the final data note.",
            "",
            "## Forbidden Opening Patterns",
            "",
            "Rewrite the report before finalizing if the first 300 visible characters contain any of these before astrology content:",
            "",
            "- data status",
            "- repo status",
            "- READ_ME_FIRST",
            "- raw_fetch",
            "- pages",
            "- cache",
            "- GitHub API",
            "- main_price_date",
            "- report_ready",
            "",
            "## Correct First Section Template",
            "",
            "Title: YYYY-MM-DD Daily Zi Wei / Ba Zi Strategy",
            "",
            "First paragraph: one sentence about today's astrology rhythm and action focus.",
            "",
            "First section: Fixed chart verification.",
            "",
            "Then continue with Today's Ba Zi, Today's Zi Wei, recent-day difference, combined interpretation, practical actions, and action instructions.",
            "",
            "## Market Data Role",
            "",
            "Stock-market repo data is only auxiliary for wealth / trading behavior-risk reminders.",
            "A stale stock-market data date does not block an astrology report.",
            "Do not turn an astrology report into a repo diagnostic report.",
        ]
    )


def sync_docs_files() -> None:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_RULES_DIR.mkdir(parents=True, exist_ok=True)

    if LATEST_PACKET.exists():
        DOCS_LATEST_PACKET.write_text(
            LATEST_PACKET.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if RULES_LATEST.exists():
        RULES_DOCS.write_text(
            RULES_LATEST.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    for src, dst in [
        (MASTER_PRIORITY_RULES, DOCS_MASTER_PRIORITY_RULES),
        (DAILY_STOCK_CANDIDATE_RULES, DOCS_DAILY_STOCK_CANDIDATE_RULES),
        (ASTROLOGY_RULES, DOCS_ASTROLOGY_RULES),
        (RULES_INDEX, DOCS_RULES_INDEX),
    ]:
        if src.exists():
            dst.write_text(src.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")

    if PDF_KLINE_STATUS_MD.exists():
        DOCS_PDF_KLINE_STATUS_MD.write_text(
            PDF_KLINE_STATUS_MD.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if CURATED_REPORT_PDF.exists():
        DOCS_CURATED_REPORT_PDF.write_bytes(CURATED_REPORT_PDF.read_bytes())

    if FULL_TABLE_REPORT_PDF.exists():
        DOCS_FULL_TABLE_REPORT_PDF.write_bytes(FULL_TABLE_REPORT_PDF.read_bytes())

    if FIXED_PDF_VALIDATION_MD.exists():
        DOCS_FIXED_PDF_VALIDATION_MD.write_text(
            FIXED_PDF_VALIDATION_MD.read_text(encoding="utf-8", errors="replace"),
            encoding="utf-8",
        )

    if DAILY_SIGNAL_WEEKLY_PDF.exists():
        DOCS_DAILY_SIGNAL_WEEKLY_PDF.write_bytes(DAILY_SIGNAL_WEEKLY_PDF.read_bytes())

    if DAILY_SIGNAL_MONTHLY_PDF.exists():
        DOCS_DAILY_SIGNAL_MONTHLY_PDF.write_bytes(DAILY_SIGNAL_MONTHLY_PDF.read_bytes())

    for src, dst in [
        (DAILY_THEME_LEADERSHIP_CSV, DOCS_DAILY_THEME_LEADERSHIP_CSV),
        (DAILY_THEME_LEADERSHIP_MD, DOCS_DAILY_THEME_LEADERSHIP_MD),
        (DAILY_CANDIDATE_TWO_LINE_VIEW_CSV, DOCS_DAILY_CANDIDATE_TWO_LINE_VIEW_CSV),
        (DAILY_CANDIDATE_TWO_LINE_VIEW_MD, DOCS_DAILY_CANDIDATE_TWO_LINE_VIEW_MD),
    ]:
        if src.exists():
            dst.write_text(src.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)

    sync_docs_files()

    freshness = extract_data_freshness()
    packet_manifest = read_json(PACKET_MANIFEST_JSON)
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)

    main_price_date = freshness.get("main_price_date") or normalize_date(packet_manifest.get("main_price_date", ""))
    report_ready = freshness.get("report_ready") or str(packet_manifest.get("report_ready", "")).strip()

    if not main_price_date:
        raise RuntimeError("main_price_date is missing")

    if not report_ready:
        report_ready = "False"

    commit_sha = get_artifact_commit_sha()
    if not commit_sha:
        raise RuntimeError("artifact commit sha is missing")

    readme_date_stamped = LATEST_DIR / f"READ_ME_FIRST_DAILY_REPORT_{main_price_date}.txt"
    docs_readme_date_stamped = DOCS_LATEST_DIR / f"READ_ME_FIRST_DAILY_REPORT_{main_price_date}.txt"
    history_readme = HISTORY_REPORT_DIR / f"{main_price_date}_READ_ME_FIRST_DAILY_REPORT.txt"
    docs_history_readme = DOCS_HISTORY_REPORT_DIR / f"{main_price_date}_READ_ME_FIRST_DAILY_REPORT.txt"
    readme_date_stamped_pages_url = pages_url(f"latest/{docs_readme_date_stamped.name}")
    readme_date_stamped_raw_url = raw_url("main", readme_date_stamped)
    readme_date_stamped_github_api_url = github_api_url(readme_date_stamped, ref="main")
    readme_history_pages_url = pages_url(f"history/reports/{docs_history_readme.name}")
    readme_history_raw_url = raw_url("main", history_readme)
    history_packet = HISTORY_REPORT_DIR / f"{main_price_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    packet_pages_url = pages_url("latest/chatgpt_daily_report_packet_latest.txt")
    packet_latest_raw_url = raw_url("main", LATEST_PACKET)
    packet_commit_raw_url = raw_url(commit_sha, history_packet)
    packet_github_api_url = github_api_url(LATEST_PACKET, ref="main")
    summary_latest_raw_url = raw_url("main", LATEST_SUMMARY_MD)
    full_latest_raw_url = raw_url("main", LATEST_FULL_MD)
    curated_pdf_info = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf_info = fixed_pdf_manifest.get("full_table_pdf", {})
    daily_market_curated_pdf_pages_url = curated_pdf_info.get("pages_url") or pages_url("latest/daily_market_curated_report_latest.pdf")
    daily_market_curated_pdf_raw_url = curated_pdf_info.get("raw_url") or raw_url("main", CURATED_REPORT_PDF)
    daily_market_full_table_pdf_pages_url = full_table_pdf_info.get("pages_url") or pages_url("latest/daily_market_full_table_report_latest.pdf")
    daily_market_full_table_pdf_raw_url = full_table_pdf_info.get("raw_url") or raw_url("main", FULL_TABLE_REPORT_PDF)
    fixed_pdf_validation_status = fixed_pdf_validation.get("status", "")
    fixed_pdf_validation_raw_url = raw_url("main", FIXED_PDF_VALIDATION_MD)
    pdf_kline_status_pages_url = pages_url("latest/pdf_kline_chart_status_latest.md")
    pdf_kline_status_raw_url = raw_url("main", PDF_KLINE_STATUS_MD)
    pdf_kline_status_json = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    pdf_kline_policy = (
        pdf_kline_status_json.get("policy")
        or packet_manifest.get("summary_pdf_kline_policy")
        or "local_price_redraw_first"
    )
    pdf_kline_status = pdf_kline_status_json.get("status") or packet_manifest.get("summary_pdf_kline_status", "")
    pdf_kline_total_charts = pdf_kline_status_json.get(
        "total_charts",
        packet_manifest.get("summary_pdf_kline_total_charts", 0),
    )
    pdf_kline_local_price_redraw_count = pdf_kline_status_json.get(
        "local_price_redraw_count",
        packet_manifest.get("summary_pdf_kline_local_price_redraw_count", 0),
    )
    fundamental_catalyst_layer_raw_url = raw_url("main", FUNDAMENTAL_CATALYST_MD)
    theme_event_calendar_raw_url = raw_url("main", THEME_EVENT_CALENDAR)
    company_theme_mapping_raw_url = raw_url("main", COMPANY_THEME_MAPPING)
    quarterly_catalyst_raw_url = raw_url("main", QUARTERLY_CATALYST)
    event_catalyst_log_raw_url = raw_url("main", EVENT_CATALYST_LOG)
    catalyst_summary_raw_url = raw_url("main", CATALYST_SUMMARY_MD)
    catalyst_summary_csv_raw_url = raw_url("main", CATALYST_SUMMARY_CSV)
    catalyst_performance_raw_url = raw_url("main", CATALYST_PERFORMANCE_CSV)
    catalyst_layer_validation_raw_url = raw_url("main", CATALYST_VALIDATION_MD)
    company_event_calendar_raw_url = raw_url("main", COMPANY_EVENT_CALENDAR)
    macro_event_calendar_raw_url = raw_url("main", MACRO_EVENT_CALENDAR)
    upcoming_catalyst_calendar_raw_url = raw_url("main", UPCOMING_CATALYST_CALENDAR)
    upcoming_macro_event_calendar_raw_url = raw_url("main", UPCOMING_MACRO_EVENT_CALENDAR)
    calendar_data_source_status_raw_url = raw_url("main", CALENDAR_DATA_SOURCE_STATUS_MD)
    event_calendar_validation_raw_url = raw_url("main", EVENT_CALENDAR_VALIDATION_MD)
    catalyst_needs_review_csv_raw_url = raw_url("main", CATALYST_NEEDS_REVIEW_CSV)
    catalyst_needs_review_md_raw_url = raw_url("main", CATALYST_NEEDS_REVIEW_MD)
    daily_signal_performance_summary_raw_url = raw_url("main", DAILY_SIGNAL_SUMMARY_MD)
    daily_signal_performance_weekly_md_raw_url = raw_url("main", DAILY_SIGNAL_WEEKLY_MD)
    daily_signal_performance_weekly_pdf_pages_url = pages_url("latest/daily_signal_performance_weekly_latest.pdf")
    daily_signal_performance_weekly_pdf_raw_url = raw_url("main", DAILY_SIGNAL_WEEKLY_PDF)
    daily_signal_performance_monthly_md_raw_url = raw_url("main", DAILY_SIGNAL_MONTHLY_MD)
    daily_signal_performance_monthly_pdf_pages_url = pages_url("latest/daily_signal_performance_monthly_latest.pdf")
    daily_signal_performance_monthly_pdf_raw_url = raw_url("main", DAILY_SIGNAL_MONTHLY_PDF)
    daily_candidate_signal_log_raw_url = raw_url("main", DAILY_CANDIDATE_SIGNAL_LOG)
    candidate_repeat_appearance_raw_url = raw_url("main", CANDIDATE_REPEAT_APPEARANCE_CSV)
    candidate_repeat_appearance_md_raw_url = raw_url("main", CANDIDATE_REPEAT_APPEARANCE_MD)
    warrant_market_report_md_raw_url = raw_url("main", WARRANT_MARKET_MD)
    warrant_market_report_pdf_pages_url = pages_url("latest/warrant_market_report_latest.pdf")
    warrant_market_report_pdf_raw_url = raw_url("main", WARRANT_MARKET_PDF)
    warrant_flow_by_stock_raw_url = raw_url("main", WARRANT_FLOW_BY_STOCK_CSV)
    warrant_sector_heat_raw_url = raw_url("main", WARRANT_SECTOR_HEAT_CSV)
    warrant_signal_performance_raw_url = raw_url("main", WARRANT_SIGNAL_PERFORMANCE_MD)
    market_regime_raw_url = raw_url("main", MARKET_REGIME_CSV)
    market_risk_dashboard_md_raw_url = raw_url("main", MARKET_RISK_DASHBOARD_MD)
    market_risk_dashboard_pdf_pages_url = pages_url("latest/market_risk_dashboard_latest.pdf")
    market_risk_dashboard_pdf_raw_url = raw_url("main", MARKET_RISK_DASHBOARD_PDF)
    futures_options_indicators_raw_url = raw_url("main", FUTURES_OPTIONS_INDICATORS_CSV)
    futures_options_source_status_raw_url = raw_url("main", FUTURES_OPTIONS_SOURCE_STATUS_MD)

    rules_pages_url = pages_url("latest/CHATGPT_DAILY_REPORT_RULES.txt")
    rules_raw_url = raw_url("main", RULES_LATEST)

    checks = [
        check_plain_packet_url("packet_pages_url", packet_pages_url),
        check_plain_packet_url("packet_commit_raw_url", packet_commit_raw_url),
        check_plain_packet_url("packet_latest_raw_url", packet_latest_raw_url),
        check_api_packet_url("packet_github_api_url", packet_github_api_url),
    ]

    preferred = choose_preferred(checks)

    readme = build_readme(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        readme_date_stamped_pages_url=readme_date_stamped_pages_url,
        readme_date_stamped_raw_url=readme_date_stamped_raw_url,
        readme_date_stamped_github_api_url=readme_date_stamped_github_api_url,
        readme_history_pages_url=readme_history_pages_url,
        readme_history_raw_url=readme_history_raw_url,
        packet_pages_url=packet_pages_url,
        packet_latest_raw_url=packet_latest_raw_url,
        packet_commit_raw_url=packet_commit_raw_url,
        packet_github_api_url=packet_github_api_url,
        summary_latest_raw_url=summary_latest_raw_url,
        full_latest_raw_url=full_latest_raw_url,
        daily_market_curated_pdf_pages_url=daily_market_curated_pdf_pages_url,
        daily_market_curated_pdf_raw_url=daily_market_curated_pdf_raw_url,
        daily_market_full_table_pdf_pages_url=daily_market_full_table_pdf_pages_url,
        daily_market_full_table_pdf_raw_url=daily_market_full_table_pdf_raw_url,
        fixed_pdf_validation_status=fixed_pdf_validation_status,
        fixed_pdf_validation_raw_url=fixed_pdf_validation_raw_url,
        pdf_kline_status_pages_url=pdf_kline_status_pages_url,
        pdf_kline_status_raw_url=pdf_kline_status_raw_url,
        pdf_kline_policy=pdf_kline_policy,
        pdf_kline_status=pdf_kline_status,
        pdf_kline_total_charts=pdf_kline_total_charts,
        pdf_kline_local_price_redraw_count=pdf_kline_local_price_redraw_count,
        fundamental_catalyst_layer_raw_url=fundamental_catalyst_layer_raw_url,
        theme_event_calendar_raw_url=theme_event_calendar_raw_url,
        company_theme_mapping_raw_url=company_theme_mapping_raw_url,
        quarterly_catalyst_raw_url=quarterly_catalyst_raw_url,
        event_catalyst_log_raw_url=event_catalyst_log_raw_url,
        catalyst_summary_raw_url=catalyst_summary_raw_url,
        catalyst_summary_csv_raw_url=catalyst_summary_csv_raw_url,
        catalyst_performance_raw_url=catalyst_performance_raw_url,
        catalyst_layer_validation_raw_url=catalyst_layer_validation_raw_url,
        company_event_calendar_raw_url=company_event_calendar_raw_url,
        macro_event_calendar_raw_url=macro_event_calendar_raw_url,
        upcoming_catalyst_calendar_raw_url=upcoming_catalyst_calendar_raw_url,
        upcoming_macro_event_calendar_raw_url=upcoming_macro_event_calendar_raw_url,
        calendar_data_source_status_raw_url=calendar_data_source_status_raw_url,
        event_calendar_validation_raw_url=event_calendar_validation_raw_url,
        catalyst_needs_review_csv_raw_url=catalyst_needs_review_csv_raw_url,
        catalyst_needs_review_md_raw_url=catalyst_needs_review_md_raw_url,
        daily_signal_performance_summary_raw_url=daily_signal_performance_summary_raw_url,
        daily_signal_performance_weekly_md_raw_url=daily_signal_performance_weekly_md_raw_url,
        daily_signal_performance_weekly_pdf_pages_url=daily_signal_performance_weekly_pdf_pages_url,
        daily_signal_performance_weekly_pdf_raw_url=daily_signal_performance_weekly_pdf_raw_url,
        daily_signal_performance_monthly_md_raw_url=daily_signal_performance_monthly_md_raw_url,
        daily_signal_performance_monthly_pdf_pages_url=daily_signal_performance_monthly_pdf_pages_url,
        daily_signal_performance_monthly_pdf_raw_url=daily_signal_performance_monthly_pdf_raw_url,
        daily_candidate_signal_log_raw_url=daily_candidate_signal_log_raw_url,
        candidate_repeat_appearance_raw_url=candidate_repeat_appearance_raw_url,
        candidate_repeat_appearance_md_raw_url=candidate_repeat_appearance_md_raw_url,
        warrant_market_report_md_raw_url=warrant_market_report_md_raw_url,
        warrant_market_report_pdf_pages_url=warrant_market_report_pdf_pages_url,
        warrant_market_report_pdf_raw_url=warrant_market_report_pdf_raw_url,
        warrant_flow_by_stock_raw_url=warrant_flow_by_stock_raw_url,
        warrant_sector_heat_raw_url=warrant_sector_heat_raw_url,
        warrant_signal_performance_raw_url=warrant_signal_performance_raw_url,
        market_regime_raw_url=market_regime_raw_url,
        market_risk_dashboard_md_raw_url=market_risk_dashboard_md_raw_url,
        market_risk_dashboard_pdf_pages_url=market_risk_dashboard_pdf_pages_url,
        market_risk_dashboard_pdf_raw_url=market_risk_dashboard_pdf_raw_url,
        futures_options_indicators_raw_url=futures_options_indicators_raw_url,
        futures_options_source_status_raw_url=futures_options_source_status_raw_url,
        rules_pages_url=rules_pages_url,
        rules_raw_url=rules_raw_url,
        preferred_chatgpt_url=preferred,
        checks=checks,
    )
    readme_index = build_readme_index(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        readme_date_stamped_pages_url=readme_date_stamped_pages_url,
        readme_date_stamped_raw_url=readme_date_stamped_raw_url,
        readme_date_stamped_github_api_url=readme_date_stamped_github_api_url,
        readme_history_pages_url=readme_history_pages_url,
        readme_history_raw_url=readme_history_raw_url,
        preferred_chatgpt_url=preferred,
    )
    readme_index_text = build_readme_index_text(readme_index)
    astrology_protocol = build_astrology_protocol()

    ASTROLOGY_PROTOCOL.write_text(astrology_protocol, encoding="utf-8")
    DOCS_ASTROLOGY_PROTOCOL.write_text(astrology_protocol, encoding="utf-8")
    README_TXT.write_text(readme, encoding="utf-8")
    DOCS_README_TXT.write_text(readme, encoding="utf-8")
    README_INDEX_TXT.write_text(readme_index_text, encoding="utf-8")
    DOCS_README_INDEX_TXT.write_text(readme_index_text, encoding="utf-8")
    README_INDEX_JSON.write_text(
        json.dumps(readme_index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    DOCS_README_INDEX_JSON.write_text(
        json.dumps(readme_index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    readme_date_stamped.write_text(readme, encoding="utf-8")
    docs_readme_date_stamped.write_text(readme, encoding="utf-8")
    history_readme.write_text(readme, encoding="utf-8")
    docs_history_readme.write_text(readme, encoding="utf-8")

    publish_check_md = build_publish_check_md(
        main_price_date=main_price_date,
        report_ready=report_ready,
        commit_sha=commit_sha,
        preferred_chatgpt_url=preferred,
        checks=checks,
        rules_pages_url=rules_pages_url,
        rules_raw_url=rules_raw_url,
        daily_market_curated_pdf_pages_url=daily_market_curated_pdf_pages_url,
        daily_market_curated_pdf_raw_url=daily_market_curated_pdf_raw_url,
        daily_market_full_table_pdf_pages_url=daily_market_full_table_pdf_pages_url,
        daily_market_full_table_pdf_raw_url=daily_market_full_table_pdf_raw_url,
        fixed_pdf_validation_status=fixed_pdf_validation_status,
        fixed_pdf_validation_raw_url=fixed_pdf_validation_raw_url,
        pdf_kline_status_pages_url=pdf_kline_status_pages_url,
        pdf_kline_status_raw_url=pdf_kline_status_raw_url,
        pdf_kline_policy=pdf_kline_policy,
        pdf_kline_status=pdf_kline_status,
        pdf_kline_total_charts=pdf_kline_total_charts,
        pdf_kline_local_price_redraw_count=pdf_kline_local_price_redraw_count,
    )

    PUBLISH_CHECK_MD.write_text(publish_check_md, encoding="utf-8")

    publish_check_json = {
        "generated_at": now_text(),
        "main_price_date": main_price_date,
        "report_ready": report_ready,
        "commit_sha": commit_sha,
        "readme_latest_pages_url": pages_url("latest/READ_ME_FIRST_DAILY_REPORT.txt"),
        "readme_latest_raw_url": raw_url("main", README_TXT),
        "readme_index_pages_url": pages_url("latest/READ_ME_FIRST_DAILY_REPORT_INDEX.txt"),
        "readme_index_raw_url": raw_url("main", README_INDEX_TXT),
        "readme_index_json_raw_url": raw_url("main", README_INDEX_JSON),
        "readme_index_github_api_url": github_api_url(README_INDEX_JSON, ref="main"),
        "readme_date_stamped_pages_url": readme_date_stamped_pages_url,
        "readme_date_stamped_raw_url": readme_date_stamped_raw_url,
        "readme_date_stamped_github_api_url": readme_date_stamped_github_api_url,
        "readme_history_pages_url": readme_history_pages_url,
        "readme_history_raw_url": readme_history_raw_url,
        "readme_cache_bypass_order": [
            "readme_date_stamped_pages_url",
            "readme_date_stamped_raw_url",
            "readme_date_stamped_github_api_url",
            "readme_index_github_api_url",
            "readme_history_pages_url",
            "readme_history_raw_url",
            "readme_latest_pages_url",
            "readme_latest_raw_url",
        ],
        "preferred_chatgpt_url": preferred,
        "read_order": [
            "packet_pages_url",
            "packet_commit_raw_url",
            "packet_latest_raw_url",
            "packet_github_api_url",
        ],
        "packet_pages_url": packet_pages_url,
        "packet_latest_raw_url": packet_latest_raw_url,
        "packet_commit_raw_url": packet_commit_raw_url,
        "packet_github_api_url": packet_github_api_url,
        "summary_latest_raw_url": summary_latest_raw_url,
        "full_latest_raw_url": full_latest_raw_url,
        "daily_market_curated_pdf_pages_url": daily_market_curated_pdf_pages_url,
        "daily_market_curated_pdf_raw_url": daily_market_curated_pdf_raw_url,
        "daily_market_full_table_pdf_pages_url": daily_market_full_table_pdf_pages_url,
        "daily_market_full_table_pdf_raw_url": daily_market_full_table_pdf_raw_url,
        "fixed_pdf_validation_status": fixed_pdf_validation_status,
        "fixed_pdf_validation_raw_url": fixed_pdf_validation_raw_url,
        "pdf_kline_status_pages_url": pdf_kline_status_pages_url,
        "pdf_kline_status_raw_url": pdf_kline_status_raw_url,
        "summary_pdf_kline_policy": pdf_kline_policy,
        "summary_pdf_kline_status": pdf_kline_status,
        "summary_pdf_kline_total_charts": pdf_kline_total_charts,
        "summary_pdf_kline_local_price_redraw_count": pdf_kline_local_price_redraw_count,
        "summary_pdf_chart_path_and_chart_url_are_fallback_only": True,
        "do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed": True,
        "fundamental_catalyst_layer_raw_url": fundamental_catalyst_layer_raw_url,
        "theme_event_calendar_raw_url": theme_event_calendar_raw_url,
        "company_theme_mapping_raw_url": company_theme_mapping_raw_url,
        "quarterly_catalyst_raw_url": quarterly_catalyst_raw_url,
        "event_catalyst_log_raw_url": event_catalyst_log_raw_url,
        "catalyst_summary_raw_url": catalyst_summary_raw_url,
        "catalyst_summary_csv_raw_url": catalyst_summary_csv_raw_url,
        "catalyst_performance_raw_url": catalyst_performance_raw_url,
        "catalyst_layer_validation_raw_url": catalyst_layer_validation_raw_url,
        "company_event_calendar_raw_url": company_event_calendar_raw_url,
        "macro_event_calendar_raw_url": macro_event_calendar_raw_url,
        "upcoming_catalyst_calendar_raw_url": upcoming_catalyst_calendar_raw_url,
        "upcoming_macro_event_calendar_raw_url": upcoming_macro_event_calendar_raw_url,
        "calendar_data_source_status_raw_url": calendar_data_source_status_raw_url,
        "event_calendar_validation_raw_url": event_calendar_validation_raw_url,
        "catalyst_needs_review_csv_raw_url": catalyst_needs_review_csv_raw_url,
        "catalyst_needs_review_md_raw_url": catalyst_needs_review_md_raw_url,
        "data_source_priority": "raw_structured_data_first,pdf_auxiliary_only,pdf_only_if_raw_unavailable",
        "pdf_only_disclosure_required": True,
        "daily_signal_performance_summary_raw_url": daily_signal_performance_summary_raw_url,
        "daily_signal_performance_weekly_md_raw_url": daily_signal_performance_weekly_md_raw_url,
        "daily_signal_performance_weekly_pdf_pages_url": daily_signal_performance_weekly_pdf_pages_url,
        "daily_signal_performance_weekly_pdf_raw_url": daily_signal_performance_weekly_pdf_raw_url,
        "daily_signal_performance_monthly_md_raw_url": daily_signal_performance_monthly_md_raw_url,
        "daily_signal_performance_monthly_pdf_pages_url": daily_signal_performance_monthly_pdf_pages_url,
        "daily_signal_performance_monthly_pdf_raw_url": daily_signal_performance_monthly_pdf_raw_url,
        "daily_candidate_signal_log_raw_url": daily_candidate_signal_log_raw_url,
        "candidate_repeat_appearance_raw_url": candidate_repeat_appearance_raw_url,
        "candidate_repeat_appearance_md_raw_url": candidate_repeat_appearance_md_raw_url,
        "daily_candidate_decision_raw_url": raw_url("main", DAILY_CANDIDATE_DECISION_CSV),
        "daily_candidate_decision_md_raw_url": raw_url("main", DAILY_CANDIDATE_DECISION_MD),
        "daily_candidate_decision_chatgpt_packet_raw_url": raw_url("main", DAILY_CANDIDATE_DECISION_PACKET_MD),
        "daily_theme_leadership_pages_url": pages_url("latest/daily_theme_leadership_latest.csv"),
        "daily_theme_leadership_raw_url": raw_url("main", DAILY_THEME_LEADERSHIP_CSV),
        "daily_theme_leadership_md_pages_url": pages_url("latest/daily_theme_leadership_latest.md"),
        "daily_theme_leadership_md_raw_url": raw_url("main", DAILY_THEME_LEADERSHIP_MD),
        "daily_candidate_two_line_view_pages_url": pages_url("latest/daily_candidate_two_line_view_latest.csv"),
        "daily_candidate_two_line_view_raw_url": raw_url("main", DAILY_CANDIDATE_TWO_LINE_VIEW_CSV),
        "daily_candidate_two_line_view_md_pages_url": pages_url("latest/daily_candidate_two_line_view_latest.md"),
        "daily_candidate_two_line_view_md_raw_url": raw_url("main", DAILY_CANDIDATE_TWO_LINE_VIEW_MD),
        "chatgpt_indicator_usage_guide_md_raw_url": raw_url("main", INDICATOR_USAGE_GUIDE_MD),
        "chatgpt_indicator_usage_guide_txt_raw_url": raw_url("main", INDICATOR_USAGE_GUIDE_TXT),
        "chatgpt_indicator_usage_guide_pages_url": pages_url("latest/chatgpt_indicator_usage_guide_latest.md"),
        "chatgpt_indicator_usage_guide_txt_pages_url": pages_url("latest/CHATGPT_INDICATOR_USAGE_GUIDE.txt"),
        "volume_breakout_watch_md_raw_url": raw_url("main", VOLUME_BREAKOUT_WATCH_MD),
        "volume_breakout_watch_csv_raw_url": raw_url("main", VOLUME_BREAKOUT_WATCH_CSV),
        "volume_breakout_backtest_md_raw_url": raw_url("main", VOLUME_BREAKOUT_BACKTEST_MD),
        "volume_breakout_backtest_csv_raw_url": raw_url("main", VOLUME_BREAKOUT_BACKTEST_CSV),
        "volume_breakout_chatgpt_packet_raw_url": raw_url("main", VOLUME_BREAKOUT_PACKET_MD),
        "volume_attack_theme_layer_md_raw_url": raw_url("main", VOLUME_ATTACK_THEME_LAYER_MD),
        "volume_attack_theme_layer_csv_raw_url": raw_url("main", VOLUME_ATTACK_THEME_LAYER_CSV),
        "volume_attack_theme_layer_md_pages_url": pages_url("latest/volume_attack_theme_layer_latest.md"),
        "volume_attack_theme_layer_csv_pages_url": pages_url("latest/volume_attack_theme_layer_latest.csv"),
        "volume_attack_theme_stocks_md_raw_url": raw_url("main", VOLUME_ATTACK_THEME_STOCKS_MD),
        "volume_attack_theme_stocks_csv_raw_url": raw_url("main", VOLUME_ATTACK_THEME_STOCKS_CSV),
        "volume_attack_theme_stocks_md_pages_url": pages_url("latest/volume_attack_theme_stocks_latest.md"),
        "volume_attack_theme_stocks_csv_pages_url": pages_url("latest/volume_attack_theme_stocks_latest.csv"),
        "tdcc_overheated_short_term_edge_md_raw_url": raw_url("main", TDCC_OVERHEATED_EDGE_MD),
        "tdcc_overheated_short_term_edge_csv_raw_url": raw_url("main", TDCC_OVERHEATED_EDGE_CSV),
        "tdcc_overheated_short_term_edge_candidates_csv_raw_url": raw_url("main", TDCC_OVERHEATED_EDGE_CANDIDATES_CSV),
        "tdcc_overheated_short_term_edge_md_pages_url": pages_url("latest/tdcc_overheated_short_term_edge_latest.md"),
        "tdcc_overheated_short_term_edge_csv_pages_url": pages_url("latest/tdcc_overheated_short_term_edge_latest.csv"),
        "tdcc_overheated_short_term_edge_candidates_csv_pages_url": pages_url("latest/tdcc_overheated_short_term_edge_candidates_latest.csv"),
        "raw_data_fetch_status_raw_url": raw_url("main", RAW_DATA_FETCH_STATUS_CSV),
        "raw_data_fetch_status_md_raw_url": raw_url("main", RAW_DATA_FETCH_STATUS_MD),
        "raw_data_fetch_status_pages_url": pages_url("latest/raw_data_fetch_status_latest.csv"),
        "raw_data_fetch_status_md_pages_url": pages_url("latest/raw_data_fetch_status_latest.md"),
        "raw_data_fetch_status_github_api_url": github_api_url(RAW_DATA_FETCH_STATUS_CSV, ref="main"),
        "raw_data_fetch_status_md_github_api_url": github_api_url(RAW_DATA_FETCH_STATUS_MD, ref="main"),
        "individual_stock_available_raw_data_index_raw_url": raw_url("main", INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_CSV),
        "individual_stock_available_raw_data_index_md_raw_url": raw_url("main", INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_MD),
        "individual_stock_available_raw_data_index_pages_url": pages_url("latest/individual_stock_available_raw_data_index.csv"),
        "individual_stock_available_raw_data_index_md_pages_url": pages_url("latest/individual_stock_available_raw_data_index.md"),
        "individual_stock_available_raw_data_index_github_api_url": github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_CSV, ref="main"),
        "individual_stock_available_raw_data_index_md_github_api_url": github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_MD, ref="main"),
        "individual_stock_available_raw_data_index_slim_raw_url": raw_url("main", INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_CSV),
        "individual_stock_available_raw_data_index_slim_md_raw_url": raw_url("main", INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_MD),
        "individual_stock_available_raw_data_index_slim_pages_url": pages_url("latest/individual_stock_available_raw_data_index_slim.csv"),
        "individual_stock_available_raw_data_index_slim_md_pages_url": pages_url("latest/individual_stock_available_raw_data_index_slim.md"),
        "individual_stock_available_raw_data_index_slim_github_api_url": github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_CSV, ref="main"),
        "individual_stock_available_raw_data_index_slim_md_github_api_url": github_api_url(INDIVIDUAL_STOCK_AVAILABLE_RAW_DATA_INDEX_SLIM_MD, ref="main"),
        "individual_stock_read_protocol_raw_url": raw_url("main", INDIVIDUAL_STOCK_READ_PROTOCOL_MD),
        "individual_stock_read_protocol_pages_url": pages_url("latest/individual_stock_read_protocol_latest.md"),
        "individual_stock_read_protocol_github_api_url": github_api_url(INDIVIDUAL_STOCK_READ_PROTOCOL_MD, ref="main"),
        "individual_stock_reports_index_raw_url": raw_url("main", INDIVIDUAL_STOCK_REPORTS_INDEX_CSV),
        "individual_stock_reports_index_md_raw_url": raw_url("main", INDIVIDUAL_STOCK_REPORTS_INDEX_MD),
        "individual_stock_reports_index_pages_url": pages_url("latest/individual_stock_reports_index.csv"),
        "individual_stock_reports_index_md_pages_url": pages_url("latest/individual_stock_reports_index.md"),
        "individual_stock_reports_index_github_api_url": github_api_url(INDIVIDUAL_STOCK_REPORTS_INDEX_CSV, ref="main"),
        "individual_stock_reports_index_md_github_api_url": github_api_url(INDIVIDUAL_STOCK_REPORTS_INDEX_MD, ref="main"),
        "individual_stock_chatgpt_packet_index_raw_url": raw_url("main", INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_CSV),
        "individual_stock_chatgpt_packet_index_md_raw_url": raw_url("main", INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_MD),
        "individual_stock_chatgpt_packet_index_pages_url": pages_url("latest/individual_stock_chatgpt_packet_index.csv"),
        "individual_stock_chatgpt_packet_index_md_pages_url": pages_url("latest/individual_stock_chatgpt_packet_index.md"),
        "individual_stock_chatgpt_packet_index_github_api_url": github_api_url(INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_CSV, ref="main"),
        "individual_stock_chatgpt_packet_index_md_github_api_url": github_api_url(INDIVIDUAL_STOCK_CHATGPT_PACKET_INDEX_MD, ref="main"),
        "individual_stock_chatgpt_packet_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md",
        "individual_stock_chatgpt_packet_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md",
        "individual_stock_chatgpt_packet_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_chatgpt_packets/{stock_id}_packet_latest.md?ref=main",
        "individual_stock_price_window_180_html_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html",
        "individual_stock_price_window_180_html_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html",
        "individual_stock_price_window_180_html_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.html?ref=main",
        "individual_stock_price_window_180_txt_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt",
        "individual_stock_price_window_180_txt_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt",
        "individual_stock_price_window_180_txt_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_price_windows/{stock_id}_price_window_180_latest.txt?ref=main",
        "individual_stock_tdcc_window_txt_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt",
        "individual_stock_tdcc_window_txt_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt",
        "individual_stock_tdcc_window_txt_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_tdcc_windows/{stock_id}_tdcc_window_latest.txt?ref=main",
        "individual_stock_primary_read_order": "individual_stock_chatgpt_packet_pages_url_template,individual_stock_chatgpt_packet_raw_url_template,individual_stock_chatgpt_packet_github_api_url_template,individual_stock_price_window_180_html_pages_url_template,individual_stock_price_window_180_html_raw_url_template,individual_stock_price_window_180_html_github_api_url_template,individual_stock_price_github_api_url_template,individual_stock_tdcc_github_api_url_template",
        "individual_stock_price_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/{stock_id}.csv",
        "individual_stock_price_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/data/stock_price_history/{stock_id}.csv",
        "individual_stock_price_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/{stock_id}.csv?ref=main",
        "individual_stock_tdcc_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/{stock_id}.csv",
        "individual_stock_tdcc_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/data/tdcc_stock_history/{stock_id}.csv",
        "individual_stock_tdcc_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/{stock_id}.csv?ref=main",
        "individual_stock_report_md_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/{stock_id}_latest.md",
        "individual_stock_report_md_pages_url_template": "https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/{stock_id}_latest.md",
        "individual_stock_report_md_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.md?ref=main",
        "individual_stock_report_json_github_api_url_template": "https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/{stock_id}_latest.json?ref=main",
        "individual_stock_sell_strategy_summary_raw_url_template": "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/history/sell_strategy_backtest/{stock_id}_sell_strategy_summary.md",
        "individual_stock_raw_cache_rule": "if raw/pages returns cache_miss, internal_error, stale date, or Total lines 1 for a known multi-line CSV, use the GitHub API contents URL and base64-decode content; do not replace repo price/TDCC raw data with external websites.",
        "individual_stock_github_api_decode_required": True,
        "warrant_market_report_md_raw_url": warrant_market_report_md_raw_url,
        "warrant_market_report_pdf_pages_url": warrant_market_report_pdf_pages_url,
        "warrant_market_report_pdf_raw_url": warrant_market_report_pdf_raw_url,
        "warrant_flow_by_stock_raw_url": warrant_flow_by_stock_raw_url,
        "warrant_sector_heat_raw_url": warrant_sector_heat_raw_url,
        "warrant_signal_performance_raw_url": warrant_signal_performance_raw_url,
        "market_regime_raw_url": market_regime_raw_url,
        "market_index_history_raw_url": raw_url("main", MARKET_INDEX_HISTORY_CSV),
        "market_index_ohlc_history_raw_url": raw_url("main", MARKET_INDEX_OHLC_HISTORY_CSV),
        "market_risk_dashboard_md_raw_url": market_risk_dashboard_md_raw_url,
        "market_risk_dashboard_pdf_pages_url": market_risk_dashboard_pdf_pages_url,
        "market_risk_dashboard_pdf_raw_url": market_risk_dashboard_pdf_raw_url,
        "futures_options_indicators_raw_url": futures_options_indicators_raw_url,
        "futures_options_source_status_raw_url": futures_options_source_status_raw_url,
        "market_timing_chatgpt_packet_raw_url": raw_url("main", MARKET_TIMING_PACKET_MD),
        "market_timing_backtest_md_raw_url": raw_url("main", MARKET_TIMING_BACKTEST_MD),
        "market_timing_backtest_csv_raw_url": raw_url("main", MARKET_TIMING_BACKTEST_CSV),
        "market_timing_composite_backtest_md_raw_url": raw_url("main", MARKET_TIMING_COMPOSITE_MD),
        "market_timing_composite_backtest_csv_raw_url": raw_url("main", MARKET_TIMING_COMPOSITE_CSV),
        "market_timing_regime_effectiveness_md_raw_url": raw_url("main", MARKET_TIMING_REGIME_MD),
        "market_timing_regime_effectiveness_csv_raw_url": raw_url("main", MARKET_TIMING_REGIME_CSV),
        "market_technical_feature_panel_raw_url": raw_url("main", MARKET_TECHNICAL_FEATURE_PANEL),
        "market_technical_event_log_raw_url": raw_url("main", MARKET_TECHNICAL_EVENT_LOG),
        "market_breadth_history_raw_url": raw_url("main", MARKET_BREADTH_HISTORY),
        "tdcc_strength_ranking_top_md_raw_url": raw_url("main", TDCC_STRENGTH_RANKING_TOP_MD),
        "tdcc_strength_ranking_top_csv_raw_url": raw_url("main", TDCC_STRENGTH_RANKING_TOP_CSV),
        "tdcc_pre_move_abm_top_md_raw_url": raw_url("main", TDCC_PRE_MOVE_ABM_TOP_MD),
        "tdcc_pre_move_abm_top_csv_raw_url": raw_url("main", TDCC_PRE_MOVE_ABM_TOP_CSV),
        "tdcc_phase_distribution_md_raw_url": raw_url("main", TDCC_PHASE_DISTRIBUTION_MD),
        "tdcc_phase_distribution_csv_raw_url": raw_url("main", TDCC_PHASE_DISTRIBUTION_CSV),
        "tdcc_top_risk_list_md_raw_url": raw_url("main", TDCC_TOP_RISK_LIST_MD),
        "tdcc_top_risk_list_csv_raw_url": raw_url("main", TDCC_TOP_RISK_LIST_CSV),
        "tdcc_chatgpt_tracking_packet_raw_url": raw_url("main", TDCC_CHATGPT_TRACKING_PACKET_MD),
        "surge_model_chatgpt_packet_raw_url": raw_url("main", SURGE_MODEL_PACKET_MD),
        "surge_precondition_candidates_md_raw_url": raw_url("main", SURGE_PRECONDITION_CANDIDATES_MD),
        "surge_precondition_candidates_csv_raw_url": raw_url("main", SURGE_PRECONDITION_CANDIDATES_CSV),
        "surge_model_backtest_md_raw_url": raw_url("main", SURGE_MODEL_BACKTEST_MD),
        "surge_model_backtest_csv_raw_url": raw_url("main", SURGE_MODEL_BACKTEST_CSV),
        "surge_model_feature_importance_md_raw_url": raw_url("main", SURGE_MODEL_FEATURE_IMPORTANCE_MD),
        "surge_model_feature_importance_csv_raw_url": raw_url("main", SURGE_MODEL_FEATURE_IMPORTANCE_CSV),
        "surge_model_validation_raw_url": raw_url("main", SURGE_MODEL_VALIDATION_MD),
        "rules_pages_url": rules_pages_url,
        "rules_raw_url": rules_raw_url,
        "checks": checks,
    }

    PUBLISH_CHECK_JSON.write_text(
        json.dumps(publish_check_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Saved: {README_TXT}")
    print(f"Saved: {DOCS_README_TXT}")
    print(f"Saved: {README_INDEX_TXT}")
    print(f"Saved: {README_INDEX_JSON}")
    print(f"Saved: {DOCS_README_INDEX_TXT}")
    print(f"Saved: {DOCS_README_INDEX_JSON}")
    print(f"Saved: {readme_date_stamped}")
    print(f"Saved: {docs_readme_date_stamped}")
    print(f"Saved: {history_readme}")
    print(f"Saved: {docs_history_readme}")
    print(f"Saved: {PUBLISH_CHECK_MD}")
    print(f"Saved: {PUBLISH_CHECK_JSON}")
    print(f"preferred_chatgpt_url={preferred}")
    print(f"rules_pages_url={rules_pages_url}")
    print(f"rules_raw_url={rules_raw_url}")

    for item in checks:
        print(f"{item.get('label')} ok={item.get('ok')} url={item.get('url')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
