from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Iterable

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    main_price_date_from_freshness,
    normalize_code,
    now_text,
    read_csv,
    resolve_candidate_signal_date,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
VOLUME_BREAKOUT_WATCH = LATEST_DIR / "volume_breakout_watch_latest.csv"
TDCC_EDGE_CANDIDATES = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
WEEKLY_SURGE_CANDIDATES = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv"
MODEL_PARAMETER_RECOMMENDATIONS = LATEST_DIR / "daily_model_parameter_recommendations_latest.csv"
STOCK_THEME_TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
MODEL_HISTORY_DIR = Path("output/history/daily_candidate_models")
MODEL_SIGNAL_LOG_CSV = MODEL_HISTORY_DIR / "daily_candidate_model_signal_log.csv"
STOCK_PRICE_HISTORY_DIR = Path("data/stock_price_history")
TDCC_STOCK_HISTORY_DIR = Path("data/tdcc_stock_history")

PARAMETERS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
PARAMETERS_MD = LATEST_DIR / "daily_candidate_model_parameters_latest.md"
SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_latest.csv"
SIGNALS_MD = LATEST_DIR / "daily_candidate_model_signals_latest.md"
REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
REPORT_SIGNALS_MD = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.md"
FRONTPAGE_UNIQUE_CSV = LATEST_DIR / "daily_candidate_frontpage_unique_latest.csv"
FRONTPAGE_UNIQUE_MD = LATEST_DIR / "daily_candidate_frontpage_unique_latest.md"
MODEL_REPEAT_CSV = LATEST_DIR / "daily_candidate_same_model_repeat_latest.csv"
MODEL_REPEAT_MD = LATEST_DIR / "daily_candidate_same_model_repeat_latest.md"
ROTATION_CSV = LATEST_DIR / "daily_candidate_group_rotation_latest.csv"
ROTATION_MD = LATEST_DIR / "daily_candidate_group_rotation_latest.md"
PACKET_MD = LATEST_DIR / "daily_candidate_model_layer_packet_latest.md"
VALIDATION_JSON = LATEST_DIR / "daily_candidate_model_layer_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_candidate_model_layer_validation_latest.md"


RECOMMENDATION_COLUMNS = [
    "recommended_usage",
    "recommended_close_exit_horizon",
    "best_close_win_rate_pct",
    "best_avg_close_return_pct",
    "recommended_high_exit_horizon",
    "best_avg_high_return_pct",
    "best_high_5pct_hit_rate_pct",
    "recommended_sample_size",
    "recommended_unique_stocks",
    "recommended_sample_status",
    "model_revision_note",
]


CORE_AI_BUCKETS = {
    "ai_server_ipc_theme",
    "ai_pc_consumer_theme",
    "ai_server_mechanical_theme",
    "ai_chip_testing_theme",
    "asic_advanced_process_theme",
    "semiconductor_equipment_material_theme",
    "advanced_packaging_theme",
    "memory_hbm_theme",
    "network_optical_datacenter_theme",
    "low_earth_orbit_satellite_theme",
    "high_speed_interconnect_theme",
    "thermal_solution_theme",
    "power_supply_theme",
    "pcb_ccl_theme",
    "glass_fiber_ccl_theme",
    "fpc_flexible_pcb_theme",
    "passive_component_theme",
    "robotics_precision_motion_theme",
    "robotics_automation_theme",
    "robotics_ipc_edge_ai_theme",
    "robotics_optics_sensor_theme",
}

BULLISH_WARRANT = {"call_inflow", "call_strong_inflow", "call_put_bullish"}
POSITIVE_TDCC = {"strong_accumulation", "mild_accumulation"}


CATEGORY_ZH = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發但股價尚未反應",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
    "volume_breakout": "帶量突破",
    "short_term_specialty": "短線專項",
}

REPORT_BUCKET_ZH = {
    "mainstream": "主流",
    "non_mainstream": "非主流",
    "unclassified": "未分類",
    "research_only": "研究用",
}

TDCC_STATUS_ZH = {
    "strong_accumulation": "大戶強累積",
    "mild_accumulation": "大戶溫和增加",
    "neutral": "中性",
    "distribution_warning": "大戶轉弱警示",
    "tdcc_leading_price": "TDCC領先股價",
    "tdcc_price_confirmed": "TDCC與股價初步確認",
    "price_leading_tdcc": "股價領先TDCC",
    "overheated_after_tdcc": "TDCC後股價過熱",
    "tdcc_price_divergence": "TDCC與股價背離",
    "insufficient_tdcc_history": "TDCC歷史不足",
    "insufficient_price_context": "價格脈絡不足",
    "neutral_or_unclear": "訊號不明",
}

WARRANT_SIGNAL_ZH = {
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購流入",
    "call_put_bullish": "認購 / 認售偏多",
    "put_inflow": "認售流入",
    "put_strong_inflow": "認售強流入",
    "put_call_bearish": "認售 / 認購偏空",
    "no_signal": "無明確權證訊號",
}

RISK_TAG_ZH = {
    "false_breakout_risk": "假突破風險",
    "tdcc_distribution_warning": "TDCC轉弱警示",
    "continued_overheated": "連續過熱",
    "overheated_breakout": "短線過熱突破",
    "overextended": "乖離過大",
    "high_level_volume_risk": "高位放量風險",
    "repeated_but_no_breakout": "反覆上榜但尚未突破",
    "needs_eps_confirmation": "需EPS / 毛利確認",
    "revenue_good_eps_unconfirmed": "營收好但獲利品質待確認",
    "must_not_overstate": "不可過度解讀",
    "warrant_overheat": "權證過熱",
    "benchmark_weak": "弱於大盤 / benchmark",
    "insufficient_tdcc_history": "TDCC歷史不足",
    "insufficient_price_data": "價格資料不足",
}

STRUCTURAL_BUCKET_ZH = {
    "ai_server_ipc_theme": "AI伺服器 / 工業電腦",
    "ai_pc_consumer_theme": "AI PC / 消費電子",
    "ai_server_mechanical_theme": "AI伺服器機構件",
    "ai_chip_testing_theme": "AI晶片測試",
    "asic_advanced_process_theme": "矽智財 / ASIC",
    "semiconductor_equipment_material_theme": "半導體設備 / 材料",
    "advanced_packaging_theme": "先進封裝",
    "memory_hbm_theme": "記憶體 / HBM / 儲存",
    "network_optical_datacenter_theme": "網通 / 光通訊 / 資料中心",
    "low_earth_orbit_satellite_theme": "低軌衛星",
    "high_speed_interconnect_theme": "高速傳輸 / 連接器",
    "thermal_solution_theme": "散熱 / 液冷",
    "power_supply_theme": "電源 / BBU",
    "pcb_ccl_theme": "PCB / CCL / ABF材料",
    "glass_fiber_ccl_theme": "玻纖布 / CCL",
    "fpc_flexible_pcb_theme": "軟板 / FPC",
    "passive_component_theme": "被動元件",
    "robotics_precision_motion_theme": "機器人 / 精密傳動",
    "robotics_automation_theme": "機器人 / 自動化",
    "robotics_ipc_edge_ai_theme": "機器人 / 邊緣AI",
    "robotics_optics_sensor_theme": "機器人 / 光學感測",
    "automotive_electronics_theme": "車用電子",
    "electrical_cable_grid_theme": "重電 / 電線電纜",
    "electronic_component_general_theme": "電子零組件",
    "other_electronics_general_theme": "其他電子",
    "computer_peripheral_general_theme": "電腦及週邊",
    "optoelectronics_general_theme": "光電",
    "information_service_general_theme": "資訊服務",
    "communications_network_general_theme": "通信網路",
}

SCORE_COMPONENT_ZH_REPLACEMENTS = {
    "base=50": "基礎分=50",
    "type=neckline_volume_breakout": "類型=頸線帶量突破",
    "type=strict_60d_volume_breakout": "類型=60日高點帶量突破",
    "type=平台_volume_breakout": "類型=平台帶量突破",
    "volume_score=": "量能分數=",
    "close_above_previous_20d_high": "收盤站上20日前高",
    "close_above_previous_60d_high": "收盤站上60日前高",
    "near_previous_60d_high_with_volume": "接近60日前高且放量",
    "not_close_near_high": "收盤未靠近日高",
    "five_day_momentum": "5日動能強",
    "long_upper_shadow_risk": "長上影風險",
    "far_above_ma20": "乖離MA20過大",
    "twenty_day_overheated": "20日漲幅過熱",
    "量比_ge_2": "量比>=2",
    "volume_ratio_ge_2": "量比>=2",
    "volume_ratio": "量比",
    "range_breakout": "盤整突破",
    "TDCC positive": "TDCC正向",
    "warrant bullish": "權證偏多",
    "revenue strong": "營收強",
    "lower position": "位階較低",
    "platform": "平台",
    "near high": "接近前高",
    "theme": "族群",
    "mainstream": "主流",
    "risk penalty": "風險扣分",
    "best D+5": "最佳D+5",
    "best D+10": "最佳D+10",
    "D+10 win": "D+10勝率",
    "D+10 rel": "D+10相對報酬",
    "D+5 win": "D+5勝率",
    "phase_overheated": "TDCC過熱階段",
    "all_thresholds": "四級距同步過熱",
    "TDCC streak": "TDCC連續週數",
    "MACD hist >0": "MACD柱狀體>0",
    "MACD hist <=0": "MACD柱狀體<=0",
    "KD bullish not overheated": "KD多方未過熱",
    "KD overheated": "KD過熱",
    "1W return 10-30": "1週漲幅10-30",
    "1W return >30": "1週漲幅>30",
    "2W return 20-50": "2週漲幅20-50",
    "2W return >60": "2週漲幅>60",
    "BB width not extreme": "布林寬度不極端",
    "BB width extreme": "布林寬度極端",
    "near 23EMA/平台": "接近23EMA / 平台",
    "EMA23 slope proxy up": "23EMA斜率向上",
    "pullback entry zone": "回檔買點區",
    "pullback not volume-chasing": "非追量買點",
    "W low position": "W底位階",
    "W neckline distance": "距頸線",
    "pre-W base width": "W底前盤整寬度",
    "right-side volume support": "右側量能支撐",
    "second attack comparable to first": "第二段攻擊接近第一段",
    "second attack volume expansion": "第二段攻擊量能放大",
    "second attack red-body improvement": "第二段紅K比例改善",
    "1w": "1週",
    "2w": "2週",
    "3w": "3週",
    "4w": "4週",
    "strong_bull": "強多市場",
    "correction": "修正市場",
    "high_risk": "高風險市場",
}


@dataclass(frozen=True)
class ModelSpec:
    model_id: str
    model_name_zh: str
    pdf_visibility: str
    entry_basis: str
    main_conditions_zh: str
    add_score_zh: str
    forbidden_veto_zh: str
    operation_guidance_zh: str
    condition_func: Callable[[pd.Series], bool]
    score_func: Callable[[pd.Series], tuple[float, list[str], list[str]]]


def text(row: pd.Series, *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            if candidate in row.index:
                value = safe_str(row.get(candidate, ""))
                if value:
                    return value
    return ""


def num(row: pd.Series, *names: str) -> float:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            if candidate in row.index:
                value = to_number(row.get(candidate, ""))
                if not math.isnan(value):
                    return float(value)
    return math.nan


def has_cjk(value: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in safe_str(value))


def zh_or_pending(value: Any, mapping: dict[str, str] | None = None) -> str:
    raw = safe_str(value)
    if not raw:
        return ""
    if mapping and raw in mapping:
        return mapping[raw]
    if has_cjk(raw) and "_" not in raw:
        return raw
    return "欄位尚未完成"


def split_tags(value: Any) -> list[str]:
    raw = safe_str(value)
    if not raw:
        return []
    for sep in [";", ",", "/", "、"]:
        raw = raw.replace(sep, "|")
    return [part.strip() for part in raw.split("|") if part.strip()]


def zh_tag_list(value: Any, mapping: dict[str, str]) -> str:
    tags = split_tags(value)
    if not tags:
        return ""
    translated = []
    for tag in tags:
        translated.append(mapping.get(tag, tag if has_cjk(tag) and "_" not in tag else "欄位尚未完成"))
    return " | ".join(dict.fromkeys(translated))


def zh_text_or_pending(value: Any) -> str:
    raw = safe_str(value)
    if raw and has_cjk(raw):
        return raw
    return "欄位尚未完成 / 暫用現有資料"


def score_components_zh(value: Any) -> str:
    raw = safe_str(value)
    if not raw:
        return ""
    out = raw
    for src, dst in SCORE_COMPONENT_ZH_REPLACEMENTS.items():
        out = out.replace(src, dst)
    return out


def column_or_default(df: pd.DataFrame, name: str, default: str = "") -> pd.Series:
    if name in df.columns:
        return df[name].astype(str)
    return pd.Series([default] * len(df), index=df.index, dtype=str)


SAME_MODEL_REPEAT_STATUS_ZH = {
    "new_model_signal": "新進榜",
    "repeated_same_model_signal": "重複進榜",
}

FRONTPAGE_DUPLICATE_REASON_ZH = {
    "not_pdf_core_model": "非PDF核心模型",
    "same_model_repeat_moved_to_persistence_table": "同模型重複進榜，移至重複進榜表",
    "duplicate_stock_already_shown_on_frontpage": "首頁已列過同股票代表",
}


def same_model_repeat_status_zh(value: Any) -> str:
    raw = safe_str(value)
    if not raw:
        return ""
    return SAME_MODEL_REPEAT_STATUS_ZH.get(raw, "欄位尚未完成 / 暫用現有資料")


def same_model_repeat_note_zh(row: pd.Series) -> str:
    status = safe_str(row.get("same_model_repeat_status", ""))
    if status == "new_model_signal":
        return "本模型今日新進榜；用新進榜排名呈現。"
    if status == "repeated_same_model_signal":
        days = safe_str(row.get("same_model_consecutive_days", "")) or "0"
        count5 = safe_str(row.get("same_model_appear_count_5d", "")) or "0"
        count10 = safe_str(row.get("same_model_appear_count_10d", "")) or "0"
        return f"同模型連續{days}天；近5日{count5}次、近10日{count10}次；移至重複進榜表，不作扣分。"
    return "欄位尚未完成 / 暫用現有資料"


def add_same_model_repeat_display_and_ranks(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    required_cols = [
        "same_model_repeat_status_zh",
        "same_model_repeat_note_zh",
        "model_rank_overall",
        "model_rank_new_signal",
        "model_rank_repeated_signal",
        "display_rank_new_signal",
        "display_rank_repeated_signal",
    ]
    for col in required_cols:
        if col not in out.columns:
            out[col] = ""
    if out.empty:
        return out

    if "same_model_repeat_status" not in out.columns:
        out["same_model_repeat_status"] = ""
    out["same_model_repeat_status_zh"] = out["same_model_repeat_status"].map(same_model_repeat_status_zh)
    out["same_model_repeat_note_zh"] = out.apply(same_model_repeat_note_zh, axis=1)
    out["model_rank_overall"] = column_or_default(out, "model_rank")

    for col in ["model_rank_new_signal", "model_rank_repeated_signal", "display_rank_new_signal", "display_rank_repeated_signal"]:
        out[col] = ""

    out["_score_num"] = pd.to_numeric(out.get("model_score", ""), errors="coerce").fillna(-999999)
    out["_rank_num"] = pd.to_numeric(out.get("model_rank", ""), errors="coerce").fillna(999999)
    out["_consec_num"] = pd.to_numeric(out.get("same_model_consecutive_days", ""), errors="coerce").fillna(0)
    out["_count10_num"] = pd.to_numeric(out.get("same_model_appear_count_10d", ""), errors="coerce").fillna(0)
    out["_stock_id_sort"] = column_or_default(out, "stock_id")

    status = out["same_model_repeat_status"].astype(str)
    new_mask = status.eq("new_model_signal")
    repeated_mask = status.eq("repeated_same_model_signal")

    if new_mask.any():
        new_sorted = out[new_mask].sort_values(
            ["report_bucket", "model_id", "_score_num", "_rank_num", "_stock_id_sort"],
            ascending=[True, True, False, True, True],
        )
        ranks = new_sorted.groupby(["report_bucket", "model_id"], dropna=False).cumcount() + 1
        out.loc[new_sorted.index, "model_rank_new_signal"] = ranks.astype(str).values
        out.loc[new_sorted.index, "display_rank_new_signal"] = [f"新進榜#{int(rank)}" for rank in ranks]

    if repeated_mask.any():
        repeated_sorted = out[repeated_mask].sort_values(
            ["report_bucket", "model_id", "_consec_num", "_count10_num", "_score_num", "_rank_num", "_stock_id_sort"],
            ascending=[True, True, False, False, False, True, True],
        )
        ranks = repeated_sorted.groupby(["report_bucket", "model_id"], dropna=False).cumcount() + 1
        out.loc[repeated_sorted.index, "model_rank_repeated_signal"] = ranks.astype(str).values
        out.loc[repeated_sorted.index, "display_rank_repeated_signal"] = [f"重複榜#{int(rank)}" for rank in ranks]

    return out.drop(columns=["_score_num", "_rank_num", "_consec_num", "_count10_num", "_stock_id_sort"], errors="ignore")


def apply_display_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    out = df.copy()

    def preserve_existing_display(name: str, candidate: pd.Series) -> pd.Series:
        existing = column_or_default(out, name)
        usable = existing.astype(str).str.strip().ne("") & ~existing.astype(str).str.contains("欄位尚未完成", na=False)
        return existing.where(usable, candidate)

    out["report_bucket_zh"] = column_or_default(out, "report_bucket").map(REPORT_BUCKET_ZH).fillna("欄位尚未完成")
    source_category_zh = column_or_default(out, "original_category").map(CATEGORY_ZH)
    source_category_zh = source_category_zh.mask(source_category_zh.isna() | source_category_zh.eq(""), out.get("model_name_zh", ""))
    out["source_category_zh"] = source_category_zh.replace("", "欄位尚未完成").fillna("欄位尚未完成")
    primary = column_or_default(out, "effective_primary_theme")
    out["effective_primary_theme_zh"] = primary.map(lambda value: value if has_cjk(value) else zh_or_pending(value, STRUCTURAL_BUCKET_ZH))
    structural = column_or_default(out, "effective_structural_theme_bucket")
    out["effective_structural_theme_bucket_zh"] = structural.map(lambda value: zh_or_pending(value, STRUCTURAL_BUCKET_ZH))
    out["tdcc_status_zh"] = column_or_default(out, "tdcc_status").map(lambda value: zh_or_pending(value, TDCC_STATUS_ZH))
    out["warrant_flow_signal_zh"] = column_or_default(out, "warrant_flow_signal").map(lambda value: zh_or_pending(value, WARRANT_SIGNAL_ZH))
    out["risk_tags_zh"] = preserve_existing_display("risk_tags_zh", column_or_default(out, "risk_penalty_tags").map(lambda value: zh_tag_list(value, RISK_TAG_ZH)))
    out["downgrade_flags_zh"] = preserve_existing_display("downgrade_flags_zh", column_or_default(out, "downgrade_flags").map(lambda value: zh_tag_list(value, RISK_TAG_ZH)))
    out["next_confirmation_zh"] = preserve_existing_display("next_confirmation_zh", column_or_default(out, "next_confirmation").map(zh_text_or_pending))
    out["recommended_usage_zh"] = preserve_existing_display("recommended_usage_zh", column_or_default(out, "recommended_usage").map(zh_text_or_pending))
    out["why_selected_zh"] = preserve_existing_display("why_selected_zh", column_or_default(out, "why_selected").map(zh_text_or_pending))
    out["score_components_zh"] = column_or_default(out, "score_components").map(score_components_zh)
    out["same_model_repeat_status_zh"] = column_or_default(out, "same_model_repeat_status").map(same_model_repeat_status_zh)
    out["same_model_repeat_note_zh"] = out.apply(same_model_repeat_note_zh, axis=1)
    if "frontpage_duplicate_reason" in out.columns:
        out["frontpage_duplicate_reason_zh"] = column_or_default(out, "frontpage_duplicate_reason").map(
            lambda value: FRONTPAGE_DUPLICATE_REASON_ZH.get(safe_str(value), "")
        )
    if "merged_source_categories" in out.columns:
        out["merged_source_categories_zh"] = out["merged_source_categories"].map(lambda value: zh_tag_list(value, CATEGORY_ZH))
        out["source_hit_labels_zh"] = preserve_existing_display("source_hit_labels_zh", out["merged_source_categories_zh"])
    if "merged_risk_penalty_tags" in out.columns:
        out["merged_risk_penalty_tags_zh"] = out["merged_risk_penalty_tags"].map(lambda value: zh_tag_list(value, RISK_TAG_ZH))
        out["risk_tags_zh"] = out["merged_risk_penalty_tags_zh"].where(out["merged_risk_penalty_tags_zh"].astype(str).ne(""), out["risk_tags_zh"])
    display_defaults = {
        "risk_tags_zh": "未見重大風險標籤",
        "downgrade_flags_zh": "無明確降級旗標",
        "source_hit_labels_zh": "模型主條件",
        "next_confirmation_zh": "依量價、支撐壓力與籌碼變化追蹤",
        "recommended_usage_zh": "模型條件成立，依支撐壓力與風控管理",
        "why_selected_zh": "依模型主條件入選",
        "same_model_repeat_status_zh": "欄位尚未完成 / 暫用現有資料",
        "same_model_repeat_note_zh": "欄位尚未完成 / 暫用現有資料",
        "effective_primary_theme_zh": "未分類族群 / 暫用產業分類",
        "effective_structural_theme_bucket_zh": "未分類族群 / 暫用產業分類",
    }
    for col, default in display_defaults.items():
        text = column_or_default(out, col).astype(str).str.strip()
        out[col] = column_or_default(out, col).where(text.ne(""), default)
    return out


def tdcc_direction_from_changes(changes: list[float]) -> str:
    valid = [value for value in changes if not math.isnan(value)]
    if not valid:
        return "中性"
    positives = sum(1 for value in valid if value > 0)
    negatives = sum(1 for value in valid if value < 0)
    total = sum(valid)
    if positives >= 4 and total > 0:
        return "強正向"
    if positives >= 2 and total > 0:
        return "正向"
    if negatives >= 4 and total < 0:
        return "強負向"
    if negatives >= 2 and total < 0:
        return "負向"
    return "中性"


@lru_cache(maxsize=4096)
def latest_tdcc_summary(stock_id: str) -> dict[str, Any]:
    code = normalize_code(stock_id)
    path = TDCC_STOCK_HISTORY_DIR / f"{code}.csv"
    empty = {
        "tdcc_direction_zh": "中性",
        "tdcc_400_change": "",
        "tdcc_600_change": "",
        "tdcc_800_change": "",
        "tdcc_1000_change": "",
        "tdcc_big_holder_summary_zh": "TDCC資料不足 / 暫用現有資料",
        "tdcc_grade_change_summary_zh": "TDCC級距變化資料不足",
        "tdcc_risk_text_zh": "僅能觀察，不可單獨作為買進理由",
    }
    if not path.exists():
        return empty
    try:
        df = pd.read_csv(path, dtype={"stock_id": str})
    except Exception:
        return empty
    if df.empty:
        return empty
    df = df.sort_values("as_of_date")
    latest = df.iloc[-1]
    changes: list[float] = []
    labels: list[str] = []
    result = dict(empty)
    for threshold in ["400", "600", "800", "1000"]:
        col = f"over_{threshold}_change_1w"
        value = to_number(latest.get(col, math.nan))
        changes.append(value)
        result[f"tdcc_{threshold}_change"] = "" if math.isnan(value) else round(value, 4)
        if not math.isnan(value):
            direction = "增加" if value > 0 else "減少" if value < 0 else "持平"
            labels.append(f">{threshold}張{direction}{value:.2f}pct")
    direction = tdcc_direction_from_changes(changes)
    result["tdcc_direction_zh"] = direction
    result["tdcc_grade_change_summary_zh"] = "；".join(labels) if labels else "TDCC級距變化資料不足"
    if direction in {"強正向", "正向"}:
        result["tdcc_big_holder_summary_zh"] = f"大戶籌碼{direction}，但仍需搭配價格與量價確認。"
        result["tdcc_risk_text_zh"] = "TDCC為加分項，不可單獨作為買進理由。"
    elif direction in {"強負向", "負向"}:
        result["tdcc_big_holder_summary_zh"] = f"大戶籌碼{direction}，需降低追價與過度解讀。"
        result["tdcc_risk_text_zh"] = "TDCC轉弱，若價格同步跌破支撐需降級。"
    else:
        result["tdcc_big_holder_summary_zh"] = "大戶籌碼中性，需看價格、量能與族群。"
        result["tdcc_risk_text_zh"] = "籌碼未形成明確方向。"
    return result


def attach_report_contract_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    out = df.copy()
    out["report_line"] = column_or_default(out, "report_bucket")
    out["display_rank"] = column_or_default(out, "model_rank")
    out["source_hit_count"] = column_or_default(out, "merged_same_model_source_count", "1")
    out["source_hit_labels"] = column_or_default(out, "merged_source_categories")
    out["source_row_indices"] = column_or_default(out, "merged_source_row_indices")
    out["why_selected"] = column_or_default(out, "score_components")
    out["risk_tags"] = column_or_default(out, "merged_risk_penalty_tags")
    out["risk_tags"] = out["risk_tags"].where(out["risk_tags"].astype(str).ne(""), column_or_default(out, "risk_penalty_tags"))
    out["downgrade_flags"] = column_or_default(out, "risk_tags")
    out["recommended_usage_zh"] = column_or_default(out, "model_operation_guidance").map(zh_text_or_pending)
    out["why_selected_zh"] = column_or_default(out, "score_components_zh").map(zh_text_or_pending)
    out["next_confirmation_zh"] = column_or_default(out, "merged_next_confirmations").map(zh_text_or_pending)
    out["source_hit_labels_zh"] = column_or_default(out, "merged_source_categories_zh").map(zh_text_or_pending)
    out["downgrade_flags_zh"] = column_or_default(out, "merged_risk_penalty_tags_zh").map(lambda v: zh_text_or_pending(v) if safe_str(v) else "")

    tdcc_rows = [latest_tdcc_summary(stock_id) for stock_id in column_or_default(out, "stock_id")]
    tdcc_df = pd.DataFrame(tdcc_rows, index=out.index)
    for col in tdcc_df.columns:
        out[col] = tdcc_df[col]
    text_defaults = {
        "risk_tags_zh": "未見重大風險標籤",
        "downgrade_flags_zh": "無明確降級旗標",
        "source_hit_labels_zh": "模型主條件",
        "next_confirmation_zh": "依量價、支撐壓力與籌碼變化追蹤",
        "recommended_usage_zh": "模型條件成立，依支撐壓力與風控管理",
        "why_selected_zh": "依模型主條件入選",
    }
    for col, default in text_defaults.items():
        if col not in out.columns:
            out[col] = default
        else:
            text = out[col].astype(str).str.strip()
            out[col] = out[col].where(text.ne(""), default)
    return out


@lru_cache(maxsize=4096)
def price_history_for_stock(stock_id: str) -> pd.DataFrame:
    code = normalize_code(stock_id)
    if not code:
        return pd.DataFrame()
    path = STOCK_PRICE_HISTORY_DIR / f"{code}.csv"
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path, dtype={"stock_id": str})
    except Exception:
        return pd.DataFrame()
    required = {"date", "open", "high", "low", "close"}
    if not required.issubset(df.columns):
        return pd.DataFrame()
    df = df.copy()
    df["date"] = df["date"].astype(str)
    for col in ["open", "high", "low", "close", "volume"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date", "high", "low", "close"]).sort_values("date")
    return df


def truthy(value: Any) -> bool:
    return safe_str(value).strip().lower() in {"true", "1", "yes", "y", "t"}


def flag(row: pd.Series, name: str) -> bool:
    return truthy(row.get(name, ""))


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    if math.isnan(value):
        return low
    return max(low, min(high, value))


def pct_points(value: float, threshold: float, points: float, cap: float) -> float:
    if math.isnan(value) or value < threshold:
        return 0
    return min(cap, (value - threshold) * points)


def category(row: pd.Series) -> str:
    return text(row, "original_category", "category").lower()


def stage(row: pd.Series) -> str:
    return text(row, "pattern_stage", "pattern").lower()


def tdcc_status(row: pd.Series) -> str:
    return text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge").lower()


def warrant_signal(row: pd.Series) -> str:
    return text(row, "warrant_flow_signal", "warrant_status").lower()


def report_bucket(row: pd.Series) -> str:
    # Mainstream/non-mainstream is a report split only. It must not change score.
    buckets = report_buckets(row)
    return buckets[0] if buckets else "non_mainstream"


def report_buckets(row: pd.Series) -> list[str]:
    # A dual-membership stock can appear in both reports. This is a report split,
    # not a score cap, veto, or model condition.
    mainstream_eligible = truthy(text(row, "mainstream_report_eligible", "taxonomy_mainstream_report_eligible"))
    non_mainstream_eligible = truthy(text(row, "non_mainstream_report_eligible", "taxonomy_non_mainstream_report_eligible"))
    memberships_raw = text(row, "report_line_memberships", "taxonomy_report_line_memberships").lower()
    membership_tokens = {token.strip() for token in memberships_raw.replace(";", ",").replace("|", ",").split(",") if token.strip()}
    buckets: list[str] = []
    if mainstream_eligible or "mainstream" in membership_tokens:
        buckets.append("mainstream")
    if non_mainstream_eligible or "non_mainstream" in membership_tokens or "non-mainstream" in membership_tokens:
        buckets.append("non_mainstream")
    if buckets:
        return list(dict.fromkeys(buckets))

    bucket = text(row, "structural_theme_bucket", "taxonomy_structural_theme_bucket").lower()
    status = text(row, "theme_structural_status", "taxonomy_theme_structural_status").lower()
    group = text(row, "theme_group").lower()
    if bucket in CORE_AI_BUCKETS or status.startswith("core_mainstream") or group == "core_mainstream":
        return ["mainstream"]
    if status.startswith("non_mainstream") or group == "non_mainstream":
        return ["non_mainstream"]
    # No third report bucket. If taxonomy is incomplete, keep the stock visible
    # in the non-mainstream report and let taxonomy validation flag the source.
    return ["non_mainstream"]


def report_line_memberships_value(row: pd.Series) -> str:
    return "|".join(report_buckets(row))


def mainstream_report_eligible_value(row: pd.Series) -> str:
    return "True" if "mainstream" in report_buckets(row) else "False"


def non_mainstream_report_eligible_value(row: pd.Series) -> str:
    return "True" if "non_mainstream" in report_buckets(row) else "False"


def dual_report_membership_flag_value(row: pd.Series) -> str:
    buckets = report_buckets(row)
    return "True" if "mainstream" in buckets and "non_mainstream" in buckets else "False"


def primary_theme(row: pd.Series) -> str:
    candidates = [
        text(row, "effective_primary_theme", "primary_theme", "taxonomy_primary_theme"),
        text(row, "basic_theme", "taxonomy_basic_theme"),
        text(row, "細分族群", "theme_name", "industry"),
    ]
    for value in candidates:
        value = safe_str(value).strip()
        if value and value.lower() not in {"theme_unknown", "unclassified", "unknown", "other"}:
            return value
    return "未分類族群"


def has_hot_theme(row: pd.Series) -> bool:
    """Hot theme tags are the required gate for the hot-theme pullback model.

    Basic theme exists for every stock and is not enough for this model.
    A stock qualifies only when taxonomy provides at least one hot theme tag.
    """
    explicit = text(row, "has_hot_theme", "taxonomy_has_hot_theme").lower()
    if explicit in {"true", "1", "yes", "y"}:
        return True
    hot_fields = [
        "hot_primary_theme",
        "taxonomy_hot_primary_theme",
        "hot_secondary_themes",
        "taxonomy_hot_secondary_themes",
    ]
    return any(bool(text(row, field).strip()) for field in hot_fields)


def hot_theme_label(row: pd.Series) -> str:
    labels: list[str] = []
    for field in [
        "hot_primary_theme",
        "taxonomy_hot_primary_theme",
        "hot_secondary_themes",
        "taxonomy_hot_secondary_themes",
    ]:
        for tag in split_tags(text(row, field)):
            if tag and tag not in labels:
                labels.append(tag)
    return " | ".join(labels)


def effective_structural_theme_bucket(row: pd.Series) -> str:
    return text(
        row,
        "effective_structural_theme_bucket",
        "structural_theme_bucket",
        "taxonomy_structural_theme_bucket",
    )


def effective_mainstream_label(row: pd.Series) -> str:
    value = text(row, "effective_mainstream_label", "taxonomy_effective_mainstream_label", "theme_mainstream_label").lower()
    if value in {"core_mainstream", "non_mainstream", "both"}:
        return value
    return "non_mainstream"


def is_suspicious_text(value: str) -> bool:
    value = safe_str(value)
    if not value:
        return True
    question_marks = value.count("?")
    replacement_marks = value.count("\ufffd")
    return question_marks >= 6 or replacement_marks >= 2


def clean_next_confirmation(row: pd.Series, spec: ModelSpec) -> str:
    raw = text(row, "next_confirmation")
    if is_suspicious_text(raw):
        return spec.operation_guidance_zh
    return raw


def revenue_yoy(row: pd.Series) -> float:
    return num(row, "latest_revenue_yoy", "revenue_yoy_pct")


def revenue_cumulative_yoy(row: pd.Series) -> float:
    return num(row, "cumulative_revenue_yoy", "cumulative_yoy_pct")


def strong_revenue(row: pd.Series) -> bool:
    yoy = revenue_yoy(row)
    cum = revenue_cumulative_yoy(row)
    return (not math.isnan(yoy) and yoy >= 30) or (not math.isnan(cum) and cum >= 20)


def close_price(row: pd.Series) -> float:
    return num(row, "close")


def close_above_open(row: pd.Series) -> bool:
    close = close_price(row)
    open_ = num(row, "open")
    return not math.isnan(close) and not math.isnan(open_) and close > open_


def red_solid_candle(row: pd.Series) -> bool:
    close = close_price(row)
    open_ = num(row, "open")
    high = num(row, "high")
    low = num(row, "low")
    if any(math.isnan(v) for v in [close, open_, high, low]) or high <= low:
        return close_above_open(row)
    body_ratio = abs(close - open_) / (high - low)
    close_location = (close - low) / (high - low)
    upper_shadow = (high - max(close, open_)) / (high - low)
    return close > open_ and body_ratio >= 0.25 and close_location >= 0.65 and upper_shadow <= 0.35


def in_recent_range(row: pd.Series, tolerance_pct: float) -> bool:
    close = close_price(row)
    high = num(row, "high_20", "previous_20d_high", "platform_high")
    low = num(row, "low_20", "previous_20d_low", "platform_low")
    if any(math.isnan(v) for v in [close, high, low]) or high <= low:
        return False
    return low * (1 - tolerance_pct / 100) <= close <= high * (1 + tolerance_pct / 100)


def near_ema23_or_platform(row: pd.Series) -> bool:
    dist_ema = num(row, "distance_to_ema23_pct", "distance_23ema_pct", "gap_ema23_pct")
    if not math.isnan(dist_ema) and -2.5 <= dist_ema <= 5:
        return True
    close = close_price(row)
    high = num(row, "platform_high", "short_platform_high")
    low = num(row, "platform_low", "short_platform_low")
    if any(math.isnan(v) for v in [close, high, low]) or high <= low:
        return False
    return low * 0.97 <= close <= high * 1.03


def near_ema23_or_support(row: pd.Series) -> bool:
    """Pullback entry should be near 23EMA or support, not near range high."""
    dist_ema = num(row, "distance_to_ema23_pct", "distance_23ema_pct", "gap_ema23_pct")
    if not math.isnan(dist_ema) and -2.5 <= dist_ema <= 5:
        return True
    close = close_price(row)
    low = num(row, "platform_low", "short_platform_low", "previous_20d_low", "low_20")
    if math.isnan(close) or math.isnan(low) or low <= 0:
        return False
    return -2.0 <= (close / low - 1) * 100 <= 8.0


def ema23_slope_proxy_up(row: pd.Series) -> bool:
    if flag(row, "ma5_turning_up_flag") or flag(row, "ma10_turning_up_flag"):
        return True
    slope = num(row, "ema23_slope_pct", "ema23_slope")
    if not math.isnan(slope) and slope > 0:
        return True
    close = close_price(row)
    ema23 = num(row, "ema23")
    ma20 = num(row, "ma20")
    if not math.isnan(close) and not math.isnan(ema23) and close >= ema23:
        return True
    if not math.isnan(ema23) and not math.isnan(ma20) and ema23 >= ma20 * 0.98:
        return True
    return False


def near_range_high(row: pd.Series, pct: float = 5) -> bool:
    close = close_price(row)
    high = num(row, "platform_high", "short_platform_high", "previous_20d_high", "previous_high")
    if math.isnan(close) or math.isnan(high) or high <= 0:
        return False
    return -pct <= (close / high - 1) * 100 <= pct


def near_neckline_or_prior_high(row: pd.Series) -> bool:
    dist = num(row, "neckline_distance_pct", "distance_to_previous_high_pct", "distance_to_previous_60d_high_pct")
    return not math.isnan(dist) and 0 <= dist <= 5


def already_confirmed_breakout(row: pd.Series) -> bool:
    cat = category(row).lower()
    stage_raw = text(row, "pattern_stage")
    stage = stage_raw.lower()
    breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
    if cat in {"true_breakout", "strict_breakout"}:
        return True
    if stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}:
        return True
    if any(marker in stage_raw for marker in ["已突破", "突破確認", "平台突破", "頸線突破"]):
        return True
    if breakout_type in {
        "range_breakout_volume",
        "platform_volume_breakout",
        "neckline_volume_breakout",
        "strict_high_breakout",
        "strict_60d_volume_breakout",
        "true_breakout",
        "breakout",
    }:
        return True
    return (
        flag(row, "platform_breakout_flag")
        or flag(row, "neckline_breakout_flag")
        or flag(row, "volume_confirmed_breakout")
        or flag(row, "close_above_range_high")
        or flag(row, "close_above_previous_20d_high")
    )


def tdcc_positive(row: pd.Series) -> bool:
    status = tdcc_status(row)
    return status in POSITIVE_TDCC or flag(row, "tdcc_accumulation_signal")


def tdcc_distribution(row: pd.Series) -> bool:
    return tdcc_status(row) == "distribution_warning" or "tdcc_distribution_warning" in text(row, "downgrade_flags")


def model_score_common(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score = 50.0
    comps: list[str] = ["base=50"]
    risks: list[str] = []
    vol = num(row, "volume_ratio")
    if not math.isnan(vol):
        add = min(15, max(0, (vol - 1) * 4))
        score += add
        comps.append(f"volume_ratio:{vol:.2f}x +{add:.1f}")
    if tdcc_positive(row):
        score += 8
        comps.append("TDCC positive +8")
    if warrant_signal(row) in BULLISH_WARRANT:
        score += 6
        comps.append("warrant bullish +6")
    if strong_revenue(row):
        score += 6
        comps.append("revenue strong +6")
    off_low = num(row, "off_60d_low_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    if not math.isnan(off_low) and off_low <= 25:
        score += 5
        comps.append("lower position +5")
    if not math.isnan(ret20) and ret20 > 35:
        score -= 5
        risks.append("20d_return_high_score_penalty")
    if tdcc_distribution(row):
        score -= 8
        risks.append("tdcc_distribution_penalty")
    if flag(row, "false_breakout_risk"):
        score -= 8
        risks.append("false_breakout_risk_penalty")
    return score, comps, risks


def score_volume_breakout(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = model_score_common(row)
    if flag(row, "platform_breakout_flag") or flag(row, "neckline_breakout_flag"):
        score += 10
        comps.append("platform/neckline breakout +10")
    if flag(row, "breakout_close_near_high_flag"):
        score += 5
        comps.append("close near high +5")
    width = num(row, "platform_width_pct", "short_platform_width_pct")
    if not math.isnan(width) and 3 <= width <= 15:
        score += 5
        comps.append("clean base width +5")
    return score, comps, risks


def score_pullback(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = model_score_common(row)
    if near_ema23_or_platform(row):
        score += 10
        comps.append("near 23EMA/platform +10")
    if ema23_slope_proxy_up(row):
        score += 7
        comps.append("EMA23 slope proxy up +7")
    if flag(row, "pullback_entry_zone_flag"):
        score += 5
        comps.append("pullback entry zone +5")
    if num(row, "volume_ratio") < 1.2:
        score += 3
        comps.append("pullback not volume-chasing +3")
    return score, comps, risks


def score_hot_theme_pullback(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = model_score_common(row)
    labels = hot_theme_label(row)
    score += 12
    comps.append(f"hot theme tag +12:{labels or 'present'}")
    if near_ema23_or_support(row):
        score += 10
        comps.append("near 23EMA/support +10")
    if ema23_slope_proxy_up(row):
        score += 6
        comps.append("EMA23 slope proxy up +6")
    if flag(row, "pullback_entry_zone_flag"):
        score += 5
        comps.append("pullback entry zone +5")
    vol = num(row, "volume_ratio")
    if not math.isnan(vol) and vol < 1.2:
        score += 3
        comps.append("pullback volume not chasing +3")
    return score, comps, risks


def score_w_bottom(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = model_score_common(row)
    second_low_gap = num(row, "second_low_gap_pct")
    neckline_distance = num(row, "distance_to_neckline_pct")
    vol = num(row, "volume_ratio")
    attack1 = num(row, "attack1_gain_pct")
    attack2 = num(row, "attack2_gain_pct")
    vol2_vs_1 = num(row, "volume_ratio_2_vs_1")
    red_body2_vs_1 = num(row, "red_body_ratio_2_vs_1")
    context = detected_w_bottom_context(row)
    if context.get("available"):
        low_pos = context.get("w_bottom_low_position_pct")
        neck_dist = context.get("neckline_distance_pct")
        base_width = context.get("pre_base_width_pct")
        if isinstance(low_pos, (int, float)):
            comps.append(f"W low position:{low_pos:.1f}%")
        if isinstance(neck_dist, (int, float)):
            comps.append(f"W neckline distance:{neck_dist:.1f}%")
        if isinstance(base_width, (int, float)) and not math.isnan(base_width):
            comps.append(f"pre-W base width:{base_width:.1f}%")
        attack1 = float(context.get("attack1_gain_pct", math.nan))
        attack2 = float(context.get("attack2_gain_pct", math.nan))
        vol2_vs_1 = float(context.get("volume_ratio_2_vs_1", math.nan))
        red_body2_vs_1 = float(context.get("red_body_ratio_2_vs_1", math.nan))
    if not math.isnan(second_low_gap):
        if 0 <= second_low_gap <= 4:
            score += 8
            comps.append("second low higher and controlled +8")
        elif -1.5 <= second_low_gap < 0:
            score += 5
            comps.append("second low slight undercut +5")
        elif 4 < second_low_gap <= 8:
            score += 3
            comps.append("second low higher but stretched +3")
    if not math.isnan(neckline_distance):
        if -3 <= neckline_distance <= 0:
            score += 8
            comps.append("near neckline from below +8")
        elif 0 < neckline_distance <= 0.5:
            score += 5
            comps.append("neckline just reclaimed +5")
        elif -5 <= neckline_distance < -3:
            score += 3
            comps.append("approaching neckline +3")
    if not math.isnan(vol) and vol >= 1.2:
        add = min(5, (vol - 1.0) * 2)
        score += add
        comps.append(f"right-side volume support +{add:.1f}")
    if not math.isnan(attack1) and not math.isnan(attack2):
        if attack2 >= attack1 + 3 and attack2 >= attack1 * 1.25:
            score += 7
            comps.append("second attack materially stronger +7")
        elif attack2 >= attack1 * 0.9:
            score += 2
            comps.append("second attack comparable to first +2")
        else:
            score -= 4
            risks.append("second_attack_weaker_watch")
    if not math.isnan(vol2_vs_1):
        if vol2_vs_1 >= 1.5:
            score += 4
            comps.append("second attack volume expansion +4")
        elif vol2_vs_1 >= 1.2:
            score += 2
            comps.append("second attack volume mildly higher +2")
        elif vol2_vs_1 < 0.8:
            risks.append("second_attack_volume_not_confirmed")
    if not math.isnan(red_body2_vs_1) and red_body2_vs_1 >= 1.2:
        score += 3
        comps.append("second attack red-body improvement +3")
    return score, comps, risks


def cond_volume_breakout(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
    range_breakout_type = breakout_type in {
        "range_breakout_volume",
        "platform_volume_breakout",
        "neckline_volume_breakout",
        "strict_60d_volume_breakout",
        "true_breakout",
        "breakout",
    }
    range_breakout_flag = flag(row, "platform_breakout_flag") or flag(row, "neckline_breakout_flag") or flag(row, "volume_confirmed_breakout")
    return not math.isnan(vol) and vol >= 1.5 and (range_breakout_type or range_breakout_flag)


def cond_pullback(row: pd.Series) -> bool:
    return near_ema23_or_support(row) and ema23_slope_proxy_up(row)


def cond_hot_theme_pullback(row: pd.Series) -> bool:
    # Key distinction from price_pullback_23ema:
    # hot theme tag + pullback near 23EMA/support is sufficient.
    # Revenue is only an add-score component, never a gate.
    return has_hot_theme(row) and near_ema23_or_support(row)


def cond_revenue_unreacted(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    ret5 = num(row, "return_5d", "return_5d_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    active_attack = cond_volume_breakout(row) or flag(row, "volume_confirmed_breakout")
    if not math.isnan(vol) and vol >= 2.5:
        active_attack = True
    if not math.isnan(ret5) and ret5 >= 8:
        active_attack = True
    if not math.isnan(ret20) and ret20 >= 20:
        active_attack = True
    return strong_revenue(row) and in_recent_range(row, 5) and not active_attack


def explicit_w_bottom_context_ok(row: pd.Series) -> bool:
    """Validate that a W-bottom is a low/base structure, not a high-level pullback."""
    low_position = num(row, "w_bottom_low_position_pct", "double_bottom_low_position_pct")
    base_width = num(row, "w_bottom_base_width_pct", "double_bottom_base_width_pct")
    if math.isnan(base_width):
        base_width = num(row, "platform_width_pct", "short_platform_width_pct")

    base_ok = not math.isnan(base_width) and base_width <= 35.0

    ret20 = num(row, "return_20d", "return_20d_pct")
    ret60 = num(row, "return_60d", "return_60d_pct")
    high_distance = num(row, "distance_to_previous_60d_high_pct", "distance_to_high_60_pct")
    not_extended = True
    if not math.isnan(ret20) and ret20 > 35:
        not_extended = False
    if not math.isnan(ret60) and ret60 > 70:
        not_extended = False
    if not math.isnan(high_distance) and high_distance >= -1:
        not_extended = False

    return base_ok and not_extended


def w_bottom_attack_confirmation_ok(row: pd.Series, context: dict[str, float | str | bool] | None = None) -> bool:
    """Require a real right-side attack, without making strength a hard veto.

    The W-bottom label should be controlled by geometry, base quality and
    neckline proximity. Second-leg strength is a ranking feature: a second
    attack that is only comparable to the first is still a valid W candidate,
    but receives a lower score than a clearly stronger second leg.
    """
    attack1 = num(row, "attack1_gain_pct")
    attack2 = num(row, "attack2_gain_pct")
    vol2_vs_1 = num(row, "volume_ratio_2_vs_1")
    red_body2_vs_1 = num(row, "red_body_ratio_2_vs_1")

    if context:
        # When price history is available, trust the detected two legs rather
        # than broad upstream pattern columns.  Otherwise a low-base or
        # post-rally pullback can inherit stale explicit W metrics and pass.
        attack1 = float(context.get("attack1_gain_pct", math.nan))
        attack2 = float(context.get("attack2_gain_pct", math.nan))
        vol2_vs_1 = float(context.get("volume_ratio_2_vs_1", math.nan))
        red_body2_vs_1 = float(context.get("red_body_ratio_2_vs_1", math.nan))

    if math.isnan(attack1) or math.isnan(attack2):
        return False

    price_leg_ok = attack2 >= 6.0 and attack2 >= attack1 * 0.85
    volume_ok = not math.isnan(vol2_vs_1) and vol2_vs_1 >= 1.2
    body_ok = not math.isnan(red_body2_vs_1) and red_body2_vs_1 >= 1.0
    return price_leg_ok and (volume_ok or body_ok)


def detected_w_bottom_context(row: pd.Series) -> dict[str, float | str | bool]:
    """Infer current W-bottom context from price history.

    This is intentionally conservative. Broad upstream pattern flags are not
    enough: the two lows must be close in height, formed in the lower part of
    the recent range, preceded by a base-like stretch, and the latest price
    must not already be far above the neckline.
    """
    stock_id = text(row, "stock_id")
    df = price_history_for_stock(stock_id)
    if df.empty or len(df) < 80:
        return {"available": False}

    date = text(row, "signal_date", "as_of_date", "date")
    if date:
        dated = df[df["date"] <= date]
        if len(dated) >= 80:
            df = dated
    df = df.tail(120).reset_index(drop=True)
    if len(df) < 80:
        return {"available": False}

    high_120 = float(df["high"].max())
    low_120 = float(df["low"].min())
    if high_120 <= low_120:
        return {"available": False}
    range_span = high_120 - low_120
    current_close = float(df["close"].iloc[-1])

    troughs: list[int] = []
    for idx in range(3, len(df) - 3):
        local = df["low"].iloc[idx - 3 : idx + 4]
        if float(df["low"].iloc[idx]) <= float(local.min()) * 1.002:
            troughs.append(idx)

    best: dict[str, float | str | bool] | None = None
    for left in troughs:
        for right in troughs:
            if right <= left:
                continue
            separation = right - left
            if separation < 8 or separation > 60:
                continue
            # The setup is intended to catch a current right-side W-bottom
            # candidate. Very old right troughs are stale base history and
            # should not keep a stock in the W-bottom model today.
            right_age = len(df) - 1 - right
            if right_age > 45:
                continue
            low_left = float(df["low"].iloc[left])
            low_right = float(df["low"].iloc[right])
            second_low_gap = (low_right / low_left - 1) * 100
            if second_low_gap < 0 or second_low_gap > 4:
                continue
            middle = df.iloc[left : right + 1]
            neckline_idx = int(middle["high"].idxmax())
            # A real W needs a rebound between the two troughs. If the highest
            # point is sitting on either trough edge, this is usually a drift,
            # low-base, or post-rally pullback rather than a double bottom.
            if neckline_idx <= left + 1 or neckline_idx >= right - 1:
                continue
            neckline = float(df["high"].iloc[neckline_idx])
            if neckline <= min(low_left, low_right):
                continue
            depth = (neckline / min(low_left, low_right) - 1) * 100
            if depth < 8:
                continue
            depth_left = (neckline / low_left - 1) * 100
            depth_right = (neckline / low_right - 1) * 100
            if min(depth_left, depth_right) < 6:
                continue

            low_left_position = (low_left - low_120) / range_span * 100
            low_right_position = (low_right - low_120) / range_span * 100
            lows_in_lower_base = low_left_position <= 35 and low_right_position <= 35

            pre_base = df.iloc[max(0, left - 30) : left]
            pre_base_ok = False
            pre_width = math.nan
            pre_return = math.nan
            if len(pre_base) >= 8:
                pre_low = float(pre_base["low"].min())
                pre_high = float(pre_base["high"].max())
                if pre_low > 0:
                    pre_width = (pre_high / pre_low - 1) * 100
                first_close = float(pre_base["close"].iloc[0])
                last_close = float(pre_base["close"].iloc[-1])
                if first_close > 0:
                    pre_return = (last_close / first_close - 1) * 100
                pre_base_ok = (math.isnan(pre_width) or pre_width <= 35) and (math.isnan(pre_return) or abs(pre_return) <= 25)

            current_to_neckline = (current_close / neckline - 1) * 100
            close_position = (current_close - low_120) / range_span * 100
            attack1_gain = (neckline / low_left - 1) * 100
            attack2_gain = (current_close / low_right - 1) * 100
            attack1_slice = df.iloc[left : min(right, left + 8)]
            attack2_slice = df.iloc[right : min(len(df), right + 8)]
            vol2_vs_1 = math.nan
            red_body2_vs_1 = math.nan
            if "volume" in df.columns and len(attack1_slice) >= 3 and len(attack2_slice) >= 3:
                vol1 = float(attack1_slice["volume"].mean())
                vol2 = float(attack2_slice["volume"].mean())
                if vol1 > 0:
                    vol2_vs_1 = vol2 / vol1
            if len(attack1_slice) >= 3 and len(attack2_slice) >= 3:
                red1 = int((attack1_slice["close"] > attack1_slice["open"]).sum())
                red2 = int((attack2_slice["close"] > attack2_slice["open"]).sum())
                if red1 > 0:
                    red_body2_vs_1 = red2 / red1
                elif red2 > 0:
                    red_body2_vs_1 = float("inf")
            not_extended = -5 <= current_to_neckline <= 5 and close_position <= 65
            # Low position is a score/ranking feature, not an absolute gate.
            # The W label itself is controlled by geometry, base quality,
            # neckline proximity, and right-side attack confirmation.
            context_ok = pre_base_ok and not_extended
            candidate: dict[str, float | str | bool] = {
                "available": True,
                "context_ok": context_ok,
                "second_low_gap_pct": second_low_gap,
                "neckline_distance_pct": current_to_neckline,
                "w_bottom_low_position_pct": max(low_left_position, low_right_position),
                "pre_base_width_pct": pre_width,
                "pre_base_return_pct": pre_return,
                "close_position_pct": close_position,
                "lows_in_lower_base": lows_in_lower_base,
                "attack1_gain_pct": attack1_gain,
                "attack2_gain_pct": attack2_gain,
                "depth_left_pct": depth_left,
                "depth_right_pct": depth_right,
                "volume_ratio_2_vs_1": vol2_vs_1,
                "red_body_ratio_2_vs_1": red_body2_vs_1,
                "left_low_date": str(df["date"].iloc[left]),
                "neckline_date": str(df["date"].iloc[neckline_idx]),
                "right_low_date": str(df["date"].iloc[right]),
                "right_low_age_days": right_age,
            }
            if best is None:
                best = candidate
            else:
                candidate_distance = abs(float(candidate["neckline_distance_pct"]))
                best_distance = abs(float(best["neckline_distance_pct"]))
                candidate_volume = float(candidate.get("volume_ratio_2_vs_1", math.nan))
                best_volume = float(best.get("volume_ratio_2_vs_1", math.nan))
                candidate_right = right
                best_date = str(best.get("right_low_date", ""))
                best_right_matches = df.index[df["date"].astype(str).eq(best_date)].tolist()
                best_right = int(best_right_matches[0]) if best_right_matches else -1
                # Prefer the more recent right trough when neckline distance is
                # effectively the same. This avoids choosing an early pullback
                # inside the middle of the W instead of the actual right low.
                if (
                    candidate_distance < best_distance - 0.25
                    or (abs(candidate_distance - best_distance) <= 0.25 and candidate_right > best_right)
                    or (
                        abs(candidate_distance - best_distance) <= 0.25
                        and candidate_right == best_right
                        and not math.isnan(candidate_volume)
                        and (math.isnan(best_volume) or candidate_volume > best_volume)
                    )
                ):
                    best = candidate

    if best is None:
        return {"available": True, "context_ok": False}
    return best


def double_bottom_structure_ok(row: pd.Series) -> bool:
    """Require actual double-bottom geometry, not only a broad pattern flag."""
    current_stage = stage(row)
    if current_stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}:
        return False
    second_low_gap = num(row, "second_low_gap_pct")
    neckline_distance = num(row, "distance_to_neckline_pct")

    price_context = detected_w_bottom_context(row)
    if math.isnan(second_low_gap) and price_context.get("available"):
        second_low_gap = float(price_context.get("second_low_gap_pct", math.nan))
    if math.isnan(neckline_distance) and price_context.get("available"):
        neckline_distance = float(price_context.get("neckline_distance_pct", math.nan))
    if math.isnan(second_low_gap) or math.isnan(neckline_distance):
        return False
    # W-bottom right side means two similar troughs in a low/base context. If
    # the right low is far higher than the left low, it is usually a pullback
    # after a prior advance, not a bottoming W.
    second_low_ok = 0.0 <= second_low_gap <= 4.0
    neckline_ok = -5.0 <= neckline_distance <= 1.0
    if not (second_low_ok and neckline_ok):
        return False

    attack_ok = w_bottom_attack_confirmation_ok(row, price_context if price_context.get("available") else None)
    if price_context.get("available"):
        return bool(price_context.get("context_ok")) and attack_ok

    return explicit_w_bottom_context_ok(row) and attack_ok


def cond_w_bottom_right(row: pd.Series) -> bool:
    if already_confirmed_breakout(row):
        return False
    return double_bottom_structure_ok(row)


def cond_neckline_challenge(row: pd.Series) -> bool:
    if already_confirmed_breakout(row):
        return False
    vol = num(row, "volume_ratio")
    return near_neckline_or_prior_high(row) and not math.isnan(vol) and vol >= 1.2 and ema23_slope_proxy_up(row)


def cond_platform_strength(row: pd.Series) -> bool:
    if already_confirmed_breakout(row):
        return False
    width = num(row, "platform_width_pct", "short_platform_width_pct")
    vol = num(row, "volume_ratio")
    return (
        (flag(row, "platform_base_flag") or not math.isnan(width))
        and (math.isnan(width) or width <= 18)
        and near_range_high(row, 5)
        and not math.isnan(vol)
        and vol >= 1.2
        and red_solid_candle(row)
    )


def cond_pullback_short_strength(row: pd.Series) -> bool:
    ret20 = num(row, "return_20d", "return_20d_pct")
    return (
        not math.isnan(ret20)
        and ret20 >= 5
        and (flag(row, "pullback_entry_zone_flag") or flag(row, "pullback_right_side_flag") or flag(row, "ma20_reclaim_setup_flag"))
        and ema23_slope_proxy_up(row)
    )


def cond_tdcc_stealth(row: pd.Series) -> bool:
    phase = text(row, "tdcc_price_phase").lower()
    vol = num(row, "volume_ratio")
    ret5 = num(row, "return_5d", "return_5d_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
        return False
    if cond_volume_breakout(row) or flag(row, "volume_confirmed_breakout"):
        return False
    if not math.isnan(vol) and vol >= 2.5:
        return False
    phase_ok = phase == "tdcc_leading_price" or (not phase and tdcc_positive(row))
    short_not_attacked = math.isnan(ret5) or ret5 < 8
    not_rallied = math.isnan(ret20) or ret20 < 20
    return phase_ok and short_not_attacked and not_rallied and in_recent_range(row, 10)


def build_specs() -> list[ModelSpec]:
    return [
        ModelSpec(
            "volume_range_breakout",
            "帶量突破模型",
            "pdf_core_model",
            "signal_date_next_open",
            "量比 >= 1.5，且股價有效突破近期盤整區間 / 平台上緣 / 壓力區。",
            "突破前高或平台、收盤站上突破區、量比越高、盤整時間越久、TDCC越好、營收越好、位階越低可加分。",
            "不得用漲幅過大、中位爆量、高位爆量直接否決；風險只作排名與操作提醒。",
            "以訊號日隔天開盤為進場原點；跌回突破區、爆量長上影或跌破支撐為退出/降風險條件。",
            cond_volume_breakout,
            score_volume_breakout,
        ),
        ModelSpec(
            "price_pullback_23ema",
            "股價回檔模型",
            "pdf_core_model",
            "signal_date_next_open",
            "股價回到23EMA或平台附近，且23EMA斜率向上。",
            "營收YoY或累計YoY強、未跌破23EMA、TDCC增加、有族群定義、回檔量縮、權證偏多可加分。",
            "不得因尚未突破直接否決；本模型目的就是在回檔區找買點。",
            "回測23EMA或平台不破可建立部位；跌破23EMA後站不回或放量破平台需退出/降風險。",
            cond_pullback,
            score_pullback,
        ),
        ModelSpec(
            "hot_theme_pullback",
            "熱門族群回檔模型",
            "pdf_core_model",
            "signal_date_next_open",
            "具備熱門族群標籤，且股價回到23EMA或支撐附近。營收不是必要條件。",
            "熱門族群標籤、接近23EMA/支撐、23EMA斜率向上、回檔量縮、TDCC正向、權證偏多、營收強可加分。",
            "不可因營收尚未確認或尚未突破而否決；營收只作加減分，風險只作排名與操作管理。",
            "用來抓熱門題材股回檔買點；先看23EMA/支撐是否守住，再用TDCC、權證、量價與營收作排序。",
            cond_hot_theme_pullback,
            score_hot_theme_pullback,
        ),
        ModelSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "pdf_core_model",
            "signal_date_next_open",
            "營收YoY或累計YoY強，且目前股價位於23日盤整區間內。",
            "接近平台突破、TDCC溫和增加、EPS/毛利確認、新聞利多或轉型題材可加分。",
            "不得只因尚未突破否決；但營收未經獲利品質確認時應降低排名或標示風險。",
            "用來尋找營收已改善但價格尚未完全反應的股票；突破平台或量價轉強是後續加碼/確認條件。",
            cond_revenue_unreacted,
            model_score_common,
        ),
        ModelSpec(
            "w_bottom_right_side",
            "W底右側模型",
            "pdf_core_model",
            "signal_date_next_open",
            "W底幾何成立，右側低點墊高但不能高太多，且接近頸線。",
            "第二段攻擊量大於第一段、第二段紅K比例提高、TDCC改善、接近頸線、低位階可加分。",
            "已確認突破或左低右高過大者不可歸為W底；那更像趨勢回檔或突破後整理。",
            "用於提前觀察頸線突破前的右側型態；突破頸線且量價確認後才升級為突破類。",
            cond_w_bottom_right,
            score_w_bottom,
        ),
        ModelSpec(
            "near_high_neckline_challenge",
            "接近前高 / 頸線挑戰模型",
            "pdf_core_model",
            "signal_date_next_open",
            "距前高或頸線0%到5%，量能開始放大，均線轉正。",
            "提前1到5日抓突破前觀察；TDCC、權證、族群、量能擴張可加分。",
            "已有效突破者不應留在本模型，應移至帶量突破或嚴格突破。",
            "用於觀察即將挑戰壓力的股票；若隔日突破且收盤站上，轉入突破模型。",
            cond_neckline_challenge,
            model_score_common,
        ),
        ModelSpec(
            "platform_strengthening",
            "平台整理轉強模型",
            "pdf_core_model",
            "signal_date_next_open",
            "盤整區間形成、波動收斂、接近上緣、量能回升，且出現帶量實體紅K。",
            "盤整時間長、回測不破、TDCC溫和增加、族群同步轉強可加分。",
            "已明確突破者不應留在平台整理轉強，應改歸帶量突破。",
            "用於平台內轉強觀察；突破上緣後才轉入突破模型。",
            cond_platform_strength,
            model_score_common,
        ),
        ModelSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "pdf_core_model",
            "signal_date_next_open",
            "前面有漲勢，回檔未破結構，重新站回23EMA。",
            "回檔量縮、再攻量增、MACD/KD轉強、TDCC或權證支持可加分。",
            "結構已破壞者不得納入。",
            "用於抓回檔後恢復動能的股票；若再跌破23EMA且站不回需退出/降風險。",
            cond_pullback_short_strength,
            model_score_common,
        ),
        ModelSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "pdf_core_model",
            "signal_date_next_open",
            "TDCC連續增加，股價尚未大漲，股價位於近期盤整區間，且屬tdcc_leading_price或近似狀態。",
            "高級距同步增加、族群也有擴散、TDCC與股價開始確認可加分。",
            "price_leading_tdcc與overheated_after_tdcc不可混入潛伏吸籌模型。",
            "用於突破前尋找籌碼先行但價格尚未完全反應的股票；帶量突破後應轉入突破模型。",
            cond_tdcc_stealth,
            model_score_common,
        ),
    ]

def build_parameter_table(specs: list[ModelSpec]) -> pd.DataFrame:
    rows = [
        {
            "model_id": spec.model_id,
            "model_name_zh": spec.model_name_zh,
            "pdf_visibility": spec.pdf_visibility,
            "entry_basis": spec.entry_basis,
            "main_conditions": spec.main_conditions_zh,
            "add_score_items": spec.add_score_zh,
            "forbidden_veto": spec.forbidden_veto_zh,
            "operation_guidance": spec.operation_guidance_zh,
            "parameter_status": "initial_program_rule_pending_backtest_optimization",
        }
        for spec in specs
    ]
    rows.extend(
        [
            {
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_name_zh": "TDCC短線延續模型 D+5/D+10",
                "pdf_visibility": "pdf_specialty_section",
                "entry_basis": "signal_date_next_open",
                "main_conditions": "all_thresholds_overheated或phase_overheated_after_tdcc，搭配MACD/KD/Bollinger與1W/2W漲幅條件。",
                "add_score_items": "D+1到D+10 next-open close/high統計、樣本數、相對報酬、market regime分層。",
                "forbidden_veto": "不是低位買進模型，不可混入TDCC潛伏吸籌。",
                "operation_guidance": "隔日開盤為進場原點；依D+1到D+10收盤/最高價統計做短線延續檢查。",
                "parameter_status": "research_reporting_only",
            },
            {
                "model_id": "short_term_surge_d5_d10",
                "model_name_zh": "短線急漲D+5/D+10模型",
                "pdf_visibility": "research_only_not_pdf_core",
                "entry_basis": "signal_date_next_open",
                "main_conditions": "5日或10日漲幅達標、量能擴張、技術動能強。",
                "add_score_items": "D+1到D+20 close/high統計、處置/注意標籤、TDCC與市場狀態分層。",
                "forbidden_veto": "不得稱為周線K；必須標清楚單位與進場原點。",
                "operation_guidance": "隔日開盤為進場原點；依D+1到D+20收盤/最高價統計檢查短線延續。",
                "parameter_status": "research_reporting_only",
            },
            {
                "model_id": "group_fund_rotation",
                "model_name_zh": "族群資金輪動模型",
                "pdf_visibility": "pdf_end_section_theme_only",
                "entry_basis": "not_stock_entry_signal",
                "main_conditions": "有基本族群或熱門族群標籤，且同族群超過1/3股票量比>=3。",
                "add_score_items": "族群出量比例、出量股票數、15-30日緩慢增量、龍頭/老二/老三擴散狀態。",
                "forbidden_veto": "不適用；這是族群資金流向預判，不是個股買進模型。",
                "operation_guidance": "只判斷族群資金是否擴散；同時保留基本族群與熱門族群兩種視角。",
                "parameter_status": "initial_program_rule_pending_backtest_optimization",
            },
            {
                "model_id": "explosive_volume_red_candle",
                "model_name_zh": "爆天量紅K模型",
                "pdf_visibility": "research_only_not_pdf_core",
                "entry_basis": "signal_date_next_open",
                "main_conditions": "月均量3倍/5倍/10倍、實體紅K、上影線小、收盤接近日高，另分低位爆量。",
                "add_score_items": "位階、主流族群、TDCC、市場狀態。",
                "forbidden_veto": "尚未納入精華PDF核心模型，需先回測參數。",
                "operation_guidance": "研究用；用隔日開盤為原點回測，不作當日PDF核心推薦。",
                "parameter_status": "research_backtest_required",
            },
            {
                "model_id": "five_day_20pct_precursor",
                "model_name_zh": "一週內上漲20%前兆模型",
                "pdf_visibility": "research_only_not_pdf_core",
                "entry_basis": "signal_date_next_open",
                "main_conditions": "歷史5日內高低點漲幅>=20%的樣本反推前一天與第一天條件。",
                "add_score_items": "量能、技術、TDCC、族群、market regime辨別度。",
                "forbidden_veto": "研究模型，不直接當每日PDF核心入選模型。",
                "operation_guidance": "研究用；先找前兆，再用全市場資料測辨別度。",
                "parameter_status": "research_backtest_required",
            },
            {
                "model_id": "disposition_attention_event_tag",
                "model_name_zh": "處置/注意股事件標籤",
                "pdf_visibility": "pdf_risk_tag_only",
                "entry_basis": "tag_only",
                "main_conditions": "處置、注意、分盤等交易事件。",
                "add_score_items": "檢查是否影響隔日開盤進場與D+5/D+10勝率。",
                "forbidden_veto": "不是買進模型，只做事件/風險標籤。",
                "operation_guidance": "事件標籤；只影響風險提示與回測分層。",
                "parameter_status": "daily_snapshot_accumulation_required",
            },
            {
                "model_id": "msci_event_tag",
                "model_name_zh": "MSCI事件標籤",
                "pdf_visibility": "pdf_event_tag_only",
                "entry_basis": "effective_date_next_open",
                "main_conditions": "MSCI新增或剔除。",
                "add_score_items": "1W/2W/3W/4W收盤報酬統計。",
                "forbidden_veto": "不是一般買進模型，先當事件標籤。",
                "operation_guidance": "事件標籤；以生效日後隔天開盤為原點做事件回測。",
                "parameter_status": "event_dataset_required",
            },
        ]
    )
    out = pd.DataFrame(rows)
    if not out.empty:
        out.loc[out["model_id"].eq("short_term_surge_d5_d10"), "pdf_visibility"] = "research_only_not_pdf_core"
    return out


def load_model_recommendations() -> pd.DataFrame:
    recs = read_csv(MODEL_PARAMETER_RECOMMENDATIONS, dtype=str, keep_default_na=False)
    if recs.empty or "model_id" not in recs.columns:
        return pd.DataFrame(columns=["model_id", *RECOMMENDATION_COLUMNS])

    work = recs.copy()
    usage_order = {
        "promote_to_pdf_core": 1,
        "pdf_secondary_watch": 2,
        "score_component_only": 3,
        "intraday_target_watch": 4,
        "research_only": 9,
    }
    work["_usage_order"] = work.get("recommended_usage", "").map(usage_order).fillna(8)
    work["_avg_close"] = pd.to_numeric(work.get("best_avg_close_return_pct", ""), errors="coerce").fillna(-999)
    work["_win_close"] = pd.to_numeric(work.get("best_close_win_rate_pct", ""), errors="coerce").fillna(-999)
    work["_sample"] = pd.to_numeric(work.get("selected_stock_days", ""), errors="coerce").fillna(0)
    work = work.sort_values(
        ["model_id", "_usage_order", "_avg_close", "_win_close", "_sample"],
        ascending=[True, True, False, False, False],
    )
    best = work.groupby("model_id", as_index=False).head(1).copy()
    rename = {
        "selected_stock_days": "recommended_sample_size",
        "selected_unique_stocks": "recommended_unique_stocks",
        "sample_status": "recommended_sample_status",
    }
    best = best.rename(columns=rename)
    keep = ["model_id", *RECOMMENDATION_COLUMNS]
    for col in keep:
        if col not in best.columns:
            best[col] = ""
    return best[keep].reset_index(drop=True)


def attach_model_recommendations(signals: pd.DataFrame, recommendations: pd.DataFrame) -> pd.DataFrame:
    if signals.empty:
        for col in RECOMMENDATION_COLUMNS:
            signals[col] = ""
        return signals
    if recommendations.empty:
        out = signals.copy()
        for col in RECOMMENDATION_COLUMNS:
            out[col] = ""
        return out
    out = signals.merge(recommendations, on="model_id", how="left")
    for col in RECOMMENDATION_COLUMNS:
        if col not in out.columns:
            out[col] = ""
        out[col] = out[col].fillna("")
    return out


def _join_unique(values: pd.Series) -> str:
    seen: list[str] = []
    for value in values:
        item = safe_str(value)
        if item and item not in seen:
            seen.append(item)
    return " | ".join(seen)


def annotate_frontpage_uniqueness(signals: pd.DataFrame) -> pd.DataFrame:
    """Mark one representative row per stock/bucket for front-page rendering.

    Full model signals intentionally keep one row per stock per model. The front
    page needs a separate uniqueness contract so a multi-model hit does not look
    like three different recommendations. Same-model repeat appearances are also
    intentionally excluded from the front-page table; they are persistence
    signals, not score penalties, and belong in daily_candidate_same_model_repeat.
    """

    if signals.empty:
        out = signals.copy()
        out["frontpage_display_allowed"] = ""
        out["frontpage_duplicate_reason"] = ""
        out["frontpage_duplicate_reason_zh"] = ""
        return out

    out = signals.copy()
    out["frontpage_display_allowed"] = "False"
    out["frontpage_duplicate_reason"] = "not_pdf_core_model"
    out["_score_num"] = pd.to_numeric(out.get("model_score", ""), errors="coerce").fillna(-999)
    out["_rank_num"] = pd.to_numeric(out.get("model_rank", ""), errors="coerce").fillna(999999)

    repeat_status = out.get("same_model_repeat_status", pd.Series("", index=out.index)).astype(str)
    repeat_mask = repeat_status.eq("repeated_same_model_signal")
    out.loc[repeat_mask, "frontpage_duplicate_reason"] = "same_model_repeat_moved_to_persistence_table"

    core_mask = out.get("model_group", "").astype(str).eq("pdf_core_model") & ~repeat_mask
    core = out[core_mask].sort_values(
        ["report_bucket", "stock_id", "_score_num", "_rank_num", "model_id"],
        ascending=[True, True, False, True, True],
    )
    allowed_idx = core.drop_duplicates(["report_bucket", "stock_id"], keep="first").index
    duplicate_idx = core.index.difference(allowed_idx)

    out.loc[core.index, "frontpage_duplicate_reason"] = ""
    out.loc[allowed_idx, "frontpage_display_allowed"] = "True"
    out.loc[duplicate_idx, "frontpage_duplicate_reason"] = "duplicate_stock_already_shown_on_frontpage"
    out["frontpage_duplicate_reason_zh"] = out["frontpage_duplicate_reason"].map(
        lambda value: FRONTPAGE_DUPLICATE_REASON_ZH.get(safe_str(value), "")
    )
    return out.drop(columns=["_score_num", "_rank_num"])


def build_frontpage_unique(signals: pd.DataFrame) -> pd.DataFrame:
    if signals.empty:
        return pd.DataFrame()

    work = signals[signals.get("model_group", "").astype(str).eq("pdf_core_model")].copy()
    if "same_model_repeat_status" in work.columns:
        work = work[work["same_model_repeat_status"].astype(str).ne("repeated_same_model_signal")].copy()
    if work.empty:
        return pd.DataFrame()
    work["_score_num"] = pd.to_numeric(work.get("model_score", ""), errors="coerce").fillna(-999)
    work["_rank_num"] = pd.to_numeric(work.get("model_rank", ""), errors="coerce").fillna(999999)
    work = work.sort_values(
        ["report_bucket", "stock_id", "_score_num", "_rank_num", "model_id"],
        ascending=[True, True, False, True, True],
    )

    rows: list[dict[str, Any]] = []
    for (bucket, stock_id), part in work.groupby(["report_bucket", "stock_id"], dropna=False):
        top = part.iloc[0]
        rows.append(
            {
                "signal_date": text(top, "signal_date"),
                "report_bucket": bucket,
                "stock_id": stock_id,
                "stock_name": text(top, "stock_name"),
                "industry": text(top, "industry"),
                "effective_primary_theme": text(top, "effective_primary_theme", "primary_theme"),
                "effective_structural_theme_bucket": text(top, "effective_structural_theme_bucket"),
                "effective_mainstream_label": text(top, "effective_mainstream_label"),
                "primary_model_id": text(top, "model_id"),
                "primary_model_name_zh": text(top, "model_name_zh"),
                "primary_model_score": top.get("model_score", ""),
                "primary_model_rank": top.get("model_rank", ""),
                "model_rank_overall": top.get("model_rank_overall", top.get("model_rank", "")),
                "model_rank_new_signal": top.get("model_rank_new_signal", ""),
                "display_rank_new_signal": top.get("display_rank_new_signal", ""),
                "model_hit_count": len(part),
                "model_hits": _join_unique(part["model_name_zh"]),
                "model_hit_ids": _join_unique(part["model_id"]),
                "same_model_repeat_status": text(top, "same_model_repeat_status"),
                "same_model_repeat_status_zh": text(top, "same_model_repeat_status_zh"),
                "same_model_repeat_note_zh": text(top, "same_model_repeat_note_zh"),
                "same_model_consecutive_days": top.get("same_model_consecutive_days", ""),
                "same_model_appear_count_5d": top.get("same_model_appear_count_5d", ""),
                "same_model_appear_count_10d": top.get("same_model_appear_count_10d", ""),
                "tdcc_status": text(top, "tdcc_status"),
                "warrant_flow_signal": text(top, "warrant_flow_signal"),
                "volume_ratio": top.get("volume_ratio", ""),
                "risk_penalty_tags": _join_unique(part["risk_penalty_tags"]),
                "risk_tags_zh": _join_unique(part["risk_tags_zh"]) if "risk_tags_zh" in part.columns else "",
                "score_components": text(top, "score_components"),
                "next_confirmation": text(top, "next_confirmation"),
                "next_confirmation_zh": text(top, "next_confirmation_zh"),
                "frontpage_usage": "Use this table for first-page representatives; full model hits remain in daily_candidate_model_signals_latest.csv.",
            }
        )

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["_bucket_order"] = out["report_bucket"].map({"mainstream": 1, "non_mainstream": 2, "unclassified": 3}).fillna(9)
    out["_fresh_order"] = out["same_model_repeat_status"].map({"new_model_signal": 0, "repeated_same_model_signal": 1}).fillna(2)
    out["_score_num"] = pd.to_numeric(out.get("primary_model_score", ""), errors="coerce").fillna(-999)
    out = out.sort_values(
        ["_bucket_order", "_fresh_order", "_score_num", "model_hit_count", "stock_id"],
        ascending=[True, True, False, False, True],
    ).reset_index(drop=True)
    out["frontpage_unique_rank"] = out.groupby("report_bucket", dropna=False).cumcount() + 1
    return out.drop(columns=["_bucket_order", "_fresh_order", "_score_num"])


def snapshot_model_signals(signals: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "signal_date",
        "report_bucket",
        "stock_id",
        "stock_name",
        "model_id",
        "model_name_zh",
        "model_group",
        "model_score",
        "model_rank",
        "effective_primary_theme",
        "risk_penalty_tags",
        "next_confirmation",
    ]
    if signals.empty:
        return pd.DataFrame(columns=cols)
    out = signals.copy()
    for col in cols:
        if col not in out.columns:
            out[col] = ""
    return out[cols].drop_duplicates(["signal_date", "report_bucket", "stock_id", "model_id"], keep="first")


def update_model_signal_log(signals: pd.DataFrame) -> pd.DataFrame:
    MODEL_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    current = snapshot_model_signals(signals)
    history = read_csv(MODEL_SIGNAL_LOG_CSV, dtype=str, keep_default_na=False)
    if history.empty:
        merged = current
    else:
        current_dates = set(current.get("signal_date", pd.Series(dtype=str)).astype(str).tolist())
        current_dates.discard("")
        if current_dates and "signal_date" in history.columns:
            max_current_date = max(current_dates)
            history = history[history["signal_date"].astype(str) <= max_current_date].copy()
            history = history[~history["signal_date"].astype(str).isin(current_dates)].copy()
        merged = pd.concat([history, current], ignore_index=True, sort=False)
        merged = merged.drop_duplicates(["signal_date", "report_bucket", "stock_id", "model_id"], keep="last")
    if not merged.empty:
        merged = merged.sort_values(["signal_date", "model_id", "report_bucket", "stock_id"]).reset_index(drop=True)
    write_csv(merged, MODEL_SIGNAL_LOG_CSV)
    return merged


def _window_count(dates: set[str], ordered_dates: list[str], current_date: str, window: int) -> int:
    if current_date not in ordered_dates:
        return 0
    idx = ordered_dates.index(current_date)
    window_dates = ordered_dates[max(0, idx - window + 1) : idx + 1]
    return sum(1 for date in window_dates if date in dates)


def _consecutive_count(dates: set[str], ordered_dates: list[str], current_date: str) -> int:
    if current_date not in ordered_dates:
        return 0
    count = 0
    idx = ordered_dates.index(current_date)
    for date in reversed(ordered_dates[: idx + 1]):
        if date not in dates:
            break
        count += 1
    return count


def attach_same_model_repeat(signals: pd.DataFrame, model_log: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if signals.empty:
        out = signals.copy()
        out["same_model_consecutive_days"] = ""
        out["same_model_appear_count_5d"] = ""
        out["same_model_appear_count_10d"] = ""
        out["same_model_repeat_status"] = ""
        return add_same_model_repeat_display_and_ranks(out), pd.DataFrame()

    out = signals.copy()
    if model_log.empty:
        out["same_model_consecutive_days"] = 1
        out["same_model_appear_count_5d"] = 1
        out["same_model_appear_count_10d"] = 1
        out["same_model_repeat_status"] = "new_model_signal"
        return add_same_model_repeat_display_and_ranks(out), pd.DataFrame()

    log = model_log.copy()
    for col in ["signal_date", "report_bucket", "stock_id", "model_id"]:
        if col not in log.columns:
            log[col] = ""
    log["signal_date"] = log["signal_date"].astype(str)
    ordered_dates = sorted(date for date in log["signal_date"].unique().tolist() if date)
    grouped_dates: dict[tuple[str, str, str], set[str]] = {}
    for key, part in log.groupby(["report_bucket", "stock_id", "model_id"], dropna=False):
        grouped_dates[(safe_str(key[0]), safe_str(key[1]), safe_str(key[2]))] = set(part["signal_date"].astype(str))

    consecutive: list[int] = []
    count_5d: list[int] = []
    count_10d: list[int] = []
    status: list[str] = []
    for _, row in out.iterrows():
        current_date = safe_str(row.get("signal_date", ""))
        key = (safe_str(row.get("report_bucket", "")), safe_str(row.get("stock_id", "")), safe_str(row.get("model_id", "")))
        dates = grouped_dates.get(key, set())
        consec = _consecutive_count(dates, ordered_dates, current_date)
        c5 = _window_count(dates, ordered_dates, current_date, 5)
        c10 = _window_count(dates, ordered_dates, current_date, 10)
        consecutive.append(consec)
        count_5d.append(c5)
        count_10d.append(c10)
        status.append("repeated_same_model_signal" if consec >= 2 else "new_model_signal")
    out["same_model_consecutive_days"] = consecutive
    out["same_model_appear_count_5d"] = count_5d
    out["same_model_appear_count_10d"] = count_10d
    out["same_model_repeat_status"] = status
    out = add_same_model_repeat_display_and_ranks(out)

    repeat = out[
        (out["model_group"].astype(str).eq("pdf_core_model"))
        & (pd.to_numeric(out["same_model_consecutive_days"], errors="coerce").fillna(0) >= 2)
    ].copy()
    if not repeat.empty:
        repeat["_consec"] = pd.to_numeric(repeat["same_model_consecutive_days"], errors="coerce").fillna(0)
        repeat["_count10"] = pd.to_numeric(repeat["same_model_appear_count_10d"], errors="coerce").fillna(0)
        repeat["_score"] = pd.to_numeric(repeat["model_score"], errors="coerce").fillna(0)
        repeat = repeat.sort_values(
            ["report_bucket", "_consec", "_count10", "_score", "stock_id"],
            ascending=[True, False, False, False, True],
        ).reset_index(drop=True)
        repeat["same_model_repeat_rank"] = repeat.groupby(["report_bucket", "model_id"], dropna=False).cumcount() + 1
        repeat["model_rank_repeated_signal"] = repeat["same_model_repeat_rank"].astype(str)
        repeat["display_rank_repeated_signal"] = repeat["same_model_repeat_rank"].map(lambda rank: f"重複榜#{int(rank)}")
        repeat = repeat.drop(columns=["_consec", "_count10", "_score"])
    return out, repeat


def build_signals(candidates: pd.DataFrame, specs: list[ModelSpec], signal_date: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if candidates.empty:
        return pd.DataFrame()
    for idx, row in candidates.iterrows():
        stock_id = normalize_code(text(row, "stock_id", "ticker"))
        if not stock_id:
            continue
        for spec in specs:
            if not spec.condition_func(row):
                continue
            raw_score, comps, risks = spec.score_func(row)
            score = round(clamp(raw_score), 1)
            for bucket in report_buckets(row):
                rows.append(
                    {
                        "signal_date": signal_date or text(row, "signal_date", "date"),
                        "source_row_index": idx,
                        "stock_id": stock_id,
                        "stock_name": text(row, "stock_name", "name"),
                        "industry": text(row, "industry"),
                        "primary_theme": primary_theme(row),
                        "effective_primary_theme": primary_theme(row),
                        "secondary_themes": text(row, "secondary_themes", "taxonomy_secondary_themes"),
                        "effective_structural_theme_bucket": effective_structural_theme_bucket(row),
                        "effective_mainstream_label": effective_mainstream_label(row),
                        "report_line_memberships": report_line_memberships_value(row),
                        "mainstream_report_eligible": mainstream_report_eligible_value(row),
                        "non_mainstream_report_eligible": non_mainstream_report_eligible_value(row),
                        "dual_report_membership_flag": dual_report_membership_flag_value(row),
                        "report_bucket": bucket,
                        "model_id": spec.model_id,
                        "model_name_zh": spec.model_name_zh,
                        "model_group": spec.pdf_visibility,
                        "main_condition_met": "True",
                        "entry_basis": spec.entry_basis,
                        "model_score": score,
                        "score_components": " | ".join(comps),
                        "risk_penalty_tags": " | ".join(dict.fromkeys(risks)),
                        "original_category": category(row),
                        "decision_priority": text(row, "decision_priority"),
                        "decision_score": text(row, "decision_score"),
                        "tdcc_status": tdcc_status(row),
                        "warrant_flow_signal": warrant_signal(row),
                        "volume_ratio": num(row, "volume_ratio"),
                        "return_5d": num(row, "return_5d", "return_5d_pct"),
                        "return_20d": num(row, "return_20d", "return_20d_pct"),
                        "next_confirmation": clean_next_confirmation(row, spec),
                        "model_main_conditions": spec.main_conditions_zh,
                        "model_add_score_items": spec.add_score_zh,
                        "model_forbidden_veto": spec.forbidden_veto_zh,
                        "model_operation_guidance": spec.operation_guidance_zh,
                        "selection_semantics": "model_condition_met_rank_by_score_no_theme_veto",
                    }
                )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    out["_bucket_order"] = out["report_bucket"].map({"mainstream": 1, "non_mainstream": 2, "unclassified": 3}).fillna(9)
    out = out.sort_values(
        ["model_id", "_bucket_order", "model_score", "stock_id", "source_row_index"],
        ascending=[True, True, False, True, True],
    ).reset_index(drop=True)
    out = out.drop_duplicates(["model_id", "report_bucket", "stock_id"], keep="first").reset_index(drop=True)
    out["model_rank"] = out.groupby(["model_id", "report_bucket"], dropna=False).cumcount() + 1
    return out.drop(columns=["_bucket_order"])


def candidate_lookup(candidates: pd.DataFrame) -> dict[str, pd.Series]:
    lookup: dict[str, pd.Series] = {}
    if candidates.empty:
        return lookup
    for _, row in candidates.iterrows():
        stock_id = normalize_code(text(row, "stock_id", "ticker"))
        if stock_id and stock_id not in lookup:
            lookup[stock_id] = row
    return lookup


@lru_cache(maxsize=1)
def taxonomy_lookup() -> dict[str, pd.Series]:
    df = read_csv(STOCK_THEME_TAXONOMY, dtype=str, keep_default_na=False)
    lookup: dict[str, pd.Series] = {}
    if df.empty:
        return lookup
    for _, row in df.iterrows():
        stock_id = normalize_code(text(row, "stock_id"))
        if stock_id and stock_id not in lookup:
            lookup[stock_id] = row
    return lookup


def taxonomy_or_source(stock_id: str, fallback: pd.Series) -> pd.Series:
    return taxonomy_lookup().get(normalize_code(stock_id), fallback)


def enrich_candidates_with_taxonomy(candidates: pd.DataFrame) -> pd.DataFrame:
    """Attach taxonomy fields before model gates run.

    all_candidates is a market-signal table and may not carry every taxonomy
    field.  Model gates that depend on hot themes must join taxonomy here; the
    PDF layer must not infer this later.
    """
    if candidates.empty or "stock_id" not in candidates.columns:
        return candidates
    taxonomy = read_csv(STOCK_THEME_TAXONOMY, dtype=str, keep_default_na=False)
    if taxonomy.empty or "stock_id" not in taxonomy.columns:
        return candidates

    left = candidates.copy()
    left["_taxonomy_join_stock_id"] = left["stock_id"].map(normalize_code)

    tax = taxonomy.copy()
    tax["_taxonomy_join_stock_id"] = tax["stock_id"].map(normalize_code)
    tax = tax[tax["_taxonomy_join_stock_id"].astype(str).ne("")]
    tax = tax.drop_duplicates("_taxonomy_join_stock_id", keep="first")

    rename: dict[str, str] = {}
    for col in tax.columns:
        if col in {"stock_id", "_taxonomy_join_stock_id"}:
            continue
        if col in left.columns:
            rename[col] = f"taxonomy_{col}"
    tax = tax.rename(columns=rename).drop(columns=["stock_id"], errors="ignore")

    out = left.merge(tax, on="_taxonomy_join_stock_id", how="left")
    return out.drop(columns=["_taxonomy_join_stock_id"], errors="ignore")


def external_report_bucket(volume_row: pd.Series, candidate_row: pd.Series | None) -> str:
    if candidate_row is not None:
        buckets = report_buckets(candidate_row)
        if buckets:
            return buckets[0]
    group = text(volume_row, "theme_group", "effective_mainstream_label").lower()
    if "core_mainstream" in group or "mainstream" in group:
        return "mainstream"
    if "non_mainstream" in group:
        return "non_mainstream"
    return "non_mainstream"


def append_volume_breakout_signals(signals: pd.DataFrame, candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    df = read_csv(VOLUME_BREAKOUT_WATCH, dtype=str, keep_default_na=False)
    if df.empty:
        return signals
    lookup = candidate_lookup(candidates)
    rows: list[dict[str, Any]] = []
    valid_statuses = {"selected", "selected_but_routed_to_other_category", "not_selected_by_candidate_model"}
    valid_types = {
        "range_breakout_volume",
        "platform_volume_breakout",
        "neckline_volume_breakout",
        "strict_high_breakout",
        "strict_60d_volume_breakout",
    }
    for idx, row in df.iterrows():
        breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
        selection_status = text(row, "selection_status").lower()
        if breakout_type not in valid_types or selection_status not in valid_statuses:
            continue
        stock_id = normalize_code(text(row, "stock_id"))
        if not stock_id:
            continue
        candidate_row = lookup.get(stock_id)
        source = candidate_row if candidate_row is not None else taxonomy_or_source(stock_id, row)
        score = to_number(row.get("volume_breakout_score", ""))
        if math.isnan(score):
            score = 50
        risks: list[str] = []
        if flag(row, "false_breakout_risk_calc") or flag(row, "false_breakout_risk"):
            risks.append("false_breakout_risk")
        if flag(row, "overheated_breakout"):
            risks.append("overheated_breakout")
        priority = text(row, "volume_breakout_priority")
        if priority.startswith("D_"):
            risks.append(priority)
        notes = text(row, "volume_breakout_notes")
        comps = [f"type={breakout_type}", f"volume_score={row.get('volume_breakout_score','')}".strip()]
        if notes:
            comps.append(notes)
        rows.append(
            {
                "signal_date": signal_date or text(row, "signal_date", "date"),
                "source_row_index": f"volume_breakout:{idx}",
                "stock_id": stock_id,
                "stock_name": text(row, "stock_name"),
                "industry": text(source, "industry"),
                "primary_theme": primary_theme(source),
                "effective_primary_theme": primary_theme(source),
                "secondary_themes": text(source, "secondary_themes", "taxonomy_secondary_themes"),
                "effective_structural_theme_bucket": effective_structural_theme_bucket(source),
                "effective_mainstream_label": effective_mainstream_label(source),
                "report_line_memberships": report_line_memberships_value(source),
                "mainstream_report_eligible": mainstream_report_eligible_value(source),
                "non_mainstream_report_eligible": non_mainstream_report_eligible_value(source),
                "dual_report_membership_flag": dual_report_membership_flag_value(source),
                "report_bucket": external_report_bucket(row, source),
                "model_id": "volume_range_breakout",
                "model_name_zh": "帶量突破模型",
                "model_group": "pdf_core_model",
                "main_condition_met": "True",
                "entry_basis": "signal_date_next_open",
                "model_score": round(clamp(score), 1),
                "score_components": " | ".join([c for c in comps if c]),
                "risk_penalty_tags": " | ".join(dict.fromkeys(risks)),
                "original_category": category(source),
                "decision_priority": text(row, "decision_priority") or text(source, "decision_priority"),
                "decision_score": text(row, "decision_score") or text(source, "decision_score"),
                "tdcc_status": text(row, "tdcc_status") or tdcc_status(source),
                "warrant_flow_signal": text(row, "warrant_flow_signal") or warrant_signal(source),
                "volume_ratio": num(row, "volume_ratio"),
                "return_5d": num(row, "return_5d", "return_5d_pct"),
                "return_20d": num(row, "return_20d", "return_20d_pct"),
                "next_confirmation": text(row, "next_volume_breakout_confirmation") or text(source, "next_confirmation"),
                "model_main_conditions": "Volume ratio and confirmed range/platform/neckline/high breakout.",
                "model_add_score_items": "Higher volume ratio, stronger breakout quality, longer base, TDCC, warrant, revenue, lower position.",
                "model_forbidden_veto": "Do not veto only because the stock was routed to another category or looks overheated; risk is ranking/operation guidance.",
                "model_operation_guidance": "Signal date next open is the entry basis; use breakout zone and 23EMA/platform as failure lines.",
                "selection_semantics": "volume_breakout_condition_met_from_dedicated_table",
            }
        )
    if not rows:
        return signals
    extra = pd.DataFrame(rows)
    out = pd.concat([signals, extra], ignore_index=True, sort=False) if not signals.empty else extra
    out["_bucket_order"] = out["report_bucket"].map({"mainstream": 1, "non_mainstream": 2, "unclassified": 3}).fillna(9)
    out["_score_num"] = pd.to_numeric(out.get("model_score", ""), errors="coerce").fillna(0)
    out = out.sort_values(
        ["model_id", "_bucket_order", "_score_num", "stock_id", "source_row_index"],
        ascending=[True, True, False, True, True],
    ).reset_index(drop=True)
    out = out.drop_duplicates(["model_id", "report_bucket", "stock_id"], keep="first").reset_index(drop=True)
    out["model_rank"] = out.groupby(["model_id", "report_bucket"], dropna=False).cumcount() + 1
    return out.drop(columns=["_bucket_order", "_score_num"])


def append_tdcc_short_term(signals: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    def tdcc_short_term_score(row: pd.Series, source: pd.Series) -> tuple[float, list[str], list[str]]:
        score = 50.0
        parts: list[str] = ["base=50"]
        risks: list[str] = []

        d10_win = to_number(row.get("d10_win_rate_pct", ""))
        d10_rel = to_number(row.get("d10_avg_relative_return_pct", ""))
        d5_win = to_number(row.get("d5_win_rate_pct", ""))
        if not math.isnan(d10_win):
            add = max(0.0, (d10_win - 50.0) * 0.25)
            score += add
            parts.append(f"D+10 win {d10_win:.1f}% +{add:.1f}")
        if not math.isnan(d10_rel):
            add = max(-8.0, min(12.0, d10_rel * 0.7))
            score += add
            parts.append(f"D+10 rel {d10_rel:.1f}% {add:+.1f}")
        if not math.isnan(d5_win):
            add = max(0.0, (d5_win - 50.0) * 0.10)
            score += add
            parts.append(f"D+5 win {d5_win:.1f}% +{add:.1f}")

        rule_id = text(row, "rule_id")
        if "all_thresholds" in rule_id:
            score += 8
            parts.append("all_thresholds +8")
        elif "phase_overheated" in rule_id:
            score += 4
            parts.append("phase_overheated +4")

        weeks = num(row, "tdcc_consecutive_up_weeks")
        if not math.isnan(weeks):
            if 1 <= weeks <= 3:
                score += 6
                parts.append(f"TDCC streak {weeks:.0f}w +6")
            elif weeks >= 4:
                score += 3
                parts.append(f"TDCC streak {weeks:.0f}w +3")

        macd_hist = num(row, "macd_hist")
        if not math.isnan(macd_hist):
            if macd_hist > 0:
                add = 8 if macd_hist >= 5 else 6
                score += add
                parts.append(f"MACD hist >0 +{add}")
            else:
                score -= 6
                risks.append("macd_hist_not_positive")
                parts.append("MACD hist <=0 -6")

        k_value = num(row, "k_value")
        d_value = num(row, "d_value")
        if not math.isnan(k_value) and not math.isnan(d_value):
            if k_value > d_value and k_value < 85:
                score += 6
                parts.append("KD bullish not overheated +6")
            elif k_value >= 90:
                score -= 5
                risks.append("kd_overheated")
                parts.append("KD overheated -5")

        ret_1w = num(row, "price_ret_1w")
        if not math.isnan(ret_1w):
            if 10 <= ret_1w <= 30:
                score += 8
                parts.append("1W return 10-30 +8")
            elif ret_1w > 30:
                score -= 8
                risks.append("one_week_return_too_extended")
                parts.append("1W return >30 -8")

        ret_2w = num(row, "price_ret_2w")
        if not math.isnan(ret_2w):
            if 20 <= ret_2w <= 50:
                score += 8
                parts.append("2W return 20-50 +8")
            elif ret_2w > 60:
                score -= 8
                risks.append("two_week_return_too_extended")
                parts.append("2W return >60 -8")

        bb_pct = num(row, "bb_width_percentile_120d")
        if not math.isnan(bb_pct):
            if bb_pct <= 80:
                score += 4
                parts.append("BB width not extreme +4")
            elif bb_pct >= 95:
                score -= 3
                risks.append("bb_width_extreme")
                parts.append("BB width extreme -3")

        if report_bucket(source) == "mainstream":
            score += 4
            parts.append("mainstream +4")

        regime = text(row, "market_regime")
        if regime == "strong_bull":
            score += 3
            parts.append("strong_bull +3")
        elif regime in {"correction", "high_risk"}:
            score -= 4
            risks.append(f"market_regime_{regime}")
            parts.append(f"{regime} -4")

        return round(clamp(score), 1), parts, risks

    rows: list[dict[str, Any]] = []
    df = read_csv(TDCC_EDGE_CANDIDATES, dtype=str, keep_default_na=False)
    if not df.empty:
        for idx, row in df.iterrows():
            stock_id = normalize_code(text(row, "stock_id"))
            source = taxonomy_or_source(stock_id, row)
            score, score_parts, risk_tags = tdcc_short_term_score(row, source)
            rows.append(
                {
                    "signal_date": signal_date,
                    "source_row_index": f"tdcc_edge:{idx}",
                    "stock_id": stock_id,
                    "stock_name": text(row, "stock_name"),
                    "industry": text(source, "industry"),
                    "primary_theme": primary_theme(source) or text(row, "theme"),
                    "effective_primary_theme": primary_theme(source) or text(row, "theme"),
                    "secondary_themes": text(source, "secondary_themes", "taxonomy_secondary_themes"),
                    "effective_structural_theme_bucket": effective_structural_theme_bucket(source),
                    "effective_mainstream_label": effective_mainstream_label(source),
                    "report_line_memberships": report_line_memberships_value(source),
                    "mainstream_report_eligible": mainstream_report_eligible_value(source),
                    "non_mainstream_report_eligible": non_mainstream_report_eligible_value(source),
                    "dual_report_membership_flag": dual_report_membership_flag_value(source),
                    "report_bucket": report_bucket(source),
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "model_name_zh": "TDCC短線延續模型 D+5/D+10",
                    "model_group": "pdf_specialty_section",
                    "main_condition_met": "True",
                    "entry_basis": "signal_date_next_open",
                    "model_score": score,
                    "score_components": " | ".join(score_parts),
                    "risk_penalty_tags": "|".join(risk_tags),
                    "original_category": "short_term_specialty",
                    "decision_priority": "",
                    "decision_score": "",
                    "tdcc_status": text(row, "tdcc_price_phase"),
                    "warrant_flow_signal": "",
                    "volume_ratio": "",
                    "return_5d": "",
                    "return_20d": "",
                    "next_confirmation": "短線延續專項；用隔日開盤為進場原點，檢查D+1到D+10收盤/最高價。",
                    "model_main_conditions": "all_thresholds_overheated或phase_overheated_after_tdcc，搭配MACD/KD/Bollinger與1W/2W漲幅條件。",
                    "model_add_score_items": "D+1到D+10 next-open close/high統計、樣本數、相對報酬、market regime分層。",
                    "model_forbidden_veto": "不是低位買進模型，不可混入TDCC潛伏吸籌。",
                    "model_operation_guidance": "隔日開盤為進場原點；依D+1到D+10收盤/最高價統計做短線延續檢查。",
                    "selection_semantics": "specialty_condition_met_rank_by_tdcc_short_term_score",
                }
            )
    # Short-term surge is a research/backtest model. It is intentionally kept
    # out of the daily PDF candidate signal table until its parameters mature.
    surge = pd.DataFrame()
    if not surge.empty:
        for idx, row in surge.iterrows():
            stock_id = normalize_code(text(row, "stock_id"))
            source = taxonomy_or_source(stock_id, row)
            d10 = to_number(row.get("best_d10_hit_rate_pct", ""))
            d5 = to_number(row.get("best_d5_hit_rate_pct", ""))
            score = 50 + (0 if math.isnan(d10) else d10 * 0.35) + (0 if math.isnan(d5) else d5 * 0.15)
            rows.append(
                {
                    "signal_date": text(row, "date") or signal_date,
                    "source_row_index": f"short_surge:{idx}",
                    "stock_id": stock_id,
                    "stock_name": text(row, "stock_name"),
                    "industry": text(source, "industry"),
                    "primary_theme": primary_theme(source) or text(row, "theme"),
                    "effective_primary_theme": primary_theme(source) or text(row, "theme"),
                    "secondary_themes": text(source, "secondary_themes", "taxonomy_secondary_themes"),
                    "effective_structural_theme_bucket": effective_structural_theme_bucket(source),
                    "effective_mainstream_label": effective_mainstream_label(source),
                    "report_line_memberships": report_line_memberships_value(source),
                    "mainstream_report_eligible": mainstream_report_eligible_value(source),
                    "non_mainstream_report_eligible": non_mainstream_report_eligible_value(source),
                    "dual_report_membership_flag": dual_report_membership_flag_value(source),
                    "report_bucket": report_bucket(source),
                    "model_id": "short_term_surge_d5_d10",
                    "model_name_zh": "短線急漲D+5/D+10模型",
                    "model_group": "research_only_not_pdf_core",
                    "main_condition_met": "True",
                    "entry_basis": "signal_date_next_open",
                    "model_score": round(clamp(score), 1),
                    "score_components": f"best D+5={row.get('best_d5_hit_rate_pct','')} / best D+10={row.get('best_d10_hit_rate_pct','')}",
                    "risk_penalty_tags": text(row, "market_abnormal_status", "execution_risk_note"),
                    "original_category": "short_term_specialty",
                    "decision_priority": text(row, "research_priority"),
                    "decision_score": "",
                    "tdcc_status": "",
                    "warrant_flow_signal": "",
                    "volume_ratio": text(row, "start_5d_avg_volume_ratio_vs_prev20"),
                    "return_5d": text(row, "return_5d_pct"),
                    "return_20d": text(row, "return_20d_pct"),
                    "next_confirmation": "短線急漲研究專項；用隔日開盤為進場原點，分D+1到D+20檢查。",
                    "model_main_conditions": "5日或10日漲幅達標、量能擴張、技術動能強。",
                    "model_add_score_items": "D+1到D+20 close/high統計、處置/注意標籤、TDCC與市場狀態分層。",
                    "model_forbidden_veto": "不得稱為周線K；必須標清楚單位與進場原點。",
                    "model_operation_guidance": "隔日開盤為進場原點；依D+1到D+20收盤/最高價統計檢查短線延續。",
                    "selection_semantics": "specialty_condition_met_rank_by_backtest_stats",
                }
            )
    if not rows:
        return signals
    extra = pd.DataFrame(rows)
    combined = pd.concat([signals, extra], ignore_index=True) if not signals.empty else extra
    combined = combined.sort_values(["model_id", "model_score", "stock_id"], ascending=[True, False, True]).reset_index(drop=True)
    combined = combined.drop_duplicates(["model_id", "report_bucket", "stock_id"], keep="first").reset_index(drop=True)
    combined["model_rank"] = combined.groupby(["model_id", "report_bucket"], dropna=False).cumcount() + 1
    return combined


def build_report_ready_model_signals(signals: pd.DataFrame) -> pd.DataFrame:
    """Collapse duplicate source rows for report rendering.

    Raw model signals may carry several source rows for the same stock and the
    same displayed model, especially when one stock enters from several original
    categories. Reports should show that as one row with merged source context,
    not as repeated stock rows inside the same model table.
    """
    if signals.empty:
        return signals.copy()

    work = signals.copy()
    for col in [
        "signal_date",
        "report_bucket",
        "model_name_zh",
        "model_id",
        "stock_id",
        "model_score",
        "model_rank",
        "original_category",
        "source_row_index",
        "next_confirmation",
        "score_components",
        "risk_penalty_tags",
    ]:
        if col not in work.columns:
            work[col] = ""

    work["_rank_num"] = pd.to_numeric(work["model_rank"], errors="coerce").fillna(999999)
    work["_score_num"] = pd.to_numeric(work["model_score"], errors="coerce").fillna(-999999)
    work = work.sort_values(
        ["report_bucket", "model_name_zh", "stock_id", "_rank_num", "_score_num"],
        ascending=[True, True, True, True, False],
    )

    grouped_rows: list[dict[str, Any]] = []
    for (_, _, _), part in work.groupby(["report_bucket", "model_name_zh", "stock_id"], dropna=False, sort=False):
        best = part.iloc[0].copy()
        row = best.to_dict()
        row["merged_same_model_source_count"] = len(part)
        row["merged_model_ids"] = _join_unique(part["model_id"])
        row["merged_source_row_indices"] = _join_unique(part["source_row_index"])
        row["merged_source_categories"] = _join_unique(part["original_category"])
        row["merged_next_confirmations"] = _join_unique(part["next_confirmation"])
        row["merged_score_components"] = _join_unique(part["score_components"])
        row["merged_risk_penalty_tags"] = _join_unique(part["risk_penalty_tags"])
        row["report_model_key"] = safe_str(best.get("model_name_zh")) or safe_str(best.get("model_id"))
        grouped_rows.append(row)

    out = pd.DataFrame(grouped_rows).drop(columns=["_rank_num", "_score_num"], errors="ignore")
    out["_bucket_order"] = out["report_bucket"].map({"mainstream": 1, "non_mainstream": 2, "unclassified": 3}).fillna(9)
    out["_score_num"] = pd.to_numeric(out["model_score"], errors="coerce").fillna(0)
    out = out.sort_values(
        ["report_bucket", "model_name_zh", "_score_num", "stock_id"],
        ascending=[True, True, False, True],
    ).reset_index(drop=True)
    out["model_rank"] = out.groupby(["report_bucket", "model_name_zh"], dropna=False).cumcount() + 1
    return out.drop(columns=["_bucket_order", "_score_num"], errors="ignore")


PDF_TOKEN_ZH = {
    "non_mainstream": "非主流",
    "mainstream": "主流",
    "mainstream_or_non_mainstream": "主流與非主流皆可",
    "dual": "雙線",
    "neckline": "頸線",
    "breakout": "突破",
    "hot theme tag": "熱門族群標籤",
    "hot_theme_tag": "熱門族群標籤",
    "range_rebound": "區間轉強",
    "short_term_specialty": "短線專項",
    "mild_accumulation": "大戶溫和增加",
    "strong_accumulation": "大戶強累積",
    "neutral": "中性",
    "distribution_warning": "大戶轉弱警示",
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購流入",
    "call_put_bullish": "權證偏多",
    "mixed_flow": "權證多空混合",
    "put_inflow": "認售流入",
    "put_strong_inflow": "認售強流入",
    "no_signal": "無明確權證訊號",
    "true_breakout": "嚴格突破",
    "volume_breakout": "帶量突破",
    "range_breakout_volume": "帶量突破盤整區間",
    "range_breakout_watch": "接近盤整上緣觀察",
    "ma_reclaim_volume_attack": "帶量站回均線",
    "near_high_volume_watch": "接近前高帶量觀察",
    "strict_high_breakout": "帶量突破波段高點",
    "failed_range_breakout_risk": "盤整區間假突破風險",
    "revenue_breakout_low_response": "營收爆發股價尚未反應",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
    "tdcc": "TDCC",
    "tdcc_leading_price": "TDCC領先股價",
    "tdcc_price_confirmed": "TDCC與股價確認",
    "price_leading_tdcc": "股價領先TDCC",
    "overheated_after_tdcc": "TDCC後股價過熱",
    "phase_overheated_after_tdcc": "TDCC後股價過熱",
    "all_thresholds_overheated": "四級距同步過熱",
    "w_bottom_right_side": "W底右側",
    "platform_right_side": "平台右側",
    "platform_breakout": "平台突破",
    "neckline_challenge": "頸線挑戰",
    "neckline_breakout": "頸線突破",
    "new_model_signal": "新進榜",
    "repeated_same_model_signal": "重複進榜",
    "same_model_repeat_moved_to_persistence_table": "同模型重複進榜，移至延續表",
    "duplicate_stock_already_shown_on_frontpage": "首頁已列示",
    "not_pdf_core_model": "非PDF核心模型",
    "ai_server_ipc_theme": "AI伺服器 / 工業電腦",
    "automotive_electronics_theme": "車用電子",
    "computer_peripheral_general_theme": "電腦週邊",
    "defense_drone_theme": "軍工 / 無人機",
    "digital_cloud_general_theme": "數位雲端",
    "electronic_component_general_theme": "電子零組件",
    "electronics_channel_general_theme": "電子通路",
    "glass_fiber_ccl_theme": "玻纖布 / CCL",
    "information_service_general_theme": "資訊服務",
    "low_earth_orbit_satellite_theme": "低軌衛星",
    "memory_hbm_theme": "記憶體 / HBM",
    "network_optical_datacenter_theme": "網通 / 光通訊 / 資料中心",
    "networking_general_theme": "網通",
    "optoelectronics_general_theme": "光電",
    "other_electronics_general_theme": "其他電子",
    "passive_component_theme": "被動元件",
    "pcb_ccl_theme": "PCB / CCL",
    "power_grid_theme": "重電 / 電網",
    "power_supply_theme": "電源 / BBU",
    "robotics_ipc_edge_ai_theme": "機器人 / 工業電腦 / Edge AI",
    "semiconductor_equipment_cowos_theme": "半導體設備 / CoWoS",
    "semiconductor_general_theme": "半導體",
    "thermal_liquid_cooling_theme": "散熱 / 液冷",
    "wire_cable_theme": "電線電纜",
    "20d_return_high_score_penalty": "20日漲幅偏高扣分",
    "tdcc_distribution_penalty": "TDCC轉弱扣分",
    "bb_width_extreme": "布林帶寬過度擴張",
    "kd_overheated": "KD過熱",
    "two_week_return_too_extended": "兩週漲幅過大",
    "one_week_return_too_extended": "一週漲幅過大",
    "second_attack_weaker_watch": "第二段攻擊量能較弱觀察",
}

MODEL_NAME_ZH_BY_ID = {
    "volume_range_breakout": "帶量突破模型",
    "price_pullback_23ema": "股價回檔模型",
    "hot_theme_pullback": "熱門族群回檔模型",
    "revenue_unreacted_range": "營收爆發但股價尚未反應模型",
    "w_bottom_right_side": "W底右側模型",
    "near_high_neckline_challenge": "接近前高 / 頸線挑戰模型",
    "platform_strengthening": "平台整理轉強模型",
    "pullback_short_reclaim": "回檔後短線轉強模型",
    "tdcc_stealth_accumulation": "TDCC潛伏吸籌模型",
    "tdcc_short_continuation": "TDCC短線延續模型 D+5/D+10",
    "tdcc_short_term_continuation_d5_d10": "TDCC短線延續模型 D+5/D+10",
    "short_term_surge_d5_d10": "短線急漲 D+5/D+10",
    "group_fund_rotation": "族群資金輪動模型",
}

MODEL_HUMAN_REASON_ZH = {
    "volume_range_breakout": "符合帶量突破模型，量能明顯放大並突破或挑戰關鍵壓力，後續依突破區與量價延續管理。",
    "price_pullback_23ema": "符合股價回檔模型，股價接近23EMA或支撐區，回測後轉強。",
    "hot_theme_pullback": "符合熱門族群回檔模型，具熱門族群標籤，股價回測23EMA或支撐後轉強。",
    "revenue_unreacted_range": "符合營收爆發但股價尚未反應模型，營收動能較強且股價仍在整理區。",
    "w_bottom_right_side": "符合W底右側模型，右側低點墊高並接近頸線或轉強區。",
    "near_high_neckline_challenge": "符合接近前高 / 頸線挑戰模型，距離關鍵壓力不遠且量能開始回升。",
    "platform_strengthening": "符合平台整理轉強模型，盤整區間形成後量能回升並接近上緣。",
    "pullback_short_reclaim": "符合回檔後短線轉強模型，前段漲勢後回檔未破結構並重新轉強。",
    "tdcc_stealth_accumulation": "符合TDCC潛伏吸籌模型，大戶籌碼改善，股價尚未完全反應。",
    "tdcc_short_continuation": "符合TDCC短線延續模型，歷史短線延續樣本具參考性，適合作D+5/D+10短線延續觀察。",
    "tdcc_short_term_continuation_d5_d10": "符合TDCC短線延續模型，歷史短線延續樣本具參考性，適合作D+5/D+10短線延續觀察。",
    "short_term_surge_d5_d10": "符合短線急漲研究條件，僅作短線動能研究觀察，不作低位買進模型。",
}

MODEL_OPERATION_REMINDER_ZH = {
    "volume_range_breakout": "若跌回突破區或量價失敗，應降低部位或退出；突破後以支撐與壓力管理。",
    "price_pullback_23ema": "回檔模型不要求先突破；若跌破23EMA或支撐且無法快速收回，需降低風險。",
    "hot_theme_pullback": "熱門族群回檔以族群標籤與23EMA附近支撐為主；若族群退潮或跌破支撐需降風險。",
    "tdcc_stealth_accumulation": "TDCC為加分與追蹤項，不可單獨作為買進理由；若價格跌破支撐或量價失敗需降風險。",
    "tdcc_short_continuation": "以訊號日隔天開盤為進場假設，後續依D+5 / D+10統計結果與價格轉弱條件管理。",
    "tdcc_short_term_continuation_d5_d10": "以訊號日隔天開盤為進場假設，後續依D+5 / D+10統計結果與價格轉弱條件管理。",
    "short_term_surge_d5_d10": "這是短線研究補充，不是低位買進模型；需用隔天開盤與D+N收盤 / 最高價統計管理。",
}

FORBIDDEN_PDF_TOKENS = [
    "call_strong_inflow",
    "call_put_bullish",
    "strong_accumulation",
    "mild_accumulation",
    "short_term_specialty",
    "range_rebound",
    "hot_theme_tag",
    "hot theme tag",
    "non_mainstream",
    "mainstream",
    "neckline",
]
RAW_PDF_TOKEN_RE = re.compile(r"(^|[\s|/、,;])([a-z]+(?:_[a-z0-9]+){1,})(?=$|[\s|/、,;])")


REPORT_MODEL_ID_ALIASES = {
    "volume_breakout_range": "volume_range_breakout",
    "tdcc_short_continuation": "tdcc_short_term_continuation_d5_d10",
}


def clean_join_unique(values: Iterable[Any], sep: str = " / ") -> str:
    seen: list[str] = []
    for value in values:
        raw = safe_str(value)
        if not raw or raw.lower() in {"nan", "none"}:
            continue
        for piece in re.split(r"[|,;/、]+", raw):
            item = piece.strip()
            if item and item not in seen:
                seen.append(item)
    return sep.join(seen)


def translate_pdf_text(value: Any) -> str:
    text_value = safe_str(value)
    if not text_value:
        return ""
    out = text_value
    for src in sorted(PDF_TOKEN_ZH, key=len, reverse=True):
        out = re.sub(rf"(?<![A-Za-z0-9_]){re.escape(src)}(?![A-Za-z0-9_])", PDF_TOKEN_ZH[src], out)
    return out


def zh_or_clean(value: Any, fallback: str = "欄位尚未完成 / 暫用現有資料") -> str:
    raw = safe_str(value).strip()
    if not raw:
        return fallback
    translated = translate_pdf_text(raw).strip()
    if any(token in translated for token in FORBIDDEN_PDF_TOKENS) or RAW_PDF_TOKEN_RE.search(translated):
        return fallback
    return translated


def zh_tag_list_clean(value: Any, mapping: dict[str, str] | None = None, fallback: str = "") -> str:
    raw = safe_str(value)
    if not raw:
        return fallback
    mapping = mapping or {}
    labels: list[str] = []
    for item in re.split(r"[|,;/、]+", raw):
        key = item.strip()
        if not key:
            continue
        label = mapping.get(key) or PDF_TOKEN_ZH.get(key) or translate_pdf_text(key)
        if RAW_PDF_TOKEN_RE.search(label):
            label = "欄位尚未完成 / 暫用現有資料"
        if label and label not in labels:
            labels.append(label)
    return " / ".join(labels) if labels else fallback


def clean_model_name_zh(row: pd.Series) -> str:
    model_id = safe_str(row.get("model_id", ""))
    existing = safe_str(row.get("model_name_zh", ""))
    if model_id in MODEL_NAME_ZH_BY_ID:
        return MODEL_NAME_ZH_BY_ID[model_id]
    cleaned = translate_pdf_text(existing)
    if cleaned and has_cjk(cleaned) and not any(token in cleaned for token in FORBIDDEN_PDF_TOKENS):
        return cleaned
    return MODEL_NAME_ZH_BY_ID.get(model_id, "欄位尚未完成 / 暫用現有資料")


def build_why_selected_human_zh(row: pd.Series) -> str:
    model_id = safe_str(row.get("model_id", ""))
    base = MODEL_HUMAN_REASON_ZH.get(model_id)
    if not base:
        model_name = clean_model_name_zh(row)
        base = f"符合{model_name}，主條件已成立，後續依模型規則與風險欄位管理。"
    additions: list[str] = []
    tdcc = safe_str(row.get("tdcc_status", "")).lower()
    if tdcc in {"strong_accumulation", "mild_accumulation"}:
        additions.append("大戶籌碼正向。")
    warrant = safe_str(row.get("warrant_flow_signal", "")).lower()
    if warrant in {"call_strong_inflow", "call_inflow", "call_put_bullish"}:
        additions.append("權證偏多。")
    theme = safe_str(row.get("effective_primary_theme", ""))
    if theme and theme.lower() not in {"unclassified", "unknown", "nan"}:
        additions.append("具族群題材。")
    return base + ("".join(additions) if additions else "")


def build_operation_reminder_zh(row: pd.Series) -> str:
    model_id = safe_str(row.get("model_id", ""))
    if model_id in MODEL_OPERATION_REMINDER_ZH:
        return MODEL_OPERATION_REMINDER_ZH[model_id]
    for col in ["operation_reminder_zh", "recommended_usage_zh", "next_confirmation_zh", "risk_tags_zh"]:
        raw = safe_str(row.get(col, ""))
        if raw and raw != "欄位尚未完成" and not any(token in raw for token in FORBIDDEN_PDF_TOKENS):
            return translate_pdf_text(raw)
    return MODEL_OPERATION_REMINDER_ZH.get(
        model_id,
        "依模型主條件入選；後續依23EMA、支撐壓力、量價與風險標籤管理。",
    )


def same_model_repeat_status_zh(value: Any) -> str:
    raw = safe_str(value)
    if raw == "new_model_signal":
        return "新進榜"
    if raw == "repeated_same_model_signal":
        return "重複進榜"
    return "欄位尚未完成 / 暫用現有資料"


def same_model_repeat_note_zh(row: pd.Series) -> str:
    status = safe_str(row.get("same_model_repeat_status", ""))
    if status == "new_model_signal":
        return "本模型新進榜，列入新進榜排名。"
    if status == "repeated_same_model_signal":
        days = safe_str(row.get("same_model_consecutive_days", "")) or "0"
        count5 = safe_str(row.get("same_model_appear_count_5d", "")) or "0"
        count10 = safe_str(row.get("same_model_appear_count_10d", "")) or "0"
        return f"同一模型連續上榜{days}天，5日出現{count5}次，10日出現{count10}次，列入重複進榜表。"
    return "欄位尚未完成 / 暫用現有資料"


def build_report_ready_model_signals(signals: pd.DataFrame) -> pd.DataFrame:
    """Build a PDF-ready table: one row per report_line + model_id + stock_id."""
    if signals.empty:
        return signals.copy()

    work = signals.copy()
    for col in [
        "signal_date",
        "report_bucket",
        "model_id",
        "model_name_zh",
        "stock_id",
        "stock_name",
        "model_score",
        "model_rank",
        "original_category",
        "source_row_index",
        "next_confirmation",
        "score_components",
        "risk_penalty_tags",
    ]:
        if col not in work.columns:
            work[col] = ""

    work["report_line"] = work["report_bucket"].astype(str).where(
        work["report_bucket"].astype(str).isin(["mainstream", "non_mainstream"]),
        "non_mainstream",
    )
    work["_canonical_model_id"] = work["model_id"].astype(str).map(lambda value: REPORT_MODEL_ID_ALIASES.get(value, value))
    work["_rank_num"] = pd.to_numeric(work["model_rank"], errors="coerce").fillna(999999)
    work["_score_num"] = pd.to_numeric(work["model_score"], errors="coerce").fillna(-999999)
    work = work.sort_values(
        ["report_line", "_canonical_model_id", "stock_id", "_rank_num", "_score_num"],
        ascending=[True, True, True, True, False],
    )

    grouped_rows: list[dict[str, Any]] = []
    for (_, _, _), part in work.groupby(["report_line", "_canonical_model_id", "stock_id"], dropna=False, sort=False):
        best = part.iloc[0].copy()
        row = best.to_dict()
        row["report_bucket"] = row.get("report_line", row.get("report_bucket", ""))
        row["model_id"] = safe_str(row.get("_canonical_model_id")) or safe_str(row.get("model_id"))
        row["merged_same_model_source_count"] = int(len(part))
        row["source_hit_count"] = int(len(part))
        row["merged_model_ids"] = clean_join_unique(part["model_id"])
        row["merged_source_row_indices"] = clean_join_unique(part["source_row_index"])
        row["source_row_indices"] = row["merged_source_row_indices"]
        row["merged_source_categories"] = clean_join_unique(part["original_category"])
        row["merged_source_categories_zh"] = zh_tag_list_clean(row["merged_source_categories"], CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料")
        row["source_hit_labels"] = row["merged_source_categories"]
        row["source_hit_labels_zh"] = row["merged_source_categories_zh"]
        row["merged_next_confirmations"] = clean_join_unique(part["next_confirmation"])
        row["merged_score_components"] = clean_join_unique(part["score_components"])
        row["merged_risk_penalty_tags"] = clean_join_unique(part["risk_penalty_tags"])
        row["report_model_key"] = row["model_id"] or safe_str(best.get("model_name_zh"))
        grouped_rows.append(row)

    out = pd.DataFrame(grouped_rows).drop(columns=["_rank_num", "_score_num", "_canonical_model_id"], errors="ignore")
    out["_score_num"] = pd.to_numeric(out["model_score"], errors="coerce").fillna(0)
    out = out.sort_values(["report_line", "model_id", "_score_num", "stock_id"], ascending=[True, True, False, True]).reset_index(drop=True)
    out["model_rank"] = out.groupby(["report_line", "model_id"], dropna=False).cumcount() + 1
    out["display_rank"] = out["model_rank"].astype(str)
    return out.drop(columns=["_score_num"], errors="ignore")


def apply_display_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    out = df.copy()

    if "report_line" not in out.columns:
        out["report_line"] = column_or_default(out, "report_bucket")
    out["report_line"] = out["report_line"].astype(str).where(out["report_line"].astype(str).isin(["mainstream", "non_mainstream"]), "non_mainstream")
    out["report_bucket"] = out["report_line"].where(column_or_default(out, "report_bucket").eq(""), column_or_default(out, "report_bucket"))
    out["model_name_zh"] = out.apply(clean_model_name_zh, axis=1)
    out["report_bucket_zh"] = out["report_line"].map({"mainstream": "主流", "non_mainstream": "非主流"}).fillna("非主流")
    out["source_category_zh"] = column_or_default(out, "original_category").map(lambda value: zh_tag_list_clean(value, CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料"))
    out["effective_primary_theme_zh"] = column_or_default(out, "effective_primary_theme").map(lambda value: zh_or_clean(value))
    out["effective_structural_theme_bucket_zh"] = column_or_default(out, "effective_structural_theme_bucket").map(lambda value: zh_or_clean(value))
    out["tdcc_status_zh"] = column_or_default(out, "tdcc_status").map(lambda value: zh_tag_list_clean(value, TDCC_STATUS_ZH, "欄位尚未完成 / 暫用現有資料"))
    out["warrant_flow_signal_zh"] = column_or_default(out, "warrant_flow_signal").map(lambda value: zh_tag_list_clean(value, WARRANT_SIGNAL_ZH, "欄位尚未完成 / 暫用現有資料"))
    out["risk_tags_zh"] = column_or_default(out, "risk_penalty_tags").where(column_or_default(out, "risk_penalty_tags").ne(""), column_or_default(out, "risk_tags")).map(lambda value: zh_tag_list_clean(value, RISK_TAG_ZH, "依模型風險欄位管理"))
    out["downgrade_flags_zh"] = column_or_default(out, "downgrade_flags").where(column_or_default(out, "downgrade_flags").ne(""), column_or_default(out, "merged_risk_penalty_tags")).map(lambda value: zh_tag_list_clean(value, RISK_TAG_ZH, "無明確降級旗標"))
    out["next_confirmation_zh"] = column_or_default(out, "merged_next_confirmations").where(column_or_default(out, "merged_next_confirmations").ne(""), column_or_default(out, "next_confirmation")).map(lambda value: zh_or_clean(value, "依23EMA、支撐壓力與量價延續確認"))
    out["recommended_usage_zh"] = column_or_default(out, "model_operation_guidance").where(column_or_default(out, "model_operation_guidance").ne(""), column_or_default(out, "recommended_usage")).map(lambda value: zh_or_clean(value, "依模型主條件與風控條件執行"))
    out["score_components_zh"] = column_or_default(out, "score_components").where(column_or_default(out, "score_components").ne(""), column_or_default(out, "merged_score_components")).map(score_components_zh).map(translate_pdf_text)
    out["why_selected_human_zh"] = out.apply(build_why_selected_human_zh, axis=1)
    out["why_selected_zh"] = out["why_selected_human_zh"]
    if "source_hit_labels_zh" not in out.columns:
        out["source_hit_labels_zh"] = column_or_default(out, "merged_source_categories").map(lambda value: zh_tag_list_clean(value, CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料"))
    else:
        out["source_hit_labels_zh"] = out["source_hit_labels_zh"].where(
            out["source_hit_labels_zh"].astype(str).str.strip().ne(""),
            column_or_default(out, "merged_source_categories").map(lambda value: zh_tag_list_clean(value, CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料")),
        ).map(translate_pdf_text)
    out["merged_source_categories_zh"] = column_or_default(out, "merged_source_categories").map(lambda value: zh_tag_list_clean(value, CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料"))
    out["operation_reminder_zh"] = out.apply(build_operation_reminder_zh, axis=1)
    out["same_model_repeat_status_zh"] = column_or_default(out, "same_model_repeat_status").map(same_model_repeat_status_zh)
    out["same_model_repeat_note_zh"] = out.apply(same_model_repeat_note_zh, axis=1)
    if "frontpage_duplicate_reason" in out.columns:
        out["frontpage_duplicate_reason_zh"] = column_or_default(out, "frontpage_duplicate_reason").map(lambda value: PDF_TOKEN_ZH.get(safe_str(value), translate_pdf_text(value)))
    return out


def attach_report_contract_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    out = df.copy()
    out["report_line"] = column_or_default(out, "report_line").where(
        column_or_default(out, "report_line").isin(["mainstream", "non_mainstream"]),
        column_or_default(out, "report_bucket").where(column_or_default(out, "report_bucket").isin(["mainstream", "non_mainstream"]), "non_mainstream"),
    )
    out["display_rank"] = column_or_default(out, "display_rank").where(column_or_default(out, "display_rank").ne(""), column_or_default(out, "model_rank"))
    out["source_hit_count"] = column_or_default(out, "merged_same_model_source_count", "1")
    out["source_hit_labels"] = column_or_default(out, "merged_source_categories")
    out["source_row_indices"] = column_or_default(out, "merged_source_row_indices")
    out["why_selected"] = column_or_default(out, "why_selected_human_zh")
    out["risk_tags"] = column_or_default(out, "merged_risk_penalty_tags").where(column_or_default(out, "merged_risk_penalty_tags").ne(""), column_or_default(out, "risk_penalty_tags"))
    out["downgrade_flags"] = column_or_default(out, "downgrade_flags").where(column_or_default(out, "downgrade_flags").ne(""), column_or_default(out, "risk_tags"))
    if "merged_same_model_source_count" not in out.columns:
        out["merged_same_model_source_count"] = "1"
    if "merged_source_categories_zh" not in out.columns:
        out["merged_source_categories_zh"] = column_or_default(out, "merged_source_categories").map(lambda value: zh_tag_list_clean(value, CATEGORY_ZH, "欄位尚未完成 / 暫用現有資料"))

    tdcc_rows = [latest_tdcc_summary(stock_id) for stock_id in column_or_default(out, "stock_id")]
    tdcc_df = pd.DataFrame(tdcc_rows, index=out.index)
    for col in tdcc_df.columns:
        out[col] = tdcc_df[col]
    out = apply_display_columns(out)
    for col in [
        "why_selected_human_zh",
        "operation_reminder_zh",
        "risk_tags_zh",
        "next_confirmation_zh",
        "recommended_usage_zh",
        "source_hit_labels_zh",
    ]:
        out[col] = column_or_default(out, col).replace("", "欄位尚未完成 / 暫用現有資料")
    return out



ROTATION_COLUMNS = [
    "signal_date",
    "rotation_model_id",
    "rotation_model_name",
    "theme",
    "stock_count",
    "volume_expansion_3x_count",
    "volume_expansion_1_5x_count",
    "volume_expansion_ratio",
    "slow_inflow_count",
    "slow_inflow_ratio",
    "median_volume_ratio",
    "median_return_15d",
    "median_return_30d",
    "leader_1",
    "leader_2",
    "leader_3",
    "diffusion_status_zh",
    "interpretation_zh",
    "interpretation",
]


def build_rotation(candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    taxonomy = read_csv(STOCK_THEME_TAXONOMY, dtype={"stock_id": str})
    if taxonomy.empty:
        return pd.DataFrame(columns=ROTATION_COLUMNS)

    def rotation_themes(item: pd.Series) -> list[str]:
        """Return all usable group labels for fund-rotation detection.

        A stock can participate in its basic listed-company industry group and
        in one or more market-theme groups.  Using only primary_theme hides
        cases like wire/cable stocks that are part of a broader slow-inflow
        group but also have a narrower provisional hot theme.
        """
        values: list[str] = []
        for key in (
            "hot_primary_theme",
            "primary_theme",
            "basic_theme",
            "industry",
        ):
            value = safe_str(item.get(key))
            if value:
                values.append(value)
        for key in ("hot_secondary_themes", "secondary_themes"):
            values.extend(split_tags(safe_str(item.get(key))))

        cleaned: list[str] = []
        seen: set[str] = set()
        skip = {"other", "theme_unknown", "unclassified", "needs_manual_review"}
        for value in values:
            theme = safe_str(value)
            if not theme or theme in skip or theme in seen:
                continue
            seen.add(theme)
            cleaned.append(theme)
        return cleaned

    # Group rotation must evaluate the whole taxonomy universe, not only rows
    # that already passed another candidate model. This catches slow theme inflow
    # before all members become individual candidates.
    rows_for_group: list[dict[str, Any]] = []
    for _, item in taxonomy.iterrows():
        stock_id = normalize_code(item.get("stock_id", ""))
        if not stock_id:
            continue
        hist = price_history_for_stock(stock_id)
        if hist.empty:
            continue
        hist = hist[hist["date"].astype(str) <= signal_date].copy()
        if len(hist) < 35:
            continue
        latest = hist.iloc[-1]
        close = float(latest.get("close", math.nan))
        vol = float(latest.get("volume", math.nan))
        vol_ma20 = float(latest.get("volume_ma20", math.nan))
        if math.isnan(vol_ma20) or vol_ma20 <= 0:
            vol_ma20 = float(hist["volume"].tail(20).mean())
        volume_ratio_num = vol / vol_ma20 if vol_ma20 and not math.isnan(vol) else math.nan

        recent15 = hist.tail(15)
        prev20 = hist.iloc[max(0, len(hist) - 35) : max(0, len(hist) - 15)]
        recent15_vol = float(recent15["volume"].mean()) if len(recent15) else math.nan
        prev20_vol = float(prev20["volume"].mean()) if len(prev20) else math.nan
        slow_volume_ratio = recent15_vol / prev20_vol if prev20_vol and not math.isnan(recent15_vol) else math.nan
        close_15_ago = float(hist["close"].iloc[-16]) if len(hist) >= 16 else math.nan
        close_30_ago = float(hist["close"].iloc[-31]) if len(hist) >= 31 else math.nan
        return_15d = (close / close_15_ago - 1) * 100 if close_15_ago and not math.isnan(close) else math.nan
        return_30d = (close / close_30_ago - 1) * 100 if close_30_ago and not math.isnan(close) else math.nan

        for theme in rotation_themes(item):
            rows_for_group.append(
                {
                    "stock_id": stock_id,
                    "stock_name": safe_str(item.get("stock_name")),
                    "theme": theme,
                    "volume_ratio_num": volume_ratio_num,
                    "slow_volume_ratio": slow_volume_ratio,
                    "return_15d": return_15d,
                    "return_30d": return_30d,
                }
            )

    work = pd.DataFrame(rows_for_group)
    if work.empty:
        return pd.DataFrame(columns=ROTATION_COLUMNS)
    work = work.drop_duplicates(["stock_id", "theme"]).reset_index(drop=True)
    work["is_volume_expansion_3x"] = work["volume_ratio_num"] >= 3
    work["is_volume_expansion_1_5x"] = work["volume_ratio_num"] >= 1.5
    work["is_slow_inflow"] = (
        (work["slow_volume_ratio"] >= 1.15)
        & (work["return_15d"].fillna(0) >= 0)
        & (work["return_30d"].fillna(0) >= -5)
    )

    rows: list[dict[str, Any]] = []
    for theme, part in work.groupby("theme", dropna=False):
        theme_text = safe_str(theme)
        if not theme_text or theme_text in {"other", "theme_unknown", "unclassified"}:
            continue
        total = len(part)
        if total < 2:
            continue
        expansion = int(part["is_volume_expansion_3x"].sum())
        expansion_15 = int(part["is_volume_expansion_1_5x"].sum())
        ratio = expansion / total if total else 0
        slow_count = int(part["is_slow_inflow"].sum())
        slow_ratio = slow_count / total if total else 0
        median_volume_ratio = float(part["volume_ratio_num"].median(skipna=True))
        median_return_15d = float(part["return_15d"].median(skipna=True))
        median_return_30d = float(part["return_30d"].median(skipna=True))

        launch_ok = ratio >= 1 / 3
        slow_ok = total >= 3 and slow_ratio >= 1 / 3 and expansion_15 >= max(1, math.ceil(total * 0.2))
        if not launch_ok and not slow_ok:
            continue

        def add_row(model_id: str, model_name: str, diffusion_status: str, interpretation: str) -> None:
            leaders = (
                part.sort_values("volume_ratio_num", ascending=False)
                .head(3)[["stock_id", "stock_name", "volume_ratio_num"]]
                .fillna("")
                .to_dict("records")
            )
            rows.append(
                {
                    "signal_date": signal_date,
                    "rotation_model_id": model_id,
                    "rotation_model_name": model_name,
                    "theme": theme,
                    "stock_count": total,
                    "volume_expansion_3x_count": expansion,
                    "volume_expansion_1_5x_count": expansion_15,
                    "volume_expansion_ratio": round(ratio, 4),
                    "slow_inflow_count": slow_count,
                    "slow_inflow_ratio": round(slow_ratio, 4),
                    "median_volume_ratio": round(median_volume_ratio, 4) if not math.isnan(median_volume_ratio) else "",
                    "median_return_15d": round(median_return_15d, 4) if not math.isnan(median_return_15d) else "",
                    "median_return_30d": round(median_return_30d, 4) if not math.isnan(median_return_30d) else "",
                    "leader_1": f"{leaders[0].get('stock_id','')} {leaders[0].get('stock_name','')}" if len(leaders) > 0 else "",
                    "leader_2": f"{leaders[1].get('stock_id','')} {leaders[1].get('stock_name','')}" if len(leaders) > 1 else "",
                    "leader_3": f"{leaders[2].get('stock_id','')} {leaders[2].get('stock_name','')}" if len(leaders) > 2 else "",
                    "diffusion_status_zh": diffusion_status,
                    "interpretation_zh": interpretation,
                    "interpretation": interpretation,
                }
            )

        if launch_ok:
            add_row(
                "group_fund_rotation_launch",
                "\u65cf\u7fa4\u8cc7\u91d1\u767c\u52d5\u578b",
                "\u540c\u6b65\u51fa\u91cf",
                "\u540c\u65cf\u7fa4\u8d85\u904e\u4e09\u5206\u4e4b\u4e00\u6210\u54e1\u91cf\u6bd4\u5927\u65bc\u7b49\u65bc3\uff0c\u5c6c\u65bc\u8cc7\u91d1\u540c\u6b65\u767c\u52d5\u89c0\u5bdf\u3002",
            )
        if slow_ok:
            add_row(
                "group_slow_inflow_rotation",
                "\u65cf\u7fa4\u6162\u901f\u8cc7\u91d1\u9032\u5165\u578b",
                "\u6162\u901f\u9032\u5834",
                "15\u65e5\u91cf\u80fd\u76f8\u5c0d\u524d\u6bb5\u653e\u5927\u4e14\u65cf\u7fa4\u5167\u591a\u6a94\u6b63\u5831\u916c\uff0c\u5c6c\u65bc\u8cc7\u91d1\u7de9\u6162\u9032\u5834\u89c0\u5bdf\uff1b\u9700\u7b49\u500b\u80a1\u6a21\u578b\u89f8\u767c\u624d\u80fd\u6210\u70ba\u9032\u5834\u4f9d\u64da\u3002",
            )

    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=ROTATION_COLUMNS)
    return out.sort_values(
        ["rotation_model_id", "volume_expansion_ratio", "slow_inflow_ratio", "volume_expansion_3x_count", "theme"],
        ascending=[True, False, False, False, True],
    ).reset_index(drop=True)


def write_md_table(path: Path, title: str, df: pd.DataFrame, intro: list[str] | None = None, limit: int = 80) -> None:
    lines = [f"# {title}", "", f"- generated_at: `{now_text()}`", ""]
    if intro:
        lines.extend(intro)
        lines.append("")
    if df.empty:
        lines.append("_No rows._")
    else:
        lines.append(df.head(limit).to_markdown(index=False))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_packet(
    params: pd.DataFrame,
    signals: pd.DataFrame,
    frontpage_unique: pd.DataFrame,
    same_model_repeat: pd.DataFrame,
    rotation: pd.DataFrame,
    signal_date: str,
) -> None:
    lines = [
        "# DAILY CANDIDATE MODEL LAYER PACKET",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{signal_date}`",
        "- contract: model main condition met means the stock enters that model candidate list.",
        "- scoring: risk, TDCC, warrant, revenue, position, and structure adjust rank inside the model; mainstream/non-mainstream only splits reports.",
        "- PDF rule: do not hard-code model count; render model sections from `daily_candidate_model_signals_for_report_latest.csv` and parameters from `daily_candidate_model_parameters_latest.md`.",
        "- Front-page rule: use `daily_candidate_frontpage_unique_latest.csv/md` for first-page representatives. This table contains new same-model signals only; repeated same-model appearances are intentionally excluded.",
        "- Repeat rule: same-stock same-model repeat appearances are not score penalties. Use `daily_candidate_same_model_repeat_latest.csv/md` as a separate persistence table. Revenue pullback or unreacted-revenue names can reasonably persist; volume-breakout repeats should be reviewed for breakout hold/failure quality.",
        "",
        "## Model Parameters",
        "",
        params[
            [
                "model_id",
                "model_name_zh",
                "pdf_visibility",
                "entry_basis",
                "recommended_usage",
                "recommended_close_exit_horizon",
                "best_close_win_rate_pct",
                "best_avg_close_return_pct",
                "main_conditions",
            ]
        ].to_markdown(index=False),
        "",
        "## Signal Counts",
        "",
    ]
    if signals.empty:
        lines.append("_No model signals._")
    else:
        counts = signals.groupby(["model_id", "model_name_zh", "report_bucket"], dropna=False).size().reset_index(name="count")
        lines.append(counts.to_markdown(index=False))
    lines.extend(["", "## Front Page Unique Representatives", ""])
    if frontpage_unique.empty:
        lines.append("_No front-page rows._")
    else:
        cols = [
            "frontpage_unique_rank",
            "report_bucket_zh",
            "display_rank_new_signal",
            "stock_id",
            "stock_name",
            "effective_primary_theme_zh",
            "primary_model_name_zh",
            "primary_model_score",
            "model_rank_new_signal",
            "model_hit_count",
            "model_hits",
            "same_model_repeat_status_zh",
            "same_model_repeat_note_zh",
            "same_model_consecutive_days",
            "risk_tags_zh",
            "next_confirmation_zh",
        ]
        available_cols = [col for col in cols if col in frontpage_unique.columns]
        lines.append(frontpage_unique[available_cols].head(60).to_markdown(index=False))
    lines.extend(["", "## Same Model Repeat Table", ""])
    if same_model_repeat.empty:
        lines.append("_No same-model repeat rows yet._")
    else:
        cols = [
            "same_model_repeat_rank",
            "display_rank_repeated_signal",
            "report_bucket_zh",
            "model_id",
            "model_name_zh",
            "stock_id",
            "stock_name",
            "same_model_repeat_status_zh",
            "same_model_repeat_note_zh",
            "same_model_consecutive_days",
            "same_model_appear_count_5d",
            "same_model_appear_count_10d",
            "model_rank_overall",
            "model_rank_repeated_signal",
            "model_score",
            "effective_primary_theme_zh",
            "next_confirmation_zh",
        ]
        available_cols = [col for col in cols if col in same_model_repeat.columns]
        lines.append(same_model_repeat[available_cols].head(80).to_markdown(index=False))
    lines.extend(["", "## Group Rotation", ""])
    if rotation.empty:
        lines.append("_No group rotation rows._")
    else:
        lines.append(rotation.head(30).to_markdown(index=False))
    PACKET_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    preferred_date = main_price_date_from_freshness()
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    candidates = enrich_candidates_with_taxonomy(candidates)
    signal_date, date_notes = resolve_candidate_signal_date(candidates, preferred_date)
    if not signal_date:
        signal_date = preferred_date
    for note in date_notes:
        print(f"date_note: {note}")
    specs = build_specs()
    recommendations = load_model_recommendations()
    params = build_parameter_table(specs)
    if not recommendations.empty:
        params = params.merge(recommendations, on="model_id", how="left")
        for col in RECOMMENDATION_COLUMNS:
            if col not in params.columns:
                params[col] = ""
            params[col] = params[col].fillna("")
    write_csv(params, PARAMETERS_CSV)
    write_md_table(
        PARAMETERS_MD,
        "Daily Candidate Model Parameters",
        params,
        [
            "- This is the readable parameter source for daily candidate models.",
            "- Main conditions select candidates into a model. Add-score items rank candidates inside that model.",
            "- Mainstream/non-mainstream is a report split, not a score cap or veto.",
        ],
        limit=200,
    )

    signals = build_signals(candidates, specs, signal_date)
    signals = append_volume_breakout_signals(signals, candidates, signal_date)
    signals = append_tdcc_short_term(signals, signal_date)
    signals = attach_model_recommendations(signals, recommendations)
    signals = apply_display_columns(signals)
    report_signals = build_report_ready_model_signals(signals)
    model_log = update_model_signal_log(report_signals)
    report_signals, same_model_repeat = attach_same_model_repeat(report_signals, model_log)
    report_signals = annotate_frontpage_uniqueness(report_signals)
    report_signals = apply_display_columns(report_signals)
    report_signals = attach_report_contract_columns(report_signals)
    report_signals = apply_display_columns(report_signals)
    same_model_repeat = apply_display_columns(same_model_repeat)
    frontpage_unique = build_frontpage_unique(report_signals)
    frontpage_unique = apply_display_columns(frontpage_unique)
    write_csv(signals, SIGNALS_CSV)
    write_md_table(
        SIGNALS_MD,
        "Daily Candidate Model Signals",
        signals,
        [
            "- One stock can appear in multiple models.",
            "- `model_rank` ranks within model and report bucket.",
            "- `selection_semantics` explicitly prevents selected rows from being rewritten as contradictory no-buy rows.",
        ],
        limit=300,
    )
    write_csv(report_signals, REPORT_SIGNALS_CSV)
    write_md_table(
        REPORT_SIGNALS_MD,
        "Daily Candidate Model Signals For Report",
        report_signals,
        [
            "- Use this table for PDF model sections.",
            "- Contract: one row per report bucket + displayed model + stock.",
            "- If one stock hit the same displayed model through several source categories, merged_* columns preserve that context.",
        ],
        limit=300,
    )
    write_csv(frontpage_unique, FRONTPAGE_UNIQUE_CSV)
    write_md_table(
        FRONTPAGE_UNIQUE_MD,
        "Daily Candidate Front Page Unique Representatives",
        frontpage_unique,
        [
            "- Use this table for the first page of curated PDFs.",
            "- A stock can hit multiple models, but the first page should show it once per report bucket.",
            "- `model_hits` preserves the full multi-model context; complete model lists remain in `daily_candidate_model_signals_latest.csv`.",
        ],
        limit=120,
    )
    write_csv(same_model_repeat, MODEL_REPEAT_CSV)
    write_md_table(
        MODEL_REPEAT_MD,
        "Daily Candidate Same Model Repeat Table",
        same_model_repeat,
        [
            "- Same-stock same-model repeat appearances are persistence information, not score penalties.",
            "- Main curated tables can prefer new model signals; use this table to rank repeated same-model signals separately.",
            "- Counts are based on accumulated `output/history/daily_candidate_models/daily_candidate_model_signal_log.csv` snapshots.",
        ],
        limit=160,
    )

    rotation = build_rotation(candidates, signal_date)
    write_csv(rotation, ROTATION_CSV)
    write_md_table(
        ROTATION_MD,
        "Daily Candidate Group Rotation",
        rotation,
        [
            "- This is theme flow detection, not a stock buy model.",
            "- Condition: same theme has at least one third of listed candidate rows with volume ratio >= 3x.",
        ],
        limit=80,
    )
    write_packet(params, report_signals, frontpage_unique, same_model_repeat, rotation, signal_date)
    print(f"Saved: {PARAMETERS_CSV}")
    print(f"Saved: {PARAMETERS_MD}")
    print(f"Saved: {SIGNALS_CSV} rows={len(signals)}")
    print(f"Saved: {SIGNALS_MD}")
    print(f"Saved: {REPORT_SIGNALS_CSV} rows={len(report_signals)}")
    print(f"Saved: {REPORT_SIGNALS_MD}")
    print(f"Saved: {FRONTPAGE_UNIQUE_CSV} rows={len(frontpage_unique)}")
    print(f"Saved: {FRONTPAGE_UNIQUE_MD}")
    print(f"Saved: {MODEL_SIGNAL_LOG_CSV} rows={len(model_log)}")
    print(f"Saved: {MODEL_REPEAT_CSV} rows={len(same_model_repeat)}")
    print(f"Saved: {MODEL_REPEAT_MD}")
    print(f"Saved: {ROTATION_CSV} rows={len(rotation)}")
    print(f"Saved: {ROTATION_MD}")
    print(f"Saved: {PACKET_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
