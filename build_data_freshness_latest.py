from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re
import json

import pandas as pd


LATEST_DIR = Path("output/latest")

STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"
OFFICIAL_PRICE_FETCH_MD = LATEST_DIR / "official_price_fetch_latest.md"
OFFICIAL_PRICE_FETCH_JSON = LATEST_DIR / "official_price_fetch_latest.json"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"

OUTPUT_MD = LATEST_DIR / "data_freshness_latest.md"
OUTPUT_CSV = LATEST_DIR / "data_freshness_latest.csv"


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def normalize_date(value) -> str:
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass

    text = str(value).strip()
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for encoding in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=encoding)
        except Exception:
            continue

    return ""


def extract_first_date_by_patterns(text: str, patterns: list[str]) -> str:
    if not text:
        return ""

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            date = normalize_date(match.group(1))
            if date:
                return date

    return ""


def extract_stock_monitor_price_date() -> str:
    text = read_text(STOCK_MONITOR_MD)

    patterns = [
        r"最新官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"最新價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"資料日期[：:\s`]*([0-9/\-]{8,10})",
        r"主資料日期[：:\s`]*([0-9/\-]{8,10})",
    ]

    return extract_first_date_by_patterns(text, patterns)


def extract_official_price_fetch_date() -> str:
    # 新版 fetch_official_daily_price.py 會輸出 JSON，優先讀 saved_price_date。
    if OFFICIAL_PRICE_FETCH_JSON.exists():
        try:
            data = json.loads(OFFICIAL_PRICE_FETCH_JSON.read_text(encoding="utf-8"))
            saved = normalize_date(data.get("saved_price_date", ""))
            if saved:
                return saved
        except Exception:
            pass

    text = read_text(OFFICIAL_PRICE_FETCH_MD)

    # 注意：必須優先抓 saved_price_date，不要先抓 target_date。
    patterns = [
        r"saved_price_date[：:\s`]*([0-9/\-]{8,10})",
        r"官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"最新官方價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"最新價格資料日[：:\s`]*([0-9/\-]{8,10})",
        r"資料日期[：:\s`]*([0-9/\-]{8,10})",
    ]

    return extract_first_date_by_patterns(text, patterns)


def extract_csv_max_date(path: Path) -> str:
    if not path.exists():
        return ""

    try:
        df = pd.read_csv(path, dtype=str)
    except Exception:
        return ""

    if df.empty:
        return ""

    date_col = ""

    for col in ["date", "資料日期", "trade_date", "main_price_date"]:
        if col in df.columns:
            date_col = col
            break

    if not date_col:
        return ""

    dates = df[date_col].map(normalize_date)
    dates = dates[dates.astype(str).str.len() == 8]

    if dates.empty:
        return ""

    return str(dates.max())


def determine_main_price_date(
    stock_monitor_date: str,
    all_candidates_date: str,
    official_fetch_date: str,
) -> str:
    # 正式每日報告現在主要靠 all_candidates_latest.csv。
    # stock_monitor_latest.md 可以是舊版主監測文字，不再讓它主導 main date。
    for date in [all_candidates_date, official_fetch_date, stock_monitor_date]:
        if date:
            return date

    return ""


def determine_report_ready(
    main_price_date: str,
    stock_monitor_date: str,
    all_candidates_date: str,
    official_fetch_date: str,
) -> tuple[bool, str]:
    if not main_price_date:
        return False, "無法判斷主資料日期"

    if all_candidates_date == main_price_date and official_fetch_date == main_price_date:
        if stock_monitor_date and stock_monitor_date != main_price_date:
            return (
                True,
                "完整候選清單與官方價格資料日期一致，可以產出正式每日報告；stock_monitor_latest.md 日期較舊，僅列為警告，不阻止報告產出",
            )

        return (
            True,
            "完整候選清單與官方價格資料日期一致，可以產出正式每日報告",
        )

    if all_candidates_date == main_price_date and not official_fetch_date:
        return (
            True,
            "完整候選清單已更新，官方價格抓取狀態檔日期缺失；可產出報告但需標示價格狀態檔缺失",
        )

    if official_fetch_date == main_price_date and not all_candidates_date:
        return (
            False,
            "官方價格資料已更新，但完整候選清單尚未產生，暫不產出正式每日報告",
        )

    if stock_monitor_date == main_price_date and all_candidates_date == main_price_date:
        return (
            True,
            "主監測報告與完整候選清單日期一致，可以產出正式每日報告",
        )

    return (
        False,
        "完整候選清單與官方價格資料日期不一致，暫不建議產出正式每日報告",
    )


def build_status() -> pd.DataFrame:
    stock_monitor_date = extract_stock_monitor_price_date()
    official_fetch_date = extract_official_price_fetch_date()
    all_candidates_date = extract_csv_max_date(ALL_CANDIDATES_CSV)
    warrant_flow_date = extract_csv_max_date(WARRANT_FLOW_CSV)

    main_price_date = determine_main_price_date(
        stock_monitor_date=stock_monitor_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
    )

    report_ready, report_ready_note = determine_report_ready(
        main_price_date=main_price_date,
        stock_monitor_date=stock_monitor_date,
        all_candidates_date=all_candidates_date,
        official_fetch_date=official_fetch_date,
    )

    official_fetch_note = ""

    if official_fetch_date and main_price_date and official_fetch_date < main_price_date:
        official_fetch_note = "official_price_fetch_latest.md 較舊，但主候選清單已更新；不可單獨用此檔判斷今日未更新"
    elif official_fetch_date == main_price_date:
        official_fetch_note = "official_price_fetch_latest.md 與主資料日期一致"
    elif not official_fetch_date:
        official_fetch_note = "official_price_fetch_latest.md 無法解析日期"
    else:
        official_fetch_note = "official_price_fetch_latest.md 日期高於或不同於主資料日期，請檢查流程順序"

    stock_monitor_note = ""

    if stock_monitor_date and main_price_date and stock_monitor_date < main_price_date:
        stock_monitor_note = "stock_monitor_latest.md 日期較舊；目前正式報告以 all_candidates_latest.csv 為主，僅列為警告"
    elif stock_monitor_date == main_price_date:
        stock_monitor_note = "stock_monitor_latest.md 與主資料日期一致"
    elif not stock_monitor_date:
        stock_monitor_note = "stock_monitor_latest.md 無法解析日期"
    else:
        stock_monitor_note = "stock_monitor_latest.md 日期高於或不同於主資料日期，請檢查"

    warrant_note = ""

    if warrant_flow_date and main_price_date and warrant_flow_date < main_price_date:
        warrant_note = "權證資料日期落後主價格資料；權證僅作輔助欄位，不應阻止主報告產出"
    elif warrant_flow_date == main_price_date:
        warrant_note = "權證資料與主價格資料日期一致"
    elif not warrant_flow_date:
        warrant_note = "權證資料無法解析日期或尚未產生"
    else:
        warrant_note = "權證資料日期高於或不同於主資料日期，請檢查"

    row = {
        "generated_at": now_taipei(),
        "main_price_date": main_price_date,
        "stock_monitor_price_date": stock_monitor_date,
        "all_candidates_date": all_candidates_date,
        "official_price_fetch_date": official_fetch_date,
        "warrant_flow_date": warrant_flow_date,
        "report_ready": report_ready,
        "report_ready_note": report_ready_note,
        "stock_monitor_note": stock_monitor_note,
        "official_fetch_note": official_fetch_note,
        "warrant_note": warrant_note,
    }

    return pd.DataFrame([row])


def write_markdown(df: pd.DataFrame) -> None:
    row = df.iloc[0].to_dict()

    lines = []

    lines.append("# 每日資料新鮮度狀態")
    lines.append("")
    lines.append(f"- 產生時間：`{row.get('generated_at', '')} Asia/Taipei`")
    lines.append(f"- 主資料日期：`{row.get('main_price_date', '')}`")
    lines.append(f"- 是否可產出正式每日報告：`{row.get('report_ready', '')}`")
    lines.append(f"- 判斷說明：{row.get('report_ready_note', '')}")
    lines.append("")
    lines.append("## 各檔案日期")
    lines.append("")
    lines.append("| 檔案 | 日期 | 說明 |")
    lines.append("|---|---:|---|")
    lines.append(f"| all_candidates_latest.csv | {row.get('all_candidates_date', '')} | 完整候選股清單日期，正式報告主資料來源 |")
    lines.append(f"| official_price_fetch_latest.md/json | {row.get('official_price_fetch_date', '')} | 官方價格抓取狀態檔日期 |")
    lines.append(f"| stock_monitor_latest.md | {row.get('stock_monitor_price_date', '')} | 舊版主監測報告日期，若落後只列警告 |")
    lines.append(f"| warrant_flow_latest.csv | {row.get('warrant_flow_date', '')} | 權證輔助資料日期 |")
    lines.append("")
    lines.append("## 判斷規則")
    lines.append("")
    lines.append("1. 每日全市場候選股報告以 `all_candidates_latest.csv` 作為主要資料來源。")
    lines.append("2. `official_price_fetch_latest.json/md` 用來確認官方價格資料是否已更新。")
    lines.append("3. `stock_monitor_latest.md` 若落後主資料日期，只列為警告，不阻止正式每日報告產出。")
    lines.append("4. `warrant_flow_latest.csv` 是權證輔助資料，日期可作為輔助檢查，不應單獨阻止主報告產出。")
    lines.append("")
    lines.append("## 補充說明")
    lines.append("")
    lines.append(f"- all candidates：主資料來源日期為 `{row.get('all_candidates_date', '')}`")
    lines.append(f"- official price fetch：{row.get('official_fetch_note', '')}")
    lines.append(f"- stock monitor：{row.get('stock_monitor_note', '')}")
    lines.append(f"- warrant flow：{row.get('warrant_note', '')}")
    lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    df = build_status()

    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    write_markdown(df)

    print(f"Saved: {OUTPUT_CSV}")
    print(f"Saved: {OUTPUT_MD}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
