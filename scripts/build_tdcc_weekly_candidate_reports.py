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

WEEKLY_INCREASE_CSV = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.csv"
WEEKLY_INCREASE_MD = LATEST_DIR / "tdcc_weekly_increase_ranking_latest.md"
CONSECUTIVE_CSV = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.csv"
CONSECUTIVE_MD = LATEST_DIR / "tdcc_consecutive_accumulation_ranking_latest.md"
MODEL_CROSS_CSV = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.csv"
MODEL_CROSS_MD = LATEST_DIR / "tdcc_weekly_model_cross_summary_latest.md"
HIGHLIGHT_MD = LATEST_DIR / "tdcc_weekly_candidate_highlight_latest.md"
FULL_MD = LATEST_DIR / "tdcc_weekly_candidate_full_latest.md"
TRACKING_PACKET_MD = LATEST_DIR / "tdcc_chatgpt_tracking_packet_latest.md"

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
    "model_score",
    "source_hit_labels_zh",
    "why_selected_zh",
    "risk_tags_zh",
    "next_confirmation_zh",
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
    }
    for col in numeric_cols & set(out.columns):
        out[col] = out[col].map(lambda v: fmt(v, 2))
    return out[columns]


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
    out = df[["stock_id", "rank", score_col]].copy()
    out = out.rename(columns={"rank": "tdcc_rank", score_col: "tdcc_score"})
    out["tdcc_list_type"] = list_type
    return out


def build_model_cross(weekly: pd.DataFrame, consecutive: pd.DataFrame) -> pd.DataFrame:
    models = read_csv(DAILY_MODEL_SIGNALS, dtype=str)
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

    merged["display_rank_num"] = pd.to_numeric(merged.get("display_rank", ""), errors="coerce").fillna(9999)
    merged["model_score_num"] = pd.to_numeric(merged.get("model_score", ""), errors="coerce").fillna(-9999)
    merged = merged.sort_values(
        ["tdcc_list_type", "model_id", "display_rank_num", "model_score_num", "stock_id"],
        ascending=[True, True, True, False, True],
    )
    merged = merged.groupby(["tdcc_list_type", "model_id"], group_keys=False).head(3)
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
        "tdcc_weekly_candidate_highlight": [HIGHLIGHT_MD],
        "tdcc_weekly_candidate_full": [FULL_MD],
    }
    fields: dict[str, str] = {}
    for prefix, paths in files.items():
        for path in paths:
            suffix = "csv" if path.suffix.lower() == ".csv" else "md"
            fields[f"{prefix}_{suffix}_raw_url"] = raw_url(path)
            fields[f"{prefix}_{suffix}_pages_url"] = pages_url(path)

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
    append_tracking_packet_section(weekly, consecutive)
    upsert_readme_fields()

    print(f"Saved: {WEEKLY_INCREASE_CSV} rows={len(weekly)}")
    print(f"Saved: {CONSECUTIVE_CSV} rows={len(consecutive)}")
    print(f"Saved: {MODEL_CROSS_CSV} rows={len(cross)}")
    print(f"Saved: {HIGHLIGHT_MD}")
    print(f"Saved: {FULL_MD}")
    print(f"latest_signal_date={meta.get('latest_signal_date', '')}")


if __name__ == "__main__":
    main()
