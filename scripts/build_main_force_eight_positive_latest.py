from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import json
import math
import re
import shutil

import pandas as pd


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

SOURCE_PATTERNS = [
    "data/chip_flow/main_force_daily/*.csv",
    "data/chip_flow/main_force_daily.csv",
    "data/chip_flow/main_force_history.csv",
    "output/latest/main_force_daily_latest.csv",
    "output/latest/chip_flow_daily_latest.csv",
]

LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_DIR = Path("output/history/main_force_eight_positive")

OUTPUT_CSV = LATEST_DIR / "main_force_eight_positive_latest.csv"
OUTPUT_MD = LATEST_DIR / "main_force_eight_positive_latest.md"
OUTPUT_JSON = LATEST_DIR / "main_force_eight_positive_latest.json"

DOCS_CSV = DOCS_LATEST_DIR / OUTPUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUTPUT_MD.name
DOCS_JSON = DOCS_LATEST_DIR / OUTPUT_JSON.name

OUTPUT_COLUMNS = [
    "date",
    "stock_id",
    "stock_name",
    "positive_streak_days",
    "streak_start_date",
    "streak_end_date",
    "latest_value",
    "previous_1_value",
    "previous_2_value",
    "latest_main_force_net_buy",
    "latest_eight_institution_net_buy",
    "latest_eight_bank_net_buy",
    "rule",
    "source_file",
]

DATE_ALIASES = ["date", "日期", "交易日期", "資料日期", "data_date"]
STOCK_ID_ALIASES = ["stock_id", "股票代號", "證券代號", "代號", "code", "ticker"]
STOCK_NAME_ALIASES = ["stock_name", "股票名稱", "證券名稱", "名稱", "name"]
MAIN_FORCE_ALIASES = [
    "main_force_net_buy",
    "main_force_buy_sell",
    "主力買賣超",
    "主力買超",
    "主力淨買超",
]
EIGHT_INSTITUTION_ALIASES = [
    "eight_institution_net_buy",
    "eight_legal_net_buy",
    "八大法人買賣超",
    "八大法人買超",
    "法人買賣超",
    "三大法人買賣超",
]
EIGHT_BANK_ALIASES = [
    "eight_bank_net_buy",
    "eight_public_bank_net_buy",
    "八大行庫買賣超",
    "八大行庫買超",
    "八大公股買賣超",
    "八大官股買賣超",
]
COMPUTED_VALUE_ALIASES = [
    "main_force_minus_eight_value",
    "main_force_minus_eight_net_buy",
    "主力扣八大買賣超",
    "主力扣八大",
    "主力買賣超扣八大法人八大行庫",
    "主力買賣超-八大法人買賣超-八大行庫買賣超",
]

RULE_TEXT = "主力買賣超 - 八大法人買賣超 - 八大行庫買賣超 > 0，且連續交易日 >= 3"


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def today_yyyymmdd() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value).upper()
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Z]", "", text)
    if text.isdigit() and len(text) < 4:
        text = text.zfill(4)
    return text


def normalize_date(value: Any) -> str:
    text = re.sub(r"[^0-9]", "", safe_str(value))
    if len(text) >= 8:
        return text[:8]
    return text


def extract_date_from_path(path: Path) -> str:
    match = re.search(r"(20\d{6})", path.as_posix())
    return match.group(1) if match else ""


def normalize_column_name(value: Any) -> str:
    return safe_str(value).replace("\ufeff", "").strip().lower()


def first_existing(columns: list[str], aliases: list[str]) -> str:
    normalized = {normalize_column_name(col): col for col in columns}
    for alias in aliases:
        key = normalize_column_name(alias)
        if key in normalized:
            return normalized[key]
    return ""


def to_number(value: Any) -> float:
    text = safe_str(value)
    if text == "":
        return math.nan

    negative = False
    if text.startswith("(") and text.endswith(")"):
        negative = True
        text = text[1:-1]

    text = text.replace("−", "-").replace("－", "-")
    multiplier = 1.0
    if "億" in text:
        multiplier = 100000000.0
    elif "萬" in text:
        multiplier = 10000.0

    text = (
        text.replace(",", "")
        .replace("%", "")
        .replace("+", "")
        .replace("張", "")
        .replace("股", "")
        .replace("仟", "")
        .replace("千", "")
        .replace(" ", "")
    )
    text = re.sub(r"[^0-9.\-]", "", text)

    if text in {"", "-", ".", "-."}:
        return math.nan

    try:
        value_float = float(text) * multiplier
        return -value_float if negative else value_float
    except Exception:
        return math.nan


def read_csv_any_encoding(path: Path) -> pd.DataFrame:
    for encoding in ["utf-8-sig", "utf-8", "cp950", "big5", "latin1"]:
        try:
            return pd.read_csv(path, dtype=str, encoding=encoding).fillna("")
        except Exception:
            continue
    return pd.DataFrame()


def collect_source_files() -> list[Path]:
    files: list[Path] = []
    seen: set[str] = set()
    for pattern in SOURCE_PATTERNS:
        for path in sorted(Path().glob(pattern)):
            if path.is_file():
                key = path.as_posix()
                if key not in seen:
                    files.append(path)
                    seen.add(key)
    return files


def normalize_source_file(path: Path) -> tuple[pd.DataFrame, list[str]]:
    warnings: list[str] = []
    raw = read_csv_any_encoding(path)
    if raw.empty:
        return pd.DataFrame(), [f"{path.as_posix()}: read failed or empty"]

    columns = list(raw.columns)
    date_col = first_existing(columns, DATE_ALIASES)
    stock_id_col = first_existing(columns, STOCK_ID_ALIASES)
    stock_name_col = first_existing(columns, STOCK_NAME_ALIASES)
    computed_col = first_existing(columns, COMPUTED_VALUE_ALIASES)
    main_col = first_existing(columns, MAIN_FORCE_ALIASES)
    eight_inst_col = first_existing(columns, EIGHT_INSTITUTION_ALIASES)
    eight_bank_col = first_existing(columns, EIGHT_BANK_ALIASES)

    inferred_date = extract_date_from_path(path)
    if not date_col and not inferred_date:
        return pd.DataFrame(), [f"{path.as_posix()}: missing date column and no YYYYMMDD in filename"]
    if not stock_id_col:
        return pd.DataFrame(), [f"{path.as_posix()}: missing stock_id column"]
    if not computed_col and not (main_col and eight_inst_col and eight_bank_col):
        return pd.DataFrame(), [
            f"{path.as_posix()}: missing formula columns; need computed value or main/eight-institution/eight-bank columns"
        ]

    df = pd.DataFrame()
    df["date"] = raw[date_col].map(normalize_date) if date_col else inferred_date
    df["stock_id"] = raw[stock_id_col].map(normalize_stock_id)
    df["stock_name"] = raw[stock_name_col].map(safe_str) if stock_name_col else ""

    if main_col:
        df["main_force_net_buy"] = raw[main_col].map(to_number)
    else:
        df["main_force_net_buy"] = math.nan

    if eight_inst_col:
        df["eight_institution_net_buy"] = raw[eight_inst_col].map(to_number)
    else:
        df["eight_institution_net_buy"] = math.nan

    if eight_bank_col:
        df["eight_bank_net_buy"] = raw[eight_bank_col].map(to_number)
    else:
        df["eight_bank_net_buy"] = math.nan

    if computed_col:
        df["main_force_minus_eight_value"] = raw[computed_col].map(to_number)
    else:
        df["main_force_minus_eight_value"] = (
            df["main_force_net_buy"] - df["eight_institution_net_buy"] - df["eight_bank_net_buy"]
        )

    df["source_file"] = path.as_posix()
    df = df[df["date"].ne("") & df["stock_id"].ne("")]
    df = df.dropna(subset=["main_force_minus_eight_value"])
    return df, warnings


def load_source_data() -> tuple[pd.DataFrame, list[str], list[str]]:
    files = collect_source_files()
    warnings: list[str] = []
    if not files:
        return pd.DataFrame(), [], ["No source files found"]

    frames: list[pd.DataFrame] = []
    for path in files:
        df, file_warnings = normalize_source_file(path)
        warnings.extend(file_warnings)
        if not df.empty:
            frames.append(df)

    if not frames:
        return pd.DataFrame(), [p.as_posix() for p in files], warnings

    data = pd.concat(frames, ignore_index=True)
    data = data.sort_values(["stock_id", "date", "source_file"])
    data = data.drop_duplicates(["stock_id", "date"], keep="last")
    data = data.sort_values(["stock_id", "date"]).reset_index(drop=True)
    return data, [p.as_posix() for p in files], warnings


def round_value(value: Any) -> Any:
    try:
        if pd.isna(value):
            return ""
        return round(float(value), 2)
    except Exception:
        return ""


def build_candidates(data: pd.DataFrame) -> pd.DataFrame:
    if data.empty:
        return pd.DataFrame(columns=OUTPUT_COLUMNS)

    latest_date = str(data["date"].max())
    rows: list[dict[str, Any]] = []

    for stock_id, group in data.groupby("stock_id", sort=True):
        group = group.sort_values("date").reset_index(drop=True)
        latest = group.iloc[-1]
        if str(latest["date"]) != latest_date:
            continue

        streak_rows: list[pd.Series] = []
        for _, row in group.iloc[::-1].iterrows():
            if float(row["main_force_minus_eight_value"]) > 0:
                streak_rows.append(row)
            else:
                break

        if len(streak_rows) < 3:
            continue

        ordered_streak = list(reversed(streak_rows))
        latest_row = ordered_streak[-1]
        previous_1 = ordered_streak[-2] if len(ordered_streak) >= 2 else None
        previous_2 = ordered_streak[-3] if len(ordered_streak) >= 3 else None
        stock_name = safe_str(latest_row.get("stock_name", ""))

        rows.append(
            {
                "date": latest_date,
                "stock_id": stock_id,
                "stock_name": stock_name,
                "positive_streak_days": len(streak_rows),
                "streak_start_date": str(ordered_streak[0]["date"]),
                "streak_end_date": str(latest_row["date"]),
                "latest_value": round_value(latest_row["main_force_minus_eight_value"]),
                "previous_1_value": round_value(previous_1["main_force_minus_eight_value"]) if previous_1 is not None else "",
                "previous_2_value": round_value(previous_2["main_force_minus_eight_value"]) if previous_2 is not None else "",
                "latest_main_force_net_buy": round_value(latest_row["main_force_net_buy"]),
                "latest_eight_institution_net_buy": round_value(latest_row["eight_institution_net_buy"]),
                "latest_eight_bank_net_buy": round_value(latest_row["eight_bank_net_buy"]),
                "rule": RULE_TEXT,
                "source_file": safe_str(latest_row["source_file"]),
            }
        )

    result = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    if result.empty:
        return result
    return result.sort_values(
        ["positive_streak_days", "latest_value", "stock_id"],
        ascending=[False, False, True],
    ).reset_index(drop=True)


def write_outputs(candidates: pd.DataFrame, status: str, source_files: list[str], warnings: list[str], latest_date: str) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    candidates.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    generated_at = now_taipei()
    metadata = {
        "generated_at": generated_at,
        "status": status,
        "rule": RULE_TEXT,
        "latest_source_date": latest_date,
        "candidate_count": int(len(candidates)),
        "source_files": source_files,
        "warnings": warnings,
        "outputs": {
            "csv": OUTPUT_CSV.as_posix(),
            "md": OUTPUT_MD.as_posix(),
            "json": OUTPUT_JSON.as_posix(),
            "pages_csv_url": f"{PAGES_PREFIX}/latest/{OUTPUT_CSV.name}",
            "pages_md_url": f"{PAGES_PREFIX}/latest/{OUTPUT_MD.name}",
            "raw_csv_url": f"{RAW_PREFIX}/{OUTPUT_CSV.as_posix()}",
            "raw_md_url": f"{RAW_PREFIX}/{OUTPUT_MD.as_posix()}",
        },
    }
    OUTPUT_JSON.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 主力扣八大連續為正清單",
        "",
        f"- generated_at: {generated_at}",
        f"- status: {status}",
        f"- latest_source_date: {latest_date or 'N/A'}",
        f"- rule: {RULE_TEXT}",
        f"- candidate_count: {len(candidates)}",
        "",
    ]

    if source_files:
        lines.append("## Source Files")
        lines.extend([f"- `{path}`" for path in source_files])
        lines.append("")
    else:
        lines.extend(
            [
                "## Source Files",
                "- No source files found. Put daily or historical chip-flow CSV files under `data/chip_flow/main_force_daily/`.",
                "",
            ]
        )

    if warnings:
        lines.append("## Warnings")
        lines.extend([f"- {warning}" for warning in warnings])
        lines.append("")

    if candidates.empty:
        if status == "missing_source_data":
            lines.extend(
                [
                    "## Result",
                    "目前沒有可計算的主力 / 八大法人 / 八大行庫原始資料，因此未產生候選清單。",
                    "",
                ]
            )
        else:
            lines.extend(["## Result", "最新資料日沒有符合連續三天以上為正的股票。", ""])
    else:
        display = candidates.copy()
        lines.append("## Candidates")
        lines.append(display.to_markdown(index=False))
        lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")

    shutil.copyfile(OUTPUT_CSV, DOCS_CSV)
    shutil.copyfile(OUTPUT_MD, DOCS_MD)
    shutil.copyfile(OUTPUT_JSON, DOCS_JSON)

    history_date = latest_date or today_yyyymmdd()
    shutil.copyfile(OUTPUT_CSV, HISTORY_DIR / f"{history_date}_main_force_eight_positive.csv")
    shutil.copyfile(OUTPUT_MD, HISTORY_DIR / f"{history_date}_main_force_eight_positive.md")
    shutil.copyfile(OUTPUT_JSON, HISTORY_DIR / f"{history_date}_main_force_eight_positive.json")


def main() -> None:
    data, source_files, warnings = load_source_data()
    if data.empty:
        candidates = pd.DataFrame(columns=OUTPUT_COLUMNS)
        write_outputs(candidates, "missing_source_data", source_files, warnings, "")
        print("Main-force/eight positive candidates: missing source data")
        return

    latest_date = str(data["date"].max())
    candidates = build_candidates(data)
    status = "ok" if not candidates.empty else "no_candidates"
    write_outputs(candidates, status, source_files, warnings, latest_date)
    print(f"Main-force/eight positive candidates: {status}, count={len(candidates)}, latest_date={latest_date}")


if __name__ == "__main__":
    main()
