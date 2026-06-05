from __future__ import annotations

import math
import re
from collections.abc import Mapping
from typing import Any

from tracking_utils import safe_str, to_number


DISPLAY_FALLBACK = "資料不足 / 暫用現有資料"

ACTION_COLUMNS = [
    "action_rating",
    "action_rating_label_zh",
    "entry_style",
    "position_sizing",
    "management_plan",
    "entry_prerequisites",
    "post_entry_watch_items",
    "downgrade_reason",
    "confidence_level",
    "thesis_state",
    "action_rating_display_zh",
    "action_summary_zh",
    "entry_strategy_zh",
    "position_sizing_zh",
    "add_position_strategy_zh",
    "take_profit_strategy_zh",
    "risk_control_zh",
    "post_entry_watch_zh",
    "final_decision_zh",
    "score_interpretation_zh",
    "model_category_display_zh",
    "entry_prerequisites_zh",
]

ACTION_LABELS = {
    "buy_now": "建議買進",
    "scale_in": "可分批買進",
    "starter_position": "可小量試單",
    "wait_pullback": "等待回檔",
    "wait_reclaim": "等待站回",
    "hold_only": "已持有續抱",
    "take_profit": "停利",
    "reduce": "減碼",
    "avoid": "不建議買進 / 避開",
}

POST_ENTRY_WATCH_ITEMS = [
    "next_monthly_revenue",
    "next_tdcc_update",
    "23ema_hold_or_reclaim",
    "volume_price_confirmation",
    "prior_high_breakout_quality",
    "sector_benchmark_strength",
    "event_follow_through",
    "warrant_overheat_check",
]

CATEGORY_LABELS = {
    "true_breakout": "嚴格突破",
    "strict_breakout": "嚴格突破",
    "volume_range_breakout": "底部放量攻擊模型",
    "range_breakout_volume": "底部放量攻擊模型",
    "bottom_volume_attack": "底部放量攻擊模型",
    "volume_breakout": "底部放量攻擊模型",
    "volume_attack": "底部放量攻擊",
    "hot_theme_pullback": "熱門族群回檔模型",
    "theme_pullback": "熱門族群回檔模型",
    "revenue_growth_pullback": "營收成長股價回檔模型",
    "revenue_pullback": "營收成長股價回檔模型",
    "revenue_breakout_low_response": "營收爆發但股價尚未反應模型",
    "tdcc_pre_move": "TDCC 潛伏吸籌模型",
    "tdcc_quiet_accumulation": "TDCC 潛伏吸籌模型",
    "tdcc_short_term_edge": "TDCC 短線延續模型 D+5/D+10",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "pullback_rebound": "回檔後短線轉強模型",
    "w_bottom_right_side": "W 底右側模型",
    "w_bottom_attack": "W 底右側模型",
    "platform_turn_strong": "平台整理轉強模型",
    "near_high_neckline": "接近前高 / 頸線挑戰模型",
    "near_resistance": "接近前高 / 頸線挑戰模型",
    "short_term_specialty": "短線專項",
    "pattern": "型態觀察",
}

ENTRY_STYLE_LABELS = {
    "current_price_ok": "目前價位可評估第一筆",
    "pullback_to_23ema": "回測 23EMA 附近",
    "pullback_to_support": "回測支撐區",
    "reclaim_23ema": "等待站回 23EMA",
    "breakout_follow": "突破後順勢追蹤",
    "post_breakout_retest": "突破後回測確認",
    "no_entry_now": "目前不適合新買",
}

POSITION_SIZE_LABELS = {
    "normal_position": "正常部位",
    "half_position": "半部位",
    "starter_1_3": "試單 1/3 部位",
    "starter_1_4": "試單 1/4 部位",
    "observe_only": "僅觀察",
    "reduce_position": "降低部位",
    "exit_position": "退出部位",
}

MANAGEMENT_LABELS = {
    "buy_first_tranche_now": "可建立第一筆部位",
    "buy_first_tranche_near_support": "接近支撐時可建立第一筆部位",
    "add_on_23ema_hold": "守住 23EMA 後再評估加碼",
    "add_on_reclaim_23ema": "站回 23EMA 後再評估加碼",
    "add_on_breakout": "放量突破後再評估加碼",
    "take_profit_near_prior_high": "接近前高或壓力區可分批停利",
    "take_profit_on_volume_price_failure": "量價失敗或爆量不漲時降低部位",
    "exit_if_lost_23ema": "跌破 23EMA 且 1 至 3 日內無法收回時退出",
    "exit_if_lost_recent_low": "跌破近期低點時退出",
    "exit_if_revenue_breaks": "營收或財報明顯轉弱時降低部位",
    "exit_if_tdcc_and_price_both_weaken": "TDCC 與價格同步轉弱時退出",
}

PREREQUISITE_LABELS = {
    "model_recommended": "已符合模型條件",
    "decision_priority_high": "追蹤優先級高",
    "decision_score_high": "模型分數高",
    "price_structure_not_broken": "價格結構未破壞",
    "near_23ema_or_support": "接近 23EMA 或支撐區",
    "revenue_not_deteriorating": "營收未明顯轉弱",
    "no_major_tdcc_warning": "沒有重大 TDCC 轉弱警訊",
    "no_major_volume_price_failure": "沒有重大量價失敗",
    "acceptable_risk_reward": "風險報酬可接受",
}

WATCH_LABELS = {
    "next_monthly_revenue": "下一次月營收",
    "next_tdcc_update": "下一次 TDCC 更新",
    "23ema_hold_or_reclaim": "23EMA 是否守住或快速站回",
    "volume_price_confirmation": "量價是否延續確認",
    "prior_high_breakout_quality": "前高突破品質",
    "sector_benchmark_strength": "族群與 benchmark 強弱",
    "event_follow_through": "事件催化是否延續",
    "warrant_overheat_check": "權證是否過熱",
}

DOWNGRADE_LABELS = {
    "insufficient_price_data": "價格資料不足",
    "insufficient_tdcc_history": "TDCC 歷史不足",
    "tdcc_distribution_warning": "TDCC 轉弱警訊",
    "volume_price_failure": "量價失敗",
    "below_23ema_not_reclaimed": "跌破 23EMA 尚未站回",
    "revenue_deceleration": "營收成長放緩",
    "benchmark_weak": "落後 benchmark",
    "price_too_extended": "股價乖離過大",
    "risk_reward_unfavorable": "風險報酬不佳",
    "event_unverified": "事件尚未確認",
    "breakout_failed": "突破失敗",
}

THESIS_LABELS = {
    "healthy_pullback": "健康回檔",
    "momentum_reset": "動能重置",
    "breakout_initial": "初步突破",
    "breakout_confirmed": "突破確認",
    "post_breakout_retest": "突破後回測",
    "high_level_consolidation": "高位整理",
    "high_level_distribution_risk": "高位派發風險",
    "failed_breakout": "突破失敗",
    "trend_failure_risk": "趨勢失敗風險",
    "unclear": "訊號不明",
}


def _get(row: Mapping[str, Any], *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_y", f"{name}_x"):
            if candidate in row:
                value = safe_str(row.get(candidate, ""))
                if value:
                    return value
    return ""


def _num(row: Mapping[str, Any], *names: str) -> float:
    for name in names:
        value = _get(row, name)
        if not value:
            continue
        number = to_number(value)
        if not math.isnan(number):
            return number
    return float("nan")


def _truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y", "t"}


def _contains_any(text: str, needles: list[str]) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def _join(items: list[str]) -> str:
    return "|".join(dict.fromkeys([item for item in items if item]))


def _split_items(value: str) -> list[str]:
    text = safe_str(value)
    if not text:
        return []
    return [part.strip() for part in re.split(r"[|,;、\n]+", text) if part.strip()]


def _translate_items(items: list[str] | str, mapping: Mapping[str, str], fallback: str = DISPLAY_FALLBACK) -> str:
    if isinstance(items, str):
        raw_items = _split_items(items)
    else:
        raw_items = [safe_str(item) for item in items if safe_str(item)]

    labels: list[str] = []
    for item in raw_items:
        key = item.lower()
        label = mapping.get(item) or mapping.get(key)
        if label:
            labels.append(label)
    if labels:
        return "、".join(dict.fromkeys(labels))
    return fallback


def re_has_slug(text: str) -> bool:
    return bool(re.search(r"\b[a-z]+_[a-z0-9_]+\b", safe_str(text)))


def _first_display_value(row: Mapping[str, Any], *names: str) -> str:
    for name in names:
        value = _get(row, name)
        if value:
            return value
    return ""


def _category_display(row: Mapping[str, Any], category: str) -> str:
    direct = _first_display_value(
        row,
        "model_name_zh",
        "category_cn",
        "category_zh",
        "source_category_zh",
        "category_display_zh",
    )
    if direct and not re_has_slug(direct):
        return direct

    for token in _split_items(category):
        label = CATEGORY_LABELS.get(token.lower())
        if label:
            return label
    return "單一個股分析"


def _score_interpretation(score: float, action_rating: str) -> str:
    if math.isnan(score):
        score_text = "目前缺少完整分數資料，需以價格、TDCC 與風險條件輔助判斷。"
    elif score >= 82:
        score_text = "模型分數高，代表條件集中度較強。"
    elif score >= 68:
        score_text = "模型分數中上，代表條件有支持，但仍需依風控管理。"
    else:
        score_text = "模型分數偏低，僅適合作為低部位觀察。"

    if action_rating in {"buy_now", "scale_in", "starter_position"}:
        return f"{score_text} 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。"
    if action_rating in {"wait_pullback", "wait_reclaim"}:
        return f"{score_text} 目前還沒有新的第一筆買點，需等待回檔或站回條件成立。"
    if action_rating in {"take_profit", "reduce", "avoid"}:
        return f"{score_text} 目前以風險管理為主，不適合新買第一筆。"
    return f"{score_text} 目前以既有部位管理與條件追蹤為主。"


def _build_display_fields(
    row: Mapping[str, Any],
    *,
    action_rating: str,
    score: float,
    category: str,
    entry_style: str,
    position_sizing: str,
    management_plan: list[str],
    entry_prerequisites: list[str],
    downgrade_reasons: list[str],
    post_entry_watch_items: list[str],
    confidence: str,
    thesis_state: str,
) -> dict[str, str]:
    action_label = ACTION_LABELS.get(action_rating, DISPLAY_FALLBACK)
    category_label = _category_display(row, category)
    thesis_label = THESIS_LABELS.get(thesis_state, "訊號不明")
    entry_label = ENTRY_STYLE_LABELS.get(entry_style, "進場條件尚未完成")
    position_label = POSITION_SIZE_LABELS.get(position_sizing, "僅觀察")
    management_text = _translate_items(management_plan, MANAGEMENT_LABELS)
    prerequisite_text = _translate_items(entry_prerequisites, PREREQUISITE_LABELS)
    watch_text = _translate_items(post_entry_watch_items, WATCH_LABELS)
    downgrade_text = _translate_items(downgrade_reasons, DOWNGRADE_LABELS)
    score_text = _score_interpretation(score, action_rating)

    if action_rating in {"buy_now", "scale_in", "starter_position"}:
        summary = f"符合 {category_label}，價格結構尚未破壞，操作評級為「{action_label}」。"
    elif action_rating == "wait_pullback":
        summary = f"{category_label} 條件有支持，但目前風險報酬不佳，操作評級為「等待回檔」。"
    elif action_rating == "wait_reclaim":
        summary = f"{category_label} 條件有支持，但價格尚未修復關鍵線，操作評級為「等待站回」。"
    elif action_rating in {"take_profit", "reduce", "avoid"}:
        summary = f"{category_label} 已出現風險管理訊號，操作評級為「{action_label}」。"
    else:
        summary = f"{category_label} 目前屬於「{thesis_label}」，以既有部位管理與條件追蹤為主。"

    if management_text == DISPLAY_FALLBACK:
        management_text = "依 23EMA、支撐壓力、量價與 TDCC 變化管理。"
    if watch_text == DISPLAY_FALLBACK:
        watch_text = "追蹤下一次營收、TDCC 更新、23EMA 防守與量價延續。"
    if downgrade_text == DISPLAY_FALLBACK:
        downgrade_text = "若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。"

    if action_rating in {"buy_now", "scale_in", "starter_position"} and position_sizing != "observe_only":
        entry_strategy = f"{entry_label}；可依「{position_label}」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。"
    elif action_rating == "hold_only":
        entry_strategy = "已持有以續抱管理為主；新買需等待重新出現進場條件。"
    elif action_rating == "wait_pullback":
        entry_strategy = "目前等待回檔，不建立新部位；回測支撐或 23EMA 不破後再評估。"
    elif action_rating == "wait_reclaim":
        entry_strategy = "目前等待站回，不建立新部位；站回 23EMA 或關鍵壓力後再評估。"
    elif action_rating == "take_profit":
        entry_strategy = "目前進入停利管理，不建議新買第一筆。"
    elif action_rating == "reduce":
        entry_strategy = "目前風險升高，以降低部位為主，不建議新買。"
    elif action_rating == "avoid":
        entry_strategy = "目前不建議新買。"
    else:
        entry_strategy = "目前僅觀察，等待新的模型條件或價格結構確認。"

    position_text = f"{position_label}；部位大小需依支撐距離、波動與模型確認度控制。"
    take_profit_text = "接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。"
    final_decision = f"{summary} 進場策略：{entry_strategy} 追蹤項目：{watch_text} 風控：{downgrade_text}"

    return {
        "action_rating_display_zh": action_label,
        "action_summary_zh": summary,
        "entry_strategy_zh": entry_strategy,
        "position_sizing_zh": position_text,
        "add_position_strategy_zh": management_text,
        "take_profit_strategy_zh": take_profit_text,
        "risk_control_zh": downgrade_text,
        "post_entry_watch_zh": watch_text,
        "final_decision_zh": final_decision,
        "score_interpretation_zh": score_text,
        "model_category_display_zh": category_label,
        "entry_prerequisites_zh": prerequisite_text,
    }


def compute_action_decision(row: Mapping[str, Any]) -> dict[str, str]:
    category = _get(row, "model_id", "original_category", "category", "breakout_type").lower()
    stage = _get(row, "pattern_stage", "pattern").lower()
    priority = _get(row, "decision_priority", "priority")
    score = _num(row, "decision_score", "model_score", "score", "pattern_score")
    return_20d = _num(row, "return_20d", "return_20d_pct")
    distance_to_ma20 = _num(row, "distance_to_ma20_pct", "gap_ma20_pct")
    distance_to_ema23 = _num(row, "distance_to_ema23_pct")
    risk_bucket = _get(row, "risk_handling_bucket")
    trade_decision = _get(row, "trade_decision")
    tdcc_status = _get(row, "tdcc_status", "tdcc_judgement", "tdcc_accumulation_signal").lower()
    warrant_signal = _get(row, "warrant_flow_signal", "warrant_status").lower()
    downgrade_flags = _get(row, "downgrade_flags")
    risk_tags = _get(row, "risk_tags")
    why_downgraded = _get(row, "why_downgraded")
    text_blob = " ".join(
        [
            category,
            stage,
            priority,
            risk_bucket,
            trade_decision,
            tdcc_status,
            warrant_signal,
            downgrade_flags,
            _get(row, "raw_downgrade_flags"),
            risk_tags,
            _get(row, "raw_risk_tags"),
            why_downgraded,
            _get(row, "overheat_status"),
            _get(row, "already_priced_in"),
            _get(row, "catalyst_overheated"),
            _get(row, "must_not_overstate"),
        ]
    ).lower()

    hard_exclusion = _truthy(_get(row, "hard_exclusion_flag")) or "hard_exclusion" in text_blob
    tdcc_distribution = "distribution" in tdcc_status or "distribution_warning" in text_blob
    volume_price_failure = _contains_any(
        text_blob,
        [
            "volume_price_failure",
            "failed_breakout",
            "false_breakout",
            "breakout_failed",
            "high_volume_black_candle",
        ],
    )
    below_reclaim_needed = _contains_any(
        text_blob,
        ["below_23ema_not_reclaimed", "lost_23ema", "wait_reclaim"],
    )
    revenue_deceleration = _contains_any(text_blob, ["revenue_deceleration", "revenue_breaks"])
    benchmark_weak = _contains_any(text_blob, ["benchmark_weak", "benchmark lag"])
    insufficient_price = _contains_any(text_blob, ["insufficient_price_data"])
    insufficient_tdcc = _contains_any(text_blob, ["insufficient_tdcc_history"])
    risk_reward_unfavorable = _contains_any(text_blob, ["risk_reward_unfavorable"])

    attack_confirmed = (
        _truthy(_get(row, "true_breakout"))
        or _truthy(_get(row, "strict_breakout"))
        or _truthy(_get(row, "platform_breakout_flag"))
        or _truthy(_get(row, "neckline_breakout_flag"))
        or stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}
    )
    model_recommended = priority in {"A_priority_watch", "B_confirm_needed"} or (
        not math.isnan(score) and score >= 68
    )
    score_high = not math.isnan(score) and score >= 82
    priority_high = priority == "A_priority_watch"
    overextended = (
        (not math.isnan(return_20d) and return_20d >= 30)
        or (not math.isnan(distance_to_ma20) and distance_to_ma20 >= 18)
        or (not math.isnan(distance_to_ema23) and distance_to_ema23 >= 15)
        or _contains_any(
            text_blob,
            [
                "continued_overheated",
                "mainstream_overheated",
                "overheated_after_tdcc",
                "already_priced_in",
                "priced_in=true",
            ],
        )
    )
    near_support = (
        "pullback" in category
        or "range_rebound" in category
        or "reclaim" in stage
        or (not math.isnan(distance_to_ma20) and abs(distance_to_ma20) <= 5)
        or (not math.isnan(distance_to_ema23) and abs(distance_to_ema23) <= 5)
    )
    price_structure_not_broken = not (
        hard_exclusion or volume_price_failure or below_reclaim_needed or "trend_failure" in text_blob
    )
    acceptable_risk_reward = not overextended and not risk_reward_unfavorable

    downgrade_reasons: list[str] = []
    if insufficient_price:
        downgrade_reasons.append("insufficient_price_data")
    if insufficient_tdcc:
        downgrade_reasons.append("insufficient_tdcc_history")
    if tdcc_distribution:
        downgrade_reasons.append("tdcc_distribution_warning")
    if volume_price_failure:
        downgrade_reasons.append("volume_price_failure")
    if below_reclaim_needed:
        downgrade_reasons.append("below_23ema_not_reclaimed")
    if revenue_deceleration:
        downgrade_reasons.append("revenue_deceleration")
    if benchmark_weak:
        downgrade_reasons.append("benchmark_weak")
    if overextended:
        downgrade_reasons.append("price_too_extended")
    if risk_reward_unfavorable:
        downgrade_reasons.append("risk_reward_unfavorable")
    if _contains_any(text_blob, ["event_unverified", "catalyst_unverified"]):
        downgrade_reasons.append("event_unverified")

    entry_prerequisites: list[str] = []
    if model_recommended:
        entry_prerequisites.append("model_recommended")
    if priority_high:
        entry_prerequisites.append("decision_priority_high")
    if score_high:
        entry_prerequisites.append("decision_score_high")
    if price_structure_not_broken:
        entry_prerequisites.append("price_structure_not_broken")
    if near_support:
        entry_prerequisites.append("near_23ema_or_support")
    if not revenue_deceleration:
        entry_prerequisites.append("revenue_not_deteriorating")
    if not tdcc_distribution:
        entry_prerequisites.append("no_major_tdcc_warning")
    if not volume_price_failure:
        entry_prerequisites.append("no_major_volume_price_failure")
    if acceptable_risk_reward:
        entry_prerequisites.append("acceptable_risk_reward")

    if hard_exclusion or insufficient_price:
        action_rating = "avoid"
    elif volume_price_failure or (tdcc_distribution and below_reclaim_needed):
        action_rating = "reduce"
    elif below_reclaim_needed:
        action_rating = "wait_reclaim"
    elif overextended and model_recommended and price_structure_not_broken:
        action_rating = "take_profit" if attack_confirmed else "wait_pullback"
    elif priority_high and score_high and price_structure_not_broken and acceptable_risk_reward:
        action_rating = "buy_now" if attack_confirmed or not near_support else "scale_in"
    elif model_recommended and price_structure_not_broken and near_support:
        action_rating = "scale_in"
    elif model_recommended and price_structure_not_broken:
        action_rating = "starter_position"
    elif price_structure_not_broken and priority == "C_watch_only":
        action_rating = "starter_position"
    else:
        action_rating = "hold_only"

    if action_rating in {"avoid", "reduce", "take_profit", "hold_only"}:
        entry_style = "no_entry_now"
    elif action_rating == "wait_reclaim":
        entry_style = "reclaim_23ema"
    elif action_rating == "wait_pullback":
        entry_style = "pullback_to_support"
    elif "breakout" in category or attack_confirmed:
        entry_style = "breakout_follow"
    elif near_support:
        entry_style = "pullback_to_23ema"
    else:
        entry_style = "current_price_ok"

    if action_rating == "buy_now":
        position_sizing = "normal_position"
    elif action_rating == "scale_in":
        position_sizing = "half_position"
    elif action_rating == "starter_position":
        position_sizing = "starter_1_3" if score_high else "starter_1_4"
    elif action_rating == "reduce":
        position_sizing = "reduce_position"
    elif action_rating == "avoid":
        position_sizing = "exit_position"
    else:
        position_sizing = "observe_only"

    management_plan: list[str] = []
    if action_rating == "buy_now":
        management_plan.append("buy_first_tranche_now")
    if action_rating in {"scale_in", "starter_position"}:
        management_plan.append(
            "buy_first_tranche_now" if entry_style == "current_price_ok" else "buy_first_tranche_near_support"
        )
    if action_rating in {"buy_now", "scale_in", "starter_position"}:
        management_plan.extend(["add_on_23ema_hold", "add_on_reclaim_23ema", "add_on_breakout"])
    if action_rating in {"buy_now", "scale_in", "starter_position", "hold_only", "take_profit"}:
        management_plan.extend(["take_profit_near_prior_high", "take_profit_on_volume_price_failure"])
    management_plan.extend(
        [
            "exit_if_lost_23ema",
            "exit_if_lost_recent_low",
            "exit_if_revenue_breaks",
            "exit_if_tdcc_and_price_both_weaken",
        ]
    )

    if action_rating in {"buy_now", "scale_in"} and not downgrade_reasons and score_high:
        confidence = "high"
    elif action_rating in {"buy_now", "scale_in", "starter_position", "wait_pullback", "hold_only"}:
        confidence = "medium"
    else:
        confidence = "low"

    if volume_price_failure:
        thesis_state = "failed_breakout"
    elif "trend_failure" in text_blob or below_reclaim_needed:
        thesis_state = "trend_failure_risk"
    elif tdcc_distribution and overextended:
        thesis_state = "high_level_distribution_risk"
    elif stage == "breakout_confirmed":
        thesis_state = "breakout_confirmed"
    elif attack_confirmed:
        thesis_state = "breakout_initial"
    elif near_support and model_recommended:
        thesis_state = "healthy_pullback"
    elif overextended:
        thesis_state = "high_level_consolidation"
    else:
        thesis_state = "unclear"

    display_fields = _build_display_fields(
        row,
        action_rating=action_rating,
        score=score,
        category=category,
        entry_style=entry_style,
        position_sizing=position_sizing,
        management_plan=management_plan,
        entry_prerequisites=entry_prerequisites,
        downgrade_reasons=downgrade_reasons,
        post_entry_watch_items=POST_ENTRY_WATCH_ITEMS,
        confidence=confidence,
        thesis_state=thesis_state,
    )

    return {
        "action_rating": action_rating,
        "action_rating_label_zh": ACTION_LABELS[action_rating],
        "entry_style": entry_style,
        "position_sizing": position_sizing,
        "management_plan": _join(management_plan),
        "entry_prerequisites": _join(entry_prerequisites),
        "post_entry_watch_items": _join(POST_ENTRY_WATCH_ITEMS),
        "downgrade_reason": _join(downgrade_reasons),
        "confidence_level": confidence,
        "thesis_state": thesis_state,
        **display_fields,
    }
