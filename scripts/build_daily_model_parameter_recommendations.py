from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, now_text, write_csv  # noqa: E402


RESEARCH_CSV = LATEST_DIR / "daily_model_parameter_research_latest.csv"
DETAIL_CSV = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.csv"
OUT_CSV = LATEST_DIR / "daily_model_parameter_recommendations_latest.csv"
OUT_MD = LATEST_DIR / "daily_model_parameter_recommendations_latest.md"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name


PROMOTE_MIN_SAMPLE = 100
PROMOTE_MIN_WIN_RATE = 60.0
PROMOTE_MIN_AVG_RETURN = 5.0
SECONDARY_MIN_WIN_RATE = 52.0
SECONDARY_MIN_AVG_RETURN = 2.0
INTRADAY_MIN_HIGH_HIT = 45.0
INTRADAY_MIN_AVG_HIGH_RETURN = 8.0


def safe_float(value: Any, default: float = math.nan) -> float:
    if value is None:
        return default
    try:
        if pd.isna(value):
            return default
    except Exception:
        pass
    text = str(value).strip().replace("%", "").replace(",", "")
    if not text or text.lower() in {"nan", "none", "<na>"}:
        return default
    try:
        return float(text)
    except Exception:
        return default


def safe_int(value: Any) -> int:
    num = safe_float(value)
    if math.isnan(num):
        return 0
    return int(num)


def best_detail(detail: pd.DataFrame, model_id: str, parameter_set_id: str) -> dict[str, Any]:
    if detail.empty:
        return {}
    part = detail[
        detail["model_id"].astype(str).eq(str(model_id))
        & detail["parameter_set_id"].astype(str).eq(str(parameter_set_id))
    ].copy()
    if part.empty:
        return {}
    for col in ["avg_high_return_pct", "high_5pct_hit_rate_pct", "avg_close_return_pct", "close_win_rate_pct"]:
        part[col] = pd.to_numeric(part[col], errors="coerce")
    high = part.sort_values(["avg_high_return_pct", "high_5pct_hit_rate_pct"], ascending=[False, False]).iloc[0]
    close = part.sort_values(["avg_close_return_pct", "close_win_rate_pct"], ascending=[False, False]).iloc[0]
    return {
        "best_high_horizon": str(high.get("horizon", "")),
        "best_avg_high_return_pct": round(float(high.get("avg_high_return_pct", math.nan)), 2),
        "best_high_5pct_hit_rate_pct": round(float(high.get("high_5pct_hit_rate_pct", math.nan)), 2),
        "best_detail_close_horizon": str(close.get("horizon", "")),
    }


def recommendation_for(row: pd.Series, high_stats: dict[str, Any]) -> tuple[str, str, str]:
    sample = safe_int(row.get("selected_stock_days"))
    win = safe_float(row.get("best_close_win_rate_pct"))
    avg = safe_float(row.get("best_avg_close_return_pct"))
    sample_status = str(row.get("sample_status", ""))
    visibility = str(row.get("pdf_visibility", ""))
    high_hit = safe_float(high_stats.get("best_high_5pct_hit_rate_pct"))
    high_avg = safe_float(high_stats.get("best_avg_high_return_pct"))
    model_id = str(row.get("model_id", ""))

    if sample_status == "insufficient_sample" or sample < 30:
        return (
            "research_only",
            "insufficient_sample",
            "樣本不足，只能保留研究觀察，不可放入 PDF 核心選股或調整權重。",
        )

    if visibility.startswith("research_only"):
        return (
            "research_only",
            "explicit_research_model",
            "此模型目前定義為研究型，不進每日 PDF 核心名單；持續累積資料與調參。",
        )

    if sample >= PROMOTE_MIN_SAMPLE and win >= PROMOTE_MIN_WIN_RATE and avg >= PROMOTE_MIN_AVG_RETURN:
        return (
            "promote_to_pdf_core",
            "close_hold_edge",
            "D+1 到 D+10 的最佳收盤勝率與平均報酬達第一版門檻，可列入 PDF 專項核心候選；仍不可直接改核心權重。",
        )

    if sample >= PROMOTE_MIN_SAMPLE and win >= SECONDARY_MIN_WIN_RATE and avg >= SECONDARY_MIN_AVG_RETURN:
        return (
            "pdf_secondary_watch",
            "moderate_close_hold_edge",
            "收盤持有邊際優勢普通，可列次要觀察或加分項，不應作為單一主條件。",
        )

    if sample >= PROMOTE_MIN_SAMPLE and high_hit >= INTRADAY_MIN_HIGH_HIT and high_avg >= INTRADAY_MIN_AVG_HIGH_RETURN:
        return (
            "intraday_target_watch",
            "high_return_not_close_hold",
            "盤中最高價命中率/高點報酬較好，但收盤勝率不足；只能作短線目標價或移動停利研究，不可寫成收盤持有勝率。",
        )

    if model_id in {"price_pullback_23ema", "tdcc_stealth_accumulation"} and avg > 0:
        return (
            "score_component_only",
            "weak_positive_edge",
            "單獨模型勝率不足，但平均報酬略正；可當 TDCC、營收、族群或權證共振的加分項。",
        )

    return (
        "research_only",
        "weak_or_unproven",
        "目前第一版回測沒有足夠收盤持有優勢；保留研究，不放入 PDF 核心推薦。",
    )


def build_recommendations(research: pd.DataFrame, detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, row in research.iterrows():
        high_stats = best_detail(detail, str(row.get("model_id", "")), str(row.get("parameter_set_id", "")))
        rec, reason_code, note = recommendation_for(row, high_stats)
        rows.append(
            {
                "generated_at": now_text(),
                "model_id": row.get("model_id", ""),
                "model_name_zh": row.get("model_name_zh", ""),
                "parameter_set_id": row.get("parameter_set_id", ""),
                "parameter_summary": row.get("parameter_summary", ""),
                "entry_basis": row.get("entry_basis", ""),
                "recommended_usage": rec,
                "recommendation_reason_code": reason_code,
                "recommended_close_exit_horizon": row.get("best_close_horizon_d1_d10", ""),
                "best_close_win_rate_pct": row.get("best_close_win_rate_pct", ""),
                "best_avg_close_return_pct": row.get("best_avg_close_return_pct", ""),
                "recommended_high_exit_horizon": high_stats.get("best_high_horizon", ""),
                "best_avg_high_return_pct": high_stats.get("best_avg_high_return_pct", ""),
                "best_high_5pct_hit_rate_pct": high_stats.get("best_high_5pct_hit_rate_pct", ""),
                "selected_stock_days": row.get("selected_stock_days", ""),
                "selected_unique_stocks": row.get("selected_unique_stocks", ""),
                "sample_status": row.get("sample_status", ""),
                "pdf_visibility": row.get("pdf_visibility", ""),
                "model_revision_note": note,
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    usage_order = {
        "promote_to_pdf_core": 0,
        "pdf_secondary_watch": 1,
        "score_component_only": 2,
        "intraday_target_watch": 3,
        "research_only": 9,
    }
    out["_usage_order"] = out["recommended_usage"].map(usage_order).fillna(9)
    out["_avg"] = pd.to_numeric(out["best_avg_close_return_pct"], errors="coerce").fillna(-999)
    out["_win"] = pd.to_numeric(out["best_close_win_rate_pct"], errors="coerce").fillna(-999)
    out = out.sort_values(
        ["_usage_order", "_avg", "_win", "selected_stock_days", "model_id", "parameter_set_id"],
        ascending=[True, False, False, False, True, True],
    ).drop(columns=["_usage_order", "_avg", "_win"])
    return out.reset_index(drop=True)


def write_markdown(df: pd.DataFrame) -> None:
    lines: list[str] = [
        "# DAILY MODEL PARAMETER RECOMMENDATIONS",
        "",
        f"- generated_at: {now_text()}",
        "- purpose: convert parameter backtests into program-side reporting recommendations",
        "- entry_basis: signal date next trading day open",
        "- close_return: D+n close divided by next open minus 1",
        "- high_return: max intraday high through D+n divided by next open minus 1",
        "- rule: recommendations affect reporting and model research priority only; do not silently change core weights",
        "",
    ]
    if df.empty:
        lines.extend(["sample_status: data_missing", ""])
    else:
        counts = df["recommended_usage"].value_counts().reset_index()
        counts.columns = ["recommended_usage", "count"]
        lines.extend(["## Usage Summary", "", markdown_table(counts, counts.columns.tolist()), ""])

        show_cols = [
            "model_id",
            "parameter_set_id",
            "recommended_usage",
            "recommended_close_exit_horizon",
            "best_close_win_rate_pct",
            "best_avg_close_return_pct",
            "recommended_high_exit_horizon",
            "best_high_5pct_hit_rate_pct",
            "selected_stock_days",
            "model_revision_note",
        ]
        lines.extend(["## Top Recommendations", "", markdown_table(df[show_cols].head(25), show_cols), ""])

        research_only = df[df["recommended_usage"].eq("research_only")].head(25)
        if not research_only.empty:
            lines.extend(["## Research Only / Not Yet Promoted", "", markdown_table(research_only[show_cols], show_cols), ""])

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    if not RESEARCH_CSV.exists():
        raise FileNotFoundError(f"missing research file: {RESEARCH_CSV}")
    research = pd.read_csv(RESEARCH_CSV)
    detail = pd.read_csv(DETAIL_CSV) if DETAIL_CSV.exists() else pd.DataFrame()
    recommendations = build_recommendations(research, detail)
    write_csv(recommendations, OUT_CSV)
    write_csv(recommendations, DOCS_CSV)
    write_markdown(recommendations)
    print(f"Saved: {OUT_CSV} rows={len(recommendations)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
