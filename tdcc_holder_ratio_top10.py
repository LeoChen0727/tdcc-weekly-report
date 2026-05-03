#!/usr/bin/env python3
from __future__ import annotations

import io
import re
from pathlib import Path

import pandas as pd
import requests

TDCC_CSV_URL = "https://opendata.tdcc.com.tw/getOD.ashx?id=1-5"
TWSE_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
TPEX_CODE_URL = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"

THRESHOLDS = {
    400: [12, 13, 14, 15],
    600: [13, 14, 15],
    800: [14, 15],
    1000: [15],
}

EXPECTED_COLUMNS = {
    "資料日期": "date",
    "證券代號": "code",
    "持股分級": "class_id",
    "人數": "holders",
    "股數": "shares",
    "占集保庫存數比例%": "ratio_pct",
    "證券名稱": "name",
}

CODE_PATTERN = re.compile(r"^[0-9]{4}$")
CODE_NAME_PATTERN = re.compile(r"^\s*([0-9]{4})\s+(.+?)\s*$")


def normalize_text(text: str) -> str:
    return text.replace("\ufeff", "").strip()


def fetch_html(url: str, timeout: int = 60) -> str:
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "Mozilla/5.0"},
    )
    response.raise_for_status()
    return response.text


def fetch_stock_code_name_map(url: str) -> dict[str, str]:
    html = fetch_html(url)
    tables = pd.read_html(io.StringIO(html))
    code_name_map: dict[str, str] = {}

    for table in tables:
        for col in table.columns:
            series = table[col].astype(str).map(normalize_text)
            for value in series:
                match = CODE_NAME_PATTERN.match(value)
                if not match:
                    continue
                code = match.group(1)
                name = match.group(2).strip()
                if code not in code_name_map:
                    code_name_map[code] = name

    return code_name_map


def get_tw_stock_code_name_map() -> dict[str, str]:
    code_name_map = {}
    code_name_map.update(fetch_stock_code_name_map(TWSE_CODE_URL))
    code_name_map.update(fetch_stock_code_name_map(TPEX_CODE_URL))
    return code_name_map


def download_tdcc_csv(url: str, timeout: int = 60) -> bytes:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/csv,application/csv,text/plain,*/*",
    }
    response = requests.get(url, timeout=timeout, headers=headers)
    response.raise_for_status()
    return response.content


def load_csv_bytes(csv_bytes: bytes) -> pd.DataFrame:
    last_error = None
    for enc in ("utf-8-sig", "utf-8", "big5", "cp950"):
        try:
            return pd.read_csv(io.BytesIO(csv_bytes), encoding=enc, dtype=str)
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f"Unable to decode TDCC CSV. Last error: {last_error}")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {}
    for col in df.columns:
        clean = normalize_text(str(col))
        rename_map[col] = EXPECTED_COLUMNS.get(clean, clean)
    df = df.rename(columns=rename_map)

    required = {"date", "code", "class_id", "holders", "shares", "ratio_pct"}
    missing = required - set(df.columns)
    if missing:
        raise RuntimeError(f"Missing required TDCC columns: {sorted(missing)}")
    return df


def clean_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False).str.strip(),
        errors="coerce",
    )


def tidy_tdcc(df: pd.DataFrame, stock_name_map: dict[str, str]) -> pd.DataFrame:
    df = normalize_columns(df).copy()

    for col in ("date", "code", "class_id", "holders", "shares", "ratio_pct"):
        df[col] = df[col].astype(str).map(normalize_text)

    df = df[df["code"].str.match(CODE_PATTERN, na=False)].copy()
    df = df[df["code"].isin(stock_name_map.keys())].copy()

    df["class_id"] = clean_numeric(df["class_id"]).astype("Int64")
    df["holders"] = clean_numeric(df["holders"]).fillna(0).astype(int)
    df["shares"] = clean_numeric(df["shares"]).fillna(0).astype("int64")
    df["ratio_pct"] = clean_numeric(df["ratio_pct"]).fillna(0.0).astype(float)

    if "name" not in df.columns:
        df["name"] = ""
    else:
        df["name"] = df["name"].astype(str).map(normalize_text)

    df["name"] = df["code"].map(stock_name_map).fillna(df["name"])
    df = df[df["class_id"].between(1, 15, inclusive="both")].copy()
    df["date"] = df["date"].astype(str).str.slice(0, 8)

    return df


def infer_snapshot_date(df: pd.DataFrame) -> str:
    dates = sorted(set(df["date"].dropna().astype(str)))
    if len(dates) != 1:
        raise RuntimeError(f"Expected one snapshot date, got: {dates}")
    return dates[0]


def aggregate_threshold_ratios(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    name_map = (
        df[["code", "name"]]
        .dropna()
        .drop_duplicates(subset=["code"])
        .set_index("code")["name"]
        .to_dict()
    )

    for threshold_lots, class_ids in THRESHOLDS.items():
        grouped = (
            df[df["class_id"].isin(class_ids)]
            .groupby("code", as_index=False)
            .agg(
                ratio_pct=("ratio_pct", "sum"),
                shares=("shares", "sum"),
                holders=("holders", "sum"),
            )
        )
        grouped["threshold_lots"] = threshold_lots
        grouped["name"] = grouped["code"].map(name_map).fillna("")
        rows.append(grouped)

    out = pd.concat(rows, ignore_index=True)
    return out[["code", "name", "threshold_lots", "ratio_pct", "shares", "holders"]]


def format_pct(value: float) -> str:
    return f"{value:.2f}%"


def main() -> int:
    stock_name_map = get_tw_stock_code_name_map()

    csv_bytes = download_tdcc_csv(TDCC_CSV_URL)
    latest_df = tidy_tdcc(load_csv_bytes(csv_bytes), stock_name_map)
    latest_date = infer_snapshot_date(latest_df)

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    latest_agg = aggregate_threshold_ratios(latest_df)

    md_lines = []
    md_lines.append("# TDCC 最新持股比例報表")
    md_lines.append("")
    md_lines.append(f"- 最新資料日：`{latest_date}`")
    md_lines.append("")
    md_lines.append("這是初始化版本，先確認資料抓取成功。")
    md_lines.append("下一步再加入前一週比較與前十名排序。")
    md_lines.append("")

    for threshold in sorted(THRESHOLDS.keys()):
        md_lines.append(f"## >{threshold} 張最新持股比例前十名")
        md_lines.append("")
        md_lines.append("| 排名 | 代號 | 名稱 | 最新比例 |")
        md_lines.append("|---:|---:|---|---:|")
        part = (
            latest_agg[latest_agg["threshold_lots"] == threshold]
            .sort_values(by=["ratio_pct", "shares", "code"], ascending=[False, False, True])
            .head(10)
            .reset_index(drop=True)
        )
        for i, (_, row) in enumerate(part.iterrows(), start=1):
            name = row["name"] if str(row["name"]).strip() else "-"
            md_lines.append(
                f"| {i} | {row['code']} | {name} | {format_pct(row['ratio_pct'])} |"
            )
        md_lines.append("")

    report_md = "\n".join(md_lines)
    report_path = output_dir / f"tdcc_latest_ratio_report_{latest_date}.md"
    report_path.write_text(report_md, encoding="utf-8")

    latest_agg.to_csv(
        output_dir / f"tdcc_latest_ratio_raw_{latest_date}.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print(report_md)
    print("")
    print(f"Saved report to: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
