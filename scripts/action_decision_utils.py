from __future__ import annotations

import math
from collections.abc import Mapping
from typing import Any

from tracking_utils import safe_str, to_number


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


def compute_action_decision(row: Mapping[str, Any]) -> dict[str, str]:
    category = _get(row, "model_id", "original_category", "category", "breakout_type").lower()
    stage = _get(row, "pattern_stage", "pattern").lower()
    priority = _get(row, "decision_priority", "priority")
    score = _num(row, "decision_score", "model_score", "score", "pattern_score")
    volume_ratio = _num(row, "volume_ratio")
    return_5d = _num(row, "return_5d", "return_5d_pct")
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
        ["below_23ema_not_reclaimed", "lost_23ema", "wait_reclaim", "跌破23ema未收回", "跌破未站回"],
    )
    revenue_deceleration = _contains_any(text_blob, ["revenue_deceleration", "revenue_breaks", "營收轉弱"])
    benchmark_weak = _contains_any(text_blob, ["benchmark_weak", "benchmark lag", "benchmark落後"])
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
        or _contains_any(text_blob, ["continued_overheated", "mainstream_overheated", "overheated_after_tdcc", "already_priced_in", "priced_in=true"])
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

    entry_prerequisites = []
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

    if action_rating in {"avoid", "reduce"}:
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
        ["exit_if_lost_23ema", "exit_if_lost_recent_low", "exit_if_revenue_breaks", "exit_if_tdcc_and_price_both_weaken"]
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
    }
