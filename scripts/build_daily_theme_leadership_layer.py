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
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
ALL_CANDIDATES_MD = LATEST_DIR / "all_candidates_latest.md"

THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
THEME_LEADERSHIP_MD = LATEST_DIR / "daily_theme_leadership_latest.md"
TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
TWO_LINE_VIEW_MD = LATEST_DIR / "daily_candidate_two_line_view_latest.md"


BULLISH_WARRANT_SIGNALS = {"call_inflow", "call_strong_inflow", "call_put_bullish", "low_float_call_spike"}
BEARISH_WARRANT_SIGNALS = {"put_inflow", "warrant_overheat", "call_profit_exit_risk", "put_call_bearish"}
MAINSTREAM_STATUSES = {"mainstream_leader", "mainstream_follow_through", "emerging_theme"}
RISK_STATUSES = {"weak_theme", "mainstream_overheated"}
GENERIC_THEME_VALUES = {"", "other", "unknown", "nan", "none", "mainstream_growth", "unclassified"}

# Structural theme buckets answer a different question from theme_final_status.
# theme_final_status = today's breadth/flow state.
# theme_structural_status = whether the industry belongs to the user's core mainstream universe.
CORE_MAINSTREAM_THEME_KEYWORDS = {
    "半導體",
    "電子零組件",
    "被動元件",
    "消費性電子",
    "電腦及週邊",
    "電腦週邊",
    "PC",
    "NB",
    "AI_PC",
    "AI PC",
    "AI",
    "伺服器",
    "PCB",
    "CCL",
    "ABF",
    "玻纖布",
    "低軌",
    "衛星",
    "網通",
    "通信網路",
    "光通訊",
    "光電",
    "CPO",
    "交換器",
    "散熱",
    "液冷",
    "連接器",
    "電源",
    "BBU",
    "重電",
    "電網",
    "記憶體",
    "儲存",
    "矽智財",
    "ASIC",
    "CoWoS",
    "先進封裝",
    "半導體設備",
    "機器人",
    "自動化",
    "軍工",
    "無人機",
    "車用電子",
    "特化",
    "特化材料",
}
NON_MAINSTREAM_THEME_KEYWORDS = {
    "金融",
    "保險",
    "金融保險",
    "紡織",
    "成衣",
    "鋼鐵",
    "建材",
    "營造",
    "建材營造",
    "營建",
    "航運",
    "化學",
    "塑膠",
    "水泥",
    "玻璃陶瓷",
    "橡膠",
    "食品",
    "觀光",
    "汽車",
    "造紙",
    "貿易百貨",
    "生技醫療",
    "油電燃氣",
    "存託憑證",
    "運動休閒",
    "綠能環保",
}

THEME_COLUMNS = [
    "taxonomy_primary_theme",
    "primary_theme",
    "effective_primary_theme",
    "theme_group",
    "sub_theme",
    "sector",
    "concept",
    "細分族群",
    "industry",
    "market",
]
THEME_COLUMNS_TO_MERGE = [
    "theme_name",
    "theme_candidate_count",
    "theme_A_candidate_count",
    "theme_B_candidate_count",
    "theme_strict_breakout_count",
    "theme_true_breakout_count",
    "theme_volume_breakout_count",
    "theme_near_high_count",
    "theme_revenue_growth_count",
    "theme_revenue_low_response_count",
    "theme_tdcc_strong_count",
    "theme_tdcc_mild_count",
    "theme_tdcc_distribution_warning_count",
    "theme_warrant_bullish_count",
    "theme_warrant_bearish_count",
    "theme_overheated_count",
    "theme_avg_volume_ratio",
    "theme_avg_relative_strength_vs_benchmark",
    "theme_leader_stock_id",
    "theme_leader_stock_name",
    "theme_leader_confirmed",
    "theme_breadth_score",
    "theme_strength_score",
    "theme_risk_score",
    "theme_final_status",
    "theme_market_flow_status",
    "theme_structural_status",
    "theme_mainstream_label",
    "candidate_source_type",
    "candidate_line",
    "candidate_line_group",
    "two_line_overlap_flag",
    "theme_leadership_note",
]


def first_text(row: pd.Series, names: list[str]) -> str:
    for name in names:
        if name in row.index:
            text = safe_str(row.get(name, ""))
            if text:
                return text
    return ""


def truthy(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y", "t"}


def num(row: pd.Series, names: list[str], default: float = math.nan) -> float:
    for name in names:
        if name in row.index:
            value = to_number(row.get(name, ""), default=math.nan)
            if not math.isnan(value):
                return value
    return default


def lower_text(row: pd.Series, names: list[str]) -> str:
    return " ".join(first_text(row, [name]).lower() for name in names if name in row.index)


def priority_order(value: Any) -> int:
    text = safe_str(value)
    return {"A_priority_watch": 1, "B_confirm_needed": 2, "C_watch_only": 3, "D_risk_downgrade": 4}.get(text, 9)


def theme_name_of(row: pd.Series) -> str:
    for col in THEME_COLUMNS:
        value = safe_str(row.get(col, ""))
        if value and value.lower() not in GENERIC_THEME_VALUES:
            return value
    return "other"


def theme_structural_status(theme_name: Any) -> str:
    text = safe_str(theme_name)
    if not text or text.lower() in GENERIC_THEME_VALUES:
        return "unknown_theme"
    if any(token.lower() in text.lower() for token in CORE_MAINSTREAM_THEME_KEYWORDS):
        return "core_mainstream_theme"
    if any(token.lower() in text.lower() for token in NON_MAINSTREAM_THEME_KEYWORDS):
        return "non_mainstream_theme"
    return "non_mainstream_theme"


def theme_structural_status_from_frame(theme_name: Any, frame: pd.DataFrame) -> str:
    labels = set(frame.get("taxonomy_effective_mainstream_label", pd.Series(dtype=str)).fillna("").astype(str))
    labels.update(frame.get("effective_mainstream_label", pd.Series(dtype=str)).fillna("").astype(str))
    labels.update(frame.get("taxonomy_theme_mainstream_label", pd.Series(dtype=str)).fillna("").astype(str))
    labels.update(frame.get("theme_mainstream_label", pd.Series(dtype=str)).fillna("").astype(str))
    statuses = set(frame.get("taxonomy_theme_structural_status", pd.Series(dtype=str)).fillna("").astype(str))
    statuses.update(frame.get("theme_structural_status", pd.Series(dtype=str)).fillna("").astype(str))
    buckets = set(frame.get("taxonomy_structural_theme_bucket", pd.Series(dtype=str)).fillna("").astype(str))
    buckets.update(frame.get("structural_theme_bucket", pd.Series(dtype=str)).fillna("").astype(str))
    if "core_mainstream" in labels or "core_mainstream_theme" in statuses or bool(buckets & CORE_MAINSTREAM_THEME_KEYWORDS):
        return "core_mainstream_theme"
    if "non_mainstream" in labels or "non_mainstream_theme" in statuses:
        return "non_mainstream_theme"
    return theme_structural_status(theme_name)


def theme_mainstream_label(flow_status: Any, structural_status: Any) -> str:
    flow = safe_str(flow_status)
    structural = safe_str(structural_status)
    if structural == "core_mainstream_theme":
        if flow in MAINSTREAM_STATUSES:
            return "core_mainstream_supported"
        if flow == "mainstream_overheated":
            return "core_mainstream_overheated"
        return "core_mainstream_watch"
    if flow in MAINSTREAM_STATUSES:
        return "non_mainstream_flow_active"
    if flow == "mainstream_overheated":
        return "non_mainstream_overheated"
    if flow == "single_name_signal":
        return "non_mainstream_single_name"
    if flow == "weak_theme":
        return "non_mainstream_weak"
    return "non_mainstream_watch"


def category_of(row: pd.Series) -> str:
    return first_text(row, ["category", "original_category", "breakout_type"]).lower()


def decision_priority_of(row: pd.Series) -> str:
    return first_text(row, ["decision_priority", "priority", "revaluation_priority"])


def tdcc_status_of(row: pd.Series) -> str:
    text = lower_text(row, ["tdcc_status", "tdcc_judgement", "tdcc_accumulation_signal", "tdcc_judge"])
    if "distribution" in text or "轉弱" in text or "頧" in text:
        return "distribution_warning"
    if "strong_accumulation" in text or "strong" in text or "強" in text:
        return "strong_accumulation"
    if "mild_accumulation" in text or "mild" in text or "溫和" in text:
        return "mild_accumulation"
    return "neutral" if text.strip() else ""


def warrant_signal_of(row: pd.Series) -> str:
    return first_text(row, ["warrant_flow_signal", "warrant_status"]).lower()


def is_strict_breakout(row: pd.Series) -> bool:
    cat = category_of(row)
    btype = first_text(row, ["breakout_type"]).lower()
    return (
        cat in {"true_breakout", "breakout"}
        or btype in {"true_breakout", "breakout", "strict_60d_volume_breakout"}
        or truthy(row.get("strict_breakout", ""))
    )


def is_true_breakout(row: pd.Series) -> bool:
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    return is_strict_breakout(row) or truthy(row.get("true_breakout", "")) or stage == "breakout_confirmed"


def is_volume_breakout(row: pd.Series) -> bool:
    btype = first_text(row, ["volume_breakout_type", "breakout_type"]).lower()
    if btype in {
        "strict_60d_volume_breakout",
        "platform_volume_breakout",
        "neckline_volume_breakout",
        "right_side_volume_attack",
    }:
        return True
    if truthy(row.get("volume_confirmed_breakout", "")):
        return True
    volume_ratio = num(row, ["volume_ratio"])
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    if not math.isnan(volume_ratio) and volume_ratio >= 1.5:
        return bool(
            stage in {"platform_breakout", "neckline_breakout", "breakout_confirmed"}
            or truthy(row.get("platform_breakout_flag", ""))
            or truthy(row.get("neckline_breakout_flag", ""))
            or truthy(row.get("breakout_close_near_high_flag", ""))
        )
    return False


def is_near_high(row: pd.Series) -> bool:
    for col in [
        "distance_to_previous_60d_high_pct",
        "distance_to_previous_high_pct",
        "distance_to_high_60_pct",
        "neckline_distance_pct",
    ]:
        value = num(row, [col])
        if not math.isnan(value) and value >= -5:
            return True
    return False


def is_revenue_growth(row: pd.Series) -> bool:
    cat = category_of(row)
    if cat in {"revenue_breakout_low_response", "revenue_pullback"}:
        return True
    for col in ["latest_revenue_yoy", "revenue_yoy_pct", "cumulative_revenue_yoy", "cumulative_yoy_pct"]:
        value = num(row, [col])
        if not math.isnan(value) and value >= 20:
            return True
    return False


def is_revenue_low_response(row: pd.Series) -> bool:
    return category_of(row) == "revenue_breakout_low_response"


def is_overheated(row: pd.Series) -> bool:
    if first_text(row, ["overheat_status"]).lower() in {"overheated_or_priced_in", "continued_overheated"}:
        return True
    if truthy(row.get("already_priced_in", "")) or truthy(row.get("catalyst_overheated", "")):
        return True
    if first_text(row, ["price_reaction_level"]).lower() in {"priced_in", "overheated"}:
        return True
    ret20 = num(row, ["return_20d", "return_20d_pct"])
    dist_ma20 = num(row, ["distance_to_ma20_pct", "gap_ma20_pct", "distance_to_ema23_pct"])
    return (not math.isnan(ret20) and ret20 > 30) or (not math.isnan(dist_ma20) and dist_ma20 > 20)


def has_confirmed_event(row: pd.Series) -> bool:
    if any(truthy(row.get(col, "")) for col in ["eps_surprise_flag", "margin_improvement_flag", "profit_turnaround_flag"]):
        return True
    text = lower_text(row, ["fundamental_catalyst_tags", "event_catalyst_tags", "catalyst_tags", "catalyst_summary"])
    return any(token in text for token in ["confirmed_event", "eps_surprise", "gross_margin", "margin_improvement", "new_order", "customer_win"])


def relative_strength(row: pd.Series) -> float:
    return num(
        row,
        [
            "relative_return_vs_benchmark",
            "theme_relative_strength",
            "relative_ret_20d_vs_benchmark",
            "relative_ret_20d_vs_twse",
            "relative_ret_20d_vs_tpex",
        ],
        default=math.nan,
    )


def leader_sort_frame(part: pd.DataFrame) -> pd.DataFrame:
    frame = part.copy()
    frame["_priority_order"] = frame.apply(lambda row: priority_order(decision_priority_of(row)), axis=1)
    frame["_true_breakout"] = frame.apply(is_true_breakout, axis=1).astype(int)
    frame["_volume_breakout"] = frame.apply(is_volume_breakout, axis=1).astype(int)
    frame["_near_high"] = frame.apply(is_near_high, axis=1).astype(int)
    frame["_decision_score"] = pd.to_numeric(frame.get("decision_score", frame.get("score", "")), errors="coerce").fillna(0)
    frame["_volume_ratio"] = pd.to_numeric(frame.get("volume_ratio", ""), errors="coerce").fillna(0)
    return frame.sort_values(
        ["_priority_order", "_true_breakout", "_volume_breakout", "_near_high", "_decision_score", "_volume_ratio"],
        ascending=[True, False, False, False, False, False],
    )


def leader_confirmed(row: pd.Series) -> bool:
    return (
        is_true_breakout(row)
        or is_volume_breakout(row)
        or (is_near_high(row) and num(row, ["volume_ratio"]) >= 1.2)
        or warrant_signal_of(row) in BULLISH_WARRANT_SIGNALS
        or tdcc_status_of(row) in {"strong_accumulation", "mild_accumulation"}
    )


def theme_status(metrics: dict[str, Any]) -> str:
    count = int(metrics["theme_candidate_count"])
    breakout_like = int(metrics["theme_strict_breakout_count"]) + int(metrics["theme_true_breakout_count"]) + int(metrics["theme_volume_breakout_count"]) + int(metrics["theme_near_high_count"])
    accumulation = int(metrics["theme_tdcc_strong_count"]) + int(metrics["theme_tdcc_mild_count"])
    risk_count = int(metrics["theme_overheated_count"]) + int(metrics["theme_tdcc_distribution_warning_count"])
    bullish_warrant = int(metrics["theme_warrant_bullish_count"])
    avg_volume = float(metrics["theme_avg_volume_ratio"])
    avg_rs = float(metrics["theme_avg_relative_strength_vs_benchmark"])
    leader_ok = bool(metrics["theme_leader_confirmed"])

    if count <= 1:
        return "single_name_signal"
    if risk_count >= max(2, math.ceil(count * 0.45)) and (int(metrics["theme_overheated_count"]) > 0 or avg_rs < -3):
        return "mainstream_overheated"
    if (
        count >= 3
        and leader_ok
        and breakout_like >= 2
        and avg_volume >= 1.15
        and avg_rs >= -2
        and risk_count <= max(1, count // 3)
    ):
        return "mainstream_leader"
    if count >= 3 and (breakout_like >= 1 or accumulation >= 2 or bullish_warrant >= 2) and risk_count < count:
        return "mainstream_follow_through"
    if count >= 2 and (breakout_like >= 1 or accumulation >= 1 or avg_volume >= 1.2):
        return "emerging_theme"
    return "weak_theme"


def build_theme_metrics(candidates: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for theme_name, part in candidates.groupby("theme_name", dropna=False):
        if not safe_str(theme_name):
            theme_name = "other"
        frame = part.copy()
        priority = frame.apply(lambda row: decision_priority_of(row), axis=1)
        tdcc = frame.apply(tdcc_status_of, axis=1)
        warrant = frame.apply(warrant_signal_of, axis=1)
        volume_ratio = pd.to_numeric(frame.get("volume_ratio", ""), errors="coerce")
        rs_values = frame.apply(relative_strength, axis=1)
        leader_frame = leader_sort_frame(frame)
        leader = leader_frame.iloc[0]

        metrics = {
            "theme_name": theme_name,
            "theme_candidate_count": int(len(frame)),
            "theme_A_candidate_count": int(priority.eq("A_priority_watch").sum()),
            "theme_B_candidate_count": int(priority.eq("B_confirm_needed").sum()),
            "theme_strict_breakout_count": int(frame.apply(is_strict_breakout, axis=1).sum()),
            "theme_true_breakout_count": int(frame.apply(is_true_breakout, axis=1).sum()),
            "theme_volume_breakout_count": int(frame.apply(is_volume_breakout, axis=1).sum()),
            "theme_near_high_count": int(frame.apply(is_near_high, axis=1).sum()),
            "theme_revenue_growth_count": int(frame.apply(is_revenue_growth, axis=1).sum()),
            "theme_revenue_low_response_count": int(frame.apply(is_revenue_low_response, axis=1).sum()),
            "theme_tdcc_strong_count": int(tdcc.eq("strong_accumulation").sum()),
            "theme_tdcc_mild_count": int(tdcc.eq("mild_accumulation").sum()),
            "theme_tdcc_distribution_warning_count": int(tdcc.eq("distribution_warning").sum()),
            "theme_warrant_bullish_count": int(warrant.isin(BULLISH_WARRANT_SIGNALS).sum()),
            "theme_warrant_bearish_count": int(warrant.isin(BEARISH_WARRANT_SIGNALS).sum()),
            "theme_overheated_count": int(frame.apply(is_overheated, axis=1).sum()),
            "theme_avg_volume_ratio": round(float(volume_ratio.dropna().mean()) if volume_ratio.notna().any() else 0.0, 2),
            "theme_avg_relative_strength_vs_benchmark": round(float(rs_values.dropna().mean()) if rs_values.notna().any() else 0.0, 2),
            "theme_leader_stock_id": normalize_code(first_text(leader, ["stock_id", "ticker"])),
            "theme_leader_stock_name": first_text(leader, ["stock_name", "name", "ticker_name"]),
            "theme_leader_confirmed": bool(leader_confirmed(leader)),
        }
        metrics["theme_breadth_score"] = round(
            min(
                100,
                metrics["theme_candidate_count"] * 4
                + metrics["theme_A_candidate_count"] * 7
                + metrics["theme_B_candidate_count"] * 4
                + metrics["theme_true_breakout_count"] * 10
                + metrics["theme_volume_breakout_count"] * 8
                + metrics["theme_near_high_count"] * 5,
            ),
            1,
        )
        metrics["theme_strength_score"] = round(
            min(
                100,
                metrics["theme_breadth_score"] * 0.55
                + metrics["theme_tdcc_strong_count"] * 8
                + metrics["theme_tdcc_mild_count"] * 4
                + metrics["theme_warrant_bullish_count"] * 5
                + max(0.0, metrics["theme_avg_volume_ratio"] - 1.0) * 8
                + max(0.0, metrics["theme_avg_relative_strength_vs_benchmark"]) * 1.5,
            ),
            1,
        )
        metrics["theme_risk_score"] = round(
            min(
                100,
                metrics["theme_tdcc_distribution_warning_count"] * 12
                + metrics["theme_overheated_count"] * 10
                + metrics["theme_warrant_bearish_count"] * 6
                + max(0.0, -metrics["theme_avg_relative_strength_vs_benchmark"]) * 2,
            ),
            1,
        )
        metrics["theme_final_status"] = theme_status(metrics)
        metrics["theme_market_flow_status"] = metrics["theme_final_status"]
        metrics["theme_structural_status"] = theme_structural_status_from_frame(theme_name, frame)
        metrics["theme_mainstream_label"] = theme_mainstream_label(
            metrics["theme_market_flow_status"],
            metrics["theme_structural_status"],
        )
        rows.append(metrics)

    if not rows:
        return pd.DataFrame(columns=[col for col in THEME_COLUMNS_TO_MERGE if col.startswith("theme_")])
    return pd.DataFrame(rows).sort_values(
        ["theme_final_status", "theme_strength_score", "theme_breadth_score", "theme_risk_score"],
        ascending=[True, False, False, True],
    )


def is_individual_quality(row: pd.Series) -> bool:
    priority = decision_priority_of(row)
    if priority in {"A_priority_watch", "B_confirm_needed"}:
        return True
    return bool(is_revenue_growth(row) or tdcc_status_of(row) in {"strong_accumulation", "mild_accumulation"} or has_confirmed_event(row))


def is_risk_downgraded(row: pd.Series, theme_status_value: str) -> bool:
    priority = decision_priority_of(row)
    downgrade = first_text(row, ["downgrade_flags", "risk_tags"]).lower()
    return bool(
        priority == "D_risk_downgrade"
        or tdcc_status_of(row) == "distribution_warning"
        or is_overheated(row)
        or "false_breakout" in downgrade
        or "continued_overheated" in downgrade
        or (theme_status_value == "weak_theme" and priority not in {"A_priority_watch", "B_confirm_needed"})
    )


def candidate_line_group(row: pd.Series) -> tuple[str, str, bool, str]:
    theme_status_value = first_text(row, ["theme_final_status"])
    structural_status = first_text(row, ["theme_structural_status"]) or theme_structural_status(first_text(row, ["theme_name"]))
    priority = decision_priority_of(row)
    theme_supported = theme_status_value in MAINSTREAM_STATUSES and structural_status == "core_mainstream_theme"
    individual_quality = is_individual_quality(row)
    risk = is_risk_downgraded(row, theme_status_value)
    attack = is_true_breakout(row) or is_volume_breakout(row) or is_near_high(row)
    tdcc_or_warrant = tdcc_status_of(row) in {"strong_accumulation", "mild_accumulation"} or warrant_signal_of(row) in BULLISH_WARRANT_SIGNALS
    overlap = bool(theme_supported and priority in {"A_priority_watch", "B_confirm_needed"} and (attack or tdcc_or_warrant))
    cat = category_of(row)

    if risk:
        return "risk_downgraded_candidate", "risk", overlap, "降級 / 鈍化 / 風險清單"
    if theme_status_value in MAINSTREAM_STATUSES and structural_status != "core_mainstream_theme":
        return "individual_quality_candidate", "non_mainstream_flow_watch", overlap, "非主流輪動觀察"
    if theme_status_value == "mainstream_leader":
        return "mainstream_theme_candidate", "mainstream_leader_stock", overlap, "主流領漲股"
    if theme_status_value == "mainstream_follow_through":
        return "mainstream_theme_candidate", "mainstream_follow_through_stock", overlap, "主流補漲股"
    if theme_status_value == "emerging_theme":
        return "mainstream_theme_candidate", "emerging_theme_watch", overlap, "新興族群觀察股"
    if has_confirmed_event(row):
        return "event_driven_candidate", "individual_fundamental_catalyst_watch", False, "基本面改善但尚未發動股"
    if cat == "revenue_breakout_low_response":
        return "latent_watch_candidate", "individual_revenue_low_response_watch", False, "營收低反應觀察股"
    if tdcc_status_of(row) in {"strong_accumulation", "mild_accumulation"}:
        return "latent_watch_candidate", "individual_tdcc_latent_watch", False, "TDCC 潛伏觀察股"
    if theme_status_value == "single_name_signal":
        return "individual_quality_candidate", "individual_single_name_signal", False, "單一個股強訊號"
    if cat == "pattern":
        return "latent_watch_candidate", "individual_pattern_watch", False, "型態觀察股"
    if individual_quality:
        return "individual_quality_candidate", "individual_quality_watch", False, "個股條件股"
    return "individual_quality_candidate", "individual_watch", False, "個股條件股"


def theme_note(row: pd.Series) -> str:
    status = first_text(row, ["theme_final_status"])
    source, line_group, overlap, line = candidate_line_group(row)
    overlap_note = "；同時有族群支持與個股條件，但只作標籤，不改分數、不另成優先 bucket" if overlap else ""
    if source == "mainstream_theme_candidate":
        return f"{status}；列入{line}{overlap_note}，仍依原模型分數排序。"
    if source == "latent_watch_candidate":
        return f"{status}；列入{line}{overlap_note}，依原模型條件與分數排序。"
    if source == "event_driven_candidate":
        return f"{status}；有催化標籤{overlap_note}，需確認利多是否已反應與 EPS/毛利品質。"
    if source == "risk_downgraded_candidate":
        return f"{status}；列入風險或鈍化清單{overlap_note}，保留模型命中並揭露風險。"
    return f"{status}；列入{line}。"


def enrich_candidates(candidates: pd.DataFrame, theme_df: pd.DataFrame) -> pd.DataFrame:
    out = candidates.copy()
    out["source_row_index"] = out.get("source_row_index", pd.Series(range(len(out)), index=out.index))
    out["theme_name"] = out.apply(theme_name_of, axis=1)
    if not theme_df.empty:
        merge_cols = [
            "theme_name",
            "theme_candidate_count",
            "theme_A_candidate_count",
            "theme_B_candidate_count",
            "theme_strict_breakout_count",
            "theme_true_breakout_count",
            "theme_volume_breakout_count",
            "theme_near_high_count",
            "theme_revenue_growth_count",
            "theme_revenue_low_response_count",
            "theme_tdcc_strong_count",
            "theme_tdcc_mild_count",
            "theme_tdcc_distribution_warning_count",
            "theme_warrant_bullish_count",
            "theme_warrant_bearish_count",
            "theme_overheated_count",
            "theme_avg_volume_ratio",
            "theme_avg_relative_strength_vs_benchmark",
            "theme_leader_stock_id",
            "theme_leader_stock_name",
            "theme_leader_confirmed",
            "theme_breadth_score",
            "theme_strength_score",
            "theme_risk_score",
            "theme_final_status",
            "theme_market_flow_status",
            "theme_structural_status",
            "theme_mainstream_label",
        ]
        for col in merge_cols:
            if col != "theme_name" and col in out.columns:
                out = out.drop(columns=[col])
        out = out.merge(theme_df[merge_cols], on="theme_name", how="left")
    else:
        for col in THEME_COLUMNS_TO_MERGE:
            if col.startswith("theme_") and col not in out.columns:
                out[col] = ""

    source_rows: list[dict[str, Any]] = []
    for _, row in out.iterrows():
        source_type, line_group, overlap, line = candidate_line_group(row)
        source_rows.append(
            {
                "candidate_source_type": source_type,
                "candidate_line": line,
                "candidate_line_group": line_group,
                "two_line_overlap_flag": "True" if overlap else "False",
                "theme_leadership_note": theme_note(row),
            }
        )
    source_df = pd.DataFrame(source_rows, index=out.index)
    for col in source_df.columns:
        if col in out.columns:
            out = out.drop(columns=[col])
    out = pd.concat([out, source_df], axis=1)
    return out.fillna("")


def build_two_line_view(enriched: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "signal_date",
        "stock_id",
        "stock_name",
        "category",
        "category_cn",
        "theme_name",
        "theme_final_status",
        "theme_structural_status",
        "theme_mainstream_label",
        "candidate_source_type",
        "candidate_line",
        "candidate_line_group",
        "two_line_overlap_flag",
        "decision_priority",
        "decision_score",
        "tdcc_status",
        "warrant_flow_signal",
        "volume_ratio",
        "return_20d",
        "repeat_appear_label",
        "downgrade_flags",
        "why_selected",
        "why_downgraded",
        "next_confirmation",
        "theme_leadership_note",
    ]
    for col in cols:
        if col not in enriched.columns:
            enriched[col] = ""
    out = enriched[cols].copy()
    out["_priority_order"] = out["decision_priority"].map(
        {"A_priority_watch": 1, "B_confirm_needed": 2, "C_watch_only": 3, "D_risk_downgrade": 4}
    ).fillna(9)
    out["_decision_score"] = pd.to_numeric(out["decision_score"], errors="coerce").fillna(0)
    group_order = {
        "mainstream_leader_stock": 1,
        "mainstream_follow_through_stock": 2,
        "emerging_theme_watch": 3,
        "individual_revenue_low_response_watch": 4,
        "individual_fundamental_catalyst_watch": 5,
        "individual_tdcc_latent_watch": 6,
        "non_mainstream_flow_watch": 7,
        "individual_single_name_signal": 8,
        "individual_pattern_watch": 9,
        "individual_quality_watch": 10,
        "individual_watch": 11,
        "risk": 99,
    }
    out["_line_order"] = out["candidate_line_group"].map(group_order).fillna(50)
    out = out.sort_values(["_line_order", "_priority_order", "_decision_score"], ascending=[True, True, False])
    return out.drop(columns=["_priority_order", "_decision_score", "_line_order"])


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> str:
    if df.empty:
        return "_No rows._"
    use_cols = [col for col in columns if col in df.columns]
    if not use_cols:
        return "_No matching columns._"
    return df[use_cols].head(limit).to_markdown(index=False)


def write_markdown(theme_df: pd.DataFrame, two_line: pd.DataFrame, main_date: str) -> None:
    theme_cols = [
        "theme_name",
        "theme_final_status",
        "theme_structural_status",
        "theme_mainstream_label",
        "theme_candidate_count",
        "theme_A_candidate_count",
        "theme_B_candidate_count",
        "theme_true_breakout_count",
        "theme_volume_breakout_count",
        "theme_near_high_count",
        "theme_tdcc_strong_count",
        "theme_tdcc_mild_count",
        "theme_warrant_bullish_count",
        "theme_overheated_count",
        "theme_avg_relative_strength_vs_benchmark",
        "theme_leader_stock_id",
        "theme_leader_stock_name",
        "theme_breadth_score",
        "theme_strength_score",
        "theme_risk_score",
    ]
    candidate_cols = [
        "stock_id",
        "stock_name",
        "category",
        "theme_name",
        "theme_final_status",
        "theme_structural_status",
        "theme_mainstream_label",
        "candidate_line",
        "decision_priority",
        "decision_score",
        "tdcc_status",
        "warrant_flow_signal",
        "repeat_appear_label",
        "theme_leadership_note",
    ]
    theme_lines = [
        "# Daily Theme Leadership Layer",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        f"- source: `{ALL_CANDIDATES.as_posix()}`",
        "- purpose: keep mainstream-theme selection separate from individual-quality / latent-watch selection.",
        "",
        "## Theme Matrix",
        "",
        markdown_table(theme_df.sort_values(["theme_strength_score", "theme_breadth_score"], ascending=False), theme_cols, 80),
        "",
        "## Status Rules",
        "",
        "- theme_final_status is the daily flow/breadth state, not the structural mainstream definition.",
        "- theme_structural_status=core_mainstream_theme only for core growth themes such as consumer electronics, semiconductors, passive components, PC/NB, AI server, PCB/CCL, networking/optical, power, thermal and connectors.",
        "- Textile, financial, steel, shipping, construction, chemical, plastic and similar cyclical/traditional groups are non_mainstream_theme even when daily flow is strong.",
        "- mainstream_leader/mainstream_follow_through/emerging_theme require core_mainstream_theme before entering the mainstream capital line.",
        "- single_name_signal: stock-level signal only; keep it in individual/latent line.",
        "- weak_theme: theme breadth or relative strength is weak.",
        "- mainstream_overheated: theme is hot but risk/overheat/distribution is high.",
        "",
    ]
    THEME_LEADERSHIP_MD.write_text("\n".join(theme_lines) + "\n", encoding="utf-8")

    lines = [
        "# Daily Candidate Two-Line View",
        "",
        f"- generated_at: `{now_text()}`",
        f"- signal_date: `{main_date}`",
        "- rule: Do not mix mainstream-theme candidates and individual-quality candidates into one total ranking.",
        "- rule: two_line_overlap_flag is informational only; it does not create a separate ranking bucket, score change, or veto.",
        "",
        "## Candidate Lines",
        "",
        "### 1. 主流資金股",
        "",
        markdown_table(
            two_line[two_line["candidate_line_group"].isin(["mainstream_leader_stock", "mainstream_follow_through_stock", "emerging_theme_watch"])],
            candidate_cols,
            60,
        ),
        "",
        "### 2. 個股條件股 / 潛伏觀察股",
        "",
        markdown_table(
            two_line[
                two_line["candidate_line_group"].isin(
                    [
                        "individual_revenue_low_response_watch",
                        "individual_fundamental_catalyst_watch",
                        "individual_tdcc_latent_watch",
                        "non_mainstream_flow_watch",
                        "individual_single_name_signal",
                        "individual_pattern_watch",
                        "individual_quality_watch",
                        "individual_watch",
                    ]
                )
            ],
            candidate_cols,
            80,
        ),
        "",
        "### 3. 族群 + 個股條件交集標籤",
        "",
        markdown_table(two_line[two_line["two_line_overlap_flag"].eq("True")], candidate_cols, 80),
        "",
        "## 降級 / 鈍化 / 風險清單",
        "",
        markdown_table(two_line[two_line["candidate_line_group"].eq("risk")], candidate_cols, 80),
        "",
        "## Usage Notes",
        "",
        "- 主流資金線 and 個股條件線 can both be useful, but they answer different questions.",
        "- single_name_signal is not bad by itself; it means the theme has not broadened yet.",
        "- stale_signal can remain in the latent-watch line, but it must carry confirmation conditions.",
        "- two_line_overlap_flag=True means theme support and stock quality are both present, but it must not override model score or act as a veto/ranking bucket.",
        "",
    ]
    TWO_LINE_VIEW_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def rewrite_all_candidates(enriched: pd.DataFrame) -> None:
    write_csv(enriched, ALL_CANDIDATES)
    try:
        with pd.ExcelWriter(ALL_CANDIDATES_XLSX, engine="openpyxl") as writer:
            enriched.to_excel(writer, sheet_name="all_candidates", index=False)
    except Exception as exc:
        print(f"WARNING: failed to write {ALL_CANDIDATES_XLSX}: {exc}")
    try:
        ALL_CANDIDATES_MD.write_text(enriched.head(300).to_markdown(index=False) + "\n", encoding="utf-8")
    except Exception:
        ALL_CANDIDATES_MD.write_text(enriched.head(300).to_csv(index=False), encoding="utf-8")


def build_layer(candidates: pd.DataFrame, main_date: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    work = candidates.copy()
    if work.empty:
        theme_df = pd.DataFrame()
        two_line = pd.DataFrame()
        return work, theme_df, two_line
    if "source_row_index" not in work.columns:
        work["source_row_index"] = range(len(work))
    work["theme_name"] = work.apply(theme_name_of, axis=1)
    theme_df = build_theme_metrics(work)
    enriched = enrich_candidates(work, theme_df)
    two_line = build_two_line_view(enriched)
    return enriched, theme_df, two_line


def main() -> int:
    main_date = main_price_date_from_freshness()
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if candidates.empty:
        raise RuntimeError(f"Missing or empty {ALL_CANDIDATES}")

    enriched, theme_df, two_line = build_layer(candidates, main_date)
    rewrite_all_candidates(enriched)
    write_csv(theme_df, THEME_LEADERSHIP_CSV)
    write_csv(two_line, TWO_LINE_VIEW_CSV)
    write_markdown(theme_df, two_line, main_date)

    print(f"Saved: {ALL_CANDIDATES} rows={len(enriched)}")
    print(f"Saved: {THEME_LEADERSHIP_CSV} rows={len(theme_df)}")
    print(f"Saved: {THEME_LEADERSHIP_MD}")
    print(f"Saved: {TWO_LINE_VIEW_CSV} rows={len(two_line)}")
    print(f"Saved: {TWO_LINE_VIEW_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
