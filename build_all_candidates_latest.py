from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re

import pandas as pd


LATEST_DIR = Path("output/latest")

BREAKOUT_CSV = LATEST_DIR / "breakout_latest.csv"
RANGE_REBOUND_CSV = LATEST_DIR / "range_rebound_watch_latest.csv"
REVENUE_PULLBACK_CSV = LATEST_DIR / "revenue_pullback_latest.csv"
PULLBACK_REBOUND_CSV = LATEST_DIR / "pullback_rebound_latest.csv"
CHART_MANIFEST_CSV = LATEST_DIR / "chart_manifest.csv"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"

OUTPUT_CSV = LATEST_DIR / "all_candidates_latest.csv"
OUTPUT_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
OUTPUT_MD = LATEST_DIR / "all_candidates_latest.md"

CATEGORY_ORDER = {
    "true_breakout": 1,
    "range_rebound": 2,
    "revenue_pullback": 3,
    "pullback_rebound": 4,
    "pattern": 5,
}

OUTPUT_COLUMNS = [
    "date",
    "category",
    "breakout_type",
    "stock_id",
    "stock_name",
    "industry",
    "score",
    "rank",
    "close",
    "volume",
    "volume_ratio",
    "ma20",
    "ma60",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "previous_high",
    "previous_40d_high",
    "previous_60d_high",
    "distance_to_previous_high_pct",
    "distance_to_previous_40d_high_pct",
    "distance_to_previous_60d_high_pct",
    "available_days",
    "price_data_warning",
    "tdcc_date",
    "holder_400_pct",
    "holder_400_change",
    "holder_1000_pct",
    "holder_1000_change",
    "tdcc_judgement",
    "chart_path",
    "chart_url",
    "note",
]


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    text = re.sub(r"[^0-9]", "", text)
    return text.zfill(4) if text else ""


def normalize_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def to_number(value):
    if pd.isna(value):
        return pd.NA
    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("--", "")
    text = text.replace("+", "")
    text = text.replace(" ", "")
    if text == "":
        return pd.NA
    return pd.to_numeric(text, errors="coerce")


def read_csv_safe(path: Path) -> pd.DataFrame:
    if not path.exists():
        print(f"Missing file: {path}")
        return pd.DataFrame()

    try:
        return pd.read_csv(path, dtype={"ticker": str, "code": str, "stock_id": str})
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def pick_column(df: pd.DataFrame, candidates: list[str], default=""):
    for col in candidates:
        if col in df.columns:
            return df[col]
    return default


def standardize_candidates(df: pd.DataFrame, category: str, default_breakout_type: str) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    result = pd.DataFrame()
    result["_source_order"] = range(len(df))

    result["date"] = pick_column(df, ["date", "資料日期"], "")
    result["category"] = category
    result["breakout_type"] = pick_column(df, ["breakout_type"], default_breakout_type)

    result["stock_id"] = pick_column(df, ["stock_id", "ticker", "code", "股票代號"], "").map(normalize_code)
    result["stock_name"] = pick_column(df, ["stock_name", "name", "company_name", "股票名稱"], "").map(normalize_text)

    result["industry"] = pick_column(df, ["industry", "產業別"], "")

    result["score"] = pick_column(df, ["score", "分數"], pd.NA)
    result["rank"] = pick_column(df, ["rank", "排行"], pd.NA)

    result["close"] = pick_column(df, ["close", "收盤價"], pd.NA)
    result["volume"] = pick_column(df, ["volume", "volume_lots", "成交量"], pd.NA)

    result["volume_ratio"] = pick_column(df, ["volume_ratio", "volume_ratio_20", "量比"], pd.NA)

    result["ma20"] = pick_column(df, ["ma20", "20MA"], pd.NA)
    result["ma60"] = pick_column(df, ["ma60", "60MA"], pd.NA)

    result["distance_to_ma20_pct"] = pick_column(df, ["distance_to_ma20_pct", "gap_ma20_pct"], pd.NA)
    result["distance_to_ma60_pct"] = pick_column(df, ["distance_to_ma60_pct", "gap_ma60_pct"], pd.NA)

    result["previous_high"] = pick_column(df, ["previous_high", "high_40", "previous_60d_high"], pd.NA)
    result["previous_40d_high"] = pick_column(df, ["previous_40d_high", "high_40"], pd.NA)
    result["previous_60d_high"] = pick_column(df, ["previous_60d_high"], pd.NA)

    result["distance_to_previous_high_pct"] = pick_column(
        df,
        ["distance_to_previous_high_pct", "distance_to_previous_60d_high_pct", "breakout_pct"],
        pd.NA,
    )
    result["distance_to_previous_40d_high_pct"] = pick_column(df, ["distance_to_previous_40d_high_pct"], pd.NA)
    result["distance_to_previous_60d_high_pct"] = pick_column(df, ["distance_to_previous_60d_high_pct"], pd.NA)

    result["available_days"] = pick_column(df, ["available_days"], pd.NA)
    result["price_data_warning"] = pick_column(df, ["price_data_warning"], "")

    result["tdcc_date"] = pick_column(df, ["tdcc_date", "TDCC日"], "")
    result["holder_400_pct"] = pick_column(df, ["holder_400_pct", "400張以上%", "over_400_pct"], pd.NA)
    result["holder_400_change"] = pick_column(df, ["holder_400_change", "400張變化", "over_400_change"], pd.NA)
    result["holder_1000_pct"] = pick_column(df, ["holder_1000_pct", "1000張以上%", "over_1000_pct"], pd.NA)
    result["holder_1000_change"] = pick_column(df, ["holder_1000_change", "1000張變化", "over_1000_change"], pd.NA)
    result["tdcc_judgement"] = pick_column(df, ["tdcc_judgement", "TDCC判斷"], "")

    result["chart_path"] = pick_column(df, ["chart_path"], "")
    result["chart_url"] = pick_column(df, ["chart_url"], "")
    result["note"] = pick_column(df, ["note", "備註"], "")

    result = result[result["stock_id"].astype(str).str.match(r"^[0-9]{4}$", na=False)].copy()

    for col in [
        "score",
        "rank",
        "close",
        "volume",
        "volume_ratio",
        "ma20",
        "ma60",
        "distance_to_ma20_pct",
        "distance_to_ma60_pct",
        "previous_high",
        "previous_40d_high",
        "previous_60d_high",
        "distance_to_previous_high_pct",
        "distance_to_previous_40d_high_pct",
        "distance_to_previous_60d_high_pct",
        "available_days",
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
    ]:
        result[col] = result[col].map(to_number)

    return result


def load_chart_manifest() -> pd.DataFrame:
    df = read_csv_safe(CHART_MANIFEST_CSV)

    if df.empty:
        return pd.DataFrame()

    if "stock_id" not in df.columns:
        if "ticker" in df.columns:
            df = df.rename(columns={"ticker": "stock_id"})
        elif "code" in df.columns:
            df = df.rename(columns={"code": "stock_id"})

    if "stock_name" not in df.columns:
        if "name" in df.columns:
            df = df.rename(columns={"name": "stock_name"})
        else:
            df["stock_name"] = ""

    if "category" not in df.columns:
        df["category"] = ""

    if "breakout_type" not in df.columns:
        df["breakout_type"] = df["category"]

    df["stock_id"] = df["stock_id"].map(normalize_code)
    df["stock_name"] = df["stock_name"].map(normalize_text)
    df["category"] = df["category"].map(normalize_text)
    df["breakout_type"] = df["breakout_type"].map(normalize_text)

    return df


def merge_chart_manifest(candidates: pd.DataFrame, chart_manifest: pd.DataFrame) -> pd.DataFrame:
    if candidates.empty:
        return candidates

    if chart_manifest.empty:
        return candidates

    manifest_cols = [
        "stock_id",
        "category",
        "breakout_type",
        "available_days",
        "price_data_warning",
        "chart_path",
        "chart_url",
        "previous_40d_high",
        "previous_60d_high",
        "distance_to_previous_40d_high_pct",
        "distance_to_previous_60d_high_pct",
        "note",
    ]

    manifest_cols = [col for col in manifest_cols if col in chart_manifest.columns]
    manifest = chart_manifest[manifest_cols].copy()

    merge_keys = ["stock_id", "category", "breakout_type"]
    merge_keys = [key for key in merge_keys if key in manifest.columns and key in candidates.columns]

    if len(merge_keys) < 2:
        return candidates

    merged = candidates.merge(
        manifest,
        on=merge_keys,
        how="left",
        suffixes=("", "_chart"),
    )

    for col in [
        "available_days",
        "price_data_warning",
        "chart_path",
        "chart_url",
        "previous_40d_high",
        "previous_60d_high",
        "distance_to_previous_40d_high_pct",
        "distance_to_previous_60d_high_pct",
        "note",
    ]:
        chart_col = f"{col}_chart"

        if chart_col in merged.columns:
            if col in merged.columns:
                merged[col] = merged[col].combine_first(merged[chart_col])
            else:
                merged[col] = merged[chart_col]

            merged = merged.drop(columns=[chart_col])

    return merged


def load_pattern_from_chart_manifest(chart_manifest: pd.DataFrame) -> pd.DataFrame:
    if chart_manifest.empty:
        return pd.DataFrame()

    pattern = chart_manifest[chart_manifest["category"] == "pattern"].copy()

    if pattern.empty:
        return pd.DataFrame()

    pattern["score"] = pd.NA
    pattern["rank"] = pd.NA
    pattern["industry"] = ""
    pattern["volume"] = pd.NA
    pattern["volume_ratio"] = pd.NA
    pattern["ma20"] = pd.NA
    pattern["ma60"] = pd.NA
    pattern["distance_to_ma20_pct"] = pd.NA
    pattern["distance_to_ma60_pct"] = pd.NA
    pattern["previous_high"] = pattern.get("previous_60d_high", pd.NA)
    pattern["distance_to_previous_high_pct"] = pattern.get("distance_to_previous_60d_high_pct", pd.NA)
    pattern["tdcc_date"] = ""
    pattern["holder_400_pct"] = pd.NA
    pattern["holder_400_change"] = pd.NA
    pattern["holder_1000_pct"] = pd.NA
    pattern["holder_1000_change"] = pd.NA
    pattern["tdcc_judgement"] = ""
    pattern["_source_order"] = range(len(pattern))

    for col in OUTPUT_COLUMNS:
        if col not in pattern.columns:
            pattern[col] = ""

    return pattern[OUTPUT_COLUMNS + ["_source_order"]].copy()


def build_all_candidates_latest() -> pd.DataFrame:
    chart_manifest = load_chart_manifest()

    frames = []

    breakout_df = standardize_candidates(
        read_csv_safe(BREAKOUT_CSV),
        category="true_breakout",
        default_breakout_type="true_breakout",
    )
    if not breakout_df.empty:
        breakout_df = breakout_df[breakout_df["breakout_type"].fillna("") == "true_breakout"].copy()
        frames.append(breakout_df)

    range_df = standardize_candidates(
        read_csv_safe(RANGE_REBOUND_CSV),
        category="range_rebound",
        default_breakout_type="range_rebound",
    )
    if not range_df.empty:
        range_df = range_df[
            range_df["breakout_type"].isin(["range_rebound", "near_resistance", "abnormal_volume_up"])
        ].copy()
        frames.append(range_df)

    revenue_df = standardize_candidates(
        read_csv_safe(REVENUE_PULLBACK_CSV),
        category="revenue_pullback",
        default_breakout_type="revenue_pullback",
    )
    if not revenue_df.empty:
        frames.append(revenue_df)

    rebound_df = standardize_candidates(
        read_csv_safe(PULLBACK_REBOUND_CSV),
        category="pullback_rebound",
        default_breakout_type="pullback_rebound",
    )
    if not rebound_df.empty:
        frames.append(rebound_df)

    pattern_df = load_pattern_from_chart_manifest(chart_manifest)
    if not pattern_df.empty:
        frames.append(pattern_df)

    if not frames:
        empty = pd.DataFrame(columns=OUTPUT_COLUMNS)
        return empty

    all_candidates = pd.concat(frames, ignore_index=True)

    all_candidates = merge_chart_manifest(all_candidates, chart_manifest)

    for col in OUTPUT_COLUMNS:
        if col not in all_candidates.columns:
            all_candidates[col] = pd.NA

    all_candidates["_category_order"] = all_candidates["category"].map(CATEGORY_ORDER).fillna(99)

    all_candidates["score_sort"] = pd.to_numeric(all_candidates["score"], errors="coerce")
    all_candidates["rank_sort"] = pd.to_numeric(all_candidates["rank"], errors="coerce")

    all_candidates = all_candidates.sort_values(
        ["_category_order", "score_sort", "rank_sort", "_source_order"],
        ascending=[True, False, True, True],
        na_position="last",
    ).reset_index(drop=True)

    all_candidates = all_candidates[OUTPUT_COLUMNS].copy()

    return all_candidates


def write_markdown_report(df: pd.DataFrame) -> None:
    lines = []
    lines.append("# 完整候選股清單")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- CSV：`{OUTPUT_CSV}`")
    lines.append(f"- Excel：`{OUTPUT_XLSX}`")
    lines.append(f"- Markdown：`{OUTPUT_MD}`")
    lines.append("")
    lines.append("## 統計摘要")
    lines.append("")

    if df.empty:
        lines.append("目前沒有完整候選股資料。")
    else:
        summary = df.groupby("category").size().reset_index(name="count")
        lines.append("| category | count |")
        lines.append("|---|---:|")

        for _, row in summary.iterrows():
            lines.append(f"| {row['category']} | {row['count']} |")

        lines.append("")
        lines.append("## 各分類完整名單")
        lines.append("")

        display_cols = [
            "date",
            "category",
            "breakout_type",
            "stock_id",
            "stock_name",
            "industry",
            "score",
            "rank",
            "close",
            "volume_ratio",
            "previous_60d_high",
            "distance_to_previous_60d_high_pct",
            "available_days",
            "price_data_warning",
            "tdcc_judgement",
            "chart_path",
            "note",
        ]

        for category in sorted(df["category"].dropna().unique(), key=lambda x: CATEGORY_ORDER.get(x, 99)):
            part = df[df["category"] == category].copy()

            lines.append(f"### {category}")
            lines.append("")
            lines.append("| " + " | ".join(display_cols) + " |")
            lines.append("| " + " | ".join(["---"] * len(display_cols)) + " |")

            for _, row in part.iterrows():
                values = []
                for col in display_cols:
                    value = row.get(col, "")
                    if pd.isna(value):
                        value = ""
                    values.append(str(value))
                lines.append("| " + " | ".join(values) + " |")

            lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_excel(df: pd.DataFrame) -> None:
    try:
        with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all_candidates", index=False)

            if not df.empty:
                summary = df.groupby("category").size().reset_index(name="count")
                summary.to_excel(writer, sheet_name="summary", index=False)

                for category in sorted(df["category"].dropna().unique(), key=lambda x: CATEGORY_ORDER.get(x, 99)):
                    sheet_name = str(category)[:31]
                    df[df["category"] == category].to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"Excel saved: {OUTPUT_XLSX}")
    except Exception as exc:
        print(f"Excel output failed: {exc}")


def update_stock_monitor_note(df: pd.DataFrame) -> None:
    if not STOCK_MONITOR_MD.exists():
        return

    text = STOCK_MONITOR_MD.read_text(encoding="utf-8")

    marker = "\n## 完整候選股清單\n"

    if marker in text:
        text = text.split(marker)[0].rstrip() + "\n"

    total_count = len(df)
    category_counts = {}

    if not df.empty:
        category_counts = df.groupby("category").size().to_dict()

    lines = []
    lines.append("")
    lines.append("## 完整候選股清單")
    lines.append("")
    lines.append("本報告上方仍為精華版觀察清單；完整合格名單已另外輸出，方便回測、比對與分享。")
    lines.append("")
    lines.append(f"- 總筆數：`{total_count}`")
    lines.append(f"- CSV：`output/latest/all_candidates_latest.csv`")
    lines.append(f"- Excel：`output/latest/all_candidates_latest.xlsx`")
    lines.append(f"- Markdown：`output/latest/all_candidates_latest.md`")
    lines.append("")

    if category_counts:
        lines.append("| category | count |")
        lines.append("|---|---:|")

        for category in sorted(category_counts.keys(), key=lambda x: CATEGORY_ORDER.get(x, 99)):
            lines.append(f"| {category} | {category_counts[category]} |")

        lines.append("")

    lines.append("說明：")
    lines.append("- `true_breakout` 只代表真正嚴格突破股。")
    lines.append("- `range_rebound` 代表區間內轉強 / 挑戰前高觀察，不可混入嚴格突破股。")
    lines.append("- `price_data_warning != ok` 的圖表或資料需標註資料品質警示。")
    lines.append("")

    STOCK_MONITOR_MD.write_text(text.rstrip() + "\n" + "\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    df = build_all_candidates_latest()

    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"CSV saved: {OUTPUT_CSV}")

    write_excel(df)
    write_markdown_report(df)
    update_stock_monitor_note(df)

    print(f"Markdown saved: {OUTPUT_MD}")
    print(f"Rows: {len(df)}")

    if not df.empty:
        print(df.groupby("category").size())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
