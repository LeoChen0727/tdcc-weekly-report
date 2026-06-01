from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_tdcc_chatgpt_tracking_outputs import prepare_latest_frame, risk_bucket  # noqa: E402
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    markdown_table,
    now_text,
    pages_url,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


DAILY_MODEL_SIGNALS = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
DAILY_DECISION = LATEST_DIR / "daily_candidate_decision_latest.csv"

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
TRACKING_PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"
TDCC_WEEKLY_RULES = Path("rules/tdcc_weekly_rules.md")

README_PATHS = [
    LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
    DOCS_LATEST_DIR / "READ_ME_FIRST_DAILY_REPORT.txt",
]

DELTA_COLS = [
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
]

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
    "tdcc_consecutive_up_weeks",
    "all_thresholds_up",
    "high_thresholds_up",
    "tdcc_price_phase",
    "tdcc_phase_group_zh",
    "risk_bucket",
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
    "tdcc_score",
    "model_id",
    "model_name_zh",
    "tdcc_model_rank_in_list",
    "model_score",
    "model_source",
    "why_selected_zh",
    "risk_tags_zh",
    "next_confirmation_zh",
    "report_usage_zh",
    "operation_note_zh",
]


def as_bool(value: Any) -> bool:
    return safe_str(value).strip().lower() in {"true", "1", "yes", "y"}


def num(df: pd.DataFrame, column: str, default: float = 0.0) -> pd.Series:
    if column not in df.columns:
        return pd.Series(default, index=df.index, dtype="float64")
    return pd.to_numeric(df[column], errors="coerce").fillna(default)


def fmt(value: Any, digits: int = 2) -> str:
    v = to_number(value)
    if math.isnan(v):
        return ""
    return f"{v:.{digits}f}"


def phase_group_zh(value: Any) -> str:
    mapping = {
        "tdcc_leading_price": "潛伏吸籌",
        "tdcc_price_confirmed": "籌碼與股價初步確認",
        "price_leading_tdcc": "股價領先 / 追高風險",
        "overheated_after_tdcc": "過熱延續",
        "tdcc_price_divergence": "背離 / 失效觀察",
        "failed_after_tdcc": "背離 / 失效觀察",
        "insufficient_price_context": "價格資料不足",
        "insufficient_tdcc_history": "TDCC 歷史不足",
        "neutral_or_unclear": "中性或不明",
    }
    return mapping.get(safe_str(value), "觀察")


def theme_bonus(series: pd.Series) -> pd.Series:
    mainstream_status = {
        "mainstream_leader",
        "mainstream_follow_through",
        "emerging_theme",
        "core_mainstream",
        "market_theme",
    }
    return series.astype(str).isin(mainstream_status).astype(int)


def add_tdcc_scores(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in DELTA_COLS:
        if col not in out.columns:
            out[col] = 0.0

    d400 = num(out, "tdcc_1w_change_400")
    d600 = num(out, "tdcc_1w_change_600")
    d800 = num(out, "tdcc_1w_change_800")
    d1000 = num(out, "tdcc_1w_change_1000")
    all_up = out.get("all_thresholds_up", pd.Series(False, index=out.index)).map(as_bool)
    high_up = out.get("high_thresholds_up", pd.Series(False, index=out.index)).map(as_bool)
    weeks = num(out, "tdcc_consecutive_up_weeks")
    bonus = theme_bonus(out.get("theme_mainstream_status", pd.Series("", index=out.index)))

    out["tdcc_four_threshold_weekly_increase_sum"] = d400 + d600 + d800 + d1000
    out["tdcc_weekly_increase_score"] = (
        d400.clip(lower=0) * 1.0
        + d600.clip(lower=0) * 1.2
        + d800.clip(lower=0) * 1.6
        + d1000.clip(lower=0) * 2.0
        + all_up.astype(int) * 5
        + high_up.astype(int) * 3
        + bonus * 2
    )
    out["tdcc_consecutive_accumulation_score"] = (
        out["tdcc_weekly_increase_score"]
        + weeks * 5
        + all_up.astype(int) * 8
        + high_up.astype(int) * 5
    )
    if "tdcc_price_phase" not in out.columns:
        out["tdcc_price_phase"] = ""
    out["tdcc_phase_group_zh"] = out["tdcc_price_phase"].map(phase_group_zh)
    out["risk_bucket"] = out["tdcc_price_phase"].map(risk_bucket)
    out["ranking_note_zh"] = out.apply(build_ranking_note, axis=1)
    return out


def build_ranking_note(row: pd.Series) -> str:
    parts: list[str] = []
    if to_number(row.get("tdcc_four_threshold_weekly_increase_sum")) > 0:
        parts.append("本週四級距合計增加")
    if as_bool(row.get("all_thresholds_up")):
        parts.append("四級距同步增加")
    if as_bool(row.get("high_thresholds_up")):
        parts.append("800/1000 高級距同步增加")
    weeks = to_number(row.get("tdcc_consecutive_up_weeks"))
    if not math.isnan(weeks) and weeks >= 2:
        parts.append(f"連續增加 {int(weeks)} 週")
    if safe_str(row.get("theme_mainstream_status")) in {
        "mainstream_leader",
        "mainstream_follow_through",
        "emerging_theme",
        "core_mainstream",
    }:
        parts.append("族群狀態加分")
    phase = safe_str(row.get("tdcc_phase_group_zh"))
    if phase:
        parts.append(phase)
    return "；".join(parts) if parts else "僅能觀察"


def format_output(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    numeric_cols = {
        "tdcc_weekly_increase_score",
        "tdcc_consecutive_accumulation_score",
        "tdcc_1w_change_400",
        "tdcc_1w_change_600",
        "tdcc_1w_change_800",
        "tdcc_1w_change_1000",
        "tdcc_four_threshold_weekly_increase_sum",
        "price_return_20d",
        "distance_ma20_pct",
        "relative_return_vs_benchmark",
        "tdcc_score",
        "model_score",
        "section_rank",
    }
    for col in numeric_cols & set(out.columns):
        out[col] = out[col].map(lambda v: fmt(v, 2))
    return out[columns]


def report_usage_for_list(list_type: Any) -> str:
    mapping = {
        "weekly_increase": "當週大戶增幅觀察：找本週大戶突然增加，偏短線籌碼變化。",
        "consecutive_accumulation": "連續累積觀察：找兩週以上穩定增加，偏中期籌碼累積。",
    }
    return mapping.get(safe_str(list_type), "TDCC 籌碼候選觀察。")


def operation_note(row: pd.Series) -> str:
    phase = safe_str(row.get("tdcc_phase_group_zh"))
    risk = safe_str(row.get("risk_bucket"))
    next_confirmation = safe_str(row.get("next_confirmation_zh"))
    if "股價領先" in phase or "overheated" in risk or "late" in risk:
        base = "股價已領先或有追高風險，需用每日模型確認量價是否續強。"
    elif "潛伏" in phase:
        base = "偏潛伏吸籌觀察，重點看量價是否開始確認。"
    elif "背離" in phase or "divergent" in risk:
        base = "列為背離或失效觀察，不可只因 TDCC 增加升級。"
    elif "不足" in phase:
        base = "資料不足，只能觀察。"
    else:
        base = "以 TDCC 作籌碼背景，仍需搭配每日模型與價格結構。"
    if next_confirmation:
        return f"{base} 下一確認：{next_confirmation}"
    return base


def build_report_rows(weekly: pd.DataFrame, consecutive: pd.DataFrame, cross: pd.DataFrame, highlight: bool) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []

    def add_rank_section(df: pd.DataFrame, section_id: str, section_name: str, list_type: str) -> None:
        if df.empty:
            return
        part = df.head(5).copy() if highlight else df.copy()
        part["report_kind"] = "highlight" if highlight else "full"
        part["section_id"] = section_id
        part["section_name_zh"] = section_name
        part["section_rank"] = range(1, len(part) + 1)
        part["tdcc_list_type"] = list_type
        part["tdcc_rank"] = part.get("rank", "")
        part["tdcc_score"] = part.get(
            "tdcc_weekly_increase_score" if list_type == "weekly_increase" else "tdcc_consecutive_accumulation_score",
            "",
        )
        part["model_id"] = ""
        part["model_name_zh"] = ""
        part["tdcc_model_rank_in_list"] = ""
        part["model_score"] = ""
        part["model_source"] = "tdcc_ranking"
        part["why_selected_zh"] = part.get("ranking_note_zh", "")
        part["risk_tags_zh"] = part.get("risk_bucket", "")
        part["next_confirmation_zh"] = "後續交叉每日模型、價格結構與量價確認。"
        part["report_usage_zh"] = report_usage_for_list(list_type)
        part["operation_note_zh"] = part.apply(operation_note, axis=1)
        frames.append(format_output(part, REPORT_COLUMNS))

    def add_cross_section(df: pd.DataFrame, list_type: str, section_id: str, section_name: str) -> None:
        if df.empty:
            return
        part = df[df["tdcc_list_type"].astype(str).eq(list_type)].copy()
        if part.empty:
            return
        if highlight:
            part = part.groupby("model_id", group_keys=False).head(3).copy()
        part["report_kind"] = "highlight" if highlight else "full"
        part["section_id"] = section_id
        part["section_name_zh"] = section_name
        part["section_rank"] = part.groupby("model_id", dropna=False).cumcount() + 1
        part["report_usage_zh"] = part["tdcc_list_type"].map(report_usage_for_list)
        part["operation_note_zh"] = part.apply(operation_note, axis=1)
        frames.append(format_output(part, REPORT_COLUMNS))

    add_rank_section(weekly, "weekly_increase_top", "當週增幅榜", "weekly_increase")
    add_rank_section(consecutive, "consecutive_accumulation_top", "連續累積榜", "consecutive_accumulation")
    if not cross.empty:
        add_cross_section(cross, "weekly_increase", "weekly_increase_model_cross", "當週增幅榜 × 每日模型")
        add_cross_section(cross, "consecutive_accumulation", "consecutive_accumulation_model_cross", "連續累積榜 × 每日模型")

    if not frames:
        return pd.DataFrame(columns=REPORT_COLUMNS)
    return pd.concat(frames, ignore_index=True)


def write_report_ready_md(path: Path, title: str, rows: pd.DataFrame, highlight: bool) -> None:
    lines = [
        f"# {title}",
        "",
        f"- generated_at: {now_text()}",
        "- purpose: 這是 TDCC 週報對話端 / PDF generator 的固定資料來源。",
        "- contract: 對話端只渲染本表，不自行改排名、不自行新增買賣判斷、不把不同模型混成單一排名。",
        "- report_mode: 精華版列當週增幅前五、連續累積前五，以及各每日模型交叉前三；完整版列完整清單。",
        "",
    ]
    if rows.empty:
        lines.append("- no rows.")
    else:
        for section_id, part in rows.groupby("section_id", sort=False):
            section_name = safe_str(part["section_name_zh"].iloc[0]) if "section_name_zh" in part.columns else section_id
            lines.extend([f"## {section_name}", "", markdown_table(part, REPORT_COLUMNS), ""])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_weekly_increase(df: pd.DataFrame) -> pd.DataFrame:
    work = df[num(df, "tdcc_four_threshold_weekly_increase_sum") > 0].copy()
    work = work.sort_values(
        [
            "tdcc_weekly_increase_score",
            "tdcc_four_threshold_weekly_increase_sum",
            "tdcc_1w_change_1000",
            "tdcc_1w_change_800",
            "stock_id",
        ],
        ascending=[False, False, False, False, True],
    )
    work["rank"] = range(1, len(work) + 1)
    return format_output(work, BASE_COLUMNS)


def build_consecutive(df: pd.DataFrame) -> pd.DataFrame:
    work = df[num(df, "tdcc_consecutive_up_weeks") >= 2].copy()
    work = work.sort_values(
        [
            "tdcc_consecutive_accumulation_score",
            "tdcc_consecutive_up_weeks",
            "tdcc_four_threshold_weekly_increase_sum",
            "stock_id",
        ],
        ascending=[False, False, False, True],
    )
    work["rank"] = range(1, len(work) + 1)
    return format_output(work, BASE_COLUMNS)


def write_rank_md(path: Path, title: str, df: pd.DataFrame, purpose: str) -> None:
    lines = [
        f"# {title}",
        "",
        f"- generated_at: {now_text()}",
        f"- purpose: {purpose}",
        "- scoring_note: 分數同時考慮 400/600/800/1000 本週增幅、四級距同步、高級距同步、連續週數與族群狀態；這是 TDCC 週報排序，不是單獨買進建議。",
        "",
        markdown_table(df, list(df.columns)),
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def rank_lookup(df: pd.DataFrame, list_type: str, score_col: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(columns=["stock_id", "tdcc_rank", "tdcc_score", "tdcc_list_type"])
    base_cols = [
        "stock_id",
        "rank",
        score_col,
        "signal_date",
        "stock_name",
        "theme",
        "tdcc_phase_group_zh",
        "risk_bucket",
    ]
    cols = [c for c in base_cols if c in df.columns]
    out = df[cols].copy()
    out = out.rename(columns={"rank": "tdcc_rank", score_col: "tdcc_score"})
    out["tdcc_list_type"] = list_type
    return out


def build_decision_model_fallback() -> pd.DataFrame:
    """Daily decision fallback for stocks not covered by the model-signal table.

    The TDCC weekly report first selects stocks by TDCC behavior, then asks where
    those stocks sit in the daily recommendation logic. Some daily candidates
    still only exist in daily_candidate_decision_latest.csv. Treat those rows as
    decision-layer model rows so TDCC-selected names such as pattern-watch stocks
    do not disappear from the cross summary.
    """
    decision = read_csv(DAILY_DECISION, dtype=str)
    if decision.empty:
        return pd.DataFrame()

    category = decision.get("original_category", pd.Series("", index=decision.index)).astype(str)
    category = category.mask(category.eq(""), "uncategorized")
    category_zh = decision.get("original_category_cn", pd.Series("", index=decision.index)).astype(str)
    category_label = category_zh.mask(category_zh.eq(""), category)
    category_label = category_label.mask(category_label.eq(""), "每日決策層")
    rank = decision.get("decision_rank_in_category", decision.get("section_rank", ""))
    if isinstance(rank, str):
        rank = pd.Series(rank, index=decision.index)
    rank = pd.Series(rank, index=decision.index).astype(str)
    missing_rank = rank.eq("") | rank.str.lower().eq("nan")
    if "decision_rank_overall_for_display" in decision.columns:
        rank = rank.mask(missing_rank, decision["decision_rank_overall_for_display"].astype(str))
    fallback = pd.DataFrame(
        {
            "stock_id": decision.get("stock_id", ""),
            "stock_name": decision.get("stock_name", ""),
            "model_id": "daily_decision_" + category,
            "model_name_zh": category_label,
            "display_rank": rank,
            "model_score": decision.get("decision_score", ""),
            "model_source": "daily_candidate_decision",
            "source_hit_labels_zh": category_label,
            "why_selected_zh": decision.get("why_selected", ""),
            "risk_tags_zh": decision.get("risk_tags", ""),
            "next_confirmation_zh": decision.get("next_confirmation", ""),
        }
    )
    fallback["model_name_zh"] = fallback["model_name_zh"].astype(str) + "（決策層）"
    return fallback


def load_daily_model_rows() -> pd.DataFrame:
    models = read_csv(DAILY_MODEL_SIGNALS, dtype=str)
    fallback = build_decision_model_fallback()
    if models.empty and fallback.empty:
        return pd.DataFrame()
    if models.empty:
        combined = fallback
    elif fallback.empty:
        combined = models
    else:
        model_keys = set(zip(models["stock_id"].astype(str), models["model_id"].astype(str)))
        fb = fallback[
            ~fallback.apply(lambda r: (safe_str(r.get("stock_id")), safe_str(r.get("model_id"))) in model_keys, axis=1)
        ]
        combined = pd.concat([models, fb], ignore_index=True, sort=False)
    if "model_source" not in combined.columns:
        combined["model_source"] = ""
    combined["model_source"] = combined["model_source"].replace("", pd.NA).fillna("daily_candidate_model_signal")
    return combined


def build_model_cross(weekly: pd.DataFrame, consecutive: pd.DataFrame) -> pd.DataFrame:
    models = load_daily_model_rows()
    if models.empty:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)

    candidates = pd.concat(
        [
            rank_lookup(weekly, "weekly_increase", "tdcc_weekly_increase_score"),
            rank_lookup(consecutive, "consecutive_accumulation", "tdcc_consecutive_accumulation_score"),
        ],
        ignore_index=True,
    )
    candidates = candidates[candidates["stock_id"].astype(str).ne("")]
    if candidates.empty:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)

    merged = candidates.merge(models, on="stock_id", how="inner", suffixes=("_tdcc", ""))
    if merged.empty:
        return pd.DataFrame(columns=MODEL_CROSS_COLUMNS)

    for column in ["signal_date", "stock_name", "theme", "tdcc_phase_group_zh", "risk_bucket"]:
        tdcc_column = f"{column}_tdcc"
        if tdcc_column not in merged.columns:
            continue
        if column not in merged.columns:
            merged[column] = merged[tdcc_column]
        else:
            current = merged[column].astype(str)
            missing = current.eq("") | current.str.lower().eq("nan")
            merged[column] = merged[column].mask(missing, merged[tdcc_column])

    merged["display_rank_num"] = pd.to_numeric(merged.get("display_rank", ""), errors="coerce").fillna(9999)
    merged["model_score_num"] = pd.to_numeric(merged.get("model_score", ""), errors="coerce").fillna(-9999)
    merged = merged.sort_values(
        ["tdcc_list_type", "model_id", "model_score_num", "display_rank_num", "stock_id"],
        ascending=[True, True, False, True, True],
    )
    merged["tdcc_model_rank_in_list"] = (
        merged.groupby(["tdcc_list_type", "model_id"], dropna=False).cumcount() + 1
    )
    return format_output(merged, MODEL_CROSS_COLUMNS)


def write_model_cross_md(df: pd.DataFrame) -> None:
    lines = [
        "# TDCC Weekly Candidates x Daily Model Cross Summary",
        "",
        f"- generated_at: {now_text()}",
        "- purpose: 將 TDCC 當週增幅榜與連續累積榜股票，交叉到每日候選模型，觀察其在各模型中的位置。",
        "- note: 這是 TDCC 週報候選的模型交叉檢查，不是每日推薦總排名。",
        "",
    ]
    if df.empty:
        lines.append("- no matched daily model rows.")
    else:
        for list_type, part in df.groupby("tdcc_list_type", dropna=False):
            lines.extend([f"## {list_type}", "", markdown_table(part, MODEL_CROSS_COLUMNS), ""])
    MODEL_CROSS_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_report_md(
    path: Path,
    title: str,
    weekly: pd.DataFrame,
    consecutive: pd.DataFrame,
    cross: pd.DataFrame,
    highlight: bool,
) -> None:
    weekly_show = weekly.head(5) if highlight else weekly
    consecutive_show = consecutive.head(5) if highlight else consecutive
    weekly_cross = (
        cross[cross["tdcc_list_type"].astype(str).eq("weekly_increase")]
        if not cross.empty
        else pd.DataFrame(columns=MODEL_CROSS_COLUMNS)
    )
    consecutive_cross = (
        cross[cross["tdcc_list_type"].astype(str).eq("consecutive_accumulation")]
        if not cross.empty
        else pd.DataFrame(columns=MODEL_CROSS_COLUMNS)
    )
    if highlight and not cross.empty:
        weekly_cross = weekly_cross.groupby("model_id", group_keys=False).head(3)
        consecutive_cross = consecutive_cross.groupby("model_id", group_keys=False).head(3)
    lines = [
        f"# {title}",
        "",
        f"- generated_at: {now_text()}",
        "- report_design: 分成當週增幅榜與連續累積榜；再用每日候選模型做交叉檢查，區分潛伏吸籌、股價領先、過熱與背離風險。",
        "- model_cross_note: 每個 TDCC 名單內的股票可出現在多個每日模型；不同模型不混成單一總排名。",
        "",
        "## 當週增幅榜",
        "",
        markdown_table(weekly_show, list(weekly_show.columns) if not weekly_show.empty else BASE_COLUMNS),
        "",
        "## 連續累積榜 / Strength Ranking",
        "",
        markdown_table(consecutive_show, list(consecutive_show.columns) if not consecutive_show.empty else BASE_COLUMNS),
        "",
        "## 當週增幅榜 x 每日候選模型前三",
        "",
        markdown_table(weekly_cross, MODEL_CROSS_COLUMNS),
        "",
        "## 連續累積榜 x 每日候選模型前三",
        "",
        markdown_table(consecutive_cross, MODEL_CROSS_COLUMNS),
        "",
    ]
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def upsert_readme_fields() -> None:
    files = {
        "tdcc_weekly_increase_ranking": [WEEKLY_INCREASE_CSV, WEEKLY_INCREASE_MD],
        "tdcc_consecutive_accumulation_ranking": [CONSECUTIVE_CSV, CONSECUTIVE_MD],
        "tdcc_weekly_model_cross_summary": [MODEL_CROSS_CSV, MODEL_CROSS_MD],
        "tdcc_weekly_candidate_highlight_for_report": [HIGHLIGHT_FOR_REPORT_CSV, HIGHLIGHT_FOR_REPORT_MD],
        "tdcc_weekly_candidate_full_for_report": [FULL_FOR_REPORT_CSV, FULL_FOR_REPORT_MD],
        "tdcc_weekly_candidate_highlight": [HIGHLIGHT_MD],
        "tdcc_weekly_candidate_full": [FULL_MD],
    }
    fields: dict[str, str] = {}
    for prefix, paths in files.items():
        for path in paths:
            suffix = "csv" if path.suffix.lower() == ".csv" else "md"
            fields[f"{prefix}_{suffix}_raw_url"] = raw_url(path)
            fields[f"{prefix}_{suffix}_pages_url"] = pages_url(path)
    if TDCC_WEEKLY_RULES.exists():
        fields["rules_tdcc_weekly_raw_url"] = raw_url(TDCC_WEEKLY_RULES)
        fields["rules_tdcc_weekly_pages_url"] = pages_url(TDCC_WEEKLY_RULES)

    for path in README_PATHS:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines() if path.exists() else []
        out: list[str] = []
        seen: set[str] = set()
        for line in lines:
            key = line.split("=", 1)[0] if "=" in line else ""
            if key in fields:
                out.append(f"{key}={fields[key]}")
                seen.add(key)
            else:
                out.append(line)
        for key, value in fields.items():
            if key not in seen:
                out.append(f"{key}={value}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def append_tracking_packet_section(weekly: pd.DataFrame, consecutive: pd.DataFrame) -> None:
    if not TRACKING_PACKET_MD.exists():
        return
    marker = "## TDCC Weekly Increase and Consecutive Candidate Reports"
    text = TRACKING_PACKET_MD.read_text(encoding="utf-8", errors="replace")
    if marker in text:
        text = text.split(marker, 1)[0].rstrip()

    top_cols = [
        "rank",
        "stock_id",
        "stock_name",
        "tdcc_1w_change_400",
        "tdcc_1w_change_600",
        "tdcc_1w_change_800",
        "tdcc_1w_change_1000",
        "tdcc_phase_group_zh",
        "risk_bucket",
    ]
    section = [
        "",
        marker,
        "",
        "- purpose: 當週增幅榜找本週大戶突然增加；連續累積榜找兩週以上穩定累積。兩者分開排名，不互相替代。",
        "- report_contract: TDCC 報告對話固定生產兩份：精華版與完整版。精華版優先讀 highlight_for_report；完整版優先讀 full_for_report。",
        f"- weekly_candidate_highlight_for_report_csv_raw_url: {raw_url(HIGHLIGHT_FOR_REPORT_CSV)}",
        f"- weekly_candidate_highlight_for_report_md_raw_url: {raw_url(HIGHLIGHT_FOR_REPORT_MD)}",
        f"- weekly_candidate_full_for_report_csv_raw_url: {raw_url(FULL_FOR_REPORT_CSV)}",
        f"- weekly_candidate_full_for_report_md_raw_url: {raw_url(FULL_FOR_REPORT_MD)}",
        f"- weekly_increase_md_raw_url: {raw_url(WEEKLY_INCREASE_MD)}",
        f"- consecutive_accumulation_md_raw_url: {raw_url(CONSECUTIVE_MD)}",
        f"- weekly_candidate_highlight_md_raw_url: {raw_url(HIGHLIGHT_MD)}",
        f"- weekly_candidate_full_md_raw_url: {raw_url(FULL_MD)}",
        "",
        "### Weekly Increase Top 5",
        "",
        markdown_table(weekly.head(5), top_cols),
        "",
        "### Consecutive Accumulation Top 5",
        "",
        markdown_table(consecutive.head(5), top_cols),
        "",
    ]
    TRACKING_PACKET_MD.write_text(text.rstrip() + "\n" + "\n".join(section).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    latest_df, meta = prepare_latest_frame()
    latest_df = add_tdcc_scores(latest_df)

    weekly = build_weekly_increase(latest_df)
    consecutive = build_consecutive(latest_df)
    write_csv(weekly, WEEKLY_INCREASE_CSV)
    write_csv(consecutive, CONSECUTIVE_CSV)
    write_rank_md(
        WEEKLY_INCREASE_MD,
        "TDCC Weekly Increase Ranking",
        weekly,
        "找出本週大戶持股比例突然增加的股票，單週即可上榜。",
    )
    write_rank_md(
        CONSECUTIVE_MD,
        "TDCC Consecutive Accumulation Ranking",
        consecutive,
        "找出連續兩週以上累積增加的股票，偏長期穩定累積。",
    )

    cross = build_model_cross(weekly, consecutive)
    write_csv(cross, MODEL_CROSS_CSV)
    write_model_cross_md(cross)

    write_report_md(HIGHLIGHT_MD, "TDCC Weekly Candidate Highlight", weekly, consecutive, cross, highlight=True)
    write_report_md(FULL_MD, "TDCC Weekly Candidate Full", weekly, consecutive, cross, highlight=False)
    highlight_for_report = build_report_rows(weekly, consecutive, cross, highlight=True)
    full_for_report = build_report_rows(weekly, consecutive, cross, highlight=False)
    write_csv(highlight_for_report, HIGHLIGHT_FOR_REPORT_CSV)
    write_csv(full_for_report, FULL_FOR_REPORT_CSV)
    write_report_ready_md(
        HIGHLIGHT_FOR_REPORT_MD,
        "TDCC Weekly Candidate Highlight For Report",
        highlight_for_report,
        highlight=True,
    )
    write_report_ready_md(
        FULL_FOR_REPORT_MD,
        "TDCC Weekly Candidate Full For Report",
        full_for_report,
        highlight=False,
    )
    append_tracking_packet_section(weekly, consecutive)
    upsert_readme_fields()

    print(f"Saved: {WEEKLY_INCREASE_CSV} rows={len(weekly)}")
    print(f"Saved: {CONSECUTIVE_CSV} rows={len(consecutive)}")
    print(f"Saved: {MODEL_CROSS_CSV} rows={len(cross)}")
    print(f"Saved: {HIGHLIGHT_FOR_REPORT_CSV} rows={len(highlight_for_report)}")
    print(f"Saved: {FULL_FOR_REPORT_CSV} rows={len(full_for_report)}")
    print(f"Saved: {HIGHLIGHT_MD}")
    print(f"Saved: {FULL_MD}")
    print(f"latest_signal_date={meta.get('latest_signal_date', '')}")


if __name__ == "__main__":
    main()
