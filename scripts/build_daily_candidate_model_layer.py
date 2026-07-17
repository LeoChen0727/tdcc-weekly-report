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
DAILY_THEME_STATUS_HISTORY_CSVS = [
    Path("output/history/daily_signals/daily_theme_status_history.csv"),
    Path("output/history/daily_candidates/daily_theme_status_history.csv"),
]
TDCC_EDGE_CANDIDATES = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
TDCC_HOLDER_RATIO = LATEST_DIR / "tdcc_holder_ratio_latest.csv"
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


def latest_tdcc_signal_date() -> str:
    """Return the latest TDCC week available in current latest outputs."""
    df = read_csv(TDCC_HOLDER_RATIO, dtype=str, keep_default_na=False)
    if df.empty or "date" not in df.columns:
        return ""
    dates = [safe_str(v).strip() for v in df["date"].astype(str) if safe_str(v).strip()]
    return max(dates) if dates else ""


def filter_tdcc_edge_candidates_to_latest_week(df: pd.DataFrame) -> pd.DataFrame:
    """Do not let stale TDCC short-edge candidate rows leak into daily models."""
    if df.empty or "signal_date" not in df.columns:
        return df
    latest_tdcc = latest_tdcc_signal_date()
    if not latest_tdcc:
        return df
    dates = sorted({safe_str(v).strip() for v in df["signal_date"].astype(str) if safe_str(v).strip()})
    if dates == [latest_tdcc]:
        return df
    print(
        "WARNING: stale tdcc_overheated_short_term_edge_candidates_latest.csv ignored; "
        f"expected TDCC week {latest_tdcc}, got {dates}"
    )
    return df[df["signal_date"].astype(str).map(lambda v: safe_str(v).strip()) == latest_tdcc].copy()


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
LEGACY_VOLUME_RANGE_BREAKOUT_MODEL_ID = "volume_range_breakout"
VOLUME_BREAKOUT_V2_LOW_MODEL_ID = "volume_range_breakout_v2_low_position_volume_attack"
VOLUME_BREAKOUT_V2_MID_MODEL_ID = "volume_range_breakout_v2_mid_position_momentum_attack"
VOLUME_BREAKOUT_V2_HIGH_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
VOLUME_BREAKOUT_V2_MODEL_IDS = {
    VOLUME_BREAKOUT_V2_LOW_MODEL_ID,
    VOLUME_BREAKOUT_V2_MID_MODEL_ID,
    VOLUME_BREAKOUT_V2_HIGH_MODEL_ID,
}

DEPRECATED_DAILY_MODEL_IDS = {
    LEGACY_VOLUME_RANGE_BREAKOUT_MODEL_ID,
    "near_high_neckline_challenge",
    "platform_strengthening",
}


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
    "price_pullback_tdcc_distribution_penalty": "回檔模型TDCC轉弱扣分",
    "price_pullback_return20_over_25_no_bonus": "回檔模型20日漲幅過高未加分",
    "price_pullback_return20_negative_no_bonus": "回檔模型20日報酬偏弱未加分",
    "false_breakout_risk": "漲幅過低",
    "false_breakout_risk_penalty": "漲幅過低扣分",
    "tdcc_distribution_penalty": "TDCC轉弱扣分",
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
    "long_upper_shadow_quality_penalty": "長上影攻擊品質扣分",
    "A_bottom_volume_attack": "放量攻擊A級",
    "B_bottom_volume_attack_with_risk": "放量攻擊但有風險標籤",
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
    "base=70": "基礎分=70",
    "price_pullback_v1_required_gate": "23EMA回檔v1必要條件通過",
    "price_pullback_return20_0_25_required": "20日漲幅0%至25%",
    "price_pullback_tdcc_high_thresholds_up_required": "高門檻籌碼增加",
    "price_pullback_obv_above_ma20_required": "OBV高於20日均線",
    "price_pullback_technical_strength_package": "技術強勢組合",
    "price_pullback_tdcc_all_thresholds_up_reason_only": "籌碼全門檻同步改善",
    "price_pullback_tdcc_status:strong_accumulation": "回檔模型TDCC強吸籌",
    "price_pullback_tdcc_status:mild_accumulation": "回檔模型TDCC溫和吸籌",
    "price_pullback_strong_tdcc_accumulation": "回檔模型強TDCC加分",
    "price_pullback_large_holder_tdcc_confirmation": "回檔模型大戶級距確認",
    "price_pullback_return20_0_25": "回檔模型20日漲幅0到25%",
    "base=50": "基礎分=50",
    "base=35": "基礎分=35",
    "profile=volume_range_breakout_v2_low_position_volume_attack": "參數=低位放量攻擊",
    "profile=volume_range_breakout_v2_mid_position_momentum_attack": "參數=中位動能放量攻擊",
    "profile=volume_range_breakout_v2_high_position_volume_attack": "參數=高位階放量攻擊",
    "ma60_gt_ma120_required": "MA60大於MA120",
    "high_pos_bonus_volume_lt2": "高位階加分：量比低於2",
    "high_pos_bonus_signal_body_le3": "高位階加分：訊號K實體小於3%",
    "high_pos_bonus_breakout_2_5": "高位階加分：突破幅度2%到5%",
    "high_pos_bonus_close_location_le80": "高位階加分：收盤位置不過熱",
    "high_pos_bonus_not_limit_up_like": "高位階加分：非漲停鎖量型",
    "profile=price_pullback_23ema": "參數=股價回檔模型",
    "profile=hot_theme_pullback": "參數=熱門族群回檔模型",
    "profile=revenue_unreacted_range": "參數=營收爆發但股價尚未反應模型",
    "profile=w_bottom_right_side": "參數=W底右側模型",
    "profile=pullback_short_reclaim": "參數=回檔後短線轉強模型",
    "profile=tdcc_stealth_accumulation": "參數=TDCC潛伏吸籌模型",
    "platform/neckline breakout": "平台/頸線突破",
    "volume started expanding": "量能開始放大",
    "near neckline from below": "由下方接近頸線",
    "neckline just reclaimed": "剛站回頸線",
    "approaching neckline": "接近頸線",
    "breakout close near high": "突破K收盤接近日高",
    "type=neckline_volume_breakout": "類型=頸線帶量突破",
    "type=platform_volume_breakout": "類型=平台帶量突破",
    "type=range_breakout_volume": "類型=盤整區間帶量突破",
    "type=strict_high_breakout": "類型=波段高點帶量突破",
    "type=strict_60d_volume_breakout": "類型=60日高點帶量突破",
    "type=bottom_volume_attack": "類型=放量攻擊",
    "breakout_pct": "突破幅度",
    "close_ge_prior20_high_102pct": "收盤突破前20日高點2%以上",
    "volume_ma20_lots_ge_1000": "20日均量>=1000張",
    "close_above_mid_high": "收盤高於日內中高位",
    "breakout_magnitude": "突破幅度",
    "locked_limit_up_breakout": "鎖量漲停突破",
    "one_price_limit_up": "一價漲停",
    "locked_limit_no_volume_gate": "鎖量漲停不套用量能門檻",
    "close_near_day_high": "收盤接近日高",
    "close_high_position": "收盤位於日內高位",
    "strong_red_body": "實體紅K",
    "red_body_confirmed": "紅K確認",
    "base_width_controlled": "盤整寬度收斂",
    "base_width_acceptable": "盤整寬度可接受",
    "base_duration_20d_plus": "盤整20日以上",
    "base_duration_10d_plus": "盤整10日以上",
    "long_upper_shadow_quality_penalty": "長上影攻擊品質扣分",
    "volume_breakout_notes": "放量攻擊註記",
    "A_bottom_volume_attack": "放量攻擊A級",
    "B_bottom_volume_attack_with_risk": "放量攻擊但有風險標籤",
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
    "near 23EMA/support": "接近23EMA / 支撐",
    "EMA23 slope proxy up": "23EMA斜率向上",
    "pullback entry zone": "回檔買點區",
    "pullback not volume-chasing": "非追量買點",
    "pullback volume not chasing": "回檔量縮、不追高",
    "re-attack volume": "再攻量能",
    "price in 23-day range": "股價仍在23日整理區",
    "price still in recent range": "股價仍在近期整理區",
    "EPS confirmation tag": "EPS確認標籤",
    "catalyst tag": "催化標籤",
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


@dataclass(frozen=True)
class ScoreProfile:
    """Independent scoring parameters for one stock-selection model.

    Feature helpers can be shared, but parameter values must not be shared
    across models.  Backtests should tune these profiles one model at a time.
    """

    model_id: str
    base_score: float = 50.0
    volume_ratio_bonus_per_1x: float = 0.0
    volume_ratio_bonus_cap: float = 0.0
    tdcc_positive_bonus: float = 0.0
    warrant_bullish_bonus: float = 0.0
    strong_revenue_bonus: float = 0.0
    lower_position_bonus: float = 0.0
    lower_position_max_off_60d_low_pct: float = 25.0
    high_return_penalty_threshold_20d: float = math.inf
    high_return_penalty: float = 0.0
    tdcc_distribution_penalty: float = 0.0
    false_breakout_penalty: float = 0.0


MODEL_SCORE_PROFILES: dict[str, ScoreProfile] = {
    "volume_range_breakout_v2_low_position_volume_attack": ScoreProfile(
        "volume_range_breakout_v2_low_position_volume_attack",
        base_score=60.0,
        volume_ratio_bonus_per_1x=3.0,
        volume_ratio_bonus_cap=12.0,
        tdcc_positive_bonus=4.0,
        warrant_bullish_bonus=2.0,
        strong_revenue_bonus=2.0,
        lower_position_bonus=6.0,
        lower_position_max_off_60d_low_pct=50.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=4.0,
    ),
    "volume_range_breakout_v2_mid_position_momentum_attack": ScoreProfile(
        "volume_range_breakout_v2_mid_position_momentum_attack",
        base_score=58.0,
        volume_ratio_bonus_per_1x=3.0,
        volume_ratio_bonus_cap=12.0,
        tdcc_positive_bonus=4.0,
        warrant_bullish_bonus=2.0,
        strong_revenue_bonus=2.0,
        lower_position_bonus=0.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=4.0,
    ),
    "volume_range_breakout_v2_high_position_volume_attack": ScoreProfile(
        "volume_range_breakout_v2_high_position_volume_attack",
        base_score=60.0,
    ),
    "price_pullback_23ema": ScoreProfile(
        "price_pullback_23ema",
        base_score=70.0,
    ),
    "hot_theme_pullback": ScoreProfile(
        "hot_theme_pullback",
        volume_ratio_bonus_per_1x=1.0,
        volume_ratio_bonus_cap=5.0,
        tdcc_positive_bonus=8.0,
        warrant_bullish_bonus=5.0,
        strong_revenue_bonus=3.0,
        lower_position_bonus=4.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=4.0,
    ),
    "revenue_unreacted_range": ScoreProfile(
        "revenue_unreacted_range",
        volume_ratio_bonus_per_1x=1.0,
        volume_ratio_bonus_cap=5.0,
        tdcc_positive_bonus=6.0,
        warrant_bullish_bonus=3.0,
        strong_revenue_bonus=12.0,
        lower_position_bonus=6.0,
        high_return_penalty_threshold_20d=25.0,
        high_return_penalty=8.0,
        tdcc_distribution_penalty=8.0,
        false_breakout_penalty=4.0,
    ),
    "w_bottom_right_side": ScoreProfile(
        "w_bottom_right_side",
        volume_ratio_bonus_per_1x=1.5,
        volume_ratio_bonus_cap=6.0,
        tdcc_positive_bonus=6.0,
        warrant_bullish_bonus=3.0,
        strong_revenue_bonus=3.0,
        lower_position_bonus=0.0,
        high_return_penalty_threshold_20d=35.0,
        high_return_penalty=5.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=5.0,
    ),
    "neckline_volume_breakout_confirmation": ScoreProfile(
        "neckline_volume_breakout_confirmation",
        base_score=38.0,
        volume_ratio_bonus_per_1x=3.0,
        volume_ratio_bonus_cap=12.0,
        tdcc_positive_bonus=6.0,
        warrant_bullish_bonus=4.0,
        strong_revenue_bonus=4.0,
        lower_position_bonus=2.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=6.0,
    ),
    "pullback_short_reclaim": ScoreProfile(
        "pullback_short_reclaim",
        volume_ratio_bonus_per_1x=2.0,
        volume_ratio_bonus_cap=8.0,
        tdcc_positive_bonus=6.0,
        warrant_bullish_bonus=4.0,
        strong_revenue_bonus=3.0,
        lower_position_bonus=3.0,
        tdcc_distribution_penalty=6.0,
        false_breakout_penalty=4.0,
    ),
    "tdcc_stealth_accumulation": ScoreProfile(
        "tdcc_stealth_accumulation",
        volume_ratio_bonus_per_1x=0.5,
        volume_ratio_bonus_cap=3.0,
        tdcc_positive_bonus=14.0,
        warrant_bullish_bonus=2.0,
        strong_revenue_bonus=4.0,
        lower_position_bonus=7.0,
        high_return_penalty_threshold_20d=20.0,
        high_return_penalty=8.0,
        tdcc_distribution_penalty=12.0,
        false_breakout_penalty=4.0,
    ),
}

SCORE_COMPONENT_EXTRA_ZH_REPLACEMENTS = {
    "profile=volume_range_breakout_v2_low_position_volume_attack": "參數=低位放量攻擊",
    "profile=volume_range_breakout_v2_mid_position_momentum_attack": "參數=中位動能放量攻擊",
    "profile=volume_range_breakout_v2_high_position_volume_attack": "參數=高位階放量攻擊",
    "base=60": "基礎分60",
    "base=58": "基礎分58",
    "position_bucket_120d=low_pos_le40": "120日位階=低位",
    "position_bucket_120d=mid_pos_40_75": "120日位階=中位",
    "position_bucket_120d=high_pos_gt75": "120日位階=高位",
    "position_bucket_120d=unknown_position": "120日位階=資料不足",
    "shape_bucket=non_consolidation": "型態=非盤整",
    "shape_bucket=consolidation": "型態=盤整",
    "shape_bucket=wide_range": "型態=寬幅震盪",
    "low_pos_le40": "低位",
    "mid_pos_40_75": "中位",
    "high_pos_gt75": "高位",
    "unknown_position": "資料不足",
    "non_consolidation": "非盤整",
    "wide_range": "寬幅震盪",
    "consolidation": "盤整",
}


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


def split_tags(value: Any) -> list[str]:
    raw = safe_str(value)
    if not raw:
        return []
    for sep in [";", ",", "/", "、"]:
        raw = raw.replace(sep, "|")
    return [part.strip() for part in raw.split("|") if part.strip()]


def score_components_zh(value: Any) -> str:
    raw = safe_str(value)
    if not raw:
        return ""
    out = raw
    for src, dst in sorted(SCORE_COMPONENT_EXTRA_ZH_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        out = out.replace(src, dst)
    for src, dst in SCORE_COMPONENT_ZH_REPLACEMENTS.items():
        out = out.replace(src, dst)
    out = re.sub(r"\bbase=(\d+(?:\.\d+)?)\b", lambda match: f"基礎分{match.group(1)}", out)
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
        out.loc[new_sorted.index, "display_rank_new_signal"] = [f"新進榜 #{int(rank)}" for rank in ranks]

    if repeated_mask.any():
        repeated_sorted = out[repeated_mask].sort_values(
            ["report_bucket", "model_id", "_consec_num", "_count10_num", "_score_num", "_rank_num", "_stock_id_sort"],
            ascending=[True, True, False, False, False, True, True],
        )
        ranks = repeated_sorted.groupby(["report_bucket", "model_id"], dropna=False).cumcount() + 1
        out.loc[repeated_sorted.index, "model_rank_repeated_signal"] = ranks.astype(str).values
        out.loc[repeated_sorted.index, "display_rank_repeated_signal"] = [f"連續榜 #{int(rank)}" for rank in ranks]

    return out.drop(columns=["_score_num", "_rank_num", "_consec_num", "_count10_num", "_stock_id_sort"], errors="ignore")


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


def compact_date(value: Any) -> str:
    text_value = safe_str(value)
    if text_value.endswith(".0"):
        text_value = text_value[:-2]
    text_value = text_value.replace("-", "").replace("/", "")
    return text_value if len(text_value) == 8 and text_value.isdigit() else ""


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


@lru_cache(maxsize=65536)
def price_pullback_price_context(stock_id: str, signal_date: str) -> dict[str, Any]:
    price = price_history_for_stock(stock_id)
    signal_date = compact_date(signal_date)
    empty = {
        "rsi14": math.nan,
        "macd_hist": math.nan,
        "macd_hist_gt0": False,
        "obv": math.nan,
        "obv_ma20": math.nan,
        "obv_above_ma20": False,
    }
    if price.empty or not signal_date:
        return empty
    work = price.copy()
    work["date"] = work["date"].map(compact_date)
    work = work[work["date"].astype(str).le(signal_date)].copy()
    if work.empty:
        return empty
    for col in ["open", "high", "low", "close", "volume"]:
        if col in work.columns:
            work[col] = pd.to_numeric(work[col], errors="coerce")
    work = work.dropna(subset=["close"]).sort_values("date").reset_index(drop=True)
    if work.empty:
        return empty

    close = work["close"]
    ema12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    ema26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    macd_dif = ema12 - ema26
    macd_dea = macd_dif.ewm(span=9, adjust=False, min_periods=9).mean()
    work["macd_hist"] = macd_dif - macd_dea

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14, min_periods=14).mean()
    avg_loss = loss.rolling(14, min_periods=14).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    work["rsi14"] = 100 - (100 / (1 + rs))

    volume = pd.to_numeric(work.get("volume", pd.Series([0.0] * len(work))), errors="coerce").fillna(0.0)
    previous_close = close.shift(1)
    obv_direction = (close - previous_close).apply(lambda value: 1.0 if value > 0 else (-1.0 if value < 0 else 0.0))
    work["obv"] = (obv_direction * volume).cumsum()
    work["obv_ma20"] = work["obv"].rolling(20, min_periods=10).mean()

    latest = work.iloc[-1]
    macd_hist = to_number(latest.get("macd_hist", math.nan))
    rsi14 = to_number(latest.get("rsi14", math.nan))
    obv = to_number(latest.get("obv", math.nan))
    obv_ma20 = to_number(latest.get("obv_ma20", math.nan))
    return {
        "rsi14": rsi14,
        "macd_hist": macd_hist,
        "macd_hist_gt0": (not math.isnan(macd_hist)) and macd_hist > 0,
        "obv": obv,
        "obv_ma20": obv_ma20,
        "obv_above_ma20": (not math.isnan(obv)) and (not math.isnan(obv_ma20)) and obv > obv_ma20,
    }


@lru_cache(maxsize=65536)
def price_pullback_tdcc_context(stock_id: str, signal_date: str) -> dict[str, Any]:
    code = normalize_code(stock_id)
    signal_date = compact_date(signal_date)
    empty = {
        "tdcc_history_available": False,
        "tdcc_as_of_date": "",
        "high_thresholds_up": False,
        "all_thresholds_up": False,
    }
    if not code or not signal_date:
        return empty
    path = TDCC_STOCK_HISTORY_DIR / f"{code}.csv"
    if not path.exists():
        return empty
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return empty
    if df.empty or "as_of_date" not in df.columns:
        return empty
    df = df.copy()
    df["as_of_date"] = df["as_of_date"].map(compact_date)
    df = df[(df["as_of_date"] != "") & df["as_of_date"].le(signal_date)].copy()
    if df.empty:
        return empty
    row = df.sort_values("as_of_date").iloc[-1]
    return {
        "tdcc_history_available": True,
        "tdcc_as_of_date": safe_str(row.get("as_of_date")),
        "high_thresholds_up": truthy(row.get("high_thresholds_up")),
        "all_thresholds_up": truthy(row.get("all_thresholds_up")),
    }


def enrich_price_pullback_v1_context(candidates: pd.DataFrame, default_signal_date: str) -> pd.DataFrame:
    if candidates.empty or "stock_id" not in candidates.columns:
        return candidates
    out = candidates.copy()
    context_rows: list[dict[str, Any]] = []
    for _, row in out.iterrows():
        stock_id = normalize_code(text(row, "stock_id", "ticker"))
        signal_date = compact_date(text(row, "signal_date", "date", "main_price_date") or default_signal_date)
        price_ctx = price_pullback_price_context(stock_id, signal_date)
        tdcc_ctx = price_pullback_tdcc_context(stock_id, signal_date)
        context_rows.append(
            {
                "price_pullback_signal_date": signal_date,
                "price_pullback_rsi14": price_ctx["rsi14"],
                "price_pullback_macd_hist": price_ctx["macd_hist"],
                "price_pullback_macd_hist_gt0": bool_text(bool(price_ctx["macd_hist_gt0"])),
                "price_pullback_obv": price_ctx["obv"],
                "price_pullback_obv_ma20": price_ctx["obv_ma20"],
                "price_pullback_obv_above_ma20": bool_text(bool(price_ctx["obv_above_ma20"])),
                "price_pullback_tdcc_history_available": bool_text(bool(tdcc_ctx["tdcc_history_available"])),
                "price_pullback_tdcc_as_of_date": tdcc_ctx["tdcc_as_of_date"],
                "price_pullback_high_thresholds_up": bool_text(bool(tdcc_ctx["high_thresholds_up"])),
                "price_pullback_all_thresholds_up": bool_text(bool(tdcc_ctx["all_thresholds_up"])),
            }
        )
    context = pd.DataFrame(context_rows, index=out.index)
    for col in context.columns:
        out[col] = context[col]
    return out


def truthy(value: Any) -> bool:
    return safe_str(value).strip().lower() in {"true", "1", "yes", "y", "t"}


def flag(row: pd.Series, name: str) -> bool:
    return truthy(row.get(name, ""))


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    if math.isnan(value):
        return low
    return max(low, min(high, value))


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


def previous_close_price(row: pd.Series) -> float:
    return num(row, "previous_close", "prev_close", "close_prev", "close_1d_ago")


def previous_20d_high_ex_today(row: pd.Series) -> float:
    value = num(
        row,
        "previous_20d_high_ex_today",
        "prior_20d_high",
        "previous_20d_high",
        "high_20_ex_today",
    )
    today_high = num(row, "high")
    close = close_price(row)
    if not math.isnan(value) and not math.isnan(today_high) and not math.isnan(close):
        # If an upstream high_20 field appears to include today's spike, fall
        # back to the available platform high so today's bar cannot raise its
        # own breakout threshold.
        platform_high = num(row, "platform_high", "short_platform_high", "range_high")
        if value >= today_high * 0.999 and not math.isnan(platform_high) and platform_high < value:
            return platform_high
    return value


def volume_ma20_lots(row: pd.Series) -> float:
    value = num(row, "volume_ma20_lots", "avg_volume_20d_lots")
    if not math.isnan(value):
        return value
    value = num(row, "volume_ma20", "avg_volume_20d")
    if math.isnan(value):
        return math.nan
    # Repo price histories may carry shares while report tables usually carry
    # lots. Normalize only clearly share-scale values.
    return value / 1000.0 if value >= 100000 else value


def bottom_volume_attack_bullish_candle(row: pd.Series) -> bool:
    close = close_price(row)
    open_ = num(row, "open")
    prev_close = previous_close_price(row)
    if math.isnan(close) or math.isnan(open_):
        return False
    if close > open_:
        return True
    return close == open_ and not math.isnan(prev_close) and close > prev_close


def bottom_volume_attack_breakout_level(row: pd.Series) -> float:
    return previous_20d_high_ex_today(row)


def bottom_volume_attack_breakout_pct(row: pd.Series) -> float:
    close = close_price(row)
    level = bottom_volume_attack_breakout_level(row)
    if math.isnan(close) or math.isnan(level) or level <= 0:
        return math.nan
    return (close / level - 1) * 100


def daily_signal_return_pct(row: pd.Series) -> float:
    ret = num(row, "daily_return_calc", "return_1d", "return_1d_pct")
    if not math.isnan(ret):
        return ret
    close = close_price(row)
    prev_close = previous_close_price(row)
    if math.isnan(close) or math.isnan(prev_close) or prev_close <= 0:
        return math.nan
    return (close / prev_close - 1.0) * 100.0


def bottom_volume_attack_normal_volume(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    volume_ma20 = volume_ma20_lots(row)
    breakout_level = bottom_volume_attack_breakout_level(row)
    close = close_price(row)
    if any(math.isnan(v) for v in [vol, volume_ma20, breakout_level, close]):
        return False
    return (
        close >= breakout_level * 1.02
        and vol >= 2.0
        and volume_ma20 >= 1000
        and bottom_volume_attack_bullish_candle(row)
    )


def bottom_volume_attack_locked_limit_up(row: pd.Series) -> bool:
    close = close_price(row)
    open_ = num(row, "open")
    high = num(row, "high")
    low = num(row, "low")
    prev_close = previous_close_price(row)
    breakout_level = bottom_volume_attack_breakout_level(row)
    ret = daily_signal_return_pct(row)
    if any(math.isnan(v) for v in [close, open_, high, low, breakout_level, ret]):
        return False
    one_price_locked = high == low
    range_pct = math.nan
    if not one_price_locked:
        if math.isnan(prev_close) or prev_close <= 0:
            return False
        range_pct = (high - low) / prev_close * 100.0
    locked_or_tight_range = one_price_locked or range_pct <= 1.0
    return (
        close >= breakout_level * 1.02
        and ret >= 9.0
        and close >= high * 0.995
        and open_ >= close * 0.995
        and locked_or_tight_range
    )


def bottom_volume_attack_like(row: pd.Series) -> bool:
    return bottom_volume_attack_normal_volume(row) or bottom_volume_attack_locked_limit_up(row)


def close_position_in_day_range(row: pd.Series) -> float:
    close = close_price(row)
    high = num(row, "high")
    low = num(row, "low")
    if any(math.isnan(v) for v in [close, high, low]) or high <= low:
        return math.nan
    return (close - low) / (high - low)


def upper_shadow_pct_of_close(row: pd.Series) -> float:
    close = close_price(row)
    open_ = num(row, "open")
    high = num(row, "high")
    if any(math.isnan(v) for v in [close, open_, high]) or close <= 0:
        return math.nan
    return (high - max(close, open_)) / close * 100


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


def score_from_profile(row: pd.Series, profile: ScoreProfile) -> tuple[float, list[str], list[str]]:
    score = float(profile.base_score)
    comps: list[str] = [f"base={profile.base_score:g}", f"profile={profile.model_id}"]
    risks: list[str] = []
    vol = num(row, "volume_ratio")
    if not math.isnan(vol) and profile.volume_ratio_bonus_per_1x > 0 and profile.volume_ratio_bonus_cap > 0:
        add = min(profile.volume_ratio_bonus_cap, max(0, (vol - 1) * profile.volume_ratio_bonus_per_1x))
        score += add
        comps.append(f"volume_ratio:{vol:.2f}x +{add:.1f}")
    if tdcc_positive(row):
        score += profile.tdcc_positive_bonus
        if profile.tdcc_positive_bonus:
            comps.append(f"TDCC positive +{profile.tdcc_positive_bonus:g}")
    if warrant_signal(row) in BULLISH_WARRANT:
        score += profile.warrant_bullish_bonus
        if profile.warrant_bullish_bonus:
            comps.append(f"warrant bullish +{profile.warrant_bullish_bonus:g}")
    if strong_revenue(row):
        score += profile.strong_revenue_bonus
        if profile.strong_revenue_bonus:
            comps.append(f"revenue strong +{profile.strong_revenue_bonus:g}")
    off_low = num(row, "off_60d_low_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    if (
        profile.lower_position_bonus
        and not math.isnan(off_low)
        and off_low <= profile.lower_position_max_off_60d_low_pct
    ):
        score += profile.lower_position_bonus
        comps.append(f"lower position +{profile.lower_position_bonus:g}")
    if (
        profile.high_return_penalty
        and not math.isnan(ret20)
        and ret20 > profile.high_return_penalty_threshold_20d
    ):
        score -= profile.high_return_penalty
        risks.append(f"20d_return_high_score_penalty:{profile.high_return_penalty:g}")
    if tdcc_distribution(row):
        score -= profile.tdcc_distribution_penalty
        if profile.tdcc_distribution_penalty:
            risks.append(f"tdcc_distribution_penalty:{profile.tdcc_distribution_penalty:g}")
    if flag(row, "false_breakout_risk"):
        score -= profile.false_breakout_penalty
        if profile.false_breakout_penalty:
            risks.append(f"false_breakout_risk_penalty:{profile.false_breakout_penalty:g}")
    return score, comps, risks


def score_volume_breakout_profile(row: pd.Series, profile_id: str) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES[profile_id])
    breakout_pct = bottom_volume_attack_breakout_pct(row)
    if profile_id != VOLUME_BREAKOUT_V2_HIGH_MODEL_ID and bottom_volume_attack_locked_limit_up(row):
        score += 8
        comps.append("locked_limit_up_breakout +8")
        if num(row, "high") == num(row, "low"):
            score += 4
            comps.append("one_price_limit_up +4")
    if not math.isnan(breakout_pct):
        add = min(12.0, max(0.0, breakout_pct - 2.0) * 2.0)
        if add:
            score += add
            comps.append(f"breakout_magnitude:{breakout_pct:.2f}% +{add:.1f}")
    close_pos = close_position_in_day_range(row)
    if not math.isnan(close_pos):
        if close_pos >= 0.90:
            score += 6
            comps.append("close_near_day_high +6")
        elif close_pos >= 0.75:
            score += 3
            comps.append("close_high_position +3")
    if red_solid_candle(row):
        score += 5
        comps.append("strong_red_body +5")
    elif bottom_volume_attack_bullish_candle(row):
        score += 2
        comps.append("red_body_confirmed +2")
    width = num(row, "platform_width_pct", "short_platform_width_pct", "range_width_pct")
    if not math.isnan(width):
        if 3 <= width <= 15:
            score += 6
            comps.append("base_width_controlled +6")
        elif 15 < width <= 25:
            score += 2
            comps.append("base_width_acceptable +2")
    days = num(row, "days_in_range", "platform_days", "range_window")
    if not math.isnan(days):
        if days >= 20:
            score += 6
            comps.append("base_duration_20d_plus +6")
        elif days >= 10:
            score += 3
            comps.append("base_duration_10d_plus +3")
    upper_shadow = upper_shadow_pct_of_close(row)
    if not math.isnan(upper_shadow) and upper_shadow > 3.0:
        penalty = min(8.0, (upper_shadow - 3.0) * 1.5)
        score -= penalty
        risks.append(f"long_upper_shadow_quality_penalty:{penalty:.1f}")
    return score, comps, risks


def score_volume_breakout_v2_low_position(row: pd.Series) -> tuple[float, list[str], list[str]]:
    return score_volume_breakout_profile(row, VOLUME_BREAKOUT_V2_LOW_MODEL_ID)


def score_volume_breakout_v2_mid_position(row: pd.Series) -> tuple[float, list[str], list[str]]:
    return score_volume_breakout_profile(row, VOLUME_BREAKOUT_V2_MID_MODEL_ID)


def score_volume_breakout_v2_high_position(row: pd.Series) -> tuple[float, list[str], list[str]]:
    profile = MODEL_SCORE_PROFILES[VOLUME_BREAKOUT_V2_HIGH_MODEL_ID]
    score = float(profile.base_score)
    comps: list[str] = [f"base={profile.base_score:g}", f"profile={profile.model_id}", "ma60_gt_ma120_required"]
    risks: list[str] = []

    vol = num(row, "volume_ratio")
    if not math.isnan(vol) and vol <= 2.0:
        score += 6.0
        comps.append("high_pos_bonus_volume_lt2 +6")

    breakout_pct = bottom_volume_attack_breakout_pct(row)
    if not math.isnan(breakout_pct) and 2.0 < breakout_pct <= 5.0:
        score += 5.0
        comps.append("high_pos_bonus_breakout_2_5 +5")

    close_pos = close_position_in_day_range(row)
    if not math.isnan(close_pos) and close_pos <= 0.80:
        score += 5.0
        comps.append("high_pos_bonus_close_location_le80 +5")

    open_ = num(row, "open")
    close = close_price(row)
    if not math.isnan(open_) and open_ > 0 and not math.isnan(close):
        body_pct = abs(close - open_) / open_ * 100.0
        if body_pct <= 3.0:
            score += 5.0
            comps.append("high_pos_bonus_signal_body_le3 +5")

    if not flag(row, "limit_up_like") and not bottom_volume_attack_locked_limit_up(row):
        score += 4.0
        comps.append("high_pos_bonus_not_limit_up_like +4")

    tdcc_rank = num(row, "tdcc_rank", "weekly_increase_rank", "ranking_rank")
    if not math.isnan(tdcc_rank) and tdcc_rank <= 20:
        score += 6.0
        comps.append("high_pos_bonus_tdcc_weekly_increase_top20 +6")

    if text(row, "market_regime", "market_regime_bucket").lower() == "mild_bull":
        score += 3.0
        comps.append("high_pos_bonus_market_mild_bull +3")

    if flag(row, "kdj_overheated") or flag(row, "kd_overheated"):
        score += 3.0
        comps.append("high_pos_bonus_kdj_overheated +3")

    return round(clamp(score), 1), comps, risks


def volume_breakout_operation_score_fields(
    row: pd.Series,
    base_score: float,
    risks: list[str],
    model_id: str = "",
) -> dict[str, Any]:
    tdcc_score = 0.0
    pattern_score = 0.0
    operation_score = 0.0
    risk_penalty = 0.0
    reasons: list[str] = []
    allow_risk_penalty = model_id != VOLUME_BREAKOUT_V2_HIGH_MODEL_ID

    tdcc_rank = num(row, "tdcc_rank", "weekly_increase_rank", "ranking_rank")
    tdcc_ranking_score = num(row, "tdcc_ranking_score", "weekly_ranking_score")
    if tdcc_positive(row):
        tdcc_score += 4.0
        reasons.append("TDCC正向 +4")
    if not math.isnan(tdcc_rank):
        if tdcc_rank <= 10:
            tdcc_score += 8.0
            reasons.append("TDCC排名前10 +8")
        elif tdcc_rank <= 20:
            tdcc_score += 5.0
            reasons.append("TDCC排名前20 +5")
        elif tdcc_rank <= 50:
            tdcc_score += 2.0
            reasons.append("TDCC排名前50 +2")
    if not math.isnan(tdcc_ranking_score) and tdcc_ranking_score > 0:
        add = min(6.0, tdcc_ranking_score / 20.0)
        tdcc_score += add
        reasons.append(f"TDCC排名分數 +{add:.1f}")

    low_pos = num(row, "low_position_60_pct", "position_in_60d_range_pct")
    if not math.isnan(low_pos):
        if low_pos <= 60:
            pattern_score += 6.0
            reasons.append("低位階<=60 +6")
        elif allow_risk_penalty and low_pos >= 80:
            risk_penalty += 8.0
            reasons.append("高位階>=80 -8")
    if bottom_volume_attack_locked_limit_up(row):
        pattern_score += 10.0
        operation_score += 6.0
        reasons.append("鎖量漲停突破 +16")
        vol_ratio = num(row, "volume_ratio")
        if not math.isnan(vol_ratio) and vol_ratio < 2.0:
            operation_score += 4.0
            reasons.append("鎖量且量比低於2.0 +4")

    breakout_pct = bottom_volume_attack_breakout_pct(row)
    if not math.isnan(breakout_pct) and breakout_pct >= 2.0:
        add = min(5.0, (breakout_pct - 2.0) * 0.8)
        pattern_score += add
        reasons.append(f"突破品質 +{add:.1f}")

    close_pos = close_position_in_day_range(row)
    if not math.isnan(close_pos) and close_pos >= 0.90:
        operation_score += 4.0
        reasons.append("收近高點 +4")

    upper_shadow = upper_shadow_pct_of_close(row)
    if allow_risk_penalty and not math.isnan(upper_shadow) and upper_shadow > 3.0:
        penalty = min(8.0, (upper_shadow - 3.0) * 1.5)
        risk_penalty += penalty
        reasons.append(f"上影線風險 -{penalty:.1f}")

    priority = text(row, "volume_breakout_priority")
    if allow_risk_penalty and priority.startswith("B_"):
        risk_penalty += 3.0
        reasons.append("B級優先序風險 -3")
    if allow_risk_penalty and any("false_breakout" in safe_str(item) for item in risks):
        risk_penalty += 4.0
        reasons.append("假突破風險 -4")
    if allow_risk_penalty and tdcc_distribution(row):
        risk_penalty += 6.0
        reasons.append("TDCC分散警示 -6")

    final_rank_score = clamp(base_score + operation_score + tdcc_score + pattern_score - risk_penalty)
    return {
        "base_model_score": round(clamp(base_score), 1),
        "operation_score": round(operation_score, 1),
        "tdcc_score": round(tdcc_score, 1),
        "pattern_score": round(pattern_score, 1),
        "risk_penalty": round(risk_penalty, 1),
        "final_rank_score": round(final_rank_score, 1),
        "rank_reason_zh": " | ".join(reasons),
    }


def score_pullback(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["price_pullback_23ema"])
    comps.append("price_pullback_v1_required_gate")
    if near_ema23_or_platform(row):
        comps.append("near 23EMA/platform")
    if ema23_slope_proxy_up(row):
        comps.append("EMA23 slope proxy up")
    if flag(row, "pullback_entry_zone_flag"):
        comps.append("pullback entry zone")
    comps.append("price_pullback_return20_0_25_required")
    comps.append("price_pullback_tdcc_high_thresholds_up_required")
    comps.append("price_pullback_obv_above_ma20_required")
    if price_pullback_technical_strength_package(row):
        comps.append("price_pullback_technical_strength_package")
    if price_pullback_all_thresholds_up(row):
        comps.append("price_pullback_tdcc_all_thresholds_up_reason_only")
    if price_pullback_volume_red_or_solid_red_risk(row):
        risks.append("price_pullback_volume_red_or_solid_red_risk")
    return score, comps, risks


def price_pullback_tdcc_signal_status(row: pd.Series) -> str:
    return text(row, "tdcc_status", "tdcc_judgement", "tdcc_judge", "tdcc_accumulation_signal").lower()


def price_pullback_large_holder_confirmation(row: pd.Series) -> bool:
    up_400 = num(row, "tdcc_400_up_weeks")
    up_1000 = num(row, "tdcc_1000_up_weeks")
    change_400 = num(row, "tdcc_400_change_sum")
    change_1000 = num(row, "tdcc_1000_change_sum")
    weeks_confirmed = not math.isnan(up_400) and not math.isnan(up_1000) and up_400 >= 1 and up_1000 >= 1
    changes_confirmed = (
        not math.isnan(change_400)
        and not math.isnan(change_1000)
        and change_400 > 0
        and change_1000 > 0
    )
    return weeks_confirmed or changes_confirmed


def price_pullback_return20_0_25(row: pd.Series) -> bool:
    ret20 = num(row, "return_20d", "return_20d_pct")
    return not math.isnan(ret20) and 0 <= ret20 <= 25


def price_pullback_tdcc_high_thresholds_up(row: pd.Series) -> bool:
    return flag(row, "price_pullback_tdcc_history_available") and flag(row, "price_pullback_high_thresholds_up")


def price_pullback_all_thresholds_up(row: pd.Series) -> bool:
    return flag(row, "price_pullback_tdcc_history_available") and flag(row, "price_pullback_all_thresholds_up")


def price_pullback_obv_above_ma20(row: pd.Series) -> bool:
    return flag(row, "price_pullback_obv_above_ma20")


def price_pullback_technical_strength_package(row: pd.Series) -> bool:
    rsi14 = num(row, "price_pullback_rsi14", "rsi14")
    macd_hist = num(row, "price_pullback_macd_hist", "macd_hist")
    return not math.isnan(rsi14) and rsi14 >= 60 and not math.isnan(macd_hist) and macd_hist > 0


def price_pullback_volume_red_or_solid_red_risk(row: pd.Series) -> bool:
    volume_ratio = num(row, "volume_ratio", "volume_ratio_prev20")
    return (
        (not math.isnan(volume_ratio) and volume_ratio >= 1.2 and bottom_volume_attack_bullish_candle(row))
        or red_solid_candle(row)
    )


def price_pullback_operation_quality(row: pd.Series) -> str:
    return "technical_strength" if price_pullback_technical_strength_package(row) else "base"


def price_pullback_reason_tags(row: pd.Series) -> str:
    tags = ["base_v1", "return20_0_25", "tdcc_high_thresholds_up", "obv_above_ma20"]
    if price_pullback_technical_strength_package(row):
        tags.append("technical_strength_rsi60_macd_positive")
    if price_pullback_all_thresholds_up(row):
        tags.append("tdcc_all_thresholds_up_reason_only")
    return "|".join(tags)


def score_hot_theme_pullback(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["hot_theme_pullback"])
    labels = hot_theme_label(row)
    score += 12
    comps.append(f"熱門族群標籤 +12:{labels or '已具備'}")
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
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["w_bottom_right_side"])
    second_low_gap = num(row, "second_low_gap_pct")
    neckline_distance = num(row, "distance_to_neckline_pct")
    vol = num(row, "volume_ratio")
    attack1 = num(row, "attack1_gain_pct")
    attack2 = num(row, "attack2_gain_pct")
    vol2_vs_1 = w_bottom_second_arc_volume_ratio(row)
    red_candle_bonus, red_candle_components = w_bottom_red_candle_ratio_bonus(row)
    low_position_score, low_position_components, low_position_risks = w_bottom_low_position_score(row)
    context = detected_w_bottom_context(row)
    if context.get("available"):
        low_pos = context.get("w_bottom_low_position_pct")
        neck_dist = context.get("neckline_distance_pct")
        base_width = context.get("pre_base_width_pct")
        if isinstance(low_pos, (int, float)):
            comps.append(f"W low position:{low_pos:.1f}%")
        if isinstance(neck_dist, (int, float)):
            comps.append(f"W neckline distance:{neck_dist:.1f}%")
            neckline_distance = float(neck_dist)
        if isinstance(base_width, (int, float)) and not math.isnan(base_width):
            comps.append(f"pre-W base width:{base_width:.1f}%")
        current_vs_median = context.get("w_bottom_current_vs_long_median_pct")
        long_days = context.get("w_bottom_long_position_days")
        if isinstance(current_vs_median, (int, float)) and not math.isnan(current_vs_median):
            comps.append(f"W long position vs median:{current_vs_median:.1f}%/{int(long_days)}d")
        attack1 = float(context.get("attack1_gain_pct", math.nan))
        attack2 = float(context.get("attack2_gain_pct", math.nan))
        vol2_vs_1 = w_bottom_second_arc_volume_ratio(row, context)
        red_candle_bonus, red_candle_components = w_bottom_red_candle_ratio_bonus(row, context)
        low_position_score, low_position_components, low_position_risks = w_bottom_low_position_score(row, context)
        first_arc_volume = float(context.get("first_arc_month_avg_volume", math.nan))
        second_arc_volume = float(context.get("second_arc_avg_daily_volume", math.nan))
        if not math.isnan(first_arc_volume):
            comps.append(f"first arc avg volume:{first_arc_volume:.0f}")
        if not math.isnan(second_arc_volume):
            comps.append(f"second arc avg volume:{second_arc_volume:.0f}")
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
            score -= 2
            risks.append("near_neckline_wait_for_breakout_confirmation")
        elif 0 < neckline_distance <= 1:
            score -= 4
            risks.append("above_neckline_without_volume_breakout_confirmation")
    if not math.isnan(vol) and vol >= 1.2:
        add = min(5, (vol - 1.0) * 2)
        score += add
        comps.append(f"right-side volume support +{add:.1f}")
    if not math.isnan(attack1) and not math.isnan(attack2):
        if W_BOTTOM_RIGHT_SIDE_REBOUND_MIN <= attack2 <= 8:
            score += 5
            comps.append("early right-side rebound +5")
        elif 8 < attack2 <= W_BOTTOM_RIGHT_SIDE_REBOUND_MAX:
            score += 3
            comps.append("right-side rebound advancing +3")
        if attack2 >= attack1 * 0.9:
            score += 2
            comps.append("second attack comparable to first +2")
        elif attack2 < attack1 * 0.5:
            score -= 2
            risks.append("second_attack_still_weak_watch")
    if not math.isnan(vol2_vs_1):
        if vol2_vs_1 >= 1.5:
            score += 4
            comps.append("second arc volume expansion +4")
        elif vol2_vs_1 >= 1.2:
            score += 2
            comps.append("second arc volume mildly higher +2")
        elif vol2_vs_1 < 0.8:
            risks.append("second_arc_volume_not_confirmed")
    if red_candle_bonus:
        score += red_candle_bonus
        comps.extend(red_candle_components)
    if low_position_score:
        score += low_position_score
        comps.extend(low_position_components)
        risks.extend(low_position_risks)
    return score, comps, risks


def score_neckline_volume_breakout_confirmation(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["neckline_volume_breakout_confirmation"])
    context = detected_w_bottom_context(row)
    context_for_use = context if context.get("available") else None
    neckline_distance = w_bottom_neckline_distance_pct(row, context_for_use)
    second_arc_ratio = w_bottom_second_arc_volume_ratio(row, context_for_use)
    red_candle_bonus, red_candle_components = w_bottom_red_candle_ratio_bonus(row, context_for_use)
    context45 = neckline_context_window(row, NECKLINE_CONTEXT_ENTRY_WINDOW_DAYS)
    context90_score, context90_components, context90_risks = neckline_context_90_score_adjustment(row)

    if safe_str(context45.get("filter")) == "auto_non_bearish":
        comps.append("45d non-bearish neckline context gate")
    else:
        risks.append("neckline_45d_context_gate_not_confirmed")
    if context90_score:
        score += context90_score
    comps.extend(context90_components)
    risks.extend(context90_risks)

    if not math.isnan(second_arc_ratio):
        if second_arc_ratio >= 1.5:
            score += 6
            comps.append("W second arc volume expansion +6")
        elif second_arc_ratio >= 1.2:
            score += 3
            comps.append("W second arc volume confirmed +3")
        else:
            risks.append("W_second_arc_volume_below_first_arc_baseline")

    if w_bottom_neckline_locked_limit_up(row, context_for_use):
        score += 8
        comps.append("locked_limit_up_neckline_breakout +8")
        if num(row, "high") == num(row, "low"):
            score += 4
            comps.append("one_price_limit_up +4")
    elif w_bottom_neckline_normal_volume_breakout(row, context_for_use):
        score += 5
        comps.append("neckline_volume_confirmation +5")
    if red_candle_bonus:
        score += red_candle_bonus
        comps.extend(red_candle_components)

    if not math.isnan(neckline_distance) and neckline_distance >= 0:
        add = min(8.0, neckline_distance * 1.2)
        if add:
            score += add
            comps.append(f"neckline breakout distance:{neckline_distance:.2f}% +{add:.1f}")

    close_pos = close_position_in_day_range(row)
    if not math.isnan(close_pos):
        if close_pos >= 0.90:
            score += 6
            comps.append("close_near_day_high +6")
        elif close_pos >= 0.75:
            score += 3
            comps.append("close_high_position +3")
    if red_solid_candle(row):
        score += 5
        comps.append("strong_red_body +5")
    elif bottom_volume_attack_bullish_candle(row):
        score += 2
        comps.append("red_body_confirmed +2")
    upper_shadow = upper_shadow_pct_of_close(row)
    if not math.isnan(upper_shadow) and upper_shadow > 3.0:
        penalty = min(8.0, (upper_shadow - 3.0) * 1.5)
        score -= penalty
        risks.append(f"long_upper_shadow_quality_penalty:{penalty:.1f}")
    return score, comps, risks


def score_revenue_unreacted(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["revenue_unreacted_range"])
    if in_recent_range(row, 5):
        score += 10
        comps.append("price in 23-day range +10")
    if near_range_high(row, 5):
        score += 6
        comps.append("near platform breakout +6")
    approved_non_financial_event_types = {
        "new_order",
        "customer_win",
        "capacity_expansion",
        "mass_production",
        "technology_validation",
        "product_certification",
        "policy_tailwind",
        "exhibition_catalyst",
        "sector_rotation",
        "international_peer_momentum",
    }
    event_type = text(row, "event_catalyst_tags").split(";", 1)[0].strip().lower()
    if event_type in approved_non_financial_event_types:
        score += 3
        comps.append("核准非財務事件 +3")
    return score, comps, risks


def score_pullback_short_reclaim(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["pullback_short_reclaim"])
    if ema23_slope_proxy_up(row):
        score += 6
        comps.append("EMA23 slope proxy up +6")
    if flag(row, "ma20_reclaim_flag") or flag(row, "ema23_reclaim_flag") or flag(row, "pullback_right_side"):
        score += 8
        comps.append("reclaim after pullback +8")
    vol = num(row, "volume_ratio")
    if not math.isnan(vol) and vol >= 1.5:
        score += 4
        comps.append("re-attack volume +4")
    if flag(row, "macd_turn_up_flag") or flag(row, "kd_turn_up_flag"):
        score += 4
        comps.append("momentum turn-up +4")
    return score, comps, risks


def score_tdcc_stealth(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = score_from_profile(row, MODEL_SCORE_PROFILES["tdcc_stealth_accumulation"])
    phase = text(row, "tdcc_price_phase").lower()
    if phase == "tdcc_leading_price":
        score += 12
        comps.append("tdcc leading price +12")
    if in_recent_range(row, 10):
        score += 8
        comps.append("price still in recent range +8")
    weeks = num(row, "tdcc_consecutive_up_weeks", "consecutive_tdcc_up_weeks")
    if not math.isnan(weeks):
        if weeks >= 3:
            score += 7
            comps.append("TDCC consecutive up 3w+ +7")
        elif weeks >= 2:
            score += 4
            comps.append("TDCC consecutive up 2w +4")
    if flag(row, "all_thresholds_up") or flag(row, "high_thresholds_up"):
        score += 7
        comps.append("high holder thresholds up +7")
    return score, comps, risks


def cond_volume_breakout_v2_low_position_watch_only(row: pd.Series) -> bool:
    """Low-position v2 volume breakout is sourced from the dedicated volume watch table."""
    return False


def cond_volume_breakout_v2_mid_position_watch_only(row: pd.Series) -> bool:
    """Mid-position v2 volume breakout is sourced from the dedicated volume watch table."""
    return False


def cond_volume_breakout_v2_high_position_watch_only(row: pd.Series) -> bool:
    """High-position v2 volume breakout is sourced from the dedicated volume watch table."""
    return False


def active_price_attack_for_early_models(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    ret5 = num(row, "return_5d", "return_5d_pct")
    ret20 = num(row, "return_20d", "return_20d_pct")
    return (
        bottom_volume_attack_like(row)
        or flag(row, "volume_confirmed_breakout")
        or (not math.isnan(vol) and vol >= 2.5)
        or (not math.isnan(ret5) and ret5 >= 8)
        or (not math.isnan(ret20) and ret20 >= 20)
    )


def tdcc_stealth_attack_already_started(row: pd.Series) -> bool:
    """TDCC stealth model's own attack exclusion.

    Keep this independent from formal v2 volume-attack gates so TDCC parameter
    tuning does not silently inherit changes from another model.
    """
    return bottom_volume_attack_like(row) or flag(row, "volume_confirmed_breakout")


def cond_pullback(row: pd.Series) -> bool:
    return (
        near_ema23_or_support(row)
        and ema23_slope_proxy_up(row)
        and price_pullback_return20_0_25(row)
        and price_pullback_tdcc_high_thresholds_up(row)
        and price_pullback_obv_above_ma20(row)
    )


def cond_hot_theme_pullback(row: pd.Series) -> bool:
    # Key distinction from price_pullback_23ema:
    # hot theme tag + pullback near 23EMA/support is sufficient.
    # Revenue is only an add-score component, never a gate.
    return has_hot_theme(row) and near_ema23_or_support(row)


def cond_revenue_unreacted(row: pd.Series) -> bool:
    active_attack = active_price_attack_for_early_models(row)
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


W_BOTTOM_SECOND_LOW_GAP_MIN = -3.0
W_BOTTOM_SECOND_LOW_GAP_MAX = 6.0
W_BOTTOM_RIGHT_SIDE_REBOUND_MIN = 3.0
W_BOTTOM_RIGHT_SIDE_REBOUND_MAX = 15.0
W_BOTTOM_LONG_POSITION_LOOKBACK_DAYS = 252
W_BOTTOM_LONG_POSITION_MIN_DAYS = 180
NECKLINE_CONTEXT_ENTRY_WINDOW_DAYS = 45
NECKLINE_CONTEXT_SCORE_WINDOW_DAYS = 90


def context_num(context: dict[str, float | str | bool] | None, *names: str) -> float:
    if not context:
        return math.nan
    for name in names:
        if name in context:
            value = to_number(context.get(name, math.nan))
            if not math.isnan(value):
                return float(value)
    return math.nan


def w_bottom_second_arc_volume_ratio(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> float:
    ratio = context_num(context, "second_arc_volume_ratio", "w_bottom_second_arc_volume_ratio")
    if not math.isnan(ratio):
        return ratio
    return num(row, "second_arc_volume_ratio", "w_bottom_second_arc_volume_ratio", "volume_ratio_2_vs_1")


def w_bottom_second_arc_volume_ok(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> bool:
    ratio = w_bottom_second_arc_volume_ratio(row, context)
    return not math.isnan(ratio) and ratio >= 1.2


def w_bottom_red_candle_ratios(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> tuple[float, float, float]:
    first_ratio = context_num(context, "first_arc_red_candle_ratio", "w_bottom_first_arc_red_candle_ratio")
    second_ratio = context_num(context, "second_arc_red_candle_ratio", "w_bottom_second_arc_red_candle_ratio")
    delta = context_num(context, "second_arc_red_candle_ratio_delta", "w_bottom_second_arc_red_candle_ratio_delta")
    if math.isnan(first_ratio):
        first_ratio = num(row, "first_arc_red_candle_ratio", "w_bottom_first_arc_red_candle_ratio")
    if math.isnan(second_ratio):
        second_ratio = num(row, "second_arc_red_candle_ratio", "w_bottom_second_arc_red_candle_ratio")
    if math.isnan(delta):
        delta = num(row, "second_arc_red_candle_ratio_delta", "w_bottom_second_arc_red_candle_ratio_delta")
    if math.isnan(delta) and not math.isnan(first_ratio) and not math.isnan(second_ratio):
        delta = second_ratio - first_ratio
    return first_ratio, second_ratio, delta


def w_bottom_red_candle_ratio_bonus(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> tuple[float, list[str]]:
    first_ratio, second_ratio, delta = w_bottom_red_candle_ratios(row, context)
    if any(math.isnan(value) for value in [first_ratio, second_ratio, delta]):
        return 0.0, []
    if second_ratio >= 0.55 and delta >= 0.15:
        return 4.0, [
            f"second arc red candle ratio improved +4 ({second_ratio:.0%} vs {first_ratio:.0%})"
        ]
    if second_ratio >= 0.45 and delta >= 0.08:
        return 2.0, [
            f"second arc red candle ratio mildly improved +2 ({second_ratio:.0%} vs {first_ratio:.0%})"
        ]
    return 0.0, []


def w_bottom_low_position_score(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> tuple[float, list[str], list[str]]:
    low_pos = context_num(context, "w_bottom_low_position_pct")
    if math.isnan(low_pos):
        low_pos = num(row, "w_bottom_low_position_pct", "double_bottom_low_position_pct")
    if math.isnan(low_pos):
        low_pos = num(row, "off_60d_low_pct")
    if math.isnan(low_pos):
        return 0.0, [], []

    if low_pos <= 10:
        return 8.0, [f"W low position very low +8 ({low_pos:.1f}%)"], []
    if low_pos <= 20:
        return 6.0, [f"W low position low +6 ({low_pos:.1f}%)"], []
    if low_pos <= 30:
        return 4.0, [f"W low position acceptable +4 ({low_pos:.1f}%)"], []
    if low_pos <= 35:
        return 2.0, [f"W low position upper base +2 ({low_pos:.1f}%)"], []
    if low_pos <= 45:
        return -2.0, [], [f"W_low_position_higher_watch:{low_pos:.1f}%"]
    return -5.0, [], [f"W_low_position_too_high_penalty:{low_pos:.1f}%"]


def w_bottom_long_price_position_metrics(
    history: pd.DataFrame,
    current_close: float,
) -> dict[str, float | str | bool]:
    lookback = history.tail(W_BOTTOM_LONG_POSITION_LOOKBACK_DAYS)
    valid_close = pd.to_numeric(lookback["close"], errors="coerce").dropna()
    days = int(len(valid_close))
    if days < W_BOTTOM_LONG_POSITION_MIN_DAYS or math.isnan(current_close):
        return {
            "w_bottom_long_position_ok": False,
            "w_bottom_long_position_fail_reason": "long_price_position_insufficient_history",
            "w_bottom_long_position_days": days,
            "w_bottom_long_close_median": math.nan,
            "w_bottom_long_close_mean": math.nan,
            "w_bottom_current_vs_long_median_pct": math.nan,
            "w_bottom_current_vs_long_mean_pct": math.nan,
        }

    median_close = float(valid_close.median())
    mean_close = float(valid_close.mean())
    current_vs_median = (current_close / median_close - 1) * 100 if median_close > 0 else math.nan
    current_vs_mean = (current_close / mean_close - 1) * 100 if mean_close > 0 else math.nan
    ok = not math.isnan(current_vs_median) and current_vs_median <= 0
    return {
        "w_bottom_long_position_ok": ok,
        "w_bottom_long_position_fail_reason": "" if ok else "current_close_above_long_median",
        "w_bottom_long_position_days": days,
        "w_bottom_long_close_median": median_close,
        "w_bottom_long_close_mean": mean_close,
        "w_bottom_current_vs_long_median_pct": current_vs_median,
        "w_bottom_current_vs_long_mean_pct": current_vs_mean,
    }


def neckline_context_pct_change(end_value: float, start_value: float) -> float:
    if math.isnan(start_value) or math.isnan(end_value) or start_value <= 0:
        return math.nan
    return (end_value / start_value - 1.0) * 100.0


def neckline_context_max_drawdown_pct(closes: list[float]) -> float:
    peak = -math.inf
    worst = 0.0
    for close in closes:
        if math.isnan(close):
            continue
        peak = max(peak, close)
        if peak > 0:
            worst = min(worst, (close / peak - 1.0) * 100.0)
    return worst if peak > 0 else math.nan


def neckline_context_slope_pct_per_20d(closes: list[float]) -> float:
    values = [value for value in closes if not math.isnan(value)]
    if len(values) < 10 or values[0] <= 0:
        return math.nan
    n = len(values)
    mean_x = (n - 1) / 2.0
    mean_y = sum(values) / n
    denom = sum((idx - mean_x) ** 2 for idx in range(n))
    if denom == 0:
        return math.nan
    slope = sum((idx - mean_x) * (value - mean_y) for idx, value in enumerate(values)) / denom
    return slope * 20.0 / values[0] * 100.0


def neckline_context_classify(return_pct: float, range_pct: float, slope20_pct: float, drawdown_pct: float) -> str:
    if any(math.isnan(value) for value in [return_pct, range_pct, slope20_pct, drawdown_pct]):
        return "unknown"
    if return_pct <= -12.0 or (slope20_pct <= -4.0 and drawdown_pct <= -18.0):
        return "bearish"
    if abs(return_pct) <= 8.0 and range_pct <= 35.0 and drawdown_pct >= -22.0:
        return "sideways_or_consolidation"
    if return_pct >= 8.0 and slope20_pct >= 1.25:
        return "slow_uptrend"
    return "volatile_mixed"


def neckline_context_filter_result(context: str) -> str:
    if context == "unknown":
        return "unknown"
    return "auto_bearish" if context == "bearish" else "auto_non_bearish"


def explicit_neckline_context(row: pd.Series, window_days: int) -> dict[str, float | str | bool] | None:
    suffix = str(window_days)
    filter_value = text(row, f"neckline_context_filter_{suffix}", f"filter_{suffix}")
    context = text(row, f"neckline_context_{suffix}", f"context_{suffix}")
    if not filter_value and not context:
        return None

    return {
        "available": True,
        "window_days": window_days,
        "context": context or ("bearish" if filter_value == "auto_bearish" else "unknown"),
        "filter": filter_value or neckline_context_filter_result(context),
        "return_pct": num(row, f"neckline_context_return_{suffix}", f"return_{suffix}"),
        "range_pct": num(row, f"neckline_context_range_{suffix}", f"range_{suffix}"),
        "slope20_pct": num(row, f"neckline_context_slope20_{suffix}", f"slope20_{suffix}"),
        "drawdown_pct": num(row, f"neckline_context_drawdown_{suffix}", f"drawdown_{suffix}"),
        "sessions": num(row, f"neckline_context_sessions_{suffix}", f"context_sessions_{suffix}"),
        "source": "row_fields",
    }


def neckline_context_window(row: pd.Series, window_days: int) -> dict[str, float | str | bool]:
    explicit = explicit_neckline_context(row, window_days)
    if explicit is not None:
        return explicit

    stock_id = text(row, "stock_id")
    df = price_history_for_stock(stock_id)
    if df.empty or "date" not in df.columns:
        return {"available": False, "window_days": window_days, "filter": "unknown", "context": "unknown"}

    signal_date = text(row, "signal_date", "as_of_date", "date")
    if signal_date:
        dated = df[df["date"].astype(str) <= signal_date].copy()
        if dated.empty:
            return {"available": False, "window_days": window_days, "filter": "unknown", "context": "unknown"}
        df = dated.reset_index(drop=True)
    else:
        df = df.reset_index(drop=True)

    signal_idx = len(df) - 1
    if signal_idx <= 1:
        return {"available": False, "window_days": window_days, "filter": "unknown", "context": "unknown"}

    start_idx = max(0, signal_idx - window_days)
    window = df.iloc[start_idx:signal_idx].copy()
    if len(window) < 20:
        return {
            "available": True,
            "window_days": window_days,
            "filter": "unknown",
            "context": "unknown",
            "sessions": len(window),
            "source": "price_history",
        }

    closes = pd.to_numeric(window["close"], errors="coerce").tolist()
    highs = pd.to_numeric(window.get("high", pd.Series(dtype=float)), errors="coerce").dropna()
    lows = pd.to_numeric(window.get("low", pd.Series(dtype=float)), errors="coerce").dropna()
    return_pct = neckline_context_pct_change(float(closes[-1]), float(closes[0]))
    range_pct = (
        (float(highs.max()) / float(lows.min()) - 1.0) * 100.0
        if len(highs) and len(lows) and float(lows.min()) > 0
        else math.nan
    )
    slope20 = neckline_context_slope_pct_per_20d([float(value) for value in closes])
    drawdown = neckline_context_max_drawdown_pct([float(value) for value in closes])
    context = neckline_context_classify(return_pct, range_pct, slope20, drawdown)
    return {
        "available": True,
        "window_days": window_days,
        "context": context,
        "filter": neckline_context_filter_result(context),
        "return_pct": return_pct,
        "range_pct": range_pct,
        "slope20_pct": slope20,
        "drawdown_pct": drawdown,
        "sessions": len(window),
        "source": "price_history",
    }


def neckline_context_45_entry_ok(row: pd.Series) -> bool:
    context = neckline_context_window(row, NECKLINE_CONTEXT_ENTRY_WINDOW_DAYS)
    return safe_str(context.get("filter")) == "auto_non_bearish"


def neckline_context_90_score_adjustment(row: pd.Series) -> tuple[float, list[str], list[str]]:
    context = neckline_context_window(row, NECKLINE_CONTEXT_SCORE_WINDOW_DAYS)
    filter_value = safe_str(context.get("filter"))
    if filter_value == "auto_non_bearish":
        return 2.0, ["90d non-bearish context +2"], []
    if filter_value != "auto_bearish":
        return 0.0, [], ["neckline_90d_context_unknown"]

    points = 2.0
    flags = ["long_90_bearish_base_risk"]
    return_90 = float(context.get("return_pct", math.nan))
    slope_90 = float(context.get("slope20_pct", math.nan))
    drawdown_90 = float(context.get("drawdown_pct", math.nan))
    if not math.isnan(return_90) and return_90 < -10.0:
        points += 1.0
        flags.append("return90_below_neg10")
    if not math.isnan(return_90) and return_90 < -20.0:
        points += 1.0
        flags.append("return90_below_neg20")
    if not math.isnan(drawdown_90) and drawdown_90 < -25.0:
        points += 1.0
        flags.append("drawdown90_below_neg25")
    if not math.isnan(slope_90) and slope_90 < -2.0:
        points += 1.0
        flags.append("slope90_below_neg2")
    return -points, [], [f"neckline_90d_context_penalty:{points:.1f}", *flags]


def w_bottom_neckline_distance_pct(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> float:
    distance = context_num(context, "neckline_distance_pct", "distance_to_neckline_pct")
    if not math.isnan(distance):
        return distance
    return num(row, "neckline_distance_pct", "distance_to_neckline_pct")


def w_bottom_neckline_price(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> float:
    price = context_num(context, "neckline_price")
    if not math.isnan(price):
        return price
    return num(row, "neckline_price")


def w_bottom_base_structure_ok(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> bool:
    second_low_gap = context_num(context, "second_low_gap_pct")
    if math.isnan(second_low_gap):
        second_low_gap = num(row, "second_low_gap_pct")
    if math.isnan(second_low_gap) or not (
        W_BOTTOM_SECOND_LOW_GAP_MIN <= second_low_gap <= W_BOTTOM_SECOND_LOW_GAP_MAX
    ):
        return False

    base_width = context_num(context, "pre_base_width_pct")
    if math.isnan(base_width):
        base_width = num(row, "w_bottom_base_width_pct", "double_bottom_base_width_pct", "platform_width_pct", "short_platform_width_pct")
    if math.isnan(base_width) or base_width > 35.0:
        return False

    pre_return = context_num(context, "pre_base_return_pct")
    if not math.isnan(pre_return) and abs(pre_return) > 25.0:
        return False
    return True


def w_bottom_neckline_normal_volume_breakout(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> bool:
    close = close_price(row)
    neckline = w_bottom_neckline_price(row, context)
    vol = num(row, "volume_ratio")
    ma20 = volume_ma20_lots(row)
    if any(math.isnan(v) for v in [close, neckline, vol, ma20]):
        return False
    return close >= neckline and vol >= 2.0 and ma20 >= 1000 and bottom_volume_attack_bullish_candle(row)


def w_bottom_neckline_locked_limit_up(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> bool:
    close = close_price(row)
    open_ = num(row, "open")
    high = num(row, "high")
    low = num(row, "low")
    prev_close = previous_close_price(row)
    neckline = w_bottom_neckline_price(row, context)
    ret = daily_signal_return_pct(row)
    if any(math.isnan(v) for v in [close, open_, high, low, neckline, ret]):
        return False
    one_price_locked = high == low
    range_pct = math.nan
    if not one_price_locked:
        if math.isnan(prev_close) or prev_close <= 0:
            return False
        range_pct = (high - low) / prev_close * 100.0
    locked_or_tight_range = one_price_locked or range_pct <= 1.0
    return close >= neckline and ret >= 9.0 and close >= high * 0.995 and open_ >= close * 0.995 and locked_or_tight_range


def w_bottom_neckline_breakout_confirmation_ok(
    row: pd.Series,
    context: dict[str, float | str | bool] | None = None,
) -> bool:
    neckline_distance = w_bottom_neckline_distance_pct(row, context)
    if math.isnan(neckline_distance) or neckline_distance < 0:
        return False
    return (
        w_bottom_base_structure_ok(row, context)
        and w_bottom_second_arc_volume_ok(row, context)
        and (
            w_bottom_neckline_normal_volume_breakout(row, context)
            or w_bottom_neckline_locked_limit_up(row, context)
        )
    )


def w_bottom_attack_confirmation_ok(row: pd.Series, context: dict[str, float | str | bool] | None = None) -> bool:
    """Require an early right-side rebound and second-arc volume confirmation."""
    attack1 = num(row, "attack1_gain_pct")
    attack2 = num(row, "attack2_gain_pct")
    vol2_vs_1 = w_bottom_second_arc_volume_ratio(row)
    red_body2_vs_1 = num(row, "red_body_ratio_2_vs_1")

    if context:
        # When price history is available, trust the detected two legs rather
        # than broad upstream pattern columns.  Otherwise a low-base or
        # post-rally pullback can inherit stale explicit W metrics and pass.
        attack1 = float(context.get("attack1_gain_pct", math.nan))
        attack2 = float(context.get("attack2_gain_pct", math.nan))
        vol2_vs_1 = w_bottom_second_arc_volume_ratio(row, context)
        red_body2_vs_1 = float(context.get("red_body_ratio_2_vs_1", math.nan))

    if math.isnan(attack1) or math.isnan(attack2):
        return False

    price_leg_ok = W_BOTTOM_RIGHT_SIDE_REBOUND_MIN <= attack2 <= W_BOTTOM_RIGHT_SIDE_REBOUND_MAX
    volume_ok = not math.isnan(vol2_vs_1) and vol2_vs_1 >= 1.2
    return price_leg_ok and volume_ok


def w_bottom_segment_quality(
    df: pd.DataFrame,
    left_peak_idx: int,
    left_low_idx: int,
    neckline_idx: int,
    right_low_idx: int,
    current_close: float,
) -> dict[str, float | str | bool]:
    """Validate W-bottom as connected segments, not only swing points."""
    left_descent = df.iloc[left_peak_idx : left_low_idx + 1]
    first_rebound = df.iloc[left_low_idx : neckline_idx + 1]
    second_decline = df.iloc[neckline_idx : right_low_idx + 1]
    right_rebound = df.iloc[right_low_idx:]

    failures: list[str] = []
    if len(left_descent) < 5:
        failures.append("left_descent_too_short")
    if len(first_rebound) < 5:
        failures.append("first_rebound_too_short")
    if len(second_decline) < 3:
        failures.append("second_decline_too_short")
    if len(right_rebound) < 4:
        failures.append("right_rebound_too_short")

    left_low = float(df["low"].iloc[left_low_idx])
    right_low = float(df["low"].iloc[right_low_idx])
    neckline = float(df["high"].iloc[neckline_idx])
    left_low_close = float(df["close"].iloc[left_low_idx])
    right_low_close = float(df["close"].iloc[right_low_idx])

    if float(first_rebound["low"].min()) < left_low * 0.98:
        failures.append("first_low_undercut_before_neckline")
    first_after_low = df.iloc[left_low_idx + 1 : neckline_idx + 1]
    first_close_undercuts = 0
    if not first_after_low.empty:
        first_close_undercuts = int((first_after_low["close"] < left_low_close * 0.98).sum())
        if first_close_undercuts > 1:
            failures.append("first_low_close_repeatedly_undercut")

    after_neckline = df.iloc[neckline_idx + 1 : right_low_idx + 1]
    if not after_neckline.empty and float(after_neckline["high"].max()) > neckline * 1.02:
        failures.append("higher_high_after_neckline_before_second_low")
    if float(second_decline["low"].min()) < right_low * 0.98:
        failures.append("second_low_undercut_inside_decline")

    if float(right_rebound["low"].min()) < right_low * 0.98:
        failures.append("second_low_undercut_after_right_side")
    right_after_low = df.iloc[right_low_idx + 1 :]
    second_close_undercuts = 0
    if not right_after_low.empty:
        second_close_undercuts = int((right_after_low["close"] < right_low_close * 0.98).sum())
        if second_close_undercuts > 1:
            failures.append("second_low_close_repeatedly_undercut")

    right_rebound_high = float(right_rebound["high"].max())
    right_span = right_rebound_high - right_low
    right_rebound_retention_pct = 100.0
    if right_span > 0:
        right_rebound_retention_pct = (current_close - right_low) / right_span * 100.0
        if right_rebound_retention_pct < 45.0:
            failures.append("right_rebound_faded")

    return {
        "w_shape_quality_passed": not failures,
        "w_shape_quality_failures": ";".join(failures),
        "left_descent_days": len(left_descent),
        "first_rebound_days": len(first_rebound),
        "second_decline_days": len(second_decline),
        "right_rebound_days": len(right_rebound),
        "first_low_close_undercut_count": first_close_undercuts,
        "second_low_close_undercut_count": second_close_undercuts,
        "right_rebound_retention_pct": right_rebound_retention_pct,
    }


def detected_w_bottom_context(row: pd.Series) -> dict[str, float | str | bool]:
    """Infer current W-bottom context from price history.

    This is intentionally conservative. Broad upstream pattern flags are not
    enough: the detector must find a connected swing sequence of left peak,
    first low, neckline, second low, and current right-side rebound. The two
    lows must be close in height, the lows must not be meaningfully undercut
    inside their own legs, and the latest price must not already be far above
    the neckline.
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
    position_history = df.reset_index(drop=True)
    current_close = float(position_history["close"].iloc[-1])
    long_position = w_bottom_long_price_position_metrics(position_history, current_close)
    df = df.tail(120).reset_index(drop=True)
    if len(df) < 80:
        return {"available": False}

    high_120 = float(df["high"].max())
    low_120 = float(df["low"].min())
    if high_120 <= low_120:
        return {"available": False}
    range_span = high_120 - low_120

    peaks: list[int] = []
    troughs: list[int] = []
    for idx in range(3, len(df) - 3):
        local = df["high"].iloc[idx - 3 : idx + 4]
        if float(df["high"].iloc[idx]) >= float(local.max()) * 0.998:
            peaks.append(idx)
    for idx in range(3, len(df) - 3):
        local = df["low"].iloc[idx - 3 : idx + 4]
        if float(df["low"].iloc[idx]) <= float(local.min()) * 1.002:
            troughs.append(idx)

    best: dict[str, float | str | bool] | None = None
    best_rejected_shape: dict[str, float | str | bool] | None = None
    for left in troughs:
        pre_peak_start = max(0, left - 45)
        pre_peak_end = left - 2
        if pre_peak_end <= pre_peak_start:
            continue
        left_peak_candidates = [idx for idx in peaks if pre_peak_start <= idx <= pre_peak_end]
        if left_peak_candidates:
            left_peak_idx = max(left_peak_candidates, key=lambda idx: float(df["high"].iloc[idx]))
        else:
            left_peak_idx = int(df["high"].iloc[pre_peak_start:pre_peak_end].idxmax())
        left_peak = float(df["high"].iloc[left_peak_idx])
        low_left = float(df["low"].iloc[left])
        left_decline_pct = (left_peak / low_left - 1) * 100 if low_left > 0 else math.nan
        if math.isnan(left_decline_pct) or left_decline_pct < 8:
            continue
        left_descent_slice = df.iloc[left_peak_idx : left + 1]
        if float(left_descent_slice["low"].min()) < low_left * 0.98:
            continue

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
            low_right = float(df["low"].iloc[right])
            second_low_gap = (low_right / low_left - 1) * 100
            if second_low_gap < W_BOTTOM_SECOND_LOW_GAP_MIN or second_low_gap > W_BOTTOM_SECOND_LOW_GAP_MAX:
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

            # A W is a connected swing sequence:
            # left peak -> first low -> neckline -> second low -> right side.
            # If the first "low" is meaningfully undercut before the neckline,
            # or the second low is undercut after it forms, the shape is not a
            # clean W-bottom for this model.
            first_rebound_slice = df.iloc[left : neckline_idx + 1]
            right_rebound_slice = df.iloc[right:]
            segment_quality = w_bottom_segment_quality(
                df,
                left_peak_idx,
                left,
                neckline_idx,
                right,
                current_close,
            )
            if not segment_quality["w_shape_quality_passed"]:
                rejected_shape: dict[str, float | str | bool] = {
                    "available": True,
                    "context_ok": False,
                    "left_peak_date": str(df["date"].iloc[left_peak_idx]),
                    "left_low_date": str(df["date"].iloc[left]),
                    "neckline_date": str(df["date"].iloc[neckline_idx]),
                    "right_low_date": str(df["date"].iloc[right]),
                    "right_low_age_days": right_age,
                    "second_low_gap_pct": second_low_gap,
                    "neckline_price": neckline,
                }
                rejected_shape.update(segment_quality)
                rejected_shape.update(long_position)
                if (
                    best_rejected_shape is None
                    or right_age < float(best_rejected_shape.get("right_low_age_days", math.inf))
                ):
                    best_rejected_shape = rejected_shape
                continue

            low_left_position = (low_left - low_120) / range_span * 100
            low_right_position = (low_right - low_120) / range_span * 100
            lows_in_lower_base = low_left_position <= 35 and low_right_position <= 35

            pre_base = df.iloc[max(0, left_peak_idx - 30) : left_peak_idx]
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
            first_arc_slice = df.iloc[left_peak_idx : neckline_idx + 1]
            second_arc_slice = df.iloc[neckline_idx:]
            attack1_slice = first_arc_slice
            attack2_slice = second_arc_slice
            vol2_vs_1 = math.nan
            first_arc_month_avg_volume = math.nan
            second_arc_avg_daily_volume = math.nan
            second_arc_volume_ratio = math.nan
            red_body2_vs_1 = math.nan
            first_arc_red_candle_count = math.nan
            second_arc_red_candle_count = math.nan
            first_arc_red_candle_ratio = math.nan
            second_arc_red_candle_ratio = math.nan
            second_arc_red_candle_ratio_delta = math.nan
            if "volume" in df.columns and len(attack1_slice) >= 3 and len(attack2_slice) >= 3:
                vol1 = float(attack1_slice["volume"].mean())
                vol2 = float(attack2_slice["volume"].mean())
                if vol1 > 0:
                    vol2_vs_1 = vol2 / vol1
            if "volume" in df.columns and len(first_arc_slice) >= 3 and len(second_arc_slice) >= 3:
                first_arc_month_avg_volume = float(first_arc_slice["volume"].mean())
                second_arc_avg_daily_volume = float(second_arc_slice["volume"].mean())
                if first_arc_month_avg_volume > 0:
                    second_arc_volume_ratio = second_arc_avg_daily_volume / first_arc_month_avg_volume
            if len(first_arc_slice) >= 3 and len(second_arc_slice) >= 3:
                first_arc_red_candle_count = int((first_arc_slice["close"] > first_arc_slice["open"]).sum())
                second_arc_red_candle_count = int((second_arc_slice["close"] > second_arc_slice["open"]).sum())
                first_arc_red_candle_ratio = first_arc_red_candle_count / len(first_arc_slice)
                second_arc_red_candle_ratio = second_arc_red_candle_count / len(second_arc_slice)
                second_arc_red_candle_ratio_delta = second_arc_red_candle_ratio - first_arc_red_candle_ratio
            if len(attack1_slice) >= 3 and len(attack2_slice) >= 3:
                red1 = int((attack1_slice["close"] > attack1_slice["open"]).sum())
                red2 = int((attack2_slice["close"] > attack2_slice["open"]).sum())
                if red1 > 0:
                    red_body2_vs_1 = red2 / red1
                elif red2 > 0:
                    red_body2_vs_1 = float("inf")
            right_side_rebound_ok = (
                W_BOTTOM_RIGHT_SIDE_REBOUND_MIN
                <= attack2_gain
                <= W_BOTTOM_RIGHT_SIDE_REBOUND_MAX
            )
            not_extended = current_to_neckline <= 1 and close_position <= 65
            # Low position is a score/ranking feature, not an absolute gate.
            # The W label itself is controlled by geometry, base quality, and
            # early right-side rebound. Neckline proximity is a scoring/risk
            # feature, not the entry gate for this pre-breakout model.
            context_ok = (
                pre_base_ok
                and bool(segment_quality["w_shape_quality_passed"])
                and bool(long_position["w_bottom_long_position_ok"])
                and right_side_rebound_ok
                and not_extended
            )
            candidate: dict[str, float | str | bool] = {
                "available": True,
                "context_ok": context_ok,
                "second_low_gap_pct": second_low_gap,
                "neckline_distance_pct": current_to_neckline,
                "neckline_price": neckline,
                "w_bottom_low_position_pct": max(low_left_position, low_right_position),
                "pre_base_width_pct": pre_width,
                "pre_base_return_pct": pre_return,
                "close_position_pct": close_position,
                "lows_in_lower_base": lows_in_lower_base,
                "attack1_gain_pct": attack1_gain,
                "attack2_gain_pct": attack2_gain,
                "left_decline_pct": left_decline_pct,
                "depth_left_pct": depth_left,
                "depth_right_pct": depth_right,
                "volume_ratio_2_vs_1": vol2_vs_1,
                "first_arc_month_avg_volume": first_arc_month_avg_volume,
                "second_arc_avg_daily_volume": second_arc_avg_daily_volume,
                "second_arc_volume_ratio": second_arc_volume_ratio,
                "first_arc_volume_days": len(first_arc_slice),
                "second_arc_volume_days": len(second_arc_slice),
                "first_arc_red_candle_count": first_arc_red_candle_count,
                "second_arc_red_candle_count": second_arc_red_candle_count,
                "first_arc_red_candle_ratio": first_arc_red_candle_ratio,
                "second_arc_red_candle_ratio": second_arc_red_candle_ratio,
                "second_arc_red_candle_ratio_delta": second_arc_red_candle_ratio_delta,
                "red_body_ratio_2_vs_1": red_body2_vs_1,
                "left_peak_date": str(df["date"].iloc[left_peak_idx]),
                "left_low_date": str(df["date"].iloc[left]),
                "neckline_date": str(df["date"].iloc[neckline_idx]),
                "right_low_date": str(df["date"].iloc[right]),
                "first_arc_start_date": str(first_arc_slice["date"].iloc[0]),
                "first_arc_end_date": str(first_arc_slice["date"].iloc[-1]),
                "second_arc_start_date": str(second_arc_slice["date"].iloc[0]),
                "second_arc_end_date": str(second_arc_slice["date"].iloc[-1]),
                "right_low_age_days": right_age,
            }
            candidate.update(segment_quality)
            candidate.update(long_position)
            if best is None:
                best = candidate
            else:
                candidate_volume = float(candidate.get("second_arc_volume_ratio", math.nan))
                best_volume = float(best.get("second_arc_volume_ratio", math.nan))
                candidate_right = right
                best_date = str(best.get("right_low_date", ""))
                best_right_matches = df.index[df["date"].astype(str).eq(best_date)].tolist()
                best_right = int(best_right_matches[0]) if best_right_matches else -1
                candidate_ok = bool(candidate.get("context_ok"))
                best_ok = bool(best.get("context_ok"))
                # Prefer a valid, recent right trough for the current
                # right-side setup. Neckline proximity should not dominate this
                # pre-breakout model.
                if (
                    (candidate_ok and not best_ok)
                    or (candidate_ok == best_ok and candidate_right > best_right)
                    or (
                        candidate_ok == best_ok
                        and candidate_right == best_right
                        and not math.isnan(candidate_volume)
                        and (math.isnan(best_volume) or candidate_volume > best_volume)
                    )
                ):
                    best = candidate

    if best is None and best_rejected_shape is not None:
        return best_rejected_shape
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
    # W-bottom right side means two similar troughs in a low/base context.
    # The second trough may slightly undercut or sit above the first trough;
    # neckline proximity is scoring/risk, not an entry gate for this model.
    second_low_ok = W_BOTTOM_SECOND_LOW_GAP_MIN <= second_low_gap <= W_BOTTOM_SECOND_LOW_GAP_MAX
    if not second_low_ok:
        return False

    attack_ok = w_bottom_attack_confirmation_ok(row, price_context if price_context.get("available") else None)
    if price_context.get("available"):
        return bool(price_context.get("context_ok")) and attack_ok

    return explicit_w_bottom_context_ok(row) and attack_ok


def cond_w_bottom_right(row: pd.Series) -> bool:
    if already_confirmed_breakout(row):
        return False
    return double_bottom_structure_ok(row)


def cond_neckline_volume_breakout_confirmation(row: pd.Series) -> bool:
    if not neckline_context_45_entry_ok(row):
        return False
    price_context = detected_w_bottom_context(row)
    context_for_use = price_context if price_context.get("available") else None
    return w_bottom_neckline_breakout_confirmation_ok(row, context_for_use)


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
    if tdcc_stealth_attack_already_started(row):
        return False
    if not math.isnan(vol) and vol >= 2.5:
        return False
    phase_ok = phase == "tdcc_leading_price" or (not phase and tdcc_positive(row))
    short_not_attacked = math.isnan(ret5) or ret5 < 8
    not_rallied = math.isnan(ret20) or ret20 < 20
    return phase_ok and short_not_attacked and not_rallied and in_recent_range(row, 10)


def build_specs() -> list[ModelSpec]:
    specs = [
        ModelSpec(
            "volume_range_breakout_v2_low_position_volume_attack",
            "低位放量攻擊",
            "pdf_core_model",
            "confirmation_next_open",
            "訊號日收盤突破前60日高點，且120日位階<=40；盤整、非盤整、寬幅三種型態都可進入。",
            "TDCC top20、MA60>MA120、距離EMA23、量比區間只作加分或分層，不是隱藏買入 gate。",
            "不是低位或未完成隔日續攻確認者不可進正式買入；舊 v1 放量攻擊不得回流 production。",
            "候選成立後先進 pending；確認日為隔日收盤高於訊號日收盤且不低於訊號日最高價；確認後下一交易日開盤進場，停損為收盤連續4天低於MA20/EMA23較低者的4%後隔日開盤，否則第15個交易日收盤出場。",
            cond_volume_breakout_v2_low_position_watch_only,
            score_volume_breakout_v2_low_position,
        ),
        ModelSpec(
            "volume_range_breakout_v2_mid_position_momentum_attack",
            "中位動能放量攻擊",
            "pdf_core_model",
            "confirmation_next_open",
            "訊號日收盤突破前60日高點，且120日位階>40且<=75，型態只收非盤整或寬幅震盪。",
            "TDCC top20、MA60>MA120、距離EMA23、量比區間只作加分或分層，不是隱藏買入 gate。",
            "中位盤整、低位分群、高位階分群與未完成隔日續攻確認者不可進正式買入；舊 v1 放量攻擊不得回流 production。",
            "候選成立後先進 pending；確認日為隔日收盤高於訊號日收盤且不低於訊號日最高價；確認後下一交易日開盤進場，停損為收盤連續4天低於MA20/EMA23較低者的4%後隔日開盤，否則第15個交易日收盤出場。",
            cond_volume_breakout_v2_mid_position_watch_only,
            score_volume_breakout_v2_mid_position,
        ),
        ModelSpec(
            "volume_range_breakout_v2_high_position_volume_attack",
            "高位階放量攻擊",
            "pdf_core_model",
            "confirmation_next_open",
            "訊號日收盤突破前60日高點，120日位階為高位 high_pos_gt75，型態僅收 non_consolidation 或 wide_range，且訊號日 MA60 > MA120。",
            "單項有改善可列加分；多項命中時只採用真實重算後仍改善的 exact combo。組合變差時退回最合適單項統計；目前不採扣分項。",
            "低位分群、中位分群、盤整型高位分群、MA60<=MA120、舊 v1 放量攻擊不得混入本模型。",
            "候選後等待隔日續攻 close-only 確認；確認日收盤成立後，下一個交易日開盤買入。收盤連續4天低於 MA20/EMA23 較低者 4% 隔日開盤停損，否則 D+15 收盤出場。",
            cond_volume_breakout_v2_high_position_watch_only,
            score_volume_breakout_v2_high_position,
        ),
        ModelSpec(
            "price_pullback_23ema",
            "股價回檔模型",
            "pdf_core_model",
            "signal_date_next_open",
            "股價回到23EMA或平台附近，且23EMA斜率向上或結構未破壞。",
            "營收YoY或累計YoY強、未跌破23EMA、TDCC增加、有族群定義、回檔量縮、權證偏多可加分。",
            "不因尚未突破而否決，因為此模型本來是回檔找買點。",
            "適合找健康回檔或回測支撐股；若跌破23EMA且站不回，需降級管理。",
            cond_pullback,
            score_pullback,
        ),
        ModelSpec(
            "hot_theme_pullback",
            "熱門族群回檔模型",
            "pdf_core_model",
            "signal_date_next_open",
            "必須有熱門族群標籤，且股價回到23EMA或合理支撐區附近；不以營收作為必要條件。",
            "熱門族群標籤、接近23EMA或支撐、23EMA向上、量縮回檔、TDCC正向、權證偏多、位階不過高可加分。",
            "基本族群不是入選條件；沒有熱門族群標籤不得進本模型。營收只作加減分，不作必要條件。",
            "用於本夢比或題材主導族群的回檔買點；買後追蹤23EMA、支撐、TDCC與題材延續。",
            cond_hot_theme_pullback,
            score_hot_theme_pullback,
        ),
        ModelSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "pdf_core_model",
            "signal_date_next_open",
            "營收YoY或累計YoY強，且股價仍位於23日盤整區間內；區間用近期最高/最低價加緩衝判斷。",
            "接近平台突破、TDCC溫和增加、量價確認，以及明確核准的非財務事件類型可加分。",
            "EPS、毛利率、營益率、營業利益、業外、淨利及未知事件類型一律不得加分；歷史財報PIT未完整前維持fail closed。",
            "用於找月營收已改善但市場尚未完全反應的股票；後續只觀察平台突破、量價與核准非財務事件，季／年財報維持獨立。",
            cond_revenue_unreacted,
            score_revenue_unreacted,
        ),
        ModelSpec(
            "w_bottom_right_side",
            "W底右側模型",
            "pdf_core_model",
            "signal_date_next_open",
            "W底右側初步成立，右側低點墊高，兩側低點高度不能差距過大；左低右高且已創高者不應歸入此模型。",
            "第二段攻擊量大於第一段、第二段紅K比例提高、TDCC改善、接近頸線、低位階可加分。",
            "低位階作為加分而非絕對條件；避免把低位盤整或創高後回檔誤判成W底。",
            "後續看頸線突破與右側量價品質；跌回右側低點或頸線攻擊失敗則降級。",
            cond_w_bottom_right,
            score_w_bottom,
        ),
        ModelSpec(
            "neckline_volume_breakout_confirmation",
            "W底頸線帶量突破確認模型",
            "pdf_core_model",
            "signal_date_next_open",
            "W底頸線帶量突破確認：股價收盤站上偵測到的W底頸線，並通過量能確認或漲停確認；第二段圓弧均量必須高於第一段基準。",
            "第二段圓弧量能品質、訊號日K棒品質、收盤接近日高、頸線突破幅度、TDCC、權證與營收支持可加分。",
            "不因頸線突破幅度超過10%或20日漲幅高就單獨排除或扣分；長上影線與K棒品質弱仍列為風險扣分。",
            "定位為W底頸線帶量突破確認；訊號日後下一個交易日開盤作為進場基準。不涵蓋倒頭肩底、三重底或其他頸線型態。",
            cond_neckline_volume_breakout_confirmation,
            score_neckline_volume_breakout_confirmation,
        ),
        ModelSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "pdf_core_model",
            "signal_date_next_open",
            "前面有漲勢，回檔未破結構，且重新站回23EMA。",
            "回檔量縮、再攻量增、MACD或KD轉強、TDCC或權證配合可加分。",
            "這是短線修復模型，不要求立即突破前高。",
            "後續看23EMA是否守住與再攻量價是否延續；若跌回23EMA下方且站不回，應降低風險。",
            cond_pullback_short_strength,
            score_pullback_short_reclaim,
        ),
        ModelSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "pdf_core_model",
            "signal_date_next_open",
            "TDCC連續增加，股價尚未大漲，且位於近期盤整區間或尚未完全反應；以tdcc_leading_price為主要狀態。",
            "高級距同步增加、族群也有擴散、TDCC與價格開始初步共振可加分。",
            "price_leading_tdcc與overheated_after_tdcc不可混入潛伏吸籌。",
            "後續看股價是否開始放量確認；若大戶轉弱或價格跌破結構，則降級。",
            cond_tdcc_stealth,
            score_tdcc_stealth,
        ),
    ]
    return [spec for spec in specs if spec.model_id not in DEPRECATED_DAILY_MODEL_IDS]

def build_parameter_table(specs: list[ModelSpec]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for spec in specs:
        profile = MODEL_SCORE_PROFILES.get(spec.model_id)
        row: dict[str, Any] = {
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
        if spec.model_id == "price_pullback_23ema":
            row.update(
                {
                    "model_name_zh": "23EMA回檔模型",
                    "main_conditions": (
                        "股價回到23EMA或支撐附近，且23EMA/均線結構未破；20日漲幅0%到25%；"
                        "TDCC高門檻籌碼增加；OBV站上OBV MA20。"
                    ),
                    "add_score_items": (
                        "技術強勢組合只作操作品質標籤：RSI14>=60且MACD histogram>0。"
                        "籌碼全同步只作理由標籤，不額外加分；本模型不使用營收、權證或熱門族群加分。"
                    ),
                    "forbidden_veto": (
                        "帶量紅K或實體紅K只作追價風險標籤，不作買點品質加分；"
                        "不得使用盤中高低點作正式進出場或勝敗報酬。"
                    ),
                    "operation_guidance": (
                        "買入：訊號成立後隔日開盤買入。賣出：收盤突破訊號日前20日高點後，"
                        "隔日開盤賣出。停損：收盤連續4天低於MA20/EMA23較低者的4%，"
                        "隔日開盤停損。"
                    ),
                    "parameter_status": "approved_operation_v1_close_confirmed",
                }
            )
        if spec.model_id == VOLUME_BREAKOUT_V2_LOW_MODEL_ID:
            row.update(
                {
                    "model_name_zh": "低位放量攻擊",
                    "main_conditions": (
                        "訊號日收盤突破前60日高點，且120日位階<=40；"
                        "盤整、非盤整、寬幅震盪三種形態皆可進入候選。"
                    ),
                    "add_score_items": "TDCC、MA60/MA120、EMA23距離、量比區間只作分層或加分，不作 hidden gate。",
                    "forbidden_veto": "舊 v1 放量攻擊、高位階分群與未符合低位 v2 桶條件者不得進正式買入模型。",
                    "operation_guidance": (
                        "候選成立後等待隔日續攻 close-only 確認；確認後下一交易日開盤進場，"
                        "收盤連續4天低於MA20/EMA23較低者的4%則隔日開盤停損，否則D+15收盤出場。"
                    ),
                    "parameter_status": "approved_operation_v1_close_confirmed",
                }
            )
        if spec.model_id == VOLUME_BREAKOUT_V2_MID_MODEL_ID:
            row.update(
                {
                    "model_name_zh": "中位動能放量攻擊",
                    "main_conditions": (
                        "訊號日收盤突破前60日高點，且120日位階>40且<=75；"
                        "形態只收非盤整或寬幅震盪。"
                    ),
                    "add_score_items": "TDCC、MA60/MA120、EMA23距離、量比區間只作分層或加分，不作 hidden gate。",
                    "forbidden_veto": "低位分群、高位階分群、盤整型中位分群與舊 v1 放量攻擊不得混入本模型。",
                    "operation_guidance": (
                        "候選成立後等待隔日續攻 close-only 確認；確認後下一交易日開盤進場，"
                        "收盤連續4天低於MA20/EMA23較低者的4%則隔日開盤停損，否則D+15收盤出場。"
                    ),
                    "parameter_status": "approved_operation_v1_close_confirmed",
                }
            )
        if profile:
            row.update(
                {
                    "score_profile_id": profile.model_id,
                    "base_score": profile.base_score,
                    "volume_ratio_bonus_per_1x": profile.volume_ratio_bonus_per_1x,
                    "volume_ratio_bonus_cap": profile.volume_ratio_bonus_cap,
                    "tdcc_positive_bonus": profile.tdcc_positive_bonus,
                    "warrant_bullish_bonus": profile.warrant_bullish_bonus,
                    "strong_revenue_bonus": profile.strong_revenue_bonus,
                    "lower_position_bonus": profile.lower_position_bonus,
                    "lower_position_max_off_60d_low_pct": profile.lower_position_max_off_60d_low_pct,
                    "high_return_penalty_threshold_20d": (
                        "" if math.isinf(profile.high_return_penalty_threshold_20d) else profile.high_return_penalty_threshold_20d
                    ),
                    "high_return_penalty": profile.high_return_penalty,
                    "tdcc_distribution_penalty": profile.tdcc_distribution_penalty,
                    "false_breakout_penalty": profile.false_breakout_penalty,
                    "score_profile_scope": "model_specific",
                }
            )
        else:
            row.update(
                {
                    "score_profile_id": "",
                    "base_score": "",
                    "volume_ratio_bonus_per_1x": "",
                    "volume_ratio_bonus_cap": "",
                    "tdcc_positive_bonus": "",
                    "warrant_bullish_bonus": "",
                    "strong_revenue_bonus": "",
                    "lower_position_bonus": "",
                    "lower_position_max_off_60d_low_pct": "",
                    "high_return_penalty_threshold_20d": "",
                    "high_return_penalty": "",
                    "tdcc_distribution_penalty": "",
                    "false_breakout_penalty": "",
                    "score_profile_scope": "not_applicable",
                }
            )
        rows.append(row)
    rows.extend(
        [
            {
                "model_id": "tdcc_short_term_continuation_d5_d10",
                "model_name_zh": "TDCC短線延續模型 D+5/D+10",
                "pdf_visibility": "pdf_core_model",
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
        "base_model_score",
        "operation_score",
        "tdcc_score",
        "pattern_score",
        "risk_penalty",
        "final_rank_score",
        "rank_reason_zh",
        "model_score",
        "model_rank",
        "effective_primary_theme",
        "risk_penalty_tags",
        "next_confirmation",
        "volume_position_bucket_120d",
        "volume_shape_bucket",
        "volume_ma60",
        "volume_ma120",
        "volume_ma60_gt_ma120",
    ]
    if signals.empty:
        return pd.DataFrame(columns=cols)
    out = signals.copy()
    for col in cols:
        if col not in out.columns:
            out[col] = ""
    return out[cols].drop_duplicates(["signal_date", "report_bucket", "stock_id", "model_id"], keep="first")


def selected_volume_breakout_history_signals(max_signal_date: str = "") -> pd.DataFrame:
    # V2 formal models intentionally do not backfill legacy v1 selected rows into
    # the model signal log. Daily operation rows must come from v2 model signals
    # generated by the current formal candidate classifier.
    return pd.DataFrame(columns=snapshot_model_signals(pd.DataFrame()).columns)



def update_model_signal_log(signals: pd.DataFrame) -> pd.DataFrame:
    MODEL_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    current = snapshot_model_signals(signals)
    history = read_csv(MODEL_SIGNAL_LOG_CSV, dtype=str, keep_default_na=False)
    if not history.empty and "model_id" in history.columns:
        history = history[~history["model_id"].astype(str).isin(DEPRECATED_DAILY_MODEL_IDS)].copy()
    current_dates = set(current.get("signal_date", pd.Series(dtype=str)).astype(str).tolist())
    current_dates.discard("")
    max_current_date = max(current_dates) if current_dates else ""
    supplemental = selected_volume_breakout_history_signals(max_current_date)
    if history.empty:
        merged_base = pd.DataFrame()
    else:
        if current_dates and "signal_date" in history.columns:
            history = history[history["signal_date"].astype(str) <= max_current_date].copy()
            history = history[~history["signal_date"].astype(str).isin(current_dates)].copy()
        merged_base = history

    def keyset(frame: pd.DataFrame) -> set[tuple[str, str, str]]:
        if frame.empty:
            return set()
        for col in ["signal_date", "stock_id", "model_id"]:
            if col not in frame.columns:
                return set()
        return {
            (safe_str(row.get("signal_date")), normalize_code(row.get("stock_id")), safe_str(row.get("model_id")))
            for _, row in frame.iterrows()
        }

    if not supplemental.empty:
        existing_keys = keyset(merged_base) | keyset(current)
        supplemental = supplemental[
            ~supplemental.apply(
                lambda row: (
                    safe_str(row.get("signal_date")),
                    normalize_code(row.get("stock_id")),
                    safe_str(row.get("model_id")),
                )
                in existing_keys,
                axis=1,
            )
        ].copy()

    frames = [frame for frame in [merged_base, supplemental, current] if not frame.empty]
    merged = pd.concat(frames, ignore_index=True, sort=False) if frames else pd.DataFrame(columns=current.columns)
    if not merged.empty:
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
        repeat["display_rank_repeated_signal"] = repeat["same_model_repeat_rank"].map(lambda rank: f"連續榜 #{int(rank)}")
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
                        "model_name_zh": "23EMA回檔模型" if spec.model_id == "price_pullback_23ema" else spec.model_name_zh,
                        "model_group": spec.pdf_visibility,
                        "main_condition_met": "True",
                        "entry_basis": spec.entry_basis,
                        "model_score": score,
                        "score_components": " | ".join(comps),
                        "risk_penalty_tags": " | ".join(dict.fromkeys(risks)),
                        "original_category": category(row),
                        "tdcc_status": tdcc_status(row),
                        "warrant_flow_signal": warrant_signal(row),
                        "volume_ratio": num(row, "volume_ratio"),
                        "return_5d": num(row, "return_5d", "return_5d_pct"),
                        "return_20d": num(row, "return_20d", "return_20d_pct"),
                        "price_pullback_signal_date": text(row, "price_pullback_signal_date"),
                        "price_pullback_operation_quality": (
                            price_pullback_operation_quality(row) if spec.model_id == "price_pullback_23ema" else ""
                        ),
                        "price_pullback_reason_tags": (
                            price_pullback_reason_tags(row) if spec.model_id == "price_pullback_23ema" else ""
                        ),
                        "price_pullback_risk_tags": (
                            "volume_red_or_solid_red_risk"
                            if spec.model_id == "price_pullback_23ema"
                            and price_pullback_volume_red_or_solid_red_risk(row)
                            else ""
                        ),
                        "price_pullback_tdcc_history_available": text(row, "price_pullback_tdcc_history_available"),
                        "price_pullback_high_thresholds_up": text(row, "price_pullback_high_thresholds_up"),
                        "price_pullback_all_thresholds_up": text(row, "price_pullback_all_thresholds_up"),
                        "price_pullback_obv_above_ma20": text(row, "price_pullback_obv_above_ma20"),
                        "price_pullback_rsi14": num(row, "price_pullback_rsi14"),
                        "price_pullback_macd_hist": num(row, "price_pullback_macd_hist"),
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


def load_volume_price_history(stock_id: str) -> pd.DataFrame:
    path = STOCK_PRICE_HISTORY_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = read_csv(path, dtype=str, keep_default_na=False)
    if price.empty or "date" not in price.columns:
        return pd.DataFrame()
    out = price.copy()
    out["date"] = out["date"].map(lambda value: safe_str(value).replace("-", "").replace("/", ""))
    out = out[out["date"].astype(str).str.fullmatch(r"\d{8}", na=False)].copy()
    for col in ["open", "high", "low", "close", "volume"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    return out


def volume_position_features(price: pd.DataFrame, signal_date: str, days: int) -> dict[str, float]:
    empty = {
        f"off_{days}d_low_pct": math.nan,
        f"range_width_{days}_pct": math.nan,
        f"position_in_{days}d_range_pct": math.nan,
    }
    if price.empty:
        return empty
    positions = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    if not positions:
        return empty
    signal_idx = int(positions[-1])
    start = max(0, signal_idx - days + 1)
    window = price.iloc[start : signal_idx + 1]
    if len(window) < min(days, 30):
        return empty
    signal_close = float(price.iloc[signal_idx]["close"])
    low = pd.to_numeric(window["low"], errors="coerce").min()
    high = pd.to_numeric(window["high"], errors="coerce").max()
    if math.isnan(signal_close) or math.isnan(low) or math.isnan(high) or low <= 0 or high <= low:
        return empty
    return {
        f"off_{days}d_low_pct": (signal_close / low - 1.0) * 100.0,
        f"range_width_{days}_pct": (high / low - 1.0) * 100.0,
        f"position_in_{days}d_range_pct": (signal_close - low) / (high - low) * 100.0,
    }


def volume_ma_trend_features(price: pd.DataFrame, signal_date: str) -> dict[str, Any]:
    empty = {
        "ma60": math.nan,
        "ma120": math.nan,
        "ma60_gt_ma120": False,
    }
    if price.empty:
        return empty
    positions = price.index[price["date"].astype(str).eq(signal_date)].tolist()
    if not positions:
        return empty
    signal_idx = int(positions[-1])
    closes = pd.to_numeric(price["close"], errors="coerce")
    ma60 = closes.rolling(60, min_periods=60).mean().iloc[signal_idx]
    ma120 = closes.rolling(120, min_periods=120).mean().iloc[signal_idx]
    if math.isnan(ma60) or math.isnan(ma120):
        return empty
    return {
        "ma60": float(ma60),
        "ma120": float(ma120),
        "ma60_gt_ma120": bool(ma60 > ma120),
    }


def volume_position_bucket(value: float) -> str:
    if math.isnan(value):
        return "unknown_position"
    if value <= 40:
        return "low_pos_le40"
    if value <= 75:
        return "mid_pos_40_75"
    return "high_pos_gt75"


def volume_shape_bucket(row: pd.Series, price: pd.DataFrame, signal_date: str) -> str:
    features_60 = volume_position_features(price, signal_date, 60)
    range_width_60 = to_number(row.get("range_width_60_pct", features_60["range_width_60_pct"]))
    if math.isnan(range_width_60):
        range_width_60 = features_60["range_width_60_pct"]

    range_width_40 = to_number(row.get("range_width_40_pct", row.get("range_width_pct", "")))
    if math.isnan(range_width_40):
        features_40 = volume_position_features(price, signal_date, 40)
        range_width_40 = features_40["range_width_40_pct"]

    if not math.isnan(range_width_60) and range_width_60 > 80:
        return "wide_range"
    if not math.isnan(range_width_40) and range_width_40 <= 40:
        return "consolidation"
    return "non_consolidation"


def volume_v2_model_memberships(row: pd.Series, stock_id: str, signal_date: str) -> tuple[list[str], dict[str, Any]]:
    price = load_volume_price_history(stock_id)
    features_120 = volume_position_features(price, signal_date, 120)
    ma_features = volume_ma_trend_features(price, signal_date)
    position_120 = features_120["position_in_120d_range_pct"]
    position_bucket = volume_position_bucket(position_120)
    shape = volume_shape_bucket(row, price, signal_date)
    memberships: list[str] = []
    if position_bucket == "low_pos_le40":
        memberships.append(VOLUME_BREAKOUT_V2_LOW_MODEL_ID)
    if position_bucket == "mid_pos_40_75" and shape in {"non_consolidation", "wide_range"}:
        memberships.append(VOLUME_BREAKOUT_V2_MID_MODEL_ID)
    if (
        position_bucket == "high_pos_gt75"
        and shape in {"non_consolidation", "wide_range"}
        and bool(ma_features["ma60_gt_ma120"])
    ):
        memberships.append(VOLUME_BREAKOUT_V2_HIGH_MODEL_ID)
    return memberships, {
        "position_bucket_120d": position_bucket,
        "shape_bucket": shape,
        **ma_features,
        **features_120,
    }


def volume_v2_model_name(model_id: str) -> str:
    if model_id == VOLUME_BREAKOUT_V2_LOW_MODEL_ID:
        return "低位放量攻擊"
    if model_id == VOLUME_BREAKOUT_V2_MID_MODEL_ID:
        return "中位動能放量攻擊"
    return "放量攻擊"


def volume_v2_model_name(model_id: str) -> str:
    if model_id == VOLUME_BREAKOUT_V2_LOW_MODEL_ID:
        return "低位放量攻擊"
    if model_id == VOLUME_BREAKOUT_V2_MID_MODEL_ID:
        return "中位動能放量攻擊"
    return "放量攻擊"


def append_volume_breakout_signals(signals: pd.DataFrame, candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    df = read_csv(VOLUME_BREAKOUT_WATCH, dtype=str, keep_default_na=False)
    if df.empty:
        return signals
    lookup = candidate_lookup(candidates)
    rows: list[dict[str, Any]] = []
    valid_statuses = {"selected"}
    valid_types = {"bottom_volume_attack"}
    for idx, row in df.iterrows():
        breakout_type = text(row, "volume_breakout_type", "breakout_type").lower()
        selection_status = text(row, "selection_status").lower()
        if breakout_type not in valid_types or selection_status not in valid_statuses:
            continue
        stock_id = normalize_code(text(row, "stock_id"))
        if not stock_id:
            continue
        candidate_row = lookup.get(stock_id)
        if candidate_row is None:
            raise RuntimeError(
                "volume breakout formal signal has no canonical all_candidates source row: "
                f"stock_id={stock_id}"
            )
        source = candidate_row
        authoritative_warrant_signal = warrant_signal(candidate_row)
        score_source = source.to_dict() if isinstance(source, pd.Series) else {}
        score_source.update(row.to_dict())
        score_source["warrant_flow_signal"] = authoritative_warrant_signal
        memberships, v2_features = volume_v2_model_memberships(
            row,
            stock_id,
            signal_date or text(row, "signal_date", "date"),
        )
        if not memberships:
            continue
        model_id = memberships[0]
        score_source.update(v2_features)
        if model_id == VOLUME_BREAKOUT_V2_HIGH_MODEL_ID:
            score, comps, risks = score_volume_breakout_v2_high_position(pd.Series(score_source))
        else:
            score, comps, risks = score_volume_breakout_profile(pd.Series(score_source), model_id)
        raw_risks = text(row, "risk_flags", "risk_penalty_tags")
        for risk in re.split(r"[|,;]+", raw_risks):
            item = risk.strip()
            if item:
                risks.append(item)
        priority = text(row, "volume_breakout_priority")
        if priority.startswith("B_"):
            risks.append(priority)
        notes = text(row, "volume_breakout_notes")
        breakout_pct = bottom_volume_attack_breakout_pct(pd.Series(score_source))
        comps = [f"type={breakout_type}", f"volume_ratio={row.get('volume_ratio','')}".strip(), *comps]
        if not math.isnan(breakout_pct):
            comps.append(f"breakout_pct={breakout_pct:.2f}%")
        comps.append(f"position_bucket_120d={v2_features['position_bucket_120d']}")
        comps.append(f"shape_bucket={v2_features['shape_bucket']}")
        if notes:
            comps.append(notes)
        score_fields = volume_breakout_operation_score_fields(pd.Series(score_source), score, risks, model_id)
        final_score = score_fields["final_rank_score"]
        if score_fields["rank_reason_zh"]:
            comps.append(f"操作排序:{score_fields['rank_reason_zh']}")
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
                "model_id": model_id,
                "model_name_zh": volume_v2_model_name(model_id),
                "model_group": "pdf_core_model",
                "main_condition_met": "True",
                "entry_basis": "confirmation_next_open",
                "base_model_score": score_fields["base_model_score"],
                "operation_score": score_fields["operation_score"],
                "tdcc_score": score_fields["tdcc_score"],
                "pattern_score": score_fields["pattern_score"],
                "risk_penalty": score_fields["risk_penalty"],
                "final_rank_score": final_score,
                "rank_reason_zh": score_fields["rank_reason_zh"],
                "model_score": final_score,
                "score_components": " | ".join([c for c in comps if c]),
                "risk_penalty_tags": " | ".join(dict.fromkeys(risks)),
                "original_category": category(source),
                "tdcc_status": text(row, "tdcc_status") or tdcc_status(source),
                "warrant_flow_signal": authoritative_warrant_signal,
                "volume_ratio": num(row, "volume_ratio"),
                "return_5d": num(row, "return_5d", "return_5d_pct"),
                "return_20d": num(row, "return_20d", "return_20d_pct"),
                "volume_position_bucket_120d": v2_features["position_bucket_120d"],
                "volume_shape_bucket": v2_features["shape_bucket"],
                "volume_position_in_120d_range_pct": (
                    round(v2_features["position_in_120d_range_pct"], 4)
                    if not math.isnan(v2_features["position_in_120d_range_pct"])
                    else ""
                ),
                "volume_range_width_120_pct": (
                    round(v2_features["range_width_120_pct"], 4)
                    if not math.isnan(v2_features["range_width_120_pct"])
                    else ""
                ),
                "volume_ma60": (
                    round(v2_features["ma60"], 4)
                    if not math.isnan(v2_features["ma60"])
                    else ""
                ),
                "volume_ma120": (
                    round(v2_features["ma120"], 4)
                    if not math.isnan(v2_features["ma120"])
                    else ""
                ),
                "volume_ma60_gt_ma120": "True" if bool(v2_features["ma60_gt_ma120"]) else "False",
                "next_confirmation": text(row, "next_volume_breakout_confirmation") or text(source, "next_confirmation"),
                "model_main_conditions": (
                    "低位放量攻擊：120日位階<=40且三種shape皆收；"
                    "中位動能放量攻擊：120日位階>40且<=75，且shape為非盤整或寬幅。"
                ),
                "model_add_score_items": "TDCC top20、MA60>MA120、距離EMA23、量比區間只作加分或分層，不作隱藏 gate。",
                "model_forbidden_veto": "舊 v1 放量攻擊、高位階分群與未符合 v2 桶條件者不得進正式買入模型。",
                "model_operation_guidance": "候選後等待隔日續攻收盤確認；確認後下一交易日開盤進場，MA20/EMA23 4日收盤停損，否則D+15收盤出場。",
                "selection_semantics": "volume_range_breakout_v2_candidate_bucket_condition_met",
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
    df = filter_tdcc_edge_candidates_to_latest_week(df)
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
                    "model_group": "pdf_core_model",
                    "main_condition_met": "True",
                    "entry_basis": "signal_date_next_open",
                    "model_score": score,
                    "score_components": " | ".join(score_parts),
                    "risk_penalty_tags": "|".join(risk_tags),
                    "original_category": "short_term_specialty",
                    "tdcc_status": text(row, "tdcc_price_phase"),
                    "warrant_flow_signal": "",
                    "volume_ratio": "",
                    "return_5d": "",
                    "return_20d": "",
                    "next_confirmation": "短線延續專項；用隔日開盤作為研究觀察基準，檢查D+1到D+10收盤/最高價。",
                    "model_main_conditions": "all_thresholds_overheated或phase_overheated_after_tdcc，搭配MACD/KD/Bollinger與1W/2W漲幅條件。",
                    "model_add_score_items": "D+1到D+10 next-open close/high統計、樣本數、相對報酬、market regime分層。",
                    "model_forbidden_veto": "不是低位布局模型，不可混入TDCC潛伏吸籌。",
                    "model_operation_guidance": "隔日開盤作為研究觀察基準；依D+1到D+10收盤/最高價統計做短線延續檢查。",
                    "selection_semantics": "specialty_condition_met_rank_by_tdcc_short_term_score",
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
    "platform_volume_breakout": "平台帶量突破",
    "neckline_volume_breakout": "頸線帶量突破",
    "strict_60d_volume_breakout": "60日高點帶量突破",
    "range_breakout_volume": "帶量突破盤整區間",
    "range_breakout_watch": "接近盤整上緣觀察",
    "ma_reclaim_volume_attack": "帶量站回均線",
    "near_high_volume_watch": "接近前高帶量觀察",
    "strict_high_breakout": "帶量突破波段高點",
    "failed_range_breakout_risk": "盤整突破漲幅過低風險",
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
    "neckline_volume_breakout_confirmation": "W底頸線帶量突破確認",
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
    "price_pullback_23ema": "股價回檔模型",
    "hot_theme_pullback": "熱門族群回檔模型",
    "revenue_unreacted_range": "營收爆發但股價尚未反應模型",
    "w_bottom_right_side": "W底右側模型",
    "neckline_volume_breakout_confirmation": "W底頸線帶量突破確認模型",
    "pullback_short_reclaim": "回檔後短線轉強模型",
    "tdcc_stealth_accumulation": "TDCC潛伏吸籌模型",
    "tdcc_short_continuation": "TDCC短線延續模型 D+5/D+10",
    "tdcc_short_term_continuation_d5_d10": "TDCC短線延續模型 D+5/D+10",
    "short_term_surge_d5_d10": "短線急漲 D+5/D+10",
    "group_fund_rotation": "族群資金輪動模型",
}

MODEL_HUMAN_REASON_ZH = {
    "price_pullback_23ema": "符合股價回檔模型，股價接近23EMA或支撐區，回測後轉強。",
    "hot_theme_pullback": "符合熱門族群回檔模型，具熱門族群標籤，股價回測23EMA或支撐後轉強。",
    "revenue_unreacted_range": "符合營收爆發但股價尚未反應模型，營收動能較強且股價仍在整理區。",
    "w_bottom_right_side": "符合W底右側模型，右側低點墊高並接近頸線或轉強區。",
    "neckline_volume_breakout_confirmation": "符合W底頸線帶量突破確認模型，股價已站上頸線且第二弧量能高於第一弧基準。",
    "pullback_short_reclaim": "符合回檔後短線轉強模型，前段漲勢後回檔未破結構並重新轉強。",
    "tdcc_stealth_accumulation": "符合TDCC潛伏吸籌模型，大戶籌碼改善，股價尚未完全反應。",
    "tdcc_short_continuation": "符合TDCC短線延續模型，歷史短線延續樣本具參考性，適合作D+5/D+10短線延續觀察。",
    "tdcc_short_term_continuation_d5_d10": "符合TDCC短線延續模型，歷史短線延續樣本具參考性，適合作D+5/D+10短線延續觀察。",
    "short_term_surge_d5_d10": "符合短線急漲研究條件，僅作短線動能研究觀察，不作低位買進模型。",
}

MODEL_OPERATION_REMINDER_ZH = {
    "price_pullback_23ema": "回檔模型不要求先突破；若跌破23EMA或支撐且無法快速收回，需降低風險。",
    "hot_theme_pullback": "熱門族群回檔以族群標籤與23EMA附近支撐為主；若族群退潮或跌破支撐需降風險。",
    "tdcc_stealth_accumulation": "TDCC為加分與追蹤項，不可單獨作為買進理由；若價格跌破支撐或量價失敗需降風險。",
    "tdcc_short_continuation": "以訊號日隔天開盤為進場假設，後續依D+5 / D+10統計結果與價格轉弱條件管理。",
    "tdcc_short_term_continuation_d5_d10": "以訊號日隔天開盤為進場假設，後續依D+5 / D+10統計結果與價格轉弱條件管理。",
    "short_term_surge_d5_d10": "這是短線研究補充，不是低位買進模型；需用隔天開盤與D+N收盤 / 最高價統計管理。",
}

MODEL_NAME_ZH_BY_ID.update(
    {
        VOLUME_BREAKOUT_V2_LOW_MODEL_ID: "低位放量攻擊",
        VOLUME_BREAKOUT_V2_MID_MODEL_ID: "中位動能放量攻擊",
    }
)
MODEL_HUMAN_REASON_ZH.update(
    {
        VOLUME_BREAKOUT_V2_LOW_MODEL_ID: "符合低位放量攻擊模型，訊號日收盤突破前60日高點，且位於120日低位區。",
        VOLUME_BREAKOUT_V2_MID_MODEL_ID: "符合中位動能放量攻擊模型，訊號日收盤突破前60日高點，且屬中位非整理或寬幅動能型態。",
    }
)
MODEL_OPERATION_REMINDER_ZH.update(
    {
        VOLUME_BREAKOUT_V2_LOW_MODEL_ID: (
            "等待隔日續攻 close-only 確認；確認後下一交易日開盤買入，"
            "MA20/EMA23 4日收盤停損，否則D+15收盤出場。"
        ),
        VOLUME_BREAKOUT_V2_MID_MODEL_ID: (
            "等待隔日續攻 close-only 確認；確認後下一交易日開盤買入，"
            "MA20/EMA23 4日收盤停損，否則D+15收盤出場。"
        ),
    }
)


MODEL_NAME_ZH_BY_ID[VOLUME_BREAKOUT_V2_HIGH_MODEL_ID] = "高位階放量攻擊"
MODEL_HUMAN_REASON_ZH[VOLUME_BREAKOUT_V2_HIGH_MODEL_ID] = (
    "符合高位階放量攻擊模型：訊號日收盤突破前60日高點，120日位階為高位，"
    "型態為非盤整或寬幅震盪，且 MA60 > MA120。"
)
MODEL_OPERATION_REMINDER_ZH[VOLUME_BREAKOUT_V2_HIGH_MODEL_ID] = (
    "等待隔日續攻 close-only 確認；確認後下一交易日開盤買入，"
    "收盤連續4天低於 MA20/EMA23 較低者 4% 隔日開盤停損，否則 D+15 收盤出場。"
)


FORBIDDEN_PDF_TOKENS = [
    "call_strong_inflow",
    "call_put_bullish",
    "call_inflow",
    "put_inflow",
    "put_strong_inflow",
    "mixed_flow",
    "no_signal",
    "strong_accumulation",
    "mild_accumulation",
    "distribution_warning",
    "short_term_specialty",
    "range_rebound",
    "revenue_pullback",
    "revenue_breakout_low_response",
    "pullback_rebound",
    "hot_theme_tag",
    "hot theme tag",
    "non_mainstream",
    "mainstream",
    "neckline",
    "breakout",
    "insufficient_data",
]
RAW_PDF_TOKEN_RE = re.compile(r"(^|[\s|/、,;])([a-z]+(?:_[a-z0-9]+){1,})(?=$|[\s|/、,;])")


REPORT_MODEL_ID_ALIASES = {
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
        suffix = ""
        lookup_key = key
        if ":" in key:
            possible_key, possible_suffix = key.split(":", 1)
            if possible_key.strip():
                lookup_key = possible_key.strip()
                suffix = ":" + possible_suffix.strip()
        label = mapping.get(lookup_key) or PDF_TOKEN_ZH.get(lookup_key) or translate_pdf_text(lookup_key)
        if suffix:
            label = f"{label}{suffix}"
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
    "theme_display_zh",
    "theme_resolution_status",
    "theme_key",
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


ROTATION_THEME_DISPLAY_ZH = {
    "ASIC": "特殊應用 IC / ASIC",
    "DRAM IC": "記憶體 IC / DRAM",
    "DRAM/Flash": "記憶體 / DRAM 與 Flash",
    "91": "DR / 外國上市",
    "DR_or_foreign_listing": "DR / 外國上市",
    "ETF_or_index_product": "指數 / ETF / ETN商品",
    "etf_or_index_product": "指數 / ETF / ETN商品",
    "MLCC": "被動元件 / MLCC",
    "MOSFET": "功率半導體 / MOSFET",
    "PCB": "印刷電路板 / PCB",
    "optoelectronics": "光電",
    "指數/ETF/ETN商品": "指數 / ETF / ETN商品",
}

UNRESOLVED_ROTATION_THEME_VALUES = {
    "",
    "其他",
    "其他業",
    "other",
    "theme_unknown",
    "unclassified",
    "needs_manual_review",
}

RAW_ENGLISH_THEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_ -]*$")


def has_cjk_text(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def is_unresolved_rotation_theme(value: Any) -> bool:
    text = safe_str(value)
    if text in UNRESOLVED_ROTATION_THEME_VALUES:
        return True
    if text.isdigit():
        return True
    if RAW_ENGLISH_THEME_RE.fullmatch(text) and not has_cjk_text(text):
        return True
    return False


def resolve_rotation_theme(value: Any) -> dict[str, str]:
    raw = safe_str(value)
    display = ROTATION_THEME_DISPLAY_ZH.get(raw, raw)
    status = "unresolved" if is_unresolved_rotation_theme(display) else "resolved"
    return {
        "theme_key": raw,
        "theme": display,
        "theme_display_zh": display,
        "theme_resolution_status": status,
    }


def build_rotation(candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    taxonomy = read_csv(STOCK_THEME_TAXONOMY, dtype={"stock_id": str})
    if taxonomy.empty:
        return pd.DataFrame(columns=ROTATION_COLUMNS)

    def rotation_themes(item: pd.Series) -> list[dict[str, str]]:
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

        cleaned: list[dict[str, str]] = []
        seen: set[str] = set()
        for value in values:
            resolved = resolve_rotation_theme(value)
            if resolved["theme_resolution_status"] != "resolved":
                continue
            theme = resolved["theme"]
            if not theme or theme in seen:
                continue
            seen.add(theme)
            cleaned.append(resolved)
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

        for theme_info in rotation_themes(item):
            rows_for_group.append(
                {
                    "stock_id": stock_id,
                    "stock_name": safe_str(item.get("stock_name")),
                    "theme": theme_info["theme"],
                    "theme_display_zh": theme_info["theme_display_zh"],
                    "theme_resolution_status": theme_info["theme_resolution_status"],
                    "theme_key": theme_info["theme_key"],
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
        if not theme_text:
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
            theme_keys = "|".join(sorted({safe_str(value) for value in part["theme_key"] if safe_str(value)}))
            theme_statuses = {safe_str(value) for value in part["theme_resolution_status"] if safe_str(value)}
            theme_status = "resolved" if theme_statuses == {"resolved"} and not is_unresolved_rotation_theme(theme_text) else "unresolved"
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
                    "theme": theme_text,
                    "theme_display_zh": theme_text,
                    "theme_resolution_status": theme_status,
                    "theme_key": theme_keys,
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
    candidates = enrich_price_pullback_v1_context(candidates, signal_date)
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
