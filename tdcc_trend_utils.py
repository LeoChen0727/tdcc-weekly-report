from __future__ import annotations

from pathlib import Path
import re
import pandas as pd


TDCC_HISTORY_DIR = Path("output/history/tdcc")
TDCC_LATEST_PATH = Path("output/latest/tdcc_holder_ratio_latest.csv")
TDCC_DEBUG_OUTPUT = Path("output/latest/tdcc_trend_debug_latest.csv")


def normalize_code(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value).strip()

    if text.endswith(".0"):
        text = text[:-2]

    text = re.sub(r"[^0-9]", "", text)

    return text.zfill(4) if text else ""


def to_number(value):
    if pd.isna(value):
        return pd.NA

    text = str(value).strip()
    text = text.replace(",", "")
    text = text.replace("%", "")
    text = text.replace("+", "")
    text = text.replace("--", "")
    text = text.replace(" ", "")

    if text == "":
        return pd.NA

    return pd.to_numeric(text, errors="coerce")


def pick_column(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col

    return None


def parse_date_from_filename(path: Path) -> str:
    match = re.search(r"(\d{8})", path.name)
    return match.group(1) if match else ""


def standardize_tdcc_df(df: pd.DataFrame, source_date: str = "") -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    code_col = pick_column(
        df,
        [
            "stock_id",
            "ticker",
            "code",
            "股票代號",
            "證券代號",
        ],
    )

    name_col = pick_column(
        df,
        [
            "stock_name",
            "name",
            "股票名稱",
            "證券名稱",
        ],
    )

    holder_400_pct_col = pick_column(
        df,
        [
            "holder_400_pct",
            "tdcc_over_400_pct",
            "over_400_pct",
            "400張以上%",
            "400張以上持股比例",
            "holder_ge_400_pct",
        ],
    )

    holder_1000_pct_col = pick_column(
        df,
        [
            "holder_1000_pct",
            "tdcc_over_1000_pct",
            "over_1000_pct",
            "1000張以上%",
            "1000張以上持股比例",
            "holder_ge_1000_pct",
        ],
    )

    holder_400_change_col = pick_column(
        df,
        [
            "holder_400_change",
            "tdcc_over_400_change",
            "over_400_change",
            "400張變化",
            "400張以上變化",
        ],
    )

    holder_1000_change_col = pick_column(
        df,
        [
            "holder_1000_change",
            "tdcc_over_1000_change",
            "over_1000_change",
            "1000張變化",
            "1000張以上變化",
        ],
    )

    if code_col is None:
        return pd.DataFrame()

    out = pd.DataFrame()
    out["stock_id"] = df[code_col].map(normalize_code)
    out["stock_name"] = df[name_col].astype(str).str.strip() if name_col else ""
    out["tdcc_date"] = source_date

    out["holder_400_pct"] = df[holder_400_pct_col].map(to_number) if holder_400_pct_col else pd.NA
    out["holder_1000_pct"] = df[holder_1000_pct_col].map(to_number) if holder_1000_pct_col else pd.NA

    out["holder_400_change_raw"] = df[holder_400_change_col].map(to_number) if holder_400_change_col else pd.NA
    out["holder_1000_change_raw"] = df[holder_1000_change_col].map(to_number) if holder_1000_change_col else pd.NA

    out = out[out["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

    return out


def load_latest_tdcc() -> pd.DataFrame:
    if not TDCC_LATEST_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(
            TDCC_LATEST_PATH,
            dtype={
                "stock_id": str,
                "ticker": str,
                "code": str,
            },
        )
    except Exception as exc:
        print(f"Read latest TDCC failed: {exc}")
        return pd.DataFrame()

    return standardize_tdcc_df(df, source_date="latest")


def classify_accumulation(
    tdcc_weeks_used: int,
    tdcc_400_change_sum: float,
    tdcc_1000_change_sum: float,
    tdcc_400_up_weeks: int,
    tdcc_1000_up_weeks: int,
) -> tuple[str, str]:
    if tdcc_weeks_used <= 1:
        return "single_week_only", "TDCC歷史週數不足，僅能參考單週"

    if (
        tdcc_400_change_sum > 0
        and tdcc_1000_change_sum > 0
        and tdcc_400_up_weeks >= 2
        and tdcc_1000_up_weeks >= 2
    ):
        return "strong_accumulation", "近幾週400張與1000張同步累積"

    if (
        tdcc_400_change_sum > 0
        and tdcc_1000_change_sum > 0
    ):
        return "mild_accumulation", "近幾週400張與1000張合計增加"

    if (
        tdcc_400_change_sum > 0
        or tdcc_1000_change_sum > 0
    ):
        return "mild_accumulation", "近幾週其中一項大戶級距增加"

    if (
        tdcc_400_change_sum < 0
        and tdcc_1000_change_sum < 0
    ):
        return "distribution_warning", "近幾週400張與1000張同步減少"

    if (
        tdcc_400_change_sum < 0
        or tdcc_1000_change_sum < 0
    ):
        return "distribution_warning", "近幾週其中一項大戶級距減少"

    return "neutral", "近幾週TDCC無明顯累積"


def load_tdcc_history_trend(max_weeks: int = 4) -> pd.DataFrame:
    if not TDCC_HISTORY_DIR.exists():
        return pd.DataFrame()

    paths = sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv"))

    if not paths:
        return pd.DataFrame()

    selected_paths = paths[-max_weeks:]
    frames = []

    for path in selected_paths:
        source_date = parse_date_from_filename(path)

        try:
            df = pd.read_csv(
                path,
                dtype={
                    "stock_id": str,
                    "ticker": str,
                    "code": str,
                },
            )
        except Exception as exc:
            print(f"Read TDCC history failed: {path}: {exc}")
            continue

        standardized = standardize_tdcc_df(df, source_date=source_date)

        if standardized.empty:
            continue

        frames.append(standardized)

    if not frames:
        return pd.DataFrame()

    history = pd.concat(frames, ignore_index=True)
    history = history.drop_duplicates(subset=["tdcc_date", "stock_id"], keep="last")
    history = history.sort_values(["stock_id", "tdcc_date"]).reset_index(drop=True)

    grouped_rows = []

    for stock_id, part in history.groupby("stock_id"):
        part = part.sort_values("tdcc_date").copy()

        stock_name = ""
        if "stock_name" in part.columns and not part["stock_name"].dropna().empty:
            stock_name = str(part["stock_name"].dropna().iloc[-1])

        tdcc_weeks_used = int(part["tdcc_date"].nunique())
        tdcc_history_dates = ",".join(part["tdcc_date"].astype(str).dropna().unique())

        holder_400_pct = pd.to_numeric(part["holder_400_pct"], errors="coerce")
        holder_1000_pct = pd.to_numeric(part["holder_1000_pct"], errors="coerce")

        holder_400_change_raw = pd.to_numeric(part["holder_400_change_raw"], errors="coerce")
        holder_1000_change_raw = pd.to_numeric(part["holder_1000_change_raw"], errors="coerce")

        # 優先用每週持股比例自行計算週變化。
        # 這比直接讀 change 欄位可靠，因為歷史檔可能沒有 change 欄位，或 change 欄位不是週對週。
        if holder_400_pct.notna().sum() >= 2:
            holder_400_change_series = holder_400_pct.diff()
            tdcc_400_change_sum = holder_400_pct.iloc[-1] - holder_400_pct.iloc[0]
            tdcc_400_up_weeks = int((holder_400_change_series > 0).sum())
            holder_400_calc_method = "pct_diff"
        else:
            holder_400_change_series = holder_400_change_raw
            tdcc_400_change_sum = holder_400_change_raw.sum(skipna=True)
            tdcc_400_up_weeks = int((holder_400_change_raw > 0).sum())
            holder_400_calc_method = "raw_change"

        if holder_1000_pct.notna().sum() >= 2:
            holder_1000_change_series = holder_1000_pct.diff()
            tdcc_1000_change_sum = holder_1000_pct.iloc[-1] - holder_1000_pct.iloc[0]
            tdcc_1000_up_weeks = int((holder_1000_change_series > 0).sum())
            holder_1000_calc_method = "pct_diff"
        else:
            holder_1000_change_series = holder_1000_change_raw
            tdcc_1000_change_sum = holder_1000_change_raw.sum(skipna=True)
            tdcc_1000_up_weeks = int((holder_1000_change_raw > 0).sum())
            holder_1000_calc_method = "raw_change"

        tdcc_400_change_sum = 0 if pd.isna(tdcc_400_change_sum) else float(tdcc_400_change_sum)
        tdcc_1000_change_sum = 0 if pd.isna(tdcc_1000_change_sum) else float(tdcc_1000_change_sum)

        signal, note = classify_accumulation(
            tdcc_weeks_used=tdcc_weeks_used,
            tdcc_400_change_sum=tdcc_400_change_sum,
            tdcc_1000_change_sum=tdcc_1000_change_sum,
            tdcc_400_up_weeks=tdcc_400_up_weeks,
            tdcc_1000_up_weeks=tdcc_1000_up_weeks,
        )

        grouped_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": stock_name,
                "tdcc_weeks_used": tdcc_weeks_used,
                "tdcc_history_dates": tdcc_history_dates,
                "tdcc_400_change_sum": round(tdcc_400_change_sum, 4),
                "tdcc_1000_change_sum": round(tdcc_1000_change_sum, 4),
                "tdcc_400_up_weeks": tdcc_400_up_weeks,
                "tdcc_1000_up_weeks": tdcc_1000_up_weeks,
                "tdcc_accumulation_signal": signal,
                "tdcc_accumulation_note": note,
                "holder_400_calc_method": holder_400_calc_method,
                "holder_1000_calc_method": holder_1000_calc_method,
            }
        )

    result = pd.DataFrame(grouped_rows)

    return result


def tdcc_trend_to_map(tdcc_trend_df: pd.DataFrame) -> dict:
    if tdcc_trend_df.empty:
        return {}

    return {
        normalize_code(row["stock_id"]): row
        for _, row in tdcc_trend_df.iterrows()
        if normalize_code(row.get("stock_id", ""))
    }


def main() -> int:
    TDCC_DEBUG_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    latest_df = load_latest_tdcc()
    trend_df = load_tdcc_history_trend(max_weeks=4)

    print("Latest TDCC rows:", len(latest_df))
    print("TDCC trend rows:", len(trend_df))

    if not trend_df.empty:
        print(trend_df["tdcc_accumulation_signal"].value_counts(dropna=False))
        trend_df.to_csv(TDCC_DEBUG_OUTPUT, index=False, encoding="utf-8-sig")
        print(f"Saved: {TDCC_DEBUG_OUTPUT}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
