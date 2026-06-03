from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
import shutil
from typing import Any

import pandas as pd


REPO_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")
DOCS_LATEST_DIR = Path("docs/latest")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
REPORT_MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
PDF_KLINE_STATUS_JSON = LATEST_DIR / "pdf_kline_chart_status_latest.json"
PDF_KLINE_STATUS_MD = LATEST_DIR / "pdf_kline_chart_status_latest.md"
FIXED_PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"
FIXED_PDF_VALIDATION_JSON = LATEST_DIR / "daily_market_report_validation_latest.json"
DAILY_SIGNAL_LOG = Path("output/history/daily_signals/daily_candidate_signal_log.csv")
DAILY_CANDIDATE_SIGNAL_LOG = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")
DAILY_SIGNAL_PERFORMANCE = Path("output/history/daily_signals/daily_candidate_signal_performance.csv")
DAILY_SIGNAL_SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
CANDIDATE_REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
CANDIDATE_REPEAT_MD = LATEST_DIR / "candidate_repeat_appearance_latest.md"
DAILY_CANDIDATE_DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
DAILY_CANDIDATE_DECISION_MD = LATEST_DIR / "daily_candidate_decision_latest.md"
DAILY_CANDIDATE_DECISION_PACKET_MD = LATEST_DIR / "daily_candidate_decision_chatgpt_packet_latest.md"
DAILY_THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
DAILY_THEME_LEADERSHIP_MD = LATEST_DIR / "daily_theme_leadership_latest.md"
DAILY_CANDIDATE_TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
DAILY_CANDIDATE_TWO_LINE_VIEW_MD = LATEST_DIR / "daily_candidate_two_line_view_latest.md"
INDICATOR_USAGE_GUIDE_MD = LATEST_DIR / "chatgpt_indicator_usage_guide_latest.md"
INDICATOR_USAGE_GUIDE_TXT = LATEST_DIR / "CHATGPT_INDICATOR_USAGE_GUIDE.txt"
SHORT_TERM_SPECIALTY_PACKET_MD = LATEST_DIR / "daily_short_term_specialty_packet_latest.md"
NON_REVENUE_MOMENTUM_MD = LATEST_DIR / "non_revenue_momentum_watch_latest.md"
NON_REVENUE_MOMENTUM_CSV = LATEST_DIR / "non_revenue_momentum_watch_latest.csv"
MARKET_ABNORMAL_STATUS_MD = LATEST_DIR / "market_abnormal_status_latest.md"
MARKET_ABNORMAL_STATUS_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"
MSCI_REBALANCE_BACKTEST_MD = LATEST_DIR / "msci_taiwan_rebalance_backtest_latest.md"
MSCI_REBALANCE_BACKTEST_CSV = LATEST_DIR / "msci_taiwan_rebalance_backtest_latest.csv"
MSCI_REBALANCE_EVENTS_CSV = LATEST_DIR / "msci_taiwan_rebalance_events_latest.csv"
DAILY_SIGNAL_WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DAILY_SIGNAL_MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
FUNDAMENTAL_CATALYST_MD = LATEST_DIR / "fundamental_catalyst_layer_latest.md"
CATALYST_SUMMARY_MD = LATEST_DIR / "catalyst_summary_latest.md"
CATALYST_SUMMARY_CSV = LATEST_DIR / "catalyst_summary_latest.csv"
CATALYST_VALIDATION_MD = LATEST_DIR / "catalyst_layer_validation_latest.md"
CATALYST_PERFORMANCE_CSV = Path("output/history/catalyst_performance/catalyst_performance.csv")
THEME_EVENT_CALENDAR = Path("data/theme_events/theme_event_calendar.csv")
THEME_EVENT_WATCH_CSV = LATEST_DIR / "theme_event_watch_latest.csv"
THEME_EVENT_WATCH_MD = LATEST_DIR / "theme_event_watch_latest.md"
COMPANY_THEME_MAPPING = Path("data/theme_events/company_theme_mapping.csv")
QUARTERLY_CATALYST = Path("data/fundamental_catalysts/quarterly_catalyst.csv")
EVENT_CATALYST_LOG = Path("data/event_catalysts/event_catalyst_log.csv")
COMPANY_EVENT_CALENDAR = Path("data/company_calendar/company_event_calendar.csv")
MACRO_EVENT_CALENDAR = Path("data/macro_events/macro_event_calendar.csv")
UPCOMING_CATALYST_CALENDAR = LATEST_DIR / "upcoming_catalyst_calendar_latest.csv"
UPCOMING_MACRO_EVENT_CALENDAR = LATEST_DIR / "upcoming_macro_event_calendar_latest.csv"
CALENDAR_DATA_SOURCE_STATUS = LATEST_DIR / "calendar_data_source_status_latest.md"
EVENT_CALENDAR_VALIDATION = LATEST_DIR / "event_calendar_validation_latest.md"
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
FUTURES_OPTIONS_INDICATORS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
FUTURES_OPTIONS_SOURCE_STATUS_MD = LATEST_DIR / "futures_options_source_status_latest.md"
MARKET_SENTIMENT_CONTEXT_CSV = LATEST_DIR / "market_sentiment_context_latest.csv"
MARKET_SENTIMENT_CONTEXT_MD = LATEST_DIR / "market_sentiment_context_latest.md"
MARKET_SENTIMENT_CONTEXT_HISTORY_CSV = Path("output/history/market_risk/market_sentiment_context_history.csv")
VIX_HISTORY_CSV = Path("output/history/market_risk/vix_history.csv")
RETAIL_MTX_SENTIMENT_HISTORY_CSV = Path("output/history/market_risk/retail_mtx_sentiment_history.csv")
FUTURES_OPTIONS_INDICATORS_HISTORY_CSV = Path("output/history/market_risk/futures_options_indicators_history.csv")
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

SUMMARY_LATEST_MD = LATEST_DIR / "daily_market_summary_latest.md"
FULL_LATEST_MD = LATEST_DIR / "daily_market_full_latest.md"
SUMMARY_LATEST_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
FULL_LATEST_PDF = LATEST_DIR / "daily_market_full_latest.pdf"
CURATED_REPORT_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_REPORT_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"

SUMMARY_CN_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
FULL_CN_MD = LATEST_DIR / "完整候選股清單_完整版.md"
SUMMARY_CN_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
FULL_CN_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

PACKET_LATEST_OLD = LATEST_DIR / "CHATGPT_DAILY_REPORT_PACKET.txt"
PACKET_LATEST = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
DOCS_PACKET_LATEST = DOCS_LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
PACKET_MANIFEST = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"

DISPLAY_TOKEN_MAP = {
    "call_put_bullish": "認購/認售結構偏多",
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購流入",
    "put_strong_inflow": "認售強流入",
    "put_inflow": "認售流入",
    "put_call_bearish": "認售/認購結構偏空",
    "mixed_flow": "多空混合",
    "no_signal": "無明確訊號",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "revenue_pullback": "營收成長股價回檔",
    "revenue_breakout_low_response": "營收爆發股價尚未反應",
    "pullback_rebound": "回檔後短線轉強",
    "true_breakout": "嚴格突破",
    "pattern": "型態觀察",
    "pattern_watch": "型態觀察",
    "short_term_specialty": "短線專項",
    "strong_accumulation": "大戶強正向",
    "mild_accumulation": "大戶正向",
    "distribution_warning": "TDCC 大戶轉弱",
    "stale_signal": "反覆上榜未突破",
}


DISPLAY_TOKEN_SUBSTRING_MAP = {
    "short_term_specialty_not_six_category": "短線專項（非六大分類）",
    "tdcc_short_term_continuation_d5_d10": "TDCC短線延續模型 D+5/D+10",
    "tdcc_short_term_edge": "TDCC短線延續",
    "semiconductor_equipment_theme": "半導體設備族群",
    "semiconductor_theme": "半導體族群",
    "consumer_electronics_theme": "消費電子族群",
    "passive_component_theme": "被動元件族群",
    "memory_theme": "記憶體族群",
    "power_discrete_theme": "功率元件族群",
    "core_mainstream_theme": "核心主流題材",
    "mainstream_growth_theme": "主流成長題材",
    "theme_context_unavailable": "族群脈絡不足",
    "structural_theme_bucket": "結構族群",
    "hot_theme_tag": "熱門族群標籤",
    "bottom_or_low_zone_volume_reversal": "低位爆量反轉",
    "long_base_low_zone_volume_reversal": "長底低位爆量反轉",
    "low_to_mid_reclaim_volume_attack": "低中位站回放量攻擊",
    "mid_range_volume_attack": "中位放量攻擊",
    "near_high_volume_attack": "近高放量攻擊",
    "high_zone_extension_or_chase": "高位延伸或追價",
    "strict_red_close_near_high": "強紅K收近高",
    "relaxed_red_small_upper_shadow": "紅K小上影",
    "invalid_intraday_range": "日內區間資料不足",
    "insufficient_position_history": "位階歷史不足",
    "overheated_after_tdcc": "TDCC後股價過熱",
    "phase_overheated_after_tdcc": "TDCC後股價過熱階段",
    "price_leading_tdcc": "股價領先TDCC",
    "tdcc_leading_price": "TDCC領先股價",
    "tdcc_price_confirmed": "TDCC與股價確認",
    "tdcc_price_divergence": "TDCC與股價背離",
    "continued_overheated": "連續過熱",
    "insufficient_data": "資料不足",
    "other electronics": "其他電子",
    "semiconductor equipment": "半導體設備",
    "semiconductor": "半導體",
    "power discrete": "功率元件",
    "networking": "網通",
    "biotechnology": "生技",
    "connector/cable": "連接器/線材",
    "memory": "記憶體",
}


def is_machine_readable_packet_line(line: str) -> bool:
    lowered = line.lower()
    machine_markers = [
        "raw_url:",
        "_raw_url:",
        "_path:",
        "path:",
        "http://",
        "https://",
        "chart_path",
        "chart_url",
        "file_path",
        "fields:",
    ]
    return any(marker in lowered for marker in machine_markers)


def sanitize_display_text(text: str) -> str:
    sanitized_lines: list[str] = []
    substring_items = sorted(
        DISPLAY_TOKEN_SUBSTRING_MAP.items(),
        key=lambda item: len(item[0]),
        reverse=True,
    )
    for line in text.splitlines():
        if not is_machine_readable_packet_line(line):
            line = line.replace("memory-based interpretations", "舊記憶解讀")
            for raw, label in substring_items:
                line = line.replace(raw, label)
            for raw, label in DISPLAY_TOKEN_MAP.items():
                pattern = rf"(?<![A-Za-z0-9_]){re.escape(raw)}(?![A-Za-z0-9_])"
                line = re.sub(pattern, label, line)
            line = line.replace("記憶體-based interpretation", "舊記憶解讀")
            line = line.replace("記憶體-based interpretations", "舊記憶解讀")
        sanitized_lines.append(line)
    return "\n".join(sanitized_lines) + ("\n" if text.endswith("\n") else "")


DISPLAY_TOKEN_SUBSTRING_MAP.update(
    {
        "tdcc_distribution_penalty": "TDCC轉弱扣分",
        "false_breakout_risk_penalty": "假突破風險扣分",
        "continued_many_days": "連續多日上榜",
        "repeated_but_no_breakout": "反覆上榜未突破",
    }
)


DISPLAY_TOKEN_MAP.update(
    {
        "call_put_bullish": "認購/認售結構偏多",
        "call_strong_inflow": "認購強流入",
        "call_inflow": "認購流入",
        "put_strong_inflow": "認售強流入",
        "put_inflow": "認售流入",
        "put_call_bearish": "認售/認購結構偏空",
        "mixed_flow": "多空混合",
        "call_activity_observation": "認購活躍觀察",
        "put_activity_observation": "認售活躍觀察",
        "low_float_call_spike": "低流通認購異常",
        "no_signal": "無明確訊號",
        "range_rebound": "區間內轉強 / 挑戰前高觀察",
        "revenue_pullback": "營收成長股價回檔",
        "revenue_breakout_low_response": "營收爆發但股價尚未反應",
        "pullback_rebound": "回檔後短線轉強",
        "true_breakout": "嚴格突破",
        "pattern": "型態觀察",
        "pattern_watch": "型態觀察",
        "short_term_specialty": "短線專項",
        "strong_accumulation": "大戶同步增加",
        "mild_accumulation": "大戶溫和增加",
        "distribution_warning": "TDCC 大戶轉弱",
        "stale_signal": "反覆上榜未突破",
        "tdcc_distribution_penalty": "TDCC 轉弱扣分",
        "false_breakout_risk_penalty": "假突破風險扣分",
        "continued_many_days": "連續多日上榜",
        "repeated_but_no_breakout": "反覆上榜未突破",
    }
)


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


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for enc in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            pass

    return ""


def safe_copy(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return True


def raw_url(path: Path, ref: str = "main") -> str:
    return f"https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/{ref}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    elif path.as_posix().startswith("output/latest/"):
        rel = path.relative_to("output").as_posix()
    else:
        rel = path.as_posix()
    return f"https://LeoChen0727.github.io/tdcc-weekly-report/{rel}"


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


def extract_data_freshness() -> dict[str, Any]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
        "report_ready_note": "",
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
                result["report_ready_note"] = str(row.get("report_ready_note", "")).strip()
                return result
        except Exception:
            pass

    text = safe_read_text(DATA_FRESHNESS_MD)

    m = re.search(r"主資料日期[：:\s`]*([0-9/\-]{8,10})", text)
    if m:
        result["main_price_date"] = normalize_date(m.group(1))

    m = re.search(r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)", text)
    if m:
        result["report_ready"] = m.group(1)

    return result


def extract_main_meta() -> dict[str, Any]:
    freshness = extract_data_freshness()
    manifest = read_json(REPORT_MANIFEST_JSON)

    main_date = (
        normalize_date(manifest.get("main_price_date", ""))
        or normalize_date(manifest.get("price_date", ""))
        or normalize_date(manifest.get("date", ""))
        or freshness.get("main_price_date", "")
    )

    report_ready = (
        str(manifest.get("report_ready", "")).strip()
        or str(manifest.get("ready", "")).strip()
        or freshness.get("report_ready", "")
    )

    if not main_date:
        main_date = now_taipei().strftime("%Y%m%d")

    if not report_ready:
        report_ready = "False"

    return {
        "main_price_date": main_date,
        "report_ready": report_ready,
        "freshness": freshness,
        "manifest": manifest,
    }


def ensure_dated_artifacts(main_date: str) -> dict[str, Path]:
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    dated_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    dated_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    dated_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    dated_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    dated_summary_cn_md = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.md"
    dated_full_cn_md = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版.md"
    dated_summary_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.pdf"
    dated_full_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版表格.pdf"

    safe_copy(SUMMARY_LATEST_MD, dated_summary_md)
    safe_copy(FULL_LATEST_MD, dated_full_md)
    safe_copy(SUMMARY_LATEST_PDF, dated_summary_pdf)
    safe_copy(FULL_LATEST_PDF, dated_full_pdf)

    safe_copy(SUMMARY_CN_MD, dated_summary_cn_md)
    safe_copy(FULL_CN_MD, dated_full_cn_md)
    safe_copy(SUMMARY_CN_PDF, dated_summary_cn_pdf)
    safe_copy(FULL_CN_PDF, dated_full_cn_pdf)

    return {
        "dated_summary_md": dated_summary_md,
        "dated_full_md": dated_full_md,
        "dated_summary_pdf": dated_summary_pdf,
        "dated_full_pdf": dated_full_pdf,
        "dated_summary_cn_md": dated_summary_cn_md,
        "dated_full_cn_md": dated_full_cn_md,
        "dated_summary_cn_pdf": dated_summary_cn_pdf,
        "dated_full_cn_pdf": dated_full_cn_pdf,
    }


def build_packet_text(main_date: str, report_ready: str, paths: dict[str, Path], meta: dict[str, Any]) -> str:
    summary_text = safe_read_text(SUMMARY_LATEST_MD)
    full_text = safe_read_text(FULL_LATEST_MD)
    freshness = meta.get("freshness", {})
    report_manifest = read_json(REPORT_MANIFEST_JSON)
    kline_status = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)
    curated_pdf = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf = fixed_pdf_manifest.get("full_table_pdf", {})

    history_packet_path = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    lines: list[str] = []

    lines.append("CHATGPT DAILY REPORT PACKET")
    lines.append("")
    lines.append(f"generated_at: {now_text()}")
    lines.append("repo: LeoChen0727/tdcc-weekly-report")
    lines.append(f"main_price_date: {main_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append(f"all_candidates_date: {freshness.get('all_candidates_date', '')}")
    lines.append(f"official_price_fetch_date: {freshness.get('official_price_fetch_date', '')}")
    lines.append(f"stock_monitor_date: {freshness.get('stock_monitor_date', '')}")
    lines.append(f"warrant_flow_date: {freshness.get('warrant_flow_date', '')}")
    lines.append("")
    lines.append("CHATGPT_DELIVERY_CONTRACT")
    lines.append("repo_artifacts_are_sources_not_final_deliverables: True")
    lines.append("report_ready_meaning: repo data packet and repo artifacts are available; this does not mean ChatGPT has produced the user's requested report.")
    lines.append("fixed_pdf_validation_meaning: repo pipeline PDF artifact validation only; this is not a newly generated ChatGPT deliverable PDF.")
    lines.append("if_user_asks_status_only: report repo artifact status and links only.")
    lines.append("if_user_asks_do_today_report_or_four_pdfs: read repo structured data and produce new ChatGPT-side PDFs; do not stop at repo PDFs.")
    lines.append("default_daily_full_market_chatgpt_deliverables: 每日推薦分析 PDF|完整候選清單補充 PDF|權證市場輔助分析 PDF|市場風險與大盤期權背景 PDF")
    lines.append("do_not_replace_required_chatgpt_pdfs_with_repo_artifacts: True")
    lines.append("do_not_paste_full_text_instead_of_pdf_unless_user_requests_text_only: True")
    lines.append("")
    lines.append("PACKET_PATHS")
    lines.append(f"latest_packet_path: {PACKET_LATEST.as_posix()}")
    lines.append(f"history_packet_path: {history_packet_path.as_posix()}")
    lines.append("")
    lines.append("SUMMARY_PDF_KLINE_STATUS")
    lines.append(f"summary_pdf_path: {SUMMARY_LATEST_PDF.as_posix()}")
    lines.append(f"summary_pdf_kline_policy: {kline_status.get('policy') or report_manifest.get('summary_pdf_kline_policy', 'local_price_redraw_first')}")
    lines.append(f"summary_pdf_kline_status: {kline_status.get('status') or report_manifest.get('summary_pdf_kline_status', '')}")
    lines.append(f"summary_pdf_kline_output_dir: {kline_status.get('pdf_kline_output_dir') or report_manifest.get('summary_pdf_kline_output_dir', 'output/latest/charts/pdf_kline')}")
    lines.append(f"summary_pdf_kline_total_charts: {kline_status.get('total_charts', report_manifest.get('summary_pdf_kline_total_charts', 0))}")
    lines.append(f"summary_pdf_kline_local_price_redraw_count: {kline_status.get('local_price_redraw_count', report_manifest.get('summary_pdf_kline_local_price_redraw_count', 0))}")
    lines.append(f"summary_pdf_kline_chart_path_fallback_count: {kline_status.get('chart_path_fallback_count', report_manifest.get('summary_pdf_kline_chart_path_fallback_count', 0))}")
    lines.append(f"summary_pdf_kline_missing_count: {kline_status.get('missing_count', report_manifest.get('summary_pdf_kline_missing_count', 0))}")
    lines.append(f"summary_pdf_kline_status_md_path: {PDF_KLINE_STATUS_MD.as_posix()}")
    lines.append("summary_pdf_chart_path_and_chart_url_are_fallback_only: True")
    lines.append("do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed: True")
    lines.append("note: The summary PDF K-line charts are generated by the pipeline from local/repo daily price data first. Candidate chart_path/chart_url values are fallback references only.")
    lines.append("")
    lines.append("CURATED PDF REPORT")
    lines.append(f"pages_url: {curated_pdf.get('pages_url') or pages_url(Path('docs/latest/daily_market_curated_report_latest.pdf'))}")
    lines.append(f"raw_url: {curated_pdf.get('raw_url') or raw_url(CURATED_REPORT_PDF)}")
    lines.append(f"file_path: {curated_pdf.get('file_path') or CURATED_REPORT_PDF.as_posix()}")
    lines.append(f"generated_at: {fixed_pdf_manifest.get('generated_at', '')}")
    lines.append(f"status: {curated_pdf.get('status') or ('generated' if CURATED_REPORT_PDF.exists() else 'missing')}")
    lines.append("")
    lines.append("FULL TABLE PDF REPORT")
    lines.append(f"pages_url: {full_table_pdf.get('pages_url') or pages_url(Path('docs/latest/daily_market_full_table_report_latest.pdf'))}")
    lines.append(f"raw_url: {full_table_pdf.get('raw_url') or raw_url(FULL_TABLE_REPORT_PDF)}")
    lines.append(f"file_path: {full_table_pdf.get('file_path') or FULL_TABLE_REPORT_PDF.as_posix()}")
    lines.append(f"generated_at: {fixed_pdf_manifest.get('generated_at', '')}")
    lines.append(f"status: {full_table_pdf.get('status') or ('generated' if FULL_TABLE_REPORT_PDF.exists() else 'missing')}")
    lines.append("")
    lines.append("FIXED PDF VALIDATION")
    lines.append(f"status: {fixed_pdf_validation.get('status', '')}")
    lines.append(f"validation_json_path: {FIXED_PDF_VALIDATION_JSON.as_posix()}")
    lines.append(f"validation_md_path: output/latest/daily_market_report_validation_latest.md")
    lines.append("")
    lines.append("DATA SOURCE PRIORITY")
    lines.append("priority_1: Use original structured data first: CSV files, packet fields, source logs, signal logs, warrant tables, market tables, and validated raw URLs.")
    lines.append("priority_2: Use Markdown reports as readable summaries only after checking the structured data when available.")
    lines.append("priority_3: Use PDF reports only when raw/packet/source-table data cannot be read, or when the user specifically asks for the shareable PDF artifact.")
    lines.append("pdf_only_disclosure_required: True")
    lines.append("pdf_only_disclosure_text: 本次僅使用 PDF 報告資料，未讀取原始 CSV / packet / source tables，因此只能做摘要型分析。")
    lines.append("note: PDFs are auxiliary outputs. They are not the primary source when raw data is available.")
    lines.append("")
    lines.append("CHATGPT INDICATOR USAGE GUIDE")
    lines.append(f"indicator_usage_guide_md_raw_url: {raw_url(INDICATOR_USAGE_GUIDE_MD)}")
    lines.append(f"indicator_usage_guide_txt_raw_url: {raw_url(INDICATOR_USAGE_GUIDE_TXT)}")
    lines.append(f"status: {'generated' if INDICATOR_USAGE_GUIDE_MD.exists() and INDICATOR_USAGE_GUIDE_TXT.exists() else 'missing'}")
    lines.append("note: This guide is the cross-indicator routing map. ChatGPT should read it before using memory-based interpretations.")
    lines.append("")
    lines.append("DAILY SHORT-TERM SPECIALTY PACKET")
    lines.append(f"daily_short_term_specialty_packet_raw_url: {raw_url(SHORT_TERM_SPECIALTY_PACKET_MD)}")
    lines.append(f"daily_short_term_specialty_packet_path: {SHORT_TERM_SPECIALTY_PACKET_MD.as_posix()}")
    lines.append(f"status: {'generated' if SHORT_TERM_SPECIALTY_PACKET_MD.exists() else 'missing'}")
    lines.append("required_in_daily_pdf: True")
    lines.append("fields_or_sections: TDCC Overheated Short-Term Edge, Next-Open +10pct Touch Strict Parameter Research, D+5 tables, D+10 tables")
    lines.append("note: Do not translate the legacy `weekly_surge` file prefix as `周線急漲`; display it as `隔日開盤買進後 D+5 / D+10 盤中觸及 +10% 研究`.")
    lines.append("note: Win rate for this section is next-open entry touch-rate: D+1 open to D+N high >= +10%, not close-to-close return.")
    lines.append("note: This is not the fixed six-category `回檔後短線轉強` category. It is a standalone short-term specialty section and must be read separately.")
    lines.append("")
    short_term_text = safe_read_text(SHORT_TERM_SPECIALTY_PACKET_MD)
    lines.append("EMBEDDED DAILY SHORT-TERM SPECIALTY PACKET")
    lines.append("=" * 80)
    if short_term_text.strip():
        lines.append(short_term_text.strip())
    else:
        lines.append("[daily_short_term_specialty_packet_latest.md missing or empty]")
    lines.append("=" * 80)
    lines.append("")
    lines.append("FUNDAMENTAL / EVENT CATALYST LAYER")
    lines.append(f"catalyst_layer_md_raw_url: {raw_url(FUNDAMENTAL_CATALYST_MD)}")
    lines.append(f"catalyst_layer_path: {FUNDAMENTAL_CATALYST_MD.as_posix()}")
    lines.append("fields: theme_strength_score,catalyst_strength_score,catalyst_tags,fundamental_catalyst_score,fundamental_catalyst_tags,event_catalyst_tags,event_calendar_tags,event_proximity_score,nearest_event_date,nearest_event_type,price_reaction_level,similar_to_shihsinko_flag,revenue_good_eps_unconfirmed_flag,already_reacted_to_catalyst,low_reaction_after_catalyst")
    lines.append(f"status: {'generated' if FUNDAMENTAL_CATALYST_MD.exists() else 'missing'}")
    lines.append("note: This is a cross-category tag layer, not a seventh category. Do not upgrade revenue-only candidates without EPS/event source confirmation.")
    lines.append("")
    lines.append("CATALYST DATA LAYER")
    lines.append(f"theme_event_calendar_raw_url: {raw_url(THEME_EVENT_CALENDAR)}")
    lines.append(f"theme_event_watch_csv_raw_url: {raw_url(THEME_EVENT_WATCH_CSV)}")
    lines.append(f"theme_event_watch_md_raw_url: {raw_url(THEME_EVENT_WATCH_MD)}")
    lines.append(f"theme_event_watch_status: {'generated' if THEME_EVENT_WATCH_CSV.exists() and THEME_EVENT_WATCH_MD.exists() else 'missing'}")
    lines.append("theme_event_watch_pdf_section: 近期事件預警 / 主題催化觀察")
    lines.append("theme_event_watch_usage: Event proximity and theme catalyst context only. It is not a standalone buy model and must not override price, volume, TDCC, revenue, or model selection fields.")
    lines.append(f"company_theme_mapping_raw_url: {raw_url(COMPANY_THEME_MAPPING)}")
    lines.append(f"quarterly_catalyst_raw_url: {raw_url(QUARTERLY_CATALYST)}")
    lines.append(f"event_catalyst_log_raw_url: {raw_url(EVENT_CATALYST_LOG)}")
    lines.append(f"catalyst_summary_raw_url: {raw_url(CATALYST_SUMMARY_MD)}")
    lines.append(f"catalyst_summary_csv_raw_url: {raw_url(CATALYST_SUMMARY_CSV)}")
    lines.append(f"catalyst_performance_raw_url: {raw_url(CATALYST_PERFORMANCE_CSV)}")
    lines.append(f"catalyst_layer_validation_raw_url: {raw_url(CATALYST_VALIDATION_MD)}")
    lines.append(f"catalyst_needs_review_csv_raw_url: {raw_url(CATALYST_NEEDS_REVIEW_CSV)}")
    lines.append(f"catalyst_needs_review_md_raw_url: {raw_url(CATALYST_NEEDS_REVIEW_MD)}")
    lines.append(f"status: {'generated' if CATALYST_SUMMARY_MD.exists() and CATALYST_PERFORMANCE_CSV.exists() else 'schema_ready_or_pending'}")
    lines.append("note: Event tables are schema-first. Empty tables mean no confirmed catalyst source has been loaded; do not infer catalysts from rumors. Rows in catalyst_needs_review have model_effect_allowed=False and pdf_effect_allowed=False.")
    lines.append("")
    lines.append("EVENT / MACRO CALENDAR LAYER")
    lines.append(f"company_event_calendar_raw_url: {raw_url(COMPANY_EVENT_CALENDAR)}")
    lines.append(f"macro_event_calendar_raw_url: {raw_url(MACRO_EVENT_CALENDAR)}")
    lines.append(f"upcoming_catalyst_calendar_raw_url: {raw_url(UPCOMING_CATALYST_CALENDAR)}")
    lines.append(f"upcoming_macro_event_calendar_raw_url: {raw_url(UPCOMING_MACRO_EVENT_CALENDAR)}")
    lines.append(f"calendar_data_source_status_raw_url: {raw_url(CALENDAR_DATA_SOURCE_STATUS)}")
    lines.append(f"event_calendar_validation_raw_url: {raw_url(EVENT_CALENDAR_VALIDATION)}")
    lines.append("fields: event_calendar_tags,event_proximity_score,nearest_event_date,nearest_event_type,nearest_event_name,days_to_nearest_event")
    lines.append(f"status: {'generated' if COMPANY_EVENT_CALENDAR.exists() and MACRO_EVENT_CALENDAR.exists() else 'missing'}")
    lines.append("note: Calendar proximity is a reminder layer. It does not create a bullish catalyst unless confirmed event or financial data is also present.")
    if THEME_EVENT_WATCH_MD.exists():
        watch_text = safe_read_text(THEME_EVENT_WATCH_MD).strip()
        if watch_text:
            lines.append("")
            lines.append("THEME EVENT WATCH SUMMARY")
            lines.append("=" * 80)
            lines.extend(watch_text.splitlines()[:120])
            lines.append("=" * 80)
    lines.append("")
    lines.append("SIGNAL PERFORMANCE TRACKING")
    lines.append(f"signal_log_path: {DAILY_SIGNAL_LOG.as_posix()}")
    lines.append(f"performance_csv_path: {DAILY_SIGNAL_PERFORMANCE.as_posix()}")
    lines.append(f"summary_latest_raw_url: {raw_url(DAILY_SIGNAL_SUMMARY_MD)}")
    lines.append(f"weekly_report_pdf_pages_url: {pages_url(Path('docs/latest/daily_signal_performance_weekly_latest.pdf'))}")
    lines.append(f"monthly_report_pdf_pages_url: {pages_url(Path('docs/latest/daily_signal_performance_monthly_latest.pdf'))}")
    lines.append(f"last_updated_at: {now_text()}")
    lines.append(f"status: {'generated' if DAILY_SIGNAL_LOG.exists() and DAILY_SIGNAL_PERFORMANCE.exists() else 'missing'}")
    lines.append("")
    history_available_days = 0
    latest_repeat_signal_date = ""
    try:
        if DAILY_CANDIDATE_SIGNAL_LOG.exists():
            repeat_log_df = pd.read_csv(DAILY_CANDIDATE_SIGNAL_LOG, dtype=str, keep_default_na=False)
        elif DAILY_SIGNAL_LOG.exists():
            repeat_log_df = pd.read_csv(DAILY_SIGNAL_LOG, dtype=str, keep_default_na=False)
        else:
            repeat_log_df = pd.DataFrame()
        if not repeat_log_df.empty and "signal_date" in repeat_log_df.columns:
            dates = sorted({normalize_date(x) for x in repeat_log_df["signal_date"].tolist() if normalize_date(x)})
            history_available_days = len(dates)
            latest_repeat_signal_date = dates[-1] if dates else ""
    except Exception:
        history_available_days = 0
    lines.append("CANDIDATE REPEAT APPEARANCE")
    lines.append(f"signal_log_path: {DAILY_CANDIDATE_SIGNAL_LOG.as_posix()}")
    lines.append(f"legacy_signal_log_path: {DAILY_SIGNAL_LOG.as_posix()}")
    lines.append(f"repeat_appearance_path: {CANDIDATE_REPEAT_CSV.as_posix()}")
    lines.append(f"repeat_appearance_raw_url: {raw_url(CANDIDATE_REPEAT_CSV)}")
    lines.append(f"repeat_appearance_md_raw_url: {raw_url(CANDIDATE_REPEAT_MD)}")
    lines.append(f"history_available_days: {history_available_days}")
    lines.append(f"status: {'generated' if CANDIDATE_REPEAT_CSV.exists() and CANDIDATE_REPEAT_MD.exists() else 'missing'}")
    lines.append(f"latest_signal_date: {latest_repeat_signal_date or main_date}")
    lines.append("fields: consecutive_appear_days_any_category,consecutive_appear_days_same_category,appear_count_5d,appear_count_10d,appear_count_20d,first_seen_date,last_seen_date,multi_category_flags,repeat_appear_label,repeat_appear_note")
    lines.append("note: Repeat appearance is calculated from raw daily candidate signal logs. ChatGPT must not infer consecutive days manually.")
    lines.append("")
    lines.append("DAILY CANDIDATE DECISION LAYER")
    lines.append(f"decision_csv_path: {DAILY_CANDIDATE_DECISION_CSV.as_posix()}")
    lines.append(f"decision_md_raw_url: {raw_url(DAILY_CANDIDATE_DECISION_MD)}")
    lines.append(f"decision_csv_raw_url: {raw_url(DAILY_CANDIDATE_DECISION_CSV)}")
    lines.append(f"decision_chatgpt_packet_raw_url: {raw_url(DAILY_CANDIDATE_DECISION_PACKET_MD)}")
    lines.append(f"status: {'generated' if DAILY_CANDIDATE_DECISION_CSV.exists() and DAILY_CANDIDATE_DECISION_PACKET_MD.exists() else 'missing'}")
    lines.append("fields: pattern_mapped_category,decision_priority,decision_score,downgrade_flags,risk_tags,why_selected,why_downgraded,next_confirmation,must_not_overstate")
    lines.append("note: This is the program-side ranking/downgrade layer. ChatGPT should use it before memory-based interpretation.")
    lines.append("")
    lines.append("DAILY THEME LEADERSHIP LAYER")
    lines.append(f"theme_leadership_csv_raw_url: {raw_url(DAILY_THEME_LEADERSHIP_CSV)}")
    lines.append(f"theme_leadership_md_raw_url: {raw_url(DAILY_THEME_LEADERSHIP_MD)}")
    lines.append(f"candidate_two_line_view_csv_raw_url: {raw_url(DAILY_CANDIDATE_TWO_LINE_VIEW_CSV)}")
    lines.append(f"candidate_two_line_view_md_raw_url: {raw_url(DAILY_CANDIDATE_TWO_LINE_VIEW_MD)}")
    lines.append(f"status: {'generated' if DAILY_THEME_LEADERSHIP_CSV.exists() and DAILY_CANDIDATE_TWO_LINE_VIEW_CSV.exists() else 'missing'}")
    lines.append("fields: theme_final_status,candidate_source_type,candidate_line,candidate_line_group,two_line_overlap_flag,theme_leadership_note")
    lines.append("note: Keep 主流資金線 separate from 個股條件線 / 潛伏觀察線. Do not mix them into one total ranking.")
    lines.append("")
    lines.append("VOLUME BREAKOUT WATCH")
    lines.append(f"volume_breakout_watch_md_raw_url: {raw_url(VOLUME_BREAKOUT_WATCH_MD)}")
    lines.append(f"volume_breakout_watch_csv_raw_url: {raw_url(VOLUME_BREAKOUT_WATCH_CSV)}")
    lines.append(f"volume_breakout_backtest_md_raw_url: {raw_url(VOLUME_BREAKOUT_BACKTEST_MD)}")
    lines.append(f"volume_breakout_backtest_csv_raw_url: {raw_url(VOLUME_BREAKOUT_BACKTEST_CSV)}")
    lines.append(f"volume_breakout_chatgpt_packet_raw_url: {raw_url(VOLUME_BREAKOUT_PACKET_MD)}")
    lines.append(f"status: {'generated' if VOLUME_BREAKOUT_WATCH_CSV.exists() and VOLUME_BREAKOUT_PACKET_MD.exists() else 'missing'}")
    lines.append("fields: volume_breakout_type,volume_watch_scope,volume_breakout_priority,selection_status,not_selected_reason,risk_flags,next_volume_breakout_confirmation")
    lines.append("note: Strict breakout is not the same as all volume-confirmed attacks. Use this packet when asked about 帶量突破 / 放量突破 / 放量攻擊.")
    lines.append("")
    lines.append("NON-REVENUE MOMENTUM WATCH")
    lines.append(f"non_revenue_momentum_watch_md_raw_url: {raw_url(NON_REVENUE_MOMENTUM_MD)}")
    lines.append(f"non_revenue_momentum_watch_csv_raw_url: {raw_url(NON_REVENUE_MOMENTUM_CSV)}")
    lines.append(f"market_abnormal_status_md_raw_url: {raw_url(MARKET_ABNORMAL_STATUS_MD)}")
    lines.append(f"market_abnormal_status_csv_raw_url: {raw_url(MARKET_ABNORMAL_STATUS_CSV)}")
    lines.append("market_abnormal_usage: disposition/attention/periodic-trading flags are execution-risk overlays; do not treat as core buy/sell signals. Historical backtests must mark disposition filtering as not_backfilled until snapshots accumulate.")
    lines.append(f"msci_taiwan_rebalance_backtest_md_raw_url: {raw_url(MSCI_REBALANCE_BACKTEST_MD)}")
    lines.append(f"msci_taiwan_rebalance_backtest_csv_raw_url: {raw_url(MSCI_REBALANCE_BACKTEST_CSV)}")
    lines.append(f"msci_taiwan_rebalance_events_csv_raw_url: {raw_url(MSCI_REBALANCE_EVENTS_CSV)}")
    lines.append("msci_rebalance_usage: MSCI addition/deletion is an event tag and research layer. Entry-backtest uses the first trading day after effective date open to D+5/D+10/D+15/D+20 close; do not treat it as a standalone buy/sell signal.")
    lines.append(f"status: {'generated' if NON_REVENUE_MOMENTUM_MD.exists() and NON_REVENUE_MOMENTUM_CSV.exists() else 'missing'}")
    lines.append("fields: non_revenue_momentum_type,revenue_confirmation_status,theme_final_status,theme_volume_attack_status,volume_breakout_type,tdcc_status,warrant_flow_signal,next_confirmation")
    lines.append("note: Standalone specialty overlay for stocks where price/theme/fund flow moves before revenue/EPS confirmation. It is not a seventh core category and must not change core weights.")
    lines.append("")
    lines.append("WARRANT MARKET ANALYSIS")
    lines.append(f"market_report_md_raw_url: {raw_url(WARRANT_MARKET_MD)}")
    lines.append(f"market_report_pdf_pages_url: {pages_url(Path('docs/latest/warrant_market_report_latest.pdf'))}")
    lines.append(f"market_report_pdf_raw_url: {raw_url(WARRANT_MARKET_PDF)}")
    lines.append(f"flow_by_stock_csv_raw_url: {raw_url(WARRANT_FLOW_BY_STOCK_CSV)}")
    lines.append(f"sector_heat_csv_raw_url: {raw_url(WARRANT_SECTOR_HEAT_CSV)}")
    lines.append(f"signal_performance_md_raw_url: {raw_url(WARRANT_SIGNAL_PERFORMANCE_MD)}")
    lines.append(f"status: {'generated' if WARRANT_MARKET_MD.exists() and WARRANT_FLOW_BY_STOCK_CSV.exists() else 'missing'}")
    lines.append("note: Warrant flow is an auxiliary signal only, not a standalone buy reason.")
    lines.append("")
    lines.append("MARKET REGIME / FUTURES OPTIONS DASHBOARD")
    lines.append(f"market_regime_csv_raw_url: {raw_url(MARKET_REGIME_CSV)}")
    lines.append(f"market_risk_dashboard_md_raw_url: {raw_url(MARKET_RISK_DASHBOARD_MD)}")
    lines.append(f"market_risk_dashboard_pdf_pages_url: {pages_url(Path('docs/latest/market_risk_dashboard_latest.pdf'))}")
    lines.append(f"market_risk_dashboard_pdf_raw_url: {raw_url(MARKET_RISK_DASHBOARD_PDF)}")
    lines.append(f"futures_options_indicators_raw_url: {raw_url(FUTURES_OPTIONS_INDICATORS_CSV)}")
    lines.append(f"futures_options_source_status_raw_url: {raw_url(FUTURES_OPTIONS_SOURCE_STATUS_MD)}")
    lines.append(f"market_sentiment_context_raw_url: {raw_url(MARKET_SENTIMENT_CONTEXT_CSV)}")
    lines.append(f"market_sentiment_context_md_raw_url: {raw_url(MARKET_SENTIMENT_CONTEXT_MD)}")
    lines.append(f"market_sentiment_context_pages_url: {pages_url(Path('docs/latest/market_sentiment_context_latest.csv'))}")
    lines.append(f"market_sentiment_context_md_pages_url: {pages_url(Path('docs/latest/market_sentiment_context_latest.md'))}")
    lines.append(f"market_sentiment_context_history_raw_url: {raw_url(MARKET_SENTIMENT_CONTEXT_HISTORY_CSV)}")
    lines.append(f"vix_history_raw_url: {raw_url(VIX_HISTORY_CSV)}")
    lines.append(f"retail_mtx_sentiment_history_raw_url: {raw_url(RETAIL_MTX_SENTIMENT_HISTORY_CSV)}")
    lines.append(f"futures_options_indicators_history_raw_url: {raw_url(FUTURES_OPTIONS_INDICATORS_HISTORY_CSV)}")
    lines.append(
        "market_sentiment_context_note: VIX / PutCall / retail MTX must be cross-checked with "
        "TWSE/TPEx position, market_regime, and foreign_tx_futures_net_oi; if sample_status="
        "insufficient_history, report 資料不足 / 僅能觀察."
    )
    lines.append(f"status: {'generated' if MARKET_REGIME_CSV.exists() and MARKET_RISK_DASHBOARD_MD.exists() else 'missing'}")
    lines.append("note: Market regime is background for index futures / exposure review, not a standalone trading instruction.")
    lines.append("")
    lines.append("SURGE PRECONDITION MODEL")
    lines.append(f"surge_model_chatgpt_packet_raw_url: {raw_url(SURGE_MODEL_PACKET_MD)}")
    lines.append(f"surge_precondition_candidates_md_raw_url: {raw_url(SURGE_PRECONDITION_CANDIDATES_MD)}")
    lines.append(f"surge_precondition_candidates_csv_raw_url: {raw_url(SURGE_PRECONDITION_CANDIDATES_CSV)}")
    lines.append(f"surge_model_backtest_md_raw_url: {raw_url(SURGE_MODEL_BACKTEST_MD)}")
    lines.append(f"surge_model_backtest_csv_raw_url: {raw_url(SURGE_MODEL_BACKTEST_CSV)}")
    lines.append(f"surge_model_feature_importance_md_raw_url: {raw_url(SURGE_MODEL_FEATURE_IMPORTANCE_MD)}")
    lines.append(f"surge_model_feature_importance_csv_raw_url: {raw_url(SURGE_MODEL_FEATURE_IMPORTANCE_CSV)}")
    lines.append(f"surge_model_validation_raw_url: {raw_url(SURGE_MODEL_VALIDATION_MD)}")
    lines.append(f"status: {'generated' if SURGE_MODEL_PACKET_MD.exists() and SURGE_PRECONDITION_CANDIDATES_CSV.exists() else 'missing'}")
    lines.append("note: This is an independent pre-surge pattern mining model. It is not the daily recommendation model and must not change core weights until mature samples are sufficient.")
    lines.append("")
    lines.append("PURPOSE")
    lines.append("This packet embeds the daily market report content directly.")
    lines.append("If ChatGPT cannot read GitHub raw/latest/MD/PDF files, paste this packet into the daily report conversation.")
    lines.append("Do not recreate this report from stale older files.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED SUMMARY REPORT")
    lines.append("=" * 80)
    lines.append("")

    if summary_text.strip():
        lines.append(summary_text)
    else:
        lines.append("[daily_market_summary_latest.md missing or empty]")

    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED FULL REPORT")
    lines.append("=" * 80)
    lines.append("")

    if full_text.strip():
        lines.append(full_text)
    else:
        lines.append("[daily_market_full_latest.md missing or empty]")

    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF PACKET")
    lines.append("=" * 80)
    lines.append("")

    return "\n".join(lines)


def write_packet_manifest(main_date: str, report_ready: str, paths: dict[str, Path]) -> None:
    history_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"
    report_manifest = read_json(REPORT_MANIFEST_JSON)
    kline_status = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)
    curated_pdf = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf = fixed_pdf_manifest.get("full_table_pdf", {})

    manifest = {
        "generated_at": now_text(),
        "main_price_date": main_date,
        "report_ready": report_ready,
        "repo_artifacts_are_sources_not_final_chatgpt_deliverables": True,
        "report_ready_is_not_chatgpt_pdf_done": True,
        "fixed_pdf_validation_is_repo_artifact_validation_only": True,
        "daily_full_market_default_chatgpt_deliverables": [
            "每日推薦分析 PDF",
            "完整候選清單補充 PDF",
            "權證市場輔助分析 PDF",
            "市場風險與大盤期權背景 PDF",
        ],
        "summary_pdf_kline_policy": kline_status.get("policy") or report_manifest.get("summary_pdf_kline_policy", "local_price_redraw_first"),
        "summary_pdf_kline_status": kline_status.get("status") or report_manifest.get("summary_pdf_kline_status", ""),
        "summary_pdf_kline_total_charts": kline_status.get("total_charts", report_manifest.get("summary_pdf_kline_total_charts", 0)),
        "summary_pdf_kline_local_price_redraw_count": kline_status.get("local_price_redraw_count", report_manifest.get("summary_pdf_kline_local_price_redraw_count", 0)),
        "summary_pdf_kline_chart_path_fallback_count": kline_status.get("chart_path_fallback_count", report_manifest.get("summary_pdf_kline_chart_path_fallback_count", 0)),
        "summary_pdf_kline_missing_count": kline_status.get("missing_count", report_manifest.get("summary_pdf_kline_missing_count", 0)),
        "summary_pdf_kline_status_md_path": PDF_KLINE_STATUS_MD.as_posix(),
        "daily_market_curated_pdf_pages_url": curated_pdf.get("pages_url") or pages_url(Path("docs/latest/daily_market_curated_report_latest.pdf")),
        "daily_market_curated_pdf_raw_url": curated_pdf.get("raw_url") or raw_url(CURATED_REPORT_PDF),
        "daily_market_curated_pdf_path": curated_pdf.get("file_path") or CURATED_REPORT_PDF.as_posix(),
        "daily_market_full_table_pdf_pages_url": full_table_pdf.get("pages_url") or pages_url(Path("docs/latest/daily_market_full_table_report_latest.pdf")),
        "daily_market_full_table_pdf_raw_url": full_table_pdf.get("raw_url") or raw_url(FULL_TABLE_REPORT_PDF),
        "daily_market_full_table_pdf_path": full_table_pdf.get("file_path") or FULL_TABLE_REPORT_PDF.as_posix(),
        "fixed_pdf_validation_status": fixed_pdf_validation.get("status", ""),
        "fundamental_catalyst_layer_md_raw_url": raw_url(FUNDAMENTAL_CATALYST_MD),
        "fundamental_catalyst_layer_path": FUNDAMENTAL_CATALYST_MD.as_posix(),
        "fundamental_catalyst_layer_status": "generated" if FUNDAMENTAL_CATALYST_MD.exists() else "missing",
        "theme_event_calendar_raw_url": raw_url(THEME_EVENT_CALENDAR),
        "theme_event_watch_csv_raw_url": raw_url(THEME_EVENT_WATCH_CSV),
        "theme_event_watch_md_raw_url": raw_url(THEME_EVENT_WATCH_MD),
        "theme_event_watch_status": "generated" if THEME_EVENT_WATCH_CSV.exists() and THEME_EVENT_WATCH_MD.exists() else "missing",
        "theme_event_watch_pdf_section": "近期事件預警 / 主題催化觀察",
        "company_theme_mapping_raw_url": raw_url(COMPANY_THEME_MAPPING),
        "quarterly_catalyst_raw_url": raw_url(QUARTERLY_CATALYST),
        "event_catalyst_log_raw_url": raw_url(EVENT_CATALYST_LOG),
        "catalyst_summary_raw_url": raw_url(CATALYST_SUMMARY_MD),
        "catalyst_summary_csv_raw_url": raw_url(CATALYST_SUMMARY_CSV),
        "catalyst_performance_raw_url": raw_url(CATALYST_PERFORMANCE_CSV),
        "catalyst_layer_validation_raw_url": raw_url(CATALYST_VALIDATION_MD),
        "catalyst_data_layer_status": "generated" if CATALYST_SUMMARY_MD.exists() and CATALYST_PERFORMANCE_CSV.exists() else "schema_ready_or_pending",
        "company_event_calendar_raw_url": raw_url(COMPANY_EVENT_CALENDAR),
        "macro_event_calendar_raw_url": raw_url(MACRO_EVENT_CALENDAR),
        "upcoming_catalyst_calendar_raw_url": raw_url(UPCOMING_CATALYST_CALENDAR),
        "upcoming_macro_event_calendar_raw_url": raw_url(UPCOMING_MACRO_EVENT_CALENDAR),
        "calendar_data_source_status_raw_url": raw_url(CALENDAR_DATA_SOURCE_STATUS),
        "event_calendar_validation_raw_url": raw_url(EVENT_CALENDAR_VALIDATION),
        "event_calendar_layer_status": "generated" if COMPANY_EVENT_CALENDAR.exists() and MACRO_EVENT_CALENDAR.exists() else "missing",
        "daily_signal_log_path": DAILY_SIGNAL_LOG.as_posix(),
        "daily_signal_performance_csv_path": DAILY_SIGNAL_PERFORMANCE.as_posix(),
        "daily_signal_performance_summary_raw_url": raw_url(DAILY_SIGNAL_SUMMARY_MD),
        "daily_signal_performance_weekly_pdf_pages_url": pages_url(Path("docs/latest/daily_signal_performance_weekly_latest.pdf")),
        "daily_signal_performance_monthly_pdf_pages_url": pages_url(Path("docs/latest/daily_signal_performance_monthly_latest.pdf")),
        "daily_signal_performance_status": "generated" if DAILY_SIGNAL_LOG.exists() and DAILY_SIGNAL_PERFORMANCE.exists() else "missing",
        "daily_candidate_signal_log_path": DAILY_CANDIDATE_SIGNAL_LOG.as_posix(),
        "daily_candidate_signal_log_raw_url": raw_url(DAILY_CANDIDATE_SIGNAL_LOG),
        "candidate_repeat_appearance_path": CANDIDATE_REPEAT_CSV.as_posix(),
        "candidate_repeat_appearance_raw_url": raw_url(CANDIDATE_REPEAT_CSV),
        "candidate_repeat_appearance_md_raw_url": raw_url(CANDIDATE_REPEAT_MD),
        "candidate_repeat_appearance_status": "generated" if CANDIDATE_REPEAT_CSV.exists() and CANDIDATE_REPEAT_MD.exists() else "missing",
        "daily_candidate_decision_csv_raw_url": raw_url(DAILY_CANDIDATE_DECISION_CSV),
        "daily_candidate_decision_md_raw_url": raw_url(DAILY_CANDIDATE_DECISION_MD),
        "daily_candidate_decision_chatgpt_packet_raw_url": raw_url(DAILY_CANDIDATE_DECISION_PACKET_MD),
        "daily_candidate_decision_status": "generated" if DAILY_CANDIDATE_DECISION_CSV.exists() and DAILY_CANDIDATE_DECISION_PACKET_MD.exists() else "missing",
        "daily_theme_leadership_csv_raw_url": raw_url(DAILY_THEME_LEADERSHIP_CSV),
        "daily_theme_leadership_md_raw_url": raw_url(DAILY_THEME_LEADERSHIP_MD),
        "daily_candidate_two_line_view_csv_raw_url": raw_url(DAILY_CANDIDATE_TWO_LINE_VIEW_CSV),
        "daily_candidate_two_line_view_md_raw_url": raw_url(DAILY_CANDIDATE_TWO_LINE_VIEW_MD),
        "daily_theme_leadership_status": "generated" if DAILY_THEME_LEADERSHIP_CSV.exists() and DAILY_CANDIDATE_TWO_LINE_VIEW_CSV.exists() else "missing",
        "chatgpt_indicator_usage_guide_md_raw_url": raw_url(INDICATOR_USAGE_GUIDE_MD),
        "chatgpt_indicator_usage_guide_txt_raw_url": raw_url(INDICATOR_USAGE_GUIDE_TXT),
        "chatgpt_indicator_usage_guide_status": "generated" if INDICATOR_USAGE_GUIDE_MD.exists() and INDICATOR_USAGE_GUIDE_TXT.exists() else "missing",
        "daily_short_term_specialty_packet_raw_url": raw_url(SHORT_TERM_SPECIALTY_PACKET_MD),
        "daily_short_term_specialty_packet_status": "generated" if SHORT_TERM_SPECIALTY_PACKET_MD.exists() else "missing",
        "non_revenue_momentum_watch_md_raw_url": raw_url(NON_REVENUE_MOMENTUM_MD),
        "non_revenue_momentum_watch_csv_raw_url": raw_url(NON_REVENUE_MOMENTUM_CSV),
        "non_revenue_momentum_watch_status": "generated" if NON_REVENUE_MOMENTUM_MD.exists() and NON_REVENUE_MOMENTUM_CSV.exists() else "missing",
        "msci_taiwan_rebalance_events_csv_raw_url": raw_url(MSCI_REBALANCE_EVENTS_CSV),
        "msci_taiwan_rebalance_backtest_md_raw_url": raw_url(MSCI_REBALANCE_BACKTEST_MD),
        "msci_taiwan_rebalance_backtest_csv_raw_url": raw_url(MSCI_REBALANCE_BACKTEST_CSV),
        "msci_taiwan_rebalance_status": "generated" if MSCI_REBALANCE_BACKTEST_MD.exists() and MSCI_REBALANCE_BACKTEST_CSV.exists() else "missing",
        "surge_model_chatgpt_packet_raw_url": raw_url(SURGE_MODEL_PACKET_MD),
        "surge_precondition_candidates_md_raw_url": raw_url(SURGE_PRECONDITION_CANDIDATES_MD),
        "surge_precondition_candidates_csv_raw_url": raw_url(SURGE_PRECONDITION_CANDIDATES_CSV),
        "surge_model_backtest_md_raw_url": raw_url(SURGE_MODEL_BACKTEST_MD),
        "surge_model_backtest_csv_raw_url": raw_url(SURGE_MODEL_BACKTEST_CSV),
        "surge_model_feature_importance_md_raw_url": raw_url(SURGE_MODEL_FEATURE_IMPORTANCE_MD),
        "surge_model_feature_importance_csv_raw_url": raw_url(SURGE_MODEL_FEATURE_IMPORTANCE_CSV),
        "surge_model_validation_raw_url": raw_url(SURGE_MODEL_VALIDATION_MD),
        "surge_model_status": "generated" if SURGE_MODEL_PACKET_MD.exists() and SURGE_PRECONDITION_CANDIDATES_CSV.exists() else "missing",
        "latest_packet_path": PACKET_LATEST.as_posix(),
        "latest_packet_raw_url_main": raw_url(PACKET_LATEST, ref="main"),
        "legacy_latest_packet_path": PACKET_LATEST_OLD.as_posix(),
        "history_packet_path": history_packet.as_posix(),
        "history_packet_raw_url_main": raw_url(history_packet, ref="main"),
        "dated_summary_md_path": paths["dated_summary_md"].as_posix(),
        "dated_full_md_path": paths["dated_full_md"].as_posix(),
        "dated_summary_pdf_path": paths["dated_summary_pdf"].as_posix(),
        "dated_full_pdf_path": paths["dated_full_pdf"].as_posix(),
    }

    PACKET_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    meta = extract_main_meta()
    main_date = meta["main_price_date"]
    report_ready = str(meta["report_ready"])

    paths = ensure_dated_artifacts(main_date)

    packet_text = build_packet_text(
        main_date=main_date,
        report_ready=report_ready,
        paths=paths,
        meta=meta,
    )
    packet_text = sanitize_display_text(packet_text)

    history_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    PACKET_LATEST.write_text(packet_text, encoding="utf-8")
    PACKET_LATEST_OLD.write_text(packet_text, encoding="utf-8")
    history_packet.write_text(packet_text, encoding="utf-8")
    DOCS_PACKET_LATEST.parent.mkdir(parents=True, exist_ok=True)
    DOCS_PACKET_LATEST.write_text(packet_text, encoding="utf-8")

    write_packet_manifest(main_date, report_ready, paths)

    print(f"Saved: {PACKET_LATEST}")
    print(f"Saved: {PACKET_LATEST_OLD}")
    print(f"Saved: {history_packet}")
    print(f"Saved: {DOCS_PACKET_LATEST}")
    print(f"Saved: {PACKET_MANIFEST}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
