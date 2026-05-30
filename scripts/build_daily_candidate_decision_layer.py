from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    main_price_date_from_freshness,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    resolve_candidate_signal_date,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
ALL_CANDIDATES_MD = LATEST_DIR / "all_candidates_latest.md"
STOCK_THEME_TAXONOMY = LATEST_DIR / "stock_theme_taxonomy_latest.csv"

REGRESSION_2484_MD = LATEST_DIR / "daily_candidate_regression_2484_latest.md"
REGRESSION_2484_CSV = LATEST_DIR / "daily_candidate_regression_2484_latest.csv"
REGRESSION_8069_CSV = LATEST_DIR / "daily_candidate_regression_8069_latest.csv"

DECISION_CSV = LATEST_DIR / "daily_candidate_decision_latest.csv"
DECISION_MD = LATEST_DIR / "daily_candidate_decision_latest.md"
DECISION_PACKET = LATEST_DIR / "daily_candidate_decision_chatgpt_packet_latest.md"


CATEGORY_ORDER = {
    "true_breakout": 10,
    "breakout": 10,
    "range_rebound": 20,
    "near_resistance": 21,
    "abnormal_volume_up": 22,
    "revenue_breakout_low_response": 30,
    "revenue_pullback": 40,
    "pullback_rebound": 50,
    "pattern": 60,
}

CATEGORY_CN = {
    "true_breakout": "嚴格突破",
    "breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

PRIORITY_SORT = {
    "A_priority_watch": 1,
    "B_confirm_needed": 2,
    "C_watch_only": 3,
    "D_risk_downgrade": 4,
}

DECISION_COLUMNS = [
    "source_row_index",
    "signal_date",
    "stock_id",
    "stock_name",
    "original_category",
    "original_category_cn",
    "breakout_type",
    "pattern_stage",
    "pattern_mapped_category",
    "pattern_route",
    "decision_priority",
    "decision_priority_label",
    "decision_score",
    "decision_rank_in_category",
    "decision_rank_overall_for_display",
    "section_rank",
    "highlight_tag",
    "trade_decision",
    "theme_group",
    "display_section",
    "risk_handling_bucket",
    "risk_handling_label",
    "momentum_risk_follow",
    "hard_exclusion_flag",
    "downgrade_flags",
    "risk_tags",
    "tdcc_status",
    "repeat_appear_label",
    "repeat_appear_summary",
    "overheat_status",
    "why_selected",
    "why_downgraded",
    "next_confirmation",
    "must_not_overstate",
    "close",
    "volume_ratio",
    "return_5d",
    "return_20d",
    "distance_to_ma20_pct",
    "tdcc_date",
    "warrant_flow_signal",
    "price_reaction_level",
    "already_priced_in",
    "catalyst_overheated",
    "primary_theme",
    "secondary_themes",
    "structural_theme_bucket",
    "theme_structural_status",
    "theme_mainstream_label",
    "industry_mainstream_label",
    "effective_mainstream_label",
    "mainstream_conflict_flag",
    "mainstream_conflict_note",
    "theme_taxonomy_source",
    "theme_taxonomy_confidence",
    "theme_taxonomy_note",
    "theme_final_status",
    "candidate_line_group",
]

BULLISH_WARRANT_SIGNALS = {"call_inflow", "call_strong_inflow", "call_put_bullish"}
NO_WARRANT_SIGNALS = {"", "no_signal", "none", "nan", "null"}
STALE_REPEAT_LABELS = {"stale_signal", "repeated_but_no_breakout", "反覆上榜未突破"}
REVENUE_LOW_RESPONSE_LABELS = {"revenue_breakout_low_response", "營收爆發低反應股"}
CONFIRMED_CATALYST_TAGS = {
    "eps_surprise",
    "margin_improvement",
    "profit_turnaround",
    "earnings_acceleration",
    "confirmed_event",
    "gross_margin",
    "new_order",
    "customer_win",
    "mass_production",
    "technology_validation",
}

CORE_AI_STRUCTURAL_THEME_BUCKETS = {
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
    "specialty_material_theme",
}

# Daily candidate rows already passed an upstream model condition.  Risk flags
# should change rank, section, and operating notes, not turn a selected model
# row into a contradictory "not buy" row.  True failed-breakout models should be
# emitted by their own risk/watch model instead of being vetoed here.
HARD_EXCLUSION_FLAGS: set[str] = set()

HIGH_MOMENTUM_RISK_FLAGS = {
    "continued_overheated",
    "already_priced_in",
    "catalyst_overheated",
    "price_reaction_priced_in",
    "price_reaction_overheated",
    "return_20d_gt_30",
    "distance_ma20_gt_20",
    "short_term_volume_overheat",
}


def truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y", "t"}


def num(row: pd.Series, names: list[str]) -> float:
    for name in names:
        if name in row.index:
            value = to_number(row.get(name, ""))
            if not math.isnan(value):
                return value
    return math.nan


def first_text(row: pd.Series, names: list[str]) -> str:
    for name in names:
        for candidate_name in (name, f"{name}_y", f"{name}_x"):
            if candidate_name not in row.index:
                continue
            text = safe_str(row.get(candidate_name, ""))
            if text:
                return text
    return ""


def apply_authoritative_taxonomy(candidates: pd.DataFrame) -> pd.DataFrame:
    taxonomy = read_csv(STOCK_THEME_TAXONOMY, dtype=str, keep_default_na=False)
    if candidates.empty or taxonomy.empty or "stock_id" not in candidates.columns or "stock_id" not in taxonomy.columns:
        return candidates

    out = candidates.copy()
    out["stock_id"] = out["stock_id"].map(normalize_code)
    drop_cols = [
        col
        for col in out.columns
        if col.startswith("taxonomy_") or col in {"theme_taxonomy_source", "theme_taxonomy_confidence", "theme_taxonomy_note"}
    ]
    if drop_cols:
        out = out.drop(columns=drop_cols)

    tax = taxonomy.copy()
    tax["stock_id"] = tax["stock_id"].map(normalize_code)
    tax_cols = [
        "stock_id",
        "primary_theme",
        "secondary_themes",
        "structural_theme_bucket",
        "theme_structural_status",
        "theme_mainstream_label",
        "industry_mainstream_label",
        "effective_mainstream_label",
        "mainstream_conflict_flag",
        "mainstream_conflict_note",
        "taxonomy_source",
        "confidence",
        "notes",
    ]
    tax = tax[[col for col in tax_cols if col in tax.columns]].rename(
        columns={
            "primary_theme": "taxonomy_primary_theme",
            "secondary_themes": "taxonomy_secondary_themes",
            "structural_theme_bucket": "taxonomy_structural_theme_bucket",
            "theme_structural_status": "taxonomy_theme_structural_status",
            "theme_mainstream_label": "taxonomy_theme_mainstream_label",
            "industry_mainstream_label": "taxonomy_industry_mainstream_label",
            "effective_mainstream_label": "taxonomy_effective_mainstream_label",
            "mainstream_conflict_flag": "taxonomy_mainstream_conflict_flag",
            "mainstream_conflict_note": "taxonomy_mainstream_conflict_note",
            "confidence": "taxonomy_confidence",
            "notes": "taxonomy_notes",
        }
    )
    out = out.merge(tax, on="stock_id", how="left")
    for target, source in [
        ("primary_theme", "taxonomy_primary_theme"),
        ("secondary_themes", "taxonomy_secondary_themes"),
        ("structural_theme_bucket", "taxonomy_structural_theme_bucket"),
        ("theme_structural_status", "taxonomy_theme_structural_status"),
        ("theme_mainstream_label", "taxonomy_theme_mainstream_label"),
        ("industry_mainstream_label", "taxonomy_industry_mainstream_label"),
        ("effective_mainstream_label", "taxonomy_effective_mainstream_label"),
        ("mainstream_conflict_flag", "taxonomy_mainstream_conflict_flag"),
        ("mainstream_conflict_note", "taxonomy_mainstream_conflict_note"),
    ]:
        if target not in out.columns:
            out[target] = ""
        if source in out.columns:
            values = out[source].fillna("").astype(str)
            out[target] = values.where(values.str.strip().ne(""), out[target].fillna("").astype(str))
    out["theme_taxonomy_source"] = out.get("taxonomy_source", "")
    out["theme_taxonomy_confidence"] = out.get("taxonomy_confidence", "")
    out["theme_taxonomy_note"] = out.get("taxonomy_notes", "")
    return out


def category_of(row: pd.Series) -> str:
    category = first_text(row, ["category", "breakout_type"]).lower()
    if category in CATEGORY_CN:
        return category
    breakout_type = first_text(row, ["breakout_type"]).lower()
    if breakout_type in CATEGORY_CN:
        return breakout_type
    return category or "unknown"


def stock_name_of(row: pd.Series) -> str:
    return first_text(row, ["stock_name", "name", "ticker_name"])


def map_pattern(row: pd.Series) -> tuple[str, str]:
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    category = category_of(row)
    volume_confirmed = truthy(row.get("volume_confirmed_breakout", ""))
    neckline_breakout = truthy(row.get("neckline_breakout_flag", ""))
    platform_breakout = truthy(row.get("platform_breakout_flag", ""))

    strict_like = category in {"true_breakout", "breakout"} or stage == "breakout_confirmed"
    if strict_like:
        return "嚴格突破", "breakout_confirmed / true_breakout"

    if platform_breakout or (neckline_breakout and volume_confirmed) or stage in {"platform_breakout", "neckline_breakout"}:
        return "區間內轉強 / 挑戰前高觀察", "neckline/platform breakout; upgrade only when risk checks pass"

    if stage in {"neckline_challenge"} or truthy(row.get("neckline_challenge_flag", "")):
        return "區間內轉強 / 挑戰前高觀察", "neckline_challenge"

    if stage in {
        "w_bottom_right_side",
        "platform_right_side",
        "early_entry_watch",
        "pullback_right_side",
        "pullback_entry_zone",
        "base_building",
    }:
        return "型態觀察", stage

    return CATEGORY_CN.get(category, safe_str(row.get("category_cn", "")) or category), stage or "no_pattern_stage"


def tdcc_status_of(row: pd.Series) -> str:
    text = " ".join(
        first_text(row, [col])
        for col in ["tdcc_judgement", "tdcc_accumulation_signal", "tdcc_judge", "tdcc_status"]
    ).lower()
    if "distribution" in text or "轉弱" in text or "減少" in text:
        return "distribution_warning"
    if "strong" in text or "強" in text:
        return "strong_accumulation"
    if "mild" in text or "溫和" in text or "增加" in text:
        return "mild_accumulation"
    if text.strip():
        return "neutral"
    return ""


def overheat_status_of(row: pd.Series) -> tuple[str, list[str]]:
    flags: list[str] = []
    ret5 = num(row, ["return_5d", "return_5d_pct"])
    ret20 = num(row, ["return_20d", "return_20d_pct"])
    dist_ma20 = num(row, ["distance_to_ma20_pct", "gap_ma20_pct"])
    volume_ratio = num(row, ["volume_ratio"])
    reaction = first_text(row, ["price_reaction_level"]).lower()

    if truthy(row.get("already_priced_in", "")):
        flags.append("already_priced_in")
    if truthy(row.get("catalyst_overheated", "")):
        flags.append("catalyst_overheated")
    if reaction in {"priced_in", "overheated"}:
        flags.append(f"price_reaction_{reaction}")
    if not math.isnan(ret20) and ret20 > 30:
        flags.append("return_20d_gt_30")
    if not math.isnan(dist_ma20) and dist_ma20 > 20:
        flags.append("distance_ma20_gt_20")
    if not math.isnan(ret5) and not math.isnan(volume_ratio) and ret5 > 15 and volume_ratio > 3:
        flags.append("short_term_volume_overheat")

    if flags:
        return "overheated_or_priced_in", flags
    return "not_overheated", []


def warrant_tag(row: pd.Series) -> str:
    signal = first_text(row, ["warrant_flow_signal", "warrant_status"]).lower()
    if signal in {"call_strong_inflow", "call_inflow", "call_put_bullish"}:
        return signal
    if signal in {"put_inflow", "warrant_overheat", "call_profit_exit_risk"}:
        return signal
    return signal or ""


def combined_text(row: pd.Series, names: list[str]) -> str:
    return " ".join(first_text(row, [name]) for name in names).lower()


def is_revenue_low_response(row: pd.Series, category: str) -> bool:
    category_cn = first_text(row, ["category_cn", "original_category_cn"])
    return category in REVENUE_LOW_RESPONSE_LABELS or category_cn in REVENUE_LOW_RESPONSE_LABELS


def is_no_warrant(row: pd.Series) -> bool:
    return warrant_tag(row) in NO_WARRANT_SIGNALS


def has_bullish_warrant(row: pd.Series) -> bool:
    return warrant_tag(row) in BULLISH_WARRANT_SIGNALS


def has_eps_or_margin_confirmation(row: pd.Series) -> bool:
    if any(
        truthy(row.get(name, ""))
        for name in [
            "eps_surprise_flag",
            "earnings_acceleration_flag",
            "margin_improvement_flag",
            "profit_turnaround_flag",
            "undervalued_after_eps_flag",
        ]
    ):
        return True
    tags = combined_text(
        row,
        [
            "fundamental_catalyst_tags",
            "event_catalyst_tags",
            "catalyst_tags",
            "theme_catalyst_tags",
            "catalyst_summary",
        ],
    )
    return any(tag in tags for tag in CONFIRMED_CATALYST_TAGS)


def has_revenue_good_eps_unconfirmed(row: pd.Series) -> bool:
    if truthy(row.get("revenue_good_eps_unconfirmed_flag", "")):
        return True
    tags = combined_text(row, ["fundamental_catalyst_tags", "catalyst_tags", "catalyst_summary"])
    return "revenue_good_eps_unconfirmed" in tags or "eps / 毛利率尚未" in tags


def has_price_breakout_confirmation(row: pd.Series, category: str, stage: str) -> bool:
    breakout_type = first_text(row, ["breakout_type"]).lower()
    if category in {"true_breakout", "breakout"} or breakout_type in {"true_breakout", "breakout", "strict_60d_volume_breakout"}:
        return True
    if truthy(row.get("strict_breakout", "")) or truthy(row.get("true_breakout", "")):
        return True
    if stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}:
        return True
    if truthy(row.get("platform_breakout_flag", "")) or truthy(row.get("neckline_breakout_flag", "")):
        return True
    for name in ["distance_to_previous_60d_high_pct", "distance_to_previous_high_pct", "distance_to_high_60_pct"]:
        value = num(row, [name])
        if not math.isnan(value) and value >= 0:
            return True
    return False


def has_volume_ma_confirmation(row: pd.Series) -> bool:
    volume_ratio = num(row, ["volume_ratio"])
    if math.isnan(volume_ratio) or volume_ratio < 1.5:
        return False
    for name in ["distance_to_ma20_pct", "gap_ma20_pct", "distance_to_ema23_pct", "gap_ema23_pct"]:
        value = num(row, [name])
        if not math.isnan(value) and value >= 0:
            return True
    return False


def has_attack_confirmation(row: pd.Series, category: str, stage: str) -> bool:
    return (
        has_price_breakout_confirmation(row, category, stage)
        or has_volume_ma_confirmation(row)
        or has_bullish_warrant(row)
        or has_eps_or_margin_confirmation(row)
    )


def structural_theme_bucket_of(row: pd.Series) -> str:
    return first_text(row, ["taxonomy_structural_theme_bucket", "structural_theme_bucket"]).lower()


def is_core_ai_theme(row: pd.Series) -> bool:
    bucket = structural_theme_bucket_of(row)
    mainstream_label = first_text(
        row,
        [
            "taxonomy_effective_mainstream_label",
            "effective_mainstream_label",
            "taxonomy_theme_mainstream_label",
            "theme_mainstream_label",
        ],
    ).lower()
    return bucket in CORE_AI_STRUCTURAL_THEME_BUCKETS or mainstream_label == "core_mainstream"


def is_non_mainstream_theme(row: pd.Series) -> bool:
    bucket = structural_theme_bucket_of(row)
    structural_status = first_text(row, ["taxonomy_theme_structural_status", "theme_structural_status"]).lower()
    mainstream_label = first_text(
        row,
        [
            "taxonomy_effective_mainstream_label",
            "effective_mainstream_label",
            "taxonomy_theme_mainstream_label",
            "theme_mainstream_label",
        ],
    ).lower()
    line_group = first_text(row, ["candidate_line_group"]).lower()
    return (
        structural_status in {"non_mainstream_theme", "theme_mapping_missing"}
        or mainstream_label.startswith("non_mainstream")
        or line_group in {"non_mainstream_flow_watch"}
    )


def theme_group_for(row: pd.Series) -> str:
    if is_core_ai_theme(row):
        return "core_mainstream"
    if is_non_mainstream_theme(row):
        return "non_mainstream"
    return "theme_unknown"


def risk_handling_for(
    downgrade_flags: list[str],
    attack_confirmed: bool,
    core_ai_theme: bool,
    non_mainstream_theme: bool,
) -> tuple[str, str, bool, bool]:
    flags = set(downgrade_flags)
    hard_exclusion = bool(flags.intersection(HARD_EXCLUSION_FLAGS))
    if hard_exclusion:
        return "hard_exclusion", "模型外排除", False, True


    high_momentum_flags = bool(flags.intersection(HIGH_MOMENTUM_RISK_FLAGS))
    tdcc_distribution_with_attack = "tdcc_distribution_warning" in flags and attack_confirmed
    if high_momentum_flags or tdcc_distribution_with_attack:
        return "high_momentum_risk_follow", "高動能風險追蹤", True, False

    if flags:
        return "risk_watch", "降級觀察", False, False

    return "normal", "一般候選", False, False


def trade_decision_for(priority: str, risk_handling_bucket: str, momentum_risk_follow: bool, hard_exclusion: bool) -> str:
    if hard_exclusion or priority == "D_risk_downgrade":
        return "ranked_risk_candidate"
    if momentum_risk_follow:
        return "short_term_risk_follow"
    if priority == "A_priority_watch":
        return "selected_priority"
    if priority == "B_confirm_needed":
        return "selected_confirm"
    return "selected_watch"


def display_section_for(theme_group: str, trade_decision: str) -> str:
    if trade_decision == "ranked_risk_candidate":
        return f"{theme_group}_risk_ranked"
    if trade_decision == "short_term_risk_follow":
        return f"{theme_group}_short_term_risk_follow"
    if trade_decision == "selected_priority":
        return f"{theme_group}_selected_priority"
    if trade_decision == "selected_confirm":
        return f"{theme_group}_selected_confirm"
    return f"{theme_group}_selected_watch"


def cap_priority(priority: str, max_priority: str) -> str:
    if PRIORITY_SORT.get(priority, 9) < PRIORITY_SORT.get(max_priority, 9):
        return max_priority
    return priority


def downgrade_original_priority_once(row: pd.Series, priority: str, default_cap: str = "B_confirm_needed") -> str:
    original = first_text(row, ["revaluation_priority", "priority"]).lower()
    if "a_" in original or "優先" in original:
        return "D_risk_downgrade" if priority == "D_risk_downgrade" else "B_confirm_needed"
    if "b_" in original or "可觀察" in original or "可等" in original:
        return "D_risk_downgrade" if priority == "D_risk_downgrade" else "C_watch_only"
    return cap_priority(priority, default_cap)


def build_reasons(row: pd.Series, pattern_category: str, pattern_route: str, tdcc_status: str) -> list[str]:
    reasons: list[str] = []
    category = category_of(row)
    score = num(row, ["score", "pattern_score"])
    volume_ratio = num(row, ["volume_ratio"])
    ret20 = num(row, ["return_20d", "return_20d_pct"])
    dist_high = num(row, ["distance_to_previous_60d_high_pct", "distance_to_previous_high_pct", "distance_to_high_60_pct"])

    if category in CATEGORY_CN:
        reasons.append(CATEGORY_CN[category])
    if pattern_route and pattern_route != "no_pattern_stage":
        reasons.append(f"型態={pattern_route}")
    if not math.isnan(score):
        reasons.append(f"分類分數={score:.0f}")
    if not math.isnan(volume_ratio):
        reasons.append(f"量比={volume_ratio:.2f}")
    if not math.isnan(dist_high):
        reasons.append(f"距前高={dist_high:.2f}%")
    if not math.isnan(ret20):
        reasons.append(f"20日漲幅={ret20:.2f}%")
    if tdcc_status:
        reasons.append(f"TDCC={tdcc_status}")
    wt = warrant_tag(row)
    if wt:
        reasons.append(f"權證={wt}")
    return reasons[:8]


def next_confirmation_for(
    row: pd.Series,
    pattern_category: str,
    priority: str,
    downgrade_flags: list[str],
    risk_handling_bucket: str = "",
) -> str:
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    if risk_handling_bucket == "hard_exclusion":
        return "??????????TDCC ?????????????????"
    if risk_handling_bucket == "high_momentum_risk_follow":
        return "??????????????????????????????????? D+5/D+10 ???"
    if "tdcc_distribution_warning" in downgrade_flags:
        return "先看 TDCC 是否停止轉弱，再看價格能否守住 MA20/EMA23 與突破區。"
    if "revenue_no_warrant_stale_no_breakout" in downgrade_flags:
        return "等待放量突破平台 / 前高，以及權證或法人資金轉為明確偏多。"
    if "revenue_eps_unconfirmed_no_attack" in downgrade_flags:
        return "等待 EPS / 毛利率或正式催化確認，並觀察是否放量突破平台 / 前高。"
    if "missing_attack_confirmation" in downgrade_flags:
        return "等待嚴格突破、放量站上重要均線、權證資金偏多，或財報品質確認。"
    if "stale_signal" in downgrade_flags:
        return "等待量價重新轉強、相對強弱轉正，否則只保留觀察。"
    if "overheated_or_priced_in" in downgrade_flags:
        return "避免追高，等待回測支撐後量縮守穩。"
    if stage in {"breakout_confirmed", "platform_breakout", "neckline_breakout"}:
        return "確認突破後不跌回平台/頸線，量能不要爆量失控或長上影。"
    if stage in {"neckline_challenge", "platform_right_side", "w_bottom_right_side"}:
        return "確認放量站上頸線/平台壓力，且收盤靠近高點。"
    if priority == "A_priority_watch":
        return "追蹤隔日是否延續量價與族群同步，不用再由 ChatGPT 重新排序。"
    return "等待量價、TDCC、相對強弱至少一項轉強。"


def evaluate_row(row: pd.Series) -> dict[str, Any]:
    category = category_of(row)
    pattern_category, pattern_route = map_pattern(row)
    tdcc_status = tdcc_status_of(row)
    overheat_status, overheat_flags = overheat_status_of(row)
    repeat_label = first_text(row, ["repeat_appear_label"])
    score = num(row, ["score", "pattern_score"])
    volume_ratio = num(row, ["volume_ratio"])
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    stale_repeat = repeat_label in STALE_REPEAT_LABELS
    no_warrant = is_no_warrant(row)
    price_breakout_confirmed = has_price_breakout_confirmation(row, category, stage)
    attack_confirmed = has_attack_confirmation(row, category, stage)
    core_ai_theme = is_core_ai_theme(row)
    non_mainstream_theme = is_non_mainstream_theme(row)
    revenue_low_response = is_revenue_low_response(row, category)
    revenue_eps_unconfirmed = has_revenue_good_eps_unconfirmed(row)
    eps_or_margin_confirmed = has_eps_or_margin_confirmation(row)

    decision_score = 50
    decision_score += {
        "true_breakout": 26,
        "breakout": 26,
        "range_rebound": 18,
        "near_resistance": 16,
        "revenue_breakout_low_response": 20,
        "revenue_pullback": 14,
        "pullback_rebound": 13,
        "pattern": 8,
    }.get(category, 5)

    decision_score += {
        "breakout_confirmed": 12,
        "neckline_breakout": 8,
        "platform_breakout": 8,
        "neckline_challenge": 4,
        "platform_right_side": 2,
        "w_bottom_right_side": 2,
        "early_entry_watch": 1,
        "pullback_entry_zone": -3,
        "failed_breakout": -15,
    }.get(stage, 0)

    if not math.isnan(score):
        decision_score += max(-5, min(8, (score - 60) / 5))
    if not math.isnan(volume_ratio) and volume_ratio >= 1.5:
        decision_score += 3
    if tdcc_status == "strong_accumulation":
        decision_score += 8
    elif tdcc_status == "mild_accumulation":
        decision_score += 4

    downgrade_flags: list[str] = []
    risk_tags: list[str] = []
    if tdcc_status == "distribution_warning":
        downgrade_flags.append("tdcc_distribution_warning")
        risk_tags.append("TDCC 大戶轉弱")
        decision_score -= 20
    if repeat_label == "stale_signal":
        downgrade_flags.append("stale_signal")
        risk_tags.append("反覆上榜鈍化")
        decision_score -= 4
    elif repeat_label == "continued_overheated":
        downgrade_flags.append("continued_overheated")
        risk_tags.append("連續上榜但過熱")
        decision_score -= 18
    elif repeat_label == "repeated_but_no_breakout":
        downgrade_flags.append("repeated_but_no_breakout")
        risk_tags.append("反覆上榜未突破")
        decision_score -= 4
    elif repeat_label == "continued_2_3d":
        decision_score += 4

    if stale_repeat and not price_breakout_confirmed and no_warrant:
        downgrade_flags.append("stale_no_warrant_no_breakout")
        risk_tags.append("反覆上榜但尚未突破，且權證資金未確認，訊號可能鈍化。")
        decision_score -= 3

    if revenue_low_response and revenue_eps_unconfirmed and not eps_or_margin_confirmed and not attack_confirmed:
        downgrade_flags.append("revenue_eps_unconfirmed_no_attack")
        risk_tags.append("營收成長尚未由 EPS / 毛利或正式催化確認，需等待獲利品質或量價突破。")
        decision_score -= 3

    if revenue_low_response and no_warrant and stale_repeat and not price_breakout_confirmed:
        downgrade_flags.append("revenue_no_warrant_stale_no_breakout")
        decision_score -= 2

    if overheat_flags:
        downgrade_flags.extend(overheat_flags)
        risk_tags.append("短線過熱或利多已反應")
        decision_score -= 16
    if truthy(row.get("false_breakout_risk", "")):
        downgrade_flags.append("false_breakout_risk")
        risk_tags.append("假突破風險")
        decision_score -= 12
    if warrant_tag(row) in {"put_inflow", "warrant_overheat", "call_profit_exit_risk"}:
        risk_tags.append("權證風險訊號")
        decision_score -= 4

    decision_score = max(0, min(100, round(decision_score, 1)))

    risk_handling_bucket, risk_handling_label, momentum_risk_follow, hard_exclusion_flag = risk_handling_for(
        downgrade_flags=downgrade_flags,
        attack_confirmed=attack_confirmed,
        core_ai_theme=core_ai_theme,
        non_mainstream_theme=non_mainstream_theme,
    )
    if hard_exclusion_flag:
        priority = "D_risk_downgrade" if decision_score < 62 else "C_watch_only"
    elif risk_handling_bucket == "high_momentum_risk_follow":
        priority = "C_watch_only" if decision_score < 76 else "B_confirm_needed"
    elif decision_score >= 82:
        priority = "A_priority_watch"
    elif decision_score >= 68:
        priority = "B_confirm_needed"
    else:
        priority = "C_watch_only"

    if stale_repeat and not price_breakout_confirmed and no_warrant:
        priority = downgrade_original_priority_once(row, priority, default_cap="B_confirm_needed")
    if revenue_low_response and revenue_eps_unconfirmed and not eps_or_margin_confirmed and not attack_confirmed:
        priority = cap_priority(priority, "B_confirm_needed")
    if revenue_low_response and no_warrant and stale_repeat and not price_breakout_confirmed:
        priority = cap_priority(priority, "B_confirm_needed")
    if priority == "A_priority_watch" and not attack_confirmed:
        downgrade_flags.append("missing_attack_confirmation")
        risk_tags.append("缺乏突破 / 量價 / 權證 / 財報品質攻擊確認，最高只能可等確認。")
        priority = "B_confirm_needed"
        decision_score = min(decision_score, 81.0)

    theme_group = theme_group_for(row)
    trade_decision = trade_decision_for(priority, risk_handling_bucket, momentum_risk_follow, hard_exclusion_flag)
    display_section = display_section_for(theme_group, trade_decision)

    priority_label = {
        "A_priority_watch": "最優先追蹤",
        "B_confirm_needed": "可等確認",
        "C_watch_only": "僅觀察",
        "D_risk_downgrade": "暫避降級 / 只保留觀察",
    }[priority]

    if hard_exclusion_flag:
        highlight = "hard_exclusion"
    elif momentum_risk_follow:
        highlight = "high_momentum_risk_follow"
    elif priority == "A_priority_watch":
        highlight = "priority_candidate"
    elif stage in {"breakout_confirmed", "neckline_breakout", "platform_breakout"}:
        highlight = "breakout_but_check_risk"
    elif stage in {"platform_right_side", "w_bottom_right_side", "neckline_challenge"}:
        highlight = "pre_breakout_watch"
    elif downgrade_flags:
        highlight = "risk_downgrade"
    else:
        highlight = "watch"

    why_selected = "；".join(build_reasons(row, pattern_category, pattern_route, tdcc_status))
    why_downgraded = "；".join(risk_tags) if risk_tags else ""
    next_confirmation = next_confirmation_for(row, pattern_category, priority, downgrade_flags, risk_handling_bucket)

    return {
        "pattern_mapped_category": pattern_category,
        "pattern_route": pattern_route,
        "decision_priority": priority,
        "decision_priority_label": priority_label,
        "decision_score": decision_score,
        "highlight_tag": highlight,
        "trade_decision": trade_decision,
        "theme_group": theme_group,
        "display_section": display_section,
        "risk_handling_bucket": risk_handling_bucket,
        "risk_handling_label": risk_handling_label,
        "momentum_risk_follow": "True" if momentum_risk_follow else "False",
        "hard_exclusion_flag": "True" if hard_exclusion_flag else "False",
        "downgrade_flags": "|".join(dict.fromkeys(downgrade_flags)),
        "risk_tags": "|".join(dict.fromkeys(risk_tags)),
        "tdcc_status": tdcc_status,
        "repeat_appear_summary": repeat_label,
        "overheat_status": overheat_status,
        "why_selected": why_selected,
        "why_downgraded": why_downgraded,
        "next_confirmation": next_confirmation,
        "must_not_overstate": "True" if priority in {"C_watch_only", "D_risk_downgrade"} or bool(downgrade_flags) or momentum_risk_follow or hard_exclusion_flag else "False",
    }


def build_decision(candidates: pd.DataFrame, main_date: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for idx, row in candidates.iterrows():
        stock_id = normalize_code(first_text(row, ["stock_id", "ticker"]))
        if not stock_id:
            continue
        category = category_of(row)
        date = normalize_date(row.get("signal_date", "")) or main_date
        base = {
            "source_row_index": idx,
            "signal_date": date,
            "stock_id": stock_id,
            "stock_name": stock_name_of(row),
            "original_category": category,
            "original_category_cn": CATEGORY_CN.get(category, safe_str(row.get("category_cn", ""))),
            "breakout_type": first_text(row, ["breakout_type"]),
            "pattern_stage": first_text(row, ["pattern_stage", "pattern"]),
            "repeat_appear_label": first_text(row, ["repeat_appear_label"]),
            "close": num(row, ["close"]),
            "volume_ratio": num(row, ["volume_ratio"]),
            "return_5d": num(row, ["return_5d", "return_5d_pct"]),
            "return_20d": num(row, ["return_20d", "return_20d_pct"]),
            "distance_to_ma20_pct": num(row, ["distance_to_ma20_pct", "gap_ma20_pct"]),
            "tdcc_date": normalize_date(row.get("tdcc_date", "")),
            "warrant_flow_signal": first_text(row, ["warrant_flow_signal", "warrant_status"]),
            "price_reaction_level": first_text(row, ["price_reaction_level"]),
            "already_priced_in": "True" if truthy(row.get("already_priced_in", "")) else "False",
            "catalyst_overheated": "True" if truthy(row.get("catalyst_overheated", "")) else "False",
            "primary_theme": first_text(row, ["taxonomy_primary_theme", "primary_theme"]),
            "secondary_themes": first_text(row, ["taxonomy_secondary_themes", "secondary_themes"]),
            "structural_theme_bucket": first_text(row, ["taxonomy_structural_theme_bucket", "structural_theme_bucket"]),
            "theme_structural_status": first_text(row, ["taxonomy_theme_structural_status", "theme_structural_status"]),
            "theme_mainstream_label": first_text(row, ["taxonomy_theme_mainstream_label", "theme_mainstream_label"]),
            "industry_mainstream_label": first_text(row, ["taxonomy_industry_mainstream_label", "industry_mainstream_label"]),
            "effective_mainstream_label": first_text(row, ["taxonomy_effective_mainstream_label", "effective_mainstream_label"]),
            "mainstream_conflict_flag": first_text(row, ["taxonomy_mainstream_conflict_flag", "mainstream_conflict_flag"]),
            "mainstream_conflict_note": first_text(row, ["taxonomy_mainstream_conflict_note", "mainstream_conflict_note"]),
            "theme_taxonomy_source": first_text(row, ["taxonomy_source", "theme_taxonomy_source"]),
            "theme_taxonomy_confidence": first_text(row, ["taxonomy_confidence", "theme_taxonomy_confidence"]),
            "theme_taxonomy_note": first_text(row, ["taxonomy_notes", "theme_taxonomy_note"]),
            "theme_final_status": first_text(row, ["theme_final_status"]),
            "candidate_line_group": first_text(row, ["candidate_line_group"]),
            "_source_index": idx,
            "_category_order": CATEGORY_ORDER.get(category, 999),
        }
        base.update(evaluate_row(row))
        rows.append(base)

    decision = pd.DataFrame(rows)
    if decision.empty:
        return pd.DataFrame(columns=DECISION_COLUMNS)

    decision["_priority_order"] = decision["decision_priority"].map(PRIORITY_SORT).fillna(9)
    decision = decision.sort_values(
        ["_category_order", "_priority_order", "decision_score", "stock_id", "_source_index"],
        ascending=[True, True, False, True, True],
    ).reset_index(drop=True)

    decision["decision_rank_overall_for_display"] = range(1, len(decision) + 1)
    decision["decision_rank_in_category"] = (
        decision.groupby("original_category", dropna=False).cumcount() + 1
    )
    section_sorted = decision.sort_values(
        ["display_section", "_priority_order", "decision_score", "stock_id", "_source_index"],
        ascending=[True, True, False, True, True],
    )
    decision["section_rank"] = 0
    decision.loc[section_sorted.index, "section_rank"] = (
        section_sorted.groupby("display_section", dropna=False).cumcount() + 1
    ).astype(int)

    for col in DECISION_COLUMNS:
        if col not in decision.columns:
            decision[col] = ""
    return decision[DECISION_COLUMNS]


def rewrite_all_candidates(candidates: pd.DataFrame, decision: pd.DataFrame) -> pd.DataFrame:
    out = candidates.copy()
    if out.empty or decision.empty:
        return out

    out["_source_index"] = range(len(out))
    decision_for_merge = decision.copy()
    if "source_row_index" not in decision_for_merge.columns:
        raise RuntimeError("decision output missing source_row_index; cannot safely merge back into all_candidates")
    decision_for_merge["_source_index"] = pd.to_numeric(decision_for_merge["source_row_index"], errors="coerce").astype("Int64")
    merge_cols = [
        "_source_index",
        "source_row_index",
        "pattern_mapped_category",
        "pattern_route",
        "decision_priority",
        "decision_priority_label",
        "decision_score",
        "decision_rank_in_category",
        "decision_rank_overall_for_display",
        "section_rank",
        "highlight_tag",
        "trade_decision",
        "theme_group",
        "display_section",
        "risk_handling_bucket",
        "risk_handling_label",
        "momentum_risk_follow",
        "hard_exclusion_flag",
        "downgrade_flags",
        "risk_tags",
        "tdcc_status",
        "repeat_appear_summary",
        "overheat_status",
        "why_selected",
        "why_downgraded",
        "next_confirmation",
        "must_not_overstate",
        "primary_theme",
        "secondary_themes",
        "structural_theme_bucket",
        "theme_structural_status",
        "theme_mainstream_label",
        "industry_mainstream_label",
        "effective_mainstream_label",
        "mainstream_conflict_flag",
        "mainstream_conflict_note",
        "theme_taxonomy_source",
        "theme_taxonomy_confidence",
        "theme_taxonomy_note",
    ]
    for col in merge_cols:
        if col != "_source_index" and col in out.columns:
            out = out.drop(columns=[col])
    out = out.merge(decision_for_merge[merge_cols], on="_source_index", how="left").drop(columns=["_source_index"])
    out = out.fillna("")
    write_csv(out, ALL_CANDIDATES)
    try:
        with pd.ExcelWriter(ALL_CANDIDATES_XLSX, engine="openpyxl") as writer:
            out.to_excel(writer, sheet_name="all_candidates", index=False)
    except Exception as exc:
        print(f"WARNING: failed to write {ALL_CANDIDATES_XLSX}: {exc}")
    try:
        ALL_CANDIDATES_MD.write_text(out.head(300).to_markdown(index=False) + "\n", encoding="utf-8")
    except Exception:
        ALL_CANDIDATES_MD.write_text(out.head(300).to_csv(index=False), encoding="utf-8")
    return out


def render_table(df: pd.DataFrame, cols: list[str], limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    use_cols = [col for col in cols if col in df.columns]
    view = df[use_cols].head(limit).copy()
    return view.to_markdown(index=False)


def regression_2484_summary() -> list[str]:
    lines: list[str] = []
    if not REGRESSION_2484_CSV.exists():
        return ["- 2484 regression file missing."]
    df = read_csv(REGRESSION_2484_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        return ["- 2484 regression file empty."]
    cols = [
        "case_date",
        "breakout_type",
        "score",
        "pattern_stage",
        "neckline_breakout_flag",
        "platform_breakout_flag",
        "volume_confirmed_breakout",
    ]
    lines.append(df[[col for col in cols if col in df.columns]].to_markdown(index=False))
    return lines


def regression_8069_summary() -> list[str]:
    lines: list[str] = []
    if not REGRESSION_8069_CSV.exists():
        return ["- 8069 regression file missing."]
    df = read_csv(REGRESSION_8069_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        return ["- 8069 regression file empty."]
    cols = [
        "case_date",
        "breakout_type",
        "score",
        "pattern_stage",
        "w_bottom_flag",
        "early_entry_watch_flag",
        "neckline_challenge_flag",
        "neckline_breakout_flag",
        "platform_breakout_flag",
        "volume_confirmed_breakout",
    ]
    lines.append(df[[col for col in cols if col in df.columns]].to_markdown(index=False))
    return lines


def write_markdown(decision: pd.DataFrame, main_date: str) -> None:
    lines = [
        "# Daily Candidate Decision Layer",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        f"- source: `{ALL_CANDIDATES.as_posix()}`",
        "- purpose: deterministic candidate classification, downgrade, sorting, and ChatGPT guidance.",
        "",
        "## How ChatGPT Should Use This",
        "",
        "- Use this decision layer before relying on memory or free-form re-ranking.",
        "- Do not mix category scores into one investment ranking; `decision_rank_overall_for_display` is only a display order. Use `display_section` and `section_rank` to compare mainstream and non-mainstream rows separately.",
        "- If `decision_priority` is `D_risk_downgrade`, explain the risk and rank it lower inside its own section.",
        "- If TDCC is `distribution_warning`, repeat label is stale/overheated, or overheat flags are present, treat them as score/rank penalties and operating risks, not as a second buy/not-buy veto.",
        "",
        "## Pattern Mapping Rules",
        "",
        "| Pattern signal | Program category used in analysis |",
        "|---|---|",
        "| w_bottom_right_side / platform_right_side | 型態觀察 |",
        "| neckline_challenge / neckline_breakout | 區間內轉強 / 挑戰前高觀察 |",
        "| platform_breakout or neckline_breakout + volume_confirmed_breakout | 嚴格突破 or 區間轉強升級, only if risk checks pass |",
        "",
        "## Priority Counts",
        "",
    ]
    if decision.empty:
        lines.append("_No decision rows._")
    else:
        counts = (
            decision.groupby(["decision_priority", "decision_priority_label"], dropna=False)
            .size()
            .reset_index(name="count")
            .sort_values("decision_priority")
        )
        lines.append(counts.to_markdown(index=False))

    lines.extend(["", "## 2484 Regression Guardrail", ""])
    lines.extend(regression_2484_summary())

    lines.extend(["", "## 8069 Regression Guardrail", ""])
    lines.extend(regression_8069_summary())

    display_cols = [
        "decision_rank_in_category",
        "stock_id",
        "stock_name",
        "original_category_cn",
        "pattern_stage",
        "pattern_mapped_category",
        "decision_priority_label",
        "decision_score",
        "tdcc_status",
        "repeat_appear_label",
        "risk_handling_bucket",
        "downgrade_flags",
        "next_confirmation",
    ]

    for category in [
        "true_breakout",
        "range_rebound",
        "revenue_breakout_low_response",
        "revenue_pullback",
        "pullback_rebound",
        "pattern",
    ]:
        part = decision[decision["original_category"].eq(category)].copy()
        lines.extend(["", f"## {CATEGORY_CN.get(category, category)}", ""])
        lines.append(render_table(part, display_cols, limit=25))

    risk = decision[decision["decision_priority"].isin(["C_watch_only", "D_risk_downgrade"])].copy()
    risk = risk[risk["downgrade_flags"].astype(str).ne("")]
    lines.extend(["", "## Risk Downgrade Watchlist", ""])
    lines.append(render_table(risk, display_cols, limit=40))

    momentum_risk = decision[decision["risk_handling_bucket"].eq("high_momentum_risk_follow")].copy()
    lines.extend(["", "## High Momentum Risk Follow Watchlist", ""])
    lines.append("These rows are selected signals with high momentum risk. Keep them visible, rank them conservatively, and verify the short-term continuation with D+5/D+10 evidence.")
    lines.append("")
    lines.append(render_table(momentum_risk, display_cols, limit=40))
    lines.append("")
    DECISION_MD.write_text("\n".join(lines), encoding="utf-8")


def write_packet(decision: pd.DataFrame, main_date: str) -> None:
    lines = [
        "# DAILY CANDIDATE DECISION CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- signal_date: {main_date}",
        f"- source_file: {ALL_CANDIDATES.as_posix()}",
        f"- decision_csv: {DECISION_CSV.as_posix()}",
        "",
        "## Interpretation Rules",
        "- This packet is the program-side decision layer. Prefer it over conversation memory.",
        "- Category scores remain category-local; do not compare them as one universal model score.",
        "- `decision_priority` is a reporting and tracking priority, not a buy/sell instruction.",
        "- Risk handling is split into hard_exclusion, high_momentum_risk_follow, risk_watch, and normal. Mainstream/non-mainstream is a display section, not a score cap.",
        "- TDCC distribution, continued overheat, and short-term overheat are rank and risk modifiers. If momentum remains strong, keep it in high_momentum_risk_follow and verify with D+5/D+10 evidence.",
        "- Mainstream and non-mainstream candidates must be shown in separate sections and compared within their own section_rank; do not use theme group alone to downgrade score or veto selection.",
        "- For 2484 regression: 20260520-20260521 platform_right_side, 20260522 neckline_breakout, 20260525 breakout_confirmed.",
        "- For 8069 regression: 20260507 early right-side watch, 20260508 neckline_challenge, 20260512 strict volume-confirmed breakout.",
        "",
        "## Priority Summary",
        "",
    ]
    if decision.empty:
        lines.append("_No rows._")
    else:
        counts = (
            decision.groupby(["decision_priority", "decision_priority_label"], dropna=False)
            .size()
            .reset_index(name="count")
            .sort_values("decision_priority")
        )
        lines.append(counts.to_markdown(index=False))

    top_cols = [
        "stock_id",
        "stock_name",
        "original_category_cn",
        "pattern_stage",
        "decision_priority_label",
        "decision_score",
        "tdcc_status",
        "repeat_appear_label",
        "risk_handling_bucket",
        "downgrade_flags",
        "next_confirmation",
    ]
    for priority, title in [
        ("A_priority_watch", "A Priority Watch"),
        ("B_confirm_needed", "B Confirm Needed"),
        ("C_watch_only", "C Watch Only"),
        ("D_risk_downgrade", "D Risk Downgrade"),
    ]:
        part = decision[decision["decision_priority"].eq(priority)].copy()
        lines.extend(["", f"## {title}", ""])
        lines.append(render_table(part, top_cols, limit=35))

    momentum_risk = decision[decision["risk_handling_bucket"].eq("high_momentum_risk_follow")].copy()
    lines.extend(["", "## High Momentum Risk Follow", ""])
    lines.append("Not a front-line buy list. Keep these rows visible for short-term D+5/D+10 validation instead of deleting them as generic overheat risk.")
    lines.append("")
    lines.append(render_table(momentum_risk, top_cols, limit=40))

    case_2484 = decision[decision["stock_id"].eq("2484")].copy()
    lines.extend(["", "## 2484 Latest Decision", ""])
    lines.append(render_table(case_2484, top_cols, limit=10))

    lines.extend(["", "## 2484 Regression Replay", ""])
    lines.extend(regression_2484_summary())

    lines.extend(["", "## 8069 Regression Replay", ""])
    lines.extend(regression_8069_summary())
    lines.append("")
    DECISION_PACKET.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    preferred_date = main_price_date_from_freshness()
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if candidates.empty:
        raise RuntimeError(f"missing or empty {ALL_CANDIDATES}")
    candidates = apply_authoritative_taxonomy(candidates)

    main_date, notes = resolve_candidate_signal_date(candidates, preferred_date)
    for note in notes:
        print(f"WARNING: {note}")

    decision = build_decision(candidates, main_date)
    write_csv(decision, DECISION_CSV)
    write_markdown(decision, main_date)
    write_packet(decision, main_date)
    enriched = rewrite_all_candidates(candidates, decision)

    print(f"Saved: {DECISION_CSV}, rows={len(decision)}")
    print(f"Saved: {DECISION_MD}")
    print(f"Saved: {DECISION_PACKET}")
    print(f"Updated: {ALL_CANDIDATES}, rows={len(enriched)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
