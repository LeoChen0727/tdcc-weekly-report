import io
import re
from pathlib import Path
from typing import Optional

import pandas as pd
import requests


TDCC_URLS = [
    "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5",
    "https://smart.tdcc.com.tw/opendata/getOD.ashx?id=1-5",
]

TWSE_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
TPEx_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"

OUTPUT_DIR = Path("output")
LATEST_DIR = OUTPUT_DIR / "latest"
HISTORY_DIR = OUTPUT_DIR / "history"
TDCC_HISTORY_DIR = HISTORY_DIR / "tdcc"
README_PATH = Path("README.md")

THRESHOLDS = [400, 600, 800, 1000]
TOP_N = 20
CONSECUTIVE_WEEKS = 2

COLUMN_ALIASES = {
    "資料日期": "date",
    "日期": "date",
    "證券代號": "code",
    "股票代號": "code",
    "代號": "code",
    "code": "code",
    "證券名稱": "name",
    "股票名稱": "name",
    "名稱": "name",
    "name": "name",
    "持股分級": "level",
    "持股級距": "level",
    "持股/單位數分級": "level",
    "持股/單位數分級代碼": "level",
    "level": "level",
    "人數": "holders",
    "holders": "holders",
    "股數": "shares",
    "持有股數": "shares",
    "shares": "shares",
    "占集保庫存數比例%": "ratio_pct",
    "占集保庫存數比例": "ratio_pct",
    "比例": "ratio_pct",
    "ratio_pct": "ratio_pct",
    "threshold_lots": "threshold_lots",
    "門檻張數": "threshold_lots",
    "張數門檻": "threshold_lots",
}

CODE_NAME_PATTERN = re.compile(r"^\s*([0-9]{4})\s+(.+?)\s*$")


def normalize_text(text) -> str:
    if pd.isna(text):
        return ""
    return str(text).replace("\ufeff", "").strip()


def is_common_stock_code(code) -> bool:
    code = normalize_text(code)

    if not re.match(r"^[0-9]{4}$", code):
        return False

    if code.startswith("00"):
        return False

    try:
        return int(code) >= 1000
    except ValueError:
        return False


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    new_columns = {}

    for col in df.columns:
        clean_col = normalize_text(col)
        lower_col = clean_col.lower()

        if clean_col in COLUMN_ALIASES:
            new_columns[col] = COLUMN_ALIASES[clean_col]
        elif lower_col in COLUMN_ALIASES:
            new_columns[col] = COLUMN_ALIASES[lower_col]
        elif "code" in lower_col or "代號" in clean_col:
            new_columns[col] = "code"
        elif "name" in lower_col or "名稱" in clean_col:
            new_columns[col] = "name"
        elif "threshold" in lower_col or "門檻" in clean_col:
            new_columns[col] = "threshold_lots"
        elif "ratio" in lower_col or "比例" in clean_col:
            new_columns[col] = "ratio_pct"
        elif "date" in lower_col or "日期" in clean_col:
            new_columns[col] = "date"
        elif "level" in lower_col or "分級" in clean_col or "級距" in clean_col:
            new_columns[col] = "level"
        else:
            new_columns[col] = clean_col

    return df.rename(columns=new_columns)


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    TDCC_HISTORY_DIR.mkdir(parents=True, exist_ok=True)


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

                if not is_common_stock_code(code):
                    continue

                if not name:
                    continue

                name = name.split()[0].strip()

                invalid_keywords = [
                    "指數",
                    "ETF",
                    "ETN",
                    "受益證券",
                    "受益憑證",
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


def extract_date_from_filename(path: Path) -> Optional[str]:
    match = re.search(r"([0-9]{8})", path.name)
    if match:
        return match.group(1)
    return None


def clean_code_series(series: pd.Series) -> pd.Series:
    return series.map(normalize_text)


def clean_ratio_series(series: pd.Series) -> pd.Series:
    cleaned = (
        series.map(normalize_text)
        .str.replace("%", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    return pd.to_numeric(cleaned, errors="coerce")


def clean_tdcc_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    required_columns = {"date", "code", "level", "ratio_pct"}
    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            "TDCC 原始格式欄位不符合預期，"
            f"缺少欄位：{sorted(missing)}；"
            f"目前欄位：{list(df.columns)}"
        )

    df["date"] = df["date"].map(normalize_text)

    df["code"] = clean_code_series(df["code"])
    df = df[df["code"].map(is_common_stock_code)].copy()

    df["level"] = df["level"].map(normalize_text)
    df["ratio_pct"] = clean_ratio_series(df["ratio_pct"])

    df = df.dropna(subset=["date", "code", "level", "ratio_pct"])

    if df.empty:
        raise ValueError("TDCC 清理後沒有有效資料。")

    return df


def fetch_tdcc_data_from_url(url: str) -> tuple[pd.DataFrame, str, str]:
    print(f"Fetching TDCC data from: {url}")

    response = requests.get(
        url,
        timeout=60,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )
    response.raise_for_status()
    response.encoding = response.apparent_encoding

    text = response.text.strip()

    if not text:
        raise ValueError(f"TDCC 回傳資料為空：{url}")

    raw_df = pd.read_csv(io.StringIO(text))
    df = clean_tdcc_dataframe(raw_df)
    latest_date = df["date"].max()

    print(f"TDCC source date from {url}: {latest_date}")

    return df, latest_date, url


def fetch_tdcc_data() -> tuple[pd.DataFrame, str]:
    candidates = []
    errors = []

    for url in TDCC_URLS:
        try:
            df, latest_date, source_url = fetch_tdcc_data_from_url(url)
            candidates.append(
                {
                    "df": df,
                    "date": latest_date,
                    "url": source_url,
                    "rows": len(df),
                }
            )
        except Exception as exc:
            errors.append(f"{url}: {exc}")
            print(f"Failed to fetch TDCC source: {url}")
            print(exc)

    if not candidates:
        raise ValueError("所有 TDCC 資料來源都抓取失敗：" + " | ".join(errors))

    candidates = sorted(
        candidates,
        key=lambda item: (str(item["date"]), int(item["rows"])),
        reverse=True,
    )

    best = candidates[0]

    print("TDCC source candidates:")
    for item in candidates:
        print(f"- date={item['date']}, rows={item['rows']}, url={item['url']}")

    print(f"Selected TDCC source: {best['url']}")
    print(f"Selected TDCC date: {best['date']}")

    return best["df"], best["url"]


def parse_level_lower_bound(level: str) -> Optional[int]:
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

    df["code"] = clean_code_series(df["code"])
    df = df[df["code"].map(is_common_stock_code)].copy()

    valid_codes = set(stock_name_map.keys())
    df = df[df["code"].isin(valid_codes)].copy()

    if df.empty:
        raise ValueError("過濾上市櫃普通股後沒有資料，請檢查股票名稱對照表是否抓取失敗。")

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
        raise ValueError("沒有產生任何上市櫃普通股持股比例資料。")

    snapshot = snapshot.sort_values("code").reset_index(drop=True)

    print(f"Snapshot stock count: {len(snapshot)}")
    print("Snapshot sample:")
    print(snapshot.head(10).to_string(index=False))

    return snapshot


def build_snapshot_from_legacy_summary(
    df: pd.DataFrame,
    date: str,
    stock_name_map: dict[str, str],
) -> pd.DataFrame:
    df = normalize_columns(df)

    required = {"code", "threshold_lots", "ratio_pct"}
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            "舊版 summary 格式也不符合預期，"
            f"缺少欄位：{sorted(missing)}；目前欄位：{list(df.columns)}"
        )

    df["code"] = clean_code_series(df["code"])
    df = df[df["code"].map(is_common_stock_code)].copy()
    df = df[df["code"].isin(stock_name_map.keys())].copy()

    df["threshold_lots"] = pd.to_numeric(
        df["threshold_lots"].map(normalize_text).str.replace(",", "", regex=False),
        errors="coerce",
    )
    df["ratio_pct"] = clean_ratio_series(df["ratio_pct"])

    df = df.dropna(subset=["code", "threshold_lots", "ratio_pct"])
    df["threshold_lots"] = df["threshold_lots"].astype(int)

    rows = []

    for code, group in df.groupby("code"):
        name = stock_name_map.get(code, "")

        if not name and "name" in group.columns:
            non_empty_names = group["name"].dropna()
            if not non_empty_names.empty:
                name = normalize_text(non_empty_names.iloc[0])

        if not name:
            continue

        row = {
            "date": date,
            "code": code,
            "name": name,
        }

        for threshold in THRESHOLDS:
            matched = group[group["threshold_lots"] == threshold]

            if matched.empty:
                row[f"over_{threshold}_pct"] = pd.NA
            else:
                row[f"over_{threshold}_pct"] = round(float(matched["ratio_pct"].iloc[0]), 4)

        rows.append(row)

    snapshot = pd.DataFrame(rows)

    if snapshot.empty:
        raise ValueError("舊版 summary 轉 snapshot 後沒有資料。")

    snapshot = snapshot.sort_values("code").reset_index(drop=True)

    print(f"Legacy summary converted. Date={date}, stock count={len(snapshot)}")
    print(snapshot.head(10).to_string(index=False))

    return snapshot


def read_legacy_file_as_snapshot(
    path: Path,
    stock_name_map: dict[str, str],
) -> pd.DataFrame:
    date = extract_date_from_filename(path)

    if not date:
        raise ValueError(f"檔名找不到日期：{path}")

    last_error = None

    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5"]:
        try:
            raw_df = pd.read_csv(path, encoding=encoding)
            normalized = normalize_columns(raw_df)

            if {"date", "code", "level", "ratio_pct"}.issubset(set(normalized.columns)):
                cleaned_tdcc = clean_tdcc_dataframe(raw_df)
                return build_holder_ratio_snapshot(cleaned_tdcc, stock_name_map)

            if {"code", "threshold_lots", "ratio_pct"}.issubset(set(normalized.columns)):
                return build_snapshot_from_legacy_summary(
                    df=raw_df,
                    date=date,
                    stock_name_map=stock_name_map,
                )

            raise ValueError(f"不支援的舊檔欄位格式：{list(normalized.columns)}")

        except Exception as exc:
            last_error = exc

    raise ValueError(f"無法讀取舊檔：{path}，最後錯誤：{last_error}")


def get_snapshot_date(snapshot: pd.DataFrame) -> str:
    dates = snapshot["date"].dropna().astype(str).unique()

    if len(dates) == 0:
        raise ValueError("snapshot 沒有 date。")

    return max(dates)


def save_raw_tdcc(tdcc_df: pd.DataFrame) -> Path:
    latest_date = tdcc_df["date"].max()
    raw_path = TDCC_HISTORY_DIR / f"tdcc_latest_ratio_raw_{latest_date}.csv"
    tdcc_df.to_csv(raw_path, index=False, encoding="utf-8-sig")
    return raw_path


def save_current_snapshot(snapshot: pd.DataFrame) -> Path:
    latest_date = get_snapshot_date(snapshot)

    history_path = TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{latest_date}.csv"
    latest_path = LATEST_DIR / "tdcc_holder_ratio_latest.csv"

    snapshot.to_csv(history_path, index=False, encoding="utf-8-sig")
    snapshot.to_csv(latest_path, index=False, encoding="utf-8-sig")

    return history_path


def bootstrap_history_from_legacy_raw_files(stock_name_map: dict[str, str]) -> None:
    legacy_paths = sorted(OUTPUT_DIR.glob("tdcc_latest_ratio_raw_*.csv")) + sorted(TDCC_HISTORY_DIR.glob("tdcc_latest_ratio_raw_*.csv"))

    if not legacy_paths:
        print("No legacy raw files found.")
        return

    print(f"Legacy raw files found: {len(legacy_paths)}")

    for raw_path in legacy_paths:
        date = extract_date_from_filename(raw_path)

        if not date:
            print(f"Skip legacy file without date: {raw_path}")
            continue

        history_path = TDCC_HISTORY_DIR / f"tdcc_holder_ratio_{date}.csv"

        print(f"Rebuilding history snapshot from legacy file: {raw_path}")

        try:
            snapshot = read_legacy_file_as_snapshot(raw_path, stock_name_map)
            snapshot.to_csv(history_path, index=False, encoding="utf-8-sig")
            print(f"Saved history snapshot: {history_path}")

        except Exception as exc:
            print(f"Failed to convert legacy file {raw_path}: {exc}")


def find_previous_snapshot(current_date: str) -> Optional[Path]:
    snapshot_paths = sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv"))

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


def get_recent_snapshot_paths(required_count: int) -> list[Path]:
    snapshot_paths = []

    for path in sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv")):
        match = re.search(r"tdcc_holder_ratio_([0-9]{8})\.csv$", path.name)
        if match:
            snapshot_paths.append(path)

    return snapshot_paths[-required_count:]


def load_snapshot(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"code": str})
    df["code"] = df["code"].map(normalize_text).str.zfill(4)
    df = df[df["code"].map(is_common_stock_code)].copy()
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
            ).head(TOP_N)

            result[threshold] = table.reset_index(drop=True)

        return result

    current_cols = ["code", "name"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]
    previous_cols = ["code"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]

    current = current_snapshot[current_cols].copy()
    previous = previous_snapshot[previous_cols].copy()

    merged = current.merge(
        previous,
        on="code",
        how="inner",
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

        table["current_pct"] = pd.to_numeric(table["current_pct"], errors="coerce")
        table["previous_pct"] = pd.to_numeric(table["previous_pct"], errors="coerce")

        table = table.dropna(subset=["current_pct", "previous_pct"])
        table["change_pct"] = table["current_pct"] - table["previous_pct"]

        table = table.sort_values(
            ["change_pct", "current_pct", "code"],
            ascending=[False, False, True],
        ).head(TOP_N)

        result[threshold] = table.reset_index(drop=True)

    return result


def build_consecutive_increase_table() -> tuple[pd.DataFrame, str]:
    required_count = CONSECUTIVE_WEEKS + 1
    recent_paths = get_recent_snapshot_paths(required_count)

    if len(recent_paths) < required_count:
        message = (
            f"歷史資料不足，至少需要 {required_count} 週 snapshot，"
            f"目前只有 {len(recent_paths)} 週。"
        )
        return pd.DataFrame(), message

    snapshots = []
    dates = []

    for path in recent_paths:
        snapshot = load_snapshot(path)
        date = get_snapshot_date(snapshot)
        dates.append(date)
        snapshots.append(snapshot)

    base = snapshots[-1][["code", "name"]].copy()

    for i, snapshot in enumerate(snapshots):
        cols = ["code"] + [f"over_{threshold}_pct" for threshold in THRESHOLDS]
        temp = snapshot[cols].copy()

        rename_map = {
            f"over_{threshold}_pct": f"over_{threshold}_pct_w{i}"
            for threshold in THRESHOLDS
        }
        temp = temp.rename(columns=rename_map)

        base = base.merge(temp, on="code", how="inner")

    for threshold in THRESHOLDS:
        for i in range(1, len(snapshots)):
            prev_col = f"over_{threshold}_pct_w{i - 1}"
            curr_col = f"over_{threshold}_pct_w{i}"
            delta_col = f"delta_{threshold}_w{i}"

            base[prev_col] = pd.to_numeric(base[prev_col], errors="coerce")
            base[curr_col] = pd.to_numeric(base[curr_col], errors="coerce")
            base[delta_col] = base[curr_col] - base[prev_col]

    delta_cols = [
        f"delta_{threshold}_w{i}"
        for threshold in THRESHOLDS
        for i in range(1, len(snapshots))
    ]

    table = base.dropna(subset=delta_cols).copy()

    for col in delta_cols:
        table = table[table[col] > 0].copy()

    for threshold in THRESHOLDS:
        threshold_delta_cols = [
            f"delta_{threshold}_w{i}"
            for i in range(1, len(snapshots))
        ]

        table[f"over_{threshold}_total_change"] = table[threshold_delta_cols].sum(axis=1)

        table[f"over_{threshold}_weekly_changes"] = table[threshold_delta_cols].apply(
            lambda row: " / ".join(format_change_pct(value) for value in row),
            axis=1,
        )

    score_cols = [f"over_{threshold}_total_change" for threshold in THRESHOLDS]
    table["score"] = table[score_cols].sum(axis=1)

    output_cols = ["code", "name"]

    for threshold in THRESHOLDS:
        output_cols.append(f"over_{threshold}_weekly_changes")

    for threshold in THRESHOLDS:
        output_cols.append(f"over_{threshold}_total_change")

    output_cols.append("score")

    table = table[output_cols].copy()

    table = table.sort_values(
        ["score", "code"],
        ascending=[False, True],
    ).head(TOP_N)

    message = f"比較區間：{' → '.join(dates)}"

    return table.reset_index(drop=True), message


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


def make_consecutive_increase_markdown_table(table: pd.DataFrame) -> str:
    if table.empty:
        return "目前沒有符合條件的股票。"

    lines = []
    lines.append(
        "| 排名 | 代號 | 名稱 | 400張近兩週變化 | 600張近兩週變化 | 800張近兩週變化 | 1000張近兩週變化 | 400累增 | 600累增 | 800累增 | 1000累增 | 綜合分數 |"
    )
    lines.append(
        "|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"
    )

    for idx, row in table.iterrows():
        lines.append(
            "| "
            f"{idx + 1} | "
            f"{row['code']} | "
            f"{row['name']} | "
            f"{row['over_400_weekly_changes']} | "
            f"{row['over_600_weekly_changes']} | "
            f"{row['over_800_weekly_changes']} | "
            f"{row['over_1000_weekly_changes']} | "
            f"{format_change_pct(row['over_400_total_change'])} | "
            f"{format_change_pct(row['over_600_total_change'])} | "
            f"{format_change_pct(row['over_800_total_change'])} | "
            f"{format_change_pct(row['over_1000_total_change'])} | "
            f"{format_change_pct(row['score'])} |"
        )

    return "\n".join(lines)


def build_markdown_report(
    current_snapshot: pd.DataFrame,
    previous_snapshot_path: Optional[Path],
    weekly_tables: dict[int, pd.DataFrame],
    consecutive_table: pd.DataFrame,
    consecutive_message: str,
    tdcc_source_url: str,
) -> str:
    latest_date = get_snapshot_date(current_snapshot)
    has_previous = previous_snapshot_path is not None

    lines = []
    lines.append("# TDCC 週增持股比例報表")
    lines.append("")
    lines.append(f"- 最新資料日：`{latest_date}`")
    lines.append(f"- TDCC 資料來源：`{tdcc_source_url}`")

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
        lines.append("- 篩選規則：排除 ETF / 指數商品，只保留一般上市櫃普通股")
        lines.append("")
        lines.append("這份報表追蹤大戶持股比例週增幅，數字越高代表該級距以上持股比例增加越明顯。")

    else:
        lines.append("- 比較基準日：尚無上一週資料")
        lines.append("- 篩選規則：排除 ETF / 指數商品，只保留一般上市櫃普通股")
        lines.append("")
        lines.append("目前只能顯示最新持股比例前二十名。下一次成功執行後，會自動產生週增 Top 20。")

    lines.append("")

    for threshold in THRESHOLDS:
        if has_previous:
            lines.append(f"## >{threshold} 張持股比例週增前二十名")
        else:
            lines.append(f"## >{threshold} 張最新持股比例前二十名")

        lines.append("")
        lines.append(make_markdown_table(weekly_tables[threshold], has_previous=has_previous))
        lines.append("")

    lines.append("## 最近兩週 400 / 600 / 800 / 1000 張連續週增股票")
    lines.append("")
    lines.append("- 條件：最近 3 份 snapshot 產生 2 次週變化，四個級距每一次週變化都必須 > 0")
    lines.append(f"- {consecutive_message}")
    lines.append("")
    lines.append(make_consecutive_increase_markdown_table(consecutive_table))
    lines.append("")

    lines.append("## 檔案說明")
    lines.append("")
    lines.append("- `README.md`：GitHub 首頁顯示用報表")
    lines.append("- `output/latest/tdcc_holder_ratio_latest.csv`：最新一次完整快照")
    lines.append("- `output/history/tdcc/`：每週歷史快照")
    lines.append("- `output/latest/tdcc_weekly_report_latest.md`：最新 Markdown 報表")
    lines.append("- `output/history/tdcc/tdcc_weekly_report_日期.md`：每週 Markdown 歷史報表")
    lines.append("- `output/history/tdcc/tdcc_latest_ratio_raw_日期.csv`：TDCC 原始或舊版整理資料")
    lines.append("")

    return "\n".join(lines)


def write_reports(
    current_snapshot: pd.DataFrame,
    previous_snapshot_path: Optional[Path],
    weekly_tables: dict[int, pd.DataFrame],
    consecutive_table: pd.DataFrame,
    consecutive_message: str,
    tdcc_source_url: str,
) -> None:
    latest_date = get_snapshot_date(current_snapshot)

    report_text = build_markdown_report(
        current_snapshot=current_snapshot,
        previous_snapshot_path=previous_snapshot_path,
        weekly_tables=weekly_tables,
        consecutive_table=consecutive_table,
        consecutive_message=consecutive_message,
        tdcc_source_url=tdcc_source_url,
    )

    README_PATH.write_text(report_text, encoding="utf-8")

    latest_report_path = LATEST_DIR / "tdcc_weekly_report_latest.md"
    dated_report_path = TDCC_HISTORY_DIR / f"tdcc_weekly_report_{latest_date}.md"

    latest_report_path.write_text(report_text, encoding="utf-8")
    dated_report_path.write_text(report_text, encoding="utf-8")


def main() -> int:
    ensure_dirs()

    print("Fetching Taiwan stock code/name map...")
    stock_name_map = get_tw_stock_code_name_map()
    print(f"Loaded stock names: {len(stock_name_map)}")

    if not stock_name_map:
        raise ValueError("股票名稱對照表抓取失敗，stock_name_map 為空。")

    print("Bootstrapping history from legacy files...")
    bootstrap_history_from_legacy_raw_files(stock_name_map)

    print("Fetching latest TDCC data from multiple sources...")
    tdcc_df, tdcc_source_url = fetch_tdcc_data()
    print(f"Loaded TDCC rows: {len(tdcc_df)}")
    print(f"Selected TDCC source URL: {tdcc_source_url}")

    print("Saving latest TDCC data...")
    raw_path = save_raw_tdcc(tdcc_df)
    print(f"Latest data saved: {raw_path}")

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

    print("Building consecutive increase table...")
    consecutive_table, consecutive_message = build_consecutive_increase_table()
    print(consecutive_message)

    print("Writing reports...")
    write_reports(
        current_snapshot=current_snapshot,
        previous_snapshot_path=previous_snapshot_path,
        weekly_tables=weekly_tables,
        consecutive_table=consecutive_table,
        consecutive_message=consecutive_message,
        tdcc_source_url=tdcc_source_url,
    )

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
