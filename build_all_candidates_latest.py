from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import math
import re

import pandas as pd

from scripts.tracking_utils import (
    latest_stock_price_history_date,
    main_price_date_from_freshness,
    resolve_candidate_signal_date,
)


LATEST_DIR = Path("output/latest")
DATA_PRICE_DIR = Path("data/daily_price")
DEFAULT_CHART_DAYS = 180

OUTPUT_CSV = LATEST_DIR / "all_candidates_latest.csv"
OUTPUT_XLSX = LATEST_DIR / "all_candidates_latest.xlsx"
OUTPUT_MD = LATEST_DIR / "all_candidates_latest.md"

TDCC_HOLDER_CSV = LATEST_DIR / "tdcc_holder_ratio_latest.csv"
TDCC_TREND_CSV = LATEST_DIR / "tdcc_trend_debug_latest.csv"

SOURCE_FILES = [
    {
        "path": LATEST_DIR / "breakout_latest.csv",
        "default_category": "true_breakout",
        "default_category_cn": "嚴格突破",
    },
    {
        "path": LATEST_DIR / "range_rebound_watch_latest.csv",
        "default_category": "range_rebound",
        "default_category_cn": "區間內轉強 / 挑戰前高觀察",
    },
    {
        "path": LATEST_DIR / "revenue_breakout_low_response_latest.csv",
        "default_category": "revenue_breakout_low_response",
        "default_category_cn": "營收爆發低反應股",
    },
    {
        "path": LATEST_DIR / "revenue_pullback_latest.csv",
        "default_category": "revenue_pullback",
        "default_category_cn": "營收成長股價回檔",
    },
    {
        "path": LATEST_DIR / "pullback_rebound_latest.csv",
        "default_category": "pullback_rebound",
        "default_category_cn": "回檔後短線轉強",
    },
    {
        "path": LATEST_DIR / "daily_pattern_watch_latest.csv",
        "default_category": "pattern",
        "default_category_cn": "型態觀察",
    },
    {
        "path": LATEST_DIR / "pattern_scan_latest.csv",
        "default_category": "pattern",
        "default_category_cn": "型態觀察",
    },
    {
        "path": LATEST_DIR / "w_bottom_attack_latest.csv",
        "default_category": "pattern",
        "default_category_cn": "型態觀察",
    },
]

CATEGORY_CN = {
    "true_breakout": "嚴格突破",
    "breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

CATEGORY_ORDER = {
    "true_breakout": 10,
    "breakout": 10,
    "range_rebound": 20,
    "near_resistance": 21,
    "abnormal_volume_up": 22,
    "revenue_breakout_low_response": 30,
    "revenue_pullback": 40,
    "pullback_rebound": 50,
    "pattern": 60,
}

FINAL_COLUMNS = [
    "date",
    "signal_date",
    "main_price_date",
    "source_date",
    "category",
    "category_cn",
    "breakout_type",
    "stock_id",
    "stock_name",
    "industry",
    "細分族群",
    "theme_group",
    "theme_score",
    "theme_note",
    "revaluation_priority",
    "score",
    "rank",
    "latest_revenue_yoy",
    "cumulative_revenue_yoy",
    "revenue_acceleration_note",
    "revenue_warning",
    "revenue_release_date",
    "return_after_revenue_1d",
    "return_after_revenue_3d",
    "return_5d",
    "return_10d",
    "return_20d",
    "return_60d",
    "return_120d",
    "off_60d_low_pct",
    "off_120d_low_pct",
    "already_priced_in",
    "priced_in_reason",
    "close",
    "volume",
    "volume_lots",
    "volume_ratio",
    "ma20",
    "ma60",
    "ema23",
    "distance_to_ma20_pct",
    "distance_to_ma60_pct",
    "distance_to_ema23_pct",
    "previous_high",
    "previous_40d_high",
    "previous_60d_high",
    "distance_to_previous_high_pct",
    "distance_to_previous_40d_high_pct",
    "distance_to_previous_60d_high_pct",
    "high_20",
    "low_20",
    "high_60",
    "low_60",
    "high_120",
    "low_120",
    "platform_high",
    "platform_low",
    "platform_width_pct",
    "in_platform",
    "w_bottom_flag",
    "w_bottom_right_side_flag",
    "platform_base_flag",
    "platform_right_side_flag",
    "pullback_entry_zone_flag",
    "pullback_right_side_flag",
    "ma20_reclaim_setup_flag",
    "early_attack_volume_flag",
    "early_entry_watch_flag",
    "right_side_follow_through_flag",
    "rebound_from_5d_low_pct",
    "neckline_price",
    "neckline_source",
    "neckline_distance_pct",
    "neckline_challenge_flag",
    "neckline_breakout_flag",
    "platform_breakout_flag",
    "volume_confirmed_breakout",
    "breakout_close_near_high_flag",
    "false_breakout_risk",
    "pattern_stage",
    "short_platform_high",
    "short_platform_low",
    "short_platform_width_pct",
    "higher_lows_flag",
    "ma5_turning_up_flag",
    "ma10_turning_up_flag",
    "near_ma",
    "available_days",
    "price_data_warning",
    "tdcc_date",
    "holder_400_pct",
    "holder_400_change",
    "holder_1000_pct",
    "holder_1000_change",
    "tdcc_judgement",
    "tdcc_weeks_used",
    "tdcc_400_change_sum",
    "tdcc_1000_change_sum",
    "tdcc_400_up_weeks",
    "tdcc_1000_up_weeks",
    "tdcc_accumulation_signal",
    "tdcc_accumulation_note",
    "main_force_net_lots",
    "institutional_net_lots",
    "eight_banks_net_lots",
    "chip_flow_adjusted_net_lots",
    "positive_streak_days",
    "latest_positive",
    "chart_path",
    "chart_url",
    "price_data_path",
    "chart_days",
    "note",
]


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def safe_str(value) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in ["nan", "none", "<na>"]:
        return ""
    return text


def normalize_stock_id(value) -> str:
    text = safe_str(value)
    text = re.sub(r"\.0$", "", text)
    text = re.sub(r"[^0-9A-Za-z]", "", text)
    if text.isdigit():
        return text.zfill(4)
    return text


def normalize_date(value) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return text


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def format_float(value, digits: int = 2) -> str:
    number = safe_float(value)
    if math.isnan(number):
        return ""
    return f"{number:.{digits}f}".rstrip("0").rstrip(".")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()

    for encoding in ["utf-8-sig", "utf-8", "cp950"]:
        try:
            return pd.read_csv(path, dtype=str, encoding=encoding)
        except Exception:
            continue

    print(f"[WARN] failed to read CSV: {path}")
    return pd.DataFrame()


def coalesce_columns(df: pd.DataFrame, target: str, candidates: list[str]) -> pd.DataFrame:
    if target not in df.columns:
        df[target] = ""

    for col in candidates:
        if col in df.columns:
            df[target] = df[target].where(df[target].astype(str).str.strip() != "", df[col])

    return df


def normalize_basic_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    rename_candidates = {
        "stock_id": ["stock_id", "code", "ticker", "證券代號", "股票代號"],
        "stock_name": ["stock_name", "name", "證券名稱", "股票名稱"],
        "industry": ["industry", "產業別", "industry_name"],
        "date": ["date", "資料日期", "price_date", "trade_date"],
        "score": ["score", "總分", "分數"],
        "rank": ["rank", "排名"],
        "close": ["close", "收盤價", "收盤"],
        "volume": ["volume", "成交股數", "成交量"],
        "volume_lots": ["volume_lots", "成交張數"],
        "volume_ratio": ["volume_ratio", "volume_ratio_20", "量比"],
        "breakout_type": ["breakout_type", "signal_type", "pattern_type"],
        "note": ["note", "reason", "理由", "備註"],
    }

    for target, candidates in rename_candidates.items():
        existing = [col for col in candidates if col in df.columns]
        if existing:
            if target not in df.columns:
                df[target] = ""
            for col in existing:
                df[target] = df[target].where(df[target].astype(str).str.strip() != "", df[col])

    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].map(normalize_stock_id)
    else:
        df["stock_id"] = ""

    if "stock_name" not in df.columns:
        df["stock_name"] = ""

    if "date" in df.columns:
        df["date"] = df["date"].map(normalize_date)
    else:
        df["date"] = ""

    if "category" not in df.columns:
        df["category"] = ""

    if "category_cn" not in df.columns:
        df["category_cn"] = ""

    if "breakout_type" not in df.columns:
        df["breakout_type"] = ""

    if "note" not in df.columns:
        df["note"] = ""

    if "細分族群" not in df.columns:
        df["細分族群"] = ""

    return df


def load_source_file(info: dict) -> pd.DataFrame:
    path = info["path"]
    df = read_csv(path)

    if df.empty:
        print(f"[INFO] source missing or empty: {path}")
        return pd.DataFrame()

    df = normalize_basic_columns(df)

    default_category = info["default_category"]
    default_category_cn = info["default_category_cn"]

    df["category"] = df["category"].map(safe_str)
    df.loc[df["category"] == "", "category"] = default_category

    if default_category == "true_breakout":
        df.loc[df["category"].isin(["breakout", "true_breakout", ""]), "category"] = "true_breakout"

    if default_category == "range_rebound":
        df.loc[df["category"].isin(["", "range_rebound_watch"]), "category"] = "range_rebound"

    if default_category == "pattern":
        df.loc[df["category"] == "", "category"] = "pattern"

    df["category_cn"] = df["category_cn"].map(safe_str)
    df.loc[df["category_cn"] == "", "category_cn"] = df["category"].map(
        lambda x: CATEGORY_CN.get(safe_str(x), default_category_cn)
    )

    if "breakout_type" not in df.columns:
        df["breakout_type"] = ""

    if default_category == "true_breakout":
        df.loc[df["breakout_type"].map(safe_str) == "", "breakout_type"] = "true_breakout"

    if default_category == "range_rebound":
        df.loc[df["breakout_type"].map(safe_str) == "", "breakout_type"] = df["category"]

    if default_category == "revenue_breakout_low_response":
        df.loc[df["breakout_type"].map(safe_str) == "", "breakout_type"] = "revenue_breakout_low_response"

    print(f"[INFO] loaded {len(df)} rows from {path}")

    return df


def load_all_sources() -> pd.DataFrame:
    frames = []

    for info in SOURCE_FILES:
        df = load_source_file(info)
        if not df.empty:
            frames.append(df)

    if not frames:
        return pd.DataFrame(columns=FINAL_COLUMNS)

    all_df = pd.concat(frames, ignore_index=True, sort=False)
    all_df = normalize_basic_columns(all_df)

    all_df = all_df[all_df["stock_id"].map(safe_str) != ""].copy()

    return all_df


def canonicalize_candidate_dates(df: pd.DataFrame) -> tuple[pd.DataFrame, str, list[str]]:
    """Normalize daily candidate dates to the accepted market price date.

    Category source files may carry stale scan dates, source event dates, or the
    workflow execution date.  `all_candidates_latest` is the canonical daily
    candidate table, so `date` and `signal_date` must match `main_price_date`.
    The original source date is retained in `source_date` for diagnostics.
    """
    df = df.copy()

    if len(df) == 0:
        preferred_date = main_price_date_from_freshness() or latest_stock_price_history_date()
        return df, preferred_date, ["empty_candidates"]

    original_date = pd.Series([""] * len(df), index=df.index, dtype="object")
    if "date" in df.columns:
        original_date = df["date"].map(normalize_date)

    if "source_date" not in df.columns:
        df["source_date"] = original_date
    else:
        df["source_date"] = df["source_date"].where(
            df["source_date"].astype(str).str.strip() != "",
            original_date,
        )

    # Do not use raw stock_price_history max date directly here.  The raw
    # history can contain a future calendar-date snapshot whose OHLCV copied
    # the prior trading day.  `data_freshness_latest` owns that quality check.
    preferred_date = main_price_date_from_freshness() or latest_stock_price_history_date()
    signal_date, notes = resolve_candidate_signal_date(df, preferred_date)
    if signal_date:
        df["date"] = signal_date
        df["signal_date"] = signal_date
        df["main_price_date"] = signal_date

    return df, signal_date, notes


def normalize_tdcc_holder_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    rename_sets = {
        "stock_id": ["stock_id", "code", "ticker", "證券代號", "股票代號"],
        "stock_name": ["stock_name", "name", "證券名稱", "股票名稱"],
        "tdcc_date": ["tdcc_date", "date", "資料日期", "week_date", "週別"],
        "holder_400_pct": [
            "holder_400_pct",
            "400張以上%",
            "400張以上持股比例",
            "holder_400_ratio",
            "holders_400_pct",
        ],
        "holder_400_change": [
            "holder_400_change",
            "400張變化",
            "400張以上變化",
            "holder_400_change_pct",
            "holders_400_change",
        ],
        "holder_1000_pct": [
            "holder_1000_pct",
            "1000張以上%",
            "1000張以上持股比例",
            "holder_1000_ratio",
            "holders_1000_pct",
        ],
        "holder_1000_change": [
            "holder_1000_change",
            "1000張變化",
            "1000張以上變化",
            "holder_1000_change_pct",
            "holders_1000_change",
        ],
        "tdcc_judgement": [
            "tdcc_judgement",
            "TDCC判斷",
            "tdcc_signal",
            "tdcc_note",
        ],
    }

    for target, candidates in rename_sets.items():
        if target not in df.columns:
            df[target] = ""
        for col in candidates:
            if col in df.columns:
                df[target] = df[target].where(df[target].astype(str).str.strip() != "", df[col])

    df["stock_id"] = df["stock_id"].map(normalize_stock_id)
    df["tdcc_date"] = df["tdcc_date"].map(normalize_date)

    keep_cols = [
        "stock_id",
        "tdcc_date",
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
        "tdcc_judgement",
    ]

    df = df[keep_cols].copy()
    df = df[df["stock_id"] != ""].copy()

    if "tdcc_date" in df.columns:
        df = df.sort_values(["stock_id", "tdcc_date"]).drop_duplicates("stock_id", keep="last")
    else:
        df = df.drop_duplicates("stock_id", keep="last")

    return df


def normalize_tdcc_trend_columns(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    rename_sets = {
        "stock_id": ["stock_id", "code", "ticker", "證券代號", "股票代號"],
        "tdcc_weeks_used": ["tdcc_weeks_used"],
        "tdcc_400_change_sum": ["tdcc_400_change_sum"],
        "tdcc_1000_change_sum": ["tdcc_1000_change_sum"],
        "tdcc_400_up_weeks": ["tdcc_400_up_weeks"],
        "tdcc_1000_up_weeks": ["tdcc_1000_up_weeks"],
        "tdcc_accumulation_signal": ["tdcc_accumulation_signal"],
        "tdcc_accumulation_note": ["tdcc_accumulation_note"],
    }

    for target, candidates in rename_sets.items():
        if target not in df.columns:
            df[target] = ""
        for col in candidates:
            if col in df.columns:
                df[target] = df[target].where(df[target].astype(str).str.strip() != "", df[col])

    df["stock_id"] = df["stock_id"].map(normalize_stock_id)

    keep_cols = [
        "stock_id",
        "tdcc_weeks_used",
        "tdcc_400_change_sum",
        "tdcc_1000_change_sum",
        "tdcc_400_up_weeks",
        "tdcc_1000_up_weeks",
        "tdcc_accumulation_signal",
        "tdcc_accumulation_note",
    ]

    df = df[keep_cols].copy()
    df = df[df["stock_id"] != ""].copy()
    df = df.drop_duplicates("stock_id", keep="last")

    return df


def merge_without_duplicate_columns(
    left: pd.DataFrame,
    right: pd.DataFrame,
    on: str,
    suffix: str,
) -> pd.DataFrame:
    if right.empty:
        return left

    left = left.copy()
    right = right.copy()

    overlap = [col for col in right.columns if col in left.columns and col != on]

    rename_map = {col: f"{col}{suffix}" for col in overlap}
    right = right.rename(columns=rename_map)

    merged = left.merge(right, on=on, how="left")

    for original_col in overlap:
        new_col = f"{original_col}{suffix}"

        if new_col in merged.columns:
            if original_col not in merged.columns:
                merged[original_col] = ""

            merged[original_col] = merged[original_col].where(
                merged[original_col].map(safe_str) != "",
                merged[new_col],
            )
            merged = merged.drop(columns=[new_col])

    return merged


def infer_tdcc_signal_from_numbers(row: pd.Series) -> tuple[str, str]:
    signal = safe_str(row.get("tdcc_accumulation_signal", ""))
    note = safe_str(row.get("tdcc_accumulation_note", ""))

    if signal:
        return signal, note

    change_400 = safe_float(row.get("tdcc_400_change_sum", ""))
    change_1000 = safe_float(row.get("tdcc_1000_change_sum", ""))

    if math.isnan(change_400):
        change_400 = safe_float(row.get("holder_400_change", ""))

    if math.isnan(change_1000):
        change_1000 = safe_float(row.get("holder_1000_change", ""))

    if math.isnan(change_400) and math.isnan(change_1000):
        return "", note

    c400 = 0 if math.isnan(change_400) else change_400
    c1000 = 0 if math.isnan(change_1000) else change_1000

    if c400 > 0 and c1000 > 0:
        return "strong_accumulation", "近幾週400張與1000張同步累積"

    if c400 < 0 and c1000 < 0:
        return "distribution_warning", "近幾週400張與1000張同步減少"

    if c400 + c1000 > 0:
        return "mild_accumulation", "近幾週其中一項大戶級距增加"

    if c400 + c1000 < 0:
        return "distribution_warning", "近幾週其中一項大戶級距減少"

    return "neutral", "近期TDCC無明顯累積"


def merge_tdcc(all_df: pd.DataFrame) -> pd.DataFrame:
    if all_df.empty:
        return all_df

    holder_df = normalize_tdcc_holder_columns(read_csv(TDCC_HOLDER_CSV))
    trend_df = normalize_tdcc_trend_columns(read_csv(TDCC_TREND_CSV))

    if holder_df.empty:
        print("[WARN] TDCC holder file missing or empty")
    else:
        print(f"[INFO] TDCC holder rows: {len(holder_df)}")

    if trend_df.empty:
        print("[WARN] TDCC trend file missing or empty")
    else:
        print(f"[INFO] TDCC trend rows: {len(trend_df)}")

    merged = merge_without_duplicate_columns(all_df, holder_df, on="stock_id", suffix="_tdcc_holder")
    merged = merge_without_duplicate_columns(merged, trend_df, on="stock_id", suffix="_tdcc_trend")

    for col in [
        "tdcc_date",
        "holder_400_pct",
        "holder_400_change",
        "holder_1000_pct",
        "holder_1000_change",
        "tdcc_judgement",
        "tdcc_weeks_used",
        "tdcc_400_change_sum",
        "tdcc_1000_change_sum",
        "tdcc_400_up_weeks",
        "tdcc_1000_up_weeks",
        "tdcc_accumulation_signal",
        "tdcc_accumulation_note",
    ]:
        if col not in merged.columns:
            merged[col] = ""

    inferred = merged.apply(infer_tdcc_signal_from_numbers, axis=1)
    merged["tdcc_accumulation_signal"] = [
        signal if safe_str(row_signal) == "" else row_signal
        for row_signal, (signal, note) in zip(merged["tdcc_accumulation_signal"], inferred)
    ]
    merged["tdcc_accumulation_note"] = [
        note if safe_str(row_note) == "" else row_note
        for row_note, (signal, note) in zip(merged["tdcc_accumulation_note"], inferred)
    ]

    return merged


def improve_notes(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    if "note" not in df.columns:
        df["note"] = ""

    def add_note(row: pd.Series) -> str:
        parts = []
        original_note = safe_str(row.get("note", ""))

        if original_note:
            parts.append(original_note)

        tdcc_signal = safe_str(row.get("tdcc_accumulation_signal", ""))
        tdcc_note = safe_str(row.get("tdcc_accumulation_note", ""))

        if tdcc_signal == "strong_accumulation":
            parts.append("TDCC近幾週400張與1000張同步累積")
        elif tdcc_signal == "mild_accumulation":
            parts.append("TDCC近幾週大戶溫和增加")
        elif tdcc_signal == "distribution_warning":
            parts.append("TDCC近幾週大戶籌碼轉弱")
        elif tdcc_note:
            parts.append(tdcc_note)

        seen = []
        for part in parts:
            part = safe_str(part)
            if part and part not in seen:
                seen.append(part)

        return "；".join(seen)

    df["note"] = df.apply(add_note, axis=1)

    return df


def finalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in FINAL_COLUMNS:
        if col not in df.columns:
            df[col] = ""

    default_price_data_path = DATA_PRICE_DIR.as_posix()

    df["price_data_path"] = df["price_data_path"].map(safe_str)
    df.loc[df["price_data_path"] == "", "price_data_path"] = default_price_data_path

    df["chart_days"] = df["chart_days"].map(safe_str)
    df.loc[df["chart_days"] == "", "chart_days"] = str(DEFAULT_CHART_DAYS)

    extra_cols = [col for col in df.columns if col not in FINAL_COLUMNS]

    df = df[FINAL_COLUMNS + extra_cols].copy()

    return df


def sort_output(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["_category_order"] = df["category"].map(lambda x: CATEGORY_ORDER.get(safe_str(x), 999))
    df["_score_sort"] = pd.to_numeric(df.get("score", ""), errors="coerce").fillna(-999999)
    df["_rank_sort"] = pd.to_numeric(df.get("rank", ""), errors="coerce").fillna(999999)
    df["_stock_sort"] = df["stock_id"].map(safe_str)

    df = df.sort_values(
        ["_category_order", "_score_sort", "_rank_sort", "_stock_sort"],
        ascending=[True, False, True, True],
    )

    df = df.drop(columns=["_category_order", "_score_sort", "_rank_sort", "_stock_sort"], errors="ignore")

    return df


def deduplicate_candidates(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.copy()

    # 同一支股票如果在不同 category 同時出現，保留不同 category。
    # 同 category 重複才去重，保留排序後第一筆。
    df = sort_output(df)
    df = df.drop_duplicates(["date", "category", "stock_id"], keep="first")

    return df


def build_markdown_report(df: pd.DataFrame) -> str:
    lines = []
    lines.append("# 完整候選股清單")
    lines.append("")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 總筆數：`{len(df)}`")
    lines.append("")
    lines.append("說明：本檔案由 `build_all_candidates_latest.py` 產生，負責整合各類候選股，並補上 TDCC 欄位。權證欄位由後續 `merge_warrant_flow_into_candidates.py` 補上。")
    lines.append("")

    if df.empty:
        lines.append("目前沒有候選股資料。")
        return "\n".join(lines)

    for category, part in df.groupby("category", sort=False):
        category_cn = CATEGORY_CN.get(safe_str(category), safe_str(part["category_cn"].iloc[0]))
        lines.append(f"## {category_cn}")
        lines.append("")
        lines.append(f"- 檔數：`{len(part)}`")
        lines.append("")

        display_cols = [
            "date",
            "stock_id",
            "stock_name",
            "industry",
            "細分族群",
            "category_cn",
            "breakout_type",
            "score",
            "rank",
            "revaluation_priority",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "tdcc_accumulation_signal",
            "tdcc_accumulation_note",
            "tdcc_judgement",
            "note",
        ]

        display_cols = [col for col in display_cols if col in part.columns]

        lines.append("| " + " | ".join(display_cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(display_cols)) + " |")

        for _, row in part.iterrows():
            values = []
            for col in display_cols:
                value = safe_str(row.get(col, ""))
                value = value.replace("\n", " ").replace("|", "/")
                if len(value) > 120:
                    value = value[:120] + "..."
                values.append(value)

            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    return "\n".join(lines)


def write_outputs(df: pd.DataFrame) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    try:
        with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all_candidates", index=False)

            summary = (
                df.groupby(["category", "category_cn"], dropna=False)
                .size()
                .reset_index(name="count")
            )
            summary.to_excel(writer, sheet_name="summary", index=False)
    except Exception as exc:
        print(f"[WARN] failed to write xlsx: {exc}")

    OUTPUT_MD.write_text(build_markdown_report(df), encoding="utf-8")


def main() -> int:
    all_df = load_all_sources()

    if all_df.empty:
        print("[WARN] no candidate source rows found")
        all_df = pd.DataFrame(columns=FINAL_COLUMNS)

    all_df, signal_date, date_notes = canonicalize_candidate_dates(all_df)
    if signal_date:
        print(f"[INFO] all_candidates canonical signal_date={signal_date}")
    for note in date_notes:
        print(f"[INFO] date note: {note}")

    all_df = merge_tdcc(all_df)
    all_df = improve_notes(all_df)
    all_df = finalize_columns(all_df)
    all_df = deduplicate_candidates(all_df)
    all_df = sort_output(all_df)

    write_outputs(all_df)

    print(f"[OK] saved {OUTPUT_CSV} rows={len(all_df)}")
    print(f"[OK] saved {OUTPUT_XLSX}")
    print(f"[OK] saved {OUTPUT_MD}")

    if not all_df.empty:
        tdcc_non_empty = (all_df["tdcc_accumulation_signal"].map(safe_str) != "").sum()
        print(f"[INFO] rows with tdcc_accumulation_signal: {tdcc_non_empty}/{len(all_df)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
