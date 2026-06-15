from __future__ import annotations

import math
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_tdcc_chatgpt_tracking_outputs import prepare_latest_frame, risk_bucket  # noqa: E402
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    load_price_history,
    markdown_table,
    pages_url,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


DAILY_MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
STOCK_THEME_TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"

WEEKLY_INCREASE_CSV = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.csv"
WEEKLY_INCREASE_MD = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.md"
CONSECUTIVE_CSV = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.csv"
CONSECUTIVE_MD = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.md"
MODEL_CROSS_CSV = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.csv"
MODEL_CROSS_MD = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.md"
HIGHLIGHT_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_highlight_for_report_latest.csv"
HIGHLIGHT_FOR_REPORT_MD = LATEST_DIR / "tdcc_weekly_candidate_highlight_for_report_latest.md"
FULL_FOR_REPORT_CSV = LATEST_DIR / "tdcc_weekly_candidate_full_for_report_latest.csv"
FULL_FOR_REPORT_MD = LATEST_DIR / "tdcc_weekly_candidate_full_for_report_latest.md"
HIGHLIGHT_MD = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.md"
FULL_MD = LATEST_DIR / "tdcc_weekly_candidate_full_latest.md"
HIGHLIGHT_PDF = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.pdf"
FULL_PDF = LATEST_DIR / "tdcc_weekly_candidate_full_latest.pdf"
SECTION_MANIFEST_CSV = LATEST_DIR / "tdcc_weekly_report_section_manifest_latest.csv"
TRACKING_PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"

TDCC_FULL_REPORT_ALLOWED_MODEL_CROSS_IDS = {"tdcc_short_term_continuation_d5_d10"}
TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT = 10
TDCC_FULL_REPORT_SECTION_LIMIT = 50
TDCC_EFFECTIVE_INCREASE_THRESHOLD = 0.5
TDCC_LOW_VOLUME_MA20_LOTS_THRESHOLD = 1000.0
TDCC_LOW_VOLUME_PENALTY = 10.0
TDCC_HIGH_PAIR_STREAK_BONUS_STEP = 5.0
TDCC_HIGH_PAIR_STREAK_BONUS_CAP = 20.0
TDCC_STOCK_HISTORY_DIR = Path("data/tdcc_stock_history")
PRICE_HISTORY_CACHE: dict[str, pd.DataFrame] = {}
TDCC_STOCK_HISTORY_CACHE: dict[str, pd.DataFrame] = {}

SECTION_MANIFEST_COLUMNS = [
    "section_order",
    "section_id",
    "section_title_zh",
    "table_contract",
    "include_in_highlight",
    "highlight_limit",
    "include_in_full",
    "full_limit",
    "required",
    "enabled",
    "notes_zh",
]

DEFAULT_SECTION_MANIFEST_ROWS = [
    {
        "section_order": 1,
        "section_id": "weekly_increase",
        "section_title_zh": "當週增幅排名",
        "table_contract": "tdcc_ranking",
        "include_in_highlight": True,
        "highlight_limit": TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT,
        "include_in_full": True,
        "full_limit": TDCC_FULL_REPORT_SECTION_LIMIT,
        "required": True,
        "enabled": True,
        "notes_zh": "核心 section；本週正增幅排名。",
    },
    {
        "section_order": 2,
        "section_id": "consecutive_accumulation",
        "section_title_zh": "連續累積排名",
        "table_contract": "tdcc_ranking",
        "include_in_highlight": True,
        "highlight_limit": TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT,
        "include_in_full": True,
        "full_limit": TDCC_FULL_REPORT_SECTION_LIMIT,
        "required": True,
        "enabled": True,
        "notes_zh": "核心 section；800/1000 張大戶有效連續增加。",
    },
    {
        "section_order": 3,
        "section_id": "model_cross_weekly_increase_tdcc_short_term_continuation_d5_d10",
        "section_title_zh": "當週增幅榜 × TDCC短線延續模型 D+5/D+10",
        "table_contract": "model_cross",
        "include_in_highlight": True,
        "highlight_limit": TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT,
        "include_in_full": True,
        "full_limit": TDCC_FULL_REPORT_SECTION_LIMIT,
        "required": True,
        "enabled": True,
        "notes_zh": "核心 section；當週增幅名單與 TDCC 短線延續模型交集。",
    },
    {
        "section_order": 4,
        "section_id": "model_cross_consecutive_accumulation_tdcc_short_term_continuation_d5_d10",
        "section_title_zh": "連續累積榜 × TDCC短線延續模型 D+5/D+10",
        "table_contract": "model_cross",
        "include_in_highlight": True,
        "highlight_limit": TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT,
        "include_in_full": True,
        "full_limit": TDCC_FULL_REPORT_SECTION_LIMIT,
        "required": True,
        "enabled": True,
        "notes_zh": "核心 section；連續累積名單與 TDCC 短線延續模型交集。",
    },
]

README_PATHS = [
    LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
    DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
]

DOCS_SYNC_PATHS = [
    WEEKLY_INCREASE_CSV,
    WEEKLY_INCREASE_MD,
    CONSECUTIVE_CSV,
    CONSECUTIVE_MD,
    MODEL_CROSS_CSV,
    MODEL_CROSS_MD,
    HIGHLIGHT_FOR_REPORT_CSV,
    HIGHLIGHT_FOR_REPORT_MD,
    FULL_FOR_REPORT_CSV,
    FULL_FOR_REPORT_MD,
    HIGHLIGHT_MD,
    FULL_MD,
    HIGHLIGHT_PDF,
    FULL_PDF,
    SECTION_MANIFEST_CSV,
]

DELTA_COLS = [
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
]
DELTA_WEIGHTS = {
    "tdcc_1w_change_400": 1,
    "tdcc_1w_change_600": 2,
    "tdcc_1w_change_800": 3,
    "tdcc_1w_change_1000": 4,
}

BASE_COLUMNS = [
    "rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "theme",
    "theme_mainstream_status",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
    "tdcc_four_threshold_weekly_increase_sum",
    "tdcc_weighted_weekly_increase_score",
    "tdcc_effective_increase_count",
    "tdcc_sync_bonus",
    "tdcc_theme_bonus",
    "volume_ma20_lots",
    "tdcc_low_volume_penalty",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_high_pair_streak_bonus",
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "tdcc_phase_group_zh",
    "risk_bucket",
    "risk_bucket_zh",
    "price_return_20d",
    "distance_ma20_pct",
    "relative_return_vs_benchmark",
    "ranking_note_zh",
]

MODEL_CROSS_COLUMNS = [
    "tdcc_list_type",
    "tdcc_rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "theme",
    "tdcc_phase_group_zh",
    "risk_bucket",
    "risk_bucket_zh",
    "tdcc_score",
    "model_id",
    "model_name_zh",
    "display_rank",
    "tdcc_model_rank_in_list",
    "model_score",
    "model_source",
    "source_hit_labels_zh",
    "why_selected_zh",
    "risk_tags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "report_usage_zh",
    "operation_note_zh",
]

REPORT_COLUMNS = [
    "report_kind",
    "section_id",
    "section_name_zh",
    "section_rank",
    "tdcc_list_type",
    "tdcc_rank",
    "signal_date",
    "stock_id",
    "stock_name",
    "theme",
    "tdcc_phase_group_zh",
    "risk_bucket",
    "risk_bucket_zh",
    "tdcc_score",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
    "tdcc_weighted_weekly_increase_score",
    "tdcc_effective_increase_count",
    "tdcc_sync_bonus",
    "tdcc_theme_bonus",
    "volume_ma20_lots",
    "tdcc_low_volume_penalty",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_high_pair_streak_bonus",
    "tdcc_consecutive_up_weeks",
    "model_id",
    "model_name_zh",
    "model_rank",
    "tdcc_model_rank_in_list",
    "model_score",
    "model_source",
    "source_hit_labels_zh",
    "why_selected_zh",
    "risk_tags_zh",
    "next_confirmation_zh",
    "recommended_usage_zh",
    "report_usage_zh",
    "operation_note_zh",
]

PDF_RANKING_COLUMNS = [
    "section_rank",
    "stock_id",
    "stock_name",
    "tdcc_phase_group_zh",
    "risk_bucket",
    "tdcc_score",
    "why_selected_zh",
    "next_confirmation_zh",
    "operation_note_zh",
]

PDF_MODEL_CROSS_COLUMNS = [
    "section_rank",
    "stock_id",
    "stock_name",
    "tdcc_phase_group_zh",
    "risk_bucket",
    "tdcc_score",
    "model_name_zh",
    "tdcc_model_rank_in_list",
    "model_score",
    "why_selected_zh",
    "next_confirmation_zh",
    "operation_note_zh",
]

PDF_HEADER_ZH = {
    "rank": "排名",
    "signal_date": "資料日",
    "report_kind": "報告版本",
    "section_id": "區塊ID",
    "section_name_zh": "區塊",
    "section_rank": "序",
    "tdcc_list_type": "TDCC名單類型",
    "tdcc_rank": "TDCC排名",
    "stock_id": "代號",
    "stock_name": "股票",
    "theme": "族群",
    "theme_mainstream_status": "族群主流狀態",
    "tdcc_phase_group_zh": "TDCC階段",
    "risk_bucket": "風險類型",
    "risk_bucket_zh": "風險",
    "tdcc_score": "TDCC分數",
    "tdcc_weekly_increase_score": "當週增幅分數",
    "tdcc_consecutive_accumulation_score": "連續累積分數",
    "tdcc_1w_change_400": ">400張週變化",
    "tdcc_1w_change_600": ">600張週變化",
    "tdcc_1w_change_800": ">800張週變化",
    "tdcc_1w_change_1000": ">1000張週變化",
    "tdcc_four_threshold_weekly_increase_sum": "四級距週變化合計",
    "tdcc_weighted_weekly_increase_score": "加權週增基礎分",
    "tdcc_effective_increase_count": "有效增加級距數",
    "tdcc_sync_bonus": "同步增加加分",
    "tdcc_theme_bonus": "主流題材加分",
    "volume_ma20_lots": "20日均量(張)",
    "tdcc_low_volume_penalty": "低量扣分",
    "tdcc_high_pair_effective_streak_weeks": "800/1000有效連續週數",
    "tdcc_high_pair_streak_bonus": "高級距連續加分",
    "tdcc_consecutive_up_weeks": "連續增加週數",
    "all_thresholds_up": "四級距同步增加",
    "high_thresholds_up": "高級距同步增加",
    "tdcc_price_phase": "TDCC股價階段",
    "price_return_20d": "20日漲跌幅",
    "distance_ma20_pct": "距MA20",
    "relative_return_vs_benchmark": "相對大盤報酬",
    "ranking_note_zh": "排名說明",
    "model_id": "每日模型ID",
    "model_name_zh": "每日模型",
    "model_rank": "模型排名",
    "display_rank": "顯示排名",
    "tdcc_model_rank_in_list": "模型內排名",
    "model_score": "模型分數",
    "model_source": "模型來源",
    "source_hit_labels_zh": "同時命中來源",
    "why_selected_zh": "入選原因",
    "risk_tags_zh": "風險標籤",
    "next_confirmation_zh": "下一確認",
    "recommended_usage_zh": "建議用途",
    "report_usage_zh": "報告用途",
    "operation_note_zh": "操作提醒",
}

RANK_COLUMNS = {"section_rank", "tdcc_rank", "tdcc_model_rank_in_list"}
SCORE_COLUMNS = {"tdcc_score", "model_score"}
SNAKE_CASE_RE = re.compile(r"\b[a-z]+(?:_[a-z0-9]+)+\b")


TOKEN_ZH = {
    "tdcc_short_term_continuation_d5_d10": "TDCC 短線延續模型 D+5/D+10",
    "tdcc_short_term_edge": "TDCC 短線延續模型 D+5/D+10",
    "range_rebound": "區間轉強",
    "revenue_pullback": "營收成長股價回檔",
    "revenue_breakout_low_response": "營收爆發股價尚未反應",
    "pullback_rebound": "回檔後短線轉強",
    "short_term_specialty": "短線專項",
    "volume_range_breakout": "放量攻擊",
    "bottom_volume_attack": "放量攻擊",
    "volume_breakout": "放量攻擊",
    "w_bottom_right_side": "W底右側",
    "theme_pullback": "熱門族群回檔",
    "hot_theme_pullback": "熱門族群回檔",
    "platform_turning_up": "平台整理轉強",
    "tdcc_pre_move_accumulation": "TDCC 潛伏吸籌",
    "tdcc_leading_price": "TDCC 領先股價 / 潛伏吸籌",
    "tdcc_price_confirmed": "TDCC 與股價初步確認",
    "price_leading_tdcc": "股價領先 TDCC / 追高風險",
    "overheated_after_tdcc": "TDCC 後股價過熱",
    "tdcc_price_divergence": "TDCC 與股價背離",
    "failed_after_tdcc": "TDCC 訊號後失效",
    "insufficient_price_context": "價格資料不足",
    "insufficient_tdcc_history": "TDCC 歷史不足",
    "neutral_or_unclear": "中性 / 不明",
    "strong_but_pre_move": "籌碼強但尚未發動",
    "strong_confirmed": "籌碼與股價確認",
    "strong_but_late": "股價已領先",
    "strong_but_overheated": "短線過熱",
    "strong_but_divergent": "籌碼與股價背離",
    "insufficient_data": "資料不足",
    "mainstream": "主流",
    "non_mainstream": "非主流",
    "single_stock_signal": "單一個股訊號",
    "mainstream_leader": "主流領先族群",
    "mainstream_follow_through": "主流續強族群",
    "emerging_theme": "早期題材",
    "weak_theme": "弱勢族群",
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購偏多",
    "call_put_bullish": "權證偏多",
    "no_signal": "無明確權證訊號",
    "mixed_flow": "權證多空混合",
    "mild_accumulation": "大戶溫和增加",
    "strong_accumulation": "大戶強累積",
    "distribution_warning": "大戶轉弱警示",
    "neckline": "頸線",
    "breakout": "突破",
    "hot theme tag": "熱門族群標籤",
}

THEME_FALLBACK_ZH = {
    "other electronics": "其他電子",
    "semiconductor": "半導體",
    "semiconductor equipment/materials": "半導體設備 / 材料",
    "power discrete/diodes": "功率元件 / 二極體",
    "networking": "網通",
    "memory": "記憶體",
    "biotechnology": "生技醫療",
    "connector/cable": "連接器 / 線纜",
    "electronic components": "電子零組件",
    "communications": "通訊網路",
    "computer peripherals": "電腦及週邊設備",
    "optoelectronics": "光電",
}

RISK_BUCKET_ZH = {
    "strong_but_pre_move": "籌碼強但尚未發動",
    "strong_confirmed": "籌碼與股價確認",
    "strong_but_late": "股價已領先",
    "strong_but_overheated": "短線過熱",
    "strong_but_divergent": "籌碼與股價背離",
    "insufficient_data": "資料不足",
}

PHASE_ZH = {
    "tdcc_leading_price": "TDCC 領先股價 / 潛伏吸籌",
    "tdcc_price_confirmed": "TDCC 與股價初步確認",
    "price_leading_tdcc": "股價領先 TDCC / 追高風險",
    "overheated_after_tdcc": "TDCC 後股價過熱",
    "tdcc_price_divergence": "TDCC 與股價背離",
    "failed_after_tdcc": "TDCC 訊號後失效",
    "insufficient_price_context": "價格資料不足",
    "insufficient_tdcc_history": "TDCC 歷史不足",
    "neutral_or_unclear": "中性 / 不明",
}


def zh(value: Any) -> str:
    value = scalar_value(value)
    text = safe_str(value).strip()
    if not text:
        return ""
    for raw, label in sorted(TOKEN_ZH.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(raw, label)
    return text


def scalar_value(value: Any) -> Any:
    if isinstance(value, pd.Series):
        for item in value.tolist():
            if safe_str(item).strip():
                return item
        return ""
    return value


def clean_pdf_text(value: Any) -> str:
    value = scalar_value(value)
    text = zh(value).strip()
    if not text:
        return ""

    def replace_unknown(match: re.Match[str]) -> str:
        token = match.group(0)
        return TOKEN_ZH.get(token, "資料不足 / 暫用現有資料")

    return SNAKE_CASE_RE.sub(replace_unknown, text)


def format_rank_value(value: Any) -> str:
    value = scalar_value(value)
    raw = safe_str(value).strip()
    if not raw:
        return ""
    number = to_number(value)
    if number is None or (isinstance(number, float) and math.isnan(number)):
        return clean_pdf_text(raw)
    if float(number).is_integer():
        return str(int(number))
    return f"{number:.2f}".rstrip("0").rstrip(".")


def format_score_value(value: Any) -> str:
    value = scalar_value(value)
    raw = safe_str(value).strip()
    if not raw:
        return ""
    number = to_number(value)
    if number is None or (isinstance(number, float) and math.isnan(number)):
        return clean_pdf_text(raw)
    return f"{number:.2f}".rstrip("0").rstrip(".")


def is_model_cross_section_id(value: Any) -> bool:
    return "model_cross" in safe_str(value)


def pdf_columns_for_section(group: pd.DataFrame) -> list[str]:
    if group.empty:
        return PDF_RANKING_COLUMNS
    section_ids = group.get("section_id", pd.Series(dtype=str)).map(safe_str)
    if section_ids.map(is_model_cross_section_id).any():
        return PDF_MODEL_CROSS_COLUMNS
    return PDF_RANKING_COLUMNS


def pdf_display_cell(row: pd.Series, column: str) -> str:
    if column in RANK_COLUMNS:
        return format_rank_value(row.get(column))
    if column in SCORE_COLUMNS:
        return format_score_value(row.get(column))
    if column == "risk_bucket":
        return clean_pdf_text(row.get("risk_bucket_zh")) or clean_pdf_text(row.get("risk_bucket"))
    return clean_pdf_text(row.get(column))


def pdf_headers_for_columns(columns: list[str]) -> list[str]:
    seen: dict[str, int] = {}
    headers: list[str] = []
    for column in columns:
        base = PDF_HEADER_ZH.get(column, clean_pdf_text(column) or column)
        count = seen.get(base, 0) + 1
        seen[base] = count
        headers.append(base if count == 1 else f"{base}({count})")
    return headers


def pdf_display_table(df: pd.DataFrame, columns: list[str], limit: int | None = None) -> pd.DataFrame:
    """Return a human-facing table with translated headers and display-safe cells."""
    if limit is not None:
        df = df.head(limit)
    headers = pdf_headers_for_columns(columns)
    rows: list[dict[str, str]] = []
    for _, row in df.iterrows():
        display_row: dict[str, str] = {}
        for column, header in zip(columns, headers):
            display_row[header] = pdf_display_cell(row, column)
        rows.append(display_row)
    return pd.DataFrame(rows, columns=headers)


def theme_display_from_raw(value: Any) -> str:
    text = safe_str(value).strip()
    if not text:
        return "未分類"
    text = (
        text.replace("_待細分", "")
        .replace("業_待細分", "")
        .replace("_", " / ")
        .strip(" /")
    )
    lower = text.lower()
    if lower in THEME_FALLBACK_ZH:
        return THEME_FALLBACK_ZH[lower]
    for raw, label in sorted(THEME_FALLBACK_ZH.items(), key=lambda item: len(item[0]), reverse=True):
        lower = lower.replace(raw, label)
    if lower != text.lower():
        return lower
    return zh(text) or text


def load_theme_display_map() -> dict[str, str]:
    if not STOCK_THEME_TAXONOMY.exists():
        return {}
    try:
        df = pd.read_csv(STOCK_THEME_TAXONOMY, dtype=str).fillna("")
    except Exception:
        return {}
    out: dict[str, str] = {}
    for _, row in df.iterrows():
        stock_id = safe_str(row.get("stock_id")).strip()
        if not stock_id:
            continue
        display = (
            safe_str(row.get("hot_primary_theme")).strip()
            or safe_str(row.get("primary_theme")).strip()
            or safe_str(row.get("basic_theme")).strip()
            or safe_str(row.get("industry")).strip()
        )
        out[stock_id] = theme_display_from_raw(display)
    return out


def apply_theme_display(df: pd.DataFrame, theme_map: dict[str, str]) -> pd.DataFrame:
    out = df.copy()
    if "theme" not in out.columns:
        out["theme"] = ""
    if "stock_id" not in out.columns:
        out["stock_id"] = ""
    out["theme"] = out.apply(
        lambda row: theme_map.get(safe_str(row.get("stock_id")).strip())
        or theme_display_from_raw(row.get("theme")),
        axis=1,
    )
    return out


def pct(value: Any, digits: int = 2) -> str:
    n = to_number(value)
    if pd.isna(n):
        return ""
    return f"{n:.{digits}f}"


def boolish(value: Any) -> bool:
    return safe_str(value).strip().lower() in {"1", "true", "yes", "y", "是"}


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def manifest_bool(value: Any, default: bool) -> bool:
    text = safe_str(value).strip().lower()
    if not text:
        return default
    return text in {"1", "true", "yes", "y", "on", "是", "啟用"}


def manifest_limit(value: Any, default: int) -> int:
    number = to_number(value)
    if math.isnan(number) or number <= 0:
        return default
    return int(number)


def manifest_table_contract(section_id: Any, value: Any = "") -> str:
    text = safe_str(value).strip()
    if text:
        return text
    return "model_cross" if safe_str(section_id).startswith("model_cross_") else "tdcc_ranking"


def fallback_section_manifest(source_df: pd.DataFrame) -> pd.DataFrame:
    default_by_id = {safe_str(row["section_id"]): row for row in DEFAULT_SECTION_MANIFEST_ROWS}
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    if source_df.empty or "section_id" not in source_df.columns:
        return pd.DataFrame(DEFAULT_SECTION_MANIFEST_ROWS, columns=SECTION_MANIFEST_COLUMNS)
    for _, source_row in source_df.iterrows():
        section_id = safe_str(source_row.get("section_id"))
        if not section_id or section_id in seen:
            continue
        seen.add(section_id)
        default = default_by_id.get(section_id, {})
        rows.append(
            {
                "section_order": len(rows) + 1,
                "section_id": section_id,
                "section_title_zh": safe_str(default.get("section_title_zh"))
                or safe_str(source_row.get("section_name_zh"))
                or section_id,
                "table_contract": safe_str(default.get("table_contract")) or manifest_table_contract(section_id),
                "include_in_highlight": default.get("include_in_highlight", True),
                "highlight_limit": default.get("highlight_limit", TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT),
                "include_in_full": default.get("include_in_full", True),
                "full_limit": default.get("full_limit", TDCC_FULL_REPORT_SECTION_LIMIT),
                "required": default.get("required", True),
                "enabled": default.get("enabled", True),
                "notes_zh": safe_str(default.get("notes_zh")),
            }
        )
    if not rows:
        rows = DEFAULT_SECTION_MANIFEST_ROWS
    return pd.DataFrame(rows, columns=SECTION_MANIFEST_COLUMNS)


def normalize_section_manifest(manifest: pd.DataFrame, source_df: pd.DataFrame) -> pd.DataFrame:
    if manifest.empty:
        manifest = fallback_section_manifest(source_df)
    manifest = ensure_columns(manifest, SECTION_MANIFEST_COLUMNS)
    source_title_by_id: dict[str, str] = {}
    if not source_df.empty and {"section_id", "section_name_zh"}.issubset(source_df.columns):
        for _, source_row in source_df.iterrows():
            section_id = safe_str(source_row.get("section_id"))
            if section_id and section_id not in source_title_by_id:
                source_title_by_id[section_id] = safe_str(source_row.get("section_name_zh"))

    rows: list[dict[str, Any]] = []
    for idx, row in manifest.iterrows():
        section_id = safe_str(row.get("section_id"))
        if not section_id:
            continue
        order = manifest_limit(row.get("section_order"), idx + 1)
        rows.append(
            {
                "section_order": order,
                "section_id": section_id,
                "section_title_zh": safe_str(row.get("section_title_zh"))
                or source_title_by_id.get(section_id, "")
                or section_id,
                "table_contract": manifest_table_contract(section_id, row.get("table_contract")),
                "include_in_highlight": manifest_bool(row.get("include_in_highlight"), True),
                "highlight_limit": manifest_limit(row.get("highlight_limit"), TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT),
                "include_in_full": manifest_bool(row.get("include_in_full"), True),
                "full_limit": manifest_limit(row.get("full_limit"), TDCC_FULL_REPORT_SECTION_LIMIT),
                "required": manifest_bool(row.get("required"), True),
                "enabled": manifest_bool(row.get("enabled"), True),
                "notes_zh": safe_str(row.get("notes_zh")),
            }
        )
    out = pd.DataFrame(rows, columns=SECTION_MANIFEST_COLUMNS)
    if out.empty:
        out = fallback_section_manifest(source_df)
    return out.sort_values(
        by=["section_order", "section_id"],
        key=lambda series: pd.to_numeric(series, errors="coerce").fillna(999999)
        if series.name == "section_order"
        else series,
    ).reset_index(drop=True)


def load_section_manifest(source_df: pd.DataFrame) -> pd.DataFrame:
    manifest = read_csv(SECTION_MANIFEST_CSV, dtype=str)
    manifest = normalize_section_manifest(manifest, source_df)
    write_csv(manifest, SECTION_MANIFEST_CSV)
    return manifest


def sections_for_report(manifest: pd.DataFrame, report_kind: str) -> pd.DataFrame:
    include_col = "include_in_highlight" if report_kind == "highlight" else "include_in_full"
    if include_col not in manifest.columns:
        return pd.DataFrame(columns=SECTION_MANIFEST_COLUMNS)
    out = manifest[
        manifest["enabled"].map(lambda value: manifest_bool(value, True))
        & manifest[include_col].map(lambda value: manifest_bool(value, True))
    ].copy()
    return out.sort_values(
        by=["section_order", "section_id"],
        key=lambda series: pd.to_numeric(series, errors="coerce").fillna(999999)
        if series.name == "section_order"
        else series,
    )


def section_limit(row: pd.Series, report_kind: str) -> int:
    return manifest_limit(
        row.get("highlight_limit" if report_kind == "highlight" else "full_limit"),
        TDCC_HIGHLIGHT_REPORT_SECTION_LIMIT if report_kind == "highlight" else TDCC_FULL_REPORT_SECTION_LIMIT,
    )


def pdf_columns_for_contract(table_contract: Any, fallback_group: pd.DataFrame | None = None) -> list[str]:
    contract = safe_str(table_contract)
    if contract == "model_cross":
        return PDF_MODEL_CROSS_COLUMNS
    if contract == "tdcc_ranking":
        return PDF_RANKING_COLUMNS
    return pdf_columns_for_section(fallback_group if fallback_group is not None else pd.DataFrame())


def sync_bonus(effective_count: Any) -> float:
    try:
        count = int(effective_count)
    except Exception:
        return 0.0
    return {4: 15.0, 3: 10.0, 2: 5.0}.get(count, 0.0)


def is_mainstream_theme(value: Any) -> bool:
    return safe_str(value).startswith("mainstream")


def normalize_volume_ma20_lots(value: Any) -> float:
    volume = to_number(value)
    if math.isnan(volume):
        return math.nan
    return volume / 1000.0 if volume >= 100000 else volume


def cached_price_history(stock_id: Any) -> pd.DataFrame:
    code = safe_str(stock_id)
    if not code:
        return pd.DataFrame()
    if code not in PRICE_HISTORY_CACHE:
        PRICE_HISTORY_CACHE[code] = load_price_history(code)
    return PRICE_HISTORY_CACHE[code]


def latest_volume_ma20_lots(row: pd.Series) -> float:
    stock_id = safe_str(row.get("stock_id")) or safe_str(row.get("code"))
    signal_date = safe_str(row.get("signal_date")) or safe_str(row.get("signal_trade_date"))
    price = cached_price_history(stock_id)
    if price.empty or "volume_ma20" not in price.columns:
        return math.nan
    part = price
    if signal_date and "date" in price.columns:
        part = price[price["date"].astype(str) <= signal_date]
    if part.empty:
        return math.nan
    return normalize_volume_ma20_lots(part.iloc[-1].get("volume_ma20"))


def cached_tdcc_stock_history(stock_id: Any) -> pd.DataFrame:
    code = safe_str(stock_id)
    if not code:
        return pd.DataFrame()
    if code not in TDCC_STOCK_HISTORY_CACHE:
        path = TDCC_STOCK_HISTORY_DIR / f"{code}.csv"
        history = read_csv(path, dtype=str)
        if not history.empty and "as_of_date" in history.columns:
            history = history.copy()
            history["as_of_date"] = history["as_of_date"].map(safe_str)
        TDCC_STOCK_HISTORY_CACHE[code] = history
    return TDCC_STOCK_HISTORY_CACHE[code]


def high_pair_effective_streak_weeks(row: pd.Series) -> int:
    stock_id = safe_str(row.get("stock_id")) or safe_str(row.get("code"))
    signal_date = safe_str(row.get("signal_date")) or safe_str(row.get("signal_trade_date"))
    history = cached_tdcc_stock_history(stock_id)
    if history.empty or "as_of_date" not in history.columns:
        return 0
    part = history
    if signal_date:
        part = history[history["as_of_date"].astype(str) <= signal_date]
    if part.empty:
        return 0
    part = part.sort_values("as_of_date")
    streak = 0
    for _, hist_row in part.iloc[::-1].iterrows():
        change_800 = to_number(hist_row.get("over_800_change_1w"))
        change_1000 = to_number(hist_row.get("over_1000_change_1w"))
        if (
            not math.isnan(change_800)
            and not math.isnan(change_1000)
            and change_800 > TDCC_EFFECTIVE_INCREASE_THRESHOLD
            and change_1000 > TDCC_EFFECTIVE_INCREASE_THRESHOLD
        ):
            streak += 1
            continue
        break
    return streak


def high_pair_streak_bonus(streak: Any) -> float:
    weeks = to_number(streak)
    if math.isnan(weeks) or weeks < 2:
        return 0.0
    return min((weeks - 1) * TDCC_HIGH_PAIR_STREAK_BONUS_STEP, TDCC_HIGH_PAIR_STREAK_BONUS_CAP)


def add_tdcc_scores(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in DELTA_COLS:
        out[col] = out.get(col, pd.Series(index=out.index, dtype="float64")).map(to_number)

    weekly_sum = sum(out[col].fillna(0).clip(lower=0) for col in DELTA_COLS)
    out["tdcc_four_threshold_weekly_increase_sum"] = weekly_sum

    effective_count = sum(
        (out[col].fillna(0) > TDCC_EFFECTIVE_INCREASE_THRESHOLD).astype(int) for col in DELTA_COLS
    )
    weighted_score = sum(out[col].fillna(0) * weight for col, weight in DELTA_WEIGHTS.items())
    theme_bonus = out.get("theme_mainstream_status", "").map(lambda x: 5.0 if is_mainstream_theme(x) else 0.0)
    volume_ma20_lots = out.apply(latest_volume_ma20_lots, axis=1)
    low_volume_penalty = volume_ma20_lots.map(
        lambda x: TDCC_LOW_VOLUME_PENALTY
        if not math.isnan(to_number(x)) and to_number(x) < TDCC_LOW_VOLUME_MA20_LOTS_THRESHOLD
        else 0.0
    )
    high_pair_streak = out.apply(high_pair_effective_streak_weeks, axis=1)
    streak_bonus = high_pair_streak.map(high_pair_streak_bonus)

    out["tdcc_weighted_weekly_increase_score"] = weighted_score.round(2)
    out["tdcc_effective_increase_count"] = effective_count
    out["tdcc_sync_bonus"] = effective_count.map(sync_bonus)
    out["tdcc_theme_bonus"] = theme_bonus
    out["volume_ma20_lots"] = volume_ma20_lots.round(2)
    out["tdcc_low_volume_penalty"] = low_volume_penalty
    out["tdcc_high_pair_effective_streak_weeks"] = high_pair_streak
    out["tdcc_high_pair_streak_bonus"] = streak_bonus

    out["tdcc_weekly_increase_score"] = (
        out["tdcc_weighted_weekly_increase_score"]
        + out["tdcc_sync_bonus"]
        + out["tdcc_theme_bonus"]
        - out["tdcc_low_volume_penalty"]
    ).round(2)
    out["tdcc_consecutive_accumulation_score"] = (
        out["tdcc_weighted_weekly_increase_score"]
        + out["tdcc_sync_bonus"]
        + out["tdcc_high_pair_streak_bonus"]
        + out["tdcc_theme_bonus"]
        - out["tdcc_low_volume_penalty"]
    ).round(2)
    out["risk_bucket"] = out.get("tdcc_price_phase", "").map(risk_bucket)
    out["risk_bucket_zh"] = out["risk_bucket"].map(lambda x: RISK_BUCKET_ZH.get(safe_str(x), zh(x)))
    out["tdcc_phase_group_zh"] = out.get("tdcc_price_phase", "").map(lambda x: PHASE_ZH.get(safe_str(x), zh(x)))
    out["ranking_note_zh"] = out.apply(ranking_note, axis=1)
    return out


def ranking_note(row: pd.Series) -> str:
    deltas = [
        to_number(row.get("tdcc_1w_change_400")),
        to_number(row.get("tdcc_1w_change_600")),
        to_number(row.get("tdcc_1w_change_800")),
        to_number(row.get("tdcc_1w_change_1000")),
    ]
    effective_count = sum(
        1 for x in deltas if not pd.isna(x) and x > TDCC_EFFECTIVE_INCREASE_THRESHOLD
    )
    high_pair_streak = to_number(row.get("tdcc_high_pair_effective_streak_weeks"))
    parts = [f"有效級距增加 {effective_count}/4（門檻 >0.5）"]
    if not pd.isna(high_pair_streak) and high_pair_streak >= 2:
        parts.append(f"800/1000張有效連續增加 {high_pair_streak:.0f} 週")
    volume_lots = to_number(row.get("volume_ma20_lots"))
    if not pd.isna(volume_lots) and volume_lots < TDCC_LOW_VOLUME_MA20_LOTS_THRESHOLD:
        parts.append("20日均量低於1000張")
    phase = row.get("tdcc_phase_group_zh")
    if safe_str(phase):
        parts.append(safe_str(phase))
    return "；".join(parts)


def build_weekly_increase(df: pd.DataFrame) -> pd.DataFrame:
    eligible = df.copy()
    effective_count = eligible.get("tdcc_effective_increase_count", pd.Series(index=eligible.index)).map(to_number).fillna(0)
    eligible = eligible[effective_count >= 1].copy()
    eligible = eligible.sort_values(
        [
            "tdcc_weekly_increase_score",
            "tdcc_weighted_weekly_increase_score",
            "tdcc_1w_change_1000",
            "tdcc_1w_change_800",
        ],
        ascending=[False, False, False, False],
    )
    eligible["rank"] = range(1, len(eligible) + 1)
    return ensure_columns(eligible, BASE_COLUMNS)


def build_consecutive_accumulation(df: pd.DataFrame) -> pd.DataFrame:
    high_pair_streak = (
        df.get("tdcc_high_pair_effective_streak_weeks", pd.Series(index=df.index)).map(to_number).fillna(0)
    )
    eligible = df[high_pair_streak >= 2].copy()
    eligible = eligible.sort_values(
        [
            "tdcc_consecutive_accumulation_score",
            "tdcc_high_pair_effective_streak_weeks",
            "tdcc_weighted_weekly_increase_score",
        ],
        ascending=[False, False, False],
    )
    eligible["rank"] = range(1, len(eligible) + 1)
    return ensure_columns(eligible, BASE_COLUMNS)


def read_daily_model_signals() -> pd.DataFrame:
    signals = read_csv(DAILY_MODEL_SIGNALS, dtype=str)
    if not signals.empty:
        return signals
    return pd.DataFrame()


def build_model_cross(
    weekly: pd.DataFrame,
    consecutive: pd.DataFrame,
    daily_models: pd.DataFrame,
) -> pd.DataFrame:
    if daily_models.empty:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)

    daily = daily_models.copy()
    daily["stock_id"] = daily["stock_id"].astype(str).str.strip()
    daily["model_id"] = daily.get("model_id", "").map(safe_str)
    daily = daily[daily["model_id"].isin(TDCC_FULL_REPORT_ALLOWED_MODEL_CROSS_IDS)].copy()
    if daily.empty:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)
    daily["display_rank_num"] = daily.get("display_rank", daily.get("model_rank", "")).map(to_number)
    daily["model_score_num"] = daily.get("model_score", "").map(to_number)
    daily = daily.sort_values(
        ["stock_id", "model_id", "display_rank_num", "model_score_num"],
        ascending=[True, True, True, False],
    )
    daily = daily.drop_duplicates(["stock_id", "model_id"], keep="first")

    frames: list[pd.DataFrame] = []
    for list_type, ranking, score_col in [
        ("weekly_increase", weekly, "tdcc_weekly_increase_score"),
        ("consecutive_accumulation", consecutive, "tdcc_consecutive_accumulation_score"),
    ]:
        if ranking.empty:
            continue
        base = ranking.copy()
        base["stock_id"] = base["stock_id"].astype(str).str.strip()
        base = base.rename(columns={"rank": "tdcc_rank", score_col: "tdcc_score"})
        merged = base.merge(daily, on="stock_id", how="inner", suffixes=("", "_model"))
        if merged.empty:
            continue
        merged["tdcc_list_type"] = list_type
        merged["model_name_zh"] = merged.get("model_name_zh", "").map(lambda x: zh(x) or zh(merged.get("model_id", "")))
        merged["source_hit_labels_zh"] = merged.get("source_hit_labels_zh", "").map(zh)
        merged["why_selected_zh"] = merged.apply(human_reason_from_model, axis=1)
        merged["risk_tags_zh"] = merged.get("risk_tags_zh", "").map(zh)
        merged["next_confirmation_zh"] = merged.get("next_confirmation_zh", "").map(zh)
        merged["recommended_usage_zh"] = merged.get("recommended_usage_zh", "").map(zh)
        merged["operation_note_zh"] = merged.apply(operation_note, axis=1)
        merged["model_source"] = merged.get("source_category_zh", merged.get("original_category_cn", "")).map(zh)
        merged["display_rank"] = merged.get("display_rank", merged.get("model_rank", ""))
        merged["model_score"] = merged.get("model_score", "")
        merged["tdcc_model_rank_in_list"] = (
            merged.sort_values(["tdcc_list_type", "model_id", "tdcc_rank", "display_rank_num"])
            .groupby(["tdcc_list_type", "model_id"])
            .cumcount()
            + 1
        )
        frames.append(ensure_columns(merged, MODEL_CROSS_COLUMNS))

    if not frames:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)
    out = pd.concat(frames, ignore_index=True)
    return out.sort_values(["tdcc_list_type", "model_id", "tdcc_model_rank_in_list", "tdcc_rank"])


def human_reason_from_model(row: pd.Series) -> str:
    existing = zh(row.get("why_selected_human_zh"))
    if existing and "基礎分=" not in existing:
        return existing
    model = zh(row.get("model_name_zh")) or zh(row.get("model_id")) or "每日候選模型"
    phase = safe_str(row.get("tdcc_phase_group_zh"))
    risk = safe_str(row.get("risk_bucket_zh"))
    return f"符合 {model}；TDCC 狀態為 {phase or '資料不足'}，風險桶為 {risk or '待確認'}。"


def operation_note(row: pd.Series) -> str:
    model_id = safe_str(row.get("model_id"))
    if model_id in TDCC_FULL_REPORT_ALLOWED_MODEL_CROSS_IDS:
        return "以訊號日隔天開盤為進場假設，依 D+5 / D+10 統計與短線支撐管理；這是短線延續研究，不是低位買進模型。"
    next_text = zh(row.get("next_confirmation_zh"))
    usage = zh(row.get("recommended_usage_zh"))
    if usage:
        return usage
    if next_text:
        return next_text
    return "TDCC 為加分項，不可單獨作為買進理由；需搭配價格、量價與族群強弱確認。"


def row_from_ranking(row: pd.Series, report_kind: str, section_id: str, section_name: str, section_rank: int) -> dict[str, Any]:
    score = row.get("tdcc_weekly_increase_score")
    if section_id == "consecutive_accumulation":
        score = row.get("tdcc_consecutive_accumulation_score")
    return {
        "report_kind": report_kind,
        "section_id": section_id,
        "section_name_zh": section_name,
        "section_rank": section_rank,
        "tdcc_list_type": section_id,
        "tdcc_rank": row.get("rank", ""),
        "signal_date": row.get("signal_date", ""),
        "stock_id": row.get("stock_id", ""),
        "stock_name": row.get("stock_name", ""),
        "theme": row.get("theme", ""),
        "tdcc_phase_group_zh": row.get("tdcc_phase_group_zh", ""),
        "risk_bucket": row.get("risk_bucket", ""),
        "risk_bucket_zh": row.get("risk_bucket_zh", ""),
        "tdcc_score": score,
        "tdcc_weekly_increase_score": row.get("tdcc_weekly_increase_score", ""),
        "tdcc_consecutive_accumulation_score": row.get("tdcc_consecutive_accumulation_score", ""),
        "tdcc_1w_change_400": row.get("tdcc_1w_change_400", ""),
        "tdcc_1w_change_600": row.get("tdcc_1w_change_600", ""),
        "tdcc_1w_change_800": row.get("tdcc_1w_change_800", ""),
        "tdcc_1w_change_1000": row.get("tdcc_1w_change_1000", ""),
        "tdcc_weighted_weekly_increase_score": row.get("tdcc_weighted_weekly_increase_score", ""),
        "tdcc_effective_increase_count": row.get("tdcc_effective_increase_count", ""),
        "tdcc_sync_bonus": row.get("tdcc_sync_bonus", ""),
        "tdcc_theme_bonus": row.get("tdcc_theme_bonus", ""),
        "volume_ma20_lots": row.get("volume_ma20_lots", ""),
        "tdcc_low_volume_penalty": row.get("tdcc_low_volume_penalty", ""),
        "tdcc_high_pair_effective_streak_weeks": row.get("tdcc_high_pair_effective_streak_weeks", ""),
        "tdcc_high_pair_streak_bonus": row.get("tdcc_high_pair_streak_bonus", ""),
        "tdcc_consecutive_up_weeks": row.get("tdcc_consecutive_up_weeks", ""),
        "model_id": "",
        "model_name_zh": "",
        "model_rank": "",
        "model_score": "",
        "model_source": "",
        "source_hit_labels_zh": "",
        "why_selected_zh": row.get("ranking_note_zh", ""),
        "risk_tags_zh": row.get("risk_bucket_zh", ""),
        "next_confirmation_zh": "用每日候選模型與價格位置確認可操作性。",
        "recommended_usage_zh": "TDCC 排名用於籌碼追蹤，不單獨作為買進理由。",
        "report_usage_zh": "TDCC 排名用於籌碼追蹤，不單獨作為買進理由。",
        "operation_note_zh": "若價格已領先或過熱，需降為觀察；若仍在潛伏或初步確認，才進一步看每日候選模型。",
    }


def build_report_source_sections(
    weekly: pd.DataFrame,
    consecutive: pd.DataFrame,
    model_cross: pd.DataFrame,
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []

    for idx, (_, row) in enumerate(weekly.iterrows(), start=1):
        rows.append(row_from_ranking(row, "", "weekly_increase", "當週增幅排名", idx))
    for idx, (_, row) in enumerate(consecutive.iterrows(), start=1):
        rows.append(row_from_ranking(row, "", "consecutive_accumulation", "連續累積排名", idx))

    if not model_cross.empty:
        cross = model_cross.copy()
        cross = cross[cross["model_id"].isin(TDCC_FULL_REPORT_ALLOWED_MODEL_CROSS_IDS)]
        cross["_tdcc_list_order"] = cross["tdcc_list_type"].map(
            lambda value: {"weekly_increase": 1, "consecutive_accumulation": 2}.get(safe_str(value), 99)
        )
        cross = cross.sort_values(["_tdcc_list_order", "model_id", "tdcc_model_rank_in_list", "tdcc_rank"])
        for (list_type, model_id), group in cross.groupby(["tdcc_list_type", "model_id"], dropna=False, sort=False):
            group = group.sort_values(["tdcc_model_rank_in_list", "tdcc_rank"])
            section_id = f"model_cross_{list_type}_{model_id}"
            section_name = f"{list_type_zh(list_type)} × {zh(group.iloc[0].get('model_name_zh')) or zh(model_id)}"
            for idx, (_, row) in enumerate(group.iterrows(), start=1):
                rows.append(
                    {
                        "report_kind": "",
                        "section_id": section_id,
                        "section_name_zh": section_name,
                        "section_rank": idx,
                        "tdcc_list_type": list_type,
                        "tdcc_rank": row.get("tdcc_rank", ""),
                        "signal_date": row.get("signal_date", ""),
                        "stock_id": row.get("stock_id", ""),
                        "stock_name": row.get("stock_name", ""),
                        "theme": row.get("theme", ""),
                        "tdcc_phase_group_zh": row.get("tdcc_phase_group_zh", ""),
                        "risk_bucket": row.get("risk_bucket", ""),
                        "risk_bucket_zh": row.get("risk_bucket_zh", ""),
                        "tdcc_score": row.get("tdcc_score", ""),
                        "tdcc_weekly_increase_score": "",
                        "tdcc_consecutive_accumulation_score": "",
                        "tdcc_1w_change_400": "",
                        "tdcc_1w_change_600": "",
                        "tdcc_1w_change_800": "",
                        "tdcc_1w_change_1000": "",
                        "tdcc_weighted_weekly_increase_score": "",
                        "tdcc_effective_increase_count": "",
                        "tdcc_sync_bonus": "",
                        "tdcc_theme_bonus": "",
                        "volume_ma20_lots": "",
                        "tdcc_low_volume_penalty": "",
                        "tdcc_high_pair_effective_streak_weeks": "",
                        "tdcc_high_pair_streak_bonus": "",
                        "tdcc_consecutive_up_weeks": "",
                        "model_id": row.get("model_id", ""),
                        "model_name_zh": zh(row.get("model_name_zh")) or zh(row.get("model_id")),
                        "model_rank": row.get("display_rank", ""),
                        "tdcc_model_rank_in_list": row.get("tdcc_model_rank_in_list", row.get("display_rank", "")),
                        "model_score": row.get("model_score", ""),
                        "model_source": row.get("model_source", ""),
                        "source_hit_labels_zh": row.get("source_hit_labels_zh", ""),
                        "why_selected_zh": row.get("why_selected_zh", ""),
                        "risk_tags_zh": row.get("risk_tags_zh", ""),
                        "next_confirmation_zh": row.get("next_confirmation_zh", ""),
                        "recommended_usage_zh": row.get("recommended_usage_zh", ""),
                        "report_usage_zh": row.get("recommended_usage_zh", "") or row.get("operation_note_zh", ""),
                        "operation_note_zh": row.get("operation_note_zh", ""),
                    }
                )

    return ensure_columns(pd.DataFrame(rows), REPORT_COLUMNS)


def build_report_ready(source_sections: pd.DataFrame, manifest: pd.DataFrame, report_kind: str) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for _, section_row in sections_for_report(manifest, report_kind).iterrows():
        section_id = safe_str(section_row.get("section_id"))
        if not section_id:
            continue
        section_rows = source_sections[source_sections["section_id"].map(safe_str) == section_id].copy()
        if section_rows.empty:
            continue
        limit = section_limit(section_row, report_kind)
        section_rows = section_rows.head(limit)
        section_rows["report_kind"] = report_kind
        section_rows["section_name_zh"] = safe_str(section_row.get("section_title_zh")) or section_id
        section_rows["section_rank"] = range(1, len(section_rows) + 1)
        frames.append(section_rows)

    if not frames:
        return ensure_columns(pd.DataFrame(), REPORT_COLUMNS)
    return ensure_columns(pd.concat(frames, ignore_index=True), REPORT_COLUMNS)


def list_type_zh(value: Any) -> str:
    return {
        "weekly_increase": "當週增幅榜",
        "consecutive_accumulation": "連續累積榜",
    }.get(safe_str(value), zh(value))


def write_md_table(df: pd.DataFrame, path: Path, title: str, columns: list[str], limit: int | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    display_df = pdf_display_table(df, columns, limit=limit)
    content = [
        f"# {title}",
        "",
        f"- TDCC data date: {signal_date_label(df)}",
        "",
        f"- generated_at: {pd.Timestamp.now(tz='Asia/Taipei').strftime('%Y-%m-%d %H:%M:%S Asia/Taipei')}",
        f"- rows: {len(df)}",
        "",
        markdown_table(display_df, list(display_df.columns), limit=None),
        "",
    ]
    path.write_text("\n".join(content), encoding="utf-8")


def signal_date_label(df: pd.DataFrame) -> str:
    if df.empty or "signal_date" not in df.columns:
        return "unknown"
    dates = sorted({safe_str(value) for value in df["signal_date"].dropna() if safe_str(value)})
    if not dates:
        return "unknown"
    return dates[0] if len(dates) == 1 else ", ".join(dates)


def unique_report_signal_date(df: pd.DataFrame, label: str) -> str:
    if df.empty or "signal_date" not in df.columns:
        raise RuntimeError(f"{label} must contain a signal_date column before TDCC report rendering.")
    dates = sorted({safe_str(value) for value in df["signal_date"].dropna() if safe_str(value)})
    if len(dates) != 1:
        raise RuntimeError(f"{label} must contain exactly one signal_date before TDCC report rendering, got: {dates}")
    return dates[0]


def report_date_from_ready_csvs(highlight: pd.DataFrame, full: pd.DataFrame) -> str:
    highlight_date = unique_report_signal_date(highlight, "highlight report-ready CSV")
    full_date = unique_report_signal_date(full, "full report-ready CSV")
    if highlight_date != full_date:
        raise RuntimeError(f"TDCC report-ready CSV signal_date mismatch: highlight={highlight_date}, full={full_date}")
    return highlight_date


def write_report_md(df: pd.DataFrame, path: Path, title: str, manifest: pd.DataFrame, report_kind: str, report_date: str) -> None:
    lines = [
        f"# {title}",
        "",
        f"- TDCC data date: {signal_date_label(df)}",
        "",
        "這份報告使用 TDCC weekly report-ready structured data 產生；TDCC 是籌碼追蹤，不是單獨買進理由。",
        "",
    ]
    if df.empty:
        lines.append("目前沒有可用資料。")
    else:
        for _, section_row in sections_for_report(manifest, report_kind).iterrows():
            section_id = safe_str(section_row.get("section_id"))
            section = safe_str(section_row.get("section_title_zh")) or section_id
            show = df[df["section_id"].map(safe_str) == section_id].copy()
            columns = pdf_columns_for_contract(section_row.get("table_contract"), show)
            display_df = pdf_display_table(show, columns)
            lines += [
                f"## {section}",
                "",
                markdown_table(display_df, list(display_df.columns), limit=None)
                if not display_df.empty
                else "沒有可用報告資料。",
                "",
            ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def wrap_text(text: Any, max_chars: int) -> str:
    s = safe_str(text)
    if not s:
        return ""
    parts = []
    while len(s) > max_chars:
        parts.append(s[:max_chars])
        s = s[max_chars:]
    parts.append(s)
    return "\n".join(parts)


def write_pdf(df: pd.DataFrame, path: Path, title: str, max_rows_per_section: int | None = None) -> None:
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import cm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except Exception as exc:  # pragma: no cover - validated in CI
        raise RuntimeError(f"reportlab unavailable; TDCC weekly PDF cannot be generated: {exc}") from exc

    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        "zh-normal",
        parent=styles["Normal"],
        fontName="STSong-Light",
        fontSize=8.5,
        leading=11,
        wordWrap="CJK",
    )
    title_style = ParagraphStyle(
        "zh-title",
        parent=styles["Title"],
        fontName="STSong-Light",
        fontSize=18,
        leading=24,
        alignment=1,
    )
    h2 = ParagraphStyle(
        "zh-h2",
        parent=styles["Heading2"],
        fontName="STSong-Light",
        fontSize=12,
        leading=15,
        spaceBefore=8,
        spaceAfter=6,
    )

    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        rightMargin=0.8 * cm,
        leftMargin=0.8 * cm,
        topMargin=0.8 * cm,
        bottomMargin=0.8 * cm,
    )
    story: list[Any] = [
        Paragraph(title, title_style),
        Spacer(1, 0.2 * cm),
        Paragraph("TDCC 週報以當週增幅、連續累積與每日候選模型交集呈現。TDCC 不作單獨買進理由。", normal),
        Spacer(1, 0.3 * cm),
    ]
    if df.empty:
        story.append(Paragraph("目前沒有可用資料。", normal))
    else:
        first = True
        headers = ["序", "代號", "股票", "族群", "TDCC階段", "風險桶", "TDCC分數", "模型", "模型名次", "模型分數", "入選 / 用途", "操作提醒"]
        col_widths = [0.8 * cm, 1.3 * cm, 1.6 * cm, 2.1 * cm, 3.0 * cm, 2.5 * cm, 1.4 * cm, 3.0 * cm, 1.2 * cm, 1.3 * cm, 5.0 * cm, 5.0 * cm]
        for section, group in df.groupby("section_id", sort=False):
            if not first:
                story.append(PageBreak())
            first = False
            story.append(Paragraph(safe_str(section), h2))
            show = group.head(max_rows_per_section) if max_rows_per_section else group
            table_data = [[Paragraph(h, normal) for h in headers]]
            for _, row in show.iterrows():
                table_data.append(
                    [
                        Paragraph(safe_str(row.get("section_rank")), normal),
                        Paragraph(safe_str(row.get("stock_id")), normal),
                        Paragraph(safe_str(row.get("stock_name")), normal),
                        Paragraph(wrap_text(row.get("theme"), 10), normal),
                        Paragraph(wrap_text(row.get("tdcc_phase_group_zh"), 12), normal),
                        Paragraph(wrap_text(row.get("risk_bucket_zh"), 12), normal),
                        Paragraph(pct(row.get("tdcc_score"), 1), normal),
                        Paragraph(wrap_text(row.get("model_name_zh"), 12), normal),
                        Paragraph(safe_str(row.get("model_rank")), normal),
                        Paragraph(pct(row.get("model_score"), 1), normal),
                        Paragraph(wrap_text(row.get("why_selected_zh"), 26), normal),
                        Paragraph(wrap_text(row.get("operation_note_zh"), 26), normal),
                    ]
                )
            table = Table(table_data, colWidths=col_widths, repeatRows=1)
            table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("FONTNAME", (0, 0), (-1, -1), "STSong-Light"),
                        ("FONTSIZE", (0, 0), (-1, -1), 8),
                        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f3f6f8")]),
                    ]
                )
            )
            story.append(table)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def write_pdf_v2(df: pd.DataFrame, path: Path, title: str, manifest: pd.DataFrame, report_kind: str, report_date: str) -> None:
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4, landscape
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import cm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
    except Exception as exc:  # pragma: no cover - validated in CI
        raise RuntimeError(f"reportlab unavailable; TDCC weekly PDF cannot be generated: {exc}") from exc

    def register_report_font() -> str:
        font_path = Path(r"C:\Windows\Fonts\kaiu.ttf")
        if font_path.exists():
            pdfmetrics.registerFont(TTFont("DFKai-SB", str(font_path)))
            return "DFKai-SB"
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"

    pdf_font = register_report_font()
    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        "zh-normal-v2",
        parent=styles["Normal"],
        fontName=pdf_font,
        fontSize=14,
        leading=17,
        wordWrap="CJK",
    )
    small = ParagraphStyle(
        "zh-small-v2",
        parent=normal,
        fontSize=14,
        leading=17,
    )
    title_style = ParagraphStyle(
        "zh-title-v2",
        parent=styles["Title"],
        fontName=pdf_font,
        fontSize=18,
        leading=24,
        alignment=1,
    )
    h2 = ParagraphStyle(
        "zh-h2-v2",
        parent=styles["Heading2"],
        fontName=pdf_font,
        fontSize=14,
        leading=18,
        spaceBefore=8,
        spaceAfter=6,
    )

    def para(value: Any, max_chars: int, style: Any = normal) -> Any:
        return Paragraph(wrap_text(clean_pdf_text(value), max_chars), style)

    def table_style() -> Any:
        return TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONTNAME", (0, 0), (-1, -1), pdf_font),
                ("FONTSIZE", (0, 0), (-1, -1), 14),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f3f6f8")]),
            ]
        )

    def headers_for_columns(columns: list[str]) -> list[Any]:
        return [Paragraph(PDF_HEADER_ZH.get(column, column), normal) for column in columns]

    def widths_for_columns(columns: list[str]) -> list[Any]:
        if columns == PDF_MODEL_CROSS_COLUMNS:
            return [
                0.7 * cm,
                1.4 * cm,
                1.55 * cm,
                2.35 * cm,
                1.9 * cm,
                1.45 * cm,
                2.55 * cm,
                1.35 * cm,
                1.4 * cm,
                4.25 * cm,
                3.55 * cm,
                4.65 * cm,
            ]
        return [
            0.8 * cm,
            1.45 * cm,
            1.65 * cm,
            2.7 * cm,
            2.1 * cm,
            1.8 * cm,
            5.35 * cm,
            4.45 * cm,
            6.35 * cm,
        ]

    def cell_para(row: pd.Series, column: str) -> Any:
        text = pdf_display_cell(row, column)
        if column in {"section_rank", "stock_id", "tdcc_model_rank_in_list", "tdcc_score", "model_score"}:
            return text
        max_chars = {
            "section_rank": 4,
            "tdcc_model_rank_in_list": 4,
            "tdcc_score": 6,
            "model_score": 6,
            "stock_name": 8,
            "tdcc_phase_group_zh": 10,
            "risk_bucket": 10,
            "model_name_zh": 10,
            "why_selected_zh": 20,
            "next_confirmation_zh": 18,
            "operation_note_zh": 22,
        }.get(column, 16)
        return Paragraph(wrap_text(text, max_chars), small if column in {"why_selected_zh", "next_confirmation_zh", "operation_note_zh"} else normal)

    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        rightMargin=0.8 * cm,
        leftMargin=0.8 * cm,
        topMargin=0.8 * cm,
        bottomMargin=0.8 * cm,
    )
    story: list[Any] = [
        Paragraph(title, title_style),
        Spacer(1, 0.2 * cm),
        Paragraph(f"TDCC data date: {report_date}", normal),
        Spacer(1, 0.2 * cm),
        Paragraph("TDCC 週報以當週增幅、連續累積與每日候選模型交集呈現。TDCC 不作單獨買進理由。", normal),
        Spacer(1, 0.3 * cm),
    ]
    if df.empty:
        story.append(Paragraph("目前沒有可用資料。", normal))
    else:
        first = True
        for _, section_row in sections_for_report(manifest, report_kind).iterrows():
            section_id = safe_str(section_row.get("section_id"))
            section = safe_str(section_row.get("section_title_zh")) or section_id
            group = df[df["section_id"].map(safe_str) == section_id].copy()
            if not first:
                story.append(PageBreak())
            first = False
            story.append(Paragraph(safe_str(section), h2))
            show = group

            if show.empty:
                story.append(Paragraph("沒有可用報告資料。", normal))
                continue

            columns = pdf_columns_for_contract(section_row.get("table_contract"), show)
            col_widths = widths_for_columns(columns)
            table_data = [headers_for_columns(columns)]
            for _, row in show.iterrows():
                table_data.append([cell_para(row, column) for column in columns])

            table = Table(table_data, colWidths=col_widths, repeatRows=1)
            table.setStyle(table_style())
            story.append(table)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def upsert_readme_fields(fields: dict[str, str]) -> None:
    for path in README_PATHS:
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        existing = {line.split("=", 1)[0]: i for i, line in enumerate(lines) if "=" in line}
        for key, value in fields.items():
            line = f"{key}={value}"
            if key in existing:
                lines[existing[key]] = line
            else:
                lines.append(line)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


MODEL_TUNING_MARKER = "## Model Tuning Recommendation"
INTERPRETATION_RULES_MARKER = "## Interpretation Rules"


def tracking_model_tuning_section() -> str:
    lines = [
        MODEL_TUNING_MARKER,
        "",
        "- tuning_status: not_ready",
        "- reason: insufficient mature D+10 / D+20 samples",
        "- allowed_changes: reporting_priority_only",
        "- forbidden_changes: core_weight_change",
        "- threshold_for_review: each major phase mature_d10 >= 30, or overall mature_d20 >= 100 with at least 3-4 weeks of data",
        "- note: keep TDCC/ABM model weights frozen until mature samples are sufficient.",
    ]
    return "\n".join(lines)


def ensure_tracking_model_tuning_contract(text: str) -> str:
    required = [
        MODEL_TUNING_MARKER,
        "tuning_status: not_ready",
        "forbidden_changes: core_weight_change",
    ]
    if all(item in text for item in required):
        return text.rstrip() + "\n"

    section = tracking_model_tuning_section()
    if MODEL_TUNING_MARKER in text:
        prefix, tail = text.split(MODEL_TUNING_MARKER, 1)
        if INTERPRETATION_RULES_MARKER in tail:
            _, suffix = tail.split(INTERPRETATION_RULES_MARKER, 1)
            return prefix.rstrip() + "\n\n" + section + "\n\n" + INTERPRETATION_RULES_MARKER + "\n" + suffix.lstrip("\r\n")
        return prefix.rstrip() + "\n\n" + section + "\n"

    if INTERPRETATION_RULES_MARKER in text:
        prefix, suffix = text.split(INTERPRETATION_RULES_MARKER, 1)
        return prefix.rstrip() + "\n\n" + section + "\n\n" + INTERPRETATION_RULES_MARKER + "\n" + suffix.lstrip("\r\n")

    return text.rstrip() + "\n\n" + section + "\n"


def upsert_tracking_weekly_section(text: str, marker: str, legacy_marker: str, section: list[str]) -> str:
    section_text = "\n".join(section).rstrip()
    active_marker = marker if marker in text else legacy_marker if legacy_marker in text else ""
    if not active_marker:
        return text.rstrip() + "\n\n" + section_text + "\n"

    prefix, tail = text.split(active_marker, 1)
    for next_marker in [MODEL_TUNING_MARKER, INTERPRETATION_RULES_MARKER]:
        if next_marker in tail:
            _, suffix = tail.split(next_marker, 1)
            return prefix.rstrip() + "\n\n" + section_text + "\n\n" + next_marker + "\n" + suffix.lstrip("\r\n")
    return prefix.rstrip() + "\n\n" + section_text + "\n"


def append_tracking_packet(fields: dict[str, str]) -> None:
    if not TRACKING_PACKET_MD.exists():
        return
    text = TRACKING_PACKET_MD.read_text(encoding="utf-8", errors="replace")
    marker = "## TDCC Weekly Increase and Consecutive Candidate Reports"
    legacy_marker = "## TDCC WEEKLY CANDIDATE REPORTS"
    section = [
        marker,
        "",
        "- 精華版與完整版由 report-ready CSV/MD/PDF 產出。",
        "- 精華版包含當週增幅、連續累積、當週增幅 x TDCC 短線延續 D+5/D+10、連續累積 x TDCC 短線延續 D+5/D+10，各最多前十名。",
        "- 完整版使用相同四個清單，各最多列前五十名；不足五十就全列。",
        "",
    ]
    for key, value in fields.items():
        section.append(f"- {key}: {value}")
    section.append("")
    text = upsert_tracking_weekly_section(text, marker, legacy_marker, section)
    text = ensure_tracking_model_tuning_contract(text)
    TRACKING_PACKET_MD.write_text(text, encoding="utf-8")


def validate_outputs(highlight: pd.DataFrame, full: pd.DataFrame, manifest: pd.DataFrame) -> None:
    if highlight.empty:
        raise RuntimeError("TDCC highlight report-ready table is empty.")
    if full.empty:
        raise RuntimeError("TDCC full report-ready table is empty.")
    for report_name, report_df in [("highlight", highlight), ("full", full)]:
        counts = report_df.groupby("section_id", dropna=False).size()
        for _, section_row in sections_for_report(manifest, report_name).iterrows():
            section_id = safe_str(section_row.get("section_id"))
            count = int(counts.get(section_id, 0))
            limit = section_limit(section_row, report_name)
            if count > limit:
                raise RuntimeError(f"{report_name} TDCC report section {section_id} has {count} rows above limit {limit}")
            if manifest_bool(section_row.get("required"), True) and count == 0:
                raise RuntimeError(f"{report_name} TDCC report required section is empty: {section_id}")
        title_groups = report_df.groupby("section_name_zh", dropna=False)["section_id"].nunique()
        merged_titles = title_groups[title_groups > 1]
        if not merged_titles.empty:
            detail = ", ".join(safe_str(section) for section in merged_titles.index)
            raise RuntimeError(f"{report_name} TDCC report maps multiple section_id values to one section title: {detail}")
    for report_name, report_df in [("highlight", highlight), ("full", full)]:
        signal_dates = sorted({safe_str(value) for value in report_df["signal_date"].dropna() if safe_str(value)})
        if len(signal_dates) != 1:
            raise RuntimeError(f"{report_name} TDCC report must contain exactly one signal_date, got: {signal_dates}")
        consecutive_rows = report_df[report_df["section_id"].map(safe_str) == "consecutive_accumulation"]
        high_pair_weeks = consecutive_rows["tdcc_high_pair_effective_streak_weeks"].map(to_number).fillna(0)
        bad_consecutive = consecutive_rows[high_pair_weeks < 2]
        if not bad_consecutive.empty:
            examples = ", ".join(
                f"{safe_str(row.get('stock_id'))}:{safe_str(row.get('tdcc_high_pair_effective_streak_weeks'))}"
                for _, row in bad_consecutive.head(10).iterrows()
            )
            raise RuntimeError(
                f"{report_name} TDCC consecutive accumulation section contains rows below 2-week 800/1000 effective streak: {examples}"
            )
        model_rows = report_df[report_df["model_id"].map(safe_str) != ""]
        bad_models = sorted(set(model_rows["model_id"].map(safe_str)) - TDCC_FULL_REPORT_ALLOWED_MODEL_CROSS_IDS)
        if bad_models:
            raise RuntimeError(f"{report_name} TDCC report contains unsupported model cross sections: {bad_models}")
    highlight_date = sorted({safe_str(value) for value in highlight["signal_date"].dropna() if safe_str(value)})
    full_date = sorted({safe_str(value) for value in full["signal_date"].dropna() if safe_str(value)})
    if highlight_date != full_date:
        raise RuntimeError(f"TDCC highlight/full signal_date mismatch: highlight={highlight_date}, full={full_date}")
    for path in [HIGHLIGHT_PDF, FULL_PDF]:
        if not path.exists() or path.stat().st_size < 10_000:
            raise RuntimeError(f"TDCC PDF not generated or too small: {path}")


def sync_docs_latest() -> None:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    for src in DOCS_SYNC_PATHS:
        if not src.exists():
            continue
        dst = DOCS_LATEST_DIR / src.name
        shutil.copyfile(src, dst)


def main() -> int:
    latest, meta = prepare_latest_frame()
    if latest.empty:
        raise RuntimeError("No TDCC latest frame available.")
    latest = add_tdcc_scores(latest)
    theme_map = load_theme_display_map()
    latest = apply_theme_display(latest, theme_map)

    weekly = build_weekly_increase(latest)
    consecutive = build_consecutive_accumulation(latest)
    daily_models = read_daily_model_signals()
    model_cross = build_model_cross(weekly, consecutive, daily_models)

    report_source_sections = build_report_source_sections(weekly, consecutive, model_cross)
    manifest = load_section_manifest(report_source_sections)
    highlight = build_report_ready(report_source_sections, manifest, "highlight")
    full = build_report_ready(report_source_sections, manifest, "full")

    write_csv(weekly, WEEKLY_INCREASE_CSV)
    write_csv(consecutive, CONSECUTIVE_CSV)
    write_csv(model_cross, MODEL_CROSS_CSV)
    write_csv(highlight, HIGHLIGHT_FOR_REPORT_CSV)
    write_csv(full, FULL_FOR_REPORT_CSV)

    highlight_for_render = read_csv(HIGHLIGHT_FOR_REPORT_CSV, dtype=str)
    full_for_render = read_csv(FULL_FOR_REPORT_CSV, dtype=str)
    report_date = report_date_from_ready_csvs(highlight_for_render, full_for_render)
    render_source = pd.concat([highlight_for_render, full_for_render], ignore_index=True)
    render_manifest = load_section_manifest(render_source)

    write_md_table(weekly, WEEKLY_INCREASE_MD, "TDCC 當週增幅排名", BASE_COLUMNS, limit=TDCC_FULL_REPORT_SECTION_LIMIT)
    write_md_table(consecutive, CONSECUTIVE_MD, "TDCC 連續累積排名", BASE_COLUMNS, limit=TDCC_FULL_REPORT_SECTION_LIMIT)
    write_md_table(model_cross, MODEL_CROSS_MD, "TDCC 名單與每日候選模型交集", MODEL_CROSS_COLUMNS, limit=200)
    write_report_md(highlight_for_render, HIGHLIGHT_FOR_REPORT_MD, "TDCC 週報精華版 report-ready table", render_manifest, "highlight", report_date)
    write_report_md(full_for_render, FULL_FOR_REPORT_MD, "TDCC 週報完整版 report-ready table", render_manifest, "full", report_date)
    write_report_md(highlight_for_render, HIGHLIGHT_MD, "TDCC 大戶籌碼週報精華版", render_manifest, "highlight", report_date)
    write_report_md(full_for_render, FULL_MD, "TDCC 大戶籌碼週報完整版", render_manifest, "full", report_date)

    write_pdf_v2(highlight_for_render, HIGHLIGHT_PDF, "TDCC 大戶籌碼週報精華版", render_manifest, "highlight", report_date)
    write_pdf_v2(full_for_render, FULL_PDF, "TDCC 大戶籌碼週報完整版", render_manifest, "full", report_date)

    fields = {
        "tdcc_weekly_report_section_manifest_csv_raw_url": raw_url(SECTION_MANIFEST_CSV),
        "tdcc_weekly_report_section_manifest_csv_pages_url": pages_url(SECTION_MANIFEST_CSV),
        "tdcc_weekly_candidate_highlight_for_report_csv_raw_url": raw_url(HIGHLIGHT_FOR_REPORT_CSV),
        "tdcc_weekly_candidate_highlight_for_report_md_raw_url": raw_url(HIGHLIGHT_FOR_REPORT_MD),
        "tdcc_weekly_candidate_full_for_report_csv_raw_url": raw_url(FULL_FOR_REPORT_CSV),
        "tdcc_weekly_candidate_full_for_report_md_raw_url": raw_url(FULL_FOR_REPORT_MD),
        "tdcc_weekly_candidate_highlight_pdf_raw_url": raw_url(HIGHLIGHT_PDF),
        "tdcc_weekly_candidate_full_pdf_raw_url": raw_url(FULL_PDF),
        "tdcc_weekly_candidate_highlight_pdf_pages_url": pages_url(HIGHLIGHT_PDF),
        "tdcc_weekly_candidate_full_pdf_pages_url": pages_url(FULL_PDF),
    }
    upsert_readme_fields(fields)
    append_tracking_packet(fields)
    validate_outputs(highlight_for_render, full_for_render, render_manifest)
    sync_docs_latest()

    print(f"latest_signal_date={meta.get('latest_signal_date', '')}")
    for path in [
        WEEKLY_INCREASE_CSV,
        CONSECUTIVE_CSV,
        MODEL_CROSS_CSV,
        SECTION_MANIFEST_CSV,
        HIGHLIGHT_FOR_REPORT_CSV,
        FULL_FOR_REPORT_CSV,
        HIGHLIGHT_PDF,
        FULL_PDF,
    ]:
        print(f"Saved: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
