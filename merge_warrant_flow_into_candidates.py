from __future__ import annotations

from pathlib import Path
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent / "scripts"))

from tracking_utils import main_price_date_from_freshness, normalize_report_candidate_dates  # noqa: E402


LATEST_DIR = Path("output/latest")

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
ALL_CANDIDATES_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
ALL_CANDIDATES_MD = LATEST_DIR / "all_candidates_latest.md"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"

WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
MERGE_STATUS_MD = LATEST_DIR / "warrant_flow_merge_latest.md"


# 從 warrant_flow_latest.csv 合併到 all_candidates_latest.csv 的欄位
WARRANT_SOURCE_COLUMNS = [
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

# 合併後在候選股檔案裡呈現的欄位
WARRANT_OUTPUT_COLUMNS = [
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
]

# 舊版可能已經寫進 all_candidates_latest.csv 的欄位，重跑前先移除，避免 merge duplicate columns
OLD_WARRANT_COLUMNS_TO_DROP = [
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

    # Pandas merge 失敗前或舊版殘留可能出現的欄位
    "warrant_flow_signal_warrant",
    "warrant_flow_score_warrant",
    "warrant_flow_warning_warrant",
    "call_turnover_warrant",
    "put_turnover_warrant",
    "call_put_turnover_ratio_warrant",
    "call_turnover_change_1d_warrant",
    "call_turnover_change_5d_warrant",
    "low_float_call_spike_count_warrant",
    "top_issuer_warrant",
    "warrant_note_warrant",
    "note_warrant",
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
        return pd.read_csv(
            path,
            dtype={
                "stock_id": str,
                "ticker": str,
                "code": str,
                "股票代號": str,
            },
        )
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def load_candidate_csv(path: Path) -> pd.DataFrame:
    """Load the published candidate table without coercing non-warrant text."""
    if not path.exists():
        return pd.DataFrame()

    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def detect_stock_id_col(df: pd.DataFrame) -> str:
    for col in ["stock_id", "ticker", "code", "股票代號"]:
        if col in df.columns:
            return col

    return ""


def remove_old_warrant_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    cols_to_drop = [col for col in OLD_WARRANT_COLUMNS_TO_DROP if col in df.columns]

    if cols_to_drop:
        df = df.drop(columns=cols_to_drop)

    # 保險：任何意外殘留的 _warrant 欄位都移除
    suffix_cols = [col for col in df.columns if str(col).endswith("_warrant")]

    if suffix_cols:
        df = df.drop(columns=suffix_cols)

    return df


def restore_candidate_column_order(
    df: pd.DataFrame,
    original_columns: list[str],
) -> pd.DataFrame:
    """Preserve the published candidate schema while allowing new columns at the end."""
    preserved_columns = [column for column in original_columns if column in df.columns]
    appended_columns = [column for column in df.columns if column not in original_columns]
    return df.reindex(columns=[*preserved_columns, *appended_columns])


def prepare_warrant_flow(warrant: pd.DataFrame) -> pd.DataFrame:
    if warrant.empty:
        return pd.DataFrame(columns=["stock_id"] + WARRANT_OUTPUT_COLUMNS)

    warrant = warrant.copy()

    if "stock_id" not in warrant.columns:
        return pd.DataFrame(columns=["stock_id"] + WARRANT_OUTPUT_COLUMNS)

    warrant["stock_id"] = warrant["stock_id"].map(normalize_code)

    keep_cols = ["stock_id"] + [col for col in WARRANT_SOURCE_COLUMNS if col in warrant.columns]
    warrant_small = warrant[keep_cols].copy()

    if "note" in warrant_small.columns:
        warrant_small = warrant_small.rename(columns={"note": "warrant_note"})

    for col in WARRANT_OUTPUT_COLUMNS:
        if col not in warrant_small.columns:
            warrant_small[col] = pd.NA

    warrant_small = warrant_small[["stock_id"] + WARRANT_OUTPUT_COLUMNS].copy()

    # 同一股票理論上只會一筆，但保險起見：
    # 以 warrant_flow_score 高、call_turnover 大的那筆為準
    sort_cols = []
    ascending = []

    if "warrant_flow_score" in warrant_small.columns:
        warrant_small["warrant_flow_score"] = pd.to_numeric(
            warrant_small["warrant_flow_score"],
            errors="coerce",
        )
        sort_cols.append("warrant_flow_score")
        ascending.append(False)

    if "call_turnover" in warrant_small.columns:
        warrant_small["call_turnover"] = pd.to_numeric(
            warrant_small["call_turnover"],
            errors="coerce",
        )
        sort_cols.append("call_turnover")
        ascending.append(False)

    if sort_cols:
        warrant_small = warrant_small.sort_values(sort_cols, ascending=ascending)

    warrant_small = warrant_small.drop_duplicates(subset=["stock_id"], keep="first")

    return warrant_small


def merge_warrant_flow() -> tuple[pd.DataFrame, str]:
    candidates = load_candidate_csv(ALL_CANDIDATES_CSV)

    if candidates.empty:
        return candidates, "all_candidates_latest.csv not found or empty. Skip merge."

    candidate_stock_col = detect_stock_id_col(candidates)

    if not candidate_stock_col:
        return candidates, "Cannot find stock_id column in all_candidates_latest.csv."

    original_candidate_columns = list(candidates.columns)

    # 重點：先移除舊權證欄位，避免重跑 workflow 時 duplicate columns
    candidates = remove_old_warrant_columns(candidates)

    candidates["_stock_id_for_merge"] = candidates[candidate_stock_col].map(normalize_code)

    warrant = load_csv(WARRANT_FLOW_CSV)

    if warrant.empty:
        for col in WARRANT_OUTPUT_COLUMNS:
            candidates[col] = pd.NA

        if "_stock_id_for_merge" in candidates.columns:
            candidates = candidates.drop(columns=["_stock_id_for_merge"])

        candidates = normalize_report_candidate_dates(candidates, main_price_date_from_freshness())
        candidates = restore_candidate_column_order(candidates, original_candidate_columns)
        candidates.to_csv(ALL_CANDIDATES_CSV, index=False, encoding="utf-8-sig")
        write_excel_and_md(candidates)

        return candidates, "warrant_flow_latest.csv empty. Added empty warrant columns only."

    warrant_small = prepare_warrant_flow(warrant)

    if warrant_small.empty:
        for col in WARRANT_OUTPUT_COLUMNS:
            candidates[col] = pd.NA

        if "_stock_id_for_merge" in candidates.columns:
            candidates = candidates.drop(columns=["_stock_id_for_merge"])

        candidates = normalize_report_candidate_dates(candidates, main_price_date_from_freshness())
        candidates = restore_candidate_column_order(candidates, original_candidate_columns)
        candidates.to_csv(ALL_CANDIDATES_CSV, index=False, encoding="utf-8-sig")
        write_excel_and_md(candidates)

        return candidates, "warrant_flow_latest.csv has no usable stock_id rows. Added empty warrant columns only."

    merged = candidates.merge(
        warrant_small,
        left_on="_stock_id_for_merge",
        right_on="stock_id",
        how="left",
        suffixes=("", "_from_warrant"),
    )

    # 若原本候選股主欄位就是 stock_id，merge 會產生 stock_id_from_warrant，刪掉右側版本
    if "stock_id_from_warrant" in merged.columns:
        merged = merged.drop(columns=["stock_id_from_warrant"])

    if "_stock_id_for_merge" in merged.columns:
        merged = merged.drop(columns=["_stock_id_for_merge"])

    # 再保險一次：移除任何意外 suffix 欄位
    suffix_cols = [col for col in merged.columns if str(col).endswith("_from_warrant")]

    if suffix_cols:
        merged = merged.drop(columns=suffix_cols)

    merged = normalize_report_candidate_dates(merged, main_price_date_from_freshness())
    merged = restore_candidate_column_order(merged, original_candidate_columns)
    merged.to_csv(ALL_CANDIDATES_CSV, index=False, encoding="utf-8-sig")
    write_excel_and_md(merged)

    matched = 0

    if "warrant_flow_signal" in merged.columns:
        matched = int(merged["warrant_flow_signal"].notna().sum())

    return merged, f"Merged warrant flow into all candidates. rows={len(merged)}, matched_rows={matched}"


def write_excel_and_md(df: pd.DataFrame) -> None:
    try:
        with pd.ExcelWriter(ALL_CANDIDATES_XLSX, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all_candidates", index=False)

            if "category" in df.columns:
                summary = (
                    df.groupby(["category"], dropna=False)
                    .size()
                    .reset_index(name="count")
                )
                summary.to_excel(writer, sheet_name="summary", index=False)

            if "warrant_flow_signal" in df.columns:
                warrant_summary = (
                    df.groupby(["warrant_flow_signal"], dropna=False)
                    .size()
                    .reset_index(name="count")
                )
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
            "細分族群",
            "theme_group",
            "revaluation_priority",
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
            if category != "all":
                part = df[df["category"].astype(str) == category].copy()
            else:
                part = df.copy()

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

                    value = str(value).replace("|", "/").replace("\n", " ")
                    values.append(value)

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
    lines.append("- `高位 true_breakout + warrant_overheat / call_profit_exit_risk`：追高或獲利結清風險提高。")
    lines.append("- `put_inflow`：偏空或避險警訊，不直接否定，但降低追價意願。")
    lines.append("")

    STOCK_MONITOR_MD.write_text(
        text.rstrip() + "\n" + "\n".join(lines),
        encoding="utf-8",
    )


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
