from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd


LATEST_DIR = Path("output/latest")

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
ALL_CANDIDATES_MD = LATEST_DIR / "all_candidates_latest.md"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"

WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"

MERGE_STATUS_MD = LATEST_DIR / "warrant_flow_merge_latest.md"

WARRANT_COLUMNS = [
    "warrant_flow_signal",
    "warrant_flow_score",
    "warrant_flow_warning",
    "call_turnover",
    "put_turnover",
    "call_put_turnover_ratio",
    "call_turnover_change_1d",
    "call_turnover_change_5d",
    "low_float_call_spike_count",
    "top_issuer",
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

    text = "".join(ch for ch in text if ch.isdigit())

    return text.zfill(4) if text else ""


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path, dtype={"stock_id": str, "ticker": str, "code": str})
    except Exception:
        return pd.DataFrame()


def detect_stock_id_col(df: pd.DataFrame) -> str:
    for col in ["stock_id", "ticker", "code", "股票代號"]:
        if col in df.columns:
            return col

    return ""


def merge_warrant_flow() -> tuple[pd.DataFrame, str]:
    candidates = load_csv(ALL_CANDIDATES_CSV)

    if candidates.empty:
        return candidates, "all_candidates_latest.csv not found or empty. Skip merge."

    warrant = load_csv(WARRANT_FLOW_CSV)

    if warrant.empty:
        for col in WARRANT_COLUMNS:
            target_col = "warrant_note" if col == "note" else col

            if target_col not in candidates.columns:
                candidates[target_col] = pd.NA

        candidates.to_csv(ALL_CANDIDATES_CSV, index=False, encoding="utf-8-sig")
        write_excel_and_md(candidates)

        return candidates, "warrant_flow_latest.csv empty. Added empty warrant columns only."

    candidate_stock_col = detect_stock_id_col(candidates)

    if not candidate_stock_col:
        return candidates, "Cannot find stock_id column in all_candidates_latest.csv."

    candidates["_stock_id_for_merge"] = candidates[candidate_stock_col].map(normalize_code)
    warrant["stock_id"] = warrant["stock_id"].map(normalize_code)

    keep_cols = ["stock_id"] + [col for col in WARRANT_COLUMNS if col in warrant.columns]
    warrant_small = warrant[keep_cols].copy()
    warrant_small = warrant_small.rename(columns={"note": "warrant_note"})

    merged = candidates.merge(
        warrant_small,
        left_on="_stock_id_for_merge",
        right_on="stock_id",
        how="left",
        suffixes=("", "_warrant"),
    )

    if "stock_id_warrant" in merged.columns:
        merged = merged.drop(columns=["stock_id_warrant"])

    if "_stock_id_for_merge" in merged.columns:
        merged = merged.drop(columns=["_stock_id_for_merge"])

    merged.to_csv(ALL_CANDIDATES_CSV, index=False, encoding="utf-8-sig")
    write_excel_and_md(merged)

    matched = merged["warrant_flow_signal"].notna().sum() if "warrant_flow_signal" in merged.columns else 0

    return merged, f"Merged warrant flow into all candidates. rows={len(merged)}, matched_rows={matched}"


def write_excel_and_md(df: pd.DataFrame) -> None:
    try:
        with pd.ExcelWriter(ALL_CANDIDATES_XLSX, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all_candidates", index=False)

            if "category" in df.columns:
                summary = df.groupby(["category"], dropna=False).size().reset_index(name="count")
                summary.to_excel(writer, sheet_name="summary", index=False)

            if "warrant_flow_signal" in df.columns:
                warrant_summary = df.groupby(["warrant_flow_signal"], dropna=False).size().reset_index(name="count")
                warrant_summary.to_excel(writer, sheet_name="warrant_summary", index=False)
    except Exception as exc:
        print(f"Excel rewrite failed: {exc}")

    lines = []
    lines.append("# 完整候選股清單")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- CSV：`{ALL_CANDIDATES_CSV}`")
    lines.append(f"- Excel：`{ALL_CANDIDATES_XLSX}`")
    lines.append("")
    lines.append("## 權證欄位說明")
    lines.append("")
    lines.append("- `warrant_flow_signal`：標的股票層級權證金流訊號")
    lines.append("- `warrant_flow_score`：權證金流輔助分數，不直接改變原始入選條件")
    lines.append("- `warrant_flow_warning`：權證過熱、認售升溫、低流通量異常等警示")
    lines.append("")

    if df.empty:
        lines.append("目前沒有完整候選股資料。")
    else:
        display_cols = [
            "date",
            "category",
            "category_cn",
            "breakout_type",
            "stock_id",
            "stock_name",
            "industry",
            "score",
            "rank",
            "warrant_flow_signal",
            "warrant_flow_score",
            "warrant_flow_warning",
            "call_turnover",
            "put_turnover",
            "call_put_turnover_ratio",
            "call_turnover_change_1d",
            "call_turnover_change_5d",
            "low_float_call_spike_count",
            "top_issuer",
            "warrant_note",
            "chart_url",
            "note",
        ]

        display_cols = [col for col in display_cols if col in df.columns]

        if "category" in df.columns:
            categories = list(df["category"].dropna().astype(str).unique())
        else:
            categories = ["all"]

        for category in categories:
            part = df[df["category"].astype(str) == category].copy() if category != "all" else df.copy()

            lines.append(f"## {category}")
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

    ALL_CANDIDATES_MD.write_text("\n".join(lines), encoding="utf-8")


def append_stock_monitor_note(status: str) -> None:
    if not STOCK_MONITOR_MD.exists():
        return

    text = STOCK_MONITOR_MD.read_text(encoding="utf-8")

    marker = "\n## 權證金流輔助欄位\n"

    if marker in text:
        text = text.split(marker)[0].rstrip() + "\n"

    lines = []
    lines.append("")
    lines.append("## 權證金流輔助欄位")
    lines.append("")
    lines.append(f"- 更新時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 狀態：`{status}`")
    lines.append(f"- 權證金流檔案：`output/latest/warrant_flow_latest.csv`")
    lines.append("")
    lines.append("使用方式：")
    lines.append("- `true_breakout + call_strong_inflow`：突破動能加分，但仍需確認位階、TDCC、量能。")
    lines.append("- `range_rebound + call_inflow`：挑戰前高動能加分，但未突破前不可歸為嚴格突破。")
    lines.append("- `revenue_pullback + call_inflow`：回檔後資金試單，可提高觀察優先度。")
    lines.append("- `warrant_overheat / call_profit_exit_risk`：追高或獲利結清風險提高。")
    lines.append("- `put_inflow`：偏空或避險警訊，不直接否定，但降低追價意願。")
    lines.append("")

    STOCK_MONITOR_MD.write_text(text.rstrip() + "\n" + "\n".join(lines), encoding="utf-8")


def write_status(status: str) -> None:
    lines = []
    lines.append("# 權證金流合併狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 狀態：`{status}`")
    lines.append(f"- 候選股檔案：`{ALL_CANDIDATES_CSV}`")
    lines.append(f"- 權證金流檔案：`{WARRANT_FLOW_CSV}`")
    lines.append("")

    MERGE_STATUS_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    df, status = merge_warrant_flow()
    append_stock_monitor_note(status)
    write_status(status)

    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
