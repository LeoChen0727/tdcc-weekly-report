from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    is_construction_like,
    main_price_date_from_freshness,
    normalize_report_candidate_dates,
    now_text,
    recognition_type,
    safe_str,
    write_csv,
)


ALL_CANDIDATES = LATEST_DIR / "all_candidates_latest.csv"
OUTPUT_MD = LATEST_DIR / "revenue_industry_applicability_latest.md"
REVENUE_CATEGORIES = {"revenue_breakout_low_response", "revenue_pullback"}


def downgrade_priority(value: str) -> str:
    text = safe_str(value)
    if text.startswith("A_"):
        return "B_可等確認_營建認列型需基本面確認"
    if text.startswith("B_"):
        return text
    if not text:
        return "C_僅觀察_營建認列型需基本面確認"
    return text


def main() -> int:
    if not ALL_CANDIDATES.exists():
        raise FileNotFoundError(f"Missing {ALL_CANDIDATES}")

    df = pd.read_csv(ALL_CANDIDATES, dtype=str, keep_default_na=False)
    if df.empty:
        OUTPUT_MD.write_text("# 產業營收適用性檢查\n\n目前沒有候選股。\n", encoding="utf-8")
        return 0

    for col in ["is_construction_recognition", "recognition_type", "revenue_signal_type", "revenue_applicability_note"]:
        if col not in df.columns:
            df[col] = ""

    construction_mask = df.apply(is_construction_like, axis=1)
    revenue_mask = df["category"].isin(REVENUE_CATEGORIES) if "category" in df.columns else pd.Series(False, index=df.index)
    target_mask = construction_mask & revenue_mask

    df.loc[construction_mask, "is_construction_recognition"] = "True"
    df.loc[construction_mask, "recognition_type"] = df.loc[construction_mask].apply(recognition_type, axis=1)
    df.loc[construction_mask, "revenue_signal_type"] = "營建認列型 / 交屋認列型"
    df.loc[revenue_mask & ~construction_mask, "revenue_signal_type"] = "出貨型營收 / 其他"

    if target_mask.any():
        note = "月營收 YoY 屬認列型訊號，需 EPS、毛利率、合約負債、在建工程或交屋進度確認；不得只因單月 YoY 暴增列為最優先。"
        df.loc[target_mask, "revenue_applicability_note"] = df.loc[target_mask, "recognition_type"].astype(str) + "；" + note
        if "revaluation_priority" in df.columns:
            df.loc[target_mask, "revaluation_priority"] = df.loc[target_mask, "revaluation_priority"].map(downgrade_priority)
        if "priority" in df.columns:
            df.loc[target_mask, "priority"] = df.loc[target_mask, "priority"].map(downgrade_priority)
        if "note" in df.columns:
            df.loc[target_mask, "note"] = df.loc[target_mask, "note"].astype(str) + "；營建/交屋認列型營收需基本面確認"

    df = normalize_report_candidate_dates(df, main_price_date_from_freshness())
    write_csv(df, ALL_CANDIDATES)

    lines = [
        "# 產業營收適用性檢查",
        "",
        f"- generated_at: `{now_text()}`",
        f"- source: `{ALL_CANDIDATES.as_posix()}`",
        f"- construction_like_rows: `{int(construction_mask.sum())}`",
        f"- revenue_category_construction_rows: `{int(target_mask.sum())}`",
        "",
        "## 規則",
        "",
        "營建業、建材營造、不動產開發、工程承攬等認列型產業，月營收 YoY 不與電子、半導體、零組件等出貨型產業同權重比較。",
        "若進入營收爆發低反應股或營收成長股價回檔，預設降至可等確認或僅觀察，除非同時具備 TDCC、股價平台、EPS/毛利率與認列進度支持。",
        "",
        "## 受影響候選股",
        "",
    ]

    if target_mask.any():
        cols = ["date", "stock_id", "stock_name", "industry", "category", "revaluation_priority", "recognition_type", "revenue_applicability_note"]
        show = df.loc[target_mask, [col for col in cols if col in df.columns]].head(100)
        lines.append("| " + " | ".join(show.columns) + " |")
        lines.append("| " + " | ".join(["---"] * len(show.columns)) + " |")
        for _, row in show.iterrows():
            values = [safe_str(row.get(col, "")).replace("|", "/").replace("\n", " ") for col in show.columns]
            lines.append("| " + " | ".join(values) + " |")
    else:
        lines.append("本批次沒有營收分類中的營建/交屋認列型候選股。")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {ALL_CANDIDATES}")
    print(f"Saved: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
