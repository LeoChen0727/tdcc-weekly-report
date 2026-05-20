from __future__ import annotations

from pathlib import Path
import re
import pandas as pd


TDCC_HISTORY_DIR = Path("output/history/tdcc")
TDCC_LATEST_PATH = Path("output/latest/tdcc_holder_ratio_latest.csv")


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

    code_col = pick_column(df, ["stock_id", "ticker", "code", "股票代號", "證券代號"])
    name_col = pick_column(df, ["stock_name", "name", "股票名稱", "證券名稱"])

    holder_400_pct_col = pick_column(
        df,
        [
            "holder_400_pct",
            "tdcc_over_400_pct",
            "over_400_pct",
            "400張以上%",
            "400張以上持股比例",
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

    holder_1000_pct_col = pick_column(
        df,
        [
            "holder_1000_pct",
            "tdcc_over_1000_pct",
            "over_1000_pct",
            "1000張以上%",
            "1000張以上持股比例",
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
    out["holder_400_change"] = df[holder_400_change_col].map(to_number) if holder_400_change_col else pd.NA
    out["holder_1000_pct"] = df[holder_1000_pct_col].map(to_number) if holder_1000_pct_col else pd.NA
    out["holder_1000_change"] = df[holder_1000_change_col].map(to_number) if holder_1000_change_col else pd.NA

    out = out[out["stock_id"].str.match(r"^[0-9]{4}$", na=False)].copy()

    return out


def load_latest_tdcc() -> pd.DataFrame:
    if not TDCC_LATEST_PATH.exists():
        return pd.DataFrame()

    try:
        df = pd.read_csv(TDCC_LATEST_PATH, dtype={"stock_id": str, "ticker": str, "code": str})
    except Exception as exc:
        print(f"Read latest TDCC failed: {exc}")
        return pd.DataFrame()

    return standardize_tdcc_df(df, source_date="latest")


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
            df = pd.read_csv(path, dtype={"stock_id": str, "ticker": str, "code": str})
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

    grouped_rows = []

    for stock_id, part in history.groupby("stock_id"):
        part = part.sort_values("tdcc_date").copy()

        holder_400_change = pd.to_numeric(part["holder_400_change"], errors="coerce")
        holder_1000_change = pd.to_numeric(part["holder_1000_change"], errors="coerce")

        tdcc_400_change_sum = holder_400_change.sum(skipna=True)
        tdcc_1000_change_sum = holder_1000_change.sum(skipna=True)

        tdcc_400_up_weeks = int((holder_400_change > 0).sum())
        tdcc_1000_up_weeks = int((holder_1000_change > 0).sum())

        tdcc_weeks_used = int(part["tdcc_date"].nunique())

        signal = "neutral"
        note_parts = []

        if tdcc_weeks_used <= 1:
            signal = "single_week_only"
            note_parts.append("TDCC歷史週數不足，僅能參考單週")
        else:
            if (
                tdcc_400_change_sum > 0
                and tdcc_1000_change_sum > 0
                and tdcc_400_up_weeks >= 2
                and tdcc_1000_up_weeks >= 2
            ):
                signal = "strong_accumulation"
                note_parts.append("近幾週400張與1000張同步累積")
            elif tdcc_400_change_sum > 0 or tdcc_1000_change_sum > 0:
                signal = "mild_accumulation"
                note_parts.append("近幾週大戶級距溫和增加")
            elif tdcc_400_change_sum < 0 and tdcc_1000_change_sum < 0:
                signal = "distribution_warning"
                note_parts.append("近幾週400張與1000張同步減少")
            elif tdcc_400_change_sum < 0 or tdcc_1000_change_sum < 0:
                signal = "distribution_warning"
                note_parts.append("近幾週其中一項大戶級距減少")
            else:
                signal = "neutral"
                note_parts.append("近幾週TDCC無明顯累積")

        grouped_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": part["stock_name"].dropna().iloc[-1] if not part["stock_name"].dropna().empty else "",
                "tdcc_weeks_used": tdcc_weeks_used,
                "tdcc_history_dates": ",".join(part["tdcc_date"].astype(str).dropna().unique()),
                "tdcc_400_change_sum": round(float(tdcc_400_change_sum), 4),
                "tdcc_1000_change_sum": round(float(tdcc_1000_change_sum), 4),
                "tdcc_400_up_weeks": tdcc_400_up_weeks,
                "tdcc_1000_up_weeks": tdcc_1000_up_weeks,
                "tdcc_accumulation_signal": signal,
                "tdcc_accumulation_note": "；".join(note_parts),
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


def latest_tdcc_to_map(latest_tdcc_df: pd.DataFrame) -> dict:
    if latest_tdcc_df.empty:
        return {}

    return {
        normalize_code(row["stock_id"]): row
        for _, row in latest_tdcc_df.iterrows()
        if normalize_code(row.get("stock_id", ""))
    }


def main() -> int:
    latest_df = load_latest_tdcc()
    trend_df = load_tdcc_history_trend(max_weeks=4)

    print("Latest TDCC rows:", len(latest_df))
    print("TDCC trend rows:", len(trend_df))

    if not trend_df.empty:
        print(trend_df["tdcc_accumulation_signal"].value_counts(dropna=False))
        trend_df.to_csv("output/latest/tdcc_trend_debug_latest.csv", index=False, encoding="utf-8-sig")
        print("Saved: output/latest/tdcc_trend_debug_latest.csv")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
