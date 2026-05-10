import io
import re
from pathlib import Path
from typing import Optional

import pandas as pd
import requests


TDCC_URL = "https://smart.tdcc.com.tw/opendata/getOD.ashx?id=1-5"
TWSE_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
TPEx_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"

OUTPUT_DIR = Path("output")
HISTORY_DIR = OUTPUT_DIR / "history"
README_PATH = Path("README.md")

THRESHOLDS = [400, 600, 800, 1000]

COLUMN_ALIASES = {
    "資料日期": "date",
    "日期": "date",
    "證券代號": "code",
    "股票代號": "code",
    "代號": "code",
    "證券名稱": "name",
    "股票名稱": "name",
    "名稱": "name",
    "持股分級": "level",
    "持股級距": "level",
    "持股/單位數分級": "level",
    "持股/單位數分級代碼": "level",
    "人數": "holders",
    "股數": "shares",
    "持有股數": "shares",
    "占集保庫存數比例%": "ratio_pct",
    "占集保庫存數比例": "ratio_pct",
    "比例": "ratio_pct",
}

CODE_PATTERN = re.compile(r"^[0-9]{4}$")
CODE_NAME_PATTERN = re.compile(r"^\s*([0-9]{4})\s+(.+?)\s*$")


def normalize_text(text) -> str:
    if pd.isna(text):
        return ""
    return str(text).replace("\ufeff", "").strip()


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    new_columns = {}

    for col in df.columns:
        clean_col = normalize_text(col)
        new_columns[col] = COLUMN_ALIASES.get(clean_col, clean_col)

    return df.rename(columns=new_columns)


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def fetch_html(url: str, timeout: int = 60) -> str:
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    return response.text


def fetch_stock_code_name_map(url: str) -> dict[str, str]:
    html = fetch_html(url)
    tables = pd.read_html(io.StringIO(html))

    code_name_map: dict[str, str] = {}

    for table in tables:
        if table.empty:
            continue

        for col in table.columns:
            series = table[col].map(normalize_text)

            for value in series:
                match = CODE_NAME_PATTERN.match(value)
                if not match:
                    continue

                code = match.group(1)
                name = match.group(2).strip()

                if not CODE_PATTERN.match(code):
                    continue

                if not name:
                    continue

                name = name.split()[0].strip()

                invalid_keywords = [
                    "指數",
                    "ETN",
                    "受益證券",
                    "認購",
                    "認售",
                    "牛證",
                    "熊證",
                ]

                if any(keyword in name for keyword in invalid_keywords):
                    continue

                code_name_map[code] = name

    return code_name_map


def get_tw_stock_code_name_map() -> dict[str, str]:
    code_name_map: dict[str, str] = {}

    print("Fetching TWSE stock names...")
    code_name_map.update(fetch_stock_code_name_map(TWSE_CODE_URL))

    print("Fetching TPEx stock names...")
    code_name_map.update(fetch_stock_code_name_map(TPEx_CODE_URL))

    return code_name_map


def clean_tdcc_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    required_columns = {"date", "code", "level", "ratio_pct"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            "TDCC 欄位格式不符合預期，"
            f"缺少欄位：{sorted(missing)}；"
            f"目前欄位：{list(df.columns)}"
        )

    df["date"] = df["date"].map(normalize_text)

    # 只接受剛好四碼數字，避免 2887A 被誤合併成 2887
    df["code"] = df["code"].map(normalize_text)
    df = df[df["code"].str.match(r"^[0-9]{4}$", na=False)].copy()

    df["level"] = df["level"].map(normalize_text)

    df["ratio_pct"] = (
        df["ratio_pct"]
        .map(normalize_text)
        .str.replace("%", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    df["ratio_pct"] = pd.to_numeric(df["ratio_pct"], errors="coerce")

    df = df.dropna(subset=["date", "code", "level", "ratio_pct"])

    if df.empty:
        raise ValueError("TDCC 清理後沒有有效資料。")

    return df


def fetch_tdcc_data() -> pd.DataFrame:
    response = requests.get(
        TDCC_URL,
        timeout=60,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    text = response.text.strip()

    if not text:
        raise ValueError("TDCC 回傳資料為空。")

    raw_df = pd.read_csv(io.StringIO(text))
    return clean_tdcc_dataframe(raw_df)


def read_legacy_raw_csv(path: Path) -> pd.DataFrame:
    last_error = None

    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5"]:
        try:
            raw_df = pd.read_csv(path, encoding=encoding)
            return clean_tdcc_dataframe(raw_df)
        except Exception as exc:
            last_error = exc

    raise ValueError(f"無法讀取舊 raw csv：{path}，錯誤：{last_error}")


def parse_level_lower_bound(level: str) -> Optional[int]:
    """
    TDCC 持股分級：
    1  = 1-999 股
    2  = 1,000-5,000 股
    3  = 5,001-10,000 股
    4  = 10,001-15,000 股
    5  = 15,001-20,000 股
    6  = 20,001-30,000 股
    7  = 30,001-40,000 股
    8  = 40,001-50,000 股
    9  = 50,001-100,000 股
    10 = 100,001-200,000 股
    11 = 200,001-400,000 股
    12 = 400,001-600,000 股
    13 = 600,001-800,000 股
    14 = 800,001-1,000,000 股
    15 = 1,000,001 股以上
    16 = 合計，排除
    """

    level_text = normalize_text(level)

    if level_text == "16":
        return None

    level_code_map = {
        "1": 0,
        "2": 1,
        "3": 5,
        "4": 10,
        "5": 15,
        "6": 20,
        "7": 30,
        "8": 40,
        "9": 50,
        "10": 100,
        "11": 200,
        "12": 400,
        "13": 600,
        "14": 800,
        "15": 1000,
    }

    if level_text in level_code_map:
        return level_code_map[level_text]

    numbers = re.findall(r"[0-9,]+", level_text)

    if not numbers:
        return None

    first_number = int(numbers[0].replace(",", ""))

    if first_number >= 1000:
        return first_number // 1000

    return first_number


def build_holder_ratio_snapshot(
    tdcc_df: pd.DataFrame,
    stock_name_map: dict[str, str],
) -> pd.DataFrame:
    df = tdcc_df.copy()

    df["code"] = df["code"].map(normalize_text)
    df = df[df["code"].str.match(r"^[0-9]{4}$", na=False)].copy()

    valid_codes = set(stock_name_map.keys())
    df = df[df["code"].isin(valid_codes)].copy()

    if df.empty:
        raise ValueError("過濾上市櫃股票後沒有資料，請檢查股票名稱對照表是否抓取失敗。")

    df["lower_lots"] = df["level"].map(parse_level_lower_bound)
    df = df.dropna(subset=["lower_lots"])
    df["lower_lots"] = df["lower_lots"].astype(int)

    if df.empty:
        raise ValueError("解析 TDCC 持股分級後沒有資料，請檢查 level 欄位格式。")

    latest_date = df["date"].max()
    latest_df = df[df["date"] == latest_date].copy()

    rows = []

    for code, group in latest_df.groupby("code"):
        name = stock_name_map.get(code, "")

        if not name:
            continue

        row = {
            "date": latest_date,
            "code": code,
            "name": name,
        }

        for threshold in THRESHOLDS:
            ratio_sum = group.loc[group["lower_lots"] >= threshold, "ratio_pct"].sum()
            row[f"over_{threshold}_pct"] = round(float(ratio_sum), 4)

        rows.append(row)

    snapshot = pd.DataFrame(rows)

    if snapshot.empty:
        raise ValueError("沒有產生任何上市櫃股票持股比例資料。")

    snapshot = snapshot.sort_values("code").reset_index(drop=True)

    print(f"Snapshot stock count: {len(snapshot)}")
    print("Snapshot sample:")
    print(snapshot.head(10).to_string(index=False))

    return snapshot


def get_snapshot_date(snapshot: pd.DataFrame) -> str:
    dates = snapshot["date"].dropna().astype(str).unique()

    if len(dates) == 0:
        raise ValueError("snapshot 沒有 date。")

    return max(dates)


def save_raw_tdcc(tdcc_df: pd.DataFrame) -> Path:
    latest_date = tdcc_df["date"].max()
    raw_path = OUTPUT_DIR / f"tdcc_latest_ratio_raw_{latest_date}.csv"
    tdcc_df.to_csv(raw_path, index=False, encoding="utf-8-sig")
    return raw_path


def save_current_snapshot(snapshot: pd.DataFrame) -> Path:
    latest_date = get_snapshot_date(snapshot)

    history_path = HISTORY_DIR / f"tdcc_holder_ratio_{latest_date}.csv"
    latest_path = OUTPUT_DIR / "tdcc_holder_ratio_latest.csv"

    snapshot.to_csv(history_path, index=False, encoding="utf-8-sig")
    snapshot.to_csv(latest_path, index=False, encoding="utf-8-sig")

    return history_path


def bootstrap_history_from_legacy_raw_files(stock_name_map: dict[str, str]) -> None:
    """
    把舊版 output/tdcc_latest_ratio_raw_YYYYMMDD.csv
    轉成新版 output/history/tdcc_holder_ratio_YYYYMMDD.csv。

    這樣不用等下週，現在就能用 20260430 對 20260508 做週增比較。
    """

    legacy_paths = sorted(OUTPUT_DIR.glob("tdcc_latest_ratio_raw_*.csv"))

    if not legacy_paths:
        print("No legacy raw files found.")
        return

    print(f"Legacy raw files found: {len(legacy_paths)}")

    for raw_path in legacy_paths:
        match = re.search(r"tdcc_latest_ratio_raw_([0-9]{8})\.csv$", raw_path.name)
        if not match:
            continue

        date = match.group(1)
        history_path = HISTORY_DIR / f"tdcc_holder_ratio_{date}.csv"

        if history_path.exists():
            print(f"History already exists, skip: {history_path}")
            continue

        print(f"Converting legacy raw file to history snapshot: {raw_path}")

        try:
            legacy_tdcc_df = read_legacy_raw_csv(raw_path)
            snapshot = build_holder_ratio_snapshot(legacy_tdcc_df, stock_name_map)
            snapshot_date = get_snapshot_date(snapshot)

            if snapshot_date != date:
                print(f"Warning: filename date {date} != data date {snapshot_date}")

            snapshot.to_csv(history_path, index=False, encoding="utf-8-sig")
            print(f"Saved history snapshot: {history_path}")

        except Exception as exc:
            print(f"Failed to convert legacy raw file {raw_path}: {exc}")


def find_previous_snapshot(current_date: str) -> Optional[Path]:
    snapshot_paths = sorted(HISTORY_DIR.glob("tdcc_holder_ratio_*.csv"))

    previous_paths = []

    for path in snapshot_paths:
        match = re.search(r"tdcc_holder_ratio_([0-9]{8})\.csv$", path.name)

        if not match:
            continue

        snapshot_date = match.group(1)

        if snapshot_date < current_date:
            previous_paths.append(path)

    if not previous_paths:
        return None

    return previous_paths[-1]


def load_snapshot(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"code": str})
    df["code"] = df["code"].map(normalize_text).str.zfill(4)
    return df


def build_weekly_change_tables(
    current_snapshot: pd.DataFrame,
    previous_snapshot: Optional[pd.DataFrame],
) -> dict[int, pd.DataFrame]:
    result: dict[int, pd.DataFrame] = {}

    if previous_snapshot is None:
        for threshold in THRESHOLDS:
            col = f"over_{threshold}_pct"

            table = current_snapshot[["code", "name", col]].copy()
            table = table.rename(columns={col: "current_pct"})
            table["previous_pct"] = pd.NA
            table["change_pct"] = pd.NA

            table = table.sort_values(
                ["current_pct", "code"],
                ascending=[False, True],
            ).head(10)

            result[threshold] = table.reset_index(drop=True)

        return result

    current_cols = ["code", "name"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]
    previous_cols = ["code"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]

    current = current_snapshot[current_cols].copy()
    previous = previous_snapshot[previous_cols].copy()

    merged = current.merge(
        previous,
        on="code",
        how="left",
        suffixes=("_current", "_previous"),
    )

    for threshold in THRESHOLDS:
        current_col = f"over_{threshold}_pct_current"
        previous_col = f"over_{threshold}_pct_previous"

        table = merged[["code", "name", current_col, previous_col]].copy()
        table = table.rename(
            columns={
                current_col: "current_pct",
                previous_col: "previous_pct",
            }
        )

        table["current_pct"] = pd.to_numeric(table["current_pct"], errors="coerce").fillna(0)
        table["previous_pct"] = pd.to_numeric(table["previous_pct"], errors="coerce").fillna(0)
        table["change_pct"] = table["current_pct"] - table["previous_pct"]

        table = table.sort_values(
            ["change_pct", "current_pct", "code"],
            ascending=[False, False, True],
        ).head(10)

        result[threshold] = table.reset_index(drop=True)

    return result


def format_pct(value) -> str:
    if pd.isna(value):
        return "-"
    return f"{float(value):.2f}%"


def format_change_pct(value) -> str:
    if pd.isna(value):
        return "-"

    value = float(value)
    sign = "+" if value > 0 else ""

    return f"{sign}{value:.2f}%"


def make_markdown_table(table: pd.DataFrame, has_previous: bool) -> str:
    lines = []

    if has_previous:
        lines.append("| 排名 | 代號 | 名稱 | 本週比例 | 上週比例 | 週增減 |")
        lines.append("|---:|---:|---|---:|---:|---:|")

        for idx, row in table.iterrows():
            lines.append(
                "| "
                f"{idx + 1} | "
                f"{row['code']} | "
                f"{row['name']} | "
                f"{format_pct(row['current_pct'])} | "
                f"{format_pct(row['previous_pct'])} | "
                f"{format_change_pct(row['change_pct'])} |"
            )

    else:
        lines.append("| 排名 | 代號 | 名稱 | 最新比例 |")
        lines.append("|---:|---:|---|---:|")

        for idx, row in table.iterrows():
            lines.append(
                "| "
                f"{idx + 1} | "
                f"{row['code']} | "
                f"{row['name']} | "
                f"{format_pct(row['current_pct'])} |"
            )

    return "\n".join(lines)


def build_markdown_report(
    current_snapshot: pd.DataFrame,
    previous_snapshot_path: Optional[Path],
    weekly_tables: dict[int, pd.DataFrame],
) -> str:
    latest_date = get_snapshot_date(current_snapshot)
    has_previous = previous_snapshot_path is not None

    lines = []
    lines.append("# TDCC 週增持股比例報表")
    lines.append("")
    lines.append(f"- 最新資料日：`{latest_date}`")

    if has_previous:
        previous_date_match = re.search(
            r"tdcc_holder_ratio_([0-9]{8})\.csv$",
            previous_snapshot_path.name,
        )
        previous_date = (
            previous_date_match.group(1)
            if previous_date_match
            else previous_snapshot_path.name
        )

        lines.append(f"- 比較基準日：`{previous_date}`")
        lines.append("- 排名邏輯：本週持股比例 - 上週持股比例")
        lines.append("")
        lines.append("這份報表追蹤大戶持股比例週增幅，數字越高代表該級距以上持股比例增加越明顯。")

    else:
        lines.append("- 比較基準日：尚無上一週資料")
        lines.append("")
        lines.append("這是第一次建立基準快照，因此目前只能顯示最新持股比例前十名。下一次成功執行後，會自動產生週增 Top 10。")

    lines.append("")

    for threshold in THRESHOLDS:
        if has_previous:
            lines.append(f"## >{threshold} 張持股比例週增前十名")
        else:
            lines.append(f"## >{threshold} 張最新持股比例前十名")

        lines.append("")
        lines.append(make_markdown_table(weekly_tables[threshold], has_previous=has_previous))
        lines.append("")

    lines.append("## 檔案說明")
    lines.append("")
    lines.append("- `README.md`：GitHub 首頁顯示用報表")
    lines.append("- `output/tdcc_holder_ratio_latest.csv`：最新一次完整快照")
    lines.append("- `output/history/`：每週歷史快照")
    lines.append("- `output/tdcc_weekly_report_latest.md`：最新 Markdown 報表")
    lines.append("- `output/tdcc_weekly_report_日期.md`：每週 Markdown 歷史報表")
    lines.append("- `output/tdcc_latest_ratio_raw_日期.csv`：TDCC 原始清理資料")
    lines.append("")

    return "\n".join(lines)


def write_reports(
    current_snapshot: pd.DataFrame,
    previous_snapshot_path: Optional[Path],
    weekly_tables: dict[int, pd.DataFrame],
) -> None:
    latest_date = get_snapshot_date(current_snapshot)

    report_text = build_markdown_report(
        current_snapshot=current_snapshot,
        previous_snapshot_path=previous_snapshot_path,
        weekly_tables=weekly_tables,
    )

    README_PATH.write_text(report_text, encoding="utf-8")

    latest_report_path = OUTPUT_DIR / "tdcc_weekly_report_latest.md"
    dated_report_path = OUTPUT_DIR / f"tdcc_weekly_report_{latest_date}.md"

    latest_report_path.write_text(report_text, encoding="utf-8")
    dated_report_path.write_text(report_text, encoding="utf-8")


def main() -> int:
    ensure_dirs()

    print("Fetching Taiwan stock code/name map...")
    stock_name_map = get_tw_stock_code_name_map()
    print(f"Loaded stock names: {len(stock_name_map)}")

    if not stock_name_map:
        raise ValueError("股票名稱對照表抓取失敗，stock_name_map 為空。")

    print("Bootstrapping history from legacy raw files...")
    bootstrap_history_from_legacy_raw_files(stock_name_map)

    print("Fetching latest TDCC data...")
    tdcc_df = fetch_tdcc_data()
    print(f"Loaded TDCC rows: {len(tdcc_df)}")

    print("Saving latest raw TDCC data...")
    raw_path = save_raw_tdcc(tdcc_df)
    print(f"Latest raw saved: {raw_path}")

    print("Building current snapshot...")
    current_snapshot = build_holder_ratio_snapshot(tdcc_df, stock_name_map)
    current_date = get_snapshot_date(current_snapshot)
    print(f"Current TDCC date: {current_date}")

    print("Saving current snapshot...")
    current_snapshot_path = save_current_snapshot(current_snapshot)
    print(f"Current snapshot saved: {current_snapshot_path}")

    previous_snapshot_path = find_previous_snapshot(current_date)

    previous_snapshot = None
    if previous_snapshot_path is not None:
        print(f"Previous snapshot found: {previous_snapshot_path}")
        previous_snapshot = load_snapshot(previous_snapshot_path)
    else:
        print("No previous snapshot found. This run will create baseline report.")

    print("Building weekly change tables...")
    weekly_tables = build_weekly_change_tables(
        current_snapshot=current_snapshot,
        previous_snapshot=previous_snapshot,
    )

    print("Writing reports...")
    write_reports(
        current_snapshot=current_snapshot,
        previous_snapshot_path=previous_snapshot_path,
        weekly_tables=weekly_tables,
    )

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
