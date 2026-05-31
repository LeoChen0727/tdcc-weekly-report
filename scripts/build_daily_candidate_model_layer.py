from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    main_price_date_from_freshness,
    normalize_code,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
VOLUME_BREAKOUT_WATCH = LATEST_DIR / "volume_breakout_watch_latest.csv"
TDCC_EDGE_CANDIDATES = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
WEEKLY_SURGE_CANDIDATES = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv"
MODEL_PARAMETER_RECOMMENDATIONS = LATEST_DIR / "daily_model_parameter_recommendations_latest.csv"
MODEL_HISTORY_DIR = Path("output/history/daily_candidate_models")
MODEL_SIGNAL_LOG_CSV = MODEL_HISTORY_DIR / "daily_candidate_model_signal_log.csv"

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
    return buckets[0] if buckets else "unclassified"


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
    return ["unclassified"]


def primary_theme(row: pd.Series) -> str:
    return (
        text(row, "effective_primary_theme", "primary_theme", "taxonomy_primary_theme")
        or text(row, "細分族群", "theme_name", "industry")
        or "未分類"
    )


def effective_structural_theme_bucket(row: pd.Series) -> str:
    return text(
        row,
        "effective_structural_theme_bucket",
        "structural_theme_bucket",
        "taxonomy_structural_theme_bucket",
    )


def effective_mainstream_label(row: pd.Series) -> str:
    return text(row, "effective_mainstream_label", "taxonomy_effective_mainstream_label", "theme_mainstream_label")


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


def score_w_bottom(row: pd.Series) -> tuple[float, list[str], list[str]]:
    score, comps, risks = model_score_common(row)
    second_low_gap = num(row, "second_low_gap_pct")
    neckline_distance = num(row, "distance_to_neckline_pct")
    vol = num(row, "volume_ratio")
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
    return near_ema23_or_platform(row) and ema23_slope_proxy_up(row)


def cond_revenue_unreacted(row: pd.Series) -> bool:
    return strong_revenue(row) and in_recent_range(row, 5)


def double_bottom_structure_ok(row: pd.Series) -> bool:
    """Require actual double-bottom geometry, not only a broad pattern flag."""
    if text(row, "category", "original_category").lower() != "pattern":
        return False
    current_stage = stage(row)
    if current_stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}:
        return False
    second_low_gap = num(row, "second_low_gap_pct")
    neckline_distance = num(row, "distance_to_neckline_pct")
    if math.isnan(second_low_gap) or math.isnan(neckline_distance):
        return False
    # W-bottom right side means the second low is higher and price is still
    # challenging the neckline from below. Confirmed breakouts belong to other
    # breakout models, not this early right-side model.
    second_low_ok = 0.0 <= second_low_gap <= 4.0
    neckline_ok = -3.0 <= neckline_distance < 0.0
    return second_low_ok and neckline_ok


def cond_w_bottom_right(row: pd.Series) -> bool:
    return double_bottom_structure_ok(row)


def cond_neckline_challenge(row: pd.Series) -> bool:
    vol = num(row, "volume_ratio")
    return near_neckline_or_prior_high(row) and not math.isnan(vol) and vol >= 1.2 and ema23_slope_proxy_up(row)


def cond_platform_strength(row: pd.Series) -> bool:
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
    ret20 = num(row, "return_20d", "return_20d_pct")
    if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
        return False
    phase_ok = phase == "tdcc_leading_price" or tdcc_positive(row)
    not_rallied = math.isnan(ret20) or ret20 < 20
    return phase_ok and not_rallied and in_recent_range(row, 10)


def build_specs() -> list[ModelSpec]:
    common_add = "TDCC正向、權證偏多、營收較佳、位階較低可加分；主流/非主流只分報告，不扣分。"
    return [
        ModelSpec(
            "volume_range_breakout",
            "帶量突破模型",
            "pdf_core_model",
            "signal_date_next_open",
            "量比 >= 1.5 且突破盤整區間/平台/頸線/波段高點。",
            "突破前高/平台、收盤站上突破區、量比越高、盤整結構越乾淨、TDCC/權證/營收越好加分。",
            "不以漲幅過大、中位爆量、高位爆量直接否決；風險只扣分排序。",
            "隔日開盤為進場原點；觀察收盤是否守住突破區，跌回突破區或爆量長上影則降風險。",
            cond_volume_breakout,
            score_volume_breakout,
        ),
        ModelSpec(
            "price_pullback_23ema",
            "股價回檔模型",
            "pdf_core_model",
            "signal_date_next_open",
            "股價回到23EMA或平台附近，且23EMA斜率代理為正。",
            "營收YoY/累計YoY、未跌破23EMA、TDCC增加、族群定義、量縮回檔、權證偏多加分。",
            "不因尚未突破而否決，因本模型本來就是回檔找買點。",
            "隔日開盤為進場原點；回測23EMA或平台不破才續看，跌破後1到3日站不回則降級。",
            cond_pullback,
            score_pullback,
        ),
        ModelSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "pdf_core_model",
            "signal_date_next_open",
            "營收YoY或累計YoY強，且股價仍在近20/23日區間上下5%內。",
            "接近平台突破、TDCC溫和增加、EPS/毛利確認、新聞或轉型題材加分。",
            "不可只因尚未突破就否決。",
            "隔日開盤為進場原點；等待營收題材轉成量價或籌碼確認，跌破盤整下緣則退出觀察。",
            cond_revenue_unreacted,
            model_score_common,
        ),
        ModelSpec(
            "w_bottom_right_side",
            "W底右側模型",
            "pdf_core_model",
            "signal_date_next_open",
            "W底成立且右側低點墊高。",
            "第二段攻擊量大於第一段、紅K比例提高、TDCC改善、接近頸線加分。",
            "不與嚴格突破混成同一條件。",
            "隔日開盤為進場原點；右側低點不可跌破，接近頸線後需放量確認。",
            cond_w_bottom_right,
            score_w_bottom,
        ),
        ModelSpec(
            "near_high_neckline_challenge",
            "接近前高/頸線挑戰模型",
            "pdf_core_model",
            "signal_date_next_open",
            "距前高/頸線0%到5%，量能開始放大，均線轉正。",
            "越接近頸線、TDCC/權證越好、成交量溫和放大加分。",
            "用途是提前抓突破前1到5日，不要求已突破。",
            "隔日開盤為進場原點；若放量突破前高/頸線且收盤不跌回，優先度提高。",
            cond_neckline_challenge,
            model_score_common,
        ),
        ModelSpec(
            "platform_strengthening",
            "平台整理轉強模型",
            "pdf_core_model",
            "signal_date_next_open",
            "盤整區間形成、波動收斂、接近上緣、量能回升且出現帶量實體紅K。",
            "盤整時間長、回測不破、TDCC溫和增加加分。",
            "不以未突破60日高點否決。",
            "隔日開盤為進場原點；守住平台上緣或回測不破才續看，跌回區間內則降級。",
            cond_platform_strength,
            model_score_common,
        ),
        ModelSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "pdf_core_model",
            "signal_date_next_open",
            "前面有漲勢，回檔未破結構，重新站回23EMA或短均結構轉強。",
            "回檔量縮、再攻量增、MACD/KD轉強、TDCC/權證加分。",
            "不以還沒創高否決。",
            "隔日開盤為進場原點；重新站回23EMA後不可快速跌回，量價續強才保留。",
            cond_pullback_short_strength,
            model_score_common,
        ),
        ModelSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "pdf_core_model",
            "signal_date_next_open",
            "TDCC連續或溫和增加，股價尚未大漲，且股價仍在近20/23日區間上下10%內；優先tdcc_leading_price。",
            "高級距同步增加、族群擴散、TDCC/權證正向加分。",
            "排除price_leading_tdcc與overheated_after_tdcc，不混入過熱模型。",
            "隔日開盤為進場原點；等待價格開始反應且TDCC未轉弱，若股價先過熱則改列短線/風險觀察。",
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
                "pdf_visibility": "pdf_specialty_section",
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
                "main_conditions": "有族群標籤，且同族群超過1/3股票量比>=3。",
                "add_score_items": "族群出量比例、出量股票數、龍頭/老二/老三擴散狀態。",
                "forbidden_veto": "不是個股買進模型，只列族群。",
                "operation_guidance": "只判斷族群資金是否擴散，不直接產生個股買進結論。",
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
    return pd.DataFrame(rows)


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
    like three different recommendations.
    """

    if signals.empty:
        out = signals.copy()
        out["frontpage_display_allowed"] = ""
        out["frontpage_duplicate_reason"] = ""
        return out

    out = signals.copy()
    out["frontpage_display_allowed"] = "False"
    out["frontpage_duplicate_reason"] = "not_pdf_core_model"
    out["_score_num"] = pd.to_numeric(out.get("model_score", ""), errors="coerce").fillna(-999)
    out["_rank_num"] = pd.to_numeric(out.get("model_rank", ""), errors="coerce").fillna(999999)

    core_mask = out.get("model_group", "").astype(str).eq("pdf_core_model")
    core = out[core_mask].sort_values(
        ["report_bucket", "stock_id", "_score_num", "_rank_num", "model_id"],
        ascending=[True, True, False, True, True],
    )
    allowed_idx = core.drop_duplicates(["report_bucket", "stock_id"], keep="first").index
    duplicate_idx = core.index.difference(allowed_idx)

    out.loc[core.index, "frontpage_duplicate_reason"] = ""
    out.loc[allowed_idx, "frontpage_display_allowed"] = "True"
    out.loc[duplicate_idx, "frontpage_duplicate_reason"] = "duplicate_stock_already_shown_on_frontpage"
    return out.drop(columns=["_score_num", "_rank_num"])


def build_frontpage_unique(signals: pd.DataFrame) -> pd.DataFrame:
    if signals.empty:
        return pd.DataFrame()

    work = signals[signals.get("model_group", "").astype(str).eq("pdf_core_model")].copy()
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
                "model_hit_count": len(part),
                "model_hits": _join_unique(part["model_name_zh"]),
                "model_hit_ids": _join_unique(part["model_id"]),
                "same_model_repeat_status": text(top, "same_model_repeat_status"),
                "same_model_consecutive_days": top.get("same_model_consecutive_days", ""),
                "same_model_appear_count_5d": top.get("same_model_appear_count_5d", ""),
                "same_model_appear_count_10d": top.get("same_model_appear_count_10d", ""),
                "tdcc_status": text(top, "tdcc_status"),
                "warrant_flow_signal": text(top, "warrant_flow_signal"),
                "volume_ratio": top.get("volume_ratio", ""),
                "risk_penalty_tags": _join_unique(part["risk_penalty_tags"]),
                "score_components": text(top, "score_components"),
                "next_confirmation": text(top, "next_confirmation"),
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
        return out, pd.DataFrame()

    out = signals.copy()
    if model_log.empty:
        out["same_model_consecutive_days"] = 1
        out["same_model_appear_count_5d"] = 1
        out["same_model_appear_count_10d"] = 1
        out["same_model_repeat_status"] = "new_model_signal"
        return out, pd.DataFrame()

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
                        "report_line_memberships": text(row, "report_line_memberships", "taxonomy_report_line_memberships"),
                        "mainstream_report_eligible": text(row, "mainstream_report_eligible", "taxonomy_mainstream_report_eligible"),
                        "non_mainstream_report_eligible": text(row, "non_mainstream_report_eligible", "taxonomy_non_mainstream_report_eligible"),
                        "dual_report_membership_flag": text(row, "dual_report_membership_flag", "taxonomy_dual_report_membership_flag"),
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
    return "unclassified"


def append_volume_breakout_signals(signals: pd.DataFrame, candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    df = read_csv(VOLUME_BREAKOUT_WATCH, dtype=str, keep_default_na=False)
    if df.empty:
        return signals
    lookup = candidate_lookup(candidates)
    rows: list[dict[str, Any]] = []
    valid_statuses = {"selected", "selected_but_routed_to_other_category"}
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
        source = candidate_row if candidate_row is not None else row
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
                "report_line_memberships": text(source, "report_line_memberships", "taxonomy_report_line_memberships"),
                "mainstream_report_eligible": text(source, "mainstream_report_eligible", "taxonomy_mainstream_report_eligible"),
                "non_mainstream_report_eligible": text(source, "non_mainstream_report_eligible", "taxonomy_non_mainstream_report_eligible"),
                "dual_report_membership_flag": text(source, "dual_report_membership_flag", "taxonomy_dual_report_membership_flag"),
                "report_bucket": external_report_bucket(row, candidate_row),
                "model_id": "volume_breakout_range",
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
    rows: list[dict[str, Any]] = []
    df = read_csv(TDCC_EDGE_CANDIDATES, dtype=str, keep_default_na=False)
    if not df.empty:
        for idx, row in df.iterrows():
            d10 = to_number(row.get("d10_win_rate_pct", ""))
            d5 = to_number(row.get("d5_win_rate_pct", ""))
            score = 50 + (0 if math.isnan(d10) else d10 * 0.35) + (0 if math.isnan(d5) else d5 * 0.15)
            rows.append(
                {
                    "signal_date": text(row, "signal_date") or signal_date,
                    "source_row_index": f"tdcc_edge:{idx}",
                    "stock_id": normalize_code(text(row, "stock_id")),
                    "stock_name": text(row, "stock_name"),
                    "industry": "",
                    "primary_theme": text(row, "theme"),
                    "effective_primary_theme": text(row, "theme"),
                    "secondary_themes": "",
                    "effective_structural_theme_bucket": "",
                    "effective_mainstream_label": "",
                    "report_line_memberships": "",
                    "mainstream_report_eligible": "",
                    "non_mainstream_report_eligible": "",
                    "dual_report_membership_flag": "",
                    "report_bucket": "unclassified",
                    "model_id": "tdcc_short_term_continuation_d5_d10",
                    "model_name_zh": "TDCC短線延續模型 D+5/D+10",
                    "model_group": "pdf_specialty_section",
                    "main_condition_met": "True",
                    "entry_basis": "signal_date_next_open",
                    "model_score": round(clamp(score), 1),
                    "score_components": f"D+5 win={row.get('d5_win_rate_pct','')} / D+10 win={row.get('d10_win_rate_pct','')}",
                    "risk_penalty_tags": "",
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
                    "selection_semantics": "specialty_condition_met_rank_by_backtest_stats",
                }
            )
    surge = read_csv(WEEKLY_SURGE_CANDIDATES, dtype=str, keep_default_na=False)
    if not surge.empty:
        for idx, row in surge.iterrows():
            d10 = to_number(row.get("best_d10_hit_rate_pct", ""))
            d5 = to_number(row.get("best_d5_hit_rate_pct", ""))
            score = 50 + (0 if math.isnan(d10) else d10 * 0.35) + (0 if math.isnan(d5) else d5 * 0.15)
            rows.append(
                {
                    "signal_date": text(row, "date") or signal_date,
                    "source_row_index": f"short_surge:{idx}",
                    "stock_id": normalize_code(text(row, "stock_id")),
                    "stock_name": text(row, "stock_name"),
                    "industry": "",
                    "primary_theme": text(row, "theme"),
                    "effective_primary_theme": text(row, "theme"),
                    "secondary_themes": "",
                    "effective_structural_theme_bucket": "",
                    "effective_mainstream_label": "",
                    "report_line_memberships": "",
                    "mainstream_report_eligible": "",
                    "non_mainstream_report_eligible": "",
                    "dual_report_membership_flag": "",
                    "report_bucket": "unclassified",
                    "model_id": "short_term_surge_d5_d10",
                    "model_name_zh": "短線急漲D+5/D+10模型",
                    "model_group": "pdf_specialty_section",
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


def build_rotation(candidates: pd.DataFrame, signal_date: str) -> pd.DataFrame:
    if candidates.empty:
        return pd.DataFrame()
    work = candidates.copy()
    work["primary_theme"] = work.apply(primary_theme, axis=1)
    work["volume_ratio_num"] = pd.to_numeric(work.get("volume_ratio", ""), errors="coerce")
    work["is_volume_expansion_3x"] = work["volume_ratio_num"] >= 3
    rows: list[dict[str, Any]] = []
    for theme, part in work.groupby("primary_theme", dropna=False):
        if not safe_str(theme) or theme == "未分類":
            continue
        total = len(part)
        if total < 2:
            continue
        expansion = int(part["is_volume_expansion_3x"].sum())
        ratio = expansion / total if total else 0
        if ratio < 1 / 3:
            continue
        leaders = (
            part.sort_values("volume_ratio_num", ascending=False)
            .head(3)[["stock_id", "stock_name", "volume_ratio_num"]]
            .fillna("")
            .to_dict("records")
        )
        rows.append(
            {
                "signal_date": signal_date,
                "theme": theme,
                "stock_count": total,
                "volume_expansion_3x_count": expansion,
                "volume_expansion_ratio": round(ratio, 4),
                "leader_1": f"{leaders[0].get('stock_id','')} {leaders[0].get('stock_name','')}" if len(leaders) > 0 else "",
                "leader_2": f"{leaders[1].get('stock_id','')} {leaders[1].get('stock_name','')}" if len(leaders) > 1 else "",
                "leader_3": f"{leaders[2].get('stock_id','')} {leaders[2].get('stock_name','')}" if len(leaders) > 2 else "",
                "interpretation": "族群資金輪動觀察；不是個股買進模型。",
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(["volume_expansion_ratio", "volume_expansion_3x_count", "theme"], ascending=[False, False, True]).reset_index(drop=True)


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
        "- Front-page rule: use `daily_candidate_frontpage_unique_latest.csv/md` for first-page representatives; do not repeat the same stock three times because it hit multiple models.",
        "- Repeat rule: same-stock same-model repeat appearances are not score penalties. Use `daily_candidate_same_model_repeat_latest.csv/md` as a separate persistence table.",
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
            "report_bucket",
            "stock_id",
            "stock_name",
            "effective_primary_theme",
            "primary_model_name_zh",
            "primary_model_score",
            "model_hit_count",
            "model_hits",
            "same_model_repeat_status",
            "same_model_consecutive_days",
            "risk_penalty_tags",
            "next_confirmation",
        ]
        available_cols = [col for col in cols if col in frontpage_unique.columns]
        lines.append(frontpage_unique[available_cols].head(60).to_markdown(index=False))
    lines.extend(["", "## Same Model Repeat Table", ""])
    if same_model_repeat.empty:
        lines.append("_No same-model repeat rows yet._")
    else:
        cols = [
            "same_model_repeat_rank",
            "report_bucket",
            "model_id",
            "model_name_zh",
            "stock_id",
            "stock_name",
            "same_model_consecutive_days",
            "same_model_appear_count_5d",
            "same_model_appear_count_10d",
            "model_score",
            "effective_primary_theme",
            "next_confirmation",
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
    signal_date = main_price_date_from_freshness()
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
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
    report_signals = build_report_ready_model_signals(signals)
    model_log = update_model_signal_log(report_signals)
    report_signals, same_model_repeat = attach_same_model_repeat(report_signals, model_log)
    report_signals = annotate_frontpage_uniqueness(report_signals)
    frontpage_unique = build_frontpage_unique(report_signals)
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
