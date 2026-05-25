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

REGRESSION_2484_MD = LATEST_DIR / "daily_candidate_regression_2484_latest.md"
REGRESSION_2484_CSV = LATEST_DIR / "daily_candidate_regression_2484_latest.csv"

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
    "highlight_tag",
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
]


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
        if name in row.index:
            text = safe_str(row.get(name, ""))
            if text:
                return text
    return ""


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


def next_confirmation_for(row: pd.Series, pattern_category: str, priority: str, downgrade_flags: list[str]) -> str:
    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
    if "tdcc_distribution_warning" in downgrade_flags:
        return "先看 TDCC 是否停止轉弱，再看價格能否守住 MA20/EMA23 與突破區。"
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

    stage = first_text(row, ["pattern_stage", "pattern"]).lower()
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
        decision_score -= 14
    elif repeat_label == "continued_overheated":
        downgrade_flags.append("continued_overheated")
        risk_tags.append("連續上榜但過熱")
        decision_score -= 18
    elif repeat_label == "repeated_but_no_breakout":
        downgrade_flags.append("repeated_but_no_breakout")
        risk_tags.append("反覆上榜未突破")
        decision_score -= 6
    elif repeat_label == "continued_2_3d":
        decision_score += 4

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

    severe_flags = {
        "tdcc_distribution_warning",
        "stale_signal",
        "continued_overheated",
        "return_20d_gt_30",
        "distance_ma20_gt_20",
        "short_term_volume_overheat",
        "false_breakout_risk",
    }
    has_severe = bool(severe_flags.intersection(downgrade_flags))
    if has_severe:
        priority = "D_risk_downgrade" if decision_score < 62 else "C_watch_only"
    elif decision_score >= 82:
        priority = "A_priority_watch"
    elif decision_score >= 68:
        priority = "B_confirm_needed"
    else:
        priority = "C_watch_only"

    priority_label = {
        "A_priority_watch": "最優先追蹤",
        "B_confirm_needed": "可等確認",
        "C_watch_only": "僅觀察",
        "D_risk_downgrade": "暫避降級 / 只保留觀察",
    }[priority]

    if priority == "A_priority_watch":
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
    next_confirmation = next_confirmation_for(row, pattern_category, priority, downgrade_flags)

    return {
        "pattern_mapped_category": pattern_category,
        "pattern_route": pattern_route,
        "decision_priority": priority,
        "decision_priority_label": priority_label,
        "decision_score": decision_score,
        "highlight_tag": highlight,
        "downgrade_flags": "|".join(dict.fromkeys(downgrade_flags)),
        "risk_tags": "|".join(dict.fromkeys(risk_tags)),
        "tdcc_status": tdcc_status,
        "repeat_appear_summary": repeat_label,
        "overheat_status": overheat_status,
        "why_selected": why_selected,
        "why_downgraded": why_downgraded,
        "next_confirmation": next_confirmation,
        "must_not_overstate": "True" if priority in {"C_watch_only", "D_risk_downgrade"} or bool(downgrade_flags) else "False",
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

    for col in DECISION_COLUMNS:
        if col not in decision.columns:
            decision[col] = ""
    return decision[DECISION_COLUMNS]


def rewrite_all_candidates(candidates: pd.DataFrame, decision: pd.DataFrame) -> pd.DataFrame:
    out = candidates.copy()
    if out.empty or decision.empty:
        return out

    out["_row_key"] = range(len(out))
    decision_for_merge = decision.copy()
    decision_for_merge["_row_key"] = range(len(decision_for_merge))
    merge_cols = [
        "_row_key",
        "pattern_mapped_category",
        "pattern_route",
        "decision_priority",
        "decision_priority_label",
        "decision_score",
        "decision_rank_in_category",
        "decision_rank_overall_for_display",
        "highlight_tag",
        "downgrade_flags",
        "risk_tags",
        "tdcc_status",
        "repeat_appear_summary",
        "overheat_status",
        "why_selected",
        "why_downgraded",
        "next_confirmation",
        "must_not_overstate",
    ]
    for col in merge_cols:
        if col != "_row_key" and col in out.columns:
            out = out.drop(columns=[col])
    out = out.merge(decision_for_merge[merge_cols], on="_row_key", how="left").drop(columns=["_row_key"])
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
        "- Do not mix category scores into one investment ranking; `decision_rank_overall_for_display` is only a display order.",
        "- If `decision_priority` is `D_risk_downgrade`, explain the risk and do not present it as top priority.",
        "- If TDCC is `distribution_warning`, repeat label is stale/overheated, or overheat flags are present, downgrade even when the breakout pattern is strong.",
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
        "- Strong breakout patterns must still be downgraded when TDCC distribution, stale repeat appearance, or overheat flags appear.",
        "- For 2484 regression: 20260520-20260521 platform_right_side, 20260522 neckline_breakout, 20260525 breakout_confirmed.",
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

    case_2484 = decision[decision["stock_id"].eq("2484")].copy()
    lines.extend(["", "## 2484 Latest Decision", ""])
    lines.append(render_table(case_2484, top_cols, limit=10))

    lines.extend(["", "## 2484 Regression Replay", ""])
    lines.extend(regression_2484_summary())
    lines.append("")
    DECISION_PACKET.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    preferred_date = main_price_date_from_freshness()
    candidates = read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if candidates.empty:
        raise RuntimeError(f"missing or empty {ALL_CANDIDATES}")

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
